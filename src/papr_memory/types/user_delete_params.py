# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UserDeleteParams"]


class UserDeleteParams(TypedDict, total=False):
    x_api_key: Required[Annotated[str, PropertyInfo(alias="X-API-Key")]]

    is_external: bool
    """Is this an external user ID?"""
