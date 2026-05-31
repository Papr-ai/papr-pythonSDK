# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["GraphDomainRoutingConfigParam"]


class GraphDomainRoutingConfigParam(TypedDict, total=False):
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
