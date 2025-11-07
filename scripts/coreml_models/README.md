# CoreML Model Management

This directory contains scripts for converting, evaluating, and distributing CoreML models for the Papr Memory SDK.

## 🚀 Quick Start for Users

When you install `papr-memory` with CoreML support, models are **automatically downloaded** from Hugging Face:

```bash
pip install papr-memory[coreml]

# Enable CoreML (model auto-downloads on first use)
export PAPR_ENABLE_COREML=true

# Optional: Choose variant (default: fp16)
export PAPR_COREML_VARIANT=fp16  # or "int8"
```

That's it! The SDK will auto-download and cache the model on first use.

---

## 🛠️ For Maintainers

### 1. Convert Model to CoreML

```bash
# FP16 (recommended - fastest on Apple Silicon)
rye run python scripts/coreml_models/convert_qwen_coreml.py \
  --hf Qwen/Qwen3-Embedding-4B \
  --out ./coreml/Qwen3-Embedding-4B-FP16.mlpackage \
  --fp16

# INT8 (smaller, requires 32GB+ RAM)
rye run python scripts/coreml_models/convert_qwen_coreml.py \
  --hf Qwen/Qwen3-Embedding-4B \
  --out ./coreml/Qwen3-Embedding-4B-INT8.mlpackage \
  --int8
```

**Requirements:**
- **FP16**: 16GB RAM, ~5 min conversion time
- **INT8**: 32GB+ RAM, ~10-15 min conversion time (may OOM on 16GB)

---

### 2. Evaluate Accuracy

Before uploading, test the quantized model accuracy:

```bash
rye run python scripts/coreml_models/evaluate_accuracy.py \
  --coreml ./coreml/Qwen3-Embedding-4B-FP16.mlpackage \
  --hf Qwen/Qwen3-Embedding-4B \
  --num-samples 50
```

**Expected Results:**
```
Average cosine similarity: 0.999950 (99.9950%)
Accuracy loss: 0.0050%
Quality Rating: 🟢 EXCELLENT
✅ FP16 quantization is highly recommended for production use.
```

---

### 3. Upload to Hugging Face

Once you've verified the model quality:

```bash
# Login (one-time)
huggingface-cli login

# Upload FP16 model
rye run python scripts/coreml_models/upload_to_hf.py \
  --model ./coreml/Qwen3-Embedding-4B-FP16.mlpackage \
  --repo papr-ai/Qwen3-Embedding-4B-CoreML \
  --variant fp16

# Upload INT8 model (optional)
rye run python scripts/coreml_models/upload_to_hf.py \
  --model ./coreml/Qwen3-Embedding-4B-INT8.mlpackage \
  --repo papr-ai/Qwen3-Embedding-4B-CoreML \
  --variant int8
```

This uploads to: https://huggingface.co/papr-ai/Qwen3-Embedding-4B-CoreML

---

## 📊 Model Variants

| Variant | Size | Speed (M1) | Accuracy | Use Case |
|---------|------|------------|----------|----------|
| **FP16** | 7.5GB | 70ms | 99.995% | **Recommended** - Best speed/accuracy |
| **INT8** | 4GB | 100-150ms | 98-99% | Storage-constrained devices |

### Why FP16 is Faster on Apple Silicon

Apple's Neural Engine (ANE) is optimized for **FP16**, not INT8:
- FP16 runs on ANE (fastest)
- INT8 falls back to GPU (slower)
- See `agent.md` Learning #9 for details

---

## 🔧 Advanced Usage

### Manual Model Path

If you don't want auto-download, specify a local path:

```bash
export PAPR_COREML_MODEL=/path/to/your/model.mlpackage
```

### Custom HuggingFace Repo

The SDK auto-downloads from `papr-ai/Qwen3-Embedding-4B-CoreML` by default. To use a different repo, you'll need to modify `src/papr_memory/_model_cache.py:DEFAULT_COREML_REPO`.

---

## 📝 Files

- `convert_qwen_coreml.py` - Convert HuggingFace models to CoreML
- `evaluate_accuracy.py` - Test quantized model accuracy
- `upload_to_hf.py` - Upload models to Hugging Face Hub
- `measure_search_latency.py` - Benchmark end-to-end search speed
- `cleanup_memory.sh` - Clean caches before conversion

---

## 🐛 Troubleshooting

### "CoreML model not found"

Install huggingface_hub for auto-download:
```bash
pip install huggingface_hub
```

Or manually specify path:
```bash
export PAPR_COREML_MODEL=./coreml/model.mlpackage
```

### INT8 Conversion Killed (OOM)

INT8 quantization needs 24-32GB RAM. Solutions:
1. Use FP16 instead (faster anyway on ANE)
2. Convert on a 32GB+ machine
3. Close all other applications

### Slow First Query

The first query loads the CoreML model (~52s). Subsequent queries are fast (70ms). This is expected - the model stays in memory.

---

## 📚 Further Reading

- [ENV_VARIABLES.md](../../ENV_VARIABLES.md) - Configuration options
- [agent.md](../../agent.md) - Detailed learnings and best practices
- [Qwen3 on HuggingFace](https://huggingface.co/Qwen/Qwen3-Embedding-4B)

