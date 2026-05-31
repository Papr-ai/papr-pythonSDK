# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from papr_memory import Papr, AsyncPapr
from tests.utils import assert_matches_type
from papr_memory.types import GraphRerankResponse, GraphTransformResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGraph:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rerank(self, client: Papr) -> None:
        graph = client.graph.rerank(
            documents=["string"],
            query="string",
        )
        assert_matches_type(GraphRerankResponse, graph, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rerank_with_all_params(self, client: Papr) -> None:
        graph = client.graph.rerank(
            documents=["string"],
            query="string",
            domain_id="domain_id",
            method="fast",
            return_debug=True,
            return_documents=True,
            return_signal_scores=True,
            routing_config={
                "caesar4_source": "caesar4_source",
                "ce_gate_min_phi": 0,
                "disabled_rules": ["string"],
                "egr_lambda_ce": 0,
                "enabled_rule_packs": ["string"],
                "enhanced_initial_source": "enhanced_initial_source",
                "holographic_floor": True,
                "threshold_overrides": {"foo": 0},
            },
            signal_embedder="sbert",
            signal_filters={"foo": 0},
            signal_multipliers={"foo": "bar"},
            top_k=1,
        )
        assert_matches_type(GraphRerankResponse, graph, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rerank(self, client: Papr) -> None:
        response = client.graph.with_raw_response.rerank(
            documents=["string"],
            query="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = response.parse()
        assert_matches_type(GraphRerankResponse, graph, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rerank(self, client: Papr) -> None:
        with client.graph.with_streaming_response.rerank(
            documents=["string"],
            query="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = response.parse()
            assert_matches_type(GraphRerankResponse, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_transform(self, client: Papr) -> None:
        graph = client.graph.transform(
            text="text",
        )
        assert_matches_type(GraphTransformResponse, graph, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_transform_with_all_params(self, client: Papr) -> None:
        graph = client.graph.transform(
            text="text",
            domain_id="domain_id",
            embedding=[0],
            metadata={"foo": "bar"},
            return_concat=True,
            return_rot_v3=True,
            signal_embedder="sbert",
        )
        assert_matches_type(GraphTransformResponse, graph, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_transform(self, client: Papr) -> None:
        response = client.graph.with_raw_response.transform(
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = response.parse()
        assert_matches_type(GraphTransformResponse, graph, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_transform(self, client: Papr) -> None:
        with client.graph.with_streaming_response.transform(
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = response.parse()
            assert_matches_type(GraphTransformResponse, graph, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGraph:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rerank(self, async_client: AsyncPapr) -> None:
        graph = await async_client.graph.rerank(
            documents=["string"],
            query="string",
        )
        assert_matches_type(GraphRerankResponse, graph, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rerank_with_all_params(self, async_client: AsyncPapr) -> None:
        graph = await async_client.graph.rerank(
            documents=["string"],
            query="string",
            domain_id="domain_id",
            method="fast",
            return_debug=True,
            return_documents=True,
            return_signal_scores=True,
            routing_config={
                "caesar4_source": "caesar4_source",
                "ce_gate_min_phi": 0,
                "disabled_rules": ["string"],
                "egr_lambda_ce": 0,
                "enabled_rule_packs": ["string"],
                "enhanced_initial_source": "enhanced_initial_source",
                "holographic_floor": True,
                "threshold_overrides": {"foo": 0},
            },
            signal_embedder="sbert",
            signal_filters={"foo": 0},
            signal_multipliers={"foo": "bar"},
            top_k=1,
        )
        assert_matches_type(GraphRerankResponse, graph, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rerank(self, async_client: AsyncPapr) -> None:
        response = await async_client.graph.with_raw_response.rerank(
            documents=["string"],
            query="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = await response.parse()
        assert_matches_type(GraphRerankResponse, graph, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rerank(self, async_client: AsyncPapr) -> None:
        async with async_client.graph.with_streaming_response.rerank(
            documents=["string"],
            query="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = await response.parse()
            assert_matches_type(GraphRerankResponse, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_transform(self, async_client: AsyncPapr) -> None:
        graph = await async_client.graph.transform(
            text="text",
        )
        assert_matches_type(GraphTransformResponse, graph, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_transform_with_all_params(self, async_client: AsyncPapr) -> None:
        graph = await async_client.graph.transform(
            text="text",
            domain_id="domain_id",
            embedding=[0],
            metadata={"foo": "bar"},
            return_concat=True,
            return_rot_v3=True,
            signal_embedder="sbert",
        )
        assert_matches_type(GraphTransformResponse, graph, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_transform(self, async_client: AsyncPapr) -> None:
        response = await async_client.graph.with_raw_response.transform(
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = await response.parse()
        assert_matches_type(GraphTransformResponse, graph, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_transform(self, async_client: AsyncPapr) -> None:
        async with async_client.graph.with_streaming_response.transform(
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = await response.parse()
            assert_matches_type(GraphTransformResponse, graph, path=["response"])

        assert cast(Any, response.is_closed) is True
