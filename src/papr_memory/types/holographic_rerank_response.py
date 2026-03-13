# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["HolographicRerankResponse", "Data", "DataRanking"]


class DataRanking(BaseModel):
    """Single ranked result."""

    id: str

    path: str
    """'fast' (phases provided) or 'cold' (content-only)"""

    rank: int

    score: float
    """Ensemble score"""

    original_score: Optional[float] = None
    """Original retrieval score if provided"""

    scores: Optional[Dict[str, float]] = None
    """Per-method score breakdown (if return_scores=true)"""


class Data(BaseModel):
    domain: str

    ensemble_used: str

    rankings: List[DataRanking]

    timing_ms: float

    optimization_hint: Optional[str] = None
    """Present when cold path was used. Suggests storing phases for faster reranking."""


class HolographicRerankResponse(BaseModel):
    """Response for POST /v1/holographic/rerank"""

    data: Data

    status: Optional[str] = None
