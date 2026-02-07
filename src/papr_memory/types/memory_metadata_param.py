# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["MemoryMetadataParam"]


class MemoryMetadataParamTyped(TypedDict, total=False):
    """Metadata for memory request"""

    acl: Optional[Dict[str, SequenceNotStr[str]]]
    """DEPRECATED: Use 'memory_policy.acl' at request level instead.

    Format: {'read': [...], 'write': [...]}.
    """

    assistant_message: Annotated[Optional[str], PropertyInfo(alias="assistantMessage")]

    category: Optional[Literal["preference", "task", "goal", "fact", "context", "skills", "learning"]]
    """Memory category based on role.

    For users: preference, task, goal, fact, context. For assistants: skills,
    learning, task, goal, fact, context.
    """

    consent: Optional[str]
    """DEPRECATED: Use 'memory_policy.consent' at request level instead.

    Values: 'explicit', 'implicit' (default), 'terms', 'none'.
    """

    conversation_id: Annotated[Optional[str], PropertyInfo(alias="conversationId")]

    created_at: Annotated[Optional[str], PropertyInfo(alias="createdAt")]
    """ISO datetime when the memory was created"""

    custom_metadata: Annotated[
        Optional[Dict[str, Union[str, float, bool, SequenceNotStr[str]]]], PropertyInfo(alias="customMetadata")
    ]
    """Optional object for arbitrary custom metadata fields.

    Only string, number, boolean, or list of strings allowed. Nested dicts are not
    allowed.
    """

    emoji_tags: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="emoji tags")]

    emotion_tags: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="emotion tags")]

    external_user_id: Optional[str]
    """DEPRECATED: Use 'external_user_id' at request level instead.

    This field will be removed in v2.
    """

    external_user_read_access: Optional[SequenceNotStr[str]]
    """INTERNAL: Auto-populated for vector store filtering.

    Use memory_policy.acl instead.
    """

    external_user_write_access: Optional[SequenceNotStr[str]]
    """INTERNAL: Auto-populated for vector store filtering.

    Use memory_policy.acl instead.
    """

    goal_classification_scores: Annotated[Optional[Iterable[float]], PropertyInfo(alias="goalClassificationScores")]

    hierarchical_structures: Union[str, Iterable[object], None]
    """Hierarchical structures to enable navigation from broad topics to specific ones"""

    location: Optional[str]

    namespace_id: Optional[str]
    """DEPRECATED: Use 'namespace_id' at request level instead.

    This field will be removed in v2.
    """

    namespace_read_access: Optional[SequenceNotStr[str]]
    """INTERNAL: Auto-populated for vector store filtering.

    Use memory_policy.acl instead.
    """

    namespace_write_access: Optional[SequenceNotStr[str]]
    """INTERNAL: Auto-populated for vector store filtering.

    Use memory_policy.acl instead.
    """

    organization_id: Optional[str]
    """DEPRECATED: Use 'organization_id' at request level instead.

    This field will be removed in v2.
    """

    organization_read_access: Optional[SequenceNotStr[str]]
    """INTERNAL: Auto-populated for vector store filtering.

    Use memory_policy.acl instead.
    """

    organization_write_access: Optional[SequenceNotStr[str]]
    """INTERNAL: Auto-populated for vector store filtering.

    Use memory_policy.acl instead.
    """

    page_id: Annotated[Optional[str], PropertyInfo(alias="pageId")]

    post: Optional[str]

    related_goals: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="relatedGoals")]

    related_steps: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="relatedSteps")]

    related_use_cases: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="relatedUseCases")]

    risk: Optional[str]
    """DEPRECATED: Use 'memory_policy.risk' at request level instead.

    Values: 'none' (default), 'sensitive', 'flagged'.
    """

    role: Optional[Literal["user", "assistant"]]
    """Role of the message sender"""

    role_read_access: Optional[SequenceNotStr[str]]
    """INTERNAL: Auto-populated for vector store filtering.

    Use memory_policy.acl instead.
    """

    role_write_access: Optional[SequenceNotStr[str]]
    """INTERNAL: Auto-populated for vector store filtering.

    Use memory_policy.acl instead.
    """

    session_id: Annotated[Optional[str], PropertyInfo(alias="sessionId")]

    source_type: Annotated[Optional[str], PropertyInfo(alias="sourceType")]

    source_url: Annotated[Optional[str], PropertyInfo(alias="sourceUrl")]

    step_classification_scores: Annotated[Optional[Iterable[float]], PropertyInfo(alias="stepClassificationScores")]

    topics: Optional[SequenceNotStr[str]]

    upload_id: Optional[str]
    """Upload ID for document processing workflows"""

    use_case_classification_scores: Annotated[
        Optional[Iterable[float]], PropertyInfo(alias="useCaseClassificationScores")
    ]

    user_id: Optional[str]
    """DEPRECATED: Use 'external_user_id' at request level instead.

    This field will be removed in v2.
    """

    user_read_access: Optional[SequenceNotStr[str]]
    """INTERNAL: Auto-populated for vector store filtering.

    Use memory_policy.acl instead.
    """

    user_write_access: Optional[SequenceNotStr[str]]
    """INTERNAL: Auto-populated for vector store filtering.

    Use memory_policy.acl instead.
    """

    user_message: Annotated[Optional[str], PropertyInfo(alias="userMessage")]

    workspace_id: Optional[str]

    workspace_read_access: Optional[SequenceNotStr[str]]
    """INTERNAL: Auto-populated for vector store filtering.

    Use memory_policy.acl instead.
    """

    workspace_write_access: Optional[SequenceNotStr[str]]
    """INTERNAL: Auto-populated for vector store filtering.

    Use memory_policy.acl instead.
    """


MemoryMetadataParam: TypeAlias = Union[MemoryMetadataParamTyped, Dict[str, object]]
