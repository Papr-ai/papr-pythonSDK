# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["LoginInitiateResponse"]


class LoginInitiateResponse(BaseModel):
    message: Optional[str] = None

    redirect_url: Optional[str] = None
