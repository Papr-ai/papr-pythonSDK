# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .search_result import SearchResult

__all__ = ["SearchResponse"]


class SearchResponse(BaseModel):
    code: Optional[int] = None
    """HTTP status code"""

    data: Optional[SearchResult] = None
    """Return type for SearchResult"""

    details: Optional[object] = None
    """Additional error details or context"""

    error: Optional[str] = None
    """Error message if failed"""

    search_id: Optional[str] = None
    """
    Unique identifier for this search query, maps to QueryLog objectId in Parse
    Server
    """

    status: Optional[str] = None
    """'success' or 'error'"""
