# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .memory_metadata_param import MemoryMetadataParam
from .shared_params.acl_config import ACLConfig
from .shared_params.graph_policy_block import GraphPolicyBlock

__all__ = [
    "MemorySearchParams",
    "OmoFilter",
    "Policy",
    "PolicyVector",
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

    policy: Optional[Policy]
    """Policy for POST /v1/memory/search.

    External Cohere/OpenAI rerank and search-time ACL use top-level fields on
    SearchRequest (`reranking_config`, `search_acl`) until wired here.
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
    """Ranking provider for search results (cosine candidates → ranked list)."""

    schema_id: Optional[str]
    """Optional user-defined schema ID to use for this search.

    If provided, this schema (plus system schema) will be used for query generation.
    If not provided, system will automatically select relevant schema based on query
    content.
    """

    search_acl: Optional[ACLConfig]
    """Simplified Access Control List configuration.

    Aligned with Open Memory Object (OMO) standard. See:
    https://github.com/anthropics/open-memory-object

    **Supported Entity Prefixes:**

    | Prefix           | Description           | Validation                           |
    | ---------------- | --------------------- | ------------------------------------ |
    | `user:`          | Internal Papr user ID | Validated against Parse users        |
    | `external_user:` | Your app's user ID    | Not validated (your responsibility)  |
    | `organization:`  | Organization ID       | Validated against your organizations |
    | `namespace:`     | Namespace ID          | Validated against your namespaces    |
    | `workspace:`     | Workspace ID          | Validated against your workspaces    |
    | `role:`          | Parse role ID         | Validated against your roles         |

    **Examples:**

    ```python
    acl = ACLConfig(
        read=["external_user:alice_123", "organization:org_acme"],
        write=["external_user:alice_123"]
    )
    ```

    **Validation Rules:**

    - Internal entities (user, organization, namespace, workspace, role) are
      validated
    - External entities (external_user) are NOT validated - your app is responsible
    - Invalid internal entities will return an error
    - Unprefixed values default to `external_user:` for backwards compatibility
    """

    search_override: Optional[SearchOverride]
    """Complete search override specification provided by developer"""

    user_id: Optional[str]
    """DEPRECATED: Use 'external_user_id' instead.

    Internal Papr Parse user ID. Most developers should not use this field directly.
    """

    accept_encoding: Annotated[str, PropertyInfo(alias="Accept-Encoding")]


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


class PolicyVector(TypedDict, total=False):
    domain_id: Optional[str]

    mode: Literal["fast", "enhanced", "max"]
    """fast=cosine; enhanced=graph rerank enhanced; max=graph rerank max"""

    return_debug: bool

    return_signal_scores: bool

    signal_multipliers: Optional[Dict[str, Union[float, str]]]

    signal_thresholds: Optional[Dict[str, float]]
    """Min per-band scores; maps to graph rerank signal_filters"""


class Policy(TypedDict, total=False):
    """Policy for POST /v1/memory/search.

    External Cohere/OpenAI rerank and search-time ACL use top-level fields on
    SearchRequest (``reranking_config``, ``search_acl``) until wired here.
    """

    consent: Literal["explicit", "implicit", "terms", "none"]
    """How the data owner allowed this memory to be stored/used.

    Aligned with Open Memory Object (OMO) standard.
    """

    graph: Optional[GraphPolicyBlock]

    risk: Literal["none", "sensitive", "flagged"]
    """Post-ingest safety assessment of memory content.

    Aligned with Open Memory Object (OMO) standard.
    """

    vector: Optional[PolicyVector]


class RerankingConfig(TypedDict, total=False):
    """Ranking provider for search results (cosine candidates → ranked list)."""

    domain_id: Optional[str]
    """Signal domain for papr_enhanced / papr_max (default general)."""

    reranking_enabled: bool
    """When false, results stay in cosine order (same as provider=none)."""

    reranking_model: str
    """Model for cohere/openai providers.

    Cohere: rerank-v3.5. OpenAI: gpt-5-nano, gpt-5-mini.
    """

    reranking_provider: Literal["none", "cohere", "openai", "papr_enhanced", "papr_max"]
    """
    Ranking provider: none (cosine), cohere, openai, papr_enhanced (graph rerank),
    papr_max (graph rerank + CE + EGR).
    """

    return_debug: bool

    return_signal_scores: bool

    signal_multipliers: Optional[Dict[str, Union[float, str]]]

    signal_thresholds: Optional[Dict[str, float]]
    """Min per-band scores for papr providers."""


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
