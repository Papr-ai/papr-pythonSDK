# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MemorySearchParams"]


class MemorySearchParams(TypedDict, total=False):
    query: Required[str]
    """Detailed search query describing what you're looking for.

    For best results, write 2-3 sentences that include specific details, context,
    and time frame. For example: 'Find recurring customer complaints about API
    performance from the last month. Focus on issues where customers specifically
    mentioned timeout errors or slow response times in their conversations.'
    """

    max_memories: int
    """Maximum number of memories to return"""

    max_nodes: int
    """Maximum number of neo nodes to return"""

    rank_results: bool
    """Whether to enable additional ranking of search results.

    Default is false because results are already ranked when using an LLM for search
    (recommended approach). Only enable this if you're not using an LLM in your
    search pipeline and need additional result ranking.
    """

    user_id: Optional[str]
    """Optional user ID to filter search results by a specific user.

    If not provided, results are not filtered by user.
    """

    accept_encoding: Annotated[str, PropertyInfo(alias="Accept-Encoding")]
