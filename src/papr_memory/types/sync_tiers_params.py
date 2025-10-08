# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from .._types import NOT_GIVEN, NotGiven
from .._models import BaseModel

__all__ = ["SyncTiersParams"]


class SyncTiersParams(BaseModel):
    include_embeddings: Optional[bool] = None
    embed_limit: Optional[int] = None
    max_tier0: Optional[int] = None
    max_tier1: Optional[int] = None
