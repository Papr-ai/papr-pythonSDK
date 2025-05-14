# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from papr_memory import Papr, AsyncPapr
from tests.utils import assert_matches_type
from papr_memory.types import DocumentUploadResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocument:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_upload(self, client: Papr) -> None:
        document = client.document.upload()
        assert_matches_type(DocumentUploadResponse, document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_upload_with_all_params(self, client: Papr) -> None:
        document = client.document.upload(
            post_object_id="post_objectId",
            skip_background_processing=True,
        )
        assert_matches_type(DocumentUploadResponse, document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_upload(self, client: Papr) -> None:
        response = client.document.with_raw_response.upload()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentUploadResponse, document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_upload(self, client: Papr) -> None:
        with client.document.with_streaming_response.upload() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentUploadResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDocument:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_upload(self, async_client: AsyncPapr) -> None:
        document = await async_client.document.upload()
        assert_matches_type(DocumentUploadResponse, document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncPapr) -> None:
        document = await async_client.document.upload(
            post_object_id="post_objectId",
            skip_background_processing=True,
        )
        assert_matches_type(DocumentUploadResponse, document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncPapr) -> None:
        response = await async_client.document.with_raw_response.upload()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentUploadResponse, document, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncPapr) -> None:
        async with async_client.document.with_streaming_response.upload() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentUploadResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True
