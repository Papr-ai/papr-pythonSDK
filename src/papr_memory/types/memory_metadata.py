# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MemoryMetadata"]


class MemoryMetadata(BaseModel):
    assistant_message: Optional[str] = FieldInfo(alias="assistantMessage", default=None)

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

    external_user_read_access: Optional[List[str]] = None

    external_user_write_access: Optional[List[str]] = None

    goal_classification_scores: Optional[List[float]] = FieldInfo(alias="goalClassificationScores", default=None)

    hierarchical_structures: Optional[str] = None
    """Hierarchical structures to enable navigation from broad topics to specific ones"""

    location: Optional[str] = None

    page_id: Optional[str] = FieldInfo(alias="pageId", default=None)

    post: Optional[str] = None

    related_goals: Optional[List[str]] = FieldInfo(alias="relatedGoals", default=None)

    related_steps: Optional[List[str]] = FieldInfo(alias="relatedSteps", default=None)

    related_use_cases: Optional[List[str]] = FieldInfo(alias="relatedUseCases", default=None)

    role_read_access: Optional[List[str]] = None

    role_write_access: Optional[List[str]] = None

    session_id: Optional[str] = FieldInfo(alias="sessionId", default=None)

    source_type: Optional[str] = FieldInfo(alias="sourceType", default=None)

    source_url: Optional[str] = FieldInfo(alias="sourceUrl", default=None)

    step_classification_scores: Optional[List[float]] = FieldInfo(alias="stepClassificationScores", default=None)

    topics: Optional[List[str]] = None

    use_case_classification_scores: Optional[List[float]] = FieldInfo(alias="useCaseClassificationScores", default=None)

    user_id: Optional[str] = None

    user_read_access: Optional[List[str]] = None

    user_write_access: Optional[List[str]] = None

    user_message: Optional[str] = FieldInfo(alias="userMessage", default=None)

    workspace_id: Optional[str] = None

    workspace_read_access: Optional[List[str]] = None

    workspace_write_access: Optional[List[str]] = None

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
