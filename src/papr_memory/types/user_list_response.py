# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .user_response import UserResponse

__all__ = ["UserListResponse"]


class UserListResponse(BaseModel):
    code: int
    """HTTP status code"""

    status: str
    """'success' or 'error'"""

    data: Optional[List[UserResponse]] = None

    details: Optional[object] = None

    error: Optional[str] = None

    page: Optional[int] = None

    page_size: Optional[int] = None

    total: Optional[int] = None
