# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AddMemoryResponse", "Data"]


class Data(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    memory_id: str = FieldInfo(alias="memoryId")

    object_id: str = FieldInfo(alias="objectId")

    memory_chunk_ids: Optional[List[str]] = FieldInfo(alias="memoryChunkIds", default=None)


class AddMemoryResponse(BaseModel):
    code: Optional[int] = None
    """HTTP status code"""

    data: Optional[List[Data]] = None
    """List of memory items if successful"""

    details: Optional[object] = None
    """Additional error details or context"""

    error: Optional[str] = None
    """Error message if failed"""

    status: Optional[str] = None
    """'success' or 'error'"""
