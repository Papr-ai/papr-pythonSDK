# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["SyncGetTiersParams"]


class SyncGetTiersParams(TypedDict, total=False):
    embed_limit: int
    """Max items to embed per tier to control latency"""

    embed_model: str
    """Embedding model hint: 'sbert' or 'bigbird' or 'Qwen4B'"""

    embedding_format: Literal["int8", "float32"]
    """
    Embedding format: 'int8' (quantized, 4x smaller, default for efficiency),
    'float32' (full precision, recommended for CoreML/ANE fp16 models). Only applies
    to Tier1; Tier0 always uses float32 when embeddings are included.
    """

    external_user_id: Optional[str]
    """Optional external user ID to filter tiers by a specific external user.

    If both user_id and external_user_id are provided, user_id takes precedence.
    """

    include_embeddings: bool
    """Include embeddings in the response.

    Format controlled by embedding_format parameter.
    """

    max_tier0: int
    """Max Tier 0 items (goals/OKRs/use-cases)"""

    max_tier1: int
    """Max Tier 1 items (hot memories)"""

    namespace_id: Optional[str]
    """Optional namespace ID for multi-tenant scoping.

    When provided, tiers are scoped to memories within this namespace.
    """

    organization_id: Optional[str]
    """Optional organization ID for multi-tenant scoping.

    When provided, tiers are scoped to memories within this organization.
    """

    user_id: Optional[str]
    """Optional internal user ID to filter tiers by a specific user.

    If not provided, results are not filtered by user. If both user_id and
    external_user_id are provided, user_id takes precedence.
    """

    workspace_id: Optional[str]
    """Optional workspace id to scope tiers"""
