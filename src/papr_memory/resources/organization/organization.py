# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .instance import (
    InstanceResource,
    AsyncInstanceResource,
    InstanceResourceWithRawResponse,
    AsyncInstanceResourceWithRawResponse,
    InstanceResourceWithStreamingResponse,
    AsyncInstanceResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["OrganizationResource", "AsyncOrganizationResource"]


class OrganizationResource(SyncAPIResource):
    @cached_property
    def instance(self) -> InstanceResource:
        return InstanceResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrganizationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return OrganizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return OrganizationResourceWithStreamingResponse(self)


class AsyncOrganizationResource(AsyncAPIResource):
    @cached_property
    def instance(self) -> AsyncInstanceResource:
        return AsyncInstanceResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrganizationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AsyncOrganizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AsyncOrganizationResourceWithStreamingResponse(self)


class OrganizationResourceWithRawResponse:
    def __init__(self, organization: OrganizationResource) -> None:
        self._organization = organization

    @cached_property
    def instance(self) -> InstanceResourceWithRawResponse:
        return InstanceResourceWithRawResponse(self._organization.instance)


class AsyncOrganizationResourceWithRawResponse:
    def __init__(self, organization: AsyncOrganizationResource) -> None:
        self._organization = organization

    @cached_property
    def instance(self) -> AsyncInstanceResourceWithRawResponse:
        return AsyncInstanceResourceWithRawResponse(self._organization.instance)


class OrganizationResourceWithStreamingResponse:
    def __init__(self, organization: OrganizationResource) -> None:
        self._organization = organization

    @cached_property
    def instance(self) -> InstanceResourceWithStreamingResponse:
        return InstanceResourceWithStreamingResponse(self._organization.instance)


class AsyncOrganizationResourceWithStreamingResponse:
    def __init__(self, organization: AsyncOrganizationResource) -> None:
        self._organization = organization

    @cached_property
    def instance(self) -> AsyncInstanceResourceWithStreamingResponse:
        return AsyncInstanceResourceWithStreamingResponse(self._organization.instance)
