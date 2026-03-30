# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BatchMemoryError"]


class BatchMemoryError(BaseModel):
    error: str

    index: int

    code: Optional[int] = None

    details: Optional[object] = None

    status: Optional[str] = None
