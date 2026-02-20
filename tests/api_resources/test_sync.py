# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from papr_memory import Papr, AsyncPapr
from tests.utils import assert_matches_type
from papr_memory.types import SyncGetDeltaResponse, SyncGetTiersResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSync:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_delta(self, client: Papr) -> None:
        sync = client.sync.get_delta()
        assert_matches_type(SyncGetDeltaResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_delta_with_all_params(self, client: Papr) -> None:
        sync = client.sync.get_delta(
            cursor="cursor",
            include_embeddings=True,
            limit=1,
            workspace_id="workspace_id",
        )
        assert_matches_type(SyncGetDeltaResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_delta(self, client: Papr) -> None:
        response = client.sync.with_raw_response.get_delta()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(SyncGetDeltaResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_delta(self, client: Papr) -> None:
        with client.sync.with_streaming_response.get_delta() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = response.parse()
            assert_matches_type(SyncGetDeltaResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_tiers(self, client: Papr) -> None:
        sync = client.sync.get_tiers()
        assert_matches_type(SyncGetTiersResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_tiers_with_all_params(self, client: Papr) -> None:
        sync = client.sync.get_tiers(
            embed_limit=200,
            embed_model="sbert",
            embedding_format="int8",
            external_user_id="external_user_abc",
            include_embeddings=False,
            max_tier0=300,
            max_tier1=1000,
            namespace_id="namespace_id",
            organization_id="organization_id",
            user_id="internal_user_123",
            workspace_id="workspace_123",
        )
        assert_matches_type(SyncGetTiersResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_tiers(self, client: Papr) -> None:
        response = client.sync.with_raw_response.get_tiers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(SyncGetTiersResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_tiers(self, client: Papr) -> None:
        with client.sync.with_streaming_response.get_tiers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = response.parse()
            assert_matches_type(SyncGetTiersResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSync:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_delta(self, async_client: AsyncPapr) -> None:
        sync = await async_client.sync.get_delta()
        assert_matches_type(SyncGetDeltaResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_delta_with_all_params(self, async_client: AsyncPapr) -> None:
        sync = await async_client.sync.get_delta(
            cursor="cursor",
            include_embeddings=True,
            limit=1,
            workspace_id="workspace_id",
        )
        assert_matches_type(SyncGetDeltaResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_delta(self, async_client: AsyncPapr) -> None:
        response = await async_client.sync.with_raw_response.get_delta()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(SyncGetDeltaResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_delta(self, async_client: AsyncPapr) -> None:
        async with async_client.sync.with_streaming_response.get_delta() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = await response.parse()
            assert_matches_type(SyncGetDeltaResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_tiers(self, async_client: AsyncPapr) -> None:
        sync = await async_client.sync.get_tiers()
        assert_matches_type(SyncGetTiersResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_tiers_with_all_params(self, async_client: AsyncPapr) -> None:
        sync = await async_client.sync.get_tiers(
            embed_limit=200,
            embed_model="sbert",
            embedding_format="int8",
            external_user_id="external_user_abc",
            include_embeddings=False,
            max_tier0=300,
            max_tier1=1000,
            namespace_id="namespace_id",
            organization_id="organization_id",
            user_id="internal_user_123",
            workspace_id="workspace_123",
        )
        assert_matches_type(SyncGetTiersResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_tiers(self, async_client: AsyncPapr) -> None:
        response = await async_client.sync.with_raw_response.get_tiers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(SyncGetTiersResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_tiers(self, async_client: AsyncPapr) -> None:
        async with async_client.sync.with_streaming_response.get_tiers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = await response.parse()
            assert_matches_type(SyncGetTiersResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True
