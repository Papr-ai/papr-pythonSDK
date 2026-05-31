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

    frequency_scores: Optional[Dict[str, float]] = None
    """
    Per-frequency-field alignment scores (when
    options.include_frequency_scores=true).
    """

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

    query_dimension_weights: Optional[Dict[str, float]] = None
    """LLM-determined importance weights per dimension for this query (0.0-1.0).

    Shows how the adaptive weighting system interpreted this query's intent.
    """


class HolographicRerankResponse(BaseModel):
    """Response for POST /v1/holographic/rerank"""

    data: Data

    status: Optional[str] = None
