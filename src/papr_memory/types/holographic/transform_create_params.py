# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TransformCreateParams"]


class TransformCreateParams(TypedDict, total=False):
    content: Required[str]
    """Text content for LLM metadata extraction"""

    embedding: Required[Iterable[float]]
    """Base embedding vector (any dimensionality)"""

    domain: Optional[str]
    """Domain for frequency schema selection (e.g. 'biomedical', 'code', 'general')"""

    frequency_schema_id: Optional[str]
    """Specific frequency schema ID override (e.g.

    'biomedical:scifact:2.0.0'). Takes precedence over domain.
    """

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
    """Which output fields to return.

    Default: ['rotation_v3', 'metadata']. Request only what you need to minimize
    response size.
    """
