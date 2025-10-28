# Parse Server Integration for On-Device Retrieval Logging

This document explains how to configure the SDK to log on-device retrieval metrics to the same Parse Server database used by the memory server.

## Overview

The SDK can now log detailed retrieval performance metrics to the existing `QueryLog` collection in Parse Server, providing unified logging across both server-side and on-device processing.

## Configuration

### Environment Variables

Set the following environment variables to enable Parse Server logging:

```bash
# Parse Server Configuration
export PAPR_PARSE_SERVER_URL="https://your-parse-server.com/parse"
export PAPR_PARSE_APP_ID="your-app-id"
export PAPR_PARSE_MASTER_KEY="your-master-key"  # or PAPR_PARSE_API_KEY
export PAPR_MEMORY_API_KEY="your-sdk-api-key"  # SDK API key for user lookup

# Enable metrics logging
export PAPR_ENABLE_METRICS="true"
export PAPR_ONDEVICE_PROCESSING="true"
```

### Optional Configuration

```bash
# Optional: File logging
export PAPR_LOG_FILE="./logs/retrieval.log"

# Optional: Log level
export PAPR_LOG_LEVEL="INFO"
```

## QueryLog Schema

The SDK logs to the same `QueryLog` collection with the following schema:

```json
{
  "_id": "generated-object-id",
  "_p_user": "User$user-id",
  "_p_workspace": "WorkSpace$workspace-id",
  "queryText": "User's search query",
  "retrievalLatencyMs": 58.67,
  "totalProcessingTimeMs": 58.67,
  "queryEmbeddingTokens": 14,
  "retrievedMemoryTokens": 500,
  "apiVersion": "v1",
  "infrastructureRegion": "us-east-1",
  "rankingEnabled": true,
  "enabledAgenticGraph": false,
  // Tier fields not populated yet
  // "tierSequence": [0],
  // "predictedTier": "0", 
  // "tierPredictionConfidence": 1.0,
  "onDevice": true,  // true = on-device processing
  "SDKLog": true,  // true = SDK-generated log
  "goalClassificationScores": [],
  "useCaseClassificationScores": [],
  "stepClassificationScores": [],
  "_created_at": "2025-01-13T10:30:00.000Z",
  "_updated_at": "2025-01-13T10:30:00.000Z"
}
```

## Key Differences from Server-Side Logging

| Field | Server-Side | On-Device (SDK) |
|-------|-------------|------------------|
| `tierSequence` | `[2, 3]` | Not populated yet |
| `predictedTier` | `"1"`, `"2"`, `"3"` | Not populated yet |
| `tierPredictionConfidence` | `0.75` | Not populated yet |
| `onDevice` | `false` | `true` |
| `SDKLog` | `false` | `true` |
| `retrievalLatencyMs` | Server processing time | Local processing time |
| `infrastructureRegion` | Server region | Client region |

## Performance Metrics Tracked

### Retrieval Latency
- **Total Latency**: Complete search time from query to results
- **Embedding Latency**: Time to generate query embeddings
- **ChromaDB Latency**: Time for vector search in ChromaDB

### Token Usage
- **Query Embedding Tokens**: Estimated tokens in the query
- **Retrieved Memory Tokens**: Estimated tokens in retrieved memories

### Model Metrics
- **Model Loading Time**: Time to load the embedding model
- **Device Type**: CUDA, CPU, MPS, etc.
- **Embedding Dimensions**: Vector dimension size (2560 for Qwen3-4B)

## Usage Examples

### Basic Usage

```python
import os
from papr_memory import Papr

# Configure Parse Server logging
os.environ["PAPR_PARSE_SERVER_URL"] = "https://your-parse-server.com/parse"
os.environ["PAPR_PARSE_APP_ID"] = "your-app-id"
os.environ["PAPR_PARSE_MASTER_KEY"] = "your-master-key"
os.environ["PAPR_ENABLE_METRICS"] = "true"
os.environ["PAPR_ONDEVICE_PROCESSING"] = "true"

# Create client
client = Papr(x_api_key="your-api-key")

# Search (automatically logs to Parse Server)
response = client.memory.search(
    query="Find information about recent projects",
    max_memories=10
)
```

### User ID Resolution Logic

The SDK determines the user_id for Parse Server logging based on the search metadata:

1. **SDK API Key Lookup**: The SDK queries the `_User` collection using the configured SDK API key to get the developer ID
2. **User Collection Query**: Searches for users where `apiKey` matches the configured `PAPR_MEMORY_API_KEY`
3. **Metadata-based Resolution**:
   - **If `metadata.user_id` is provided**: Use this user_id directly in QueryLog
   - **If `metadata.user_id` is not provided**: Use developer ID (auto-resolved from SDK API key)
4. **Default Fallback**: If resolution fails, uses "default_user"

```python
# Case 1: metadata.user_id provided -> use this user_id directly
from papr_memory.types import MemoryMetadata

client.memory.search(
    query="specific user search",
    metadata=MemoryMetadata(user_id="specific-user-456")  # Will log with this user_id
)

# Case 2: no metadata.user_id -> use developer ID (auto-resolved from API key)
client.memory.search(
    query="developer search"  # Will log with developer ID
)

# Case 3: metadata provided but no user_id -> use developer ID
client.memory.search(
    query="search with other metadata",
    metadata=MemoryMetadata(location="office")  # Will log with developer ID
)
```

## Advanced Usage with User Context

```python
# The SDK automatically logs with resolved user IDs
# User resolution happens in background thread (non-blocking)
```

## Logging Behavior

### Automatic Logging
- Logs are created automatically for every on-device search
- Non-blocking: logging doesn't affect search performance
- Graceful failure: continues working even if Parse Server is unavailable

### Log Levels
- **INFO**: Basic retrieval metrics and timing
- **DEBUG**: Detailed embedding and ChromaDB metrics
- **WARNING**: Parse Server connection issues

### File Logging
When `PAPR_LOG_FILE` is set, metrics are also written to a local file:

```json
{
  "type": "retrieval_metrics",
  "data": {
    "timestamp": "2025-01-13T10:30:00.000Z",
    "query": "Find information about recent projects",
    "performance": {
      "total_latency_ms": 58.67,
      "embedding_latency_ms": 45.23,
      "chromadb_latency_ms": 12.45
    },
    "search_results": {
      "num_results": 5,
      "embedding_dimensions": 2560
    },
    "model_info": {
      "model_name": "Qwen/Qwen3-Embedding-4B",
      "device_type": "cuda"
    }
  }
}
```

## Troubleshooting

### Parse Server Connection Issues
```
WARNING - Parse Server logging disabled (missing configuration)
```
**Solution**: Set the required environment variables.

### Authentication Errors
```
ERROR - Error sending to Parse Server: 401 Unauthorized
```
**Solution**: Check your `PAPR_PARSE_MASTER_KEY` or `PAPR_PARSE_API_KEY`.

### Network Timeouts
```
ERROR - Error sending to Parse Server: timeout
```
**Solution**: Check your Parse Server URL and network connectivity.

## Benefits

1. **Unified Logging**: Same database for server-side and on-device metrics
2. **Performance Analysis**: Compare server vs on-device performance
3. **User Analytics**: Track how users interact with on-device features
4. **Debugging**: Detailed metrics for troubleshooting performance issues
5. **Compliance**: Maintain audit trails for data processing

## Security Considerations

- Parse Server credentials should be stored securely
- Use environment variables or secure configuration management
- Consider using API keys instead of master keys for production
- Ensure Parse Server is properly secured and accessible only to authorized clients
