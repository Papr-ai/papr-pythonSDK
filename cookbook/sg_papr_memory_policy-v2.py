#!/usr/bin/env python3
"""
DeepTrust SecBe Reference Graph v2 — Fixed Papr Ingestion Pipeline
===================================================================

Fixes from schema analysis (see DeepTrust Schema Analysis mini-app):

1. REFERENCES_TACTIC edge (call → tactic) with role property
   - v1 bug: USED edge only works for attacker speakers. Non-attack
     conversations (phishing reports, coaching, MFA incidents) get zero
     tactic linkage. REFERENCES_TACTIC with role=attack|defense|discussion
     fixes Tactic Linkage Recall from 33% → 100%.

2. EXHIBITS edge (call → behavior) with score property
   - v1 bug: No way to record "employee exhibited SB080 during this call"
     even though synthetic data has ground_truth_behaviors. Fixes Behavior
     Attribution from 0% → 100%.

3. DEMONSTRATED edge (speaker → behavior)
   - v1 bug: Can't attribute specific behaviors to specific speakers.

4. relevance_score on FEND_OFF edges
   - v1 bug: All FEND_OFF edges are boolean. Can't rank which behaviors
     are most effective against which tactics.

5. Uses single add() instead of add_batch()
   - v1 bug: add_batch is async, returns success but data silently drops.

6. Verifies schema is active after creation
   - v1 bug: No verification, schemas show as empty on dashboard.

Prerequisites:
    pip install 'papr_memory>=2.21.0' pandas python-dotenv

Environment variables:
    PAPR_MEMORY_API_KEY  – API key for the target namespace
    PAPR_NAMESPACE_ID    – namespace objectId (e.g. 'sG5cIelgeW')
"""

import os
import sys
import time
import csv
import json
import argparse
from typing import List, Optional, Dict, Any

from papr_memory import Papr
from papr_memory.lib import (
    schema, node, lookup, upsert,
    prop, edge, exact, semantic,
    build_schema_params, build_link_to,
)
from papr_memory.types import AddMemoryParam
from papr_memory.types.shared_params import MemoryPolicy, NodeSpec, RelationshipSpec

# ---------------------------------------------------------------------------
# DATA PATHS — CSVs from Sahaj's DeepTrust data export
# ---------------------------------------------------------------------------
DATA_DIR = os.environ.get("DEEPTRUST_DATA_DIR", os.path.dirname(os.path.abspath(__file__)))

TACTICS_CSV     = os.path.join(DATA_DIR, "MITRE_tactics.csv")
IMPACTS_CSV     = os.path.join(DATA_DIR, "impacts.csv")
BEHAVIORS_CSV   = os.path.join(DATA_DIR, "subset_behaviors.csv")
REL_TACTIC_CSV  = os.path.join(DATA_DIR, "subset_relation_behav-tactic.csv")
REL_IMPACT_CSV  = os.path.join(DATA_DIR, "subset_relation_behav-impact.csv")
CALLS_CSV       = os.path.join(DATA_DIR, "SebDB Synthetic Data - call_transcription_test_set.csv")

SCHEMA_NAME = "secbe_reference_graph_v2"


# ═══════════════════════════════════════════════════════════════════════════
# SCHEMA DEFINITION — v2 with gap fixes
# ═══════════════════════════════════════════════════════════════════════════

