# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .user_graph_schema_output import UserGraphSchemaOutput

__all__ = ["SchemaListResponse"]


class SchemaListResponse(BaseModel):
    success: bool

    code: Optional[int] = None

    data: Optional[List[UserGraphSchemaOutput]] = None

    error: Optional[str] = None

    total: Optional[int] = None
