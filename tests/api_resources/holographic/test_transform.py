# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from papr_memory import Papr, AsyncPapr
from tests.utils import assert_matches_type
from papr_memory.types.holographic import (
    TransformCreateResponse,
    TransformCreateBatchResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransform:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Papr) -> None:
        transform = client.holographic.transform.create(
            content="The patient presents with elevated troponin levels indicating myocardial damage",
            embedding=[0.1, -0.2, 0.3],
        )
        assert_matches_type(TransformCreateResponse, transform, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Papr) -> None:
        transform = client.holographic.transform.create(
            content="The patient presents with elevated troponin levels indicating myocardial damage",
            embedding=[0.1, -0.2, 0.3],
            context_metadata={
                "createdAt": "bar",
                "sourceType": "bar",
            },
            domain="biomedical",
            frequency_schema_id="frequency_schema_id",
            output=["rotation_v3", "phases", "metadata"],
        )
        assert_matches_type(TransformCreateResponse, transform, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Papr) -> None:
        response = client.holographic.transform.with_raw_response.create(
            content="The patient presents with elevated troponin levels indicating myocardial damage",
            embedding=[0.1, -0.2, 0.3],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transform = response.parse()
        assert_matches_type(TransformCreateResponse, transform, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Papr) -> None:
        with client.holographic.transform.with_streaming_response.create(
            content="The patient presents with elevated troponin levels indicating myocardial damage",
            embedding=[0.1, -0.2, 0.3],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transform = response.parse()
            assert_matches_type(TransformCreateResponse, transform, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_batch(self, client: Papr) -> None:
        transform = client.holographic.transform.create_batch(
            items=[
                {
                    "id": "id",
                    "content": "content",
                    "embedding": [0],
                }
            ],
        )
        assert_matches_type(TransformCreateBatchResponse, transform, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_batch_with_all_params(self, client: Papr) -> None:
        transform = client.holographic.transform.create_batch(
            items=[
                {
                    "id": "id",
                    "content": "content",
                    "embedding": [0],
                    "context_metadata": {"foo": "bar"},
                }
            ],
            domain="domain",
            frequency_schema_id="frequency_schema_id",
            output=["base"],
        )
        assert_matches_type(TransformCreateBatchResponse, transform, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_batch(self, client: Papr) -> None:
        response = client.holographic.transform.with_raw_response.create_batch(
            items=[
                {
                    "id": "id",
                    "content": "content",
                    "embedding": [0],
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transform = response.parse()
        assert_matches_type(TransformCreateBatchResponse, transform, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_batch(self, client: Papr) -> None:
        with client.holographic.transform.with_streaming_response.create_batch(
            items=[
                {
                    "id": "id",
                    "content": "content",
                    "embedding": [0],
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transform = response.parse()
            assert_matches_type(TransformCreateBatchResponse, transform, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTransform:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPapr) -> None:
        transform = await async_client.holographic.transform.create(
            content="The patient presents with elevated troponin levels indicating myocardial damage",
            embedding=[0.1, -0.2, 0.3],
        )
        assert_matches_type(TransformCreateResponse, transform, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPapr) -> None:
        transform = await async_client.holographic.transform.create(
            content="The patient presents with elevated troponin levels indicating myocardial damage",
            embedding=[0.1, -0.2, 0.3],
            context_metadata={
                "createdAt": "bar",
                "sourceType": "bar",
            },
            domain="biomedical",
            frequency_schema_id="frequency_schema_id",
            output=["rotation_v3", "phases", "metadata"],
        )
        assert_matches_type(TransformCreateResponse, transform, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPapr) -> None:
        response = await async_client.holographic.transform.with_raw_response.create(
            content="The patient presents with elevated troponin levels indicating myocardial damage",
            embedding=[0.1, -0.2, 0.3],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transform = await response.parse()
        assert_matches_type(TransformCreateResponse, transform, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPapr) -> None:
        async with async_client.holographic.transform.with_streaming_response.create(
            content="The patient presents with elevated troponin levels indicating myocardial damage",
            embedding=[0.1, -0.2, 0.3],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transform = await response.parse()
            assert_matches_type(TransformCreateResponse, transform, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_batch(self, async_client: AsyncPapr) -> None:
        transform = await async_client.holographic.transform.create_batch(
            items=[
                {
                    "id": "id",
                    "content": "content",
                    "embedding": [0],
                }
            ],
        )
        assert_matches_type(TransformCreateBatchResponse, transform, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_batch_with_all_params(self, async_client: AsyncPapr) -> None:
        transform = await async_client.holographic.transform.create_batch(
            items=[
                {
                    "id": "id",
                    "content": "content",
                    "embedding": [0],
                    "context_metadata": {"foo": "bar"},
                }
            ],
            domain="domain",
            frequency_schema_id="frequency_schema_id",
            output=["base"],
        )
        assert_matches_type(TransformCreateBatchResponse, transform, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_batch(self, async_client: AsyncPapr) -> None:
        response = await async_client.holographic.transform.with_raw_response.create_batch(
            items=[
                {
                    "id": "id",
                    "content": "content",
                    "embedding": [0],
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transform = await response.parse()
        assert_matches_type(TransformCreateBatchResponse, transform, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_batch(self, async_client: AsyncPapr) -> None:
        async with async_client.holographic.transform.with_streaming_response.create_batch(
            items=[
                {
                    "id": "id",
                    "content": "content",
                    "embedding": [0],
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transform = await response.parse()
            assert_matches_type(TransformCreateBatchResponse, transform, path=["response"])

        assert cast(Any, response.is_closed) is True
