# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .memory_type import MemoryType
from .context_item_param import ContextItemParam
from .memory_metadata_param import MemoryMetadataParam
from .relationship_item_param import RelationshipItemParam

__all__ = ["AddMemoryParam"]


class AddMemoryParam(TypedDict, total=False):
    content: Required[str]
    """The content of the memory item you want to add to memory"""

    type: Required[MemoryType]
    """Valid memory types"""

    context: Optional[Iterable[ContextItemParam]]
    """Context can be conversation history or any relevant context for a memory item"""

    metadata: Optional[MemoryMetadataParam]
    """Metadata for memory request"""

    relationships_json: Optional[Iterable[RelationshipItemParam]]
    """Array of relationships that we can use in Graph DB (neo4J)"""