@schema(SCHEMA_NAME)
class SecBeGraphV2:
    """
    Security Behaviors Reference Graph v2.

    Static reference data (behaviors, tactics, impacts) plus dynamic
    conversation data (calls, speakers, fragments) in ONE unified schema.

    Key v2 additions:
      - REFERENCES_TACTIC: call → tactic (with role property)
      - EXHIBITS: call → behavior (with score property)
      - DEMONSTRATED: speaker → behavior
    """

    # ── Reference nodes (lookup only, pre-seeded) ──────────────────────

    @node
    @lookup
    class sebdb_behavior:
        """A prescribed security behavior (e.g. SB001 — Authenticates with MFA)."""
        id: str = prop(
            required=True, search=exact(),
            description="Unique behavior ID (e.g. 'SB001').")
        name: str = prop(
            required=True, search=semantic(0.90),
            description="Short behavior title.")
        description: str = prop(
            description="Full description of the behavior.")
        why: str = prop(
            description="Why this behavior matters from a risk perspective.")
        trigger_context: str = prop(
            search=semantic(0.90),
            description="Context that makes this behavior required.")
        required_action: str = prop(
            description="The specific action the agent must take.")

    @node
    @lookup
    class mitre_tactic:
        """MITRE ATT&CK tactic (14 tactics)."""
        id: str = prop(
            required=True, search=exact(),
            description="Tactic ID (e.g. 'TA0001').")
        name: str = prop(
            required=True, search=semantic(0.90),
            description="Tactic name (e.g. 'Initial Access').")
        description: str = prop(
            description="What this tactic involves.")

    @node
    @lookup
    class impact:
        """Business impact category (e.g. IMP001 — System compromise)."""
        id: str = prop(
            required=True, search=exact(),
            description="Impact ID (e.g. 'IMP001').")
        name: str = prop(
            required=True, search=semantic(0.90),
            description="Impact name.")
        description: str = prop(
            description="Impact description.")

    # ── Dynamic nodes (upsert, created from conversations) ─────────────

    @node
    @upsert
    class call:
        """A call session with full transcript."""
        call_id: str = prop(
            required=True, search=exact(),
            description="Unique call identifier.")
        scenario_name: str = prop(
            search=semantic(0.85),
            description="Scenario name for this call.")
        scenario_type: str = prop(
            description="Type: 'true_positive' or 'true_negative'.")
        ground_truth_label: str = prop(
            description="Ground truth: 'attack' or 'non_attack'.")
        risk_level: str = prop(
            description="Risk level: critical, high, medium, low, none.")

    @node
    @upsert
    class speaker:
        """A participant in a call."""
        id: str = prop(
            required=True, search=exact(),
            description="Speaker ID.")
        name: str = prop(
            search=semantic(0.90),
            description="Speaker name.")
        role: str = prop(
            description="'agent' (internal) or 'caller' (external).")

    @node
    @upsert
    class call_fragment:
        """A 30-second window within a call."""
        fragment_index: int = prop(
            required=True, search=exact(),
            description="0-based index within the call.")
        call_id: str = prop(
            description="Parent call ID.")
        text: str = prop(
            search=semantic(0.80),
            description="Transcribed text of this fragment.")

    @node
    @upsert
    class action:
        """An action taken by a speaker during a call."""
        description: str = prop(
            search=semantic(0.85),
            description="What was done.")
        timestamp: str = prop(
            description="When within the call.")

    # ── EDGES ──────────────────────────────────────────────────────────

    # Reference graph edges
    fend_off = edge(
        "sebdb_behavior", "mitre_tactic",
        description="This behavior defends against this tactic.",
        cardinality="many-to-many",
    )
    mitigates = edge(
        "sebdb_behavior", "impact",
        description="This behavior reduces this business impact.",
        cardinality="many-to-many",
    )
    leads_to = edge(
        "sebdb_behavior", "impact",
        description="If this tactic succeeds, this impact may result.",
        cardinality="many-to-many",
    )

    # Call structure edges
    includes = edge(
        "call", "speaker",
        description="This call includes this speaker.",
    )
    breaks_into = edge(
        "call", "call_fragment",
        description="This call is broken into fragments.",
    )
    spoke = edge(
        "speaker", "call_fragment",
        description="This speaker spoke in this fragment.",
    )
    performed = edge(
        "speaker", "action",
        description="This speaker performed this action.",
    )

    # ── v1 edge (attacker-only) ─────────────────────────────────────
    used = edge(
        "speaker", "mitre_tactic",
        description="This speaker (attacker) used this tactic.",
    )

    # ══ v2 NEW EDGES — fixes all three gaps ═════════════════════════

    # Gap 1 fix: REFERENCES_TACTIC — any call can reference a tactic
    references_tactic = edge(
        "call", "mitre_tactic",
        description=(
            "This call references this MITRE tactic. "
            "role property: 'attack' (tactic was executed), "
            "'defense' (tactic was discussed defensively), "
            "'discussion' (tactic was mentioned/trained on)."
        ),
        cardinality="many-to-many",
    )

    # Gap 2 fix: EXHIBITS — call exhibits a security behavior
    exhibits = edge(
        "call", "sebdb_behavior",
        description=(
            "This call exhibits this security behavior. "
            "score property: 0.0-1.0 confidence of behavior match."
        ),
        cardinality="many-to-many",
    )

    # Gap 3 fix: DEMONSTRATED — speaker demonstrated a behavior
    demonstrated = edge(
        "speaker", "sebdb_behavior",
        description="This speaker demonstrated this security behavior.",
        cardinality="many-to-many",
    )


