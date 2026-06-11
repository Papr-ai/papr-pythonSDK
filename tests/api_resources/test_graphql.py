# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from papr_memory import Papr, AsyncPapr
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGraphql:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_playground(self, client: Papr) -> None:
        graphql = client.graphql.playground()
        assert_matches_type(object, graphql, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_playground(self, client: Papr) -> None:
        response = client.graphql.with_raw_response.playground()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graphql = response.parse()
        assert_matches_type(object, graphql, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_playground(self, client: Papr) -> None:
        with client.graphql.with_streaming_response.playground() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graphql = response.parse()
            assert_matches_type(object, graphql, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query(self, client: Papr) -> None:
        graphql = client.graphql.query()
        assert_matches_type(object, graphql, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_query(self, client: Papr) -> None:
        response = client.graphql.with_raw_response.query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graphql = response.parse()
        assert_matches_type(object, graphql, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_query(self, client: Papr) -> None:
        with client.graphql.with_streaming_response.query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graphql = response.parse()
            assert_matches_type(object, graphql, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGraphql:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_playground(self, async_client: AsyncPapr) -> None:
        graphql = await async_client.graphql.playground()
        assert_matches_type(object, graphql, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_playground(self, async_client: AsyncPapr) -> None:
        response = await async_client.graphql.with_raw_response.playground()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graphql = await response.parse()
        assert_matches_type(object, graphql, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_playground(self, async_client: AsyncPapr) -> None:
        async with async_client.graphql.with_streaming_response.playground() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graphql = await response.parse()
            assert_matches_type(object, graphql, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query(self, async_client: AsyncPapr) -> None:
        graphql = await async_client.graphql.query()
        assert_matches_type(object, graphql, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_query(self, async_client: AsyncPapr) -> None:
        response = await async_client.graphql.with_raw_response.query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graphql = await response.parse()
        assert_matches_type(object, graphql, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncPapr) -> None:
        async with async_client.graphql.with_streaming_response.query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graphql = await response.parse()
            assert_matches_type(object, graphql, path=["response"])

        assert cast(Any, response.is_closed) is True
