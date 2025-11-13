"""
Resource checking utility for papr_memory SDK.

Automatically checks system resources and recommends whether to use
on-device CoreML processing or API backend based on available disk space,
RAM, and memory pressure.
"""

import shutil
import psutil
import os
import logging
from typing import Tuple


logger = logging.getLogger(__name__)


def get_disk_space_gb(path="/") -> float:
    """
    Get free disk space in GB for the given path.

    Args:
        path: Path to check (default: root "/" for macOS/Linux)

    Returns:
        float: Free space in GB
    """
    try:
        usage = shutil.disk_usage(path)
        return usage.free / (1024**3)
    except Exception as e:
        logger.debug(f"Could not get disk space: {e}")
        return 0


def get_available_ram_gb() -> Tuple[float, float]:
    """
    Get available RAM in GB.

    Returns:
        tuple: (available_gb: float, used_percent: float)
    """
    try:
        mem = psutil.virtual_memory()
        return mem.available / (1024**3), mem.percent
    except Exception as e:
        logger.debug(f"Could not get memory info: {e}")
        return 0, 100


def check_ondevice_resources(
    min_disk_gb: float = 30,
    min_ram_gb: float = 6,
    max_memory_pressure_percent: float = 85,
    verbose: bool = False
) -> Tuple[bool, str, dict]:
    """
    Check if system has enough resources for CoreML on-device processing.

    CoreML requires:
    - 30GB+ free disk space for ANE compilation artifacts
    - 6GB+ available RAM for model runtime
    - <85% memory pressure to avoid swapping

    Args:
        min_disk_gb: Minimum free disk space in GB (default: 30)
        min_ram_gb: Minimum available RAM in GB (default: 6)
        max_memory_pressure_percent: Maximum memory usage % (default: 85)
        verbose: Print detailed status (default: False)

    Returns:
        tuple: (
            should_use_ondevice: bool,
            reason: str,
            details: dict with disk_gb, ram_gb, memory_percent
        )
    """
    # Check disk space
    free_gb = get_disk_space_gb()
    disk_ok = free_gb >= min_disk_gb

    # Check available RAM
    available_gb, memory_percent = get_available_ram_gb()
    ram_ok = available_gb >= min_ram_gb

    # Check memory pressure
    pressure_ok = memory_percent <= max_memory_pressure_percent

    # Determine if we should use on-device
    all_ok = disk_ok and ram_ok and pressure_ok

    # Build detailed reason
    failures = []
    if not disk_ok:
        failures.append(f"disk space: {free_gb:.1f}GB free (need {min_disk_gb}GB+)")
    if not ram_ok:
        failures.append(f"RAM: {available_gb:.1f}GB available (need {min_ram_gb}GB+)")
    if not pressure_ok:
        failures.append(f"memory pressure: {memory_percent:.1f}% used (need <{max_memory_pressure_percent}%)")

    if all_ok:
        reason = f"Sufficient resources: {free_gb:.1f}GB disk, {available_gb:.1f}GB RAM, {memory_percent:.1f}% memory"
    else:
        reason = f"Insufficient resources: {', '.join(failures)}"

    details = {
        "disk_gb": free_gb,
        "ram_gb": available_gb,
        "memory_percent": memory_percent,
        "disk_ok": disk_ok,
        "ram_ok": ram_ok,
        "pressure_ok": pressure_ok
    }

    if verbose:
        logger.info("=" * 80)
        logger.info("Resource Check for CoreML On-Device Processing")
        logger.info("=" * 80)
        logger.info(f"{'✅' if disk_ok else '❌'} Disk Space: {free_gb:.1f}GB free (need {min_disk_gb}GB+)")
        logger.info(f"{'✅' if ram_ok else '❌'} Available RAM: {available_gb:.1f}GB (need {min_ram_gb}GB+)")
        logger.info(f"{'✅' if pressure_ok else '❌'} Memory Pressure: {memory_percent:.1f}% (need <{max_memory_pressure_percent}%)")
        logger.info("-" * 80)
        if all_ok:
            logger.info("✅ Recommendation: Enable on-device CoreML processing")
        else:
            logger.info("⚠️  Recommendation: Use API backend (insufficient resources)")
        logger.info(f"   {reason}")
        logger.info("=" * 80)

    return all_ok, reason, details


def auto_configure_processing_mode(
    respect_env_override: bool = True,
    verbose: bool = True
) -> Tuple[bool, str]:
    """
    Automatically configure PAPR_ONDEVICE_PROCESSING based on system resources.

    This function is called during SDK initialization if PAPR_AUTO_CONFIGURE is true.

    Args:
        respect_env_override: If True, respect explicit PAPR_ONDEVICE_PROCESSING setting
        verbose: Print decision to logs

    Returns:
        tuple: (using_ondevice: bool, reason: str)
    """
    # Check if user explicitly set on-device processing
    env_value = os.environ.get("PAPR_ONDEVICE_PROCESSING", "").lower()

    if respect_env_override and env_value in ("true", "1", "yes"):
        logger.info("Using on-device processing (explicitly enabled via PAPR_ONDEVICE_PROCESSING)")
        return True, "Explicitly enabled by user"

    if respect_env_override and env_value in ("false", "0", "no"):
        logger.info("Using API backend (explicitly disabled via PAPR_ONDEVICE_PROCESSING)")
        return False, "Explicitly disabled by user"

    # Auto-detect based on resources
    can_use_ondevice, reason, details = check_ondevice_resources(verbose=verbose)

    if can_use_ondevice:
        os.environ["PAPR_ONDEVICE_PROCESSING"] = "true"
        if verbose:
            logger.info("🚀 Auto-configured for CoreML on-device processing")
    else:
        os.environ["PAPR_ONDEVICE_PROCESSING"] = "false"
        if verbose:
            logger.warning(f"☁️  Auto-configured for API backend: {reason}")
            logger.warning("   To enable on-device processing:")
            if not details["disk_ok"]:
                logger.warning(f"   - Free up disk space (need 30GB+, have {details['disk_gb']:.1f}GB)")
            if not details["ram_ok"]:
                logger.warning(f"   - Close memory-intensive applications (need 6GB+, have {details['ram_gb']:.1f}GB available)")
            if not details["pressure_ok"]:
                logger.warning(f"   - Reduce memory pressure (currently {details['memory_percent']:.1f}%)")

    return can_use_ondevice, reason
