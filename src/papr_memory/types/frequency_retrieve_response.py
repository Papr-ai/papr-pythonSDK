# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .schema_config_response import SchemaConfigResponse
from .frequency_field_response import FrequencyFieldResponse

__all__ = ["FrequencyRetrieveResponse"]


class FrequencyRetrieveResponse(BaseModel):
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
