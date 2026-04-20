# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["OmoExportMemoriesParams"]


class OmoExportMemoriesParams(TypedDict, total=False):
    memory_ids: Required[SequenceNotStr[str]]
    """List of memory IDs to export"""
