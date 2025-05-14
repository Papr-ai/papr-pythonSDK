# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import document_upload_params
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
from ..types.document_upload_response import DocumentUploadResponse

__all__ = ["DocumentResource", "AsyncDocumentResource"]


class DocumentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DocumentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return DocumentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocumentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return DocumentResourceWithStreamingResponse(self)

    def upload(
        self,
        *,
        post_object_id: Optional[str] | NotGiven = NOT_GIVEN,
        skip_background_processing: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentUploadResponse:
        """
        Upload a document (PDF/HTML/TXT) to be processed and added to memory.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - Content-Type: multipart/form-data
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

            **Form Data**:
            - file: The document file to upload (PDF/HTML/TXT)
            - metadata: (optional) JSON string containing additional metadata

        Args:
          post_object_id: Optional Post objectId for updating status

          skip_background_processing: If True, skips adding background tasks for processing

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/document",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "post_object_id": post_object_id,
                        "skip_background_processing": skip_background_processing,
                    },
                    document_upload_params.DocumentUploadParams,
                ),
            ),
            cast_to=DocumentUploadResponse,
        )


class AsyncDocumentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDocumentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AsyncDocumentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocumentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AsyncDocumentResourceWithStreamingResponse(self)

    async def upload(
        self,
        *,
        post_object_id: Optional[str] | NotGiven = NOT_GIVEN,
        skip_background_processing: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentUploadResponse:
        """
        Upload a document (PDF/HTML/TXT) to be processed and added to memory.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - Content-Type: multipart/form-data
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

            **Form Data**:
            - file: The document file to upload (PDF/HTML/TXT)
            - metadata: (optional) JSON string containing additional metadata

        Args:
          post_object_id: Optional Post objectId for updating status

          skip_background_processing: If True, skips adding background tasks for processing

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/document",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "post_object_id": post_object_id,
                        "skip_background_processing": skip_background_processing,
                    },
                    document_upload_params.DocumentUploadParams,
                ),
            ),
            cast_to=DocumentUploadResponse,
        )


class DocumentResourceWithRawResponse:
    def __init__(self, document: DocumentResource) -> None:
        self._document = document

        self.upload = to_raw_response_wrapper(
            document.upload,
        )


class AsyncDocumentResourceWithRawResponse:
    def __init__(self, document: AsyncDocumentResource) -> None:
        self._document = document

        self.upload = async_to_raw_response_wrapper(
            document.upload,
        )


class DocumentResourceWithStreamingResponse:
    def __init__(self, document: DocumentResource) -> None:
        self._document = document

        self.upload = to_streamed_response_wrapper(
            document.upload,
        )


class AsyncDocumentResourceWithStreamingResponse:
    def __init__(self, document: AsyncDocumentResource) -> None:
        self._document = document

        self.upload = async_to_streamed_response_wrapper(
            document.upload,
        )
