# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MemoryDeleteResponse", "DeletionStatus"]


class DeletionStatus(BaseModel):
    neo4j: Optional[bool] = None

    parse: Optional[bool] = None

    pinecone: Optional[bool] = None

    qdrant: Optional[bool] = None


class MemoryDeleteResponse(BaseModel):
    code: Optional[int] = None
    """HTTP status code"""

    deletion_status: Optional[DeletionStatus] = None

    details: Optional[object] = None

    error: Optional[str] = None

    memory_id: Optional[str] = FieldInfo(alias="memoryId", default=None)

    message: Optional[str] = None

    object_id: Optional[str] = FieldInfo(alias="objectId", default=None)

    status: Optional[str] = None
    """'success' or 'error'"""
