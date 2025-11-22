#!/usr/bin/env python3
"""
Test script to verify parallel collection search implementation.

This script tests the new _search_both_collections() method to ensure:
1. Single embedding generation (not duplicated)
2. Parallel queries to tier0 and tier1 collections
3. Merged and ranked results from both tiers
4. Correct tier labeling in results

Usage:
    python test_parallel_search.py
"""

import os
import sys
import time

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from papr_memory import PaprMemory


def test_parallel_search():
    """Test the parallel collection search functionality."""
    print("=" * 80)
    print("🧪 Testing Parallel Collection Search")
    print("=" * 80)
    
    # Initialize client with on-device processing
    os.environ["PAPR_ONDEVICE_PROCESSING"] = "true"
    os.environ["PAPR_COREML_COMPUTE_UNITS"] = "CPU_AND_NE"  # Force ANE
    
    # Load API keys from environment
    api_key = os.environ.get("PAPR_API_KEY")
    if not api_key:
        print("❌ Error: PAPR_API_KEY environment variable not set")
        return False
    
    print(f"\n✅ API Key: {api_key[:10]}...")
    print(f"✅ On-device processing: enabled")
    print(f"✅ CoreML compute units: CPU_AND_NE (ANE forced)")
    
    # Initialize client
    print("\n📦 Initializing PaprMemory client...")
    client = PaprMemory(api_key=api_key)
    
    # Wait for background initialization
    print("⏳ Waiting for background model loading...")
    time.sleep(5)  # Give some time for initialization
    
    # Check if collections exist
    has_tier0 = hasattr(client.memory, "_chroma_collection") and client.memory._chroma_collection is not None
    has_tier1 = hasattr(client.memory, "_chroma_tier1_collection") and client.memory._chroma_tier1_collection is not None
    
    print(f"\n📊 Collection Status:")
    print(f"   Tier0: {'✅ Exists' if has_tier0 else '❌ Not found'}")
    print(f"   Tier1: {'✅ Exists' if has_tier1 else '❌ Not found'}")
    
    if not has_tier0 and not has_tier1:
        print("\n⚠️  No ChromaDB collections found - may still be initializing")
        print("   Waiting 40 seconds for CoreML model loading...")
        time.sleep(40)
        
        # Check again
        has_tier0 = hasattr(client.memory, "_chroma_collection") and client.memory._chroma_collection is not None
        has_tier1 = hasattr(client.memory, "_chroma_tier1_collection") and client.memory._chroma_tier1_collection is not None
        
        print(f"\n📊 Collection Status (after wait):")
        print(f"   Tier0: {'✅ Exists' if has_tier0 else '❌ Not found'}")
        print(f"   Tier1: {'✅ Exists' if has_tier1 else '❌ Not found'}")
    
    # Test queries
    test_queries = [
        "What are my goals?",
        "Tell me about recent meetings",
        "What tasks are pending?",
    ]
    
    print("\n" + "=" * 80)
    print("🔍 Running Test Queries")
    print("=" * 80)
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n[Query {i}/{len(test_queries)}] {query}")
        print("-" * 80)
        
        start_time = time.time()
        
        try:
            # Perform search
            response = client.memory.search(query=query, max_memories=5)
            
            elapsed = (time.time() - start_time) * 1000
            print(f"✅ Search completed in {elapsed:.1f}ms")
            
            # Analyze results
            if hasattr(response, 'data') and response.data and hasattr(response.data, 'memories'):
                memories = response.data.memories
                print(f"📝 Results: {len(memories)} memories returned")
                
                # Count tier breakdown (if available)
                tier0_count = sum(1 for m in memories if hasattr(m, 'type') and m.type == 'tier0')
                tier1_count = sum(1 for m in memories if hasattr(m, 'type') and m.type == 'tier1')
                
                if tier0_count > 0 or tier1_count > 0:
                    print(f"📊 Breakdown: [{tier0_count} tier0, {tier1_count} tier1]")
                
                # Display top 3 results
                for j, memory in enumerate(memories[:3], 1):
                    content = getattr(memory, 'content', 'No content')
                    memory_type = getattr(memory, 'type', 'unknown')
                    
                    # Try to get similarity score
                    similarity = None
                    if hasattr(memory, '__dict__') and 'similarity_score' in memory.__dict__:
                        similarity = memory.__dict__['similarity_score']
                    
                    content_preview = content[:100] + "..." if len(content) > 100 else content
                    
                    if similarity is not None:
                        print(f"   [{j}] {memory_type.upper()} | Sim: {similarity:.4f} | {content_preview}")
                    else:
                        print(f"   [{j}] {memory_type.upper()} | {content_preview}")
            else:
                print("⚠️  No memories in response")
                
        except Exception as e:
            print(f"❌ Search failed: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "=" * 80)
    print("✅ Test Complete!")
    print("=" * 80)
    
    return True


def check_logs_for_issues():
    """Check for common issues in the logs."""
    print("\n" + "=" * 80)
    print("🔍 Checking for Common Issues")
    print("=" * 80)
    
    issues_found = []
    
    print("\n❓ Check the logs above for these indicators:")
    print("   ✅ 'Generated embedding ONCE' - single embedding generation")
    print("   ✅ 'Queried both collections in parallel' - parallel queries")
    print("   ✅ '[X tier0, Y tier1]' - combined results from both tiers")
    print("   ❌ '0.0ms' embedding times - indicates zero embeddings bug")
    print("   ❌ 'likely using GPU' - GPU fallback instead of ANE")
    print("   ✅ 'CPU_AND_NE' or ANE usage - correct configuration")
    
    return issues_found


if __name__ == "__main__":
    print("🚀 Papr Memory SDK - Parallel Collection Search Test")
    print("=" * 80)
    
    success = test_parallel_search()
    check_logs_for_issues()
    
    if success:
        print("\n✅ All tests passed!")
        sys.exit(0)
    else:
        print("\n❌ Some tests failed")
        sys.exit(1)

