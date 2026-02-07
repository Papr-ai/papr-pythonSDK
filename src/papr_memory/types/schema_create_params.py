# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .property_definition_param import PropertyDefinitionParam
from .shared_params.edge_constraint_input import EdgeConstraintInput
from .shared_params.node_constraint_input import NodeConstraintInput

__all__ = ["SchemaCreateParams", "NodeTypes", "RelationshipTypes"]


class SchemaCreateParams(TypedDict, total=False):
    name: Required[str]

    id: str

    created_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    description: Optional[str]

    last_used_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    memory_policy: Optional[Dict[str, object]]
    """Default memory policy for memories using this schema.

    Includes mode ('auto', 'manual'), node_constraints (applied in auto mode when
    present), and OMO safety settings (consent, risk). Memory-level policies
    override schema-level.
    """

    namespace: Union[str, Dict[str, object], None]
    """DEPRECATED: Use 'namespace_id' instead. Accepts Parse pointer or objectId."""

    namespace_id: Optional[str]
    """Namespace ID this schema belongs to. Accepts legacy 'namespace' alias."""

    node_types: Dict[str, NodeTypes]
    """Custom node types (max 10 per schema)"""

    organization: Union[str, Dict[str, object], None]
    """DEPRECATED: Use 'organization_id' instead. Accepts Parse pointer or objectId."""

    organization_id: Optional[str]
    """Organization ID this schema belongs to. Accepts legacy 'organization' alias."""

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


class NodeTypes(TypedDict, total=False):
    """User-defined node type with optional inline constraint.

    The `constraint` field allows defining default matching/creation behavior
    directly within the node type definition. This replaces the need to put
    constraints only in memory_policy.node_constraints.

    Schema-level constraints:
    - `node_type` is implicit (taken from parent UserNodeType.name)
    - Defines default matching strategy via `search.properties`
    - Can be overridden per-memory via memory_policy.node_constraints

    Example:
        UserNodeType(
            name="Task",
            label="Task",
            properties={
                "id": PropertyDefinition(type="string"),
                "title": PropertyDefinition(type="string", required=True)
            },
            constraint=NodeConstraint(
                search=SearchConfig(properties=[
                    PropertyMatch(name="id", mode="exact"),
                    PropertyMatch(name="title", mode="semantic", threshold=0.85)
                ]),
                create="auto"
            )
        )
    """

    label: Required[str]

    name: Required[str]

    color: Optional[str]

    constraint: Optional[NodeConstraintInput]
    """Policy for how nodes of a specific type should be handled.

    Used in two places:

    1. **Schema level**: Inside `UserNodeType.constraint` - `node_type` is implicit
       from parent
    2. **Memory level**: In `memory_policy.node_constraints[]` - `node_type` is
       required

    Node constraints allow developers to control:

    - Which node types can be created vs. linked
    - How to find/select existing nodes (via `search`)
    - What property values to set (exact or auto-extracted)
    - When to apply the constraint (conditional with logical operators)

    **The `search` field** handles node selection:

    - Uses PropertyMatch list to define unique identifiers and matching strategy
    - Example:
      `{"properties": [{"name": "id", "mode": "exact"}, {"name": "title", "mode": "semantic"}]}`
    - For direct selection, use PropertyMatch with value:
      `{"name": "id", "mode": "exact", "value": "proj_123"}`

    **The `set` field** controls property values:

    - Exact value: `{"status": "done"}` - sets exact value
    - Auto-extract: `{"status": {"mode": "auto"}}` - LLM extracts from content

    **The `when` field** supports logical operators:

    - Simple: `{"priority": "high"}`
    - AND: `{"_and": [{"priority": "high"}, {"status": "active"}]}`
    - OR: `{"_or": [{"status": "active"}, {"status": "pending"}]}`
    - NOT: `{"_not": {"status": "completed"}}`
    - Complex:
      `{"_and": [{"priority": "high"}, {"_or": [{"status": "active"}, {"urgent": true}]}]}`
    """

    description: Optional[str]

    icon: Optional[str]

    link_only: bool
    """DEPRECATED: Use resolution_policy='lookup' instead.

    Shorthand for constraint with create='lookup'. When True, only links to existing
    nodes (controlled vocabulary). Equivalent to @lookup decorator. If constraint is
    also provided, link_only=True will override constraint.create to 'lookup'.
    """

    properties: Dict[str, PropertyDefinitionParam]
    """Node properties (max 10 per node type)"""

    required_properties: SequenceNotStr[str]

    resolution_policy: Literal["upsert", "lookup"]
    """Shorthand for constraint.create.

    'upsert': Create if not found (default). 'lookup': Only link to existing nodes
    (controlled vocabulary). Equivalent to @upsert/@lookup decorators. If constraint
    is also provided, resolution_policy will set constraint.create accordingly.
    """

    unique_identifiers: SequenceNotStr[str]
    """DEPRECATED: Use 'constraint.search.properties' instead.

    Properties that uniquely identify this node type. Example: ['name', 'email'] for
    Customer nodes.
    """


