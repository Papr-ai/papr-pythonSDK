# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["NamespaceUpdateParams"]


class NamespaceUpdateParams(TypedDict, total=False):
    environment_type: Optional[Literal["development", "staging", "production"]]
    """Environment types for namespaces"""

    is_active: Optional[bool]
    """Whether this namespace is active"""

    name: Optional[str]
    """Updated namespace name"""

    rate_limits: Optional[Dict[str, Optional[int]]]
    """Updated rate limits (None values inherit from organization)"""
