# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DocumentGetStatusResponse", "Timeline", "TimelineStep"]


class TimelineStep(BaseModel):
    id: str
    """Stable step identifier for UI rendering"""

    description: str
    """Customer-facing step description"""

    label: str
    """Customer-facing step title"""

    status: Literal["pending", "in_progress", "completed", "failed", "skipped"]
    """Current state of this step"""

    completed_at: Optional[datetime] = None
    """When this step completed"""

    duration_ms: Optional[int] = None
    """Step duration in milliseconds"""

    error: Optional[str] = None
    """Customer-safe error message for failed steps"""

    page_id: Optional[str] = None
    """User-facing document Post ID, when available"""

    progress: Optional[float] = None
    """Overall pipeline progress when this step was last updated (0.0-1.0)"""

    started_at: Optional[datetime] = None
    """When this step started"""

    total_pages: Optional[int] = None
    """Total pages processed, when known"""


class Timeline(BaseModel):
    """
    Optional step-by-step detail included when GET /document/status/{id}?timeline=true.
    """

    steps: Optional[List[TimelineStep]] = None
    """Ordered processing steps with per-step status and timing"""

    total_elapsed_ms: Optional[int] = None
    """Total elapsed processing time in milliseconds"""

    updated_at: Optional[datetime] = None
    """Timestamp of the latest timeline update"""


class DocumentGetStatusResponse(BaseModel):
    """GET /v1/document/status/{upload_id} response.

    Pass ?timeline=true to include timeline.
    """

    status: str
    """Current processing status"""

    upload_id: str
    """Document upload identifier"""

    current_page: Optional[int] = None
    """Current page being processed"""

    error: Optional[str] = None
    """Customer-safe error message when processing failed"""

    message: Optional[str] = None
    """Additional status message"""

    page_id: Optional[str] = None
    """User-facing document Post ID, when available"""

    progress: Optional[float] = None
    """Overall progress from 0.0 to 1.0"""

    timeline: Optional[Timeline] = None
    """
    Optional step-by-step detail included when GET
    /document/status/{id}?timeline=true.
    """

    timestamp: Optional[datetime] = None
    """Timestamp of the latest status update"""

    total_pages: Optional[int] = None
    """Total pages in the document"""

    workflow_type: Optional[str] = None
    """Processing backend type"""
