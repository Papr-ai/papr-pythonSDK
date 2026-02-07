# INT8 Quantization Status

## Current Status: 🏃 **RUNNING**

INT8 quantization for Qwen3-Embedding-4B is currently in progress.

### What's Happening
The conversion script is:
1. ✅ Cleaning up caches (freed 2.15GB of RAM)
2. ✅ Loading Qwen3-Embedding-4B from Hugging Face
3. ✅ Converting PyTorch → TorchScript → Core ML (FP16)
4. 🏃 **Quantizing weights to INT8** ← Currently here (most memory-intensive step)
5. ⏳ Saving quantized model

### Expected Timeline
- **Total time**: 5-10 minutes
- **Current step (quantization)**: 3-5 minutes
- **Peak memory usage**: ~12-16GB

### Memory Status
- **Before cleanup**: 0.06GB free
- **After cleanup**: 2.21GB free
- **Docker**: Kept running (services need to stay up)
- **Caches cleared**: Core ML cache, ChromaDB, Python caches, old models

### If Quantization Succeeds
You'll get:
- **Model size**: ~2-4GB (instead of 7.5GB FP16)
- **Output dimensions**: [1, 2560] (verified automatically)
- **Accuracy**: ~99% of FP16 (minimal loss)
- **Speed**: Same or faster than FP16 on ANE/GPU

### If Quantization Fails (OOM)
**Fallback Option 1**: Stop Docker temporarily
```bash
docker stop $(docker ps -q)
# This frees an additional ~1.3GB
# Re-run: python scripts/convert_qwen_coreml.py --int8
# Restart Docker after: docker start $(docker ps -aq)
```

**Fallback Option 2**: Use 4-bit palettization (more memory-efficient)
```bash
python scripts/convert_qwen_coreml.py \
  --hf Qwen/Qwen3-Embedding-4B \
  --out ./coreml/Qwen3-Embedding-4B-4BIT.mlpackage \
  --k4bit
```
- **Model size**: ~1-2GB (even smaller!)
- **Memory required**: Less than INT8 during conversion
- **Accuracy**: ~97-98% of FP16 (acceptable for most use cases)

**Fallback Option 3**: Stick with FP16
The FP16 model is already working great:
- ✅ 2560 dimensions
- ✅ Running on ANE/GPU
- ✅ ~0.08-0.1s per embedding (after warmup)
- ✅ Production ready

## How to Check Progress

### Monitor the conversion:
```bash
# Check if process is still running
ps aux | grep convert_qwen_coreml

# Check memory usage
memory_pressure

# Check for output
ls -lh coreml/
```

### Expected Output:
```
🧹 Cleaning up caches...
  ✅ Cache cleanup completed

Core ML model output shape: [1, 2560]
Core ML model output data type: 65568

⚙️  Starting INT8 quantization...
   Quantizing model weights to INT8...
   ✅ INT8 quantization successful!
   Output shape after quantization: [1, 2560]

💾 Saving Core ML model...

✅ Core ML model created successfully!
   📁 Location: ./coreml/Qwen3-Embedding-4B-INT8.mlpackage
   📊 Size: 2000-4000 MB (2-4 GB)
   🎯 Output dimensions: [1, 2560]
   🔧 Quantization: INT8 (2-4x smaller than FP16)
```

## Next Steps After Success

1. **Test the quantized model**:
   ```bash
   python -c "
   import coremltools as ct
   import numpy as np
   from transformers import AutoTokenizer
   
   model = ct.models.MLModel('coreml/Qwen3-Embedding-4B-INT8.mlpackage')
   tokenizer = AutoTokenizer.from_pretrained('Qwen/Qwen3-Embedding-4B')
   
   enc = tokenizer(['test'], padding='max_length', max_length=32, truncation=True, return_tensors='np')
   result = model.predict({'input_ids': enc['input_ids'].astype(np.int32), 'attention_mask': enc['attention_mask'].astype(np.int32)})
   print('Output shape:', next(iter(result.values())).shape)  # Should be (1, 2560)
   "
   ```

2. **Update environment to use INT8 model**:
   ```bash
   export PAPR_ENABLE_COREML=true
   export PAPR_COREML_MODEL=./coreml/Qwen3-Embedding-4B-INT8.mlpackage
   export PAPR_ONDEVICE_PROCESSING=true
   ```

3. **Run latency test**:
   ```bash
   python measure_search_latency.py
   ```

4. **Compare with FP16**:
   - Model size: INT8 should be 2-4GB vs FP16's 7.5GB
   - Speed: Should be similar or faster
   - Accuracy: Compare embedding similarity on sample queries

## Key Files

- **Conversion script**: `scripts/convert_qwen_coreml.py`
- **Cleanup script**: `scripts/cleanup_memory.sh`
- **Learnings**: `agent.md` (Learning #8: Memory Management)
- **Full docs**: `COREML_INTEGRATION_SUMMARY.md`

## Troubleshooting

### Process killed/OOM
- Run cleanup script again: `bash scripts/cleanup_memory.sh`
- Stop Docker: `docker stop $(docker ps -q)`
- Try 4-bit palettization: `--k4bit` instead of `--int8`

### Quantization fails with error
- Check logs for specific error message
- Verify `coremltools` version: `pip show coremltools`
- Try without quantization: Use FP16 model (already working)

### Model outputs wrong dimensions
- This is automatically verified during conversion
- If it happens, check `convert_qwen_coreml.py` EmbedWrapper implementation

---

**Last Updated**: 2025-10-16
**Status**: INT8 quantization in progress
**Memory**: Cleaned up, 2.21GB free, Docker kept running

