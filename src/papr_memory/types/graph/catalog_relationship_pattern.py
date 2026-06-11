# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["CatalogRelationshipPattern"]


class CatalogRelationshipPattern(BaseModel):
    """A cluster of semantically-similar relationship types."""

    label: str
    """Canonical label (e.g. 'Causal', 'Preventive')."""

    count: Optional[int] = None
    """Total occurrences."""

    members: Optional[List[str]] = None
    """Raw relationship values in this cluster."""
