# Shared Types

```python
from papr_memory.types import (
    ACLConfig,
    AddMemoryItem,
    EdgeConstraintInput,
    Memory,
    MemoryPolicy,
    NodeConstraintInput,
    NodeSpec,
    PropertyValue,
    RelationshipSpec,
    SearchConfigInput,
)
```

# User

Types:

```python
from papr_memory.types import (
    UserResponse,
    UserType,
    UserListResponse,
    UserDeleteResponse,
    UserCreateBatchResponse,
)
```

Methods:

- <code title="post /v1/user">client.user.<a href="./src/papr_memory/resources/user.py">create</a>(\*\*<a href="src/papr_memory/types/user_create_params.py">params</a>) -> <a href="./src/papr_memory/types/user_response.py">UserResponse</a></code>
- <code title="put /v1/user/{user_id}">client.user.<a href="./src/papr_memory/resources/user.py">update</a>(user_id, \*\*<a href="src/papr_memory/types/user_update_params.py">params</a>) -> <a href="./src/papr_memory/types/user_response.py">UserResponse</a></code>
- <code title="get /v1/user">client.user.<a href="./src/papr_memory/resources/user.py">list</a>(\*\*<a href="src/papr_memory/types/user_list_params.py">params</a>) -> <a href="./src/papr_memory/types/user_list_response.py">UserListResponse</a></code>
- <code title="delete /v1/user/{user_id}">client.user.<a href="./src/papr_memory/resources/user.py">delete</a>(user_id, \*\*<a href="src/papr_memory/types/user_delete_params.py">params</a>) -> <a href="./src/papr_memory/types/user_delete_response.py">UserDeleteResponse</a></code>
- <code title="post /v1/user/batch">client.user.<a href="./src/papr_memory/resources/user.py">create_batch</a>(\*\*<a href="src/papr_memory/types/user_create_batch_params.py">params</a>) -> <a href="./src/papr_memory/types/user_create_batch_response.py">UserCreateBatchResponse</a></code>
- <code title="get /v1/user/{user_id}">client.user.<a href="./src/papr_memory/resources/user.py">get</a>(user_id) -> <a href="./src/papr_memory/types/user_response.py">UserResponse</a></code>

# Memory

Types:

```python
from papr_memory.types import (
    AddMemory,
    AddMemoryResponse,
    AutoGraphGeneration,
    BatchMemoryError,
    BatchMemoryResponse,
    ContextItem,
    GraphGeneration,
    HTTPValidationError,
    ManualGraphGeneration,
    MemoryMetadata,
    MemoryType,
    RelationshipItem,
    SearchResponse,
    SearchResult,
    MemoryUpdateResponse,
    MemoryDeleteResponse,
    MemoryRetrieveBatchStatusResponse,
    MemoryRetrieveStatusResponse,
)
```

Methods:

