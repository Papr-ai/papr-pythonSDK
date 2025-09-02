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
from ..types.me_retrieve_response import MeRetrieveResponse

__all__ = ["MeResource", "AsyncMeResource"]


class MeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return MeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return MeResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeRetrieveResponse:
        """Get current user information.

        Validates authentication and returns user details.

            **Authentication Required:**
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header: `Authorization: Bearer <access_token>`
            - Session token in `Authorization` header: `Authorization: Session <session_token>`
            - API Key in `Authorization` header: `Authorization: APIKey <api_key>`

            **Headers:**
            - `Authorization`: Authentication token (required)
            - `X-Client-Type`: Client type for logging (optional, default: papr_plugin)

            **Response:**
            - `user_id`: Internal user ID
            - `sessionToken`: Session token for API access (if available)
            - `imageUrl`: User profile image URL (if available)
            - `displayName`: User display name (if available)
            - `email`: User email address (if available)
            - `message`: Authentication status message

            **Example:**
            ```
            GET /me
            Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
            X-Client-Type: papr_plugin
            ```
        """
        return self._get(
            "/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeRetrieveResponse,
        )


class AsyncMeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AsyncMeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AsyncMeResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeRetrieveResponse:
        """Get current user information.

        Validates authentication and returns user details.

            **Authentication Required:**
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header: `Authorization: Bearer <access_token>`
            - Session token in `Authorization` header: `Authorization: Session <session_token>`
            - API Key in `Authorization` header: `Authorization: APIKey <api_key>`

            **Headers:**
            - `Authorization`: Authentication token (required)
            - `X-Client-Type`: Client type for logging (optional, default: papr_plugin)

            **Response:**
            - `user_id`: Internal user ID
            - `sessionToken`: Session token for API access (if available)
            - `imageUrl`: User profile image URL (if available)
            - `displayName`: User display name (if available)
            - `email`: User email address (if available)
            - `message`: Authentication status message

            **Example:**
            ```
            GET /me
            Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
            X-Client-Type: papr_plugin
            ```
        """
        return await self._get(
            "/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeRetrieveResponse,
        )


class MeResourceWithRawResponse:
    def __init__(self, me: MeResource) -> None:
        self._me = me

        self.retrieve = to_raw_response_wrapper(
            me.retrieve,
        )


class AsyncMeResourceWithRawResponse:
    def __init__(self, me: AsyncMeResource) -> None:
        self._me = me

        self.retrieve = async_to_raw_response_wrapper(
            me.retrieve,
        )


class MeResourceWithStreamingResponse:
    def __init__(self, me: MeResource) -> None:
        self._me = me

        self.retrieve = to_streamed_response_wrapper(
            me.retrieve,
        )


class AsyncMeResourceWithStreamingResponse:
    def __init__(self, me: AsyncMeResource) -> None:
        self._me = me

        self.retrieve = async_to_streamed_response_wrapper(
            me.retrieve,
        )
