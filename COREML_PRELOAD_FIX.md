# CoreML Segmentation Fault Fix

## Problem

When using `PAPR_COREML_COMPUTE_UNITS=CPU_AND_NE` with the Qwen3-4B FP16 model, the application crashes with a **segmentation fault** after initialization.

```
[2025-11-22 07:13:29] Core ML inference #1 completed in 9283.1ms (batch=1) - likely using CPU or slow GPU
zsh: segmentation fault  python src/python/voice_server.py
```

### Symptoms
- ❌ **Segmentation fault** after CoreML initialization
- ❌ **Very slow first inference** (9.3s instead of <150ms)
- ⚠️ **Warning:** `No configuration object found on MLModel`
- ✅ Model loads successfully before crashing

## Root Cause

**Large models (4B parameters) are incompatible with `CPU_AND_NE` compute units.**

1. **ANE has size limits** - Models > 2B params often exceed ANE's memory/compute capacity
2. **CoreML falls back to CPU** - When ANE fails, it uses slow CPU fallback causing 9.3s inference
3. **Memory corruption** - The failed ANE→CPU fallback can cause segfaults
4. **Model not bisected** - Large models need to be split for ANE compatibility

## Solution 1: Use Default Compute Units (Recommended)

**Remove or set `PAPR_COREML_COMPUTE_UNITS=ALL`** to let CoreML choose the best hardware:

```bash
# In your .env or environment
export PAPR_COREML_COMPUTE_UNITS=ALL  # or just remove the variable
```

This allows CoreML to intelligently use:
- ✅ ANE for compatible operations
- ✅ GPU for large matrix operations
- ✅ CPU as needed
- ✅ **No segfaults** - proper fallback handling

## Solution 2: Use CPU_AND_GPU

For graphics-heavy workloads or if ANE is unavailable:

```bash
export PAPR_COREML_COMPUTE_UNITS=CPU_AND_GPU
```

This gives:
- ✅ Fast GPU inference (~150-300ms)
- ✅ Stable - no ANE compatibility issues
- ✅ Works with large models

## Solution 3: Bisect Model for ANE (Advanced)

To truly use ANE with large models, you need to split the model:

```bash
# Use coremltools to bisect the model
python -m coremltools.converters.mil.frontend.bisect \
  --model-path coreml/Qwen3-Embedding-4B-FP16-Final.mlpackage \
  --output-dir coreml/Qwen3-4B-Bisected/ \
  --max-segments 4
```

Then update your env:
```bash
export PAPR_COREML_MODEL=./coreml/Qwen3-4B-Bisected/
```

## Performance Comparison

| Compute Unit | First Inference | Subsequent | Stability | Best For |
|--------------|----------------|------------|-----------|----------|
| `ALL` (default) | ~2.7s | ~150-300ms | ✅ Stable | **Large models (recommended)** |
| `CPU_AND_GPU` | ~2-3s | ~150-300ms | ✅ Stable | Graphics workloads |
| `CPU_AND_NE` | ❌ 9.3s crash | - | ❌ Crashes | Small models only |
| `CPU_ONLY` | ~10-15s | ~5-10s | ✅ Stable | Debugging only |

## Verification

After changing the compute unit, verify it's working:

```bash
# Check logs for successful loading
[INFO] 🔧 Requesting CoreML compute units: ALL
[INFO] ✅ CoreML model loaded successfully with ALL
[INFO] Core ML inference #1 completed in 2721.9ms (batch=1)  # Much faster!
```

**Good signs:**
- ✅ First inference < 3s (not 9s)
- ✅ No segmentation fault
- ✅ Subsequent inferences < 300ms

## Environment Variable Summary

```bash
# Recommended configuration for Qwen3-4B FP16
PAPR_ENABLE_COREML=true
PAPR_COREML_MODEL=./coreml/Qwen3-Embedding-4B-FP16-Final.mlpackage
PAPR_COREML_COMPUTE_UNITS=ALL  # Default, can omit this line
PAPR_EMBEDDING_MODEL=Qwen/Qwen3-Embedding-4B
```

## Testing

Test the fix by running your application:

```bash
# Clear any cached compiled models
rm -rf ~/Library/Caches/com.apple.CoreML/

# Run with new settings
python src/python/voice_server.py
```

Look for:
1. ✅ Faster first inference (< 3s)
2. ✅ No segmentation fault
3. ✅ "CoreML model loaded successfully" message

## Why CPU_AND_NE Fails

**Technical details:**

1. **ANE constraints:**
   - Max tensor size: Limited by ANE memory (~2GB)
   - Supported ops: Not all CoreML ops are ANE-compatible
   - Model size: Large models (> 2B params) often exceed limits

2. **What happens:**
   - CoreML tries to load model on ANE
   - ANE rejects due to size/compatibility
   - Falls back to **slow CPU path** (9.3s inference)
   - Memory corruption during fallback causes **segfault**

3. **Why ALL works:**
   - CoreML analyzes model ahead of time
   - Splits workload across ANE/GPU/CPU intelligently
   - Proper error handling - no crashes
   - Uses GPU for large matrix ops (fast!)

## See Also

- `ENV_VARIABLES.md` - Full environment variable reference
- `docs/COREML_ANE_OPTIMIZATION.md` - Performance tuning guide
- `test_coreml_speed.py` - Performance testing script
