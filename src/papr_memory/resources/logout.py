# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.logout_perform_response import LogoutPerformResponse

__all__ = ["LogoutResource", "AsyncLogoutResource"]


class LogoutResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LogoutResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return LogoutResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogoutResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return LogoutResourceWithStreamingResponse(self)

    def perform(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogoutPerformResponse:
        """OAuth2 logout endpoint.

        Logs out the user from Auth0 and redirects to specified
        URL.

            **Query Parameters:**
            - `returnTo`: URL to redirect to after logout (optional, default: extension logout page)
            - `client_type`: Client type for determining Auth0 client ID (optional, default: papr_plugin)

            **Flow:**
            1. Client redirects user to this endpoint
            2. This endpoint redirects to Auth0 logout URL
            3. Auth0 logs out the user and redirects to the specified return URL

            **Example:**
            ```
            GET /logout?returnTo=https://chat.openai.com
            ```

            **Note:** This endpoint initiates the logout process. The actual logout completion happens on Auth0's side.
        """
        return self._get(
            "/logout",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogoutPerformResponse,
        )


class AsyncLogoutResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLogoutResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AsyncLogoutResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogoutResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AsyncLogoutResourceWithStreamingResponse(self)

    async def perform(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogoutPerformResponse:
        """OAuth2 logout endpoint.

        Logs out the user from Auth0 and redirects to specified
        URL.

            **Query Parameters:**
            - `returnTo`: URL to redirect to after logout (optional, default: extension logout page)
            - `client_type`: Client type for determining Auth0 client ID (optional, default: papr_plugin)

            **Flow:**
            1. Client redirects user to this endpoint
            2. This endpoint redirects to Auth0 logout URL
            3. Auth0 logs out the user and redirects to the specified return URL

            **Example:**
            ```
            GET /logout?returnTo=https://chat.openai.com
            ```

            **Note:** This endpoint initiates the logout process. The actual logout completion happens on Auth0's side.
        """
        return await self._get(
            "/logout",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogoutPerformResponse,
        )


class LogoutResourceWithRawResponse:
    def __init__(self, logout: LogoutResource) -> None:
        self._logout = logout

        self.perform = to_raw_response_wrapper(
            logout.perform,
        )


class AsyncLogoutResourceWithRawResponse:
    def __init__(self, logout: AsyncLogoutResource) -> None:
        self._logout = logout

        self.perform = async_to_raw_response_wrapper(
            logout.perform,
        )


class LogoutResourceWithStreamingResponse:
    def __init__(self, logout: LogoutResource) -> None:
        self._logout = logout

        self.perform = to_streamed_response_wrapper(
            logout.perform,
        )


class AsyncLogoutResourceWithStreamingResponse:
    def __init__(self, logout: AsyncLogoutResource) -> None:
        self._logout = logout

        self.perform = async_to_streamed_response_wrapper(
            logout.perform,
        )
