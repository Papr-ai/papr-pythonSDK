"""Schema packs: versioned, published schemas + policies that apps bind to.

Hand-written (lib/ is preserved by codegen). Uses the client's raw ``get`` /
``post`` so it works before the endpoints are in the OpenAPI spec.

Usage::

    from papr_memory import Papr
    from papr_memory.lib import schema_packs, build_memory_policy

    client = Papr(x_api_key=...)
    packs = schema_packs(client)
    result = packs.install("papr/fundraising@^1")
    client.memory.add(
        content="Met Scott Beechuk (Norwest) about the seed round",
        memory_policy=build_memory_policy(schema_id=result["schema_id"]),
    )
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Tuple, Optional
from urllib.parse import quote

_PACK_REF = re.compile(r"^[a-z0-9_-]+/[a-z0-9_-]+(@([\^~]?\d+(\.\d+){0,2}|latest))?$")


def parse_pack_ref(ref: str) -> Tuple[str, Optional[str]]:
    """``'papr/fundraising@^1'`` -> ``('papr/fundraising', '^1')``. No range means latest."""
    trimmed = (ref or "").strip()
    if not _PACK_REF.match(trimmed):
        raise ValueError(f"Invalid pack reference '{ref}' (expected scope/name@range, e.g. papr/fundraising@^1)")
    name, _, rng = trimmed.partition("@")
    return name, (None if rng in ("", "latest") else rng)


def _unwrap(res: Any) -> Any:
    if not isinstance(res, dict) or res.get("success") is False:
        raise RuntimeError((res or {}).get("error") if isinstance(res, dict) else "Schema pack request failed")
    return res.get("data")


class SchemaPacks:
    def __init__(self, client: Any) -> None:
        self._client = client

    def _get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        options: Dict[str, Any] = {"params": params} if params else {}
        return self._client.get(path, cast_to=object, options=options)

    def _post(self, path: str, body: Dict[str, Any]) -> Any:
        return self._client.post(path, cast_to=object, body=body)

    def list(self) -> List[Dict[str, Any]]:
        """Latest version of every published pack."""
        return _unwrap(self._get("/v1/schemas/packs"))

    def get(self, ref: str) -> Dict[str, Any]:
        """One pack, resolved by exact version or range. Includes the expanded schema."""
        name, rng = parse_pack_ref(ref)
        return _unwrap(self._get(f"/v1/schemas/packs/{name}", {"version": rng} if rng else None))

    def install(self, ref: str, *, allow_major: bool = False, dry_run: bool = False) -> Dict[str, Any]:
        """Install a pack into the API key's namespace, or upgrade it.

        A major upgrade returns ``{"action": "needs_approval", ...}`` unless ``allow_major``.
        """
        parse_pack_ref(ref)
        res = self._post("/v1/schemas/packs/install", {"pack": ref, "allow_major": allow_major, "dry_run": dry_run})
        if isinstance(res, dict) and res.get("success") is False and (res.get("data") or {}).get("action") == "needs_approval":
            return res["data"]
        return _unwrap(res)

    def diff(self, old: Dict[str, Any], new: Dict[str, Any]) -> Dict[str, Any]:
        """Classify a change (additive / policy / tightening / breaking) without writing."""
        return _unwrap(self._post("/v1/schemas/diff", {"old": old, "new": new}))

    def versions(self, schema_id: str) -> List[Dict[str, Any]]:
        """Previous versions of an installed schema, newest first."""
        return _unwrap(self._get(f"/v1/schemas/{quote(schema_id, safe='')}/versions"))


def schema_packs(client: Any) -> SchemaPacks:
    return SchemaPacks(client)
