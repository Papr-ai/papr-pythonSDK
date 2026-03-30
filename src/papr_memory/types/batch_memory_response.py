# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .batch_memory_error import BatchMemoryError
from .add_memory_response import AddMemoryResponse

__all__ = ["BatchMemoryResponse"]


class BatchMemoryResponse(BaseModel):
    batch_id: Optional[str] = None
    """
    Batch tracking ID for status polling via GET /v1/memory/batch/status/{batch_id}
    and WebSocket updates
    """

    code: Optional[int] = None
    """HTTP status code for the batch operation"""

    details: Optional[object] = None
    """Additional error details or context"""

    error: Optional[str] = None
    """Batch-level error message, if any"""

    errors: Optional[List[BatchMemoryError]] = None
    """List of errors for failed items"""

    message: Optional[str] = None
    """Human-readable status message"""

    status: Optional[str] = None
    """'success', 'partial', or 'error'"""

    successful: Optional[List[AddMemoryResponse]] = None
    """List of successful add responses"""

    total_content_size: Optional[int] = None

    total_failed: Optional[int] = None

    total_processed: Optional[int] = None

    total_storage_size: Optional[int] = None

    total_successful: Optional[int] = None
