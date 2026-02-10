# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["DocumentUploadParams"]


class DocumentUploadParams(TypedDict, total=False):
    file: Required[FileTypes]

    external_user_id: Optional[str]
    """Your application's user identifier.

    This is the primary way to identify users. Also accepts legacy 'end_user_id'.
    """

    graph_override: Optional[str]

    hierarchical_enabled: bool

    memory_policy: Optional[str]
    """JSON-encoded memory policy.

    Includes mode ('auto'/'manual'), schema_id, node_constraints (applied in auto
    mode when present), and OMO fields (consent, risk, acl). This is the recommended
    way to configure memory processing.
    """

    metadata: Optional[str]

    namespace_id: Optional[str]

    preferred_provider: Optional[Literal["gemini", "tensorlake", "reducto", "auto"]]
    """Preferred provider for document processing."""

    property_overrides: Optional[str]

    schema_id: Optional[str]

    user_id: Optional[str]
    """DEPRECATED: Internal Papr Parse user ID.

    Most developers should use external_user_id.
    """

    webhook_secret: Optional[str]

    webhook_url: Optional[str]
