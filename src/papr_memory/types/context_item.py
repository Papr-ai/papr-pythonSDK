# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ContextItem"]


class ContextItem(BaseModel):
    content: str

    role: Literal["user", "assistant"]
