# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SignalField"]


class SignalField(BaseModel):
    description: str
    """Human prompt used by extractor."""

    name: str
    """Snake_case signal identifier."""

    allowed_values: Optional[List[str]] = None
    """For type='enum': allowed vocabulary."""

    frequency_hz: Optional[float] = None
    """Hz band mapping (0.1 … 70.0). Auto-assigned if omitted."""

    required: Optional[bool] = None
    """Warn when missing at extract time."""

    type: Optional[Literal["enum", "text", "numeric", "date", "boolean", "multi_value_text"]] = None
    """Extraction / phase type for this signal."""

    weight: Optional[float] = None
    """Relative weight in the fusion."""
