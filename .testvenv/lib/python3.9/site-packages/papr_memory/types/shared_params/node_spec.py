# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["NodeSpec"]


class NodeSpec(TypedDict, total=False):
    """Specification for a node in manual mode.

    Used when mode='manual' to define exact nodes to create.
    """

    id: Required[str]
    """Unique identifier for this node"""

    type: Required[str]
    """Node type/label (e.g., 'Transaction', 'Product', 'Person')"""

    properties: Dict[str, object]
    """Properties for this node"""
