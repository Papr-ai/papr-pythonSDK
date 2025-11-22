# Implementation Plan: User Context & Parallel Search

**Date**: November 22, 2025  
**Status**: 🚧 In Progress  

---

## ✅ Completed

### 1. Pydantic Types
- ✅ Created `src/papr_memory/types/sync_tiers_request.py`
- ✅ Created `src/papr_memory/types/sync_tiers_response.py`
- ✅ Updated `src/papr_memory/types/__init__.py` to export new types

### 2. Environment Variables
- ✅ Updated `ENV_VARIABLES.md` with new configuration options:
  - `PAPR_INCLUDE_SERVER_EMBEDDINGS=true` (default)
  - `PAPR_EMBED_LIMIT=200`
  - `PAPR_EMBED_MODEL=Qwen4B`
  - `PAPR_ONDEVICE_SIMILARITY_THRESHOLD=0.80`
  - `PAPR_ENABLE_PARALLEL_SEARCH=true`
  - `PAPR_USER_ID` (optional)
  - `PAPR_EXTERNAL_USER_ID` (optional)

### 3. Client Initialization
- ✅ Updated `Papr` client to accept `user_id` and `external_user_id`
- ✅ Added environment variable inference for user context
- ✅ Updated `memory.MemoryResource` initialization to receive user context

---

## 🚧 TODO: Critical Implementation

### 1. MemoryResource `__init__` (memory.py ~line 76)

**Add user context storage**:
```python
class MemoryResource(SyncAPIResource):
    def __init__(
        self,
        client: SyncAPIResource,
        user_id: Optional[str] = None,
        external_user_id: Optional[str] = None
    ):
        super().__init__(client)
        self._user_id = user_id
        self._external_user_id = external_user_id
        self._user_context_version = 0  # Track changes
```

### 2. User Context Management Methods (memory.py ~after line 95)

```python
def set_user_context(
    self,
    user_id: Optional[str] = None,
    external_user_id: Optional[str] = None,
    resync: bool = True,
    clear_cache: bool = True
) -> None:
    """Set or update user context and optionally re-fetch memories"""
    # Implementation: see design doc

def clear_user_context(self, clear_cache: bool = True) -> None:
    """Clear user context (e.g., on logout)"""
    # Implementation: see design doc

def _clear_chromadb_collections(self) -> None:
    """Clear both tier0 and tier1 ChromaDB collections"""
    # Implementation: see design doc
```

### 3. Refactor `_sync_tiers_data()` (memory.py ~line 500-700)

**Use Pydantic types and request server embeddings**:
```python
def _sync_tiers_data(self) -> tuple[list[dict], list[dict]]:
    """Fetch tiers using Pydantic types with user context and server embeddings"""
    import os
    from papr_memory.types.sync_tiers_request import SyncTiersRequest
    from papr_memory.types.sync_tiers_response import SyncTiersResponse
    from papr_memory._logging import get_logger
    
    logger = get_logger(__name__)
    
    # Build request with user context and server embeddings
    request = SyncTiersRequest(
        max_tier0=int(os.environ.get("PAPR_MAX_TIER0", "300")),
        max_tier1=int(os.environ.get("PAPR_MAX_TIER1", "1000")),
        include_embeddings=os.environ.get("PAPR_INCLUDE_SERVER_EMBEDDINGS", "true").lower() == "true",
        embed_limit=int(os.environ.get("PAPR_EMBED_LIMIT", "200")),
        embed_model=os.environ.get("PAPR_EMBED_MODEL", "Qwen4B"),
        user_id=self._user_id,
        external_user_id=self._external_user_id,
    )
    
    logger.info(f"🔒 Fetching tiers for user: {self._user_id or self._external_user_id or 'ALL'}")
    logger.info(f"📊 Request: max_tier0={request.max_tier0}, max_tier1={request.max_tier1}, include_embeddings={request.include_embeddings}, embed_limit={request.embed_limit}")
    
    response = self._post(
        "/v1/sync/tiers",
        body=request.model_dump(exclude_none=True),
        cast_to=SyncTiersResponse,
    )
    
    # Convert Memory objects to dicts
    tier0 = [item.model_dump() for item in response.tier0]
    tier1 = [item.model_dump() for item in response.tier1]
    
    logger.info(f"✅ Received {len(tier0)} tier0, {len(tier1)} tier1 items")
    if request.include_embeddings:
        tier0_with_emb = sum(1 for item in tier0 if item.get("embedding"))
        tier1_with_emb = sum(1 for item in tier1 if item.get("embedding"))
        logger.info(f"📊 Server embeddings: tier0={tier0_with_emb}/{len(tier0)}, tier1={tier1_with_emb}/{len(tier1)}")
    
    return tier0, tier1
```

