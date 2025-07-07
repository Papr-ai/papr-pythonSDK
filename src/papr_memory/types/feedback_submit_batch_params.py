# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

from .feedback_request_param import FeedbackRequestParam

__all__ = ["FeedbackSubmitBatchParams"]


class FeedbackSubmitBatchParams(TypedDict, total=False):
    feedback_items: Required[Iterable[FeedbackRequestParam]]
    """List of feedback items to submit"""

    session_context: Optional[Dict[str, object]]
    """Session-level context for batch feedback"""