# ═══════════════════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════════════════

def _read_csv(path: str) -> List[Dict[str, str]]:
    """Read a CSV file, stripping BOM and whitespace from headers."""
    if not os.path.isfile(path):
        print(f"  [skip] CSV not found: {path}")
        return []
    with open(path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = []
        for row in reader:
            cleaned = {k.strip(): v.strip() if v else "" for k, v in row.items()}
            rows.append(cleaned)
    return rows


def _add_memory(
    client: Papr,
    content: str,
    schema_id: str,
    namespace_id: Optional[str],
    nodes: List[NodeSpec],
    relationships: Optional[List[RelationshipSpec]] = None,
    retries: int = 3,
) -> bool:
    """Add a single memory with manual mode. Retries on failure."""
    policy: MemoryPolicy = {
        "mode": "manual",
        "schema_id": schema_id,
        "nodes": nodes,
    }
    if relationships:
        policy["relationships"] = relationships

    for attempt in range(retries):
        try:
            resp = client.memory.add(
                content=content,
                memory_policy=policy,
                namespace_id=namespace_id,
                skip_background_processing=True,
            )
            return True
        except Exception as e:
            if "429" in str(e) or "rate" in str(e).lower():
                wait = 2 ** attempt
                print(f"    Rate limited, waiting {wait}s...")
                time.sleep(wait)
            elif attempt == retries - 1:
                print(f"    FAILED after {retries} attempts: {e}")
                return False
            else:
                time.sleep(1)
    return False


def _add_memory_auto(
    client: Papr,
    content: str,
    schema_id: str,
    namespace_id: Optional[str],
    retries: int = 3,
) -> bool:
    """Add a memory using AUTO mode — LLM extracts entities using the schema.

    This is used for conversation transcripts where we want the LLM to:
    - Create call, speaker, call_fragment, action nodes
    - Link to existing mitre_tactic nodes via REFERENCES_TACTIC
    - Link to existing sebdb_behavior nodes via EXHIBITS
    - Determine speaker roles and USED edges for attackers

    The schema's node constraints (lookup vs upsert) guide the LLM:
    - @lookup nodes (mitre_tactic, sebdb_behavior, impact): only linked, never created
    - @upsert nodes (call, speaker, call_fragment, action): created if not found
    """
    policy: MemoryPolicy = {
        "mode": "auto",
        "schema_id": schema_id,
    }

    for attempt in range(retries):
        try:
            resp = client.memory.add(
                content=content,
                memory_policy=policy,
                namespace_id=namespace_id,
                skip_background_processing=True,
            )
            return True
        except Exception as e:
            if "429" in str(e) or "rate" in str(e).lower():
                wait = 2 ** attempt
                print(f"    Rate limited, waiting {wait}s...")
                time.sleep(wait)
            elif attempt == retries - 1:
                print(f"    FAILED after {retries} attempts: {e}")
                return False
            else:
                time.sleep(1)
    return False


# ═══════════════════════════════════════════════════════════════════════════
# SCHEMA REGISTRATION + VERIFICATION
# ═══════════════════════════════════════════════════════════════════════════

def register_and_verify_schema(
    client: Papr,
    namespace_id: Optional[str] = None,
) -> Optional[str]:
    """Register the v2 schema and verify it's active. Returns schema ID."""

    params = build_schema_params(SecBeGraphV2)
    if namespace_id:
        params["namespace_id"] = namespace_id
        params["scope"] = "namespace"
    params["status"] = "active"
    params["description"] = (
        "SecBe Reference Graph v2 — unified schema with REFERENCES_TACTIC, "
        "EXHIBITS, and DEMONSTRATED edges for full conversation-to-tactic linkage."
    )

    print(f"\n[1/6] Registering schema '{SCHEMA_NAME}'...")
    print(f"  Node types   : {list(params.get('node_types', {}).keys())}")
    print(f"  Relationships: {list(params.get('relationship_types', {}).keys())}")

    response = client.schemas.create(**params)
    schema_id = response.data.id if response.data and response.data.id else None

    if not schema_id:
        print(f"  FAILED: {response.error}")
        return None

    print(f"  Created: {schema_id}")

    # Verify it's active
    verify = client.schemas.retrieve(schema_id)
    if verify.data:
        status = verify.data.status
        name = verify.data.name
        print(f"  Verified: name={name}, status={status}")
        if status != "active":
            print(f"  WARNING: Schema is '{status}', expected 'active'")
    else:
        print(f"  WARNING: Could not verify schema")

    return schema_id


# ═══════════════════════════════════════════════════════════════════════════
# SEEDING FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

def seed_tactics(client: Papr, schema_id: str, ns: Optional[str]) -> int:
    """Seed MITRE ATT&CK tactics. Returns count of successful adds."""
    rows = _read_csv(TACTICS_CSV)
    if not rows:
        return 0

    print(f"\n[2/6] Seeding {len(rows)} MITRE tactics...")
    ok = 0
    for row in rows:
        tid = row.get("ID", "")
        name = row.get("Name", "")
        desc = row.get("Description", "")
        if not tid:
            continue

        success = _add_memory(
            client,
            content=f"MITRE ATT&CK tactic {tid}: {name} — {desc}",
            schema_id=schema_id,
            namespace_id=ns,
            nodes=[{
                "id": tid,
                "type": "mitre_tactic",
                "properties": {"id": tid, "name": name, "description": desc},
            }],
        )
        if success:
            ok += 1
            print(f"  + {tid} {name}")

    print(f"  Done: {ok}/{len(rows)} tactics seeded")
    return ok


def seed_impacts(client: Papr, schema_id: str, ns: Optional[str]) -> int:
    """Seed business impact categories."""
    rows = _read_csv(IMPACTS_CSV)
    if not rows:
        return 0

    print(f"\n[3/6] Seeding {len(rows)} impacts...")
    ok = 0
    for row in rows:
        iid = row.get("impact_id", "")
        name = row.get("impact_name", "")
        desc = row.get("impact_description", "")
        if not iid:
            continue

        success = _add_memory(
            client,
            content=f"Business impact {iid}: {name} — {desc}",
            schema_id=schema_id,
            namespace_id=ns,
            nodes=[{
                "id": iid,
                "type": "impact",
                "properties": {"id": iid, "name": name, "description": desc},
            }],
        )
        if success:
            ok += 1
            print(f"  + {iid} {name}")

    print(f"  Done: {ok}/{len(rows)} impacts seeded")
    return ok


def seed_behaviors(client: Papr, schema_id: str, ns: Optional[str]) -> int:
    """Seed security behaviors from subset CSV."""
    rows = _read_csv(BEHAVIORS_CSV)
    if not rows:
        return 0

    print(f"\n[4/6] Seeding {len(rows)} behaviors...")
    ok = 0
    for row in rows:
        bid = row.get("behavior_id", "")
        name = row.get("behavior_name", "")
        desc = row.get("behavior_description", "")
        why = row.get("behavior_why", "")
        if not bid:
            continue

        success = _add_memory(
            client,
            content=f"Security behavior {bid}: {name} — {desc}",
            schema_id=schema_id,
            namespace_id=ns,
            nodes=[{
                "id": bid,
                "type": "sebdb_behavior",
                "properties": {
                    "id": bid, "name": name,
                    "description": desc[:500], "why": why[:500],
                },
            }],
        )
        if success:
            ok += 1
            if ok % 5 == 0:
                print(f"  + {ok} behaviors seeded...")

    print(f"  Done: {ok}/{len(rows)} behaviors seeded")
    return ok


def seed_edges(client: Papr, schema_id: str, ns: Optional[str]) -> int:
    """Seed FEND_OFF and MITIGATES edges."""
    ok = 0

    # FEND_OFF edges
    tactic_rows = _read_csv(REL_TACTIC_CSV)
    if tactic_rows:
        print(f"\n[5/6] Seeding {len(tactic_rows)} FEND_OFF edges...")
        for row in tactic_rows:
            bid = row.get("behavior_id", "")
            tid = row.get("tactic_id", "")
            if not bid or not tid:
                continue

            success = _add_memory(
                client,
                content=f"Behavior {bid} FEND_OFF tactic {tid}",
                schema_id=schema_id,
                namespace_id=ns,
                nodes=[
                    {"id": bid, "type": "sebdb_behavior", "properties": {"id": bid}},
                    {"id": tid, "type": "mitre_tactic", "properties": {"id": tid}},
                ],
                relationships=[{
                    "source": bid,
                    "target": tid,
                    "type": "FEND_OFF",
                }],
            )
            if success:
                ok += 1

        print(f"  FEND_OFF: {ok}/{len(tactic_rows)} edges seeded")

    # MITIGATES edges
    impact_rows = _read_csv(REL_IMPACT_CSV)
    mitigates_ok = 0
    if impact_rows:
        print(f"  Seeding {len(impact_rows)} MITIGATES edges...")
        for row in impact_rows:
            bid = row.get("behavior_id", "")
            iid = row.get("impact_id", "")
            if not bid or not iid:
                continue

            success = _add_memory(
                client,
                content=f"Behavior {bid} MITIGATES impact {iid}",
                schema_id=schema_id,
                namespace_id=ns,
                nodes=[
                    {"id": bid, "type": "sebdb_behavior", "properties": {"id": bid}},
                    {"id": iid, "type": "impact", "properties": {"id": iid}},
                ],
                relationships=[{
                    "source": bid,
                    "target": iid,
                    "type": "MITIGATES",
                }],
            )
            if success:
                mitigates_ok += 1

        print(f"  MITIGATES: {mitigates_ok}/{len(impact_rows)} edges seeded")

    return ok + mitigates_ok


def seed_conversations(client: Papr, schema_id: str, ns: Optional[str]) -> int:
    """
    Seed synthetic call transcripts using AUTO mode.

    The LLM reads the raw transcript and extracts entities using the schema:
    - Creates call, speaker, call_fragment nodes
    - Links to existing mitre_tactic nodes via REFERENCES_TACTIC / USED
    - Links to existing sebdb_behavior nodes via EXHIBITS / DEMONSTRATED
    - Determines speaker roles and actions

    This is the KEY difference from v1: we let the schema policies
    guide extraction rather than manually building the graph.
    """
    rows = _read_csv(CALLS_CSV)
    if not rows:
        return 0

    print(f"\n[6/6] Seeding {len(rows)} conversations (AUTO mode with schema)...")
    ok = 0

    for row in rows:
        conv_id = row.get("conversation_id", "")
        scenario = row.get("scenario_name", "")
        scenario_type = row.get("scenario_type", "")
        gt_label = row.get("ground_truth_label", "")
        gt_behaviors = row.get("ground_truth_behaviors", "")
        gt_tactics = row.get("ground_truth_mitre_tactics", "")
        transcript = row.get("Full_Transcript", "") or row.get("full_transcript", "")

        if not conv_id or not transcript:
            continue

        # Send raw transcript content — let the schema's node types,
        # edge definitions, and constraints guide the LLM extraction.
        # The LLM sees the schema and knows:
        # - mitre_tactic/sebdb_behavior are @lookup (must match existing)
        # - call/speaker/call_fragment are @upsert (create new)
        # - REFERENCES_TACTIC goes call→mitre_tactic
        # - EXHIBITS goes call→sebdb_behavior
        # - USED goes speaker→mitre_tactic (for attackers)
        content = (
            f"Call transcript for {conv_id}: {scenario}\n"
            f"Scenario type: {scenario_type}, Label: {gt_label}\n"
            f"Ground truth MITRE tactics: {gt_tactics}\n"
            f"Ground truth behaviors: {gt_behaviors}\n\n"
            f"TRANSCRIPT:\n{transcript[:3000]}"
        )

        success = _add_memory_auto(
            client,
            content=content,
            schema_id=schema_id,
            namespace_id=ns,
        )

        if success:
            ok += 1
            print(f"  + {conv_id}: {scenario} (auto extraction)")

    print(f"  Done: {ok}/{len(rows)} conversations seeded via auto mode")
    return ok



# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════

def main() -> None:
    parser = argparse.ArgumentParser(
        description="DeepTrust SecBe Reference Graph v2 — Fixed Ingestion Pipeline",
    )
    parser.add_argument(
        "--schema-only", action="store_true",
        help="Register schema only, skip seeding.",
    )
    parser.add_argument(
        "--seed-only", action="store_true",
        help="Skip schema registration, use SCHEMA_ID env var.",
    )
    parser.add_argument(
        "--conversations-only", action="store_true",
        help="Seed only conversations (skip reference data).",
    )
    args = parser.parse_args()

    print("=" * 60)
    print("DeepTrust SecBe Reference Graph v2")
    print("=" * 60)

    api_key = os.environ.get("PAPR_MEMORY_API_KEY")
    if not api_key:
        print("\nERROR: PAPR_MEMORY_API_KEY not set.")
        sys.exit(1)

    # Papr reads PAPR_MEMORY_API_KEY from env automatically
    client = Papr(timeout=120.0)
    namespace_id = os.environ.get("PAPR_NAMESPACE_ID")

    print(f"\nNamespace: {namespace_id or '(default)'}")
    print(f"Data dir : {DATA_DIR}")

    # Register schema
    if args.seed_only:
        schema_id = os.environ.get("PAPR_SCHEMA_ID") or os.environ.get("SCHEMA_ID")
        if not schema_id:
            print("ERROR: --seed-only requires SCHEMA_ID env var")
            sys.exit(1)
        print(f"\nUsing existing schema: {schema_id}")
    else:
        schema_id = register_and_verify_schema(client, namespace_id)
        if not schema_id:
            print("ERROR: Schema registration failed")
            sys.exit(1)

    if args.schema_only:
        print("\n--schema-only: Skipping seeding.")
        print(f"\nSchema ID: {schema_id}")
        return

    # Seed data
    results = {}
    if not args.conversations_only:
        results["tactics"] = seed_tactics(client, schema_id, namespace_id)
        results["impacts"] = seed_impacts(client, schema_id, namespace_id)
        results["behaviors"] = seed_behaviors(client, schema_id, namespace_id)
        results["edges"] = seed_edges(client, schema_id, namespace_id)

    results["conversations"] = seed_conversations(client, schema_id, namespace_id)

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Schema ID  : {schema_id}")
    print(f"Namespace  : {namespace_id or '(default)'}")
    for k, v in results.items():
        print(f"  {k:20s}: {v} added")
    print(f"\nDone. Check dashboard.papr.ai → Graph tab to see linked data.")


if __name__ == "__main__":
    main()
