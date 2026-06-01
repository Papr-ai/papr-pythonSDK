# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

from ..graph_domain_routing_config_param import GraphDomainRoutingConfigParam

__all__ = ["DomainUpdateParams"]


class DomainUpdateParams(TypedDict, total=False):
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
