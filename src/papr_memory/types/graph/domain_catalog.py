# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel
from .catalog_entity_cluster import CatalogEntityCluster
from .catalog_relationship_pattern import CatalogRelationshipPattern

__all__ = ["DomainCatalog"]


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
