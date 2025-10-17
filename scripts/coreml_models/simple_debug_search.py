#!/usr/bin/env python3
"""
Simple debug script for searching memories with the Papr Memory SDK.

This script shows the minimal setup needed to debug memory searches.
Demonstrates on-device processing control with PAPR_ONDEVICE_PROCESSING environment variable.
"""

import os
from dotenv import load_dotenv
from papr_memory import Papr

# Load environment variables
load_dotenv()

def main():
    # Setup logging
    import logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Check if on-device processing is enabled
    ondevice_processing = os.environ.get("PAPR_ONDEVICE_PROCESSING", "false").lower() in ("true", "1", "yes", "on")
    print(f"🔧 On-device processing: {'ENABLED' if ondevice_processing else 'DISABLED'}")
    print(f"📊 Environment variable PAPR_ONDEVICE_PROCESSING: {os.environ.get('PAPR_ONDEVICE_PROCESSING', 'not set (defaults to false)')}")
    print("=" * 60)
    
    # Set log level via environment variable
    os.environ["PAPR_LOG_LEVEL"] = "INFO"
    
    # Create client with increased timeout
    client = Papr(
        x_api_key=os.environ.get("PAPR_MEMORY_API_KEY"),
        timeout=120.0  # Increase timeout to 120 seconds
    )
    
    print("🔍 Searching memories with debug logging enabled...")
    
    try:
        # Search with automatic internal sync_tiers integration
        print("📡 Testing search with automatic sync_tiers integration...")
        response = client.memory.search(
            query="Find latest memories",
            max_memories=10,
            max_nodes=10,
            enable_agentic_graph=False,
            timeout=180.0  # 3 minutes timeout for search
        )

        if response and response.data:
            print(f"✅ Found {len(response.data.memories)} memories")
            print(f"🔗 Found {len(response.data.nodes)} graph nodes")
            
            # Show first few results
            for i, memory in enumerate(response.data.memories[:3], 1):
                print(f"\n{i}. {memory.content[:100]}...")
        else:
            print("❌ No response data received")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
