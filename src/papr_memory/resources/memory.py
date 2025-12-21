# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os as _os
import warnings
from typing import Iterable, Optional, cast

import httpx

# Suppress deprecation warning from sentence_transformers
warnings.filterwarnings("ignore", message=".*_target_device.*deprecated.*", category=UserWarning)

# Silence HF tokenizers fork warnings globally
_os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

from papr_memory.types import (
    MemoryType,
    GraphGenerationParam,
    memory_add_params,
    memory_delete_params,
    memory_search_params,
    memory_update_params,
    memory_add_batch_params,
    memory_delete_all_params,
)
from papr_memory._base_client import make_request_options
from papr_memory.types.search_response import SearchResponse
from papr_memory.types.add_memory_param import AddMemoryParam
from papr_memory.types.sync_tiers_params import SyncTiersParams
from papr_memory.types.context_item_param import ContextItemParam
from papr_memory.types.add_memory_response import AddMemoryResponse
from papr_memory.types.sync_tiers_response import SyncTiersResponse
from papr_memory.types.batch_memory_response import BatchMemoryResponse
from papr_memory.types.memory_metadata_param import MemoryMetadataParam
from papr_memory.types.memory_delete_response import MemoryDeleteResponse
from papr_memory.types.memory_update_response import MemoryUpdateResponse
from papr_memory.types.relationship_item_param import RelationshipItemParam

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)

__all__ = ["MemoryResource", "AsyncMemoryResource"]


# Global singleton instances to avoid multiple initializations
import os
import threading
from typing import Optional

# import chromadb  # Used for type hints only

_global_qwen_model: Optional[object] = None
_global_coreml_model: Optional[object] = None  # Cache CoreML model to avoid reloading
_global_coreml_tokenizer: Optional[object] = None  # Cache tokenizer too
_global_chroma_client: Optional[object] = None
_global_chroma_collection: Optional[object] = None
_global_sync_lock: Optional[threading.Lock] = None
_global_model_cache_lock = threading.Lock()  # Thread-safe model loading
_background_sync_task: Optional[threading.Thread] = None
_background_model_loading_task: Optional[threading.Thread] = None
_background_initialization_task: Optional[threading.Thread] = None
_model_loading_complete = False
_model_loading_callback = None
_sync_interval = int(os.environ.get("PAPR_SYNC_INTERVAL", "300"))  # 5 minutes default


