# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from .anthropic import (
    AnthropicResource,
    AsyncAnthropicResource,
    AnthropicResourceWithRawResponse,
    AsyncAnthropicResourceWithRawResponse,
    AnthropicResourceWithStreamingResponse,
    AsyncAnthropicResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .google.google import (
    GoogleResource,
    AsyncGoogleResource,
    GoogleResourceWithRawResponse,
    AsyncGoogleResourceWithRawResponse,
    GoogleResourceWithStreamingResponse,
    AsyncGoogleResourceWithStreamingResponse,
)
from .openai.openai import (
    OpenAIResource,
    AsyncOpenAIResource,
    OpenAIResourceWithRawResponse,
    AsyncOpenAIResourceWithRawResponse,
    OpenAIResourceWithStreamingResponse,
    AsyncOpenAIResourceWithStreamingResponse,
)
from ..._base_client import make_request_options

__all__ = ["AIResource", "AsyncAIResource"]


class AIResource(SyncAPIResource):
    @cached_property
    def openai(self) -> OpenAIResource:
        return OpenAIResource(self._client)

    @cached_property
    def anthropic(self) -> AnthropicResource:
        return AnthropicResource(self._client)

    @cached_property
    def google(self) -> GoogleResource:
        return GoogleResource(self._client)

    @cached_property
    def with_raw_response(self) -> AIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AIResourceWithStreamingResponse(self)

    def get_usage(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Get user's AI proxy usage stats and subscription info."""
        return self._get(
            "/v1/ai/usage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncAIResource(AsyncAPIResource):
    @cached_property
    def openai(self) -> AsyncOpenAIResource:
        return AsyncOpenAIResource(self._client)

    @cached_property
    def anthropic(self) -> AsyncAnthropicResource:
        return AsyncAnthropicResource(self._client)

    @cached_property
    def google(self) -> AsyncGoogleResource:
        return AsyncGoogleResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AsyncAIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AsyncAIResourceWithStreamingResponse(self)

    async def get_usage(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Get user's AI proxy usage stats and subscription info."""
        return await self._get(
            "/v1/ai/usage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AIResourceWithRawResponse:
    def __init__(self, ai: AIResource) -> None:
        self._ai = ai

        self.get_usage = to_raw_response_wrapper(
            ai.get_usage,
        )

    @cached_property
    def openai(self) -> OpenAIResourceWithRawResponse:
        return OpenAIResourceWithRawResponse(self._ai.openai)

    @cached_property
    def anthropic(self) -> AnthropicResourceWithRawResponse:
        return AnthropicResourceWithRawResponse(self._ai.anthropic)

    @cached_property
    def google(self) -> GoogleResourceWithRawResponse:
        return GoogleResourceWithRawResponse(self._ai.google)


class AsyncAIResourceWithRawResponse:
    def __init__(self, ai: AsyncAIResource) -> None:
        self._ai = ai

        self.get_usage = async_to_raw_response_wrapper(
            ai.get_usage,
        )

    @cached_property
    def openai(self) -> AsyncOpenAIResourceWithRawResponse:
        return AsyncOpenAIResourceWithRawResponse(self._ai.openai)

    @cached_property
    def anthropic(self) -> AsyncAnthropicResourceWithRawResponse:
        return AsyncAnthropicResourceWithRawResponse(self._ai.anthropic)

    @cached_property
    def google(self) -> AsyncGoogleResourceWithRawResponse:
        return AsyncGoogleResourceWithRawResponse(self._ai.google)


class AIResourceWithStreamingResponse:
    def __init__(self, ai: AIResource) -> None:
        self._ai = ai

        self.get_usage = to_streamed_response_wrapper(
            ai.get_usage,
        )

    @cached_property
    def openai(self) -> OpenAIResourceWithStreamingResponse:
        return OpenAIResourceWithStreamingResponse(self._ai.openai)

    @cached_property
    def anthropic(self) -> AnthropicResourceWithStreamingResponse:
        return AnthropicResourceWithStreamingResponse(self._ai.anthropic)

    @cached_property
    def google(self) -> GoogleResourceWithStreamingResponse:
        return GoogleResourceWithStreamingResponse(self._ai.google)


class AsyncAIResourceWithStreamingResponse:
    def __init__(self, ai: AsyncAIResource) -> None:
        self._ai = ai

        self.get_usage = async_to_streamed_response_wrapper(
            ai.get_usage,
        )

    @cached_property
    def openai(self) -> AsyncOpenAIResourceWithStreamingResponse:
        return AsyncOpenAIResourceWithStreamingResponse(self._ai.openai)

    @cached_property
    def anthropic(self) -> AsyncAnthropicResourceWithStreamingResponse:
        return AsyncAnthropicResourceWithStreamingResponse(self._ai.anthropic)

    @cached_property
    def google(self) -> AsyncGoogleResourceWithStreamingResponse:
        return AsyncGoogleResourceWithStreamingResponse(self._ai.google)
