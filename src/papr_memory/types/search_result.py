# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel
from .shared.memory import Memory

__all__ = ["SearchResult", "Node"]


class Node(BaseModel):
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


class SearchResult(BaseModel):
    """Return type for SearchResult"""

    memories: List[Memory]

    nodes: List[Node]

    schemas_used: Optional[List[str]] = None
    """List of UserGraphSchema IDs used in this response.

    Use GET /v1/schemas/{id} to get full schema definitions.
    """
