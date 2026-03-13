# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["PropertyValue"]


class PropertyValue(TypedDict, total=False):
    """Configuration for a property value in NodeConstraint.set.

    Supports two modes:
    1. Exact value: Just pass the value directly (e.g., "done", 123, True)
    2. Auto-extract: {"mode": "auto"} - LLM extracts from memory content

    For text properties, use text_mode to control how updates are applied.
    Use prompt to provide per-field extraction guidance to the LLM.
    """

    mode: Literal["auto"]
    """'auto': LLM extracts value from memory content."""

    prompt: Optional[str]
    """Custom extraction prompt for this field.

    Guides the LLM on what to extract and how to format it. Example: 'Summarize in
    1-2 sentences with attack vector and affected systems.'
    """

    text_mode: Literal["replace", "append", "merge"]
    """
    For text properties: 'replace' (overwrite), 'append' (add to), 'merge' (LLM
    combines existing + new).
    """
