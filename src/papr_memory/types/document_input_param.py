# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import TypedDict

__all__ = ["DocumentInputParam"]


class DocumentInputParam(TypedDict, total=False):
    """Object form of a document (when developer wants to attach an id/metadata).

    Either ``embedding`` or ``text`` should be set; both are accepted by the
    rerank pipeline. ``metadata`` round-trips into the response if requested.

    BYO artifact fields (``signals``, ``signal_embeddings``,
    ``phases``, ``rot_v3``, ``concat_embedding``) are all optional and let
    callers skip the per-doc extract+embed pass at scoring time. They map
    1:1 to the producer fields returned by /v1/graph/transform.
    """

    id: Optional[str]
    """Stable doc identifier echoed back in results."""

    concat_embedding: Optional[Iterable[float]]
    """Pre-computed concat reconstruction."""

    embedding: Optional[Iterable[float]]
    """Pre-computed base embedding (BYOE). Qwen 2560-d expected."""

    metadata: Optional[Dict[str, object]]
    """Free-form user metadata, echoed back if return_documents=true."""

    phases: Optional[Iterable[float]]
    """Pre-computed per-frequency phase angles (14-dim).

    If provided, phase computation is skipped.
    """

    rot_v3: Optional[Iterable[float]]
    """Pre-computed rotation v3 vector."""

    signal_embeddings: Optional[Dict[str, Iterable[float]]]
    """Pre-computed signal band-name -> vector (typically 384d sbert).

    If provided, per-band embedding step is skipped.
    """

    signals: Optional[Dict[str, str]]
    """Pre-extracted signal band-name -> text.

    If provided, the LLM extractor is skipped for this doc.
    """

    text: Optional[str]
    """Document text (if not BYOE)."""
