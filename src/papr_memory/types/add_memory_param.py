# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .memory_type import MemoryType
from .context_item_param import ContextItemParam
from .memory_metadata_param import MemoryMetadataParam
from .graph_generation_param import GraphGenerationParam
from .relationship_item_param import RelationshipItemParam

__all__ = ["AddMemoryParam"]


class AddMemoryParam(TypedDict, total=False):
    content: Required[str]
    """The content of the memory item you want to add to memory"""

    context: Optional[Iterable[ContextItemParam]]
    """Context can be conversation history or any relevant context for a memory item"""

    graph_generation: Optional[GraphGenerationParam]
    """Graph generation configuration"""

    metadata: Optional[MemoryMetadataParam]
    """Metadata for memory request"""

    namespace_id: Optional[str]
    """Optional namespace ID for multi-tenant memory scoping.

    When provided, memory is associated with this namespace.
    """

    organization_id: Optional[str]
    """Optional organization ID for multi-tenant memory scoping.

    When provided, memory is associated with this organization.
    """

    relationships_json: Optional[Iterable[RelationshipItemParam]]
    """Array of relationships that we can use in Graph DB (neo4J)"""

    type: MemoryType
    """Memory item type; defaults to 'text' if omitted"""
