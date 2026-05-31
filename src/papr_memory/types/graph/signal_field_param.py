# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["SignalFieldParam"]


class SignalFieldParam(TypedDict, total=False):
    description: Required[str]
    """Human prompt used by extractor."""

    name: Required[str]
    """Snake_case signal identifier."""

    allowed_values: Optional[SequenceNotStr[str]]
    """For type='enum': allowed vocabulary."""

    frequency_hz: Optional[float]
    """Hz band mapping (0.1 … 70.0). Auto-assigned if omitted."""

    required: bool
    """Warn when missing at extract time."""

    type: Literal["enum", "text", "numeric", "date", "boolean", "multi_value_text"]
    """Extraction / phase type for this signal."""

    weight: float
    """Relative weight in the fusion."""
