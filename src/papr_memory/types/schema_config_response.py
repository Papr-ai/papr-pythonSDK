# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SchemaConfigResponse"]


class SchemaConfigResponse(BaseModel):
    """Operational configuration for a frequency schema."""

    contrast_gamma: Optional[float] = None
    """Contrast enhancement gamma"""

    cross_encoder_model: Optional[str] = None
    """Cross-encoder reranking model"""

    cross_encoder_topk: Optional[int] = None
    """Number of candidates for cross-encoder reranking"""

    default_scoring_method: Optional[str] = None
    """Default scoring method for this schema"""

    dspy_model_path: Optional[str] = None
    """Path to DSPy-optimized extractor model (null = use direct LLM)"""

    enable_entailment_rerank: Optional[bool] = None
    """Enable entailment-gated reranking (EGR)"""

    llm_metadata_model: Optional[str] = None
    """LLM model for metadata extraction"""

    qdrant_topk: Optional[int] = None
    """Over-fetch count from Qdrant for reranking"""

    use_adaptive_weights: Optional[bool] = None
    """Enable query-adaptive frequency weights"""

    use_complex_interference: Optional[bool] = None
    """Enable complex interference scoring (PDCI, SFI)"""

    use_sparse_weights: Optional[bool] = None
    """Enable sparse frequency weights"""

    weight_mode: Optional[str] = None
    """Frequency weight mode (legacy_sparse, code_search_v2, hybrid_optimized_v2)"""
