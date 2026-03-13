# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
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

    embedding: Optional[Iterable[float]]
    """Base embedding. If missing and content provided, computed server-side."""

    phases: Optional[Iterable[float]]
    """Pre-computed phases from a prior /transform call. Enables fast path."""

    score: Optional[float]
    """Original retrieval score (used as a signal in ensemble methods)"""


class Options(TypedDict, total=False):
    """Options for the rerank endpoint."""

    ensemble: Literal["auto", "caesar_8", "caesar_9"]
    """Ensemble method: 'auto' (recommended), 'caesar_8', or 'caesar_9'"""

    return_scores: bool
    """Include per-method score breakdown in response"""

    scoring_method: Optional[str]
    """Specific scoring method from 160+ available (power user). Overrides ensemble."""

    use_cross_encoder: bool
    """Enable cross-encoder scoring. Requires content on candidates."""
