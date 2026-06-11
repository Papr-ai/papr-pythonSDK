# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ConversationSummaryResponse"]


class ConversationSummaryResponse(BaseModel):
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
