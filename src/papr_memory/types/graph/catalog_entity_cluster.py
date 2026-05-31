# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["CatalogEntityCluster"]


class CatalogEntityCluster(BaseModel):
    """A cluster of semantically-similar entity values."""

    label: str
    """LLM-chosen canonical label for this cluster."""

    count: Optional[int] = None
    """Total occurrences across all transforms."""

    members: Optional[List[str]] = None
    """Raw signal values merged into this cluster."""
