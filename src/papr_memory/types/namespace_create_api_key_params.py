# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["NamespaceCreateAPIKeyParams"]


class NamespaceCreateAPIKeyParams(TypedDict, total=False):
    name: Required[str]
    """Human-readable name for the API key (shown in admin UIs)."""

    environment: Literal["development", "staging", "production"]
    """Environment label: development, staging, or production."""

    permissions: List[Literal["read", "write", "delete"]]
    """Permissions granted by this key.

    Must be a subset of ['read', 'write', 'delete'].
    """
