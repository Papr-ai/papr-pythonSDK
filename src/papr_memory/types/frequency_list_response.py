# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["FrequencyListResponse", "Schema", "SchemaConfig", "SchemaFrequency"]


class SchemaConfig(BaseModel):
    """Operational configuration"""

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


class SchemaFrequency(BaseModel):
    """Single frequency band definition."""

    frequency_hz: float
    """Frequency in Hz (brain-inspired band)"""

    name: str
    """Field name extracted at this frequency"""

    type: str
    """Field type: ENUM, FREE_TEXT, NUMERIC, DATE, MULTI_VALUE"""

    description: Optional[str] = None
    """Human-readable field description"""

    weight: Optional[float] = None
    """Default weight for this frequency band"""


class Schema(BaseModel):
    """Full frequency schema with fields and config."""

    config: SchemaConfig
    """Operational configuration"""

    domain: str
    """Domain (e.g. code_search, biomedical)"""

    frequencies: List[SchemaFrequency]
    """Frequency band definitions"""

    name: str
    """Schema name"""

    num_frequencies: int
    """Number of frequency bands"""

    schema_id: str
    """Unique schema ID (domain:name:version)"""

    version: str
    """Schema version"""

    description: Optional[str] = None
    """Human-readable description"""


class FrequencyListResponse(BaseModel):
    """Response for listing all frequency schemas."""

    schemas: List[Schema]

    total: int

    shortcuts: Optional[Dict[str, str]] = None
    """Shorthand aliases (e.g. 'cosqa' -> 'code_search:cosqa:2.0.0')"""

    success: Optional[bool] = None
