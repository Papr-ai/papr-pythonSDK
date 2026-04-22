# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["InstanceUpdateParams", "Neo4j"]


class InstanceUpdateParams(TypedDict, total=False):
    validate: bool
    """Test connection before saving"""

    neo4j: Optional[Neo4j]
    """Neo4j AuraDB instance configuration — input (plain password)."""

    provider: str
    """Cloud provider (only 'gcp' supported today)"""

    region: str
    """Cloud region (only 'us-west1' supported today)"""


class Neo4j(TypedDict, total=False):
    """Neo4j AuraDB instance configuration — input (plain password)."""

    bolt_url: Required[str]
    """Neo4j bolt connection URL (e.g. 'neo4j+s://xxxxx.databases.neo4j.io')"""

    password: Required[str]
    """Neo4j password (encrypted before storage)"""

    graphql_endpoint: Optional[str]
    """Neo4j hosted GraphQL endpoint URL (e.g.

    'https://xxxxx-graphql.production-orch-xxxx.neo4j.io/graphql')
    """

    username: str
    """Neo4j username"""
