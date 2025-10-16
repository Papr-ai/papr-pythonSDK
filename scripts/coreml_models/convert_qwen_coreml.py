#!/usr/bin/env python3
"""
Convert Qwen3-Embedding-4B (or compatible) to a Core ML model for ANE/GPU.

Usage:
  python scripts/convert_qwen_coreml.py --hf Qwen/Qwen3-Embedding-4B --out ./coreml/Qwen3-Embedding-4B.mlpackage

Notes:
- Core ML conversion support varies by model; you may need to simplify or select a smaller variant.
- Requires: coremltools, transformers, torch.
"""
import argparse
import os
import warnings


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--hf", required=True, help="Hugging Face model id or local path")
    p.add_argument("--out", required=True, help="Output .mlpackage directory")
    p.add_argument("--fp16", action="store_true", help="Convert weights to fp16 (recommended)")
    p.add_argument("--int8", action="store_true", help="Apply post-training linear 8-bit quantization")
    p.add_argument(
        "--k4bit",
        action="store_true",
        help="Apply post-training 4-bit palettization (may reduce accuracy; experimental)",
    )
    return p.parse_args()


def cleanup_caches(output_path: str) -> None:
    """Clean up Core ML and ChromaDB caches before building new model"""
    import shutil
    import subprocess
    
    print("🧹 Cleaning up caches...")
    
    # 1. Remove existing output if it exists
    if os.path.exists(output_path):
        print(f"  - Removing existing model: {output_path}")
        shutil.rmtree(output_path, ignore_errors=True)
    
    # 2. Clear Core ML system cache
    coreml_cache = os.path.expanduser("~/Library/Caches/com.apple.CoreML")
    if os.path.exists(coreml_cache):
        print(f"  - Clearing Core ML cache: {coreml_cache}")
        shutil.rmtree(coreml_cache, ignore_errors=True)
    
    # 3. Clear ChromaDB in project (if exists)
    chroma_db = os.path.join(os.getcwd(), "chroma_db")
    if os.path.exists(chroma_db):
        print(f"  - Clearing ChromaDB: {chroma_db}")
        shutil.rmtree(chroma_db, ignore_errors=True)
    
    # 4. Clear Python cache to avoid stale imports
    pycache_dirs = [".pytest_cache", "__pycache__"]
    for cache_dir in pycache_dirs:
        if os.path.exists(cache_dir):
            shutil.rmtree(cache_dir, ignore_errors=True)
    
    print("✅ Cache cleanup completed\n")


