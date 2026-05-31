# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["DomainDeleteResponse"]


class DomainDeleteResponse(BaseModel):
    deleted: bool

    domain_id: str
