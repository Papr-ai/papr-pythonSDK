# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel
from .signal_field import SignalField
from .catalog_buffer_entry import CatalogBufferEntry
from .catalog_entity_cluster import CatalogEntityCluster
from ..graph_domain_routing_config import GraphDomainRoutingConfig
from .catalog_relationship_pattern import CatalogRelationshipPattern

__all__ = ["DomainListResponse", "Domain", "DomainCatalog", "DomainCatalogConfig"]


class DomainCatalog(BaseModel):
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


class DomainCatalogConfig(BaseModel):
    """Catalog settings on a domain."""

    enabled: Optional[bool] = None
    """Whether to auto-accumulate signals on transform."""

    refresh_every_n: Optional[int] = None
    """Run LLM clustering after this many buffered entries."""


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
