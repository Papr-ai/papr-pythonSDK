# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["MemoryGetParams"]


class MemoryGetParams(TypedDict, total=False):
    exclude_flagged: bool
    """If true, return 404 if the memory has risk='flagged'.

    Filters out flagged content.
    """

    max_risk: Optional[str]
    """Maximum risk level allowed.

    Values: 'none', 'sensitive', 'flagged'. If memory exceeds this, return 404.
    """

    require_consent: bool
    """If true, return 404 if the memory has consent='none'.

    Ensures only consented memories are returned.
    """
