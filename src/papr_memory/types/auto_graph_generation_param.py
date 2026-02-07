# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AutoGraphGenerationParam", "PropertyOverride"]


class PropertyOverride(TypedDict, total=False):
    """Property override rule with optional match conditions"""

    node_label: Required[Annotated[str, PropertyInfo(alias="nodeLabel")]]
    """Node type to apply overrides to (e.g., 'User', 'SecurityBehavior')"""

    set: Required[Dict[str, object]]
    """Properties to set/override on matching nodes"""

    match: Optional[Dict[str, object]]
    """Optional conditions that must be met for override to apply.

    If not provided, applies to all nodes of this type
    """


class AutoGraphGenerationParam(TypedDict, total=False):
    """AI-powered graph generation with optional guidance"""

    property_overrides: Optional[Iterable[PropertyOverride]]
    """Override specific property values in AI-generated nodes with match conditions"""

    schema_id: Optional[str]
    """Force AI to use this specific schema instead of auto-selecting"""
