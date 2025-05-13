# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ContextItemParam"]


class ContextItemParam(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["user", "assistant"]]
