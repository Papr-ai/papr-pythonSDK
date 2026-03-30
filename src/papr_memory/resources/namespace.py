# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ..types import namespace_list_params, namespace_create_params, namespace_delete_params, namespace_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.namespace_list_response import NamespaceListResponse
from ..types.namespace_create_response import NamespaceCreateResponse
from ..types.namespace_delete_response import NamespaceDeleteResponse
from ..types.namespace_update_response import NamespaceUpdateResponse
from ..types.namespace_retrieve_response import NamespaceRetrieveResponse

__all__ = ["NamespaceResource", "AsyncNamespaceResource"]


class NamespaceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NamespaceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return NamespaceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NamespaceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return NamespaceResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        environment_type: Literal["development", "staging", "production"] | Omit = omit,
        is_active: bool | Omit = omit,
        rate_limits: Optional[Dict[str, Optional[int]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamespaceCreateResponse:
        """
        Create a new namespace within the developer's organization.

        Args:
          name: Namespace name (e.g., 'acme-production')

          environment_type: Environment type: development, staging, production

          is_active: Whether this namespace is active

          rate_limits: Rate limits for this namespace (None values inherit from organization)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/namespace",
            body=maybe_transform(
                {
                    "name": name,
                    "environment_type": environment_type,
                    "is_active": is_active,
                    "rate_limits": rate_limits,
                },
                namespace_create_params.NamespaceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamespaceCreateResponse,
        )

    def retrieve(
        self,
        namespace_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamespaceRetrieveResponse:
        """
        Retrieve a single namespace by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        return self._get(
            f"/v1/namespace/{namespace_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamespaceRetrieveResponse,
        )

    def update(
        self,
        namespace_id: str,
        *,
        environment_type: Optional[Literal["development", "staging", "production"]] | Omit = omit,
        is_active: Optional[bool] | Omit = omit,
        name: Optional[str] | Omit = omit,
        rate_limits: Optional[Dict[str, Optional[int]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamespaceUpdateResponse:
        """
        Update an existing namespace.

        Args:
          environment_type: Environment types for namespaces

          is_active: Whether this namespace is active

          name: Updated namespace name

          rate_limits: Updated rate limits (None values inherit from organization)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        return self._put(
            f"/v1/namespace/{namespace_id}",
            body=maybe_transform(
                {
                    "environment_type": environment_type,
                    "is_active": is_active,
                    "name": name,
                    "rate_limits": rate_limits,
                },
                namespace_update_params.NamespaceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamespaceUpdateResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        skip: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamespaceListResponse:
        """
        List namespaces for the developer's organization.

        Args:
          limit: Max items to return

          skip: Number of items to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/namespace",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    namespace_list_params.NamespaceListParams,
                ),
            ),
            cast_to=NamespaceListResponse,
        )

    def delete(
        self,
        namespace_id: str,
        *,
        delete_memories: bool | Omit = omit,
        delete_neo4j_nodes: bool | Omit = omit,
        remove_acl_references: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamespaceDeleteResponse:
        """
        Delete a namespace and optionally cascade-delete all memories, Neo4j nodes, and
        ACL references associated with it.

        Args:
          delete_memories: Delete all memories in this namespace

          delete_neo4j_nodes: Delete all Neo4j nodes in this namespace

          remove_acl_references: Remove namespace from ACL arrays on remaining nodes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        return self._delete(
            f"/v1/namespace/{namespace_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "delete_memories": delete_memories,
                        "delete_neo4j_nodes": delete_neo4j_nodes,
                        "remove_acl_references": remove_acl_references,
                    },
                    namespace_delete_params.NamespaceDeleteParams,
                ),
            ),
            cast_to=NamespaceDeleteResponse,
        )


class AsyncNamespaceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNamespaceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AsyncNamespaceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNamespaceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AsyncNamespaceResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        environment_type: Literal["development", "staging", "production"] | Omit = omit,
        is_active: bool | Omit = omit,
        rate_limits: Optional[Dict[str, Optional[int]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamespaceCreateResponse:
        """
        Create a new namespace within the developer's organization.

        Args:
          name: Namespace name (e.g., 'acme-production')

          environment_type: Environment type: development, staging, production

          is_active: Whether this namespace is active

          rate_limits: Rate limits for this namespace (None values inherit from organization)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/namespace",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "environment_type": environment_type,
                    "is_active": is_active,
                    "rate_limits": rate_limits,
                },
                namespace_create_params.NamespaceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamespaceCreateResponse,
        )

    async def retrieve(
        self,
        namespace_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamespaceRetrieveResponse:
        """
        Retrieve a single namespace by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        return await self._get(
            f"/v1/namespace/{namespace_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamespaceRetrieveResponse,
        )

    async def update(
        self,
        namespace_id: str,
        *,
        environment_type: Optional[Literal["development", "staging", "production"]] | Omit = omit,
        is_active: Optional[bool] | Omit = omit,
        name: Optional[str] | Omit = omit,
        rate_limits: Optional[Dict[str, Optional[int]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamespaceUpdateResponse:
        """
        Update an existing namespace.

        Args:
          environment_type: Environment types for namespaces

          is_active: Whether this namespace is active

          name: Updated namespace name

          rate_limits: Updated rate limits (None values inherit from organization)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        return await self._put(
            f"/v1/namespace/{namespace_id}",
            body=await async_maybe_transform(
                {
                    "environment_type": environment_type,
                    "is_active": is_active,
                    "name": name,
                    "rate_limits": rate_limits,
                },
                namespace_update_params.NamespaceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamespaceUpdateResponse,
        )

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        skip: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamespaceListResponse:
        """
        List namespaces for the developer's organization.

        Args:
          limit: Max items to return

          skip: Number of items to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/namespace",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    namespace_list_params.NamespaceListParams,
                ),
            ),
            cast_to=NamespaceListResponse,
        )

    async def delete(
        self,
        namespace_id: str,
        *,
        delete_memories: bool | Omit = omit,
        delete_neo4j_nodes: bool | Omit = omit,
        remove_acl_references: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamespaceDeleteResponse:
        """
        Delete a namespace and optionally cascade-delete all memories, Neo4j nodes, and
        ACL references associated with it.

        Args:
          delete_memories: Delete all memories in this namespace

          delete_neo4j_nodes: Delete all Neo4j nodes in this namespace

          remove_acl_references: Remove namespace from ACL arrays on remaining nodes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace_id:
            raise ValueError(f"Expected a non-empty value for `namespace_id` but received {namespace_id!r}")
        return await self._delete(
            f"/v1/namespace/{namespace_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "delete_memories": delete_memories,
                        "delete_neo4j_nodes": delete_neo4j_nodes,
                        "remove_acl_references": remove_acl_references,
                    },
                    namespace_delete_params.NamespaceDeleteParams,
                ),
            ),
            cast_to=NamespaceDeleteResponse,
        )


