# Environment Variables Reference

This document lists all environment variables used by the Papr Memory Python SDK.

## Quick Setup

Add these to your `.env` file:

```bash
# Papr Memory API Configuration
PAPR_MEMORY_API_KEY=your_api_key_here
PAPR_BASE_URL=https://your-ngrok-url.ngrok.app

# Debugging and Logging
PAPR_LOG=debug
PAPR_LOG_FILE=logs

# On-Device Processing Configuration
PAPR_ONDEVICE_PROCESSING=true
PAPR_MAX_TIER0=30
PAPR_MAX_TIER1=30
PAPR_SYNC_INTERVAL=30

# Core ML Configuration (Recommended for Apple Silicon)
PAPR_ENABLE_COREML=true
PAPR_COREML_MODEL=./coreml/Qwen3-Embedding-4B.mlpackage

# System Configuration
PYTHONPATH=src:$PYTHONPATH
TOKENIZERS_PARALLELISM=false
```

## Variable Descriptions

### Core API Configuration

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `PAPR_MEMORY_API_KEY` | **Yes** | - | Your Papr Memory API key |
| `PAPR_BASE_URL` | **Yes** | - | Base URL for Papr Memory API |

### On-Device Processing

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `PAPR_ONDEVICE_PROCESSING` | No | `false` | Enable local embedding and search |
| `PAPR_MAX_TIER0` | No | `300` | Max tier0 memories to sync and store locally |
| `PAPR_MAX_TIER1` | No | `1000` | Max tier1 memories to sync and store locally |
| `PAPR_SYNC_INTERVAL` | No | `3600` | Background sync interval in seconds |
| `PAPR_INCLUDE_SERVER_EMBEDDINGS` | No | `true` | Request pre-computed embeddings from server |
| `PAPR_EMBEDDING_FORMAT` | No | `float32` (if CoreML), `int8` (otherwise) | Embedding format for tier1: `float32` (recommended for CoreML/ANE fp16), `int8` (4x smaller, default). Tier0 always uses float32. |
| `PAPR_EMBED_LIMIT` | No | `200` | Max items to embed on server per tier (controls server latency) |
| `PAPR_EMBED_MODEL` | No | `Qwen4B` | Embedding model hint for server: `sbert`, `bigbird`, `Qwen4B` |
| `PAPR_ONDEVICE_SIMILARITY_THRESHOLD` | No | `0.80` | Min similarity score for on-device results (0.0-1.0) |
| `PAPR_ENABLE_PARALLEL_SEARCH` | No | `true` | Run on-device and cloud search in parallel |

### Core ML (Apple Silicon - Recommended)

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `PAPR_ENABLE_COREML` | No | `false` | Enable Core ML embedder (ANE/GPU) |
| `PAPR_COREML_MODEL` | No | `./coreml/Qwen3-Embedding-4B.mlpackage` | Path to Core ML model |
| `PAPR_COREML_COMPUTE_UNITS` | No | `CPU_AND_NE` | CoreML compute units: `ALL`, `CPU_AND_GPU`, `CPU_AND_NE`, `CPU_ONLY` |

**Benefits:**
- ✅ Runs on Apple Neural Engine (ANE) + GPU
- ✅ ~0.08-0.1s per embedding (after warmup)
- ✅ Low memory usage (~1-2GB for INT8, ~7GB for FP16)
- ✅ No MPS memory issues
- ✅ Automatically skips ST preload

**Compute Units Guide:**
- `ALL` (default): Let CoreML choose best hardware (recommended for large models)
- `CPU_AND_GPU`: Force GPU + CPU (good for graphics-heavy workloads)
- `CPU_AND_NE`: Force ANE + CPU (best for small models, may crash on large models)
- `CPU_ONLY`: CPU only (slowest, for debugging)

### MLX (Apple Silicon - Alternative)

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `PAPR_ENABLE_MLX` | No | `false` | Enable MLX quantized embedder |
| `PAPR_EMBEDDING_MODEL` | No | `Qwen/Qwen3-Embedding-4B` | HuggingFace model ID for MLX |

**Benefits:**
- ✅ Native quantized models (4-bit)
- ✅ Optimized for Apple Silicon
- ✅ Smaller model size
- ❌ Slower than Core ML

### Sentence Transformers (Fallback)

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `PAPR_DISABLE_ST_PRELOAD` | No | `false` | Disable ST model preloading |
| `PAPR_EMBEDDING_MODEL` | No | `Qwen/Qwen3-Embedding-4B` | HuggingFace model ID |

