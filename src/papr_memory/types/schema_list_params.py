# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["SchemaListParams"]


class SchemaListParams(TypedDict, total=False):
    status_filter: Optional[str]
    """Filter by status (draft, active, deprecated, archived)"""

    workspace_id: Optional[str]
    """Filter by workspace ID"""
