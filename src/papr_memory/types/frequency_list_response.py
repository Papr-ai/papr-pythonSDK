# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel
from .schema_config_response import SchemaConfigResponse
from .frequency_field_response import FrequencyFieldResponse

__all__ = ["FrequencyListResponse", "Schema"]


class Schema(BaseModel):
    """Full frequency schema with fields and config."""

    config: SchemaConfigResponse
    """Operational configuration"""

    domain: str
    """Domain (e.g. code_search, biomedical)"""

    frequencies: List[FrequencyFieldResponse]
    """Frequency band definitions"""

    name: str
    """Schema name"""

    num_frequencies: int
    """Number of frequency bands"""

    schema_id: str
    """Unique schema ID (domain:name:version)"""

    version: str
    """Schema version"""

    description: Optional[str] = None
    """Human-readable description"""


class FrequencyListResponse(BaseModel):
    """Response for listing all frequency schemas."""

    schemas: List[Schema]

    total: int

    shortcuts: Optional[Dict[str, str]] = None
    """Shorthand aliases (e.g. 'cosqa' -> 'code_search:cosqa:2.0.0')"""

    success: Optional[bool] = None
