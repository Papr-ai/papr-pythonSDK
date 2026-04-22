# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..instance_config_item import InstanceConfigItem

__all__ = ["InstanceRetrieveResponse"]


class InstanceRetrieveResponse(BaseModel):
    """Standard response envelope for instance config operations."""

    code: Optional[int] = None
    """HTTP status code"""

    data: Optional[InstanceConfigItem] = None
    """Instance configuration — response model for GET endpoints."""

    details: Optional[object] = None
    """Additional context"""

    error: Optional[str] = None
    """Error message if failed"""

    status: Optional[str] = None
    """'success' or 'error'"""
