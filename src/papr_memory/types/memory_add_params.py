# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .memory_type import MemoryType
from .context_item_param import ContextItemParam
from .memory_metadata_param import MemoryMetadataParam
from .graph_generation_param import GraphGenerationParam
from .relationship_item_param import RelationshipItemParam

__all__ = [
    "MemoryAddParams",
    "MemoryPolicy",
    "MemoryPolicyACL",
    "MemoryPolicyEdgeConstraint",
    "MemoryPolicyEdgeConstraintSearch",
    "MemoryPolicyEdgeConstraintSearchProperty",
    "MemoryPolicyEdgeConstraintSet",
    "MemoryPolicyEdgeConstraintSetPropertyValue",
    "MemoryPolicyNodeConstraint",
    "MemoryPolicyNodeConstraintSearch",
    "MemoryPolicyNodeConstraintSearchProperty",
    "MemoryPolicyNodeConstraintSet",
    "MemoryPolicyNodeConstraintSetPropertyValue",
    "MemoryPolicyNode",
    "MemoryPolicyRelationship",
]


class MemoryAddParams(TypedDict, total=False):
    content: Required[str]
    """The content of the memory item you want to add to memory"""

    enable_holographic: bool
    """
    If True, applies holographic neural transforms and stores in holographic
    collection
    """

    format: Optional[str]
    """Response format.

    Use 'omo' for Open Memory Object standard format (portable across platforms).
    """

    skip_background_processing: bool
    """If True, skips adding background tasks for processing"""

    context: Optional[Iterable[ContextItemParam]]
    """Conversation history context for this memory.

    Use for providing message history when adding a memory. Format: [{role:
    'user'|'assistant', content: '...'}]
    """

    external_user_id: Optional[str]
    """Your application's user identifier.

    This is the primary way to identify users. Use this for your app's user IDs
    (e.g., 'user_alice_123', UUID, email). Papr will automatically resolve or create
    internal users as needed.
    """

    graph_generation: Optional[GraphGenerationParam]
    """Graph generation configuration"""

    link_to: Union[str, SequenceNotStr[str], Dict[str, object], None]
    """Shorthand DSL for node/edge constraints.

    Expands to memory_policy.node_constraints and edge_constraints. Formats: -
    String: 'Task:title' (semantic match on Task.title) - List: ['Task:title',
    'Person:email'] (multiple constraints) - Dict: {'Task:title': {'set': {...}}}
    (with options) Syntax: - Node: 'Type:property', 'Type:prop=value' (exact),
    'Type:prop~value' (semantic) - Edge: 'Source->EDGE->Target:property' (arrow
    syntax) - Via: 'Type.via(EDGE->Target:prop)' (relationship traversal) - Special:
    '$this', '$previous', '$context:N' Example:
    'SecurityBehavior->MITIGATES->TacticDef:name' with {'create': 'never'}
    """

    memory_policy: Optional[MemoryPolicy]
    """Unified memory processing policy.

    This is the SINGLE source of truth for how a memory should be processed,
    combining graph generation control AND OMO (Open Memory Object) safety
    standards.

    **Graph Generation Modes:**

    - auto: LLM extracts entities freely (default)
    - manual: Developer provides exact nodes (no LLM extraction)

    **OMO Safety Standards:**

    - consent: How data owner allowed storage (explicit, implicit, terms, none)
    - risk: Safety assessment (none, sensitive, flagged)
    - acl: Access control list for read/write permissions

    **Schema Integration:**

    - schema_id: Reference a schema that may have its own default memory_policy
    - Schema-level policies are merged with request-level (request takes precedence)
    """

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
    """DEPRECATED: Use 'memory_policy' instead.

    Migration options: 1. Specific memory: relationships=[{source: '$this', target:
    'mem_123', type: 'FOLLOWS'}] 2. Previous memory: link_to_previous_memory=True 3.
    Related memories: link_to_related_memories=3
    """

    type: MemoryType
    """Memory item type; defaults to 'text' if omitted"""

    user_id: Optional[str]
    """DEPRECATED: Use 'external_user_id' instead.

    Internal Papr Parse user ID. Most developers should not use this field directly.
    """


