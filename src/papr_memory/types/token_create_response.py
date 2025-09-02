# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["TokenCreateResponse"]


class TokenCreateResponse(BaseModel):
    access_token: str
    """OAuth2 access token"""

    expires_in: int
    """Token expiration time in seconds"""

    scope: str
    """OAuth2 scopes granted"""

    message: Optional[str] = None
    """Additional message or status"""

    refresh_token: Optional[str] = None
    """Refresh token for getting new access tokens"""

    token_type: Optional[str] = None
    """Token type"""

    user_id: Optional[str] = None
    """User ID from Auth0"""
