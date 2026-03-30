# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from papr_memory import Papr, AsyncPapr
from tests.utils import assert_matches_type
from papr_memory.types.holographic import DomainListResponse, DomainCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDomains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Papr) -> None:
        domain = client.holographic.domains.create(
            fields=[
                {
                    "frequency": 4,
                    "name": "priority",
                    "type": "enum",
                },
                {
                    "frequency": 6,
                    "name": "component",
                    "type": "free_text",
                },
                {
                    "frequency": 12,
                    "name": "resolution_type",
                    "type": "enum",
                },
            ],
            name="acme:support_tickets:1.0.0",
        )
        assert_matches_type(DomainCreateResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Papr) -> None:
        domain = client.holographic.domains.create(
            fields=[
                {
                    "frequency": 4,
                    "name": "priority",
                    "type": "enum",
                    "description": "description",
                    "values": ["P0", "P1", "P2", "P3"],
                    "weight": 0.9,
                },
                {
                    "frequency": 6,
                    "name": "component",
                    "type": "free_text",
                    "description": "description",
                    "values": ["string"],
                    "weight": 0.7,
                },
                {
                    "frequency": 12,
                    "name": "resolution_type",
                    "type": "enum",
                    "description": "description",
                    "values": ["bug_fix", "config", "wontfix"],
                    "weight": 0.8,
                },
            ],
            name="acme:support_tickets:1.0.0",
            description="Support ticket classification schema",
        )
        assert_matches_type(DomainCreateResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Papr) -> None:
        response = client.holographic.domains.with_raw_response.create(
            fields=[
                {
                    "frequency": 4,
                    "name": "priority",
                    "type": "enum",
                },
                {
                    "frequency": 6,
                    "name": "component",
                    "type": "free_text",
                },
                {
                    "frequency": 12,
                    "name": "resolution_type",
                    "type": "enum",
                },
            ],
            name="acme:support_tickets:1.0.0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainCreateResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Papr) -> None:
        with client.holographic.domains.with_streaming_response.create(
            fields=[
                {
                    "frequency": 4,
                    "name": "priority",
                    "type": "enum",
                },
                {
                    "frequency": 6,
                    "name": "component",
                    "type": "free_text",
                },
                {
                    "frequency": 12,
                    "name": "resolution_type",
                    "type": "enum",
                },
            ],
            name="acme:support_tickets:1.0.0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainCreateResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Papr) -> None:
        domain = client.holographic.domains.list()
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Papr) -> None:
        response = client.holographic.domains.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Papr) -> None:
        with client.holographic.domains.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainListResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDomains:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPapr) -> None:
        domain = await async_client.holographic.domains.create(
            fields=[
                {
                    "frequency": 4,
                    "name": "priority",
                    "type": "enum",
                },
                {
                    "frequency": 6,
                    "name": "component",
                    "type": "free_text",
                },
                {
                    "frequency": 12,
                    "name": "resolution_type",
                    "type": "enum",
                },
            ],
            name="acme:support_tickets:1.0.0",
        )
        assert_matches_type(DomainCreateResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPapr) -> None:
        domain = await async_client.holographic.domains.create(
            fields=[
                {
                    "frequency": 4,
                    "name": "priority",
                    "type": "enum",
                    "description": "description",
                    "values": ["P0", "P1", "P2", "P3"],
                    "weight": 0.9,
                },
                {
                    "frequency": 6,
                    "name": "component",
                    "type": "free_text",
                    "description": "description",
                    "values": ["string"],
                    "weight": 0.7,
                },
                {
                    "frequency": 12,
                    "name": "resolution_type",
                    "type": "enum",
                    "description": "description",
                    "values": ["bug_fix", "config", "wontfix"],
                    "weight": 0.8,
                },
            ],
            name="acme:support_tickets:1.0.0",
            description="Support ticket classification schema",
        )
        assert_matches_type(DomainCreateResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPapr) -> None:
        response = await async_client.holographic.domains.with_raw_response.create(
            fields=[
                {
                    "frequency": 4,
                    "name": "priority",
                    "type": "enum",
                },
                {
                    "frequency": 6,
                    "name": "component",
                    "type": "free_text",
                },
                {
                    "frequency": 12,
                    "name": "resolution_type",
                    "type": "enum",
                },
            ],
            name="acme:support_tickets:1.0.0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainCreateResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPapr) -> None:
        async with async_client.holographic.domains.with_streaming_response.create(
            fields=[
                {
                    "frequency": 4,
                    "name": "priority",
                    "type": "enum",
                },
                {
                    "frequency": 6,
                    "name": "component",
                    "type": "free_text",
                },
                {
                    "frequency": 12,
                    "name": "resolution_type",
                    "type": "enum",
                },
            ],
            name="acme:support_tickets:1.0.0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainCreateResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPapr) -> None:
        domain = await async_client.holographic.domains.list()
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPapr) -> None:
        response = await async_client.holographic.domains.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPapr) -> None:
        async with async_client.holographic.domains.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainListResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True
