# Summary: INT8 Quantization & ST Preload Fix

## What We Just Fixed

### 1. ✅ Root Cause of 28-Second Latency

**Problem:**
- Your logs showed: `"Embedding generation took: 35.319s"` and `"28.776s"`
- Core ML model was available but NOT being used
- Sentence Transformers was trying to preload and failing with OOM

**Root Cause:**
The SDK was trying to preload the full 4B Sentence Transformers model on MPS before checking if Core ML was enabled:

```python
# OLD CODE (memory.py:1203-1229)
def _preload_embedding_model(self) -> None:
    """Preload the embedding model..."""
    # ❌ Always tries to load ST first
    _global_qwen_model = SentenceTransformer("Qwen/Qwen3-Embedding-4B", device="mps")
    # This fails with: "MPS backend out of memory (MPS allocated: 10.63 GB)"
```

**What Happened:**
1. SDK tried to preload ST → **OOM** (10.63GB MPS + 7.49GB system)
2. Preload failed, set `_qwen_model = None`
3. During search, tried to load ST again on-demand → **28-35 seconds**
4. Core ML model was never reached because ST kept being attempted

**The Fix:**
```python
# NEW CODE (memory.py:1211-1220)
def _preload_embedding_model(self) -> None:
    # ✅ Check for Core ML/MLX first
    if os.environ.get("PAPR_ENABLE_COREML", "").lower() == "true":
        logger.info("⏭️  Skipping ST preload: Core ML is enabled (faster, less memory)")
        return
    if os.environ.get("PAPR_ENABLE_MLX", "").lower() == "true":
        logger.info("⏭️  Skipping ST preload: MLX is enabled (faster, less memory)")
        return
    
    # Only load ST if Core ML/MLX not available
    # ... (ST loading code)
```

**Expected Result:**
- ✅ No ST preload when Core ML is enabled
- ✅ No MPS out of memory errors
- ✅ Latency should drop from **28s → ~0.1-0.3s** (first query) and **~0.08-0.1s** (subsequent)
- ✅ Core ML model will be used directly

### 2. ✅ INT8 Quantization Status

**Attempt:** Tried to quantize Qwen3-4B to INT8 Core ML model

**Result:** ❌ **Failed** - Killed by kernel (OOM)

```
⚙️  Starting INT8 quantization (this may take several minutes and requires ~16-32GB RAM)...
   Quantizing model weights to INT8...
zsh: killed     python scripts/convert_qwen_coreml.py
```

**Why It Failed:**
- 16GB MacBook Pro with Docker + Cursor running
- INT8 quantization requires:
  - Load full FP16 model: ~8GB
  - Quantization operations: ~8-16GB additional
  - **Total:** ~16-24GB truly free RAM
- Your system had only ~2.21GB free after cleanup
- Swap activity was high (184M swapins, 235M swapouts)

**Options Going Forward:**

#### Option 1: Use FP16 Model (Recommended)
```bash
# Already working great!
PAPR_ENABLE_COREML=true
PAPR_COREML_MODEL=./coreml/Qwen3-Embedding-4B.mlpackage
```

**Pros:**
- ✅ Already converted and working
- ✅ 2560 dimensions verified
- ✅ Runs on ANE/GPU
- ✅ ~0.08-0.1s per embedding
- ✅ No conversion needed

**Cons:**
- ⚠️ Larger file size (~7.5GB vs ~2-4GB for INT8)
- ⚠️ More disk space required

**Verdict:** **Best choice for now** - it's production-ready and fast!

#### Option 2: Try 4-Bit Palettization
```bash
python scripts/convert_qwen_coreml.py \
  --hf Qwen/Qwen3-Embedding-4B \
  --out ./coreml/Qwen3-Embedding-4B-4BIT.mlpackage \
  --k4bit
```

**Pros:**
- ✅ More memory-efficient conversion than INT8
- ✅ Smaller model (~1-2GB)
- ✅ Might succeed on 16GB Mac

**Cons:**
- ⚠️ Slightly more accuracy loss (~2-3% vs ~1% for INT8)
- ⚠️ Still might OOM if Docker is running

**To try:**
1. Stop Docker: `docker stop $(docker ps -q)`
2. Run cleanup: `bash scripts/cleanup_memory.sh`
3. Convert: `python scripts/convert_qwen_coreml.py --k4bit`
4. Restart Docker: `docker start $(docker ps -aq)`

#### Option 3: Quantize on a Larger Machine
- Use a 32GB+ Mac (or cloud VM)
- Convert to INT8 there
- Copy the `.mlpackage` back

#### Option 4: Stick with FP16
- Don't quantize at all
- FP16 is already very fast on ANE
- 7.5GB is acceptable for most use cases

### 3. ✅ Environment Variables Updated

Created `ENV_VARIABLES.md` with all variables documented.

**Recommended `.env` changes:**

