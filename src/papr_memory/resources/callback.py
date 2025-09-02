# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.callback_process_response import CallbackProcessResponse

__all__ = ["CallbackResource", "AsyncCallbackResource"]


class CallbackResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CallbackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return CallbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallbackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return CallbackResourceWithStreamingResponse(self)

    def process(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallbackProcessResponse:
        """OAuth2 callback endpoint.

        Processes the authorization code from Auth0.

            **Query Parameters:**
            - `code`: Authorization code from Auth0 (required)
            - `state`: State parameter for CSRF protection (required)

            **Flow:**
            1. Auth0 redirects to this endpoint after successful authentication
            2. This endpoint validates the authorization code and state
            3. Redirects back to the original `redirect_uri` with code and state
            4. Client can then exchange the code for tokens at `/token` endpoint

            **Security:**
            - Validates state parameter to prevent CSRF attacks
            - Checks authorization code expiration
            - Cleans up session data after processing
        """
        return self._get(
            "/callback",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallbackProcessResponse,
        )


class AsyncCallbackResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCallbackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AsyncCallbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallbackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AsyncCallbackResourceWithStreamingResponse(self)

    async def process(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallbackProcessResponse:
        """OAuth2 callback endpoint.

        Processes the authorization code from Auth0.

            **Query Parameters:**
            - `code`: Authorization code from Auth0 (required)
            - `state`: State parameter for CSRF protection (required)

            **Flow:**
            1. Auth0 redirects to this endpoint after successful authentication
            2. This endpoint validates the authorization code and state
            3. Redirects back to the original `redirect_uri` with code and state
            4. Client can then exchange the code for tokens at `/token` endpoint

            **Security:**
            - Validates state parameter to prevent CSRF attacks
            - Checks authorization code expiration
            - Cleans up session data after processing
        """
        return await self._get(
            "/callback",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallbackProcessResponse,
        )


class CallbackResourceWithRawResponse:
    def __init__(self, callback: CallbackResource) -> None:
        self._callback = callback

        self.process = to_raw_response_wrapper(
            callback.process,
        )


class AsyncCallbackResourceWithRawResponse:
    def __init__(self, callback: AsyncCallbackResource) -> None:
        self._callback = callback

        self.process = async_to_raw_response_wrapper(
            callback.process,
        )


class CallbackResourceWithStreamingResponse:
    def __init__(self, callback: CallbackResource) -> None:
        self._callback = callback

        self.process = to_streamed_response_wrapper(
            callback.process,
        )


class AsyncCallbackResourceWithStreamingResponse:
    def __init__(self, callback: AsyncCallbackResource) -> None:
        self._callback = callback

        self.process = async_to_streamed_response_wrapper(
            callback.process,
        )
