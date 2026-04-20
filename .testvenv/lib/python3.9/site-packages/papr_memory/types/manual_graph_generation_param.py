# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ManualGraphGenerationParam", "Node", "Relationship"]


class Node(TypedDict, total=False):
    """Developer-specified node for graph override.

    IMPORTANT:
    - 'id' is REQUIRED (relationships reference nodes by these IDs)
    - 'label' must match a node type from your registered UserGraphSchema
    - 'properties' must include ALL required fields from your schema definition

    📋 Schema Management:
    - Register schemas: POST /v1/schemas
    - View your schemas: GET /v1/schemas
    """

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


class Relationship(TypedDict, total=False):
    """Developer-specified relationship for graph override.

    IMPORTANT:
    - source_node_id MUST exactly match a node 'id' from the 'nodes' array
    - target_node_id MUST exactly match a node 'id' from the 'nodes' array
    - relationship_type MUST exist in your registered UserGraphSchema
    """

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


class ManualGraphGenerationParam(TypedDict, total=False):
    """Complete manual control over graph structure"""

    nodes: Required[Iterable[Node]]
    """Exact nodes to create"""

    relationships: Iterable[Relationship]
    """Exact relationships to create"""
