# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AddMemoryItem"]


class AddMemoryItem(BaseModel):
    """Response model for a single memory item in add_memory response"""

    created_at: datetime = FieldInfo(alias="createdAt")

    memory_id: str = FieldInfo(alias="memoryId")

    object_id: str = FieldInfo(alias="objectId")

    memory_chunk_ids: Optional[List[str]] = FieldInfo(alias="memoryChunkIds", default=None)
