# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.graph.domains.catalog_refresh_response import CatalogRefreshResponse
from ....types.graph.domains.catalog_retrieve_response import CatalogRetrieveResponse

__all__ = ["CatalogResource", "AsyncCatalogResource"]


class CatalogResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CatalogResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return CatalogResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CatalogResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return CatalogResourceWithStreamingResponse(self)

    def retrieve(
        self,
        domain_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CatalogRetrieveResponse:
        """
        Return the LLM-curated catalog showing what signal values exist in this domain.

        The catalog is built incrementally from transform calls. It contains:

        - entity_clusters: semantically-grouped entity values
        - relationship_patterns: clustered relationship types
        - signal_value_counts: raw per-band value frequencies
        - domain_distribution: per-band document counts
        - total_documents: total transforms processed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return self._get(
            path_template("/v1/graph/domains/{domain_id}/catalog", domain_id=domain_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CatalogRetrieveResponse,
        )

    def refresh(
        self,
        domain_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CatalogRefreshResponse:
        """
        Process any buffered signal values through LLM clustering.

        This merges raw signal values from recent transform calls into semantic
        clusters. Normally happens automatically every N transforms, but this endpoint
        lets you trigger it on-demand.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return self._post(
            path_template("/v1/graph/domains/{domain_id}/catalog/refresh", domain_id=domain_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CatalogRefreshResponse,
        )


class AsyncCatalogResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCatalogResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AsyncCatalogResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCatalogResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AsyncCatalogResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        domain_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CatalogRetrieveResponse:
        """
        Return the LLM-curated catalog showing what signal values exist in this domain.

        The catalog is built incrementally from transform calls. It contains:

        - entity_clusters: semantically-grouped entity values
        - relationship_patterns: clustered relationship types
        - signal_value_counts: raw per-band value frequencies
        - domain_distribution: per-band document counts
        - total_documents: total transforms processed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return await self._get(
            path_template("/v1/graph/domains/{domain_id}/catalog", domain_id=domain_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CatalogRetrieveResponse,
        )

    async def refresh(
        self,
        domain_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CatalogRefreshResponse:
        """
        Process any buffered signal values through LLM clustering.

        This merges raw signal values from recent transform calls into semantic
        clusters. Normally happens automatically every N transforms, but this endpoint
        lets you trigger it on-demand.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return await self._post(
            path_template("/v1/graph/domains/{domain_id}/catalog/refresh", domain_id=domain_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CatalogRefreshResponse,
        )


class CatalogResourceWithRawResponse:
    def __init__(self, catalog: CatalogResource) -> None:
        self._catalog = catalog

        self.retrieve = to_raw_response_wrapper(
            catalog.retrieve,
        )
        self.refresh = to_raw_response_wrapper(
            catalog.refresh,
        )


class AsyncCatalogResourceWithRawResponse:
    def __init__(self, catalog: AsyncCatalogResource) -> None:
        self._catalog = catalog

        self.retrieve = async_to_raw_response_wrapper(
            catalog.retrieve,
        )
        self.refresh = async_to_raw_response_wrapper(
            catalog.refresh,
        )


class CatalogResourceWithStreamingResponse:
    def __init__(self, catalog: CatalogResource) -> None:
        self._catalog = catalog

        self.retrieve = to_streamed_response_wrapper(
            catalog.retrieve,
        )
        self.refresh = to_streamed_response_wrapper(
            catalog.refresh,
        )


class AsyncCatalogResourceWithStreamingResponse:
    def __init__(self, catalog: AsyncCatalogResource) -> None:
        self._catalog = catalog

        self.retrieve = async_to_streamed_response_wrapper(
            catalog.retrieve,
        )
        self.refresh = async_to_streamed_response_wrapper(
            catalog.refresh,
        )
