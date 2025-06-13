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

    custom_metadata: Annotated[
        Optional[Dict[str, Union[str, float, bool, List[str]]]], PropertyInfo(alias="customMetadata")
    ]
    """Optional object for arbitrary custom metadata fields.

    Only string, number, boolean, or list of strings allowed. Nested dicts are not
    allowed.
    """

    emoji_tags: Annotated[Optional[List[str]], PropertyInfo(alias="emoji tags")]

    emotion_tags: Annotated[Optional[List[str]], PropertyInfo(alias="emotion tags")]

    external_user_id: Optional[str]

    external_user_read_access: Optional[List[str]]

    external_user_write_access: Optional[List[str]]

    hierarchical_structures: Optional[str]
    """Hierarchical structures to enable navigation from broad topics to specific ones"""

    location: Optional[str]

    page_id: Annotated[Optional[str], PropertyInfo(alias="pageId")]

    role_read_access: Optional[List[str]]

    role_write_access: Optional[List[str]]

    source_type: Annotated[Optional[str], PropertyInfo(alias="sourceType")]

    source_url: Annotated[Optional[str], PropertyInfo(alias="sourceUrl")]

    topics: Optional[List[str]]

    user_id: Optional[str]

    user_read_access: Optional[List[str]]

    user_write_access: Optional[List[str]]

    workspace_id: Optional[str]

    workspace_read_access: Optional[List[str]]

    workspace_write_access: Optional[List[str]]


MemoryMetadataParam: TypeAlias = Union[MemoryMetadataParamTyped, Dict[str, object]]
