# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["OmoImportMemoriesResponse"]


class OmoImportMemoriesResponse(BaseModel):
    """Response model for OMO import."""

    imported: int
    """Number of memories successfully imported"""

    code: Optional[int] = None

    errors: Optional[List[Dict[str, object]]] = None
    """Import errors"""

    memory_ids: Optional[List[str]] = None
    """IDs of imported memories"""

    skipped: Optional[int] = None
    """Number of memories skipped (duplicates)"""

    status: Optional[str] = None
