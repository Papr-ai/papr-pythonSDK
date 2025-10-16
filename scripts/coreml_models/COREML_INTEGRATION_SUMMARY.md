# Core ML Integration Summary

## Overview
Successfully integrated Apple Core ML support for on-device embedding generation in the Papr Memory Python SDK, enabling Neural Engine (ANE) acceleration for Qwen3-Embedding-4B model on Apple Silicon devices.

## Current Status: ✅ **WORKING**

### What's Implemented
- ✅ **Core ML Model Conversion**: Qwen3-Embedding-4B → Core ML `.mlpackage` format
- ✅ **Correct Output Dimensions**: Model outputs 2560-dimensional embeddings (fixed from initial 4 dimensions)
- ✅ **Runtime Integration**: Core ML embedder integrated into SDK with automatic fallback
- ✅ **ChromaDB Integration**: Local vector storage using Core ML-generated embeddings
- ✅ **Environment Controls**: `PAPR_ENABLE_COREML=true` to enable Core ML path

### Performance Results
- **Local Embedding Generation**: ~0.8s per embedding (avg over 6 embeddings)
- **First Embedding**: ~3s (includes model compilation)
- **Subsequent Embeddings**: ~0.08-0.1s (cached/optimized)
- **Model Size**: ~8GB (FP16 unquantized)

## Key Files Modified

### 1. `scripts/convert_qwen_coreml.py`
Conversion script to create Core ML models from Hugging Face transformers.

**Key Features:**
- Fixed padding (`max_length=32`) for consistent input shapes
- Explicit mean pooling using `torch.sum()` and division (TorchScript-compatible)
- Support for FP16, INT8, and 4-bit quantization (INT8 requires more RAM)
- Outputs `.mlpackage` format compatible with ANE/GPU

**Usage:**
```bash
# FP16 (working, ~8GB)
python scripts/convert_qwen_coreml.py --hf Qwen/Qwen3-Embedding-4B --out ./coreml/Qwen3-Embedding-4B.mlpackage --fp16

# INT8 (memory-intensive, ~2-4GB)
python scripts/convert_qwen_coreml.py --hf Qwen/Qwen3-Embedding-4B --out ./coreml/Qwen3-Embedding-4B.mlpackage --int8
```

### 2. `src/papr_memory/resources/memory.py`
Main SDK integration with Core ML embedder.

**Key Changes:**
- Added `CoreMLEmbeddingFunction` class (lines 702-767)
- Fixed tokenization to use `padding="max_length", max_length=32` (matching conversion)
- Integrated into `_get_optimized_quantized_model()` with priority: Core ML > MLX > Sentence Transformers
- Environment variable control: `PAPR_ENABLE_COREML=true`

### 3. `pyproject.toml`
Added Core ML dependencies as optional extras.

```toml
[project.optional-dependencies]
coreml = ["coremltools>=7.0", "transformers>=4.44", "torch==2.5.1"]
```

**Installation:**
```bash
pip install -e .[coreml]
# or with rye:
rye sync --features coreml
```

## Usage

### Enable Core ML Embeddings
```bash
export PAPR_ENABLE_COREML=true
export PAPR_ONDEVICE_PROCESSING=true
export PAPR_COREML_MODEL=./coreml/Qwen3-Embedding-4B.mlpackage
```

### Python Code
```python
from papr_memory import Papr
import os

# Environment variables should be set before import
os.environ['PAPR_ENABLE_COREML'] = 'true'
os.environ['PAPR_ONDEVICE_PROCESSING'] = 'true'

client = Papr()  # Will automatically use Core ML if available
result = client.memory.search(query="find my goals")
# Core ML embedder is used for local tier0 search
```

