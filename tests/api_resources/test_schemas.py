# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from papr_memory import Papr, AsyncPapr
from tests.utils import assert_matches_type
from papr_memory.types import (
    SchemaListResponse,
    SchemaCreateResponse,
    SchemaUpdateResponse,
    SchemaRetrieveResponse,
)
from papr_memory._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSchemas:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Papr) -> None:
        schema = client.schemas.create(
            name="x",
        )
        assert_matches_type(SchemaCreateResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Papr) -> None:
        schema = client.schemas.create(
            name="x",
            id="id",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            description="description",
            last_used_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            node_types={
                "foo": {
                    "label": "label",
                    "name": "name",
                    "color": "color",
                    "description": "description",
                    "icon": "icon",
                    "properties": {
                        "foo": {
                            "type": "string",
                            "default": {},
                            "description": "description",
                            "enum_values": ["string"],
                            "max_length": 0,
                            "max_value": 0,
                            "min_length": 0,
                            "min_value": 0,
                            "pattern": "pattern",
                            "required": True,
                        }
                    },
                    "required_properties": ["string"],
                    "unique_identifiers": ["string"],
                }
            },
            organization_id="organization_id",
            read_access=["string"],
            relationship_types={
                "foo": {
                    "allowed_source_types": ["string"],
                    "allowed_target_types": ["string"],
                    "label": "label",
                    "name": "N96",
                    "cardinality": "one-to-one",
                    "color": "color",
                    "description": "description",
                    "properties": {
                        "foo": {
                            "type": "string",
                            "default": {},
                            "description": "description",
                            "enum_values": ["string"],
                            "max_length": 0,
                            "max_value": 0,
                            "min_length": 0,
                            "min_value": 0,
                            "pattern": "pattern",
                            "required": True,
                        }
                    },
                }
            },
            scope="personal",
            status="draft",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            usage_count=0,
            user_id="string",
            version="321669910225.155771193.090",
            workspace_id="string",
            write_access=["string"],
        )
        assert_matches_type(SchemaCreateResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Papr) -> None:
        response = client.schemas.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(SchemaCreateResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Papr) -> None:
        with client.schemas.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(SchemaCreateResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Papr) -> None:
        schema = client.schemas.retrieve(
            "schema_id",
        )
        assert_matches_type(SchemaRetrieveResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Papr) -> None:
        response = client.schemas.with_raw_response.retrieve(
            "schema_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(SchemaRetrieveResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Papr) -> None:
        with client.schemas.with_streaming_response.retrieve(
            "schema_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(SchemaRetrieveResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Papr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_id` but received ''"):
            client.schemas.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Papr) -> None:
        schema = client.schemas.update(
            schema_id="schema_id",
            body={"foo": "bar"},
        )
        assert_matches_type(SchemaUpdateResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Papr) -> None:
        response = client.schemas.with_raw_response.update(
            schema_id="schema_id",
            body={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(SchemaUpdateResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Papr) -> None:
        with client.schemas.with_streaming_response.update(
            schema_id="schema_id",
            body={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(SchemaUpdateResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Papr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_id` but received ''"):
            client.schemas.with_raw_response.update(
                schema_id="",
                body={"foo": "bar"},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Papr) -> None:
        schema = client.schemas.list()
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Papr) -> None:
        schema = client.schemas.list(
            status_filter="status_filter",
            workspace_id="workspace_id",
        )
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Papr) -> None:
        response = client.schemas.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Papr) -> None:
        with client.schemas.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(SchemaListResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_activate(self, client: Papr) -> None:
        schema = client.schemas.activate(
            schema_id="schema_id",
        )
        assert_matches_type(object, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_activate_with_all_params(self, client: Papr) -> None:
        schema = client.schemas.activate(
            schema_id="schema_id",
            body=True,
        )
        assert_matches_type(object, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_activate(self, client: Papr) -> None:
        response = client.schemas.with_raw_response.activate(
            schema_id="schema_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(object, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_activate(self, client: Papr) -> None:
        with client.schemas.with_streaming_response.activate(
            schema_id="schema_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(object, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_activate(self, client: Papr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_id` but received ''"):
            client.schemas.with_raw_response.activate(
                schema_id="",
            )


class TestAsyncSchemas:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPapr) -> None:
        schema = await async_client.schemas.create(
            name="x",
        )
        assert_matches_type(SchemaCreateResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPapr) -> None:
        schema = await async_client.schemas.create(
            name="x",
            id="id",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            description="description",
            last_used_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            node_types={
                "foo": {
                    "label": "label",
                    "name": "name",
                    "color": "color",
                    "description": "description",
                    "icon": "icon",
                    "properties": {
                        "foo": {
                            "type": "string",
                            "default": {},
                            "description": "description",
                            "enum_values": ["string"],
                            "max_length": 0,
                            "max_value": 0,
                            "min_length": 0,
                            "min_value": 0,
                            "pattern": "pattern",
                            "required": True,
                        }
                    },
                    "required_properties": ["string"],
                    "unique_identifiers": ["string"],
                }
            },
            organization_id="organization_id",
            read_access=["string"],
            relationship_types={
                "foo": {
                    "allowed_source_types": ["string"],
                    "allowed_target_types": ["string"],
                    "label": "label",
                    "name": "N96",
                    "cardinality": "one-to-one",
                    "color": "color",
                    "description": "description",
                    "properties": {
                        "foo": {
                            "type": "string",
                            "default": {},
                            "description": "description",
                            "enum_values": ["string"],
                            "max_length": 0,
                            "max_value": 0,
                            "min_length": 0,
                            "min_value": 0,
                            "pattern": "pattern",
                            "required": True,
                        }
                    },
                }
            },
            scope="personal",
            status="draft",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            usage_count=0,
            user_id="string",
            version="321669910225.155771193.090",
            workspace_id="string",
            write_access=["string"],
        )
        assert_matches_type(SchemaCreateResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPapr) -> None:
        response = await async_client.schemas.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(SchemaCreateResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPapr) -> None:
        async with async_client.schemas.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(SchemaCreateResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPapr) -> None:
        schema = await async_client.schemas.retrieve(
            "schema_id",
        )
        assert_matches_type(SchemaRetrieveResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPapr) -> None:
        response = await async_client.schemas.with_raw_response.retrieve(
            "schema_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(SchemaRetrieveResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPapr) -> None:
        async with async_client.schemas.with_streaming_response.retrieve(
            "schema_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(SchemaRetrieveResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPapr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_id` but received ''"):
            await async_client.schemas.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncPapr) -> None:
        schema = await async_client.schemas.update(
            schema_id="schema_id",
            body={"foo": "bar"},
        )
        assert_matches_type(SchemaUpdateResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPapr) -> None:
        response = await async_client.schemas.with_raw_response.update(
            schema_id="schema_id",
            body={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(SchemaUpdateResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPapr) -> None:
        async with async_client.schemas.with_streaming_response.update(
            schema_id="schema_id",
            body={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(SchemaUpdateResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncPapr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_id` but received ''"):
            await async_client.schemas.with_raw_response.update(
                schema_id="",
                body={"foo": "bar"},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPapr) -> None:
        schema = await async_client.schemas.list()
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPapr) -> None:
        schema = await async_client.schemas.list(
            status_filter="status_filter",
            workspace_id="workspace_id",
        )
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPapr) -> None:
        response = await async_client.schemas.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPapr) -> None:
        async with async_client.schemas.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(SchemaListResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_activate(self, async_client: AsyncPapr) -> None:
        schema = await async_client.schemas.activate(
            schema_id="schema_id",
        )
        assert_matches_type(object, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_activate_with_all_params(self, async_client: AsyncPapr) -> None:
        schema = await async_client.schemas.activate(
            schema_id="schema_id",
            body=True,
        )
        assert_matches_type(object, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_activate(self, async_client: AsyncPapr) -> None:
        response = await async_client.schemas.with_raw_response.activate(
            schema_id="schema_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(object, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_activate(self, async_client: AsyncPapr) -> None:
        async with async_client.schemas.with_streaming_response.activate(
            schema_id="schema_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(object, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_activate(self, async_client: AsyncPapr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_id` but received ''"):
            await async_client.schemas.with_raw_response.activate(
                schema_id="",
            )
