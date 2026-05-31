# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .memory_type import MemoryType
from .context_item_param import ContextItemParam
from .memory_metadata_param import MemoryMetadataParam
from .graph_generation_param import GraphGenerationParam
from .relationship_item_param import RelationshipItemParam
from .shared_params.node_spec import NodeSpec
from .shared_params.acl_config import ACLConfig
from .shared_params.memory_policy import MemoryPolicy
from .shared_params.relationship_spec import RelationshipSpec
from .shared_params.edge_constraint_input import EdgeConstraintInput
from .shared_params.node_constraint_input import NodeConstraintInput

__all__ = ["AddMemoryParam", "Policy", "PolicyGraph", "PolicyTransformEmbedding"]


class PolicyGraph(TypedDict, total=False):
    edge_constraints: Optional[Iterable[EdgeConstraintInput]]
    """Full edge constraint objects.

    Same rules as edge entries in policy.graph.link_to after expansion; both may be
    set in the same request.
    """

    link_to: Union[str, SequenceNotStr[str], Dict[str, object], None]
    """Shorthand DSL for node/edge constraints under policy.graph.

    Not a separate graph mode — expands into node_constraints and edge_constraints
    at resolve time and merges with any explicit constraints in the same request.
    Default create policy is upsert (create if not found); use dict form with
    create='lookup' for link-only. Prefer over deprecated top-level link_to.
    """

    mode: Literal["none", "auto", "manual"]

    node_constraints: Optional[Iterable[NodeConstraintInput]]
    """Full node constraint objects.

    Same rules as policy.graph.link_to after expansion; use link_to for compact DSL
    or this field for explicit control. Both may be set.
    """

    nodes: Optional[Iterable[NodeSpec]]

    relationships: Optional[Iterable[RelationshipSpec]]

    schema_id: Optional[str]


class PolicyTransformEmbedding(TypedDict, total=False):
    domain_id: Optional[str]
    """Signal domain id or shorthand (e.g. cosqa)"""

    mode: Literal["none", "auto", "manual"]
    """none=base embed only; auto=run graph transform; manual=BYO signals"""

    signals: Optional[Dict[str, str]]
    """BYO band text values when mode=manual"""


class Policy(TypedDict, total=False):
    """Policy for add / batch / document / message ingestion."""

    acl: Optional[ACLConfig]
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

    Aligned with Open Memory Object (OMO) standard.
    """

    graph: Optional[PolicyGraph]

    risk: Literal["none", "sensitive", "flagged"]
    """Post-ingest safety assessment of memory content.

    Aligned with Open Memory Object (OMO) standard.
    """

    transform_embedding: Optional[PolicyTransformEmbedding]


class AddMemoryParam(TypedDict, total=False):
    """Request model for adding a new memory"""

    content: Required[str]
    """The content of the memory item you want to add to memory"""

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
    """DEPRECATED: Use policy.graph.link_to instead.

    Shorthand DSL for node/edge constraints (same as node_constraints, compact
    syntax). Expands and merges into memory_policy.node_constraints and
    edge_constraints at resolve time. Default create is upsert; use dict form with
    create='lookup' (or legacy 'never') for link-only. Formats: - String:
    'Task:title' (semantic match on Task.title, upsert by default) - List:
    ['Task:title', 'Person:email'] (multiple constraints) - Dict: {'Task:title':
    {'set': {...}, 'create': 'lookup'}} (full options) Syntax: - Node:
    'Type:property', 'Type:prop=value' (exact), 'Type:prop~value' (semantic) - Edge:
    'Source->EDGE->Target:property' (arrow syntax) - Via:
    'Type.via(EDGE->Target:prop)' (relationship traversal) - Special:
    '$this', '$previous', '$context:N' Example lookup-only: {'SecurityPolicy:name':
    {'create': 'lookup'}}
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
    """DEPRECATED - Internal only.

    Auto-populated from API key scope. Do not set manually. The organization is
    resolved automatically from the API key's associated organization.
    """

    policy: Optional[Policy]
    """Policy for add / batch / document / message ingestion."""

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
