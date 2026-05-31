# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr
from .memory_type import MemoryType
from .context_item_param import ContextItemParam
from .memory_metadata_param import MemoryMetadataParam
from .graph_generation_param import GraphGenerationParam
from .relationship_item_param import RelationshipItemParam
from .shared_params.memory_policy import MemoryPolicy
from .shared_params.memory_add_policy import MemoryAddPolicy

__all__ = ["MemoryUpdateParams"]


class MemoryUpdateParams(TypedDict, total=False):
    enable_holographic: bool
    """If True, re-processes holographic neural transforms after content update"""

    frequency_schema_id: Optional[str]
    """Frequency schema for holographic embedding (e.g. 'cosqa', 'scifact')."""

    content: Optional[str]
    """The new content of the memory item"""

    context: Optional[Iterable[ContextItemParam]]
    """Updated context for the memory item"""

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

    When provided, update is scoped to memories within this namespace.
    """

    organization_id: Optional[str]
    """Optional organization ID for multi-tenant memory scoping.

    When provided, update is scoped to memories within this organization.
    """

    policy: Optional[MemoryAddPolicy]
    """Policy for add / batch / document / message ingestion."""

    relationships_json: Optional[Iterable[RelationshipItemParam]]
    """Updated relationships for Graph DB (neo4J)"""

    type: Optional[MemoryType]
    """Valid memory types"""
