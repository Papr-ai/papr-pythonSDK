# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ParsePointerParam"]


class ParsePointerParam(TypedDict, total=False):
    class_name: Required[Annotated[str, PropertyInfo(alias="className")]]

    object_id: Required[Annotated[str, PropertyInfo(alias="objectId")]]

    _type: Annotated[str, PropertyInfo(alias="__type")]
