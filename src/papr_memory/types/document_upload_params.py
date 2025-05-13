# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentUploadParams"]


class DocumentUploadParams(TypedDict, total=False):
    post_object_id: Annotated[Optional[str], PropertyInfo(alias="post_objectId")]
    """Optional Post objectId for updating status"""

    skip_background_processing: bool
    """If True, skips adding background tasks for processing"""
