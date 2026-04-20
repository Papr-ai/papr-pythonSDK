from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `papr_memory.resources` module.

    This is used so that we can lazily import `papr_memory.resources` only when
    needed *and* so that users can just import `papr_memory` and reference `papr_memory.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("papr_memory.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
