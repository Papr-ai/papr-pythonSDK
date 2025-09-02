# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .parse_pointer_param import ParsePointerParam

__all__ = ["FeedbackSubmitParams", "FeedbackData"]


class FeedbackSubmitParams(TypedDict, total=False):
    feedback_data: Required[Annotated[FeedbackData, PropertyInfo(alias="feedbackData")]]
    """The feedback data containing all feedback information"""

    search_id: Required[str]
    """The search_id from SearchResponse that this feedback relates to"""

    external_user_id: Optional[str]
    """External user ID for developer API keys acting on behalf of end users"""

    user_id: Optional[str]
    """Internal user ID (if not provided, will be resolved from authentication)"""


class FeedbackData(TypedDict, total=False):
    feedback_source: Required[
        Annotated[
            Literal["inline", "post_query", "session_end", "memory_citation", "answer_panel"],
            PropertyInfo(alias="feedbackSource"),
        ]
    ]
    """Where the feedback was provided from"""

    feedback_type: Required[
        Annotated[
            Literal[
                "thumbs_up",
                "thumbs_down",
                "rating",
                "correction",
                "report",
                "copy_action",
                "save_action",
                "create_document",
                "memory_relevance",
                "answer_quality",
            ],
            PropertyInfo(alias="feedbackType"),
        ]
    ]
    """Types of feedback that can be provided"""

    assistant_message: Annotated[Optional[ParsePointerParam], PropertyInfo(alias="assistantMessage")]
    """A pointer to a Parse object"""

    cited_memory_ids: Annotated[Optional[List[str]], PropertyInfo(alias="citedMemoryIds")]

    cited_node_ids: Annotated[Optional[List[str]], PropertyInfo(alias="citedNodeIds")]

    feedback_impact: Annotated[Optional[str], PropertyInfo(alias="feedbackImpact")]

    feedback_processed: Annotated[Optional[bool], PropertyInfo(alias="feedbackProcessed")]

    feedback_score: Annotated[Optional[float], PropertyInfo(alias="feedbackScore")]

    feedback_text: Annotated[Optional[str], PropertyInfo(alias="feedbackText")]

    feedback_value: Annotated[Optional[str], PropertyInfo(alias="feedbackValue")]

    user_message: Annotated[Optional[ParsePointerParam], PropertyInfo(alias="userMessage")]
    """A pointer to a Parse object"""
