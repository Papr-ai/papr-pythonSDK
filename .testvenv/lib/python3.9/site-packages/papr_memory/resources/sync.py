# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import sync_get_delta_params, sync_get_tiers_params
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
from ..types.sync_get_delta_response import SyncGetDeltaResponse
from ..types.sync_get_tiers_response import SyncGetTiersResponse

__all__ = ["SyncResource", "AsyncSyncResource"]


class SyncResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SyncResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return SyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SyncResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return SyncResourceWithStreamingResponse(self)

    def get_delta(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        include_embeddings: bool | Omit = omit,
        limit: int | Omit = omit,
        workspace_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncGetDeltaResponse:
        """Return upserts/deletes since the provided cursor for a user/workspace.

        Cursor is
        an opaque watermark over updatedAt and objectId.

        Args:
          cursor: Opaque cursor from previous sync

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/sync/delta",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "include_embeddings": include_embeddings,
                        "limit": limit,
                        "workspace_id": workspace_id,
                    },
                    sync_get_delta_params.SyncGetDeltaParams,
                ),
            ),
            cast_to=SyncGetDeltaResponse,
        )

    def get_tiers(
        self,
        *,
        embed_limit: int | Omit = omit,
        embed_model: str | Omit = omit,
        embedding_format: Literal["int8", "float32"] | Omit = omit,
        external_user_id: Optional[str] | Omit = omit,
        include_embeddings: bool | Omit = omit,
        max_tier0: int | Omit = omit,
        max_tier1: int | Omit = omit,
        namespace_id: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        workspace_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncGetTiersResponse:
        """
        Return initial Tier 0 (goals/OKRs/use-cases --> tier 0 memories) and Tier 1 (hot
        memories) for the requesting user/workspace.

        This is a minimal initial implementation to enable SDK integration. It uses
        simple heuristics and will be enhanced with analytics-driven selection.

        Args:
          embed_limit: Max items to embed per tier to control latency

          embed_model: Embedding model hint: 'sbert' or 'bigbird' or 'Qwen4B'

          embedding_format: Embedding format: 'int8' (quantized, 4x smaller, default for efficiency),
              'float32' (full precision, recommended for CoreML/ANE fp16 models). Only applies
              to Tier1; Tier0 always uses float32 when embeddings are included.

          external_user_id: Optional external user ID to filter tiers by a specific external user. If both
              user_id and external_user_id are provided, user_id takes precedence.

          include_embeddings: Include embeddings in the response. Format controlled by embedding_format
              parameter.

          max_tier0: Max Tier 0 items (goals/OKRs/use-cases)

          max_tier1: Max Tier 1 items (hot memories)

          namespace_id: Optional namespace ID for multi-tenant scoping. When provided, tiers are scoped
              to memories within this namespace.

          organization_id: Optional organization ID for multi-tenant scoping. When provided, tiers are
              scoped to memories within this organization.

          user_id: Optional internal user ID to filter tiers by a specific user. If not provided,
              results are not filtered by user. If both user_id and external_user_id are
              provided, user_id takes precedence.

          workspace_id: Optional workspace id to scope tiers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/sync/tiers",
            body=maybe_transform(
                {
                    "embed_limit": embed_limit,
                    "embed_model": embed_model,
                    "embedding_format": embedding_format,
                    "external_user_id": external_user_id,
                    "include_embeddings": include_embeddings,
                    "max_tier0": max_tier0,
                    "max_tier1": max_tier1,
                    "namespace_id": namespace_id,
                    "organization_id": organization_id,
                    "user_id": user_id,
                    "workspace_id": workspace_id,
                },
                sync_get_tiers_params.SyncGetTiersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SyncGetTiersResponse,
        )


class AsyncSyncResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSyncResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AsyncSyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSyncResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AsyncSyncResourceWithStreamingResponse(self)

    async def get_delta(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        include_embeddings: bool | Omit = omit,
        limit: int | Omit = omit,
        workspace_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncGetDeltaResponse:
        """Return upserts/deletes since the provided cursor for a user/workspace.

        Cursor is
        an opaque watermark over updatedAt and objectId.

        Args:
          cursor: Opaque cursor from previous sync

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/sync/delta",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "include_embeddings": include_embeddings,
                        "limit": limit,
                        "workspace_id": workspace_id,
                    },
                    sync_get_delta_params.SyncGetDeltaParams,
                ),
            ),
            cast_to=SyncGetDeltaResponse,
        )

    async def get_tiers(
        self,
        *,
        embed_limit: int | Omit = omit,
        embed_model: str | Omit = omit,
        embedding_format: Literal["int8", "float32"] | Omit = omit,
        external_user_id: Optional[str] | Omit = omit,
        include_embeddings: bool | Omit = omit,
        max_tier0: int | Omit = omit,
        max_tier1: int | Omit = omit,
        namespace_id: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        workspace_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncGetTiersResponse:
        """
        Return initial Tier 0 (goals/OKRs/use-cases --> tier 0 memories) and Tier 1 (hot
        memories) for the requesting user/workspace.

        This is a minimal initial implementation to enable SDK integration. It uses
        simple heuristics and will be enhanced with analytics-driven selection.

        Args:
          embed_limit: Max items to embed per tier to control latency

          embed_model: Embedding model hint: 'sbert' or 'bigbird' or 'Qwen4B'

          embedding_format: Embedding format: 'int8' (quantized, 4x smaller, default for efficiency),
              'float32' (full precision, recommended for CoreML/ANE fp16 models). Only applies
              to Tier1; Tier0 always uses float32 when embeddings are included.

          external_user_id: Optional external user ID to filter tiers by a specific external user. If both
              user_id and external_user_id are provided, user_id takes precedence.

          include_embeddings: Include embeddings in the response. Format controlled by embedding_format
              parameter.

          max_tier0: Max Tier 0 items (goals/OKRs/use-cases)

          max_tier1: Max Tier 1 items (hot memories)

          namespace_id: Optional namespace ID for multi-tenant scoping. When provided, tiers are scoped
              to memories within this namespace.

          organization_id: Optional organization ID for multi-tenant scoping. When provided, tiers are
              scoped to memories within this organization.

          user_id: Optional internal user ID to filter tiers by a specific user. If not provided,
              results are not filtered by user. If both user_id and external_user_id are
              provided, user_id takes precedence.

          workspace_id: Optional workspace id to scope tiers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/sync/tiers",
            body=await async_maybe_transform(
                {
                    "embed_limit": embed_limit,
                    "embed_model": embed_model,
                    "embedding_format": embedding_format,
                    "external_user_id": external_user_id,
                    "include_embeddings": include_embeddings,
                    "max_tier0": max_tier0,
                    "max_tier1": max_tier1,
                    "namespace_id": namespace_id,
                    "organization_id": organization_id,
                    "user_id": user_id,
                    "workspace_id": workspace_id,
                },
                sync_get_tiers_params.SyncGetTiersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SyncGetTiersResponse,
        )


class SyncResourceWithRawResponse:
    def __init__(self, sync: SyncResource) -> None:
        self._sync = sync

        self.get_delta = to_raw_response_wrapper(
            sync.get_delta,
        )
        self.get_tiers = to_raw_response_wrapper(
            sync.get_tiers,
        )


class AsyncSyncResourceWithRawResponse:
    def __init__(self, sync: AsyncSyncResource) -> None:
        self._sync = sync

        self.get_delta = async_to_raw_response_wrapper(
            sync.get_delta,
        )
        self.get_tiers = async_to_raw_response_wrapper(
            sync.get_tiers,
        )


class SyncResourceWithStreamingResponse:
    def __init__(self, sync: SyncResource) -> None:
        self._sync = sync

        self.get_delta = to_streamed_response_wrapper(
            sync.get_delta,
        )
        self.get_tiers = to_streamed_response_wrapper(
            sync.get_tiers,
        )


class AsyncSyncResourceWithStreamingResponse:
    def __init__(self, sync: AsyncSyncResource) -> None:
        self._sync = sync

        self.get_delta = async_to_streamed_response_wrapper(
            sync.get_delta,
        )
        self.get_tiers = async_to_streamed_response_wrapper(
            sync.get_tiers,
        )
