# CoreML ANE Usage Investigation

**Date**: November 22, 2025  
**Issue**: CoreML queries showing "likely using GPU" (250ms) despite `CPU_AND_NE` configuration  
**Expected**: Consistent ANE usage (142ms) as observed during warmup  

---

## Problem Statement

### Observed Behavior

**Warmup (Background Model Loading)**:
```
✅ CoreML model loaded with CPU_AND_NE
✅ Warmup inference: 142ms (ANE - expected performance)
```

**Live Queries (During Search)**:
```
❌ Core ML inference #1 completed in 250.0ms - likely using GPU
❌ Inconsistent with warmup performance
```

### Configuration

Current configuration in `memory.py`:
```python
coreml_compute_units_env = os.environ.get("PAPR_COREML_COMPUTE_UNITS", "CPU_AND_NE").upper()
compute_unit_map = {
    "ALL": ct.ComputeUnit.ALL,
    "CPU_AND_GPU": ct.ComputeUnit.CPU_AND_GPU,
    "CPU_AND_NE": ct.ComputeUnit.CPU_AND_NE,
    "CPU_ONLY": ct.ComputeUnit.CPU_ONLY,
}
compute_units_to_use = compute_unit_map.get(coreml_compute_units_env, ct.ComputeUnit.ALL)
mlmodel = ct.models.MLModel(coreml_path, compute_units=compute_units_to_use)
```

---

## Possible Root Causes

### 1. Model Caching Issue

**Hypothesis**: The globally cached model may not preserve the `CPU_AND_NE` configuration.

**Evidence**:
```python
# First load (warmup)
mlmodel = ct.models.MLModel(coreml_path, compute_units=ct.ComputeUnit.CPU_AND_NE)
_global_coreml_model = mlmodel  # Cache it

# Later use (search)
mlmodel = _global_coreml_model  # Uses cached model
```

**Question**: Does the cached `MLModel` object preserve the compute units configuration, or does it need to be respecified on each prediction?

**Test**:
```python
# Check if compute_units is preserved
if hasattr(mlmodel, 'compute_unit'):
    logger.info(f"Cached model compute unit: {mlmodel.compute_unit}")
```

### 2. Inference Context Switching

**Hypothesis**: CoreML may dynamically switch compute units based on runtime conditions.

**Conditions that trigger GPU fallback**:
- Memory pressure (insufficient ANE memory)
- Concurrent ANE usage (another model using ANE)
- Model complexity (some operations not ANE-compatible)
- Batch size changes (warmup vs live queries)
- Thread context (background thread vs main thread)

**Evidence Needed**:
- Compare warmup thread vs search thread contexts
- Monitor ANE memory usage during queries
- Check if warmup and search use same batch size

### 3. Compilation vs Runtime Discrepancy

**Hypothesis**: Model compilation happens during warmup (142ms, optimized for ANE), but subsequent calls use a different execution path.

**CoreML Compilation Process**:
1. **First call**: Model is compiled for target hardware (ANE)
   - Takes longer (warmup: multiple seconds)
   - Optimized binary cached in `~/Library/Caches/com.apple.CoreML/`
2. **Subsequent calls**: Uses compiled binary
   - Should be fast (142ms expected)
   - But may fallback to GPU if ANE unavailable

**Verification**:
```bash
# Check compiled model cache
ls -lh ~/Library/Caches/com.apple.CoreML/
# Should contain compiled .mil files
```

### 4. Input Shape or Type Mismatch

**Hypothesis**: Warmup and live queries use different input configurations, causing CoreML to switch execution paths.

**Differences to check**:
```python
# Warmup (in _warmup_coreml_model)
inputs = {
    "input_ids": np.array([[101, 102, 103, ...]], dtype=np.int32),  # Shape: (1, 32)
    "attention_mask": np.array([[1, 1, 1, ...]], dtype=np.int32),
}

# Live query (in _embed_query_with_qwen)
enc = self._coreml_tokenizer(text, padding="max_length", max_length=32, truncation=True, return_tensors="np")
inputs = {
    "input_ids": enc["input_ids"].astype(np.int32),
    "attention_mask": enc["attention_mask"].astype(np.int32),
}
```

**Potential issues**:
- Different dtypes (int32 vs int64)
- Different shapes (1D vs 2D arrays)
- Different padding (actual padded length)

---

## Diagnostic Steps

### Step 1: Log Model Configuration

Add logging to verify compute units configuration:

```python
# After loading model
logger.info(f"🔧 CoreML model loaded with compute_units: {compute_units_to_use}")
if hasattr(mlmodel, '_spec'):
    logger.info(f"📋 Model spec compute units: {mlmodel._spec.specificationVersion}")

# Before prediction
logger.info(f"🔍 About to run prediction with compute_units: {compute_units_to_use}")
```

### Step 2: Compare Warmup vs Live Query Inputs

Add detailed input logging:

```python
def _log_input_details(inputs: dict, context: str):
    logger.info(f"[{context}] Input details:")
    for key, val in inputs.items():
        logger.info(f"  {key}: shape={val.shape}, dtype={val.dtype}, range=[{val.min()}, {val.max()}]")

# In _warmup_coreml_model
_log_input_details(inputs, "WARMUP")

# In _embed_query_with_qwen
_log_input_details(inputs, "LIVE_QUERY")
```

### Step 3: Monitor ANE Usage with System Tools

Use macOS tools to verify ANE activity:

```bash
# Monitor ANE usage (requires sudo)
sudo powermetrics --samplers cpu_power,gpu_power --show-process-energy -i 1000

# Check CoreML cache
ls -lh ~/Library/Caches/com.apple.CoreML/

# Monitor memory pressure
memory_pressure
```

### Step 4: Force Model Reload per Query (Test)

