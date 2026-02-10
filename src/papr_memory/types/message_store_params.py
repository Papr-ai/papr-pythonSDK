# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .memory_metadata_param import MemoryMetadataParam
from .graph_generation_param import GraphGenerationParam
from .shared_params.memory_policy import MemoryPolicy

__all__ = ["MessageStoreParams"]


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