class MemoryPolicyACL(TypedDict, total=False):
    """Simplified Access Control List configuration.

    Aligned with Open Memory Object (OMO) standard.
    See: https://github.com/anthropics/open-memory-object

    **Supported Entity Prefixes:**

    | Prefix | Description | Validation |
    |--------|-------------|------------|
    | `user:` | Internal Papr user ID | Validated against Parse users |
    | `external_user:` | Your app's user ID | Not validated (your responsibility) |
    | `organization:` | Organization ID | Validated against your organizations |
    | `namespace:` | Namespace ID | Validated against your namespaces |
    | `workspace:` | Workspace ID | Validated against your workspaces |
    | `role:` | Parse role ID | Validated against your roles |

    **Examples:**
    ```python
    acl = ACLConfig(read=["external_user:alice_123", "organization:org_acme"], write=["external_user:alice_123"])
    ```

    **Validation Rules:**
    - Internal entities (user, organization, namespace, workspace, role) are validated
    - External entities (external_user) are NOT validated - your app is responsible
    - Invalid internal entities will return an error
    - Unprefixed values default to `external_user:` for backwards compatibility
    """

    read: SequenceNotStr[str]
    """Entity IDs that can read this memory.

    Format: 'prefix:id' (e.g., 'external_user:alice', 'organization:org_123').
    Supported prefixes: user, external_user, organization, namespace, workspace,
    role. Unprefixed values treated as external_user for backwards compatibility.
    """

    write: SequenceNotStr[str]
    """Entity IDs that can write/modify this memory.

    Format: 'prefix:id' (e.g., 'external_user:alice'). Supported prefixes: user,
    external_user, organization, namespace, workspace, role.
    """


class MemoryPolicyEdgeConstraintSearchProperty(TypedDict, total=False):
    """Property matching configuration.

    Defines which property to match on and how.
    When listed in search.properties, this property becomes a unique identifier.

    **Shorthand Helpers** (recommended for common cases):
        PropertyMatch.exact("id")                    # Exact match on id
        PropertyMatch.exact("id", "TASK-123")        # Exact match with specific value
        PropertyMatch.semantic("title")              # Semantic match with default threshold
        PropertyMatch.semantic("title", 0.9)         # Semantic match with custom threshold
        PropertyMatch.semantic("title", value="bug") # Semantic search for "bug"
        PropertyMatch.fuzzy("name", 0.8)             # Fuzzy match

    **Full Form** (when you need all options):
        PropertyMatch(name="title", mode="semantic", threshold=0.9, value="auth bug")

    **String Shorthand** (in SearchConfig.properties):
        properties=["id", "email"]  # Equivalent to [PropertyMatch.exact("id"), PropertyMatch.exact("email")]
    """

    name: Required[str]
    """Property name to match on (e.g., 'id', 'email', 'title')"""

    mode: Literal["semantic", "exact", "fuzzy"]
    """
    Matching mode: 'exact' (string match), 'semantic' (embedding similarity),
    'fuzzy' (Levenshtein distance)
    """

    threshold: float
    """Similarity threshold for semantic/fuzzy modes (0.0-1.0).

    Ignored for exact mode.
    """

    value: object
    """Runtime value override.

    If set, use this value for matching instead of extracting from content. Useful
    for memory-level overrides when you know the exact value to search for.
    """


class MemoryPolicyEdgeConstraintSearch(TypedDict, total=False):
    """Configuration for finding/selecting existing nodes.

    Defines which properties to match on and how, in priority order.
    The first matching property wins.

    **String Shorthand** (simple cases - converts to exact match):
        SearchConfig(properties=["id", "email"])
        # Equivalent to:
        SearchConfig(properties=[PropertyMatch.exact("id"), PropertyMatch.exact("email")])

    **Mixed Form** (combine strings and PropertyMatch):
        SearchConfig(properties=[
            "id",                                    # String -> exact match
            PropertyMatch.semantic("title", 0.9)     # Full control
        ])

    **Full Form** (maximum control):
        SearchConfig(properties=[
            PropertyMatch(name="id", mode="exact"),
            PropertyMatch(name="title", mode="semantic", threshold=0.85)
        ])

    **To select a specific node by ID**:
        SearchConfig(properties=[PropertyMatch.exact("id", "TASK-123")])
    """

    mode: Literal["semantic", "exact", "fuzzy"]
    """Default search mode when property doesn't specify one.

    'semantic' (vector similarity), 'exact' (property match), 'fuzzy' (partial
    match).
    """

    properties: Optional[Iterable[MemoryPolicyEdgeConstraintSearchProperty]]
    """Properties to match on, in priority order (first match wins).

    Accepts strings (converted to exact match) or PropertyMatch objects. Use
    PropertyMatch with 'value' field for specific node selection.
    """

    threshold: float
    """Default similarity threshold for semantic/fuzzy matching (0.0-1.0).

    Used when property doesn't specify its own threshold.
    """

    via_relationship: Optional[Iterable[object]]
    """Search for nodes via their relationships.

    Example: Find tasks assigned to a specific person. Each RelationshipMatch
    specifies edge_type, target_type, and target_search. Multiple relationship
    matches are ANDed together.
    """


