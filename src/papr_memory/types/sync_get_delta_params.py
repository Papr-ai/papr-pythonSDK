# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["SyncGetDeltaParams"]


class SyncGetDeltaParams(TypedDict, total=False):
    cursor: Optional[str]
    """Opaque cursor from previous sync"""

    include_embeddings: bool

    limit: int

    workspace_id: Optional[str]
