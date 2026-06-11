# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["AnthropicResource", "AsyncAnthropicResource"]


class AnthropicResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnthropicResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AnthropicResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnthropicResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AnthropicResourceWithStreamingResponse(self)

    def send_message(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Anthropic Messages API proxy (Claude models)"""
        return self._post(
            "/v1/ai/anthropic/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncAnthropicResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnthropicResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AsyncAnthropicResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnthropicResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AsyncAnthropicResourceWithStreamingResponse(self)

    async def send_message(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Anthropic Messages API proxy (Claude models)"""
        return await self._post(
            "/v1/ai/anthropic/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AnthropicResourceWithRawResponse:
    def __init__(self, anthropic: AnthropicResource) -> None:
        self._anthropic = anthropic

        self.send_message = to_raw_response_wrapper(
            anthropic.send_message,
        )


class AsyncAnthropicResourceWithRawResponse:
    def __init__(self, anthropic: AsyncAnthropicResource) -> None:
        self._anthropic = anthropic

        self.send_message = async_to_raw_response_wrapper(
            anthropic.send_message,
        )


class AnthropicResourceWithStreamingResponse:
    def __init__(self, anthropic: AnthropicResource) -> None:
        self._anthropic = anthropic

        self.send_message = to_streamed_response_wrapper(
            anthropic.send_message,
        )


class AsyncAnthropicResourceWithStreamingResponse:
    def __init__(self, anthropic: AsyncAnthropicResource) -> None:
        self._anthropic = anthropic

        self.send_message = async_to_streamed_response_wrapper(
            anthropic.send_message,
        )
