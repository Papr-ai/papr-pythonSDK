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
from ..types.login_initiate_response import LoginInitiateResponse

__all__ = ["LoginResource", "AsyncLoginResource"]


class LoginResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LoginResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return LoginResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoginResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return LoginResourceWithStreamingResponse(self)

    def initiate(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoginInitiateResponse:
        """OAuth2 login endpoint.

        Initiates the OAuth2 authorization code flow.

            **Query Parameters:**
            - `redirect_uri`: The URI to redirect to after authentication (required)
            - `state`: A random string for CSRF protection (optional but recommended)

            **Flow:**
            1. Client redirects user to this endpoint with `redirect_uri` and `state`
            2. This endpoint redirects user to Auth0 for authentication
            3. After authentication, Auth0 redirects to `/callback` with authorization code
            4. `/callback` redirects back to the original `redirect_uri` with code and state

            **Example:**
            ```
            GET /login?redirect_uri=https://chat.openai.com&state=abc123
            ```
        """
        return self._get(
            "/login",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoginInitiateResponse,
        )


class AsyncLoginResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLoginResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AsyncLoginResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoginResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AsyncLoginResourceWithStreamingResponse(self)

    async def initiate(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoginInitiateResponse:
        """OAuth2 login endpoint.

        Initiates the OAuth2 authorization code flow.

            **Query Parameters:**
            - `redirect_uri`: The URI to redirect to after authentication (required)
            - `state`: A random string for CSRF protection (optional but recommended)

            **Flow:**
            1. Client redirects user to this endpoint with `redirect_uri` and `state`
            2. This endpoint redirects user to Auth0 for authentication
            3. After authentication, Auth0 redirects to `/callback` with authorization code
            4. `/callback` redirects back to the original `redirect_uri` with code and state

            **Example:**
            ```
            GET /login?redirect_uri=https://chat.openai.com&state=abc123
            ```
        """
        return await self._get(
            "/login",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoginInitiateResponse,
        )


class LoginResourceWithRawResponse:
    def __init__(self, login: LoginResource) -> None:
        self._login = login

        self.initiate = to_raw_response_wrapper(
            login.initiate,
        )


class AsyncLoginResourceWithRawResponse:
    def __init__(self, login: AsyncLoginResource) -> None:
        self._login = login

        self.initiate = async_to_raw_response_wrapper(
            login.initiate,
        )


class LoginResourceWithStreamingResponse:
    def __init__(self, login: LoginResource) -> None:
        self._login = login

        self.initiate = to_streamed_response_wrapper(
            login.initiate,
        )


class AsyncLoginResourceWithStreamingResponse:
    def __init__(self, login: AsyncLoginResource) -> None:
        self._login = login

        self.initiate = async_to_streamed_response_wrapper(
            login.initiate,
        )
