# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TransformCreateBatchParams", "Item"]


class TransformCreateBatchParams(TypedDict, total=False):
    items: Required[Iterable[Item]]
    """Items to transform (max 50)"""

    domain: Optional[str]
    """Domain for all items"""

    frequency_schema_id: Optional[str]
    """Schema override for all items"""

    output: Optional[
        List[
            Literal[
                "base",
                "rotation_v1",
                "rotation_v2",
                "rotation_v3",
                "concat",
                "phases",
                "metadata",
                "metadata_embeddings",
            ]
        ]
    ]
    """Which output fields to return for each item"""


class Item(TypedDict, total=False):
    """Single item in a batch transform request."""

    id: Required[str]
    """Unique identifier for this item"""

    content: Required[str]
    """Text content for metadata extraction"""

    embedding: Required[Iterable[float]]
    """Base embedding vector"""
