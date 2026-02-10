# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from papr_memory import Papr, AsyncPapr
from tests.utils import assert_matches_type
from papr_memory.types import (
    OmoExportMemoriesResponse,
    OmoImportMemoriesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOmo:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_export_memories(self, client: Papr) -> None:
        omo = client.omo.export_memories(
            memory_ids=["string"],
        )
        assert_matches_type(OmoExportMemoriesResponse, omo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_export_memories(self, client: Papr) -> None:
        response = client.omo.with_raw_response.export_memories(
            memory_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        omo = response.parse()
        assert_matches_type(OmoExportMemoriesResponse, omo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_export_memories(self, client: Papr) -> None:
        with client.omo.with_streaming_response.export_memories(
            memory_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            omo = response.parse()
            assert_matches_type(OmoExportMemoriesResponse, omo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_export_memories_as_json(self, client: Papr) -> None:
        omo = client.omo.export_memories_as_json(
            memory_ids="memory_ids",
        )
        assert_matches_type(object, omo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_export_memories_as_json(self, client: Papr) -> None:
        response = client.omo.with_raw_response.export_memories_as_json(
            memory_ids="memory_ids",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        omo = response.parse()
        assert_matches_type(object, omo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_export_memories_as_json(self, client: Papr) -> None:
        with client.omo.with_streaming_response.export_memories_as_json(
            memory_ids="memory_ids",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            omo = response.parse()
            assert_matches_type(object, omo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_import_memories(self, client: Papr) -> None:
        omo = client.omo.import_memories(
            memories=[{"foo": "bar"}],
        )
        assert_matches_type(OmoImportMemoriesResponse, omo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_import_memories_with_all_params(self, client: Papr) -> None:
        omo = client.omo.import_memories(
            memories=[{"foo": "bar"}],
            skip_duplicates=True,
        )
        assert_matches_type(OmoImportMemoriesResponse, omo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_import_memories(self, client: Papr) -> None:
        response = client.omo.with_raw_response.import_memories(
            memories=[{"foo": "bar"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        omo = response.parse()
        assert_matches_type(OmoImportMemoriesResponse, omo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_import_memories(self, client: Papr) -> None:
        with client.omo.with_streaming_response.import_memories(
            memories=[{"foo": "bar"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            omo = response.parse()
            assert_matches_type(OmoImportMemoriesResponse, omo, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOmo:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_export_memories(self, async_client: AsyncPapr) -> None:
        omo = await async_client.omo.export_memories(
            memory_ids=["string"],
        )
        assert_matches_type(OmoExportMemoriesResponse, omo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_export_memories(self, async_client: AsyncPapr) -> None:
        response = await async_client.omo.with_raw_response.export_memories(
            memory_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        omo = await response.parse()
        assert_matches_type(OmoExportMemoriesResponse, omo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_export_memories(self, async_client: AsyncPapr) -> None:
        async with async_client.omo.with_streaming_response.export_memories(
            memory_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            omo = await response.parse()
            assert_matches_type(OmoExportMemoriesResponse, omo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_export_memories_as_json(self, async_client: AsyncPapr) -> None:
        omo = await async_client.omo.export_memories_as_json(
            memory_ids="memory_ids",
        )
        assert_matches_type(object, omo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_export_memories_as_json(self, async_client: AsyncPapr) -> None:
        response = await async_client.omo.with_raw_response.export_memories_as_json(
            memory_ids="memory_ids",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        omo = await response.parse()
        assert_matches_type(object, omo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_export_memories_as_json(self, async_client: AsyncPapr) -> None:
        async with async_client.omo.with_streaming_response.export_memories_as_json(
            memory_ids="memory_ids",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            omo = await response.parse()
            assert_matches_type(object, omo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_import_memories(self, async_client: AsyncPapr) -> None:
        omo = await async_client.omo.import_memories(
            memories=[{"foo": "bar"}],
        )
        assert_matches_type(OmoImportMemoriesResponse, omo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_import_memories_with_all_params(self, async_client: AsyncPapr) -> None:
        omo = await async_client.omo.import_memories(
            memories=[{"foo": "bar"}],
            skip_duplicates=True,
        )
        assert_matches_type(OmoImportMemoriesResponse, omo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_import_memories(self, async_client: AsyncPapr) -> None:
        response = await async_client.omo.with_raw_response.import_memories(
            memories=[{"foo": "bar"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        omo = await response.parse()
        assert_matches_type(OmoImportMemoriesResponse, omo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_import_memories(self, async_client: AsyncPapr) -> None:
        async with async_client.omo.with_streaming_response.import_memories(
            memories=[{"foo": "bar"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            omo = await response.parse()
            assert_matches_type(OmoImportMemoriesResponse, omo, path=["response"])

        assert cast(Any, response.is_closed) is True
