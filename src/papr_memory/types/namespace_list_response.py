# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .namespace_item import NamespaceItem

__all__ = ["NamespaceListResponse"]


class NamespaceListResponse(BaseModel):
    """Response for listing namespaces with pagination."""

    code: Optional[int] = None
    """HTTP status code"""

    data: Optional[List[NamespaceItem]] = None
    """List of namespaces"""

    details: Optional[object] = None
    """Additional error details or context"""

    error: Optional[str] = None
    """Error message if failed"""

    page: Optional[int] = None
    """Current page (0-indexed skip)"""

    page_size: Optional[int] = None
    """Items per page"""

    status: Optional[str] = None
    """'success' or 'error'"""

    total: Optional[int] = None
    """Total matching namespaces"""
