# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SessionRetrieveHistoryParams"]


class SessionRetrieveHistoryParams(TypedDict, total=False):
    limit: int
    """Maximum number of messages to return"""

    skip: int
    """Number of messages to skip for pagination"""
