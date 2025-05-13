# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["UserDeleteResponse"]


class UserDeleteResponse(BaseModel):
    code: int
    """HTTP status code"""

    status: str
    """'success' or 'error'"""

    details: Optional[object] = None
    """Additional error details or context"""

    error: Optional[str] = None
    """Error message if failed"""

    message: Optional[str] = None
    """Success or error message"""

    user_id: Optional[str] = None
    """ID of the user attempted to delete"""