Temporarily reload model on each query to test caching hypothesis:

```python
def _embed_query_with_qwen(self, query: str):
    # TEST: Force reload model with explicit compute units
    mlmodel = ct.models.MLModel(coreml_path, compute_units=ct.ComputeUnit.CPU_AND_NE)
    
    # Run prediction
    output = mlmodel.predict(inputs)
    # ... rest of logic
```

If this fixes the issue → caching problem  
If this doesn't fix it → runtime context issue

---

## Proposed Fixes

### Fix 1: Explicit Compute Units on Cached Model

If caching loses configuration:

```python
# Store both model and config
_global_coreml_model = (mlmodel, compute_units_to_use)

# When retrieving
mlmodel, compute_units = _global_coreml_model
# Re-specify compute units if needed
mlmodel = ct.models.MLModel(mlmodel._spec, compute_units=compute_units)
```

### Fix 2: Ensure Consistent Input Format

Standardize input preprocessing:

```python
def _prepare_coreml_inputs(self, text: str) -> dict:
    """Standardized input preparation for CoreML (warmup + live)"""
    enc = self._coreml_tokenizer(
        text, 
        padding="max_length",  # Always fixed padding
        max_length=32,         # Always 32
        truncation=True,
        return_tensors="np"
    )
    return {
        "input_ids": enc["input_ids"].astype(np.int32),      # Explicit int32
        "attention_mask": enc["attention_mask"].astype(np.int32),
    }

# Use in both warmup and live queries
inputs = self._prepare_coreml_inputs(text)
```

### Fix 3: Pre-compile Model Explicitly

Force compilation during warmup:

```python
def _warmup_coreml_model(self):
    # Load model
    mlmodel = ct.models.MLModel(coreml_path, compute_units=ct.ComputeUnit.CPU_AND_NE)
    
    # Run multiple warmup queries to ensure compilation
    for i in range(3):
        inputs = self._prepare_coreml_inputs(f"warmup query {i}")
        _ = mlmodel.predict(inputs)
        logger.info(f"Warmup iteration {i+1}/3 completed")
    
    # Cache compiled model
    _global_coreml_model = mlmodel
```

### Fix 4: Monitor and Log Execution Path

Add detailed timing breakdowns:

```python
import time

def _embed_query_with_qwen(self, query: str):
    total_start = time.time()
    
    # Tokenization
    tok_start = time.time()
    inputs = self._prepare_coreml_inputs(query)
    tok_time = (time.time() - tok_start) * 1000
    
    # Model prediction
    pred_start = time.time()
    output = self._global_coreml_model.predict(inputs)
    pred_time = (time.time() - pred_start) * 1000
    
    # Post-processing
    post_start = time.time()
    embedding = self._extract_embedding_from_output(output)
    post_time = (time.time() - post_start) * 1000
    
    total_time = (time.time() - total_start) * 1000
    
    logger.info(f"⏱️  Breakdown: tok={tok_time:.1f}ms | pred={pred_time:.1f}ms | post={post_time:.1f}ms | total={total_time:.1f}ms")
    
    # ANE heuristic: <150ms = likely ANE, >200ms = likely GPU
    if pred_time < 150:
        logger.info(f"✅ Prediction time suggests ANE usage ({pred_time:.1f}ms)")
    else:
        logger.warning(f"⚠️  Prediction time suggests GPU fallback ({pred_time:.1f}ms)")
    
    return embedding
```

---

## Expected Outcomes

### If Fix Works (ANE Consistent)

**Logs should show**:
```
✅ CoreML model loaded with CPU_AND_NE
✅ Warmup: 142ms (ANE)
✅ Query 1: 145ms (ANE)
✅ Query 2: 138ms (ANE)
✅ Query 3: 141ms (ANE)
⏱️  Breakdown: tok=5.2ms | pred=142.1ms | post=1.3ms | total=148.6ms
✅ Prediction time suggests ANE usage (142.1ms)
```

### If Fix Doesn't Work (GPU Fallback Persists)

**Logs would show**:
```
⚠️  CoreML model loaded with CPU_AND_NE
✅ Warmup: 142ms (ANE)
❌ Query 1: 248ms (GPU)
❌ Query 2: 252ms (GPU)
❌ Query 3: 245ms (GPU)
⏱️  Breakdown: tok=5.1ms | pred=250.3ms | post=1.2ms | total=256.6ms
⚠️  Prediction time suggests GPU fallback (250.3ms)
```

**Next steps if this happens**:
1. Check system ANE availability: `sysctl hw.optional.arm.FEAT_*`
2. Monitor concurrent ANE usage: `ps aux | grep CoreML`
3. Try `ComputeUnit.CPU_ONLY` to verify CPU path works
4. File bug report with Apple (possible ANE availability issue)

---

## Testing Plan

1. **Add diagnostic logging** (Step 1-2)
2. **Run test_parallel_search.py** with enhanced logs
3. **Analyze warmup vs query timing**
4. **Implement Fix 2 (standardized inputs)** + **Fix 4 (detailed breakdown)**
5. **Re-test and verify consistent 142ms ± 10ms**
6. **Document final solution in COREML_ANE_OPTIMIZATION.md**

---

## Related Documents

- [COREML_ANE_OPTIMIZATION.md](./COREML_ANE_OPTIMIZATION.md) - CoreML ANE configuration guide
- [PARALLEL_COLLECTION_SEARCH.md](./PARALLEL_COLLECTION_SEARCH.md) - Parallel search implementation
- [agent.md](../agent.md#learning-14-coreml-cpu_and_ne-forces-ane-usage) - Learning about CPU_AND_NE

---

## Status

🔍 **Investigation Phase**  
Next action: Implement diagnostic logging and run test_parallel_search.py

