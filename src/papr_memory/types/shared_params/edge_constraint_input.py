# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, TypeAlias, TypedDict

from .property_value import PropertyValue
from .search_config_input import SearchConfigInput

__all__ = ["EdgeConstraintInput", "Set"]

Set: TypeAlias = Union[str, float, bool, Iterable[object], Dict[str, object], PropertyValue]


class EdgeConstraintInput(TypedDict, total=False):
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

    create: Literal["upsert", "lookup", "auto", "never"]
    """'upsert': Create target node if not found via search (default).

    'lookup': Only link to existing target nodes (controlled vocabulary). When
    'lookup', edges to non-existing targets are skipped. Deprecated aliases: 'auto'
    -> 'upsert', 'never' -> 'lookup'.
    """

    direction: Literal["outgoing", "incoming", "both"]
    """Direction of edges this constraint applies to.

    'outgoing': edges where current node is source (default). 'incoming': edges
    where current node is target. 'both': applies in either direction.
    """

    edge_type: Optional[str]
    """
    Edge/relationship type this constraint applies to (e.g., 'MITIGATES',
    'ASSIGNED_TO'). Optional at schema level (implicit from parent
    UserRelationshipType), required at memory level (in
    memory_policy.edge_constraints).
    """

    link_only: bool
    """DEPRECATED: Use create='lookup' instead.

    Shorthand for create='lookup'. When True, only links to existing target nodes.
    Equivalent to @lookup decorator in schema definitions.
    """

    on_miss: Optional[Literal["create", "ignore", "error"]]
    """Explicit behavior when no target match found via search.

    'create': create new target node (same as upsert). 'ignore': skip edge creation
    (same as lookup). 'error': raise error if target not found. If specified,
    overrides 'create' field.
    """

    search: Optional[SearchConfigInput]
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

    set: Optional[Dict[str, Set]]
    """Set property values on edges.

    Supports: 1. Exact value: {'weight': 1.0} - sets exact value. 2. Auto-extract:
    {'reason': {'mode': 'auto'}} - LLM extracts from content. Edge properties are
    useful for relationship metadata (weight, timestamp, reason, etc.).
    """

    source_type: Optional[str]
    """Filter: only apply when source node is of this type.

    Example: source_type='SecurityBehavior' - only applies to edges from
    SecurityBehavior nodes.
    """

    target_type: Optional[str]
    """Filter: only apply when target node is of this type.

    Example: target_type='TacticDef' - only applies to edges targeting TacticDef
    nodes.
    """

    when: Optional[Dict[str, object]]
    """Condition for when this constraint applies.

    Supports logical operators: '\\__and', '\\__or', '\\__not'. Applied to edge properties
    or context. Example: {'\\__and': [{'severity': 'high'}, {'_not': {'status':
    'deprecated'}}]}
    """
