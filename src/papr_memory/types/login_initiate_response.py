# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["LoginInitiateResponse"]


class LoginInitiateResponse(BaseModel):
    """Response model for OAuth2 login endpoint"""

    message: Optional[str] = None

    redirect_url: Optional[str] = None
