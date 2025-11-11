#!/usr/bin/env python3
"""
Test CoreML model with proper warm-up to achieve cached performance
"""

import os
import time
import sys
from dotenv import load_dotenv

load_dotenv()

# Ensure we're using the right model
os.environ['PAPR_ENABLE_COREML'] = 'true'
os.environ['PAPR_ONDEVICE_PROCESSING'] = 'true'
os.environ['PAPR_COREML_MODEL'] = '/Users/shawkatkabbara/Documents/GitHub/papr-pythonSDK/coreml/Qwen3-Embedding-4B-FP16-Final.mlpackage'

from papr_memory import Papr

print("🔧 Initializing Papr client with CoreML...")
client = Papr(
    x_api_key=os.environ.get("PAPR_MEMORY_API_KEY"),
    base_url=os.environ.get("PAPR_BASE_URL"),
    timeout=120.0
)

print("✅ Client initialized\n")

# Warm-up: Run 3 searches to ensure model is compiled and cached
print("🔥 Warming up CoreML model (3 warm-up searches)...")
warmup_queries = ["warmup 1", "warmup 2", "warmup 3"]

for i, query in enumerate(warmup_queries, 1):
    start = time.perf_counter()
    response = client.memory.search(
        query=query,
        max_memories=5,
        max_nodes=10,
        enable_agentic_graph=False,
        timeout=180.0
    )
    elapsed_ms = (time.perf_counter() - start) * 1000
    print(f"  Warm-up {i}: {elapsed_ms:.0f}ms")

print("\n" + "="*60)
print("📊 Running 10 test searches (model should be warm now)...")
print("="*60 + "\n")

test_queries = [
    "find my goals",
    "what are my tasks",
    "show customer feedback",
    "product roadmap",
    "engineering docs",
    "meeting notes",
    "project status",
    "technical specs",
    "user research",
    "performance metrics"
]

timings = []

for i, query in enumerate(test_queries, 1):
    start = time.perf_counter()

    response = client.memory.search(
        query=query,
        max_memories=5,
        max_nodes=10,
        enable_agentic_graph=False,
        timeout=180.0
    )

    elapsed_ms = (time.perf_counter() - start) * 1000
    timings.append(elapsed_ms)

    num_results = len(response.data.memories) if response and response.data else 0
    print(f"Search {i:2d}: {elapsed_ms:6.1f}ms - '{query}' ({num_results} results)")

print("\n" + "="*60)
print("📈 Performance Statistics:")
print("="*60)
print(f"Minimum:  {min(timings):.1f}ms")
print(f"Maximum:  {max(timings):.1f}ms")
print(f"Average:  {sum(timings)/len(timings):.1f}ms")
print(f"Median:   {sorted(timings)[len(timings)//2]:.1f}ms")

print("\n" + "="*60)
if min(timings) < 150:
    print("✅ SUCCESS: Achieving sub-150ms performance!")
    print(f"   Best time: {min(timings):.1f}ms")
elif min(timings) < 500:
    print("⚠️  MODERATE: Performance is better but not optimal")
    print(f"   Best time: {min(timings):.1f}ms (target: <150ms)")
else:
    print("❌ SLOW: Model not using cached/warm path")
    print(f"   Best time: {min(timings):.1f}ms (target: <150ms)")
print("="*60)
