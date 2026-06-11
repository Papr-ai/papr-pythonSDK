# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ConversationSummaryResponse"]


class ConversationSummaryResponse(BaseModel):
    """Hierarchical conversation summaries for context window compression"""

    current_state: Optional[str] = None
    """Current progress: what is working, not working, blocked, or unverified"""

    files_accessed: Optional[Dict[str, object]] = None
    """Files read, modified, created, or deleted during the session"""

    key_decisions: Optional[List[str]] = None
    """Important decisions made and their reasoning"""

    last_updated: Optional[datetime] = None
    """When summaries were last updated"""

    long_term: Optional[str] = None
    """Full session summary"""

    medium_term: Optional[str] = None
    """Summary of last ~100 messages"""

    next_steps: Optional[List[str]] = None
    """Specific actionable next steps"""

    project_context: Optional[Dict[str, object]] = None
    """Detected project context (name, path, tech stack, current task)"""

    session_intent: Optional[str] = None
    """What the user is trying to accomplish in this session"""

    short_term: Optional[str] = None
    """Summary of last 15 messages"""

    technical_details: Optional[List[str]] = None
    """Technical details to remember (URLs, errors, config values, function names)"""

    topics: Optional[List[str]] = None
    """Key topics discussed"""
