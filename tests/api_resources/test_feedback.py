# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from papr_memory import Papr, AsyncPapr
from tests.utils import assert_matches_type
from papr_memory.types import BatchResponse, FeedbackResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFeedback:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_by_id(self, client: Papr) -> None:
        feedback = client.feedback.get_by_id(
            "feedback_id",
        )
        assert_matches_type(FeedbackResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_by_id(self, client: Papr) -> None:
        response = client.feedback.with_raw_response.get_by_id(
            "feedback_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = response.parse()
        assert_matches_type(FeedbackResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_by_id(self, client: Papr) -> None:
        with client.feedback.with_streaming_response.get_by_id(
            "feedback_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = response.parse()
            assert_matches_type(FeedbackResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_by_id(self, client: Papr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feedback_id` but received ''"):
            client.feedback.with_raw_response.get_by_id(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit(self, client: Papr) -> None:
        feedback = client.feedback.submit(
            feedback_data={
                "feedback_source": "inline",
                "feedback_type": "thumbs_up",
            },
            search_id="abc123def456",
        )
        assert_matches_type(FeedbackResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit_with_all_params(self, client: Papr) -> None:
        feedback = client.feedback.submit(
            feedback_data={
                "feedback_source": "inline",
                "feedback_type": "thumbs_up",
                "assistant_message": {
                    "class_name": "PostMessage",
                    "object_id": "abc123def456",
                    "_type": "Pointer",
                },
                "cited_memory_ids": ["mem_123", "mem_456"],
                "cited_node_ids": ["node_123", "node_456"],
                "feedback_impact": "positive",
                "feedback_processed": True,
                "feedback_score": 1,
                "feedback_text": "This answer was very helpful and accurate",
                "feedback_value": "helpful",
                "user_message": {
                    "class_name": "PostMessage",
                    "object_id": "abc123def456",
                    "_type": "Pointer",
                },
            },
            search_id="abc123def456",
            external_user_id="dev_api_key_123",
            user_id="abc123def456",
        )
        assert_matches_type(FeedbackResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_submit(self, client: Papr) -> None:
        response = client.feedback.with_raw_response.submit(
            feedback_data={
                "feedback_source": "inline",
                "feedback_type": "thumbs_up",
            },
            search_id="abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = response.parse()
        assert_matches_type(FeedbackResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_submit(self, client: Papr) -> None:
        with client.feedback.with_streaming_response.submit(
            feedback_data={
                "feedback_source": "inline",
                "feedback_type": "thumbs_up",
            },
            search_id="abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = response.parse()
            assert_matches_type(FeedbackResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit_batch(self, client: Papr) -> None:
        feedback = client.feedback.submit_batch(
            feedback_items=[
                {
                    "feedback_data": {
                        "feedback_source": "inline",
                        "feedback_type": "thumbs_up",
                    },
                    "search_id": "abc123def456",
                }
            ],
        )
        assert_matches_type(BatchResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit_batch_with_all_params(self, client: Papr) -> None:
        feedback = client.feedback.submit_batch(
            feedback_items=[
                {
                    "feedback_data": {
                        "feedback_source": "inline",
                        "feedback_type": "thumbs_up",
                        "assistant_message": {
                            "class_name": "PostMessage",
                            "object_id": "abc123def456",
                            "_type": "Pointer",
                        },
                        "cited_memory_ids": ["mem_123", "mem_456"],
                        "cited_node_ids": ["node_123", "node_456"],
                        "feedback_impact": "positive",
                        "feedback_processed": True,
                        "feedback_score": 1,
                        "feedback_text": "This answer was very helpful and accurate",
                        "feedback_value": "helpful",
                        "user_message": {
                            "class_name": "PostMessage",
                            "object_id": "abc123def456",
                            "_type": "Pointer",
                        },
                    },
                    "search_id": "abc123def456",
                    "external_user_id": "dev_api_key_123",
                    "user_id": "abc123def456",
                }
            ],
            session_context={"foo": "bar"},
        )
        assert_matches_type(BatchResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_submit_batch(self, client: Papr) -> None:
        response = client.feedback.with_raw_response.submit_batch(
            feedback_items=[
                {
                    "feedback_data": {
                        "feedback_source": "inline",
                        "feedback_type": "thumbs_up",
                    },
                    "search_id": "abc123def456",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = response.parse()
        assert_matches_type(BatchResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_submit_batch(self, client: Papr) -> None:
        with client.feedback.with_streaming_response.submit_batch(
            feedback_items=[
                {
                    "feedback_data": {
                        "feedback_source": "inline",
                        "feedback_type": "thumbs_up",
                    },
                    "search_id": "abc123def456",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = response.parse()
            assert_matches_type(BatchResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFeedback:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncPapr) -> None:
        feedback = await async_client.feedback.get_by_id(
            "feedback_id",
        )
        assert_matches_type(FeedbackResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncPapr) -> None:
        response = await async_client.feedback.with_raw_response.get_by_id(
            "feedback_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = await response.parse()
        assert_matches_type(FeedbackResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncPapr) -> None:
        async with async_client.feedback.with_streaming_response.get_by_id(
            "feedback_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = await response.parse()
            assert_matches_type(FeedbackResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncPapr) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feedback_id` but received ''"):
            await async_client.feedback.with_raw_response.get_by_id(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit(self, async_client: AsyncPapr) -> None:
        feedback = await async_client.feedback.submit(
            feedback_data={
                "feedback_source": "inline",
                "feedback_type": "thumbs_up",
            },
            search_id="abc123def456",
        )
        assert_matches_type(FeedbackResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit_with_all_params(self, async_client: AsyncPapr) -> None:
        feedback = await async_client.feedback.submit(
            feedback_data={
                "feedback_source": "inline",
                "feedback_type": "thumbs_up",
                "assistant_message": {
                    "class_name": "PostMessage",
                    "object_id": "abc123def456",
                    "_type": "Pointer",
                },
                "cited_memory_ids": ["mem_123", "mem_456"],
                "cited_node_ids": ["node_123", "node_456"],
                "feedback_impact": "positive",
                "feedback_processed": True,
                "feedback_score": 1,
                "feedback_text": "This answer was very helpful and accurate",
                "feedback_value": "helpful",
                "user_message": {
                    "class_name": "PostMessage",
                    "object_id": "abc123def456",
                    "_type": "Pointer",
                },
            },
            search_id="abc123def456",
            external_user_id="dev_api_key_123",
            user_id="abc123def456",
        )
        assert_matches_type(FeedbackResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncPapr) -> None:
        response = await async_client.feedback.with_raw_response.submit(
            feedback_data={
                "feedback_source": "inline",
                "feedback_type": "thumbs_up",
            },
            search_id="abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = await response.parse()
        assert_matches_type(FeedbackResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncPapr) -> None:
        async with async_client.feedback.with_streaming_response.submit(
            feedback_data={
                "feedback_source": "inline",
                "feedback_type": "thumbs_up",
            },
            search_id="abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = await response.parse()
            assert_matches_type(FeedbackResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit_batch(self, async_client: AsyncPapr) -> None:
        feedback = await async_client.feedback.submit_batch(
            feedback_items=[
                {
                    "feedback_data": {
                        "feedback_source": "inline",
                        "feedback_type": "thumbs_up",
                    },
                    "search_id": "abc123def456",
                }
            ],
        )
        assert_matches_type(BatchResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit_batch_with_all_params(self, async_client: AsyncPapr) -> None:
        feedback = await async_client.feedback.submit_batch(
            feedback_items=[
                {
                    "feedback_data": {
                        "feedback_source": "inline",
                        "feedback_type": "thumbs_up",
                        "assistant_message": {
                            "class_name": "PostMessage",
                            "object_id": "abc123def456",
                            "_type": "Pointer",
                        },
                        "cited_memory_ids": ["mem_123", "mem_456"],
                        "cited_node_ids": ["node_123", "node_456"],
                        "feedback_impact": "positive",
                        "feedback_processed": True,
                        "feedback_score": 1,
                        "feedback_text": "This answer was very helpful and accurate",
                        "feedback_value": "helpful",
                        "user_message": {
                            "class_name": "PostMessage",
                            "object_id": "abc123def456",
                            "_type": "Pointer",
                        },
                    },
                    "search_id": "abc123def456",
                    "external_user_id": "dev_api_key_123",
                    "user_id": "abc123def456",
                }
            ],
            session_context={"foo": "bar"},
        )
        assert_matches_type(BatchResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_submit_batch(self, async_client: AsyncPapr) -> None:
        response = await async_client.feedback.with_raw_response.submit_batch(
            feedback_items=[
                {
                    "feedback_data": {
                        "feedback_source": "inline",
                        "feedback_type": "thumbs_up",
                    },
                    "search_id": "abc123def456",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = await response.parse()
        assert_matches_type(BatchResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_submit_batch(self, async_client: AsyncPapr) -> None:
        async with async_client.feedback.with_streaming_response.submit_batch(
            feedback_items=[
                {
                    "feedback_data": {
                        "feedback_source": "inline",
                        "feedback_type": "thumbs_up",
                    },
                    "search_id": "abc123def456",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = await response.parse()
            assert_matches_type(BatchResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True
