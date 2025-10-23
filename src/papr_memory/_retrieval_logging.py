"""
Retrieval logging service for on-device tier0 search performance tracking.

This module provides logging functionality similar to the memory server's QueryLogService,
but optimized for the SDK's local processing capabilities.
"""

import os
import json
import time
import asyncio
from typing import Any, Dict, List, Optional
from datetime import datetime, timezone

from papr_memory._logging import get_logger

from ._parse_integration import parse_logging_service

logger = get_logger(__name__)


class RetrievalMetrics:
    """Metrics for tracking retrieval performance"""
    
    def __init__(self):
        self.query_start_time: Optional[float] = None
        self.embedding_start_time: Optional[float] = None
        self.embedding_end_time: Optional[float] = None
        self.chromadb_start_time: Optional[float] = None
        self.chromadb_end_time: Optional[float] = None
        self.total_end_time: Optional[float] = None
        
        # Performance metrics
        self.embedding_latency_ms: Optional[float] = None
        self.chromadb_latency_ms: Optional[float] = None
        self.total_latency_ms: Optional[float] = None
        
        # Search metrics
        self.query_text: Optional[str] = None
        self.num_results: int = 0
        self.embedding_dimensions: Optional[int] = None
        self.model_name: Optional[str] = None
        
        # System metrics
        self.device_type: Optional[str] = None
        self.memory_usage_mb: Optional[float] = None