class MemoryResource(SyncAPIResource):
    # Class-level type hints for user context attributes
    _user_id: Optional[str]
    _external_user_id: Optional[str]
    _user_context_version: int
    
    @cached_property
    def with_raw_response(self) -> MemoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return MemoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MemoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return MemoryResourceWithStreamingResponse(self)

    def set_user_context(
        self,
        user_id: Optional[str] = None,
        external_user_id: Optional[str] = None,
        resync: bool = True,
        clear_cache: bool = True,
    ) -> None:
        """
        Set or update user context and optionally re-fetch memories.
        
        This is useful when a user logs in and you want to fetch their specific memories,
        or when switching between different user accounts.
        
        Args:
            user_id: Internal user ID to filter memories
            external_user_id: External user ID to filter memories
            resync: If True, immediately re-fetch tiers with new user context
            clear_cache: If True, clear ChromaDB cache before re-syncing
        
        Example:
            ```python
            # User logs in
            client.memory.set_user_context(
                user_id="user_123",
                resync=True  # Fetch this user's memories
            )
            ```
        """
        from papr_memory._logging import get_logger

        logger = get_logger(__name__)

        old_user = self._user_id or self._external_user_id
        new_user = user_id or external_user_id

        # Check if context actually changed
        if old_user == new_user:
            logger.info(f"🔒 User context unchanged: {new_user}")
            return

        logger.info(f"🔄 Updating user context: {old_user} → {new_user}")

        # Update context
        self._user_id = user_id
        self._external_user_id = external_user_id
        self._user_context_version += 1

        # Clear old user's data
        if clear_cache:
            logger.info("🧹 Clearing ChromaDB cache (old user's memories)")
            self._clear_chromadb_collections()

        # Re-fetch new user's memories
        if resync:
            logger.info(f"🔄 Re-syncing tiers for user: {new_user}")
            try:
                self._start_background_initialization()
                logger.info("✅ Background re-sync started")
            except Exception as e:
                logger.warning(f"Failed to start background re-sync: {e}")

    def clear_user_context(self, clear_cache: bool = True) -> None:
        """
        Clear user context (e.g., on logout).
        
        Args:
            clear_cache: If True, clear ChromaDB cache
        
        Example:
            ```python
            # User logs out
            client.memory.clear_user_context(clear_cache=True)
            ```
        """
        from papr_memory._logging import get_logger

        logger = get_logger(__name__)

        logger.info(f"🔓 Clearing user context: {self._user_id or self._external_user_id}")

        self._user_id = None
        self._external_user_id = None
        self._user_context_version += 1

        if clear_cache:
            logger.info("🧹 Clearing ChromaDB cache")
            self._clear_chromadb_collections()

    def _clear_chromadb_collections(self) -> None:
        """Clear both tier0 and tier1 ChromaDB collections."""
        from papr_memory._logging import get_logger

        logger = get_logger(__name__)

        try:
            import chromadb

            if hasattr(self, "_chroma_client") and self._chroma_client:
                # Delete collections
                for collection_name in ["tier0_goals_okrs", "tier1_memories"]:
                    try:
                        self._chroma_client.delete_collection(collection_name)
                        logger.info(f"✅ Cleared collection: {collection_name}")
                    except Exception as e:
                        logger.debug(f"Collection {collection_name} not found or already deleted: {e}")

                # Reset collection references
                self._chroma_collection = None  # type: ignore
                self._chroma_tier1_collection = None  # type: ignore
                logger.info("✅ ChromaDB collections cleared successfully")

        except ImportError:
            logger.debug("ChromaDB not available - skipping collection cleanup")
        except Exception as e:
            logger.warning(f"Failed to clear ChromaDB collections: {e}")

    def update(
        self,
        memory_id: str,
        *,
        content: Optional[str] | Omit = omit,
        context: Optional[Iterable[ContextItemParam]] | Omit = omit,
        metadata: Optional[MemoryMetadataParam] | Omit = omit,
        namespace_id: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        relationships_json: Optional[Iterable[RelationshipItemParam]] | Omit = omit,
        type: Optional[MemoryType] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryUpdateResponse:
        """
        Update an existing memory item by ID.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - Content-Type: application/json
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

            The API validates content size against MAX_CONTENT_LENGTH environment variable (defaults to 15000 bytes).

        Args:
          content: The new content of the memory item

          context: Updated context for the memory item

          metadata: Metadata for memory request

          namespace_id: Optional namespace ID for multi-tenant memory scoping. When provided, update is
              scoped to memories within this namespace.

          organization_id: Optional organization ID for multi-tenant memory scoping. When provided, update
              is scoped to memories within this organization.

          relationships_json: Updated relationships for Graph DB (neo4J)

          type: Valid memory types

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not memory_id:
            raise ValueError(f"Expected a non-empty value for `memory_id` but received {memory_id!r}")
        return self._put(
            f"/v1/memory/{memory_id}",
            body=maybe_transform(
                {
                    "content": content,
                    "context": context,
                    "metadata": metadata,
                    "namespace_id": namespace_id,
                    "organization_id": organization_id,
                    "relationships_json": relationships_json,
                    "type": type,
                },
                memory_update_params.MemoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryUpdateResponse,
        )

    def delete(
        self,
        memory_id: str,
        *,
        skip_parse: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryDeleteResponse:
        """
        Delete a memory item by ID.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

        Args:
          skip_parse: Skip Parse Server deletion

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not memory_id:
            raise ValueError(f"Expected a non-empty value for `memory_id` but received {memory_id!r}")
        return self._delete(
            f"/v1/memory/{memory_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"skip_parse": skip_parse}, memory_delete_params.MemoryDeleteParams),
            ),
            cast_to=MemoryDeleteResponse,
        )

    def add(
        self,
        *,
        content: str,
        skip_background_processing: bool | Omit = omit,
        context: Optional[Iterable[ContextItemParam]] | Omit = omit,
        graph_generation: Optional[GraphGenerationParam] | Omit = omit,
        metadata: Optional[MemoryMetadataParam] | Omit = omit,
        namespace_id: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        relationships_json: Optional[Iterable[RelationshipItemParam]] | Omit = omit,
        type: MemoryType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddMemoryResponse:
        """
        Add a new memory item to the system with size validation and background
        processing.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - Content-Type: application/json
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

            **Role-Based Memory Categories**:
            - **User memories**: preference, task, goal, facts, context
            - **Assistant memories**: skills, learning

            **New Metadata Fields**:
            - `metadata.role`: Optional field to specify who generated the memory (user or assistant)
            - `metadata.category`: Optional field for memory categorization based on role
            - Both fields are stored within metadata at the same level as topics, location, etc.

            The API validates content size against MAX_CONTENT_LENGTH environment variable (defaults to 15000 bytes).

        Args:
          content: The content of the memory item you want to add to memory

          skip_background_processing: If True, skips adding background tasks for processing

          context: Context can be conversation history or any relevant context for a memory item

          graph_generation: Graph generation configuration

          metadata: Metadata for memory request

          namespace_id: Optional namespace ID for multi-tenant memory scoping. When provided, memory is
              associated with this namespace.

          organization_id: Optional organization ID for multi-tenant memory scoping. When provided, memory
              is associated with this organization.

          relationships_json: Array of relationships that we can use in Graph DB (neo4J)

          type: Memory item type; defaults to 'text' if omitted

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/memory",
            body=maybe_transform(
                {
                    "content": content,
                    "context": context,
                    "graph_generation": graph_generation,
                    "metadata": metadata,
                    "namespace_id": namespace_id,
                    "organization_id": organization_id,
                    "relationships_json": relationships_json,
                    "type": type,
                },
                memory_add_params.MemoryAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"skip_background_processing": skip_background_processing}, memory_add_params.MemoryAddParams
                ),
            ),
            cast_to=AddMemoryResponse,
        )

    def add_batch(
        self,
        *,
        memories: Iterable[AddMemoryParam],
        skip_background_processing: bool | Omit = omit,
        batch_size: Optional[int] | Omit = omit,
        external_user_id: Optional[str] | Omit = omit,
        graph_generation: Optional[GraphGenerationParam] | Omit = omit,
        namespace_id: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        webhook_secret: Optional[str] | Omit = omit,
        webhook_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchMemoryResponse:
        """
        Add multiple memory items in a batch with size validation and background
        processing.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - Content-Type: application/json
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

            The API validates individual memory content size against MAX_CONTENT_LENGTH environment variable (defaults to 15000 bytes).

        Args:
          memories: List of memory items to add in batch

          skip_background_processing: If True, skips adding background tasks for processing

          batch_size: Number of items to process in parallel

          external_user_id: External user ID for all memories in the batch. If provided and user_id is not,
              will be resolved to internal user ID.

          graph_generation: Graph generation configuration

          namespace_id: Optional namespace ID for multi-tenant batch memory scoping. When provided, all
              memories in the batch are associated with this namespace.

          organization_id: Optional organization ID for multi-tenant batch memory scoping. When provided,
              all memories in the batch are associated with this organization.

          user_id: Internal user ID for all memories in the batch. If not provided, developer's
              user ID will be used.

          webhook_secret: Optional secret key for webhook authentication. If provided, will be included in
              the webhook request headers as 'X-Webhook-Secret'.

          webhook_url: Optional webhook URL to notify when batch processing is complete. The webhook
              will receive a POST request with batch completion details.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/memory/batch",
            body=maybe_transform(
                {
                    "memories": memories,
                    "batch_size": batch_size,
                    "external_user_id": external_user_id,
                    "graph_generation": graph_generation,
                    "namespace_id": namespace_id,
                    "organization_id": organization_id,
                    "user_id": user_id,
                    "webhook_secret": webhook_secret,
                    "webhook_url": webhook_url,
                },
                memory_add_batch_params.MemoryAddBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"skip_background_processing": skip_background_processing},
                    memory_add_batch_params.MemoryAddBatchParams,
                ),
            ),
            cast_to=BatchMemoryResponse,
        )

    def delete_all(
        self,
        *,
        external_user_id: Optional[str] | Omit = omit,
        skip_parse: bool | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchMemoryResponse:
        """
        Delete all memory items for a user.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **User Resolution**:
            - If only API key is provided: deletes memories for the developer
            - If user_id or external_user_id is provided: resolves and deletes memories for that user
            - Uses the same user resolution logic as other endpoints

            **Required Headers**:
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

            **WARNING**: This operation cannot be undone. All memories for the resolved user will be permanently deleted.

        Args:
          external_user_id: Optional external user ID to resolve and delete memories for

          skip_parse: Skip Parse Server deletion

          user_id: Optional user ID to delete memories for (if not provided, uses authenticated
              user)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/v1/memory/all",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "external_user_id": external_user_id,
                        "skip_parse": skip_parse,
                        "user_id": user_id,
                    },
                    memory_delete_all_params.MemoryDeleteAllParams,
                ),
            ),
            cast_to=BatchMemoryResponse,
        )

    def sync_tiers(
        self,
        *,
        include_embeddings: bool | NotGiven = not_given,
        embed_limit: int | NotGiven = not_given,
        max_tier0: int | NotGiven = not_given,
        max_tier1: int | NotGiven = not_given,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncTiersResponse:
        """
        Get sync tiers for memory synchronization.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')
            - Accept-Encoding: gzip (recommended)

        Args:
          include_embeddings: Whether to include embeddings in the response

          embed_limit: Limit for embeddings

          max_tier0: Maximum number of tier 0 items

          max_tier1: Maximum number of tier 1 items

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Accept-Encoding": "gzip"}), **(extra_headers or {})}
        return self._post(
            "/v1/sync/tiers",
            body=maybe_transform(
                {
                    "include_embeddings": include_embeddings,
                    "embed_limit": embed_limit,
                    "max_tier0": max_tier0,
                    "max_tier1": max_tier1,
                },
                SyncTiersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=SyncTiersResponse,
        )

    def get(
        self,
        memory_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchResponse:
        """
        Retrieve a memory item by ID.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not memory_id:
            raise ValueError(f"Expected a non-empty value for `memory_id` but received {memory_id!r}")
        return self._get(
            f"/v1/memory/{memory_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchResponse,
        )

    def _process_sync_tiers_and_store(
        self,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = None,
    ) -> None:
        """Internal method to call sync_tiers and store tier0 data in ChromaDB"""
        from papr_memory._logging import get_logger

        logger = get_logger(__name__)
        
        try:
            # Call the sync_tiers method with parameters from environment variables
            # Get max_tier0 from environment variable with fallback to 30
            import os

            max_tier0_env = os.environ.get("PAPR_MAX_TIER0", "30")
            try:
                max_tier0_value = int(max_tier0_env)
            except ValueError:
                max_tier0_value = 30  # fallback to default if invalid
            
            # Get max_tier1 from environment variable, defaulting to same as tier0
            max_tier1_env = os.environ.get("PAPR_MAX_TIER1", str(max_tier0_value))
            try:
                max_tier1_value = int(max_tier1_env)
            except ValueError:
                max_tier1_value = max_tier0_value  # fallback to tier0 value if invalid
            
            # Get server embedding configuration
            include_server_embeddings = os.environ.get("PAPR_INCLUDE_SERVER_EMBEDDINGS", "true").lower() in ("true", "1", "yes")
            embed_limit_env = os.environ.get("PAPR_EMBED_LIMIT", "200")
            try:
                embed_limit_value = int(embed_limit_env)
            except ValueError:
                embed_limit_value = 200  # fallback to default
            
            embed_model_value = os.environ.get("PAPR_EMBED_MODEL", "Qwen4B")
            
            # Detect if CoreML is enabled - if so, request float32 embeddings for tier1
            # CoreML/ANE fp16 models need full precision embeddings for best accuracy
            coreml_enabled = os.environ.get("PAPR_ENABLE_COREML", "false").lower() in ("true", "1", "yes", "on")
            embedding_format_value = os.environ.get("PAPR_EMBEDDING_FORMAT", "float32" if coreml_enabled else "int8")
            
            if coreml_enabled and embedding_format_value == "int8":
                logger.warning("⚠️  CoreML enabled but embedding_format is int8. Switching to float32 for better accuracy with fp16 ANE models.")
                embedding_format_value = "float32"
            
            # Set a reasonable timeout for sync_tiers to prevent hanging
            # Increased to 300s to handle large tier0 (1000 memories with embeddings)
            sync_timeout = timeout if timeout is not None else 300.0  # 5 minutes default
            
            logger.info(f"🔒 Fetching tiers for user: {self._user_id or self._external_user_id or 'ALL'}")
            logger.info(f"📊 Request: max_tier0={max_tier0_value}, max_tier1={max_tier1_value}, include_embeddings={include_server_embeddings}, embed_limit={embed_limit_value}, embed_model={embed_model_value}, embedding_format={embedding_format_value}")
            
            # Build extra_body with user context, embed_model, and embedding_format
            sync_extra_body: dict[str, any] = {  # type: ignore
                "embed_model": embed_model_value,
                "embedding_format": embedding_format_value,
            }
            
            # Add user context if available
            if self._user_id:
                sync_extra_body["user_id"] = self._user_id
            if self._external_user_id:
                sync_extra_body["external_user_id"] = self._external_user_id
            
            # Merge with any additional extra_body params
            if extra_body:
                sync_extra_body.update(extra_body)  # type: ignore
            
            sync_response = self.sync_tiers(
                include_embeddings=include_server_embeddings,
                embed_limit=embed_limit_value,
                max_tier0=max_tier0_value,
                max_tier1=max_tier1_value,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=sync_extra_body,
                timeout=sync_timeout,
            )
            
            if sync_response:
                # Extract tier0 data using SyncTiersResponse model
                tier0_data = sync_response.tier0
                tier1_data = sync_response.tier1
                
                logger.info(f"✅ Received {len(tier0_data)} tier0, {len(tier1_data)} tier1 items")
                
                # Log server embeddings statistics
                if include_server_embeddings:
                    tier0_with_emb = sum(1 for item in tier0_data if hasattr(item, 'embedding') and item.embedding)
                    tier1_with_emb = sum(1 for item in tier1_data if hasattr(item, 'embedding') and item.embedding)
                    logger.info(f"📊 Server embeddings: tier0={tier0_with_emb}/{len(tier0_data)}, tier1={tier1_with_emb}/{len(tier1_data)}")
                    
                    if tier0_with_emb > 0:
                        logger.info(f"✅ Using {tier0_with_emb} server-provided tier0 embeddings (faster initialization!)")
                    if tier1_with_emb > 0:
                        logger.info(f"✅ Using {tier1_with_emb} server-provided tier1 embeddings (faster initialization!)")
                
                if tier0_data:
                    logger.info(f"Found {len(tier0_data)} tier0 items in sync response")
                    for i in range(min(3, len(tier0_data))):
                        logger.debug(f"Tier0 {i + 1}: Item extracted")
                    
                    # Log first 20 tier0 items to file for debugging
                    self._log_sync_response_to_file(tier0_data, "tier0")
                
                if tier1_data:
                    logger.info(f"Found {len(tier1_data)} tier1 items in sync response")
                    
                    # Log first 20 tier1 items to file for debugging
                    self._log_sync_response_to_file(tier1_data, "tier1")
                
                # Store tier0 data in ChromaDB (sync path)
                if tier0_data:
                    logger.info(f"Using {len(tier0_data)} tier0 items for search enhancement")
                    try:
                        self._store_tier0_in_chromadb(tier0_data)  # type: ignore[arg-type]
                    except Exception as store_e:
                        logger.warning(f"Failed to store tier0 in ChromaDB: {store_e}")
                else:
                    logger.info("No tier0 data found in sync response")
                
                # Store tier1 data in ChromaDB (sync path)
                if tier1_data:
                    logger.info(f"Using {len(tier1_data)} tier1 items for search enhancement")
                    try:
                        self._store_tier1_in_chromadb(tier1_data)  # type: ignore[arg-type]
                    except Exception as store_e:
                        logger.warning(f"Failed to store tier1 in ChromaDB: {store_e}")
                else:
                    logger.info("No tier1 data found in sync response")
                    
        except Exception as e:
            logger.error(f"Error in sync_tiers processing: {e}")
            # Check if it's a timeout error
            if "timeout" in str(e).lower() or "timed out" in str(e).lower():
                logger.error("Sync_tiers call timed out - background initialization will continue without local data")
            else:
                logger.error(f"Sync_tiers failed with error: {e}")

    def _log_sync_response_to_file(self, data: list, tier_name: str) -> None:
        """Log first 20 items from sync response to file for debugging
        
        Args:
            data: List of memory items from server
            tier_name: "tier0" or "tier1"
        """
        from papr_memory._logging import get_logger
        logger = get_logger(__name__)
        
        try:
            import json
            from datetime import datetime
            
            # Limit to first 20 items
            items_to_log = data[:min(20, len(data))]
            
            # Create filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"papr_sync_{tier_name}_{timestamp}.json"
            
            # Prepare output
            output = {
                "tier": tier_name,
                "timestamp": timestamp,
                "total_items": len(data),
                "items_logged": len(items_to_log),
                "items": []
            }
            
            for i, item in enumerate(items_to_log):
                item_data = {
                    "index": i,
                    "id": None,
                    "type": None,
                    "content": None,
                    "content_length": 0,
                    "has_embedding": False,
                    "embedding_dimension": 0,
                    "metadata": {},
                    "topics": [],
                    "tags": [],
                    "title": None,
                    "role": None,
                    "category": None,
                    "user_id": None,
                    "external_user_id": None,
                    "workspace_id": None,
                    "organization_id": None,
                    "namespace_id": None,
                    "source_type": None,
                    "source_url": None,
                    "source_document_id": None,
                    "source_message_id": None,
                    "conversation_id": None,
                    "created_at": None,
                    "updated_at": None,
                    # ACL fields
                    "acl": {},
                    "external_user_read_access": [],
                    "external_user_write_access": [],
                    "user_read_access": [],
                    "user_write_access": [],
                    "workspace_read_access": [],
                    "workspace_write_access": [],
                    "role_read_access": [],
                    "role_write_access": [],
                    "namespace_read_access": [],
                    "namespace_write_access": [],
                    "organization_read_access": [],
                    "organization_write_access": [],
                    # Document-specific fields
                    "page_number": None,
                    "total_pages": None,
                    "file_url": None,
                    "filename": None,
                    "page": None,
                    # Relevance score from server ranking
                    "relevance_score": None,
                    "raw_keys": []
                }
                
                if isinstance(item, dict):
                    item_data["raw_keys"] = list(item.keys())
                    item_data["id"] = item.get("id")
                    item_data["type"] = item.get("type")
                    item_data["topics"] = item.get("topics", [])
                    item_data["tags"] = item.get("tags", [])
                    item_data["title"] = item.get("title")
                    item_data["role"] = item.get("role")
                    item_data["category"] = item.get("category")
                    item_data["user_id"] = item.get("user_id")
                    item_data["external_user_id"] = item.get("external_user_id")
                    item_data["workspace_id"] = item.get("workspace_id")
                    item_data["organization_id"] = item.get("organization_id")
                    item_data["namespace_id"] = item.get("namespace_id")
                    item_data["source_type"] = item.get("source_type")
                    item_data["source_url"] = item.get("source_url")
                    item_data["source_document_id"] = item.get("source_document_id")
                    item_data["source_message_id"] = item.get("source_message_id")
                    item_data["conversation_id"] = item.get("conversation_id")
                    item_data["created_at"] = item.get("createdAt") or item.get("created_at")
                    item_data["updated_at"] = item.get("updatedAt") or item.get("updated_at")
                    item_data["metadata"] = item.get("metadata", {})
                    
                    # ACL fields
                    item_data["acl"] = item.get("acl", {})
                    item_data["external_user_read_access"] = item.get("external_user_read_access", [])
                    item_data["external_user_write_access"] = item.get("external_user_write_access", [])
                    item_data["user_read_access"] = item.get("user_read_access", [])
                    item_data["user_write_access"] = item.get("user_write_access", [])
                    item_data["workspace_read_access"] = item.get("workspace_read_access", [])
                    item_data["workspace_write_access"] = item.get("workspace_write_access", [])
                    item_data["role_read_access"] = item.get("role_read_access", [])
                    item_data["role_write_access"] = item.get("role_write_access", [])
                    item_data["namespace_read_access"] = item.get("namespace_read_access", [])
                    item_data["namespace_write_access"] = item.get("namespace_write_access", [])
                    item_data["organization_read_access"] = item.get("organization_read_access", [])
                    item_data["organization_write_access"] = item.get("organization_write_access", [])
                    
                    # Document-specific fields
                    item_data["page_number"] = item.get("page_number")
                    item_data["total_pages"] = item.get("total_pages")
                    item_data["file_url"] = item.get("file_url")
                    item_data["filename"] = item.get("filename")
                    item_data["page"] = item.get("page")
                    
                    # Relevance score from server ranking
                    item_data["relevance_score"] = item.get("relevance_score")
                    
                    # Content
                    raw_content = item.get("content", item.get("description", None))
                    if raw_content is not None:
                        content_str = str(raw_content)
                        item_data["content"] = content_str[:500]  # First 500 chars
                        item_data["content_length"] = len(content_str)
                        item_data["content_is_empty"] = not content_str.strip()
                    else:
                        item_data["content"] = None
                        item_data["content_is_empty"] = True
                    
                    # Embedding
                    if "embedding" in item:
                        embedding = item["embedding"]
                        if embedding and isinstance(embedding, list):
                            item_data["has_embedding"] = True
                            item_data["embedding_dimension"] = len(embedding)
                            item_data["embedding_first_10"] = embedding[:10] if len(embedding) >= 10 else embedding
                elif hasattr(item, 'id'):
                    # Handle Pydantic Memory object
                    item_data["raw_keys"] = list(item.__dict__.keys()) if hasattr(item, '__dict__') else []
                    item_data["id"] = getattr(item, "id", None)
                    item_data["type"] = getattr(item, "type", None)
                    item_data["topics"] = getattr(item, "topics", []) or []
                    item_data["tags"] = getattr(item, "tags", []) or []
                    item_data["title"] = getattr(item, "title", None)
                    item_data["role"] = getattr(item, "role", None)
                    item_data["category"] = getattr(item, "category", None)
                    item_data["user_id"] = getattr(item, "user_id", None)
                    item_data["external_user_id"] = getattr(item, "external_user_id", None)
                    item_data["workspace_id"] = getattr(item, "workspace_id", None)
                    item_data["organization_id"] = getattr(item, "organization_id", None)
                    item_data["namespace_id"] = getattr(item, "namespace_id", None)
                    item_data["source_type"] = getattr(item, "source_type", None)
                    item_data["source_url"] = getattr(item, "source_url", None)
                    item_data["source_document_id"] = getattr(item, "source_document_id", None)
                    item_data["source_message_id"] = getattr(item, "source_message_id", None)
                    item_data["conversation_id"] = getattr(item, "conversation_id", None)
                    
                    # Handle datetime serialization for created_at
                    created_at = getattr(item, "created_at", None)
                    if created_at is not None:
                        item_data["created_at"] = created_at.isoformat() if hasattr(created_at, 'isoformat') else str(created_at)
                    else:
                        item_data["created_at"] = None
                    
                    # Handle datetime serialization for updated_at
                    updated_at = getattr(item, "updated_at", None)
                    if updated_at is not None:
                        item_data["updated_at"] = updated_at.isoformat() if hasattr(updated_at, 'isoformat') else str(updated_at)
                    else:
                        item_data["updated_at"] = None
                    
                    item_data["metadata"] = getattr(item, "metadata", {}) or {}
                    
                    # ACL fields
                    item_data["acl"] = getattr(item, "acl", {}) or {}
                    item_data["external_user_read_access"] = getattr(item, "external_user_read_access", []) or []
                    item_data["external_user_write_access"] = getattr(item, "external_user_write_access", []) or []
                    item_data["user_read_access"] = getattr(item, "user_read_access", []) or []
                    item_data["user_write_access"] = getattr(item, "user_write_access", []) or []
                    item_data["workspace_read_access"] = getattr(item, "workspace_read_access", []) or []
                    item_data["workspace_write_access"] = getattr(item, "workspace_write_access", []) or []
                    item_data["role_read_access"] = getattr(item, "role_read_access", []) or []
                    item_data["role_write_access"] = getattr(item, "role_write_access", []) or []
                    item_data["namespace_read_access"] = getattr(item, "namespace_read_access", []) or []
                    item_data["namespace_write_access"] = getattr(item, "namespace_write_access", []) or []
                    item_data["organization_read_access"] = getattr(item, "organization_read_access", []) or []
                    item_data["organization_write_access"] = getattr(item, "organization_write_access", []) or []
                    
                    # Document-specific fields
                    item_data["page_number"] = getattr(item, "page_number", None)
                    item_data["total_pages"] = getattr(item, "total_pages", None)
                    item_data["file_url"] = getattr(item, "file_url", None)
                    item_data["filename"] = getattr(item, "filename", None)
                    item_data["page"] = getattr(item, "page", None)
                    
                    # Relevance score from server ranking
                    item_data["relevance_score"] = getattr(item, "relevance_score", None)
                    
                    # Content
                    raw_content = getattr(item, "content", None) or getattr(item, "description", None)
                    if raw_content is not None:
                        content_str = str(raw_content)
                        item_data["content"] = content_str[:500]  # First 500 chars
                        item_data["content_length"] = len(content_str)
                        item_data["content_is_empty"] = not content_str.strip()
                    else:
                        item_data["content"] = None
                        item_data["content_is_empty"] = True
                    
                    # Embedding
                    if hasattr(item, 'embedding'):
                        embedding = item.embedding
                        if embedding and isinstance(embedding, list):
                            item_data["has_embedding"] = True
                            item_data["embedding_dimension"] = len(embedding)
                            item_data["embedding_first_10"] = embedding[:10] if len(embedding) >= 10 else embedding
                
                output["items"].append(item_data)
            
            # Write to file
            with open(filename, 'w') as f:
                json.dump(output, f, indent=2)
            
            logger.info(f"📄 Logged first {len(items_to_log)} {tier_name} items to: {filename}")
            
            # Also log summary to console
            empty_count = sum(1 for item in output["items"] if item.get("content_is_empty", True))
            with_embedding_count = sum(1 for item in output["items"] if item.get("has_embedding", False))
            
            logger.info(f"   {tier_name} summary:")
            logger.info(f"   - Items with content: {len(items_to_log) - empty_count}/{len(items_to_log)}")
            logger.info(f"   - Items with NO/EMPTY content: {empty_count}/{len(items_to_log)}")
            logger.info(f"   - Items with embeddings: {with_embedding_count}/{len(items_to_log)}")
            
        except Exception as e:
            logger.warning(f"Failed to log {tier_name} sync response to file: {e}")

    def _is_old_platform(self) -> bool:
        """Detect if platform is too old for efficient local processing"""
        from papr_memory._logging import get_logger

        logger = get_logger(__name__)
        
        try:
            import platform
            import subprocess

            import psutil  # type: ignore
            
            system = platform.system()
            
            # Check Apple platforms
            if system == "Darwin":
                try:
                    # Get Apple chip info
                    result = subprocess.run(
                        ["sysctl", "-n", "machdep.cpu.brand_string"], capture_output=True, text=True, timeout=5
                    )
                    if result.returncode == 0:
                        cpu_info = result.stdout.strip()
                        # Check for old Intel Macs (pre-Apple Silicon)
                        if "Intel" in cpu_info and "Apple" not in cpu_info:
                            logger.info("Detected old Intel Mac - using API instead of local processing")
                            return True
                        # Check for very old Apple Silicon (M1 without sufficient performance)
                        elif "Apple" in cpu_info:
                            # Check for M1 vs M2/M3/M4
                            if (
                                "M1" in cpu_info
                                and "M1 Pro" not in cpu_info
                                and "M1 Max" not in cpu_info
                                and "M1 Ultra" not in cpu_info
                            ):
                                # Check RAM - M1 with < 16GB might be too slow
                                ram_gb = psutil.virtual_memory().total / (1024**3)
                                if ram_gb < 16:
                                    logger.info("Detected M1 with limited RAM - using API instead of local processing")
                                    return True
                except Exception:
                    pass
            
            # Check Intel platforms
            elif system == "Linux" or system == "Windows":
                try:
                    cpu_info = platform.processor() or platform.machine()
                    # Check for old Intel CPUs (pre-10th gen or < 4 cores)
                    if "Intel" in cpu_info:
                        cpu_count = psutil.cpu_count(logical=False)
                        if cpu_count is not None and cpu_count < 4:
                            logger.info("Detected old Intel CPU with < 4 cores - using API instead of local processing")
                            return True
                    
                    # Check for old AMD CPUs
                    elif "AMD" in cpu_info:
                        cpu_count = psutil.cpu_count(logical=False)
                        if cpu_count is not None and cpu_count < 4:
                            logger.info("Detected old AMD CPU with < 4 cores - using API instead of local processing")
                            return True
                except Exception:
                    pass
            
            # Check available RAM (less than 8GB is too little for local processing)
            ram_gb = psutil.virtual_memory().total / (1024**3)
            if ram_gb < 8:
                logger.info(f"Insufficient RAM ({ram_gb:.1f}GB) - using API instead of local processing")
                return True
                
        except ImportError:
            logger.info("psutil not available - assuming modern platform")
        except Exception as e:
            logger.error(f"Error detecting platform age: {e}")
        
        return False

    def _get_optimized_quantized_model(self, device: str, device_name: str) -> object:
        """Get the best quantized model for the specific platform"""
        from papr_memory._logging import get_logger

        logger = get_logger(__name__)
        
        try:
            # Try Core ML path first if enabled on Apple (runs on ANE/GPU)
            enable_coreml = os.environ.get("PAPR_ENABLE_COREML", "false").lower() in ("true", "1", "yes", "on")
            if ("Apple" in device_name or device == "mps") and enable_coreml:
                try:
                    import numpy as np  # type: ignore
                    import coremltools as ct  # type: ignore
                    from transformers import AutoTokenizer  # type: ignore

                    from papr_memory._model_cache import resolve_coreml_model_path

                    # Check if CoreML model is cached globally (from warmup)
                    global _global_coreml_model, _global_coreml_tokenizer, _global_model_cache_lock

                    # Thread-safe model loading to prevent race conditions
                    with _global_model_cache_lock:
                        if _global_coreml_model is not None and _global_coreml_tokenizer is not None:
                            logger.info("Using cached CoreML model (preloaded during warmup)")
                            mlmodel = _global_coreml_model
                            tokenizer = _global_coreml_tokenizer
                        else:
                            # Auto-download from HuggingFace if not found locally
                            coreml_path_env = os.environ.get("PAPR_COREML_MODEL")
                            coreml_path = resolve_coreml_model_path(coreml_path_env)
                            tok_id = os.environ.get("PAPR_EMBEDDING_MODEL", "Qwen/Qwen3-Embedding-4B")

                            logger.info(f"Loading Core ML model from {coreml_path}")
                            
                            # Get compute units from environment or use CPU_AND_NE for ANE optimization
                            # Options: ALL, CPU_AND_GPU, CPU_AND_NE, CPU_ONLY
                            # CPU_AND_NE forces ANE usage for FP16 models (best performance if model is ANE-compatible)
                            compute_unit_str = os.environ.get("PAPR_COREML_COMPUTE_UNITS", "CPU_AND_NE")
                            compute_unit_map = {
                                "ALL": ct.ComputeUnit.ALL,
                                "CPU_AND_GPU": ct.ComputeUnit.CPU_AND_GPU,
                                "CPU_AND_NE": ct.ComputeUnit.CPU_AND_NE,
                                "CPU_ONLY": ct.ComputeUnit.CPU_ONLY,
                            }
                            requested_compute_unit = compute_unit_map.get(compute_unit_str, ct.ComputeUnit.CPU_AND_NE)
                            
                            logger.info(f"🔧 Requesting CoreML compute units: {compute_unit_str}")
                            logger.info(f"   💡 To change: export PAPR_COREML_COMPUTE_UNITS=ALL|CPU_AND_GPU|CPU_AND_NE|CPU_ONLY")
                            
                            # Try to load model with requested compute unit, with fallback
                            mlmodel = None
                            load_error = None
                            
                            try:
                                mlmodel = ct.models.MLModel(coreml_path, compute_units=requested_compute_unit)
                                logger.info(f"✅ CoreML model loaded successfully with {compute_unit_str}")
                            except Exception as e:
                                load_error = e
                                logger.warning(f"⚠️  Failed to load model with {compute_unit_str}: {e}")
                                
                                # Fallback to ALL if specific compute unit failed
                                if requested_compute_unit != ct.ComputeUnit.ALL:
                                    logger.info(f"🔄 Falling back to compute_units=ALL")
                                    try:
                                        mlmodel = ct.models.MLModel(coreml_path, compute_units=ct.ComputeUnit.ALL)
                                        logger.info(f"✅ CoreML model loaded successfully with fallback (ALL)")
                                    except Exception as fallback_e:
                                        logger.error(f"❌ Failed to load model even with fallback: {fallback_e}")
                                        raise fallback_e
                                else:
                                    raise e
                            
                            # Log detailed compute unit configuration
                            try:
                                import platform
                                logger.info(f"📱 Device: {platform.machine()} running macOS {platform.mac_ver()[0]}")
                                
                                configuration = getattr(mlmodel, "configuration", None)
                                if configuration:
                                    compute_units = getattr(configuration, "compute_units", None)
                                    logger.info(f"✅ CoreML configuration found")
                                    logger.info(f"   Compute units reported: {compute_units}")
                                    
                                    # Try to get more detailed info
                                    if hasattr(configuration, 'computeUnits'):
                                        logger.info(f"   computeUnits property: {configuration.computeUnits}")
                                else:
                                    logger.warning(f"⚠️  No configuration object found on MLModel")
                                    logger.warning(f"   This may indicate model conversion issues or compatibility problems")
                            except Exception as e:
                                logger.warning(f"⚠️  Could not read CoreML configuration: {e}")
                            
                            # Load tokenizer (ALWAYS - not just on exception!)
                            logger.info(f"Loading tokenizer from {tok_id}")
                            tokenizer = AutoTokenizer.from_pretrained(tok_id)

                            # Cache for future use
                            _global_coreml_model = mlmodel
                            _global_coreml_tokenizer = tokenizer
                            logger.info("Cached CoreML model globally for future searches")

                    class CoreMLEmbeddingFunction:
                        def __init__(self, model: object, tokenizer: object, logger: object):
                            self.model = model
                            self.tokenizer = tokenizer
                            self.logger = logger
                            self._inference_count = 0

                        def _encode(self, texts: list[str]) -> list[list[float]]:
                            # Normalize inputs to list[str]
                            if isinstance(texts, str):
                                texts = [texts]
                            texts = ["" if t is None else str(t) for t in texts]

                            # Use fixed padding to match Core ML conversion (max_length=32)
                            enc = self.tokenizer(  # type: ignore
                                texts,
                                padding="max_length",
                                max_length=32,
                                truncation=True,
                                return_tensors="np",
                            )
                            # Core ML expects int32 inputs typically
                            feed = {
                                "input_ids": enc["input_ids"].astype(np.int32),
                                "attention_mask": enc["attention_mask"].astype(np.int32),
                            }
                            import time as _time

                            predict_start = _time.perf_counter()
                            out = self.model.predict(feed)  # type: ignore
                            duration_ms = (_time.perf_counter() - predict_start) * 1000
                            self._inference_count += 1
                            
                            # Determine likely compute unit based on latency
                            compute_unit_guess = "unknown"
                            if duration_ms < 150:
                                compute_unit_guess = "ANE (Neural Engine)"
                            elif duration_ms < 300:
                                compute_unit_guess = "GPU"
                            else:
                                compute_unit_guess = "CPU or slow GPU"
                            
                            if self._inference_count <= 3 or duration_ms > 500:
                                self.logger.info(  # type: ignore
                                    "Core ML inference #%s completed in %.1fms (batch=%s) - likely using %s",
                                    self._inference_count,
                                    duration_ms,
                                    len(texts),
                                    compute_unit_guess,
                                )

                            # Select the most likely embedding tensor among outputs
                            candidates = []
                            for v in out.values():
                                arr = np.asarray(v)
                                candidates.append(arr)

                            # Prefer tensors with last dim == 2560, else highest last-dim, else highest ndim
                            def score(a: np.ndarray) -> tuple[int, int, int]:  # type: ignore[name-defined]
                                last_dim = a.shape[-1] if a.ndim >= 1 else 0
                                return (
                                    2 if last_dim == 2560 else (1 if a.ndim >= 2 else 0),
                                    last_dim,
                                    a.size,
                                )

                            best = max(candidates, key=score)

                            # Pool to [batch, dim]
                            if best.ndim == 3:
                                pooled = best.mean(axis=1).astype(np.float32)
                            elif best.ndim == 2:
                                pooled = best.astype(np.float32)
                            elif best.ndim == 1:
                                pooled = best.astype(np.float32)[None, :]
                            else:
                                raise TypeError(f"Unexpected Core ML output shape: {best.shape}")

                            return pooled.tolist()

                        def embed_query(self, input: str) -> list[float]:
                            return self._encode([input])[0]

                        def embed_documents(self, input: list[str]) -> list[list[float]]:
                            return self._encode(input)

                        # Compatibility: some callsites expect encode() or __call__
                        def encode(self, inputs: list[str]) -> list[list[float]]:  # type: ignore[override]
                            return self._encode(inputs)

                        def __call__(self, inputs: list[str]) -> list[list[float]]:  # type: ignore[override]
                            return self._encode(inputs)

                    logger.info("Using Core ML embedding function (ANE/GPU capable)")
                    return CoreMLEmbeddingFunction(mlmodel, tokenizer, logger)
                except Exception as coreml_e:  # pragma: no cover
                    logger.info(f"Core ML path unavailable, will try MLX/ST: {coreml_e}")

            # If MLX is explicitly enabled on Apple, attempt a native MLX embedding path next
            enable_mlx = os.environ.get("PAPR_ENABLE_MLX", "false").lower() in ("true", "1", "yes", "on")
            if ("Apple" in device_name or device == "mps") and enable_mlx:
                try:
                    from mlx_lm import load as mlx_load  # type: ignore

                    mlx_model_name = os.environ.get(
                        "PAPR_EMBEDDING_MODEL", "mlx-community/Qwen3-Embedding-4B-4bit-DWQ"
                    )
                    logger.info(f"Attempting MLX native embedder: {mlx_model_name}")

                    mlx_model, mlx_tokenizer = mlx_load(mlx_model_name)

                    class MlxQwenEmbeddingFunction:  # Chroma-compatible
                        def __init__(self, model: object, tokenizer: object):
                            self.model = model
                            self.tokenizer = tokenizer

                        def _encode_texts(self, inputs: list[str]) -> list[list[float]]:
                            try:
                                # Prefer HF tokenizer for MLX models when available
                                from typing import Any, Callable, cast
                                try:
                                    from transformers import AutoTokenizer  # type: ignore
                                    hf_tok = AutoTokenizer.from_pretrained(
                                        os.environ.get("PAPR_EMBEDDING_MODEL", "Qwen/Qwen3-Embedding-4B")
                                    )
                                    enc: Any = hf_tok(inputs, padding=True, truncation=True, return_tensors=None)
                                except Exception:
                                    if not callable(self.tokenizer):
                                        raise TypeError("MLX tokenizer is not callable; falling back to ST embedder") from None
                                    tok: Callable[..., Any] = cast(Callable[..., Any], self.tokenizer)
                                    enc = tok(inputs, return_tensors=None, padding=True, truncation=True)
                                # Some MLX models expose a nested .model; try both
                                mdl: object = getattr(self.model, "model", self.model)

                                # Request hidden states if supported
                                if not callable(mdl):  # type: ignore[misc]
                                    raise TypeError("MLX model is not callable; using fallback embedder")
                                mdl_callable: Callable[..., Any] = cast(Callable[..., Any], mdl)
                                outputs: Any = mdl_callable(
                                    **{k: enc[k] for k in enc if isinstance(enc[k], list)},
                                    output_hidden_states=True,
                                )
                                hidden: object | None = None
                                if hasattr(outputs, "hidden_states") and outputs.hidden_states:
                                    hidden = outputs.hidden_states[-1]
                                elif hasattr(outputs, "last_hidden_state"):
                                    hidden = outputs.last_hidden_state

                                if hidden is None:
                                    raise RuntimeError("MLX model did not return hidden states for pooling")

                                # Normalize to ndarray then mean-pool
                                import numpy as np  # local import to avoid global dependency changes
                                arr = np.asarray(hidden)
                                if arr.ndim == 3:  # [batch, seq_len, dim]
                                    pooled = arr.mean(axis=1).tolist()
                                elif arr.ndim == 2:  # [seq_len, dim] -> single item
                                    pooled = [arr.mean(axis=0).tolist()]
                                else:
                                    raise TypeError(f"Unexpected hidden shape: {arr.shape}")
                                return pooled
                            except Exception as e:  # pragma: no cover
                                logger.warning(f"MLX embedding failed, falling back to ST: {e}")
                                # Fallback: sentence-transformers on local device
                                try:
                                    import torch
                                    from sentence_transformers import SentenceTransformer

                                    device = (
                                        "mps"
                                        if hasattr(torch.backends, "mps") and torch.backends.mps.is_available()
                                        else ("cuda" if torch.cuda.is_available() else "cpu")
                                    )
                                    fallback_name = os.environ.get(
                                        "PAPR_EMBEDDING_FALLBACK_MODEL", "Qwen/Qwen3-Embedding-4B"
                                    )
                                    st_model = SentenceTransformer(fallback_name, device=device)
                                    embs = st_model.encode(inputs)
                                    return embs.tolist()  # type: ignore
                                except Exception as e2:
                                    logger.error(f"Fallback ST embedding failed: {e2}")
                                    return [[] for _ in inputs]

                        def embed_query(self, input: str) -> list[float]:
                            return self._encode_texts([input])[0]

                        def embed_documents(self, input: list[str]) -> list[list[float]]:
                            return self._encode_texts(input)

                    mlx_func = MlxQwenEmbeddingFunction(mlx_model, mlx_tokenizer)
                    logger.info("Using native MLX embedding function for Qwen (quantized)")
                    return mlx_func
                except Exception as mlx_e:  # pragma: no cover
                    logger.info(f"MLX path unavailable, will try sentence-transformers: {mlx_e}")

            from sentence_transformers import SentenceTransformer
            
            # Platform-specific model selection (using sentence-transformers compatible models)
            if "Apple" in device_name or device == "mps":
                # If MLX is not enabled on Apple, do not use on-device ST fallback (too heavy); prefer API
                enable_mlx = os.environ.get("PAPR_ENABLE_MLX", "false").lower() in ("true", "1", "yes", "on")
                enable_coreml = os.environ.get("PAPR_ENABLE_COREML", "false").lower() in ("true", "1", "yes", "on")
                if not enable_mlx and not enable_coreml:
                    logger.info("Apple Silicon detected without MLX; disabling ondevice and using API")
                    self._ondevice_processing_disabled = True
                    return None
                # Otherwise, allow ST fallback only if explicitly configured
                model_options = [
                    os.environ.get("PAPR_EMBEDDING_MODEL", "Qwen/Qwen3-Embedding-4B"),
                ]
                logger.info("Apple Silicon: MLX enabled; ST fallback allowed if MLX fails")
                
            elif "NVIDIA" in device_name or device == "cuda":
                # NVIDIA GPU - use original model (sentence-transformers compatible)
                model_options = [
                    "Qwen/Qwen3-Embedding-4B"  # Original model (best compatibility)
                ]
                logger.info("Using NVIDIA CUDA optimized model")
                
            elif "Intel" in device_name or device == "xpu":
                # Intel GPU/XPU - use original model
                model_options = [
                    "Qwen/Qwen3-Embedding-4B"  # Original model (best compatibility)
                ]
                logger.info("Using Intel XPU optimized model")
                
            elif "AMD" in device_name or device == "hip":
                # AMD GPU - use original model
                model_options = [
                    "Qwen/Qwen3-Embedding-4B"  # Original model (best compatibility)
                ]
                logger.info("Using AMD HIP optimized model")
                
            else:
                # CPU or unknown - fallback to API instead of slow CPU processing
                logger.warning("No accelerator available (CPU only) - falling back to API processing")
                logger.warning("Disabling ondevice processing to use API instead of slow CPU processing")
                self._ondevice_processing_disabled = True
                return None
            
            # Try each model option in order of preference
            for model_name in model_options:
                try:
                    # Try with memory optimization for CUDA
                    if device == "cuda":
                        import torch

                        torch.cuda.empty_cache()  # Clear CUDA cache before loading
                        # Try with lower precision
                        model = SentenceTransformer(model_name, device=device)
                        # Move to CPU if CUDA fails
                        if hasattr(model, "to"):
                            model = model.to("cpu")
                            logger.info(f"Loaded {model_name} on CPU due to CUDA memory constraints")
                        else:
                            logger.info(f"Loaded {model_name} on {device}")
                    else:
                        model = SentenceTransformer(model_name, device=device)
                        logger.info(f"Loaded {model_name} on {device}")
                    
                    if "4bit" in model_name or "Q4" in model_name or "W4" in model_name:
                        logger.info(f"Loaded quantized {model_name}")
                    else:
                        logger.info(f"Loaded original {model_name}")
                    return model
                except Exception as e:
                    logger.warning(f"Failed to load {model_name}: {e}")
                    # Try CPU fallback for CUDA errors
                    if device == "cuda" and "CUDA out of memory" in str(e):
                        logger.warning("CUDA out of memory - falling back to API processing instead of slow CPU")
                        logger.warning("Disabling ondevice processing to use API instead of slow CPU processing")
                        self._ondevice_processing_disabled = True
                        return None
                    continue
            
            # Final fallback - use API instead of slow CPU processing
            logger.warning("All primary models failed - falling back to API processing instead of slow CPU")
            logger.warning("Disabling ondevice processing to use API instead of slow CPU processing")
            self._ondevice_processing_disabled = True
            return None
            
        except Exception as e:
            logger.error(f"Error loading optimized quantized model: {e}")
            return None

    def _get_local_embedder(self) -> object:
        """Get local embedder optimized for the current platform"""
        from papr_memory._logging import get_logger

        logger = get_logger(__name__)
        
        try:
            # Check if platform is too old for local processing
            if self._is_old_platform():
                logger.info("Platform detected as too old - skipping local embedding generation")
                return None
                
            import platform
            import subprocess

            import torch
            
            # Detect platform and set optimal device (NPU first, then GPU, then CPU)
            device = None
            device_name = None
            
            # 1. Check for Apple Silicon NPU (highest priority for NPU platforms)
            if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
                device = "mps"  # Apple Silicon (includes NPU via MPS)
                # Check if we're on Apple Silicon with Neural Engine
                if platform.system() == "Darwin":
                    try:
                        # Check for Apple Silicon chip
                        result = subprocess.run(
                            ["sysctl", "-n", "machdep.cpu.brand_string"], capture_output=True, text=True, timeout=5
                        )
                        if result.returncode == 0 and "Apple" in result.stdout:
                            device_name = "Apple Silicon with Neural Engine NPU (via MPS)"
                        else:
                            device_name = "Apple Metal Performance Shaders (MPS)"
                    except Exception:
                        device_name = "Apple Metal Performance Shaders (MPS) - includes Neural Engine NPU"
                else:
                    device_name = "Apple Metal Performance Shaders (MPS) - includes Neural Engine NPU"
            
            # 2. Check for Intel NPU (Intel Arc with NPU)
            elif (
                hasattr(torch.backends, "xpu")
                and getattr(torch.backends, "xpu", None)
                and hasattr(getattr(torch.backends, "xpu", None), "is_available")
                and getattr(torch.backends, "xpu", None).is_available()  # type: ignore
            ):
                device = "xpu"  # Intel GPU (Arc, Xe) - may include NPU
                device_name = "Intel XPU (Arc/Xe with potential NPU)"
            
            # 3. Fallback to traditional GPUs
            elif torch.cuda.is_available():
                device = "cuda"
                device_name = "NVIDIA CUDA GPU"
            elif (
                hasattr(torch.backends, "hip")
                and getattr(torch.backends, "hip", None)
                and hasattr(getattr(torch.backends, "hip", None), "is_available")
                and getattr(torch.backends, "hip", None).is_available()  # type: ignore
            ):
                device = "hip"  # AMD GPU (ROCm)
                device_name = "AMD HIP/ROCm GPU"
            
            # 4. Final fallback to CPU
            if device is None:
                device = "cpu"
                device_name = "CPU"
            
            # Ensure device_name is never None
            if device_name is None:
                device_name = "CPU"
            
            logger.info(f"Using {device_name} for embeddings")
            
            # Use platform-optimized quantized Qwen3-Embedding-4B model
            model = self._get_optimized_quantized_model(device, device_name)
            return model
            
        except ImportError:
            logger.warning("sentence-transformers not available - install with: pip install sentence-transformers")
            return None
        except Exception as e:
            logger.error(f"Error initializing local embedder: {e}")
            return None

    def _embed_query_locally(self, query: str) -> list[float] | None:
        """Generate embedding for query using local hardware"""
        from papr_memory._logging import get_logger

        logger = get_logger(__name__)
        
        # Use cached embedder if available, otherwise get new one
        if not hasattr(self, "_local_embedder") or self._local_embedder is None:  # type: ignore
            self._local_embedder = self._get_local_embedder()
        
        embedder = self._local_embedder
        if embedder:
            try:
                import time

                start_time = time.time()
                embedding = getattr(embedder, 'encode', lambda _: None)([query])[0].tolist()  # type: ignore
                generation_time = time.time() - start_time
                logger.info(f"Generated local query embedding (dim: {len(embedding)}) in {generation_time:.2f}s")
                return embedding  # type: ignore
            except Exception as e:
                logger.error(f"Error generating local embedding: {e}")
        else:
            logger.info("Local embedding generation skipped - using API-based search")
        return None

    def _optimize_chromadb_collection(self) -> None:
        """Optimize ChromaDB collection for better performance"""
        from papr_memory._logging import get_logger

        logger = get_logger(__name__)
        
        try:
            if hasattr(self, "_chroma_collection") and self._chroma_collection is not None:  # type: ignore
                logger.info("Optimizing ChromaDB collection for performance...")

                # Get collection info to verify optimization settings
                collection_info = self._chroma_collection.get()  # type: ignore
                logger.info(f"Collection contains {len(collection_info['ids'])} documents")

                # Log optimization settings
                logger.info("ChromaDB collection optimized with:")
                logger.info("  - HNSW index with cosine similarity")
                logger.info("  - Construction EF: 200 (high quality index)")
                logger.info("  - Search EF: 50 (balanced speed/accuracy)")
                logger.info("  - M: 16 (high recall)")
                logger.info("  - DuckDB backend for better performance")

                logger.info("✅ ChromaDB collection optimization completed")
            else:
                logger.warning("No ChromaDB collection available for optimization")

        except Exception as e:
            logger.warning(f"Failed to optimize ChromaDB collection: {e}")

    def _start_background_sync(self) -> None:
        """Start background sync task for periodic tier0 data updates"""
        global _background_sync_task, _global_sync_lock
        import os
        import threading

        from papr_memory._logging import get_logger

        logger = get_logger(__name__)

        # Initialize global sync lock if not exists
        if _global_sync_lock is None:
            _global_sync_lock = threading.Lock()

        # Use thread-safe singleton pattern
        with _global_sync_lock:
            # Check if background sync task exists and is alive
            if _background_sync_task is None:
                logger.info("No background sync task found")
            elif not _background_sync_task.is_alive():
                logger.warning("Background sync task died, will restart")
                _background_sync_task = None
            else:
                logger.info("Background sync task already running (shared across clients)")
                return

            # Start new background sync task
            current_interval = int(os.environ.get("PAPR_SYNC_INTERVAL", "300"))
            logger.info(f"Starting background sync task (every {current_interval}s)")

            _background_sync_task = threading.Thread(
                target=self._background_sync_worker, daemon=True, name="PaprBackgroundSync"
            )
            _background_sync_task.start()
            logger.info("Background sync task started successfully")

    def _start_background_model_loading(self) -> None:
        """Start background model loading for non-blocking initialization"""
        global _background_model_loading_task, _model_loading_complete, _global_sync_lock, _global_qwen_model

        from papr_memory._logging import get_logger

        logger = get_logger(__name__)

        # Initialize global sync lock if not exists
        if _global_sync_lock is None:
            _global_sync_lock = threading.Lock()

        # Use thread-safe singleton pattern
        with _global_sync_lock:
            # Check if model loading is already complete
            if _model_loading_complete:
                logger.info("Model loading already complete")
                return

            # Check if model is already loaded globally
            if _global_qwen_model is not None:
                logger.info("Model already loaded globally, marking as complete")
                _model_loading_complete = True
                return
            
            # Check if model is already loaded in ChromaDB collection
            if hasattr(self, "_chroma_collection") and self._chroma_collection is not None:
                embedding_function = getattr(self._chroma_collection, "_embedding_function", None)
                if embedding_function is not None and hasattr(embedding_function, "model"):
                    logger.info("Model already loaded in ChromaDB collection, marking as complete")
                    _global_qwen_model = embedding_function.model
                    _model_loading_complete = True
                    return

            # Check if background model loading task exists and is alive
            if _background_model_loading_task is None:
                logger.info("Starting background model loading...")
            elif not _background_model_loading_task.is_alive():
                logger.warning("Background model loading task died, will restart")
                _background_model_loading_task = None
            else:
                logger.info("Background model loading already running (shared across clients)")
                return

            # Start new background model loading task
            _model_loading_complete = False
            
            _background_model_loading_task = threading.Thread(
                target=self._background_model_loading_worker,
                name="PaprModelLoading",
                daemon=True
            )
            _background_model_loading_task.start()
            logger.info("Background model loading started")
        
        # Set completion callback for better user experience
        def on_model_loading_complete():
            logger.info("🎉 Background model loading finished - local search is now optimized!")
        
        global _model_loading_callback
        _model_loading_callback = on_model_loading_complete

    def _start_background_initialization(self) -> None:
        """Start complete background initialization (sync_tiers + ChromaDB + model loading)"""
        global _background_initialization_task, _global_sync_lock

        from papr_memory._logging import get_logger

        logger = get_logger(__name__)

        # Initialize global sync lock if not exists
        if _global_sync_lock is None:
            _global_sync_lock = threading.Lock()

        # Use thread-safe singleton pattern
        with _global_sync_lock:
            # Check if background initialization is already running
            if _background_initialization_task is not None and _background_initialization_task.is_alive():
                logger.info("Background initialization already running (shared across clients)")
                return

            # Check if initialization is already complete
            if hasattr(self, "_collection_initialized") and self._collection_initialized:  # type: ignore
                logger.info("Background initialization already completed")
                return

            logger.info("Starting complete background initialization...")
            
            # Start background initialization worker
            _background_initialization_task = threading.Thread(
                target=self._background_initialization_worker,
                name="PaprBackgroundInit",
                daemon=True
            )
            _background_initialization_task.start()
        logger.info("Background initialization started")

    def _background_initialization_worker(self) -> None:
        """Background worker for complete initialization"""
        from papr_memory._logging import get_logger

        logger = get_logger(__name__)

        try:
            logger.info("🚀 Background initialization worker started")
            
            # Step 1: Initialize sync_tiers and ChromaDB collection (immediate)
            logger.info("📡 Initializing sync_tiers and ChromaDB collection...")
            self._process_sync_tiers_and_store()
            logger.info("✅ Sync_tiers and ChromaDB collection initialized")
            
            # Step 2: Start background model loading
            logger.info("🤖 Starting background model loading...")
            self._start_background_model_loading()
            
            # Step 3: Start background sync task (will wait for next interval)
            logger.info("🔄 Starting background sync task...")
            self._start_background_sync()
            
            logger.info("🎉 Complete background initialization finished!")
            
        except Exception as e:
            logger.error(f"Background initialization failed: {e}")

    def _get_model_loading_status(self) -> dict[str, any]:  # type: ignore
        """Get model loading status for debugging"""
        global _background_model_loading_task, _model_loading_complete

        from papr_memory._logging import get_logger

        logger = get_logger(__name__)

        if _background_model_loading_task is None:
            return {"status": "not_started", "complete": False, "alive": False}
        elif _background_model_loading_task.is_alive():
            return {
                "status": "loading",
                "complete": _model_loading_complete,
                "alive": True,
                "name": _background_model_loading_task.name,
            }
        else:
            return {
                "status": "completed" if _model_loading_complete else "failed",
                "complete": _model_loading_complete,
                "alive": False,
                "name": _background_model_loading_task.name,
            }

    def _background_model_loading_worker(self) -> None:
        """Background worker for model loading"""
        import time
        global _model_loading_complete, _global_qwen_model

        from papr_memory._logging import get_logger

        logger = get_logger(__name__)

        try:
            logger.info("Background model loading worker started")
            
            # Check if model is already loaded
            if _global_qwen_model is not None:
                logger.info("Model already loaded globally, marking as complete")
                _model_loading_complete = True
                logger.info("🚀 Model is now ready for fast local search!")
                return
            
            # Start timing
            model_load_start = time.time()
            logger.info(f"⏱️ Model loading started at {time.strftime('%H:%M:%S', time.localtime(model_load_start))}")
            
            # Load the embedding model in the background
            self._preload_embedding_model()
            
            # Calculate timing
            model_load_end = time.time()
            model_load_duration = model_load_end - model_load_start
            
            _model_loading_complete = True
            logger.info(f"✅ Background model loading completed successfully in {model_load_duration:.2f}s")
            logger.info(f"⏱️ Model loading finished at {time.strftime('%H:%M:%S', time.localtime(model_load_end))}")
            logger.info("🚀 Model is now ready for fast local search!")
            
            # Call completion callback if set
            global _model_loading_callback
            if _model_loading_callback:
                try:
                    _model_loading_callback()
                except Exception as callback_error:
                    logger.warning(f"Model loading callback failed: {callback_error}")
            
            logger.info("🎉 Background model loading finished - local search is now optimized!")
            
        except Exception as e:
            # Calculate timing even on failure
            model_load_end = time.time()
            model_load_duration = model_load_end - model_load_start if 'model_load_start' in locals() else 0
            
            logger.error(f"❌ Background model loading FAILED after {model_load_duration:.2f}s: {e}")
            logger.error(f"⏱️ Model loading failed at {time.strftime('%H:%M:%S', time.localtime(model_load_end))}")
            logger.warning("⚠️ Local search will fallback to server-side processing")
            _model_loading_complete = False

    def _get_background_sync_status(self) -> dict[str, any]:  # type: ignore
        """Get background sync task status for debugging"""
        global _background_sync_task
        from papr_memory._logging import get_logger

        logger = get_logger(__name__)

        if _background_sync_task is None:
            return {"status": "not_started", "alive": False, "name": None}
        elif _background_sync_task.is_alive():
            return {
                "status": "running",
                "alive": True,
                "name": _background_sync_task.name,
                "daemon": _background_sync_task.daemon,
            }
        else:
            return {"status": "dead", "alive": False, "name": _background_sync_task.name}

    def _background_sync_worker(self) -> None:
        """Background worker that periodically syncs tier0 data"""
        import os
        import time
        import signal
        import threading

        from papr_memory._logging import get_logger

        logger = get_logger(__name__)

        # Set up graceful shutdown handling
        def signal_handler(signum: int, _frame: object) -> None:
            logger.info(f"Background sync received signal {signum}, shutting down gracefully...")
            # The daemon thread will exit automatically when main thread exits

        # Register signal handlers for graceful shutdown (main thread only)
        if threading.current_thread() is threading.main_thread():
            try:
                signal.signal(signal.SIGTERM, signal_handler)
                signal.signal(signal.SIGINT, signal_handler)
            except Exception:
                # Some environments may not allow signal registration; continue without it
                pass

        logger.info("Background sync worker started")

        while True:
            try:
                # Check if we should exit (daemon threads exit when main thread exits)
                if not threading.main_thread().is_alive():
                    logger.info("Main thread died, background sync exiting...")
                    break

                # Get current sync interval (may have changed via environment variable)
                current_interval = int(os.environ.get("PAPR_SYNC_INTERVAL", "300"))
                logger.info(f"Background sync: Waiting {current_interval}s before next sync...")
                time.sleep(current_interval)

                logger.info("Background sync: Updating tier0 data...")
                self._process_sync_tiers_and_store()
                logger.info("Background sync: Completed successfully")
            except KeyboardInterrupt:
                logger.info("Background sync interrupted by user, exiting...")
                break
            except Exception as e:
                logger.error(f"Background sync failed: {e}")
                # Continue running even if sync fails
                time.sleep(5)  # Brief pause before retrying

        logger.info("Background sync worker stopped")

    def _preload_embedding_model(self) -> None:
        """Preload the embedding model during client initialization to avoid loading overhead during search"""
        global _global_qwen_model

        from papr_memory._logging import get_logger
        from papr_memory._retrieval_logging import retrieval_logging_service

        logger = get_logger(__name__)

        # Preload CoreML model if enabled (prevents slow first search)
        if os.environ.get("PAPR_ENABLE_COREML", "").lower() == "true":
            logger.info("🚀 Core ML is enabled - preloading model...")
            try:
                self._warmup_coreml_model()
                logger.info("✅ Core ML model preloaded successfully")
            except Exception as e:
                logger.warning(f"⚠️  Core ML preload failed: {e}. Will load on first search.")
            return
        if os.environ.get("PAPR_ENABLE_MLX", "").lower() == "true":
            logger.info("⏭️  Skipping ST preload: MLX is enabled (faster, less memory)")
            return
        if os.environ.get("PAPR_DISABLE_ST_PRELOAD", "").lower() == "true":
            logger.info("⏭️  Skipping ST preload: PAPR_DISABLE_ST_PRELOAD=true")
            return

        try:
            if _global_qwen_model is None:
                # Use thread-safe singleton pattern for model loading
                global _global_sync_lock
                import threading
                if _global_sync_lock is None:
                    _global_sync_lock = threading.Lock()
                
                with _global_sync_lock:
                    # Double-check after acquiring lock
                    if _global_qwen_model is None:
                        # Start timing for model loading
                        import time
                        model_start = time.time()
                        logger.info(f"⏱️ Model loading started at {time.strftime('%H:%M:%S', time.localtime(model_start))}")

                        # Load model with timeout protection
                        import threading

                        import torch
                from sentence_transformers import SentenceTransformer

                # Detect platform
                device = None
                if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
                    device = "mps"
                elif torch.cuda.is_available():
                    device = "cuda"
                else:
                    device = "cpu"

                # Load model with timeout protection
                model_loading_success = False
                
                def load_model_with_timeout():
                    nonlocal model_loading_success
                    try:
                        # Load Qwen3-4B model directly
                        global _global_qwen_model
                        _global_qwen_model = SentenceTransformer("Qwen/Qwen3-Embedding-4B", device=device)

                        # Optimize model for inference
                        _global_qwen_model.eval()  # type: ignore
                        
                        # Warm up the model with a dummy query to ensure it's ready
                        dummy_query = "warmup"
                        _ = _global_qwen_model.encode([dummy_query])  # type: ignore
                        
                        model_loading_success = True
                        
                    except Exception as model_error:
                        logger.error(f"Model loading failed: {model_error}")
                        model_loading_success = False

                # Start model loading in a separate thread with timeout
                model_thread = threading.Thread(target=load_model_with_timeout, daemon=True)
                model_thread.start()
                
                # Wait for model loading with timeout (60 seconds)
                model_thread.join(timeout=60.0)
                
                if not model_loading_success or _global_qwen_model is None:
                    logger.error("Model loading failed or timed out")
                    return
                
                # Calculate and log model loading time
                model_end = time.time()
                model_duration = model_end - model_start
                logger.info(f"✅ Preloaded Qwen3-4B model on {device} - ready for fast inference")
                logger.info(f"⏱️ Model loading completed in {model_duration:.2f}s")
                logger.info(f"⏱️ Model loading finished at {time.strftime('%H:%M:%S', time.localtime(model_end))}")
                
                # Log model loading metrics
                retrieval_logging_service.log_model_loading_metrics(
                    "Qwen/Qwen3-Embedding-4B", 
                    model_duration * 1000,  # Convert to milliseconds
                    device
                )

                # Set instance reference to global model
                self._qwen_model = _global_qwen_model  # type: ignore
            else:
                logger.info("Embedding model already loaded (singleton)")
                # Set instance reference to global model
                self._qwen_model = _global_qwen_model  # type: ignore

        except Exception as e:
            # Calculate timing even on failure
            model_end = time.time()
            model_duration = model_end - model_start if 'model_start' in locals() else 0
            
            logger.error(f"❌ Model loading FAILED after {model_duration:.2f}s: {e}")
            logger.error(f"⏱️ Model loading failed at {time.strftime('%H:%M:%S', time.localtime(model_end))}")
            logger.warning("⚠️ Model will be loaded on-demand during search")

    async def _preload_embedding_model_async(self) -> None:
        """Preload the embedding model during async client initialization to avoid loading overhead during search"""
        from papr_memory._logging import get_logger

        logger = get_logger(__name__)

        # Preload CoreML model if enabled (prevents slow first search)
        if os.environ.get("PAPR_ENABLE_COREML", "").lower() == "true":
            logger.info("🚀 Core ML is enabled - preloading model...")
            try:
                self._warmup_coreml_model()
                logger.info("✅ Core ML model preloaded successfully")
            except Exception as e:
                logger.warning(f"⚠️  Core ML preload failed: {e}. Will load on first search.")
            return
        if os.environ.get("PAPR_ENABLE_MLX", "").lower() == "true":
            logger.info("⏭️  Skipping ST preload: MLX is enabled (faster, less memory)")
            return
        if os.environ.get("PAPR_DISABLE_ST_PRELOAD", "").lower() == "true":
            logger.info("⏭️  Skipping ST preload: PAPR_DISABLE_ST_PRELOAD=true")
            return

        try:
            if not hasattr(self, "_qwen_model") or self._qwen_model is None:
                logger.info("Preloading Qwen3-4B embedding model (async)...")
                import torch
                from sentence_transformers import SentenceTransformer
                
                # Detect platform
                device = None
                if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
                    device = "mps"
                elif torch.cuda.is_available():
                    device = "cuda"
                else:
                    device = "cpu"
                
                # Load Qwen3-4B model directly
                self._qwen_model = SentenceTransformer("Qwen/Qwen3-Embedding-4B", device=device)

                # Optimize model for inference
                self._qwen_model.eval()

                # Warm up the model with a dummy query to ensure it's ready
                dummy_query = "warmup"
                _ = self._qwen_model.encode([dummy_query])

                logger.info(f"✅ Preloaded Qwen3-4B model on {device} - ready for fast inference")
            else:
                logger.info("Embedding model already loaded")

        except Exception as e:
            logger.warning(f"Failed to preload embedding model: {e}")
            logger.warning("Model will be loaded on-demand during search")

    def _warmup_coreml_model(self) -> None:
        """Preload and warm up CoreML model to avoid slow first search"""
        global _global_coreml_model, _global_coreml_tokenizer, _global_model_cache_lock
        from papr_memory._logging import get_logger
        import numpy as np

        logger = get_logger(__name__)

        # Thread-safe warmup to prevent race conditions
        with _global_model_cache_lock:
            # Check if already loaded
            if _global_coreml_model is not None:
                logger.info("CoreML model already cached globally, skipping warmup")
                return

            try:
                import coremltools as ct
                from transformers import AutoTokenizer
                from papr_memory._model_cache import resolve_coreml_model_path

                # Get CoreML model path
                coreml_path_env = os.environ.get("PAPR_COREML_MODEL")
                coreml_path = resolve_coreml_model_path(coreml_path_env)
                tok_id = os.environ.get("PAPR_EMBEDDING_MODEL", "Qwen/Qwen3-Embedding-4B")

                logger.info(f"Loading CoreML model from {coreml_path}...")

                # Get compute units from environment or use CPU_AND_NE for ANE
                compute_unit_str = os.environ.get("PAPR_COREML_COMPUTE_UNITS", "CPU_AND_NE")
                compute_unit_map = {
                    "ALL": ct.ComputeUnit.ALL,
                    "CPU_AND_GPU": ct.ComputeUnit.CPU_AND_GPU,
                    "CPU_AND_NE": ct.ComputeUnit.CPU_AND_NE,
                    "CPU_ONLY": ct.ComputeUnit.CPU_ONLY,
                }
                requested_compute_unit = compute_unit_map.get(compute_unit_str, ct.ComputeUnit.CPU_AND_NE)
                
                # Load model with fallback
                mlmodel = None
                try:
                    mlmodel = ct.models.MLModel(coreml_path, compute_units=requested_compute_unit)
                    logger.info(f"✅ CoreML model loaded in warmup with {compute_unit_str}")
                except Exception as e:
                    logger.warning(f"⚠️  Failed to load model with {compute_unit_str}: {e}")
                    if requested_compute_unit != ct.ComputeUnit.ALL:
                        logger.info(f"🔄 Falling back to compute_units=ALL in warmup")
                        mlmodel = ct.models.MLModel(coreml_path, compute_units=ct.ComputeUnit.ALL)
                    else:
                        raise
                
                tokenizer = AutoTokenizer.from_pretrained(tok_id)

                logger.info("Running warmup inference to compile model...")

                # Run a warmup inference to trigger compilation
                # This takes ~60s first time, but macOS caches the compiled model
                warmup_text = "warmup query"
                enc = tokenizer(
                    [warmup_text],
                    padding="max_length",
                    max_length=32,
                    truncation=True,
                    return_tensors="np",
                )
                feed = {
                    "input_ids": enc["input_ids"].astype(np.int32),
                    "attention_mask": enc["attention_mask"].astype(np.int32),
                }

                # First inference triggers compilation and caching
                _ = mlmodel.predict(feed)

                # Store in global cache for reuse
                _global_coreml_model = mlmodel
                _global_coreml_tokenizer = tokenizer

                logger.info("✅ CoreML model preloaded and compiled successfully")
                logger.info(f"   Model cached globally for reuse (no reload needed)")
                logger.info(f"   macOS also cached at: ~/Library/Caches/com.apple.CoreML/")
                logger.info(f"   Future app starts will be faster (~1-2s vs ~60s)")

            except Exception as e:
                logger.warning(f"CoreML warmup failed: {e}")
                logger.warning("Model will be loaded on first search (may take 60+ seconds)")

    def _embed_query_with_qwen(self, query: str) -> list[float] | None:
        """Generate embedding for query using preloaded Qwen3-4B model"""
        global _global_qwen_model
        from papr_memory._logging import get_logger

        logger = get_logger(__name__)

        try:
            # Use the global singleton model if available
            if _global_qwen_model is not None:
                logger.info("Using preloaded Qwen3-4B model for query embedding")
                model = _global_qwen_model
            elif hasattr(self, "_qwen_model") and self._qwen_model is not None:
                logger.info("Using instance Qwen3-4B model for query embedding")
                model = self._qwen_model
            else:
                logger.warning("No preloaded model available, loading on-demand...")
                import torch
                from sentence_transformers import SentenceTransformer

                # Detect platform
                device = None
                if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
                    device = "mps"
                elif torch.cuda.is_available():
                    device = "cuda"
                else:
                    device = "cpu"

                try:
                    # Load Qwen3-4B model directly
                    model = SentenceTransformer("Qwen/Qwen3-Embedding-4B", device=device)
                    logger.info(f"Loaded Qwen3-4B model on {device}")
                except Exception as e:
                    if "meta tensor" in str(e).lower():
                        logger.warning("Meta tensor issue detected, trying CPU fallback...")
                        model = SentenceTransformer("Qwen/Qwen3-Embedding-4B", device="cpu")
                        logger.info("Loaded Qwen3-4B model on CPU (fallback)")
                    else:
                        raise e
            
            import time

            start_time = time.time()
            # Generate embedding using the model
            raw_embedding = getattr(model, 'encode', lambda _: None)([query])[0]  # type: ignore
            logger.info(f"Raw Qwen3-4B embedding: shape={raw_embedding.shape}, type={type(raw_embedding)}")
            
            embedding = raw_embedding.tolist()
            generation_time = time.time() - start_time
            logger.info(f"Generated Qwen3-4B query embedding (dim: {len(embedding)}) in {generation_time:.2f}s")
            return embedding  # type: ignore
            
        except Exception as e:
            logger.error(f"Error generating Qwen3-4B embedding: {e}")
            return None

    def _get_qwen_embedding_function(self) -> object:
        """Get Qwen-based embedding function for ChromaDB using the correct interface with timeout protection"""
        import threading

        from papr_memory._logging import get_logger

        logger = get_logger(__name__)
        
        try:
            logger.info("Creating Qwen embedding function...")
            
            # Use the preloaded global model if available (fastest path)
            if _global_qwen_model is not None:
                logger.info("Using preloaded global Qwen model for embedding function")
                model = _global_qwen_model
            else:
                # Fallback: create a new model instance with timeout protection
                logger.info("Creating new Qwen model instance for embedding function")
            import torch
            
            # Detect platform (NPU first, then GPU, then CPU)
            device = None
            
            # 1. Check for Apple Silicon NPU (highest priority for NPU platforms)
            if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
                device = "mps"  # Apple Silicon (includes NPU via MPS)
            # 2. Check for Intel NPU (Intel Arc with NPU)
            elif (
                hasattr(torch.backends, "xpu")
                and getattr(torch.backends, "xpu", None)
                and hasattr(getattr(torch.backends, "xpu", None), "is_available")
                and getattr(torch.backends, "xpu", None).is_available()  # type: ignore
            ):
                device = "xpu"  # Intel GPU (Arc, Xe) - may include NPU
            # 3. Fallback to traditional GPUs
            elif torch.cuda.is_available():
                device = "cuda"
                logger.info("Using NVIDIA CUDA GPU for embeddings")
            elif (
                hasattr(torch.backends, "hip")
                and getattr(torch.backends, "hip", None)
                and hasattr(getattr(torch.backends, "hip", None), "is_available")
                and getattr(torch.backends, "hip", None).is_available()  # type: ignore
            ):
                device = "hip"  # AMD GPU (ROCm)
            # 4. Final fallback to CPU
            if device is None:
                device = "cpu"
            
            # Load model with timeout protection
            model = None
            model_loading_success = False
            
            def load_model_with_timeout():
                nonlocal model, model_loading_success
                try:
                    from sentence_transformers import SentenceTransformer
                    
                    # Try to load with CUDA first
                    if device == "cuda":
                        try:
                            model = SentenceTransformer("Qwen/Qwen3-Embedding-4B", device=device)
                            logger.info("Using NVIDIA CUDA optimized model")
                        except Exception as cuda_error:
                            logger.warning(f"CUDA loading failed: {cuda_error}")
                            logger.info("Falling back to CPU loading...")
                            model = SentenceTransformer("Qwen/Qwen3-Embedding-4B", device="cpu")
                            logger.info("Loaded Qwen/Qwen3-Embedding-4B on CPU due to CUDA memory constraints")
                    else:
                        model = SentenceTransformer("Qwen/Qwen3-Embedding-4B", device=device)
                        logger.info("Loaded original Qwen/Qwen3-Embedding-4B")

                    # Optimize model for inference
                    model.eval()
                    model_loading_success = True
                    
                except Exception as model_error:
                    logger.error(f"Failed to load Qwen model: {model_error}")
                    model_loading_success = False

            # Start model loading in a separate thread with timeout
            model_thread = threading.Thread(target=load_model_with_timeout, daemon=True)
            model_thread.start()
            
            # Wait for model loading with timeout (30 seconds)
            model_thread.join(timeout=30.0)
            
            if not model_loading_success or model is None:
                logger.error("Model loading failed or timed out")
                # Fallback to default embedding function
                logger.warning("Falling back to default ChromaDB embedding function")
                return None
            
            # Create a proper ChromaDB embedding function class
            class QwenEmbeddingFunction:
                def __init__(self, model: any) -> None:  # type: ignore
                    self.model = model
                    # Set global model reference to avoid redundant loading
                    global _global_qwen_model
                    _global_qwen_model = model
                
                def __call__(self, input: any) -> any:  # type: ignore
                    # Handle both single string and list of strings
                    if isinstance(input, str):
                        input = [input]
                    # Support either ST model or embedding-function interface
                    if hasattr(self.model, "embed_documents"):
                        embs = self.model.embed_documents(input)  # type: ignore
                        return embs  # already a list[list[float]]
                    embeddings = self.model.encode(input)  # type: ignore
                    return embeddings.tolist()  # type: ignore

                def embed_query(self, input: any) -> any:  # type: ignore
                    # Method required by ChromaDB for query embedding
                    try:
                        if hasattr(self.model, "embed_documents"):
                            embs = self.model.embed_documents([input])  # type: ignore
                            return embs[0]
                        embeddings = self.model.encode([input])  # type: ignore
                        if len(embeddings) > 0:
                            return embeddings[0].tolist()  # type: ignore
                            # Fallback: encode single input directly
                        return self.model.encode(input).tolist()  # type: ignore
                    except Exception as e:
                        # Fallback: encode single input directly
                        return self.model.encode(input).tolist()  # type: ignore
                
                def embed_documents(self, input: any) -> any:  # type: ignore
                    # Method required by ChromaDB for document embedding
                    try:
                        if isinstance(input, str):
                            input = [input]
                        if hasattr(self.model, "embed_documents"):
                            return self.model.embed_documents(input)  # type: ignore
                        return self.model.encode(input).tolist()  # type: ignore
                    except Exception as e:
                        # Fallback: handle single string
                        return self.model.encode([input]).tolist()  # type: ignore
            
            embedding_function = QwenEmbeddingFunction(model)  # type: ignore
            logger.info(f"Qwen embedding function created successfully: {embedding_function is not None}")
            return embedding_function
            
        except Exception as e:
            logger.error(f"Error creating Qwen embedding function: {e}")
            return None

    def _search_both_collections(
        self,
        query: str,
        n_results: int = 5,
        metadata: Optional[MemoryMetadataParam] | NotGiven = not_given,
        user_id: Optional[str] | NotGiven = not_given,
        external_user_id: Optional[str] | NotGiven = not_given
    ) -> list[tuple[str, float, str]] | None:
        """
        Search BOTH tier0 and tier1 collections in parallel using a single embedding.
        
        Returns list of tuples: (document, distance, tier_label)
        """
        import time
        import threading
        from typing import List, Tuple, Optional as TypingOptional

        from papr_memory._logging import get_logger
        from papr_memory._retrieval_logging import retrieval_logging_service

        logger = get_logger(__name__)
        
        # Check if both collections exist
        has_tier0 = hasattr(self, "_chroma_collection") and self._chroma_collection is not None
        has_tier1 = hasattr(self, "_chroma_tier1_collection") and self._chroma_tier1_collection is not None
        
        if not has_tier0 and not has_tier1:
            logger.warning("No ChromaDB collections available for search")
            return []
        
        # Start retrieval metrics tracking
        metrics = retrieval_logging_service.start_query_timing(query)
        
        try:
            # ===== STEP 1: Generate embedding ONCE =====
            retrieval_logging_service.start_embedding_timing(metrics)
            embedding_start = time.time()
            
            # Get embedder (prefer CoreML if available)
            embedder: object | None = None
            if has_tier0 and hasattr(self._chroma_collection, "_embedding_function"):
                ef = getattr(self._chroma_collection, "_embedding_function", None)
                if ef is not None and not ("DefaultEmbeddingFunction" in str(ef.__class__)):
                    embedder = ef
            
            if embedder is None:
                embedder = getattr(self, "_local_embedder", None)
                if embedder is None:
                    embedder = self._get_local_embedder()
            
            # Helper function to generate embedding
            def _embed_with(obj: object, text: str) -> list[float] | None:
                try:
                    if hasattr(obj, "embed_query"):
                        out = obj.embed_query(text)  # type: ignore
                        import numpy as _np
                        if isinstance(out, _np.ndarray):
                            return out.astype(_np.float32).tolist()
                        if isinstance(out, list):
                            if out and isinstance(out[0], list):
                                return [float(x) for x in out[0]]
                            return [float(x) for x in out]
                    if hasattr(obj, "encode"):
                        enc = obj.encode([text])  # type: ignore
                        import numpy as _np
                        if isinstance(enc, _np.ndarray):
                            return enc[0].astype(_np.float32).tolist()
                        if isinstance(enc, list) and enc:
                            first = enc[0]
                            if hasattr(first, 'tolist'):
                                return first.tolist()
                            if isinstance(first, list):
                                return [float(x) for x in first]
                    if callable(obj):
                        out = obj([text])  # type: ignore
                        import numpy as _np
                        if out and isinstance(out, list):
                            first = out[0]
                            if hasattr(first, 'tolist'):
                                return first.tolist()
                            if isinstance(first, list):
                                return [float(x) for x in first]
                except Exception as e:
                    logger.debug(f"Embedder failed: {e}")
                return None
            
            # Generate embedding once
            query_embedding: list[float] | None = None
            if embedder is not None:
                logger.info("Using local embedder for query (prefers Core ML if enabled)")
                query_embedding = _embed_with(embedder, query)
            
            if not query_embedding:
                logger.info("Local embedder unavailable; using Qwen3-4B model")
                query_embedding = self._embed_query_with_qwen(query)
            
            if not query_embedding:
                logger.error("Failed to generate query embedding")
                return []
            
            embedding_time = (time.time() - embedding_start) * 1000  # Convert to ms
            logger.info(f"✨ Generated embedding ONCE in {embedding_time:.1f}ms (will query both collections)")
            
            retrieval_logging_service.end_embedding_timing(
                metrics,
                len(query_embedding),
                getattr(self, "_model_name", "Qwen3-4B")
            )
            
            # ===== STEP 2: Query both collections IN PARALLEL =====
            retrieval_logging_service.start_chromadb_timing(metrics)
            search_start = time.time()
            
            tier0_results: TypingOptional[dict] = None
            tier1_results: TypingOptional[dict] = None
            tier0_error: TypingOptional[Exception] = None
            tier1_error: TypingOptional[Exception] = None
            
            # Thread-safe query function for tier0
            def query_tier0():
                nonlocal tier0_results, tier0_error
                try:
                    if has_tier0:
                        tier0_results = self._chroma_collection.query(  # type: ignore
                            query_embeddings=[query_embedding],
                            n_results=n_results,
                            include=["documents", "metadatas", "distances"],
                            where=None,
                        )
                except Exception as e:
                    tier0_error = e
                    logger.warning(f"Tier0 query failed: {e}")
            
            # Thread-safe query function for tier1
            def query_tier1():
                nonlocal tier1_results, tier1_error
                try:
                    if has_tier1:
                        tier1_results = self._chroma_tier1_collection.query(  # type: ignore
                            query_embeddings=[query_embedding],
                            n_results=n_results,
                            include=["documents", "metadatas", "distances"],
                            where=None,
                        )
                except Exception as e:
                    tier1_error = e
                    logger.warning(f"Tier1 query failed: {e}")
            
            # Launch both queries in parallel
            tier0_thread = threading.Thread(target=query_tier0) if has_tier0 else None
            tier1_thread = threading.Thread(target=query_tier1) if has_tier1 else None
            
            if tier0_thread:
                tier0_thread.start()
            if tier1_thread:
                tier1_thread.start()
            
            # Wait for both to complete
            if tier0_thread:
                tier0_thread.join()
            if tier1_thread:
                tier1_thread.join()
            
            search_time = (time.time() - search_start) * 1000  # Convert to ms
            logger.info(f"⚡ Queried both collections in parallel in {search_time:.1f}ms")
            
            # ===== STEP 3: Merge results by similarity score =====
            combined_results: List[Tuple[str, float, str]] = []
            
            # Extract tier0 results
            if tier0_results and tier0_results.get("documents") and tier0_results["documents"][0]:
                docs = tier0_results["documents"][0]
                dists = tier0_results.get("distances", [[]])[0] or [0.0] * len(docs)
                for doc, dist in zip(docs, dists):
                    combined_results.append((doc, float(dist), "tier0"))
                logger.info(f"📊 Tier0: {len(docs)} results")
            else:
                logger.info("📊 Tier0: 0 results")
            
            # Extract tier1 results
            if tier1_results and tier1_results.get("documents") and tier1_results["documents"][0]:
                docs = tier1_results["documents"][0]
                dists = tier1_results.get("distances", [[]])[0] or [0.0] * len(docs)
                for doc, dist in zip(docs, dists):
                    combined_results.append((doc, float(dist), "tier1"))
                logger.info(f"📊 Tier1: {len(docs)} results")
            else:
                logger.info("📊 Tier1: 0 results")
            
            # Sort by distance (lower is better) and take top N
            combined_results.sort(key=lambda x: x[1])
            combined_results = combined_results[:n_results]
            
            # Log tier breakdown
            tier0_count = sum(1 for _, _, tier in combined_results if tier == "tier0")
            tier1_count = sum(1 for _, _, tier in combined_results if tier == "tier1")
            logger.info(f"🎯 Final results: {len(combined_results)} total [{tier0_count} tier0, {tier1_count} tier1]")
            
            # End ChromaDB timing
            retrieval_logging_service.end_chromadb_timing(metrics, len(combined_results))
            
            # End query timing
            device_type = "cpu"
            if hasattr(self, "_global_coreml_model") or '_global_coreml_model' in globals():
                device_type = "ane"
            retrieval_logging_service.end_query_timing(metrics, device_type)
            
            # Log preview of top results
            logger.info("=" * 80)
            logger.info(f"📋 TOP RESULTS (from {len(combined_results)} combined)")
            logger.info("=" * 80)
            for idx, (doc, dist, tier) in enumerate(combined_results[:5]):
                similarity = 1.0 - dist
                content_preview = doc[:150] + "..." if len(doc) > 150 else doc
                logger.info(f"[{idx + 1}] {tier.upper()} | Similarity: {similarity:.4f} | {content_preview}")
            logger.info("=" * 80)
            
            return combined_results
            
        except Exception as e:
            logger.error(f"Error in parallel collection search: {e}")
            import traceback
            logger.error(traceback.format_exc())
            return []

    def _search_tier0_locally(
        self, 
        query: str, 
        n_results: int = 5,
        metadata: Optional[MemoryMetadataParam] | NotGiven = not_given,
        user_id: Optional[str] | NotGiven = not_given,
        external_user_id: Optional[str] | NotGiven = not_given
    ) -> list[str] | None:
        """Search tier0 data using local vector search"""
        import time

        from papr_memory._logging import get_logger
        from papr_memory._retrieval_logging import retrieval_logging_service

        logger = get_logger(__name__)
        
        if not hasattr(self, "_chroma_collection") or self._chroma_collection is None:  # type: ignore
            return []
        
        # Start retrieval metrics tracking
        metrics = retrieval_logging_service.start_query_timing(query)
        
        try:
            # Start embedding timing
            retrieval_logging_service.start_embedding_timing(metrics)
            embedding_start = time.time()

            # Prefer Core ML/collection embedder if available; otherwise use local embedder; final fallback: ST preload
            embedder: object | None = None
            coll_func = getattr(self, "_chroma_collection", None)
            if coll_func is not None and hasattr(self._chroma_collection, "_embedding_function"):
                ef = getattr(self._chroma_collection, "_embedding_function", None)
                # Avoid using Chroma DefaultEmbeddingFunction (384-dim) for local query
                ef_is_default = False
                if ef is not None and hasattr(ef, "__class__") and "DefaultEmbeddingFunction" in str(ef.__class__):
                    ef_is_default = True
                if ef is not None and not ef_is_default and (
                    hasattr(ef, "embed_query") or hasattr(ef, "encode") or callable(ef)
                ):
                    embedder = ef

            if embedder is None:
                embedder = getattr(self, "_local_embedder", None)
                if embedder is None:
                    embedder = self._get_local_embedder()

            def _embed_with(obj: object, text: str) -> list[float] | None:
                try:
                    if hasattr(obj, "embed_query"):
                        out = obj.embed_query(text)  # type: ignore
                        import numpy as _np  # local import
                        if isinstance(out, _np.ndarray):
                            return out.astype(_np.float32).tolist()
                        if isinstance(out, list):
                            # If list[list[float]], take first
                            if out and isinstance(out[0], list):
                                return [float(x) for x in out[0]]
                            return [float(x) for x in out]
                        return None
                    if hasattr(obj, "encode"):
                        enc = obj.encode([text])  # type: ignore
                        import numpy as _np
                        if isinstance(enc, _np.ndarray):
                            return enc[0].astype(_np.float32).tolist()
                        if isinstance(enc, list) and enc:
                            first = enc[0]
                            if isinstance(first, _np.ndarray):
                                return first.astype(_np.float32).tolist()
                            if isinstance(first, list):
                                return [float(x) for x in first]
                        return None
                    if callable(obj):
                        out = obj([text])  # type: ignore
                        import numpy as _np
                        if out and isinstance(out, list):
                            first = out[0]
                            if isinstance(first, _np.ndarray):
                                return first.astype(_np.float32).tolist()
                            if isinstance(first, list):
                                return [float(x) for x in first]
                        return None
                except Exception as e:  # pragma: no cover
                    logger.debug(f"Local embedder failed, will fallback: {e}")
                return None

            query_embedding: list[float] | None = None
            if embedder is not None:
                logger.info("Using local embedder for query (prefers Core ML if enabled)")
                query_embedding = _embed_with(embedder, query)

            if not query_embedding:
                logger.info("Local embedder unavailable or failed; using preloaded Qwen3-4B model")
                query_embedding = self._embed_query_with_qwen(query)
            logger.debug(
                f"Using preloaded Qwen3-4B embedder (dim: {len(query_embedding) if query_embedding else 'None'})"
            )

            embedding_time = time.time() - embedding_start
            logger.info(f"Embedding generation took: {embedding_time:.3f}s")
            
            # End embedding timing and log metrics
            retrieval_logging_service.end_embedding_timing(
                metrics, 
                len(query_embedding) if query_embedding else 0,
                getattr(self, "_model_name", "Qwen3-4B")
            )
            
            if not query_embedding:
                return []
            
            # Check for dimension mismatch before querying
            self._check_embedding_dimensions_before_query(query_embedding)

            # Start ChromaDB timing
            retrieval_logging_service.start_chromadb_timing(metrics)
            search_start = time.time()
            
            # Perform vector search in ChromaDB
            try:
                # Optimized ChromaDB query with performance settings
                                results = self._chroma_collection.query(  # type: ignore
                    query_embeddings=[query_embedding],
                    n_results=n_results,
                    # Performance optimizations
                    include=["documents", "metadatas", "distances"],
                    # Use optimized search parameters
                    where=None,  # No filtering for faster search
                )
            except Exception as e:
                if "dimension" in str(e).lower():
                    logger.error(f"Embedding dimension mismatch: {e}")
                    logger.info("Attempting to fix dimension mismatch by recreating collection...")
                    
                    # Try to fix the dimension mismatch immediately
                    if self._fix_dimension_mismatch_immediately():
                        logger.info("Collection recreated successfully, retrying search...")
                        # Retry the search with the new collection
                        try:
                                results = self._chroma_collection.query(  # type: ignore  # type: ignore
                                query_embeddings=[query_embedding],
                                n_results=n_results,
                                # Performance optimizations
                                include=["documents", "metadatas", "distances"],
                                where=None,  # No filtering for faster search
                            )
                        except Exception as retry_e:
                            logger.error(f"Search still failed after collection recreation: {retry_e}")
                            return []
                    else:
                        logger.error("Failed to fix dimension mismatch")
                        logger.info("Falling back to API-only search")
                        return []
                else:
                    raise e
            
            search_time = time.time() - search_start
            logger.info(f"ChromaDB vector search took: {search_time:.3f}s")

            # End ChromaDB timing and log final metrics
            documents_result = results.get("documents")
            num_results = len(documents_result[0]) if documents_result and len(documents_result) > 0 and documents_result[0] else 0
            retrieval_logging_service.end_chromadb_timing(metrics, num_results)
            
            # End query timing and log comprehensive metrics
            # Detect device type: CoreML (ANE), PyTorch (CUDA/MPS), or CPU
            device_type = "cpu"  # default
            if _global_coreml_model is not None:
                device_type = "ane"  # Apple Neural Engine
            elif hasattr(self, "_qwen_model") and self._qwen_model is not None:
                # Check PyTorch model device
                try:
                    import torch
                    model_device = next(self._qwen_model.parameters()).device  # type: ignore
                    if model_device.type == "cuda":
                        device_type = "cuda"
                    elif model_device.type == "mps":
                        device_type = "mps"
                    else:
                        device_type = "cpu"
                except Exception:
                    device_type = "cpu"
            retrieval_logging_service.end_query_timing(metrics, device_type)
            
            # Log to Parse Server (non-blocking) - user resolution will happen in background
            try:
                # Pass search context to Parse Server logging for background user resolution
                search_context = {
                    'query': query,
                    'metadata': metadata if metadata != not_given else None,
                    'user_id': user_id if user_id != not_given else None,
                    'external_user_id': external_user_id if external_user_id != not_given else None
                }
                
                retrieval_logging_service.log_to_parse_server_sync(
                    metrics, 
                    search_context=search_context,
                    ranking_enabled=True  # Default to True, can be made configurable
                )
            except Exception as parse_e:
                logger.warning(f"Parse Server logging failed: {parse_e}")

            documents_result = results.get("documents")
            if documents_result and len(documents_result) > 0 and documents_result[0]:
                logger.info(f"Found {len(documents_result[0])} relevant tier0 items locally")

                # Return tuples of (document, distance) for score calculation
                documents_batch = results.get("documents") or []
                documents = documents_batch[0] if documents_batch else []

                distances_batch = results.get("distances") or []
                if distances_batch:
                    distances = distances_batch[0] or []
                else:
                    distances = []

                if not distances:
                    distances = [0.0] * len(documents)
                elif len(distances) < len(documents):
                    # pad distances to match documents length if chroma omits some entries
                    distances = distances + [0.0] * (len(documents) - len(distances))

                # Log retrieved memories with content preview
                logger.info("=" * 80)
                logger.info(f"📋 RETRIEVED MEMORIES (Top {min(len(documents), 10)} of {len(documents)})")
                logger.info("=" * 80)
                for idx, (doc, dist) in enumerate(list(zip(documents, distances))[:10]):  # Show first 10
                    # Convert distance to similarity score (cosine: 1 - distance)
                    similarity = 1.0 - dist
                    # Truncate content for logging (first 200 chars)
                    content_preview = doc[:200] + "..." if len(doc) > 200 else doc
                    logger.info(f"\n[{idx + 1}] Similarity: {similarity:.4f} (distance: {dist:.4f})")
                    logger.info(f"    Content: {content_preview}")
                logger.info("=" * 80)

                return list(zip(documents, distances))  # type: ignore
            else:
                logger.info("No relevant tier0 items found locally")
                return []
                
        except Exception as e:
            logger.error(f"Error in local tier0 search: {e}")
            return []

    def _fix_dimension_mismatch_immediately(self) -> bool:
        """Fix dimension mismatch by immediately recreating the collection"""
        from papr_memory._logging import get_logger

        logger = get_logger(__name__)
        
        try:
            if not hasattr(self, "_chroma_collection") or self._chroma_collection is None:  # type: ignore
                return False
            
            collection_name = self._chroma_collection.name  # type: ignore
            logger.info(f"Recreating collection '{collection_name}' with correct embedding dimensions...")
            
            # Delete existing collection
            try:
                self._chroma_client.delete_collection(name=collection_name)
                logger.info(f"Deleted existing collection: {collection_name}")
            except Exception as delete_e:
                logger.warning(f"Error deleting collection (may not exist): {delete_e}")
            
            # Create new collection with Qwen3-4B embedding function
            embedding_function = self._get_qwen_embedding_function()
            if embedding_function:
                # Cast to Any to satisfy ChromaDB's EmbeddingFunction protocol
                from typing import Any

                self._chroma_collection = self._chroma_client.create_collection(
                    name=collection_name,
                    embedding_function=cast(Any, embedding_function),
                    metadata={"description": "Tier0 goals, OKRs, and use-cases from sync_tiers"},
                )
                logger.info(f"Recreated collection with Qwen3-4B embeddings: {collection_name}")
                return True
            else:
                logger.error("Failed to get Qwen3-4B embedding function")
                return False
                
        except Exception as e:
            logger.error(f"Error fixing dimension mismatch: {e}")
            return False

    def _check_embedding_dimensions_before_query(self, query_embedding: list[float]) -> None:
        """Check embedding dimensions before querying to prevent dimension mismatch errors"""
        from papr_memory._logging import get_logger

        logger = get_logger(__name__)
        
        try:
            if not hasattr(self, "_chroma_collection") or self._chroma_collection is None:  # type: ignore
                return
            
            # Get query embedding dimension
            query_dim = len(query_embedding)
            logger.debug(f"Query embedding dimension: {query_dim}")
            
            # Check if collection has custom embedding function (using correct attribute name)
            if hasattr(self._chroma_collection, "_embedding_function") and self._chroma_collection._embedding_function:
                # Collection has custom embedding function (should be 2560 dimensions for Qwen3-4B)
                expected_dim = 2560
                if query_dim != expected_dim:
                    logger.warning(
                        f"Potential dimension mismatch: query has {query_dim} dimensions, collection expects {expected_dim}"
                    )
                    logger.info("This will cause a dimension mismatch error during query")
                    logger.info("The collection needs to be recreated with correct embedding dimensions")
                else:
                    logger.debug(f"Query dimensions match collection: {query_dim} dimensions")
            else:
                # Collection uses default embedding function (384 dimensions)
                expected_dim = 384
                if query_dim != expected_dim:
                    logger.warning(
                        f"Potential dimension mismatch: query has {query_dim} dimensions, collection expects {expected_dim}"
                    )
                    logger.info("This will cause a dimension mismatch error during query")
                    logger.info("The collection needs to be recreated with correct embedding dimensions")
                else:
                    logger.debug(f"Query dimensions match collection: {query_dim} dimensions")
                
        except Exception as e:
            logger.debug(f"Error checking embedding dimensions: {e}")

    def _check_and_fix_embedding_dimensions(self, collection: object, tier0_data: list[dict[str, any]]) -> None:  # type: ignore
        """Check for embedding dimension mismatches and fix by recreating collection if needed"""
        from papr_memory._logging import get_logger

        logger = get_logger(__name__)
        
        try:
            # Get expected embedding dimension from tier0 data
            expected_dim = None
            if tier0_data and isinstance(tier0_data[0], dict) and "embedding" in tier0_data[0]:
                expected_dim = len(tier0_data[0]["embedding"])
                logger.info(f"Expected embedding dimension from tier0 data: {expected_dim}")
            
            # If we have server embeddings, check if collection dimensions match
            if expected_dim is not None:
                try:
                    # Try to get collection metadata to check dimensions
                    collection_metadata = getattr(collection, 'metadata', {})  # type: ignore
                    if hasattr(collection, "_embedding_function") and getattr(collection, '_embedding_function', None):
                        # Collection has custom embedding function
                        logger.info("Collection has custom embedding function")
                    else:
                        # Collection uses default embedding function (384 dimensions)
                        logger.info("Collection uses default embedding function (384 dimensions)")
                        
                        # If expected dimension is not 384, we need to recreate the collection
                        if expected_dim != 384:
                            logger.warning(
                                f"Dimension mismatch detected: collection expects 384, tier0 data has {expected_dim}"
                            )
                            logger.info("Recreating collection with correct embedding dimensions...")
                            
                            # Delete existing collection
                            collection_name = getattr(collection, 'name', 'unknown')  # type: ignore
                            self._chroma_client.delete_collection(name=collection_name)
                            logger.info(f"Deleted existing collection: {collection_name}")
                            
                            # Create new collection with Qwen3-4B embedding function
                            embedding_function = self._get_qwen_embedding_function()
                            logger.info(f"Embedding function created: {embedding_function is not None}")
                            if embedding_function:
                                try:
                                    # Cast to Any to satisfy ChromaDB's EmbeddingFunction protocol
                                    from typing import Any

                                    self._chroma_collection = self._chroma_client.create_collection(
                                        name=collection_name,
                                        embedding_function=cast(Any, embedding_function),
                                        metadata={"description": "Tier0 goals, OKRs, and use-cases from sync_tiers"},
                                    )
                                    logger.info(f"Recreated collection with Qwen3-4B embeddings: {collection_name}")
                                    # Verify the collection has the embedding function
                                    if (
                                        hasattr(self._chroma_collection, "_embedding_function")
                                        and self._chroma_collection._embedding_function
                                    ):
                                        logger.info(
                                            "Collection created with custom embedding function (2560 dimensions)"
                                        )
                                    else:
                                        logger.warning("Collection created but without custom embedding function")
                                    # Update the collection reference
                                    collection = self._chroma_collection
                                except Exception as create_e:
                                    error_msg = str(create_e)
                                    if "already exists" in error_msg.lower():
                                        logger.warning(f"Collection already exists: {create_e}")
                                        logger.info("Using existing collection...")
                                        try:
                                            self._chroma_collection = self._chroma_client.get_collection(name=collection_name)
                                            logger.info(f"Successfully retrieved existing collection: {collection_name}")
                                            collection = self._chroma_collection
                                        except Exception as get_e:
                                            logger.error(f"Failed to get existing collection: {get_e}")
                                            logger.info("Falling back to collection without embedding function...")
                                            self._chroma_collection = self._chroma_client.create_collection(
                                                name=collection_name,
                                                metadata={"description": "Tier0 goals, OKRs, and use-cases from sync_tiers"},
                                            )
                                            logger.warning("Collection created without embedding function (384 dimensions)")
                                            collection = self._chroma_collection
                                    else:
                                        logger.error(f"Failed to create collection with embedding function: {create_e}")
                                        logger.info("Falling back to collection without embedding function...")
                                        self._chroma_collection = self._chroma_client.create_collection(
                                            name=collection_name,
                                            metadata={"description": "Tier0 goals, OKRs, and use-cases from sync_tiers"},
                                        )
                                    logger.warning("Collection created without embedding function (384 dimensions)")
                                    collection = self._chroma_collection
                            else:
                                logger.error(
                                    "Failed to get Qwen3-4B embedding function - cannot fix dimension mismatch"
                                )
                                return
                        
                except Exception as e:
                    logger.debug(f"Could not check collection dimensions: {e}")
                    # If we can't check dimensions, try to proceed and let ChromaDB handle the error
                    pass
                    
        except Exception as e:
            logger.error(f"Error checking embedding dimensions: {e}")

    def _compare_tier0_data(self, collection: object, _tier0_data: list[dict], documents: list[str], metadatas: list[dict], ids: list[str]) -> dict[str, any]:  # type: ignore
        """Compare new tier0 data with existing data to detect changes"""
        from papr_memory._logging import get_logger

        logger = get_logger(__name__)
        
        try:
            # Get existing data from collection
            existing_data = {}
            try:
                existing = getattr(collection, 'get', lambda: {})().get()  # type: ignore
                if existing["ids"]:
                    for i, doc_id in enumerate(existing["ids"]):
                        existing_data[doc_id] = {
                            "document": existing["documents"][i] if existing["documents"] else None,
                            "metadata": existing["metadatas"][i] if existing["metadatas"] else None,
                            "id": doc_id,
                        }
            except Exception as e:
                logger.debug(f"No existing data found in collection: {e}")
                existing_data = {}
            
            # Compare new data with existing data
            new_documents = []
            new_metadatas = []
            new_ids = []
            updated_documents = []
            updated_metadatas = []
            updated_ids = []
            unchanged_count = 0
            
            for i, doc_id in enumerate(ids):
                if doc_id not in existing_data:
                    # New document
                    new_documents.append(documents[i])
                    new_metadatas.append(metadatas[i])
                    new_ids.append(doc_id)
                else:
                    # Check if content has changed
                    existing_doc = existing_data[doc_id]
                    current_doc = documents[i]
                    current_meta = metadatas[i]
                    
                    # Compare document content
                    content_changed = existing_doc["document"] != current_doc
                    
                    # Compare metadata (check key fields)
                    metadata_changed = False
                    if existing_doc["metadata"] and current_meta:
                        # Compare important metadata fields
                        important_fields = ["source", "tier", "type", "topics", "id", "updatedAt"]
                        for field in important_fields:
                            if existing_doc["metadata"].get(field) != current_meta.get(field):
                                metadata_changed = True
                                logger.debug(
                                    f"Metadata field '{field}' changed: '{existing_doc['metadata'].get(field)}' -> '{current_meta.get(field)}'"
                                )
                                break
                    
                    if content_changed or metadata_changed:
                        # Document has changed
                        updated_documents.append(documents[i])
                        updated_metadatas.append(metadatas[i])
                        updated_ids.append(doc_id)
                        logger.debug(
                            f"Document {doc_id} has changes: content={content_changed}, metadata={metadata_changed}"
                        )
                    else:
                        # Document is unchanged
                        unchanged_count += 1
                        logger.debug(f"Document {doc_id} is unchanged")
            
            # Prepare summary
            total_new = len(new_documents)
            total_updated = len(updated_documents)
            total_unchanged = unchanged_count
            has_changes = total_new > 0 or total_updated > 0
            
            summary_parts = []
            if total_new > 0:
                summary_parts.append(f"{total_new} new")
            if total_updated > 0:
                summary_parts.append(f"{total_updated} updated")
            if total_unchanged > 0:
                summary_parts.append(f"{total_unchanged} unchanged")
            
            summary = ", ".join(summary_parts) if summary_parts else "no data"
            
            logger.info(f"Tier0 data comparison: {summary}")
            
            return {
                "has_changes": has_changes,
                "summary": summary,
                "new_documents": new_documents,
                "new_metadatas": new_metadatas,
                "new_ids": new_ids,
                "updated_documents": updated_documents,
                "updated_metadatas": updated_metadatas,
                "updated_ids": updated_ids,
                "unchanged_count": unchanged_count,
            }
            
        except Exception as e:
            logger.error(f"Error comparing tier0 data: {e}")
            # Fallback: treat all as new documents
            return {
                "has_changes": True,
                "summary": f"error during comparison, treating all as new: {e}",
                "new_documents": documents,
                "new_metadatas": metadatas,
                "new_ids": ids,
                "updated_documents": [],
                "updated_metadatas": [],
                "updated_ids": [],
                "unchanged_count": 0,
            }

    def _store_tier0_in_chromadb(self, tier0_data: list[dict[str, any]]) -> None:  # type: ignore
        """Store tier0 data in ChromaDB with duplicate prevention"""
        import os

        from papr_memory._logging import get_logger

        logger = get_logger(__name__)
        
        try:
            logger.info("Attempting to import ChromaDB...")
            import chromadb  # type: ignore
            from chromadb.config import Settings  # type: ignore

            logger.info("ChromaDB imported successfully")
            
            # Initialize ChromaDB client (singleton pattern)
            if not hasattr(self, "_chroma_client"):
                # Get ChromaDB path from environment variable or use default
                chroma_path = os.environ.get("PAPR_CHROMADB_PATH", "./chroma_db")
                logger.info(f"Creating ChromaDB persistent client at: {chroma_path}")

                try:
                    # Use the new ChromaDB client configuration (non-deprecated)
                    self._chroma_client = chromadb.PersistentClient(
                        path=chroma_path,
                        settings=Settings(
                                anonymized_telemetry=False,
                                allow_reset=True,
                                is_persistent=True,
                            ),
                    )
                    logger.info("Initialized ChromaDB persistent client")
                except Exception as chroma_error:
                    if "deprecated" in str(chroma_error).lower():
                        logger.warning("ChromaDB data migration may be required")
                        logger.warning("If you have existing data, run: pip install chroma-migrate && chroma-migrate")
                        logger.warning("If no data to migrate, the old database will be recreated automatically")
                        # Try to delete old database and recreate
                        import os
                        import shutil

                        if os.path.exists(chroma_path):
                            logger.info(f"Removing old ChromaDB database at: {chroma_path}")
                            shutil.rmtree(chroma_path, ignore_errors=True)
                        # Retry with clean database
                        self._chroma_client = chromadb.PersistentClient(
                            path=chroma_path,
                            settings=Settings(
                                anonymized_telemetry=False,
                                allow_reset=True,
                                is_persistent=True,
                            ),
                        )
                        logger.info("Created new ChromaDB client with clean database")
                    else:
                        raise chroma_error
            
            # Create or get collection for tier0 data
            collection_name = "tier0_goals_okrs"
            logger.info(f"Attempting to get/create collection: {collection_name}")
            
            # Check if we have a valid collection with proper embedding function
            collection_needs_recreation = False
            if (
                hasattr(self, "_chroma_collection")
                and self._chroma_collection is not None
                and hasattr(self, "_collection_initialized")
                    and self._collection_initialized  # type: ignore
            ):
                # Collection is already validated and initialized
                return
            
            # Check if the existing collection has the correct embedding function
            if hasattr(self, "_chroma_collection") and self._chroma_collection is not None:
                embedding_function = getattr(self._chroma_collection, "_embedding_function", None)
                if embedding_function is not None:
                    # Check if it's a default embedding function by testing dimensions
                    try:
                        # Test the embedding function to see if it produces 384-dim (default) or 2560-dim (Qwen3-4B) embeddings
                        test_embedding = embedding_function.embed_query("test")
                        if len(test_embedding) == 384:
                            logger.warning("Existing collection uses default embedding function (384 dims)")
                            collection_needs_recreation = True
                        elif len(test_embedding) == 2560:
                            logger.info("Existing collection has correct Qwen3-4B embedding function (2560 dims)")
                            # Verify it has the required methods
                            if not hasattr(embedding_function, "embed_documents"):
                                logger.warning("Collection has correct dimensions but missing embed_documents method - will recreate")
                                collection_needs_recreation = True
                        else:
                            logger.warning(f"Existing collection has unexpected embedding dimensions: {len(test_embedding)} - will recreate")
                            collection_needs_recreation = True
                    except Exception as e:
                        logger.warning(f"Could not test embedding function: {e}")
                        # Fallback to class name check
                        if hasattr(embedding_function, "__class__") and "DefaultEmbeddingFunction" in str(
                            embedding_function.__class__
                        ):
                            logger.warning("Existing collection uses default embedding function (384 dims)")
                            collection_needs_recreation = True
                    else:
                        # It's a custom embedding function - test it
                        try:
                            if hasattr(embedding_function, "embed_documents"):
                                test_embedding = embedding_function.embed_documents(["test"])[0]
                                if len(test_embedding) != 2560:
                                    logger.warning(
                                        f"Existing collection has wrong embedding dimensions: {len(test_embedding)} (expected 2560)"
                                    )
                                    collection_needs_recreation = True
                                else:
                                    logger.info(
                                        "Existing collection has correct Qwen3-4B embedding function (2560 dims)"
                                    )
                            else:
                                logger.warning(
                                    "Existing collection has custom embedding function but missing embed_documents method"
                                )
                                collection_needs_recreation = True
                        except Exception as embed_test_e:
                            logger.warning(f"Existing collection embedding function test failed: {embed_test_e}")
                            collection_needs_recreation = True
                else:
                    logger.warning("Existing collection has no embedding function (384 dims)")
                    collection_needs_recreation = True
            
            # Try to get existing collection first
            if not hasattr(self, "_chroma_collection") or self._chroma_collection is None:  # type: ignore
                try:
                    logger.info("Trying to get existing collection...")
                    self._chroma_collection = self._chroma_client.get_collection(name=collection_name)
                    logger.info(f"Using existing ChromaDB collection: {collection_name}")
                    
                    # Validate the loaded collection's embedding function
                    embedding_function = getattr(self._chroma_collection, "_embedding_function", None)
                    
                    # Check collection metadata first for embedding model info
                    collection_metadata = getattr(self._chroma_collection, "metadata", {})
                    has_qwen_metadata = (
                        collection_metadata.get("embedding_model") == "Qwen3-4B" or
                        collection_metadata.get("embedding_dimensions") == "2560"
                    )
                    
                    if embedding_function is not None:
                        # Test the embedding function to see if it produces the correct dimensions
                        try:
                            test_embedding = embedding_function.embed_query("test")
                            if len(test_embedding) == 384:
                                if has_qwen_metadata:
                                    logger.info("Collection has Qwen3-4B metadata but default embedding function - will recreate")
                                else:
                                    logger.warning(
                                        "Loaded collection uses default embedding function (384 dims) - will recreate"
                                    )
                                collection_needs_recreation = True
                            elif len(test_embedding) == 2560:
                                logger.info("Collection has correct Qwen3-4B embedding function (2560 dims)")
                            else:
                                logger.warning(f"Collection has unexpected embedding dimensions: {len(test_embedding)} - will recreate")
                                collection_needs_recreation = True
                        except Exception as e:
                            logger.warning(f"Could not test embedding function: {e}")
                            # Fallback to class name check
                            if hasattr(embedding_function, "__class__") and "DefaultEmbeddingFunction" in str(
                                embedding_function.__class__
                            ):
                                if has_qwen_metadata:
                                    logger.info("Collection has Qwen3-4B metadata but default embedding function - will recreate")
                                else:
                                    logger.warning(
                                        "Loaded collection uses default embedding function (384 dims) - will recreate"
                                    )
                            collection_needs_recreation = True
                        else:
                            try:
                                if hasattr(embedding_function, "embed_documents"):
                                    test_embedding = embedding_function.embed_documents(["test"])[0]
                                    if len(test_embedding) != 2560:
                                        logger.warning(
                                            f"Loaded collection has wrong embedding dimensions: {len(test_embedding)} (expected 2560) - will recreate"
                                        )
                                        collection_needs_recreation = True
                                    else:
                                        logger.info(
                                            "Loaded collection has correct Qwen3-4B embedding function (2560 dims)"
                                        )
                                        # Collection is already properly configured, no need to recreate
                                        collection_needs_recreation = False
                                else:
                                    logger.warning(
                                        "Loaded collection has custom embedding function but missing embed_documents method - will recreate"
                                    )
                                    collection_needs_recreation = True
                            except Exception as embed_test_e:
                                logger.warning(
                                    f"Loaded collection embedding function test failed: {embed_test_e} - will recreate"
                                )
                                collection_needs_recreation = True
                    else:
                        if has_qwen_metadata:
                            logger.warning("Loaded collection has Qwen3-4B metadata but no embedding function - will recreate")
                            collection_needs_recreation = True
                        else:
                            logger.warning("Loaded collection has no embedding function (384 dims) - will recreate")
                            collection_needs_recreation = True
                    
                    # If collection is valid, we can skip creation
                    if not collection_needs_recreation:
                        self._collection_initialized = True
                        return
                        
                except Exception as e:
                    logger.info(f"Collection doesn't exist or error getting collection: {e}")
                    collection_needs_recreation = True
            
            # Create or recreate collection if needed
            if collection_needs_recreation:
                logger.info("Collection needs recreation due to embedding function mismatch")
                # Delete the existing collection first
                try:
                    self._chroma_client.delete_collection(name=collection_name)
                    logger.info(f"Deleted existing collection: {collection_name}")
                except Exception as delete_e:
                    logger.debug(f"No existing collection to delete: {delete_e}")
                
                # Create collection with consistent embedding function
                logger.info("Creating collection with consistent embedding function...")

                # OPTIMIZATION: Skip sentence-transformers when CoreML is enabled
                # Use server embeddings only to avoid loading 8GB model during collection creation
                if os.environ.get("PAPR_ENABLE_COREML", "").lower() == "true":
                    logger.info("⚡ CoreML enabled - using smart passthrough for ChromaDB")
                    logger.info("   Passthrough will use already-loaded CoreML for queries")

                    # Capture self reference for the passthrough function to use
                    memory_instance = self

                    # Smart passthrough that uses already-loaded CoreML model for queries
                    class SmartPassthroughEmbeddingFunction:
                        """Smart passthrough that NEVER generates embeddings - embeddings come from server or direct calls"""
                        def embed_documents(self, texts: list[str]) -> list[list[float]]:
                            # This should NEVER be called during normal operation because:
                            # 1. Server provides embeddings for tier0/tier1 (90%+ of items)
                            # 2. Legacy items are embedded via direct _get_local_embedder() calls
                            # 3. Only ChromaDB internal tests should trigger this
                            
                            # Return dummy 2560-dim vectors for dimension detection only
                            logger.debug(f"embed_documents called with {len(texts)} items (ChromaDB internal test), returning dummy 2560-dim vectors")
                            return [[0.0] * 2560 for _ in texts]

                        def embed_query(self, text: str | None = None, input: str | None = None) -> list[float]:
                            # ChromaDB sometimes calls this instead of using query_embeddings parameter
                            # Use the already-loaded CoreML model to generate real embeddings
                            query_text = text or input or ""

                            # Try to use already-loaded local embedder
                            embedder = memory_instance._get_local_embedder()
                            if embedder:
                                try:
                                    if hasattr(embedder, 'embed_query'):
                                        return embedder.embed_query(query_text)  # type: ignore
                                    elif hasattr(embedder, 'encode'):
                                        return embedder.encode([query_text])[0].tolist()  # type: ignore
                                except Exception as e:
                                    logger.debug(f"Local embedder failed in passthrough: {e}")

                            # Fallback to preloaded Qwen model
                            try:
                                qwen_embedding = memory_instance._embed_query_with_qwen(query_text)
                                if qwen_embedding:
                                    return qwen_embedding
                            except Exception as e:
                                logger.debug(f"Qwen embedder failed in passthrough: {e}")

                            # Last resort: zeros (this maintains dimension compatibility)
                            logger.warning("All embedders failed in passthrough, returning zeros")
                            return [0.0] * 2560

                        def __call__(self, input: list[str]) -> list[list[float]]:
                            return self.embed_documents(input)

                    embedding_function = SmartPassthroughEmbeddingFunction()
                    logger.info("   Created smart passthrough embedding function (2560 dims)")
                    logger.info("   Server embeddings will be used when available (preferred)")
                    logger.info("   Local CoreML will only generate embeddings for legacy items")
                    
                    # Store for tier1 to reuse (prevents tier1 from using 384-dim default)
                    self._embedding_function = embedding_function
                    logger.info("   Stored embedding function for tier1 reuse")
                else:
                    embedding_function = self._get_qwen_embedding_function()
                    logger.info(f"Qwen embedding function result: {embedding_function is not None}")
                    
                    # Store for tier1 to reuse
                    if embedding_function:
                        self._embedding_function = embedding_function
                        logger.info("   Stored embedding function for tier1 reuse")
                if embedding_function:
                    try:
                        # Test the embedding function to ensure it works
                        test_embedding = getattr(embedding_function, 'embed_documents', lambda _: [None])(["test"])[0]  # type: ignore
                        logger.info(f"Embedding function test successful (dim: {len(test_embedding) if test_embedding else 0})")

                        # Create collection with optimized settings for performance
                        # Cast to Any to satisfy ChromaDB's EmbeddingFunction protocol
                        from typing import Any
                        
                        self._chroma_collection = self._chroma_client.create_collection(
                            name=collection_name,
                            embedding_function=cast(Any, embedding_function),
                            metadata={
                                "description": "Tier0 goals, OKRs, and use-cases from sync_tiers",
                                "embedding_model": "Qwen3-4B",
                                "embedding_dimensions": "2560",
                                # Simplified metadata to avoid parsing errors
                                "optimized": "true",
                                "space": "cosine",
                            },
                        )
                        logger.info(f"Created new ChromaDB collection with Qwen3-4B embeddings: {collection_name}")
                        
                        # Verify the embedding function was properly stored
                        stored_embedding_function = getattr(self._chroma_collection, "_embedding_function", None)
                        if stored_embedding_function:
                            logger.info("✅ Embedding function properly stored in collection")
                        else:
                            logger.warning("⚠️ Embedding function not properly stored in collection")

                        # Optimize the collection for better performance
                        self._optimize_chromadb_collection()
                        
                        # Log ChromaDB collection metrics
                        from papr_memory._retrieval_logging import retrieval_logging_service
                        try:
                            collection_info = self._chroma_collection.get()  # type: ignore
                            documents = collection_info.get("documents", []) if collection_info else []
                            num_documents = len(documents) if documents is not None else 0
                            embedding_function_name = "Qwen3-4B" if embedding_function else "DefaultEmbeddingFunction"
                            retrieval_logging_service.log_chromadb_metrics(
                                collection_name, 
                                num_documents, 
                                embedding_function_name
                            )
                        except Exception as metrics_e:
                            logger.warning(f"Could not log ChromaDB metrics: {metrics_e}")
                    except Exception as create_e:
                        error_msg = str(create_e)
                        if "already exists" in error_msg.lower():
                            logger.warning(f"Collection already exists: {create_e}")
                            logger.info("Using existing collection...")
                            try:
                                self._chroma_collection = self._chroma_client.get_collection(name=collection_name)
                                logger.info(f"Successfully retrieved existing collection: {collection_name}")
                            except Exception as get_e:
                                logger.error(f"Failed to get existing collection: {get_e}")
                                logger.info("Falling back to collection without embedding function...")
                                self._chroma_collection = self._chroma_client.create_collection(
                                    name=collection_name,
                                    metadata={"description": "Tier0 goals, OKRs, and use-cases from sync_tiers"},
                                )
                                logger.info(f"Created new ChromaDB collection without embedding function: {collection_name}")
                        else:
                            logger.error(f"Failed to create collection with embedding function: {create_e}")
                            logger.info("Falling back to collection without embedding function...")
                            self._chroma_collection = self._chroma_client.create_collection(
                                name=collection_name,
                                metadata={"description": "Tier0 goals, OKRs, and use-cases from sync_tiers"},
                            )
                            logger.info(f"Created new ChromaDB collection without embedding function: {collection_name}")
                else:
                    # Fallback: create without custom embedding function
                    logger.warning(
                        "Qwen3-4B embedding function not available, creating collection without custom embedding function..."
                    )
                    logger.warning(
                        "This will result in a collection with DefaultEmbeddingFunction (384 dims) instead of Qwen3-4B (2560 dims)"
                    )
                    self._chroma_collection = self._chroma_client.create_collection(
                        name=collection_name,
                        metadata={"description": "Tier0 goals, OKRs, and use-cases from sync_tiers"},
                    )
                    logger.info(f"Created new ChromaDB collection without custom embedding function: {collection_name}")
                
                # Verify collection was created successfully
                if self._chroma_collection is None:
                    logger.error("Failed to create ChromaDB collection - collection is None")  # type: ignore
                    # Set to None to indicate failure
                    self._chroma_collection = None  # type: ignore
                else:
                    logger.info(f"ChromaDB collection created successfully: {self._chroma_collection.name}")
            
            collection = self._chroma_collection
            
            # Check for dimension mismatch and fix if needed
            self._check_and_fix_embedding_dimensions(collection, tier0_data)
            
            # Update collection reference in case it was recreated
            collection = self._chroma_collection
            
            # Verify collection is still valid
            if collection is None:
                logger.error("ChromaDB collection is None after dimension mismatch fix")  # type: ignore
                # Set _chroma_collection to None to indicate failure
                self._chroma_collection = None  # type: ignore
                return
            
            logger.info(f"Using ChromaDB collection: {collection.name}")
            
            # Prepare documents for ChromaDB
            documents = []
            metadatas = []
            ids = []
            embeddings = []  # Build embeddings in sync with documents

            for i, item in enumerate(tier0_data):
                # Extract content for embedding
                raw_content = None
                if isinstance(item, dict):
                    # Get content, handling None values properly
                    raw_content = item.get("content", item.get("description", None))
                elif hasattr(item, 'content'):
                    # Pydantic Memory object
                    raw_content = getattr(item, 'content', None) or getattr(item, 'description', None)
                else:
                    # Fallback for unknown types
                    raw_content = str(item)
                
                # Skip if None, "none" (case-insensitive), or empty/whitespace-only string
                if raw_content is None or (isinstance(raw_content, str) and (raw_content.strip().lower() == "none" or not raw_content.strip())):
                    # Skip items with no content - they won't be useful for search
                    item_id = item.get('id', 'unknown') if isinstance(item, dict) else getattr(item, 'id', 'unknown')
                    logger.debug(f"Skipping item {i} (id: {item_id}) with no/empty content")
                    continue  # Skip this item entirely - don't add to documents OR embeddings
                
                content = str(raw_content)

                # Create metadata - use item's metadata if exists, otherwise create default
                if isinstance(item, dict):
                    # Start with item's metadata if it exists
                    metadata = dict(item.get("metadata", {}))

                    # Add/override with our standard fields
                    metadata.update(
                        {
                        "source": "sync_tiers",
                        "tier": 0,
                            "type": str(item.get("type", "unknown")),
                            "topics": str(item.get("topics", [])),
                            "tags": str(item.get("tags", [])),
                            "id": str(item.get("id", f"tier0_{i}")),
                            "updatedAt": str(item.get("updatedAt", "")),
                        }
                    )

                    # Preserve server-side similarity_score (relevance score from tier0_builder)
                    # This is the composite score: 60% vector + 30% transition + 20% hotness
                    if "similarity_score" in item:
                        metadata["similarity_score"] = float(item["similarity_score"])
                    
                    # Preserve server-side relevance_score if available
                    if "relevance_score" in item:
                        metadata["relevance_score"] = float(item["relevance_score"])
                elif hasattr(item, 'id'):
                    # Pydantic Memory object
                    base_metadata = getattr(item, 'metadata', {}) or {}
                    metadata = dict(base_metadata)
                    
                    # Add standard fields
                    metadata.update({
                        "source": "sync_tiers",
                        "tier": 0,
                        "type": str(getattr(item, "type", "unknown")),
                        "topics": str(getattr(item, "topics", [])),
                        "tags": str(getattr(item, "tags", [])),
                        "id": str(getattr(item, "id", f"tier0_{i}")),
                        "updatedAt": str(getattr(item, "updated_at", "")),
                    })
                    
                    # Preserve server-side similarity_score if available
                    if hasattr(item, 'pydantic_extra__') and item.pydantic_extra__:  # type: ignore
                        if "similarity_score" in item.pydantic_extra__:  # type: ignore
                            metadata["similarity_score"] = float(item.pydantic_extra__["similarity_score"])  # type: ignore
                        if "relevance_score" in item.pydantic_extra__:  # type: ignore
                            metadata["relevance_score"] = float(item.pydantic_extra__["relevance_score"])  # type: ignore
                    
                    # Also check if relevance_score is a direct attribute on the Memory object
                    if hasattr(item, 'relevance_score') and item.relevance_score is not None:  # type: ignore
                        metadata["relevance_score"] = float(item.relevance_score)  # type: ignore
                else:
                    # Fallback for non-dict items
                    metadata = {"source": "sync_tiers", "tier": 0, "type": "unknown", "topics": "unknown"}  # type: ignore

                documents.append(content)
                metadatas.append(metadata)
                item_id = f"tier0_{i}"
                if isinstance(item, dict) and "id" in item:
                    item_id = f"tier0_{i}_{item['id']}"
                ids.append(item_id)

                # Extract embedding for this item (in sync with documents list)
                embedding = None
                if isinstance(item, dict) and "embedding" in item:
                    server_embedding = item["embedding"]
                    # Validate embedding format
                    if (
                        isinstance(server_embedding, list)
                        and len(server_embedding) > 0
                            and isinstance(server_embedding[0], (int, float))  # type: ignore
                    ):
                        embedding = server_embedding
                        logger.info(f"Valid server embedding for item {i} (dim: {len(embedding)})")
                    else:
                        logger.warning(f"Invalid server embedding format for item {i}, will use local generation")
                elif hasattr(item, 'embedding') and item.embedding:  # type: ignore
                    # Handle Pydantic Memory object with embedding attribute
                    server_embedding = item.embedding  # type: ignore
                    if (
                        isinstance(server_embedding, list)
                        and len(server_embedding) > 0
                        and isinstance(server_embedding[0], (int, float))  # type: ignore
                    ):
                        embedding = server_embedding
                        logger.info(f"Valid server embedding for item {i} (dim: {len(embedding)})")
                    else:
                        logger.warning(f"Invalid server embedding format for item {i}, will use local generation")

                embeddings.append(embedding)

            # Log embedding extraction summary
            server_embeddings_count = len([e for e in embeddings if e is not None])
            if server_embeddings_count > 0:
                logger.info(f"✅ Extracted {server_embeddings_count}/{len(embeddings)} server embeddings for tier0")
            else:
                logger.info("No server embeddings found, will generate locally for all items")
            
            # Generate local embeddings for items without server embeddings
            if any(emb is None for emb in embeddings):
                logger.info("Generating local embeddings for missing items...")
                try:
                    import time

                    start_time = time.time()
                    
                    # IMPORTANT: Use direct local embedder (CoreML), NOT collection's passthrough function
                    # The collection's embedding function is SmartPassthroughEmbeddingFunction which returns dummy vectors
                    # We need real CoreML embeddings here
                    embedder = self._get_local_embedder()  # type: ignore
                    logger.info("Using direct CoreML embedder for missing items (bypassing collection passthrough)")
                    
                    if embedder:
                        local_embedding_count = 0
                        for i, embedding in enumerate(embeddings):
                            if embedding is None:
                                try:
                                    item_start_time = time.time()
                                    
                                    # Use the appropriate embedding method based on embedder type
                                    if hasattr(embedder, "embed_documents"):
                                        # ChromaDB embedding function
                                        local_embedding = embedder.embed_documents([documents[i]])[0]  # type: ignore
                                    else:
                                        # SentenceTransformer model
                                        local_embedding = embedder.encode([documents[i]])[0].tolist()  # type: ignore
                                    
                                    item_time = (time.time() - item_start_time) * 1000  # Convert to ms
                                    embeddings[i] = local_embedding
                                    local_embedding_count += 1
                                    logger.info(
                                        f"Generated local embedding for item {i} (dim: {len(local_embedding)}) in {item_time:.1f}ms"
                                    )
                                except Exception as e:
                                    logger.error(f"Failed to generate local embedding for item {i}: {e}")
                        
                        total_time = (time.time() - start_time) * 1000  # Convert to ms
                        if local_embedding_count > 0:
                            avg_time = total_time / local_embedding_count
                            logger.info(
                                f"Generated {local_embedding_count} local embeddings in {total_time:.1f}ms (avg: {avg_time:.1f}ms per embedding)"
                            )
                    else:
                        logger.warning("No local embedder available for missing embeddings")
                except Exception as e:
                    logger.error(f"Error generating local embeddings: {e}")
            
            # Add documents to ChromaDB (compare with existing data)
            if documents:
                # Compare new data with existing data to detect changes
                comparison_result = self._compare_tier0_data(collection, tier0_data, documents, metadatas, ids)
                
                if comparison_result["has_changes"]:
                    logger.info(f"Detected changes in tier0 data: {comparison_result['summary']}")
                    
                    # Only add/update documents that are new or changed
                    new_documents = comparison_result["new_documents"]
                    new_metadatas = comparison_result["new_metadatas"]
                    new_ids = comparison_result["new_ids"]
                    updated_documents = comparison_result["updated_documents"]
                    updated_metadatas = comparison_result["updated_metadatas"]
                    updated_ids = comparison_result["updated_ids"]
                
                    # Add new documents
                    if new_documents:
                        # Filter embeddings for new documents only
                        new_embeddings = []
                        for doc_id in new_ids:  # type: ignore
                            original_index = ids.index(doc_id)
                            new_embeddings.append(embeddings[original_index])
                        
                        # Add documents with embeddings if available; filter out invalid/None
                        filtered_docs = []
                        filtered_meta = []
                        filtered_ids = []
                        filtered_embs = []
                        for idx, emb in enumerate(new_embeddings):
                            if emb is None:
                                continue
                            try:
                                # Ensure 1D numeric list
                                vec = list(map(float, emb))  # type: ignore
                                filtered_docs.append(new_documents[idx])
                                filtered_meta.append(new_metadatas[idx])
                                filtered_ids.append(new_ids[idx])
                                filtered_embs.append(vec)
                            except Exception:
                                continue

                        if filtered_embs:
                            collection.add(
                                documents=filtered_docs, metadatas=filtered_meta, ids=filtered_ids, embeddings=filtered_embs
                            )
                            logger.info(f"Added {len(new_documents)} new documents with local embeddings")
                        else:
                            collection.add(documents=new_documents, metadatas=new_metadatas, ids=new_ids)
                            logger.info(f"Added {len(new_documents)} new documents with ChromaDB default embeddings")
                    
                    # Update existing documents that have changed
                    if updated_documents:
                        # Filter embeddings for updated documents
                        updated_embeddings = []
                        for doc_id in updated_ids:  # type: ignore
                            original_index = ids.index(doc_id)
                            updated_embeddings.append(embeddings[original_index])
                        
                        # Update documents (ChromaDB doesn't have direct update, so we delete and re-add)
                        try:
                            collection.delete(ids=updated_ids)
                            filtered_docs = []
                            filtered_meta = []
                            filtered_ids = []
                            filtered_embs = []
                            for idx, emb in enumerate(updated_embeddings):
                                if emb is None:
                                    continue
                                try:
                                    vec = list(map(float, emb))  # type: ignore
                                    filtered_docs.append(updated_documents[idx])
                                    filtered_meta.append(updated_metadatas[idx])
                                    filtered_ids.append(updated_ids[idx])
                                    filtered_embs.append(vec)
                                except Exception:
                                    continue

                            if filtered_embs:
                                collection.add(
                                    documents=filtered_docs,
                                    metadatas=filtered_meta,
                                    ids=filtered_ids,
                                    embeddings=filtered_embs,
                                )
                                logger.info(f"Updated {len(updated_documents)} documents with local embeddings")
                            else:
                                collection.add(
                                    documents=updated_documents, metadatas=updated_metadatas, ids=updated_ids
                                )
                                logger.info(
                                    f"Updated {len(updated_documents)} documents with ChromaDB default embeddings"
                                )
                        except Exception as e:
                            logger.warning(f"Failed to update documents, adding as new: {e}")
                            # Fallback: add as new documents
                            if any(emb is not None for emb in updated_embeddings):
                                collection.add(
                                    documents=updated_documents,
                                    metadatas=updated_metadatas,
                                    ids=updated_ids,
                                    embeddings=updated_embeddings,
                                )
                            else:
                                collection.add(
                                    documents=updated_documents, metadatas=updated_metadatas, ids=updated_ids
                                )
                            logger.info(f"Added {len(updated_documents)} documents as new (update failed)")
                    
                    total_changes = len(new_documents) + len(updated_documents)
                    logger.info(
                        f"ChromaDB updated: {len(new_documents)} new, {len(updated_documents)} updated, {total_changes} total changes"
                    )
                else:
                    logger.info(f"No changes detected in tier0 data - ChromaDB collection unchanged")  # type: ignore
                
                # Query to verify storage (use safe query method)
                try:
                    # Check if we can safely query without dimension mismatch
                    if hasattr(collection, "_embedding_function") and collection._embedding_function:
                        # Collection has custom embedding function - should be safe to query
                        # But first, let's ensure the embedding function is working correctly
                        try:
                            # Test the embedding function to ensure it produces the right dimensions
                            test_result = collection._embedding_function.embed_documents(["test"])  # type: ignore
                            # Handle different return formats
                            if isinstance(test_result, list) and len(test_result) > 0:
                                test_embedding = test_result[0]
                                if isinstance(test_embedding, (list, tuple)) and len(test_embedding) > 0:
                                    logger.info(f"Collection embedding function test successful (dim: {len(test_embedding)})")
                                else:
                                    logger.debug(f"Unexpected embedding format: {type(test_embedding)}")
                            
                            # Skip the actual query test to avoid slow CoreML inference during initialization
                            # The embedding function test above is sufficient to verify the collection works
                            logger.info("Skipping query test (embedding function verified)")
                            count = collection.count()
                            logger.info(f"ChromaDB collection contains {count} documents (verified via count)")
                        except Exception as embed_test_e:
                            logger.debug(f"Collection embedding function test failed: {embed_test_e}")
                            logger.info("Skipping query test to avoid dimension mismatch")
                            count = collection.count()
                            logger.info(f"ChromaDB collection contains {count} documents (verified via count)")
                    else:
                        # Collection uses default embedding function - might have dimension issues
                        logger.info(
                            "Collection uses default embedding function - skipping query test to avoid dimension mismatch"
                        )
                        count = collection.count()
                        logger.info(f"ChromaDB collection contains {count} documents (verified via count)")
                except Exception as query_e:
                    logger.warning(f"ChromaDB query test failed (likely dimension mismatch): {query_e}")
                    logger.info(
                        "This indicates the collection was created with different embedding dimensions than expected"
                    )
                    logger.info("The collection will need to be recreated with the correct embedding function")
                    
                    # Try alternative verification method
                    try:
                        count = collection.count()
                        logger.info(f"ChromaDB collection contains {count} documents (verified via count)")
                    except Exception as count_e:
                        logger.warning(f"Could not verify collection via count: {count_e}")
                    
                    # Mark collection as needing recreation due to dimension mismatch
                    logger.warning("Collection has dimension mismatch - will be recreated on next run")
                    if hasattr(self, "_chroma_collection"):
                        # Delete the problematic collection
                        try:
                            collection_name = "tier0_goals_okrs"
                            self._chroma_client.delete_collection(name=collection_name)
                            logger.info(f"Deleted collection {collection_name} due to dimension mismatch")
                            # Clear the collection reference so it gets recreated
                            self._chroma_collection = None  # type: ignore
                        except Exception as delete_e:
                            logger.warning(f"Could not delete problematic collection: {delete_e}")
                
        except ImportError:
            logger.warning("ChromaDB not available - install with: pip install chromadb")
            logger.warning("Tier0 data will not be stored in vector database")
            # Set _chroma_collection to None to indicate ChromaDB is not available
            self._chroma_collection = None  # type: ignore
        except Exception as e:
            error_msg = str(e)
            if "already exists" in error_msg.lower():
                logger.warning(f"Collection already exists: {e}")
                logger.info("Using existing collection for local search")
                # Don't set _chroma_collection to None - use the existing collection
                try:
                    # Try to get the existing collection
                    if hasattr(self, "_chroma_client") and self._chroma_client:
                        self._chroma_collection = self._chroma_client.get_collection(name="tier0_goals_okrs")
                        logger.info("Successfully retrieved existing collection")
                        self._collection_initialized = True
                    else:
                        logger.error("ChromaDB client not available")
                        self._chroma_collection = None  # type: ignore
                except Exception as get_e:
                    logger.error(f"Failed to get existing collection: {get_e}")
                    self._chroma_collection = None  # type: ignore
            else:
                logger.error(f"Error storing tier0 data in ChromaDB: {e}")
                # Set _chroma_collection to None to indicate ChromaDB initialization failed
                self._chroma_collection = None  # type: ignore
        else:
            # Mark collection as successfully initialized
            self._collection_initialized = True

    def _store_tier1_in_chromadb(self, tier1_data: list[dict[str, any]]) -> None:  # type: ignore
        """Store tier1 data in ChromaDB with duplicate prevention"""
        import os

        from papr_memory._logging import get_logger

        logger = get_logger(__name__)
        
        try:
            logger.info("Attempting to store tier1 data in ChromaDB...")
            import chromadb  # type: ignore
            from chromadb.config import Settings  # type: ignore

            logger.info("ChromaDB imported successfully for tier1")
            
            # Initialize ChromaDB client (singleton pattern - reuse if already exists)
            if not hasattr(self, "_chroma_client"):
                # Get ChromaDB path from environment variable or use default
                chroma_path = os.environ.get("PAPR_CHROMADB_PATH", "./chroma_db")
                logger.info(f"Creating ChromaDB persistent client at: {chroma_path}")

                self._chroma_client = chromadb.PersistentClient(
                    path=chroma_path,
                    settings=Settings(
                        anonymized_telemetry=False,
                        allow_reset=True,
                        is_persistent=True,
                    ),
                )
                logger.info("Initialized ChromaDB persistent client for tier1")
            
            # Create or get collection for tier1 data
            collection_name = "tier1_memories"
            logger.info(f"Attempting to get/create tier1 collection: {collection_name}")
            
            # Get the embedding function (reuse from tier0 if available)
            embedding_function = None
            if hasattr(self, "_embedding_function") and self._embedding_function is not None:
                embedding_function = self._embedding_function
                logger.info("✅ Reusing embedding function from tier0 (self._embedding_function)")
            else:
                logger.warning("⚠️  self._embedding_function not found, trying tier0 collection...")
                # If no embedding function, try to get from tier0 collection
                if hasattr(self, "_collection") and self._collection is not None:  # type: ignore
                    try:
                        embedding_function = self._collection._embedding_function  # type: ignore
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
            
            # Get or create the tier1 collection
            try:
                if embedding_function:
                    # Try to get existing collection first to check dimension mismatch
                    collection = None
                    try:
                        existing_collection = self._chroma_client.get_collection(name=collection_name)
                        
                        # Check if dimensions match
                        can_test_dimensions = False
                        expected_dim = None
                        
                        if hasattr(embedding_function, 'embed_documents'):
                            test_embedding = embedding_function.embed_documents(["test"])  # type: ignore
                            expected_dim = len(test_embedding[0]) if isinstance(test_embedding, list) else len(test_embedding)
                            can_test_dimensions = True
                        elif hasattr(embedding_function, 'embed_query'):
                            test_embedding = embedding_function.embed_query("test")  # type: ignore
                            expected_dim = len(test_embedding) if test_embedding else None
                            can_test_dimensions = expected_dim is not None
                        
                        if not can_test_dimensions:
                            # Can't test, just use existing collection
                            collection = existing_collection
                            logger.info(f"Using existing tier1 collection (cannot test embedding dimensions)")
                        else:
                            # Get actual dimension from collection
                            if existing_collection.count() > 0:
                                sample = existing_collection.get(limit=1, include=["embeddings"])
                                if sample and sample.get("embeddings") and len(sample["embeddings"]) > 0:  # type: ignore
                                    actual_dim = len(sample["embeddings"][0]) if sample["embeddings"][0] else 0  # type: ignore
                                    if actual_dim != expected_dim and expected_dim and actual_dim > 0:
                                        logger.warning(f"Tier1 collection has wrong dimensions ({actual_dim} != {expected_dim}), recreating...")
                                        self._chroma_client.delete_collection(name=collection_name)
                                        collection = self._chroma_client.create_collection(
                                            name=collection_name, embedding_function=embedding_function  # type: ignore
                                        )
                                        logger.info(f"Recreated tier1 collection with correct embedding function")
                                    else:
                                        collection = existing_collection
                                        logger.info(f"Using existing tier1 collection with correct dimensions")
                                else:
                                    # Empty collection, just use it
                                    collection = existing_collection
                                    logger.info(f"Using existing empty tier1 collection")
                            else:
                                collection = existing_collection
                                logger.info(f"Using existing empty tier1 collection")
                    except Exception as get_ex:
                        # Collection doesn't exist or error checking it, create it
                        logger.info(f"Creating new tier1 collection: {get_ex}")
                        collection = self._chroma_client.create_collection(
                            name=collection_name, embedding_function=embedding_function  # type: ignore
                        )
                        logger.info(f"Created new tier1 collection with embedding function")
                    
                    if collection:
                        logger.info(f"Got/created tier1 collection: {collection.name}")
                else:
                    collection = self._chroma_client.get_or_create_collection(name=collection_name)
                    logger.info(f"Got/created tier1 collection: {collection.name}")
            except Exception as e:
                logger.warning(f"Error creating tier1 collection: {e}")
                # Try to get existing collection
                collection = self._chroma_client.get_collection(name=collection_name)
                logger.info(f"Retrieved existing tier1 collection: {collection.name}")
            
            # Store the tier1 collection reference
            self._chroma_tier1_collection = collection
            
            logger.info(f"Using ChromaDB tier1 collection: {collection.name}")
            
            # Deduplicate tier1_data by ID to avoid ChromaDB duplicate ID errors
            seen_ids = set()
            deduplicated_tier1 = []
            duplicate_count = 0
            for item in tier1_data:
                item_id = None
                if isinstance(item, dict):
                    item_id = item.get("id")
                elif hasattr(item, 'id'):
                    item_id = getattr(item, 'id', None)
                
                if item_id and item_id in seen_ids:
                    duplicate_count += 1
                    continue
                    
                if item_id:
                    seen_ids.add(item_id)
                deduplicated_tier1.append(item)
            
            if duplicate_count > 0:
                logger.info(f"Removed {duplicate_count} duplicate tier1 items (unique: {len(deduplicated_tier1)})")
            
            # Prepare documents for ChromaDB
            documents = []
            metadatas = []
            ids = []
            embeddings = []

            for i, item in enumerate(deduplicated_tier1):
                # Extract content for embedding
                raw_content = None
                if isinstance(item, dict):
                    # Get content, handling None values properly
                    raw_content = item.get("content", item.get("description", None))
                elif hasattr(item, 'content'):
                    # Pydantic Memory object
                    raw_content = getattr(item, 'content', None) or getattr(item, 'description', None)
                else:
                    # Fallback for unknown types
                    raw_content = str(item)
                
                # Skip if None, "none" (case-insensitive), or empty/whitespace-only string
                if raw_content is None or (isinstance(raw_content, str) and (raw_content.strip().lower() == "none" or not raw_content.strip())):
                    item_id = item.get('id', 'unknown') if isinstance(item, dict) else getattr(item, 'id', 'unknown')
                    logger.debug(f"Skipping tier1 item {i} (id: {item_id}) with no/empty content")
                    continue
                
                content = str(raw_content)

                # Create metadata
                if isinstance(item, dict):
                    metadata = dict(item.get("metadata", {}))
                    metadata.update(
                        {
                            "source": "sync_tiers",
                            "tier": 1,
                            "type": str(item.get("type", "unknown")),
                            "topics": str(item.get("topics", [])),
                            "tags": str(item.get("tags", [])),
                            "id": str(item.get("id", f"tier1_{i}")),
                            "updatedAt": str(item.get("updatedAt", "")),
                        }
                    )
                    
                    # Preserve server-side similarity_score if available
                    if "similarity_score" in item:
                        metadata["similarity_score"] = float(item["similarity_score"])
                    
                    # Preserve server-side relevance_score if available
                    if "relevance_score" in item:
                        metadata["relevance_score"] = float(item["relevance_score"])
                elif hasattr(item, 'id'):
                    # Pydantic Memory object
                    base_metadata = getattr(item, 'metadata', {}) or {}
                    metadata = dict(base_metadata)
                    
                    # Add standard fields
                    metadata.update({
                        "source": "sync_tiers",
                        "tier": 1,
                        "type": str(getattr(item, "type", "unknown")),
                        "topics": str(getattr(item, "topics", [])),
                        "tags": str(getattr(item, "tags", [])),
                        "id": str(getattr(item, "id", f"tier1_{i}")),
                        "updatedAt": str(getattr(item, "updated_at", "")),
                    })
                    
                    # Preserve server-side similarity_score if available
                    if hasattr(item, 'pydantic_extra__') and item.pydantic_extra__:  # type: ignore
                        if "similarity_score" in item.pydantic_extra__:  # type: ignore
                            metadata["similarity_score"] = float(item.pydantic_extra__["similarity_score"])  # type: ignore
                        if "relevance_score" in item.pydantic_extra__:  # type: ignore
                            metadata["relevance_score"] = float(item.pydantic_extra__["relevance_score"])  # type: ignore
                    
                    # Also check if relevance_score is a direct attribute on the Memory object
                    if hasattr(item, 'relevance_score') and item.relevance_score is not None:  # type: ignore
                        metadata["relevance_score"] = float(item.relevance_score)  # type: ignore
                    
                    # Also check if similarity_score is a direct attribute on the Memory object
                    if hasattr(item, 'similarity_score') and item.similarity_score is not None:  # type: ignore
                        metadata["similarity_score"] = float(item.similarity_score)  # type: ignore
                else:
                    metadata = {"source": "sync_tiers", "tier": 1, "type": "unknown", "topics": "unknown"}  # type: ignore

                documents.append(content)
                metadatas.append(metadata)
                item_id = f"tier1_{i}"
                if isinstance(item, dict) and "id" in item:
                    item_id = f"tier1_{item['id']}"
                elif hasattr(item, 'id'):
                    item_id = f"tier1_{getattr(item, 'id', i)}"
                ids.append(item_id)

                # Extract embedding if present
                embedding = None
                if isinstance(item, dict) and "embedding" in item:
                    server_embedding = item["embedding"]
                    # Validate embedding format
                    if (
                        isinstance(server_embedding, list)
                        and len(server_embedding) > 0
                        and isinstance(server_embedding[0], (int, float))  # type: ignore
                    ):
                        embedding = server_embedding
                        logger.info(f"Valid server embedding for tier1 item {i} (dim: {len(embedding)})")
                    else:
                        logger.warning(f"Invalid server embedding format for tier1 item {i}, will use local generation")
                elif hasattr(item, 'embedding') and item.embedding:  # type: ignore
                    # Handle Pydantic Memory object with embedding attribute
                    server_embedding = item.embedding  # type: ignore
                    if (
                        isinstance(server_embedding, list)
                        and len(server_embedding) > 0
                        and isinstance(server_embedding[0], (int, float))  # type: ignore
                    ):
                        embedding = server_embedding
                        logger.info(f"Valid server embedding for tier1 item {i} (dim: {len(embedding)})")
                    else:
                        logger.warning(f"Invalid server embedding format for tier1 item {i}, will use local generation")
                embeddings.append(embedding)

            # Log embedding extraction summary
            server_embeddings_count = len([e for e in embeddings if e is not None])
            if server_embeddings_count > 0:
                logger.info(f"✅ Extracted {server_embeddings_count}/{len(embeddings)} server embeddings for tier1")
            else:
                logger.info("No server embeddings found for tier1, will generate locally for all items")
            
            # Generate local embeddings for items without server embeddings (same as tier0)
            if any(emb is None for emb in embeddings):
                logger.info("Generating local embeddings for tier1 missing items...")
                try:
                    import time

                    start_time = time.time()
                    
                    # IMPORTANT: Use direct local embedder (CoreML), NOT collection's passthrough function
                    # The collection's embedding function is SmartPassthroughEmbeddingFunction which returns dummy vectors
                    # We need real CoreML embeddings here
                    embedder = self._get_local_embedder()  # type: ignore
                    logger.info("Using direct CoreML embedder for tier1 missing items (bypassing collection passthrough)")
                    
                    if embedder:
                        local_embedding_count = 0
                        for i, embedding in enumerate(embeddings):
                            if embedding is None:
                                try:
                                    item_start_time = time.time()
                                    
                                    # Use the appropriate embedding method based on embedder type
                                    if hasattr(embedder, "embed_documents"):
                                        # ChromaDB embedding function
                                        local_embedding = embedder.embed_documents([documents[i]])[0]  # type: ignore
                                    else:
                                        # SentenceTransformer model
                                        local_embedding = embedder.encode([documents[i]])[0].tolist()  # type: ignore
                                    
                                    item_time = (time.time() - item_start_time) * 1000  # Convert to ms
                                    embeddings[i] = local_embedding
                                    local_embedding_count += 1
                                    logger.info(
                                        f"Generated local embedding for tier1 item {i} (dim: {len(local_embedding)}) in {item_time:.1f}ms"
                                    )
                                except Exception as e:
                                    logger.error(f"Failed to generate local embedding for tier1 item {i}: {e}")
                        
                        total_time = (time.time() - start_time) * 1000  # Convert to ms
                        if local_embedding_count > 0:
                            avg_time = total_time / local_embedding_count
                            logger.info(
                                f"Generated {local_embedding_count} local tier1 embeddings in {total_time:.1f}ms (avg: {avg_time:.1f}ms per embedding)"
                            )
                    else:
                        logger.warning("No local embedder available for tier1 missing embeddings")
                except Exception as e:
                    logger.error(f"Error generating local embeddings for tier1: {e}")

            # Add documents to ChromaDB
            if documents:
                logger.info(f"Adding {len(documents)} tier1 documents to ChromaDB")
                
                # Add all documents with embeddings (local or server-provided)
                if all(emb is not None for emb in embeddings):
                    # All embeddings are available
                    validated_embs = []
                    for idx, emb in enumerate(embeddings):
                        try:
                            vec = list(map(float, emb))  # type: ignore
                            validated_embs.append(vec)
                        except Exception as e:
                            logger.error(f"Invalid embedding at index {idx}: {e}")
                            # Use zero vector as fallback
                            validated_embs.append([0.0] * 2560)
                    
                    collection.add(
                        documents=documents, metadatas=metadatas, ids=ids, embeddings=validated_embs
                    )
                    logger.info(f"✅ Added {len(documents)} tier1 documents with embeddings")
                elif any(emb is not None for emb in embeddings):
                    # Partial embeddings - filter and add only those with embeddings
                    filtered_docs = []
                    filtered_meta = []
                    filtered_ids = []
                    filtered_embs = []
                    
                    for idx, emb in enumerate(embeddings):
                        if emb is not None:
                            try:
                                vec = list(map(float, emb))  # type: ignore
                                filtered_docs.append(documents[idx])
                                filtered_meta.append(metadatas[idx])
                                filtered_ids.append(ids[idx])
                                filtered_embs.append(vec)
                            except Exception:
                                continue
                    
                    if filtered_embs:
                        collection.add(
                            documents=filtered_docs, metadatas=filtered_meta, ids=filtered_ids, embeddings=filtered_embs
                        )
                        logger.info(f"✅ Added {len(filtered_docs)} tier1 documents with partial embeddings")
                    else:
                        # No valid embeddings, let ChromaDB generate them
                        collection.add(documents=documents, metadatas=metadatas, ids=ids)
                        logger.warning(f"⚠️  Added {len(documents)} tier1 documents WITHOUT embeddings (ChromaDB will generate)")
                else:
                    # No embeddings at all - let ChromaDB generate them
                    collection.add(documents=documents, metadatas=metadatas, ids=ids)
                    logger.warning(f"⚠️  Added {len(documents)} tier1 documents WITHOUT embeddings (ChromaDB will generate)")
                
                # Verify storage
                try:
                    count = collection.count()
                    logger.info(f"ChromaDB tier1 collection contains {count} documents")
                except Exception as count_e:
                    logger.warning(f"Could not verify tier1 collection: {count_e}")
            else:
                logger.info("No tier1 documents to add to ChromaDB")
                
        except ImportError:
            logger.warning("ChromaDB not available for tier1 - install with: pip install chromadb")
            self._chroma_tier1_collection = None  # type: ignore
        except Exception as e:
            logger.error(f"Error storing tier1 data in ChromaDB: {e}")
            self._chroma_tier1_collection = None  # type: ignore

    def _get_max_similarity(self, results: list[tuple[str, float, str]]) -> float:
        """
        Get maximum similarity score from search results.
        
        Args:
            results: List of (document, distance, tier) tuples
        
        Returns:
            Maximum similarity score (0.0-1.0), where higher is better
        """
        if not results:
            return 0.0
        
        # Convert distance to similarity (1 - distance)
        # Lower distance = higher similarity
        similarities = [1.0 - dist for _, dist, _ in results]
        return max(similarities) if similarities else 0.0

    def search(
        self,
        *,
        query: str,
        max_memories: int | Omit = omit,
        max_nodes: int | Omit = omit,
        enable_agentic_graph: bool | Omit = omit,
        external_user_id: Optional[str] | Omit = omit,
        metadata: Optional[MemoryMetadataParam] | Omit = omit,
        namespace_id: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        rank_results: bool | Omit = omit,
        schema_id: Optional[str] | Omit = omit,
        search_override: Optional[memory_search_params.SearchOverride] | Omit = omit,
        simple_schema_mode: bool | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        accept_encoding: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchResponse:
        """
        Search through memories with authentication required.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Custom Schema Support**:
            This endpoint supports both system-defined and custom user-defined node types:
            - **System nodes**: Memory, Person, Company, Project, Task, Insight, Meeting, Opportunity, Code
            - **Custom nodes**: Defined by developers via UserGraphSchema (e.g., Developer, Product, Customer, Function)

            When custom schema nodes are returned:
            - Each custom node includes a `schema_id` field referencing the UserGraphSchema
            - The response includes a `schemas_used` array listing all schema IDs used
            - Use `GET /v1/schemas/{schema_id}` to retrieve full schema definitions including:
              - Node type definitions and properties
              - Relationship type definitions and constraints
              - Validation rules and requirements

            **Recommended Headers**:
            ```
            Accept-Encoding: gzip
            ```

            The API supports response compression for improved performance. Responses larger than 1KB will be automatically compressed when this header is present.

            **HIGHLY RECOMMENDED SETTINGS FOR BEST RESULTS:**
            - Set `enable_agentic_graph: true` for intelligent, context-aware search that can understand ambiguous references
            - Use `max_memories: 15-20` for comprehensive memory coverage
            - Use `max_nodes: 10-15` for comprehensive graph entity relationships

            **Agentic Graph Benefits:**
            When enabled, the system can understand vague references by first identifying specific entities from your memory graph, then performing targeted searches. For example:
            - "customer feedback" → identifies your customers first, then finds their specific feedback
            - "project issues" → identifies your projects first, then finds related issues
            - "team meeting notes" → identifies your team members first, then finds meeting notes
            - "code functions" → identifies your functions first, then finds related code

            **Role-Based Memory Filtering:**
            Filter memories by role and category using metadata fields:
            - `metadata.role`: Filter by "user" or "assistant"
            - `metadata.category`: Filter by category (user: preference, task, goal, facts, context | assistant: skills, learning)

            **User Resolution Precedence:**
            - If both user_id and external_user_id are provided, user_id takes precedence.
            - If only external_user_id is provided, it will be resolved to the internal user.
            - If neither is provided, the authenticated user is used.

        Args:
          query: Detailed search query describing what you're looking for. For best results,
              write 2-3 sentences that include specific details, context, and time frame.
              Examples: 'Find recurring customer complaints about API performance from the
              last month. Focus on issues where customers specifically mentioned timeout
              errors or slow response times in their conversations.' 'What are the main issues
              and blockers in my current projects? Focus on technical challenges and timeline
              impacts.' 'Find insights about team collaboration and communication patterns
              from recent meetings and discussions.'

          max_memories: HIGHLY RECOMMENDED: Maximum number of memories to return. Use at least 15-20 for
              comprehensive results. Lower values (5-10) may miss relevant information.
              Default is 20 for optimal coverage.

          max_nodes: HIGHLY RECOMMENDED: Maximum number of neo nodes to return. Use at least 10-15
              for comprehensive graph results. Lower values may miss important entity
              relationships. Default is 15 for optimal coverage.

          enable_agentic_graph: HIGHLY RECOMMENDED: Enable agentic graph search for intelligent, context-aware
              results. When enabled, the system can understand ambiguous references by first
              identifying specific entities from your memory graph, then performing targeted
              searches. Examples: 'customer feedback' → identifies your customers first, then
              finds their specific feedback; 'project issues' → identifies your projects
              first, then finds related issues; 'team meeting notes' → identifies team members
              first, then finds meeting notes. This provides much more relevant and
              comprehensive results. Set to false only if you need faster, simpler
              keyword-based search.

          external_user_id: Optional external user ID to filter search results by a specific external user.
              If both user_id and external_user_id are provided, user_id takes precedence.

          metadata: Metadata for memory request

          namespace_id: Optional namespace ID for multi-tenant search scoping. When provided, search is
              scoped to memories within this namespace.

          organization_id: Optional organization ID for multi-tenant search scoping. When provided, search
              is scoped to memories within this organization.

          rank_results: Whether to enable additional ranking of search results. Default is false because
              results are already ranked when using an LLM for search (recommended approach).
              Only enable this if you're not using an LLM in your search pipeline and need
              additional result ranking.

          schema_id: Optional user-defined schema ID to use for this search. If provided, this schema
              (plus system schema) will be used for query generation. If not provided, system
              will automatically select relevant schema based on query content.

          search_override: Complete search override specification provided by developer

          simple_schema_mode: If true, uses simple schema mode: system schema + ONE most relevant user schema.
              This ensures better consistency between add/search operations and reduces query
              complexity. Recommended for production use.

          user_id: Optional internal user ID to filter search results by a specific user. If not
              provided, results are not filtered by user. If both user_id and external_user_id
              are provided, user_id takes precedence.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # Check if on-device processing is enabled
        import os

        from papr_memory._logging import get_logger

        logger = get_logger(__name__)
        
        # Declare global variables at the top of the method
        global _model_loading_complete
        
        ondevice_processing = os.environ.get("PAPR_ONDEVICE_PROCESSING", "false").lower() in ("true", "1", "yes", "on")
        enable_parallel = os.environ.get("PAPR_ENABLE_PARALLEL_SEARCH", "true").lower() in ("true", "1", "yes", "on")
        similarity_threshold = float(os.environ.get("PAPR_ONDEVICE_SIMILARITY_THRESHOLD", "0.70"))
        
        # Check if agentic graph is enabled
        agentic_enabled = enable_agentic_graph if enable_agentic_graph is not omit else False
        
        # Check if ondevice processing was disabled due to CPU fallback
        if hasattr(self, "_ondevice_processing_disabled") and self._ondevice_processing_disabled:
            ondevice_processing = False
            logger.info("Ondevice processing disabled due to CPU fallback - using API processing")
        
        # CASE 1: Agentic graph enabled → always use cloud only
        if agentic_enabled:
            logger.info("🌐 Agentic graph enabled - using cloud search only")
            # Fall through to cloud API call at end of method
        
        # CASE 2: On-device enabled AND parallel search enabled → run both in parallel
        elif ondevice_processing and enable_parallel and hasattr(self, "_chroma_collection") and self._chroma_collection is not None:
            import time
            import threading

            # Check if model is loaded
            if not _model_loading_complete:
                logger.info("Model still loading in background, using server-side search for optimal UX")
                # Fall through to cloud API call
            else:
                logger.info("⚡ Starting parallel search (on-device + cloud)")
                
                # Ensure max_memories is not NotGiven
                n_results = max_memories if max_memories is not omit else 5
                assert isinstance(n_results, int), "n_results must be an int"
                
                # Variables to store results from both threads
                ondevice_result = None
                cloud_result = None
                ondevice_time = None
                cloud_time = None
                ondevice_error = None
                cloud_error = None
                
                # Thread function for on-device search
                def run_ondevice():
                    nonlocal ondevice_result, ondevice_time, ondevice_error
                    start = time.time()
                    try:
                        # Search both tier0 and tier1 collections in parallel
                        combined_results = self._search_both_collections(
                            query, 
                            n_results=n_results,
                            metadata=cast(Optional[MemoryMetadataParam] | NotGiven, metadata if metadata is not omit else not_given),
                            user_id=cast(Optional[str] | NotGiven, user_id if user_id is not omit else not_given),
                            external_user_id=cast(Optional[str] | NotGiven, external_user_id if external_user_id is not omit else not_given)
                        ) or []
                        
                        # Convert to SearchResponse
                        from papr_memory.types.search_response import Data, DataMemory
                        
                        memories = []
                        for i, (content, distance, tier) in enumerate(combined_results):
                            try:
                                similarity_score = 1.0 - float(distance)
                                memory_data: dict[str, any] = {  # type: ignore
                                    "id": f"{tier}_{i}",
                                    "acl": {},
                                    "content": content,
                                    "type": tier,
                                    "user_id": "local",
                                    "pydantic_extra__": {"similarity_score": similarity_score},
                                }
                                memories.append(DataMemory(**memory_data))  # type: ignore
                            except Exception as e:
                                logger.warning(f"Failed to create DataMemory: {e}")
                                continue
                        
                        ondevice_result = SearchResponse(data=Data(memories=memories, nodes=[]), status="success")
                        ondevice_time = (time.time() - start) * 1000
                        logger.info(f"✅ On-device search completed in {ondevice_time:.1f}ms")
                    except Exception as e:
                        ondevice_error = e
                        logger.warning(f"❌ On-device search failed: {e}")
                
                # Thread function for cloud search
                def run_cloud():
                    nonlocal cloud_result, cloud_time, cloud_error
                    start = time.time()
                    try:
                        extra_headers_cloud = {**strip_not_given({"Accept-Encoding": accept_encoding}), **(extra_headers or {})}
                        cloud_result = self._post(
                            "/v1/memory/search",
                            body=maybe_transform(
                                {
                                    "query": query,
                                    "enable_agentic_graph": enable_agentic_graph,
                                    "external_user_id": external_user_id,
                                    "metadata": metadata,
                                    "namespace_id": namespace_id,
                                    "organization_id": organization_id,
                                    "rank_results": rank_results,
                                    "schema_id": schema_id,
                                    "search_override": search_override,
                                    "simple_schema_mode": simple_schema_mode,
                                    "user_id": user_id,
                                },
                                memory_search_params.MemorySearchParams,
                            ),
                            options=make_request_options(
                                extra_headers=extra_headers_cloud,
                                extra_query=extra_query,
                                extra_body=extra_body,
                                timeout=timeout,
                                query=maybe_transform(
                                    {
                                        "max_memories": max_memories,
                                        "max_nodes": max_nodes,
                                    },
                                    memory_search_params.MemorySearchParams,
                                ),
                            ),
                            cast_to=SearchResponse,
                        )
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
                
                # RACE WITH THRESHOLD: Wait for on-device first, return immediately if it meets threshold
                # This gives us fast results when on-device is good enough
                ondevice_thread.join()  # Wait for on-device to complete
                
                # Check on-device results immediately
                if ondevice_result and not ondevice_error:
                    # Extract combined_results from ondevice memories
                    combined_results_for_check = [
                        (mem.content, 1.0 - getattr(mem, 'pydantic_extra__', {}).get('similarity_score', 0.0), mem.type)
                        for mem in ondevice_result.data.memories  # type: ignore
                    ]
                    max_similarity = self._get_max_similarity(combined_results_for_check)
                    
                    # If on-device meets threshold, return immediately WITHOUT waiting for cloud
                    if max_similarity >= similarity_threshold:
                        logger.info(f"✅ Using on-device results (similarity={max_similarity:.3f}, time={ondevice_time:.1f}ms) - cloud still running")
                        # Don't wait for cloud thread - let it finish in background if needed
                        return ondevice_result
                    else:
                        # On-device doesn't meet threshold - now wait for cloud
                        logger.info(f"⚠️  On-device similarity too low ({max_similarity:.3f} < {similarity_threshold}) - waiting for cloud results")
                        cloud_thread.join()  # Wait for cloud to complete
                        if cloud_result and not cloud_error:
                            logger.info(f"✅ Using cloud results (time={cloud_time:.1f}ms)")
                            return cloud_result
                        else:
                            logger.warning("Cloud search also failed, returning low-quality on-device results")
                            return ondevice_result
                else:
                    # On-device failed - wait for cloud
                    logger.warning("On-device search failed, waiting for cloud results")
                    cloud_thread.join()
                    if cloud_result and not cloud_error:
                        logger.info(f"✅ Using cloud results (on-device failed, time={cloud_time:.1f}ms)")
                        return cloud_result
                    else:
                        # Both failed - raise error
                        logger.error("❌ Both on-device and cloud search failed")
                        if cloud_error:
                            raise cloud_error
                        if ondevice_error:
                            raise ondevice_error
        
        # CASE 3: On-device enabled BUT parallel search disabled → on-device only (legacy behavior)
        elif ondevice_processing and hasattr(self, "_chroma_collection") and self._chroma_collection is not None:
            import time

            start_time = time.time()
            # Ensure max_memories is not NotGiven
            n_results = max_memories if max_memories is not omit else 5
            assert isinstance(n_results, int), "n_results must be an int"
            
            # Check if model is loaded, fallback to server-side search if not
            if not _model_loading_complete:
                logger.info("Model still loading in background, using server-side search for optimal UX")
                # Fall through to cloud API call
            else:
                logger.info("🔍 On-device search only (parallel search disabled)")
                
                # Search both tier0 and tier1 collections in parallel
                combined_results = self._search_both_collections(
                    query, 
                    n_results=n_results,
                    metadata=cast(Optional[MemoryMetadataParam] | NotGiven, metadata if metadata is not omit else not_given),
                    user_id=cast(Optional[str] | NotGiven, user_id if user_id is not omit else not_given),
                    external_user_id=cast(Optional[str] | NotGiven, external_user_id if external_user_id is not omit else not_given)
                ) or []
                
                # Extract documents from results
                tier0_context = [(doc, dist) for doc, dist, _ in combined_results]
            
                search_time = time.time() - start_time
                logger.info(f"🔍 Local parallel search (tier0 + tier1) completed in {search_time:.2f}s")
                if tier0_context:
                    logger.info(f"Using {len(tier0_context)} combined items for search context enhancement")
                    from papr_memory.types.search_response import Data, DataMemory

                    memories = []
                    for i, item in enumerate(tier0_context):
                        try:
                            if isinstance(item, tuple):
                                content, distance = item
                                similarity_score = 1.0 - float(distance)
                            else:
                                content = item
                                similarity_score = 0.0

                            memory_data: dict[str, any] = {  # type: ignore
                                "id": f"tier0_{i}",
                                "acl": {},
                                "content": content,
                                "type": "tier0",
                                "user_id": "local",
                                "pydantic_extra__": {"similarity_score": similarity_score},
                            }
                            memories.append(DataMemory(**memory_data))  # type: ignore
                        except Exception as e:
                            logger.warning(f"Failed to create DataMemory for item {i}: {e}")
                            continue
                
                # Return search results with proper SearchResponse structure
                return SearchResponse(data=Data(memories=memories, nodes=[]), status="success")
        
        # CASE 4: On-device disabled → cloud only
        elif not ondevice_processing:
            logger.info("On-device processing disabled - using API-only search")
        else:
            logger.info("No ChromaDB collection available for local search")
        
        # Perform the main cloud search (for cases that fall through)
        extra_headers = {**strip_not_given({"Accept-Encoding": accept_encoding}), **(extra_headers or {})}
        return self._post(
            "/v1/memory/search",
            body=maybe_transform(
                {
                    "query": query,
                    "enable_agentic_graph": enable_agentic_graph,
                    "external_user_id": external_user_id,
                    "metadata": metadata,
                    "namespace_id": namespace_id,
                    "organization_id": organization_id,
                    "rank_results": rank_results,
                    "schema_id": schema_id,
                    "search_override": search_override,
                    "simple_schema_mode": simple_schema_mode,
                    "user_id": user_id,
                },
                memory_search_params.MemorySearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "max_memories": max_memories,
                        "max_nodes": max_nodes,
                    },
                    memory_search_params.MemorySearchParams,
                ),
            ),
            cast_to=SearchResponse,
        )


class AsyncMemoryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMemoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AsyncMemoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMemoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AsyncMemoryResourceWithStreamingResponse(self)

    async def update(
        self,
        memory_id: str,
        *,
        content: Optional[str] | Omit = omit,
        context: Optional[Iterable[ContextItemParam]] | Omit = omit,
        metadata: Optional[MemoryMetadataParam] | Omit = omit,
        namespace_id: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        relationships_json: Optional[Iterable[RelationshipItemParam]] | Omit = omit,
        type: Optional[MemoryType] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryUpdateResponse:
        """
        Update an existing memory item by ID.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - Content-Type: application/json
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

            The API validates content size against MAX_CONTENT_LENGTH environment variable (defaults to 15000 bytes).

        Args:
          content: The new content of the memory item

          context: Updated context for the memory item

          metadata: Metadata for memory request

          namespace_id: Optional namespace ID for multi-tenant memory scoping. When provided, update is
              scoped to memories within this namespace.

          organization_id: Optional organization ID for multi-tenant memory scoping. When provided, update
              is scoped to memories within this organization.

          relationships_json: Updated relationships for Graph DB (neo4J)

          type: Valid memory types

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not memory_id:
            raise ValueError(f"Expected a non-empty value for `memory_id` but received {memory_id!r}")
        return await self._put(
            f"/v1/memory/{memory_id}",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "context": context,
                    "metadata": metadata,
                    "namespace_id": namespace_id,
                    "organization_id": organization_id,
                    "relationships_json": relationships_json,
                    "type": type,
                },
                memory_update_params.MemoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryUpdateResponse,
        )

    async def delete(
        self,
        memory_id: str,
        *,
        skip_parse: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryDeleteResponse:
        """
        Delete a memory item by ID.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

        Args:
          skip_parse: Skip Parse Server deletion

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not memory_id:
            raise ValueError(f"Expected a non-empty value for `memory_id` but received {memory_id!r}")
        return await self._delete(
            f"/v1/memory/{memory_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"skip_parse": skip_parse}, memory_delete_params.MemoryDeleteParams),
            ),
            cast_to=MemoryDeleteResponse,
        )

    async def add(
        self,
        *,
        content: str,
        skip_background_processing: bool | Omit = omit,
        context: Optional[Iterable[ContextItemParam]] | Omit = omit,
        graph_generation: Optional[GraphGenerationParam] | Omit = omit,
        metadata: Optional[MemoryMetadataParam] | Omit = omit,
        namespace_id: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        relationships_json: Optional[Iterable[RelationshipItemParam]] | Omit = omit,
        type: MemoryType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddMemoryResponse:
        """
        Add a new memory item to the system with size validation and background
        processing.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - Content-Type: application/json
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

            **Role-Based Memory Categories**:
            - **User memories**: preference, task, goal, facts, context
            - **Assistant memories**: skills, learning

            **New Metadata Fields**:
            - `metadata.role`: Optional field to specify who generated the memory (user or assistant)
            - `metadata.category`: Optional field for memory categorization based on role
            - Both fields are stored within metadata at the same level as topics, location, etc.

            The API validates content size against MAX_CONTENT_LENGTH environment variable (defaults to 15000 bytes).

        Args:
          content: The content of the memory item you want to add to memory

          skip_background_processing: If True, skips adding background tasks for processing

          context: Context can be conversation history or any relevant context for a memory item

          graph_generation: Graph generation configuration

          metadata: Metadata for memory request

          namespace_id: Optional namespace ID for multi-tenant memory scoping. When provided, memory is
              associated with this namespace.

          organization_id: Optional organization ID for multi-tenant memory scoping. When provided, memory
              is associated with this organization.

          relationships_json: Array of relationships that we can use in Graph DB (neo4J)

          type: Memory item type; defaults to 'text' if omitted

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/memory",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "context": context,
                    "graph_generation": graph_generation,
                    "metadata": metadata,
                    "namespace_id": namespace_id,
                    "organization_id": organization_id,
                    "relationships_json": relationships_json,
                    "type": type,
                },
                memory_add_params.MemoryAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"skip_background_processing": skip_background_processing}, memory_add_params.MemoryAddParams
                ),
            ),
            cast_to=AddMemoryResponse,
        )

    async def add_batch(
        self,
        *,
        memories: Iterable[AddMemoryParam],
        skip_background_processing: bool | Omit = omit,
        batch_size: Optional[int] | Omit = omit,
        external_user_id: Optional[str] | Omit = omit,
        graph_generation: Optional[GraphGenerationParam] | Omit = omit,
        namespace_id: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        webhook_secret: Optional[str] | Omit = omit,
        webhook_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchMemoryResponse:
        """
        Add multiple memory items in a batch with size validation and background
        processing.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - Content-Type: application/json
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

            The API validates individual memory content size against MAX_CONTENT_LENGTH environment variable (defaults to 15000 bytes).

        Args:
          memories: List of memory items to add in batch

          skip_background_processing: If True, skips adding background tasks for processing

          batch_size: Number of items to process in parallel

          external_user_id: External user ID for all memories in the batch. If provided and user_id is not,
              will be resolved to internal user ID.

          graph_generation: Graph generation configuration

          namespace_id: Optional namespace ID for multi-tenant batch memory scoping. When provided, all
              memories in the batch are associated with this namespace.

          organization_id: Optional organization ID for multi-tenant batch memory scoping. When provided,
              all memories in the batch are associated with this organization.

          user_id: Internal user ID for all memories in the batch. If not provided, developer's
              user ID will be used.

          webhook_secret: Optional secret key for webhook authentication. If provided, will be included in
              the webhook request headers as 'X-Webhook-Secret'.

          webhook_url: Optional webhook URL to notify when batch processing is complete. The webhook
              will receive a POST request with batch completion details.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/memory/batch",
            body=await async_maybe_transform(
                {
                    "memories": memories,
                    "batch_size": batch_size,
                    "external_user_id": external_user_id,
                    "graph_generation": graph_generation,
                    "namespace_id": namespace_id,
                    "organization_id": organization_id,
                    "user_id": user_id,
                    "webhook_secret": webhook_secret,
                    "webhook_url": webhook_url,
                },
                memory_add_batch_params.MemoryAddBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"skip_background_processing": skip_background_processing},
                    memory_add_batch_params.MemoryAddBatchParams,
                ),
            ),
            cast_to=BatchMemoryResponse,
        )

    async def delete_all(
        self,
        *,
        external_user_id: Optional[str] | Omit = omit,
        skip_parse: bool | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchMemoryResponse:
        """
        Delete all memory items for a user.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **User Resolution**:
            - If only API key is provided: deletes memories for the developer
            - If user_id or external_user_id is provided: resolves and deletes memories for that user
            - Uses the same user resolution logic as other endpoints

            **Required Headers**:
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

            **WARNING**: This operation cannot be undone. All memories for the resolved user will be permanently deleted.

        Args:
          external_user_id: Optional external user ID to resolve and delete memories for

          skip_parse: Skip Parse Server deletion

          user_id: Optional user ID to delete memories for (if not provided, uses authenticated
              user)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/v1/memory/all",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "external_user_id": external_user_id,
                        "skip_parse": skip_parse,
                        "user_id": user_id,
                    },
                    memory_delete_all_params.MemoryDeleteAllParams,
                ),
            ),
            cast_to=BatchMemoryResponse,
        )

    async def sync_tiers(
        self,
        *,
        include_embeddings: bool | NotGiven = not_given,
        embed_limit: int | NotGiven = not_given,
        max_tier0: int | NotGiven = not_given,
        max_tier1: int | NotGiven = not_given,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncTiersResponse:
        """
        Get sync tiers for memory synchronization.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')
            - Accept-Encoding: gzip (recommended)

        Args:
          include_embeddings: Whether to include embeddings in the response

          embed_limit: Limit for embeddings

          max_tier0: Maximum number of tier 0 items

          max_tier1: Maximum number of tier 1 items

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Accept-Encoding": "gzip"}), **(extra_headers or {})}
        return await self._post(
            "/v1/sync/tiers",
            body=await async_maybe_transform(
                {
                    "include_embeddings": include_embeddings,
                    "embed_limit": embed_limit,
                    "max_tier0": max_tier0,
                    "max_tier1": max_tier1,
                },
                SyncTiersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=SyncTiersResponse,
        )

    async def get(
        self,
        memory_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchResponse:
        """
        Retrieve a memory item by ID.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not memory_id:
            raise ValueError(f"Expected a non-empty value for `memory_id` but received {memory_id!r}")
        return await self._get(
            f"/v1/memory/{memory_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchResponse,
        )

    async def _process_sync_tiers_and_store(
        self,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = None,
    ) -> None:
        """Internal async method to call sync_tiers and store tier0 data in ChromaDB"""
        from papr_memory._logging import get_logger

        logger = get_logger(__name__)
        
        try:
            # Call the async sync_tiers method with parameters from environment variables
            # Get max_tier0 from environment variable with fallback to 30
            import os

            max_tier0_env = os.environ.get("PAPR_MAX_TIER0", "30")
            try:
                max_tier0_value = int(max_tier0_env)
            except ValueError:
                max_tier0_value = 30  # fallback to default if invalid
            
            # Get max_tier1 from environment variable, defaulting to same as tier0
            max_tier1_env = os.environ.get("PAPR_MAX_TIER1", str(max_tier0_value))
            try:
                max_tier1_value = int(max_tier1_env)
            except ValueError:
                max_tier1_value = max_tier0_value  # fallback to tier0 value if invalid
            
            # Set a reasonable timeout for sync_tiers to prevent hanging
            sync_timeout = timeout if timeout is not None else 300.0  # 5 minutes default
            
            logger.info(f"Calling async sync_tiers with max_tier0={max_tier0_value}, max_tier1={max_tier1_value}, timeout={sync_timeout}s")
            sync_response = await self.sync_tiers(
                include_embeddings=True,
                embed_limit=max_tier0_value,
                max_tier0=max_tier0_value,
                max_tier1=max_tier1_value,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=sync_timeout,
            )
            
            if sync_response:
                # Extract tier0 data using SyncTiersResponse model
                tier0_data = sync_response.tier0
                tier1_data = sync_response.tier1
                
                if tier0_data:
                    logger.info(f"Found {len(tier0_data)} tier0 items in sync response")
                    for i in range(min(3, len(tier0_data))):
                        logger.debug(f"Tier0 {i + 1}: Item extracted")
                
                if tier1_data:
                    logger.info(f"Found {len(tier1_data)} tier1 items in sync response")
                
                # Store tier0 data in ChromaDB
                if tier0_data:
                    logger.info(f"Using {len(tier0_data)} tier0 items for search enhancement")
                    # Note: AsyncMemoryResource does not support ChromaDB storage
                    logger.info("Async version does not support local storage")
                else:
                    logger.info("No tier0 data found in sync response")
                    
        except Exception as e:
            logger.error(f"Error in sync_tiers processing: {e}")

    async def search(
        self,
        *,
        query: str,
        max_memories: int | Omit = omit,
        max_nodes: int | Omit = omit,
        enable_agentic_graph: bool | Omit = omit,
        external_user_id: Optional[str] | Omit = omit,
        metadata: Optional[MemoryMetadataParam] | Omit = omit,
        namespace_id: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        rank_results: bool | Omit = omit,
        schema_id: Optional[str] | Omit = omit,
        search_override: Optional[memory_search_params.SearchOverride] | Omit = omit,
        simple_schema_mode: bool | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        accept_encoding: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchResponse:
        """
        Search through memories with authentication required.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Custom Schema Support**:
            This endpoint supports both system-defined and custom user-defined node types:
            - **System nodes**: Memory, Person, Company, Project, Task, Insight, Meeting, Opportunity, Code
            - **Custom nodes**: Defined by developers via UserGraphSchema (e.g., Developer, Product, Customer, Function)

            When custom schema nodes are returned:
            - Each custom node includes a `schema_id` field referencing the UserGraphSchema
            - The response includes a `schemas_used` array listing all schema IDs used
            - Use `GET /v1/schemas/{schema_id}` to retrieve full schema definitions including:
              - Node type definitions and properties
              - Relationship type definitions and constraints
              - Validation rules and requirements

            **Recommended Headers**:
            ```
            Accept-Encoding: gzip
            ```

            The API supports response compression for improved performance. Responses larger than 1KB will be automatically compressed when this header is present.

            **HIGHLY RECOMMENDED SETTINGS FOR BEST RESULTS:**
            - Set `enable_agentic_graph: true` for intelligent, context-aware search that can understand ambiguous references
            - Use `max_memories: 15-20` for comprehensive memory coverage
            - Use `max_nodes: 10-15` for comprehensive graph entity relationships

            **Agentic Graph Benefits:**
            When enabled, the system can understand vague references by first identifying specific entities from your memory graph, then performing targeted searches. For example:
            - "customer feedback" → identifies your customers first, then finds their specific feedback
            - "project issues" → identifies your projects first, then finds related issues
            - "team meeting notes" → identifies your team members first, then finds meeting notes
            - "code functions" → identifies your functions first, then finds related code

            **Role-Based Memory Filtering:**
            Filter memories by role and category using metadata fields:
            - `metadata.role`: Filter by "user" or "assistant"
            - `metadata.category`: Filter by category (user: preference, task, goal, facts, context | assistant: skills, learning)

            **User Resolution Precedence:**
            - If both user_id and external_user_id are provided, user_id takes precedence.
            - If only external_user_id is provided, it will be resolved to the internal user.
            - If neither is provided, the authenticated user is used.

        Args:
          query: Detailed search query describing what you're looking for. For best results,
              write 2-3 sentences that include specific details, context, and time frame.
              Examples: 'Find recurring customer complaints about API performance from the
              last month. Focus on issues where customers specifically mentioned timeout
              errors or slow response times in their conversations.' 'What are the main issues
              and blockers in my current projects? Focus on technical challenges and timeline
              impacts.' 'Find insights about team collaboration and communication patterns
              from recent meetings and discussions.'

          max_memories: HIGHLY RECOMMENDED: Maximum number of memories to return. Use at least 15-20 for
              comprehensive results. Lower values (5-10) may miss relevant information.
              Default is 20 for optimal coverage.

          max_nodes: HIGHLY RECOMMENDED: Maximum number of neo nodes to return. Use at least 10-15
              for comprehensive graph results. Lower values may miss important entity
              relationships. Default is 15 for optimal coverage.

          enable_agentic_graph: HIGHLY RECOMMENDED: Enable agentic graph search for intelligent, context-aware
              results. When enabled, the system can understand ambiguous references by first
              identifying specific entities from your memory graph, then performing targeted
              searches. Examples: 'customer feedback' → identifies your customers first, then
              finds their specific feedback; 'project issues' → identifies your projects
              first, then finds related issues; 'team meeting notes' → identifies team members
              first, then finds meeting notes. This provides much more relevant and
              comprehensive results. Set to false only if you need faster, simpler
              keyword-based search.

          external_user_id: Optional external user ID to filter search results by a specific external user.
              If both user_id and external_user_id are provided, user_id takes precedence.

          metadata: Metadata for memory request

          namespace_id: Optional namespace ID for multi-tenant search scoping. When provided, search is
              scoped to memories within this namespace.

          organization_id: Optional organization ID for multi-tenant search scoping. When provided, search
              is scoped to memories within this organization.

          rank_results: Whether to enable additional ranking of search results. Default is false because
              results are already ranked when using an LLM for search (recommended approach).
              Only enable this if you're not using an LLM in your search pipeline and need
              additional result ranking.

          schema_id: Optional user-defined schema ID to use for this search. If provided, this schema
              (plus system schema) will be used for query generation. If not provided, system
              will automatically select relevant schema based on query content.

          search_override: Complete search override specification provided by developer

          simple_schema_mode: If true, uses simple schema mode: system schema + ONE most relevant user schema.
              This ensures better consistency between add/search operations and reduces query
              complexity. Recommended for production use.

          user_id: Optional internal user ID to filter search results by a specific user. If not
              provided, results are not filtered by user. If both user_id and external_user_id
              are provided, user_id takes precedence.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # Note: AsyncMemoryResource does not support ondevice processing
        # Ondevice processing is only available in the synchronous MemoryResource
        
        # Perform the main search
        extra_headers = {**strip_not_given({"Accept-Encoding": accept_encoding}), **(extra_headers or {})}
        return await self._post(
            "/v1/memory/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "enable_agentic_graph": enable_agentic_graph,
                    "external_user_id": external_user_id,
                    "metadata": metadata,
                    "namespace_id": namespace_id,
                    "organization_id": organization_id,
                    "rank_results": rank_results,
                    "schema_id": schema_id,
                    "search_override": search_override,
                    "simple_schema_mode": simple_schema_mode,
                    "user_id": user_id,
                },
                memory_search_params.MemorySearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "max_memories": max_memories,
                        "max_nodes": max_nodes,
                    },
                    memory_search_params.MemorySearchParams,
                ),
            ),
            cast_to=SearchResponse,
        )


