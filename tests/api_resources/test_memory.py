# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from papr_memory import Papr, AsyncPapr
from tests.utils import assert_matches_type
from papr_memory.types import (
    SearchResponse,
    AddMemoryResponse,
    BatchMemoryResponse,
    MemoryDeleteResponse,
    MemoryUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMemory:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Papr) -> None:
        memory = client.memory.update(
            memory_id="memory_id",
        )
        assert_matches_type(MemoryUpdateResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Papr) -> None:
        memory = client.memory.update(
            memory_id="memory_id",
            content="Updated meeting notes from the product planning session",
            context=[
                {
                    "content": "Let's update the Q2 product roadmap",
                    "role": "user",
                },
                {
                    "content": "I'll help you update the roadmap. What changes would you like to make?",
                    "role": "assistant",
                },
            ],
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
            link_to="string",
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
                            "via_relationship": [{}],
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
                            "via_relationship": [{}],
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
            relationships_json=[
                {
                    "relation_type": "updates",
                    "metadata": {"relevance": "bar"},
                    "related_item_id": "previous_memory_item_id",
                    "related_item_type": "TextMemoryItem",
                    "relationship_type": "previous_memory_item_id",
                }
            ],
            type="text",
        )
        assert_matches_type(MemoryUpdateResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Papr) -> None:
        response = client.memory.with_raw_response.update(
            memory_id="memory_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(MemoryUpdateResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Papr) -> None:
        with client.memory.with_streaming_response.update(
            memory_id="memory_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(MemoryUpdateResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Papr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_id` but received ''"):
            client.memory.with_raw_response.update(
                memory_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Papr) -> None:
        memory = client.memory.delete(
            memory_id="memory_id",
        )
        assert_matches_type(MemoryDeleteResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Papr) -> None:
        memory = client.memory.delete(
            memory_id="memory_id",
            skip_parse=True,
        )
        assert_matches_type(MemoryDeleteResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Papr) -> None:
        response = client.memory.with_raw_response.delete(
            memory_id="memory_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(MemoryDeleteResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Papr) -> None:
        with client.memory.with_streaming_response.delete(
            memory_id="memory_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(MemoryDeleteResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Papr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_id` but received ''"):
            client.memory.with_raw_response.delete(
                memory_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add(self, client: Papr) -> None:
        memory = client.memory.add(
            content="Meeting with John Smith from Acme Corp about the Q4 project timeline",
        )
        assert_matches_type(AddMemoryResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_with_all_params(self, client: Papr) -> None:
        memory = client.memory.add(
            content="Meeting with John Smith from Acme Corp about the Q4 project timeline",
            enable_holographic=True,
            format="format",
            skip_background_processing=True,
            context=[
                {
                    "content": "Let's discuss the Q4 project timeline with John",
                    "role": "user",
                },
                {
                    "content": "I'll help you prepare for the timeline discussion. What are your key milestones?",
                    "role": "assistant",
                },
            ],
            external_user_id="external_user_id",
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
            link_to="string",
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
                            "via_relationship": [{}],
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
                            "via_relationship": [{}],
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
                "conversation_id": "conv-123",
                "created_at": "2024-10-04T10:00:00Z",
                "custom_metadata": {"foo": "string"},
                "emoji_tags": ["string"],
                "emotion_tags": ["string"],
                "external_user_id": "external_user_123",
                "external_user_read_access": ["external_user_123", "external_user_789"],
                "external_user_write_access": ["external_user_123"],
                "goal_classification_scores": [0],
                "hierarchical_structures": "Business/Meetings/Project Planning",
                "location": "Conference Room A",
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
                "source_url": "https://calendar.example.com/meeting/123",
                "step_classification_scores": [0],
                "topics": ["product", "planning"],
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
            relationships_json=[
                {
                    "relation_type": "relation_type",
                    "metadata": {"foo": "bar"},
                    "related_item_id": "related_item_id",
                    "related_item_type": "related_item_type",
                    "relationship_type": "previous_memory_item_id",
                }
            ],
            type="text",
            user_id="user_id",
        )
        assert_matches_type(AddMemoryResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Papr) -> None:
        response = client.memory.with_raw_response.add(
            content="Meeting with John Smith from Acme Corp about the Q4 project timeline",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(AddMemoryResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Papr) -> None:
        with client.memory.with_streaming_response.add(
            content="Meeting with John Smith from Acme Corp about the Q4 project timeline",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(AddMemoryResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_batch(self, client: Papr) -> None:
        memory = client.memory.add_batch(
            memories=[
                {"content": "Meeting notes from the product planning session"},
                {"content": "Follow-up tasks from the planning meeting"},
            ],
        )
        assert_matches_type(BatchMemoryResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_batch_with_all_params(self, client: Papr) -> None:
        memory = client.memory.add_batch(
            memories=[
                {
                    "content": "Meeting notes from the product planning session",
                    "context": [
                        {
                            "content": "Let's discuss the Q4 project timeline with John",
                            "role": "user",
                        },
                        {
                            "content": "I'll help you prepare for the timeline discussion. What are your key milestones?",
                            "role": "assistant",
                        },
                    ],
                    "external_user_id": "external_user_id",
                    "graph_generation": {
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
                    "link_to": "string",
                    "memory_policy": {
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
                                    "via_relationship": [{}],
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
                                    "via_relationship": [{}],
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
                    "metadata": {
                        "acl": {"foo": ["string"]},
                        "assistant_message": "assistantMessage",
                        "category": "preference",
                        "consent": "consent",
                        "conversation_id": "conversationId",
                        "created_at": "2024-03-21T10:00:00Z",
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
                    "namespace_id": "namespace_id",
                    "organization_id": "organization_id",
                    "relationships_json": [
                        {
                            "relation_type": "relation_type",
                            "metadata": {"foo": "bar"},
                            "related_item_id": "related_item_id",
                            "related_item_type": "related_item_type",
                            "relationship_type": "previous_memory_item_id",
                        }
                    ],
                    "type": "text",
                    "user_id": "user_id",
                },
                {
                    "content": "Follow-up tasks from the planning meeting",
                    "context": [
                        {
                            "content": "Let's discuss the Q4 project timeline with John",
                            "role": "user",
                        },
                        {
                            "content": "I'll help you prepare for the timeline discussion. What are your key milestones?",
                            "role": "assistant",
                        },
                    ],
                    "external_user_id": "external_user_id",
                    "graph_generation": {
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
                    "link_to": "string",
                    "memory_policy": {
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
                                    "via_relationship": [{}],
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
                                    "via_relationship": [{}],
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
                    "metadata": {
                        "acl": {"foo": ["string"]},
                        "assistant_message": "assistantMessage",
                        "category": "preference",
                        "consent": "consent",
                        "conversation_id": "conversationId",
                        "created_at": "2024-03-21T11:00:00Z",
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
                    "namespace_id": "namespace_id",
                    "organization_id": "organization_id",
                    "relationships_json": [
                        {
                            "relation_type": "relation_type",
                            "metadata": {"foo": "bar"},
                            "related_item_id": "related_item_id",
                            "related_item_type": "related_item_type",
                            "relationship_type": "previous_memory_item_id",
                        }
                    ],
                    "type": "text",
                    "user_id": "user_id",
                },
            ],
            skip_background_processing=True,
            batch_size=10,
            external_user_id="external_user_abcde",
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
            link_to="string",
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
                            "via_relationship": [{}],
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
                            "via_relationship": [{}],
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
            namespace_id="namespace_id",
            organization_id="organization_id",
            user_id="internal_user_id_12345",
            webhook_secret="webhook_secret",
            webhook_url="webhook_url",
        )
        assert_matches_type(BatchMemoryResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add_batch(self, client: Papr) -> None:
        response = client.memory.with_raw_response.add_batch(
            memories=[
                {"content": "Meeting notes from the product planning session"},
                {"content": "Follow-up tasks from the planning meeting"},
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(BatchMemoryResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add_batch(self, client: Papr) -> None:
        with client.memory.with_streaming_response.add_batch(
            memories=[
                {"content": "Meeting notes from the product planning session"},
                {"content": "Follow-up tasks from the planning meeting"},
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(BatchMemoryResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_all(self, client: Papr) -> None:
        memory = client.memory.delete_all()
        assert_matches_type(BatchMemoryResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_all_with_all_params(self, client: Papr) -> None:
        memory = client.memory.delete_all(
            external_user_id="external_user_id",
            skip_parse=True,
            user_id="user_id",
        )
        assert_matches_type(BatchMemoryResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_all(self, client: Papr) -> None:
        response = client.memory.with_raw_response.delete_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(BatchMemoryResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_all(self, client: Papr) -> None:
        with client.memory.with_streaming_response.delete_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(BatchMemoryResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Papr) -> None:
        memory = client.memory.get(
            memory_id="memory_id",
        )
        assert_matches_type(SearchResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Papr) -> None:
        memory = client.memory.get(
            memory_id="memory_id",
            exclude_flagged=True,
            max_risk="max_risk",
            require_consent=True,
        )
        assert_matches_type(SearchResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Papr) -> None:
        response = client.memory.with_raw_response.get(
            memory_id="memory_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(SearchResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Papr) -> None:
        with client.memory.with_streaming_response.get(
            memory_id="memory_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(SearchResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Papr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_id` but received ''"):
            client.memory.with_raw_response.get(
                memory_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search(self, client: Papr) -> None:
        memory = client.memory.search(
            query="Find recurring customer complaints about API performance from the last month. Focus on issues that multiple customers have mentioned and any specific feature requests or workflow improvements they've suggested.",
        )
        assert_matches_type(SearchResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Papr) -> None:
        memory = client.memory.search(
            query="Find recurring customer complaints about API performance from the last month. Focus on issues that multiple customers have mentioned and any specific feature requests or workflow improvements they've suggested.",
            max_memories=10,
            max_nodes=10,
            response_format="json",
            enable_agentic_graph=False,
            external_user_id="external_user_123",
            holographic_config={
                "enabled": True,
                "hcond_boost_factor": 0.12,
                "hcond_boost_threshold": 0.35,
                "hcond_penalty_factor": 0.06,
                "search_mode": "post_search",
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
            omo_filter={
                "exclude_consent": ["none"],
                "exclude_flagged": True,
                "exclude_risk": ["flagged"],
                "max_risk": "sensitive",
                "min_consent": "implicit",
                "require_consent": True,
            },
            organization_id="organization_id",
            rank_results=True,
            reranking_config={
                "reranking_enabled": True,
                "reranking_model": "gpt-5-nano",
                "reranking_provider": "openai",
            },
            schema_id="schema_id",
            search_override={
                "pattern": {
                    "relationship_type": "ASSOCIATED_WITH",
                    "source_label": "Memory",
                    "target_label": "Person",
                    "direction": "->",
                },
                "filters": [
                    {
                        "node_type": "Person",
                        "operator": "CONTAINS",
                        "property_name": "name",
                        "value": "John",
                    },
                    {
                        "node_type": "Memory",
                        "operator": "IN",
                        "property_name": "topics",
                        "value": ["project", "meeting"],
                    },
                ],
                "return_properties": ["name", "content", "createdAt"],
            },
            user_id="user_id",
            accept_encoding="Accept-Encoding",
        )
        assert_matches_type(SearchResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Papr) -> None:
        response = client.memory.with_raw_response.search(
            query="Find recurring customer complaints about API performance from the last month. Focus on issues that multiple customers have mentioned and any specific feature requests or workflow improvements they've suggested.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(SearchResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Papr) -> None:
        with client.memory.with_streaming_response.search(
            query="Find recurring customer complaints about API performance from the last month. Focus on issues that multiple customers have mentioned and any specific feature requests or workflow improvements they've suggested.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(SearchResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMemory:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncPapr) -> None:
        memory = await async_client.memory.update(
            memory_id="memory_id",
        )
        assert_matches_type(MemoryUpdateResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPapr) -> None:
        memory = await async_client.memory.update(
            memory_id="memory_id",
            content="Updated meeting notes from the product planning session",
            context=[
                {
                    "content": "Let's update the Q2 product roadmap",
                    "role": "user",
                },
                {
                    "content": "I'll help you update the roadmap. What changes would you like to make?",
                    "role": "assistant",
                },
            ],
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
            link_to="string",
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
                            "via_relationship": [{}],
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
                            "via_relationship": [{}],
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
            relationships_json=[
                {
                    "relation_type": "updates",
                    "metadata": {"relevance": "bar"},
                    "related_item_id": "previous_memory_item_id",
                    "related_item_type": "TextMemoryItem",
                    "relationship_type": "previous_memory_item_id",
                }
            ],
            type="text",
        )
        assert_matches_type(MemoryUpdateResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPapr) -> None:
        response = await async_client.memory.with_raw_response.update(
            memory_id="memory_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(MemoryUpdateResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPapr) -> None:
        async with async_client.memory.with_streaming_response.update(
            memory_id="memory_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(MemoryUpdateResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncPapr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_id` but received ''"):
            await async_client.memory.with_raw_response.update(
                memory_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncPapr) -> None:
        memory = await async_client.memory.delete(
            memory_id="memory_id",
        )
        assert_matches_type(MemoryDeleteResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncPapr) -> None:
        memory = await async_client.memory.delete(
            memory_id="memory_id",
            skip_parse=True,
        )
        assert_matches_type(MemoryDeleteResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPapr) -> None:
        response = await async_client.memory.with_raw_response.delete(
            memory_id="memory_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(MemoryDeleteResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPapr) -> None:
        async with async_client.memory.with_streaming_response.delete(
            memory_id="memory_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(MemoryDeleteResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPapr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_id` but received ''"):
            await async_client.memory.with_raw_response.delete(
                memory_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncPapr) -> None:
        memory = await async_client.memory.add(
            content="Meeting with John Smith from Acme Corp about the Q4 project timeline",
        )
        assert_matches_type(AddMemoryResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncPapr) -> None:
        memory = await async_client.memory.add(
            content="Meeting with John Smith from Acme Corp about the Q4 project timeline",
            enable_holographic=True,
            format="format",
            skip_background_processing=True,
            context=[
                {
                    "content": "Let's discuss the Q4 project timeline with John",
                    "role": "user",
                },
                {
                    "content": "I'll help you prepare for the timeline discussion. What are your key milestones?",
                    "role": "assistant",
                },
            ],
            external_user_id="external_user_id",
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
            link_to="string",
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
                            "via_relationship": [{}],
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
                            "via_relationship": [{}],
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
                "conversation_id": "conv-123",
                "created_at": "2024-10-04T10:00:00Z",
                "custom_metadata": {"foo": "string"},
                "emoji_tags": ["string"],
                "emotion_tags": ["string"],
                "external_user_id": "external_user_123",
                "external_user_read_access": ["external_user_123", "external_user_789"],
                "external_user_write_access": ["external_user_123"],
                "goal_classification_scores": [0],
                "hierarchical_structures": "Business/Meetings/Project Planning",
                "location": "Conference Room A",
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
                "source_url": "https://calendar.example.com/meeting/123",
                "step_classification_scores": [0],
                "topics": ["product", "planning"],
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
            relationships_json=[
                {
                    "relation_type": "relation_type",
                    "metadata": {"foo": "bar"},
                    "related_item_id": "related_item_id",
                    "related_item_type": "related_item_type",
                    "relationship_type": "previous_memory_item_id",
                }
            ],
            type="text",
            user_id="user_id",
        )
        assert_matches_type(AddMemoryResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncPapr) -> None:
        response = await async_client.memory.with_raw_response.add(
            content="Meeting with John Smith from Acme Corp about the Q4 project timeline",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(AddMemoryResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncPapr) -> None:
        async with async_client.memory.with_streaming_response.add(
            content="Meeting with John Smith from Acme Corp about the Q4 project timeline",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(AddMemoryResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_batch(self, async_client: AsyncPapr) -> None:
        memory = await async_client.memory.add_batch(
            memories=[
                {"content": "Meeting notes from the product planning session"},
                {"content": "Follow-up tasks from the planning meeting"},
            ],
        )
        assert_matches_type(BatchMemoryResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_batch_with_all_params(self, async_client: AsyncPapr) -> None:
        memory = await async_client.memory.add_batch(
            memories=[
                {
                    "content": "Meeting notes from the product planning session",
                    "context": [
                        {
                            "content": "Let's discuss the Q4 project timeline with John",
                            "role": "user",
                        },
                        {
                            "content": "I'll help you prepare for the timeline discussion. What are your key milestones?",
                            "role": "assistant",
                        },
                    ],
                    "external_user_id": "external_user_id",
                    "graph_generation": {
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
                    "link_to": "string",
                    "memory_policy": {
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
                                    "via_relationship": [{}],
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
                                    "via_relationship": [{}],
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
                    "metadata": {
                        "acl": {"foo": ["string"]},
                        "assistant_message": "assistantMessage",
                        "category": "preference",
                        "consent": "consent",
                        "conversation_id": "conversationId",
                        "created_at": "2024-03-21T10:00:00Z",
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
                    "namespace_id": "namespace_id",
                    "organization_id": "organization_id",
                    "relationships_json": [
                        {
                            "relation_type": "relation_type",
                            "metadata": {"foo": "bar"},
                            "related_item_id": "related_item_id",
                            "related_item_type": "related_item_type",
                            "relationship_type": "previous_memory_item_id",
                        }
                    ],
                    "type": "text",
                    "user_id": "user_id",
                },
                {
                    "content": "Follow-up tasks from the planning meeting",
                    "context": [
                        {
                            "content": "Let's discuss the Q4 project timeline with John",
                            "role": "user",
                        },
                        {
                            "content": "I'll help you prepare for the timeline discussion. What are your key milestones?",
                            "role": "assistant",
                        },
                    ],
                    "external_user_id": "external_user_id",
                    "graph_generation": {
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
                    "link_to": "string",
                    "memory_policy": {
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
                                    "via_relationship": [{}],
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
                                    "via_relationship": [{}],
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
                    "metadata": {
                        "acl": {"foo": ["string"]},
                        "assistant_message": "assistantMessage",
                        "category": "preference",
                        "consent": "consent",
                        "conversation_id": "conversationId",
                        "created_at": "2024-03-21T11:00:00Z",
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
                    "namespace_id": "namespace_id",
                    "organization_id": "organization_id",
                    "relationships_json": [
                        {
                            "relation_type": "relation_type",
                            "metadata": {"foo": "bar"},
                            "related_item_id": "related_item_id",
                            "related_item_type": "related_item_type",
                            "relationship_type": "previous_memory_item_id",
                        }
                    ],
                    "type": "text",
                    "user_id": "user_id",
                },
            ],
            skip_background_processing=True,
            batch_size=10,
            external_user_id="external_user_abcde",
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
            link_to="string",
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
                            "via_relationship": [{}],
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
                            "via_relationship": [{}],
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
            namespace_id="namespace_id",
            organization_id="organization_id",
            user_id="internal_user_id_12345",
            webhook_secret="webhook_secret",
            webhook_url="webhook_url",
        )
        assert_matches_type(BatchMemoryResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add_batch(self, async_client: AsyncPapr) -> None:
        response = await async_client.memory.with_raw_response.add_batch(
            memories=[
                {"content": "Meeting notes from the product planning session"},
                {"content": "Follow-up tasks from the planning meeting"},
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(BatchMemoryResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add_batch(self, async_client: AsyncPapr) -> None:
        async with async_client.memory.with_streaming_response.add_batch(
            memories=[
                {"content": "Meeting notes from the product planning session"},
                {"content": "Follow-up tasks from the planning meeting"},
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(BatchMemoryResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_all(self, async_client: AsyncPapr) -> None:
        memory = await async_client.memory.delete_all()
        assert_matches_type(BatchMemoryResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_all_with_all_params(self, async_client: AsyncPapr) -> None:
        memory = await async_client.memory.delete_all(
            external_user_id="external_user_id",
            skip_parse=True,
            user_id="user_id",
        )
        assert_matches_type(BatchMemoryResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_all(self, async_client: AsyncPapr) -> None:
        response = await async_client.memory.with_raw_response.delete_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(BatchMemoryResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_all(self, async_client: AsyncPapr) -> None:
        async with async_client.memory.with_streaming_response.delete_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(BatchMemoryResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncPapr) -> None:
        memory = await async_client.memory.get(
            memory_id="memory_id",
        )
        assert_matches_type(SearchResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncPapr) -> None:
        memory = await async_client.memory.get(
            memory_id="memory_id",
            exclude_flagged=True,
            max_risk="max_risk",
            require_consent=True,
        )
        assert_matches_type(SearchResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPapr) -> None:
        response = await async_client.memory.with_raw_response.get(
            memory_id="memory_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(SearchResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPapr) -> None:
        async with async_client.memory.with_streaming_response.get(
            memory_id="memory_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(SearchResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncPapr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_id` but received ''"):
            await async_client.memory.with_raw_response.get(
                memory_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncPapr) -> None:
        memory = await async_client.memory.search(
            query="Find recurring customer complaints about API performance from the last month. Focus on issues that multiple customers have mentioned and any specific feature requests or workflow improvements they've suggested.",
        )
        assert_matches_type(SearchResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncPapr) -> None:
        memory = await async_client.memory.search(
            query="Find recurring customer complaints about API performance from the last month. Focus on issues that multiple customers have mentioned and any specific feature requests or workflow improvements they've suggested.",
            max_memories=10,
            max_nodes=10,
            response_format="json",
            enable_agentic_graph=False,
            external_user_id="external_user_123",
            holographic_config={
                "enabled": True,
                "hcond_boost_factor": 0.12,
                "hcond_boost_threshold": 0.35,
                "hcond_penalty_factor": 0.06,
                "search_mode": "post_search",
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
            omo_filter={
                "exclude_consent": ["none"],
                "exclude_flagged": True,
                "exclude_risk": ["flagged"],
                "max_risk": "sensitive",
                "min_consent": "implicit",
                "require_consent": True,
            },
            organization_id="organization_id",
            rank_results=True,
            reranking_config={
                "reranking_enabled": True,
                "reranking_model": "gpt-5-nano",
                "reranking_provider": "openai",
            },
            schema_id="schema_id",
            search_override={
                "pattern": {
                    "relationship_type": "ASSOCIATED_WITH",
                    "source_label": "Memory",
                    "target_label": "Person",
                    "direction": "->",
                },
                "filters": [
                    {
                        "node_type": "Person",
                        "operator": "CONTAINS",
                        "property_name": "name",
                        "value": "John",
                    },
                    {
                        "node_type": "Memory",
                        "operator": "IN",
                        "property_name": "topics",
                        "value": ["project", "meeting"],
                    },
                ],
                "return_properties": ["name", "content", "createdAt"],
            },
            user_id="user_id",
            accept_encoding="Accept-Encoding",
        )
        assert_matches_type(SearchResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncPapr) -> None:
        response = await async_client.memory.with_raw_response.search(
            query="Find recurring customer complaints about API performance from the last month. Focus on issues that multiple customers have mentioned and any specific feature requests or workflow improvements they've suggested.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(SearchResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncPapr) -> None:
        async with async_client.memory.with_streaming_response.search(
            query="Find recurring customer complaints about API performance from the last month. Focus on issues that multiple customers have mentioned and any specific feature requests or workflow improvements they've suggested.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(SearchResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True
