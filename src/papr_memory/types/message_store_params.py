# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .memory_metadata_param import MemoryMetadataParam
from .graph_generation_param import GraphGenerationParam
from .shared_params.node_spec import NodeSpec
from .shared_params.acl_config import ACLConfig
from .shared_params.memory_policy import MemoryPolicy
from .shared_params.relationship_spec import RelationshipSpec
from .shared_params.edge_constraint_input import EdgeConstraintInput
from .shared_params.node_constraint_input import NodeConstraintInput

__all__ = ["MessageStoreParams", "Policy", "PolicyGraph", "PolicyTransformEmbedding"]


class MessageStoreParams(TypedDict, total=False):
    content: Required[Union[str, Iterable[Dict[str, object]]]]
    """
    The content of the chat message - can be a simple string or structured content
    objects
    """

    role: Required[Literal["user", "assistant"]]
    """Role of the message sender (user or assistant)"""

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionId")]]
    """Session ID to group related messages in a conversation"""

    context: Optional[Iterable[Dict[str, object]]]
    """Optional context for the message (conversation history or relevant context)"""

    graph_generation: Optional[GraphGenerationParam]
    """Graph generation configuration"""

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
    """Optional namespace ID for multi-tenant message scoping"""

    organization_id: Optional[str]
    """Optional organization ID for multi-tenant message scoping"""

    policy: Optional[Policy]
    """Policy for add / batch / document / message ingestion."""

    process_messages: bool
    """Whether to process messages into memories (true) or just store them (false).

    Default is true.
    """

    relationships_json: Optional[Iterable[Dict[str, object]]]
    """Optional array of relationships for Graph DB (Neo4j)"""

    title: Optional[str]
    """Optional title for the conversation session.

    Sets the Chat.title in Parse Server for easy identification.
    """


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
