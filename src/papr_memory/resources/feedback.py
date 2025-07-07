# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from ..types import feedback_submit_params, feedback_submit_batch_params
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
from ..types.batch_response import BatchResponse
from ..types.feedback_response import FeedbackResponse
from ..types.feedback_request_param import FeedbackRequestParam

__all__ = ["FeedbackResource", "AsyncFeedbackResource"]


class FeedbackResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FeedbackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return FeedbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FeedbackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return FeedbackResourceWithStreamingResponse(self)

    def get_by_id(
        self,
        feedback_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeedbackResponse:
        """
        Retrieve feedback by ID.

            This endpoint allows developers to fetch feedback details by feedback ID.
            Only the user who created the feedback or users with appropriate permissions can access it.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not feedback_id:
            raise ValueError(f"Expected a non-empty value for `feedback_id` but received {feedback_id!r}")
        return self._get(
            f"/v1/feedback/{feedback_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedbackResponse,
        )

    def submit(
        self,
        *,
        feedback_data: feedback_submit_params.FeedbackData,
        search_id: str,
        external_user_id: Optional[str] | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeedbackResponse:
        """
        Submit feedback on search results to help improve model performance.

            This endpoint allows developers to provide feedback on:
            - Overall answer quality (thumbs up/down, ratings)
            - Specific memory relevance and accuracy
            - User engagement signals (copy, save, create document actions)
            - Corrections and improvements

            The feedback is used to train and improve:
            - Router model tier predictions
            - Memory retrieval ranking
            - Answer generation quality
            - Agentic graph search performance

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - Content-Type: application/json
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

        Args:
          feedback_data: The feedback data containing all feedback information

          search_id: The search_id from SearchResponse that this feedback relates to

          external_user_id: External user ID for developer API keys acting on behalf of end users

          user_id: Internal user ID (if not provided, will be resolved from authentication)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/feedback",
            body=maybe_transform(
                {
                    "feedback_data": feedback_data,
                    "search_id": search_id,
                    "external_user_id": external_user_id,
                    "user_id": user_id,
                },
                feedback_submit_params.FeedbackSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedbackResponse,
        )

    def submit_batch(
        self,
        *,
        feedback_items: Iterable[FeedbackRequestParam],
        session_context: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchResponse:
        """
        Submit multiple feedback items in a single request.

            Useful for submitting session-end feedback or bulk feedback collection.
            Each feedback item is processed independently, so partial success is possible.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - Content-Type: application/json
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

        Args:
          feedback_items: List of feedback items to submit

          session_context: Session-level context for batch feedback

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/feedback/batch",
            body=maybe_transform(
                {
                    "feedback_items": feedback_items,
                    "session_context": session_context,
                },
                feedback_submit_batch_params.FeedbackSubmitBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponse,
        )


class AsyncFeedbackResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFeedbackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AsyncFeedbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFeedbackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AsyncFeedbackResourceWithStreamingResponse(self)

    async def get_by_id(
        self,
        feedback_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeedbackResponse:
        """
        Retrieve feedback by ID.

            This endpoint allows developers to fetch feedback details by feedback ID.
            Only the user who created the feedback or users with appropriate permissions can access it.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not feedback_id:
            raise ValueError(f"Expected a non-empty value for `feedback_id` but received {feedback_id!r}")
        return await self._get(
            f"/v1/feedback/{feedback_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedbackResponse,
        )

    async def submit(
        self,
        *,
        feedback_data: feedback_submit_params.FeedbackData,
        search_id: str,
        external_user_id: Optional[str] | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeedbackResponse:
        """
        Submit feedback on search results to help improve model performance.

            This endpoint allows developers to provide feedback on:
            - Overall answer quality (thumbs up/down, ratings)
            - Specific memory relevance and accuracy
            - User engagement signals (copy, save, create document actions)
            - Corrections and improvements

            The feedback is used to train and improve:
            - Router model tier predictions
            - Memory retrieval ranking
            - Answer generation quality
            - Agentic graph search performance

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - Content-Type: application/json
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

        Args:
          feedback_data: The feedback data containing all feedback information

          search_id: The search_id from SearchResponse that this feedback relates to

          external_user_id: External user ID for developer API keys acting on behalf of end users

          user_id: Internal user ID (if not provided, will be resolved from authentication)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/feedback",
            body=await async_maybe_transform(
                {
                    "feedback_data": feedback_data,
                    "search_id": search_id,
                    "external_user_id": external_user_id,
                    "user_id": user_id,
                },
                feedback_submit_params.FeedbackSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedbackResponse,
        )

    async def submit_batch(
        self,
        *,
        feedback_items: Iterable[FeedbackRequestParam],
        session_context: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchResponse:
        """
        Submit multiple feedback items in a single request.

            Useful for submitting session-end feedback or bulk feedback collection.
            Each feedback item is processed independently, so partial success is possible.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - Content-Type: application/json
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

        Args:
          feedback_items: List of feedback items to submit

          session_context: Session-level context for batch feedback

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/feedback/batch",
            body=await async_maybe_transform(
                {
                    "feedback_items": feedback_items,
                    "session_context": session_context,
                },
                feedback_submit_batch_params.FeedbackSubmitBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponse,
        )


class FeedbackResourceWithRawResponse:
    def __init__(self, feedback: FeedbackResource) -> None:
        self._feedback = feedback

        self.get_by_id = to_raw_response_wrapper(
            feedback.get_by_id,
        )
        self.submit = to_raw_response_wrapper(
            feedback.submit,
        )
        self.submit_batch = to_raw_response_wrapper(
            feedback.submit_batch,
        )


class AsyncFeedbackResourceWithRawResponse:
    def __init__(self, feedback: AsyncFeedbackResource) -> None:
        self._feedback = feedback

        self.get_by_id = async_to_raw_response_wrapper(
            feedback.get_by_id,
        )
        self.submit = async_to_raw_response_wrapper(
            feedback.submit,
        )
        self.submit_batch = async_to_raw_response_wrapper(
            feedback.submit_batch,
        )


class FeedbackResourceWithStreamingResponse:
    def __init__(self, feedback: FeedbackResource) -> None:
        self._feedback = feedback

        self.get_by_id = to_streamed_response_wrapper(
            feedback.get_by_id,
        )
        self.submit = to_streamed_response_wrapper(
            feedback.submit,
        )
        self.submit_batch = to_streamed_response_wrapper(
            feedback.submit_batch,
        )


class AsyncFeedbackResourceWithStreamingResponse:
    def __init__(self, feedback: AsyncFeedbackResource) -> None:
        self._feedback = feedback

        self.get_by_id = async_to_streamed_response_wrapper(
            feedback.get_by_id,
        )
        self.submit = async_to_streamed_response_wrapper(
            feedback.submit,
        )
        self.submit_batch = async_to_streamed_response_wrapper(
            feedback.submit_batch,
        )
