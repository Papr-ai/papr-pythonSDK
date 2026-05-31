# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["DocumentUploadParams"]


class DocumentUploadParams(TypedDict, total=False):
    file: Required[FileTypes]

    enable_holographic: bool
    """DEPRECATED: Use policy.transform_embedding instead.

    If True, applies holographic neural transforms and stores in holographic
    collection.
    """

    external_user_id: Optional[str]
    """Your application's user identifier.

    This is the primary way to identify users. Also accepts legacy 'end_user_id'.
    """

    frequency_schema_id: Optional[str]
    """DEPRECATED: Use policy.transform_embedding.domain_id instead.

    Frequency schema for holographic embedding (e.g. 'cosqa', 'scifact'). Required
    when enable_holographic=True. Call GET /v1/frequencies to see available schemas.
    """

    graph_override: Optional[str]

    hierarchical_enabled: bool

    memory_policy: Optional[str]
    """DEPRECATED: Use 'policy' instead.

    JSON-encoded memory policy. Includes mode ('auto'/'manual'), schema_id,
    node_constraints (applied in auto mode when present), and OMO fields (consent,
    risk, acl).
    """

    metadata: Optional[str]

    namespace_id: Optional[str]

    policy: Optional[str]
    """JSON-encoded unified processing policy (transform_embedding, graph incl.

    link_to, consent, risk, acl). Applies to all chunks from this document.
    """

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
