# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel
from .signal_field import SignalField
from .domain_catalog import DomainCatalog
from .catalog_buffer_entry import CatalogBufferEntry
from .domain_catalog_config import DomainCatalogConfig
from ..graph_domain_routing_config import GraphDomainRoutingConfig

__all__ = ["DomainListResponse", "Domain"]


class Domain(BaseModel):
    description: str

    domain_id: str

    name: str

    signals: List[SignalField]

    builtin: Optional[bool] = None
    """True for built-in domains shipped with Papr (read-only)."""

    catalog: Optional[DomainCatalog] = None
    """Curated summary of what's in a domain's frequency space."""

    catalog_buffer: Optional[List[CatalogBufferEntry]] = None
    """Buffered raw signals awaiting LLM clustering (internal)."""

    catalog_config: Optional[DomainCatalogConfig] = None
    """Catalog settings on a domain."""

    created_at: Optional[str] = None

    owner_namespace_id: Optional[str] = None
    """Namespace this domain belongs to, if any."""

    owner_organization_id: Optional[str] = None
    """Organization that owns this domain."""

    owner_user_id: Optional[str] = None

    owner_workspace_id: Optional[str] = None
    """Workspace that owns this domain. Domains are scoped to workspace when set."""

    routing_config: Optional[GraphDomainRoutingConfig] = None
    """Domain-scoped CAESAR-VIII routing overrides (stored on graph_domains)."""

    signal_multipliers: Optional[Dict[str, float]] = None
    """Domain-level default signal multipliers (see GraphDomainCreate)."""


class DomainListResponse(BaseModel):
    domains: List[Domain]
