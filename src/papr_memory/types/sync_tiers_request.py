# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field

from .._models import BaseModel

__all__ = ["SyncTiersRequest"]


class SyncTiersRequest(BaseModel):
    """Request model for sync tiers endpoint"""

    max_tier0: int = Field(
        default=300,
        ge=0,
        le=2000,
        description="Max Tier 0 items (goals/OKRs/use-cases)",
    )

    max_tier1: int = Field(
        default=1000,
        ge=0,
        le=5000,
        description="Max Tier 1 items (hot memories)",
    )

    workspace_id: Optional[str] = Field(
        default=None,
        description="Optional workspace id to scope tiers",
    )

    user_id: Optional[str] = Field(
        default=None,
        description="Optional internal user ID to filter tiers by a specific user. If not provided, uses authenticated user.",
    )

    external_user_id: Optional[str] = Field(
        default=None,
        description="Optional external user ID to filter tiers by a specific external user. If both user_id and external_user_id are provided, user_id takes precedence.",
    )

    organization_id: Optional[str] = Field(
        default=None,
        description="Optional organization ID for multi-tenant scoping. When provided, tiers are scoped to memories within this organization.",
    )

    namespace_id: Optional[str] = Field(
        default=None,
        description="Optional namespace ID for multi-tenant scoping. When provided, tiers are scoped to memories within this namespace.",
    )

    include_embeddings: bool = Field(
        default=False,
        description="Include float32 embeddings for Tier 0 and INT8 for Tier 1",
    )

    embed_model: str = Field(
        default="Qwen4B",
        description="Embedding model hint: 'sbert' or 'bigbird' or 'Qwen4B'",
    )

    embed_limit: int = Field(
        default=200,
        ge=0,
        le=1000,
        description="Max items to embed per tier to control latency",
    )

