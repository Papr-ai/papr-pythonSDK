# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .property_definition import PropertyDefinition
from .search_config_output import SearchConfigOutput
from .shared.property_value import PropertyValue

__all__ = [
    "UserGraphSchemaOutput",
    "NodeTypes",
    "NodeTypesConstraint",
    "NodeTypesConstraintSet",
    "RelationshipTypes",
    "RelationshipTypesConstraint",
    "RelationshipTypesConstraintSet",
]

NodeTypesConstraintSet: TypeAlias = Union[str, float, bool, List[object], Dict[str, object], PropertyValue]


class NodeTypesConstraint(BaseModel):
    """Policy for how nodes of a specific type should be handled.

    Used in two places:
    1. **Schema level**: Inside `UserNodeType.constraint` - `node_type` is implicit from parent
    2. **Memory level**: In `memory_policy.node_constraints[]` - `node_type` is required

    Node constraints allow developers to control:
    - Which node types can be created vs. linked
    - How to find/select existing nodes (via `search`)
    - What property values to set (exact or auto-extracted)
    - When to apply the constraint (conditional with logical operators)

    **The `search` field** handles node selection:
    - Uses PropertyMatch list to define unique identifiers and matching strategy
    - Example: `{"properties": [{"name": "id", "mode": "exact"}, {"name": "title", "mode": "semantic"}]}`
    - For direct selection, use PropertyMatch with value: `{"name": "id", "mode": "exact", "value": "proj_123"}`

    **The `set` field** controls property values:
    - Exact value: `{"status": "done"}` - sets exact value
    - Auto-extract: `{"status": {"mode": "auto"}}` - LLM extracts from content

    **The `when` field** supports logical operators:
    - Simple: `{"priority": "high"}`
    - AND: `{"_and": [{"priority": "high"}, {"status": "active"}]}`
    - OR: `{"_or": [{"status": "active"}, {"status": "pending"}]}`
    - NOT: `{"_not": {"status": "completed"}}`
    - Complex: `{"_and": [{"priority": "high"}, {"_or": [{"status": "active"}, {"urgent": true}]}]}`
    """

    create: Optional[Literal["upsert", "lookup", "auto", "never"]] = None
    """'upsert': Create if not found via search (default).

    'lookup': Only link to existing nodes (controlled vocabulary). Deprecated
    aliases: 'auto' -> 'upsert', 'never' -> 'lookup'.
    """

    link_only: Optional[bool] = None
    """DEPRECATED: Use create='lookup' instead.

    Shorthand for create='lookup'. When True, only links to existing nodes
    (controlled vocabulary). Equivalent to @lookup decorator in schema definitions.
    """

    node_type: Optional[str] = None
    """Node type this constraint applies to (e.g., 'Task', 'Project', 'Person').

    Optional at schema level (implicit from parent UserNodeType), required at memory
    level (in memory_policy.node_constraints).
    """

    on_miss: Optional[Literal["create", "ignore", "error"]] = None
    """Explicit behavior when no match found via search.

    'create': create new node (same as upsert). 'ignore': skip node creation (same
    as lookup). 'error': raise error if node not found. If specified, overrides
    'create' field.
    """

    search: Optional[SearchConfigOutput] = None
    """Configuration for finding/selecting existing nodes.

    Defines which properties to match on and how, in priority order. The first
    matching property wins.

    **String Shorthand** (simple cases - converts to exact match):
    SearchConfig(properties=["id", "email"]) # Equivalent to:
    SearchConfig(properties=[PropertyMatch.exact("id"),
    PropertyMatch.exact("email")])

    **Mixed Form** (combine strings and PropertyMatch): SearchConfig(properties=[
    "id", # String -> exact match PropertyMatch.semantic("title", 0.9) # Full
    control ])

    **Full Form** (maximum control): SearchConfig(properties=[
    PropertyMatch(name="id", mode="exact"), PropertyMatch(name="title",
    mode="semantic", threshold=0.85) ])

    **To select a specific node by ID**:
    SearchConfig(properties=[PropertyMatch.exact("id", "TASK-123")])
    """

    set: Optional[Dict[str, NodeTypesConstraintSet]] = None
    """Set property values on nodes.

    Supports: 1. Exact value: {'status': 'done'} - sets exact value. 2.
    Auto-extract: {'status': {'mode': 'auto'}} - LLM extracts from content. 3. Text
    mode: {'summary': {'mode': 'auto', 'text_mode': 'merge'}} - controls text
    updates. For text properties, text_mode can be 'replace', 'append', or 'merge'.
    """

    when: Optional[Dict[str, object]] = None
    """Condition for when this constraint applies.

    Supports logical operators: '\\__and', '\\__or', '\\__not'. Examples: Simple:
    {'priority': 'high'} - matches when priority equals 'high'. AND: {'\\__and':
    [{'priority': 'high'}, {'status': 'active'}]} - all must match. OR: {'\\__or':
    [{'status': 'active'}, {'status': 'pending'}]} - any must match. NOT: {'\\__not':
    {'status': 'completed'}} - negation. Complex: {'\\__and': [{'priority': 'high'},
    {'\\__or': [{'status': 'active'}, {'urgent': true}]}]}
    """


