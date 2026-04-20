# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal

import httpx

from ...types import message_store_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .sessions import (
    SessionsResource,
    AsyncSessionsResource,
    SessionsResourceWithRawResponse,
    AsyncSessionsResourceWithRawResponse,
    SessionsResourceWithStreamingResponse,
    AsyncSessionsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.memory_metadata_param import MemoryMetadataParam
from ...types.graph_generation_param import GraphGenerationParam
from ...types.message_store_response import MessageStoreResponse
from ...types.shared_params.memory_policy import MemoryPolicy

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def sessions(self) -> SessionsResource:
        return SessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    def store(
        self,
        *,
        content: Union[str, Iterable[Dict[str, object]]],
        role: Literal["user", "assistant"],
        session_id: str,
        context: Optional[Iterable[Dict[str, object]]] | Omit = omit,
        graph_generation: Optional[GraphGenerationParam] | Omit = omit,
        memory_policy: Optional[MemoryPolicy] | Omit = omit,
        metadata: Optional[MemoryMetadataParam] | Omit = omit,
        namespace_id: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        process_messages: bool | Omit = omit,
        relationships_json: Optional[Iterable[Dict[str, object]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageStoreResponse:
        """
        Store a chat message and queue it for AI analysis and memory creation.

            **Authentication Required**: Bearer token, API key, or session token

            **Processing Control**:
            - Set `process_messages: true` (default) to enable full AI analysis and memory creation
            - Set `process_messages: false` to store messages only without processing into memories

            **Processing Flow** (when process_messages=true):
            1. Message is immediately stored in PostMessage class
            2. Background processing analyzes the message for memory-worthiness
            3. If worthy, creates a memory with appropriate role-based categorization
            4. Links the message to the created memory

            **Role-Based Categories**:
            - **User messages**: preference, task, goal, facts, context
            - **Assistant messages**: skills, learning

            **Session Management**:
            - `sessionId` is required to group related messages
            - Use the same `sessionId` for an entire conversation
            - Retrieve conversation history using GET /messages/sessions/{sessionId}

        Args:
          content: The content of the chat message - can be a simple string or structured content
              objects

          role: Role of the message sender (user or assistant)

          session_id: Session ID to group related messages in a conversation

          context: Optional context for the message (conversation history or relevant context)

          graph_generation: Graph generation configuration

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

          namespace_id: Optional namespace ID for multi-tenant message scoping

          organization_id: Optional organization ID for multi-tenant message scoping

          process_messages: Whether to process messages into memories (true) or just store them (false).
              Default is true.

          relationships_json: Optional array of relationships for Graph DB (Neo4j)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/messages",
            body=maybe_transform(
                {
                    "content": content,
                    "role": role,
                    "session_id": session_id,
                    "context": context,
                    "graph_generation": graph_generation,
                    "memory_policy": memory_policy,
                    "metadata": metadata,
                    "namespace_id": namespace_id,
                    "organization_id": organization_id,
                    "process_messages": process_messages,
                    "relationships_json": relationships_json,
                },
                message_store_params.MessageStoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageStoreResponse,
        )


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def sessions(self) -> AsyncSessionsResource:
        return AsyncSessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    async def store(
        self,
        *,
        content: Union[str, Iterable[Dict[str, object]]],
        role: Literal["user", "assistant"],
        session_id: str,
        context: Optional[Iterable[Dict[str, object]]] | Omit = omit,
        graph_generation: Optional[GraphGenerationParam] | Omit = omit,
        memory_policy: Optional[MemoryPolicy] | Omit = omit,
        metadata: Optional[MemoryMetadataParam] | Omit = omit,
        namespace_id: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        process_messages: bool | Omit = omit,
        relationships_json: Optional[Iterable[Dict[str, object]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageStoreResponse:
        """
        Store a chat message and queue it for AI analysis and memory creation.

            **Authentication Required**: Bearer token, API key, or session token

            **Processing Control**:
            - Set `process_messages: true` (default) to enable full AI analysis and memory creation
            - Set `process_messages: false` to store messages only without processing into memories

            **Processing Flow** (when process_messages=true):
            1. Message is immediately stored in PostMessage class
            2. Background processing analyzes the message for memory-worthiness
            3. If worthy, creates a memory with appropriate role-based categorization
            4. Links the message to the created memory

            **Role-Based Categories**:
            - **User messages**: preference, task, goal, facts, context
            - **Assistant messages**: skills, learning

            **Session Management**:
            - `sessionId` is required to group related messages
            - Use the same `sessionId` for an entire conversation
            - Retrieve conversation history using GET /messages/sessions/{sessionId}

        Args:
          content: The content of the chat message - can be a simple string or structured content
              objects

          role: Role of the message sender (user or assistant)

          session_id: Session ID to group related messages in a conversation

          context: Optional context for the message (conversation history or relevant context)

          graph_generation: Graph generation configuration

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

          namespace_id: Optional namespace ID for multi-tenant message scoping

          organization_id: Optional organization ID for multi-tenant message scoping

          process_messages: Whether to process messages into memories (true) or just store them (false).
              Default is true.

          relationships_json: Optional array of relationships for Graph DB (Neo4j)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/messages",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "role": role,
                    "session_id": session_id,
                    "context": context,
                    "graph_generation": graph_generation,
                    "memory_policy": memory_policy,
                    "metadata": metadata,
                    "namespace_id": namespace_id,
                    "organization_id": organization_id,
                    "process_messages": process_messages,
                    "relationships_json": relationships_json,
                },
                message_store_params.MessageStoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageStoreResponse,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.store = to_raw_response_wrapper(
            messages.store,
        )

    @cached_property
    def sessions(self) -> SessionsResourceWithRawResponse:
        return SessionsResourceWithRawResponse(self._messages.sessions)


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.store = async_to_raw_response_wrapper(
            messages.store,
        )

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithRawResponse:
        return AsyncSessionsResourceWithRawResponse(self._messages.sessions)


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.store = to_streamed_response_wrapper(
            messages.store,
        )

    @cached_property
    def sessions(self) -> SessionsResourceWithStreamingResponse:
        return SessionsResourceWithStreamingResponse(self._messages.sessions)


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.store = async_to_streamed_response_wrapper(
            messages.store,
        )

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithStreamingResponse:
        return AsyncSessionsResourceWithStreamingResponse(self._messages.sessions)
