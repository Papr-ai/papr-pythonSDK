# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from papr_memory import Papr, AsyncPapr
from tests.utils import assert_matches_type
from papr_memory.types import CallbackProcessResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCallback:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_process(self, client: Papr) -> None:
        callback = client.callback.process()
        assert_matches_type(CallbackProcessResponse, callback, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_process(self, client: Papr) -> None:
        response = client.callback.with_raw_response.process()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        callback = response.parse()
        assert_matches_type(CallbackProcessResponse, callback, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_process(self, client: Papr) -> None:
        with client.callback.with_streaming_response.process() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            callback = response.parse()
            assert_matches_type(CallbackProcessResponse, callback, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCallback:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_process(self, async_client: AsyncPapr) -> None:
        callback = await async_client.callback.process()
        assert_matches_type(CallbackProcessResponse, callback, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_process(self, async_client: AsyncPapr) -> None:
        response = await async_client.callback.with_raw_response.process()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        callback = await response.parse()
        assert_matches_type(CallbackProcessResponse, callback, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_process(self, async_client: AsyncPapr) -> None:
        async with async_client.callback.with_streaming_response.process() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            callback = await response.parse()
            assert_matches_type(CallbackProcessResponse, callback, path=["response"])

        assert cast(Any, response.is_closed) is True
