# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .transform_data import TransformData

__all__ = ["TransformCreateBatchResponse", "Result"]


class Result(BaseModel):
    """Single result in a batch transform response."""

    id: str

    data: TransformData
    """Inner data for transform response — only requested fields are populated."""


class TransformCreateBatchResponse(BaseModel):
    """Response for POST /v1/holographic/transform/batch"""

    results: List[Result]

    timing_ms: float

    total: int

    status: Optional[str] = None
