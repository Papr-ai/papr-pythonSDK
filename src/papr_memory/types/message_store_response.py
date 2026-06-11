# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MessageStoreResponse", "ContentUnionMember1"]


class ContentUnionMember1(BaseModel):
    """
    Structured message content block (OpenAPI-typed alternative to free-form dicts).
    """

    type: str
    """Content block type (e.g. 'text')"""

    text: Optional[str] = None
    """Text payload when type is 'text'"""


class MessageStoreResponse(BaseModel):
    """Response model for message storage"""

    content: Union[str, List[ContentUnionMember1]]
    """Content of the message - can be a simple string or structured content objects"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the message was created"""

    object_id: str = FieldInfo(alias="objectId")
    """Parse Server objectId of the stored message"""

    role: Literal["user", "assistant"]
    """Role of the message sender"""

    session_id: str = FieldInfo(alias="sessionId")
    """Session ID of the conversation"""

    processing_status: Optional[str] = None
    """Status of background processing (queued, analyzing, completed, failed)"""
