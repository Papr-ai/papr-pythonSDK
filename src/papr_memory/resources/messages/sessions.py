# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.messages import session_retrieve_history_params
from ...types.messages.session_retrieve_history_response import SessionRetrieveHistoryResponse

__all__ = ["SessionsResource", "AsyncSessionsResource"]


class SessionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return SessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return SessionsResourceWithStreamingResponse(self)

    def process_messages(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Process all stored messages in a session that were previously stored with
        process_messages=false.

            **Authentication Required**: Bearer token, API key, or session token

            This endpoint allows you to retroactively process messages that were initially stored
            without processing. Useful for:
            - Processing messages after deciding you want them as memories
            - Batch processing large conversation sessions
            - Re-processing sessions with updated AI models

            **Processing Behavior**:
            - Only processes messages with status 'stored_only' or 'pending'
            - Uses the same smart batch analysis (every 15 messages)
            - Respects existing memory creation pipeline

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/v1/messages/sessions/{session_id}/process",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def retrieve_history(
        self,
        session_id: str,
        *,
        limit: int | Omit = omit,
        skip: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionRetrieveHistoryResponse:
        """
        Retrieve message history for a specific conversation session.

            **Authentication Required**: Bearer token, API key, or session token

            **Pagination**:
            - Use `limit` and `skip` parameters for pagination
            - Messages are returned in chronological order (oldest first)
            - `total_count` indicates total messages in the session

            **Access Control**:
            - Only returns messages for the authenticated user
            - Workspace scoping is applied if available

        Args:
          limit: Maximum number of messages to return

          skip: Number of messages to skip for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/v1/messages/sessions/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    session_retrieve_history_params.SessionRetrieveHistoryParams,
                ),
            ),
            cast_to=SessionRetrieveHistoryResponse,
        )

    def retrieve_status(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get processing status for messages in a session.

            **Authentication Required**: Bearer token, API key, or session token

            **Status Information**:
            - Total messages in session
            - Processing status breakdown (queued, analyzing, completed, failed)
            - Any messages with processing errors

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/v1/messages/sessions/{session_id}/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncSessionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AsyncSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AsyncSessionsResourceWithStreamingResponse(self)

    async def process_messages(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Process all stored messages in a session that were previously stored with
        process_messages=false.

            **Authentication Required**: Bearer token, API key, or session token

            This endpoint allows you to retroactively process messages that were initially stored
            without processing. Useful for:
            - Processing messages after deciding you want them as memories
            - Batch processing large conversation sessions
            - Re-processing sessions with updated AI models

            **Processing Behavior**:
            - Only processes messages with status 'stored_only' or 'pending'
            - Uses the same smart batch analysis (every 15 messages)
            - Respects existing memory creation pipeline

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/v1/messages/sessions/{session_id}/process",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def retrieve_history(
        self,
        session_id: str,
        *,
        limit: int | Omit = omit,
        skip: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionRetrieveHistoryResponse:
        """
        Retrieve message history for a specific conversation session.

            **Authentication Required**: Bearer token, API key, or session token

            **Pagination**:
            - Use `limit` and `skip` parameters for pagination
            - Messages are returned in chronological order (oldest first)
            - `total_count` indicates total messages in the session

            **Access Control**:
            - Only returns messages for the authenticated user
            - Workspace scoping is applied if available

        Args:
          limit: Maximum number of messages to return

          skip: Number of messages to skip for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/v1/messages/sessions/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    session_retrieve_history_params.SessionRetrieveHistoryParams,
                ),
            ),
            cast_to=SessionRetrieveHistoryResponse,
        )

    async def retrieve_status(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get processing status for messages in a session.

            **Authentication Required**: Bearer token, API key, or session token

            **Status Information**:
            - Total messages in session
            - Processing status breakdown (queued, analyzing, completed, failed)
            - Any messages with processing errors

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/v1/messages/sessions/{session_id}/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class SessionsResourceWithRawResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.process_messages = to_raw_response_wrapper(
            sessions.process_messages,
        )
        self.retrieve_history = to_raw_response_wrapper(
            sessions.retrieve_history,
        )
        self.retrieve_status = to_raw_response_wrapper(
            sessions.retrieve_status,
        )


class AsyncSessionsResourceWithRawResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.process_messages = async_to_raw_response_wrapper(
            sessions.process_messages,
        )
        self.retrieve_history = async_to_raw_response_wrapper(
            sessions.retrieve_history,
        )
        self.retrieve_status = async_to_raw_response_wrapper(
            sessions.retrieve_status,
        )


class SessionsResourceWithStreamingResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.process_messages = to_streamed_response_wrapper(
            sessions.process_messages,
        )
        self.retrieve_history = to_streamed_response_wrapper(
            sessions.retrieve_history,
        )
        self.retrieve_status = to_streamed_response_wrapper(
            sessions.retrieve_status,
        )


class AsyncSessionsResourceWithStreamingResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.process_messages = async_to_streamed_response_wrapper(
            sessions.process_messages,
        )
        self.retrieve_history = async_to_streamed_response_wrapper(
            sessions.retrieve_history,
        )
        self.retrieve_status = async_to_streamed_response_wrapper(
            sessions.retrieve_status,
        )
