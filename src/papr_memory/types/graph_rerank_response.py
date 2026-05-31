# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["GraphRerankResponse", "Meta", "Result", "ResultDocument"]


class Meta(BaseModel):
    domain_id: str

    method_used: Literal["enhanced", "max", "fast"]

    billed_units: Optional[int] = None
    """Mini interactions consumed."""

    debug: Optional[Dict[str, object]] = None
    """Debug payload when return_debug=true.

    Includes: `selection_signals` (scalar routing inputs), `v3a_routing` /
    `v4a_routing` (method selection diagnostics), `routing_signals` (method_bgrs,
    method_t1lrs, pool quality), `spread_signals` (gauss/sfi/hcond spread boosters),
    `signal_multipliers`, `signal_weights`, `signal_weights_sparse`,
    `routing_config`, `domain_method_priors`, `doc_scores` (per-doc method score
    vectors), `router_state` (v4a EMA snapshot), `rule_fired`, `zone`,
    `caesar8_mode`. Per-phase timings live in `timing_ms.phases`.
    """

    timing_ms: Optional[Dict[str, object]] = None
    """Latency breakdown in milliseconds.

    Top-level keys: `services_init`, `pipeline`, `total`. Optional `phases` is a
    nested dict with per-stage timings: query_processing, retrieval, rerank,
    caesar_routing.
    """

    usage: Optional[Dict[str, object]] = None
    """Cohere/Voyage-compatible usage block, e.g.

    {'search_units': 1, 'docs_scored': 100}. Populated for /v1/graph/rerank and
    /v1/graph/search.
    """


class ResultDocument(BaseModel):
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


class Result(BaseModel):
    index: int
    """Position in the input documents array."""

    relevance_score: float
    """Final ranked score — the real similarity from the CAESAR-8 routed method."""

    id: Optional[str] = None
    """Doc id if input was an object, else null."""

    debug_scores: Optional[Dict[str, float]] = None
    """Kitchen-sink: every \\**\\__sim signal computed by the pipeline.

    Only if return_debug=true. NOT a stable contract — keys may change.
    """

    document: Optional[ResultDocument] = None
    """Object form of a document (when developer wants to attach an id/metadata).

    Either `embedding` or `text` should be set; both are accepted by the rerank
    pipeline. `metadata` round-trips into the response if requested.

    BYO artifact fields (`signals`, `signal_embeddings`, `phases`, `rot_v3`,
    `concat_embedding`) are all optional and let callers skip the per-doc
    extract+embed pass at scoring time. They map 1:1 to the producer fields returned
    by /v1/graph/transform.
    """

    score_method: Optional[str] = None
    """Which method CAESAR-8 routed to for this query (e.g.

    'caesar7', 'baseline_rerank'). Tells you what kind of signal `relevance_score`
    reflects.
    """

    signal_scores: Optional[Dict[str, float]] = None
    """Stable, documented signals (only if return_signal_scores=true).

    Always includes `base_sim` and `caesar8_score`. On `enhanced` method, also
    includes `rot_k{32,128,256,512}_sim` low-rank rotation variants.
    """

    signal_scores_by_band: Optional[Dict[str, float]] = None
    """Per-band signal similarities, keyed by band name (e.g.

    {'causal_agent': 0.83, 'causal_verb': 0.91}). Only set if
    return_signal_scores=true and the pipeline computed gated SFI.
    """


class GraphRerankResponse(BaseModel):
    id: str
    """Request id for log correlation."""

    meta: Meta

    results: List[Result]
