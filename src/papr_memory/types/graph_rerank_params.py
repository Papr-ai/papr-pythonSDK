# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = ["GraphRerankParams", "Document", "DocumentDocumentInput", "Query", "QueryQueryItem", "RoutingConfig"]


class GraphRerankParams(TypedDict, total=False):
    documents: Required[SequenceNotStr[Document]]
    """Candidate documents (string or DocumentInput with pre-computed artifacts)."""

    query: Required[Query]
    """Query text (string) or QueryItem with pre-computed artifacts."""

    domain_id: Optional[str]
    """
    Domain shortname or full schema id controlling which frequency bands and
    extraction rules are used. Built-in shortnames: "general" (default), "code",
    "cosqa", "codetrans", "codetransocean", "codetransocean_hybrid", "text2sql",
    "scifact", "nfcorpus", "fiqa", "legal", "medical", "ecommerce", "coffee_shops".
    You can also pass a full schema id (e.g. "code_search:cosqa:2.0.0") or a custom
    domain_id registered via POST /v1/graph/domains.
    """

    method: Literal["fast", "enhanced"]
    """Public: enhanced or max (CE reranker).

    Accepts deprecated 'fast'/'enhanced' aliases.
    """

    return_debug: bool
    """If true, include CAESAR meta-signals + timing in `meta.debug`."""

    return_documents: bool
    """If true, echo back each input document in the result."""

    return_signal_scores: bool
    """
    If true, each result carries `signal_scores` (method-level scores like
    `base_sim`, `caesar8_score`) and `signal_scores_by_band` (per-frequency band
    alignments such as `key_apis`, `language`).
    """

    routing_config: Optional[RoutingConfig]
    """Domain-scoped CAESAR-VIII routing overrides (stored on graph_domains)."""

    signal_embedder: Literal["sbert", "qwen"]
    """Embedder for per-band signal vectors when extracting query/docs.

    'sbert' (384d, default) is ~10x cheaper to store than 'qwen' (2560d). Must match
    the embedder used for any BYO signal_embeddings.
    """

    signal_filters: Optional[Dict[str, float]]
    """Hard cutoffs on per-frequency signals, e.g.

    {'domain_match': 0.6}. Docs below are dropped.
    """

    signal_multipliers: Optional[Dict[str, object]]
    """Per-frequency scoring weight multipliers.

    Keys may be field names (e.g. 'claim_stance', 'causal_verb') or Hz-strings (e.g.
    '19.0'). Values: 'auto' (default) or 1.0 = unchanged, 2.0 = 2x boost, 0.0 =
    disable that band. Fields not specified default to 'auto'. Stacks on top of the
    schema-level FrequencyField.weight multipliers; request-level overrides win on
    conflict.
    """

    top_k: Optional[int]
    """Return at most this many results. Defaults to len(documents)."""


class DocumentDocumentInput(TypedDict, total=False):
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


Document: TypeAlias = Union[str, DocumentDocumentInput]


class QueryQueryItem(TypedDict, total=False):
    """Query with optional pre-computed artifacts from /v1/graph/transform.

    Similar to DocumentInput but for queries. Pass pre-computed artifacts
    to skip LLM extraction and embedding for faster reranking.
    """

    text: Required[str]
    """Query text."""

    concat_embedding: Optional[Iterable[float]]
    """Pre-computed concat reconstruction."""

    embedding: Optional[Iterable[float]]
    """Pre-computed base embedding. Skips embedder call."""

    phases: Optional[Iterable[float]]
    """Pre-computed per-frequency phase angles (14-dim)."""

    rot_v3: Optional[Iterable[float]]
    """Pre-computed rotation v3 vector."""

    signal_embeddings: Optional[Dict[str, Iterable[float]]]
    """Pre-computed signal band-name -> vector. Skips per-band embed."""

    signals: Optional[Dict[str, str]]
    """Pre-extracted signal band-name -> text. Skips LLM extractor."""


Query: TypeAlias = Union[str, QueryQueryItem]


class RoutingConfig(TypedDict, total=False):
    """Domain-scoped CAESAR-VIII routing overrides (stored on graph_domains)."""

    caesar4_source: Optional[str]
    """
    Which ranking is exposed as rankings['caesar4'] to CAESAR-VIII rules
    (c4_c7_diverge, etc.). Accepts 'v4a' (default — alias to family-routed v4a / v3a
    fallback), 'v3a' (force v3a only), or 'legacy' (SKIP the alias; keep the
    original Jaccard / trust-score selection at rankings['caesar4'] and stash a copy
    at rankings['_caesar4_legacy']). Use 'legacy' to A/B C-VIII rules against the
    original SciFact calibration semantics. Label-free in all modes.
    """

    ce_gate_min_phi: Optional[float]
    """Minimum phi to allow caesar7/baseline_rerank to bypass holographic floor."""

    disabled_rules: Optional[SequenceNotStr[str]]
    """Global SciFact routing rule names to skip for this domain (e.g.

    'DANGER_LOW_RSG_LOW_PHI').
    """

    egr_lambda_ce: Optional[float]
    """Stacked EGR entailment fusion weight (0–1). Lower for code domains."""

    enabled_rule_packs: Optional[SequenceNotStr[str]]
    """Named domain rule packs to run after global rules (e.g. 'cosqa_caesar8_v2')."""

    enhanced_initial_source: Optional[str]
    """CAESAR-VIII initial source for the CE-on path.

    Domain defaults may pin 'caesar4_5_v4a' on code_search for public enhanced;
    public max overrides to 'caesar7' unless this field is set.
    """

    holographic_floor: Optional[bool]
    """
    When true, never return a ranking worse than max(v4a, baseline) unless CE gate
    (ce_gate_min_phi) passes.
    """

    threshold_overrides: Optional[Dict[str, float]]
    """Optional CaesarConfig field overrides keyed by threshold name (e.g.

    {'cmas_c4_trust_jaccard_threshold': 0.95}).
    """
