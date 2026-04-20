# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OmoExportMemoriesAsJsonParams"]


class OmoExportMemoriesAsJsonParams(TypedDict, total=False):
    memory_ids: Required[str]
    """Comma-separated list of memory IDs"""
