# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .memory_type import MemoryType
from .context_item_param import ContextItemParam
from .memory_metadata_param import MemoryMetadataParam
from .relationship_item_param import RelationshipItemParam

__all__ = [
    "MemoryAddParams",
    "GraphGeneration",
    "GraphGenerationAuto",
    "GraphGenerationAutoPropertyOverride",
    "GraphGenerationManual",
    "GraphGenerationManualNode",
    "GraphGenerationManualRelationship",
]


class MemoryAddParams(TypedDict, total=False):
    content: Required[str]
    """The content of the memory item you want to add to memory"""

    skip_background_processing: bool
    """If True, skips adding background tasks for processing"""

    context: Optional[Iterable[ContextItemParam]]
    """Context can be conversation history or any relevant context for a memory item"""

    graph_generation: Optional[GraphGeneration]
    """Graph generation configuration"""

    metadata: Optional[MemoryMetadataParam]
    """Metadata for memory request"""

    namespace_id: Optional[str]
    """Optional namespace ID for multi-tenant memory scoping.

    When provided, memory is associated with this namespace.
    """

    organization_id: Optional[str]
    """Optional organization ID for multi-tenant memory scoping.

    When provided, memory is associated with this organization.
    """

    relationships_json: Optional[Iterable[RelationshipItemParam]]
    """Array of relationships that we can use in Graph DB (neo4J)"""

    type: MemoryType
    """Memory item type; defaults to 'text' if omitted"""


class GraphGenerationAutoPropertyOverride(TypedDict, total=False):
    node_label: Required[Annotated[str, PropertyInfo(alias="nodeLabel")]]
    """Node type to apply overrides to (e.g., 'User', 'SecurityBehavior')"""

    set: Required[Dict[str, object]]
    """Properties to set/override on matching nodes"""

    match: Optional[Dict[str, object]]
    """Optional conditions that must be met for override to apply.

    If not provided, applies to all nodes of this type
    """


class GraphGenerationAuto(TypedDict, total=False):
    property_overrides: Optional[Iterable[GraphGenerationAutoPropertyOverride]]
    """Override specific property values in AI-generated nodes with match conditions"""

    schema_id: Optional[str]
    """Force AI to use this specific schema instead of auto-selecting"""

    simple_schema_mode: bool
    """Limit AI to system + one user schema for consistency"""


class GraphGenerationManualNode(TypedDict, total=False):
    id: Required[str]
    """**REQUIRED**: Unique identifier for this node.

    Must be unique within this request. Relationships reference this via
    source_node_id/target_node_id. Example: 'person_john_123',
    'finding_cve_2024_1234'
    """

    label: Required[str]
    """**REQUIRED**: Node type from your UserGraphSchema.

    View available types at GET /v1/schemas. System types: Memory, Person, Company,
    Project, Task, Insight, Meeting, Opportunity, Code
    """

    properties: Required[Dict[str, object]]
    """**REQUIRED**: Node properties matching your UserGraphSchema definition.

    Must include: (1) All required properties from your schema, (2)
    unique_identifiers if defined (e.g., 'email' for Person) to enable MERGE
    deduplication. View schema requirements at GET /v1/schemas
    """


class GraphGenerationManualRelationship(TypedDict, total=False):
    relationship_type: Required[str]
    """**REQUIRED**: Relationship type from your UserGraphSchema.

    View available types at GET /v1/schemas. System types: WORKS_FOR, WORKS_ON,
    HAS_PARTICIPANT, DISCUSSES, MENTIONS, RELATES_TO, CREATED_BY
    """

    source_node_id: Required[str]
    """
    **REQUIRED**: Must exactly match the 'id' field of a node defined in the 'nodes'
    array of this request
    """

    target_node_id: Required[str]
    """
    **REQUIRED**: Must exactly match the 'id' field of a node defined in the 'nodes'
    array of this request
    """

    properties: Optional[Dict[str, object]]
    """
    Optional relationship properties (e.g., {'since': '2024-01-01', 'role':
    'manager'})
    """


class GraphGenerationManual(TypedDict, total=False):
    nodes: Required[Iterable[GraphGenerationManualNode]]
    """Exact nodes to create"""

    relationships: Iterable[GraphGenerationManualRelationship]
    """Exact relationships to create"""


class GraphGeneration(TypedDict, total=False):
    auto: Optional[GraphGenerationAuto]
    """AI-powered graph generation with optional guidance"""

    manual: Optional[GraphGenerationManual]
    """Complete manual control over graph structure"""

    mode: Literal["auto", "manual"]
    """Graph generation mode: 'auto' (AI-powered) or 'manual' (exact specification)"""
