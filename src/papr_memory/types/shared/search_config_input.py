# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SearchConfigInput", "Property"]


class Property(BaseModel):
    """Property matching configuration.

    Defines which property to match on and how.
    When listed in search.properties, this property becomes a unique identifier.

    **Shorthand Helpers** (recommended for common cases):
        PropertyMatch.exact("id")                    # Exact match on id
        PropertyMatch.exact("id", "TASK-123")        # Exact match with specific value
        PropertyMatch.semantic("title")              # Semantic match with default threshold
        PropertyMatch.semantic("title", 0.9)         # Semantic match with custom threshold
        PropertyMatch.semantic("title", value="bug") # Semantic search for "bug"
        PropertyMatch.fuzzy("name", 0.8)             # Fuzzy match

    **Full Form** (when you need all options):
        PropertyMatch(name="title", mode="semantic", threshold=0.9, value="auth bug")

    **String Shorthand** (in SearchConfig.properties):
        properties=["id", "email"]  # Equivalent to [PropertyMatch.exact("id"), PropertyMatch.exact("email")]
    """

    name: str
    """Property name to match on (e.g., 'id', 'email', 'title')"""

    mode: Optional[Literal["semantic", "exact", "fuzzy"]] = None
    """
    Matching mode: 'exact' (string match), 'semantic' (embedding similarity),
    'fuzzy' (Levenshtein distance)
    """

    threshold: Optional[float] = None
    """Similarity threshold for semantic/fuzzy modes (0.0-1.0).

    Ignored for exact mode.
    """

    value: Optional[object] = None
    """Runtime value override.

    If set, use this value for matching instead of extracting from content. Useful
    for memory-level overrides when you know the exact value to search for.
    """


class SearchConfigInput(BaseModel):
    """Configuration for finding/selecting existing nodes.

    Defines which properties to match on and how, in priority order.
    The first matching property wins.

    **String Shorthand** (simple cases - converts to exact match):
        SearchConfig(properties=["id", "email"])
        # Equivalent to:
        SearchConfig(properties=[PropertyMatch.exact("id"), PropertyMatch.exact("email")])

    **Mixed Form** (combine strings and PropertyMatch):
        SearchConfig(properties=[
            "id",                                    # String -> exact match
            PropertyMatch.semantic("title", 0.9)     # Full control
        ])

    **Full Form** (maximum control):
        SearchConfig(properties=[
            PropertyMatch(name="id", mode="exact"),
            PropertyMatch(name="title", mode="semantic", threshold=0.85)
        ])

    **To select a specific node by ID**:
        SearchConfig(properties=[PropertyMatch.exact("id", "TASK-123")])
    """

    mode: Optional[Literal["semantic", "exact", "fuzzy"]] = None
    """Default search mode when property doesn't specify one.

    'semantic' (vector similarity), 'exact' (property match), 'fuzzy' (partial
    match).
    """

    properties: Optional[List[Property]] = None
    """Properties to match on, in priority order (first match wins).

    Accepts strings (converted to exact match) or PropertyMatch objects. Use
    PropertyMatch with 'value' field for specific node selection.
    """

    threshold: Optional[float] = None
    """Default similarity threshold for semantic/fuzzy matching (0.0-1.0).

    Used when property doesn't specify its own threshold.
    """

    via_relationship: Optional[List[object]] = None
    """Search for nodes via their relationships.

    Example: Find tasks assigned to a specific person. Each RelationshipMatch
    specifies edge_type, target_type, and target_search. Multiple relationship
    matches are ANDed together.
    """
