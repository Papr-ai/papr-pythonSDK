# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from papr_memory import Papr, AsyncPapr
from tests.utils import assert_matches_type
from papr_memory.types import (
    NamespaceListResponse,
    NamespaceCreateResponse,
    NamespaceDeleteResponse,
    NamespaceUpdateResponse,
    NamespaceRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNamespace:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Papr) -> None:
        namespace = client.namespace.create(
            name="acme-production",
        )
        assert_matches_type(NamespaceCreateResponse, namespace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Papr) -> None:
        namespace = client.namespace.create(
            name="acme-production",
            environment_type="production",
            is_active=True,
            rate_limits={},
        )
        assert_matches_type(NamespaceCreateResponse, namespace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Papr) -> None:
        response = client.namespace.with_raw_response.create(
            name="acme-production",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert_matches_type(NamespaceCreateResponse, namespace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Papr) -> None:
        with client.namespace.with_streaming_response.create(
            name="acme-production",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert_matches_type(NamespaceCreateResponse, namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Papr) -> None:
        namespace = client.namespace.retrieve(
            "namespace_id",
        )
        assert_matches_type(NamespaceRetrieveResponse, namespace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Papr) -> None:
        response = client.namespace.with_raw_response.retrieve(
            "namespace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert_matches_type(NamespaceRetrieveResponse, namespace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Papr) -> None:
        with client.namespace.with_streaming_response.retrieve(
            "namespace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert_matches_type(NamespaceRetrieveResponse, namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Papr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            client.namespace.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Papr) -> None:
        namespace = client.namespace.update(
            namespace_id="namespace_id",
        )
        assert_matches_type(NamespaceUpdateResponse, namespace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Papr) -> None:
        namespace = client.namespace.update(
            namespace_id="namespace_id",
            environment_type="staging",
            is_active=True,
            name="acme-staging",
            rate_limits={"foo": 0},
        )
        assert_matches_type(NamespaceUpdateResponse, namespace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Papr) -> None:
        response = client.namespace.with_raw_response.update(
            namespace_id="namespace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert_matches_type(NamespaceUpdateResponse, namespace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Papr) -> None:
        with client.namespace.with_streaming_response.update(
            namespace_id="namespace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert_matches_type(NamespaceUpdateResponse, namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Papr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            client.namespace.with_raw_response.update(
                namespace_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Papr) -> None:
        namespace = client.namespace.list()
        assert_matches_type(NamespaceListResponse, namespace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Papr) -> None:
        namespace = client.namespace.list(
            limit=1,
            skip=0,
        )
        assert_matches_type(NamespaceListResponse, namespace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Papr) -> None:
        response = client.namespace.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert_matches_type(NamespaceListResponse, namespace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Papr) -> None:
        with client.namespace.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert_matches_type(NamespaceListResponse, namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Papr) -> None:
        namespace = client.namespace.delete(
            namespace_id="namespace_id",
        )
        assert_matches_type(NamespaceDeleteResponse, namespace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Papr) -> None:
        namespace = client.namespace.delete(
            namespace_id="namespace_id",
            delete_memories=True,
            delete_neo4j_nodes=True,
            remove_acl_references=True,
        )
        assert_matches_type(NamespaceDeleteResponse, namespace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Papr) -> None:
        response = client.namespace.with_raw_response.delete(
            namespace_id="namespace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert_matches_type(NamespaceDeleteResponse, namespace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Papr) -> None:
        with client.namespace.with_streaming_response.delete(
            namespace_id="namespace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert_matches_type(NamespaceDeleteResponse, namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Papr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            client.namespace.with_raw_response.delete(
                namespace_id="",
            )


class TestAsyncNamespace:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPapr) -> None:
        namespace = await async_client.namespace.create(
            name="acme-production",
        )
        assert_matches_type(NamespaceCreateResponse, namespace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPapr) -> None:
        namespace = await async_client.namespace.create(
            name="acme-production",
            environment_type="production",
            is_active=True,
            rate_limits={},
        )
        assert_matches_type(NamespaceCreateResponse, namespace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPapr) -> None:
        response = await async_client.namespace.with_raw_response.create(
            name="acme-production",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert_matches_type(NamespaceCreateResponse, namespace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPapr) -> None:
        async with async_client.namespace.with_streaming_response.create(
            name="acme-production",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert_matches_type(NamespaceCreateResponse, namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPapr) -> None:
        namespace = await async_client.namespace.retrieve(
            "namespace_id",
        )
        assert_matches_type(NamespaceRetrieveResponse, namespace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPapr) -> None:
        response = await async_client.namespace.with_raw_response.retrieve(
            "namespace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert_matches_type(NamespaceRetrieveResponse, namespace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPapr) -> None:
        async with async_client.namespace.with_streaming_response.retrieve(
            "namespace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert_matches_type(NamespaceRetrieveResponse, namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPapr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            await async_client.namespace.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncPapr) -> None:
        namespace = await async_client.namespace.update(
            namespace_id="namespace_id",
        )
        assert_matches_type(NamespaceUpdateResponse, namespace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPapr) -> None:
        namespace = await async_client.namespace.update(
            namespace_id="namespace_id",
            environment_type="staging",
            is_active=True,
            name="acme-staging",
            rate_limits={"foo": 0},
        )
        assert_matches_type(NamespaceUpdateResponse, namespace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPapr) -> None:
        response = await async_client.namespace.with_raw_response.update(
            namespace_id="namespace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert_matches_type(NamespaceUpdateResponse, namespace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPapr) -> None:
        async with async_client.namespace.with_streaming_response.update(
            namespace_id="namespace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert_matches_type(NamespaceUpdateResponse, namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncPapr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            await async_client.namespace.with_raw_response.update(
                namespace_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPapr) -> None:
        namespace = await async_client.namespace.list()
        assert_matches_type(NamespaceListResponse, namespace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPapr) -> None:
        namespace = await async_client.namespace.list(
            limit=1,
            skip=0,
        )
        assert_matches_type(NamespaceListResponse, namespace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPapr) -> None:
        response = await async_client.namespace.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert_matches_type(NamespaceListResponse, namespace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPapr) -> None:
        async with async_client.namespace.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert_matches_type(NamespaceListResponse, namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncPapr) -> None:
        namespace = await async_client.namespace.delete(
            namespace_id="namespace_id",
        )
        assert_matches_type(NamespaceDeleteResponse, namespace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncPapr) -> None:
        namespace = await async_client.namespace.delete(
            namespace_id="namespace_id",
            delete_memories=True,
            delete_neo4j_nodes=True,
            remove_acl_references=True,
        )
        assert_matches_type(NamespaceDeleteResponse, namespace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPapr) -> None:
        response = await async_client.namespace.with_raw_response.delete(
            namespace_id="namespace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert_matches_type(NamespaceDeleteResponse, namespace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPapr) -> None:
        async with async_client.namespace.with_streaming_response.delete(
            namespace_id="namespace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert_matches_type(NamespaceDeleteResponse, namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPapr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            await async_client.namespace.with_raw_response.delete(
                namespace_id="",
            )
