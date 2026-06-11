# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DocumentGetStatusParams"]


class DocumentGetStatusParams(TypedDict, total=False):
    timeline: bool
    """
    When true, include a `timeline` object with ordered processing steps, per-step
    status, and timing. Default response shape is unchanged.
    """
