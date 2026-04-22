# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .namespace_item import NamespaceItem

__all__ = ["NamespaceUpdateResponse"]


class NamespaceUpdateResponse(BaseModel):
    """Response for single-namespace operations (create, get, update)."""

    code: Optional[int] = None
    """HTTP status code"""

    data: Optional[NamespaceItem] = None
    """Public-facing namespace data returned in API responses."""

    details: Optional[object] = None
    """Additional error details or context"""

    error: Optional[str] = None
    """Error message if failed"""

    status: Optional[str] = None
    """'success' or 'error'"""
