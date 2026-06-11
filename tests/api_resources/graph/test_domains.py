# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from papr_memory import Papr, AsyncPapr
from tests.utils import assert_matches_type
from papr_memory.types.graph import (
    DomainListResponse,
    DomainCreateResponse,
    DomainDeleteResponse,
    DomainUpdateResponse,
    DomainRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDomains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Papr) -> None:
        domain = client.graph.domains.create(
            description="description",
            domain_id="domain_id",
            name="name",
            signals=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        )
        assert_matches_type(DomainCreateResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Papr) -> None:
        domain = client.graph.domains.create(
            description="description",
            domain_id="domain_id",
            name="name",
            signals=[
                {
                    "description": "description",
                    "name": "name",
                    "allowed_values": ["string"],
                    "frequency_hz": 0,
                    "required": True,
                    "type": "enum",
                    "weight": 0,
                }
            ],
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
            signal_multipliers={"foo": 0},
        )
        assert_matches_type(DomainCreateResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Papr) -> None:
        response = client.graph.domains.with_raw_response.create(
            description="description",
            domain_id="domain_id",
            name="name",
            signals=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainCreateResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Papr) -> None:
        with client.graph.domains.with_streaming_response.create(
            description="description",
            domain_id="domain_id",
            name="name",
            signals=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainCreateResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Papr) -> None:
        domain = client.graph.domains.retrieve(
            "domain_id",
        )
        assert_matches_type(DomainRetrieveResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Papr) -> None:
        response = client.graph.domains.with_raw_response.retrieve(
            "domain_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainRetrieveResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Papr) -> None:
        with client.graph.domains.with_streaming_response.retrieve(
            "domain_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainRetrieveResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Papr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            client.graph.domains.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Papr) -> None:
        domain = client.graph.domains.update(
            domain_id="domain_id",
        )
        assert_matches_type(DomainUpdateResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Papr) -> None:
        domain = client.graph.domains.update(
            domain_id="domain_id",
            description="description",
            name="name",
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
            signal_multipliers={"foo": 0},
        )
        assert_matches_type(DomainUpdateResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Papr) -> None:
        response = client.graph.domains.with_raw_response.update(
            domain_id="domain_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainUpdateResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Papr) -> None:
        with client.graph.domains.with_streaming_response.update(
            domain_id="domain_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainUpdateResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Papr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            client.graph.domains.with_raw_response.update(
                domain_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Papr) -> None:
        domain = client.graph.domains.list()
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Papr) -> None:
        response = client.graph.domains.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Papr) -> None:
        with client.graph.domains.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainListResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Papr) -> None:
        domain = client.graph.domains.delete(
            "domain_id",
        )
        assert_matches_type(DomainDeleteResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Papr) -> None:
        response = client.graph.domains.with_raw_response.delete(
            "domain_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainDeleteResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Papr) -> None:
        with client.graph.domains.with_streaming_response.delete(
            "domain_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainDeleteResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Papr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            client.graph.domains.with_raw_response.delete(
                "",
            )


class TestAsyncDomains:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPapr) -> None:
        domain = await async_client.graph.domains.create(
            description="description",
            domain_id="domain_id",
            name="name",
            signals=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        )
        assert_matches_type(DomainCreateResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPapr) -> None:
        domain = await async_client.graph.domains.create(
            description="description",
            domain_id="domain_id",
            name="name",
            signals=[
                {
                    "description": "description",
                    "name": "name",
                    "allowed_values": ["string"],
                    "frequency_hz": 0,
                    "required": True,
                    "type": "enum",
                    "weight": 0,
                }
            ],
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
            signal_multipliers={"foo": 0},
        )
        assert_matches_type(DomainCreateResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPapr) -> None:
        response = await async_client.graph.domains.with_raw_response.create(
            description="description",
            domain_id="domain_id",
            name="name",
            signals=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainCreateResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPapr) -> None:
        async with async_client.graph.domains.with_streaming_response.create(
            description="description",
            domain_id="domain_id",
            name="name",
            signals=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainCreateResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPapr) -> None:
        domain = await async_client.graph.domains.retrieve(
            "domain_id",
        )
        assert_matches_type(DomainRetrieveResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPapr) -> None:
        response = await async_client.graph.domains.with_raw_response.retrieve(
            "domain_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainRetrieveResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPapr) -> None:
        async with async_client.graph.domains.with_streaming_response.retrieve(
            "domain_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainRetrieveResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPapr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            await async_client.graph.domains.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncPapr) -> None:
        domain = await async_client.graph.domains.update(
            domain_id="domain_id",
        )
        assert_matches_type(DomainUpdateResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPapr) -> None:
        domain = await async_client.graph.domains.update(
            domain_id="domain_id",
            description="description",
            name="name",
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
            signal_multipliers={"foo": 0},
        )
        assert_matches_type(DomainUpdateResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPapr) -> None:
        response = await async_client.graph.domains.with_raw_response.update(
            domain_id="domain_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainUpdateResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPapr) -> None:
        async with async_client.graph.domains.with_streaming_response.update(
            domain_id="domain_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainUpdateResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncPapr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            await async_client.graph.domains.with_raw_response.update(
                domain_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPapr) -> None:
        domain = await async_client.graph.domains.list()
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPapr) -> None:
        response = await async_client.graph.domains.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPapr) -> None:
        async with async_client.graph.domains.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainListResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncPapr) -> None:
        domain = await async_client.graph.domains.delete(
            "domain_id",
        )
        assert_matches_type(DomainDeleteResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPapr) -> None:
        response = await async_client.graph.domains.with_raw_response.delete(
            "domain_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainDeleteResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPapr) -> None:
        async with async_client.graph.domains.with_streaming_response.delete(
            "domain_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainDeleteResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPapr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            await async_client.graph.domains.with_raw_response.delete(
                "",
            )
