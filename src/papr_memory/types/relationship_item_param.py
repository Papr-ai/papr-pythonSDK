# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RelationshipItemParam"]


class RelationshipItemParam(TypedDict, total=False):
    related_item_id: Required[Literal["TextMemoryItem", "previous_memory_item_id"]]

    related_item_type: Required[Literal["TextMemoryItem"]]

    relation_type: Required[str]

    metadata: object