- <code title="put /v1/memory/{memory_id}">client.memory.<a href="./src/papr_memory/resources/memory.py">update</a>(memory_id, \*\*<a href="src/papr_memory/types/memory_update_params.py">params</a>) -> <a href="./src/papr_memory/types/memory_update_response.py">MemoryUpdateResponse</a></code>
- <code title="delete /v1/memory/{memory_id}">client.memory.<a href="./src/papr_memory/resources/memory.py">delete</a>(memory_id, \*\*<a href="src/papr_memory/types/memory_delete_params.py">params</a>) -> <a href="./src/papr_memory/types/memory_delete_response.py">MemoryDeleteResponse</a></code>
- <code title="post /v1/memory">client.memory.<a href="./src/papr_memory/resources/memory.py">add</a>(\*\*<a href="src/papr_memory/types/memory_add_params.py">params</a>) -> <a href="./src/papr_memory/types/add_memory_response.py">AddMemoryResponse</a></code>
- <code title="post /v1/memory/batch">client.memory.<a href="./src/papr_memory/resources/memory.py">add_batch</a>(\*\*<a href="src/papr_memory/types/memory_add_batch_params.py">params</a>) -> <a href="./src/papr_memory/types/batch_memory_response.py">BatchMemoryResponse</a></code>
- <code title="delete /v1/memory/all">client.memory.<a href="./src/papr_memory/resources/memory.py">delete_all</a>(\*\*<a href="src/papr_memory/types/memory_delete_all_params.py">params</a>) -> <a href="./src/papr_memory/types/batch_memory_response.py">BatchMemoryResponse</a></code>
- <code title="get /v1/memory/{memory_id}">client.memory.<a href="./src/papr_memory/resources/memory.py">get</a>(memory_id, \*\*<a href="src/papr_memory/types/memory_get_params.py">params</a>) -> <a href="./src/papr_memory/types/search_response.py">SearchResponse</a></code>
- <code title="get /v1/memory/batch/status/{batch_id}">client.memory.<a href="./src/papr_memory/resources/memory.py">retrieve_batch_status</a>(batch_id) -> <a href="./src/papr_memory/types/memory_retrieve_batch_status_response.py">MemoryRetrieveBatchStatusResponse</a></code>
- <code title="get /v1/memory/status/{memory_id}">client.memory.<a href="./src/papr_memory/resources/memory.py">retrieve_status</a>(memory_id) -> <a href="./src/papr_memory/types/memory_retrieve_status_response.py">MemoryRetrieveStatusResponse</a></code>
- <code title="post /v1/memory/search">client.memory.<a href="./src/papr_memory/resources/memory.py">search</a>(\*\*<a href="src/papr_memory/types/memory_search_params.py">params</a>) -> <a href="./src/papr_memory/types/search_response.py">SearchResponse</a></code>

# Feedback

Types:

```python
from papr_memory.types import (
    BatchRequest,
    BatchResponse,
    FeedbackRequest,
    FeedbackResponse,
    ParsePointer,
)
```

Methods:

- <code title="get /v1/feedback/{feedback_id}">client.feedback.<a href="./src/papr_memory/resources/feedback.py">get_by_id</a>(feedback_id) -> <a href="./src/papr_memory/types/feedback_response.py">FeedbackResponse</a></code>
- <code title="post /v1/feedback">client.feedback.<a href="./src/papr_memory/resources/feedback.py">submit</a>(\*\*<a href="src/papr_memory/types/feedback_submit_params.py">params</a>) -> <a href="./src/papr_memory/types/feedback_response.py">FeedbackResponse</a></code>
- <code title="post /v1/feedback/batch">client.feedback.<a href="./src/papr_memory/resources/feedback.py">submit_batch</a>(\*\*<a href="src/papr_memory/types/feedback_submit_batch_params.py">params</a>) -> <a href="./src/papr_memory/types/batch_response.py">BatchResponse</a></code>

# Document

Types:

```python
from papr_memory.types import (
    DocumentCancelProcessingResponse,
    DocumentGetStatusResponse,
    DocumentUploadResponse,
)
```

Methods:

- <code title="delete /v1/document/{upload_id}">client.document.<a href="./src/papr_memory/resources/document.py">cancel_processing</a>(upload_id) -> <a href="./src/papr_memory/types/document_cancel_processing_response.py">DocumentCancelProcessingResponse</a></code>
- <code title="get /v1/document/status/{upload_id}">client.document.<a href="./src/papr_memory/resources/document.py">get_status</a>(upload_id) -> <a href="./src/papr_memory/types/document_get_status_response.py">DocumentGetStatusResponse</a></code>
- <code title="post /v1/document">client.document.<a href="./src/papr_memory/resources/document.py">upload</a>(\*\*<a href="src/papr_memory/types/document_upload_params.py">params</a>) -> <a href="./src/papr_memory/types/document_upload_response.py">DocumentUploadResponse</a></code>

# Schemas

Types:

```python
from papr_memory.types import (
    PropertyDefinition,
    SearchConfigOutput,
    UserGraphSchemaOutput,
    SchemaCreateResponse,
    SchemaRetrieveResponse,
    SchemaUpdateResponse,
    SchemaListResponse,
)
```

Methods:

