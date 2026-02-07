# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MemoryMetadata"]


class MemoryMetadata(BaseModel):
    """Metadata for memory request"""

    acl: Optional[Dict[str, List[str]]] = None
    """DEPRECATED: Use 'memory_policy.acl' at request level instead.

    Format: {'read': [...], 'write': [...]}.
    """

    assistant_message: Optional[str] = FieldInfo(alias="assistantMessage", default=None)

    category: Optional[Literal["preference", "task", "goal", "fact", "context", "skills", "learning"]] = None
    """Memory category based on role.

    For users: preference, task, goal, fact, context. For assistants: skills,
    learning, task, goal, fact, context.
    """

    consent: Optional[str] = None
    """DEPRECATED: Use 'memory_policy.consent' at request level instead.

    Values: 'explicit', 'implicit' (default), 'terms', 'none'.
    """

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)
    """ISO datetime when the memory was created"""

    custom_metadata: Optional[Dict[str, Union[str, float, bool, List[str]]]] = FieldInfo(
        alias="customMetadata", default=None
    )
    """Optional object for arbitrary custom metadata fields.

    Only string, number, boolean, or list of strings allowed. Nested dicts are not
    allowed.
    """

    emoji_tags: Optional[List[str]] = FieldInfo(alias="emoji tags", default=None)

    emotion_tags: Optional[List[str]] = FieldInfo(alias="emotion tags", default=None)

    external_user_id: Optional[str] = None
    """DEPRECATED: Use 'external_user_id' at request level instead.

    This field will be removed in v2.
    """

    external_user_read_access: Optional[List[str]] = None
    """INTERNAL: Auto-populated for vector store filtering.

    Use memory_policy.acl instead.
    """

    external_user_write_access: Optional[List[str]] = None
    """INTERNAL: Auto-populated for vector store filtering.

    Use memory_policy.acl instead.
    """

    goal_classification_scores: Optional[List[float]] = FieldInfo(alias="goalClassificationScores", default=None)

    hierarchical_structures: Union[str, List[object], None] = None
    """Hierarchical structures to enable navigation from broad topics to specific ones"""

    location: Optional[str] = None

    namespace_id: Optional[str] = None
    """DEPRECATED: Use 'namespace_id' at request level instead.

    This field will be removed in v2.
    """

    namespace_read_access: Optional[List[str]] = None
    """INTERNAL: Auto-populated for vector store filtering.

    Use memory_policy.acl instead.
    """

    namespace_write_access: Optional[List[str]] = None
    """INTERNAL: Auto-populated for vector store filtering.

    Use memory_policy.acl instead.
    """

    organization_id: Optional[str] = None
    """DEPRECATED: Use 'organization_id' at request level instead.

    This field will be removed in v2.
    """

    organization_read_access: Optional[List[str]] = None
    """INTERNAL: Auto-populated for vector store filtering.

    Use memory_policy.acl instead.
    """

    organization_write_access: Optional[List[str]] = None
    """INTERNAL: Auto-populated for vector store filtering.

    Use memory_policy.acl instead.
    """

    page_id: Optional[str] = FieldInfo(alias="pageId", default=None)

    post: Optional[str] = None

    related_goals: Optional[List[str]] = FieldInfo(alias="relatedGoals", default=None)

    related_steps: Optional[List[str]] = FieldInfo(alias="relatedSteps", default=None)

    related_use_cases: Optional[List[str]] = FieldInfo(alias="relatedUseCases", default=None)

    risk: Optional[str] = None
    """DEPRECATED: Use 'memory_policy.risk' at request level instead.

    Values: 'none' (default), 'sensitive', 'flagged'.
    """

    role: Optional[Literal["user", "assistant"]] = None
    """Role of the message sender"""

    role_read_access: Optional[List[str]] = None
    """INTERNAL: Auto-populated for vector store filtering.

    Use memory_policy.acl instead.
    """

    role_write_access: Optional[List[str]] = None
    """INTERNAL: Auto-populated for vector store filtering.

    Use memory_policy.acl instead.
    """

    session_id: Optional[str] = FieldInfo(alias="sessionId", default=None)

    source_type: Optional[str] = FieldInfo(alias="sourceType", default=None)

    source_url: Optional[str] = FieldInfo(alias="sourceUrl", default=None)

    step_classification_scores: Optional[List[float]] = FieldInfo(alias="stepClassificationScores", default=None)

    topics: Optional[List[str]] = None

    upload_id: Optional[str] = None
    """Upload ID for document processing workflows"""

    use_case_classification_scores: Optional[List[float]] = FieldInfo(alias="useCaseClassificationScores", default=None)

    user_id: Optional[str] = None
    """DEPRECATED: Use 'external_user_id' at request level instead.

    This field will be removed in v2.
    """

    user_read_access: Optional[List[str]] = None
    """INTERNAL: Auto-populated for vector store filtering.

    Use memory_policy.acl instead.
    """

    user_write_access: Optional[List[str]] = None
    """INTERNAL: Auto-populated for vector store filtering.

    Use memory_policy.acl instead.
    """

    user_message: Optional[str] = FieldInfo(alias="userMessage", default=None)

    workspace_id: Optional[str] = None

    workspace_read_access: Optional[List[str]] = None
    """INTERNAL: Auto-populated for vector store filtering.

    Use memory_policy.acl instead.
    """

    workspace_write_access: Optional[List[str]] = None
    """INTERNAL: Auto-populated for vector store filtering.

    Use memory_policy.acl instead.
    """
