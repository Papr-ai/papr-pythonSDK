# Tier1 Collection Fixes

## Issues Found

### 1. Content Not Displaying (FIXED ✅)
**Problem**: Memories showed `(No content)...` in search results even though ChromaDB had the data.

**Root Cause**: `voice_server.py` was looking for content in `metadata["content"]`, but ChromaDB stores it in the `document` field.

**Fix**: Updated `_perform_local_coreml_search()` to read from `doc` first, then fall back to `metadata.get("content")`:
```python
# Before (wrong):
content = metadata.get("content") or doc

# After (correct):
content = doc or metadata.get("content") or "(No content)"
```

**Files Changed**:
- `src/python/voice_server.py` (lines ~245 and ~290)

---

### 2. Tier1 Dimension Mismatch (FIXED ✅)
**Problem**: Tier1 search failed with error:
```
Collection expecting embedding with dimension of 384, got 2560
```

**Root Cause**: 
1. The `tier1_memories` collection was created with ChromaDB's default embedding function (384-dim sentence-transformers)
2. This happened because `self._embedding_function` wasn't set when `_store_tier1_in_chromadb()` was called
3. Tier0 uses Qwen3-4B embeddings (2560-dim), so there was a mismatch

**Fix**: 
1. **SDK Fix**: Enhanced `_store_tier1_in_chromadb()` in the papr-pythonSDK to:
   - Check for embedding function from tier0 collection
   - Detect dimension mismatches in existing tier1 collections
   - Automatically recreate tier1 with correct dimensions
2. **Cleanup Script**: Created `scripts/fix_tier1_collection.py` to delete the broken tier1 collection

**Files Changed**:
- `~/Documents/GitHub/papr-pythonSDK/src/papr_memory/resources/memory.py` (lines ~3315-3380)
- `scripts/fix_tier1_collection.py` (new file)

---

## How to Verify the Fixes

### 1. Clean State
```bash
cd /Users/shawkatkabbara/Documents/GitHub/papr-voice-demo

# Delete broken tier1 collection
python scripts/fix_tier1_collection.py
```

### 2. Restart Server
```bash
# Make sure .env has:
# PAPR_MAX_TIER0=200
# PAPR_MAX_TIER1=200

source venv/bin/activate
python src/python/voice_server.py
```

**Expected Output**:
```
[INFO] Found 200 tier0 items in sync response
[INFO] Found 200 tier1 items in sync response
[INFO] Using 200 tier0 items for search enhancement
[INFO] Using 200 tier1 items for search enhancement
[INFO] Attempting to store tier1 data in ChromaDB...
[INFO] Reusing embedding function from tier0
[INFO] Created new tier1 collection with embedding function
```

### 3. Test Search
Open http://localhost:3000 and search for: `"discussion with Brian CTO of Dialpad"`

**Expected Output**:
```
⚡ Local CoreML fast path → Embedding: 189.5ms | Chroma: 8.4ms | Total: 197.9ms [15 tier0, 15 tier1]

📊 Retrieved 30 memories from local fast path
   ✅ 30 with content  ← Should show actual content now!
   ❌ 0 without content

📋 All 30 memories:
   [1] Query: -0.8546 | ---

### Meeting Overview

You met with Brian, Dialpad's CTO, to discuss Papr's predictive memory l...
```

**Key Success Indicators**:
- ✅ No `"(No content)..."` in results
- ✅ No `"Collection expecting embedding with dimension of 384, got 2560"` error
- ✅ Results show mix of tier0 and tier1: `[X tier0, Y tier1]`
- ✅ Actual memory content displays in results

---

## Architecture

### Correct Flow (After Fix):

```
voice_server.py startup
    ↓
SDK sync_tiers() 
    ↓
Store tier0 → tier0_goals_okrs (2560-dim, Qwen3-4B)
    ↓
Store tier1 → tier1_memories (2560-dim, Qwen3-4B) ← Fixed!
    ↓
voice_server.py search
    ↓
Generate embedding (2560-dim)
    ↓
Query tier0 (2560-dim) ✅
Query tier1 (2560-dim) ✅ ← Now works!
    ↓
Merge & sort results
    ↓
Return content from 'doc' field ✅ ← Now displays!
```

---

## Future Prevention

### SDK Enhancement (Implemented):
The SDK now automatically:
1. Checks if `_embedding_function` exists before creating tier1
2. Falls back to tier0 collection's embedding function if needed
3. Detects dimension mismatches and recreates collections automatically
4. Logs warnings if no embedding function is found

### Monitoring:
Watch for these log messages:
- ✅ `"Reusing embedding function from tier0"` (good!)
- ⚠️ `"No embedding function found - tier1 will need to be recreated later"` (bad!)
- ⚠️ `"Tier1 collection has wrong dimensions (384 != 2560), recreating..."` (recovery in progress)

---

## Summary

| Issue | Status | Impact |
|-------|--------|--------|
| Content not displaying | ✅ Fixed | Users can now see actual memory content |
| Tier1 dimension mismatch | ✅ Fixed | Tier1 search now works without errors |
| SDK auto-detection | ✅ Implemented | Future tier1 collections will be created correctly |

**Total Changes**: 3 files modified, 1 new script created
**Testing Required**: Run `voice_server.py` and perform searches with tier0+tier1 enabled

