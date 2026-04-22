# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from papr_memory import Papr, AsyncPapr
from tests.utils import assert_matches_type
from papr_memory.types.organization import (
    InstanceDeleteResponse,
    InstanceUpdateResponse,
    InstanceRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInstance:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Papr) -> None:
        instance = client.organization.instance.retrieve()
        assert_matches_type(InstanceRetrieveResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Papr) -> None:
        response = client.organization.instance.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceRetrieveResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Papr) -> None:
        with client.organization.instance.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceRetrieveResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Papr) -> None:
        instance = client.organization.instance.update()
        assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Papr) -> None:
        instance = client.organization.instance.update(
            validate=True,
            neo4j={
                "bolt_url": "neo4j+s://abc12345.databases.neo4j.io",
                "password": "my-secret-password",
                "graphql_endpoint": "https://abc12345-graphql.production-orch-0042.neo4j.io/graphql",
                "username": "neo4j",
            },
            provider="gcp",
            region="us-west1",
        )
        assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Papr) -> None:
        response = client.organization.instance.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Papr) -> None:
        with client.organization.instance.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Papr) -> None:
        instance = client.organization.instance.delete()
        assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Papr) -> None:
        response = client.organization.instance.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Papr) -> None:
        with client.organization.instance.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInstance:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPapr) -> None:
        instance = await async_client.organization.instance.retrieve()
        assert_matches_type(InstanceRetrieveResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPapr) -> None:
        response = await async_client.organization.instance.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceRetrieveResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPapr) -> None:
        async with async_client.organization.instance.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceRetrieveResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncPapr) -> None:
        instance = await async_client.organization.instance.update()
        assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPapr) -> None:
        instance = await async_client.organization.instance.update(
            validate=True,
            neo4j={
                "bolt_url": "neo4j+s://abc12345.databases.neo4j.io",
                "password": "my-secret-password",
                "graphql_endpoint": "https://abc12345-graphql.production-orch-0042.neo4j.io/graphql",
                "username": "neo4j",
            },
            provider="gcp",
            region="us-west1",
        )
        assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPapr) -> None:
        response = await async_client.organization.instance.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPapr) -> None:
        async with async_client.organization.instance.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncPapr) -> None:
        instance = await async_client.organization.instance.delete()
        assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPapr) -> None:
        response = await async_client.organization.instance.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPapr) -> None:
        async with async_client.organization.instance.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True
