# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .context_item import ContextItem

__all__ = [
    "SearchResponse",
    "Data",
    "DataMemory",
    "DataNode",
    "DataNodeProperties",
    "DataNodePropertiesPaprMemoryNodeProperties",
    "DataNodePropertiesPersonNodeProperties",
    "DataNodePropertiesCompanyNodeProperties",
    "DataNodePropertiesProjectNodeProperties",
    "DataNodePropertiesTaskNodeProperties",
    "DataNodePropertiesInsightNodeProperties",
    "DataNodePropertiesMeetingNodeProperties",
    "DataNodePropertiesOpportunityNodeProperties",
    "DataNodePropertiesCodeNodeProperties",
]


class DataMemory(BaseModel):
    id: str

    acl: Dict[str, Dict[str, bool]]

    content: str

    type: str

    user_id: str

    context: Optional[List[ContextItem]] = None

    conversation_id: Optional[str] = None

    created_at: Optional[datetime] = None

    current_step: Optional[str] = None

    custom_metadata: Optional[Dict[str, object]] = FieldInfo(alias="customMetadata", default=None)

    external_user_id: Optional[str] = None

    external_user_read_access: Optional[List[str]] = None

    external_user_write_access: Optional[List[str]] = None

    file_url: Optional[str] = None

    filename: Optional[str] = None

    hierarchical_structures: Optional[str] = None

    location: Optional[str] = None

    metadata: Union[str, Dict[str, object], None] = None

    page: Optional[str] = None

    page_number: Optional[int] = None

    role_read_access: Optional[List[str]] = None

    role_write_access: Optional[List[str]] = None

    source_document_id: Optional[str] = None

    source_message_id: Optional[str] = None

    source_type: Optional[str] = None

    source_url: Optional[str] = None

    steps: Optional[List[str]] = None

    tags: Optional[List[str]] = None

    title: Optional[str] = None

    topics: Optional[List[str]] = None

    total_pages: Optional[int] = None

    updated_at: Optional[datetime] = None

    user_read_access: Optional[List[str]] = None

    user_write_access: Optional[List[str]] = None

    workspace_id: Optional[str] = None

    workspace_read_access: Optional[List[str]] = None

    workspace_write_access: Optional[List[str]] = None

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class DataNodePropertiesPaprMemoryNodeProperties(BaseModel):
    id: str

    content: str

    current_step: str

    emotion_tags: List[str]

    steps: List[str]

    topics: List[str]

    type: str

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    emoji_tags: Optional[List[str]] = None

    external_user_read_access: Optional[List[str]] = None

    external_user_write_access: Optional[List[str]] = None

    hierarchical_structures: Optional[str] = None

    page_id: Optional[str] = FieldInfo(alias="pageId", default=None)

    role_read_access: Optional[List[str]] = None

    role_write_access: Optional[List[str]] = None

    source_type: Optional[str] = FieldInfo(alias="sourceType", default=None)

    source_url: Optional[str] = FieldInfo(alias="sourceUrl", default=None)

    title: Optional[str] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    user_id: Optional[str] = None

    user_read_access: Optional[List[str]] = None

    user_write_access: Optional[List[str]] = None

    workspace_id: Optional[str] = None

    workspace_read_access: Optional[List[str]] = None

    workspace_write_access: Optional[List[str]] = None