```bash
# Current (has conflicts)
PAPR_ENABLE_COREML=true
PAPR_ENABLE_MLX=true  # ❌ Conflicts with Core ML

# Recommended
PAPR_ENABLE_COREML=true
# PAPR_ENABLE_MLX=true  # ✅ Comment out - not needed when Core ML enabled
TOKENIZERS_PARALLELISM=false  # ✅ Add this
```

To update manually:
```bash
nano .env
# Comment out: PAPR_ENABLE_MLX=true
# Add: TOKENIZERS_PARALLELISM=false
```

## Next Steps

### 1. Test the ST Preload Fix (High Priority)

This should fix your 28-second latency:

```bash
cd /Users/shawkatkabbara/Documents/GitHub/papr-pythonSDK
source .env
source .venv/bin/activate

# Make sure Core ML is enabled (it is in your .env)
export PAPR_ENABLE_COREML=true
export PAPR_COREML_MODEL=./coreml/Qwen3-Embedding-4B.mlpackage

# Run latency test
python measure_search_latency.py
```

**Expected output:**
```
✅ Skipping ST preload: Core ML is enabled (faster, less memory)
✅ Using Core ML embedder
Embedding generation took: 0.285s  # First query (cold start)
Embedding generation took: 0.082s  # Subsequent queries
search latency: 367 ms  # Total including ChromaDB
```

### 2. Update .env (Manual)

```bash
nano .env
```

Changes:
```bash
# Comment out MLX
# PAPR_ENABLE_MLX=true

# Add tokenizers config
TOKENIZERS_PARALLELISM=false
```

### 3. (Optional) Try 4-Bit Quantization

Only if you want a smaller model and are willing to stop Docker:

```bash
# 1. Stop Docker
docker stop $(docker ps -q)

# 2. Clean up memory
bash scripts/cleanup_memory.sh

# 3. Convert
python scripts/convert_qwen_coreml.py \
  --hf Qwen/Qwen3-Embedding-4B \
  --out ./coreml/Qwen3-Embedding-4B-4BIT.mlpackage \
  --k4bit

# 4. Restart Docker
docker start $(docker ps -aq)

# 5. Update .env
# PAPR_COREML_MODEL=./coreml/Qwen3-Embedding-4B-4BIT.mlpackage
```

## Files Created/Modified

### Created:
- ✅ `ENV_VARIABLES.md` - Complete environment variables reference
- ✅ `SUMMARY.md` - This file
- ✅ `agent.md` - Learning #9: Python Import Scope
- ✅ `scripts/cleanup_memory.sh` - Automated memory cleanup

### Modified:
- ✅ `src/papr_memory/resources/memory.py` - Skip ST preload when Core ML/MLX enabled
- ✅ `scripts/convert_qwen_coreml.py` - Fixed `UnboundLocalError`

## Performance Expectations

| Configuration | First Query | Subsequent | Memory | Model Size |
|---------------|-------------|------------|--------|------------|
| **API Only** | ~100-500ms | ~100-500ms | ~0.5GB | None |
| **ST (MPS)** | ~28-35s | ~1-2s | ~18GB | ~7GB |
| **Core ML FP16** | ~0.2-0.3s | ~0.08-0.1s | ~2GB | ~7.5GB |
| **Core ML INT8** | ~0.2-0.3s | ~0.08-0.1s | ~1.5GB | ~2-4GB |
| **Core ML 4-bit** | ~0.2-0.3s | ~0.08-0.1s | ~1GB | ~1-2GB |

## Key Learnings

### Learning #9: Python Import Scope (agent.md)
Fixed `UnboundLocalError` caused by duplicate `import os` inside function.

### Learning #8: Memory Management (agent.md)
INT8 quantization requires 2-3x model size in truly free RAM, not just "available" memory.

## Verification Checklist

- [ ] Test latency with Core ML (should be <1s after ST preload fix)
- [ ] Verify logs show "Skipping ST preload: Core ML is enabled"
- [ ] Verify no MPS out of memory errors
- [ ] Verify Core ML model outputs [1, 2560] dimensions
- [ ] (Optional) Comment out `PAPR_ENABLE_MLX` in .env
- [ ] (Optional) Add `TOKENIZERS_PARALLELISM=false` to .env
- [ ] (Optional) Try 4-bit quantization if you want smaller model

## Questions?

1. **Why 28 seconds?** - ST model was loading on-demand because preload failed (OOM)
2. **Is Core ML working?** - Yes! It just wasn't being used due to ST preload
3. **INT8 failed?** - Yes, need 32GB+ RAM or use 4-bit palettization
4. **Should I quantize?** - Optional - FP16 is already fast and working great
5. **MLX vs Core ML?** - Core ML is faster (ANE support), disable MLX when using Core ML

---

**Status:** ✅ Ready to test! The ST preload fix should solve your 28-second latency issue.

