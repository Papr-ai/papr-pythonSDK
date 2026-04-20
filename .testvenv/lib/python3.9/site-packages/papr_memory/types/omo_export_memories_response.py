# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["OmoExportMemoriesResponse"]


class OmoExportMemoriesResponse(BaseModel):
    """Response model for OMO export."""

    count: int
    """Number of memories exported"""

    memories: List[Dict[str, object]]
    """Memories in OMO v1 format"""

    code: Optional[int] = None

    error: Optional[str] = None

    status: Optional[str] = None
