# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["HolographicExtractMetadataResponse", "Data"]


class Data(BaseModel):
    domain: str

    frequency_schema_id: str

    metadata: Dict[str, object]
    """LLM-extracted metadata keyed by frequency field name"""

    phases: List[float]
    """14 phase values for on-device transform"""

    timing_ms: float


class HolographicExtractMetadataResponse(BaseModel):
    """Response for POST /v1/holographic/metadata"""

    data: Data

    status: Optional[str] = None
