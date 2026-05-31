# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "DomainRetrieveResponse",
    "Signal",
    "Catalog",
    "CatalogEntityCluster",
    "CatalogRelationshipPattern",
    "CatalogBuffer",
    "CatalogConfig",
    "RoutingConfig",
]


class Signal(BaseModel):
    description: str
    """Human prompt used by extractor."""

    name: str
    """Snake_case signal identifier."""

    allowed_values: Optional[List[str]] = None
    """For type='enum': allowed vocabulary."""

    frequency_hz: Optional[float] = None
    """Hz band mapping (0.1 … 70.0). Auto-assigned if omitted."""

    required: Optional[bool] = None
    """Warn when missing at extract time."""

    type: Optional[Literal["enum", "text", "numeric", "date", "boolean", "multi_value_text"]] = None
    """Extraction / phase type for this signal."""

    weight: Optional[float] = None
    """Relative weight in the fusion."""


class CatalogEntityCluster(BaseModel):
    """A cluster of semantically-similar entity values."""

    label: str
    """LLM-chosen canonical label for this cluster."""

    count: Optional[int] = None
    """Total occurrences across all transforms."""

    members: Optional[List[str]] = None
    """Raw signal values merged into this cluster."""


class CatalogRelationshipPattern(BaseModel):
    """A cluster of semantically-similar relationship types."""

    label: str
    """Canonical label (e.g. 'Causal', 'Preventive')."""

    count: Optional[int] = None
    """Total occurrences."""

    members: Optional[List[str]] = None
    """Raw relationship values in this cluster."""


class Catalog(BaseModel):
    """Curated summary of what's in a domain's frequency space."""

    domain_distribution: Optional[Dict[str, int]] = None
    """Signal band name -> total doc count."""

    entity_clusters: Optional[List[CatalogEntityCluster]] = None

    last_refreshed: Optional[str] = None
    """ISO timestamp of last LLM clustering run."""

    last_updated: Optional[str] = None
    """ISO timestamp of last buffer append."""

    relationship_patterns: Optional[List[CatalogRelationshipPattern]] = None

    signal_value_counts: Optional[Dict[str, Dict[str, int]]] = None
    """Per-band raw value counts, e.g. {'domain': {'Health': 500, 'Tech': 200}}."""

    total_documents: Optional[int] = None
    """Total transforms processed."""


class CatalogBuffer(BaseModel):
    """Raw signal snapshot from a single transform call."""

    signals: Dict[str, str]
    """Band name -> extracted value."""

    timestamp: str
    """ISO timestamp of the transform call."""


class CatalogConfig(BaseModel):
    """Catalog settings on a domain."""

    enabled: Optional[bool] = None
    """Whether to auto-accumulate signals on transform."""

    refresh_every_n: Optional[int] = None
    """Run LLM clustering after this many buffered entries."""


class RoutingConfig(BaseModel):
    """Domain-scoped CAESAR-VIII routing overrides (stored on graph_domains)."""

    caesar4_source: Optional[str] = None
    """
    Which ranking is exposed as rankings['caesar4'] to CAESAR-VIII rules
    (c4_c7_diverge, etc.). Accepts 'v4a' (default — alias to family-routed v4a / v3a
    fallback), 'v3a' (force v3a only), or 'legacy' (SKIP the alias; keep the
    original Jaccard / trust-score selection at rankings['caesar4'] and stash a copy
    at rankings['_caesar4_legacy']). Use 'legacy' to A/B C-VIII rules against the
    original SciFact calibration semantics. Label-free in all modes.
    """

    ce_gate_min_phi: Optional[float] = None
    """Minimum phi to allow caesar7/baseline_rerank to bypass holographic floor."""

    disabled_rules: Optional[List[str]] = None
    """Global SciFact routing rule names to skip for this domain (e.g.

    'DANGER_LOW_RSG_LOW_PHI').
    """

    egr_lambda_ce: Optional[float] = None
    """Stacked EGR entailment fusion weight (0–1). Lower for code domains."""

    enabled_rule_packs: Optional[List[str]] = None
    """Named domain rule packs to run after global rules (e.g. 'cosqa_caesar8_v2')."""

    enhanced_initial_source: Optional[str] = None
    """CAESAR-VIII initial source for the CE-on path.

    Domain defaults may pin 'caesar4_5_v4a' on code_search for public enhanced;
    public max overrides to 'caesar7' unless this field is set.
    """

    holographic_floor: Optional[bool] = None
    """
    When true, never return a ranking worse than max(v4a, baseline) unless CE gate
    (ce_gate_min_phi) passes.
    """

    threshold_overrides: Optional[Dict[str, float]] = None
    """Optional CaesarConfig field overrides keyed by threshold name (e.g.

    {'cmas_c4_trust_jaccard_threshold': 0.95}).
    """


class DomainRetrieveResponse(BaseModel):
    description: str

    domain_id: str

    name: str

    signals: List[Signal]

    builtin: Optional[bool] = None
    """True for built-in domains shipped with Papr (read-only)."""

    catalog: Optional[Catalog] = None
    """Curated summary of what's in a domain's frequency space."""

    catalog_buffer: Optional[List[CatalogBuffer]] = None
    """Buffered raw signals awaiting LLM clustering (internal)."""

    catalog_config: Optional[CatalogConfig] = None
    """Catalog settings on a domain."""

    created_at: Optional[str] = None

    owner_namespace_id: Optional[str] = None
    """Namespace this domain belongs to, if any."""

    owner_organization_id: Optional[str] = None
    """Organization that owns this domain."""

    owner_user_id: Optional[str] = None

    owner_workspace_id: Optional[str] = None
    """Workspace that owns this domain. Domains are scoped to workspace when set."""

    routing_config: Optional[RoutingConfig] = None
    """Domain-scoped CAESAR-VIII routing overrides (stored on graph_domains)."""

    signal_multipliers: Optional[Dict[str, float]] = None
    """Domain-level default signal multipliers (see GraphDomainCreate)."""
