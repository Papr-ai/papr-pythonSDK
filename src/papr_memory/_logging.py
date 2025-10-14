"""
Logging utilities for the Papr Memory SDK.
"""

import os
import logging
from typing import Optional


def get_logger(name: str) -> logging.Logger:
    """Get a logger with appropriate configuration."""
    logger = logging.getLogger(name)

    # Set log level based on environment variable
    log_level = os.environ.get("PAPR_LOG_LEVEL", "INFO").upper()
    logger.setLevel(getattr(logging, log_level, logging.INFO))

    # Only add handler if not already configured
    if not logger.handlers:
        # Check if file logging is enabled
        log_file = os.environ.get("PAPR_LOG_FILE")

        if log_file:
            # Create file handler
            handler = logging.FileHandler(log_file)
        else:
            # Create console handler
            handler = logging.StreamHandler()

        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


def log_ondevice_status(logger: logging.Logger, enabled: bool, reason: Optional[str] = None):
    """Log on-device processing status."""
    if enabled:
        logger.info("On-device processing enabled")
    else:
        if reason:
            logger.info(f"On-device processing disabled: {reason}")
        else:
            logger.info("On-device processing disabled")


def log_chromadb_status(logger: logging.Logger, status: str, details: Optional[str] = None):
    """Log ChromaDB status messages."""
    if status == "initializing":
        logger.info("Initializing ChromaDB client")
    elif status == "initialized":
        logger.info("ChromaDB client initialized successfully")
    elif status == "collection_created":
        logger.info(f"ChromaDB collection created: {details}")
    elif status == "collection_exists":
        logger.info(f"Using existing ChromaDB collection: {details}")
    elif status == "error":
        logger.error(f"ChromaDB error: {details}")
    elif status == "not_available":
        logger.warning("ChromaDB not available - install with: pip install chromadb")


def log_embedding_status(logger: logging.Logger, status: str, details: Optional[str] = None):
    """Log embedding generation status."""
    if status == "generating":
        logger.info("Generating local embeddings")
    elif status == "generated":
        logger.info(f"Generated local embedding (dim: {details})")
    elif status == "failed":
        logger.error(f"Failed to generate local embedding: {details}")
    elif status == "skipped":
        logger.info("Local embedding generation skipped - using API-based search")
    elif status == "platform_old":
        logger.info("Platform detected as too old - skipping local embedding generation")


def log_tier0_status(logger: logging.Logger, status: str, count: Optional[int] = None, details: Optional[str] = None):
    """Log tier0 data processing status."""
    if status == "found":
        logger.info(f"Found {count} tier0 items in sync response")
    elif status == "using":
        logger.info(f"Using {count} tier0 items for search context enhancement")
    elif status == "stored":
        logger.info(f"Stored {count} new tier0 items in ChromaDB")
    elif status == "exists":
        logger.info(f"All {count} tier0 items already exist in ChromaDB")
    elif status == "none":
        logger.info("No tier0 data found in sync response")
    elif status == "error":
        logger.error(f"Error processing tier0 data: {details}")


def log_search_status(logger: logging.Logger, status: str, count: Optional[int] = None, details: Optional[str] = None):
    """Log search operation status."""
    if status == "local_search":
        logger.info(f"Using {count} tier0 items for search context enhancement")
    elif status == "api_only":
        logger.info("On-device processing disabled - using API-only search")
    elif status == "no_collection":
        logger.info("No ChromaDB collection available for local search")
    elif status == "results":
        logger.info(f"Found {count} memories and {details} graph nodes")
