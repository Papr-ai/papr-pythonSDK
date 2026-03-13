# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["TransformCreateBatchResponse", "Result", "ResultData"]


class ResultData(BaseModel):
    """Inner data for transform response — only requested fields are populated."""

    base_dim: int
    """Input embedding dimensionality"""

    domain: str
    """Domain used for this transform"""

    frequency_schema_id: str
    """Exact frequency schema ID used"""

    timing_ms: float
    """Server-side processing time in milliseconds"""

    base: Optional[List[float]] = None
    """Original embedding echoed back"""

    concat: Optional[List[float]] = None
    """Concatenation transform (input_dims + 196)"""

    metadata: Optional[Dict[str, object]] = None
    """LLM-extracted metadata keyed by frequency field name"""

    metadata_embeddings: Optional[Dict[str, List[float]]] = None
    """Per-frequency metadata embeddings"""

    phases: Optional[List[float]] = None
    """14 raw phase values for on-device reconstruction and fast-path rerank"""

    rotation_v1: Optional[List[float]] = None
    """Rotation V1 transform (same dims as input)"""

    rotation_v2: Optional[List[float]] = None
    """Rotation V2 transform (same dims as input)"""

    rotation_v3: Optional[List[float]] = None
    """Rotation V3 transform (recommended for search, same dims as input)"""


class Result(BaseModel):
    """Single result in a batch transform response."""

    id: str

    data: ResultData
    """Inner data for transform response — only requested fields are populated."""


class TransformCreateBatchResponse(BaseModel):
    """Response for POST /v1/holographic/transform/batch"""

    results: List[Result]

    timing_ms: float

    total: int

    status: Optional[str] = None