class NamespaceResourceWithRawResponse:
    def __init__(self, namespace: NamespaceResource) -> None:
        self._namespace = namespace

        self.create = to_raw_response_wrapper(
            namespace.create,
        )
        self.retrieve = to_raw_response_wrapper(
            namespace.retrieve,
        )
        self.update = to_raw_response_wrapper(
            namespace.update,
        )
        self.list = to_raw_response_wrapper(
            namespace.list,
        )
        self.delete = to_raw_response_wrapper(
            namespace.delete,
        )


class AsyncNamespaceResourceWithRawResponse:
    def __init__(self, namespace: AsyncNamespaceResource) -> None:
        self._namespace = namespace

        self.create = async_to_raw_response_wrapper(
            namespace.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            namespace.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            namespace.update,
        )
        self.list = async_to_raw_response_wrapper(
            namespace.list,
        )
        self.delete = async_to_raw_response_wrapper(
            namespace.delete,
        )


class NamespaceResourceWithStreamingResponse:
    def __init__(self, namespace: NamespaceResource) -> None:
        self._namespace = namespace

        self.create = to_streamed_response_wrapper(
            namespace.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            namespace.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            namespace.update,
        )
        self.list = to_streamed_response_wrapper(
            namespace.list,
        )
        self.delete = to_streamed_response_wrapper(
            namespace.delete,
        )


class AsyncNamespaceResourceWithStreamingResponse:
    def __init__(self, namespace: AsyncNamespaceResource) -> None:
        self._namespace = namespace

        self.create = async_to_streamed_response_wrapper(
            namespace.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            namespace.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            namespace.update,
        )
        self.list = async_to_streamed_response_wrapper(
            namespace.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            namespace.delete,
        )
