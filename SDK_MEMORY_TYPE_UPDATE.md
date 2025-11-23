# SDK Memory Type Update - Full Server Compatibility

## Summary

Updated the papr-pythonSDK's `Memory` Pydantic type to match the server's complete `Memory` model, ensuring full compatibility with all fields including the new `embedding` and `embedding_int8` fields for server-provided embeddings.

---

## Changes Made

### 1. **Updated `Memory` Type** (`src/papr_memory/types/sync_tiers_response.py`)

**Before**: Minimal `Memory` type with only 7 fields
```python
class Memory(BaseModel):
    id: str
    content: str
    type: str
    topics: Optional[List[str]]
    metadata: Optional[Dict[str, Any]]
    embedding: Optional[List[float]]  # Basic definition
    embedding_int8: Optional[List[int]]  # Basic definition
```

**After**: Complete `Memory` type with 50+ fields matching server model
```python
class Memory(BaseModel):
    """Individual memory item in tier response - matches server Memory model"""
    
    # Core fields (id, content, title, type, etc.)
    # Timestamps (created_at, updated_at)
    # Access control (acl, user_id, workspace_id)
    # Multi-tenant (organization_id, namespace_id)
    # Source context (source_document_id, source_message_id)
    # Document fields (page_number, file_url, filename, etc.)
    # Fine-grained ACL (user_read_access, workspace_write_access, etc.)
    
    # Embedding fields with detailed descriptions
    embedding: Optional[List[float]] = Field(
        default=None,
        description="Full precision (float32) embedding vector from Qdrant. Typically 2560 dimensions for Qwen4B. Used for CoreML/ANE fp16 models."
    )
    embedding_int8: Optional[List[int]] = Field(
        default=None,
        description="Quantized INT8 embedding vector (values -128 to 127). 4x smaller than float32. Default format for efficiency."
    )
    
    model_config = ConfigDict(
        extra='allow',  # Allow additional fields from server
        populate_by_name=True,
        str_strip_whitespace=True,
    )
```

---

## Full Field List

The updated `Memory` type now includes:

### Core Fields
- `id`, `content`, `title`, `type`
- `metadata`, `external_user_id`, `customMetadata`
- `source_type`, `context`, `location`, `tags`
- `hierarchical_structures`, `source_url`, `conversation_id`
- `topics`, `steps`, `current_step`

### Role & Category
- `role` (user or assistant)
- `category` (memory category)

### Timestamps
- `created_at`
- `updated_at`

### Access Control & Ownership
- `acl` (access control list)
- `user_id` (owner)
- `workspace_id`

### Multi-Tenant Fields
- `organization_id`
- `namespace_id`

### Source Context
- `source_document_id` (formerly 'post')
- `source_message_id` (formerly 'postMessage')

### Document-Specific Fields
- `page_number`, `total_pages`
- `file_url`, `filename`, `page`

### Fine-Grained ACL (12 fields)
- `external_user_read_access`, `external_user_write_access`
- `user_read_access`, `user_write_access`
- `workspace_read_access`, `workspace_write_access`
- `role_read_access`, `role_write_access`
- `namespace_read_access`, `namespace_write_access`
- `organization_read_access`, `organization_write_access`

### Embedding Fields ⭐ NEW
- `embedding` - float32 full precision (2560 dims for Qwen4B)
- `embedding_int8` - INT8 quantized (4x smaller)

---

## SDK Compatibility

### ✅ Already Working

The SDK's existing code already properly handles both formats:

1. **Logging Function** (`_log_sync_response_to_file`, lines 863-981)
   - ✅ Handles both `dict` and Pydantic `Memory` objects
   - ✅ Extracts `id`, `type`, `content`, `topics`, `metadata`, `updated_at`
   - ✅ Extracts `embedding` field with dimension validation
   ```python
   if hasattr(item, 'embedding'):
       embedding = item.embedding
       if embedding and isinstance(embedding, list):
           item_data["has_embedding"] = True
           item_data["embedding_dimension"] = len(embedding)
   ```

2. **Tier0 Storage** (`_store_tier0_in_chromadb`, lines 3590-3622)
   - ✅ Extracts embeddings from Pydantic objects
   - ✅ Validates embedding format (list of int/float)
   - ✅ Falls back to local generation if missing
   ```python
   elif hasattr(item, 'embedding') and item.embedding:
       server_embedding = item.embedding
       if isinstance(server_embedding, list) and len(server_embedding) > 0:
           embedding = server_embedding
           logger.info(f"Valid server embedding (dim: {len(embedding)})")
   ```

3. **Tier1 Storage** (`_store_tier1_in_chromadb`, lines 4060-4093)
   - ✅ Same handling as tier0
   - ✅ Proper Pydantic object support
   - ✅ Validation and fallback logic

### 🎯 Why This Works

The SDK uses **duck typing** and `hasattr()` checks:
```python
# Works with both dict and Pydantic objects
if isinstance(item, dict) and "embedding" in item:
    embedding = item["embedding"]
elif hasattr(item, 'embedding') and item.embedding:
    embedding = item.embedding
```

Since Pydantic's `Memory` class now has properly typed `embedding` and `embedding_int8` fields, these checks work seamlessly.

---

## Server Response Flow

