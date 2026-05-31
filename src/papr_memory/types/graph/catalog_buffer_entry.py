# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from ..._models import BaseModel

__all__ = ["CatalogBufferEntry"]


class CatalogBufferEntry(BaseModel):
    """Raw signal snapshot from a single transform call."""

    signals: Dict[str, str]
    """Band name -> extracted value."""

    timestamp: str
    """ISO timestamp of the transform call."""
