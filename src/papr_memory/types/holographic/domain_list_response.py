# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["DomainListResponse", "Domain"]


class Domain(BaseModel):
    """Summary of an available domain."""

    domain: str

    name: str

    num_frequencies: int

    schema_id: str

    description: Optional[str] = None

    is_custom: Optional[bool] = None
    """True if created by developer via POST"""


class DomainListResponse(BaseModel):
    """Response for GET /v1/holographic/domains"""

    domains: List[Domain]

    total: int

    shortcuts: Optional[Dict[str, str]] = None
    """Shorthand aliases (e.g. 'cosqa' -> 'code_search:cosqa:2.0.0')"""

    status: Optional[str] = None
