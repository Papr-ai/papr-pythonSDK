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
from ..types.frequency_list_response import FrequencyListResponse
from ..types.frequency_retrieve_response import FrequencyRetrieveResponse

__all__ = ["FrequenciesResource", "AsyncFrequenciesResource"]


class FrequenciesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FrequenciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return FrequenciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FrequenciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return FrequenciesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        frequency_schema_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FrequencyRetrieveResponse:
        """
        Retrieve a specific frequency schema by its full ID (e.g.
        'code_search:cosqa:2.0.0') or shorthand alias (e.g. 'cosqa').

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not frequency_schema_id:
            raise ValueError(
                f"Expected a non-empty value for `frequency_schema_id` but received {frequency_schema_id!r}"
            )
        return self._get(
            f"/v1/frequencies/{frequency_schema_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FrequencyRetrieveResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FrequencyListResponse:
        """
        Returns all built-in frequency schemas with their field definitions and
        operational configuration. Use the schema_id or a shorthand alias when adding or
        searching memories with holographic embedding enabled.
        """
        return self._get(
            "/v1/frequencies",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FrequencyListResponse,
        )


class AsyncFrequenciesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFrequenciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AsyncFrequenciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFrequenciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AsyncFrequenciesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        frequency_schema_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FrequencyRetrieveResponse:
        """
        Retrieve a specific frequency schema by its full ID (e.g.
        'code_search:cosqa:2.0.0') or shorthand alias (e.g. 'cosqa').

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not frequency_schema_id:
            raise ValueError(
                f"Expected a non-empty value for `frequency_schema_id` but received {frequency_schema_id!r}"
            )
        return await self._get(
            f"/v1/frequencies/{frequency_schema_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FrequencyRetrieveResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FrequencyListResponse:
        """
        Returns all built-in frequency schemas with their field definitions and
        operational configuration. Use the schema_id or a shorthand alias when adding or
        searching memories with holographic embedding enabled.
        """
        return await self._get(
            "/v1/frequencies",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FrequencyListResponse,
        )


class FrequenciesResourceWithRawResponse:
    def __init__(self, frequencies: FrequenciesResource) -> None:
        self._frequencies = frequencies

        self.retrieve = to_raw_response_wrapper(
            frequencies.retrieve,
        )
        self.list = to_raw_response_wrapper(
            frequencies.list,
        )


class AsyncFrequenciesResourceWithRawResponse:
    def __init__(self, frequencies: AsyncFrequenciesResource) -> None:
        self._frequencies = frequencies

        self.retrieve = async_to_raw_response_wrapper(
            frequencies.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            frequencies.list,
        )


class FrequenciesResourceWithStreamingResponse:
    def __init__(self, frequencies: FrequenciesResource) -> None:
        self._frequencies = frequencies

        self.retrieve = to_streamed_response_wrapper(
            frequencies.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            frequencies.list,
        )


class AsyncFrequenciesResourceWithStreamingResponse:
    def __init__(self, frequencies: AsyncFrequenciesResource) -> None:
        self._frequencies = frequencies

        self.retrieve = async_to_streamed_response_wrapper(
            frequencies.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            frequencies.list,
        )
