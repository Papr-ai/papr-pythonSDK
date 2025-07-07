# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["UserResponse"]


class UserResponse(BaseModel):
    code: int
    """HTTP status code"""

    status: str
    """'success' or 'error'"""

    created_at: Optional[str] = None

    details: Optional[object] = None

    email: Optional[str] = None

    error: Optional[str] = None

    external_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    updated_at: Optional[str] = None

    user_id: Optional[str] = None
