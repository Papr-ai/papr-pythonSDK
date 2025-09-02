# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import is_given, get_async_library
from ._oauth2 import OAuth2ClientCredentials
from ._version import __version__
from .resources import user, memory, feedback
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import PaprError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Papr", "AsyncPapr", "Client", "AsyncClient"]


class Papr(SyncAPIClient):
    user: user.UserResource
    memory: memory.MemoryResource
    feedback: feedback.FeedbackResource
    with_raw_response: PaprWithRawResponse
    with_streaming_response: PaprWithStreamedResponse

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
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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

        self.user = user.UserResource(self)
        self.memory = memory.MemoryResource(self)
        self.feedback = feedback.FeedbackResource(self)
        self.with_raw_response = PaprWithRawResponse(self)
        self.with_streaming_response = PaprWithStreamedResponse(self)

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
    def custom_auth(self) -> httpx.Auth | None:
        raise NotImplementedError("This auth method has not been implemented yet.")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _should_retry(self, response: httpx.Response) -> bool:
        # Retry on 401 if we are using OAuth2 and the token might be expired
        if response.status_code == 401 and isinstance(self.custom_auth, OAuth2ClientCredentials):
            if self.custom_auth.token_is_expired():
                self.custom_auth.invalidate_token()
                return True
        return super()._should_retry(response)

    def copy(
        self,
        *,
        x_api_key: str | None = None,
        x_session_token: str | None = None,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
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
    user: user.AsyncUserResource
    memory: memory.AsyncMemoryResource
    feedback: feedback.AsyncFeedbackResource
    with_raw_response: AsyncPaprWithRawResponse
    with_streaming_response: AsyncPaprWithStreamedResponse

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
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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

        self.user = user.AsyncUserResource(self)
        self.memory = memory.AsyncMemoryResource(self)
        self.feedback = feedback.AsyncFeedbackResource(self)
        self.with_raw_response = AsyncPaprWithRawResponse(self)
        self.with_streaming_response = AsyncPaprWithStreamedResponse(self)

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
    def custom_auth(self) -> httpx.Auth | None:
        raise NotImplementedError("This auth method has not been implemented yet.")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _should_retry(self, response: httpx.Response) -> bool:
        # Retry on 401 if we are using OAuth2 and the token might be expired
        if response.status_code == 401 and isinstance(self.custom_auth, OAuth2ClientCredentials):
            if self.custom_auth.token_is_expired():
                self.custom_auth.invalidate_token()
                return True
        return super()._should_retry(response)

    def copy(
        self,
        *,
        x_api_key: str | None = None,
        x_session_token: str | None = None,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
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
    def __init__(self, client: Papr) -> None:
        self.user = user.UserResourceWithRawResponse(client.user)
        self.memory = memory.MemoryResourceWithRawResponse(client.memory)
        self.feedback = feedback.FeedbackResourceWithRawResponse(client.feedback)


class AsyncPaprWithRawResponse:
    def __init__(self, client: AsyncPapr) -> None:
        self.user = user.AsyncUserResourceWithRawResponse(client.user)
        self.memory = memory.AsyncMemoryResourceWithRawResponse(client.memory)
        self.feedback = feedback.AsyncFeedbackResourceWithRawResponse(client.feedback)


class PaprWithStreamedResponse:
    def __init__(self, client: Papr) -> None:
        self.user = user.UserResourceWithStreamingResponse(client.user)
        self.memory = memory.MemoryResourceWithStreamingResponse(client.memory)
        self.feedback = feedback.FeedbackResourceWithStreamingResponse(client.feedback)


class AsyncPaprWithStreamedResponse:
    def __init__(self, client: AsyncPapr) -> None:
        self.user = user.AsyncUserResourceWithStreamingResponse(client.user)
        self.memory = memory.AsyncMemoryResourceWithStreamingResponse(client.memory)
        self.feedback = feedback.AsyncFeedbackResourceWithStreamingResponse(client.feedback)


Client = Papr

AsyncClient = AsyncPapr
