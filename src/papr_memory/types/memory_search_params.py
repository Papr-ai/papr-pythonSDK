# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .memory_metadata_param import MemoryMetadataParam

__all__ = [
    "MemorySearchParams",
    "HolographicConfig",
    "OmoFilter",
    "RerankingConfig",
    "SearchOverride",
    "SearchOverridePattern",
    "SearchOverrideFilter",
]


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

    response_format: Literal["json", "toon"]
    """
    Response format: 'json' (default) or 'toon' (Token-Oriented Object Notation for
    30-60% token reduction in LLM contexts)
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
    """Your application's user identifier to filter search results.

    This is the primary way to identify users. Use this for your app's user IDs
    (e.g., 'user_alice_123', UUID, email).
    """

    holographic_config: Optional[HolographicConfig]
    """Configuration for holographic neural embedding transforms and H-COND scoring.

    Neural holographic embeddings use 13 brain-inspired frequency bands to encode
    hierarchical semantic metadata alongside the base embedding. H-COND (Holographic
    CONDitional) scoring uses phase alignment for improved relevance ranking.
    """

    metadata: Optional[MemoryMetadataParam]
    """Metadata for memory request"""

    namespace_id: Optional[str]
    """Optional namespace ID for multi-tenant search scoping.

    When provided, search is scoped to memories within this namespace.
    """

    omo_filter: Optional[OmoFilter]
    """Filter for Open Memory Object (OMO) safety standards in search/retrieval.

    Use this to filter search results by consent level and/or risk level.
    """

    organization_id: Optional[str]
    """Optional organization ID for multi-tenant search scoping.

    When provided, search is scoped to memories within this organization.
    """

    rank_results: bool
    """DEPRECATED: Use 'reranking_config' instead.

    Whether to enable additional ranking of search results. Default is false because
    results are already ranked when using an LLM for search (recommended approach).
    Only enable this if you're not using an LLM in your search pipeline and need
    additional result ranking. Migration: Replace 'rank_results: true' with
    'reranking_config: {reranking_enabled: true, reranking_provider: "cohere",
    reranking_model: "rerank-v3.5"}'
    """

    reranking_config: Optional[RerankingConfig]
    """Configuration for reranking memory search results"""

    schema_id: Optional[str]
    """Optional user-defined schema ID to use for this search.

    If provided, this schema (plus system schema) will be used for query generation.
    If not provided, system will automatically select relevant schema based on query
    content.
    """

    search_override: Optional[SearchOverride]
    """Complete search override specification provided by developer"""

    user_id: Optional[str]
    """DEPRECATED: Use 'external_user_id' instead.

    Internal Papr Parse user ID. Most developers should not use this field directly.
    """

    accept_encoding: Annotated[str, PropertyInfo(alias="Accept-Encoding")]


class HolographicConfig(TypedDict, total=False):
    """Configuration for holographic neural embedding transforms and H-COND scoring.

    Neural holographic embeddings use 13 brain-inspired frequency bands to encode
    hierarchical semantic metadata alongside the base embedding. H-COND (Holographic
    CONDitional) scoring uses phase alignment for improved relevance ranking.
    """

    enabled: bool
    """Whether to enable holographic embedding transforms"""

    hcond_boost_factor: float
    """Maximum boost to add for high alignment (0.0-0.5)"""

    hcond_boost_threshold: float
    """Phase alignment threshold above which to apply boost (0.0-1.0)"""

    hcond_penalty_factor: float
    """Maximum penalty for low alignment (0.0-0.5)"""

    search_mode: Literal["disabled", "integrated", "post_search"]
    """
    Search mode: 'disabled' (off), 'integrated' (search transformed embeddings),
    'post_search' (fetch then rerank with H-COND)
    """


class OmoFilter(TypedDict, total=False):
    """Filter for Open Memory Object (OMO) safety standards in search/retrieval.

    Use this to filter search results by consent level and/or risk level.
    """

    exclude_consent: Optional[List[Literal["explicit", "implicit", "terms", "none"]]]
    """Explicitly exclude memories with these consent levels.

    Example: exclude_consent=['none'] filters out all memories without consent.
    """

    exclude_flagged: bool
    """If true, exclude all flagged content (risk == 'flagged').

    Shorthand for exclude_risk=['flagged'].
    """

    exclude_risk: Optional[List[Literal["none", "sensitive", "flagged"]]]
    """Explicitly exclude memories with these risk levels.

    Example: exclude_risk=['flagged'] filters out all flagged content.
    """

    max_risk: Optional[Literal["none", "sensitive", "flagged"]]
    """Post-ingest safety assessment of memory content.

    Aligned with Open Memory Object (OMO) standard.
    """

    min_consent: Optional[Literal["explicit", "implicit", "terms", "none"]]
    """How the data owner allowed this memory to be stored/used.

    Aligned with Open Memory Object (OMO) standard.
    """

    require_consent: bool
    """If true, only return memories with explicit consent (consent != 'none').

    Shorthand for exclude_consent=['none'].
    """


class RerankingConfig(TypedDict, total=False):
    """Configuration for reranking memory search results"""

    reranking_enabled: bool
    """Whether to enable reranking of search results"""

    reranking_model: str
    """Model to use for reranking.

    OpenAI (LLM): 'gpt-5-nano' (fast reasoning, default), 'gpt-5-mini' (better
    quality reasoning). Cohere (cross-encoder): 'rerank-v3.5' (latest),
    'rerank-english-v3.0', 'rerank-multilingual-v3.0'
    """

    reranking_provider: Literal["openai", "cohere"]
    """
    Reranking provider: 'openai' (better quality, slower) or 'cohere' (faster,
    optimized for reranking)
    """


class SearchOverridePattern(TypedDict, total=False):
    """Graph pattern to search for (source)-[relationship]->(target)"""

    relationship_type: Required[str]
    """Relationship type (e.g., 'ASSOCIATED_WITH', 'WORKS_FOR').

    Must match schema relationship types.
    """

    source_label: Required[str]
    """Source node label (e.g., 'Memory', 'Person', 'Company').

    Must match schema node types.
    """

    target_label: Required[str]
    """Target node label (e.g., 'Person', 'Company', 'Project').

    Must match schema node types.
    """

    direction: str
    """
    Relationship direction: '->' (outgoing), '<-' (incoming), or '-' (bidirectional)
    """


class SearchOverrideFilter(TypedDict, total=False):
    """Property filters for search override"""

    node_type: Required[str]
    """Node type to filter (e.g., 'Person', 'Memory', 'Company')"""

    operator: Required[str]
    """Filter operator: 'CONTAINS', 'EQUALS', 'STARTS_WITH', 'IN'"""

    property_name: Required[str]
    """Property name to filter on (e.g., 'name', 'content', 'role')"""

    value: Required[Union[str, SequenceNotStr[str], float, bool]]
    """Filter value(s). Use list for 'IN' operator."""


class SearchOverride(TypedDict, total=False):
    """Complete search override specification provided by developer"""

    pattern: Required[SearchOverridePattern]
    """Graph pattern to search for (source)-[relationship]->(target)"""

    filters: Iterable[SearchOverrideFilter]
    """Property filters to apply to the search pattern"""

    return_properties: Optional[SequenceNotStr[str]]
    """Specific properties to return. If not specified, returns all properties."""