class NodeTypes(BaseModel):
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

    label: str

    name: str

    color: Optional[str] = None

    constraint: Optional[NodeTypesConstraint] = None
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

    description: Optional[str] = None

    icon: Optional[str] = None

    link_only: Optional[bool] = None
    """DEPRECATED: Use resolution_policy='lookup' instead.

    Shorthand for constraint with create='lookup'. When True, only links to existing
    nodes (controlled vocabulary). Equivalent to @lookup decorator. If constraint is
    also provided, link_only=True will override constraint.create to 'lookup'.
    """

    properties: Optional[Dict[str, PropertyDefinition]] = None
    """Node properties (max 10 per node type)"""

    required_properties: Optional[List[str]] = None

    resolution_policy: Optional[Literal["upsert", "lookup"]] = None
    """Shorthand for constraint.create.

    'upsert': Create if not found (default). 'lookup': Only link to existing nodes
    (controlled vocabulary). Equivalent to @upsert/@lookup decorators. If constraint
    is also provided, resolution_policy will set constraint.create accordingly.
    """

    unique_identifiers: Optional[List[str]] = None
    """DEPRECATED: Use 'constraint.search.properties' instead.

    Properties that uniquely identify this node type. Example: ['name', 'email'] for
    Customer nodes.
    """


RelationshipTypesConstraintSet: TypeAlias = Union[str, float, bool, List[object], Dict[str, object], PropertyValue]