**Note:** Automatically disabled when `PAPR_ENABLE_COREML` or `PAPR_ENABLE_MLX` is `true`.

**Issues:**
- ⚠️ High memory usage (~10GB MPS + 7GB system)
- ⚠️ Slow first query (~28-35s)
- ⚠️ Can cause MPS out of memory

### Logging

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `PAPR_LOG` | No | `info` | Log level: `debug`, `info`, `warning`, `error` |
| `PAPR_LOG_FILE` | No | - | Log file path (optional) |

### System

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `PYTHONPATH` | No | - | Add `src:$PYTHONPATH` for local development |
| `TOKENIZERS_PARALLELISM` | No | - | Set to `false` to silence tokenizers warnings |

## Configuration Examples

### 1. Production (Core ML - Recommended)

```bash
PAPR_MEMORY_API_KEY=your_key
PAPR_BASE_URL=https://api.papr-memory.com
PAPR_ONDEVICE_PROCESSING=true
PAPR_ENABLE_COREML=true
PAPR_COREML_MODEL=./coreml/Qwen3-Embedding-4B-INT8.mlpackage
TOKENIZERS_PARALLELISM=false
```

**Result:** Fast (~0.08-0.1s), low memory, ANE accelerated

### 2. Development (MLX)

```bash
PAPR_MEMORY_API_KEY=your_key
PAPR_BASE_URL=http://localhost:3000
PAPR_ONDEVICE_PROCESSING=true
PAPR_ENABLE_MLX=true
PAPR_EMBEDDING_MODEL=mlx-community/Qwen3-Embedding-4B-4bit-DWQ
PAPR_LOG=debug
```

**Result:** Smaller models, good for development

### 3. API Only (No On-Device)

```bash
PAPR_MEMORY_API_KEY=your_key
PAPR_BASE_URL=https://api.papr-memory.com
PAPR_ONDEVICE_PROCESSING=false
```

**Result:** All processing on server, no local models

### 4. Testing/Debugging

```bash
PAPR_MEMORY_API_KEY=your_key
PAPR_BASE_URL=http://localhost:4010
PAPR_LOG=debug
PAPR_LOG_FILE=logs/papr-sdk.log
PAPR_ONDEVICE_PROCESSING=true
PAPR_ENABLE_COREML=true
```

## Your Current Configuration

Based on your `.env` file:

```bash
✅ PAPR_MEMORY_API_KEY - Set
✅ PAPR_BASE_URL - Set (ngrok)
✅ PAPR_ONDEVICE_PROCESSING - Enabled
✅ PAPR_ENABLE_COREML - Enabled
✅ PAPR_COREML_MODEL - Set to FP16 model
⚠️ PAPR_ENABLE_MLX - Enabled (should disable - conflicts with Core ML)
⚠️ TOKENIZERS_PARALLELISM - Not set (add this)
```

## Recommended Changes

Update your `.env` to:

```bash
# Comment out MLX (not needed when Core ML is enabled)
# PAPR_ENABLE_MLX=true
# PAPR_EMBEDDING_MODEL=mlx-community/Qwen3-Embedding-4B-4bit-DWQ

# Add tokenizers config
TOKENIZERS_PARALLELISM=false
```

## Priority Order

The SDK uses this priority for embedding:

1. **Core ML** (if `PAPR_ENABLE_COREML=true`) ← Fastest
2. **MLX** (if `PAPR_ENABLE_MLX=true`)
3. **Sentence Transformers** (fallback) ← Slowest
4. **API** (if on-device fails or disabled)

## Troubleshooting

### "MPS backend out of memory"
- ✅ **Solution:** Enable Core ML (`PAPR_ENABLE_COREML=true`)
- ✅ Core ML automatically skips ST preload

### "28-35 second latency"
- ❌ **Cause:** ST model loading on-demand
- ✅ **Solution:** Enable Core ML or MLX to skip ST

### "Collection embedding function test failed"
- ℹ️ **Info:** Harmless ChromaDB internal test
- ✅ **Status:** Core ML model is working correctly

## More Information

- Core ML Integration: See `COREML_INTEGRATION_SUMMARY.md`
- Conversion Guide: See `scripts/convert_qwen_coreml.py --help`
- Learnings: See `agent.md`

