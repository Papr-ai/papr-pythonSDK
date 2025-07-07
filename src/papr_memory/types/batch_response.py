# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["BatchResponse"]


class BatchResponse(BaseModel):
    code: int
    """HTTP status code"""

    message: str
    """Human-readable message"""

    status: str
    """'success' or 'error'"""

    error: Optional[str] = None
    """Error message if status is 'error'"""

    errors: Optional[List[Dict[str, object]]] = None
    """List of error details"""

    failed_count: Optional[int] = None
    """Number of failed feedback items"""

    feedback_ids: Optional[List[str]] = None
    """List of feedback IDs"""

    successful_count: Optional[int] = None
    """Number of successfully processed feedback items"""
