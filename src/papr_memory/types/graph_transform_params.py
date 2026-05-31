# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["GraphTransformParams"]


class GraphTransformParams(TypedDict, total=False):
    text: Required[str]
    """Source text to transform."""

    domain_id: Optional[str]
    """
    Domain shortname or full schema id controlling which frequency bands and
    extraction rules are used. Built-in shortnames: "general" (default), "code",
    "cosqa", "codetrans", "codetransocean", "codetransocean_hybrid", "text2sql",
    "scifact", "nfcorpus", "fiqa", "legal", "medical", "ecommerce", "coffee_shops".
    You can also pass a full schema id (e.g. "code_search:cosqa:2.0.0") or a custom
    domain_id registered via POST /v1/graph/domains.
    """

    embedding: Optional[Iterable[float]]
    """Optional caller-provided base embedding (Qwen 2560-d).

    If omitted, the server computes it.
    """

    metadata: Optional[Dict[str, object]]
    """Free-form user metadata to attach (optional, not used for scoring)."""

    return_concat: bool
    """If true, include the base + bands concatenation embedding."""

    return_rot_v3: bool
    """If true, include the rot_v3 vector in the response."""

    signal_embedder: Literal["sbert", "qwen"]
    """Embedder for per-band signal vectors.

    'sbert' (384d, default) is ~10x cheaper to store than 'qwen' (2560d, matched to
    base).
    """
