# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from papr_memory import Papr, AsyncPapr
from tests.utils import assert_matches_type
from papr_memory.types import TokenCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestToken:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Papr) -> None:
        token = client.token.create()
        assert_matches_type(TokenCreateResponse, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Papr) -> None:
        response = client.token.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(TokenCreateResponse, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Papr) -> None:
        with client.token.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(TokenCreateResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncToken:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPapr) -> None:
        token = await async_client.token.create()
        assert_matches_type(TokenCreateResponse, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPapr) -> None:
        response = await async_client.token.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(TokenCreateResponse, token, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPapr) -> None:
        async with async_client.token.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(TokenCreateResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True
