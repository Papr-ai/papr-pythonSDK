# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

from .memory_type import MemoryType
from .context_item_param import ContextItemParam
from .memory_metadata_param import MemoryMetadataParam
from .relationship_item_param import RelationshipItemParam

__all__ = ["MemoryUpdateParams"]


class MemoryUpdateParams(TypedDict, total=False):
    content: Optional[str]
    """The new content of the memory item"""

    context: Optional[Iterable[ContextItemParam]]
    """Updated context for the memory item"""

    metadata: Optional[MemoryMetadataParam]
    """Metadata for memory request"""

    namespace_id: Optional[str]
    """Optional namespace ID for multi-tenant memory scoping.

    When provided, update is scoped to memories within this namespace.
    """

    organization_id: Optional[str]
    """Optional organization ID for multi-tenant memory scoping.

    When provided, update is scoped to memories within this organization.
    """

    relationships_json: Optional[Iterable[RelationshipItemParam]]
    """Updated relationships for Graph DB (neo4J)"""

    type: Optional[MemoryType]
    """Valid memory types"""
