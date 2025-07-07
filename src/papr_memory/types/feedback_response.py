# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["FeedbackResponse"]


class FeedbackResponse(BaseModel):
    code: int
    """HTTP status code"""

    message: str
    """Human-readable message"""

    status: str
    """'success' or 'error'"""

    details: Optional[Dict[str, object]] = None
    """Additional error details"""

    error: Optional[str] = None
    """Error message if status is 'error'"""

    feedback_id: Optional[str] = None
    """Unique feedback ID"""
