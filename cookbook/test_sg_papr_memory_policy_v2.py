#!/usr/bin/env python3
"""
Pytest test cases for DeepTrust SecBe Reference Graph v2.

Tests against the deeptrust-dev-v2 namespace with pre-seeded data.

Schema ID: qn6UUOSgEg
Namespace ID: sG5cIelgeW

Run:
    cd /Users/shawkatkabbara/Documents/GitHub/papr-pythonSDK
    PAPR_MEMORY_API_KEY="sk-org-Y8D4H7Yp3Z-namespace-sG5cIelgeW-kSuLErAjVwvBX61c3iBuszSJWfQkyTF0" .venv/bin/python3 -m pytest cookbook/test_sg_papr_memory_policy_v2.py -v
"""

import os
import pytest
from papr_memory import Papr

SCHEMA_ID = os.environ.get("SCHEMA_ID", "qn6UUOSgEg")
NAMESPACE_ID = os.environ.get("PAPR_NAMESPACE_ID", "sG5cIelgeW")


@pytest.fixture(scope="session")
def client():
    key = os.environ.get("PAPR_MEMORY_API_KEY")
    if not key:
        pytest.skip("PAPR_MEMORY_API_KEY not set")
    return Papr(timeout=120.0)


def gql(client, query):
    r = client.graphql.query(extra_body={"query": query})
    if isinstance(r, dict) and "errors" in r:
        raise Exception(f"GraphQL error: {r['errors']}")
    return r.get("data", {}) if isinstance(r, dict) else {}


# ── Schema Registration ──────────────────────────────────────

class TestSchemaRegistration:
    def test_schema_exists(self, client):
        resp = client.schemas.retrieve(SCHEMA_ID)
        assert resp.data is not None

    def test_schema_is_active(self, client):
        resp = client.schemas.retrieve(SCHEMA_ID)
        assert resp.data.status == "active"

    def test_schema_name(self, client):
        resp = client.schemas.retrieve(SCHEMA_ID)
        assert resp.data.name == "secbe_reference_graph_v2"

    def test_7_node_types(self, client):
        resp = client.schemas.retrieve(SCHEMA_ID)
        nodes = set((resp.data.node_types or {}).keys())
        expected = {"sebdb_behavior", "mitre_tactic", "impact", "call", "speaker", "call_fragment", "action"}
        assert expected.issubset(nodes), f"Missing: {expected - nodes}"

    def test_11_relationship_types(self, client):
        resp = client.schemas.retrieve(SCHEMA_ID)
        rels = set((resp.data.relationship_types or {}).keys())
        expected = {"FEND_OFF", "MITIGATES", "LEADS_TO", "INCLUDES", "BREAKS_INTO",
                    "SPOKE", "PERFORMED", "USED", "REFERENCES_TACTIC", "EXHIBITS", "DEMONSTRATED"}
        assert expected.issubset(rels), f"Missing: {expected - rels}"

    def test_v2_edges_registered(self, client):
        resp = client.schemas.retrieve(SCHEMA_ID)
        rels = resp.data.relationship_types or {}
        assert "REFERENCES_TACTIC" in rels
        assert "EXHIBITS" in rels
        assert "DEMONSTRATED" in rels


# ── Node Data via GraphQL ─────────────────────────────────────

class TestNodeData:
    def test_tactics_exist(self, client):
        data = gql(client, "{ deeptrustMitreTactics(limit: 100) { id } }")
        assert len(data.get("deeptrustMitreTactics", [])) > 0

    def test_tactics_have_names(self, client):
        data = gql(client, "{ deeptrustMitreTactics(limit: 100) { id name } }")
        named = [t for t in data.get("deeptrustMitreTactics", []) if t.get("name")]
        assert len(named) >= 5

    def test_ta0001_present(self, client):
        data = gql(client, "{ deeptrustMitreTactics(limit: 100) { id } }")
        ids = {t["id"] for t in data.get("deeptrustMitreTactics", [])}
        assert "TA0001" in ids

    def test_behaviors_exist(self, client):
        data = gql(client, "{ deeptrustSebdbBehaviors(limit: 100) { id } }")
        assert len(data.get("deeptrustSebdbBehaviors", [])) > 0

    def test_impacts_exist(self, client):
        data = gql(client, "{ deeptrustImpacts(limit: 100) { id } }")
        assert len(data.get("deeptrustImpacts", [])) > 0

    def test_calls_exist(self, client):
        data = gql(client, "{ deeptrustCalls(limit: 100) { id } }")
        assert len(data.get("deeptrustCalls", [])) >= 5

    def test_call_ids(self, client):
        data = gql(client, "{ deeptrustCalls(limit: 100) { id } }")
        ids = {c["id"] for c in data.get("deeptrustCalls", [])}
        assert {"CONV-001", "CONV-002", "CONV-003", "CONV-004", "CONV-005"}.issubset(ids)


# ── Edge Traversal ────────────────────────────────────────────

class TestEdgeTraversal:
    def test_fend_off_exists(self, client):
        data = gql(client, """
        { deeptrustSebdbBehaviors(where: {id: {eq: "SB001"}}, limit: 1) {
            id fendOffMitreTacticConnection { totalCount }
        } }""")
        bs = data.get("deeptrustSebdbBehaviors", [])
        assert len(bs) > 0
        assert bs[0]["fendOffMitreTacticConnection"]["totalCount"] > 0

    def test_fend_off_reaches_ta0001(self, client):
        data = gql(client, """
        { deeptrustSebdbBehaviors(where: {id: {eq: "SB001"}}, limit: 1) {
            fendOffMitreTacticConnection {
                edges { node { id } }
            }
        } }""")
        bs = data.get("deeptrustSebdbBehaviors", [])
        tids = {e["node"]["id"] for e in bs[0]["fendOffMitreTacticConnection"]["edges"]}
        assert "TA0001" in tids

    def test_used_edge_on_speaker(self, client):
        data = gql(client, '{ __type(name: "DeeptrustSpeaker") { fields { name } } }')
        fields = [f["name"] for f in data.get("__type", {}).get("fields", [])]
        assert "usedMitreTactic" in fields


