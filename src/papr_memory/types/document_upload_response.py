# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .add_memory_item import AddMemoryItem

__all__ = ["DocumentUploadResponse", "DocumentStatus"]


class DocumentStatus(BaseModel):
    progress: float
    """0.0 to 1.0 for percentage"""

    current_filename: Optional[str] = None

    current_page: Optional[int] = None

    error: Optional[str] = None
    """Error message if failed"""

    status_type: Optional[Literal["processing", "completed", "failed", "not_found", "queued", "cancelled"]] = None
    """Processing status type"""

    total_pages: Optional[int] = None

    upload_id: Optional[str] = None


class DocumentUploadResponse(BaseModel):
    document_status: DocumentStatus
    """Status and progress of the document upload"""

    code: Optional[int] = None
    """HTTP status code"""

    details: Optional[object] = None
    """Additional error details or context"""

    error: Optional[str] = None
    """Error message if failed"""

    memories: Optional[List[AddMemoryItem]] = None
    """For backward compatibility"""

    memory_items: Optional[List[AddMemoryItem]] = None
    """List of memory items created from the document"""

    message: Optional[str] = None
    """Human-readable status message"""

    status: Optional[str] = None
    """'success', 'processing', 'error', etc."""
