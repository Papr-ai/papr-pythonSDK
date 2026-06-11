# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from papr_memory import Papr, AsyncPapr
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnthropic:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_message(self, client: Papr) -> None:
        anthropic = client.ai.anthropic.send_message()
        assert_matches_type(object, anthropic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send_message(self, client: Papr) -> None:
        response = client.ai.anthropic.with_raw_response.send_message()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        anthropic = response.parse()
        assert_matches_type(object, anthropic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send_message(self, client: Papr) -> None:
        with client.ai.anthropic.with_streaming_response.send_message() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            anthropic = response.parse()
            assert_matches_type(object, anthropic, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAnthropic:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_message(self, async_client: AsyncPapr) -> None:
        anthropic = await async_client.ai.anthropic.send_message()
        assert_matches_type(object, anthropic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send_message(self, async_client: AsyncPapr) -> None:
        response = await async_client.ai.anthropic.with_raw_response.send_message()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        anthropic = await response.parse()
        assert_matches_type(object, anthropic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send_message(self, async_client: AsyncPapr) -> None:
        async with async_client.ai.anthropic.with_streaming_response.send_message() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            anthropic = await response.parse()
            assert_matches_type(object, anthropic, path=["response"])

        assert cast(Any, response.is_closed) is True
