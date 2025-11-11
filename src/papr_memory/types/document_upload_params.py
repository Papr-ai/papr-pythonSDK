# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["DocumentUploadParams"]


class DocumentUploadParams(TypedDict, total=False):
    file: Required[FileTypes]

    end_user_id: Optional[str]

    graph_override: Optional[str]

    hierarchical_enabled: bool

    metadata: Optional[str]

    namespace: Optional[str]

    preferred_provider: Optional[Literal["gemini", "tensorlake", "reducto", "auto"]]
    """Preferred provider for document processing."""

    property_overrides: Optional[str]

    schema_id: Optional[str]

    simple_schema_mode: bool

    user_id: Optional[str]

    webhook_secret: Optional[str]

    webhook_url: Optional[str]
