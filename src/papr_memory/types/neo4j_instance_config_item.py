# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Neo4jInstanceConfigItem"]


class Neo4jInstanceConfigItem(BaseModel):
    """Neo4j instance configuration — response (password masked)."""

    bolt_url: str
    """Neo4j bolt connection URL"""

    password_masked: str
    """Masked password (e.g. '\\**\\**\\**\\**ab12')"""

    username: str
    """Neo4j username"""

    graphql_endpoint: Optional[str] = None
    """Neo4j GraphQL endpoint URL"""
