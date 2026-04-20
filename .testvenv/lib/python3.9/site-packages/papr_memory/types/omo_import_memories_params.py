# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["OmoImportMemoriesParams"]


class OmoImportMemoriesParams(TypedDict, total=False):
    memories: Required[Iterable[Dict[str, object]]]
    """List of memories in OMO v1 format"""

    skip_duplicates: bool
    """Skip memories with IDs that already exist"""
