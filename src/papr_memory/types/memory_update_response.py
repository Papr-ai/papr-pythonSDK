# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .memory_metadata import MemoryMetadata

__all__ = ["MemoryUpdateResponse", "MemoryItem", "StatusObj"]


class MemoryItem(BaseModel):
    memory_id: str = FieldInfo(alias="memoryId")

    object_id: str = FieldInfo(alias="objectId")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    content: Optional[str] = None

    memory_chunk_ids: Optional[List[str]] = FieldInfo(alias="memoryChunkIds", default=None)

    metadata: Optional[MemoryMetadata] = None
    """Metadata for memory request"""


class StatusObj(BaseModel):
    neo4j: Optional[bool] = None

    parse: Optional[bool] = None

    pinecone: Optional[bool] = None


class MemoryUpdateResponse(BaseModel):
    code: Optional[int] = None
    """HTTP status code"""

    details: Optional[object] = None
    """Additional error details or context"""

    error: Optional[str] = None
    """Error message if failed"""

    memory_items: Optional[List[MemoryItem]] = None
    """List of updated memory items if successful"""

    message: Optional[str] = None
    """Status message"""

    status: Optional[str] = None
    """'success' or 'error'"""

    status_obj: Optional[StatusObj] = None
    """Status of update operation for each system"""
