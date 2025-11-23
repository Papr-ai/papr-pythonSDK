"""
Tests for Papr client initialization with user context and environment variables
"""
import os
import pytest
from unittest.mock import Mock, patch, MagicMock
from papr_memory import Papr


class TestClientInitialization:
    """Test suite for Papr client initialization"""

    def test_basic_initialization(self):
        """Test basic client initialization without user context"""
        with patch.dict(os.environ, {"PAPR_MEMORY_API_KEY": "test_key"}):
            client = Papr(x_api_key="test_key")
            assert client is not None
            assert hasattr(client, "memory")
            assert client.memory is not None

    def test_initialization_with_user_id(self):
        """Test client initialization with user_id parameter"""
        with patch.dict(os.environ, {"PAPR_MEMORY_API_KEY": "test_key"}):
            client = Papr(x_api_key="test_key", user_id="test_user_123")
            assert client is not None
            assert hasattr(client.memory, "_user_id")
            assert client.memory._user_id == "test_user_123"
            assert client.memory._user_context_version == 1

    def test_initialization_with_external_user_id(self):
        """Test client initialization with external_user_id parameter"""
        with patch.dict(os.environ, {"PAPR_MEMORY_API_KEY": "test_key"}):
            client = Papr(x_api_key="test_key", external_user_id="ext_user_abc")
            assert client is not None
            assert hasattr(client.memory, "_external_user_id")
            assert client.memory._external_user_id == "ext_user_abc"
            assert client.memory._user_context_version == 1

    def test_initialization_with_both_user_ids(self):
        """Test client initialization with both user_id and external_user_id"""
        with patch.dict(os.environ, {"PAPR_MEMORY_API_KEY": "test_key"}):
            client = Papr(
                x_api_key="test_key",
                user_id="test_user_123",
                external_user_id="ext_user_abc"
            )
            assert client is not None
            assert client.memory._user_id == "test_user_123"
            assert client.memory._external_user_id == "ext_user_abc"
            assert client.memory._user_context_version == 1

    def test_initialization_from_env_variables(self):
        """Test that client reads user context from environment variables"""
        env_vars = {
            "PAPR_MEMORY_API_KEY": "test_key",
            "PAPR_USER_ID": "env_user_123",
            "PAPR_EXTERNAL_USER_ID": "env_ext_abc"
        }
        with patch.dict(os.environ, env_vars, clear=False):
            client = Papr(x_api_key="test_key")
            assert client is not None
            assert client.memory._user_id == "env_user_123"
            assert client.memory._external_user_id == "env_ext_abc"

    def test_explicit_params_override_env_variables(self):
        """Test that explicit parameters override environment variables"""
        env_vars = {
            "PAPR_MEMORY_API_KEY": "test_key",
            "PAPR_USER_ID": "env_user_123"
        }
        with patch.dict(os.environ, env_vars, clear=False):
            client = Papr(x_api_key="test_key", user_id="explicit_user_456")
            assert client is not None
            assert client.memory._user_id == "explicit_user_456"

    @patch('papr_memory.resources.memory.MemoryResource._process_sync_tiers_and_store')
    def test_set_user_context_method(self, mock_sync):
        """Test set_user_context method updates user context correctly"""
        with patch.dict(os.environ, {"PAPR_MEMORY_API_KEY": "test_key"}):
            client = Papr(x_api_key="test_key")
            
            # Mock the sync method to avoid actual API calls
            mock_sync.return_value = None
            
            # Set user context
            client.memory.set_user_context(
                user_id="new_user_789",
                resync=False,  # Don't trigger actual sync in test
                clear_cache=False
            )
            
            assert client.memory._user_id == "new_user_789"
            assert client.memory._user_context_version == 2

    @patch('papr_memory.resources.memory.MemoryResource._clear_chromadb_collections')
    def test_clear_user_context_method(self, mock_clear):
        """Test clear_user_context method clears user context correctly"""
        with patch.dict(os.environ, {"PAPR_MEMORY_API_KEY": "test_key"}):
            client = Papr(x_api_key="test_key", user_id="test_user_123")
            
            # Mock the clear method to avoid actual ChromaDB operations
            mock_clear.return_value = None
            
            # Clear user context
            client.memory.clear_user_context(clear_cache=True)
            
            assert client.memory._user_id is None
            assert client.memory._external_user_id is None
            # Context version should still increment
            assert client.memory._user_context_version == 2
            
            # Verify clear was called
            mock_clear.assert_called_once()

    def test_user_context_version_increments(self):
        """Test that user context version increments correctly"""
        with patch.dict(os.environ, {"PAPR_MEMORY_API_KEY": "test_key"}):
            with patch('papr_memory.resources.memory.MemoryResource._process_sync_tiers_and_store'):
                client = Papr(x_api_key="test_key", user_id="user_1")
                assert client.memory._user_context_version == 1
                
                # Change user context
                client.memory.set_user_context(user_id="user_2", resync=False, clear_cache=False)
                assert client.memory._user_context_version == 2
                
                # Change again
                client.memory.set_user_context(user_id="user_3", resync=False, clear_cache=False)
                assert client.memory._user_context_version == 3

    def test_initialization_without_api_key_raises_error(self):
        """Test that initialization without API key raises appropriate error"""
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(Exception):
                # Should raise an error due to missing API key
                Papr()

    def test_initialization_with_custom_base_url(self):
        """Test client initialization with custom base URL"""
        with patch.dict(os.environ, {"PAPR_MEMORY_API_KEY": "test_key"}):
            custom_url = "https://custom.papr.ai"
            client = Papr(x_api_key="test_key", base_url=custom_url)
            assert client is not None
            assert client.base_url == custom_url

    @patch('papr_memory.resources.memory.MemoryResource._process_sync_tiers_and_store')
    def test_user_context_triggers_resync(self, mock_sync):
        """Test that changing user context triggers a resync when requested"""
        with patch.dict(os.environ, {"PAPR_MEMORY_API_KEY": "test_key"}):
            client = Papr(x_api_key="test_key", user_id="user_1")
            
            # Reset the mock (it might have been called during init)
            mock_sync.reset_mock()
            
            # Change user context with resync=True
            client.memory.set_user_context(
                user_id="user_2",
                resync=True,
                clear_cache=False
            )
            
            # Verify sync was called
            assert mock_sync.called

    def test_coreml_environment_variables(self):
        """Test that CoreML-related environment variables are respected"""
        env_vars = {
            "PAPR_MEMORY_API_KEY": "test_key",
            "PAPR_ENABLE_COREML": "true",
            "PAPR_COREML_MODEL": "/path/to/model.mlpackage",
            "PAPR_ONDEVICE_PROCESSING": "true"
        }
        with patch.dict(os.environ, env_vars, clear=False):
            # Just verify client can be initialized with these env vars
            # Actual CoreML functionality would require model files
            client = Papr(x_api_key="test_key")
            assert client is not None

    def test_parallel_search_environment_variables(self):
        """Test that parallel search environment variables are respected"""
        env_vars = {
            "PAPR_MEMORY_API_KEY": "test_key",
            "PAPR_ENABLE_PARALLEL_SEARCH": "true",
            "PAPR_ONDEVICE_SIMILARITY_THRESHOLD": "0.85"
        }
        with patch.dict(os.environ, env_vars, clear=False):
            client = Papr(x_api_key="test_key")
            assert client is not None

    def test_server_embeddings_environment_variables(self):
        """Test that server embeddings environment variables are respected"""
        env_vars = {
            "PAPR_MEMORY_API_KEY": "test_key",
            "PAPR_INCLUDE_SERVER_EMBEDDINGS": "true",
            "PAPR_EMBED_LIMIT": "200",
            "PAPR_EMBED_MODEL": "Qwen4B",
            "PAPR_EMBEDDING_FORMAT": "float32"
        }
        with patch.dict(os.environ, env_vars, clear=False):
            client = Papr(x_api_key="test_key")
            assert client is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