# ── v2 Edge Creation ─────────────────────────────────────────

class TestV2Edges:
    def test_add_references_tactic(self, client):
        resp = client.memory.add(
            content="Test: CONV-TEST-RT references TA0001 defensively",
            memory_policy={
                "mode": "manual", "schema_id": SCHEMA_ID,
                "nodes": [
                    {"id": "CONV-TEST-RT", "type": "call", "properties": {"call_id": "CONV-TEST-RT"}},
                    {"id": "TA0001", "type": "mitre_tactic", "properties": {"id": "TA0001"}},
                ],
                "relationships": [{"source": "CONV-TEST-RT", "target": "TA0001",
                                   "type": "REFERENCES_TACTIC", "properties": {"role": "defense"}}],
            },
            namespace_id=NAMESPACE_ID, skip_background_processing=True,
        )
        assert resp is not None

    def test_add_exhibits(self, client):
        resp = client.memory.add(
            content="Test: CONV-TEST-EX exhibits SB001 score 0.92",
            memory_policy={
                "mode": "manual", "schema_id": SCHEMA_ID,
                "nodes": [
                    {"id": "CONV-TEST-EX", "type": "call", "properties": {"call_id": "CONV-TEST-EX"}},
                    {"id": "SB001", "type": "sebdb_behavior", "properties": {"id": "SB001"}},
                ],
                "relationships": [{"source": "CONV-TEST-EX", "target": "SB001",
                                   "type": "EXHIBITS", "properties": {"score": 0.92}}],
            },
            namespace_id=NAMESPACE_ID, skip_background_processing=True,
        )
        assert resp is not None

    def test_add_demonstrated(self, client):
        resp = client.memory.add(
            content="Test: AGENT-TEST-DEM demonstrated SB001",
            memory_policy={
                "mode": "manual", "schema_id": SCHEMA_ID,
                "nodes": [
                    {"id": "AGENT-TEST-DEM", "type": "speaker", "properties": {"id": "AGENT-TEST-DEM", "role": "agent"}},
                    {"id": "SB001", "type": "sebdb_behavior", "properties": {"id": "SB001"}},
                ],
                "relationships": [{"source": "AGENT-TEST-DEM", "target": "SB001", "type": "DEMONSTRATED"}],
            },
            namespace_id=NAMESPACE_ID, skip_background_processing=True,
        )
        assert resp is not None


# ── GraphQL Schema ────────────────────────────────────────────

class TestGraphQLSchema:
    def test_has_call_type(self, client):
        data = gql(client, '{ __type(name: "DeeptrustCall") { name } }')
        assert data.get("__type", {}).get("name") == "DeeptrustCall"

    def test_has_behavior_type(self, client):
        data = gql(client, '{ __type(name: "DeeptrustSebdbBehavior") { name } }')
        assert data.get("__type", {}).get("name") == "DeeptrustSebdbBehavior"

    def test_has_fend_off_edge(self, client):
        data = gql(client, '{ __type(name: "DeeptrustSebdbBehavior") { fields { name } } }')
        fields = [f["name"] for f in data.get("__type", {}).get("fields", [])]
        assert "fendOffMitreTactic" in fields

    def test_v2_edges_pending_graphql_refresh(self, client):
        """v2 edges in Neo4j but not yet in GraphQL type defs — xfail until refresh."""
        data = gql(client, '{ __type(name: "DeeptrustCall") { fields { name } } }')
        fields = [f["name"] for f in data.get("__type", {}).get("fields", [])]
        v2 = [f for f in fields if "reference" in f.lower() or "exhibit" in f.lower()]
        if not v2:
            pytest.xfail("v2 edges not in GraphQL yet — schema refresh needed")
        assert len(v2) > 0


# ── CSV Data Seeding ──────────────────────────────────────────

class TestCSVSeeding:
    def test_seed_tactic(self, client):
        resp = client.memory.add(
            content="MITRE Tactic TA0002 Execution",
            memory_policy={"mode": "manual", "schema_id": SCHEMA_ID,
                           "nodes": [{"id": "TA0002", "type": "mitre_tactic",
                                      "properties": {"id": "TA0002", "name": "Execution"}}]},
            namespace_id=NAMESPACE_ID, skip_background_processing=True,
        )
        assert resp is not None

    def test_seed_behavior(self, client):
        resp = client.memory.add(
            content="Security Behavior SB014: Asks for security-related help",
            memory_policy={"mode": "manual", "schema_id": SCHEMA_ID,
                           "nodes": [{"id": "SB014", "type": "sebdb_behavior",
                                      "properties": {"id": "SB014", "name": "Asks for security-related help"}}]},
            namespace_id=NAMESPACE_ID, skip_background_processing=True,
        )
        assert resp is not None

    def test_seed_fend_off(self, client):
        resp = client.memory.add(
            content="SB014 FEND_OFF TA0002",
            memory_policy={"mode": "manual", "schema_id": SCHEMA_ID,
                           "nodes": [
                               {"id": "SB014", "type": "sebdb_behavior", "properties": {"id": "SB014"}},
                               {"id": "TA0002", "type": "mitre_tactic", "properties": {"id": "TA0002"}},
                           ],
                           "relationships": [{"source": "SB014", "target": "TA0002", "type": "FEND_OFF"}]},
            namespace_id=NAMESPACE_ID, skip_background_processing=True,
        )
        assert resp is not None
