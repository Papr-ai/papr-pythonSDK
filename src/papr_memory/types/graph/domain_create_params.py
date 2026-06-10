# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

from .signal_field_param import SignalFieldParam
from ..graph_domain_routing_config_param import GraphDomainRoutingConfigParam

__all__ = ["DomainCreateParams", "CatalogConfig"]


class DomainCreateParams(TypedDict, total=False):
    description: Required[str]
    """What this domain models."""

    domain_id: Required[str]
    """Custom id, e.g. 'acme:support_tickets:1.0.0'."""

    name: Required[str]
    """Human-readable domain name."""

    signals: Required[Iterable[SignalFieldParam]]
    """Per-domain signal definitions."""

    catalog_config: Optional[CatalogConfig]
    """Catalog settings on a domain."""

    routing_config: Optional[GraphDomainRoutingConfigParam]
    """Domain-scoped CAESAR-VIII routing overrides (stored on graph_domains)."""

    signal_multipliers: Optional[Dict[str, float]]
    """Domain-level default signal weight multipliers.

    Applied automatically on every rerank/search request for this domain (unless the
    caller supplies their own signal_multipliers, which take priority). Keys are
    field names (e.g. 'key_claim') or Hz-strings (e.g. '70.0'). Values: 0.0 =
    disable band, 1.0 = unchanged, 2.0 = 2× boost.
    """


class CatalogConfig(TypedDict, total=False):
    """Catalog settings on a domain."""

    enabled: bool
    """Whether to auto-accumulate signals on transform."""

    refresh_every_n: int
    """Run LLM clustering after this many buffered entries."""
