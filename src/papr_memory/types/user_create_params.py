# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .user_type import UserType

__all__ = ["UserCreateParams"]


class UserCreateParams(TypedDict, total=False):
    external_id: Required[str]

    x_api_key: Required[Annotated[str, PropertyInfo(alias="X-API-Key")]]

    email: Optional[str]

    metadata: Optional[object]

    type: UserType
