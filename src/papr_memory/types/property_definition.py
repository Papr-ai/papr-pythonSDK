# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PropertyDefinition"]


class PropertyDefinition(BaseModel):
    """Property definition for nodes/relationships"""

    type: Literal["string", "integer", "float", "boolean", "array", "datetime", "object"]

    default: Optional[object] = None

    description: Optional[str] = None

    enum_values: Optional[List[str]] = None
    """List of allowed enum values (max 15)"""

    max_length: Optional[int] = None

    max_value: Optional[float] = None

    min_length: Optional[int] = None

    min_value: Optional[float] = None

    pattern: Optional[str] = None

    required: Optional[bool] = None