class RetrievalLoggingService:
    """Service for logging on-device retrieval performance"""
    
    def __init__(self):
        self.log_file = os.environ.get("PAPR_LOG_FILE", None)
        self.log_level = os.environ.get("PAPR_LOG_LEVEL", "INFO").upper()
        self.enable_metrics = os.environ.get("PAPR_ENABLE_METRICS", "true").lower() in ("true", "1", "yes", "on")
        
    def start_query_timing(self, query: str) -> RetrievalMetrics:
        """Start timing a query and return metrics object"""
        if not self.enable_metrics:
            return RetrievalMetrics()
            
        metrics = RetrievalMetrics()
        metrics.query_start_time = time.time()
        metrics.query_text = query
        
        logger.info(f"🔍 Starting on-device search for: '{query[:50]}{'...' if len(query) > 50 else ''}'")
        return metrics
    
    def start_embedding_timing(self, metrics: RetrievalMetrics) -> None:
        """Start timing embedding generation"""
        if not self.enable_metrics or not metrics.query_start_time:
            return
            
        metrics.embedding_start_time = time.time()
        logger.debug("⏱️ Starting embedding generation...")
    
    def end_embedding_timing(self, metrics: RetrievalMetrics, embedding_dimensions: int, model_name: str) -> None:
        """End timing embedding generation"""
        if not self.enable_metrics or not metrics.embedding_start_time:
            return
            
        metrics.embedding_end_time = time.time()
        metrics.embedding_latency_ms = (metrics.embedding_end_time - metrics.embedding_start_time) * 1000
        metrics.embedding_dimensions = embedding_dimensions
        metrics.model_name = model_name
        
        logger.info(f"✅ Embedding generation completed in {metrics.embedding_latency_ms:.2f}ms (dim: {embedding_dimensions})")
    
    def start_chromadb_timing(self, metrics: RetrievalMetrics) -> None:
        """Start timing ChromaDB search"""
        if not self.enable_metrics or not metrics.embedding_end_time:
            return
            
        metrics.chromadb_start_time = time.time()
        logger.debug("🔍 Starting ChromaDB vector search...")
    
    def end_chromadb_timing(self, metrics: RetrievalMetrics, num_results: int) -> None:
        """End timing ChromaDB search"""
        if not self.enable_metrics or not metrics.chromadb_start_time:
            return
            
        metrics.chromadb_end_time = time.time()
        metrics.chromadb_latency_ms = (metrics.chromadb_end_time - metrics.chromadb_start_time) * 1000
        metrics.num_results = num_results
        
        logger.info(f"✅ ChromaDB search completed in {metrics.chromadb_latency_ms:.2f}ms ({num_results} results)")
    
    def end_query_timing(self, metrics: RetrievalMetrics, device_type: str = None) -> None:
        """End timing the entire query and log final metrics"""
        if not self.enable_metrics or not metrics.query_start_time:
            return
            
        metrics.total_end_time = time.time()
        metrics.total_latency_ms = (metrics.total_end_time - metrics.query_start_time) * 1000
        metrics.device_type = device_type or "unknown"
        
        # Log comprehensive metrics
        self._log_retrieval_metrics(metrics)
    
    def _log_retrieval_metrics(self, metrics: RetrievalMetrics) -> None:
        """Log comprehensive retrieval metrics"""
        try:
            # Create metrics summary
            metrics_summary = {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "query": metrics.query_text,
                "performance": {
                    "total_latency_ms": round(metrics.total_latency_ms, 2) if metrics.total_latency_ms else None,
                    "embedding_latency_ms": round(metrics.embedding_latency_ms, 2) if metrics.embedding_latency_ms else None,
                    "chromadb_latency_ms": round(metrics.chromadb_latency_ms, 2) if metrics.chromadb_latency_ms else None,
                },
                "search_results": {
                    "num_results": metrics.num_results,
                    "embedding_dimensions": metrics.embedding_dimensions,
                },
                "model_info": {
                    "model_name": metrics.model_name,
                    "device_type": metrics.device_type,
                },
                "system": {
                    "memory_usage_mb": metrics.memory_usage_mb,
                }
            }
            
            # Log to console with structured format
            logger.info("📊 On-Device Retrieval Metrics:")
            logger.info(f"   🔍 Query: '{metrics.query_text[:50]}{'...' if len(metrics.query_text) > 50 else ''}'")
            logger.info(f"   ⏱️  Total Latency: {metrics.total_latency_ms:.2f}ms")
            logger.info(f"   🧠 Embedding: {metrics.embedding_latency_ms:.2f}ms (dim: {metrics.embedding_dimensions})")
            logger.info(f"   🔍 ChromaDB: {metrics.chromadb_latency_ms:.2f}ms ({metrics.num_results} results)")
            logger.info(f"   🤖 Model: {metrics.model_name} on {metrics.device_type}")
            
            # Log to file if configured
            if self.log_file:
                self._write_metrics_to_file(metrics_summary)
                
        except Exception as e:
            logger.error(f"Error logging retrieval metrics: {e}")
    
    def _write_metrics_to_file(self, metrics_summary: Dict[str, Any]) -> None:
        """Write metrics to log file"""
        try:
            log_entry = {
                "type": "retrieval_metrics",
                "data": metrics_summary
            }
            
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(json.dumps(log_entry) + "\n")
                
        except Exception as e:
            logger.error(f"Error writing metrics to file: {e}")
    
    def log_performance_comparison(self, local_latency_ms: float, server_latency_ms: float = None) -> None:
        """Log performance comparison between local and server search"""
        if not self.enable_metrics:
            return
            
        improvement = None
        if server_latency_ms:
            improvement = ((server_latency_ms - local_latency_ms) / server_latency_ms) * 100
            logger.info(f"🚀 Performance Comparison:")
            logger.info(f"   📱 Local: {local_latency_ms:.2f}ms")
            logger.info(f"   ☁️  Server: {server_latency_ms:.2f}ms")
            logger.info(f"   ⚡ Improvement: {improvement:.1f}% faster")
        else:
            logger.info(f"📱 Local search completed in {local_latency_ms:.2f}ms")
    
    def log_model_loading_metrics(self, model_name: str, loading_time_ms: float, device: str) -> None:
        """Log model loading performance"""
        if not self.enable_metrics:
            return
            
        logger.info(f"🤖 Model Loading Metrics:")
        logger.info(f"   📦 Model: {model_name}")
        logger.info(f"   ⏱️  Loading Time: {loading_time_ms:.2f}ms")
        logger.info(f"   🖥️  Device: {device}")
    
    def log_chromadb_metrics(self, collection_name: str, num_documents: int, embedding_function: str) -> None:
        """Log ChromaDB collection metrics"""
        if not self.enable_metrics:
            return
            
        logger.info(f"🗄️  ChromaDB Collection Metrics:")
        logger.info(f"   📁 Collection: {collection_name}")
        logger.info(f"   📄 Documents: {num_documents}")
        logger.info(f"   🧠 Embedding Function: {embedding_function}")
    
    async def log_to_parse_server(
        self,
        metrics: RetrievalMetrics,
        user_id: str = None,
        workspace_id: str = None,
        session_id: str = None,
        post_id: str = None,
        user_message_id: str = None,
        assistant_message_id: str = None,
        goal_classification_scores: List[float] = None,
        use_case_classification_scores: List[float] = None,
        step_classification_scores: List[float] = None,
        related_goals: List[str] = None,
        related_use_cases: List[str] = None,
        related_steps: List[str] = None
    ) -> Optional[str]:
        """Log retrieval metrics to Parse Server QueryLog collection"""
        
        if not self.enable_metrics or not metrics.query_start_time:
            return None
        
        try:
            # Calculate token metrics (simplified estimation)
            query_embedding_tokens = len(metrics.query_text.split()) if metrics.query_text else 0
            retrieved_memory_tokens = metrics.num_results * 50  # Estimate 50 tokens per result
            
            # Log to Parse Server
            query_log_id = await parse_logging_service.log_retrieval_metrics(
                query=metrics.query_text,
                retrieval_latency_ms=metrics.total_latency_ms or 0,
                total_processing_time_ms=metrics.total_latency_ms or 0,
                query_embedding_tokens=query_embedding_tokens,
                retrieved_memory_tokens=retrieved_memory_tokens,
                user_id=user_id,
                workspace_id=workspace_id,
                session_id=session_id,
                post_id=post_id,
                user_message_id=user_message_id,
                assistant_message_id=assistant_message_id,
                goal_classification_scores=goal_classification_scores,
                use_case_classification_scores=use_case_classification_scores,
                step_classification_scores=step_classification_scores,
                related_goals=related_goals,
                related_use_cases=related_use_cases,
                related_steps=related_steps
            )
            
            if query_log_id:
                logger.info(f"📊 QueryLog saved to Parse Server: {query_log_id}")
            else:
                logger.warning("Failed to save QueryLog to Parse Server")
                
            return query_log_id
            
        except Exception as e:
            logger.error(f"Error logging to Parse Server: {e}")
            return None
    
    def log_to_parse_server_sync(
        self,
        metrics: RetrievalMetrics,
        user_id: str = None,
        workspace_id: str = None,
        session_id: str = None,
        post_id: str = None,
        user_message_id: str = None,
        assistant_message_id: str = None,
        goal_classification_scores: List[float] = None,
        use_case_classification_scores: List[float] = None,
        step_classification_scores: List[float] = None,
        related_goals: List[str] = None,
        related_use_cases: List[str] = None,
        related_steps: List[str] = None
    ) -> Optional[str]:
        """Synchronous wrapper for Parse Server logging"""
        try:
            # Run async function in event loop
            loop = asyncio.get_event_loop()
            if loop.is_running():
                # If we're already in an event loop, create a task
                task = asyncio.create_task(
                    self.log_to_parse_server(
                        metrics, user_id, workspace_id, session_id, post_id,
                        user_message_id, assistant_message_id, goal_classification_scores,
                        use_case_classification_scores, step_classification_scores,
                        related_goals, related_use_cases, related_steps
                    )
                )
                # Don't wait for completion to avoid blocking
                return None
            else:
                return loop.run_until_complete(
                    self.log_to_parse_server(
                        metrics, user_id, workspace_id, session_id, post_id,
                        user_message_id, assistant_message_id, goal_classification_scores,
                        use_case_classification_scores, step_classification_scores,
                        related_goals, related_use_cases, related_steps
                    )
                )
        except Exception as e:
            logger.error(f"Error in sync Parse Server logging: {e}")
            return None


# Global instance
retrieval_logging_service = RetrievalLoggingService()
