# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["GraphTransformResponse"]


class GraphTransformResponse(BaseModel):
    """Transform response - returns artifacts that can be passed to rerank/search.

    All fields map 1:1 to DocumentInput fields for rerank.
    """

    id: str
    """Request id for log correlation."""

    domain_id: str
    """Domain used for extraction."""

    embedding: List[float]
    """Base embedding (normalized Qwen 2560-d)."""

    phases: List[float]
    """Per-frequency phase angles (14-dim)."""

    concat_embedding: Optional[List[float]] = None
    """Base + bands concatenation (only when return_concat=true)."""

    meta: Optional[Dict[str, object]] = None
    """Timing and stats."""

    rot_v3: Optional[List[float]] = None
    """Rotation v3 vector (only when return_rot_v3=true)."""

    signal_embeddings: Optional[Dict[str, List[float]]] = None
    """Signal band-name -> embedding vector (384-d sbert or 2560-d qwen)."""

    signals: Optional[Dict[str, str]] = None
    """Signal band-name -> extracted text (e.g.

    {'docstring': '...', 'function_name': '...'}).
    """