- <code title="post /v1/schemas">client.schemas.<a href="./src/papr_memory/resources/schemas.py">create</a>(\*\*<a href="src/papr_memory/types/schema_create_params.py">params</a>) -> <a href="./src/papr_memory/types/schema_create_response.py">SchemaCreateResponse</a></code>
- <code title="get /v1/schemas/{schema_id}">client.schemas.<a href="./src/papr_memory/resources/schemas.py">retrieve</a>(schema_id) -> <a href="./src/papr_memory/types/schema_retrieve_response.py">SchemaRetrieveResponse</a></code>
- <code title="put /v1/schemas/{schema_id}">client.schemas.<a href="./src/papr_memory/resources/schemas.py">update</a>(schema_id, \*\*<a href="src/papr_memory/types/schema_update_params.py">params</a>) -> <a href="./src/papr_memory/types/schema_update_response.py">SchemaUpdateResponse</a></code>
- <code title="get /v1/schemas">client.schemas.<a href="./src/papr_memory/resources/schemas.py">list</a>(\*\*<a href="src/papr_memory/types/schema_list_params.py">params</a>) -> <a href="./src/papr_memory/types/schema_list_response.py">SchemaListResponse</a></code>
- <code title="delete /v1/schemas/{schema_id}">client.schemas.<a href="./src/papr_memory/resources/schemas.py">delete</a>(schema_id) -> object</code>

# Graphql

Methods:

- <code title="get /v1/graphql">client.graphql.<a href="./src/papr_memory/resources/graphql.py">playground</a>() -> object</code>
- <code title="post /v1/graphql">client.graphql.<a href="./src/papr_memory/resources/graphql.py">query</a>() -> object</code>

# Messages

Types:

```python
from papr_memory.types import MessageStoreResponse
```

Methods:

- <code title="post /v1/messages">client.messages.<a href="./src/papr_memory/resources/messages/messages.py">store</a>(\*\*<a href="src/papr_memory/types/message_store_params.py">params</a>) -> <a href="./src/papr_memory/types/message_store_response.py">MessageStoreResponse</a></code>

## Sessions

Types:

```python
from papr_memory.types.messages import (
    ConversationSummaryResponse,
    SessionCompressResponse,
    SessionRetrieveHistoryResponse,
)
```

Methods:

- <code title="patch /v1/messages/sessions/{session_id}">client.messages.sessions.<a href="./src/papr_memory/resources/messages/sessions.py">update</a>(session_id, \*\*<a href="src/papr_memory/types/messages/session_update_params.py">params</a>) -> object</code>
- <code title="get /v1/messages/sessions/{session_id}/compress">client.messages.sessions.<a href="./src/papr_memory/resources/messages/sessions.py">compress</a>(session_id) -> <a href="./src/papr_memory/types/messages/session_compress_response.py">SessionCompressResponse</a></code>
- <code title="post /v1/messages/sessions/{session_id}/process">client.messages.sessions.<a href="./src/papr_memory/resources/messages/sessions.py">process</a>(session_id) -> object</code>
- <code title="get /v1/messages/sessions/{session_id}">client.messages.sessions.<a href="./src/papr_memory/resources/messages/sessions.py">retrieve_history</a>(session_id, \*\*<a href="src/papr_memory/types/messages/session_retrieve_history_params.py">params</a>) -> <a href="./src/papr_memory/types/messages/session_retrieve_history_response.py">SessionRetrieveHistoryResponse</a></code>
- <code title="get /v1/messages/sessions/{session_id}/status">client.messages.sessions.<a href="./src/papr_memory/resources/messages/sessions.py">retrieve_status</a>(session_id) -> object</code>

# Omo

Types:

```python
from papr_memory.types import OmoExportMemoriesResponse, OmoImportMemoriesResponse
```

Methods:

