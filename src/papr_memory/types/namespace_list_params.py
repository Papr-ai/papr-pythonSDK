# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["NamespaceListParams"]


class NamespaceListParams(TypedDict, total=False):
    limit: int
    """Max items to return"""

    skip: int
    """Number of items to skip"""
