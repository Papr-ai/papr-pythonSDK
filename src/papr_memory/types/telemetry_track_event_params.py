# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["TelemetryTrackEventParams", "Event"]


class TelemetryTrackEventParams(TypedDict, total=False):
    events: Required[Iterable[Event]]
    """List of telemetry events to track"""

    anonymous_id: Optional[str]
    """Anonymous session ID"""


class Event(TypedDict, total=False):
    """Single telemetry event"""

    event_name: Required[str]
    """Event name (e.g., 'memory_created', 'search_performed')"""

    properties: Optional[Dict[str, object]]
    """Event properties (will be anonymized)"""

    timestamp: Optional[int]
    """Event timestamp (Unix epoch in milliseconds)"""

    user_id: Optional[str]
    """Anonymous user ID (hashed)"""
