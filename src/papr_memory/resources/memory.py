# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import (
    MemoryType,
    memory_add_params,
    memory_delete_params,
    memory_search_params,
    memory_update_params,
    memory_add_batch_params,
    memory_delete_all_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.memory_type import MemoryType
from ..types.search_response import SearchResponse
from ..types.add_memory_param import AddMemoryParam
from ..types.context_item_param import ContextItemParam
from ..types.add_memory_response import AddMemoryResponse
from ..types.batch_memory_response import BatchMemoryResponse
from ..types.memory_metadata_param import MemoryMetadataParam
from ..types.memory_delete_response import MemoryDeleteResponse
from ..types.memory_update_response import MemoryUpdateResponse
from ..types.relationship_item_param import RelationshipItemParam

__all__ = ["MemoryResource", "AsyncMemoryResource"]


class MemoryResource(SyncAPIResource):
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

    def update(
        self,
        memory_id: str,
        *,
        content: Optional[str] | NotGiven = NOT_GIVEN,
        context: Optional[Iterable[ContextItemParam]] | NotGiven = NOT_GIVEN,
        metadata: Optional[MemoryMetadataParam] | NotGiven = NOT_GIVEN,
        relationships_json: Optional[Iterable[RelationshipItemParam]] | NotGiven = NOT_GIVEN,
        type: Optional[MemoryType] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        skip_parse: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        type: MemoryType,
        skip_background_processing: bool | NotGiven = NOT_GIVEN,
        context: Optional[Iterable[ContextItemParam]] | NotGiven = NOT_GIVEN,
        metadata: Optional[MemoryMetadataParam] | NotGiven = NOT_GIVEN,
        relationships_json: Optional[Iterable[RelationshipItemParam]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

            The API validates content size against MAX_CONTENT_LENGTH environment variable (defaults to 15000 bytes).

        Args:
          content: The content of the memory item you want to add to memory

          type: Valid memory types

          skip_background_processing: If True, skips adding background tasks for processing

          context: Context can be conversation history or any relevant context for a memory item

          metadata: Metadata for memory request

          relationships_json: Array of relationships that we can use in Graph DB (neo4J)

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
                    "type": type,
                    "context": context,
                    "metadata": metadata,
                    "relationships_json": relationships_json,
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
        skip_background_processing: bool | NotGiven = NOT_GIVEN,
        batch_size: Optional[int] | NotGiven = NOT_GIVEN,
        external_user_id: Optional[str] | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_secret: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_url: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        external_user_id: Optional[str] | NotGiven = NOT_GIVEN,
        skip_parse: bool | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    def get(
        self,
        memory_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    def search(
        self,
        *,
        query: str,
        max_memories: int | NotGiven = NOT_GIVEN,
        max_nodes: int | NotGiven = NOT_GIVEN,
        enable_agentic_graph: bool | NotGiven = NOT_GIVEN,
        external_user_id: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[MemoryMetadataParam] | NotGiven = NOT_GIVEN,
        rank_results: bool | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        accept_encoding: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchResponse:
        """
        Search through memories with authentication required.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

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

          rank_results: Whether to enable additional ranking of search results. Default is false because
              results are already ranked when using an LLM for search (recommended approach).
              Only enable this if you're not using an LLM in your search pipeline and need
              additional result ranking.

          user_id: Optional internal user ID to filter search results by a specific user. If not
              provided, results are not filtered by user. If both user_id and external_user_id
              are provided, user_id takes precedence.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Accept-Encoding": accept_encoding}), **(extra_headers or {})}
        return self._post(
            "/v1/memory/search",
            body=maybe_transform(
                {
                    "query": query,
                    "enable_agentic_graph": enable_agentic_graph,
                    "external_user_id": external_user_id,
                    "metadata": metadata,
                    "rank_results": rank_results,
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
        content: Optional[str] | NotGiven = NOT_GIVEN,
        context: Optional[Iterable[ContextItemParam]] | NotGiven = NOT_GIVEN,
        metadata: Optional[MemoryMetadataParam] | NotGiven = NOT_GIVEN,
        relationships_json: Optional[Iterable[RelationshipItemParam]] | NotGiven = NOT_GIVEN,
        type: Optional[MemoryType] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        skip_parse: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        type: MemoryType,
        skip_background_processing: bool | NotGiven = NOT_GIVEN,
        context: Optional[Iterable[ContextItemParam]] | NotGiven = NOT_GIVEN,
        metadata: Optional[MemoryMetadataParam] | NotGiven = NOT_GIVEN,
        relationships_json: Optional[Iterable[RelationshipItemParam]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

            The API validates content size against MAX_CONTENT_LENGTH environment variable (defaults to 15000 bytes).

        Args:
          content: The content of the memory item you want to add to memory

          type: Valid memory types

          skip_background_processing: If True, skips adding background tasks for processing

          context: Context can be conversation history or any relevant context for a memory item

          metadata: Metadata for memory request

          relationships_json: Array of relationships that we can use in Graph DB (neo4J)

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
                    "type": type,
                    "context": context,
                    "metadata": metadata,
                    "relationships_json": relationships_json,
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
        skip_background_processing: bool | NotGiven = NOT_GIVEN,
        batch_size: Optional[int] | NotGiven = NOT_GIVEN,
        external_user_id: Optional[str] | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_secret: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_url: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        external_user_id: Optional[str] | NotGiven = NOT_GIVEN,
        skip_parse: bool | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    async def get(
        self,
        memory_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    async def search(
        self,
        *,
        query: str,
        max_memories: int | NotGiven = NOT_GIVEN,
        max_nodes: int | NotGiven = NOT_GIVEN,
        enable_agentic_graph: bool | NotGiven = NOT_GIVEN,
        external_user_id: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[MemoryMetadataParam] | NotGiven = NOT_GIVEN,
        rank_results: bool | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        accept_encoding: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchResponse:
        """
        Search through memories with authentication required.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

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

          rank_results: Whether to enable additional ranking of search results. Default is false because
              results are already ranked when using an LLM for search (recommended approach).
              Only enable this if you're not using an LLM in your search pipeline and need
              additional result ranking.

          user_id: Optional internal user ID to filter search results by a specific user. If not
              provided, results are not filtered by user. If both user_id and external_user_id
              are provided, user_id takes precedence.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Accept-Encoding": accept_encoding}), **(extra_headers or {})}
        return await self._post(
            "/v1/memory/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "enable_agentic_graph": enable_agentic_graph,
                    "external_user_id": external_user_id,
                    "metadata": metadata,
                    "rank_results": rank_results,
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
        self.search = async_to_streamed_response_wrapper(
            memory.search,
        )