class MemoryPolicyEdgeConstraintSetPropertyValue(TypedDict, total=False):
    """Configuration for a property value in NodeConstraint.set.

    Supports two modes:
    1. Exact value: Just pass the value directly (e.g., "done", 123, True)
    2. Auto-extract: {"mode": "auto"} - LLM extracts from memory content

    For text properties, use text_mode to control how updates are applied.
    """

    mode: Literal["auto"]
    """'auto': LLM extracts value from memory content."""

    text_mode: Literal["replace", "append", "merge"]
    """
    For text properties: 'replace' (overwrite), 'append' (add to), 'merge' (LLM
    combines existing + new).
    """


MemoryPolicyEdgeConstraintSet: TypeAlias = Union[
    str, float, bool, Iterable[object], Dict[str, object], MemoryPolicyEdgeConstraintSetPropertyValue
]


class MemoryPolicyEdgeConstraint(TypedDict, total=False):
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

    search: Optional[MemoryPolicyEdgeConstraintSearch]
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

    set: Optional[Dict[str, MemoryPolicyEdgeConstraintSet]]
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


class MemoryPolicyNodeConstraintSearchProperty(TypedDict, total=False):
    """Property matching configuration.

    Defines which property to match on and how.
    When listed in search.properties, this property becomes a unique identifier.

    **Shorthand Helpers** (recommended for common cases):
        PropertyMatch.exact("id")                    # Exact match on id
        PropertyMatch.exact("id", "TASK-123")        # Exact match with specific value
        PropertyMatch.semantic("title")              # Semantic match with default threshold
        PropertyMatch.semantic("title", 0.9)         # Semantic match with custom threshold
        PropertyMatch.semantic("title", value="bug") # Semantic search for "bug"
        PropertyMatch.fuzzy("name", 0.8)             # Fuzzy match

    **Full Form** (when you need all options):
        PropertyMatch(name="title", mode="semantic", threshold=0.9, value="auth bug")

    **String Shorthand** (in SearchConfig.properties):
        properties=["id", "email"]  # Equivalent to [PropertyMatch.exact("id"), PropertyMatch.exact("email")]
    """

    name: Required[str]
    """Property name to match on (e.g., 'id', 'email', 'title')"""

    mode: Literal["semantic", "exact", "fuzzy"]
    """
    Matching mode: 'exact' (string match), 'semantic' (embedding similarity),
    'fuzzy' (Levenshtein distance)
    """

    threshold: float
    """Similarity threshold for semantic/fuzzy modes (0.0-1.0).

    Ignored for exact mode.
    """

    value: object
    """Runtime value override.

    If set, use this value for matching instead of extracting from content. Useful
    for memory-level overrides when you know the exact value to search for.
    """


class MemoryPolicyNodeConstraintSearch(TypedDict, total=False):
    """Configuration for finding/selecting existing nodes.

    Defines which properties to match on and how, in priority order.
    The first matching property wins.

    **String Shorthand** (simple cases - converts to exact match):
        SearchConfig(properties=["id", "email"])
        # Equivalent to:
        SearchConfig(properties=[PropertyMatch.exact("id"), PropertyMatch.exact("email")])

    **Mixed Form** (combine strings and PropertyMatch):
        SearchConfig(properties=[
            "id",                                    # String -> exact match
            PropertyMatch.semantic("title", 0.9)     # Full control
        ])

    **Full Form** (maximum control):
        SearchConfig(properties=[
            PropertyMatch(name="id", mode="exact"),
            PropertyMatch(name="title", mode="semantic", threshold=0.85)
        ])

    **To select a specific node by ID**:
        SearchConfig(properties=[PropertyMatch.exact("id", "TASK-123")])
    """

    mode: Literal["semantic", "exact", "fuzzy"]
    """Default search mode when property doesn't specify one.

    'semantic' (vector similarity), 'exact' (property match), 'fuzzy' (partial
    match).
    """

    properties: Optional[Iterable[MemoryPolicyNodeConstraintSearchProperty]]
    """Properties to match on, in priority order (first match wins).

    Accepts strings (converted to exact match) or PropertyMatch objects. Use
    PropertyMatch with 'value' field for specific node selection.
    """

    threshold: float
    """Default similarity threshold for semantic/fuzzy matching (0.0-1.0).

    Used when property doesn't specify its own threshold.
    """

    via_relationship: Optional[Iterable[object]]
    """Search for nodes via their relationships.

    Example: Find tasks assigned to a specific person. Each RelationshipMatch
    specifies edge_type, target_type, and target_search. Multiple relationship
    matches are ANDed together.
    """


