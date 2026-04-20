# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import PaprError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import omo, sync, user, memory, graphql, schemas, document, feedback, messages
    from .resources.omo import OmoResource, AsyncOmoResource
    from .resources.sync import SyncResource, AsyncSyncResource
    from .resources.user import UserResource, AsyncUserResource
    from .resources.memory import MemoryResource, AsyncMemoryResource
    from .resources.graphql import GraphqlResource, AsyncGraphqlResource
    from .resources.schemas import SchemasResource, AsyncSchemasResource
    from .resources.document import DocumentResource, AsyncDocumentResource
    from .resources.feedback import FeedbackResource, AsyncFeedbackResource
    from .resources.messages.messages import MessagesResource, AsyncMessagesResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Papr", "AsyncPapr", "Client", "AsyncClient"]


class Papr(SyncAPIClient):
    # client options
    x_api_key: str
    x_session_token: str | None
    bearer_token: str | None

    def __init__(
        self,
        *,
        x_api_key: str | None = None,
        x_session_token: str | None = None,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Papr client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `x_api_key` from `PAPR_MEMORY_API_KEY`
        - `x_session_token` from `PAPR_MEMORY_Session_Token`
        - `bearer_token` from `PAPR_MEMORY_BEARER_TOKEN`
        """
        if x_api_key is None:
            x_api_key = os.environ.get("PAPR_MEMORY_API_KEY")
        if x_api_key is None:
            raise PaprError(
                "The x_api_key client option must be set either by passing x_api_key to the client or by setting the PAPR_MEMORY_API_KEY environment variable"
            )
        self.x_api_key = x_api_key

        if x_session_token is None:
            x_session_token = os.environ.get("PAPR_MEMORY_Session_Token")
        self.x_session_token = x_session_token

        if bearer_token is None:
            bearer_token = os.environ.get("PAPR_MEMORY_BEARER_TOKEN")
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("PAPR_BASE_URL")
        if base_url is None:
            base_url = f"https://memory.papr.ai"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def user(self) -> UserResource:
        from .resources.user import UserResource

        return UserResource(self)

    @cached_property
    def memory(self) -> MemoryResource:
        from .resources.memory import MemoryResource

        return MemoryResource(self)

    @cached_property
    def feedback(self) -> FeedbackResource:
        from .resources.feedback import FeedbackResource

        return FeedbackResource(self)

    @cached_property
    def document(self) -> DocumentResource:
        from .resources.document import DocumentResource

        return DocumentResource(self)

    @cached_property
    def schemas(self) -> SchemasResource:
        from .resources.schemas import SchemasResource

        return SchemasResource(self)

    @cached_property
    def graphql(self) -> GraphqlResource:
        from .resources.graphql import GraphqlResource

        return GraphqlResource(self)

    @cached_property
    def messages(self) -> MessagesResource:
        from .resources.messages import MessagesResource

        return MessagesResource(self)

    @cached_property
    def omo(self) -> OmoResource:
        from .resources.omo import OmoResource

        return OmoResource(self)

    @cached_property
    def sync(self) -> SyncResource:
        from .resources.sync import SyncResource

        return SyncResource(self)

    @cached_property
    def with_raw_response(self) -> PaprWithRawResponse:
        return PaprWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaprWithStreamedResponse:
        return PaprWithStreamedResponse(self)

        # Initialize sync_tiers and ChromaDB collection if on-device processing is enabled
        from ._logging import get_logger, log_ondevice_status

        logger = get_logger(__name__)
        ondevice_processing = os.environ.get("PAPR_ONDEVICE_PROCESSING", "false").lower() in ("true", "1", "yes", "on")

        if ondevice_processing:
            try:
                # Start background initialization for truly non-blocking client creation
                logger.info("Starting background initialization for optimal user experience")
                self.memory._start_background_initialization()

                logger.info("Client initialization completed successfully (all setup in background)")
            except Exception as e:
                logger.warning(f"Failed to start background initialization: {e}")
                logger.warning("Client will still work, but local search features may be limited")

        log_ondevice_status(logger, ondevice_processing)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._bearer, **self._x_session_token, **self._x_api_key}

    @property
    def _bearer(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        if bearer_token is None:
            return {}
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    def _x_session_token(self) -> dict[str, str]:
        x_session_token = self.x_session_token
        if x_session_token is None:
            return {}
        return {"X-Session-Token": x_session_token}

    @property
    def _x_api_key(self) -> dict[str, str]:
        x_api_key = self.x_api_key
        return {"X-API-Key": x_api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        x_api_key: str | None = None,
        x_session_token: str | None = None,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            x_api_key=x_api_key or self.x_api_key,
            x_session_token=x_session_token or self.x_session_token,
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncPapr(AsyncAPIClient):
    # client options
    x_api_key: str
    x_session_token: str | None
    bearer_token: str | None

    def __init__(
        self,
        *,
        x_api_key: str | None = None,
        x_session_token: str | None = None,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncPapr client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `x_api_key` from `PAPR_MEMORY_API_KEY`
        - `x_session_token` from `PAPR_MEMORY_Session_Token`
        - `bearer_token` from `PAPR_MEMORY_BEARER_TOKEN`
        """
        if x_api_key is None:
            x_api_key = os.environ.get("PAPR_MEMORY_API_KEY")
        if x_api_key is None:
            raise PaprError(
                "The x_api_key client option must be set either by passing x_api_key to the client or by setting the PAPR_MEMORY_API_KEY environment variable"
            )
        self.x_api_key = x_api_key

        if x_session_token is None:
            x_session_token = os.environ.get("PAPR_MEMORY_Session_Token")
        self.x_session_token = x_session_token

        if bearer_token is None:
            bearer_token = os.environ.get("PAPR_MEMORY_BEARER_TOKEN")
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("PAPR_BASE_URL")
        if base_url is None:
            base_url = f"https://memory.papr.ai"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def user(self) -> AsyncUserResource:
        from .resources.user import AsyncUserResource

        return AsyncUserResource(self)

    @cached_property
    def memory(self) -> AsyncMemoryResource:
        from .resources.memory import AsyncMemoryResource

        return AsyncMemoryResource(self)

    @cached_property
    def feedback(self) -> AsyncFeedbackResource:
        from .resources.feedback import AsyncFeedbackResource

        return AsyncFeedbackResource(self)

    @cached_property
    def document(self) -> AsyncDocumentResource:
        from .resources.document import AsyncDocumentResource

        return AsyncDocumentResource(self)

    @cached_property
    def schemas(self) -> AsyncSchemasResource:
        from .resources.schemas import AsyncSchemasResource

        return AsyncSchemasResource(self)

    @cached_property
    def graphql(self) -> AsyncGraphqlResource:
        from .resources.graphql import AsyncGraphqlResource

        return AsyncGraphqlResource(self)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        from .resources.messages import AsyncMessagesResource

        return AsyncMessagesResource(self)

    @cached_property
    def omo(self) -> AsyncOmoResource:
        from .resources.omo import AsyncOmoResource

        return AsyncOmoResource(self)

    @cached_property
    def sync(self) -> AsyncSyncResource:
        from .resources.sync import AsyncSyncResource

        return AsyncSyncResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncPaprWithRawResponse:
        return AsyncPaprWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaprWithStreamedResponse:
        return AsyncPaprWithStreamedResponse(self)

        # Initialize sync_tiers and ChromaDB collection (async) if on-device processing is enabled
        from ._logging import get_logger, log_ondevice_status

        logger = get_logger(__name__)
        ondevice_processing = os.environ.get("PAPR_ONDEVICE_PROCESSING", "false").lower() in ("true", "1", "yes", "on")

        if ondevice_processing:
            try:
                logger.info("Preparing async sync_tiers initialization")
                # Note: We can't call async methods in __init__, so we'll do this lazily
                self._sync_tiers_initialized = False
            except Exception as e:
                logger.warning(f"Failed to prepare async sync_tiers initialization: {e}")
                self._sync_tiers_initialized = False
        else:
            self._sync_tiers_initialized = False

        log_ondevice_status(logger, ondevice_processing)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._bearer, **self._x_session_token, **self._x_api_key}

    @property
    def _bearer(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        if bearer_token is None:
            return {}
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    def _x_session_token(self) -> dict[str, str]:
        x_session_token = self.x_session_token
        if x_session_token is None:
            return {}
        return {"X-Session-Token": x_session_token}

    @property
    def _x_api_key(self) -> dict[str, str]:
        x_api_key = self.x_api_key
        return {"X-API-Key": x_api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        x_api_key: str | None = None,
        x_session_token: str | None = None,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            x_api_key=x_api_key or self.x_api_key,
            x_session_token=x_session_token or self.x_session_token,
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class PaprWithRawResponse:
    _client: Papr

    def __init__(self, client: Papr) -> None:
        self._client = client

    @cached_property
    def user(self) -> user.UserResourceWithRawResponse:
        from .resources.user import UserResourceWithRawResponse

        return UserResourceWithRawResponse(self._client.user)

    @cached_property
    def memory(self) -> memory.MemoryResourceWithRawResponse:
        from .resources.memory import MemoryResourceWithRawResponse

        return MemoryResourceWithRawResponse(self._client.memory)

    @cached_property
    def feedback(self) -> feedback.FeedbackResourceWithRawResponse:
        from .resources.feedback import FeedbackResourceWithRawResponse

        return FeedbackResourceWithRawResponse(self._client.feedback)

    @cached_property
    def document(self) -> document.DocumentResourceWithRawResponse:
        from .resources.document import DocumentResourceWithRawResponse

        return DocumentResourceWithRawResponse(self._client.document)

    @cached_property
    def schemas(self) -> schemas.SchemasResourceWithRawResponse:
        from .resources.schemas import SchemasResourceWithRawResponse

        return SchemasResourceWithRawResponse(self._client.schemas)

    @cached_property
    def graphql(self) -> graphql.GraphqlResourceWithRawResponse:
        from .resources.graphql import GraphqlResourceWithRawResponse

        return GraphqlResourceWithRawResponse(self._client.graphql)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithRawResponse:
        from .resources.messages import MessagesResourceWithRawResponse

        return MessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def omo(self) -> omo.OmoResourceWithRawResponse:
        from .resources.omo import OmoResourceWithRawResponse

        return OmoResourceWithRawResponse(self._client.omo)

    @cached_property
    def sync(self) -> sync.SyncResourceWithRawResponse:
        from .resources.sync import SyncResourceWithRawResponse

        return SyncResourceWithRawResponse(self._client.sync)


class AsyncPaprWithRawResponse:
    _client: AsyncPapr

    def __init__(self, client: AsyncPapr) -> None:
        self._client = client

    @cached_property
    def user(self) -> user.AsyncUserResourceWithRawResponse:
        from .resources.user import AsyncUserResourceWithRawResponse

        return AsyncUserResourceWithRawResponse(self._client.user)

    @cached_property
    def memory(self) -> memory.AsyncMemoryResourceWithRawResponse:
        from .resources.memory import AsyncMemoryResourceWithRawResponse

        return AsyncMemoryResourceWithRawResponse(self._client.memory)

    @cached_property
    def feedback(self) -> feedback.AsyncFeedbackResourceWithRawResponse:
        from .resources.feedback import AsyncFeedbackResourceWithRawResponse

        return AsyncFeedbackResourceWithRawResponse(self._client.feedback)

    @cached_property
    def document(self) -> document.AsyncDocumentResourceWithRawResponse:
        from .resources.document import AsyncDocumentResourceWithRawResponse

        return AsyncDocumentResourceWithRawResponse(self._client.document)

    @cached_property
    def schemas(self) -> schemas.AsyncSchemasResourceWithRawResponse:
        from .resources.schemas import AsyncSchemasResourceWithRawResponse

        return AsyncSchemasResourceWithRawResponse(self._client.schemas)

    @cached_property
    def graphql(self) -> graphql.AsyncGraphqlResourceWithRawResponse:
        from .resources.graphql import AsyncGraphqlResourceWithRawResponse

        return AsyncGraphqlResourceWithRawResponse(self._client.graphql)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithRawResponse:
        from .resources.messages import AsyncMessagesResourceWithRawResponse

        return AsyncMessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def omo(self) -> omo.AsyncOmoResourceWithRawResponse:
        from .resources.omo import AsyncOmoResourceWithRawResponse

        return AsyncOmoResourceWithRawResponse(self._client.omo)

    @cached_property
    def sync(self) -> sync.AsyncSyncResourceWithRawResponse:
        from .resources.sync import AsyncSyncResourceWithRawResponse

        return AsyncSyncResourceWithRawResponse(self._client.sync)


class PaprWithStreamedResponse:
    _client: Papr

    def __init__(self, client: Papr) -> None:
        self._client = client

    @cached_property
    def user(self) -> user.UserResourceWithStreamingResponse:
        from .resources.user import UserResourceWithStreamingResponse

        return UserResourceWithStreamingResponse(self._client.user)

    @cached_property
    def memory(self) -> memory.MemoryResourceWithStreamingResponse:
        from .resources.memory import MemoryResourceWithStreamingResponse

        return MemoryResourceWithStreamingResponse(self._client.memory)

    @cached_property
    def feedback(self) -> feedback.FeedbackResourceWithStreamingResponse:
        from .resources.feedback import FeedbackResourceWithStreamingResponse

        return FeedbackResourceWithStreamingResponse(self._client.feedback)

    @cached_property
    def document(self) -> document.DocumentResourceWithStreamingResponse:
        from .resources.document import DocumentResourceWithStreamingResponse

        return DocumentResourceWithStreamingResponse(self._client.document)

    @cached_property
    def schemas(self) -> schemas.SchemasResourceWithStreamingResponse:
        from .resources.schemas import SchemasResourceWithStreamingResponse

        return SchemasResourceWithStreamingResponse(self._client.schemas)

    @cached_property
    def graphql(self) -> graphql.GraphqlResourceWithStreamingResponse:
        from .resources.graphql import GraphqlResourceWithStreamingResponse

        return GraphqlResourceWithStreamingResponse(self._client.graphql)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithStreamingResponse:
        from .resources.messages import MessagesResourceWithStreamingResponse

        return MessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def omo(self) -> omo.OmoResourceWithStreamingResponse:
        from .resources.omo import OmoResourceWithStreamingResponse

        return OmoResourceWithStreamingResponse(self._client.omo)

    @cached_property
    def sync(self) -> sync.SyncResourceWithStreamingResponse:
        from .resources.sync import SyncResourceWithStreamingResponse

        return SyncResourceWithStreamingResponse(self._client.sync)


class AsyncPaprWithStreamedResponse:
    _client: AsyncPapr

    def __init__(self, client: AsyncPapr) -> None:
        self._client = client

    @cached_property
    def user(self) -> user.AsyncUserResourceWithStreamingResponse:
        from .resources.user import AsyncUserResourceWithStreamingResponse

        return AsyncUserResourceWithStreamingResponse(self._client.user)

    @cached_property
    def memory(self) -> memory.AsyncMemoryResourceWithStreamingResponse:
        from .resources.memory import AsyncMemoryResourceWithStreamingResponse

        return AsyncMemoryResourceWithStreamingResponse(self._client.memory)

    @cached_property
    def feedback(self) -> feedback.AsyncFeedbackResourceWithStreamingResponse:
        from .resources.feedback import AsyncFeedbackResourceWithStreamingResponse

        return AsyncFeedbackResourceWithStreamingResponse(self._client.feedback)

    @cached_property
    def document(self) -> document.AsyncDocumentResourceWithStreamingResponse:
        from .resources.document import AsyncDocumentResourceWithStreamingResponse

        return AsyncDocumentResourceWithStreamingResponse(self._client.document)

    @cached_property
    def schemas(self) -> schemas.AsyncSchemasResourceWithStreamingResponse:
        from .resources.schemas import AsyncSchemasResourceWithStreamingResponse

        return AsyncSchemasResourceWithStreamingResponse(self._client.schemas)

    @cached_property
    def graphql(self) -> graphql.AsyncGraphqlResourceWithStreamingResponse:
        from .resources.graphql import AsyncGraphqlResourceWithStreamingResponse

        return AsyncGraphqlResourceWithStreamingResponse(self._client.graphql)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithStreamingResponse:
        from .resources.messages import AsyncMessagesResourceWithStreamingResponse

        return AsyncMessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def omo(self) -> omo.AsyncOmoResourceWithStreamingResponse:
        from .resources.omo import AsyncOmoResourceWithStreamingResponse

        return AsyncOmoResourceWithStreamingResponse(self._client.omo)

    @cached_property
    def sync(self) -> sync.AsyncSyncResourceWithStreamingResponse:
        from .resources.sync import AsyncSyncResourceWithStreamingResponse

        return AsyncSyncResourceWithStreamingResponse(self._client.sync)


Client = Papr

AsyncClient = AsyncPapr
