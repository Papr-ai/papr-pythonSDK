#!/usr/bin/env python3
"""
Upload CoreML models to Hugging Face Hub for easy distribution.

Usage:
  # Install huggingface_hub
  pip install huggingface_hub
  
  # Login (one-time)
  huggingface-cli login
  
  # Upload model
  python scripts/coreml_models/upload_to_hf.py \
    --model ./coreml/Qwen3-Embedding-4B-FP16.mlpackage \
    --repo papr-ai/Qwen3-Embedding-4B-CoreML
"""
import argparse
import os
from pathlib import Path


def upload_to_huggingface(model_path: str, repo_id: str, variant: str = "fp16") -> None:
    """Upload CoreML model to Hugging Face Hub."""
    try:
        from huggingface_hub import HfApi, create_repo
    except ImportError:
        print("❌ huggingface_hub not installed. Run: pip install huggingface_hub")
        return

    api = HfApi()
    
    # Create repo if it doesn't exist
    try:
        create_repo(repo_id=repo_id, repo_type="model", exist_ok=True)
        print(f"✅ Repository created/verified: {repo_id}")
    except Exception as e:
        print(f"⚠️  Repository creation: {e}")
    
    # Upload the model
    print(f"📤 Uploading {model_path} to {repo_id}/{variant}/...")
    api.upload_folder(
        folder_path=model_path,
        repo_id=repo_id,
        path_in_repo=f"{variant}",
        repo_type="model",
    )
    
    # Create README
    readme_content = f"""---
tags:
- coreml
- embeddings
- papr-memory
- qwen3
library_name: coremltools
---

# Qwen3-Embedding-4B CoreML Models

Pre-converted CoreML models for Apple Silicon (M1/M2/M3) optimized for the [Papr Memory Python SDK](https://github.com/Papr-ai/papr-pythonSDK).

## Available Variants

- **FP16** (Recommended): 7.5GB, ~70ms inference, <0.1% accuracy loss
- **INT8**: 4GB, ~100-150ms inference, ~1-2% accuracy loss

## Performance

| Variant | Size | Latency | Accuracy | Hardware |
|---------|------|---------|----------|----------|
| FP16 | 7.5GB | 70ms | 99.99% | ANE + GPU |
| INT8 | 4GB | 100-150ms | 98-99% | GPU |

## Usage

```python
from papr_memory import Papr
import os

# Download model (one-time)
from huggingface_hub import snapshot_download
model_path = snapshot_download(
    repo_id="{repo_id}",
    allow_patterns=["fp16/*"],
    local_dir="./coreml"
)

# Configure environment
os.environ["PAPR_ENABLE_COREML"] = "true"
os.environ["PAPR_COREML_MODEL"] = "./coreml/fp16"

# Use in SDK
client = Papr(x_api_key="your_key")
results = client.memory.search(query="test", max_memories=10)
```

## Manual Download

```bash
# FP16 (recommended)
huggingface-cli download {repo_id} --local-dir ./coreml fp16/

# INT8 (smaller, slightly slower)
huggingface-cli download {repo_id} --local-dir ./coreml int8/
```

## Build Yourself

Alternatively, build from source:

```bash
pip install coremltools transformers torch
python scripts/coreml_models/convert_qwen_coreml.py \\
  --hf Qwen/Qwen3-Embedding-4B \\
  --out ./coreml/model.mlpackage \\
  --fp16
```

## Citation

```bibtex
@software{{qwen3_coreml,
  title = {{Qwen3-Embedding-4B CoreML}},
  author = {{Papr AI}},
  year = {{2025}},
  url = {{https://huggingface.co/{repo_id}}}
}}
```

## License

Apache 2.0 (same as base Qwen3 model)
"""
    
    readme_path = Path("README_HF.md")
    readme_path.write_text(readme_content)
    
    api.upload_file(
        path_or_fileobj=str(readme_path),
        path_in_repo="README.md",
        repo_id=repo_id,
        repo_type="model",
    )
    readme_path.unlink()  # Clean up temp file
    
    print(f"✅ Upload complete!")
    print(f"🔗 View at: https://huggingface.co/{repo_id}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Upload CoreML models to Hugging Face")
    parser.add_argument("--model", required=True, help="Path to .mlpackage directory")
    parser.add_argument("--repo", required=True, help="HuggingFace repo ID (org/repo-name)")
    parser.add_argument("--variant", default="fp16", help="Model variant (fp16, int8, etc)")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.model):
        print(f"❌ Model not found: {args.model}")
        return
    
    upload_to_huggingface(args.model, args.repo, args.variant)


if __name__ == "__main__":
    main()

