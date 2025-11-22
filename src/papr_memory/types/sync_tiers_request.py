# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from enum import Enum

from pydantic import Field

from .._models import BaseModel

__all__ = ["SyncTiersRequest", "EmbeddingFormat"]


class EmbeddingFormat(str, Enum):
    """Embedding format for sync_tiers response"""
    INT8 = "int8"
    FLOAT32 = "float32"


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
        description="Include embeddings in the response. Format controlled by embedding_format parameter.",
    )

    embedding_format: EmbeddingFormat = Field(
        default=EmbeddingFormat.INT8,
        description="Embedding format: 'int8' (quantized, 4x smaller, default for efficiency), 'float32' (full precision, recommended for CoreML/ANE fp16 models). Only applies to Tier1; Tier0 always uses float32 when embeddings are included.",
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

