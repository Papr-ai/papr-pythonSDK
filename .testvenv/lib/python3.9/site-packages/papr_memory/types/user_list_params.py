# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["UserListParams"]


class UserListParams(TypedDict, total=False):
    email: Optional[str]

    external_id: Optional[str]

    page: int

    page_size: int
