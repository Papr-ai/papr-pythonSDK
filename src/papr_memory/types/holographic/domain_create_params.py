# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["DomainCreateParams", "Field"]


class DomainCreateParams(TypedDict, total=False):
    fields: Required[Iterable[Field]]
    """Frequency field definitions (1-14 fields, one per frequency band)"""

    name: Required[str]
    """Schema name in format 'company:domain:version' (e.g.

    'acme:support_tickets:1.0.0')
    """

    description: Optional[str]
    """Human-readable description"""


class Field(TypedDict, total=False):
    """Single field definition for a custom frequency schema."""

    frequency: Required[float]
    """
    Hz value (must be one of the 14 standard frequencies: 0.1, 0.5, 2.0, 4.0, 6.0,
    10.0, 12.0, 18.0, 19.0, 24.0, 30.0, 40.0, 50.0, 70.0)
    """

    name: Required[str]
    """Field name (e.g. 'ticket_priority', 'component')"""

    type: Required[Literal["enum", "free_text", "numeric", "boolean", "date", "sequence", "multi_value_text"]]
    """Field type"""

    description: Optional[str]
    """Field description"""

    values: Optional[SequenceNotStr[str]]
    """Allowed values for enum type"""

    weight: float
    """Importance weight"""