class MemoryPolicyNodeConstraintSetPropertyValue(TypedDict, total=False):
    """Configuration for a property value in NodeConstraint.set.

    Supports two modes:
    1. Exact value: Just pass the value directly (e.g., "done", 123, True)
    2. Auto-extract: {"mode": "auto"} - LLM extracts from memory content

    For text properties, use text_mode to control how updates are applied.
    """

    mode: Literal["auto"]
    """'auto': LLM extracts value from memory content."""

    text_mode: Literal["replace", "append", "merge"]
    """
    For text properties: 'replace' (overwrite), 'append' (add to), 'merge' (LLM
    combines existing + new).
    """


MemoryPolicyNodeConstraintSet: TypeAlias = Union[
    str, float, bool, Iterable[object], Dict[str, object], MemoryPolicyNodeConstraintSetPropertyValue
]


class MemoryPolicyNodeConstraint(TypedDict, total=False):
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

    create: Literal["upsert", "lookup", "auto", "never"]
    """'upsert': Create if not found via search (default).

    'lookup': Only link to existing nodes (controlled vocabulary). Deprecated
    aliases: 'auto' -> 'upsert', 'never' -> 'lookup'.
    """

    link_only: bool
    """DEPRECATED: Use create='lookup' instead.

    Shorthand for create='lookup'. When True, only links to existing nodes
    (controlled vocabulary). Equivalent to @lookup decorator in schema definitions.
    """

    node_type: Optional[str]
    """Node type this constraint applies to (e.g., 'Task', 'Project', 'Person').

    Optional at schema level (implicit from parent UserNodeType), required at memory
    level (in memory_policy.node_constraints).
    """

    on_miss: Optional[Literal["create", "ignore", "error"]]
    """Explicit behavior when no match found via search.

    'create': create new node (same as upsert). 'ignore': skip node creation (same
    as lookup). 'error': raise error if node not found. If specified, overrides
    'create' field.
    """

    search: Optional[MemoryPolicyNodeConstraintSearch]
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

    set: Optional[Dict[str, MemoryPolicyNodeConstraintSet]]
    """Set property values on nodes.

    Supports: 1. Exact value: {'status': 'done'} - sets exact value. 2.
    Auto-extract: {'status': {'mode': 'auto'}} - LLM extracts from content. 3. Text
    mode: {'summary': {'mode': 'auto', 'text_mode': 'merge'}} - controls text
    updates. For text properties, text_mode can be 'replace', 'append', or 'merge'.
    """

    when: Optional[Dict[str, object]]
    """Condition for when this constraint applies.

    Supports logical operators: '\\__and', '\\__or', '\\__not'. Examples: Simple:
    {'priority': 'high'} - matches when priority equals 'high'. AND: {'\\__and':
    [{'priority': 'high'}, {'status': 'active'}]} - all must match. OR: {'\\__or':
    [{'status': 'active'}, {'status': 'pending'}]} - any must match. NOT: {'\\__not':
    {'status': 'completed'}} - negation. Complex: {'\\__and': [{'priority': 'high'},
    {'\\__or': [{'status': 'active'}, {'urgent': true}]}]}
    """


class MemoryPolicyNode(TypedDict, total=False):
    """Specification for a node in manual mode.

    Used when mode='manual' to define exact nodes to create.
    """

    id: Required[str]
    """Unique identifier for this node"""

    type: Required[str]
    """Node type/label (e.g., 'Transaction', 'Product', 'Person')"""

    properties: Dict[str, object]
    """Properties for this node"""


class MemoryPolicyRelationship(TypedDict, total=False):
    """Specification for a relationship in manual mode.

    Used when mode='manual' to define exact relationships between nodes.
    """

    source: Required[str]
    """ID of the source node"""

    target: Required[str]
    """ID of the target node"""

    type: Required[str]
    """Relationship type (e.g., 'PURCHASED', 'WORKS_AT', 'ASSIGNED_TO')"""

    properties: Optional[Dict[str, object]]
    """Optional properties for this relationship"""


