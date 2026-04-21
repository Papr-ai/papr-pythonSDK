# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from papr_memory import Papr, AsyncPapr
from tests.utils import assert_matches_type
from papr_memory.types.namespace import (
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
        instance = client.namespace.instance.retrieve(
            "namespace_id",
        )
        assert_matches_type(InstanceRetrieveResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Papr) -> None:
        response = client.namespace.instance.with_raw_response.retrieve(
            "namespace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceRetrieveResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Papr) -> None:
        with client.namespace.instance.with_streaming_response.retrieve(
            "namespace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceRetrieveResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Papr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            client.namespace.instance.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Papr) -> None:
        instance = client.namespace.instance.update(
            namespace_id="namespace_id",
        )
        assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Papr) -> None:
        instance = client.namespace.instance.update(
            namespace_id="namespace_id",
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
        response = client.namespace.instance.with_raw_response.update(
            namespace_id="namespace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Papr) -> None:
        with client.namespace.instance.with_streaming_response.update(
            namespace_id="namespace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Papr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            client.namespace.instance.with_raw_response.update(
                namespace_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Papr) -> None:
        instance = client.namespace.instance.delete(
            "namespace_id",
        )
        assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Papr) -> None:
        response = client.namespace.instance.with_raw_response.delete(
            "namespace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Papr) -> None:
        with client.namespace.instance.with_streaming_response.delete(
            "namespace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Papr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            client.namespace.instance.with_raw_response.delete(
                "",
            )


class TestAsyncInstance:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPapr) -> None:
        instance = await async_client.namespace.instance.retrieve(
            "namespace_id",
        )
        assert_matches_type(InstanceRetrieveResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPapr) -> None:
        response = await async_client.namespace.instance.with_raw_response.retrieve(
            "namespace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceRetrieveResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPapr) -> None:
        async with async_client.namespace.instance.with_streaming_response.retrieve(
            "namespace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceRetrieveResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPapr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            await async_client.namespace.instance.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncPapr) -> None:
        instance = await async_client.namespace.instance.update(
            namespace_id="namespace_id",
        )
        assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPapr) -> None:
        instance = await async_client.namespace.instance.update(
            namespace_id="namespace_id",
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
        response = await async_client.namespace.instance.with_raw_response.update(
            namespace_id="namespace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPapr) -> None:
        async with async_client.namespace.instance.with_streaming_response.update(
            namespace_id="namespace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceUpdateResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncPapr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            await async_client.namespace.instance.with_raw_response.update(
                namespace_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncPapr) -> None:
        instance = await async_client.namespace.instance.delete(
            "namespace_id",
        )
        assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPapr) -> None:
        response = await async_client.namespace.instance.with_raw_response.delete(
            "namespace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPapr) -> None:
        async with async_client.namespace.instance.with_streaming_response.delete(
            "namespace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPapr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            await async_client.namespace.instance.with_raw_response.delete(
                "",
            )