- <code title="post /v1/omo/export">client.omo.<a href="./src/papr_memory/resources/omo.py">export_memories</a>(\*\*<a href="src/papr_memory/types/omo_export_memories_params.py">params</a>) -> <a href="./src/papr_memory/types/omo_export_memories_response.py">OmoExportMemoriesResponse</a></code>
- <code title="get /v1/omo/export.json">client.omo.<a href="./src/papr_memory/resources/omo.py">export_memories_as_json</a>(\*\*<a href="src/papr_memory/types/omo_export_memories_as_json_params.py">params</a>) -> object</code>
- <code title="post /v1/omo/import">client.omo.<a href="./src/papr_memory/resources/omo.py">import_memories</a>(\*\*<a href="src/papr_memory/types/omo_import_memories_params.py">params</a>) -> <a href="./src/papr_memory/types/omo_import_memories_response.py">OmoImportMemoriesResponse</a></code>

# Sync

Types:

```python
from papr_memory.types import SyncGetDeltaResponse, SyncGetTiersResponse
```

Methods:

- <code title="get /v1/sync/delta">client.sync.<a href="./src/papr_memory/resources/sync.py">get_delta</a>(\*\*<a href="src/papr_memory/types/sync_get_delta_params.py">params</a>) -> <a href="./src/papr_memory/types/sync_get_delta_response.py">SyncGetDeltaResponse</a></code>
- <code title="post /v1/sync/tiers">client.sync.<a href="./src/papr_memory/resources/sync.py">get_tiers</a>(\*\*<a href="src/papr_memory/types/sync_get_tiers_params.py">params</a>) -> <a href="./src/papr_memory/types/sync_get_tiers_response.py">SyncGetTiersResponse</a></code>

# Namespace

Types:

```python
from papr_memory.types import (
    InstanceConfigItem,
    NamespaceItem,
    Neo4jInstanceConfigItem,
    NamespaceCreateResponse,
    NamespaceRetrieveResponse,
    NamespaceUpdateResponse,
    NamespaceListResponse,
    NamespaceDeleteResponse,
)
```

Methods:

- <code title="post /v1/namespace">client.namespace.<a href="./src/papr_memory/resources/namespace/namespace.py">create</a>(\*\*<a href="src/papr_memory/types/namespace_create_params.py">params</a>) -> <a href="./src/papr_memory/types/namespace_create_response.py">NamespaceCreateResponse</a></code>
- <code title="get /v1/namespace/{namespace_id}">client.namespace.<a href="./src/papr_memory/resources/namespace/namespace.py">retrieve</a>(namespace_id) -> <a href="./src/papr_memory/types/namespace_retrieve_response.py">NamespaceRetrieveResponse</a></code>
- <code title="put /v1/namespace/{namespace_id}">client.namespace.<a href="./src/papr_memory/resources/namespace/namespace.py">update</a>(namespace_id, \*\*<a href="src/papr_memory/types/namespace_update_params.py">params</a>) -> <a href="./src/papr_memory/types/namespace_update_response.py">NamespaceUpdateResponse</a></code>
- <code title="get /v1/namespace">client.namespace.<a href="./src/papr_memory/resources/namespace/namespace.py">list</a>(\*\*<a href="src/papr_memory/types/namespace_list_params.py">params</a>) -> <a href="./src/papr_memory/types/namespace_list_response.py">NamespaceListResponse</a></code>
- <code title="delete /v1/namespace/{namespace_id}">client.namespace.<a href="./src/papr_memory/resources/namespace/namespace.py">delete</a>(namespace_id, \*\*<a href="src/papr_memory/types/namespace_delete_params.py">params</a>) -> <a href="./src/papr_memory/types/namespace_delete_response.py">NamespaceDeleteResponse</a></code>

## Instance

Types:

```python
from papr_memory.types.namespace import (
    InstanceRetrieveResponse,
    InstanceUpdateResponse,
    InstanceDeleteResponse,
)
```

Methods:

