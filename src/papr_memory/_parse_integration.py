"""
Parse Server integration for logging retrieval metrics to the existing QueryLog collection.

This module provides functionality to log on-device retrieval performance
to the same Parse Server database used by the memory server.
"""

import os
import json
from typing import Any, Dict, List, Tuple, Optional

import httpx

from ._logging import get_logger

logger = get_logger(__name__)


class ParsePointer:
    """Parse Server pointer object"""
    
    def __init__(self, objectId: str, className: str):
        self.objectId = objectId
        self.className = className
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "__type": "Pointer",
            "className": self.className,
            "objectId": self.objectId
        }


class QueryLog:
    """QueryLog model for Parse Server integration"""
    
    def __init__(
        self,
        user: ParsePointer,
        workspace: ParsePointer,
        queryText: str,
        retrievalLatencyMs: float,
        totalProcessingTimeMs: float,
        queryEmbeddingTokens: int,
        retrievedMemoryTokens: int,
        apiVersion: str = "v1",
        infrastructureRegion: str = "us-east-1",
        rankingEnabled: bool = True,
        enabledAgenticGraph: bool = False,
        tierSequence: Optional[List[int]] = None,
        predictedTier: Optional[str] = None,  # Not populated yet
        tierPredictionConfidence: Optional[float] = None,  # Not populated yet
        onDevice: bool = True,  # True for on-device processing
        SDKLog: bool = True,  # True for SDK-generated logs
        goalClassificationScores: Optional[List[float]] = None,
        useCaseClassificationScores: Optional[List[float]] = None,
        stepClassificationScores: Optional[List[float]] = None,
        relatedGoals: Optional[List[ParsePointer]] = None,
        relatedUseCases: Optional[List[ParsePointer]] = None,
        relatedSteps: Optional[List[ParsePointer]] = None,
        post: Optional[ParsePointer] = None,
        userMessage: Optional[ParsePointer] = None,
        assistantMessage: Optional[ParsePointer] = None,
        sessionId: Optional[str] = None,
        objectId: Optional[str] = None
    ):
        self.user = user
        self.workspace = workspace
        self.queryText = queryText
        self.retrievalLatencyMs = retrievalLatencyMs
        self.totalProcessingTimeMs = totalProcessingTimeMs
        self.queryEmbeddingTokens = queryEmbeddingTokens
        self.retrievedMemoryTokens = retrievedMemoryTokens
        self.apiVersion = apiVersion
        self.infrastructureRegion = infrastructureRegion
        self.rankingEnabled = rankingEnabled
        self.enabledAgenticGraph = enabledAgenticGraph
        self.tierSequence = tierSequence  # Not populated yet
        self.predictedTier = predictedTier  # Not populated yet
        self.tierPredictionConfidence = tierPredictionConfidence  # Not populated yet
        self.onDevice = onDevice
        self.SDKLog = SDKLog
        self.goalClassificationScores = goalClassificationScores or []
        self.useCaseClassificationScores = useCaseClassificationScores or []
        self.stepClassificationScores = stepClassificationScores or []
        self.relatedGoals = relatedGoals or []
        self.relatedUseCases = relatedUseCases or []
        self.relatedSteps = relatedSteps or []
        self.post = post
        self.userMessage = userMessage
        self.assistantMessage = assistantMessage
        self.sessionId = sessionId
        self.objectId = objectId
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for Parse Server"""
        data = {
            "user": self.user.to_dict(),
            "workspace": self.workspace.to_dict(),
            "queryText": self.queryText,
            "retrievalLatencyMs": self.retrievalLatencyMs,
            "totalProcessingTimeMs": self.totalProcessingTimeMs,
            "queryEmbeddingTokens": self.queryEmbeddingTokens,
            "retrievedMemoryTokens": self.retrievedMemoryTokens,
            "apiVersion": self.apiVersion,
            "infrastructureRegion": self.infrastructureRegion,
            "rankingEnabled": self.rankingEnabled,
            "enabledAgenticGraph": self.enabledAgenticGraph,
            # Tier fields not populated yet
            # "tierSequence": self.tierSequence,
            # "predictedTier": self.predictedTier,
            # "tierPredictionConfidence": self.tierPredictionConfidence,
            "onDevice": self.onDevice,
            "SDKLog": self.SDKLog,
            "goalClassificationScores": self.goalClassificationScores,
            "useCaseClassificationScores": self.useCaseClassificationScores,
            "stepClassificationScores": self.stepClassificationScores,
        }
        
        # Add optional fields if they exist
        if self.relatedGoals:
            data["relatedGoals"] = [goal.to_dict() for goal in self.relatedGoals]
        if self.relatedUseCases:
            data["relatedUseCases"] = [uc.to_dict() for uc in self.relatedUseCases]
        if self.relatedSteps:
            data["relatedSteps"] = [step.to_dict() for step in self.relatedSteps]
        if self.post:
            data["post"] = self.post.to_dict()
        if self.userMessage:
            data["userMessage"] = self.userMessage.to_dict()
        if self.assistantMessage:
            data["assistantMessage"] = self.assistantMessage.to_dict()
        if self.sessionId:
            data["sessionId"] = self.sessionId
        if self.objectId:
            data["objectId"] = self.objectId
            
        return data


class ParseServerLoggingService:
    """Service for logging retrieval metrics to Parse Server"""
    
    def __init__(self):
        self.parse_server_url = None
        self.parse_app_id = None
        self.parse_master_key = None
        self.parse_api_key = None
        self.enabled = False
        self._check_configuration()
    
    def _check_configuration(self):
        """Check and update configuration from environment variables"""
        self.parse_server_url = os.environ.get("PAPR_PARSE_SERVER_URL")
        self.parse_app_id = os.environ.get("PAPR_PARSE_APP_ID")
        self.parse_master_key = os.environ.get("PAPR_PARSE_MASTER_KEY")
        self.parse_api_key = os.environ.get("PAPR_PARSE_API_KEY")  # Parse Server API key
        self.memory_api_key = os.environ.get("PAPR_MEMORY_API_KEY")  # SDK API key for user lookup
        self.enabled = self._is_enabled()
        
        if self.enabled:
            logger.info("Parse Server logging enabled")
        else:
            logger.info("Parse Server logging disabled (missing configuration)")
    
    def _is_enabled(self) -> bool:
        """Check if Parse Server logging is enabled and configured"""
        return bool(
            self.parse_server_url and 
            self.parse_app_id and 
            (self.parse_master_key or self.parse_api_key) and
            self.memory_api_key  # Need SDK API key for user lookup
        )
    
    async def log_retrieval_metrics(
        self,
        query: str,
        retrieval_latency_ms: float,
        total_processing_time_ms: float,
        query_embedding_tokens: int,
        retrieved_memory_tokens: int,
        user_id: Optional[str] = None,
        workspace_id: Optional[str] = None,
        session_id: Optional[str] = None,
        post_id: Optional[str] = None,
        user_message_id: Optional[str] = None,
        assistant_message_id: Optional[str] = None,
        goal_classification_scores: Optional[List[float]] = None,
        use_case_classification_scores: Optional[List[float]] = None,
        step_classification_scores: Optional[List[float]] = None,
        related_goals: Optional[List[str]] = None,
        related_use_cases: Optional[List[str]] = None,
        related_steps: Optional[List[str]] = None
    ) -> Optional[str]:
        """Log retrieval metrics to Parse Server QueryLog collection"""
        
        # Check configuration before attempting to log
        self._check_configuration()
        if not self.enabled:
            logger.debug("Parse Server logging disabled, skipping log")
            return None
        
        try:
            # Create QueryLog object
            query_log = self._create_query_log(
                query=query,
                retrieval_latency_ms=retrieval_latency_ms,
                total_processing_time_ms=total_processing_time_ms,
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
            
            # Send to Parse Server
            result = await self._send_to_parse_server(query_log)
            
            if result and result.get("objectId"):
                logger.info(f"✅ QueryLog created successfully: {result['objectId']}")
                return result["objectId"]
            else:
                logger.error("Failed to create QueryLog - no objectId returned")
                return None
                
        except Exception as e:
            logger.error(f"Error logging retrieval metrics to Parse Server: {e}")
            return None
    
    def _create_query_log(
        self,
        query: str,
        retrieval_latency_ms: float,
        total_processing_time_ms: float,
        query_embedding_tokens: int,
        retrieved_memory_tokens: int,
        user_id: Optional[str] = None,
        workspace_id: Optional[str] = None,
        session_id: Optional[str] = None,
        post_id: Optional[str] = None,
        user_message_id: Optional[str] = None,
        assistant_message_id: Optional[str] = None,
        goal_classification_scores: Optional[List[float]] = None,
        use_case_classification_scores: Optional[List[float]] = None,
        step_classification_scores: Optional[List[float]] = None,
        related_goals: Optional[List[str]] = None,
        related_use_cases: Optional[List[str]] = None,
        related_steps: Optional[List[str]] = None
    ) -> QueryLog:
        """Create QueryLog object from parameters"""
        
        # Create pointers
        user_pointer = ParsePointer(
            objectId=user_id or "default_user",
            className="_User"
        )
        
        workspace_pointer = ParsePointer(
            objectId=workspace_id or "default_workspace",
            className="WorkSpace"
        )
        
        # Optional pointers
        post_pointer = None
        if post_id:
            post_pointer = ParsePointer(objectId=post_id, className="Post")
        
        user_message_pointer = None
        if user_message_id:
            user_message_pointer = ParsePointer(objectId=user_message_id, className="PostMessage")
        
        assistant_message_pointer = None
        if assistant_message_id:
            assistant_message_pointer = ParsePointer(objectId=assistant_message_id, className="PostMessage")
        
        # Related items pointers
        related_goals_pointers = []
        if related_goals:
            for goal_id in related_goals:
                related_goals_pointers.append(ParsePointer(objectId=goal_id, className="Goal"))
        
        related_use_cases_pointers = []
        if related_use_cases:
            for uc_id in related_use_cases:
                related_use_cases_pointers.append(ParsePointer(objectId=uc_id, className="Usecase"))
        
        related_steps_pointers = []
        if related_steps:
            for step_id in related_steps:
                related_steps_pointers.append(ParsePointer(objectId=step_id, className="Step"))
        
        return QueryLog(
            user=user_pointer,
            workspace=workspace_pointer,
            queryText=query,
            retrievalLatencyMs=retrieval_latency_ms,
            totalProcessingTimeMs=total_processing_time_ms,
            queryEmbeddingTokens=query_embedding_tokens,
            retrievedMemoryTokens=retrieved_memory_tokens,
            sessionId=session_id,
            post=post_pointer,
            userMessage=user_message_pointer,
            assistantMessage=assistant_message_pointer,
            goalClassificationScores=goal_classification_scores or [],
            useCaseClassificationScores=use_case_classification_scores or [],
            stepClassificationScores=step_classification_scores or [],
            relatedGoals=related_goals_pointers,
            relatedUseCases=related_use_cases_pointers,
            relatedSteps=related_steps_pointers,
            onDevice=True,  # Always True for SDK on-device searches
            SDKLog=True  # Always True for SDK-generated logs
        )
    
    async def _send_to_parse_server(self, query_log: QueryLog) -> Optional[Dict[str, Any]]:
        """Send QueryLog to Parse Server"""
        
        try:
            # Prepare headers
            headers = {
                "X-Parse-Application-Id": self.parse_app_id,
                "Content-Type": "application/json"
            }
            
            # Add authentication
            if self.parse_master_key:
                headers["X-Parse-Master-Key"] = self.parse_master_key
            elif self.parse_api_key:
                headers["X-Parse-REST-API-Key"] = self.parse_api_key
            
            # Prepare URL
            url = f"{self.parse_server_url}/classes/QueryLog"
            
            # Prepare data
            data = query_log.to_dict()
            
            # Send request
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(url, headers=headers, json=data)
                response.raise_for_status()
                
                result = response.json()
                logger.debug(f"Parse Server response: {result}")
                return result
                
        except Exception as e:
            logger.error(f"Error sending to Parse Server: {e}")
            return None
    
    async def _get_user_id_from_api_key(self, api_key: str) -> Optional[str]:
        """Query Parse Server User collection to get user ID from SDK API key"""
        if not self.parse_server_url or not self.parse_app_id:
            return None
            
        try:
            # Use Parse Server API key for authentication, but search by SDK API key
            headers = {
                "X-Parse-Application-Id": self.parse_app_id,
                "Content-Type": "application/json"
            }
            
            # Use the correct authentication header
            if self.parse_master_key:
                headers["X-Parse-Master-Key"] = self.parse_master_key
            elif self.parse_api_key:
                headers["X-Parse-REST-API-Key"] = self.parse_api_key
            
            # Query User collection to find user by SDK API key
            url = f"{self.parse_server_url}/classes/_User"
            params = {
                "where": json.dumps({"userAPIkey": api_key}),  # Search by SDK API key
                "limit": 10,  # Get multiple users to handle duplicates
                "order": "-updatedAt"  # Order by most recently updated
            }
            
            async with httpx.AsyncClient() as client:
                response = await client.get(url, headers=headers, params=params)
                response.raise_for_status()
                
                data = response.json()
                results = data.get("results", [])
                
                if results:
                    if len(results) > 1:
                        logger.warning(f"Found {len(results)} users with same API key, using most recent")
                    
                    # Use the first result (most recently updated due to ordering)
                    user_id = results[0].get("objectId")
                    logger.debug(f"Found user ID: {user_id} for SDK API key")
                    return user_id
                else:
                    logger.warning(f"No user found for SDK API key")
                    return None
                    
        except Exception as e:
            logger.error(f"Error querying User collection: {e}")
            return None
    
    async def get_developer_id(self) -> Optional[str]:
        """Get the developer ID from the SDK API key"""
        if not self.memory_api_key:
            return None
        return await self._get_user_id_from_api_key(self.memory_api_key)
    
    async def resolve_user_for_search(
        self,
        query: str,  # noqa: ARG002
        metadata: Optional[Dict[str, Any]] = None,
        user_id: Optional[str] = None,
        external_user_id: Optional[str] = None,
        httpx_client: Optional[httpx.AsyncClient] = None  # noqa: ARG002
    ) -> Tuple[Optional[str], Optional[str]]:
        """
        Resolve user ID for search based on search parameters.
        Returns: (resolved_user_id, developer_user_id)
        """
        try:
            logger.info("Starting user resolution for search")
            
            # Get developer ID from API key
            developer_user_id = await self.get_developer_id()
            if not developer_user_id:
                logger.warning("Could not resolve developer ID from API key")
                return None, None
            
            logger.info(f"Developer ID resolved: {developer_user_id}")
            
            # Check if any user identification is provided in the search request
            has_user_id = user_id is not None
            has_external_user_id = external_user_id is not None
            has_metadata_user_id = metadata and metadata.get('user_id') is not None
            has_metadata_external_user_id = metadata and metadata.get('external_user_id') is not None
            
            # Case 1: Developer is the end user (no user identification provided)
            if not has_user_id and not has_external_user_id and not has_metadata_user_id and not has_metadata_external_user_id:
                logger.info("Case 1: Developer is end user - no additional user identification provided")
                return developer_user_id, developer_user_id
            
            # Case 2: User ID provided directly
            elif has_user_id:
                logger.info(f"Case 2: User ID provided directly: {user_id}")
                return user_id, developer_user_id
            
            # Case 3: External user ID provided
            elif has_external_user_id:
                logger.info(f"Case 3: External user ID provided: {external_user_id}")
                # For external_user_id, we still use the developer ID in QueryLog
                # but the search will be filtered by external_user_id
                return developer_user_id, developer_user_id
            
            # Case 4: User ID in metadata
            elif has_metadata_user_id:
                metadata_user_id = metadata.get('user_id') if metadata else None
                logger.info(f"Case 4: User ID in metadata: {metadata_user_id}")
                return metadata_user_id, developer_user_id
            
            # Case 5: External user ID in metadata
            elif has_metadata_external_user_id:
                external_user_id_in_metadata = metadata.get('external_user_id') if metadata else None
                logger.info(f"Case 5: External user ID in metadata: {external_user_id_in_metadata}")
                # For external_user_id in metadata, we still use the developer ID in QueryLog
                return developer_user_id, developer_user_id
            
            # Default fallback
            else:
                logger.info("Default case: Using developer ID")
                return developer_user_id, developer_user_id
                
        except Exception as e:
            logger.error(f"Error in user resolution for search: {e}")
            return None, None


# Global instance
parse_logging_service = ParseServerLoggingService()
