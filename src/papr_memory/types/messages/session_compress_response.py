# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .conversation_summary_response import ConversationSummaryResponse

__all__ = ["SessionCompressResponse"]


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

    summaries: ConversationSummaryResponse
    """Hierarchical conversation summaries"""

    message_count: Optional[int] = None
    """Number of messages summarized (only present if just generated)"""
