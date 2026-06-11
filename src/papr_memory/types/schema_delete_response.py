# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SchemaDeleteResponse"]


class SchemaDeleteResponse(BaseModel):
    """Response model for schema deletion."""

    message: str
    """Deletion status message"""
