# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["TelemetryTrackEventResponse"]


class TelemetryTrackEventResponse(BaseModel):
    """Response from telemetry endpoint"""

    events_processed: int
    """Number of events successfully processed"""

    events_received: int
    """Number of events received"""

    success: bool
    """Whether the events were successfully processed"""

    message: Optional[str] = None
    """Optional message"""
