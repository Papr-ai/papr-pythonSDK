# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from papr_memory import Papr, AsyncPapr
from tests.utils import assert_matches_type
from papr_memory.types import TelemetryTrackEventResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTelemetry:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_track_event(self, client: Papr) -> None:
        telemetry = client.telemetry.track_event(
            events=[{"event_name": "event_name"}],
        )
        assert_matches_type(TelemetryTrackEventResponse, telemetry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_track_event_with_all_params(self, client: Papr) -> None:
        telemetry = client.telemetry.track_event(
            events=[
                {
                    "event_name": "event_name",
                    "properties": {"foo": "bar"},
                    "timestamp": 0,
                    "user_id": "user_id",
                }
            ],
            anonymous_id="anonymous_id",
        )
        assert_matches_type(TelemetryTrackEventResponse, telemetry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_track_event(self, client: Papr) -> None:
        response = client.telemetry.with_raw_response.track_event(
            events=[{"event_name": "event_name"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = response.parse()
        assert_matches_type(TelemetryTrackEventResponse, telemetry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_track_event(self, client: Papr) -> None:
        with client.telemetry.with_streaming_response.track_event(
            events=[{"event_name": "event_name"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = response.parse()
            assert_matches_type(TelemetryTrackEventResponse, telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTelemetry:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_track_event(self, async_client: AsyncPapr) -> None:
        telemetry = await async_client.telemetry.track_event(
            events=[{"event_name": "event_name"}],
        )
        assert_matches_type(TelemetryTrackEventResponse, telemetry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_track_event_with_all_params(self, async_client: AsyncPapr) -> None:
        telemetry = await async_client.telemetry.track_event(
            events=[
                {
                    "event_name": "event_name",
                    "properties": {"foo": "bar"},
                    "timestamp": 0,
                    "user_id": "user_id",
                }
            ],
            anonymous_id="anonymous_id",
        )
        assert_matches_type(TelemetryTrackEventResponse, telemetry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_track_event(self, async_client: AsyncPapr) -> None:
        response = await async_client.telemetry.with_raw_response.track_event(
            events=[{"event_name": "event_name"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = await response.parse()
        assert_matches_type(TelemetryTrackEventResponse, telemetry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_track_event(self, async_client: AsyncPapr) -> None:
        async with async_client.telemetry.with_streaming_response.track_event(
            events=[{"event_name": "event_name"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = await response.parse()
            assert_matches_type(TelemetryTrackEventResponse, telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True
