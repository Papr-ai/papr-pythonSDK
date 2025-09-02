# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["LogoutLogoutResponse"]


class LogoutLogoutResponse(BaseModel):
    logout_url: str
    """URL to complete logout process"""

    message: Optional[str] = None
    """Logout status message"""
