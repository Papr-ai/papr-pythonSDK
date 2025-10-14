#!/usr/bin/env python3
"""
Uninstall hook for Papr SDK.
Automatically cleans up ChromaDB data when package is uninstalled.
"""

import os


def uninstall_cleanup():
    """Clean up ChromaDB data during package uninstall"""
    try:
        # Import cleanup function
        from ._cleanup import cleanup_chromadb

        # Set environment variable to indicate uninstall cleanup
        os.environ["PAPR_UNINSTALL_CLEANUP"] = "true"

        # Run cleanup
        cleanup_chromadb()

        print("✅ Papr SDK uninstall cleanup completed")
        return True

    except Exception as e:
        print(f"⚠️  Papr SDK uninstall cleanup failed: {e}")
        print("ℹ️  You can manually clean up with: papr-cleanup")
        return False


if __name__ == "__main__":
    uninstall_cleanup()
