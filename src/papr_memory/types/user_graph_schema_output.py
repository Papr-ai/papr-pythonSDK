# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "UserGraphSchemaOutput",
    "NodeTypes",
    "NodeTypesProperties",
    "RelationshipTypes",
    "RelationshipTypesProperties",
]


class NodeTypesProperties(BaseModel):
    type: Literal["string", "integer", "float", "boolean", "array", "datetime", "object"]

    default: Optional[object] = None

    description: Optional[str] = None

    enum_values: Optional[List[str]] = None
    """List of allowed enum values (max 15)"""

    max_length: Optional[int] = None

    max_value: Optional[float] = None

    min_length: Optional[int] = None

    min_value: Optional[float] = None

    pattern: Optional[str] = None

    required: Optional[bool] = None


class NodeTypes(BaseModel):
    label: str

    name: str

    color: Optional[str] = None

    description: Optional[str] = None

    icon: Optional[str] = None

    properties: Optional[Dict[str, NodeTypesProperties]] = None
    """Node properties (max 10 per node type)"""

    required_properties: Optional[List[str]] = None

    unique_identifiers: Optional[List[str]] = None
    """Properties that uniquely identify this node type.

    Used for MERGE operations to avoid duplicates. Example: ['name', 'email'] for
    Customer nodes.
    """


class RelationshipTypesProperties(BaseModel):
    type: Literal["string", "integer", "float", "boolean", "array", "datetime", "object"]

    default: Optional[object] = None

    description: Optional[str] = None

    enum_values: Optional[List[str]] = None
    """List of allowed enum values (max 15)"""

    max_length: Optional[int] = None

    max_value: Optional[float] = None

    min_length: Optional[int] = None

    min_value: Optional[float] = None

    pattern: Optional[str] = None

    required: Optional[bool] = None


class RelationshipTypes(BaseModel):
    allowed_source_types: List[str]

    allowed_target_types: List[str]

    label: str

    name: str

    cardinality: Optional[Literal["one-to-one", "one-to-many", "many-to-many"]] = None

    color: Optional[str] = None

    description: Optional[str] = None

    properties: Optional[Dict[str, RelationshipTypesProperties]] = None


class UserGraphSchemaOutput(BaseModel):
    name: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    description: Optional[str] = None

    last_used_at: Optional[datetime] = None

    namespace: Union[str, Dict[str, object], None] = None

    node_types: Optional[Dict[str, NodeTypes]] = None
    """Custom node types (max 10 per schema)"""

    organization: Union[str, Dict[str, object], None] = None

    read_access: Optional[List[str]] = None

    relationship_types: Optional[Dict[str, RelationshipTypes]] = None
    """Custom relationship types (max 20 per schema)"""

    scope: Optional[Literal["personal", "workspace", "namespace", "organization"]] = None
    """Schema scopes available through the API"""

    status: Optional[Literal["draft", "active", "deprecated", "archived"]] = None

    updated_at: Optional[datetime] = None

    usage_count: Optional[int] = None

    user_id: Union[str, Dict[str, object], None] = None

    version: Optional[str] = None

    workspace_id: Union[str, Dict[str, object], None] = None

    write_access: Optional[List[str]] = None
