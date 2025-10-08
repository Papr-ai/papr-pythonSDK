# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import (
    MemoryType,
    memory_add_params,
    memory_delete_params,
    memory_search_params,
    memory_update_params,
    memory_add_batch_params,
    memory_delete_all_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.search_response import SearchResponse
from ..types.add_memory_param import AddMemoryParam
from ..types.context_item_param import ContextItemParam
from ..types.add_memory_response import AddMemoryResponse
from ..types.batch_memory_response import BatchMemoryResponse
from ..types.memory_metadata_param import MemoryMetadataParam
from ..types.memory_delete_response import MemoryDeleteResponse
from ..types.memory_update_response import MemoryUpdateResponse
from ..types.relationship_item_param import RelationshipItemParam
from ..types.sync_tiers_response import SyncTiersResponse
from ..types.sync_tiers_params import SyncTiersParams

__all__ = ["MemoryResource", "AsyncMemoryResource"]


class MemoryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MemoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return MemoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MemoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return MemoryResourceWithStreamingResponse(self)

    def update(
        self,
        memory_id: str,
        *,
        content: Optional[str] | NotGiven = NOT_GIVEN,
        context: Optional[Iterable[ContextItemParam]] | NotGiven = NOT_GIVEN,
        metadata: Optional[MemoryMetadataParam] | NotGiven = NOT_GIVEN,
        relationships_json: Optional[Iterable[RelationshipItemParam]] | NotGiven = NOT_GIVEN,
        type: Optional[MemoryType] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemoryUpdateResponse:
        """
        Update an existing memory item by ID.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - Content-Type: application/json
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

            The API validates content size against MAX_CONTENT_LENGTH environment variable (defaults to 15000 bytes).

        Args:
          content: The new content of the memory item

          context: Updated context for the memory item

          metadata: Metadata for memory request

          relationships_json: Updated relationships for Graph DB (neo4J)

          type: Valid memory types

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not memory_id:
            raise ValueError(f"Expected a non-empty value for `memory_id` but received {memory_id!r}")
        return self._put(
            f"/v1/memory/{memory_id}",
            body=maybe_transform(
                {
                    "content": content,
                    "context": context,
                    "metadata": metadata,
                    "relationships_json": relationships_json,
                    "type": type,
                },
                memory_update_params.MemoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryUpdateResponse,
        )

    def delete(
        self,
        memory_id: str,
        *,
        skip_parse: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemoryDeleteResponse:
        """
        Delete a memory item by ID.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

        Args:
          skip_parse: Skip Parse Server deletion

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not memory_id:
            raise ValueError(f"Expected a non-empty value for `memory_id` but received {memory_id!r}")
        return self._delete(
            f"/v1/memory/{memory_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"skip_parse": skip_parse}, memory_delete_params.MemoryDeleteParams),
            ),
            cast_to=MemoryDeleteResponse,
        )

    def add(
        self,
        *,
        content: str,
        type: MemoryType,
        skip_background_processing: bool | NotGiven = NOT_GIVEN,
        context: Optional[Iterable[ContextItemParam]] | NotGiven = NOT_GIVEN,
        metadata: Optional[MemoryMetadataParam] | NotGiven = NOT_GIVEN,
        relationships_json: Optional[Iterable[RelationshipItemParam]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddMemoryResponse:
        """
        Add a new memory item to the system with size validation and background
        processing.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - Content-Type: application/json
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

            The API validates content size against MAX_CONTENT_LENGTH environment variable (defaults to 15000 bytes).

        Args:
          content: The content of the memory item you want to add to memory

          type: Valid memory types

          skip_background_processing: If True, skips adding background tasks for processing

          context: Context can be conversation history or any relevant context for a memory item

          metadata: Metadata for memory request

          relationships_json: Array of relationships that we can use in Graph DB (neo4J)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/memory",
            body=maybe_transform(
                {
                    "content": content,
                    "type": type,
                    "context": context,
                    "metadata": metadata,
                    "relationships_json": relationships_json,
                },
                memory_add_params.MemoryAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"skip_background_processing": skip_background_processing}, memory_add_params.MemoryAddParams
                ),
            ),
            cast_to=AddMemoryResponse,
        )

    def add_batch(
        self,
        *,
        memories: Iterable[AddMemoryParam],
        skip_background_processing: bool | NotGiven = NOT_GIVEN,
        batch_size: Optional[int] | NotGiven = NOT_GIVEN,
        external_user_id: Optional[str] | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_secret: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_url: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchMemoryResponse:
        """
        Add multiple memory items in a batch with size validation and background
        processing.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - Content-Type: application/json
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

            The API validates individual memory content size against MAX_CONTENT_LENGTH environment variable (defaults to 15000 bytes).

        Args:
          memories: List of memory items to add in batch

          skip_background_processing: If True, skips adding background tasks for processing

          batch_size: Number of items to process in parallel

          external_user_id: External user ID for all memories in the batch. If provided and user_id is not,
              will be resolved to internal user ID.

          user_id: Internal user ID for all memories in the batch. If not provided, developer's
              user ID will be used.

          webhook_secret: Optional secret key for webhook authentication. If provided, will be included in
              the webhook request headers as 'X-Webhook-Secret'.

          webhook_url: Optional webhook URL to notify when batch processing is complete. The webhook
              will receive a POST request with batch completion details.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/memory/batch",
            body=maybe_transform(
                {
                    "memories": memories,
                    "batch_size": batch_size,
                    "external_user_id": external_user_id,
                    "user_id": user_id,
                    "webhook_secret": webhook_secret,
                    "webhook_url": webhook_url,
                },
                memory_add_batch_params.MemoryAddBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"skip_background_processing": skip_background_processing},
                    memory_add_batch_params.MemoryAddBatchParams,
                ),
            ),
            cast_to=BatchMemoryResponse,
        )

    def delete_all(
        self,
        *,
        external_user_id: Optional[str] | NotGiven = NOT_GIVEN,
        skip_parse: bool | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchMemoryResponse:
        """
        Delete all memory items for a user.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **User Resolution**:
            - If only API key is provided: deletes memories for the developer
            - If user_id or external_user_id is provided: resolves and deletes memories for that user
            - Uses the same user resolution logic as other endpoints

            **Required Headers**:
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

            **WARNING**: This operation cannot be undone. All memories for the resolved user will be permanently deleted.

        Args:
          external_user_id: Optional external user ID to resolve and delete memories for

          skip_parse: Skip Parse Server deletion

          user_id: Optional user ID to delete memories for (if not provided, uses authenticated
              user)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/v1/memory/all",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "external_user_id": external_user_id,
                        "skip_parse": skip_parse,
                        "user_id": user_id,
                    },
                    memory_delete_all_params.MemoryDeleteAllParams,
                ),
            ),
            cast_to=BatchMemoryResponse,
        )

    def sync_tiers(
        self,
        *,
        include_embeddings: bool | NotGiven = NOT_GIVEN,
        embed_limit: int | NotGiven = NOT_GIVEN,
        max_tier0: int | NotGiven = NOT_GIVEN,
        max_tier1: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncTiersResponse:
        """
        Get sync tiers for memory synchronization.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')
            - Accept-Encoding: gzip (recommended)

        Args:
          include_embeddings: Whether to include embeddings in the response

          embed_limit: Limit for embeddings

          max_tier0: Maximum number of tier 0 items

          max_tier1: Maximum number of tier 1 items

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Accept-Encoding": "gzip"}), **(extra_headers or {})}
        return self._post(
            "/v1/sync/tiers",
            body=maybe_transform(
                {
                    "include_embeddings": include_embeddings,
                    "embed_limit": embed_limit,
                    "max_tier0": max_tier0,
                    "max_tier1": max_tier1,
                },
                SyncTiersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=SyncTiersResponse,
        )

    def get(
        self,
        memory_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchResponse:
        """
        Retrieve a memory item by ID.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not memory_id:
            raise ValueError(f"Expected a non-empty value for `memory_id` but received {memory_id!r}")
        return self._get(
            f"/v1/memory/{memory_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchResponse,
        )

    def _process_sync_tiers_and_store(self, extra_headers: Headers | None = None, extra_query: Query | None = None, extra_body: Body | None = None, timeout: float | httpx.Timeout | None | NotGiven = None):
        """Internal method to call sync_tiers and store tier0 data in ChromaDB"""
        from .._logging import get_logger
        logger = get_logger(__name__)
        
        try:
            # Call the sync_tiers method with hardcoded parameters
            sync_response = self.sync_tiers(
                include_embeddings=True,
                embed_limit=2,
                max_tier0=2,
                max_tier1=0,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            )
            
            if sync_response:
                # Extract tier0 data using SyncTiersResponse model
                tier0_data = sync_response.tier0
                tier1_data = sync_response.tier1
                
                if tier0_data:
                    logger.info(f"Found {len(tier0_data)} tier0 items in sync response")
                    for i in range(min(3, len(tier0_data))):
                        logger.debug(f"Tier0 {i+1}: Item extracted")
                
                if tier1_data:
                    logger.info(f"Found {len(tier1_data)} tier1 items in sync response")
                
                # Store tier0 data in ChromaDB
                if tier0_data:
                    logger.info(f"Using {len(tier0_data)} tier0 items for search enhancement")
                    self._store_tier0_in_chromadb(tier0_data)
                else:
                    logger.info("No tier0 data found in sync response")
                    
        except Exception as e:
            logger.error(f"Error in sync_tiers processing: {e}")

    def _is_old_platform(self):
        """Detect if platform is too old for efficient local processing"""
        from .._logging import get_logger
        logger = get_logger(__name__)
        
        try:
            import platform
            import subprocess
            import psutil
            
            system = platform.system()
            
            # Check Apple platforms
            if system == "Darwin":
                try:
                    # Get Apple chip info
                    result = subprocess.run(['sysctl', '-n', 'machdep.cpu.brand_string'], 
                                         capture_output=True, text=True, timeout=5)
                    if result.returncode == 0:
                        cpu_info = result.stdout.strip()
                        # Check for old Intel Macs (pre-Apple Silicon)
                        if 'Intel' in cpu_info and 'Apple' not in cpu_info:
                            logger.info("Detected old Intel Mac - using API instead of local processing")
                            return True
                        # Check for very old Apple Silicon (M1 without sufficient performance)
                        elif 'Apple' in cpu_info:
                            # Check for M1 vs M2/M3/M4
                            if 'M1' in cpu_info and 'M1 Pro' not in cpu_info and 'M1 Max' not in cpu_info and 'M1 Ultra' not in cpu_info:
                                # Check RAM - M1 with < 16GB might be too slow
                                ram_gb = psutil.virtual_memory().total / (1024**3)
                                if ram_gb < 16:
                                    logger.info("Detected M1 with limited RAM - using API instead of local processing")
                                    return True
                except:
                    pass
            
            # Check Intel platforms
            elif system == "Linux" or system == "Windows":
                try:
                    cpu_info = platform.processor() or platform.machine()
                    # Check for old Intel CPUs (pre-10th gen or < 4 cores)
                    if 'Intel' in cpu_info:
                        cpu_count = psutil.cpu_count(logical=False)
                        if cpu_count < 4:
                            logger.info("Detected old Intel CPU with < 4 cores - using API instead of local processing")
                            return True
                    
                    # Check for old AMD CPUs
                    elif 'AMD' in cpu_info:
                        cpu_count = psutil.cpu_count(logical=False)
                        if cpu_count < 4:
                            logger.info("Detected old AMD CPU with < 4 cores - using API instead of local processing")
                            return True
                except:
                    pass
            
            # Check available RAM (less than 8GB is too little for local processing)
            ram_gb = psutil.virtual_memory().total / (1024**3)
            if ram_gb < 8:
                logger.info(f"Insufficient RAM ({ram_gb:.1f}GB) - using API instead of local processing")
                return True
                
        except ImportError:
            logger.info("psutil not available - assuming modern platform")
        except Exception as e:
            logger.error(f"Error detecting platform age: {e}")
        
        return False

    def _get_optimized_quantized_model(self, device: str, device_name: str):
        """Get the best quantized model for the specific platform"""
        from .._logging import get_logger
        logger = get_logger(__name__)
        
        try:
            from sentence_transformers import SentenceTransformer
            
            # Platform-specific model selection (using sentence-transformers compatible models)
            if "Apple" in device_name or device == "mps":
                # Apple Silicon - use MLX-optimized quantized model
                model_options = [
                    'mlx-community/Qwen3-Embedding-4B-4bit-DWQ',  # MLX optimized
                    'Qwen/Qwen3-Embedding-4B'  # Original fallback
                ]
                logger.info("Using Apple Silicon optimized quantized model")
                
            elif "NVIDIA" in device_name or device == "cuda":
                # NVIDIA GPU - use original model (sentence-transformers compatible)
                model_options = [
                    'Qwen/Qwen3-Embedding-4B'  # Original model (best compatibility)
                ]
                logger.info("Using NVIDIA CUDA optimized model")
                
            elif "Intel" in device_name or device == "xpu":
                # Intel GPU/XPU - use original model
                model_options = [
                    'Qwen/Qwen3-Embedding-4B'  # Original model (best compatibility)
                ]
                logger.info("Using Intel XPU optimized model")
                
            elif "AMD" in device_name or device == "hip":
                # AMD GPU - use original model
                model_options = [
                    'Qwen/Qwen3-Embedding-4B'  # Original model (best compatibility)
                ]
                logger.info("Using AMD HIP optimized model")
                
            else:
                # CPU or unknown - use original model
                model_options = [
                    'Qwen/Qwen3-Embedding-4B'  # Original model (best compatibility)
                ]
                logger.info("Using CPU/universal optimized model")
            
            # Try each model option in order of preference
            for model_name in model_options:
                try:
                    model = SentenceTransformer(model_name, device=device)
                    if "4bit" in model_name or "Q4" in model_name or "W4" in model_name:
                        logger.info(f"Loaded quantized {model_name} on {device}")
                    else:
                        logger.info(f"Loaded original {model_name} on {device}")
                    return model
                except Exception as e:
                    logger.warning(f"Failed to load {model_name}: {e}")
                    continue
            
            # Final fallback - this should never be reached
            raise Exception("All model options failed")
            
        except Exception as e:
            logger.error(f"Error loading optimized quantized model: {e}")
            return None

    def _get_local_embedder(self):
        """Get local embedder optimized for the current platform"""
        from .._logging import get_logger
        logger = get_logger(__name__)
        
        try:
            # Check if platform is too old for local processing
            if self._is_old_platform():
                logger.info("Platform detected as too old - skipping local embedding generation")
                return None
                
            from sentence_transformers import SentenceTransformer
            import torch
            import platform
            import subprocess
            
            # Detect platform and set optimal device (NPU first, then GPU, then CPU)
            device = None
            device_name = None
            
            # 1. Check for Apple Silicon NPU (highest priority for NPU platforms)
            if hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
                device = "mps"  # Apple Silicon (includes NPU via MPS)
                # Check if we're on Apple Silicon with Neural Engine
                if platform.system() == "Darwin":
                    try:
                        # Check for Apple Silicon chip
                        result = subprocess.run(['sysctl', '-n', 'machdep.cpu.brand_string'], 
                                             capture_output=True, text=True, timeout=5)
                        if result.returncode == 0 and 'Apple' in result.stdout:
                            device_name = "Apple Silicon with Neural Engine NPU (via MPS)"
                        else:
                            device_name = "Apple Metal Performance Shaders (MPS)"
                    except:
                        device_name = "Apple Metal Performance Shaders (MPS) - includes Neural Engine NPU"
                else:
                    device_name = "Apple Metal Performance Shaders (MPS) - includes Neural Engine NPU"
            
            # 2. Check for Intel NPU (Intel Arc with NPU)
            elif hasattr(torch.backends, 'xpu') and torch.backends.xpu.is_available():
                device = "xpu"  # Intel GPU (Arc, Xe) - may include NPU
                device_name = "Intel XPU (Arc/Xe with potential NPU)"
            
            # 3. Fallback to traditional GPUs
            elif torch.cuda.is_available():
                device = "cuda"
                device_name = "NVIDIA CUDA GPU"
            elif hasattr(torch.backends, 'hip') and torch.backends.hip.is_available():
                device = "hip"  # AMD GPU (ROCm)
                device_name = "AMD HIP/ROCm GPU"
            
            # 4. Final fallback to CPU
            if device is None:
                device = "cpu"
                device_name = "CPU"
            
            logger.info(f"Using {device_name} for embeddings")
            
            # Use platform-optimized quantized Qwen3-Embedding-4B model
            model = self._get_optimized_quantized_model(device, device_name)
            return model
            
        except ImportError:
            logger.warning("sentence-transformers not available - install with: pip install sentence-transformers")
            return None
        except Exception as e:
            logger.error(f"Error initializing local embedder: {e}")
            return None

    def _embed_query_locally(self, query: str):
        """Generate embedding for query using local hardware"""
        from .._logging import get_logger
        logger = get_logger(__name__)
        
        embedder = self._get_local_embedder()
        if embedder:
            try:
                import time
                start_time = time.time()
                embedding = embedder.encode([query])[0].tolist()
                generation_time = time.time() - start_time
                logger.info(f"Generated local query embedding (dim: {len(embedding)}) in {generation_time:.2f}s")
                return embedding
            except Exception as e:
                logger.error(f"Error generating local embedding: {e}")
        else:
            logger.info("Local embedding generation skipped - using API-based search")
        return None

    def _get_qwen_embedding_function(self):
        """Get Qwen-based embedding function for ChromaDB using the correct interface"""
        from .._logging import get_logger
        logger = get_logger(__name__)
        
        try:
            from sentence_transformers import SentenceTransformer
            import torch
            
            # Detect platform (NPU first, then GPU, then CPU)
            device = None
            
            # 1. Check for Apple Silicon NPU (highest priority for NPU platforms)
            if hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
                device = "mps"  # Apple Silicon (includes NPU via MPS)
            # 2. Check for Intel NPU (Intel Arc with NPU)
            elif hasattr(torch.backends, 'xpu') and torch.backends.xpu.is_available():
                device = "xpu"  # Intel GPU (Arc, Xe) - may include NPU
            # 3. Fallback to traditional GPUs
            elif torch.cuda.is_available():
                device = "cuda"
            elif hasattr(torch.backends, 'hip') and torch.backends.hip.is_available():
                device = "hip"  # AMD GPU (ROCm)
            # 4. Final fallback to CPU
            if device is None:
                device = "cpu"
            
            # Use platform-optimized quantized model
            model = self._get_optimized_quantized_model(device, f"Device: {device}")
            
            # Create a proper ChromaDB embedding function class
            class QwenEmbeddingFunction:
                def __init__(self, model):
                    self.model = model
                
                def __call__(self, input_texts):
                    # Handle both single string and list of strings
                    if isinstance(input_texts, str):
                        input_texts = [input_texts]
                    embeddings = self.model.encode(input_texts)
                    return embeddings.tolist()
            
            return QwenEmbeddingFunction(model)
            
        except Exception as e:
            logger.error(f"Error creating Qwen embedding function: {e}")
            return None

    def _search_tier0_locally(self, query: str, n_results: int = 5):
        """Search tier0 data using local vector search"""
        from .._logging import get_logger
        logger = get_logger(__name__)
        
        if not hasattr(self, '_chroma_collection'):
            return []
        
        try:
            query_embedding = self._embed_query_locally(query)
            if not query_embedding:
                return []
            
            # Perform vector search in ChromaDB
            results = self._chroma_collection.query(
                query_embeddings=[query_embedding],
                n_results=n_results
            )
            
            if results['documents'] and results['documents'][0]:
                logger.info(f"Found {len(results['documents'][0])} relevant tier0 items locally")
                return results['documents'][0]
            else:
                logger.info("No relevant tier0 items found locally")
                return []
                
        except Exception as e:
            logger.error(f"Error in local tier0 search: {e}")
            return []

    def _store_tier0_in_chromadb(self, tier0_data):
        """Store tier0 data in ChromaDB with duplicate prevention"""
        from .._logging import get_logger
        logger = get_logger(__name__)
        
        try:
            logger.info("Attempting to import ChromaDB...")
            import chromadb  # type: ignore
            from chromadb.config import Settings  # type: ignore
            logger.info("ChromaDB imported successfully")
            
            # Initialize ChromaDB client (singleton pattern)
            if not hasattr(self, '_chroma_client'):
                logger.info("Creating ChromaDB client...")
                self._chroma_client = chromadb.Client(Settings(
                    persist_directory="./chroma_db",
                    anonymized_telemetry=False
                ))
                logger.info("Initialized ChromaDB client")
            
            # Create or get collection for tier0 data
            collection_name = "tier0_goals_okrs"
            logger.info(f"Attempting to get/create collection: {collection_name}")
            if not hasattr(self, '_chroma_collection'):
                try:
                    logger.info("Trying to get existing collection...")
                    self._chroma_collection = self._chroma_client.get_collection(name=collection_name)
                    logger.info(f"Using existing ChromaDB collection: {collection_name}")
                except Exception as e:
                    logger.info(f"Collection doesn't exist, creating new one: {e}")
                    # Create collection without custom embedding function
                    logger.info("Creating collection without custom embedding function...")
                    self._chroma_collection = self._chroma_client.create_collection(
                        name=collection_name,
                        metadata={"description": "Tier0 goals, OKRs, and use-cases from sync_tiers"}
                    )
                    logger.info(f"Created new ChromaDB collection: {collection_name}")
            
            collection = self._chroma_collection
            
            # Prepare documents for ChromaDB
            documents = []
            metadatas = []
            ids = []
            
            for i, item in enumerate(tier0_data):
                # Extract content for embedding
                content = str(item)
                if isinstance(item, dict):
                    content = str(item.get('content', item.get('description', str(item))))
                
                # Create metadata
                metadata = {
                    "source": "sync_tiers",
                    "tier": 0,
                    "type": "unknown",
                    "topics": "unknown"
                }
                
                if isinstance(item, dict):
                    metadata["type"] = str(item.get('type', 'unknown'))
                    metadata["topics"] = str(item.get('topics', []))
                    if 'metadata' in item:
                        metadata.update(item['metadata'])
                
                documents.append(content)
                metadatas.append(metadata)
                item_id = f"tier0_{i}"
                if isinstance(item, dict) and 'id' in item:
                    item_id = f"tier0_{i}_{item['id']}"
                ids.append(item_id)
            
            # Extract embeddings from server response
            embeddings = []
            if tier0_data and isinstance(tier0_data[0], dict) and 'embedding' in tier0_data[0]:
                logger.info("Using embeddings from server response...")
                for i, item in enumerate(tier0_data):
                    if isinstance(item, dict) and 'embedding' in item:
                        embedding = item['embedding']
                        # Validate embedding format
                        if isinstance(embedding, list) and len(embedding) > 0 and isinstance(embedding[0], (int, float)):
                            embeddings.append(embedding)
                            logger.info(f"Valid server embedding for item {i} (dim: {len(embedding)})")
                        else:
                            logger.warning(f"Invalid server embedding format for item {i}, will use local generation")
                            embeddings.append(None)
                    else:
                        embeddings.append(None)
            else:
                logger.info("No server embeddings found, will generate locally")
                embeddings = [None] * len(documents)
            
            # Generate local embeddings for items without server embeddings
            if any(emb is None for emb in embeddings):
                logger.info("Generating local embeddings for missing items...")
                try:
                    import time
                    start_time = time.time()
                    
                    embedder = self._get_local_embedder()
                    if embedder:
                        local_embedding_count = 0
                        for i, embedding in enumerate(embeddings):
                            if embedding is None:
                                try:
                                    item_start_time = time.time()
                                    local_embedding = embedder.encode([documents[i]])[0].tolist()
                                    item_time = time.time() - item_start_time
                                    embeddings[i] = local_embedding
                                    local_embedding_count += 1
                                    logger.info(f"Generated local embedding for item {i} (dim: {len(local_embedding)}) in {item_time:.2f}s")
                                except Exception as e:
                                    logger.error(f"Failed to generate local embedding for item {i}: {e}")
                        
                        total_time = time.time() - start_time
                        if local_embedding_count > 0:
                            avg_time = total_time / local_embedding_count
                            logger.info(f"Generated {local_embedding_count} local embeddings in {total_time:.2f}s (avg: {avg_time:.2f}s per embedding)")
                    else:
                        logger.warning("No local embedder available for missing embeddings")
                except Exception as e:
                    logger.error(f"Error generating local embeddings: {e}")
            
            # Add documents to ChromaDB (avoid duplicates)
            if documents:
                # Check if documents already exist to avoid duplicates
                existing_ids = set()
                try:
                    existing = collection.get(ids=ids)
                    existing_ids = set(existing['ids']) if existing['ids'] else set()
                except:
                    pass  # Collection might be empty
                
                # Only add new documents
                new_documents = []
                new_metadatas = []
                new_ids = []
                
                for i, doc_id in enumerate(ids):
                    if doc_id not in existing_ids:
                        new_documents.append(documents[i])
                        new_metadatas.append(metadatas[i])
                        new_ids.append(doc_id)
                
                if new_documents:
                    # Filter embeddings for new documents only
                    new_embeddings = []
                    for i, doc_id in enumerate(new_ids):
                        original_index = ids.index(doc_id)
                        new_embeddings.append(embeddings[original_index])
                    
                    # Add documents with embeddings if available
                    if any(emb is not None for emb in new_embeddings):
                        collection.add(
                            documents=new_documents,
                            metadatas=new_metadatas,
                            ids=new_ids,
                            embeddings=new_embeddings
                        )
                        logger.info(f"Added {len(new_documents)} documents with local embeddings")
                    else:
                        collection.add(
                            documents=new_documents,
                            metadatas=new_metadatas,
                            ids=new_ids
                        )
                        logger.info(f"Added {len(new_documents)} documents with ChromaDB default embeddings")
                    logger.info(f"Stored {len(new_documents)} new tier0 items in ChromaDB")
                else:
                    logger.info(f"All {len(documents)} tier0 items already exist in ChromaDB")
                
                # Query to verify storage
                results = collection.query(
                    query_texts=["goals objectives"],
                    n_results=min(3, len(documents))
                )
                logger.info(f"ChromaDB query test returned {len(results['documents'][0])} results")
                
        except ImportError:
            logger.warning("ChromaDB not available - install with: pip install chromadb")
            logger.warning("Tier0 data will not be stored in vector database")
        except Exception as e:
            logger.error(f"Error storing tier0 data in ChromaDB: {e}")

    def search(
        self,
        *,
        query: str,
        max_memories: int | NotGiven = NOT_GIVEN,
        max_nodes: int | NotGiven = NOT_GIVEN,
        enable_agentic_graph: bool | NotGiven = NOT_GIVEN,
        external_user_id: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[MemoryMetadataParam] | NotGiven = NOT_GIVEN,
        rank_results: bool | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        accept_encoding: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchResponse:
        """
        Search through memories with authentication required.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Recommended Headers**:
            ```
            Accept-Encoding: gzip
            ```

            The API supports response compression for improved performance. Responses larger than 1KB will be automatically compressed when this header is present.

            **HIGHLY RECOMMENDED SETTINGS FOR BEST RESULTS:**
            - Set `enable_agentic_graph: true` for intelligent, context-aware search that can understand ambiguous references
            - Use `max_memories: 15-20` for comprehensive memory coverage
            - Use `max_nodes: 10-15` for comprehensive graph entity relationships

            **Agentic Graph Benefits:**
            When enabled, the system can understand vague references by first identifying specific entities from your memory graph, then performing targeted searches. For example:
            - "customer feedback" → identifies your customers first, then finds their specific feedback
            - "project issues" → identifies your projects first, then finds related issues
            - "team meeting notes" → identifies your team members first, then finds meeting notes

            **User Resolution Precedence:**
            - If both user_id and external_user_id are provided, user_id takes precedence.
            - If only external_user_id is provided, it will be resolved to the internal user.
            - If neither is provided, the authenticated user is used.

        Args:
          query: Detailed search query describing what you're looking for. For best results,
              write 2-3 sentences that include specific details, context, and time frame.
              Examples: 'Find recurring customer complaints about API performance from the
              last month. Focus on issues where customers specifically mentioned timeout
              errors or slow response times in their conversations.' 'What are the main issues
              and blockers in my current projects? Focus on technical challenges and timeline
              impacts.' 'Find insights about team collaboration and communication patterns
              from recent meetings and discussions.'

          max_memories: HIGHLY RECOMMENDED: Maximum number of memories to return. Use at least 15-20 for
              comprehensive results. Lower values (5-10) may miss relevant information.
              Default is 20 for optimal coverage.

          max_nodes: HIGHLY RECOMMENDED: Maximum number of neo nodes to return. Use at least 10-15
              for comprehensive graph results. Lower values may miss important entity
              relationships. Default is 15 for optimal coverage.

          enable_agentic_graph: HIGHLY RECOMMENDED: Enable agentic graph search for intelligent, context-aware
              results. When enabled, the system can understand ambiguous references by first
              identifying specific entities from your memory graph, then performing targeted
              searches. Examples: 'customer feedback' → identifies your customers first, then
              finds their specific feedback; 'project issues' → identifies your projects
              first, then finds related issues; 'team meeting notes' → identifies team members
              first, then finds meeting notes. This provides much more relevant and
              comprehensive results. Set to false only if you need faster, simpler
              keyword-based search.

          external_user_id: Optional external user ID to filter search results by a specific external user.
              If both user_id and external_user_id are provided, user_id takes precedence.

          metadata: Metadata for memory request

          rank_results: Whether to enable additional ranking of search results. Default is false because
              results are already ranked when using an LLM for search (recommended approach).
              Only enable this if you're not using an LLM in your search pipeline and need
              additional result ranking.

          user_id: Optional internal user ID to filter search results by a specific user. If not
              provided, results are not filtered by user. If both user_id and external_user_id
              are provided, user_id takes precedence.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # Check if on-device processing is enabled
        import os
        from .._logging import get_logger
        logger = get_logger(__name__)
        
        ondevice_processing = os.environ.get("PAPR_ONDEVICE_PROCESSING", "false").lower() in ("true", "1", "yes", "on")
        
        # Search tier0 data locally for context enhancement if enabled
        tier0_context = []
        if ondevice_processing and hasattr(self, '_chroma_collection'):
            tier0_context = self._search_tier0_locally(query, n_results=3)
            if tier0_context:
                logger.info(f"Using {len(tier0_context)} tier0 items for search context enhancement")
        elif not ondevice_processing:
            logger.info("On-device processing disabled - using API-only search")
        else:
            logger.info("No ChromaDB collection available for local search")
        
        # Perform the main search
        extra_headers = {**strip_not_given({"Accept-Encoding": accept_encoding}), **(extra_headers or {})}
        return self._post(
            "/v1/memory/search",
            body=maybe_transform(
                {
                    "query": query,
                    "enable_agentic_graph": enable_agentic_graph,
                    "external_user_id": external_user_id,
                    "metadata": metadata,
                    "rank_results": rank_results,
                    "user_id": user_id,
                },
                memory_search_params.MemorySearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "max_memories": max_memories,
                        "max_nodes": max_nodes,
                    },
                    memory_search_params.MemorySearchParams,
                ),
            ),
            cast_to=SearchResponse,
        )


class AsyncMemoryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMemoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#accessing-raw-response-data-eg-headers
        """
        return AsyncMemoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMemoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Papr-ai/papr-pythonSDK#with_streaming_response
        """
        return AsyncMemoryResourceWithStreamingResponse(self)

    async def update(
        self,
        memory_id: str,
        *,
        content: Optional[str] | NotGiven = NOT_GIVEN,
        context: Optional[Iterable[ContextItemParam]] | NotGiven = NOT_GIVEN,
        metadata: Optional[MemoryMetadataParam] | NotGiven = NOT_GIVEN,
        relationships_json: Optional[Iterable[RelationshipItemParam]] | NotGiven = NOT_GIVEN,
        type: Optional[MemoryType] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemoryUpdateResponse:
        """
        Update an existing memory item by ID.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - Content-Type: application/json
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

            The API validates content size against MAX_CONTENT_LENGTH environment variable (defaults to 15000 bytes).

        Args:
          content: The new content of the memory item

          context: Updated context for the memory item

          metadata: Metadata for memory request

          relationships_json: Updated relationships for Graph DB (neo4J)

          type: Valid memory types

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not memory_id:
            raise ValueError(f"Expected a non-empty value for `memory_id` but received {memory_id!r}")
        return await self._put(
            f"/v1/memory/{memory_id}",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "context": context,
                    "metadata": metadata,
                    "relationships_json": relationships_json,
                    "type": type,
                },
                memory_update_params.MemoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryUpdateResponse,
        )

    async def delete(
        self,
        memory_id: str,
        *,
        skip_parse: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemoryDeleteResponse:
        """
        Delete a memory item by ID.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

        Args:
          skip_parse: Skip Parse Server deletion

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not memory_id:
            raise ValueError(f"Expected a non-empty value for `memory_id` but received {memory_id!r}")
        return await self._delete(
            f"/v1/memory/{memory_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"skip_parse": skip_parse}, memory_delete_params.MemoryDeleteParams),
            ),
            cast_to=MemoryDeleteResponse,
        )

    async def add(
        self,
        *,
        content: str,
        type: MemoryType,
        skip_background_processing: bool | NotGiven = NOT_GIVEN,
        context: Optional[Iterable[ContextItemParam]] | NotGiven = NOT_GIVEN,
        metadata: Optional[MemoryMetadataParam] | NotGiven = NOT_GIVEN,
        relationships_json: Optional[Iterable[RelationshipItemParam]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddMemoryResponse:
        """
        Add a new memory item to the system with size validation and background
        processing.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - Content-Type: application/json
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

            The API validates content size against MAX_CONTENT_LENGTH environment variable (defaults to 15000 bytes).

        Args:
          content: The content of the memory item you want to add to memory

          type: Valid memory types

          skip_background_processing: If True, skips adding background tasks for processing

          context: Context can be conversation history or any relevant context for a memory item

          metadata: Metadata for memory request

          relationships_json: Array of relationships that we can use in Graph DB (neo4J)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/memory",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "type": type,
                    "context": context,
                    "metadata": metadata,
                    "relationships_json": relationships_json,
                },
                memory_add_params.MemoryAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"skip_background_processing": skip_background_processing}, memory_add_params.MemoryAddParams
                ),
            ),
            cast_to=AddMemoryResponse,
        )

    async def add_batch(
        self,
        *,
        memories: Iterable[AddMemoryParam],
        skip_background_processing: bool | NotGiven = NOT_GIVEN,
        batch_size: Optional[int] | NotGiven = NOT_GIVEN,
        external_user_id: Optional[str] | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_secret: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_url: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchMemoryResponse:
        """
        Add multiple memory items in a batch with size validation and background
        processing.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - Content-Type: application/json
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

            The API validates individual memory content size against MAX_CONTENT_LENGTH environment variable (defaults to 15000 bytes).

        Args:
          memories: List of memory items to add in batch

          skip_background_processing: If True, skips adding background tasks for processing

          batch_size: Number of items to process in parallel

          external_user_id: External user ID for all memories in the batch. If provided and user_id is not,
              will be resolved to internal user ID.

          user_id: Internal user ID for all memories in the batch. If not provided, developer's
              user ID will be used.

          webhook_secret: Optional secret key for webhook authentication. If provided, will be included in
              the webhook request headers as 'X-Webhook-Secret'.

          webhook_url: Optional webhook URL to notify when batch processing is complete. The webhook
              will receive a POST request with batch completion details.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/memory/batch",
            body=await async_maybe_transform(
                {
                    "memories": memories,
                    "batch_size": batch_size,
                    "external_user_id": external_user_id,
                    "user_id": user_id,
                    "webhook_secret": webhook_secret,
                    "webhook_url": webhook_url,
                },
                memory_add_batch_params.MemoryAddBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"skip_background_processing": skip_background_processing},
                    memory_add_batch_params.MemoryAddBatchParams,
                ),
            ),
            cast_to=BatchMemoryResponse,
        )

    async def delete_all(
        self,
        *,
        external_user_id: Optional[str] | NotGiven = NOT_GIVEN,
        skip_parse: bool | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchMemoryResponse:
        """
        Delete all memory items for a user.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **User Resolution**:
            - If only API key is provided: deletes memories for the developer
            - If user_id or external_user_id is provided: resolves and deletes memories for that user
            - Uses the same user resolution logic as other endpoints

            **Required Headers**:
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

            **WARNING**: This operation cannot be undone. All memories for the resolved user will be permanently deleted.

        Args:
          external_user_id: Optional external user ID to resolve and delete memories for

          skip_parse: Skip Parse Server deletion

          user_id: Optional user ID to delete memories for (if not provided, uses authenticated
              user)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/v1/memory/all",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "external_user_id": external_user_id,
                        "skip_parse": skip_parse,
                        "user_id": user_id,
                    },
                    memory_delete_all_params.MemoryDeleteAllParams,
                ),
            ),
            cast_to=BatchMemoryResponse,
        )

    async def sync_tiers(
        self,
        *,
        include_embeddings: bool | NotGiven = NOT_GIVEN,
        embed_limit: int | NotGiven = NOT_GIVEN,
        max_tier0: int | NotGiven = NOT_GIVEN,
        max_tier1: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncTiersResponse:
        """
        Get sync tiers for memory synchronization.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')
            - Accept-Encoding: gzip (recommended)

        Args:
          include_embeddings: Whether to include embeddings in the response

          embed_limit: Limit for embeddings

          max_tier0: Maximum number of tier 0 items

          max_tier1: Maximum number of tier 1 items

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Accept-Encoding": "gzip"}), **(extra_headers or {})}
        return await self._post(
            "/v1/sync/tiers",
            body=await async_maybe_transform(
                {
                    "include_embeddings": include_embeddings,
                    "embed_limit": embed_limit,
                    "max_tier0": max_tier0,
                    "max_tier1": max_tier1,
                },
                SyncTiersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=SyncTiersResponse,
        )

    async def get(
        self,
        memory_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchResponse:
        """
        Retrieve a memory item by ID.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Required Headers**:
            - X-Client-Type: (e.g., 'papr_plugin', 'browser_extension')

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not memory_id:
            raise ValueError(f"Expected a non-empty value for `memory_id` but received {memory_id!r}")
        return await self._get(
            f"/v1/memory/{memory_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchResponse,
        )

    async def _process_sync_tiers_and_store(self, extra_headers: Headers | None = None, extra_query: Query | None = None, extra_body: Body | None = None, timeout: float | httpx.Timeout | None | NotGiven = None):
        """Internal async method to call sync_tiers and store tier0 data in ChromaDB"""
        from .._logging import get_logger
        logger = get_logger(__name__)
        
        try:
            # Call the async sync_tiers method with hardcoded parameters
            sync_response = await self.sync_tiers(
                include_embeddings=True,
                embed_limit=2,
                max_tier0=2,
                max_tier1=0,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            )
            
            if sync_response:
                # Extract tier0 data using SyncTiersResponse model
                tier0_data = sync_response.tier0
                tier1_data = sync_response.tier1
                
                if tier0_data:
                    logger.info(f"Found {len(tier0_data)} tier0 items in sync response")
                    for i in range(min(3, len(tier0_data))):
                        logger.debug(f"Tier0 {i+1}: Item extracted")
                
                if tier1_data:
                    logger.info(f"Found {len(tier1_data)} tier1 items in sync response")
                
                # Store tier0 data in ChromaDB
                if tier0_data:
                    logger.info(f"Using {len(tier0_data)} tier0 items for search enhancement")
                    self._store_tier0_in_chromadb(tier0_data)
                else:
                    logger.info("No tier0 data found in sync response")
                    
        except Exception as e:
            logger.error(f"Error in sync_tiers processing: {e}")

    async def search(
        self,
        *,
        query: str,
        max_memories: int | NotGiven = NOT_GIVEN,
        max_nodes: int | NotGiven = NOT_GIVEN,
        enable_agentic_graph: bool | NotGiven = NOT_GIVEN,
        external_user_id: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[MemoryMetadataParam] | NotGiven = NOT_GIVEN,
        rank_results: bool | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        accept_encoding: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchResponse:
        """
        Search through memories with authentication required.

            **Authentication Required**:
            One of the following authentication methods must be used:
            - Bearer token in `Authorization` header
            - API Key in `X-API-Key` header
            - Session token in `X-Session-Token` header

            **Recommended Headers**:
            ```
            Accept-Encoding: gzip
            ```

            The API supports response compression for improved performance. Responses larger than 1KB will be automatically compressed when this header is present.

            **HIGHLY RECOMMENDED SETTINGS FOR BEST RESULTS:**
            - Set `enable_agentic_graph: true` for intelligent, context-aware search that can understand ambiguous references
            - Use `max_memories: 15-20` for comprehensive memory coverage
            - Use `max_nodes: 10-15` for comprehensive graph entity relationships

            **Agentic Graph Benefits:**
            When enabled, the system can understand vague references by first identifying specific entities from your memory graph, then performing targeted searches. For example:
            - "customer feedback" → identifies your customers first, then finds their specific feedback
            - "project issues" → identifies your projects first, then finds related issues
            - "team meeting notes" → identifies your team members first, then finds meeting notes

            **User Resolution Precedence:**
            - If both user_id and external_user_id are provided, user_id takes precedence.
            - If only external_user_id is provided, it will be resolved to the internal user.
            - If neither is provided, the authenticated user is used.

        Args:
          query: Detailed search query describing what you're looking for. For best results,
              write 2-3 sentences that include specific details, context, and time frame.
              Examples: 'Find recurring customer complaints about API performance from the
              last month. Focus on issues where customers specifically mentioned timeout
              errors or slow response times in their conversations.' 'What are the main issues
              and blockers in my current projects? Focus on technical challenges and timeline
              impacts.' 'Find insights about team collaboration and communication patterns
              from recent meetings and discussions.'

          max_memories: HIGHLY RECOMMENDED: Maximum number of memories to return. Use at least 15-20 for
              comprehensive results. Lower values (5-10) may miss relevant information.
              Default is 20 for optimal coverage.

          max_nodes: HIGHLY RECOMMENDED: Maximum number of neo nodes to return. Use at least 10-15
              for comprehensive graph results. Lower values may miss important entity
              relationships. Default is 15 for optimal coverage.

          enable_agentic_graph: HIGHLY RECOMMENDED: Enable agentic graph search for intelligent, context-aware
              results. When enabled, the system can understand ambiguous references by first
              identifying specific entities from your memory graph, then performing targeted
              searches. Examples: 'customer feedback' → identifies your customers first, then
              finds their specific feedback; 'project issues' → identifies your projects
              first, then finds related issues; 'team meeting notes' → identifies team members
              first, then finds meeting notes. This provides much more relevant and
              comprehensive results. Set to false only if you need faster, simpler
              keyword-based search.

          external_user_id: Optional external user ID to filter search results by a specific external user.
              If both user_id and external_user_id are provided, user_id takes precedence.

          metadata: Metadata for memory request

          rank_results: Whether to enable additional ranking of search results. Default is false because
              results are already ranked when using an LLM for search (recommended approach).
              Only enable this if you're not using an LLM in your search pipeline and need
              additional result ranking.

          user_id: Optional internal user ID to filter search results by a specific user. If not
              provided, results are not filtered by user. If both user_id and external_user_id
              are provided, user_id takes precedence.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # Check if on-device processing is enabled
        import os
        from .._logging import get_logger
        logger = get_logger(__name__)
        
        ondevice_processing = os.environ.get("PAPR_ONDEVICE_PROCESSING", "false").lower() in ("true", "1", "yes", "on")
        
        # Search tier0 data locally for context enhancement if enabled
        tier0_context = []
        if ondevice_processing and hasattr(self, '_chroma_collection'):
            tier0_context = self._search_tier0_locally(query, n_results=3)
            if tier0_context:
                logger.info(f"Using {len(tier0_context)} tier0 items for search context enhancement")
        elif not ondevice_processing:
            logger.info("On-device processing disabled - using API-only search")
        else:
            logger.info("No ChromaDB collection available for local search")
        
        # Perform the main search
        extra_headers = {**strip_not_given({"Accept-Encoding": accept_encoding}), **(extra_headers or {})}
        return await self._post(
            "/v1/memory/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "enable_agentic_graph": enable_agentic_graph,
                    "external_user_id": external_user_id,
                    "metadata": metadata,
                    "rank_results": rank_results,
                    "user_id": user_id,
                },
                SyncTiersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "max_memories": max_memories,
                        "max_nodes": max_nodes,
                    },
                    SyncTiersParams,
                ),
            ),
            cast_to=SyncTiersResponse,
        )


