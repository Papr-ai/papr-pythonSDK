# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Any, Dict, List, Optional

from pydantic import Field

from .._models import BaseModel

__all__ = ["SyncTiersResponse", "Memory"]


class Memory(BaseModel):
    """Individual memory item in tier response"""

    id: str = Field(description="Memory ID")
    content: str = Field(description="Memory content text")
    type: str = Field(description="Memory type (e.g., 'goal', 'text', 'okr')")
    topics: Optional[List[str]] = Field(default=None, description="List of topics/tags")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="Additional metadata")
    embedding: Optional[List[float]] = Field(
        default=None, description="Full precision embedding (if requested)"
    )
    embedding_int8: Optional[List[int]] = Field(
        default=None, description="INT8 quantized embedding (if requested)"
    )


class SyncTiersResponse(BaseModel):
    """Response model for sync tiers endpoint"""

    code: int = Field(default=200, description="HTTP status code")
    status: str = Field(default="success", description="'success' or 'error'")
    tier0: List[Memory] = Field(default_factory=list, description="Tier 0 items (goals/OKRs/use-cases)")
    tier1: List[Memory] = Field(default_factory=list, description="Tier 1 items (hot memories)")
    transitions: List[Dict[str, Any]] = Field(
        default_factory=list, description="Transition items between tiers"
    )
    next_cursor: Optional[str] = Field(default=None, description="Cursor for pagination")
    has_more: bool = Field(default=False, description="Whether there are more items available")
    error: Optional[str] = Field(default=None, description="Error message if failed")
    details: Optional[Any] = Field(default=None, description="Additional error details or context")

    @classmethod
    def success(cls, tier0: List[Memory], tier1: List[Memory], **kwargs):
        """Create a success response"""
        return cls(
            code=200,
            status="success",
            tier0=tier0,
            tier1=tier1,
            transitions=kwargs.get("transitions", []),
            next_cursor=kwargs.get("next_cursor"),
            has_more=kwargs.get("has_more", False),
            error=None,
            details=None,
        )

    @classmethod
    def failure(cls, error: str, code: int = 500, details: Any = None):
        """Create a failure response"""
        return cls(
            code=code,
            status="error",
            tier0=[],
            tier1=[],
            transitions=[],
            next_cursor=None,
            has_more=False,
            error=error,
            details=details,
        )
