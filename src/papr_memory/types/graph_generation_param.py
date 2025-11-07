# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .auto_graph_generation_param import AutoGraphGenerationParam
from .manual_graph_generation_param import ManualGraphGenerationParam

__all__ = ["GraphGenerationParam"]


class GraphGenerationParam(TypedDict, total=False):
    auto: Optional[AutoGraphGenerationParam]
    """AI-powered graph generation with optional guidance"""

    manual: Optional[ManualGraphGenerationParam]
    """Complete manual control over graph structure"""

    mode: Literal["auto", "manual"]
    """Graph generation mode: 'auto' (AI-powered) or 'manual' (exact specification)"""
