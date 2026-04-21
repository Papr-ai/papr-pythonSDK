# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ...types.organization import instance_update_params
from ...types.organization.instance_delete_response import InstanceDeleteResponse
from ...types.organization.instance_update_response import InstanceUpdateResponse
from ...types.organization.instance_retrieve_response import InstanceRetrieveResponse

__all__ = ["InstanceResource", "AsyncInstanceResource"]


class InstanceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InstanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return InstanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return InstanceResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceRetrieveResponse:
        """Get organization-level instance configuration (masked passwords)."""
        return self._get(
            "/v1/organization/instance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceRetrieveResponse,
        )

    def update(
        self,
        *,
        validate: bool | Omit = omit,
        neo4j: Optional[instance_update_params.Neo4j] | Omit = omit,
        provider: str | Omit = omit,
        region: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceUpdateResponse:
        """
        Set default dedicated instance configuration for the organization (inherited by
        namespaces without their own config).

        Args:
          validate: Test connection before saving

          neo4j: Neo4j AuraDB instance configuration — input (plain password).

          provider: Cloud provider (only 'gcp' supported today)

          region: Cloud region (only 'us-west1' supported today)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v1/organization/instance",
            body=maybe_transform(
                {
                    "neo4j": neo4j,
                    "provider": provider,
                    "region": region,
                },
                instance_update_params.InstanceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"validate": validate}, instance_update_params.InstanceUpdateParams),
            ),
            cast_to=InstanceUpdateResponse,
        )

    def delete(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceDeleteResponse:
        """
        Remove organization-level instance configuration (all namespaces revert to
        shared).
        """
        return self._delete(
            "/v1/organization/instance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceDeleteResponse,
        )


class AsyncInstanceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInstanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AsyncInstanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AsyncInstanceResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceRetrieveResponse:
        """Get organization-level instance configuration (masked passwords)."""
        return await self._get(
            "/v1/organization/instance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceRetrieveResponse,
        )

    async def update(
        self,
        *,
        validate: bool | Omit = omit,
        neo4j: Optional[instance_update_params.Neo4j] | Omit = omit,
        provider: str | Omit = omit,
        region: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceUpdateResponse:
        """
        Set default dedicated instance configuration for the organization (inherited by
        namespaces without their own config).

        Args:
          validate: Test connection before saving

          neo4j: Neo4j AuraDB instance configuration — input (plain password).

          provider: Cloud provider (only 'gcp' supported today)

          region: Cloud region (only 'us-west1' supported today)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v1/organization/instance",
            body=await async_maybe_transform(
                {
                    "neo4j": neo4j,
                    "provider": provider,
                    "region": region,
                },
                instance_update_params.InstanceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"validate": validate}, instance_update_params.InstanceUpdateParams),
            ),
            cast_to=InstanceUpdateResponse,
        )

    async def delete(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceDeleteResponse:
        """
        Remove organization-level instance configuration (all namespaces revert to
        shared).
        """
        return await self._delete(
            "/v1/organization/instance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceDeleteResponse,
        )


class InstanceResourceWithRawResponse:
    def __init__(self, instance: InstanceResource) -> None:
        self._instance = instance

        self.retrieve = to_raw_response_wrapper(
            instance.retrieve,
        )
        self.update = to_raw_response_wrapper(
            instance.update,
        )
        self.delete = to_raw_response_wrapper(
            instance.delete,
        )


class AsyncInstanceResourceWithRawResponse:
    def __init__(self, instance: AsyncInstanceResource) -> None:
        self._instance = instance

        self.retrieve = async_to_raw_response_wrapper(
            instance.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            instance.update,
        )
        self.delete = async_to_raw_response_wrapper(
            instance.delete,
        )


class InstanceResourceWithStreamingResponse:
    def __init__(self, instance: InstanceResource) -> None:
        self._instance = instance

        self.retrieve = to_streamed_response_wrapper(
            instance.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            instance.update,
        )
        self.delete = to_streamed_response_wrapper(
            instance.delete,
        )


class AsyncInstanceResourceWithStreamingResponse:
    def __init__(self, instance: AsyncInstanceResource) -> None:
        self._instance = instance

        self.retrieve = async_to_streamed_response_wrapper(
            instance.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            instance.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            instance.delete,
        )