class MemoryResourceWithRawResponse:
    def __init__(self, memory: MemoryResource) -> None:
        self._memory = memory

        self.update = to_raw_response_wrapper(
            memory.update,
        )
        self.delete = to_raw_response_wrapper(
            memory.delete,
        )
        self.add = to_raw_response_wrapper(
            memory.add,
        )
        self.add_batch = to_raw_response_wrapper(
            memory.add_batch,
        )
        self.delete_all = to_raw_response_wrapper(
            memory.delete_all,
        )
        self.get = to_raw_response_wrapper(
            memory.get,
        )
        self.sync_tiers = to_raw_response_wrapper(
            memory.sync_tiers,
        )
        self.search = to_raw_response_wrapper(
            memory.search,
        )


class AsyncMemoryResourceWithRawResponse:
    def __init__(self, memory: AsyncMemoryResource) -> None:
        self._memory = memory

        self.update = async_to_raw_response_wrapper(
            memory.update,
        )
        self.delete = async_to_raw_response_wrapper(
            memory.delete,
        )
        self.add = async_to_raw_response_wrapper(
            memory.add,
        )
        self.add_batch = async_to_raw_response_wrapper(
            memory.add_batch,
        )
        self.delete_all = async_to_raw_response_wrapper(
            memory.delete_all,
        )
        self.get = async_to_raw_response_wrapper(
            memory.get,
        )
        self.sync_tiers = async_to_raw_response_wrapper(
            memory.sync_tiers,
        )
        self.search = async_to_raw_response_wrapper(
            memory.search,
        )