class RelationshipTypes(TypedDict, total=False):
    """User-defined relationship type with optional inline constraint.

    The `constraint` field allows defining default matching/creation behavior
    directly within the relationship type definition. This mirrors the pattern
    used in UserNodeType.constraint for nodes.

    Schema-level edge constraints:
    - `edge_type` is implicit (taken from parent UserRelationshipType.name)
    - Defines default target node matching strategy via `search.properties`
    - Can be overridden per-memory via memory_policy.edge_constraints

    Example:
        UserRelationshipType(
            name="MITIGATES",
            label="Mitigates",
            allowed_source_types=["SecurityBehavior"],
            allowed_target_types=["TacticDef"],
            constraint=EdgeConstraint(
                search=SearchConfig(properties=[
                    PropertyMatch(name="name", mode="semantic", threshold=0.90)
                ]),
                create="never"  # Controlled vocabulary - only link to existing targets
            )
        )
    """

    allowed_source_types: Required[SequenceNotStr[str]]

    allowed_target_types: Required[SequenceNotStr[str]]

    label: Required[str]

    name: Required[str]

    cardinality: Literal["one-to-one", "one-to-many", "many-to-many"]

    color: Optional[str]

    constraint: Optional[EdgeConstraintInput]
    """Policy for how edges/relationships of a specific type should be handled.

    Used in two places:

    1. **Schema level**: Inside `UserRelationshipType.constraint` - `edge_type` is
       implicit from parent
    2. **Memory level**: In `memory_policy.edge_constraints[]` - `edge_type` is
       required

    Edge constraints allow developers to control:

    - Which edge types can be created vs. linked to existing targets
    - How to find/select target nodes (via `search`)
    - What edge property values to set (exact or auto-extracted)
    - When to apply the constraint (conditional with logical operators)
    - Filter by source/target node types

    **The `search` field** handles target node selection:

    - Uses SearchConfig to define how to find existing target nodes
    - Example: `{"properties": [{"name": "name", "mode": "semantic"}]}`
    - For controlled vocabulary: find existing target, don't create new

    **The `set` field** controls edge property values:

    - Exact value: `{"weight": 1.0}` - sets exact value
    - Auto-extract: `{"reason": {"mode": "auto"}}` - LLM extracts from content

    **The `when` field** supports logical operators (same as NodeConstraint):

    - Simple: `{"severity": "high"}`
    - AND: `{"_and": [{"severity": "high"}, {"confirmed": true}]}`
    - OR: `{"_or": [{"type": "MITIGATES"}, {"type": "PREVENTS"}]}`
    - NOT: `{"_not": {"status": "deprecated"}}`
    """

    description: Optional[str]

    link_only: bool
    """DEPRECATED: Use resolution_policy='lookup' instead.

    Shorthand for constraint with create='lookup'. When True, only links to existing
    target nodes (controlled vocabulary). Equivalent to @lookup decorator. If
    constraint is also provided, link_only=True will override constraint.create to
    'lookup'.
    """

    properties: Dict[str, PropertyDefinitionParam]

    resolution_policy: Literal["upsert", "lookup"]
    """Shorthand for constraint.create.

    'upsert': Create target if not found (default). 'lookup': Only link to existing
    targets (controlled vocabulary). Equivalent to @upsert/@lookup decorators. If
    constraint is also provided, resolution_policy will set constraint.create
    accordingly.
    """
