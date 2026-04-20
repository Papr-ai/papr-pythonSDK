# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["RelationshipSpec"]


class RelationshipSpec(BaseModel):
    """Specification for a relationship in manual mode.

    Used when mode='manual' to define exact relationships between nodes.
    """

    source: str
    """ID of the source node"""

    target: str
    """ID of the target node"""

    type: str
    """Relationship type (e.g., 'PURCHASED', 'WORKS_AT', 'ASSIGNED_TO')"""

    properties: Optional[Dict[str, object]] = None
    """Optional properties for this relationship"""
