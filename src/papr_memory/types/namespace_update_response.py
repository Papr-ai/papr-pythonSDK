# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["NamespaceUpdateResponse", "Data"]


class Data(BaseModel):
    """Public-facing namespace data returned in API responses."""

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)
    """Creation timestamp"""

    environment_type: Optional[str] = None
    """Environment type"""

    is_active: Optional[bool] = None
    """Whether namespace is active"""

    memories_count: Optional[int] = FieldInfo(alias="memoriesCount", default=None)
    """Total memories"""

    name: Optional[str] = None
    """Namespace name"""

    object_id: Optional[str] = FieldInfo(alias="objectId", default=None)
    """Parse objectId"""

    organization_id: Optional[str] = None
    """Owning organization ID"""

    rate_limits: Optional[Dict[str, Optional[int]]] = None
    """Rate limits"""

    storage_count: Optional[int] = FieldInfo(alias="storageCount", default=None)
    """Total storage items"""

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)
    """Last update timestamp"""

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


class NamespaceUpdateResponse(BaseModel):
    """Response for single-namespace operations (create, get, update)."""

    code: Optional[int] = None
    """HTTP status code"""

    data: Optional[Data] = None
    """Public-facing namespace data returned in API responses."""

    details: Optional[object] = None
    """Additional error details or context"""

    error: Optional[str] = None
    """Error message if failed"""

    status: Optional[str] = None
    """'success' or 'error'"""
