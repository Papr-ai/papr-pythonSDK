# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .property_value import PropertyValue
from .search_config_input import SearchConfigInput

__all__ = ["NodeConstraintInput", "Set"]

Set: TypeAlias = Union[str, float, bool, List[object], Dict[str, object], PropertyValue]


class NodeConstraintInput(BaseModel):
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

    search: Optional[SearchConfigInput] = None
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

    set: Optional[Dict[str, Set]] = None
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
