# SDK Fix: Unified Tier Storage for ChromaDB
# File: ~/Documents/GitHub/papr-pythonSDK/src/papr_memory/resources/memory.py

## Problem Analysis

### Current Issues:
1. **Tier0** (`_store_tier0_in_chromadb`) creates the embedding function but doesn't save it
2. **Tier1** (`_store_tier1_in_chromadb`) tries to reuse tier0's embedding function but it's not available
3. **Result**: Tier1 falls back to ChromaDB's default (384-dim sentence-transformers) instead of using Qwen3-4B (2560-dim)
4. **Code duplication**: Both functions have similar logic, making maintenance harder

### Root Causes:
```python
# Tier0 (line ~2827):
embedding_function = SmartPassthroughEmbeddingFunction()  # ← Created but NOT stored to self

# Tier1 (line ~3322):
if hasattr(self, "_embedding_function") and self._embedding_function is not None:
    # ← This never succeeds because tier0 didn't store it!
```

## Solution

### Fix 1: Store Embedding Function in Tier0
After creating the embedding function in `_store_tier0_in_chromadb`, store it:

```python
# Around line 2828 in _store_tier0_in_chromadb:
embedding_function = SmartPassthroughEmbeddingFunction()
logger.info("   Created smart passthrough embedding function (2560 dims)")

# ADD THIS LINE:
self._embedding_function = embedding_function  # ← Store for tier1 to reuse!
```

### Fix 2: Ensure Tier1 Properly Falls Back
The tier1 code (lines 3324-3337) already tries to get the embedding function from tier0, which is good.
But we need to ensure it's actually available.

### Fix 3: Add Better Logging
Add logging to track whether embedding function is being reused:

```python
# In _store_tier1_in_chromadb around line 3322:
if hasattr(self, "_embedding_function") and self._embedding_function is not None:
    embedding_function = self._embedding_function
    logger.info("✅ Reusing embedding function from tier0 (stored in self._embedding_function)")
elif hasattr(self, "_collection") and self._collection is not None:
    try:
        embedding_function = self._collection._embedding_function
        logger.info("✅ Retrieved embedding function from tier0 collection")
    except Exception as e:
        logger.warning(f"❌ Could not get embedding function from tier0 collection: {e}")
# ...
```

## Implementation Plan

### Step 1: Fix tier0 to store embedding function
Location: `~/Documents/GitHub/papr-pythonSDK/src/papr_memory/resources/memory.py` line ~2828

```python
# In _store_tier0_in_chromadb, after creating SmartPassthroughEmbeddingFunction:

if os.environ.get("PAPR_ENABLE_COREML", "").lower() == "true":
    logger.info("⚡ CoreML enabled - using smart passthrough for ChromaDB")
    logger.info("   Passthrough will use already-loaded CoreML for queries")
    
    # ... (SmartPassthroughEmbeddingFunction class definition) ...
    
    embedding_function = SmartPassthroughEmbeddingFunction()
    logger.info("   Created smart passthrough embedding function (2560 dims)")
    
    # ✅ ADD THIS LINE:
    self._embedding_function = embedding_function
    logger.info("   Stored embedding function for tier1 reuse")
else:
    embedding_function = self._get_qwen_embedding_function()
    logger.info(f"Qwen embedding function result: {embedding_function is not None}")
    
    # ✅ ADD THIS LINE:
    if embedding_function:
        self._embedding_function = embedding_function
        logger.info("   Stored embedding function for tier1 reuse")
```

### Step 2: Verify tier1 gets the function
The existing code in `_store_tier1_in_chromadb` (lines 3320-3338) already tries to get it, which is good!
But let's add better logging:

```python
# In _store_tier1_in_chromadb around line 3320:

# Get the embedding function (reuse from tier0 if available)
embedding_function = None
if hasattr(self, "_embedding_function") and self._embedding_function is not None:
    embedding_function = self._embedding_function
    logger.info("✅ Reusing embedding function from tier0 (self._embedding_function)")
else:
    logger.warning("⚠️  self._embedding_function not found, trying tier0 collection...")
    # If no embedding function, try to get from tier0 collection
    if hasattr(self, "_collection") and self._collection is not None:
        try:
            embedding_function = self._collection._embedding_function
            logger.info("✅ Retrieved embedding function from tier0 _collection")
        except Exception as e:
            logger.warning(f"❌ Could not get embedding function from tier0 _collection: {e}")
    elif hasattr(self, "_chroma_collection") and self._chroma_collection is not None:
        try:
            embedding_function = self._chroma_collection._embedding_function
            logger.info("✅ Retrieved embedding function from tier0 _chroma_collection")
        except Exception as e:
            logger.warning(f"❌ Could not get embedding function from tier0 _chroma_collection: {e}")

# If still no embedding function, we need to recreate tier1 collection
if not embedding_function:
    logger.error("❌ No embedding function found - tier1 will use 384-dim default (WRONG!)")
    logger.error("   This will cause dimension mismatch errors during search")
else:
    logger.info(f"✅ Tier1 will use correct embedding function (2560 dims)")
```

### Step 3: Clean up existing broken tier1 collection
Use the cleanup script we already created:
```bash
python scripts/fix_tier1_collection.py
```

## Testing

### Expected Logs (Success):
```
[INFO] Using 200 tier0 items for search enhancement
[INFO]    Created smart passthrough embedding function (2560 dims)
[INFO]    Stored embedding function for tier1 reuse
[INFO] Created new ChromaDB collection with Qwen3-4B embeddings: tier0_goals_okrs

[INFO] Using 200 tier1 items for search enhancement
[INFO] Attempting to store tier1 data in ChromaDB...
[INFO] ✅ Reusing embedding function from tier0 (self._embedding_function)
[INFO] ✅ Tier1 will use correct embedding function (2560 dims)
[INFO] Created new tier1 collection with embedding function
```

### Search Results (Success):
```
⚡ Local CoreML fast path → Embedding: 189ms | Chroma: 8ms | Total: 197ms [15 tier0, 15 tier1]
```

### Error to Watch For (Failure):
```
[ERROR] ❌ No embedding function found - tier1 will use 384-dim default (WRONG!)
⚠️  Tier1 search failed: Collection expecting embedding with dimension of 384, got 2560
```

## Files to Modify

1. **SDK**: `~/Documents/GitHub/papr-pythonSDK/src/papr_memory/resources/memory.py`
   - Line ~2828: Store `self._embedding_function` after creating it
   - Line ~2831: Store `self._embedding_function` for Qwen path too
   - Lines 3320-3340: Add better logging for tier1

2. **Cleanup Script** (already created): `scripts/fix_tier1_collection.py`

## Rollout Plan

1. ✅ Modify SDK code (add `self._embedding_function =`)
2. ✅ Clean broken tier1 collection (`python scripts/fix_tier1_collection.py`)
3. ✅ Restart `voice_server.py`
4. ✅ Verify logs show tier1 reusing embedding function
5. ✅ Test search returns results from both tier0 and tier1

