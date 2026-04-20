# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["MemoryDeleteAllParams"]


class MemoryDeleteAllParams(TypedDict, total=False):
    external_user_id: Optional[str]
    """Optional external user ID to resolve and delete memories for"""

    skip_parse: bool
    """Skip Parse Server deletion"""

    user_id: Optional[str]
    """
    Optional user ID to delete memories for (if not provided, uses authenticated
    user)
    """
