# Logging in Papr Memory SDK

The Papr Memory SDK uses proper Python logging instead of print statements for better debugging, monitoring, and production use.

## Logging Configuration

### Environment Variables

- **`PAPR_LOG_LEVEL`**: Set the logging level (DEBUG, INFO, WARNING, ERROR)
- **`PAPR_LOG_FILE`**: Optional path to log file. If not set, logs go to console
- **`PAPR_ONDEVICE_PROCESSING`**: Enable/disable on-device processing (affects log messages)
- **`PAPR_CHROMADB_PATH`**: Path for ChromaDB persistent storage (default: `./chroma_db`)

### Log Levels

| Level | Description | Use Case |
|-------|-------------|----------|
| **DEBUG** | Detailed information for debugging | Development, troubleshooting |
| **INFO** | General information about operations | Production monitoring |
| **WARNING** | Warning messages for potential issues | Production monitoring |
| **ERROR** | Error messages for failures | Error tracking |

## Usage Examples

### Basic Logging Setup

```python
import logging
from papr_memory import Papr

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Create client
client = Papr(x_api_key="your-key")
```

### Environment Variable Control

```bash
# Set log level via environment variable
export PAPR_LOG_LEVEL=DEBUG
python your_script.py

# Log to a file
export PAPR_LOG_FILE="/path/to/papr.log"
export PAPR_LOG_LEVEL=INFO
python your_script.py

# Combine both
export PAPR_LOG_LEVEL=DEBUG
export PAPR_LOG_FILE="./logs/papr_debug.log"
python your_script.py

# Configure ChromaDB persistent storage
export PAPR_CHROMADB_PATH="/path/to/persistent/chromadb"
export PAPR_ONDEVICE_PROCESSING=true
python your_script.py
```

```python
import os
os.environ["PAPR_LOG_LEVEL"] = "INFO"
os.environ["PAPR_LOG_FILE"] = "/tmp/papr.log"
os.environ["PAPR_CHROMADB_PATH"] = "/home/user/chromadb_data"
```

### Programmatic Control

```python
import logging

# Get the Papr logger
logger = logging.getLogger("papr_memory")

# Set level
logger.setLevel(logging.DEBUG)

# Add custom handler
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
```

## Log Message Categories

### Client Initialization

```
2024-01-15 10:30:15 - papr_memory._client - INFO - Initializing sync_tiers and ChromaDB collection
2024-01-15 10:30:16 - papr_memory._client - INFO - Client initialization completed successfully
```

### On-Device Processing

```
2024-01-15 10:30:15 - papr_memory._client - INFO - On-device processing enabled
2024-01-15 10:30:15 - papr_memory._client - INFO - On-device processing disabled - using API-only mode
```

### ChromaDB Operations

```
2024-01-15 10:30:16 - papr_memory.resources.memory - INFO - Initializing ChromaDB client
2024-01-15 10:30:16 - papr_memory.resources.memory - INFO - ChromaDB client initialized successfully
2024-01-15 10:30:16 - papr_memory.resources.memory - INFO - ChromaDB collection created: tier0_goals_okrs
```

### Embedding Generation

```
2024-01-15 10:30:17 - papr_memory.resources.memory - INFO - Generating local embeddings
2024-01-15 10:30:18 - papr_memory.resources.memory - INFO - Generated local embedding (dim: 4096)
```

### Search Operations

```
2024-01-15 10:30:20 - papr_memory.resources.memory - INFO - Using 3 tier0 items for search context enhancement
2024-01-15 10:30:21 - papr_memory.resources.memory - INFO - Found 5 memories and 3 graph nodes
```

## Production Logging

### Recommended Setup

```python
import logging
import sys
from papr_memory import Papr

# Production logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('papr_memory.log')
    ]
)

# Create client
client = Papr(x_api_key="your-key")
```

### Docker Logging

```dockerfile
# Dockerfile
ENV PAPR_LOG_LEVEL=INFO
ENV PAPR_ONDEVICE_PROCESSING=false

# Run with logging
CMD ["python", "your_app.py"]
```

### Kubernetes Logging

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: papr-app
spec:
  template:
    spec:
      containers:
      - name: papr-app
        image: your-app:latest
        env:
        - name: PAPR_LOG_LEVEL
          value: "INFO"
        - name: PAPR_ONDEVICE_PROCESSING
          value: "false"
```

## Log Filtering

### Filter by Component

```python
import logging

# Only show Papr logs
logging.getLogger("papr_memory").setLevel(logging.INFO)

# Hide other libraries
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("chromadb").setLevel(logging.WARNING)
```

### Filter by Level

```python
import logging

# Only show warnings and errors
logging.getLogger("papr_memory").setLevel(logging.WARNING)
```

## Log Analysis

### Common Log Patterns

**Successful On-Device Processing:**
```
INFO - On-device processing enabled
INFO - Initializing ChromaDB client
INFO - ChromaDB client initialized successfully
INFO - ChromaDB collection created: tier0_goals_okrs
INFO - Using 3 tier0 items for search context enhancement
```

**API-Only Mode:**
```
INFO - On-device processing disabled - using API-only mode
INFO - On-device processing disabled - using API-only search
```

**Error Scenarios:**
```
WARNING - Failed to initialize sync_tiers during client setup: ChromaDB not available
WARNING - Client will still work, but local search features may be limited
```

## Benefits of Proper Logging

### ✅ Production Ready
- **Structured messages** - Easy to parse and analyze
- **Configurable levels** - Control verbosity
- **Timestamps** - Track operation timing
- **Source information** - Know which component logged

### ✅ Debugging
- **Detailed information** - DEBUG level shows everything
- **Error tracking** - WARNING and ERROR levels
- **Performance monitoring** - Track operation timing

### ✅ Monitoring
- **Log aggregation** - Send to ELK, Splunk, etc.
- **Alerting** - Set up alerts on ERROR messages
- **Metrics** - Extract performance data

### ✅ Clean Code
- **No print pollution** - Clean console output
- **Professional logging** - Industry standard approach
- **Maintainable** - Easy to modify log messages

## Migration from Print Statements

The SDK has been updated to use proper logging instead of print statements:

**Before (Print Statements):**
```python
print("📊 On-device processing enabled")
print("📊 ChromaDB client initialized")
print("📊 Using 3 tier0 items for search")
```

**After (Proper Logging):**
```python
logger.info("On-device processing enabled")
logger.info("ChromaDB client initialized")
logger.info("Using 3 tier0 items for search")
```

This provides better structure, configurability, and production readiness! 🚀