class MemoryResourceWithStreamingResponse:
    def __init__(self, memory: MemoryResource) -> None:
        self._memory = memory

        self.update = to_streamed_response_wrapper(
            memory.update,
        )
        self.delete = to_streamed_response_wrapper(
            memory.delete,
        )
        self.add = to_streamed_response_wrapper(
            memory.add,
        )
        self.add_batch = to_streamed_response_wrapper(
            memory.add_batch,
        )
        self.delete_all = to_streamed_response_wrapper(
            memory.delete_all,
        )
        self.get = to_streamed_response_wrapper(
            memory.get,
        )
        self.sync_tiers = to_streamed_response_wrapper(
            memory.sync_tiers,
        )
        self.search = to_streamed_response_wrapper(
            memory.search,
        )


class AsyncMemoryResourceWithStreamingResponse:
    def __init__(self, memory: AsyncMemoryResource) -> None:
        self._memory = memory

        self.update = async_to_streamed_response_wrapper(
            memory.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            memory.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            memory.add,
        )
        self.add_batch = async_to_streamed_response_wrapper(
            memory.add_batch,
        )
        self.delete_all = async_to_streamed_response_wrapper(
            memory.delete_all,
        )
        self.get = async_to_streamed_response_wrapper(
            memory.get,
        )
        self.sync_tiers = async_to_streamed_response_wrapper(
            memory.sync_tiers,
        )
        self.search = async_to_streamed_response_wrapper(
            memory.search,
        )