class MemoryResourceWithRawResponse:
    def __init__(self, memory: MemoryResource) -> None:
        self._memory = memory

        self.update = to_raw_response_wrapper(
            memory.update,
        )
        self.delete = to_raw_response_wrapper(
            memory.delete,
        )
        self.add = to_raw_response_wrapper(
            memory.add,
        )
        self.add_batch = to_raw_response_wrapper(
            memory.add_batch,
        )
        self.delete_all = to_raw_response_wrapper(
            memory.delete_all,
        )
        self.get = to_raw_response_wrapper(
            memory.get,
        )
        self.sync_tiers = to_raw_response_wrapper(
            memory.sync_tiers,
        )
        self.search = to_raw_response_wrapper(
            memory.search,
        )


class AsyncMemoryResourceWithRawResponse:
    def __init__(self, memory: AsyncMemoryResource) -> None:
        self._memory = memory

        self.update = async_to_raw_response_wrapper(
            memory.update,
        )
        self.delete = async_to_raw_response_wrapper(
            memory.delete,
        )
        self.add = async_to_raw_response_wrapper(
            memory.add,
        )
        self.add_batch = async_to_raw_response_wrapper(
            memory.add_batch,
        )
        self.delete_all = async_to_raw_response_wrapper(
            memory.delete_all,
        )
        self.get = async_to_raw_response_wrapper(
            memory.get,
        )
        self.sync_tiers = async_to_raw_response_wrapper(
            memory.sync_tiers,
        )
        self.search = async_to_raw_response_wrapper(
            memory.search,
        )


