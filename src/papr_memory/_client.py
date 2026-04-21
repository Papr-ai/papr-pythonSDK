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
    from .resources import (
        ai,
        me,
        omo,
        sync,
        user,
        login,
        token,
        logout,
        memory,
        graphql,
        schemas,
        callback,
        document,
        feedback,
        messages,
        namespace,
        telemetry,
        frequencies,
        holographic,
        organization,
    )
    from .resources.me import MeResource, AsyncMeResource
    from .resources.omo import OmoResource, AsyncOmoResource
    from .resources.sync import SyncResource, AsyncSyncResource
    from .resources.user import UserResource, AsyncUserResource
    from .resources.ai.ai import AIResource, AsyncAIResource
    from .resources.login import LoginResource, AsyncLoginResource
    from .resources.token import TokenResource, AsyncTokenResource
    from .resources.logout import LogoutResource, AsyncLogoutResource
    from .resources.memory import MemoryResource, AsyncMemoryResource
    from .resources.graphql import GraphqlResource, AsyncGraphqlResource
    from .resources.schemas import SchemasResource, AsyncSchemasResource
    from .resources.callback import CallbackResource, AsyncCallbackResource
    from .resources.document import DocumentResource, AsyncDocumentResource
    from .resources.feedback import FeedbackResource, AsyncFeedbackResource
    from .resources.telemetry import TelemetryResource, AsyncTelemetryResource
    from .resources.frequencies import FrequenciesResource, AsyncFrequenciesResource
    from .resources.messages.messages import MessagesResource, AsyncMessagesResource
    from .resources.namespace.namespace import NamespaceResource, AsyncNamespaceResource
    from .resources.holographic.holographic import HolographicResource, AsyncHolographicResource
    from .resources.organization.organization import OrganizationResource, AsyncOrganizationResource

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
    def namespace(self) -> NamespaceResource:
        from .resources.namespace import NamespaceResource

        return NamespaceResource(self)

    @cached_property
    def frequencies(self) -> FrequenciesResource:
        from .resources.frequencies import FrequenciesResource

        return FrequenciesResource(self)

    @cached_property
    def holographic(self) -> HolographicResource:
        from .resources.holographic import HolographicResource

        return HolographicResource(self)

    @cached_property
    def organization(self) -> OrganizationResource:
        from .resources.organization import OrganizationResource

        return OrganizationResource(self)

    @cached_property
    def ai(self) -> AIResource:
        from .resources.ai import AIResource

        return AIResource(self)

    @cached_property
    def telemetry(self) -> TelemetryResource:
        from .resources.telemetry import TelemetryResource

        return TelemetryResource(self)

    @cached_property
    def login(self) -> LoginResource:
        from .resources.login import LoginResource

        return LoginResource(self)

    @cached_property
    def callback(self) -> CallbackResource:
        from .resources.callback import CallbackResource

        return CallbackResource(self)

    @cached_property
    def token(self) -> TokenResource:
        from .resources.token import TokenResource

        return TokenResource(self)

    @cached_property
    def me(self) -> MeResource:
        from .resources.me import MeResource

        return MeResource(self)

    @cached_property
    def logout(self) -> LogoutResource:
        from .resources.logout import LogoutResource

        return LogoutResource(self)

    @cached_property
    def with_raw_response(self) -> PaprWithRawResponse:
        return PaprWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaprWithStreamedResponse:
        return PaprWithStreamedResponse(self)

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
    def namespace(self) -> AsyncNamespaceResource:
        from .resources.namespace import AsyncNamespaceResource

        return AsyncNamespaceResource(self)

    @cached_property
    def frequencies(self) -> AsyncFrequenciesResource:
        from .resources.frequencies import AsyncFrequenciesResource

        return AsyncFrequenciesResource(self)

    @cached_property
    def holographic(self) -> AsyncHolographicResource:
        from .resources.holographic import AsyncHolographicResource

        return AsyncHolographicResource(self)

    @cached_property
    def organization(self) -> AsyncOrganizationResource:
        from .resources.organization import AsyncOrganizationResource

        return AsyncOrganizationResource(self)

    @cached_property
    def ai(self) -> AsyncAIResource:
        from .resources.ai import AsyncAIResource

        return AsyncAIResource(self)

    @cached_property
    def telemetry(self) -> AsyncTelemetryResource:
        from .resources.telemetry import AsyncTelemetryResource

        return AsyncTelemetryResource(self)

    @cached_property
    def login(self) -> AsyncLoginResource:
        from .resources.login import AsyncLoginResource

        return AsyncLoginResource(self)

    @cached_property
    def callback(self) -> AsyncCallbackResource:
        from .resources.callback import AsyncCallbackResource

        return AsyncCallbackResource(self)

    @cached_property
    def token(self) -> AsyncTokenResource:
        from .resources.token import AsyncTokenResource

        return AsyncTokenResource(self)

    @cached_property
    def me(self) -> AsyncMeResource:
        from .resources.me import AsyncMeResource

        return AsyncMeResource(self)

    @cached_property
    def logout(self) -> AsyncLogoutResource:
        from .resources.logout import AsyncLogoutResource

        return AsyncLogoutResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncPaprWithRawResponse:
        return AsyncPaprWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaprWithStreamedResponse:
        return AsyncPaprWithStreamedResponse(self)

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

    @cached_property
    def namespace(self) -> namespace.NamespaceResourceWithRawResponse:
        from .resources.namespace import NamespaceResourceWithRawResponse

        return NamespaceResourceWithRawResponse(self._client.namespace)

    @cached_property
    def frequencies(self) -> frequencies.FrequenciesResourceWithRawResponse:
        from .resources.frequencies import FrequenciesResourceWithRawResponse

        return FrequenciesResourceWithRawResponse(self._client.frequencies)

    @cached_property
    def holographic(self) -> holographic.HolographicResourceWithRawResponse:
        from .resources.holographic import HolographicResourceWithRawResponse

        return HolographicResourceWithRawResponse(self._client.holographic)

    @cached_property
    def organization(self) -> organization.OrganizationResourceWithRawResponse:
        from .resources.organization import OrganizationResourceWithRawResponse

        return OrganizationResourceWithRawResponse(self._client.organization)

    @cached_property
    def ai(self) -> ai.AIResourceWithRawResponse:
        from .resources.ai import AIResourceWithRawResponse

        return AIResourceWithRawResponse(self._client.ai)

    @cached_property
    def telemetry(self) -> telemetry.TelemetryResourceWithRawResponse:
        from .resources.telemetry import TelemetryResourceWithRawResponse

        return TelemetryResourceWithRawResponse(self._client.telemetry)

    @cached_property
    def login(self) -> login.LoginResourceWithRawResponse:
        from .resources.login import LoginResourceWithRawResponse

        return LoginResourceWithRawResponse(self._client.login)

    @cached_property
    def callback(self) -> callback.CallbackResourceWithRawResponse:
        from .resources.callback import CallbackResourceWithRawResponse

        return CallbackResourceWithRawResponse(self._client.callback)

    @cached_property
    def token(self) -> token.TokenResourceWithRawResponse:
        from .resources.token import TokenResourceWithRawResponse

        return TokenResourceWithRawResponse(self._client.token)

    @cached_property
    def me(self) -> me.MeResourceWithRawResponse:
        from .resources.me import MeResourceWithRawResponse

        return MeResourceWithRawResponse(self._client.me)

    @cached_property
    def logout(self) -> logout.LogoutResourceWithRawResponse:
        from .resources.logout import LogoutResourceWithRawResponse

        return LogoutResourceWithRawResponse(self._client.logout)


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

    @cached_property
    def namespace(self) -> namespace.AsyncNamespaceResourceWithRawResponse:
        from .resources.namespace import AsyncNamespaceResourceWithRawResponse

        return AsyncNamespaceResourceWithRawResponse(self._client.namespace)

    @cached_property
    def frequencies(self) -> frequencies.AsyncFrequenciesResourceWithRawResponse:
        from .resources.frequencies import AsyncFrequenciesResourceWithRawResponse

        return AsyncFrequenciesResourceWithRawResponse(self._client.frequencies)

    @cached_property
    def holographic(self) -> holographic.AsyncHolographicResourceWithRawResponse:
        from .resources.holographic import AsyncHolographicResourceWithRawResponse

        return AsyncHolographicResourceWithRawResponse(self._client.holographic)

    @cached_property
    def organization(self) -> organization.AsyncOrganizationResourceWithRawResponse:
        from .resources.organization import AsyncOrganizationResourceWithRawResponse

        return AsyncOrganizationResourceWithRawResponse(self._client.organization)

    @cached_property
    def ai(self) -> ai.AsyncAIResourceWithRawResponse:
        from .resources.ai import AsyncAIResourceWithRawResponse

        return AsyncAIResourceWithRawResponse(self._client.ai)

    @cached_property
    def telemetry(self) -> telemetry.AsyncTelemetryResourceWithRawResponse:
        from .resources.telemetry import AsyncTelemetryResourceWithRawResponse

        return AsyncTelemetryResourceWithRawResponse(self._client.telemetry)

    @cached_property
    def login(self) -> login.AsyncLoginResourceWithRawResponse:
        from .resources.login import AsyncLoginResourceWithRawResponse

        return AsyncLoginResourceWithRawResponse(self._client.login)

    @cached_property
    def callback(self) -> callback.AsyncCallbackResourceWithRawResponse:
        from .resources.callback import AsyncCallbackResourceWithRawResponse

        return AsyncCallbackResourceWithRawResponse(self._client.callback)

    @cached_property
    def token(self) -> token.AsyncTokenResourceWithRawResponse:
        from .resources.token import AsyncTokenResourceWithRawResponse

        return AsyncTokenResourceWithRawResponse(self._client.token)

    @cached_property
    def me(self) -> me.AsyncMeResourceWithRawResponse:
        from .resources.me import AsyncMeResourceWithRawResponse

        return AsyncMeResourceWithRawResponse(self._client.me)

    @cached_property
    def logout(self) -> logout.AsyncLogoutResourceWithRawResponse:
        from .resources.logout import AsyncLogoutResourceWithRawResponse

        return AsyncLogoutResourceWithRawResponse(self._client.logout)


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

    @cached_property
    def namespace(self) -> namespace.NamespaceResourceWithStreamingResponse:
        from .resources.namespace import NamespaceResourceWithStreamingResponse

        return NamespaceResourceWithStreamingResponse(self._client.namespace)

    @cached_property
    def frequencies(self) -> frequencies.FrequenciesResourceWithStreamingResponse:
        from .resources.frequencies import FrequenciesResourceWithStreamingResponse

        return FrequenciesResourceWithStreamingResponse(self._client.frequencies)

    @cached_property
    def holographic(self) -> holographic.HolographicResourceWithStreamingResponse:
        from .resources.holographic import HolographicResourceWithStreamingResponse

        return HolographicResourceWithStreamingResponse(self._client.holographic)

    @cached_property
    def organization(self) -> organization.OrganizationResourceWithStreamingResponse:
        from .resources.organization import OrganizationResourceWithStreamingResponse

        return OrganizationResourceWithStreamingResponse(self._client.organization)

    @cached_property
    def ai(self) -> ai.AIResourceWithStreamingResponse:
        from .resources.ai import AIResourceWithStreamingResponse

        return AIResourceWithStreamingResponse(self._client.ai)

    @cached_property
    def telemetry(self) -> telemetry.TelemetryResourceWithStreamingResponse:
        from .resources.telemetry import TelemetryResourceWithStreamingResponse

        return TelemetryResourceWithStreamingResponse(self._client.telemetry)

    @cached_property
    def login(self) -> login.LoginResourceWithStreamingResponse:
        from .resources.login import LoginResourceWithStreamingResponse

        return LoginResourceWithStreamingResponse(self._client.login)

    @cached_property
    def callback(self) -> callback.CallbackResourceWithStreamingResponse:
        from .resources.callback import CallbackResourceWithStreamingResponse

        return CallbackResourceWithStreamingResponse(self._client.callback)

    @cached_property
    def token(self) -> token.TokenResourceWithStreamingResponse:
        from .resources.token import TokenResourceWithStreamingResponse

        return TokenResourceWithStreamingResponse(self._client.token)

    @cached_property
    def me(self) -> me.MeResourceWithStreamingResponse:
        from .resources.me import MeResourceWithStreamingResponse

        return MeResourceWithStreamingResponse(self._client.me)

    @cached_property
    def logout(self) -> logout.LogoutResourceWithStreamingResponse:
        from .resources.logout import LogoutResourceWithStreamingResponse

        return LogoutResourceWithStreamingResponse(self._client.logout)


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

    @cached_property
    def namespace(self) -> namespace.AsyncNamespaceResourceWithStreamingResponse:
        from .resources.namespace import AsyncNamespaceResourceWithStreamingResponse

        return AsyncNamespaceResourceWithStreamingResponse(self._client.namespace)

    @cached_property
    def frequencies(self) -> frequencies.AsyncFrequenciesResourceWithStreamingResponse:
        from .resources.frequencies import AsyncFrequenciesResourceWithStreamingResponse

        return AsyncFrequenciesResourceWithStreamingResponse(self._client.frequencies)

    @cached_property
    def holographic(self) -> holographic.AsyncHolographicResourceWithStreamingResponse:
        from .resources.holographic import AsyncHolographicResourceWithStreamingResponse

        return AsyncHolographicResourceWithStreamingResponse(self._client.holographic)

    @cached_property
    def organization(self) -> organization.AsyncOrganizationResourceWithStreamingResponse:
        from .resources.organization import AsyncOrganizationResourceWithStreamingResponse

        return AsyncOrganizationResourceWithStreamingResponse(self._client.organization)

    @cached_property
    def ai(self) -> ai.AsyncAIResourceWithStreamingResponse:
        from .resources.ai import AsyncAIResourceWithStreamingResponse

        return AsyncAIResourceWithStreamingResponse(self._client.ai)

    @cached_property
    def telemetry(self) -> telemetry.AsyncTelemetryResourceWithStreamingResponse:
        from .resources.telemetry import AsyncTelemetryResourceWithStreamingResponse

        return AsyncTelemetryResourceWithStreamingResponse(self._client.telemetry)

    @cached_property
    def login(self) -> login.AsyncLoginResourceWithStreamingResponse:
        from .resources.login import AsyncLoginResourceWithStreamingResponse

        return AsyncLoginResourceWithStreamingResponse(self._client.login)

    @cached_property
    def callback(self) -> callback.AsyncCallbackResourceWithStreamingResponse:
        from .resources.callback import AsyncCallbackResourceWithStreamingResponse

        return AsyncCallbackResourceWithStreamingResponse(self._client.callback)

    @cached_property
    def token(self) -> token.AsyncTokenResourceWithStreamingResponse:
        from .resources.token import AsyncTokenResourceWithStreamingResponse

        return AsyncTokenResourceWithStreamingResponse(self._client.token)

    @cached_property
    def me(self) -> me.AsyncMeResourceWithStreamingResponse:
        from .resources.me import AsyncMeResourceWithStreamingResponse

        return AsyncMeResourceWithStreamingResponse(self._client.me)

    @cached_property
    def logout(self) -> logout.AsyncLogoutResourceWithStreamingResponse:
        from .resources.logout import AsyncLogoutResourceWithStreamingResponse

        return AsyncLogoutResourceWithStreamingResponse(self._client.logout)


Client = Papr

AsyncClient = AsyncPapr
