# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .memory_metadata_param import MemoryMetadataParam

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
