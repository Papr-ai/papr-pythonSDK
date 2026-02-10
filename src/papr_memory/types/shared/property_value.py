# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PropertyValue"]


class PropertyValue(BaseModel):
    """Configuration for a property value in NodeConstraint.set.

    Supports two modes:
    1. Exact value: Just pass the value directly (e.g., "done", 123, True)
    2. Auto-extract: {"mode": "auto"} - LLM extracts from memory content

    For text properties, use text_mode to control how updates are applied.
    """

    mode: Optional[Literal["auto"]] = None
    """'auto': LLM extracts value from memory content."""

    text_mode: Optional[Literal["replace", "append", "merge"]] = None
    """
    For text properties: 'replace' (overwrite), 'append' (add to), 'merge' (LLM
    combines existing + new).
    """