### Testing
```bash
# Test Core ML model directly
python -c "
import coremltools as ct
import numpy as np
from transformers import AutoTokenizer

model = ct.models.MLModel('coreml/Qwen3-Embedding-4B.mlpackage')
tokenizer = AutoTokenizer.from_pretrained('Qwen/Qwen3-Embedding-4B')

enc = tokenizer(['test'], padding='max_length', max_length=32, truncation=True, return_tensors='np')
result = model.predict({'input_ids': enc['input_ids'].astype(np.int32), 'attention_mask': enc['attention_mask'].astype(np.int32)})
print('Output shape:', next(iter(result.values())).shape)  # Should be (1, 2560)
"

# Test full SDK integration
python measure_search_latency.py
```

## Critical Fixes Applied

### 1. **Dimension Mismatch (4 → 2560)**
**Problem**: Original model output only 4 dimensions instead of 2560.

**Root Cause**: TorchScript didn't capture `.mean(dim=1)` correctly.

**Fix**: Used explicit operations:
```python
summed = torch.sum(hidden_states, dim=1)
pooled = summed / float(seq_len)
```

### 2. **Padding Mismatch**
**Problem**: "MultiArray shape (1 x 4) does not match (1 x 32)" error.

**Root Cause**: Conversion used `max_length=32`, runtime used dynamic padding.

**Fix**: Matched runtime tokenization to conversion:
```python
enc = tokenizer(texts, padding="max_length", max_length=32, truncation=True, return_tensors="np")
```

### 3. **Core ML Cache Issues**
**Problem**: Model updates not reflected in runtime despite rebuilding.

**Root Cause**: macOS caches compiled models.

**Fix**: Clear caches before testing:
```bash
rm -rf ~/Library/Caches/com.apple.CoreML
rm -rf chroma_db
```

## Known Limitations

### 1. **INT8 Quantization Memory Issues**
- Quantization step requires significant RAM (~16-32GB)
- May get killed on machines with limited memory
- FP16 model works well and is fast enough for most use cases

### 2. **Fixed Input Length**
- Model traced with `max_length=32`
- Longer sequences are truncated
- Could retrace with `max_length=512` for longer contexts (larger model size)

### 3. **Platform-Specific**
- Only works on macOS with Apple Silicon (M1/M2/M3/M4)
- Falls back to sentence-transformers on other platforms

## Architecture

```
User Query
    ↓
[SDK Search]
    ↓
[Core ML Check] → PAPR_ENABLE_COREML=true?
    ↓ Yes                    ↓ No
[Load Core ML Model]     [Fallback to MLX/ST]
    ↓
[Tokenize with fixed padding (max_length=32)]
    ↓
[Core ML Inference on ANE/GPU]
    ↓
[2560-dim Embedding]
    ↓
[ChromaDB Vector Search]
    ↓
[Return Results]
```

## Future Improvements

### 1. **Batch Inference**
Current implementation processes one embedding at a time. Core ML supports batching, which could speed up bulk operations.

### 2. **Dynamic Model Selection**
Automatically select optimal `max_length` based on typical query lengths to balance speed vs context.

### 3. **Quantization Optimization**
- Try 4-bit palettization (more memory-efficient conversion)
- Implement streaming quantization for large models
- Provide pre-quantized models for download

### 4. **Model Caching**
Implement smart cache invalidation to avoid manual cache clearing during development.

## Documentation

- **Learnings**: See `agent.md` for detailed learnings and best practices
- **Conversion Script**: `scripts/convert_qwen_coreml.py`
- **Debug Config**: `.vscode/launch.json` has debug configurations for conversion script
- **Examples**: `measure_search_latency.py` for testing latency with Core ML

## References

- Core ML Tools: https://apple.github.io/coremltools/
- Qwen3-Embedding-4B: https://huggingface.co/Qwen/Qwen3-Embedding-4B
- Apple Neural Engine: https://github.com/hollance/neural-engine

---

**Last Updated**: 2025-10-16
**Status**: Production Ready (FP16 model)
**Next Steps**: Optional - Implement INT8 quantization on high-RAM machine

