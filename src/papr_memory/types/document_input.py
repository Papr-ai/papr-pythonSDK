# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["DocumentInput"]


class DocumentInput(BaseModel):
    """Object form of a document (when developer wants to attach an id/metadata).

    Either ``embedding`` or ``text`` should be set; both are accepted by the
    rerank pipeline. ``metadata`` round-trips into the response if requested.

    BYO artifact fields (``signals``, ``signal_embeddings``,
    ``phases``, ``rot_v3``, ``concat_embedding``) are all optional and let
    callers skip the per-doc extract+embed pass at scoring time. They map
    1:1 to the producer fields returned by /v1/graph/transform.
    """

    id: Optional[str] = None
    """Stable doc identifier echoed back in results."""

    concat_embedding: Optional[List[float]] = None
    """Pre-computed concat reconstruction."""

    embedding: Optional[List[float]] = None
    """Pre-computed base embedding (BYOE). Qwen 2560-d expected."""

    metadata: Optional[Dict[str, object]] = None
    """Free-form user metadata, echoed back if return_documents=true."""

    phases: Optional[List[float]] = None
    """Pre-computed per-frequency phase angles (14-dim).

    If provided, phase computation is skipped.
    """

    rot_v3: Optional[List[float]] = None
    """Pre-computed rotation v3 vector."""

    signal_embeddings: Optional[Dict[str, List[float]]] = None
    """Pre-computed signal band-name -> vector (typically 384d sbert).

    If provided, per-band embedding step is skipped.
    """

    signals: Optional[Dict[str, str]] = None
    """Pre-extracted signal band-name -> text.

    If provided, the LLM extractor is skipped for this doc.
    """

    text: Optional[str] = None
    """Document text (if not BYOE)."""
