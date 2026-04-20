# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .user_graph_schema_output import UserGraphSchemaOutput

__all__ = ["SchemaRetrieveResponse"]


class SchemaRetrieveResponse(BaseModel):
    """Response model for schema operations"""

    success: bool

    code: Optional[int] = None

    data: Optional[UserGraphSchemaOutput] = None
    """Complete user-defined graph schema"""

    error: Optional[str] = None
