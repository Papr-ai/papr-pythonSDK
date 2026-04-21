# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .transform_data import TransformData

__all__ = ["TransformCreateResponse"]


class TransformCreateResponse(BaseModel):
    """Response for POST /v1/holographic/transform"""

    data: TransformData
    """Inner data for transform response — only requested fields are populated."""

    status: Optional[str] = None
