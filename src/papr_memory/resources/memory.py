# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    MemoryType,
    memory_add_params,
    memory_get_params,
    memory_delete_params,
    memory_search_params,
    memory_update_params,
    memory_add_batch_params,
    memory_delete_all_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.graph_generation_param import GraphGenerationParam
from ..types.memory_delete_response import MemoryDeleteResponse
from ..types.memory_update_response import MemoryUpdateResponse
from ..types.relationship_item_param import RelationshipItemParam
from ..types.shared_params.memory_policy import MemoryPolicy

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
        content: Optional[str] | Omit = omit,
        context: Optional[Iterable[ContextItemParam]] | Omit = omit,
        graph_generation: Optional[GraphGenerationParam] | Omit = omit,
        link_to: Union[str, SequenceNotStr[str], Dict[str, object], None] | Omit = omit,
        memory_policy: Optional[MemoryPolicy] | Omit = omit,
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

          graph_generation: Graph generation configuration

          link_to: Shorthand DSL for node/edge constraints. Expands to
              memory_policy.node_constraints and edge_constraints. Formats: - String:
              'Task:title' (semantic match on Task.title) - List: ['Task:title',
              'Person:email'] (multiple constraints) - Dict: {'Task:title': {'set': {...}}}
              (with options) Syntax: - Node: 'Type:property', 'Type:prop=value' (exact),
              'Type:prop~value' (semantic) - Edge: 'Source->EDGE->Target:property' (arrow
              syntax) - Via: 'Type.via(EDGE->Target:prop)' (relationship traversal) - Special:
              '$this', '$previous', '$context:N' Example:
              'SecurityBehavior->MITIGATES->TacticDef:name' with {'create': 'never'}

          memory_policy: Unified memory processing policy.

              This is the SINGLE source of truth for how a memory should be processed,
              combining graph generation control AND OMO (Open Memory Object) safety
              standards.

              **Graph Generation Modes:**

              - auto: LLM extracts entities freely (default)
              - manual: Developer provides exact nodes (no LLM extraction)

              **OMO Safety Standards:**

              - consent: How data owner allowed storage (explicit, implicit, terms, none)
              - risk: Safety assessment (none, sensitive, flagged)
              - acl: Access control list for read/write permissions

              **Schema Integration:**

              - schema_id: Reference a schema that may have its own default memory_policy
              - Schema-level policies are merged with request-level (request takes precedence)

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
                    "graph_generation": graph_generation,
                    "link_to": link_to,
                    "memory_policy": memory_policy,
                    "graph_generation": graph_generation,
                    "link_to": link_to,
                    "memory_policy": memory_policy,
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
        enable_holographic: bool | Omit = omit,
        format: Optional[str] | Omit = omit,
        skip_background_processing: bool | Omit = omit,
        context: Optional[Iterable[ContextItemParam]] | Omit = omit,
        external_user_id: Optional[str] | Omit = omit,
        graph_generation: Optional[GraphGenerationParam] | Omit = omit,
        link_to: Union[str, SequenceNotStr[str], Dict[str, object], None] | Omit = omit,
        memory_policy: Optional[MemoryPolicy] | Omit = omit,
        metadata: Optional[MemoryMetadataParam] | Omit = omit,
        namespace_id: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        relationships_json: Optional[Iterable[RelationshipItemParam]] | Omit = omit,
        type: MemoryType | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
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

          enable_holographic: If True, applies holographic neural transforms and stores in holographic
              collection

          format: Response format. Use 'omo' for Open Memory Object standard format (portable
              across platforms).

          skip_background_processing: If True, skips adding background tasks for processing

          context: Conversation history context for this memory. Use for providing message history
              when adding a memory. Format: [{role: 'user'|'assistant', content: '...'}]

          external_user_id: Your application's user identifier. This is the primary way to identify users.
              Use this for your app's user IDs (e.g., 'user_alice_123', UUID, email). Papr
              will automatically resolve or create internal users as needed.

          graph_generation: Graph generation configuration

          link_to: Shorthand DSL for node/edge constraints. Expands to
              memory_policy.node_constraints and edge_constraints. Formats: - String:
              'Task:title' (semantic match on Task.title) - List: ['Task:title',
              'Person:email'] (multiple constraints) - Dict: {'Task:title': {'set': {...}}}
              (with options) Syntax: - Node: 'Type:property', 'Type:prop=value' (exact),
              'Type:prop~value' (semantic) - Edge: 'Source->EDGE->Target:property' (arrow
              syntax) - Via: 'Type.via(EDGE->Target:prop)' (relationship traversal) - Special:
              '$this', '$previous', '$context:N' Example:
              'SecurityBehavior->MITIGATES->TacticDef:name' with {'create': 'never'}

          memory_policy: Unified memory processing policy.

              This is the SINGLE source of truth for how a memory should be processed,
              combining graph generation control AND OMO (Open Memory Object) safety
              standards.

              **Graph Generation Modes:**

              - auto: LLM extracts entities freely (default)
              - manual: Developer provides exact nodes (no LLM extraction)

              **OMO Safety Standards:**

              - consent: How data owner allowed storage (explicit, implicit, terms, none)
              - risk: Safety assessment (none, sensitive, flagged)
              - acl: Access control list for read/write permissions

              **Schema Integration:**

              - schema_id: Reference a schema that may have its own default memory_policy
              - Schema-level policies are merged with request-level (request takes precedence)

          metadata: Metadata for memory request

          namespace_id: Optional namespace ID for multi-tenant memory scoping. When provided, memory is
              associated with this namespace.

          organization_id: Optional organization ID for multi-tenant memory scoping. When provided, memory
              is associated with this organization.

          relationships_json:
              DEPRECATED: Use 'memory_policy' instead. Migration options: 1. Specific memory:
              relationships=[{source: '$this', target: 'mem_123', type: 'FOLLOWS'}] 2.
              Previous memory: link_to_previous_memory=True 3. Related memories:
              link_to_related_memories=3

          type: Memory item type; defaults to 'text' if omitted

          user_id: DEPRECATED: Use 'external_user_id' instead. Internal Papr Parse user ID. Most
              developers should not use this field directly.

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
                    "external_user_id": external_user_id,
                    "graph_generation": graph_generation,
                    "link_to": link_to,
                    "memory_policy": memory_policy,
                    "metadata": metadata,
                    "namespace_id": namespace_id,
                    "organization_id": organization_id,
                    "relationships_json": relationships_json,
                    "type": type,
                    "user_id": user_id,
                },
                memory_add_params.MemoryAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "enable_holographic": enable_holographic,
                        "format": format,
                        "skip_background_processing": skip_background_processing,
                    },
                    memory_add_params.MemoryAddParams,
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
        link_to: Union[str, SequenceNotStr[str], Dict[str, object], None] | Omit = omit,
        memory_policy: Optional[MemoryPolicy] | Omit = omit,
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

          external_user_id: Your application's user identifier for all memories in the batch. This is the
              primary way to identify users. Papr will automatically resolve or create
              internal users as needed.

          graph_generation: Graph generation configuration

          link_to: Shorthand DSL for node/edge constraints. Expands to
              memory_policy.node_constraints and edge_constraints. Formats: - String:
              'Task:title' (semantic match on Task.title) - List: ['Task:title',
              'Person:email'] (multiple constraints) - Dict: {'Task:title': {'set': {...}}}
              (with options) Syntax: - Node: 'Type:property', 'Type:prop=value' (exact),
              'Type:prop~value' (semantic) - Edge: 'Source->EDGE->Target:property' (arrow
              syntax) - Via: 'Type.via(EDGE->Target:prop)' (relationship traversal) - Special:
              '$this', '$previous', '$context:N' Example:
              'SecurityBehavior->MITIGATES->TacticDef:name' with {'create': 'never'}

          memory_policy: Unified memory processing policy.

              This is the SINGLE source of truth for how a memory should be processed,
              combining graph generation control AND OMO (Open Memory Object) safety
              standards.

              **Graph Generation Modes:**

              - auto: LLM extracts entities freely (default)
              - manual: Developer provides exact nodes (no LLM extraction)

              **OMO Safety Standards:**

              - consent: How data owner allowed storage (explicit, implicit, terms, none)
              - risk: Safety assessment (none, sensitive, flagged)
              - acl: Access control list for read/write permissions

              **Schema Integration:**

              - schema_id: Reference a schema that may have its own default memory_policy
              - Schema-level policies are merged with request-level (request takes precedence)

          namespace_id: Optional namespace ID for multi-tenant batch memory scoping. When provided, all
              memories in the batch are associated with this namespace.

          organization_id: Optional organization ID for multi-tenant batch memory scoping. When provided,
              all memories in the batch are associated with this organization.

          user_id: DEPRECATED: Use 'external_user_id' instead. Internal Papr Parse user ID.

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
                    "link_to": link_to,
                    "memory_policy": memory_policy,
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

    def get(
        self,
        memory_id: str,
        *,
        exclude_flagged: bool | Omit = omit,
        max_risk: Optional[str] | Omit = omit,
        require_consent: bool | Omit = omit,
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
          exclude_flagged: If true, return 404 if the memory has risk='flagged'. Filters out flagged
              content.

          max_risk: Maximum risk level allowed. Values: 'none', 'sensitive', 'flagged'. If memory
              exceeds this, return 404.

          require_consent: If true, return 404 if the memory has consent='none'. Ensures only consented
              memories are returned.

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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "exclude_flagged": exclude_flagged,
                        "max_risk": max_risk,
                        "require_consent": require_consent,
                    },
                    memory_get_params.MemoryGetParams,
                ),
            ),
            cast_to=SearchResponse,
        )

    def search(
        self,
        *,
        query: str,
        max_memories: int | Omit = omit,
        max_nodes: int | Omit = omit,
        response_format: Literal["json", "toon"] | Omit = omit,
        enable_agentic_graph: bool | Omit = omit,
        external_user_id: Optional[str] | Omit = omit,
        holographic_config: Optional[memory_search_params.HolographicConfig] | Omit = omit,
        metadata: Optional[MemoryMetadataParam] | Omit = omit,
        namespace_id: Optional[str] | Omit = omit,
        omo_filter: Optional[memory_search_params.OmoFilter] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        rank_results: bool | Omit = omit,
        reranking_config: Optional[memory_search_params.RerankingConfig] | Omit = omit,
        schema_id: Optional[str] | Omit = omit,
        search_override: Optional[memory_search_params.SearchOverride] | Omit = omit,
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

            **Response Format Options**:
            Choose between standard JSON or TOON (Token-Oriented Object Notation) format:
            - **JSON (default)**: Standard JSON response format
            - **TOON**: Optimized format achieving 30-60% token reduction for LLM contexts
              - Use `response_format=toon` query parameter
              - Returns `text/plain` with TOON-formatted content
              - Ideal for LLM integrations to reduce API costs and latency
              - Maintains semantic clarity while minimizing token usage
              - Example: `/v1/memory/search?response_format=toon`

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
            - Use `response_format: toon` when integrating with LLMs to reduce token costs by 30-60%

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

          response_format: Response format: 'json' (default) or 'toon' (Token-Oriented Object Notation for
              30-60% token reduction in LLM contexts)

          enable_agentic_graph: HIGHLY RECOMMENDED: Enable agentic graph search for intelligent, context-aware
              results. When enabled, the system can understand ambiguous references by first
              identifying specific entities from your memory graph, then performing targeted
              searches. Examples: 'customer feedback' → identifies your customers first, then
              finds their specific feedback; 'project issues' → identifies your projects
              first, then finds related issues; 'team meeting notes' → identifies team members
              first, then finds meeting notes. This provides much more relevant and
              comprehensive results. Set to false only if you need faster, simpler
              keyword-based search.

          external_user_id: Your application's user identifier to filter search results. This is the primary
              way to identify users. Use this for your app's user IDs (e.g., 'user_alice_123',
              UUID, email).

          holographic_config: Configuration for holographic neural embedding transforms and H-COND scoring.

              Neural holographic embeddings use 13 brain-inspired frequency bands to encode
              hierarchical semantic metadata alongside the base embedding. H-COND (Holographic
              CONDitional) scoring uses phase alignment for improved relevance ranking.

          metadata: Metadata for memory request

          namespace_id: Optional namespace ID for multi-tenant search scoping. When provided, search is
              scoped to memories within this namespace.

          omo_filter: Filter for Open Memory Object (OMO) safety standards in search/retrieval.

              Use this to filter search results by consent level and/or risk level.

          organization_id: Optional organization ID for multi-tenant search scoping. When provided, search
              is scoped to memories within this organization.

          rank_results: DEPRECATED: Use 'reranking_config' instead. Whether to enable additional ranking
              of search results. Default is false because results are already ranked when
              using an LLM for search (recommended approach). Only enable this if you're not
              using an LLM in your search pipeline and need additional result ranking.
              Migration: Replace 'rank_results: true' with 'reranking_config:
              {reranking_enabled: true, reranking_provider: "cohere", reranking_model:
              "rerank-v3.5"}'

          reranking_config: Configuration for reranking memory search results

          schema_id: Optional user-defined schema ID to use for this search. If provided, this schema
              (plus system schema) will be used for query generation. If not provided, system
              will automatically select relevant schema based on query content.

          search_override: Complete search override specification provided by developer

          user_id: DEPRECATED: Use 'external_user_id' instead. Internal Papr Parse user ID. Most
              developers should not use this field directly.

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
                    "holographic_config": holographic_config,
                    "metadata": metadata,
                    "namespace_id": namespace_id,
                    "omo_filter": omo_filter,
                    "organization_id": organization_id,
                    "rank_results": rank_results,
                    "reranking_config": reranking_config,
                    "schema_id": schema_id,
                    "search_override": search_override,
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
                        "response_format": response_format,
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
        graph_generation: Optional[GraphGenerationParam] | Omit = omit,
        link_to: Union[str, SequenceNotStr[str], Dict[str, object], None] | Omit = omit,
        memory_policy: Optional[MemoryPolicy] | Omit = omit,
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

          graph_generation: Graph generation configuration

          link_to: Shorthand DSL for node/edge constraints. Expands to
              memory_policy.node_constraints and edge_constraints. Formats: - String:
              'Task:title' (semantic match on Task.title) - List: ['Task:title',
              'Person:email'] (multiple constraints) - Dict: {'Task:title': {'set': {...}}}
              (with options) Syntax: - Node: 'Type:property', 'Type:prop=value' (exact),
              'Type:prop~value' (semantic) - Edge: 'Source->EDGE->Target:property' (arrow
              syntax) - Via: 'Type.via(EDGE->Target:prop)' (relationship traversal) - Special:
              '$this', '$previous', '$context:N' Example:
              'SecurityBehavior->MITIGATES->TacticDef:name' with {'create': 'never'}

          memory_policy: Unified memory processing policy.

              This is the SINGLE source of truth for how a memory should be processed,
              combining graph generation control AND OMO (Open Memory Object) safety
              standards.

              **Graph Generation Modes:**

              - auto: LLM extracts entities freely (default)
              - manual: Developer provides exact nodes (no LLM extraction)

              **OMO Safety Standards:**

              - consent: How data owner allowed storage (explicit, implicit, terms, none)
              - risk: Safety assessment (none, sensitive, flagged)
              - acl: Access control list for read/write permissions

              **Schema Integration:**

              - schema_id: Reference a schema that may have its own default memory_policy
              - Schema-level policies are merged with request-level (request takes precedence)

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
                    "graph_generation": graph_generation,
                    "link_to": link_to,
                    "memory_policy": memory_policy,
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
        enable_holographic: bool | Omit = omit,
        format: Optional[str] | Omit = omit,
        skip_background_processing: bool | Omit = omit,
        context: Optional[Iterable[ContextItemParam]] | Omit = omit,
        external_user_id: Optional[str] | Omit = omit,
        graph_generation: Optional[GraphGenerationParam] | Omit = omit,
        link_to: Union[str, SequenceNotStr[str], Dict[str, object], None] | Omit = omit,
        memory_policy: Optional[MemoryPolicy] | Omit = omit,
        metadata: Optional[MemoryMetadataParam] | Omit = omit,
        namespace_id: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        relationships_json: Optional[Iterable[RelationshipItemParam]] | Omit = omit,
        type: MemoryType | Omit = omit,
        user_id: Optional[str] | Omit = omit,
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

          enable_holographic: If True, applies holographic neural transforms and stores in holographic
              collection

          format: Response format. Use 'omo' for Open Memory Object standard format (portable
              across platforms).

          skip_background_processing: If True, skips adding background tasks for processing

          context: Conversation history context for this memory. Use for providing message history
              when adding a memory. Format: [{role: 'user'|'assistant', content: '...'}]

          external_user_id: Your application's user identifier. This is the primary way to identify users.
              Use this for your app's user IDs (e.g., 'user_alice_123', UUID, email). Papr
              will automatically resolve or create internal users as needed.

          graph_generation: Graph generation configuration

          link_to: Shorthand DSL for node/edge constraints. Expands to
              memory_policy.node_constraints and edge_constraints. Formats: - String:
              'Task:title' (semantic match on Task.title) - List: ['Task:title',
              'Person:email'] (multiple constraints) - Dict: {'Task:title': {'set': {...}}}
              (with options) Syntax: - Node: 'Type:property', 'Type:prop=value' (exact),
              'Type:prop~value' (semantic) - Edge: 'Source->EDGE->Target:property' (arrow
              syntax) - Via: 'Type.via(EDGE->Target:prop)' (relationship traversal) - Special:
              '$this', '$previous', '$context:N' Example:
              'SecurityBehavior->MITIGATES->TacticDef:name' with {'create': 'never'}

          memory_policy: Unified memory processing policy.

              This is the SINGLE source of truth for how a memory should be processed,
              combining graph generation control AND OMO (Open Memory Object) safety
              standards.

              **Graph Generation Modes:**

              - auto: LLM extracts entities freely (default)
              - manual: Developer provides exact nodes (no LLM extraction)

              **OMO Safety Standards:**

              - consent: How data owner allowed storage (explicit, implicit, terms, none)
              - risk: Safety assessment (none, sensitive, flagged)
              - acl: Access control list for read/write permissions

              **Schema Integration:**

              - schema_id: Reference a schema that may have its own default memory_policy
              - Schema-level policies are merged with request-level (request takes precedence)

          metadata: Metadata for memory request

          namespace_id: Optional namespace ID for multi-tenant memory scoping. When provided, memory is
              associated with this namespace.

          organization_id: Optional organization ID for multi-tenant memory scoping. When provided, memory
              is associated with this organization.

          relationships_json:
              DEPRECATED: Use 'memory_policy' instead. Migration options: 1. Specific memory:
              relationships=[{source: '$this', target: 'mem_123', type: 'FOLLOWS'}] 2.
              Previous memory: link_to_previous_memory=True 3. Related memories:
              link_to_related_memories=3

          type: Memory item type; defaults to 'text' if omitted

          user_id: DEPRECATED: Use 'external_user_id' instead. Internal Papr Parse user ID. Most
              developers should not use this field directly.

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
                    "external_user_id": external_user_id,
                    "graph_generation": graph_generation,
                    "link_to": link_to,
                    "memory_policy": memory_policy,
                    "metadata": metadata,
                    "namespace_id": namespace_id,
                    "organization_id": organization_id,
                    "relationships_json": relationships_json,
                    "type": type,
                    "user_id": user_id,
                },
                memory_add_params.MemoryAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "enable_holographic": enable_holographic,
                        "format": format,
                        "skip_background_processing": skip_background_processing,
                    },
                    memory_add_params.MemoryAddParams,
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
        link_to: Union[str, SequenceNotStr[str], Dict[str, object], None] | Omit = omit,
        memory_policy: Optional[MemoryPolicy] | Omit = omit,
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

          external_user_id: Your application's user identifier for all memories in the batch. This is the
              primary way to identify users. Papr will automatically resolve or create
              internal users as needed.

          graph_generation: Graph generation configuration

          link_to: Shorthand DSL for node/edge constraints. Expands to
              memory_policy.node_constraints and edge_constraints. Formats: - String:
              'Task:title' (semantic match on Task.title) - List: ['Task:title',
              'Person:email'] (multiple constraints) - Dict: {'Task:title': {'set': {...}}}
              (with options) Syntax: - Node: 'Type:property', 'Type:prop=value' (exact),
              'Type:prop~value' (semantic) - Edge: 'Source->EDGE->Target:property' (arrow
              syntax) - Via: 'Type.via(EDGE->Target:prop)' (relationship traversal) - Special:
              '$this', '$previous', '$context:N' Example:
              'SecurityBehavior->MITIGATES->TacticDef:name' with {'create': 'never'}

          memory_policy: Unified memory processing policy.

              This is the SINGLE source of truth for how a memory should be processed,
              combining graph generation control AND OMO (Open Memory Object) safety
              standards.

              **Graph Generation Modes:**

              - auto: LLM extracts entities freely (default)
              - manual: Developer provides exact nodes (no LLM extraction)

              **OMO Safety Standards:**

              - consent: How data owner allowed storage (explicit, implicit, terms, none)
              - risk: Safety assessment (none, sensitive, flagged)
              - acl: Access control list for read/write permissions

              **Schema Integration:**

              - schema_id: Reference a schema that may have its own default memory_policy
              - Schema-level policies are merged with request-level (request takes precedence)

          namespace_id: Optional namespace ID for multi-tenant batch memory scoping. When provided, all
              memories in the batch are associated with this namespace.

          organization_id: Optional organization ID for multi-tenant batch memory scoping. When provided,
              all memories in the batch are associated with this organization.

          user_id: DEPRECATED: Use 'external_user_id' instead. Internal Papr Parse user ID.

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
                    "link_to": link_to,
                    "memory_policy": memory_policy,
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

    async def get(
        self,
        memory_id: str,
        *,
        exclude_flagged: bool | Omit = omit,
        max_risk: Optional[str] | Omit = omit,
        require_consent: bool | Omit = omit,
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
          exclude_flagged: If true, return 404 if the memory has risk='flagged'. Filters out flagged
              content.

          max_risk: Maximum risk level allowed. Values: 'none', 'sensitive', 'flagged'. If memory
              exceeds this, return 404.

          require_consent: If true, return 404 if the memory has consent='none'. Ensures only consented
              memories are returned.

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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "exclude_flagged": exclude_flagged,
                        "max_risk": max_risk,
                        "require_consent": require_consent,
                    },
                    memory_get_params.MemoryGetParams,
                ),
            ),
            cast_to=SearchResponse,
        )

    async def search(
        self,
        *,
        query: str,
        max_memories: int | Omit = omit,
        max_nodes: int | Omit = omit,
        response_format: Literal["json", "toon"] | Omit = omit,
        enable_agentic_graph: bool | Omit = omit,
        external_user_id: Optional[str] | Omit = omit,
        holographic_config: Optional[memory_search_params.HolographicConfig] | Omit = omit,
        metadata: Optional[MemoryMetadataParam] | Omit = omit,
        namespace_id: Optional[str] | Omit = omit,
        omo_filter: Optional[memory_search_params.OmoFilter] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        rank_results: bool | Omit = omit,
        reranking_config: Optional[memory_search_params.RerankingConfig] | Omit = omit,
        schema_id: Optional[str] | Omit = omit,
        search_override: Optional[memory_search_params.SearchOverride] | Omit = omit,
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

            **Response Format Options**:
            Choose between standard JSON or TOON (Token-Oriented Object Notation) format:
            - **JSON (default)**: Standard JSON response format
            - **TOON**: Optimized format achieving 30-60% token reduction for LLM contexts
              - Use `response_format=toon` query parameter
              - Returns `text/plain` with TOON-formatted content
              - Ideal for LLM integrations to reduce API costs and latency
              - Maintains semantic clarity while minimizing token usage
              - Example: `/v1/memory/search?response_format=toon`

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
            - Use `response_format: toon` when integrating with LLMs to reduce token costs by 30-60%

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

          response_format: Response format: 'json' (default) or 'toon' (Token-Oriented Object Notation for
              30-60% token reduction in LLM contexts)

          enable_agentic_graph: HIGHLY RECOMMENDED: Enable agentic graph search for intelligent, context-aware
              results. When enabled, the system can understand ambiguous references by first
              identifying specific entities from your memory graph, then performing targeted
              searches. Examples: 'customer feedback' → identifies your customers first, then
              finds their specific feedback; 'project issues' → identifies your projects
              first, then finds related issues; 'team meeting notes' → identifies team members
              first, then finds meeting notes. This provides much more relevant and
              comprehensive results. Set to false only if you need faster, simpler
              keyword-based search.

          external_user_id: Your application's user identifier to filter search results. This is the primary
              way to identify users. Use this for your app's user IDs (e.g., 'user_alice_123',
              UUID, email).

          holographic_config: Configuration for holographic neural embedding transforms and H-COND scoring.

              Neural holographic embeddings use 13 brain-inspired frequency bands to encode
              hierarchical semantic metadata alongside the base embedding. H-COND (Holographic
              CONDitional) scoring uses phase alignment for improved relevance ranking.

          metadata: Metadata for memory request

          namespace_id: Optional namespace ID for multi-tenant search scoping. When provided, search is
              scoped to memories within this namespace.

          omo_filter: Filter for Open Memory Object (OMO) safety standards in search/retrieval.

              Use this to filter search results by consent level and/or risk level.

          organization_id: Optional organization ID for multi-tenant search scoping. When provided, search
              is scoped to memories within this organization.

          rank_results: DEPRECATED: Use 'reranking_config' instead. Whether to enable additional ranking
              of search results. Default is false because results are already ranked when
              using an LLM for search (recommended approach). Only enable this if you're not
              using an LLM in your search pipeline and need additional result ranking.
              Migration: Replace 'rank_results: true' with 'reranking_config:
              {reranking_enabled: true, reranking_provider: "cohere", reranking_model:
              "rerank-v3.5"}'

          reranking_config: Configuration for reranking memory search results

          schema_id: Optional user-defined schema ID to use for this search. If provided, this schema
              (plus system schema) will be used for query generation. If not provided, system
              will automatically select relevant schema based on query content.

          search_override: Complete search override specification provided by developer

          user_id: DEPRECATED: Use 'external_user_id' instead. Internal Papr Parse user ID. Most
              developers should not use this field directly.

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
                    "holographic_config": holographic_config,
                    "metadata": metadata,
                    "namespace_id": namespace_id,
                    "omo_filter": omo_filter,
                    "organization_id": organization_id,
                    "rank_results": rank_results,
                    "reranking_config": reranking_config,
                    "schema_id": schema_id,
                    "search_override": search_override,
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
                        "response_format": response_format,
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
