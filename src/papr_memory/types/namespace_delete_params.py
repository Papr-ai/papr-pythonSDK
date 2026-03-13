# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["NamespaceDeleteParams"]


class NamespaceDeleteParams(TypedDict, total=False):
    delete_memories: bool
    """Delete all memories in this namespace"""

    delete_neo4j_nodes: bool
    """Delete all Neo4j nodes in this namespace"""

    remove_acl_references: bool
    """Remove namespace from ACL arrays on remaining nodes"""
