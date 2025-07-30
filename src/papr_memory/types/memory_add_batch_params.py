# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .add_memory_param import AddMemoryParam

__all__ = ["MemoryAddBatchParams"]


class MemoryAddBatchParams(TypedDict, total=False):
    memories: Required[Iterable[AddMemoryParam]]
    """List of memory items to add in batch"""

    skip_background_processing: bool
    """If True, skips adding background tasks for processing"""

    batch_size: Optional[int]
    """Number of items to process in parallel"""

    external_user_id: Optional[str]
    """External user ID for all memories in the batch.

    If provided and user_id is not, will be resolved to internal user ID.
    """

    user_id: Optional[str]
    """Internal user ID for all memories in the batch.

    If not provided, developer's user ID will be used.
    """

    webhook_secret: Optional[str]
    """Optional secret key for webhook authentication.

    If provided, will be included in the webhook request headers as
    'X-Webhook-Secret'.
    """

    webhook_url: Optional[str]
    """Optional webhook URL to notify when batch processing is complete.

    The webhook will receive a POST request with batch completion details.
    """
