# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .user_type import UserType

__all__ = ["UserCreateBatchParams", "User"]


class UserCreateBatchParams(TypedDict, total=False):
    users: Required[Iterable[User]]

    x_api_key: Required[Annotated[str, PropertyInfo(alias="X-API-Key")]]


class User(TypedDict, total=False):
    external_id: Required[str]

    email: Optional[str]

    metadata: Optional[Dict[str, object]]

    type: UserType
