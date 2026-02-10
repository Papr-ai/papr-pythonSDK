# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["PropertyDefinitionParam"]


class PropertyDefinitionParam(TypedDict, total=False):
    """Property definition for nodes/relationships"""

    type: Required[Literal["string", "integer", "float", "boolean", "array", "datetime", "object"]]

    default: object

    description: Optional[str]

    enum_values: Optional[SequenceNotStr[str]]
    """List of allowed enum values (max 15)"""

    max_length: Optional[int]

    max_value: Optional[float]

    min_length: Optional[int]

    min_value: Optional[float]

    pattern: Optional[str]

    required: bool
