# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, TypedDict

from .node_spec import NodeSpec
from .acl_config import ACLConfig
from .relationship_spec import RelationshipSpec
from .edge_constraint_input import EdgeConstraintInput
from .node_constraint_input import NodeConstraintInput

__all__ = ["MemoryPolicy"]


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

    'explicit': User explicitly agreed. 'implicit': Inferred from context (default).
    'terms': Covered by Terms of Service. 'none': No consent - graph extraction will
    be SKIPPED.
    """

    edge_constraints: Optional[Iterable[EdgeConstraintInput]]
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

    node_constraints: Optional[Iterable[NodeConstraintInput]]
    """Rules for how LLM-extracted nodes should be created/updated.

    Used in 'auto' mode when present. Controls creation policy, property forcing,
    and merge behavior.
    """

    nodes: Optional[Iterable[NodeSpec]]
    """For manual mode: Exact nodes to create (no LLM extraction).

    Required when mode='manual'. Each node needs id, type, and properties.
    """

    relationships: Optional[Iterable[RelationshipSpec]]
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
