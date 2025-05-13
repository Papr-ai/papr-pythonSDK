# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .add_memory_item import AddMemoryItem

__all__ = ["AddMemoryResponse"]


class AddMemoryResponse(BaseModel):
    code: Optional[int] = None
    """HTTP status code"""

    data: Optional[List[AddMemoryItem]] = None
    """List of memory items if successful"""

    details: Optional[object] = None
    """Additional error details or context"""

    error: Optional[str] = None
    """Error message if failed"""

    status: Optional[str] = None
    """'success' or 'error'"""
