# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .neo4j_instance_config_item import Neo4jInstanceConfigItem

__all__ = ["InstanceConfigItem"]


class InstanceConfigItem(BaseModel):
    """Instance configuration — response model for GET endpoints."""

    provider: str
    """Cloud provider"""

    region: str
    """Cloud region"""

    scope: str
    """Where this config was resolved from: 'namespace' or 'organization'"""

    neo4j: Optional[Neo4jInstanceConfigItem] = None
    """Neo4j instance configuration — response (password masked)."""
