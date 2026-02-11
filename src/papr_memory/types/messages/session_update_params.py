# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["SessionUpdateParams"]


class SessionUpdateParams(TypedDict, total=False):
    metadata: Optional[Dict[str, object]]
    """Metadata to merge with existing session metadata"""

    title: Optional[str]
    """New title for the session"""