### 4. Parallel Search Implementation (memory.py `search()` method ~line 4150)

**Replace synchronous on-device search with parallel on-device + cloud**:

```python
def search(self, *, query: str, ...) -> SearchResponse:
    import os
    import threading
    import time
    from papr_memory._logging import get_logger
    
    logger = get_logger(__name__)
    
    ondevice_processing = os.environ.get("PAPR_ONDEVICE_PROCESSING", "false").lower() in ("true", "1", "yes", "on")
    enable_parallel = os.environ.get("PAPR_ENABLE_PARALLEL_SEARCH", "true").lower() in ("true", "1", "yes", "on")
    similarity_threshold = float(os.environ.get("PAPR_ONDEVICE_SIMILARITY_THRESHOLD", "0.80"))
    enable_agentic_graph = enable_agentic_graph if enable_agentic_graph is not omit else False
    
    # If agentic graph is enabled, always use cloud
    if enable_agentic_graph:
        logger.info("🌐 Agentic graph enabled - using cloud search")
        return self._cloud_search(query, ...)
    
    # If on-device not enabled, use cloud
    if not ondevice_processing:
        return self._cloud_search(query, ...)
    
    # If parallel search not enabled, use on-device only
    if not enable_parallel:
        logger.info("🔍 On-device search only (parallel disabled)")
        ondevice_results = self._ondevice_search(query, ...)
        return self._format_search_response(ondevice_results, source="on-device")
    
    # PARALLEL SEARCH: Run on-device and cloud simultaneously
    logger.info("⚡ Starting parallel search (on-device + cloud)")
    
    ondevice_results = None
    cloud_results = None
    ondevice_time = None
    cloud_time = None
    ondevice_error = None
    cloud_error = None
    
    def run_ondevice():
        nonlocal ondevice_results, ondevice_time, ondevice_error
        start = time.time()
        try:
            ondevice_results = self._ondevice_search(query, ...)
            ondevice_time = (time.time() - start) * 1000
            logger.info(f"✅ On-device search completed in {ondevice_time:.1f}ms")
        except Exception as e:
            ondevice_error = e
            logger.warning(f"❌ On-device search failed: {e}")
    
    def run_cloud():
        nonlocal cloud_results, cloud_time, cloud_error
        start = time.time()
        try:
            cloud_results = self._cloud_search(query, ...)
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
    if ondevice_results and not ondevice_error:
        # Check similarity threshold
        max_similarity = self._get_max_similarity(ondevice_results)
        
        if max_similarity < similarity_threshold:
            logger.info(f"⚠️  On-device similarity too low ({max_similarity:.3f} < {similarity_threshold}) - using cloud results")
            return cloud_results if cloud_results else ondevice_results
        
        # On-device results are good
        logger.info(f"✅ Using on-device results (similarity={max_similarity:.3f}, time={ondevice_time:.1f}ms)")
        return ondevice_results
    
    # Fallback to cloud
    if cloud_results and not cloud_error:
        logger.info(f"✅ Using cloud results (on-device failed, time={cloud_time:.1f}ms)")
        return cloud_results
    
    # Both failed
    logger.error("❌ Both on-device and cloud search failed")
    if cloud_error:
        raise cloud_error
    if ondevice_error:
        raise ondevice_error

def _ondevice_search(self, query: str, ...) -> SearchResponse:
    """On-device search using _search_both_collections()"""
    combined_results = self._search_both_collections(query, ...)
    # Format as SearchResponse
    return self._format_search_response(combined_results, source="on-device")

def _cloud_search(self, query: str, ...) -> SearchResponse:
    """Cloud search using API"""
    return self._post("/v1/memory/search", ...)

def _get_max_similarity(self, results: list) -> float:
    """Get maximum similarity score from results"""
    if not results:
        return 0.0
    # Extract similarity from results
    similarities = [1.0 - result[1] for result in results]  # Convert distance to similarity
    return max(similarities) if similarities else 0.0
```

