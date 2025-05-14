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
