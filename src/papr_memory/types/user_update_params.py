# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .user_type import UserType

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    x_api_key: Required[Annotated[str, PropertyInfo(alias="X-API-Key")]]

    email: Optional[str]

    external_id: Optional[str]

    metadata: Optional[Dict[str, object]]

    type: Optional[UserType]
