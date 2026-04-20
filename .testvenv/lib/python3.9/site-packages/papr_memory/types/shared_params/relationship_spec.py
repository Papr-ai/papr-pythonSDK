# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["RelationshipSpec"]


class RelationshipSpec(TypedDict, total=False):
    """Specification for a relationship in manual mode.

    Used when mode='manual' to define exact relationships between nodes.
    """

    source: Required[str]
    """ID of the source node"""

    target: Required[str]
    """ID of the target node"""

    type: Required[str]
    """Relationship type (e.g., 'PURCHASED', 'WORKS_AT', 'ASSIGNED_TO')"""

    properties: Optional[Dict[str, object]]
    """Optional properties for this relationship"""
