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
            metadata={
                "assistant_message": "assistantMessage",
                "category": "preference",
                "conversation_id": "conversationId",
                "created_at": "createdAt",
                "custom_metadata": {"foo": "string"},
                "emoji_tags": ["string"],
                "emotion_tags": ["string"],
                "external_user_id": "external_user_id",
                "external_user_read_access": ["string"],
                "external_user_write_access": ["string"],
                "goal_classification_scores": [0],
                "hierarchical_structures": "hierarchical_structures",
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
                    "simple_schema_mode": True,
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
            metadata={
                "assistant_message": "assistantMessage",
                "category": "preference",
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
                            "simple_schema_mode": True,
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
                    "metadata": {
                        "assistant_message": "assistantMessage",
                        "category": "preference",
                        "conversation_id": "conversationId",
                        "created_at": "2024-03-21T10:00:00Z",
                        "custom_metadata": {"foo": "string"},
                        "emoji_tags": ["string"],
                        "emotion_tags": ["string"],
                        "external_user_id": "external_user_id",
                        "external_user_read_access": ["string"],
                        "external_user_write_access": ["string"],
                        "goal_classification_scores": [0],
                        "hierarchical_structures": "hierarchical_structures",
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
                            "simple_schema_mode": True,
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
                    "metadata": {
                        "assistant_message": "assistantMessage",
                        "category": "preference",
                        "conversation_id": "conversationId",
                        "created_at": "2024-03-21T11:00:00Z",
                        "custom_metadata": {"foo": "string"},
                        "emoji_tags": ["string"],
                        "emotion_tags": ["string"],
                        "external_user_id": "external_user_id",
                        "external_user_read_access": ["string"],
                        "external_user_write_access": ["string"],
                        "goal_classification_scores": [0],
                        "hierarchical_structures": "hierarchical_structures",
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
                    "simple_schema_mode": True,
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
            "memory_id",
        )
        assert_matches_type(SearchResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Papr) -> None:
        response = client.memory.with_raw_response.get(
            "memory_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(SearchResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Papr) -> None:
        with client.memory.with_streaming_response.get(
            "memory_id",
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
                "",
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
            metadata={
                "assistant_message": "assistantMessage",
                "category": "preference",
                "conversation_id": "conversationId",
                "created_at": "createdAt",
                "custom_metadata": {"foo": "string"},
                "emoji_tags": ["string"],
                "emotion_tags": ["string"],
                "external_user_id": "external_user_id",
                "external_user_read_access": ["string"],
                "external_user_write_access": ["string"],
                "goal_classification_scores": [0],
                "hierarchical_structures": "hierarchical_structures",
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
            rank_results=True,
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
            simple_schema_mode=True,
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
            metadata={
                "assistant_message": "assistantMessage",
                "category": "preference",
                "conversation_id": "conversationId",
                "created_at": "createdAt",
                "custom_metadata": {"foo": "string"},
                "emoji_tags": ["string"],
                "emotion_tags": ["string"],
                "external_user_id": "external_user_id",
                "external_user_read_access": ["string"],
                "external_user_write_access": ["string"],
                "goal_classification_scores": [0],
                "hierarchical_structures": "hierarchical_structures",
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
                    "simple_schema_mode": True,
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
            metadata={
                "assistant_message": "assistantMessage",
                "category": "preference",
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
                            "simple_schema_mode": True,
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
                    "metadata": {
                        "assistant_message": "assistantMessage",
                        "category": "preference",
                        "conversation_id": "conversationId",
                        "created_at": "2024-03-21T10:00:00Z",
                        "custom_metadata": {"foo": "string"},
                        "emoji_tags": ["string"],
                        "emotion_tags": ["string"],
                        "external_user_id": "external_user_id",
                        "external_user_read_access": ["string"],
                        "external_user_write_access": ["string"],
                        "goal_classification_scores": [0],
                        "hierarchical_structures": "hierarchical_structures",
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
                            "simple_schema_mode": True,
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
                    "metadata": {
                        "assistant_message": "assistantMessage",
                        "category": "preference",
                        "conversation_id": "conversationId",
                        "created_at": "2024-03-21T11:00:00Z",
                        "custom_metadata": {"foo": "string"},
                        "emoji_tags": ["string"],
                        "emotion_tags": ["string"],
                        "external_user_id": "external_user_id",
                        "external_user_read_access": ["string"],
                        "external_user_write_access": ["string"],
                        "goal_classification_scores": [0],
                        "hierarchical_structures": "hierarchical_structures",
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
                    "simple_schema_mode": True,
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
            "memory_id",
        )
        assert_matches_type(SearchResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPapr) -> None:
        response = await async_client.memory.with_raw_response.get(
            "memory_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(SearchResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPapr) -> None:
        async with async_client.memory.with_streaming_response.get(
            "memory_id",
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
                "",
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
            metadata={
                "assistant_message": "assistantMessage",
                "category": "preference",
                "conversation_id": "conversationId",
                "created_at": "createdAt",
                "custom_metadata": {"foo": "string"},
                "emoji_tags": ["string"],
                "emotion_tags": ["string"],
                "external_user_id": "external_user_id",
                "external_user_read_access": ["string"],
                "external_user_write_access": ["string"],
                "goal_classification_scores": [0],
                "hierarchical_structures": "hierarchical_structures",
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
            rank_results=True,
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
            simple_schema_mode=True,
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
