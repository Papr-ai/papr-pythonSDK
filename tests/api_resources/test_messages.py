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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_store(self, client: Papr) -> None:
        message = client.messages.store(
            content="string",
            role="user",
            session_id="sessionId",
        )
        assert_matches_type(MessageStoreResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_store_with_all_params(self, client: Papr) -> None:
        message = client.messages.store(
            content="string",
            role="user",
            session_id="sessionId",
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
                "organization_id": "organization_id",
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
            process_messages=True,
        )
        assert_matches_type(MessageStoreResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_store(self, async_client: AsyncPapr) -> None:
        message = await async_client.messages.store(
            content="string",
            role="user",
            session_id="sessionId",
        )
        assert_matches_type(MessageStoreResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_store_with_all_params(self, async_client: AsyncPapr) -> None:
        message = await async_client.messages.store(
            content="string",
            role="user",
            session_id="sessionId",
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
                "organization_id": "organization_id",
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
            process_messages=True,
        )
        assert_matches_type(MessageStoreResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
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
