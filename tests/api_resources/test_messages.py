# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from papr_memory import Papr, AsyncPapr
from tests.utils import assert_matches_type
from papr_memory.types import MessageStoreResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_store(self, client: Papr) -> None:
        message = client.messages.store(
            content="string",
            role="user",
            session_id="sessionId",
        )
        assert_matches_type(MessageStoreResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_store_with_all_params(self, client: Papr) -> None:
        message = client.messages.store(
            content="string",
            role="user",
            session_id="sessionId",
            context=[{"foo": "bar"}],
            graph_generation={
                "auto": {
                    "property_overrides": [
                        {
                            "node_label": "User",
                            "set": {
                                "id": "bar",
                                "role": "bar",
                            },
                            "match": {"name": "bar"},
                        }
                    ],
                    "schema_id": "schema_id",
                },
                "manual": {
                    "nodes": [
                        {
                            "id": "x",
                            "label": "x",
                            "properties": {"foo": "bar"},
                        }
                    ],
                    "relationships": [
                        {
                            "relationship_type": "x",
                            "source_node_id": "x",
                            "target_node_id": "x",
                            "properties": {"foo": "bar"},
                        }
                    ],
                },
                "mode": "auto",
            },
            memory_policy={
                "acl": {
                    "read": ["external_user:alice_123", "organization:org_acme"],
                    "write": ["external_user:alice_123"],
                },
                "consent": "explicit",
                "edge_constraints": [
                    {
                        "create": "upsert",
                        "direction": "outgoing",
                        "edge_type": "x",
                        "link_only": True,
                        "on_miss": "create",
                        "search": {
                            "mode": "semantic",
                            "properties": [
                                {
                                    "name": "Exact ID match",
                                    "mode": "semantic",
                                    "threshold": 0,
                                    "value": {
                                        "mode": "exact",
                                        "name": "id",
                                    },
                                }
                            ],
                            "threshold": 0,
                            "via_relationship": [
                                {
                                    "name": "Find via ASSIGNED_TO",
                                    "summary": "Find nodes assigned to a specific person",
                                    "value": {
                                        "edge_type": "ASSIGNED_TO",
                                        "target_search": {
                                            "properties": [
                                                {
                                                    "name": "email",
                                                    "mode": "exact",
                                                    "value": "alice@example.com",
                                                }
                                            ]
                                        },
                                        "target_type": "Person",
                                    },
                                }
                            ],
                        },
                        "set": {"foo": "string"},
                        "source_type": "source_type",
                        "target_type": "target_type",
                        "when": {"foo": "bar"},
                    }
                ],
                "mode": "auto",
                "node_constraints": [
                    {
                        "create": "upsert",
                        "link_only": True,
                        "node_type": "x",
                        "on_miss": "create",
                        "search": {
                            "mode": "semantic",
                            "properties": [
                                {
                                    "name": "Exact ID match",
                                    "mode": "semantic",
                                    "threshold": 0,
                                    "value": {
                                        "mode": "exact",
                                        "name": "id",
                                    },
                                }
                            ],
                            "threshold": 0,
                            "via_relationship": [
                                {
                                    "name": "Find via ASSIGNED_TO",
                                    "summary": "Find nodes assigned to a specific person",
                                    "value": {
                                        "edge_type": "ASSIGNED_TO",
                                        "target_search": {
                                            "properties": [
                                                {
                                                    "name": "email",
                                                    "mode": "exact",
                                                    "value": "alice@example.com",
                                                }
                                            ]
                                        },
                                        "target_type": "Person",
                                    },
                                }
                            ],
                        },
                        "set": {"foo": "string"},
                        "when": {"foo": "bar"},
                    }
                ],
                "nodes": [
                    {
                        "id": "txn_12345",
                        "type": "Transaction",
                        "properties": {
                            "amount": "bar",
                            "product": "bar",
                            "timestamp": "bar",
                        },
                    }
                ],
                "relationships": [
                    {
                        "source": "txn_12345",
                        "target": "product_latte",
                        "type": "PURCHASED",
                        "properties": {"foo": "bar"},
                    }
                ],
                "risk": "none",
                "schema_id": "schema_id",
            },
            metadata={
                "acl": {"foo": ["string"]},
                "assistant_message": "assistantMessage",
                "category": "preference",
                "consent": "consent",
                "conversation_id": "conversationId",
                "created_at": "createdAt",
                "custom_metadata": {"foo": "string"},
                "emoji_tags": ["string"],
                "emotion_tags": ["string"],
                "external_user_id": "external_user_id",
                "external_user_read_access": ["string"],
                "external_user_write_access": ["string"],
                "goal_classification_scores": [0],
                "hierarchical_structures": "string",
                "location": "location",
                "namespace_id": "namespace_id",
                "namespace_read_access": ["string"],
                "namespace_write_access": ["string"],
                "organization_id": "organization_id",
                "organization_read_access": ["string"],
                "organization_write_access": ["string"],
                "page_id": "pageId",
                "post": "post",
                "related_goals": ["string"],
                "related_steps": ["string"],
                "related_use_cases": ["string"],
                "risk": "risk",
                "role": "user",
                "role_read_access": ["string"],
                "role_write_access": ["string"],
                "session_id": "sessionId",
                "source_type": "sourceType",
                "source_url": "sourceUrl",
                "step_classification_scores": [0],
                "topics": ["string"],
                "upload_id": "upload_id",
                "use_case_classification_scores": [0],
                "user_id": "user_id",
                "user_read_access": ["string"],
                "user_write_access": ["string"],
                "user_message": "userMessage",
                "workspace_id": "workspace_id",
                "workspace_read_access": ["string"],
                "workspace_write_access": ["string"],
            },
            namespace_id="namespace_id",
            organization_id="organization_id",
            process_messages=True,
            relationships_json=[{"foo": "bar"}],
            title="title",
        )
        assert_matches_type(MessageStoreResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_store(self, client: Papr) -> None:
        response = client.messages.with_raw_response.store(
            content="string",
            role="user",
            session_id="sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageStoreResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_store(self, client: Papr) -> None:
        with client.messages.with_streaming_response.store(
            content="string",
            role="user",
            session_id="sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageStoreResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_store(self, async_client: AsyncPapr) -> None:
        message = await async_client.messages.store(
            content="string",
            role="user",
            session_id="sessionId",
        )
        assert_matches_type(MessageStoreResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_store_with_all_params(self, async_client: AsyncPapr) -> None:
        message = await async_client.messages.store(
            content="string",
            role="user",
            session_id="sessionId",
            context=[{"foo": "bar"}],
            graph_generation={
                "auto": {
                    "property_overrides": [
                        {
                            "node_label": "User",
                            "set": {
                                "id": "bar",
                                "role": "bar",
                            },
                            "match": {"name": "bar"},
                        }
                    ],
                    "schema_id": "schema_id",
                },
                "manual": {
                    "nodes": [
                        {
                            "id": "x",
                            "label": "x",
                            "properties": {"foo": "bar"},
                        }
                    ],
                    "relationships": [
                        {
                            "relationship_type": "x",
                            "source_node_id": "x",
                            "target_node_id": "x",
                            "properties": {"foo": "bar"},
                        }
                    ],
                },
                "mode": "auto",
            },
            memory_policy={
                "acl": {
                    "read": ["external_user:alice_123", "organization:org_acme"],
                    "write": ["external_user:alice_123"],
                },
                "consent": "explicit",
                "edge_constraints": [
                    {
                        "create": "upsert",
                        "direction": "outgoing",
                        "edge_type": "x",
                        "link_only": True,
                        "on_miss": "create",
                        "search": {
                            "mode": "semantic",
                            "properties": [
                                {
                                    "name": "Exact ID match",
                                    "mode": "semantic",
                                    "threshold": 0,
                                    "value": {
                                        "mode": "exact",
                                        "name": "id",
                                    },
                                }
                            ],
                            "threshold": 0,
                            "via_relationship": [
                                {
                                    "name": "Find via ASSIGNED_TO",
                                    "summary": "Find nodes assigned to a specific person",
                                    "value": {
                                        "edge_type": "ASSIGNED_TO",
                                        "target_search": {
                                            "properties": [
                                                {
                                                    "name": "email",
                                                    "mode": "exact",
                                                    "value": "alice@example.com",
                                                }
                                            ]
                                        },
                                        "target_type": "Person",
                                    },
                                }
                            ],
                        },
                        "set": {"foo": "string"},
                        "source_type": "source_type",
                        "target_type": "target_type",
                        "when": {"foo": "bar"},
                    }
                ],
                "mode": "auto",
                "node_constraints": [
                    {
                        "create": "upsert",
                        "link_only": True,
                        "node_type": "x",
                        "on_miss": "create",
                        "search": {
                            "mode": "semantic",
                            "properties": [
                                {
                                    "name": "Exact ID match",
                                    "mode": "semantic",
                                    "threshold": 0,
                                    "value": {
                                        "mode": "exact",
                                        "name": "id",
                                    },
                                }
                            ],
                            "threshold": 0,
                            "via_relationship": [
                                {
                                    "name": "Find via ASSIGNED_TO",
                                    "summary": "Find nodes assigned to a specific person",
                                    "value": {
                                        "edge_type": "ASSIGNED_TO",
                                        "target_search": {
                                            "properties": [
                                                {
                                                    "name": "email",
                                                    "mode": "exact",
                                                    "value": "alice@example.com",
                                                }
                                            ]
                                        },
                                        "target_type": "Person",
                                    },
                                }
                            ],
                        },
                        "set": {"foo": "string"},
                        "when": {"foo": "bar"},
                    }
                ],
                "nodes": [
                    {
                        "id": "txn_12345",
                        "type": "Transaction",
                        "properties": {
                            "amount": "bar",
                            "product": "bar",
                            "timestamp": "bar",
                        },
                    }
                ],
                "relationships": [
                    {
                        "source": "txn_12345",
                        "target": "product_latte",
                        "type": "PURCHASED",
                        "properties": {"foo": "bar"},
                    }
                ],
                "risk": "none",
                "schema_id": "schema_id",
            },
            metadata={
                "acl": {"foo": ["string"]},
                "assistant_message": "assistantMessage",
                "category": "preference",
                "consent": "consent",
                "conversation_id": "conversationId",
                "created_at": "createdAt",
                "custom_metadata": {"foo": "string"},
                "emoji_tags": ["string"],
                "emotion_tags": ["string"],
                "external_user_id": "external_user_id",
                "external_user_read_access": ["string"],
                "external_user_write_access": ["string"],
                "goal_classification_scores": [0],
                "hierarchical_structures": "string",
                "location": "location",
                "namespace_id": "namespace_id",
                "namespace_read_access": ["string"],
                "namespace_write_access": ["string"],
                "organization_id": "organization_id",
                "organization_read_access": ["string"],
                "organization_write_access": ["string"],
                "page_id": "pageId",
                "post": "post",
                "related_goals": ["string"],
                "related_steps": ["string"],
                "related_use_cases": ["string"],
                "risk": "risk",
                "role": "user",
                "role_read_access": ["string"],
                "role_write_access": ["string"],
                "session_id": "sessionId",
                "source_type": "sourceType",
                "source_url": "sourceUrl",
                "step_classification_scores": [0],
                "topics": ["string"],
                "upload_id": "upload_id",
                "use_case_classification_scores": [0],
                "user_id": "user_id",
                "user_read_access": ["string"],
                "user_write_access": ["string"],
                "user_message": "userMessage",
                "workspace_id": "workspace_id",
                "workspace_read_access": ["string"],
                "workspace_write_access": ["string"],
            },
            namespace_id="namespace_id",
            organization_id="organization_id",
            process_messages=True,
            relationships_json=[{"foo": "bar"}],
            title="title",
        )
        assert_matches_type(MessageStoreResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_store(self, async_client: AsyncPapr) -> None:
        response = await async_client.messages.with_raw_response.store(
            content="string",
            role="user",
            session_id="sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageStoreResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_store(self, async_client: AsyncPapr) -> None:
        async with async_client.messages.with_streaming_response.store(
            content="string",
            role="user",
            session_id="sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageStoreResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True
