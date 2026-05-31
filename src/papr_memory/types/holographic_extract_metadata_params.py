# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["HolographicExtractMetadataParams"]


class HolographicExtractMetadataParams(TypedDict, total=False):
    content: Required[str]
    """Text content for metadata extraction"""

    concat_embedding: Optional[Iterable[float]]
    """Pre-computed concat (new) embedding from holographic transform."""

    context_metadata: Optional[Dict[str, object]]
    """Optional context metadata (createdAt, sourceType, etc.) to improve extraction."""

    domain: Optional[str]
    """Domain for frequency schema"""

    frequency_schema_id: Optional[str]
    """Schema override"""

    rotation_embedding: Optional[Iterable[float]]
    """Pre-computed rotation (old) embedding from holographic transform.

    Enables rot_v2/v3 similarity scoring and full CAESAR ensemble.
    """

    rotation_v2_embedding: Optional[Iterable[float]]
    """Pre-computed rotation V2 embedding from holographic transform."""

    rotation_v3_embedding: Optional[Iterable[float]]
    """Pre-computed rotation V3 embedding from holographic transform."""
