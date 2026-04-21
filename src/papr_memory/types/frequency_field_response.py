# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["FrequencyFieldResponse"]


class FrequencyFieldResponse(BaseModel):
    """Single frequency band definition."""

    frequency_hz: float
    """Frequency in Hz (brain-inspired band)"""

    name: str
    """Field name extracted at this frequency"""

    type: str
    """Field type: ENUM, FREE_TEXT, NUMERIC, DATE, MULTI_VALUE"""

    description: Optional[str] = None
    """Human-readable field description"""

    weight: Optional[float] = None
    """Default weight for this frequency band"""