class DataNodePropertiesPersonNodeProperties(BaseModel):
    id: str

    description: str

    name: str

    role: str

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    external_user_read_access: Optional[List[str]] = None

    external_user_write_access: Optional[List[str]] = None

    page_id: Optional[str] = FieldInfo(alias="pageId", default=None)

    role_read_access: Optional[List[str]] = None

    role_write_access: Optional[List[str]] = None

    source_type: Optional[str] = FieldInfo(alias="sourceType", default=None)

    source_url: Optional[str] = FieldInfo(alias="sourceUrl", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    user_id: Optional[str] = None

    user_read_access: Optional[List[str]] = None

    user_write_access: Optional[List[str]] = None

    workspace_id: Optional[str] = None

    workspace_read_access: Optional[List[str]] = None

    workspace_write_access: Optional[List[str]] = None


class DataNodePropertiesCompanyNodeProperties(BaseModel):
    id: str

    description: str

    name: str

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    external_user_read_access: Optional[List[str]] = None

    external_user_write_access: Optional[List[str]] = None

    page_id: Optional[str] = FieldInfo(alias="pageId", default=None)

    role_read_access: Optional[List[str]] = None

    role_write_access: Optional[List[str]] = None

    source_type: Optional[str] = FieldInfo(alias="sourceType", default=None)

    source_url: Optional[str] = FieldInfo(alias="sourceUrl", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    user_id: Optional[str] = None

    user_read_access: Optional[List[str]] = None

    user_write_access: Optional[List[str]] = None

    workspace_id: Optional[str] = None

    workspace_read_access: Optional[List[str]] = None

    workspace_write_access: Optional[List[str]] = None


class DataNodePropertiesProjectNodeProperties(BaseModel):
    id: str

    description: str

    name: str

    type: str

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    external_user_read_access: Optional[List[str]] = None

    external_user_write_access: Optional[List[str]] = None

    page_id: Optional[str] = FieldInfo(alias="pageId", default=None)

    role_read_access: Optional[List[str]] = None

    role_write_access: Optional[List[str]] = None

    source_type: Optional[str] = FieldInfo(alias="sourceType", default=None)

    source_url: Optional[str] = FieldInfo(alias="sourceUrl", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    user_id: Optional[str] = None

    user_read_access: Optional[List[str]] = None

    user_write_access: Optional[List[str]] = None

    workspace_id: Optional[str] = None

    workspace_read_access: Optional[List[str]] = None

    workspace_write_access: Optional[List[str]] = None


class DataNodePropertiesTaskNodeProperties(BaseModel):
    id: str

    description: str

    status: Literal["new", "in_progress", "completed"]

    title: str

    type: Literal["task", "subtask", "bug", "feature_request", "epic", "support_ticket"]

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    date: Optional[datetime] = None
    """Due date for the task in ISO 8601 format"""

    external_user_read_access: Optional[List[str]] = None

    external_user_write_access: Optional[List[str]] = None

    page_id: Optional[str] = FieldInfo(alias="pageId", default=None)

    priority: Optional[Literal["low", "medium", "high", "urgent"]] = None

    role_read_access: Optional[List[str]] = None

    role_write_access: Optional[List[str]] = None

    source_type: Optional[str] = FieldInfo(alias="sourceType", default=None)

    source_url: Optional[str] = FieldInfo(alias="sourceUrl", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    user_id: Optional[str] = None

    user_read_access: Optional[List[str]] = None

    user_write_access: Optional[List[str]] = None

    workspace_id: Optional[str] = None

    workspace_read_access: Optional[List[str]] = None

    workspace_write_access: Optional[List[str]] = None


class DataNodePropertiesInsightNodeProperties(BaseModel):
    id: str

    description: str

    source: str

    title: str

    type: Literal[
        "customer_insight", "product_insight", "market_insight", "competitive_insight", "technical_insight", "other"
    ]

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    external_user_read_access: Optional[List[str]] = None

    external_user_write_access: Optional[List[str]] = None

    page_id: Optional[str] = FieldInfo(alias="pageId", default=None)

    role_read_access: Optional[List[str]] = None

    role_write_access: Optional[List[str]] = None

    source_type: Optional[str] = FieldInfo(alias="sourceType", default=None)

    source_url: Optional[str] = FieldInfo(alias="sourceUrl", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    user_id: Optional[str] = None

    user_read_access: Optional[List[str]] = None

    user_write_access: Optional[List[str]] = None

    workspace_id: Optional[str] = None

    workspace_read_access: Optional[List[str]] = None

    workspace_write_access: Optional[List[str]] = None


class DataNodePropertiesMeetingNodeProperties(BaseModel):
    id: str

    action_items: List[str]

    agenda: str

    date: str

    outcome: str

    participants: List[str]

    summary: str

    time: str

    title: str

    type: str

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    external_user_read_access: Optional[List[str]] = None

    external_user_write_access: Optional[List[str]] = None

    page_id: Optional[str] = FieldInfo(alias="pageId", default=None)

    role_read_access: Optional[List[str]] = None

    role_write_access: Optional[List[str]] = None

    source_type: Optional[str] = FieldInfo(alias="sourceType", default=None)

    source_url: Optional[str] = FieldInfo(alias="sourceUrl", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    user_id: Optional[str] = None

    user_read_access: Optional[List[str]] = None

    user_write_access: Optional[List[str]] = None

    workspace_id: Optional[str] = None

    workspace_read_access: Optional[List[str]] = None

    workspace_write_access: Optional[List[str]] = None


class DataNodePropertiesOpportunityNodeProperties(BaseModel):
    id: str

    close_date: str

    description: str

    next_steps: List[str]

    probability: float

    stage: Literal["prospect", "lead", "opportunity", "won", "lost"]

    title: str

    value: float

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    external_user_read_access: Optional[List[str]] = None

    external_user_write_access: Optional[List[str]] = None

    page_id: Optional[str] = FieldInfo(alias="pageId", default=None)

    role_read_access: Optional[List[str]] = None

    role_write_access: Optional[List[str]] = None

    source_type: Optional[str] = FieldInfo(alias="sourceType", default=None)

    source_url: Optional[str] = FieldInfo(alias="sourceUrl", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    user_id: Optional[str] = None

    user_read_access: Optional[List[str]] = None

    user_write_access: Optional[List[str]] = None

    workspace_id: Optional[str] = None

    workspace_read_access: Optional[List[str]] = None

    workspace_write_access: Optional[List[str]] = None


class DataNodePropertiesCodeNodeProperties(BaseModel):
    id: str

    author: str

    language: str

    name: str

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    external_user_read_access: Optional[List[str]] = None

    external_user_write_access: Optional[List[str]] = None

    page_id: Optional[str] = FieldInfo(alias="pageId", default=None)

    role_read_access: Optional[List[str]] = None

    role_write_access: Optional[List[str]] = None

    source_type: Optional[str] = FieldInfo(alias="sourceType", default=None)

    source_url: Optional[str] = FieldInfo(alias="sourceUrl", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    user_id: Optional[str] = None

    user_read_access: Optional[List[str]] = None

    user_write_access: Optional[List[str]] = None

    workspace_id: Optional[str] = None

    workspace_read_access: Optional[List[str]] = None

    workspace_write_access: Optional[List[str]] = None


DataNodeProperties: TypeAlias = Union[
    DataNodePropertiesPaprMemoryNodeProperties,
    DataNodePropertiesPersonNodeProperties,
    DataNodePropertiesCompanyNodeProperties,
    DataNodePropertiesProjectNodeProperties,
    DataNodePropertiesTaskNodeProperties,
    DataNodePropertiesInsightNodeProperties,
    DataNodePropertiesMeetingNodeProperties,
    DataNodePropertiesOpportunityNodeProperties,
    DataNodePropertiesCodeNodeProperties,
]


class DataNode(BaseModel):
    label: Literal["Memory", "Person", "Company", "Project", "Task", "Insight", "Meeting", "Opportunity", "Code"]

    properties: DataNodeProperties
    """Memory node properties"""


class Data(BaseModel):
    memories: List[DataMemory]

    nodes: List[DataNode]


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
