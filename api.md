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
    BatchMemoryResponse,
    ContextItem,
    HTTPValidationError,
    MemoryMetadata,
    MemoryType,
    RelationshipItem,
    SearchResponse,
    MemoryUpdateResponse,
    MemoryDeleteResponse,
)
```

Methods:

- <code title="put /v1/memory/{memory_id}">client.memory.<a href="./src/papr_memory/resources/memory.py">update</a>(memory_id, \*\*<a href="src/papr_memory/types/memory_update_params.py">params</a>) -> <a href="./src/papr_memory/types/memory_update_response.py">MemoryUpdateResponse</a></code>
- <code title="delete /v1/memory/{memory_id}">client.memory.<a href="./src/papr_memory/resources/memory.py">delete</a>(memory_id, \*\*<a href="src/papr_memory/types/memory_delete_params.py">params</a>) -> <a href="./src/papr_memory/types/memory_delete_response.py">MemoryDeleteResponse</a></code>
- <code title="post /v1/memory">client.memory.<a href="./src/papr_memory/resources/memory.py">add</a>(\*\*<a href="src/papr_memory/types/memory_add_params.py">params</a>) -> <a href="./src/papr_memory/types/add_memory_response.py">AddMemoryResponse</a></code>
- <code title="post /v1/memory/batch">client.memory.<a href="./src/papr_memory/resources/memory.py">add_batch</a>(\*\*<a href="src/papr_memory/types/memory_add_batch_params.py">params</a>) -> <a href="./src/papr_memory/types/batch_memory_response.py">BatchMemoryResponse</a></code>
- <code title="delete /v1/memory/all">client.memory.<a href="./src/papr_memory/resources/memory.py">delete_all</a>(\*\*<a href="src/papr_memory/types/memory_delete_all_params.py">params</a>) -> <a href="./src/papr_memory/types/batch_memory_response.py">BatchMemoryResponse</a></code>
- <code title="get /v1/memory/{memory_id}">client.memory.<a href="./src/papr_memory/resources/memory.py">get</a>(memory_id) -> <a href="./src/papr_memory/types/search_response.py">SearchResponse</a></code>
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
