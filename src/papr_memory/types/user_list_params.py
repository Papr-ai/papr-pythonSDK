# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UserListParams"]


class UserListParams(TypedDict, total=False):
    x_api_key: Required[Annotated[str, PropertyInfo(alias="X-API-Key")]]

    email: Optional[str]

    external_id: Optional[str]

    page: int

    page_size: int
