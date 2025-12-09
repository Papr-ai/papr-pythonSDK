# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SchemaCreateParams", "NodeTypes", "NodeTypesProperties", "RelationshipTypes", "RelationshipTypesProperties"]


class SchemaCreateParams(TypedDict, total=False):
    name: Required[str]

    id: str

    created_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    description: Optional[str]

    last_used_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    namespace: Union[str, Dict[str, object], None]

    node_types: Dict[str, NodeTypes]
    """Custom node types (max 10 per schema)"""

    organization: Union[str, Dict[str, object], None]

    read_access: SequenceNotStr[str]

    relationship_types: Dict[str, RelationshipTypes]
    """Custom relationship types (max 20 per schema)"""

    scope: Literal["personal", "workspace", "namespace", "organization"]
    """Schema scopes available through the API"""

    status: Literal["draft", "active", "deprecated", "archived"]

    updated_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    usage_count: int

    user_id: Union[str, Dict[str, object], None]

    version: str

    workspace_id: Union[str, Dict[str, object], None]

    write_access: SequenceNotStr[str]


class NodeTypesProperties(TypedDict, total=False):
    """Property definition for nodes/relationships"""

    type: Required[Literal["string", "integer", "float", "boolean", "array", "datetime", "object"]]

    default: object

    description: Optional[str]

    enum_values: Optional[SequenceNotStr[str]]
    """List of allowed enum values (max 15)"""

    max_length: Optional[int]

    max_value: Optional[float]

    min_length: Optional[int]

    min_value: Optional[float]

    pattern: Optional[str]

    required: bool


class NodeTypes(TypedDict, total=False):
    """User-defined node type"""

    label: Required[str]

    name: Required[str]

    color: Optional[str]

    description: Optional[str]

    icon: Optional[str]

    properties: Dict[str, NodeTypesProperties]
    """Node properties (max 10 per node type)"""

    required_properties: SequenceNotStr[str]

    unique_identifiers: SequenceNotStr[str]
    """Properties that uniquely identify this node type.

    Used for MERGE operations to avoid duplicates. Example: ['name', 'email'] for
    Customer nodes.
    """


class RelationshipTypesProperties(TypedDict, total=False):
    """Property definition for nodes/relationships"""

    type: Required[Literal["string", "integer", "float", "boolean", "array", "datetime", "object"]]

    default: object

    description: Optional[str]

    enum_values: Optional[SequenceNotStr[str]]
    """List of allowed enum values (max 15)"""

    max_length: Optional[int]

    max_value: Optional[float]

    min_length: Optional[int]

    min_value: Optional[float]

    pattern: Optional[str]

    required: bool


class RelationshipTypes(TypedDict, total=False):
    """User-defined relationship type"""

    allowed_source_types: Required[SequenceNotStr[str]]

    allowed_target_types: Required[SequenceNotStr[str]]

    label: Required[str]

    name: Required[str]

    cardinality: Literal["one-to-one", "one-to-many", "many-to-many"]

    color: Optional[str]

    description: Optional[str]

    properties: Dict[str, RelationshipTypesProperties]
