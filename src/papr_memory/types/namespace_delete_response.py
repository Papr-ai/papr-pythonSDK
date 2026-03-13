# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["NamespaceDeleteResponse", "Cascade"]


class Cascade(BaseModel):
    """Details of the cascade deletion performed when a namespace is removed."""

    acl_read_cleaned: Optional[int] = None
    """Nodes with namespace_read_access cleaned"""

    acl_write_cleaned: Optional[int] = None
    """Nodes with namespace_write_access cleaned"""

    memories_deleted: Optional[int] = None
    """Number of memories deleted"""

    memories_failed: Optional[int] = None
    """Number of memories that failed to delete"""

    neo4j_nodes_deleted: Optional[int] = None
    """Number of Neo4j nodes deleted"""


class NamespaceDeleteResponse(BaseModel):
    """Response for DELETE /v1/namespace/{namespace_id} with cascade results."""

    cascade: Optional[Cascade] = None
    """Details of the cascade deletion performed when a namespace is removed."""

    code: Optional[int] = None
    """HTTP status code"""

    details: Optional[object] = None
    """Additional error details or context"""

    error: Optional[str] = None
    """Error message if failed"""

    message: Optional[str] = None
    """Human-readable message"""

    namespace_id: Optional[str] = None
    """ID of deleted namespace"""

    status: Optional[str] = None
    """'success' or 'error'"""
