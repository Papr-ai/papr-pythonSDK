#!/usr/bin/env python3
"""
Measure latency for client.memory.search with optional warm-up.

Reads credentials and flags from .env and environment.
"""

import os
import time
import logging
from dotenv import load_dotenv
from papr_memory import Papr


def main() -> None:
    load_dotenv()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Ensure SDK logs are visible
    os.environ.setdefault("PAPR_LOG_LEVEL", "INFO")

    ondevice_processing = os.environ.get("PAPR_ONDEVICE_PROCESSING", "false").lower() in (
        "true",
        "1",
        "yes",
        "on",
    )
    print(f"🔧 On-device processing: {'ENABLED' if ondevice_processing else 'DISABLED'}")

    api_key = os.environ.get("PAPR_MEMORY_API_KEY")
    if not api_key:
        raise RuntimeError("PAPR_MEMORY_API_KEY is not set. Add it to .env or your environment.")

    client = Papr(
        x_api_key=api_key,
        timeout=120.0,
    )

    # Optional warm-up to exclude model load/prep from measured latency
    try:
        client.memory.search(
            query="warmup",
            max_memories=10,
            max_nodes=10,
            enable_agentic_graph=False,
            timeout=60.0,
        )
    except Exception as e:  # pragma: no cover - best-effort warmup
        logging.warning("Warm-up search failed: %s", e)

    t0 = time.perf_counter()
    resp = client.memory.search(
        query="Find latest memories",
        max_memories=10,
        max_nodes=10,
        enable_agentic_graph=False,
        timeout=180.0,
    )
    lat_ms = (time.perf_counter() - t0) * 1000
    print(f"search latency: {lat_ms:.1f} ms")

    data = getattr(resp, "data", None)
    if data is not None and getattr(data, "memories", None) is not None:
        num_memories = len(data.memories)
        num_nodes = len(data.nodes)
        print(f"✅ Found {num_memories} memories, {num_nodes} nodes")
    else:
        # Print basic error/status info to aid debugging without raising
        status = getattr(resp, "status", None)
        error = getattr(resp, "error", None)
        print(f"ℹ️  No data in response (status={status}, error={error})")


if __name__ == "__main__":
    main()


