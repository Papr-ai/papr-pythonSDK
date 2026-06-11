# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["GraphqlResource", "AsyncGraphqlResource"]


class GraphqlResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GraphqlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return GraphqlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GraphqlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return GraphqlResourceWithStreamingResponse(self)

    def playground(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """GraphQL Playground (development only)"""
        return self._get(
            "/v1/graphql",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def query(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        GraphQL endpoint for querying PAPR Memory using GraphQL.

            This endpoint proxies GraphQL queries to Neo4j's hosted GraphQL endpoint,
            automatically applying multi-tenant authorization filters based on user_id and workspace_id.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Request Body**:
            ```json
            {
              "query": "query { project(id: \"proj_123\") { name tasks { title } } }",
              "variables": {},
              "operationName": "GetProject"
            }
            ```

            **Example Query**:
            ```graphql
            query GetProjectTasks($projectId: ID!) {
              project(id: $projectId) {
                name
                tasks {
                  title
                  status
                }
              }
            }
            ```

            All queries are automatically filtered by user_id and workspace_id for security.
        """
        return self._post(
            "/v1/graphql",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncGraphqlResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGraphqlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AsyncGraphqlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGraphqlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AsyncGraphqlResourceWithStreamingResponse(self)

    async def playground(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """GraphQL Playground (development only)"""
        return await self._get(
            "/v1/graphql",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def query(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        GraphQL endpoint for querying PAPR Memory using GraphQL.

            This endpoint proxies GraphQL queries to Neo4j's hosted GraphQL endpoint,
            automatically applying multi-tenant authorization filters based on user_id and workspace_id.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Request Body**:
            ```json
            {
              "query": "query { project(id: \"proj_123\") { name tasks { title } } }",
              "variables": {},
              "operationName": "GetProject"
            }
            ```

            **Example Query**:
            ```graphql
            query GetProjectTasks($projectId: ID!) {
              project(id: $projectId) {
                name
                tasks {
                  title
                  status
                }
              }
            }
            ```

            All queries are automatically filtered by user_id and workspace_id for security.
        """
        return await self._post(
            "/v1/graphql",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class GraphqlResourceWithRawResponse:
    def __init__(self, graphql: GraphqlResource) -> None:
        self._graphql = graphql

        self.playground = to_raw_response_wrapper(
            graphql.playground,
        )
        self.query = to_raw_response_wrapper(
            graphql.query,
        )


class AsyncGraphqlResourceWithRawResponse:
    def __init__(self, graphql: AsyncGraphqlResource) -> None:
        self._graphql = graphql

        self.playground = async_to_raw_response_wrapper(
            graphql.playground,
        )
        self.query = async_to_raw_response_wrapper(
            graphql.query,
        )


class GraphqlResourceWithStreamingResponse:
    def __init__(self, graphql: GraphqlResource) -> None:
        self._graphql = graphql

        self.playground = to_streamed_response_wrapper(
            graphql.playground,
        )
        self.query = to_streamed_response_wrapper(
            graphql.query,
        )


class AsyncGraphqlResourceWithStreamingResponse:
    def __init__(self, graphql: AsyncGraphqlResource) -> None:
        self._graphql = graphql

        self.playground = async_to_streamed_response_wrapper(
            graphql.playground,
        )
        self.query = async_to_streamed_response_wrapper(
            graphql.query,
        )