---

## 📊 Implementation Progress

### High Priority (Must Have)
- [ ] MemoryResource `__init__` with user context
- [ ] `set_user_context()` method
- [ ] `clear_user_context()` method
- [ ] `_clear_chromadb_collections()` method
- [ ] Refactor `_sync_tiers_data()` to use Pydantic types
- [ ] Request server embeddings with `include_embeddings=True`
- [ ] Parallel search implementation (`_ondevice_search()` + `_cloud_search()`)
- [ ] Similarity threshold logic

### Medium Priority (Should Have)
- [ ] Update AsyncMemoryResource with user context
- [ ] Update AsyncPapr client with user context
- [ ] Add comprehensive logging for parallel search
- [ ] Add metrics tracking (on-device vs cloud usage)

### Low Priority (Nice to Have)
- [ ] Cache recent queries to avoid duplicate searches
- [ ] Configurable timeout for on-device search
- [ ] Fallback to cloud if on-device takes too long
- [ ] A/B testing framework for parallel search

---

## 🧪 Testing Plan

### 1. User Context Management
```bash
python -c "
from papr_memory import PaprMemory
client = PaprMemory(api_key='...', user_id='user_123')
# Verify user_id is used in sync_tiers
"
```

### 2. Server Embeddings
```bash
export PAPR_INCLUDE_SERVER_EMBEDDINGS=true
export PAPR_EMBED_LIMIT=50
# Run voice_server and check logs for server embeddings
```

### 3. Parallel Search
```bash
export PAPR_ENABLE_PARALLEL_SEARCH=true
export PAPR_ONDEVICE_SIMILARITY_THRESHOLD=0.80
# Perform searches and verify parallel execution
```

---

## 📝 Files to Modify

1. ✅ `src/papr_memory/types/sync_tiers_request.py` - CREATED
2. ✅ `src/papr_memory/types/sync_tiers_response.py` - CREATED
3. ✅ `src/papr_memory/types/__init__.py` - UPDATED
4. ✅ `src/papr_memory/_client.py` - UPDATED (Papr class)
5. ⏳ `src/papr_memory/_client.py` - TODO (AsyncPapr class)
6. ⏳ `src/papr_memory/resources/memory.py` - TODO (MemoryResource class)
7. ⏳ `src/papr_memory/resources/memory.py` - TODO (AsyncMemoryResource class)
8. ✅ `ENV_VARIABLES.md` - UPDATED

---

## 🎯 Next Steps

1. **Implement MemoryResource updates** in `memory.py`:
   - Add `__init__` with user context
   - Add user context management methods
   - Refactor `_sync_tiers_data()`
   - Implement parallel search logic

2. **Test implementation**:
   - Unit tests for user context
   - Integration tests for parallel search
   - End-to-end tests with voice_server

3. **Documentation**:
   - Update README with user context examples
   - Add parallel search guide
   - Create troubleshooting section

---

**Status**: Ready to implement memory.py changes  
**Est. Time**: 2-3 hours for core implementation + testing

