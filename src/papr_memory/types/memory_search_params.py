# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .memory_metadata_param import MemoryMetadataParam

__all__ = ["MemorySearchParams"]


class MemorySearchParams(TypedDict, total=False):
    query: Required[str]
    """Detailed search query describing what you're looking for.

    For best results, write 2-3 sentences that include specific details, context,
    and time frame. Examples: 'Find recurring customer complaints about API
    performance from the last month. Focus on issues where customers specifically
    mentioned timeout errors or slow response times in their conversations.' 'What
    are the main issues and blockers in my current projects? Focus on technical
    challenges and timeline impacts.' 'Find insights about team collaboration and
    communication patterns from recent meetings and discussions.'
    """

    max_memories: int
    """HIGHLY RECOMMENDED: Maximum number of memories to return.

    Use at least 15-20 for comprehensive results. Lower values (5-10) may miss
    relevant information. Default is 20 for optimal coverage.
    """

    max_nodes: int
    """HIGHLY RECOMMENDED: Maximum number of neo nodes to return.

    Use at least 10-15 for comprehensive graph results. Lower values may miss
    important entity relationships. Default is 15 for optimal coverage.
    """

    enable_agentic_graph: bool
    """
    HIGHLY RECOMMENDED: Enable agentic graph search for intelligent, context-aware
    results. When enabled, the system can understand ambiguous references by first
    identifying specific entities from your memory graph, then performing targeted
    searches. Examples: 'customer feedback' → identifies your customers first, then
    finds their specific feedback; 'project issues' → identifies your projects
    first, then finds related issues; 'team meeting notes' → identifies team members
    first, then finds meeting notes. This provides much more relevant and
    comprehensive results. Set to false only if you need faster, simpler
    keyword-based search.
    """

    external_user_id: Optional[str]
    """Optional external user ID to filter search results by a specific external user.

    If both user_id and external_user_id are provided, user_id takes precedence.
    """

    metadata: Optional[MemoryMetadataParam]
    """Metadata for memory request"""

    rank_results: bool
    """Whether to enable additional ranking of search results.

    Default is false because results are already ranked when using an LLM for search
    (recommended approach). Only enable this if you're not using an LLM in your
    search pipeline and need additional result ranking.
    """

    user_id: Optional[str]
    """Optional internal user ID to filter search results by a specific user.

    If not provided, results are not filtered by user. If both user_id and
    external_user_id are provided, user_id takes precedence.
    """

    accept_encoding: Annotated[str, PropertyInfo(alias="Accept-Encoding")]
