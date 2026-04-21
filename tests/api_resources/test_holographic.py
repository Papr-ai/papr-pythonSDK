# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from papr_memory import Papr, AsyncPapr
from tests.utils import assert_matches_type
from papr_memory.types import (
    HolographicRerankResponse,
    HolographicExtractMetadataResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHolographic:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_metadata(self, client: Papr) -> None:
        holographic = client.holographic.extract_metadata(
            content="content",
        )
        assert_matches_type(HolographicExtractMetadataResponse, holographic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_metadata_with_all_params(self, client: Papr) -> None:
        holographic = client.holographic.extract_metadata(
            content="content",
            context_metadata={"foo": "bar"},
            domain="domain",
            frequency_schema_id="frequency_schema_id",
        )
        assert_matches_type(HolographicExtractMetadataResponse, holographic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_extract_metadata(self, client: Papr) -> None:
        response = client.holographic.with_raw_response.extract_metadata(
            content="content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        holographic = response.parse()
        assert_matches_type(HolographicExtractMetadataResponse, holographic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_extract_metadata(self, client: Papr) -> None:
        with client.holographic.with_streaming_response.extract_metadata(
            content="content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            holographic = response.parse()
            assert_matches_type(HolographicExtractMetadataResponse, holographic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rerank(self, client: Papr) -> None:
        holographic = client.holographic.rerank(
            candidates=[{"id": "doc_1"}, {"id": "doc_2"}],
            query="How does troponin relate to myocardial infarction?",
        )
        assert_matches_type(HolographicRerankResponse, holographic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rerank_with_all_params(self, client: Papr) -> None:
        holographic = client.holographic.rerank(
            candidates=[
                {
                    "id": "doc_1",
                    "content": "Troponin is a cardiac biomarker released during myocardial injury...",
                    "context_metadata": {"foo": "bar"},
                    "embedding": [0],
                    "metadata_embeddings": {"foo": [0]},
                    "phases": [0],
                    "score": 0,
                },
                {
                    "id": "doc_2",
                    "content": "Aspirin reduces platelet aggregation...",
                    "context_metadata": {"foo": "bar"},
                    "embedding": [0],
                    "metadata_embeddings": {"foo": [0]},
                    "phases": [0],
                    "score": 0,
                },
            ],
            query="How does troponin relate to myocardial infarction?",
            domain="biomedical",
            frequency_schema_id="frequency_schema_id",
            options={
                "cross_encoder_model": "cross_encoder_model",
                "cross_encoder_weight": 0,
                "ensemble": "auto",
                "frequency_filters": {"foo": 0},
                "include_frequency_scores": True,
                "return_scores": True,
                "scoring_method": "scoring_method",
                "use_cross_encoder": True,
            },
            query_embedding=[0],
            query_metadata_embeddings={"foo": [0]},
            query_phases=[0],
            top_k=10,
        )
        assert_matches_type(HolographicRerankResponse, holographic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rerank(self, client: Papr) -> None:
        response = client.holographic.with_raw_response.rerank(
            candidates=[{"id": "doc_1"}, {"id": "doc_2"}],
            query="How does troponin relate to myocardial infarction?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        holographic = response.parse()
        assert_matches_type(HolographicRerankResponse, holographic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rerank(self, client: Papr) -> None:
        with client.holographic.with_streaming_response.rerank(
            candidates=[{"id": "doc_1"}, {"id": "doc_2"}],
            query="How does troponin relate to myocardial infarction?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            holographic = response.parse()
            assert_matches_type(HolographicRerankResponse, holographic, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHolographic:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_metadata(self, async_client: AsyncPapr) -> None:
        holographic = await async_client.holographic.extract_metadata(
            content="content",
        )
        assert_matches_type(HolographicExtractMetadataResponse, holographic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_metadata_with_all_params(self, async_client: AsyncPapr) -> None:
        holographic = await async_client.holographic.extract_metadata(
            content="content",
            context_metadata={"foo": "bar"},
            domain="domain",
            frequency_schema_id="frequency_schema_id",
        )
        assert_matches_type(HolographicExtractMetadataResponse, holographic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_extract_metadata(self, async_client: AsyncPapr) -> None:
        response = await async_client.holographic.with_raw_response.extract_metadata(
            content="content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        holographic = await response.parse()
        assert_matches_type(HolographicExtractMetadataResponse, holographic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_extract_metadata(self, async_client: AsyncPapr) -> None:
        async with async_client.holographic.with_streaming_response.extract_metadata(
            content="content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            holographic = await response.parse()
            assert_matches_type(HolographicExtractMetadataResponse, holographic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rerank(self, async_client: AsyncPapr) -> None:
        holographic = await async_client.holographic.rerank(
            candidates=[{"id": "doc_1"}, {"id": "doc_2"}],
            query="How does troponin relate to myocardial infarction?",
        )
        assert_matches_type(HolographicRerankResponse, holographic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rerank_with_all_params(self, async_client: AsyncPapr) -> None:
        holographic = await async_client.holographic.rerank(
            candidates=[
                {
                    "id": "doc_1",
                    "content": "Troponin is a cardiac biomarker released during myocardial injury...",
                    "context_metadata": {"foo": "bar"},
                    "embedding": [0],
                    "metadata_embeddings": {"foo": [0]},
                    "phases": [0],
                    "score": 0,
                },
                {
                    "id": "doc_2",
                    "content": "Aspirin reduces platelet aggregation...",
                    "context_metadata": {"foo": "bar"},
                    "embedding": [0],
                    "metadata_embeddings": {"foo": [0]},
                    "phases": [0],
                    "score": 0,
                },
            ],
            query="How does troponin relate to myocardial infarction?",
            domain="biomedical",
            frequency_schema_id="frequency_schema_id",
            options={
                "cross_encoder_model": "cross_encoder_model",
                "cross_encoder_weight": 0,
                "ensemble": "auto",
                "frequency_filters": {"foo": 0},
                "include_frequency_scores": True,
                "return_scores": True,
                "scoring_method": "scoring_method",
                "use_cross_encoder": True,
            },
            query_embedding=[0],
            query_metadata_embeddings={"foo": [0]},
            query_phases=[0],
            top_k=10,
        )
        assert_matches_type(HolographicRerankResponse, holographic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rerank(self, async_client: AsyncPapr) -> None:
        response = await async_client.holographic.with_raw_response.rerank(
            candidates=[{"id": "doc_1"}, {"id": "doc_2"}],
            query="How does troponin relate to myocardial infarction?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        holographic = await response.parse()
        assert_matches_type(HolographicRerankResponse, holographic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rerank(self, async_client: AsyncPapr) -> None:
        async with async_client.holographic.with_streaming_response.rerank(
            candidates=[{"id": "doc_1"}, {"id": "doc_2"}],
            query="How does troponin relate to myocardial infarction?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            holographic = await response.parse()
            assert_matches_type(HolographicRerankResponse, holographic, path=["response"])

        assert cast(Any, response.is_closed) is True
