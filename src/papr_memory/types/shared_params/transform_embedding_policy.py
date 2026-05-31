# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["TransformEmbeddingPolicy"]


class TransformEmbeddingPolicy(TypedDict, total=False):
    domain_id: Optional[str]
    """Signal domain id or shorthand (e.g. cosqa)"""

    mode: Literal["none", "auto", "manual"]
    """none=base embed only; auto=run graph transform; manual=BYO signals"""

    signals: Optional[Dict[str, str]]
    """BYO band text values when mode=manual"""
