# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["NodeSpec"]


class NodeSpec(BaseModel):
    """Specification for a node in manual mode.

    Used when mode='manual' to define exact nodes to create.
    """

    id: str
    """Unique identifier for this node"""

    type: str
    """Node type/label (e.g., 'Transaction', 'Product', 'Person')"""

    properties: Optional[Dict[str, object]] = None
    """Properties for this node"""
