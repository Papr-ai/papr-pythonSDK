# CoreML ANE (Apple Neural Engine) Optimization Guide

This guide explains how to ensure your CoreML FP16 model uses the Apple Neural Engine (ANE) for optimal performance.

## Quick Summary

✅ **Your model is already FP16** - confirmed in conversion script
✅ **Use `ct.ComputeUnit.CPU_AND_NE`** for explicit ANE usage
✅ **Run test script** to verify ANE is being used

## Understanding Compute Units

CoreML offers different compute unit configurations:

| Compute Unit | Description | When to Use |
|--------------|-------------|-------------|
| `CPU_AND_NE` | CPU + ANE only (no GPU) | **Best for FP16 models** - Forces ANE usage |
| `ALL` | CPU + GPU + ANE | Lets CoreML decide (may choose GPU over ANE) |
| `CPU_AND_GPU` | CPU + GPU (no ANE) | For comparison/testing only |
| `CPU_ONLY` | CPU only | Slowest, avoid in production |

## Why CPU_AND_NE Instead of ALL?

When you use `ct.ComputeUnit.ALL`, CoreML may choose GPU instead of ANE depending on various factors:
- Model size
- Operation types
- System load
- Heuristics

By using `ct.ComputeUnit.CPU_AND_NE`, you **explicitly exclude GPU** and **force ANE usage**, which is optimal for FP16 models on Apple Silicon.

## Performance Expectations

Expected latency for your Qwen3-Embedding-4B FP16 model:

| Compute Unit | Expected Latency | Notes |
|--------------|------------------|-------|
| ANE | **<150ms** | ✅ Optimal for FP16 |
| GPU | 150-300ms | Good but not optimal |
| CPU | >300ms | Too slow |

## Testing ANE Usage

### 1. Run the Enhanced Test Script

```bash
cd /Users/shawkatkabbara/Documents/GitHub/papr-pythonSDK

# Set environment variable
export PAPR_COREML_MODEL="/Users/shawkatkabbara/Documents/GitHub/papr-pythonSDK/coreml/Qwen3-Embedding-4B-FP16-Final.mlpackage"

# Run test
python test_coreml_speed.py
```

This will test all compute unit configurations and show:
- Latency for each configuration
- Which compute unit is fastest
- Whether ANE is providing speedup
- Specific recommendations

### 2. Interpret Results

The test script will analyze performance and tell you:

**✅ ANE IS ACTIVE** (if latency <150ms):
```
ANE Time:  120.50ms
GPU Time:  250.30ms
Speedup:   2.08x

✅ ANE IS ACTIVE AND PERFORMING WELL!
   - Latency <150ms indicates ANE usage
   - This is optimal performance for FP16 models
```

**⚠️ ANE NOT OPTIMAL** (if latency >300ms):
```
ANE Time:  350.20ms
GPU Time:  250.30ms
Speedup:   0.71x

❌ GPU IS FASTER THAN ANE
   - GPU is 39.9% faster
   - Model may not be optimized for ANE
```

## SDK Configuration

### Current Configuration (UPDATED)

The SDK now uses `ct.ComputeUnit.CPU_AND_NE` for explicit ANE usage:

```python
# In memory.py line ~798
mlmodel = ct.models.MLModel(coreml_path, compute_units=ct.ComputeUnit.CPU_AND_NE)
```

### Environment Variables

Set these environment variables when using the SDK:

```bash
# Enable CoreML
export PAPR_ENABLE_COREML=true

# Set model path (auto-downloads if not set)
export PAPR_COREML_MODEL="/path/to/Qwen3-Embedding-4B-FP16-Final.mlpackage"

# Set embedding model for tokenizer
export PAPR_EMBEDDING_MODEL="Qwen/Qwen3-Embedding-4B"
```

## Troubleshooting

### Problem: Slow inference in another repo

**Symptoms:**
- First inference takes >60s
- Subsequent inferences take >1s
- Expected <150ms on ANE

**Solutions:**

1. **Verify model path is correct**
   ```bash
   echo $PAPR_COREML_MODEL
   # Should print valid path to .mlpackage
   ```

2. **Check if model is being loaded**
   - Look for log: "Loading Core ML model from..."
   - Should see: "Requesting CoreML compute units: ct.ComputeUnit.CPU_AND_NE"

