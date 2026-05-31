# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ...._models import BaseModel

__all__ = ["CatalogRefreshResponse", "EntityCluster", "RelationshipPattern"]


class EntityCluster(BaseModel):
    """A cluster of semantically-similar entity values."""

    label: str
    """LLM-chosen canonical label for this cluster."""

    count: Optional[int] = None
    """Total occurrences across all transforms."""

    members: Optional[List[str]] = None
    """Raw signal values merged into this cluster."""


class RelationshipPattern(BaseModel):
    """A cluster of semantically-similar relationship types."""

    label: str
    """Canonical label (e.g. 'Causal', 'Preventive')."""

    count: Optional[int] = None
    """Total occurrences."""

    members: Optional[List[str]] = None
    """Raw relationship values in this cluster."""


class CatalogRefreshResponse(BaseModel):
    """Curated summary of what's in a domain's frequency space."""

    domain_distribution: Optional[Dict[str, int]] = None
    """Signal band name -> total doc count."""

    entity_clusters: Optional[List[EntityCluster]] = None

    last_refreshed: Optional[str] = None
    """ISO timestamp of last LLM clustering run."""

    last_updated: Optional[str] = None
    """ISO timestamp of last buffer append."""

    relationship_patterns: Optional[List[RelationshipPattern]] = None

    signal_value_counts: Optional[Dict[str, Dict[str, int]]] = None
    """Per-band raw value counts, e.g. {'domain': {'Health': 500, 'Tech': 200}}."""

    total_documents: Optional[int] = None
    """Total transforms processed."""
