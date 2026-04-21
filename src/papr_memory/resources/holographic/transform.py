# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal

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
from ...types.holographic import transform_create_params, transform_create_batch_params
from ...types.holographic.transform_create_response import TransformCreateResponse
from ...types.holographic.transform_create_batch_response import TransformCreateBatchResponse

__all__ = ["TransformResource", "AsyncTransformResource"]


class TransformResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TransformResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return TransformResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransformResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return TransformResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        content: str,
        embedding: Iterable[float],
        context_metadata: Optional[Dict[str, object]] | Omit = omit,
        domain: Optional[str] | Omit = omit,
        frequency_schema_id: Optional[str] | Omit = omit,
        output: Optional[
            List[
                Literal[
                    "base",
                    "rotation_v1",
                    "rotation_v2",
                    "rotation_v3",
                    "concat",
                    "phases",
                    "metadata",
                    "metadata_embeddings",
                ]
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransformCreateResponse:
        """Core BYOE endpoint.

        Send text content and your base embedding (any dimensions)
        to get back holographic-transformed embeddings. Use `output` to control which
        fields are returned. Default: rotation_v3 + metadata.

        Args:
          content: Text content for LLM metadata extraction

          embedding: Base embedding vector (any dimensionality)

          context_metadata: Optional context metadata (createdAt, sourceType, customMetadata, etc.) to
              improve LLM extraction accuracy, especially for dates and entities.

          domain: Domain for frequency schema selection (e.g. 'biomedical', 'code', 'general')

          frequency_schema_id: Specific frequency schema ID override (e.g. 'biomedical:scifact:2.0.0'). Takes
              precedence over domain.

          output: Which output fields to return. Default: ['rotation_v3', 'metadata']. Request
              only what you need to minimize response size.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/holographic/transform",
            body=maybe_transform(
                {
                    "content": content,
                    "embedding": embedding,
                    "context_metadata": context_metadata,
                    "domain": domain,
                    "frequency_schema_id": frequency_schema_id,
                    "output": output,
                },
                transform_create_params.TransformCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransformCreateResponse,
        )

    def create_batch(
        self,
        *,
        items: Iterable[transform_create_batch_params.Item],
        domain: Optional[str] | Omit = omit,
        frequency_schema_id: Optional[str] | Omit = omit,
        output: Optional[
            List[
                Literal[
                    "base",
                    "rotation_v1",
                    "rotation_v2",
                    "rotation_v3",
                    "concat",
                    "phases",
                    "metadata",
                    "metadata_embeddings",
                ]
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransformCreateBatchResponse:
        """Transform up to 50 items in a single request.

        Same as /transform but batched.

        Args:
          items: Items to transform (max 50)

          domain: Domain for all items

          frequency_schema_id: Schema override for all items

          output: Which output fields to return for each item

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/holographic/transform/batch",
            body=maybe_transform(
                {
                    "items": items,
                    "domain": domain,
                    "frequency_schema_id": frequency_schema_id,
                    "output": output,
                },
                transform_create_batch_params.TransformCreateBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransformCreateBatchResponse,
        )


class AsyncTransformResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTransformResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AsyncTransformResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransformResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AsyncTransformResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        content: str,
        embedding: Iterable[float],
        context_metadata: Optional[Dict[str, object]] | Omit = omit,
        domain: Optional[str] | Omit = omit,
        frequency_schema_id: Optional[str] | Omit = omit,
        output: Optional[
            List[
                Literal[
                    "base",
                    "rotation_v1",
                    "rotation_v2",
                    "rotation_v3",
                    "concat",
                    "phases",
                    "metadata",
                    "metadata_embeddings",
                ]
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransformCreateResponse:
        """Core BYOE endpoint.

        Send text content and your base embedding (any dimensions)
        to get back holographic-transformed embeddings. Use `output` to control which
        fields are returned. Default: rotation_v3 + metadata.

        Args:
          content: Text content for LLM metadata extraction

          embedding: Base embedding vector (any dimensionality)

          context_metadata: Optional context metadata (createdAt, sourceType, customMetadata, etc.) to
              improve LLM extraction accuracy, especially for dates and entities.

          domain: Domain for frequency schema selection (e.g. 'biomedical', 'code', 'general')

          frequency_schema_id: Specific frequency schema ID override (e.g. 'biomedical:scifact:2.0.0'). Takes
              precedence over domain.

          output: Which output fields to return. Default: ['rotation_v3', 'metadata']. Request
              only what you need to minimize response size.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/holographic/transform",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "embedding": embedding,
                    "context_metadata": context_metadata,
                    "domain": domain,
                    "frequency_schema_id": frequency_schema_id,
                    "output": output,
                },
                transform_create_params.TransformCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransformCreateResponse,
        )

    async def create_batch(
        self,
        *,
        items: Iterable[transform_create_batch_params.Item],
        domain: Optional[str] | Omit = omit,
        frequency_schema_id: Optional[str] | Omit = omit,
        output: Optional[
            List[
                Literal[
                    "base",
                    "rotation_v1",
                    "rotation_v2",
                    "rotation_v3",
                    "concat",
                    "phases",
                    "metadata",
                    "metadata_embeddings",
                ]
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransformCreateBatchResponse:
        """Transform up to 50 items in a single request.

        Same as /transform but batched.

        Args:
          items: Items to transform (max 50)

          domain: Domain for all items

          frequency_schema_id: Schema override for all items

          output: Which output fields to return for each item

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/holographic/transform/batch",
            body=await async_maybe_transform(
                {
                    "items": items,
                    "domain": domain,
                    "frequency_schema_id": frequency_schema_id,
                    "output": output,
                },
                transform_create_batch_params.TransformCreateBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransformCreateBatchResponse,
        )


class TransformResourceWithRawResponse:
    def __init__(self, transform: TransformResource) -> None:
        self._transform = transform

        self.create = to_raw_response_wrapper(
            transform.create,
        )
        self.create_batch = to_raw_response_wrapper(
            transform.create_batch,
        )


class AsyncTransformResourceWithRawResponse:
    def __init__(self, transform: AsyncTransformResource) -> None:
        self._transform = transform

        self.create = async_to_raw_response_wrapper(
            transform.create,
        )
        self.create_batch = async_to_raw_response_wrapper(
            transform.create_batch,
        )


class TransformResourceWithStreamingResponse:
    def __init__(self, transform: TransformResource) -> None:
        self._transform = transform

        self.create = to_streamed_response_wrapper(
            transform.create,
        )
        self.create_batch = to_streamed_response_wrapper(
            transform.create_batch,
        )


class AsyncTransformResourceWithStreamingResponse:
    def __init__(self, transform: AsyncTransformResource) -> None:
        self._transform = transform

        self.create = async_to_streamed_response_wrapper(
            transform.create,
        )
        self.create_batch = async_to_streamed_response_wrapper(
            transform.create_batch,
        )
