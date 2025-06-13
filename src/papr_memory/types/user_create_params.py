# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .user_type import UserType

__all__ = ["UserCreateParams"]


class UserCreateParams(TypedDict, total=False):
    external_id: Required[str]

    email: Optional[str]

    metadata: Optional[Dict[str, object]]

    type: UserType
