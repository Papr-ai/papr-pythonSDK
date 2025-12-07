# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import schema_list_params, schema_create_params, schema_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.schema_list_response import SchemaListResponse
from ..types.schema_create_response import SchemaCreateResponse
from ..types.schema_update_response import SchemaUpdateResponse
from ..types.schema_retrieve_response import SchemaRetrieveResponse

__all__ = ["SchemasResource", "AsyncSchemasResource"]


class SchemasResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SchemasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return SchemasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SchemasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return SchemasResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        id: str | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        description: Optional[str] | Omit = omit,
        last_used_at: Union[str, datetime, None] | Omit = omit,
        namespace: Union[str, Dict[str, object], None] | Omit = omit,
        node_types: Dict[str, schema_create_params.NodeTypes] | Omit = omit,
        organization: Union[str, Dict[str, object], None] | Omit = omit,
        read_access: SequenceNotStr[str] | Omit = omit,
        relationship_types: Dict[str, schema_create_params.RelationshipTypes] | Omit = omit,
        scope: Literal["personal", "workspace", "namespace", "organization"] | Omit = omit,
        status: Literal["draft", "active", "deprecated", "archived"] | Omit = omit,
        updated_at: Union[str, datetime, None] | Omit = omit,
        usage_count: int | Omit = omit,
        user_id: Union[str, Dict[str, object], None] | Omit = omit,
        version: str | Omit = omit,
        workspace_id: Union[str, Dict[str, object], None] | Omit = omit,
        write_access: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaCreateResponse:
        """
        Create a new user-defined graph schema.

            This endpoint allows users to define custom node types and relationships for their knowledge graph.
            The schema will be validated and stored for use in future memory extractions.

            **Features:**
            - Define custom node types with properties and validation rules
            - Define custom relationship types with constraints
            - Automatic validation against system schemas
            - Support for different scopes (personal, workspace, namespace, organization)
            - **Status control**: Set `status` to "active" to immediately activate the schema, or "draft" to save as draft (default)
            - **Enum support**: Use `enum_values` to restrict property values to a predefined list (max 15 values)
            - **Auto-indexing**: Required properties are automatically indexed in Neo4j when schema becomes active

            **Schema Limits (optimized for LLM performance):**
            - **Maximum 10 node types** per schema
            - **Maximum 20 relationship types** per schema
            - **Maximum 10 properties** per node type
            - **Maximum 15 enum values** per property

            **Property Types & Validation:**
            - `string`: Text values with optional `enum_values`, `min_length`, `max_length`, `pattern`
            - `integer`: Whole numbers with optional `min_value`, `max_value`
            - `float`: Decimal numbers with optional `min_value`, `max_value`
            - `boolean`: True/false values
            - `datetime`: ISO 8601 timestamp strings
            - `array`: Lists of values
            - `object`: Complex nested objects

            **Enum Values:**
            - Add `enum_values` to any string property to restrict values to a predefined list
            - Maximum 15 enum values allowed per property
            - Use with `default` to set a default enum value
            - Example: `"enum_values": ["small", "medium", "large"]`

            **When to Use Enums:**
            - Limited, well-defined options (≤15 values): sizes, statuses, categories, priorities
            - Controlled vocabularies: "active/inactive", "high/medium/low", "bronze/silver/gold"
            - When you want exact matching and no variations

            **When to Avoid Enums:**
            - Open-ended text fields: names, titles, descriptions, addresses
            - Large sets of options (>15): countries, cities, product models
            - When you want semantic similarity matching for entity resolution
            - Dynamic or frequently changing value sets

            **Unique Identifiers & Entity Resolution:**
            - Properties marked as `unique_identifiers` are used for entity deduplication and merging
            - **With enum_values**: Exact matching is used - entities with the same enum value are considered identical
            - **Without enum_values**: Semantic similarity matching is used - entities with similar meanings are automatically merged
            - Example: A "name" unique_identifier without enums will merge "Apple Inc" and "Apple Inc." as the same entity
            - Example: A "sku" unique_identifier with enums will only merge entities with exactly matching SKU codes
            - Use enums for unique_identifiers when you have a limited, predefined set of values (≤15 options)
            - Avoid enums for unique_identifiers when you have broad, open-ended values or >15 possible options
            - **Best practices**: Use enums for controlled vocabularies (status codes, categories), avoid for open text (company names, product titles)
            - **In the example above**: "name" uses semantic similarity (open-ended), "sku" uses exact matching (controlled set)

            **LLM-Friendly Descriptions:**
            - Write detailed property descriptions that guide the LLM on expected formats and usage
            - Include examples of typical values (e.g., "Product name, typically 2-4 words like 'iPhone 15 Pro'")
            - Specify data formats and constraints clearly (e.g., "Price in USD as decimal number")
            - For enums, explain when to use each option (e.g., "use 'new' for brand new items")

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - Content-Type: application/json
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

        Args:
          node_types: Custom node types (max 10 per schema)

          relationship_types: Custom relationship types (max 20 per schema)

          scope: Schema scopes available through the API

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/schemas",
            body=maybe_transform(
                {
                    "name": name,
                    "id": id,
                    "created_at": created_at,
                    "description": description,
                    "last_used_at": last_used_at,
                    "namespace": namespace,
                    "node_types": node_types,
                    "organization": organization,
                    "read_access": read_access,
                    "relationship_types": relationship_types,
                    "scope": scope,
                    "status": status,
                    "updated_at": updated_at,
                    "usage_count": usage_count,
                    "user_id": user_id,
                    "version": version,
                    "workspace_id": workspace_id,
                    "write_access": write_access,
                },
                schema_create_params.SchemaCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SchemaCreateResponse,
        )

    def retrieve(
        self,
        schema_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaRetrieveResponse:
        """
        Get a specific schema by ID.

            Returns the complete schema definition including node types, relationship types,
            and metadata. User must have read access to the schema.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schema_id:
            raise ValueError(f"Expected a non-empty value for `schema_id` but received {schema_id!r}")
        return self._get(
            f"/v1/schemas/{schema_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SchemaRetrieveResponse,
        )

    def update(
        self,
        schema_id: str,
        *,
        body: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaUpdateResponse:
        """
        Update an existing schema.

            Allows modification of schema properties, node types, relationship types, and status.
            User must have write access to the schema. Updates create a new version
            while preserving the existing data.

            **Status Management:**
            - Set `status` to "active" to activate the schema and trigger Neo4j index creation
            - Set `status` to "draft" to deactivate the schema
            - Set `status` to "archived" to soft-delete the schema

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schema_id:
            raise ValueError(f"Expected a non-empty value for `schema_id` but received {schema_id!r}")
        return self._put(
            f"/v1/schemas/{schema_id}",
            body=maybe_transform(body, schema_update_params.SchemaUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SchemaUpdateResponse,
        )

    def list(
        self,
        *,
        status_filter: Optional[str] | Omit = omit,
        workspace_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaListResponse:
        """
        List all schemas accessible to the authenticated user.

            Returns schemas that the user owns or has read access to, including:
            - Personal schemas created by the user
            - Workspace schemas shared within the user's workspace (legacy)
            - Namespace schemas shared within the user's namespace
            - Organization schemas available to the user's organization

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

        Args:
          status_filter: Filter by status (draft, active, deprecated, archived)

          workspace_id: Filter by workspace ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/schemas",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "status_filter": status_filter,
                        "workspace_id": workspace_id,
                    },
                    schema_list_params.SchemaListParams,
                ),
            ),
            cast_to=SchemaListResponse,
        )

    def delete(
        self,
        schema_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Delete a schema.

            Soft deletes the schema by marking it as archived.

        The schema data and
            associated graph nodes/relationships are preserved for data integrity.
            User must have write access to the schema.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schema_id:
            raise ValueError(f"Expected a non-empty value for `schema_id` but received {schema_id!r}")
        return self._delete(
            f"/v1/schemas/{schema_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncSchemasResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSchemasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AsyncSchemasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSchemasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AsyncSchemasResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        id: str | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        description: Optional[str] | Omit = omit,
        last_used_at: Union[str, datetime, None] | Omit = omit,
        namespace: Union[str, Dict[str, object], None] | Omit = omit,
        node_types: Dict[str, schema_create_params.NodeTypes] | Omit = omit,
        organization: Union[str, Dict[str, object], None] | Omit = omit,
        read_access: SequenceNotStr[str] | Omit = omit,
        relationship_types: Dict[str, schema_create_params.RelationshipTypes] | Omit = omit,
        scope: Literal["personal", "workspace", "namespace", "organization"] | Omit = omit,
        status: Literal["draft", "active", "deprecated", "archived"] | Omit = omit,
        updated_at: Union[str, datetime, None] | Omit = omit,
        usage_count: int | Omit = omit,
        user_id: Union[str, Dict[str, object], None] | Omit = omit,
        version: str | Omit = omit,
        workspace_id: Union[str, Dict[str, object], None] | Omit = omit,
        write_access: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaCreateResponse:
        """
        Create a new user-defined graph schema.

            This endpoint allows users to define custom node types and relationships for their knowledge graph.
            The schema will be validated and stored for use in future memory extractions.

            **Features:**
            - Define custom node types with properties and validation rules
            - Define custom relationship types with constraints
            - Automatic validation against system schemas
            - Support for different scopes (personal, workspace, namespace, organization)
            - **Status control**: Set `status` to "active" to immediately activate the schema, or "draft" to save as draft (default)
            - **Enum support**: Use `enum_values` to restrict property values to a predefined list (max 15 values)
            - **Auto-indexing**: Required properties are automatically indexed in Neo4j when schema becomes active

            **Schema Limits (optimized for LLM performance):**
            - **Maximum 10 node types** per schema
            - **Maximum 20 relationship types** per schema
            - **Maximum 10 properties** per node type
            - **Maximum 15 enum values** per property

            **Property Types & Validation:**
            - `string`: Text values with optional `enum_values`, `min_length`, `max_length`, `pattern`
            - `integer`: Whole numbers with optional `min_value`, `max_value`
            - `float`: Decimal numbers with optional `min_value`, `max_value`
            - `boolean`: True/false values
            - `datetime`: ISO 8601 timestamp strings
            - `array`: Lists of values
            - `object`: Complex nested objects

            **Enum Values:**
            - Add `enum_values` to any string property to restrict values to a predefined list
            - Maximum 15 enum values allowed per property
            - Use with `default` to set a default enum value
            - Example: `"enum_values": ["small", "medium", "large"]`

            **When to Use Enums:**
            - Limited, well-defined options (≤15 values): sizes, statuses, categories, priorities
            - Controlled vocabularies: "active/inactive", "high/medium/low", "bronze/silver/gold"
            - When you want exact matching and no variations

            **When to Avoid Enums:**
            - Open-ended text fields: names, titles, descriptions, addresses
            - Large sets of options (>15): countries, cities, product models
            - When you want semantic similarity matching for entity resolution
            - Dynamic or frequently changing value sets

            **Unique Identifiers & Entity Resolution:**
            - Properties marked as `unique_identifiers` are used for entity deduplication and merging
            - **With enum_values**: Exact matching is used - entities with the same enum value are considered identical
            - **Without enum_values**: Semantic similarity matching is used - entities with similar meanings are automatically merged
            - Example: A "name" unique_identifier without enums will merge "Apple Inc" and "Apple Inc." as the same entity
            - Example: A "sku" unique_identifier with enums will only merge entities with exactly matching SKU codes
            - Use enums for unique_identifiers when you have a limited, predefined set of values (≤15 options)
            - Avoid enums for unique_identifiers when you have broad, open-ended values or >15 possible options
            - **Best practices**: Use enums for controlled vocabularies (status codes, categories), avoid for open text (company names, product titles)
            - **In the example above**: "name" uses semantic similarity (open-ended), "sku" uses exact matching (controlled set)

            **LLM-Friendly Descriptions:**
            - Write detailed property descriptions that guide the LLM on expected formats and usage
            - Include examples of typical values (e.g., "Product name, typically 2-4 words like 'iPhone 15 Pro'")
            - Specify data formats and constraints clearly (e.g., "Price in USD as decimal number")
            - For enums, explain when to use each option (e.g., "use 'new' for brand new items")

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - Content-Type: application/json
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

        Args:
          node_types: Custom node types (max 10 per schema)

          relationship_types: Custom relationship types (max 20 per schema)

          scope: Schema scopes available through the API

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/schemas",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "id": id,
                    "created_at": created_at,
                    "description": description,
                    "last_used_at": last_used_at,
                    "namespace": namespace,
                    "node_types": node_types,
                    "organization": organization,
                    "read_access": read_access,
                    "relationship_types": relationship_types,
                    "scope": scope,
                    "status": status,
                    "updated_at": updated_at,
                    "usage_count": usage_count,
                    "user_id": user_id,
                    "version": version,
                    "workspace_id": workspace_id,
                    "write_access": write_access,
                },
                schema_create_params.SchemaCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SchemaCreateResponse,
        )

    async def retrieve(
        self,
        schema_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaRetrieveResponse:
        """
        Get a specific schema by ID.

            Returns the complete schema definition including node types, relationship types,
            and metadata. User must have read access to the schema.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schema_id:
            raise ValueError(f"Expected a non-empty value for `schema_id` but received {schema_id!r}")
        return await self._get(
            f"/v1/schemas/{schema_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SchemaRetrieveResponse,
        )

    async def update(
        self,
        schema_id: str,
        *,
        body: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaUpdateResponse:
        """
        Update an existing schema.

            Allows modification of schema properties, node types, relationship types, and status.
            User must have write access to the schema. Updates create a new version
            while preserving the existing data.

            **Status Management:**
            - Set `status` to "active" to activate the schema and trigger Neo4j index creation
            - Set `status` to "draft" to deactivate the schema
            - Set `status` to "archived" to soft-delete the schema

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schema_id:
            raise ValueError(f"Expected a non-empty value for `schema_id` but received {schema_id!r}")
        return await self._put(
            f"/v1/schemas/{schema_id}",
            body=await async_maybe_transform(body, schema_update_params.SchemaUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SchemaUpdateResponse,
        )

    async def list(
        self,
        *,
        status_filter: Optional[str] | Omit = omit,
        workspace_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaListResponse:
        """
        List all schemas accessible to the authenticated user.

            Returns schemas that the user owns or has read access to, including:
            - Personal schemas created by the user
            - Workspace schemas shared within the user's workspace (legacy)
            - Namespace schemas shared within the user's namespace
            - Organization schemas available to the user's organization

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

        Args:
          status_filter: Filter by status (draft, active, deprecated, archived)

          workspace_id: Filter by workspace ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/schemas",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "status_filter": status_filter,
                        "workspace_id": workspace_id,
                    },
                    schema_list_params.SchemaListParams,
                ),
            ),
            cast_to=SchemaListResponse,
        )

    async def delete(
        self,
        schema_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Delete a schema.

            Soft deletes the schema by marking it as archived.

        The schema data and
            associated graph nodes/relationships are preserved for data integrity.
            User must have write access to the schema.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schema_id:
            raise ValueError(f"Expected a non-empty value for `schema_id` but received {schema_id!r}")
        return await self._delete(
            f"/v1/schemas/{schema_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class SchemasResourceWithRawResponse:
    def __init__(self, schemas: SchemasResource) -> None:
        self._schemas = schemas

        self.create = to_raw_response_wrapper(
            schemas.create,
        )
        self.retrieve = to_raw_response_wrapper(
            schemas.retrieve,
        )
        self.update = to_raw_response_wrapper(
            schemas.update,
        )
        self.list = to_raw_response_wrapper(
            schemas.list,
        )
        self.delete = to_raw_response_wrapper(
            schemas.delete,
        )


class AsyncSchemasResourceWithRawResponse:
    def __init__(self, schemas: AsyncSchemasResource) -> None:
        self._schemas = schemas

        self.create = async_to_raw_response_wrapper(
            schemas.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            schemas.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            schemas.update,
        )
        self.list = async_to_raw_response_wrapper(
            schemas.list,
        )
        self.delete = async_to_raw_response_wrapper(
            schemas.delete,
        )


class SchemasResourceWithStreamingResponse:
    def __init__(self, schemas: SchemasResource) -> None:
        self._schemas = schemas

        self.create = to_streamed_response_wrapper(
            schemas.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            schemas.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            schemas.update,
        )
        self.list = to_streamed_response_wrapper(
            schemas.list,
        )
        self.delete = to_streamed_response_wrapper(
            schemas.delete,
        )


class AsyncSchemasResourceWithStreamingResponse:
    def __init__(self, schemas: AsyncSchemasResource) -> None:
        self._schemas = schemas

        self.create = async_to_streamed_response_wrapper(
            schemas.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            schemas.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            schemas.update,
        )
        self.list = async_to_streamed_response_wrapper(
            schemas.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            schemas.delete,
        )
