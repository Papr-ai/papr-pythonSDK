# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["SessionCompressResponse", "Summaries"]


class Summaries(BaseModel):
    """Hierarchical conversation summaries"""

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


class SessionCompressResponse(BaseModel):
    """Response model for session summarization endpoint"""

    ai_agent_note: str
    """
    Instructions for AI agents on how to search for more details about this
    conversation
    """

    from_cache: bool
    """Whether summaries were retrieved from cache (true) or just generated (false)"""

    session_id: str
    """Session ID of the conversation"""

    summaries: Summaries
    """Hierarchical conversation summaries"""

    message_count: Optional[int] = None
    """Number of messages summarized (only present if just generated)"""