class MemoryResourceWithStreamingResponse:
    def __init__(self, memory: MemoryResource) -> None:
        self._memory = memory

        self.update = to_streamed_response_wrapper(
            memory.update,
        )
        self.delete = to_streamed_response_wrapper(
            memory.delete,
        )
        self.add = to_streamed_response_wrapper(
            memory.add,
        )
        self.add_batch = to_streamed_response_wrapper(
            memory.add_batch,
        )
        self.delete_all = to_streamed_response_wrapper(
            memory.delete_all,
        )
        self.get = to_streamed_response_wrapper(
            memory.get,
        )
        self.sync_tiers = to_streamed_response_wrapper(
            memory.sync_tiers,
        )
        self.search = to_streamed_response_wrapper(
            memory.search,
        )


class AsyncMemoryResourceWithStreamingResponse:
    def __init__(self, memory: AsyncMemoryResource) -> None:
        self._memory = memory

        self.update = async_to_streamed_response_wrapper(
            memory.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            memory.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            memory.add,
        )
        self.add_batch = async_to_streamed_response_wrapper(
            memory.add_batch,
        )
        self.delete_all = async_to_streamed_response_wrapper(
            memory.delete_all,
        )
        self.get = async_to_streamed_response_wrapper(
            memory.get,
        )
        self.sync_tiers = async_to_streamed_response_wrapper(
            memory.sync_tiers,
        )
        self.search = async_to_streamed_response_wrapper(
            memory.search,
        )
