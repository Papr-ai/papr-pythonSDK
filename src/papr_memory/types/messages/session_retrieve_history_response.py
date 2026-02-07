# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SessionRetrieveHistoryResponse", "Message", "Summaries"]


class Message(BaseModel):
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


class Summaries(BaseModel):
    """Hierarchical conversation summaries for context window compression"""

    last_updated: Optional[datetime] = None
    """When summaries were last updated"""

    long_term: Optional[str] = None
    """Full session summary"""

    medium_term: Optional[str] = None
    """Summary of last ~100 messages"""

    short_term: Optional[str] = None
    """Summary of last 15 messages"""

    topics: Optional[List[str]] = None
    """Key topics discussed"""


class SessionRetrieveHistoryResponse(BaseModel):
    """Response model for retrieving message history"""

    messages: List[Message]
    """List of messages in chronological order"""

    session_id: str = FieldInfo(alias="sessionId")
    """Session ID of the conversation"""

    total_count: int
    """Total number of messages in the session"""

    context_for_llm: Optional[str] = None
    """
    Pre-formatted compressed context ready for LLM consumption (summaries + recent
    messages)
    """

    summaries: Optional[Summaries] = None
    """Hierarchical conversation summaries for context window compression"""
