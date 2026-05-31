# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TransformEmbeddingPolicy"]


class TransformEmbeddingPolicy(BaseModel):
    domain_id: Optional[str] = None
    """Signal domain id or shorthand (e.g. cosqa)"""

    mode: Optional[Literal["none", "auto", "manual"]] = None
    """none=base embed only; auto=run graph transform; manual=BYO signals"""

    signals: Optional[Dict[str, str]] = None
    """BYO band text values when mode=manual"""
