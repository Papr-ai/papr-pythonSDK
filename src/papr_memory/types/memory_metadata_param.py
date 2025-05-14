# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["MemoryMetadataParam"]


class MemoryMetadataParamTyped(TypedDict, total=False):
    conversation_id: Annotated[Optional[str], PropertyInfo(alias="conversationId")]

    created_at: Annotated[Optional[str], PropertyInfo(alias="createdAt")]
    """ISO datetime when the memory was created"""

    emoji_tags: Annotated[Optional[str], PropertyInfo(alias="emoji tags")]

    emotion_tags: Annotated[Optional[str], PropertyInfo(alias="emotion tags")]

    hierarchical_structures: Optional[str]
    """Hierarchical structures to enable navigation from broad topics to specific ones"""

    location: Optional[str]

    role_read_access: Optional[List[str]]

    role_write_access: Optional[List[str]]

    source_url: Annotated[Optional[str], PropertyInfo(alias="sourceUrl")]

    topics: Optional[str]

    user_id: Optional[str]

    user_read_access: Optional[List[str]]

    user_write_access: Optional[List[str]]

    workspace_read_access: Optional[List[str]]

    workspace_write_access: Optional[List[str]]


MemoryMetadataParam: TypeAlias = Union[MemoryMetadataParamTyped, Dict[str, object]]
