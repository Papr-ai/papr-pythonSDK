# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel
from .shared.memory import Memory

__all__ = ["SearchResponse", "Data", "DataNode"]


class DataNode(BaseModel):
    """Public-facing node structure - supports both system and custom schema nodes"""

    label: str
    """
    Node type label - can be system type (Memory, Person, etc.) or custom type from
    UserGraphSchema
    """

    properties: Dict[str, object]
    """Node properties - structure depends on node type and schema"""

    schema_id: Optional[str] = None
    """Reference to UserGraphSchema ID for custom nodes.

    Use GET /v1/schemas/{schema_id} to get full schema definition. Null for system
    nodes.
    """


class Data(BaseModel):
    """Return type for SearchResult"""

    memories: List[Memory]

    nodes: List[DataNode]

    schemas_used: Optional[List[str]] = None
    """List of UserGraphSchema IDs used in this response.

    Use GET /v1/schemas/{id} to get full schema definitions.
    """


class SearchResponse(BaseModel):
    code: Optional[int] = None
    """HTTP status code"""

    data: Optional[Data] = None
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
