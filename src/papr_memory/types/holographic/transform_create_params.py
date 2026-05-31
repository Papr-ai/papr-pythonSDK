# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TransformCreateParams"]


class TransformCreateParams(TypedDict, total=False):
    content: Required[str]
    """Text content for LLM metadata extraction"""

    embedding: Required[Iterable[float]]
    """Base embedding vector (any dimensionality)"""

    concat_embedding: Optional[Iterable[float]]
    """Pre-computed concat (new) embedding from holographic transform."""

    context_metadata: Optional[Dict[str, object]]
    """
    Optional context metadata (createdAt, sourceType, customMetadata, etc.) to
    improve LLM extraction accuracy, especially for dates and entities.
    """

    domain: Optional[str]
    """Domain for frequency schema selection (e.g. 'biomedical', 'code', 'general')"""

    frequency_schema_id: Optional[str]
    """Specific frequency schema ID override (e.g.

    'biomedical:scifact:2.0.0'). Takes precedence over domain.
    """

    is_query: bool
    """
    If true, treat content as a query (not a doc): runs adaptive dimension-weight
    scoring and returns weights in TransformData. Pass these weights into a
    subsequent /rerank call as `query_dimension_weights` to skip recomputation.
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

    rotation_embedding: Optional[Iterable[float]]
    """Pre-computed rotation (old) embedding from holographic transform.

    Enables rot_v2/v3 similarity scoring and full CAESAR ensemble.
    """

    rotation_v2_embedding: Optional[Iterable[float]]
    """Pre-computed rotation V2 embedding from holographic transform."""

    rotation_v3_embedding: Optional[Iterable[float]]
    """Pre-computed rotation V3 embedding from holographic transform."""
