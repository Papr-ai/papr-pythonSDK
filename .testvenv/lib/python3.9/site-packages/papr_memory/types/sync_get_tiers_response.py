# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel
from .shared.memory import Memory

__all__ = ["SyncGetTiersResponse"]


class SyncGetTiersResponse(BaseModel):
    """Response model for sync tiers endpoint"""

    code: Optional[int] = None
    """HTTP status code"""

    details: Optional[object] = None
    """Additional error details or context"""

    error: Optional[str] = None
    """Error message if failed"""

    has_more: Optional[bool] = None
    """Whether there are more items available"""

    next_cursor: Optional[str] = None
    """Cursor for pagination"""

    status: Optional[str] = None
    """'success' or 'error'"""

    tier0: Optional[List[Memory]] = None
    """Tier 0 items (goals/OKRs/use-cases)"""

    tier1: Optional[List[Memory]] = None
    """Tier 1 items (hot memories)"""

    transitions: Optional[List[Dict[str, object]]] = None
    """Transition items between tiers"""
