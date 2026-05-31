# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .document_input_param import DocumentInputParam
from .graph_domain_routing_config_param import GraphDomainRoutingConfigParam

__all__ = ["GraphRerankParams", "Document", "Query", "QueryQueryItem"]


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

    routing_config: Optional[GraphDomainRoutingConfigParam]
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


Document: TypeAlias = Union[str, DocumentInputParam]


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
