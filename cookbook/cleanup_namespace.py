#!/usr/bin/env python3
"""
Namespace Cleanup Script — Safely delete all memories in a specific namespace.
=============================================================================

SAFETY: This script REQUIRES an explicit namespace_id to prevent
accidental deletion of all organization memories.

Usage:
    python cleanup_namespace.py                    # uses PAPR_NAMESPACE_ID from .env
    python cleanup_namespace.py --namespace-id sG5cIelgeW
    python cleanup_namespace.py --dry-run          # preview only, no deletions
    python cleanup_namespace.py --skip-confirmation # skip "are you sure?" prompt

Environment:
    PAPR_MEMORY_API_KEY  – API key (MUST be scoped to the target namespace)
    PAPR_NAMESPACE_ID    – default namespace if --namespace-id not provided
"""

import os
import sys
import argparse
from dotenv import load_dotenv

load_dotenv()


def main():
    parser = argparse.ArgumentParser(description="Delete all memories in a Papr namespace")
    parser.add_argument("--namespace-id", default=os.environ.get("PAPR_NAMESPACE_ID"),
                        help="Namespace objectId (REQUIRED)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview what would be deleted without actually deleting")
    parser.add_argument("--skip-confirmation", action="store_true",
                        help="Skip the confirmation prompt")
    parser.add_argument("--delete-schema", action="store_true",
                        help="Also delete the schema (PAPR_SCHEMA_ID)")
    args = parser.parse_args()

    namespace_id = args.namespace_id
    api_key = os.environ.get("PAPR_MEMORY_API_KEY")

    # Safety checks
    if not namespace_id:
        print("ERROR: --namespace-id is REQUIRED (or set PAPR_NAMESPACE_ID in .env)")
        print("       This prevents accidental deletion of all org memories.")
        sys.exit(1)

    if not api_key:
        print("ERROR: PAPR_MEMORY_API_KEY not set")
        sys.exit(1)

    # Verify the API key is scoped to this namespace
    if f"-namespace-{namespace_id}-" not in api_key:
        print(f"WARNING: API key does not appear to be scoped to namespace '{namespace_id}'")
        print(f"         This could delete memories in a different namespace!")
        if not args.skip_confirmation:
            confirm = input("Continue anyway? (type 'yes' to confirm): ")
            if confirm.lower() != "yes":
                print("Aborted.")
                sys.exit(0)

    from papr_memory import Papr

    client = Papr(x_api_key=api_key)

    print(f"\n{'='*60}")
    print(f"NAMESPACE CLEANUP")
    print(f"{'='*60}")
    print(f"  Namespace ID : {namespace_id}")
    print(f"  API Key      : {api_key[:20]}...{api_key[-8:]}")
    print(f"  Dry run      : {args.dry_run}")
    print(f"  Del schema   : {args.delete_schema}")

    # Preview: search to see what exists
    print(f"\n[1] Checking existing memories...")
    try:
        search_resp = client.memory.search(
            query="security behavior",
            namespace_id=namespace_id,
        )
        count = len(search_resp.data.memories) if search_resp.data else 0
        print(f"  Found ~{count} memories in search results (may be more)")
    except Exception as e:
        print(f"  Could not search: {e}")
        count = -1

    if args.dry_run:
        print(f"\n[DRY RUN] Would delete all memories in namespace {namespace_id}")
        if args.delete_schema:
            schema_id = os.environ.get("PAPR_SCHEMA_ID")
            print(f"[DRY RUN] Would delete schema {schema_id}")
        print("Exiting without changes.")
        return

    # Confirmation
    if not args.skip_confirmation:
        print(f"\nWARNING: This will PERMANENTLY DELETE all memories in namespace '{namespace_id}'")
        confirm = input("Type the namespace ID to confirm: ")
        if confirm.strip() != namespace_id:
            print(f"Expected '{namespace_id}', got '{confirm}'. Aborted.")
            sys.exit(0)

    # Delete all memories
    print(f"\n[2] Deleting all memories in namespace {namespace_id}...")
    try:
        resp = client.memory.delete_all()
        print(f"  Response: {resp}")
        print(f"  All memories deleted.")
    except Exception as e:
        print(f"  Error: {e}")
        sys.exit(1)

    # Optionally delete schema
    if args.delete_schema:
        schema_id = os.environ.get("PAPR_SCHEMA_ID")
        if schema_id:
            print(f"\n[3] Deleting schema {schema_id}...")
            try:
                client.schemas.delete(schema_id)
                print(f"  Schema deleted.")
            except Exception as e:
                print(f"  Error deleting schema: {e}")
        else:
            print(f"\n[3] No PAPR_SCHEMA_ID set, skipping schema deletion")

    print(f"\n{'='*60}")
    print(f"CLEANUP COMPLETE")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
