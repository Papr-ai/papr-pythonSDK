# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import telemetry_track_event_params
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
from ..types.telemetry_track_event_response import TelemetryTrackEventResponse

__all__ = ["TelemetryResource", "AsyncTelemetryResource"]


class TelemetryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TelemetryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return TelemetryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TelemetryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return TelemetryResourceWithStreamingResponse(self)

    def track_event(
        self,
        *,
        events: Iterable[telemetry_track_event_params.Event],
        anonymous_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelemetryTrackEventResponse:
        """
        Telemetry proxy endpoint for anonymous OSS adoption tracking.

            This endpoint receives telemetry events from OSS installations and forwards them
            to Amplitude using Papr's API key (which stays secure on the server).

            **Privacy**:
            - All user IDs are hashed/anonymized
            - No PII is collected
            - Data is used only for understanding OSS adoption patterns

            **Opt-in**: Users must explicitly enable telemetry in their OSS installation.

            **Request Body**:
            ```json
            {
              "events": [
                {
                  "event_name": "memory_created",
                  "properties": {
                    "type": "text",
                    "has_metadata": true
                  },
                  "user_id": "hashed_user_id",
                  "timestamp": 1234567890000
                }
              ],
              "anonymous_id": "session_id"
            }
            ```

        Args:
          events: List of telemetry events to track

          anonymous_id: Anonymous session ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/telemetry/events",
            body=maybe_transform(
                {
                    "events": events,
                    "anonymous_id": anonymous_id,
                },
                telemetry_track_event_params.TelemetryTrackEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelemetryTrackEventResponse,
        )


class AsyncTelemetryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTelemetryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AsyncTelemetryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTelemetryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AsyncTelemetryResourceWithStreamingResponse(self)

    async def track_event(
        self,
        *,
        events: Iterable[telemetry_track_event_params.Event],
        anonymous_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelemetryTrackEventResponse:
        """
        Telemetry proxy endpoint for anonymous OSS adoption tracking.

            This endpoint receives telemetry events from OSS installations and forwards them
            to Amplitude using Papr's API key (which stays secure on the server).

            **Privacy**:
            - All user IDs are hashed/anonymized
            - No PII is collected
            - Data is used only for understanding OSS adoption patterns

            **Opt-in**: Users must explicitly enable telemetry in their OSS installation.

            **Request Body**:
            ```json
            {
              "events": [
                {
                  "event_name": "memory_created",
                  "properties": {
                    "type": "text",
                    "has_metadata": true
                  },
                  "user_id": "hashed_user_id",
                  "timestamp": 1234567890000
                }
              ],
              "anonymous_id": "session_id"
            }
            ```

        Args:
          events: List of telemetry events to track

          anonymous_id: Anonymous session ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/telemetry/events",
            body=await async_maybe_transform(
                {
                    "events": events,
                    "anonymous_id": anonymous_id,
                },
                telemetry_track_event_params.TelemetryTrackEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelemetryTrackEventResponse,
        )


class TelemetryResourceWithRawResponse:
    def __init__(self, telemetry: TelemetryResource) -> None:
        self._telemetry = telemetry

        self.track_event = to_raw_response_wrapper(
            telemetry.track_event,
        )


class AsyncTelemetryResourceWithRawResponse:
    def __init__(self, telemetry: AsyncTelemetryResource) -> None:
        self._telemetry = telemetry

        self.track_event = async_to_raw_response_wrapper(
            telemetry.track_event,
        )


class TelemetryResourceWithStreamingResponse:
    def __init__(self, telemetry: TelemetryResource) -> None:
        self._telemetry = telemetry

        self.track_event = to_streamed_response_wrapper(
            telemetry.track_event,
        )


class AsyncTelemetryResourceWithStreamingResponse:
    def __init__(self, telemetry: AsyncTelemetryResource) -> None:
        self._telemetry = telemetry

        self.track_event = async_to_streamed_response_wrapper(
            telemetry.track_event,
        )