- <code title="get /v1/namespace/{namespace_id}/instance">client.namespace.instance.<a href="./src/papr_memory/resources/namespace/instance.py">retrieve</a>(namespace_id) -> <a href="./src/papr_memory/types/namespace/instance_retrieve_response.py">InstanceRetrieveResponse</a></code>
- <code title="put /v1/namespace/{namespace_id}/instance">client.namespace.instance.<a href="./src/papr_memory/resources/namespace/instance.py">update</a>(namespace_id, \*\*<a href="src/papr_memory/types/namespace/instance_update_params.py">params</a>) -> <a href="./src/papr_memory/types/namespace/instance_update_response.py">InstanceUpdateResponse</a></code>
- <code title="delete /v1/namespace/{namespace_id}/instance">client.namespace.instance.<a href="./src/papr_memory/resources/namespace/instance.py">delete</a>(namespace_id) -> <a href="./src/papr_memory/types/namespace/instance_delete_response.py">InstanceDeleteResponse</a></code>

# Frequencies

Types:

```python
from papr_memory.types import (
    FrequencyFieldResponse,
    SchemaConfigResponse,
    FrequencyRetrieveResponse,
    FrequencyListResponse,
)
```

Methods:

- <code title="get /v1/frequencies/{frequency_schema_id}">client.frequencies.<a href="./src/papr_memory/resources/frequencies.py">retrieve</a>(frequency_schema_id) -> <a href="./src/papr_memory/types/frequency_retrieve_response.py">FrequencyRetrieveResponse</a></code>
- <code title="get /v1/frequencies">client.frequencies.<a href="./src/papr_memory/resources/frequencies.py">list</a>() -> <a href="./src/papr_memory/types/frequency_list_response.py">FrequencyListResponse</a></code>

# Holographic

Types:

```python
from papr_memory.types import HolographicExtractMetadataResponse, HolographicRerankResponse
```

Methods:

- <code title="post /v1/holographic/metadata">client.holographic.<a href="./src/papr_memory/resources/holographic/holographic.py">extract_metadata</a>(\*\*<a href="src/papr_memory/types/holographic_extract_metadata_params.py">params</a>) -> <a href="./src/papr_memory/types/holographic_extract_metadata_response.py">HolographicExtractMetadataResponse</a></code>
- <code title="post /v1/holographic/rerank">client.holographic.<a href="./src/papr_memory/resources/holographic/holographic.py">rerank</a>(\*\*<a href="src/papr_memory/types/holographic_rerank_params.py">params</a>) -> <a href="./src/papr_memory/types/holographic_rerank_response.py">HolographicRerankResponse</a></code>

## Transform

Types:

```python
from papr_memory.types.holographic import (
    TransformData,
    TransformCreateResponse,
    TransformCreateBatchResponse,
)
```

Methods:

- <code title="post /v1/holographic/transform">client.holographic.transform.<a href="./src/papr_memory/resources/holographic/transform.py">create</a>(\*\*<a href="src/papr_memory/types/holographic/transform_create_params.py">params</a>) -> <a href="./src/papr_memory/types/holographic/transform_create_response.py">TransformCreateResponse</a></code>
- <code title="post /v1/holographic/transform/batch">client.holographic.transform.<a href="./src/papr_memory/resources/holographic/transform.py">create_batch</a>(\*\*<a href="src/papr_memory/types/holographic/transform_create_batch_params.py">params</a>) -> <a href="./src/papr_memory/types/holographic/transform_create_batch_response.py">TransformCreateBatchResponse</a></code>

## Domains

Types:

```python
from papr_memory.types.holographic import DomainCreateResponse, DomainListResponse
```

Methods:

- <code title="post /v1/holographic/domains">client.holographic.domains.<a href="./src/papr_memory/resources/holographic/domains.py">create</a>(\*\*<a href="src/papr_memory/types/holographic/domain_create_params.py">params</a>) -> <a href="./src/papr_memory/types/holographic/domain_create_response.py">DomainCreateResponse</a></code>
- <code title="get /v1/holographic/domains">client.holographic.domains.<a href="./src/papr_memory/resources/holographic/domains.py">list</a>() -> <a href="./src/papr_memory/types/holographic/domain_list_response.py">DomainListResponse</a></code>

# Organization

## Instance

Types:

```python
from papr_memory.types.organization import (
    InstanceRetrieveResponse,
    InstanceUpdateResponse,
    InstanceDeleteResponse,
)
```

Methods:

