# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SchemaActivateParams"]


class SchemaActivateParams(TypedDict, total=False):
    body: bool
    """True to activate, False to deactivate"""
