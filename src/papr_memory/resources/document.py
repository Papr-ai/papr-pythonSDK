# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, Optional, cast
from typing_extensions import Literal

import httpx

from ..types import document_upload_params
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
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
from ..types.document_get_status_response import DocumentGetStatusResponse
from ..types.document_cancel_processing_response import DocumentCancelProcessingResponse

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

    def cancel_processing(
        self,
        upload_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentCancelProcessingResponse:
        """
        Cancel document processing

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upload_id:
            raise ValueError(f"Expected a non-empty value for `upload_id` but received {upload_id!r}")
        return self._delete(
            f"/v1/document/{upload_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentCancelProcessingResponse,
        )

    def get_status(
        self,
        upload_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentGetStatusResponse:
        """
        Get processing status for an uploaded document

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upload_id:
            raise ValueError(f"Expected a non-empty value for `upload_id` but received {upload_id!r}")
        return self._get(
            f"/v1/document/status/{upload_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentGetStatusResponse,
        )

    def upload(
        self,
        *,
        file: FileTypes,
        external_user_id: Optional[str] | Omit = omit,
        graph_override: Optional[str] | Omit = omit,
        hierarchical_enabled: bool | Omit = omit,
        memory_policy: Optional[str] | Omit = omit,
        metadata: Optional[str] | Omit = omit,
        namespace_id: Optional[str] | Omit = omit,
        preferred_provider: Optional[Literal["gemini", "tensorlake", "reducto", "auto"]] | Omit = omit,
        property_overrides: Optional[str] | Omit = omit,
        schema_id: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        webhook_secret: Optional[str] | Omit = omit,
        webhook_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentUploadResponse:
        """
        Upload and process documents using the pluggable architecture.

            **Authentication Required**: Bearer token or API key

            **Supported Providers**: TensorLake.ai, Reducto AI, Gemini Vision (fallback)

            **Features**:
            - Multi-tenant organization/namespace scoping
            - Temporal workflow for durable execution
            - Real-time WebSocket status updates
            - Integration with Parse Server (Post/PostSocial/PageVersion)
            - Automatic fallback between providers

        Args:
          external_user_id: Your application's user identifier. This is the primary way to identify users.
              Also accepts legacy 'end_user_id'.

          memory_policy: JSON-encoded memory policy. Includes mode ('auto'/'manual'), schema_id,
              node_constraints (applied in auto mode when present), and OMO fields (consent,
              risk, acl). This is the recommended way to configure memory processing.

          preferred_provider: Preferred provider for document processing.

          user_id: DEPRECATED: Internal Papr Parse user ID. Most developers should use
              external_user_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "external_user_id": external_user_id,
                "graph_override": graph_override,
                "hierarchical_enabled": hierarchical_enabled,
                "memory_policy": memory_policy,
                "metadata": metadata,
                "namespace_id": namespace_id,
                "preferred_provider": preferred_provider,
                "property_overrides": property_overrides,
                "schema_id": schema_id,
                "user_id": user_id,
                "webhook_secret": webhook_secret,
                "webhook_url": webhook_url,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/document",
            body=maybe_transform(body, document_upload_params.DocumentUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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

    async def cancel_processing(
        self,
        upload_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentCancelProcessingResponse:
        """
        Cancel document processing

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upload_id:
            raise ValueError(f"Expected a non-empty value for `upload_id` but received {upload_id!r}")
        return await self._delete(
            f"/v1/document/{upload_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentCancelProcessingResponse,
        )

    async def get_status(
        self,
        upload_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentGetStatusResponse:
        """
        Get processing status for an uploaded document

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upload_id:
            raise ValueError(f"Expected a non-empty value for `upload_id` but received {upload_id!r}")
        return await self._get(
            f"/v1/document/status/{upload_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentGetStatusResponse,
        )

    async def upload(
        self,
        *,
        file: FileTypes,
        external_user_id: Optional[str] | Omit = omit,
        graph_override: Optional[str] | Omit = omit,
        hierarchical_enabled: bool | Omit = omit,
        memory_policy: Optional[str] | Omit = omit,
        metadata: Optional[str] | Omit = omit,
        namespace_id: Optional[str] | Omit = omit,
        preferred_provider: Optional[Literal["gemini", "tensorlake", "reducto", "auto"]] | Omit = omit,
        property_overrides: Optional[str] | Omit = omit,
        schema_id: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        webhook_secret: Optional[str] | Omit = omit,
        webhook_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentUploadResponse:
        """
        Upload and process documents using the pluggable architecture.

            **Authentication Required**: Bearer token or API key

            **Supported Providers**: TensorLake.ai, Reducto AI, Gemini Vision (fallback)

            **Features**:
            - Multi-tenant organization/namespace scoping
            - Temporal workflow for durable execution
            - Real-time WebSocket status updates
            - Integration with Parse Server (Post/PostSocial/PageVersion)
            - Automatic fallback between providers

        Args:
          external_user_id: Your application's user identifier. This is the primary way to identify users.
              Also accepts legacy 'end_user_id'.

          memory_policy: JSON-encoded memory policy. Includes mode ('auto'/'manual'), schema_id,
              node_constraints (applied in auto mode when present), and OMO fields (consent,
              risk, acl). This is the recommended way to configure memory processing.

          preferred_provider: Preferred provider for document processing.

          user_id: DEPRECATED: Internal Papr Parse user ID. Most developers should use
              external_user_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "external_user_id": external_user_id,
                "graph_override": graph_override,
                "hierarchical_enabled": hierarchical_enabled,
                "memory_policy": memory_policy,
                "metadata": metadata,
                "namespace_id": namespace_id,
                "preferred_provider": preferred_provider,
                "property_overrides": property_overrides,
                "schema_id": schema_id,
                "user_id": user_id,
                "webhook_secret": webhook_secret,
                "webhook_url": webhook_url,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/document",
            body=await async_maybe_transform(body, document_upload_params.DocumentUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentUploadResponse,
        )


class DocumentResourceWithRawResponse:
    def __init__(self, document: DocumentResource) -> None:
        self._document = document

        self.cancel_processing = to_raw_response_wrapper(
            document.cancel_processing,
        )
        self.get_status = to_raw_response_wrapper(
            document.get_status,
        )
        self.upload = to_raw_response_wrapper(
            document.upload,
        )


class AsyncDocumentResourceWithRawResponse:
    def __init__(self, document: AsyncDocumentResource) -> None:
        self._document = document

        self.cancel_processing = async_to_raw_response_wrapper(
            document.cancel_processing,
        )
        self.get_status = async_to_raw_response_wrapper(
            document.get_status,
        )
        self.upload = async_to_raw_response_wrapper(
            document.upload,
        )


class DocumentResourceWithStreamingResponse:
    def __init__(self, document: DocumentResource) -> None:
        self._document = document

        self.cancel_processing = to_streamed_response_wrapper(
            document.cancel_processing,
        )
        self.get_status = to_streamed_response_wrapper(
            document.get_status,
        )
        self.upload = to_streamed_response_wrapper(
            document.upload,
        )


class AsyncDocumentResourceWithStreamingResponse:
    def __init__(self, document: AsyncDocumentResource) -> None:
        self._document = document

        self.cancel_processing = async_to_streamed_response_wrapper(
            document.cancel_processing,
        )
        self.get_status = async_to_streamed_response_wrapper(
            document.get_status,
        )
        self.upload = async_to_streamed_response_wrapper(
            document.upload,
        )
