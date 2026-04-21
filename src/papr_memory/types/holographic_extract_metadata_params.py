# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["HolographicExtractMetadataParams"]


class HolographicExtractMetadataParams(TypedDict, total=False):
    content: Required[str]
    """Text content for metadata extraction"""

    context_metadata: Optional[Dict[str, object]]
    """Optional context metadata (createdAt, sourceType, etc.) to improve extraction."""

    domain: Optional[str]
    """Domain for frequency schema"""

    frequency_schema_id: Optional[str]
    """Schema override"""