3. **Verify device supports ANE**
   ```python
   import platform
   print(platform.machine())  # Should print "arm64" for Apple Silicon
   ```

4. **Check coremltools version**
   ```python
   import coremltools as ct
   print(ct.__version__)  # Should be >=7.0
   ```

5. **Clear CoreML cache**
   ```bash
   # Clear macOS CoreML compilation cache
   rm -rf ~/Library/Caches/com.apple.CoreML/*
   ```

6. **Reconvert model if needed**
   ```bash
   cd scripts/coreml_models
   python convert_qwen_coreml.py
   ```

### Problem: Model not found

**Symptoms:**
- Error: "Model not found at..."
- SDK falls back to sentence-transformers

**Solutions:**

1. **Set correct path**
   ```bash
   # Use absolute path
   export PAPR_COREML_MODEL="/Users/your-username/path/to/model.mlpackage"
   ```

2. **Or let SDK auto-download**
   ```bash
   # Don't set PAPR_COREML_MODEL
   # SDK will download from HuggingFace automatically
   unset PAPR_COREML_MODEL
   ```

### Problem: Still using GPU instead of ANE

**Symptoms:**
- Test shows GPU faster than ANE
- Latency 200-300ms instead of <150ms

**Possible Causes:**

1. **Model has unsupported operations**
   - Some PyTorch operations don't map well to ANE
   - Check conversion warnings

2. **Model too large for ANE**
   - ANE has memory limits (~1GB)
   - Use `bisect_model` to split if needed

3. **Model not properly converted**
   - Reconvert with latest coremltools
   - Ensure FP16 precision specified

## Model Conversion Best Practices

If you need to reconvert the model for better ANE support:

```python
import coremltools as ct
from coremltools.converters.mil import Builder as mb

# Key settings for ANE optimization:
model = ct.convert(
    pytorch_model,
    
    # Explicit FP16 for ANE
    compute_precision=ct.precision.FLOAT16,
    
    # Prefer ANE
    compute_units=ct.ComputeUnit.CPU_AND_NE,
    
    # Fixed input shapes (ANE prefers static shapes)
    inputs=[
        ct.TensorType(name="input_ids", shape=(1, 32), dtype=np.int32),
        ct.TensorType(name="attention_mask", shape=(1, 32), dtype=np.int32),
    ],
    
    # Minimum deployment target
    minimum_deployment_target=ct.target.macOS13,
)

# Save
model.save("model.mlpackage")
```

## Verification Checklist

Before deploying to production:

- [ ] Ran `test_coreml_speed.py` and confirmed ANE usage
- [ ] Latency <150ms for `CPU_AND_NE` configuration
- [ ] Environment variables set correctly
- [ ] Model path accessible from other repos
- [ ] Device has Apple Silicon (arm64)
- [ ] macOS version ≥13.0 (for best ANE support)
- [ ] coremltools version ≥7.0

## Performance Monitoring in Production

Add this to your code to monitor ANE usage:

```python
import time
from papr_memory._logging import get_logger

logger = get_logger(__name__)

# Time your inferences
start = time.perf_counter()
output = mlmodel.predict(feed)
duration = (time.perf_counter() - start) * 1000  # ms

# Log and analyze
logger.info(f"CoreML inference: {duration:.2f}ms")

if duration < 150:
    logger.info("✅ ANE active (excellent performance)")
elif duration < 300:
    logger.warning("⚠️ Possibly using GPU (good but not optimal)")
else:
    logger.error("❌ Likely using CPU (performance issue)")
```

## References

- [CoreML Documentation](https://developer.apple.com/documentation/coreml)
- [coremltools Guide](https://coremltools.readme.io/)
- [ANE Performance Guide](https://machinelearning.apple.com/research/neural-engine-transformers)
- [Model Optimization](https://apple.github.io/coremltools/docs-guides/source/mlmodel-utilities.html)

## Summary

1. ✅ Your model is FP16 (confirmed)
2. ✅ SDK now uses `CPU_AND_NE` (updated)
3. ✅ Test script will verify ANE usage
4. ⚡ Expected latency: <150ms on ANE
5. 🔧 If slow, check environment variables and model path

Run `python test_coreml_speed.py` now to verify everything is working!