- <code title="get /v1/organization/instance">client.organization.instance.<a href="./src/papr_memory/resources/organization/instance.py">retrieve</a>() -> <a href="./src/papr_memory/types/organization/instance_retrieve_response.py">InstanceRetrieveResponse</a></code>
- <code title="put /v1/organization/instance">client.organization.instance.<a href="./src/papr_memory/resources/organization/instance.py">update</a>(\*\*<a href="src/papr_memory/types/organization/instance_update_params.py">params</a>) -> <a href="./src/papr_memory/types/organization/instance_update_response.py">InstanceUpdateResponse</a></code>
- <code title="delete /v1/organization/instance">client.organization.instance.<a href="./src/papr_memory/resources/organization/instance.py">delete</a>() -> <a href="./src/papr_memory/types/organization/instance_delete_response.py">InstanceDeleteResponse</a></code>

# AI

Methods:

- <code title="get /v1/ai/usage">client.ai.<a href="./src/papr_memory/resources/ai/ai.py">get_usage</a>() -> object</code>

## OpenAI

Methods:

- <code title="post /v1/ai/openai/responses">client.ai.openai.<a href="./src/papr_memory/resources/ai/openai/openai.py">create_response</a>() -> object</code>

### Chat

Methods:

- <code title="post /v1/ai/openai/chat/completions">client.ai.openai.chat.<a href="./src/papr_memory/resources/ai/openai/chat.py">create_completion</a>() -> object</code>

## Anthropic

Methods:

- <code title="post /v1/ai/anthropic/messages">client.ai.anthropic.<a href="./src/papr_memory/resources/ai/anthropic.py">send_message</a>() -> object</code>

## Google

### Models

Methods:

- <code title="post /v1/ai/google/models/{model_id}:generateContent">client.ai.google.models.<a href="./src/papr_memory/resources/ai/google/models.py">generate_content</a>(model_id) -> object</code>
- <code title="post /v1/ai/google/models/{model_id}:streamGenerateContent">client.ai.google.models.<a href="./src/papr_memory/resources/ai/google/models.py">stream_generate_content</a>(model_id) -> object</code>

# Telemetry

Types:

```python
from papr_memory.types import TelemetryTrackEventResponse
```

Methods:

- <code title="post /v1/telemetry/events">client.telemetry.<a href="./src/papr_memory/resources/telemetry.py">track_event</a>(\*\*<a href="src/papr_memory/types/telemetry_track_event_params.py">params</a>) -> <a href="./src/papr_memory/types/telemetry_track_event_response.py">TelemetryTrackEventResponse</a></code>

# Login

Types:

```python
from papr_memory.types import LoginInitiateResponse
```

Methods:

- <code title="get /login">client.login.<a href="./src/papr_memory/resources/login.py">initiate</a>() -> <a href="./src/papr_memory/types/login_initiate_response.py">LoginInitiateResponse</a></code>

# Callback

Types:

```python
from papr_memory.types import CallbackProcessResponse
```

Methods:

- <code title="get /callback">client.callback.<a href="./src/papr_memory/resources/callback.py">process</a>() -> <a href="./src/papr_memory/types/callback_process_response.py">CallbackProcessResponse</a></code>

# Token

Types:

```python
from papr_memory.types import TokenCreateResponse
```

Methods:

- <code title="post /token">client.token.<a href="./src/papr_memory/resources/token.py">create</a>() -> <a href="./src/papr_memory/types/token_create_response.py">TokenCreateResponse</a></code>

# Me

Types:

```python
from papr_memory.types import MeRetrieveResponse
```

Methods:

- <code title="get /me">client.me.<a href="./src/papr_memory/resources/me.py">retrieve</a>() -> <a href="./src/papr_memory/types/me_retrieve_response.py">MeRetrieveResponse</a></code>

# Logout

Types:

```python
from papr_memory.types import LogoutPerformResponse
```

Methods:

- <code title="get /logout">client.logout.<a href="./src/papr_memory/resources/logout.py">perform</a>() -> <a href="./src/papr_memory/types/logout_perform_response.py">LogoutPerformResponse</a></code>
