# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from ..types import (
    UserType,
    user_list_params,
    user_create_params,
    user_delete_params,
    user_update_params,
    user_create_batch_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ..types.user_type import UserType
from ..types.user_response import UserResponse
from ..types.user_list_response import UserListResponse
from ..types.user_delete_response import UserDeleteResponse
from ..types.user_create_batch_response import UserCreateBatchResponse

__all__ = ["UserResource", "AsyncUserResource"]


class UserResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return UserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return UserResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        external_id: str,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        type: UserType | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserResponse:
        """
        Create a new user or link existing user to developer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/user",
            body=maybe_transform(
                {
                    "external_id": external_id,
                    "email": email,
                    "metadata": metadata,
                    "type": type,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserResponse,
        )

    def update(
        self,
        user_id: str,
        *,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        external_id: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        type: Optional[UserType] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserResponse:
        """
        Update user details by user_id (\\__User.objectId) and developer association

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._put(
            f"/v1/user/{user_id}",
            body=maybe_transform(
                {
                    "email": email,
                    "external_id": external_id,
                    "metadata": metadata,
                    "type": type,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserResponse,
        )

    def list(
        self,
        *,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        external_id: Optional[str] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListResponse:
        """
        List users for a developer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/user",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "email": email,
                        "external_id": external_id,
                        "page": page,
                        "page_size": page_size,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=UserListResponse,
        )

    def delete(
        self,
        user_id: str,
        *,
        is_external: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserDeleteResponse:
        """
        Delete user association with developer and the user itself by , assume external
        user_id is provided, and resolve to internal user_id (\\__User.objectId)

        Args:
          is_external: Is this an external user ID?

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._delete(
            f"/v1/user/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"is_external": is_external}, user_delete_params.UserDeleteParams),
            ),
            cast_to=UserDeleteResponse,
        )

    def create_batch(
        self,
        *,
        users: Iterable[user_create_batch_params.User],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserCreateBatchResponse:
        """
        Create multiple users or link existing users to developer, and add each to the
        developer's workspace (if one exists).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/user/batch",
            body=maybe_transform({"users": users}, user_create_batch_params.UserCreateBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserCreateBatchResponse,
        )

    def get(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserResponse:
        """
        Get user details by user_id (\\__User.objectId) and developer association

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/v1/user/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserResponse,
        )


class AsyncUserResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AsyncUserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AsyncUserResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        external_id: str,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        type: UserType | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserResponse:
        """
        Create a new user or link existing user to developer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/user",
            body=await async_maybe_transform(
                {
                    "external_id": external_id,
                    "email": email,
                    "metadata": metadata,
                    "type": type,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserResponse,
        )

    async def update(
        self,
        user_id: str,
        *,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        external_id: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        type: Optional[UserType] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserResponse:
        """
        Update user details by user_id (\\__User.objectId) and developer association

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._put(
            f"/v1/user/{user_id}",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "external_id": external_id,
                    "metadata": metadata,
                    "type": type,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserResponse,
        )

    async def list(
        self,
        *,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        external_id: Optional[str] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListResponse:
        """
        List users for a developer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/user",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "email": email,
                        "external_id": external_id,
                        "page": page,
                        "page_size": page_size,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=UserListResponse,
        )

    async def delete(
        self,
        user_id: str,
        *,
        is_external: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserDeleteResponse:
        """
        Delete user association with developer and the user itself by , assume external
        user_id is provided, and resolve to internal user_id (\\__User.objectId)

        Args:
          is_external: Is this an external user ID?

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._delete(
            f"/v1/user/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"is_external": is_external}, user_delete_params.UserDeleteParams),
            ),
            cast_to=UserDeleteResponse,
        )

    async def create_batch(
        self,
        *,
        users: Iterable[user_create_batch_params.User],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserCreateBatchResponse:
        """
        Create multiple users or link existing users to developer, and add each to the
        developer's workspace (if one exists).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/user/batch",
            body=await async_maybe_transform({"users": users}, user_create_batch_params.UserCreateBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserCreateBatchResponse,
        )

    async def get(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserResponse:
        """
        Get user details by user_id (\\__User.objectId) and developer association

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/v1/user/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserResponse,
        )


class UserResourceWithRawResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.create = to_raw_response_wrapper(
            user.create,
        )
        self.update = to_raw_response_wrapper(
            user.update,
        )
        self.list = to_raw_response_wrapper(
            user.list,
        )
        self.delete = to_raw_response_wrapper(
            user.delete,
        )
        self.create_batch = to_raw_response_wrapper(
            user.create_batch,
        )
        self.get = to_raw_response_wrapper(
            user.get,
        )


class AsyncUserResourceWithRawResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.create = async_to_raw_response_wrapper(
            user.create,
        )
        self.update = async_to_raw_response_wrapper(
            user.update,
        )
        self.list = async_to_raw_response_wrapper(
            user.list,
        )
        self.delete = async_to_raw_response_wrapper(
            user.delete,
        )
        self.create_batch = async_to_raw_response_wrapper(
            user.create_batch,
        )
        self.get = async_to_raw_response_wrapper(
            user.get,
        )


class UserResourceWithStreamingResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.create = to_streamed_response_wrapper(
            user.create,
        )
        self.update = to_streamed_response_wrapper(
            user.update,
        )
        self.list = to_streamed_response_wrapper(
            user.list,
        )
        self.delete = to_streamed_response_wrapper(
            user.delete,
        )
        self.create_batch = to_streamed_response_wrapper(
            user.create_batch,
        )
        self.get = to_streamed_response_wrapper(
            user.get,
        )


class AsyncUserResourceWithStreamingResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.create = async_to_streamed_response_wrapper(
            user.create,
        )
        self.update = async_to_streamed_response_wrapper(
            user.update,
        )
        self.list = async_to_streamed_response_wrapper(
            user.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            user.delete,
        )
        self.create_batch = async_to_streamed_response_wrapper(
            user.create_batch,
        )
        self.get = async_to_streamed_response_wrapper(
            user.get,
        )