class MemoryPolicy(TypedDict, total=False):
    """Unified memory processing policy.

    This is the SINGLE source of truth for how a memory should be processed,
    combining graph generation control AND OMO (Open Memory Object) safety standards.

    **Graph Generation Modes:**
    - auto: LLM extracts entities freely (default)
    - manual: Developer provides exact nodes (no LLM extraction)

    **OMO Safety Standards:**
    - consent: How data owner allowed storage (explicit, implicit, terms, none)
    - risk: Safety assessment (none, sensitive, flagged)
    - acl: Access control list for read/write permissions

    **Schema Integration:**
    - schema_id: Reference a schema that may have its own default memory_policy
    - Schema-level policies are merged with request-level (request takes precedence)
    """

    acl: Optional[MemoryPolicyACL]
    """Simplified Access Control List configuration.

    Aligned with Open Memory Object (OMO) standard. See:
    https://github.com/anthropics/open-memory-object

    **Supported Entity Prefixes:**

    | Prefix           | Description           | Validation                           |
    | ---------------- | --------------------- | ------------------------------------ |
    | `user:`          | Internal Papr user ID | Validated against Parse users        |
    | `external_user:` | Your app's user ID    | Not validated (your responsibility)  |
    | `organization:`  | Organization ID       | Validated against your organizations |
    | `namespace:`     | Namespace ID          | Validated against your namespaces    |
    | `workspace:`     | Workspace ID          | Validated against your workspaces    |
    | `role:`          | Parse role ID         | Validated against your roles         |

    **Examples:**

    ```python
    acl = ACLConfig(
        read=["external_user:alice_123", "organization:org_acme"],
        write=["external_user:alice_123"]
    )
    ```

    **Validation Rules:**

    - Internal entities (user, organization, namespace, workspace, role) are
      validated
    - External entities (external_user) are NOT validated - your app is responsible
    - Invalid internal entities will return an error
    - Unprefixed values default to `external_user:` for backwards compatibility
    """

    consent: Literal["explicit", "implicit", "terms", "none"]
    """How the data owner allowed this memory to be stored/used.

    'explicit': User explicitly agreed. 'implicit': Inferred from context (default).
    'terms': Covered by Terms of Service. 'none': No consent - graph extraction will
    be SKIPPED.
    """

    edge_constraints: Optional[Iterable[MemoryPolicyEdgeConstraint]]
    """Rules for how LLM-extracted edges/relationships should be created/handled.

    Used in 'auto' mode when present. Controls: - create: 'auto' (create target if
    not found) or 'never' (controlled vocabulary) - search: How to find existing
    target nodes - set: Edge property values (exact or auto-extracted) -
    source_type/target_type: Filter by connected node types Example: {edge_type:
    'MITIGATES', create: 'never', search: {properties: ['name']}}
    """

    mode: Literal["auto", "manual"]
    """How to generate graph from this memory.

    'auto': LLM extracts entities freely. 'manual': You provide exact nodes (no
    LLM). Note: 'structured' is accepted as deprecated alias for 'manual'.
    """

    node_constraints: Optional[Iterable[MemoryPolicyNodeConstraint]]
    """Rules for how LLM-extracted nodes should be created/updated.

    Used in 'auto' mode when present. Controls creation policy, property forcing,
    and merge behavior.
    """

    nodes: Optional[Iterable[MemoryPolicyNode]]
    """For manual mode: Exact nodes to create (no LLM extraction).

    Required when mode='manual'. Each node needs id, type, and properties.
    """

    relationships: Optional[Iterable[MemoryPolicyRelationship]]
    """Relationships between nodes.

    Supports special placeholders:
    '$this' = the Memory node being created, '$previous' = the user's most recent
    memory. Examples: {source: '$this', target: '$previous', type: 'FOLLOWS'} links
    to previous memory. {source: '$this', target: 'mem_abc', type: 'REFERENCES'}
    links to specific memory.
    """

    risk: Literal["none", "sensitive", "flagged"]
    """Safety assessment for this memory.

    'none': Safe content (default). 'sensitive': Contains PII or sensitive info.
    'flagged': Requires review - ACL will be restricted to owner only.
    """

    schema_id: Optional[str]
    """Reference a UserGraphSchema by ID.

    The schema's memory_policy (if defined) will be used as defaults, with this
    request's settings taking precedence.
    """
