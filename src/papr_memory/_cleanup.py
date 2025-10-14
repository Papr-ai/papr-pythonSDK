#!/usr/bin/env python3
"""
ChromaDB cleanup utilities for Papr SDK.
"""

import os
import sys
import atexit
import shutil
from pathlib import Path


# Register cleanup on module import (for uninstall scenarios)
def _register_uninstall_cleanup():
    """Register cleanup function to run on Python exit"""

    def _cleanup_on_exit():
        # Only run if this is an uninstall scenario
        if os.environ.get("PAPR_UNINSTALL_CLEANUP", "false").lower() in ("true", "1", "yes", "on"):
            cleanup_chromadb()

    atexit.register(_cleanup_on_exit)


# Register the cleanup function
_register_uninstall_cleanup()


def cleanup_chromadb():
    """Clean up ChromaDB data directory"""
    print("🧹 Cleaning up Papr ChromaDB data...")

    # Get ChromaDB path from environment or use default
    chroma_path = os.environ.get("PAPR_CHROMADB_PATH", "./chroma_db")
    chroma_path = Path(chroma_path).resolve()

    if chroma_path.exists():
        try:
            shutil.rmtree(chroma_path)
            print(f"✅ Removed ChromaDB data directory: {chroma_path}")
        except Exception as e:
            print(f"❌ Failed to remove ChromaDB directory: {e}")
            return False
    else:
        print(f"ℹ️  ChromaDB directory not found: {chroma_path}")

    print("✅ ChromaDB cleanup completed")
    return True


def cleanup_all_papr_data():
    """Clean up all Papr-related data"""
    print("🧹 Cleaning up all Papr data...")

    # List of possible Papr data directories
    data_dirs = [
        "./chroma_db",
        "./papr_data",
        "./papr_cache",
        os.path.expanduser("~/.papr"),
        os.path.expanduser("~/.cache/papr"),
    ]

    cleaned_count = 0
    for data_dir in data_dirs:
        data_path = Path(data_dir).resolve()
        if data_path.exists():
            try:
                shutil.rmtree(data_path)
                print(f"✅ Removed: {data_path}")
                cleaned_count += 1
            except Exception as e:
                print(f"❌ Failed to remove {data_path}: {e}")

    if cleaned_count == 0:
        print("ℹ️  No Papr data directories found")
    else:
        print(f"✅ Cleaned up {cleaned_count} directories")

    return True


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--all":
        cleanup_all_papr_data()
    else:
        cleanup_chromadb()
