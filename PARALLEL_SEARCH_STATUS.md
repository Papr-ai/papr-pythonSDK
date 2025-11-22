# Parallel Search Implementation Status

**Date**: November 22, 2025  
**Status**: ⚠️ Partial Implementation  

---

## ✅ Completed

1. **User Context Management** (100%)
   - ✅ `MemoryResource.__init__()` with user_id/external_user_id
   - ✅ `set_user_context()` method
   - ✅ `clear_user_context()` method
   - ✅ `_clear_chromadb_collections()` helper

2. **Pydantic Types & Server Embeddings** (100%)
   - ✅ Created `SyncTiersRequest` and `SyncTiersResponse` types
   - ✅ Updated `_process_sync_tiers_and_store()` to use user context
   - ✅ Request server embeddings with `include_embeddings=True`
   - ✅ Use `embed_limit` and `embed_model` from environment variables
   - ✅ Log server embeddings statistics

3. **Helper Methods** (33%)
   - ✅ `_get_max_similarity()` - Calculate max similarity from results

---

## ⏳ In Progress

### Parallel Search Implementation

**Current State**: The `search()` method currently has a simple on-device/cloud fallback:
- If on-device enabled & model ready → use on-device, return early
- Otherwise → call cloud API

**Target State**: Need to implement intelligent parallel search:
1. Check if agentic_graph is enabled → always use cloud
2. Check if on-device is enabled
3. If parallel search enabled → run both simultaneously
4. Apply similarity threshold to on-device results
5. Return best results (on-device if good enough, cloud otherwise)

**Implementation Needed**:

```python
# In search() method around line 4300

# Get configuration
ondevice_processing = os.environ.get("PAPR_ONDEVICE_PROCESSING", "false").lower() in ("true", "1", "yes", "on")
enable_parallel = os.environ.get("PAPR_ENABLE_PARALLEL_SEARCH", "true").lower() in ("true", "1", "yes", "on")
similarity_threshold = float(os.environ.get("PAPR_ONDEVICE_SIMILARITY_THRESHOLD", "0.80"))
agentic_enabled = enable_agentic_graph if enable_agentic_graph is not omit else False

# If agentic graph is enabled, always use cloud
if agentic_enabled:
    logger.info("🌐 Agentic graph enabled - using cloud search only")
    # Fall through to cloud API call at end of method

# If on-device not enabled or no collections, use cloud only
elif not ondevice_processing or not hasattr(self, "_chroma_collection"):
    logger.info("📡 On-device not available - using cloud search only")
    # Fall through to cloud API call at end of method

# If parallel search not enabled, use on-device only (current behavior)
elif not enable_parallel:
    logger.info("🔍 On-device search only (parallel disabled)")
    # Current on-device logic here (lines 4314-4415)
    # Return early with on-device results

# PARALLEL SEARCH: Run on-device and cloud simultaneously
else:
    logger.info("⚡ Starting parallel search (on-device + cloud)")
    
    import threading
    import time
    
    ondevice_result = None
    cloud_result = None
    ondevice_time = None
    cloud_time = None
    ondevice_error = None
    cloud_error = None
    
    def run_ondevice():
        nonlocal ondevice_result, ondevice_time, ondevice_error
        start = time.time()
        try:
            # Run on-device search (use existing logic from lines 4314-4415)
            combined_results = self._search_both_collections(...)
            # Format as SearchResponse
            ondevice_result = SearchResponse(...)
            ondevice_time = (time.time() - start) * 1000
            logger.info(f"✅ On-device search completed in {ondevice_time:.1f}ms")
        except Exception as e:
            ondevice_error = e
            logger.warning(f"❌ On-device search failed: {e}")
    
    def run_cloud():
        nonlocal cloud_result, cloud_time, cloud_error
        start = time.time()
        try:
            # Run cloud search (use existing logic from lines 4422-4445)
            cloud_result = self._post("/v1/memory/search", ...)
            cloud_time = (time.time() - start) * 1000
            logger.info(f"✅ Cloud search completed in {cloud_time:.1f}ms")
        except Exception as e:
            cloud_error = e
            logger.warning(f"❌ Cloud search failed: {e}")
    
    # Launch both threads
    ondevice_thread = threading.Thread(target=run_ondevice)
    cloud_thread = threading.Thread(target=run_cloud)
    
    ondevice_thread.start()
    cloud_thread.start()
    
    # Wait for both to complete
    ondevice_thread.join()
    cloud_thread.join()
    
    # Decision logic
    if ondevice_result and not ondevice_error:
        # Extract combined_results from ondevice search
        combined_results = [(mem.content, 1.0 - getattr(mem, 'similarity_score', 0.0), mem.type) 
                           for mem in ondevice_result.data.memories]
        max_similarity = self._get_max_similarity(combined_results)
        
        if max_similarity < similarity_threshold:
            logger.info(f"⚠️  On-device similarity too low ({max_similarity:.3f} < {similarity_threshold}) - using cloud results")
            return cloud_result if cloud_result else ondevice_result
        
        logger.info(f"✅ Using on-device results (similarity={max_similarity:.3f}, time={ondevice_time:.1f}ms)")
        return ondevice_result
    
    # Fallback to cloud
    if cloud_result and not cloud_error:
        logger.info(f"✅ Using cloud results (on-device failed, time={cloud_time:.1f}ms)")
        return cloud_result
    
    # Both failed - raise error
    logger.error("❌ Both on-device and cloud search failed")
    if cloud_error:
        raise cloud_error
    if ondevice_error:
        raise ondevice_error

# Continue to cloud API call (for non-parallel paths)
extra_headers = {**strip_not_given({"Accept-Encoding": accept_encoding}), **(extra_headers or {})}
return self._post("/v1/memory/search", ...)
```

---

## 🎯 Remaining Tasks

1. **Refactor search() method** (~lines 4300-4445)
   - Add configuration checks (agentic, parallel, threshold)
   - Implement parallel threading logic
   - Add decision logic for result selection
   - Maintain backwards compatibility

2. **Testing**
   - Test with `PAPR_ENABLE_PARALLEL_SEARCH=true`
   - Test with `PAPR_ONDEVICE_SIMILARITY_THRESHOLD=0.80`
   - Test with `enable_agentic_graph=true` (should use cloud only)
   - Test fallback scenarios (on-device fails, cloud fails, both fail)

3. **Documentation**
   - Update `IMPLEMENTATION_PLAN_USER_CONTEXT.md`
   - Create parallel search usage guide
   - Add examples to README

---

## 📊 Implementation Progress

- User Context: 100% ✅
- Server Embeddings: 100% ✅  
- Helper Methods: 33% ⏳
- Parallel Search: 10% ⏳

**Overall**: ~70% complete

---

## 🚧 Blocking Issues

**None** - Implementation can proceed

---

## 💡 Key Design Decisions

1. **Agentic graph always uses cloud** - Agentic search requires server-side graph traversal
2. **Parallel is opt-in** - Default behavior preserved for backwards compatibility
3. **Similarity threshold is configurable** - Allow developers to tune quality vs speed tradeoff
4. **Both searches run to completion** - Don't cancel cloud if on-device finishes first (simplifies threading)

---

## 🔄 Next Steps

1. **Complete parallel search implementation** in `search()` method
2. **Test end-to-end** with voice_server
3. **Update documentation** with examples
4. **Create migration guide** for existing users

---

**Status**: Ready for final implementation  
**File**: `src/papr_memory/resources/memory.py` lines 4300-4445  
**Est. Time**: 30-60 minutes for implementation + testing

