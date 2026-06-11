# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

from ..graph_domain_routing_config_param import GraphDomainRoutingConfigParam

__all__ = ["DomainUpdateParams", "CatalogConfig"]


class DomainUpdateParams(TypedDict, total=False):
    catalog_config: Optional[CatalogConfig]
    """Catalog settings on a domain."""

    description: Optional[str]
    """Updated description."""

    name: Optional[str]
    """Updated human-readable name."""

    routing_config: Optional[GraphDomainRoutingConfigParam]
    """Domain-scoped CAESAR-VIII routing overrides (stored on graph_domains)."""

    signal_multipliers: Optional[Dict[str, float]]
    """Replace the domain-level signal_multipliers entirely.

    Pass an empty dict {} to clear all multipliers. Omit the field to leave existing
    multipliers unchanged.
    """


class CatalogConfig(TypedDict, total=False):
    """Catalog settings on a domain."""

    enabled: bool
    """Whether to auto-accumulate signals on transform."""

    refresh_every_n: int
    """Run LLM clustering after this many buffered entries."""
