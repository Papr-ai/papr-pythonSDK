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
from ..types.token_create_response import TokenCreateResponse

__all__ = ["TokenResource", "AsyncTokenResource"]


class TokenResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TokenResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return TokenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TokenResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return TokenResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenCreateResponse:
        """OAuth2 token endpoint.

        Exchanges authorization code for access tokens.

            **Request Body (JSON or Form):**
            - `grant_type`: OAuth2 grant type - "authorization_code" or "refresh_token" (required)
            - `code`: Authorization code from OAuth2 callback (required for authorization_code grant)
            - `redirect_uri`: Redirect URI used in authorization (required for authorization_code grant)
            - `client_type`: Client type - "papr_plugin" or "browser_extension" (optional, default: papr_plugin)
            - `refresh_token`: Refresh token for token refresh (required for refresh_token grant)

            **Response:**
            - `access_token`: OAuth2 access token for API authentication
            - `token_type`: Token type (Bearer)
            - `expires_in`: Token expiration time in seconds
            - `refresh_token`: Refresh token for getting new access tokens
            - `scope`: OAuth2 scopes granted
            - `user_id`: User ID from Auth0

            **Example Request:**
            ```json
            {
                "grant_type": "authorization_code",
                "code": "abc123...",
                "redirect_uri": "https://chat.openai.com",
                "client_type": "papr_plugin"
            }
            ```
        """
        return self._post(
            "/token",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenCreateResponse,
        )


class AsyncTokenResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTokenResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AsyncTokenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTokenResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AsyncTokenResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenCreateResponse:
        """OAuth2 token endpoint.

        Exchanges authorization code for access tokens.

            **Request Body (JSON or Form):**
            - `grant_type`: OAuth2 grant type - "authorization_code" or "refresh_token" (required)
            - `code`: Authorization code from OAuth2 callback (required for authorization_code grant)
            - `redirect_uri`: Redirect URI used in authorization (required for authorization_code grant)
            - `client_type`: Client type - "papr_plugin" or "browser_extension" (optional, default: papr_plugin)
            - `refresh_token`: Refresh token for token refresh (required for refresh_token grant)

            **Response:**
            - `access_token`: OAuth2 access token for API authentication
            - `token_type`: Token type (Bearer)
            - `expires_in`: Token expiration time in seconds
            - `refresh_token`: Refresh token for getting new access tokens
            - `scope`: OAuth2 scopes granted
            - `user_id`: User ID from Auth0

            **Example Request:**
            ```json
            {
                "grant_type": "authorization_code",
                "code": "abc123...",
                "redirect_uri": "https://chat.openai.com",
                "client_type": "papr_plugin"
            }
            ```
        """
        return await self._post(
            "/token",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenCreateResponse,
        )


class TokenResourceWithRawResponse:
    def __init__(self, token: TokenResource) -> None:
        self._token = token

        self.create = to_raw_response_wrapper(
            token.create,
        )


class AsyncTokenResourceWithRawResponse:
    def __init__(self, token: AsyncTokenResource) -> None:
        self._token = token

        self.create = async_to_raw_response_wrapper(
            token.create,
        )


class TokenResourceWithStreamingResponse:
    def __init__(self, token: TokenResource) -> None:
        self._token = token

        self.create = to_streamed_response_wrapper(
            token.create,
        )


class AsyncTokenResourceWithStreamingResponse:
    def __init__(self, token: AsyncTokenResource) -> None:
        self._token = token

        self.create = async_to_streamed_response_wrapper(
            token.create,
        )
