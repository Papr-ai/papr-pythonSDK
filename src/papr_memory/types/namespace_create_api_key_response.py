# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["NamespaceCreateAPIKeyResponse", "Data"]


class Data(BaseModel):
    """Public-facing API key data.

    The ``key`` field is populated **only** in the response of
    ``POST /v1/namespace/{namespace_id}/api-keys`` (the moment of creation).
    It is never returned by any read/list endpoint and is never logged.
    Use ``key_prefix`` (first 24 chars) to identify the key in audit trails
    and admin dashboards.
    """

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)
    """Creation timestamp (ISO 8601)"""

    environment: Optional[str] = None
    """Environment label"""

    is_active: Optional[bool] = None
    """Whether this key is active"""

    key: Optional[str] = None
    """The full API key string.

    Returned ONLY on creation; store it securely — you cannot retrieve it later.
    """

    key_prefix: Optional[str] = None
    """First 24 characters of the key, safe for audit/UI display."""

    name: Optional[str] = None
    """Human-readable name"""

    namespace_id: Optional[str] = None
    """Bound namespace objectId"""

    object_id: Optional[str] = FieldInfo(alias="objectId", default=None)
    """Parse APIKey objectId"""

    organization_id: Optional[str] = None
    """Bound organization objectId"""

    permissions: Optional[List[str]] = None
    """Granted permissions"""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class NamespaceCreateAPIKeyResponse(BaseModel):
    """Response for ``POST /v1/namespace/{namespace_id}/api-keys``."""

    code: Optional[int] = None
    """HTTP status code"""

    data: Optional[Data] = None
    """Public-facing API key data.

    The `key` field is populated **only** in the response of
    `POST /v1/namespace/{namespace_id}/api-keys` (the moment of creation). It is
    never returned by any read/list endpoint and is never logged. Use `key_prefix`
    (first 24 chars) to identify the key in audit trails and admin dashboards.
    """

    details: Optional[object] = None
    """Additional error details. NEVER contains the API key."""

    error: Optional[str] = None
    """Error message if failed"""

    status: Optional[str] = None
    """'success' or 'error'"""
