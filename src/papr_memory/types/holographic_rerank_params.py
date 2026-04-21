# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["HolographicRerankParams", "Candidate", "Options"]


class HolographicRerankParams(TypedDict, total=False):
    candidates: Required[Iterable[Candidate]]
    """Candidate documents to rerank (max 100)"""

    query: Required[str]
    """The search query text"""

    domain: Optional[str]
    """Domain for frequency schema"""

    frequency_schema_id: Optional[str]
    """Schema override"""

    options: Optional[Options]
    """Options for the rerank endpoint."""

    query_embedding: Optional[Iterable[float]]
    """Query embedding in the same space as candidate embeddings.

    If provided, used for cosine similarity. If omitted, computed server-side (Qwen
    2560d).
    """

    query_metadata_embeddings: Optional[Dict[str, Iterable[float]]]
    """
    Pre-computed query metadata embeddings from a prior /transform call (keyed by
    frequency string, e.g. '0.1'). Required for full HCond scoring with phase
    alignment.
    """

    query_phases: Optional[Iterable[float]]
    """Pre-computed query phases from a prior /transform call.

    If provided alongside query_embedding, skips LLM extraction entirely (hot path).
    """

    top_k: int
    """Number of results to return"""


class Candidate(TypedDict, total=False):
    """A candidate document for reranking.

    Auto-detection:
    - If `phases` is provided → FAST PATH (skip LLM extraction, ~2-5ms)
    - If only `content` → COLD PATH (LLM extraction + optional cross-encoder, ~100ms)
    - Must have at least one of `content` or `phases`
    """

    id: Required[str]
    """Unique identifier"""

    content: Optional[str]
    """Text content. Required for cold path (LLM extraction + cross-encoder)."""

    context_metadata: Optional[Dict[str, object]]
    """
    Optional context metadata for cold-path LLM extraction (createdAt, sourceType,
    etc.)
    """

    embedding: Optional[Iterable[float]]
    """Base embedding. If missing and content provided, computed server-side."""

    metadata_embeddings: Optional[Dict[str, Iterable[float]]]
    """
    Pre-computed SBERT metadata embeddings from a prior /transform call (keyed by
    frequency string, e.g. '0.1'). Enables full HCond scoring.
    """

    phases: Optional[Iterable[float]]
    """Pre-computed phases from a prior /transform call. Enables fast path."""

    score: Optional[float]
    """Original retrieval score (used as a signal in ensemble methods)"""


class Options(TypedDict, total=False):
    """Options for the rerank endpoint."""

    cross_encoder_model: str
    """Cross-encoder model name.

    Options: 'BAAI/bge-reranker-v2-m3' (fast, default), 'Qwen/Qwen3-Reranker-0.6B'
    (balanced), 'Qwen/Qwen3-Reranker-4B' (best quality).
    """

    cross_encoder_weight: float
    """Weight for cross-encoder score in final blend.

    final = (1 - weight) _ hcond + weight _ cross_encoder. Default 0.3.
    """

    ensemble: Literal["auto", "caesar_8", "caesar_9"]
    """Ensemble method: 'auto' (recommended), 'caesar_8', or 'caesar_9'"""

    frequency_filters: Optional[Dict[str, float]]
    """Filter candidates by minimum per-frequency-field score.

    Keys are field names (e.g. 'date', 'entity'), values are min scores [0, 1].
    """

    include_frequency_scores: bool
    """Include per-frequency-field alignment scores (e.g.

    date: 0.92, entity: 0.45). Requires return_scores=true to take effect.
    """

    return_scores: bool
    """Include per-method score breakdown in response"""

    scoring_method: Optional[str]
    """Specific scoring method from 160+ available (power user). Overrides ensemble."""

    use_cross_encoder: bool
    """Enable cross-encoder scoring.

    Requires content on candidates. Adds ~20-50ms per candidate but improves ranking
    quality by 3-8%%.
    """
