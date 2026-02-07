# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .context_item import ContextItem

__all__ = ["SearchResponse", "Data", "DataMemory", "DataNode"]


class DataMemory(BaseModel):
    """A memory item in the knowledge base"""

    id: str

    acl: Dict[str, Dict[str, bool]]

    content: str

    type: str

    user_id: str

    category: Optional[str] = None
    """Memory category based on role"""

    context: Optional[List[ContextItem]] = None

    conversation_id: Optional[str] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    current_step: Optional[str] = None

    custom_metadata: Optional[Dict[str, object]] = FieldInfo(alias="customMetadata", default=None)

    embedding: Optional[List[float]] = None
    """Full precision (float32) embedding vector from Qdrant.

    Typically 2560 dimensions for Qwen4B. Used for CoreML/ANE fp16 models.
    """

    embedding_int8: Optional[List[int]] = None
    """Quantized INT8 embedding vector (values -128 to 127).

    4x smaller than float32. Default format for efficiency.
    """

    external_user_id: Optional[str] = None

    external_user_read_access: Optional[List[str]] = None

    external_user_write_access: Optional[List[str]] = None

    file_url: Optional[str] = None

    filename: Optional[str] = None

    hierarchical_structures: Optional[str] = None

    location: Optional[str] = None

    metadata: Union[str, Dict[str, object], None] = None

    metrics: Optional[Dict[str, object]] = None

    namespace_id: Optional[str] = None
    """Namespace ID this memory belongs to"""

    namespace_read_access: Optional[List[str]] = None

    namespace_write_access: Optional[List[str]] = None

    organization_id: Optional[str] = None
    """Organization ID that owns this memory"""

    organization_read_access: Optional[List[str]] = None

    organization_write_access: Optional[List[str]] = None

    page: Optional[str] = None

    page_number: Optional[int] = None

    popularity_score: Optional[float] = None
    """
    Popularity signal (0-1): 0.5*cacheConfidenceWeighted30d +
    0.5*citationConfidenceWeighted30d. Uses stored EMA fields.
    """

    recency_score: Optional[float] = None
    """Recency signal (0-1): exp(-0.05 \\** days_since_last_access). Half-life ~14 days."""

    relevance_score: Optional[float] = None
    """Final relevance (0-1).

    rank_results=False: 0.6*sim + 0.25*pop + 0.15\\**recency. rank_results=True:
    RRF-based fusion.
    """

    reranker_confidence: Optional[float] = None
    """Reranker confidence (0-1).

    Meaningful for LLM reranking; equals reranker_score for cross-encoders.
    """

    reranker_score: Optional[float] = None
    """Reranker relevance (0-1).

    From cross-encoder (Cohere/Qwen3/BGE) or LLM (GPT-5-nano).
    """

    reranker_type: Optional[str] = None
    """
    Reranker type: 'cross_encoder' (Cohere/Qwen3/BGE) or 'llm'
    (GPT-5-nano/GPT-4o-mini).
    """

    role: Optional[str] = None
    """Role that generated this memory (user or assistant)"""

    role_read_access: Optional[List[str]] = None

    role_write_access: Optional[List[str]] = None

    similarity_score: Optional[float] = None
    """Cosine similarity from vector search (0-1).

    Measures semantic relevance to query.
    """

    source_document_id: Optional[str] = None

    source_message_id: Optional[str] = None

    source_type: Optional[str] = None

    source_url: Optional[str] = None

    steps: Optional[List[str]] = None

    tags: Optional[List[str]] = None

    title: Optional[str] = None

    topics: Optional[List[str]] = None

    total_pages: Optional[int] = None

    total_processing_cost: Optional[float] = FieldInfo(alias="totalProcessingCost", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    user_read_access: Optional[List[str]] = None

    user_write_access: Optional[List[str]] = None

    workspace_id: Optional[str] = None

    workspace_read_access: Optional[List[str]] = None

    workspace_write_access: Optional[List[str]] = None


class DataNode(BaseModel):
    """Public-facing node structure - supports both system and custom schema nodes"""

    label: str
    """
    Node type label - can be system type (Memory, Person, etc.) or custom type from
    UserGraphSchema
    """

    properties: Dict[str, object]
    """Node properties - structure depends on node type and schema"""

    schema_id: Optional[str] = None
    """Reference to UserGraphSchema ID for custom nodes.

    Use GET /v1/schemas/{schema_id} to get full schema definition. Null for system
    nodes.
    """


class Data(BaseModel):
    """Return type for SearchResult"""

    memories: List[DataMemory]

    nodes: List[DataNode]

    schemas_used: Optional[List[str]] = None
    """List of UserGraphSchema IDs used in this response.

    Use GET /v1/schemas/{id} to get full schema definitions.
    """


class SearchResponse(BaseModel):
    code: Optional[int] = None
    """HTTP status code"""

    data: Optional[Data] = None
    """Return type for SearchResult"""

    details: Optional[object] = None
    """Additional error details or context"""

    error: Optional[str] = None
    """Error message if failed"""

    search_id: Optional[str] = None
    """
    Unique identifier for this search query, maps to QueryLog objectId in Parse
    Server
    """

    status: Optional[str] = None
    """'success' or 'error'"""
