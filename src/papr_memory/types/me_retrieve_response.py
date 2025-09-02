# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MeRetrieveResponse"]


class MeRetrieveResponse(BaseModel):
    user_id: str
    """Internal user ID"""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """User display name"""

    email: Optional[str] = None
    """User email address"""

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)
    """User profile image URL"""

    message: Optional[str] = None
    """Authentication status message"""

    session_token: Optional[str] = FieldInfo(alias="sessionToken", default=None)
    """Session token for API access"""
