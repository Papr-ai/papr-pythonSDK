# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Any, Dict, List, Optional

from pydantic import Field as FieldInfo, ConfigDict

from .._models import BaseModel

__all__ = [
    "SyncTiersResponse",
]


class SyncTiersResponse(BaseModel):
    """Response model for sync tiers endpoint"""

    code: int = FieldInfo(default=200, description="HTTP status code")
    status: str = FieldInfo(default="success", description="'success' or 'error'")
    tier0: List[Dict[str, Any]] = FieldInfo(default_factory=list, description="Tier 0 items (goals/OKRs/use-cases)")
    tier1: List[Dict[str, Any]] = FieldInfo(default_factory=list, description="Tier 1 items (hot memories)")
    transitions: List[Dict[str, Any]] = FieldInfo(default_factory=list, description="Transition items between tiers")
    next_cursor: Optional[str] = FieldInfo(default=None, description="Cursor for pagination")
    has_more: bool = FieldInfo(default=False, description="Whether there are more items available")
    error: Optional[str] = FieldInfo(default=None, description="Error message if failed")
    details: Optional[Any] = FieldInfo(default=None, description="Additional error details or context")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "code": 200,
                "status": "success",
                "tier0": [
                    {
                        "id": "goal_123",
                        "content": "Improve API performance",
                        "type": "goal",
                        "topics": ["performance", "api"],
                        "metadata": {"sourceType": "papr", "class": "goal"},
                    }
                ],
                "tier1": [
                    {
                        "id": "memory_456",
                        "content": "Customer complained about slow API response times",
                        "type": "text",
                        "topics": ["customer", "api", "performance"],
                        "metadata": {"sourceType": "papr"},
                    }
                ],
                "transitions": [],
                "next_cursor": None,
                "has_more": False,
                "error": None,
                "details": None,
            }
        }
    )

    @classmethod
    def success(cls, tier0: List[Dict[str, Any]], tier1: List[Dict[str, Any]], **kwargs):
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