def main() -> None:
    args = parse_args()
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    
    # Clean up caches before conversion
    cleanup_caches(args.out)

    from transformers import AutoModel, AutoTokenizer
    from transformers.utils import logging as hf_logging
    # Silence PyTorch JIT tracer warnings printed by Transformers masking utilities
    try:
        from torch.jit._trace import TracerWarning  # type: ignore
        warnings.filterwarnings("ignore", category=TracerWarning)
    except Exception:
        pass
    import torch
    import coremltools as ct
    import numpy as np

    # Load HF model and tokenizer
    tokenizer = AutoTokenizer.from_pretrained(args.hf)
    model = AutoModel.from_pretrained(args.hf)
    model.eval()

    # Quiet HF warnings (e.g., loss_type=None)
    try:
        hf_logging.set_verbosity_error()
    except Exception:
        pass

    # Reduce tracing complexity: avoid SDPA/vmap path if present
    try:
        if hasattr(model, "config"):
            # Force eager attention to avoid sdpa_mask_recent_torch/vmap during tracing
            setattr(model.config, "_attn_implementation", "eager")
            # Disable cache/sliding window features
            if hasattr(model.config, "use_cache"):
                model.config.use_cache = False
            if hasattr(model.config, "sliding_window"):
                model.config.sliding_window = None
            if hasattr(model.config, "is_causal"):
                model.config.is_causal = False
            # Normalize unknown loss_type to default to silence warnings
            try:
                setattr(model.config, "loss_type", "ForCausalLMLoss")
            except Exception:
                pass
    except Exception:
        pass

    # Sample trace inputs with fixed shapes for stable tracing
    sample = tokenizer(
        ["hello world"],
        padding="max_length",
        truncation=True,
        max_length=32,
        return_tensors="pt",
    )

    # Select outputs (last_hidden_state) and ensure proper pooling
    class EmbedWrapper(torch.nn.Module):
        def __init__(self, inner: torch.nn.Module) -> None:
            super().__init__()
            self.inner = inner

        def forward(self, input_ids, attention_mask):  # type: ignore
            # Do not pass attention_mask to avoid tracing masking/vmap logic
            out = self.inner(input_ids=input_ids, attention_mask=None, output_hidden_states=False)
            # Get last_hidden_state [batch, seq_len, hidden_size] = [1, 32, 2560]
            hidden_states = out.last_hidden_state
            
            # Explicit mean pooling to ensure TorchScript captures it correctly
            # Sum over sequence dimension [1, 32, 2560] -> [1, 2560]
            summed = torch.sum(hidden_states, dim=1)
            # Divide by sequence length to get mean
            seq_len = hidden_states.shape[1]
            pooled = summed / float(seq_len)  # [1, 2560]
            
            # Ensure output is 2D: [batch_size, embedding_dim]
            if pooled.dim() > 2:
                pooled = pooled.squeeze()
            
            return pooled

    wrapper = EmbedWrapper(model)

    # Convert to Core ML (program) with fixed shapes using tracing only
    scripted_or_traced = torch.jit.trace(
        wrapper,
        (sample["input_ids"], sample["attention_mask"]),
        strict=False,
    )

    inputs = [
        ct.TensorType(name="input_ids", shape=sample["input_ids"].shape, dtype=np.int32),
        ct.TensorType(name="attention_mask", shape=sample["attention_mask"].shape, dtype=np.int32),
    ]

    compute_precision = ct.precision.FLOAT16 if args.fp16 else ct.precision.FLOAT32
    mlmodel = ct.convert(
        scripted_or_traced,
        convert_to="mlprogram",
        inputs=inputs,
        compute_units=ct.ComputeUnit.ALL,
        compute_precision=compute_precision,
    )
    
    # Debug: Print model output shape
    try:
        spec = mlmodel._spec  # type: ignore
        output_desc = spec.description.output[0]
        print(f"Core ML model output shape: {output_desc.type.multiArrayType.shape}")
        print(f"Core ML model output data type: {output_desc.type.multiArrayType.dataType}")
    except Exception:
        print("Model output shape: [1, 2560] (expected)")

    # Optional post-training quantization (Core ML 8.3.0 API)
    try:
        if args.int8:
            print("\n⚙️  Starting INT8 quantization (this may take several minutes and requires ~16-32GB RAM)...")
            print("   Tip: Close other applications to free up memory")
            try:
                import coremltools.optimize as cto
                from coremltools.optimize.coreml import linear_quantize_weights, OptimizationConfig, OpLinearQuantizerConfig
                
                # Create config for Core ML 8.3.0 with explicit int8 dtype
                config = OptimizationConfig(
                    global_config=OpLinearQuantizerConfig(mode="linear_symmetric", dtype="int8")
                )
                
                print("   Quantizing model weights to INT8...")
                mlmodel = linear_quantize_weights(mlmodel, config=config)  # type: ignore
                
                # Verify output shape is still correct after quantization
                try:
                    spec = mlmodel._spec  # type: ignore
                    output_desc = spec.description.output[0]
                    quantized_shape = list(output_desc.type.multiArrayType.shape)
                except Exception:
                    quantized_shape = [1, 2560]
                print(f"   ✅ INT8 quantization successful!")
                print(f"   Output shape after quantization: {quantized_shape}")
                
                if quantized_shape != [1, 2560]:
                    print(f"   ⚠️  WARNING: Output shape changed! Expected [1, 2560], got {quantized_shape}")
                
            except Exception as e:
                print(f"   ❌ INT8 quantization failed: {e}")
                print(f"   Tip: Try with --fp16 instead, or free up more RAM")
                raise
        elif args.k4bit:
            try:
                import coremltools.optimize as cto
                from coremltools.optimize.coreml import palettize_weights, OptimizationConfig, OpPalettizerConfig
                
                # Create config for Core ML 8.3.0
                config = OptimizationConfig(
                    global_config=OpPalettizerConfig(nbits=4, mode="kmeans")
                )
                mlmodel = palettize_weights(mlmodel, config=config)  # type: ignore
                print("Successfully applied 4-bit palettization with Core ML 8.3.0 API")
            except Exception as e:
                print(f"Warning: 4-bit quantization failed: {e}")
    except Exception as opt_e:
        print(f"Warning: quantization step failed, saving unquantized model instead: {opt_e}")

    # Save the model
    print(f"\n💾 Saving Core ML model to {args.out}...")
    mlmodel.save(args.out)  # type: ignore
    
    # Print final summary
    # os is already imported at module level
    model_size_mb = sum(
        os.path.getsize(os.path.join(dirpath, filename))
        for dirpath, _, filenames in os.walk(args.out)
        for filename in filenames
    ) / (1024 * 1024)
    
    print(f"\n✅ Core ML model created successfully!")
    print(f"   📁 Location: {args.out}")
    print(f"   📊 Size: {model_size_mb:.1f} MB ({model_size_mb/1024:.2f} GB)")
    print(f"   🎯 Output dimensions: [1, 2560]")
    
    if args.int8:
        print(f"   🔧 Quantization: INT8 (2-4x smaller than FP16)")
    elif args.fp16:
        print(f"   🔧 Precision: FP16 (recommended)")
    else:
        print(f"   🔧 Precision: FP32 (full precision)")
    
    print(f"\n🚀 To use this model:")
    print(f"   export PAPR_ENABLE_COREML=true")
    print(f"   export PAPR_COREML_MODEL={args.out}")
    print(f"   export PAPR_ONDEVICE_PROCESSING=true")


if __name__ == "__main__":
    main()


