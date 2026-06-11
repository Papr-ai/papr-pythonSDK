# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MessageStoreResponse"]


class MessageStoreResponse(BaseModel):
    """Response model for message storage"""

    content: Union[str, List[Dict[str, object]]]
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