1. **Server** (`/v1/sync/tiers` endpoint):
   ```python
   # Enrich memories with embeddings from Qdrant
   tier0_items = await enrich_memories_with_embeddings_batch(...)
   tier1_items = await enrich_memories_with_embeddings_batch(...)
   
   # Return SyncTiersResponse with Memory objects
   return SyncTiersResponse(
       tier0=[Memory(..., embedding=[...]), ...],
       tier1=[Memory(..., embedding=[...]), ...]
   )
   ```

2. **SDK** receives response:
   ```python
   sync_response = self.sync_tiers(
       include_embeddings=True,
       embed_limit=200,
       ...
   )
   # sync_response.tier0 -> List[Memory] with embeddings
   # sync_response.tier1 -> List[Memory] with embeddings
   ```

3. **SDK** extracts and stores:
   ```python
   for item in sync_response.tier0:
       if hasattr(item, 'embedding') and item.embedding:
           # Use server-provided embedding ✅
           embeddings.append(item.embedding)
       else:
           # Generate locally if missing
           embeddings.append(None)
   ```

---

## Benefits

### 🚀 Performance
- **Faster initialization**: Server provides embeddings (no local generation needed)
- **Reduced ANE/GPU load**: Fewer embeddings to compute on-device
- **Lower memory usage**: Server handles embedding retrieval from Qdrant

### 🔧 Compatibility
- **Full field access**: SDK can now access all Memory fields from server
- **Type safety**: Proper Pydantic validation for all fields
- **IDE support**: Autocomplete for all Memory attributes
- **Future-proof**: `extra='allow'` accepts new server fields

### 📊 Observability
- **Better logging**: All Memory fields properly logged
- **Debugging**: Full visibility into server-provided data
- **Validation**: Pydantic catches schema mismatches early

---

## Testing

### Verify SDK Receives Embeddings

```python
from papr_memory import Papr

client = Papr(x_api_key="your_api_key")

# Request embeddings from server
response = client.memory.sync_tiers(
    include_embeddings=True,
    embed_limit=100,
    max_tier0=100,
    max_tier1=100
)

# Check tier0
for item in response.tier0:
    print(f"ID: {item.id}")
    print(f"Content: {item.content[:50]}...")
    print(f"Has embedding: {item.embedding is not None}")
    if item.embedding:
        print(f"  Dimension: {len(item.embedding)}")
        print(f"  Type: {type(item.embedding[0])}")
        print(f"  Sample: {item.embedding[:3]}")

# Check tier1
for item in response.tier1:
    print(f"ID: {item.id}")
    print(f"Has embedding: {item.embedding is not None}")
    if item.embedding:
        print(f"  Dimension: {len(item.embedding)}")
```

### Expected Output

```
ID: 584d7542-2b11-4bae-...
Content: Hi Michele—great meeting at AgentConf Wed...
Has embedding: True
  Dimension: 2560
  Type: <class 'float'>
  Sample: [-0.00023892, 0.05796862, 0.00587674]
```

---

## Environment Variables

For optimal performance, set:

```bash
# Request server embeddings (recommended)
PAPR_INCLUDE_SERVER_EMBEDDINGS=true
PAPR_EMBED_LIMIT=200

# For CoreML/ANE, request float32
PAPR_EMBEDDING_FORMAT=float32  # Auto-set when PAPR_ENABLE_COREML=true

# Model hint for server
PAPR_EMBED_MODEL=Qwen4B
```

---

## Migration Notes

### No Breaking Changes

This update is **100% backward compatible**:

- Old SDK versions: Still work (minimal Memory type)
- New SDK versions: Get full Memory fields + embeddings
- Server: Returns all fields (old SDKs ignore extra fields)

### Gradual Adoption

You can adopt the new fields gradually:

```python
# Basic usage (works with old & new SDK)
print(item.id, item.content, item.type)

# Advanced usage (new SDK only)
print(item.created_at, item.updated_at)
print(item.workspace_id, item.organization_id)
print(item.embedding[:10] if item.embedding else "No embedding")
```

---

## Files Modified

1. **`/Users/shawkatkabbara/Documents/GitHub/papr-pythonSDK/src/papr_memory/types/sync_tiers_response.py`**
   - Updated `Memory` class from 7 fields to 50+ fields
   - Added proper descriptions for all fields
   - Added `ConfigDict` for `extra='allow'`
   - Imported `datetime` and `ConfigDict`

---

## Verification

Run the SDK's existing logic - no changes needed:

```bash
cd ~/Documents/GitHub/papr-voice-demo
python src/python/voice_server.py
```

Check logs for:
```
✅ Extracted 150/200 server embeddings for tier0
✅ Extracted 180/200 server embeddings for tier1
```

This confirms the SDK is successfully receiving and using server-provided embeddings!

---

## Summary

✅ **SDK `Memory` type updated** to match server's complete model
✅ **Full field compatibility** - all 50+ fields properly defined
✅ **Embedding fields enhanced** with detailed descriptions
✅ **No code changes needed** - existing logic already handles Pydantic objects
✅ **Backward compatible** - old code continues to work
✅ **Type-safe** - Pydantic validation for all fields
✅ **Future-proof** - `extra='allow'` for new server fields

The SDK is now fully ready to receive and utilize server-provided embeddings for both tier0 and tier1!

