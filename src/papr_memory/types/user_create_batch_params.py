# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

from .user_type import UserType

__all__ = ["UserCreateBatchParams", "User"]


class UserCreateBatchParams(TypedDict, total=False):
    users: Required[Iterable[User]]


class User(TypedDict, total=False):
    external_id: Required[str]

    email: Optional[str]

    metadata: Optional[Dict[str, object]]

    type: UserType