class RelationshipTypesConstraint(BaseModel):
    """Policy for how edges/relationships of a specific type should be handled.

    Used in two places:
    1. **Schema level**: Inside `UserRelationshipType.constraint` - `edge_type` is implicit from parent
    2. **Memory level**: In `memory_policy.edge_constraints[]` - `edge_type` is required

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

    create: Optional[Literal["upsert", "lookup", "auto", "never"]] = None
    """'upsert': Create target node if not found via search (default).

    'lookup': Only link to existing target nodes (controlled vocabulary). When
    'lookup', edges to non-existing targets are skipped. Deprecated aliases: 'auto'
    -> 'upsert', 'never' -> 'lookup'.
    """

    direction: Optional[Literal["outgoing", "incoming", "both"]] = None
    """Direction of edges this constraint applies to.

    'outgoing': edges where current node is source (default). 'incoming': edges
    where current node is target. 'both': applies in either direction.
    """

    edge_type: Optional[str] = None
    """
    Edge/relationship type this constraint applies to (e.g., 'MITIGATES',
    'ASSIGNED_TO'). Optional at schema level (implicit from parent
    UserRelationshipType), required at memory level (in
    memory_policy.edge_constraints).
    """

    link_only: Optional[bool] = None
    """DEPRECATED: Use create='lookup' instead.

    Shorthand for create='lookup'. When True, only links to existing target nodes.
    Equivalent to @lookup decorator in schema definitions.
    """

    on_miss: Optional[Literal["create", "ignore", "error"]] = None
    """Explicit behavior when no target match found via search.

    'create': create new target node (same as upsert). 'ignore': skip edge creation
    (same as lookup). 'error': raise error if target not found. If specified,
    overrides 'create' field.
    """

    search: Optional[SearchConfigOutput] = None
    """Configuration for finding/selecting existing nodes.

    Defines which properties to match on and how, in priority order. The first
    matching property wins.

    **String Shorthand** (simple cases - converts to exact match):
    SearchConfig(properties=["id", "email"]) # Equivalent to:
    SearchConfig(properties=[PropertyMatch.exact("id"),
    PropertyMatch.exact("email")])

    **Mixed Form** (combine strings and PropertyMatch): SearchConfig(properties=[
    "id", # String -> exact match PropertyMatch.semantic("title", 0.9) # Full
    control ])

    **Full Form** (maximum control): SearchConfig(properties=[
    PropertyMatch(name="id", mode="exact"), PropertyMatch(name="title",
    mode="semantic", threshold=0.85) ])

    **To select a specific node by ID**:
    SearchConfig(properties=[PropertyMatch.exact("id", "TASK-123")])
    """

    set: Optional[Dict[str, RelationshipTypesConstraintSet]] = None
    """Set property values on edges.

    Supports: 1. Exact value: {'weight': 1.0} - sets exact value. 2. Auto-extract:
    {'reason': {'mode': 'auto'}} - LLM extracts from content. Edge properties are
    useful for relationship metadata (weight, timestamp, reason, etc.).
    """

    source_type: Optional[str] = None
    """Filter: only apply when source node is of this type.

    Example: source_type='SecurityBehavior' - only applies to edges from
    SecurityBehavior nodes.
    """

    target_type: Optional[str] = None
    """Filter: only apply when target node is of this type.

    Example: target_type='TacticDef' - only applies to edges targeting TacticDef
    nodes.
    """

    when: Optional[Dict[str, object]] = None
    """Condition for when this constraint applies.

    Supports logical operators: '\\__and', '\\__or', '\\__not'. Applied to edge properties
    or context. Example: {'\\__and': [{'severity': 'high'}, {'_not': {'status':
    'deprecated'}}]}
    """


class RelationshipTypes(BaseModel):
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

    allowed_source_types: List[str]

    allowed_target_types: List[str]

    label: str

    name: str

    cardinality: Optional[Literal["one-to-one", "one-to-many", "many-to-many"]] = None

    color: Optional[str] = None

    constraint: Optional[RelationshipTypesConstraint] = None
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

    description: Optional[str] = None

    link_only: Optional[bool] = None
    """DEPRECATED: Use resolution_policy='lookup' instead.

    Shorthand for constraint with create='lookup'. When True, only links to existing
    target nodes (controlled vocabulary). Equivalent to @lookup decorator. If
    constraint is also provided, link_only=True will override constraint.create to
    'lookup'.
    """

    properties: Optional[Dict[str, PropertyDefinition]] = None

    resolution_policy: Optional[Literal["upsert", "lookup"]] = None
    """Shorthand for constraint.create.

    'upsert': Create target if not found (default). 'lookup': Only link to existing
    targets (controlled vocabulary). Equivalent to @upsert/@lookup decorators. If
    constraint is also provided, resolution_policy will set constraint.create
    accordingly.
    """


class UserGraphSchemaOutput(BaseModel):
    """Complete user-defined graph schema"""

    name: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    description: Optional[str] = None

    last_used_at: Optional[datetime] = None

    memory_policy: Optional[Dict[str, object]] = None
    """Default memory policy for memories using this schema.

    Includes mode ('auto', 'manual'), node_constraints (applied in auto mode when
    present), and OMO safety settings (consent, risk). Memory-level policies
    override schema-level.
    """

    namespace: Union[str, Dict[str, object], None] = None
    """DEPRECATED: Use 'namespace_id' instead. Accepts Parse pointer or objectId."""

    namespace_id: Optional[str] = None
    """Namespace ID this schema belongs to. Accepts legacy 'namespace' alias."""

    node_types: Optional[Dict[str, NodeTypes]] = None
    """Custom node types (max 10 per schema)"""

    organization: Union[str, Dict[str, object], None] = None
    """DEPRECATED: Use 'organization_id' instead. Accepts Parse pointer or objectId."""

    organization_id: Optional[str] = None
    """Organization ID this schema belongs to. Accepts legacy 'organization' alias."""

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
