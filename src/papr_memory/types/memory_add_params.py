# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .._types import SequenceNotStr
from .memory_type import MemoryType
from .context_item_param import ContextItemParam
from .memory_metadata_param import MemoryMetadataParam
from .graph_generation_param import GraphGenerationParam
from .relationship_item_param import RelationshipItemParam
from .shared_params.memory_policy import MemoryPolicy

__all__ = ["MemoryAddParams"]


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
