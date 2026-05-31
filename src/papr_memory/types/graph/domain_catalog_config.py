# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DomainCatalogConfig"]


class DomainCatalogConfig(BaseModel):
    """Catalog settings on a domain."""

    enabled: Optional[bool] = None
    """Whether to auto-accumulate signals on transform."""

    refresh_every_n: Optional[int] = None
    """Run LLM clustering after this many buffered entries."""
