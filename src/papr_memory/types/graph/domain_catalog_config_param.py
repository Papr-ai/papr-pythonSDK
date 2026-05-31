# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DomainCatalogConfigParam"]


class DomainCatalogConfigParam(TypedDict, total=False):
    """Catalog settings on a domain."""

    enabled: bool
    """Whether to auto-accumulate signals on transform."""

    refresh_every_n: int
    """Run LLM clustering after this many buffered entries."""
