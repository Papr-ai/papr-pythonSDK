# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from .catalog import (
    CatalogResource,
    AsyncCatalogResource,
    CatalogResourceWithRawResponse,
    AsyncCatalogResourceWithRawResponse,
    CatalogResourceWithStreamingResponse,
    AsyncCatalogResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.graph import domain_create_params, domain_update_params
from ...._base_client import make_request_options
from ....types.graph.signal_field_param import SignalFieldParam
from ....types.graph.domain_list_response import DomainListResponse
from ....types.graph.domain_create_response import DomainCreateResponse
from ....types.graph.domain_delete_response import DomainDeleteResponse
from ....types.graph.domain_update_response import DomainUpdateResponse
from ....types.graph.domain_retrieve_response import DomainRetrieveResponse
from ....types.graph.domain_catalog_config_param import DomainCatalogConfigParam
from ....types.graph_domain_routing_config_param import GraphDomainRoutingConfigParam

__all__ = ["DomainsResource", "AsyncDomainsResource"]


class DomainsResource(SyncAPIResource):
    @cached_property
    def catalog(self) -> CatalogResource:
        return CatalogResource(self._client)

    @cached_property
    def with_raw_response(self) -> DomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return DomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return DomainsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: str,
        domain_id: str,
        name: str,
        signals: Iterable[SignalFieldParam],
        catalog_config: Optional[DomainCatalogConfigParam] | Omit = omit,
        routing_config: Optional[GraphDomainRoutingConfigParam] | Omit = omit,
        signal_multipliers: Optional[Dict[str, float]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainCreateResponse:
        """
        Create a custom domain

        Args:
          description: What this domain models.

          domain_id: Custom id, e.g. 'acme:support_tickets:1.0.0'.

          name: Human-readable domain name.

          signals: Per-domain signal definitions.

          catalog_config: Catalog settings on a domain.

          routing_config: Domain-scoped CAESAR-VIII routing overrides (stored on graph_domains).

          signal_multipliers: Domain-level default signal weight multipliers. Applied automatically on every
              rerank/search request for this domain (unless the caller supplies their own
              signal_multipliers, which take priority). Keys are field names (e.g.
              'key_claim') or Hz-strings (e.g. '70.0'). Values: 0.0 = disable band, 1.0 =
              unchanged, 2.0 = 2× boost.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/graph/domains",
            body=maybe_transform(
                {
                    "description": description,
                    "domain_id": domain_id,
                    "name": name,
                    "signals": signals,
                    "catalog_config": catalog_config,
                    "routing_config": routing_config,
                    "signal_multipliers": signal_multipliers,
                },
                domain_create_params.DomainCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainCreateResponse,
        )

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
    ) -> DomainRetrieveResponse:
        """
        Get a single domain by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return self._get(
            path_template("/v1/graph/domains/{domain_id}", domain_id=domain_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainRetrieveResponse,
        )

    def update(
        self,
        domain_id: str,
        *,
        catalog_config: Optional[DomainCatalogConfigParam] | Omit = omit,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        routing_config: Optional[GraphDomainRoutingConfigParam] | Omit = omit,
        signal_multipliers: Optional[Dict[str, float]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainUpdateResponse:
        """
        Update name, description, or signal_multipliers for a custom domain

        Args:
          catalog_config: Catalog settings on a domain.

          description: Updated description.

          name: Updated human-readable name.

          routing_config: Domain-scoped CAESAR-VIII routing overrides (stored on graph_domains).

          signal_multipliers: Replace the domain-level signal_multipliers entirely. Pass an empty dict {} to
              clear all multipliers. Omit the field to leave existing multipliers unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return self._put(
            path_template("/v1/graph/domains/{domain_id}", domain_id=domain_id),
            body=maybe_transform(
                {
                    "catalog_config": catalog_config,
                    "description": description,
                    "name": name,
                    "routing_config": routing_config,
                    "signal_multipliers": signal_multipliers,
                },
                domain_update_params.DomainUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainUpdateResponse,
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
    ) -> DomainListResponse:
        """List available domains (builtins + caller's custom domains)"""
        return self._get(
            "/v1/graph/domains",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainListResponse,
        )

    def delete(
        self,
        domain_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainDeleteResponse:
        """
        Delete a custom domain

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return self._delete(
            path_template("/v1/graph/domains/{domain_id}", domain_id=domain_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainDeleteResponse,
        )


class AsyncDomainsResource(AsyncAPIResource):
    @cached_property
    def catalog(self) -> AsyncCatalogResource:
        return AsyncCatalogResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AsyncDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AsyncDomainsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: str,
        domain_id: str,
        name: str,
        signals: Iterable[SignalFieldParam],
        catalog_config: Optional[DomainCatalogConfigParam] | Omit = omit,
        routing_config: Optional[GraphDomainRoutingConfigParam] | Omit = omit,
        signal_multipliers: Optional[Dict[str, float]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainCreateResponse:
        """
        Create a custom domain

        Args:
          description: What this domain models.

          domain_id: Custom id, e.g. 'acme:support_tickets:1.0.0'.

          name: Human-readable domain name.

          signals: Per-domain signal definitions.

          catalog_config: Catalog settings on a domain.

          routing_config: Domain-scoped CAESAR-VIII routing overrides (stored on graph_domains).

          signal_multipliers: Domain-level default signal weight multipliers. Applied automatically on every
              rerank/search request for this domain (unless the caller supplies their own
              signal_multipliers, which take priority). Keys are field names (e.g.
              'key_claim') or Hz-strings (e.g. '70.0'). Values: 0.0 = disable band, 1.0 =
              unchanged, 2.0 = 2× boost.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/graph/domains",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "domain_id": domain_id,
                    "name": name,
                    "signals": signals,
                    "catalog_config": catalog_config,
                    "routing_config": routing_config,
                    "signal_multipliers": signal_multipliers,
                },
                domain_create_params.DomainCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainCreateResponse,
        )

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
    ) -> DomainRetrieveResponse:
        """
        Get a single domain by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return await self._get(
            path_template("/v1/graph/domains/{domain_id}", domain_id=domain_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainRetrieveResponse,
        )

    async def update(
        self,
        domain_id: str,
        *,
        catalog_config: Optional[DomainCatalogConfigParam] | Omit = omit,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        routing_config: Optional[GraphDomainRoutingConfigParam] | Omit = omit,
        signal_multipliers: Optional[Dict[str, float]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainUpdateResponse:
        """
        Update name, description, or signal_multipliers for a custom domain

        Args:
          catalog_config: Catalog settings on a domain.

          description: Updated description.

          name: Updated human-readable name.

          routing_config: Domain-scoped CAESAR-VIII routing overrides (stored on graph_domains).

          signal_multipliers: Replace the domain-level signal_multipliers entirely. Pass an empty dict {} to
              clear all multipliers. Omit the field to leave existing multipliers unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return await self._put(
            path_template("/v1/graph/domains/{domain_id}", domain_id=domain_id),
            body=await async_maybe_transform(
                {
                    "catalog_config": catalog_config,
                    "description": description,
                    "name": name,
                    "routing_config": routing_config,
                    "signal_multipliers": signal_multipliers,
                },
                domain_update_params.DomainUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainUpdateResponse,
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
    ) -> DomainListResponse:
        """List available domains (builtins + caller's custom domains)"""
        return await self._get(
            "/v1/graph/domains",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainListResponse,
        )

    async def delete(
        self,
        domain_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainDeleteResponse:
        """
        Delete a custom domain

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return await self._delete(
            path_template("/v1/graph/domains/{domain_id}", domain_id=domain_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainDeleteResponse,
        )


class DomainsResourceWithRawResponse:
    def __init__(self, domains: DomainsResource) -> None:
        self._domains = domains

        self.create = to_raw_response_wrapper(
            domains.create,
        )
        self.retrieve = to_raw_response_wrapper(
            domains.retrieve,
        )
        self.update = to_raw_response_wrapper(
            domains.update,
        )
        self.list = to_raw_response_wrapper(
            domains.list,
        )
        self.delete = to_raw_response_wrapper(
            domains.delete,
        )

    @cached_property
    def catalog(self) -> CatalogResourceWithRawResponse:
        return CatalogResourceWithRawResponse(self._domains.catalog)


class AsyncDomainsResourceWithRawResponse:
    def __init__(self, domains: AsyncDomainsResource) -> None:
        self._domains = domains

        self.create = async_to_raw_response_wrapper(
            domains.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            domains.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            domains.update,
        )
        self.list = async_to_raw_response_wrapper(
            domains.list,
        )
        self.delete = async_to_raw_response_wrapper(
            domains.delete,
        )

    @cached_property
    def catalog(self) -> AsyncCatalogResourceWithRawResponse:
        return AsyncCatalogResourceWithRawResponse(self._domains.catalog)


class DomainsResourceWithStreamingResponse:
    def __init__(self, domains: DomainsResource) -> None:
        self._domains = domains

        self.create = to_streamed_response_wrapper(
            domains.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            domains.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            domains.update,
        )
        self.list = to_streamed_response_wrapper(
            domains.list,
        )
        self.delete = to_streamed_response_wrapper(
            domains.delete,
        )

    @cached_property
    def catalog(self) -> CatalogResourceWithStreamingResponse:
        return CatalogResourceWithStreamingResponse(self._domains.catalog)


class AsyncDomainsResourceWithStreamingResponse:
    def __init__(self, domains: AsyncDomainsResource) -> None:
        self._domains = domains

        self.create = async_to_streamed_response_wrapper(
            domains.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            domains.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            domains.update,
        )
        self.list = async_to_streamed_response_wrapper(
            domains.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            domains.delete,
        )

    @cached_property
    def catalog(self) -> AsyncCatalogResourceWithStreamingResponse:
        return AsyncCatalogResourceWithStreamingResponse(self._domains.catalog)
