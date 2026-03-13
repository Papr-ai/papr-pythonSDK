# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DomainCreateResponse"]


class DomainCreateResponse(BaseModel):
    """Response for POST /v1/holographic/domains"""

    domain: str

    num_frequencies: int

    schema_id: str
    """Generated schema ID"""

    status: Optional[str] = None
