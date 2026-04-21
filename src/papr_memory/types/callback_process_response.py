# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CallbackProcessResponse"]


class CallbackProcessResponse(BaseModel):
    """Response model for OAuth2 callback endpoint"""

    code: Optional[str] = None
    """Authorization code"""

    message: Optional[str] = None
    """Callback status message"""

    state: Optional[str] = None
    """State parameter for security"""
