# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .._types import SequenceNotStr
from .add_memory_param import AddMemoryParam
from .graph_generation_param import GraphGenerationParam
from .shared_params.memory_policy import MemoryPolicy

__all__ = ["MemoryAddBatchParams"]


class MemoryAddBatchParams(TypedDict, total=False):
    memories: Required[Iterable[AddMemoryParam]]
    """List of memory items to add in batch"""

    skip_background_processing: bool
    """If True, skips adding background tasks for processing"""

    batch_size: Optional[int]
    """Number of items to process in parallel"""

    external_user_id: Optional[str]
    """Your application's user identifier for all memories in the batch.

    This is the primary way to identify users. Papr will automatically resolve or
    create internal users as needed.
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

    namespace_id: Optional[str]
    """Optional namespace ID for multi-tenant batch memory scoping.

    When provided, all memories in the batch are associated with this namespace.
    """

    organization_id: Optional[str]
    """Optional organization ID for multi-tenant batch memory scoping.

    When provided, all memories in the batch are associated with this organization.
    """

    user_id: Optional[str]
    """DEPRECATED: Use 'external_user_id' instead. Internal Papr Parse user ID."""

    webhook_secret: Optional[str]
    """Optional secret key for webhook authentication.

    If provided, will be included in the webhook request headers as
    'X-Webhook-Secret'.
    """

    webhook_url: Optional[str]
    """Optional webhook URL to notify when batch processing is complete.

    The webhook will receive a POST request with batch completion details.
    """
