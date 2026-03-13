# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["NamespaceCreateParams"]


class NamespaceCreateParams(TypedDict, total=False):
    name: Required[str]
    """Namespace name (e.g., 'acme-production')"""

    environment_type: Literal["development", "staging", "production"]
    """Environment type: development, staging, production"""

    is_active: bool
    """Whether this namespace is active"""

    rate_limits: Optional[Dict[str, Optional[int]]]
    """Rate limits for this namespace (None values inherit from organization)"""
