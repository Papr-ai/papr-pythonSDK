# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Dict, Iterable, Optional

import httpx

from ...types import holographic_rerank_params, holographic_extract_metadata_params
from .domains import (
    DomainsResource,
    AsyncDomainsResource,
    DomainsResourceWithRawResponse,
    AsyncDomainsResourceWithRawResponse,
    DomainsResourceWithStreamingResponse,
    AsyncDomainsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .transform import (
    TransformResource,
    AsyncTransformResource,
    TransformResourceWithRawResponse,
    AsyncTransformResourceWithRawResponse,
    TransformResourceWithStreamingResponse,
    AsyncTransformResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.holographic_rerank_response import HolographicRerankResponse
from ...types.holographic_extract_metadata_response import HolographicExtractMetadataResponse

__all__ = ["HolographicResource", "AsyncHolographicResource"]


class HolographicResource(SyncAPIResource):
    @cached_property
    def transform(self) -> TransformResource:
        return TransformResource(self._client)

    @cached_property
    def domains(self) -> DomainsResource:
        return DomainsResource(self._client)

    @cached_property
    def with_raw_response(self) -> HolographicResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return HolographicResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HolographicResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return HolographicResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def extract_metadata(
        self,
        *,
        content: str,
        concat_embedding: Optional[Iterable[float]] | Omit = omit,
        context_metadata: Optional[Dict[str, object]] | Omit = omit,
        domain: Optional[str] | Omit = omit,
        frequency_schema_id: Optional[str] | Omit = omit,
        rotation_embedding: Optional[Iterable[float]] | Omit = omit,
        rotation_v2_embedding: Optional[Iterable[float]] | Omit = omit,
        rotation_v3_embedding: Optional[Iterable[float]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HolographicExtractMetadataResponse:
        """
        Extracts frequency metadata from text content without requiring an embedding.
        Returns metadata + phases that can be used with the on-device SDK for local
        transforms. Call this once per document at index time, then use phases locally
        for scoring.

        Args:
          content: Text content for metadata extraction

          concat_embedding: Pre-computed concat (new) embedding from holographic transform.

          context_metadata: Optional context metadata (createdAt, sourceType, etc.) to improve extraction.

          domain: Domain for frequency schema

          frequency_schema_id: Schema override

          rotation_embedding: Pre-computed rotation (old) embedding from holographic transform. Enables
              rot_v2/v3 similarity scoring and full CAESAR ensemble.

          rotation_v2_embedding: Pre-computed rotation V2 embedding from holographic transform.

          rotation_v3_embedding: Pre-computed rotation V3 embedding from holographic transform.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/holographic/metadata",
            body=maybe_transform(
                {
                    "content": content,
                    "concat_embedding": concat_embedding,
                    "context_metadata": context_metadata,
                    "domain": domain,
                    "frequency_schema_id": frequency_schema_id,
                    "rotation_embedding": rotation_embedding,
                    "rotation_v2_embedding": rotation_v2_embedding,
                    "rotation_v3_embedding": rotation_v3_embedding,
                },
                holographic_extract_metadata_params.HolographicExtractMetadataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HolographicExtractMetadataResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def rerank(
        self,
        *,
        candidates: Iterable[holographic_rerank_params.Candidate],
        query: str,
        domain: Optional[str] | Omit = omit,
        frequency_schema_id: Optional[str] | Omit = omit,
        options: Optional[holographic_rerank_params.Options] | Omit = omit,
        query_dimension_weights: Optional[Dict[str, float]] | Omit = omit,
        query_embedding: Optional[Iterable[float]] | Omit = omit,
        query_metadata_embeddings: Optional[Dict[str, Iterable[float]]] | Omit = omit,
        query_phases: Optional[Iterable[float]] | Omit = omit,
        top_k: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HolographicRerankResponse:
        """The simplest entry point — zero infrastructure needed.

        Send your search query
        and candidate results, get back better-ranked results using CAESAR ensemble.

        **Auto-detection:** candidates with `phases` use the fast path (~2-5ms each).
        Candidates with only `content` use the cold path (~100ms each, includes LLM
        extraction). You can mix both in a single request.

        Args:
          candidates: Candidate documents to rerank (max 100)

          query: The search query text

          domain: Domain for frequency schema

          frequency_schema_id: Schema override

          options: Options for the rerank endpoint.

          query_dimension_weights: Pre-computed per-field weights from a prior /transform call (is_query=true). If
              provided, skips the adaptive Groq weights call entirely (saves ~500ms + LLM
              cost). Keyed by frequency string (e.g. '0.1') OR field name (e.g.
              'mega_domain').

          query_embedding: Query embedding in the same space as candidate embeddings. If provided, used for
              cosine similarity. If omitted, computed server-side (Qwen 2560d).

          query_metadata_embeddings: Pre-computed query metadata embeddings from a prior /transform call (keyed by
              frequency string, e.g. '0.1'). Required for full HCond scoring with phase
              alignment.

          query_phases: Pre-computed query phases from a prior /transform call. If provided alongside
              query_embedding, skips LLM extraction entirely (hot path).

          top_k: Number of results to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/holographic/rerank",
            body=maybe_transform(
                {
                    "candidates": candidates,
                    "query": query,
                    "domain": domain,
                    "frequency_schema_id": frequency_schema_id,
                    "options": options,
                    "query_dimension_weights": query_dimension_weights,
                    "query_embedding": query_embedding,
                    "query_metadata_embeddings": query_metadata_embeddings,
                    "query_phases": query_phases,
                    "top_k": top_k,
                },
                holographic_rerank_params.HolographicRerankParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HolographicRerankResponse,
        )


class AsyncHolographicResource(AsyncAPIResource):
    @cached_property
    def transform(self) -> AsyncTransformResource:
        return AsyncTransformResource(self._client)

    @cached_property
    def domains(self) -> AsyncDomainsResource:
        return AsyncDomainsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHolographicResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AsyncHolographicResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHolographicResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AsyncHolographicResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    async def extract_metadata(
        self,
        *,
        content: str,
        concat_embedding: Optional[Iterable[float]] | Omit = omit,
        context_metadata: Optional[Dict[str, object]] | Omit = omit,
        domain: Optional[str] | Omit = omit,
        frequency_schema_id: Optional[str] | Omit = omit,
        rotation_embedding: Optional[Iterable[float]] | Omit = omit,
        rotation_v2_embedding: Optional[Iterable[float]] | Omit = omit,
        rotation_v3_embedding: Optional[Iterable[float]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HolographicExtractMetadataResponse:
        """
        Extracts frequency metadata from text content without requiring an embedding.
        Returns metadata + phases that can be used with the on-device SDK for local
        transforms. Call this once per document at index time, then use phases locally
        for scoring.

        Args:
          content: Text content for metadata extraction

          concat_embedding: Pre-computed concat (new) embedding from holographic transform.

          context_metadata: Optional context metadata (createdAt, sourceType, etc.) to improve extraction.

          domain: Domain for frequency schema

          frequency_schema_id: Schema override

          rotation_embedding: Pre-computed rotation (old) embedding from holographic transform. Enables
              rot_v2/v3 similarity scoring and full CAESAR ensemble.

          rotation_v2_embedding: Pre-computed rotation V2 embedding from holographic transform.

          rotation_v3_embedding: Pre-computed rotation V3 embedding from holographic transform.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/holographic/metadata",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "concat_embedding": concat_embedding,
                    "context_metadata": context_metadata,
                    "domain": domain,
                    "frequency_schema_id": frequency_schema_id,
                    "rotation_embedding": rotation_embedding,
                    "rotation_v2_embedding": rotation_v2_embedding,
                    "rotation_v3_embedding": rotation_v3_embedding,
                },
                holographic_extract_metadata_params.HolographicExtractMetadataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HolographicExtractMetadataResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def rerank(
        self,
        *,
        candidates: Iterable[holographic_rerank_params.Candidate],
        query: str,
        domain: Optional[str] | Omit = omit,
        frequency_schema_id: Optional[str] | Omit = omit,
        options: Optional[holographic_rerank_params.Options] | Omit = omit,
        query_dimension_weights: Optional[Dict[str, float]] | Omit = omit,
        query_embedding: Optional[Iterable[float]] | Omit = omit,
        query_metadata_embeddings: Optional[Dict[str, Iterable[float]]] | Omit = omit,
        query_phases: Optional[Iterable[float]] | Omit = omit,
        top_k: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HolographicRerankResponse:
        """The simplest entry point — zero infrastructure needed.

        Send your search query
        and candidate results, get back better-ranked results using CAESAR ensemble.

        **Auto-detection:** candidates with `phases` use the fast path (~2-5ms each).
        Candidates with only `content` use the cold path (~100ms each, includes LLM
        extraction). You can mix both in a single request.

        Args:
          candidates: Candidate documents to rerank (max 100)

          query: The search query text

          domain: Domain for frequency schema

          frequency_schema_id: Schema override

          options: Options for the rerank endpoint.

          query_dimension_weights: Pre-computed per-field weights from a prior /transform call (is_query=true). If
              provided, skips the adaptive Groq weights call entirely (saves ~500ms + LLM
              cost). Keyed by frequency string (e.g. '0.1') OR field name (e.g.
              'mega_domain').

          query_embedding: Query embedding in the same space as candidate embeddings. If provided, used for
              cosine similarity. If omitted, computed server-side (Qwen 2560d).

          query_metadata_embeddings: Pre-computed query metadata embeddings from a prior /transform call (keyed by
              frequency string, e.g. '0.1'). Required for full HCond scoring with phase
              alignment.

          query_phases: Pre-computed query phases from a prior /transform call. If provided alongside
              query_embedding, skips LLM extraction entirely (hot path).

          top_k: Number of results to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/holographic/rerank",
            body=await async_maybe_transform(
                {
                    "candidates": candidates,
                    "query": query,
                    "domain": domain,
                    "frequency_schema_id": frequency_schema_id,
                    "options": options,
                    "query_dimension_weights": query_dimension_weights,
                    "query_embedding": query_embedding,
                    "query_metadata_embeddings": query_metadata_embeddings,
                    "query_phases": query_phases,
                    "top_k": top_k,
                },
                holographic_rerank_params.HolographicRerankParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HolographicRerankResponse,
        )


class HolographicResourceWithRawResponse:
    def __init__(self, holographic: HolographicResource) -> None:
        self._holographic = holographic

        self.extract_metadata = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                holographic.extract_metadata,  # pyright: ignore[reportDeprecated],
            )
        )
        self.rerank = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                holographic.rerank,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def transform(self) -> TransformResourceWithRawResponse:
        return TransformResourceWithRawResponse(self._holographic.transform)

    @cached_property
    def domains(self) -> DomainsResourceWithRawResponse:
        return DomainsResourceWithRawResponse(self._holographic.domains)


class AsyncHolographicResourceWithRawResponse:
    def __init__(self, holographic: AsyncHolographicResource) -> None:
        self._holographic = holographic

        self.extract_metadata = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                holographic.extract_metadata,  # pyright: ignore[reportDeprecated],
            )
        )
        self.rerank = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                holographic.rerank,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def transform(self) -> AsyncTransformResourceWithRawResponse:
        return AsyncTransformResourceWithRawResponse(self._holographic.transform)

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithRawResponse:
        return AsyncDomainsResourceWithRawResponse(self._holographic.domains)


class HolographicResourceWithStreamingResponse:
    def __init__(self, holographic: HolographicResource) -> None:
        self._holographic = holographic

        self.extract_metadata = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                holographic.extract_metadata,  # pyright: ignore[reportDeprecated],
            )
        )
        self.rerank = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                holographic.rerank,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def transform(self) -> TransformResourceWithStreamingResponse:
        return TransformResourceWithStreamingResponse(self._holographic.transform)

    @cached_property
    def domains(self) -> DomainsResourceWithStreamingResponse:
        return DomainsResourceWithStreamingResponse(self._holographic.domains)


class AsyncHolographicResourceWithStreamingResponse:
    def __init__(self, holographic: AsyncHolographicResource) -> None:
        self._holographic = holographic

        self.extract_metadata = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                holographic.extract_metadata,  # pyright: ignore[reportDeprecated],
            )
        )
        self.rerank = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                holographic.rerank,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def transform(self) -> AsyncTransformResourceWithStreamingResponse:
        return AsyncTransformResourceWithStreamingResponse(self._holographic.transform)

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithStreamingResponse:
        return AsyncDomainsResourceWithStreamingResponse(self._holographic.domains)
