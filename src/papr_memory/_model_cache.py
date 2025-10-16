"""
Automatic CoreML model downloading from Hugging Face Hub.

This module handles automatic downloading and caching of CoreML models
from Hugging Face when users enable CoreML without having a local model.
"""
import os
import logging
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

# Default Hugging Face repo for pre-converted CoreML models
DEFAULT_COREML_REPO = "papr-ai/Qwen3-Embedding-4B-CoreML"
DEFAULT_VARIANT = "fp16"  # or "int8"


def get_model_cache_dir() -> Path:
    """Get the local cache directory for CoreML models."""
    # Use XDG_CACHE_HOME on Unix, LOCALAPPDATA on Windows
    if os.name == "posix":
        cache_home = Path(os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache"))
    else:
        cache_home = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local"))
    
    cache_dir = cache_home / "papr_memory" / "coreml"
    cache_dir.mkdir(parents=True, exist_ok=True)
    return cache_dir


def download_coreml_model(
    repo_id: str = DEFAULT_COREML_REPO,
    variant: str = DEFAULT_VARIANT,
    cache_dir: Optional[Path] = None,
) -> Path:
    """
    Download CoreML model from Hugging Face Hub.
    
    Args:
        repo_id: HuggingFace repo ID (e.g., "papr-ai/Qwen3-Embedding-4B-CoreML")
        variant: Model variant ("fp16" or "int8")
        cache_dir: Local cache directory (default: ~/.cache/papr_memory/coreml)
    
    Returns:
        Path to the downloaded .mlpackage directory
    
    Raises:
        ImportError: If huggingface_hub is not installed
        RuntimeError: If download fails
    """
    try:
        from huggingface_hub import snapshot_download
    except ImportError as e:
        raise ImportError(
            "huggingface_hub is required to auto-download CoreML models. "
            "Install it with: pip install huggingface_hub"
        ) from e
    
    if cache_dir is None:
        cache_dir = get_model_cache_dir()
    
    model_path = cache_dir / f"Qwen3-Embedding-4B-{variant.upper()}.mlpackage"
    
    # Check if already downloaded
    if model_path.exists():
        logger.info(f"Using cached CoreML model: {model_path}")
        return model_path
    
    logger.info(f"📥 Downloading CoreML model from {repo_id}/{variant}...")
    logger.info(f"   This is a one-time download (~7.5GB for FP16, ~4GB for INT8)")
    logger.info(f"   Model will be cached at: {cache_dir}")
    
    try:
        # Download from HuggingFace
        downloaded_path = snapshot_download(
            repo_id=repo_id,
            allow_patterns=[f"{variant}/*"],
            local_dir=cache_dir / "temp",
            local_dir_use_symlinks=False,
        )
        
        # Move to final location
        temp_model = Path(downloaded_path) / variant
        if temp_model.exists():
            import shutil
            shutil.move(str(temp_model), str(model_path))
            # Clean up temp directory
            shutil.rmtree(cache_dir / "temp", ignore_errors=True)
        
        logger.info(f"✅ CoreML model downloaded successfully: {model_path}")
        return model_path
        
    except Exception as e:
        logger.error(f"❌ Failed to download CoreML model: {e}")
        raise RuntimeError(
            f"Failed to download CoreML model from {repo_id}. "
            "You can manually convert the model using: "
            "python scripts/coreml_models/convert_qwen_coreml.py --hf Qwen/Qwen3-Embedding-4B --out ./coreml/model.mlpackage --fp16"
        ) from e


def resolve_coreml_model_path(specified_path: Optional[str] = None) -> str:
    """
    Resolve CoreML model path, downloading from HuggingFace if needed.
    
    Args:
        specified_path: User-specified path (from PAPR_COREML_MODEL env var)
    
    Returns:
        Path to CoreML model (either local or auto-downloaded)
    
    Priority:
        1. User-specified path (PAPR_COREML_MODEL)
        2. Auto-download from HuggingFace (if not found locally)
    """
    # If user specified a path, use it
    if specified_path and os.path.exists(specified_path):
        logger.info(f"Using user-specified CoreML model: {specified_path}")
        return specified_path
    
    # Try to auto-download from HuggingFace
    try:
        # Get variant preference from environment
        variant = os.environ.get("PAPR_COREML_VARIANT", DEFAULT_VARIANT).lower()
        if variant not in ["fp16", "int8"]:
            logger.warning(f"Invalid PAPR_COREML_VARIANT: {variant}, using fp16")
            variant = "fp16"
        
        model_path = download_coreml_model(variant=variant)
        return str(model_path)
        
    except Exception as e:
        logger.warning(f"Could not auto-download CoreML model: {e}")
        
        # Fallback: check common local paths
        common_paths = [
            "./coreml/Qwen3-Embedding-4B-FP16.mlpackage",
            "./coreml/Qwen3-Embedding-4B.mlpackage",
            "./coreml/model.mlpackage",
        ]
        
        for path in common_paths:
            if os.path.exists(path):
                logger.info(f"Using local CoreML model: {path}")
                return path
        
        raise FileNotFoundError(
            "CoreML model not found. Please either:\n"
            "1. Install huggingface_hub for auto-download: pip install huggingface_hub\n"
            "2. Manually convert: python scripts/coreml_models/convert_qwen_coreml.py "
            "--hf Qwen/Qwen3-Embedding-4B --out ./coreml/model.mlpackage --fp16\n"
            "3. Specify model path: export PAPR_COREML_MODEL=/path/to/model.mlpackage"
        )

