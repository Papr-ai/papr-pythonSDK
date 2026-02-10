# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable

import httpx

from ..types import omo_export_memories_params, omo_import_memories_params, omo_export_memories_as_json_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.omo_export_memories_response import OmoExportMemoriesResponse
from ..types.omo_import_memories_response import OmoImportMemoriesResponse

__all__ = ["OmoResource", "AsyncOmoResource"]


class OmoResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OmoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return OmoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OmoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return OmoResourceWithStreamingResponse(self)

    def export_memories(
        self,
        *,
        memory_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OmoExportMemoriesResponse:
        """
        Export memories in Open Memory Object (OMO) standard format.

            This enables memory portability to other OMO-compliant platforms.
            The exported format follows the OMO v1 schema.

            **OMO Standard:** https://github.com/papr-ai/open-memory-object

        Args:
          memory_ids: List of memory IDs to export

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/omo/export",
            body=maybe_transform({"memory_ids": memory_ids}, omo_export_memories_params.OmoExportMemoriesParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OmoExportMemoriesResponse,
        )

    def export_memories_as_json(
        self,
        *,
        memory_ids: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Export memories in OMO JSON file format for download.

        Args:
          memory_ids: Comma-separated list of memory IDs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/omo/export.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"memory_ids": memory_ids}, omo_export_memories_as_json_params.OmoExportMemoriesAsJsonParams
                ),
            ),
            cast_to=object,
        )

    def import_memories(
        self,
        *,
        memories: Iterable[Dict[str, object]],
        skip_duplicates: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OmoImportMemoriesResponse:
        """
        Import memories from Open Memory Object (OMO) standard format.

            This enables importing memories from other OMO-compliant platforms.

            **OMO Standard:** https://github.com/papr-ai/open-memory-object

        Args:
          memories: List of memories in OMO v1 format

          skip_duplicates: Skip memories with IDs that already exist

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/omo/import",
            body=maybe_transform(
                {
                    "memories": memories,
                    "skip_duplicates": skip_duplicates,
                },
                omo_import_memories_params.OmoImportMemoriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OmoImportMemoriesResponse,
        )


class AsyncOmoResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOmoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AsyncOmoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOmoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AsyncOmoResourceWithStreamingResponse(self)

    async def export_memories(
        self,
        *,
        memory_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OmoExportMemoriesResponse:
        """
        Export memories in Open Memory Object (OMO) standard format.

            This enables memory portability to other OMO-compliant platforms.
            The exported format follows the OMO v1 schema.

            **OMO Standard:** https://github.com/papr-ai/open-memory-object

        Args:
          memory_ids: List of memory IDs to export

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/omo/export",
            body=await async_maybe_transform(
                {"memory_ids": memory_ids}, omo_export_memories_params.OmoExportMemoriesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OmoExportMemoriesResponse,
        )

    async def export_memories_as_json(
        self,
        *,
        memory_ids: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Export memories in OMO JSON file format for download.

        Args:
          memory_ids: Comma-separated list of memory IDs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/omo/export.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"memory_ids": memory_ids}, omo_export_memories_as_json_params.OmoExportMemoriesAsJsonParams
                ),
            ),
            cast_to=object,
        )

    async def import_memories(
        self,
        *,
        memories: Iterable[Dict[str, object]],
        skip_duplicates: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OmoImportMemoriesResponse:
        """
        Import memories from Open Memory Object (OMO) standard format.

            This enables importing memories from other OMO-compliant platforms.

            **OMO Standard:** https://github.com/papr-ai/open-memory-object

        Args:
          memories: List of memories in OMO v1 format

          skip_duplicates: Skip memories with IDs that already exist

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/omo/import",
            body=await async_maybe_transform(
                {
                    "memories": memories,
                    "skip_duplicates": skip_duplicates,
                },
                omo_import_memories_params.OmoImportMemoriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OmoImportMemoriesResponse,
        )


class OmoResourceWithRawResponse:
    def __init__(self, omo: OmoResource) -> None:
        self._omo = omo

        self.export_memories = to_raw_response_wrapper(
            omo.export_memories,
        )
        self.export_memories_as_json = to_raw_response_wrapper(
            omo.export_memories_as_json,
        )
        self.import_memories = to_raw_response_wrapper(
            omo.import_memories,
        )


class AsyncOmoResourceWithRawResponse:
    def __init__(self, omo: AsyncOmoResource) -> None:
        self._omo = omo

        self.export_memories = async_to_raw_response_wrapper(
            omo.export_memories,
        )
        self.export_memories_as_json = async_to_raw_response_wrapper(
            omo.export_memories_as_json,
        )
        self.import_memories = async_to_raw_response_wrapper(
            omo.import_memories,
        )


class OmoResourceWithStreamingResponse:
    def __init__(self, omo: OmoResource) -> None:
        self._omo = omo

        self.export_memories = to_streamed_response_wrapper(
            omo.export_memories,
        )
        self.export_memories_as_json = to_streamed_response_wrapper(
            omo.export_memories_as_json,
        )
        self.import_memories = to_streamed_response_wrapper(
            omo.import_memories,
        )


class AsyncOmoResourceWithStreamingResponse:
    def __init__(self, omo: AsyncOmoResource) -> None:
        self._omo = omo

        self.export_memories = async_to_streamed_response_wrapper(
            omo.export_memories,
        )
        self.export_memories_as_json = async_to_streamed_response_wrapper(
            omo.export_memories_as_json,
        )
        self.import_memories = async_to_streamed_response_wrapper(
            omo.import_memories,
        )
