# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal

import httpx

from ...types import graph_rerank_params, graph_transform_params
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from .domains.domains import (
    DomainsResource,
    AsyncDomainsResource,
    DomainsResourceWithRawResponse,
    AsyncDomainsResourceWithRawResponse,
    DomainsResourceWithStreamingResponse,
    AsyncDomainsResourceWithStreamingResponse,
)
from ...types.graph_rerank_response import GraphRerankResponse
from ...types.graph_transform_response import GraphTransformResponse

__all__ = ["GraphResource", "AsyncGraphResource"]


class GraphResource(SyncAPIResource):
    @cached_property
    def domains(self) -> DomainsResource:
        return DomainsResource(self._client)

    @cached_property
    def with_raw_response(self) -> GraphResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return GraphResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GraphResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return GraphResourceWithStreamingResponse(self)

    def rerank(
        self,
        *,
        documents: SequenceNotStr[graph_rerank_params.Document],
        query: graph_rerank_params.Query,
        domain_id: Optional[str] | Omit = omit,
        method: Literal["fast", "enhanced"] | Omit = omit,
        return_debug: bool | Omit = omit,
        return_documents: bool | Omit = omit,
        return_signal_scores: bool | Omit = omit,
        routing_config: Optional[graph_rerank_params.RoutingConfig] | Omit = omit,
        signal_embedder: Literal["sbert", "qwen"] | Omit = omit,
        signal_filters: Optional[Dict[str, float]] | Omit = omit,
        signal_multipliers: Optional[Dict[str, object]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GraphRerankResponse:
        """
        Rerank candidate documents against a query

        Args:
          documents: Candidate documents (string or DocumentInput with pre-computed artifacts).

          query: Query text (string) or QueryItem with pre-computed artifacts.

          domain_id: Domain shortname or full schema id controlling which frequency bands and
              extraction rules are used. Built-in shortnames: "general" (default), "code",
              "cosqa", "codetrans", "codetransocean", "codetransocean_hybrid", "text2sql",
              "scifact", "nfcorpus", "fiqa", "legal", "medical", "ecommerce", "coffee_shops".
              You can also pass a full schema id (e.g. "code_search:cosqa:2.0.0") or a custom
              domain_id registered via POST /v1/graph/domains.

          method: Public: enhanced or max (CE reranker). Accepts deprecated 'fast'/'enhanced'
              aliases.

          return_debug: If true, include CAESAR meta-signals + timing in `meta.debug`.

          return_documents: If true, echo back each input document in the result.

          return_signal_scores: If true, each result carries `signal_scores` (method-level scores like
              `base_sim`, `caesar8_score`) and `signal_scores_by_band` (per-frequency band
              alignments such as `key_apis`, `language`).

          routing_config: Domain-scoped CAESAR-VIII routing overrides (stored on graph_domains).

          signal_embedder: Embedder for per-band signal vectors when extracting query/docs. 'sbert' (384d,
              default) is ~10x cheaper to store than 'qwen' (2560d). Must match the embedder
              used for any BYO signal_embeddings.

          signal_filters: Hard cutoffs on per-frequency signals, e.g. {'domain_match': 0.6}. Docs below
              are dropped.

          signal_multipliers: Per-frequency scoring weight multipliers. Keys may be field names (e.g.
              'claim_stance', 'causal_verb') or Hz-strings (e.g. '19.0'). Values: 'auto'
              (default) or 1.0 = unchanged, 2.0 = 2x boost, 0.0 = disable that band. Fields
              not specified default to 'auto'. Stacks on top of the schema-level
              FrequencyField.weight multipliers; request-level overrides win on conflict.

          top_k: Return at most this many results. Defaults to len(documents).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/graph/rerank",
            body=maybe_transform(
                {
                    "documents": documents,
                    "query": query,
                    "domain_id": domain_id,
                    "method": method,
                    "return_debug": return_debug,
                    "return_documents": return_documents,
                    "return_signal_scores": return_signal_scores,
                    "routing_config": routing_config,
                    "signal_embedder": signal_embedder,
                    "signal_filters": signal_filters,
                    "signal_multipliers": signal_multipliers,
                    "top_k": top_k,
                },
                graph_rerank_params.GraphRerankParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GraphRerankResponse,
        )

    def transform(
        self,
        *,
        text: str,
        domain_id: Optional[str] | Omit = omit,
        embedding: Optional[Iterable[float]] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        return_concat: bool | Omit = omit,
        return_rot_v3: bool | Omit = omit,
        signal_embedder: Literal["sbert", "qwen"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GraphTransformResponse:
        """
        Vector-store agnostic producer.

        Returns everything you'd want to index in any vector DB -- base embedding,
        14-band extracted signals, per-band SBERT/Qwen embeddings, phases, and optional
        rot_v3 / concat reconstructions.

        Uses the SAME extraction + embedding path as /v1/graph/rerank uses for queries,
        so artifacts produced here can be scored by /v1/graph/rerank without any drift.

        Args:
          text: Source text to transform.

          domain_id: Domain shortname or full schema id controlling which frequency bands and
              extraction rules are used. Built-in shortnames: "general" (default), "code",
              "cosqa", "codetrans", "codetransocean", "codetransocean_hybrid", "text2sql",
              "scifact", "nfcorpus", "fiqa", "legal", "medical", "ecommerce", "coffee_shops".
              You can also pass a full schema id (e.g. "code_search:cosqa:2.0.0") or a custom
              domain_id registered via POST /v1/graph/domains.

          embedding: Optional caller-provided base embedding (Qwen 2560-d). If omitted, the server
              computes it.

          metadata: Free-form user metadata to attach (optional, not used for scoring).

          return_concat: If true, include the base + bands concatenation embedding.

          return_rot_v3: If true, include the rot_v3 vector in the response.

          signal_embedder: Embedder for per-band signal vectors. 'sbert' (384d, default) is ~10x cheaper to
              store than 'qwen' (2560d, matched to base).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/graph/transform",
            body=maybe_transform(
                {
                    "text": text,
                    "domain_id": domain_id,
                    "embedding": embedding,
                    "metadata": metadata,
                    "return_concat": return_concat,
                    "return_rot_v3": return_rot_v3,
                    "signal_embedder": signal_embedder,
                },
                graph_transform_params.GraphTransformParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GraphTransformResponse,
        )


class AsyncGraphResource(AsyncAPIResource):
    @cached_property
    def domains(self) -> AsyncDomainsResource:
        return AsyncDomainsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGraphResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AsyncGraphResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGraphResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AsyncGraphResourceWithStreamingResponse(self)

    async def rerank(
        self,
        *,
        documents: SequenceNotStr[graph_rerank_params.Document],
        query: graph_rerank_params.Query,
        domain_id: Optional[str] | Omit = omit,
        method: Literal["fast", "enhanced"] | Omit = omit,
        return_debug: bool | Omit = omit,
        return_documents: bool | Omit = omit,
        return_signal_scores: bool | Omit = omit,
        routing_config: Optional[graph_rerank_params.RoutingConfig] | Omit = omit,
        signal_embedder: Literal["sbert", "qwen"] | Omit = omit,
        signal_filters: Optional[Dict[str, float]] | Omit = omit,
        signal_multipliers: Optional[Dict[str, object]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GraphRerankResponse:
        """
        Rerank candidate documents against a query

        Args:
          documents: Candidate documents (string or DocumentInput with pre-computed artifacts).

          query: Query text (string) or QueryItem with pre-computed artifacts.

          domain_id: Domain shortname or full schema id controlling which frequency bands and
              extraction rules are used. Built-in shortnames: "general" (default), "code",
              "cosqa", "codetrans", "codetransocean", "codetransocean_hybrid", "text2sql",
              "scifact", "nfcorpus", "fiqa", "legal", "medical", "ecommerce", "coffee_shops".
              You can also pass a full schema id (e.g. "code_search:cosqa:2.0.0") or a custom
              domain_id registered via POST /v1/graph/domains.

          method: Public: enhanced or max (CE reranker). Accepts deprecated 'fast'/'enhanced'
              aliases.

          return_debug: If true, include CAESAR meta-signals + timing in `meta.debug`.

          return_documents: If true, echo back each input document in the result.

          return_signal_scores: If true, each result carries `signal_scores` (method-level scores like
              `base_sim`, `caesar8_score`) and `signal_scores_by_band` (per-frequency band
              alignments such as `key_apis`, `language`).

          routing_config: Domain-scoped CAESAR-VIII routing overrides (stored on graph_domains).

          signal_embedder: Embedder for per-band signal vectors when extracting query/docs. 'sbert' (384d,
              default) is ~10x cheaper to store than 'qwen' (2560d). Must match the embedder
              used for any BYO signal_embeddings.

          signal_filters: Hard cutoffs on per-frequency signals, e.g. {'domain_match': 0.6}. Docs below
              are dropped.

          signal_multipliers: Per-frequency scoring weight multipliers. Keys may be field names (e.g.
              'claim_stance', 'causal_verb') or Hz-strings (e.g. '19.0'). Values: 'auto'
              (default) or 1.0 = unchanged, 2.0 = 2x boost, 0.0 = disable that band. Fields
              not specified default to 'auto'. Stacks on top of the schema-level
              FrequencyField.weight multipliers; request-level overrides win on conflict.

          top_k: Return at most this many results. Defaults to len(documents).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/graph/rerank",
            body=await async_maybe_transform(
                {
                    "documents": documents,
                    "query": query,
                    "domain_id": domain_id,
                    "method": method,
                    "return_debug": return_debug,
                    "return_documents": return_documents,
                    "return_signal_scores": return_signal_scores,
                    "routing_config": routing_config,
                    "signal_embedder": signal_embedder,
                    "signal_filters": signal_filters,
                    "signal_multipliers": signal_multipliers,
                    "top_k": top_k,
                },
                graph_rerank_params.GraphRerankParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GraphRerankResponse,
        )

    async def transform(
        self,
        *,
        text: str,
        domain_id: Optional[str] | Omit = omit,
        embedding: Optional[Iterable[float]] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        return_concat: bool | Omit = omit,
        return_rot_v3: bool | Omit = omit,
        signal_embedder: Literal["sbert", "qwen"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GraphTransformResponse:
        """
        Vector-store agnostic producer.

        Returns everything you'd want to index in any vector DB -- base embedding,
        14-band extracted signals, per-band SBERT/Qwen embeddings, phases, and optional
        rot_v3 / concat reconstructions.

        Uses the SAME extraction + embedding path as /v1/graph/rerank uses for queries,
        so artifacts produced here can be scored by /v1/graph/rerank without any drift.

        Args:
          text: Source text to transform.

          domain_id: Domain shortname or full schema id controlling which frequency bands and
              extraction rules are used. Built-in shortnames: "general" (default), "code",
              "cosqa", "codetrans", "codetransocean", "codetransocean_hybrid", "text2sql",
              "scifact", "nfcorpus", "fiqa", "legal", "medical", "ecommerce", "coffee_shops".
              You can also pass a full schema id (e.g. "code_search:cosqa:2.0.0") or a custom
              domain_id registered via POST /v1/graph/domains.

          embedding: Optional caller-provided base embedding (Qwen 2560-d). If omitted, the server
              computes it.

          metadata: Free-form user metadata to attach (optional, not used for scoring).

          return_concat: If true, include the base + bands concatenation embedding.

          return_rot_v3: If true, include the rot_v3 vector in the response.

          signal_embedder: Embedder for per-band signal vectors. 'sbert' (384d, default) is ~10x cheaper to
              store than 'qwen' (2560d, matched to base).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/graph/transform",
            body=await async_maybe_transform(
                {
                    "text": text,
                    "domain_id": domain_id,
                    "embedding": embedding,
                    "metadata": metadata,
                    "return_concat": return_concat,
                    "return_rot_v3": return_rot_v3,
                    "signal_embedder": signal_embedder,
                },
                graph_transform_params.GraphTransformParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GraphTransformResponse,
        )


class GraphResourceWithRawResponse:
    def __init__(self, graph: GraphResource) -> None:
        self._graph = graph

        self.rerank = to_raw_response_wrapper(
            graph.rerank,
        )
        self.transform = to_raw_response_wrapper(
            graph.transform,
        )

    @cached_property
    def domains(self) -> DomainsResourceWithRawResponse:
        return DomainsResourceWithRawResponse(self._graph.domains)


class AsyncGraphResourceWithRawResponse:
    def __init__(self, graph: AsyncGraphResource) -> None:
        self._graph = graph

        self.rerank = async_to_raw_response_wrapper(
            graph.rerank,
        )
        self.transform = async_to_raw_response_wrapper(
            graph.transform,
        )

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithRawResponse:
        return AsyncDomainsResourceWithRawResponse(self._graph.domains)


class GraphResourceWithStreamingResponse:
    def __init__(self, graph: GraphResource) -> None:
        self._graph = graph

        self.rerank = to_streamed_response_wrapper(
            graph.rerank,
        )
        self.transform = to_streamed_response_wrapper(
            graph.transform,
        )

    @cached_property
    def domains(self) -> DomainsResourceWithStreamingResponse:
        return DomainsResourceWithStreamingResponse(self._graph.domains)


class AsyncGraphResourceWithStreamingResponse:
    def __init__(self, graph: AsyncGraphResource) -> None:
        self._graph = graph

        self.rerank = async_to_streamed_response_wrapper(
            graph.rerank,
        )
        self.transform = async_to_streamed_response_wrapper(
            graph.transform,
        )

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithStreamingResponse:
        return AsyncDomainsResourceWithStreamingResponse(self._graph.domains)
