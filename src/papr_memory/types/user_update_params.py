# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .user_type import UserType

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    email: Optional[str]

    external_id: Optional[str]

    metadata: Optional[object]

    type: Optional[UserType]
