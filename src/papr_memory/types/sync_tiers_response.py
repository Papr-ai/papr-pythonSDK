# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Any, Dict, List, Optional
from datetime import datetime

from pydantic import Field, ConfigDict

from .._models import BaseModel

__all__ = ["SyncTiersResponse", "Memory"]


class Memory(BaseModel):
    """Individual memory item in tier response - matches server Memory model"""

    # Core fields
    id: str = Field(description="Memory ID")
    content: str = Field(description="Memory content text")
    title: Optional[str] = Field(default=None, description="Memory title")
    type: str = Field(description="Memory type (e.g., 'TextMemoryItem', 'DocumentMemoryItem', 'goal', 'okr')")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="Additional metadata")
    external_user_id: Optional[str] = Field(default=None, description="External user ID")
    customMetadata: Optional[Dict[str, Any]] = Field(default=None, description="Custom metadata")
    source_type: str = Field(default="papr", description="Source type")
    context: Optional[List[Dict[str, Any]]] = Field(default_factory=list, description="Context items")
    location: Optional[str] = Field(default=None, description="Location")
    tags: List[str] = Field(default_factory=list, description="Emoji tags")
    hierarchical_structures: str = Field(default="", description="Hierarchical structures")
    source_url: str = Field(default="", description="Source URL")
    conversation_id: str = Field(default="", description="Conversation ID")
    topics: List[str] = Field(default_factory=list, description="List of topics/tags")
    steps: List[str] = Field(default_factory=list, description="Steps")
    current_step: Optional[str] = Field(default=None, description="Current step")
    
    # Role and category
    role: Optional[str] = Field(default=None, description="Role that generated this memory (user or assistant)")
    category: Optional[str] = Field(default=None, description="Memory category based on role")
    
    # Timestamps
    created_at: Optional[datetime] = Field(default=None, description="Creation timestamp")
    updated_at: Optional[datetime] = Field(default=None, description="Last update timestamp")
    
    # Access control and ownership
    acl: Dict[str, Dict[str, bool]] = Field(default_factory=dict, description="Access control list")
    user_id: str = Field(description="ID of the user who owns this memory")
    workspace_id: Optional[str] = Field(default=None, description="ID of the workspace this memory belongs to")
    
    # Multi-tenant fields
    organization_id: Optional[str] = Field(default=None, description="Organization ID that owns this memory")
    namespace_id: Optional[str] = Field(default=None, description="Namespace ID this memory belongs to")
    
    # Source context
    source_document_id: Optional[str] = Field(default=None, description="ID of the document/page this memory is from")
    source_message_id: Optional[str] = Field(default=None, description="ID of the chat message this memory is from")
    
    # Document specific fields
    page_number: Optional[int] = Field(default=None, description="Page number for document memories")
    total_pages: Optional[int] = Field(default=None, description="Total pages in document")
    file_url: Optional[str] = Field(default=None, description="File URL")
    filename: Optional[str] = Field(default=None, description="Filename")
    page: Optional[str] = Field(default=None, description="Page content")
    
    # ACL fields for fine-grained access control
    external_user_read_access: Optional[List[str]] = Field(default_factory=list, description="External users with read access")
    external_user_write_access: Optional[List[str]] = Field(default_factory=list, description="External users with write access")
    user_read_access: Optional[List[str]] = Field(default_factory=list, description="Users with read access")
    user_write_access: Optional[List[str]] = Field(default_factory=list, description="Users with write access")
    workspace_read_access: Optional[List[str]] = Field(default_factory=list, description="Workspaces with read access")
    workspace_write_access: Optional[List[str]] = Field(default_factory=list, description="Workspaces with write access")
    role_read_access: Optional[List[str]] = Field(default_factory=list, description="Roles with read access")
    role_write_access: Optional[List[str]] = Field(default_factory=list, description="Roles with write access")
    namespace_read_access: Optional[List[str]] = Field(default_factory=list, description="Namespaces with read access")
    namespace_write_access: Optional[List[str]] = Field(default_factory=list, description="Namespaces with write access")
    organization_read_access: Optional[List[str]] = Field(default_factory=list, description="Organizations with read access")
    organization_write_access: Optional[List[str]] = Field(default_factory=list, description="Organizations with write access")
    
    # Embedding fields (optional, populated when include_embeddings=True in sync_tiers)
    embedding: Optional[List[float]] = Field(
        default=None,
        description="Full precision (float32) embedding vector from Qdrant. Typically 2560 dimensions for Qwen4B. Used for CoreML/ANE fp16 models."
    )
    embedding_int8: Optional[List[int]] = Field(
        default=None,
        description="Quantized INT8 embedding vector (values -128 to 127). 4x smaller than float32. Default format for efficiency."
    )
    
    # Relevance score from server ranking (optional)
    relevance_score: Optional[float] = Field(
        default=None,
        description="Relevance score from server-side ranking/scoring. Higher is more relevant. Can be combined with cosine similarity for hybrid ranking."
    )
    
    model_config = ConfigDict(
        extra='allow',  # Allow additional fields from server
        populate_by_name=True,
        str_strip_whitespace=True,
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
