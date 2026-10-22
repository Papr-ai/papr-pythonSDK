"""Tests for papr_memory.lib._packs (schema pack helpers)."""

from typing import Any, Dict, List, Optional

import pytest

from papr_memory.lib import SchemaPacks, schema_packs, parse_pack_ref, build_memory_policy


class FakeClient:
    def __init__(self, responses: Dict[str, Any]) -> None:
        self.responses = responses
        self.calls: List[Dict[str, Any]] = []

    def get(self, path: str, *, cast_to: Any, options: Optional[Dict[str, Any]] = None) -> Any:
        self.calls.append({"method": "GET", "path": path, "options": options or {}, "cast_to": cast_to})
        return self.responses.get(f"GET {path}")

    def post(self, path: str, *, cast_to: Any, body: Any = None) -> Any:
        self.calls.append({"method": "POST", "path": path, "body": body, "cast_to": cast_to})
        return self.responses.get(f"POST {path}")


class TestParsePackRef:
    def test_with_and_without_range(self) -> None:
        assert parse_pack_ref("papr/fundraising@^1") == ("papr/fundraising", "^1")
        assert parse_pack_ref("papr/fundraising") == ("papr/fundraising", None)
        assert parse_pack_ref("papr/fundraising@latest") == ("papr/fundraising", None)

    @pytest.mark.parametrize("bad", ["fundraising", "Papr/Fund", "papr/fundraising@>=1", ""])
    def test_rejects_bad_refs(self, bad: str) -> None:
        with pytest.raises(ValueError, match="Invalid pack reference"):
            parse_pack_ref(bad)


class TestSchemaPacks:
    def test_factory(self) -> None:
        assert isinstance(schema_packs(FakeClient({})), SchemaPacks)

    def test_list(self) -> None:
        c = FakeClient({"GET /v1/schemas/packs": {"success": True, "data": [{"name": "papr/fundraising"}]}})
        assert schema_packs(c).list()[0]["name"] == "papr/fundraising"

    def test_get_passes_range_as_version_param(self) -> None:
        c = FakeClient({"GET /v1/schemas/packs/papr/fundraising": {"success": True, "data": {"version": "1.0.0"}}})
        schema_packs(c).get("papr/fundraising@^1")
        assert c.calls[0]["options"] == {"params": {"version": "^1"}}

    def test_install_body(self) -> None:
        c = FakeClient({"POST /v1/schemas/packs/install": {"success": True, "data": {"action": "created", "schema_id": "s1"}}})
        out = schema_packs(c).install("papr/fundraising@^1", dry_run=True)
        assert out["schema_id"] == "s1"
        assert c.calls[0]["body"] == {"pack": "papr/fundraising@^1", "allow_major": False, "dry_run": True}

    def test_install_needs_approval_is_returned_not_raised(self) -> None:
        c = FakeClient({"POST /v1/schemas/packs/install": {"success": False, "data": {"action": "needs_approval"}}})
        assert schema_packs(c).install("papr/fundraising@^2")["action"] == "needs_approval"

    def test_install_validates_ref_first(self) -> None:
        c = FakeClient({})
        with pytest.raises(ValueError):
            schema_packs(c).install("nope")
        assert c.calls == []

    def test_errors_raise_server_message(self) -> None:
        c = FakeClient({"GET /v1/schemas/packs": {"success": False, "error": "boom"}})
        with pytest.raises(RuntimeError, match="boom"):
            schema_packs(c).list()

    def test_diff_and_versions(self) -> None:
        c = FakeClient({
            "POST /v1/schemas/diff": {"success": True, "data": {"kind": "additive"}},
            "GET /v1/schemas/a%2Fb/versions": {"success": True, "data": []},
        })
        p = schema_packs(c)
        assert p.diff({}, {})["kind"] == "additive"
        assert p.versions("a/b") == []
        assert c.calls[1]["path"] == "/v1/schemas/a%2Fb/versions"


class TestBuildMemoryPolicyOmo:
    def test_passes_omo_fields(self) -> None:
        assert build_memory_policy(schema_id="s1", risk="sensitive", consent="explicit", acl={"read": ["namespace:n"]}) == {
            "schema_id": "s1", "risk": "sensitive", "consent": "explicit", "acl": {"read": ["namespace:n"]},
        }

    def test_unset_fields_omitted(self) -> None:
        assert build_memory_policy(mode="auto") == {"mode": "auto"}
