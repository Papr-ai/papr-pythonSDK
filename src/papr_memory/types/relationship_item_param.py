# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RelationshipItemParam"]


class RelationshipItemParam(TypedDict, total=False):
    relation_type: Required[str]

    metadata: object

    related_item_id: Optional[str]

    related_item_type: Optional[str]
    """Legacy field - not used in processing"""

    relationship_type: Optional[Literal["previous_memory_item_id", "all_previous_memory_items"]]
    """Enum for relationship types"""
