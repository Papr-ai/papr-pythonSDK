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
    MemoryDeleteResponse,
    MemoryUpdateResponse,
    MemoryAddBatchResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMemory:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Papr) -> None:
        memory = client.memory.update(
            memory_id="memory_id",
        )
        assert_matches_type(MemoryUpdateResponse, memory, path=["response"])

    @pytest.mark.skip()
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
                "conversation_id": "conversationId",
                "created_at": "createdAt",
                "emoji_tags": "📊,💡,📝,✨",
                "emotion_tags": "focused, productive, satisfied",
                "hierarchical_structures": "hierarchical_structures",
                "location": "location",
                "role_read_access": ["string"],
                "role_write_access": ["string"],
                "source_url": "sourceUrl",
                "topics": "product, planning, updates",
                "user_id": "user_id",
                "user_read_access": ["string"],
                "user_write_access": ["string"],
                "workspace_read_access": ["string"],
                "workspace_write_access": ["string"],
            },
            relationships_json=[
                {
                    "related_item_id": "previous_memory_item_id",
                    "related_item_type": "TextMemoryItem",
                    "relation_type": "updates",
                    "metadata": {"relevance": "high"},
                }
            ],
            type="text",
        )
        assert_matches_type(MemoryUpdateResponse, memory, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Papr) -> None:
        response = client.memory.with_raw_response.update(
            memory_id="memory_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(MemoryUpdateResponse, memory, path=["response"])

    @pytest.mark.skip()
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

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Papr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_id` but received ''"):
            client.memory.with_raw_response.update(
                memory_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Papr) -> None:
        memory = client.memory.delete(
            memory_id="memory_id",
        )
        assert_matches_type(MemoryDeleteResponse, memory, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Papr) -> None:
        memory = client.memory.delete(
            memory_id="memory_id",
            skip_parse=True,
        )
        assert_matches_type(MemoryDeleteResponse, memory, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Papr) -> None:
        response = client.memory.with_raw_response.delete(
            memory_id="memory_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(MemoryDeleteResponse, memory, path=["response"])

    @pytest.mark.skip()
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

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Papr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_id` but received ''"):
            client.memory.with_raw_response.delete(
                memory_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_add(self, client: Papr) -> None:
        memory = client.memory.add(
            content="Meeting notes from the product planning session",
        )
        assert_matches_type(AddMemoryResponse, memory, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_with_all_params(self, client: Papr) -> None:
        memory = client.memory.add(
            content="Meeting notes from the product planning session",
            skip_background_processing=True,
            context=[
                {
                    "content": "Let's discuss the Q2 product roadmap",
                    "role": "user",
                },
                {
                    "content": "I'll help you plan the roadmap. What are your key objectives?",
                    "role": "assistant",
                },
            ],
            metadata={
                "conversation_id": "conv-123",
                "created_at": "2024-03-21T10:00:00Z",
                "emoji_tags": "📊,💡,📝",
                "emotion_tags": "focused, productive",
                "hierarchical_structures": "hierarchical_structures",
                "location": "Conference Room A",
                "role_read_access": ["string"],
                "role_write_access": ["string"],
                "source_url": "https://meeting-notes.example.com/123",
                "topics": "product, planning",
                "user_id": "user_id",
                "user_read_access": ["string"],
                "user_write_access": ["string"],
                "workspace_read_access": ["string"],
                "workspace_write_access": ["string"],
            },
            relationships_json=[
                {
                    "related_item_id": "previous_memory_item_id",
                    "related_item_type": "TextMemoryItem",
                    "relation_type": "follows",
                    "metadata": {"relevance": "high"},
                }
            ],
            type="text",
        )
        assert_matches_type(AddMemoryResponse, memory, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add(self, client: Papr) -> None:
        response = client.memory.with_raw_response.add(
            content="Meeting notes from the product planning session",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(AddMemoryResponse, memory, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add(self, client: Papr) -> None:
        with client.memory.with_streaming_response.add(
            content="Meeting notes from the product planning session",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(AddMemoryResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add_batch(self, client: Papr) -> None:
        memory = client.memory.add_batch(
            memories=[
                {"content": "Meeting notes from the product planning session"},
                {"content": "Follow-up tasks from the planning meeting"},
            ],
        )
        assert_matches_type(MemoryAddBatchResponse, memory, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_batch_with_all_params(self, client: Papr) -> None:
        memory = client.memory.add_batch(
            memories=[
                {
                    "content": "Meeting notes from the product planning session",
                    "context": [
                        {
                            "content": "content",
                            "role": "user",
                        }
                    ],
                    "metadata": {
                        "conversation_id": "conversationId",
                        "created_at": "2024-03-21T10:00:00Z",
                        "emoji_tags": "📊,💡,📝",
                        "emotion_tags": "focused, productive",
                        "hierarchical_structures": "hierarchical_structures",
                        "location": "location",
                        "role_read_access": ["string"],
                        "role_write_access": ["string"],
                        "source_url": "sourceUrl",
                        "topics": "product, planning",
                        "user_id": "user_id",
                        "user_read_access": ["string"],
                        "user_write_access": ["string"],
                        "workspace_read_access": ["string"],
                        "workspace_write_access": ["string"],
                    },
                    "relationships_json": [
                        {
                            "related_item_id": "TextMemoryItem",
                            "related_item_type": "TextMemoryItem",
                            "relation_type": "relation_type",
                            "metadata": {},
                        }
                    ],
                    "type": "text",
                },
                {
                    "content": "Follow-up tasks from the planning meeting",
                    "context": [
                        {
                            "content": "content",
                            "role": "user",
                        }
                    ],
                    "metadata": {
                        "conversation_id": "conversationId",
                        "created_at": "2024-03-21T11:00:00Z",
                        "emoji_tags": "✅,📋",
                        "emotion_tags": "organized",
                        "hierarchical_structures": "hierarchical_structures",
                        "location": "location",
                        "role_read_access": ["string"],
                        "role_write_access": ["string"],
                        "source_url": "sourceUrl",
                        "topics": "tasks, planning",
                        "user_id": "user_id",
                        "user_read_access": ["string"],
                        "user_write_access": ["string"],
                        "workspace_read_access": ["string"],
                        "workspace_write_access": ["string"],
                    },
                    "relationships_json": [
                        {
                            "related_item_id": "TextMemoryItem",
                            "related_item_type": "TextMemoryItem",
                            "relation_type": "relation_type",
                            "metadata": {},
                        }
                    ],
                    "type": "text",
                },
            ],
            skip_background_processing=True,
            batch_size=10,
        )
        assert_matches_type(MemoryAddBatchResponse, memory, path=["response"])

    @pytest.mark.skip()
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
        assert_matches_type(MemoryAddBatchResponse, memory, path=["response"])

    @pytest.mark.skip()
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
            assert_matches_type(MemoryAddBatchResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Papr) -> None:
        memory = client.memory.get(
            "memory_id",
        )
        assert_matches_type(SearchResponse, memory, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Papr) -> None:
        response = client.memory.with_raw_response.get(
            "memory_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(SearchResponse, memory, path=["response"])

    @pytest.mark.skip()
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

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Papr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_id` but received ''"):
            client.memory.with_raw_response.get(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_search(self, client: Papr) -> None:
        memory = client.memory.search(
            query="Find recurring customer complaints about API performance from the last month. Focus on issues where customers specifically mentioned timeout errors or slow response times in their conversations.",
        )
        assert_matches_type(SearchResponse, memory, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_search_with_all_params(self, client: Papr) -> None:
        memory = client.memory.search(
            query="Find recurring customer complaints about API performance from the last month. Focus on issues where customers specifically mentioned timeout errors or slow response times in their conversations.",
            max_memories=1,
            max_nodes=1,
            rank_results=True,
            user_id="user123",
            accept_encoding="Accept-Encoding",
        )
        assert_matches_type(SearchResponse, memory, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_search(self, client: Papr) -> None:
        response = client.memory.with_raw_response.search(
            query="Find recurring customer complaints about API performance from the last month. Focus on issues where customers specifically mentioned timeout errors or slow response times in their conversations.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(SearchResponse, memory, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_search(self, client: Papr) -> None:
        with client.memory.with_streaming_response.search(
            query="Find recurring customer complaints about API performance from the last month. Focus on issues where customers specifically mentioned timeout errors or slow response times in their conversations.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(SearchResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMemory:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncPapr) -> None:
        memory = await async_client.memory.update(
            memory_id="memory_id",
        )
        assert_matches_type(MemoryUpdateResponse, memory, path=["response"])

    @pytest.mark.skip()
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
                "conversation_id": "conversationId",
                "created_at": "createdAt",
                "emoji_tags": "📊,💡,📝,✨",
                "emotion_tags": "focused, productive, satisfied",
                "hierarchical_structures": "hierarchical_structures",
                "location": "location",
                "role_read_access": ["string"],
                "role_write_access": ["string"],
                "source_url": "sourceUrl",
                "topics": "product, planning, updates",
                "user_id": "user_id",
                "user_read_access": ["string"],
                "user_write_access": ["string"],
                "workspace_read_access": ["string"],
                "workspace_write_access": ["string"],
            },
            relationships_json=[
                {
                    "related_item_id": "previous_memory_item_id",
                    "related_item_type": "TextMemoryItem",
                    "relation_type": "updates",
                    "metadata": {"relevance": "high"},
                }
            ],
            type="text",
        )
        assert_matches_type(MemoryUpdateResponse, memory, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPapr) -> None:
        response = await async_client.memory.with_raw_response.update(
            memory_id="memory_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(MemoryUpdateResponse, memory, path=["response"])

    @pytest.mark.skip()
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

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncPapr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_id` but received ''"):
            await async_client.memory.with_raw_response.update(
                memory_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncPapr) -> None:
        memory = await async_client.memory.delete(
            memory_id="memory_id",
        )
        assert_matches_type(MemoryDeleteResponse, memory, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncPapr) -> None:
        memory = await async_client.memory.delete(
            memory_id="memory_id",
            skip_parse=True,
        )
        assert_matches_type(MemoryDeleteResponse, memory, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPapr) -> None:
        response = await async_client.memory.with_raw_response.delete(
            memory_id="memory_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(MemoryDeleteResponse, memory, path=["response"])

    @pytest.mark.skip()
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

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPapr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_id` but received ''"):
            await async_client.memory.with_raw_response.delete(
                memory_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_add(self, async_client: AsyncPapr) -> None:
        memory = await async_client.memory.add(
            content="Meeting notes from the product planning session",
        )
        assert_matches_type(AddMemoryResponse, memory, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncPapr) -> None:
        memory = await async_client.memory.add(
            content="Meeting notes from the product planning session",
            skip_background_processing=True,
            context=[
                {
                    "content": "Let's discuss the Q2 product roadmap",
                    "role": "user",
                },
                {
                    "content": "I'll help you plan the roadmap. What are your key objectives?",
                    "role": "assistant",
                },
            ],
            metadata={
                "conversation_id": "conv-123",
                "created_at": "2024-03-21T10:00:00Z",
                "emoji_tags": "📊,💡,📝",
                "emotion_tags": "focused, productive",
                "hierarchical_structures": "hierarchical_structures",
                "location": "Conference Room A",
                "role_read_access": ["string"],
                "role_write_access": ["string"],
                "source_url": "https://meeting-notes.example.com/123",
                "topics": "product, planning",
                "user_id": "user_id",
                "user_read_access": ["string"],
                "user_write_access": ["string"],
                "workspace_read_access": ["string"],
                "workspace_write_access": ["string"],
            },
            relationships_json=[
                {
                    "related_item_id": "previous_memory_item_id",
                    "related_item_type": "TextMemoryItem",
                    "relation_type": "follows",
                    "metadata": {"relevance": "high"},
                }
            ],
            type="text",
        )
        assert_matches_type(AddMemoryResponse, memory, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncPapr) -> None:
        response = await async_client.memory.with_raw_response.add(
            content="Meeting notes from the product planning session",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(AddMemoryResponse, memory, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncPapr) -> None:
        async with async_client.memory.with_streaming_response.add(
            content="Meeting notes from the product planning session",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(AddMemoryResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_batch(self, async_client: AsyncPapr) -> None:
        memory = await async_client.memory.add_batch(
            memories=[
                {"content": "Meeting notes from the product planning session"},
                {"content": "Follow-up tasks from the planning meeting"},
            ],
        )
        assert_matches_type(MemoryAddBatchResponse, memory, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_batch_with_all_params(self, async_client: AsyncPapr) -> None:
        memory = await async_client.memory.add_batch(
            memories=[
                {
                    "content": "Meeting notes from the product planning session",
                    "context": [
                        {
                            "content": "content",
                            "role": "user",
                        }
                    ],
                    "metadata": {
                        "conversation_id": "conversationId",
                        "created_at": "2024-03-21T10:00:00Z",
                        "emoji_tags": "📊,💡,📝",
                        "emotion_tags": "focused, productive",
                        "hierarchical_structures": "hierarchical_structures",
                        "location": "location",
                        "role_read_access": ["string"],
                        "role_write_access": ["string"],
                        "source_url": "sourceUrl",
                        "topics": "product, planning",
                        "user_id": "user_id",
                        "user_read_access": ["string"],
                        "user_write_access": ["string"],
                        "workspace_read_access": ["string"],
                        "workspace_write_access": ["string"],
                    },
                    "relationships_json": [
                        {
                            "related_item_id": "TextMemoryItem",
                            "related_item_type": "TextMemoryItem",
                            "relation_type": "relation_type",
                            "metadata": {},
                        }
                    ],
                    "type": "text",
                },
                {
                    "content": "Follow-up tasks from the planning meeting",
                    "context": [
                        {
                            "content": "content",
                            "role": "user",
                        }
                    ],
                    "metadata": {
                        "conversation_id": "conversationId",
                        "created_at": "2024-03-21T11:00:00Z",
                        "emoji_tags": "✅,📋",
                        "emotion_tags": "organized",
                        "hierarchical_structures": "hierarchical_structures",
                        "location": "location",
                        "role_read_access": ["string"],
                        "role_write_access": ["string"],
                        "source_url": "sourceUrl",
                        "topics": "tasks, planning",
                        "user_id": "user_id",
                        "user_read_access": ["string"],
                        "user_write_access": ["string"],
                        "workspace_read_access": ["string"],
                        "workspace_write_access": ["string"],
                    },
                    "relationships_json": [
                        {
                            "related_item_id": "TextMemoryItem",
                            "related_item_type": "TextMemoryItem",
                            "relation_type": "relation_type",
                            "metadata": {},
                        }
                    ],
                    "type": "text",
                },
            ],
            skip_background_processing=True,
            batch_size=10,
        )
        assert_matches_type(MemoryAddBatchResponse, memory, path=["response"])

    @pytest.mark.skip()
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
        assert_matches_type(MemoryAddBatchResponse, memory, path=["response"])

    @pytest.mark.skip()
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
            assert_matches_type(MemoryAddBatchResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncPapr) -> None:
        memory = await async_client.memory.get(
            "memory_id",
        )
        assert_matches_type(SearchResponse, memory, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPapr) -> None:
        response = await async_client.memory.with_raw_response.get(
            "memory_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(SearchResponse, memory, path=["response"])

    @pytest.mark.skip()
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

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncPapr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_id` but received ''"):
            await async_client.memory.with_raw_response.get(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_search(self, async_client: AsyncPapr) -> None:
        memory = await async_client.memory.search(
            query="Find recurring customer complaints about API performance from the last month. Focus on issues where customers specifically mentioned timeout errors or slow response times in their conversations.",
        )
        assert_matches_type(SearchResponse, memory, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncPapr) -> None:
        memory = await async_client.memory.search(
            query="Find recurring customer complaints about API performance from the last month. Focus on issues where customers specifically mentioned timeout errors or slow response times in their conversations.",
            max_memories=1,
            max_nodes=1,
            rank_results=True,
            user_id="user123",
            accept_encoding="Accept-Encoding",
        )
        assert_matches_type(SearchResponse, memory, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncPapr) -> None:
        response = await async_client.memory.with_raw_response.search(
            query="Find recurring customer complaints about API performance from the last month. Focus on issues where customers specifically mentioned timeout errors or slow response times in their conversations.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(SearchResponse, memory, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncPapr) -> None:
        async with async_client.memory.with_streaming_response.search(
            query="Find recurring customer complaints about API performance from the last month. Focus on issues where customers specifically mentioned timeout errors or slow response times in their conversations.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(SearchResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True
