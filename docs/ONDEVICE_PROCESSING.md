# On-Device Processing Control

The Papr Memory SDK now supports configurable on-device processing through the `PAPR_ONDEVICE_PROCESSING` environment variable.

## Environment Variable

### `PAPR_ONDEVICE_PROCESSING`

Controls whether to enable on-device processing features like local ChromaDB storage, embedding generation, and tier0 data search.

**Default:** `false` (disabled)

**Values:**
- `true`, `1`, `yes`, `on` → Enable on-device processing
- `false`, `0`, `no`, `off` → Disable on-device processing

## Features

### When ENABLED:
- ✅ **ChromaDB collection created** during client initialization
- ✅ **Tier0 data stored locally** for fast retrieval
- ✅ **Local embedding generation** using platform-optimized models
- ✅ **Local tier0 search** for enhanced search context
- ✅ **Reduced API calls** - only one sync_tiers call per client
- ✅ **Better privacy** - data stays on your device
- ✅ **Faster subsequent searches** - no repeated setup

### When DISABLED:
- ✅ **Lower memory usage** - no local storage
- ✅ **Faster initial setup** - no ChromaDB initialization
- ✅ **No local dependencies** - works without ChromaDB/sentence-transformers
- ✅ **API-only mode** - all processing on server
- ❌ **Slower searches** - API calls for everything
- ❌ **More API calls** - repeated sync_tiers calls

## Usage Examples

### Enable On-Device Processing
```bash
# Set environment variable
export PAPR_ONDEVICE_PROCESSING=true

# Or in Python
import os
os.environ["PAPR_ONDEVICE_PROCESSING"] = "true"

# Create client
from papr_memory import Papr
client = Papr(x_api_key="your-key")
```

### Disable On-Device Processing
```bash
# Set environment variable
export PAPR_ONDEVICE_PROCESSING=false

# Or in Python
import os
os.environ["PAPR_ONDEVICE_PROCESSING"] = "false"

# Create client
from papr_memory import Papr
client = Papr(x_api_key="your-key")
```

## Platform Optimization

When on-device processing is enabled, the SDK automatically detects your platform and uses the optimal configuration:

### Apple Silicon (M1/M2/M3/M4)
- **NPU Priority:** Uses Neural Engine NPU via MPS
- **Model:** `mlx-community/Qwen3-Embedding-4B-4bit-DWQ`
- **Performance:** ~0.05-0.15s per embedding

### NVIDIA GPU
- **GPU Priority:** Uses CUDA acceleration
- **Model:** `Qwen/Qwen3-Embedding-4B`
- **Performance:** ~0.10-0.25s per embedding

### Intel/AMD
- **XPU/HIP Priority:** Uses Intel XPU or AMD HIP
- **Model:** `Qwen/Qwen3-Embedding-4B`
- **Performance:** ~0.15-0.30s per embedding

### CPU Fallback
- **CPU Processing:** Uses CPU for all operations
- **Model:** `Qwen/Qwen3-Embedding-4B`
- **Performance:** ~0.50-2.00s per embedding

## Old Platform Detection

The SDK automatically detects older platforms and disables local processing:

- **Old Intel Macs** (pre-Apple Silicon)
- **M1 with < 16GB RAM**
- **< 4 CPU cores**
- **< 8GB total RAM**

## Debug Output

### On-Device Processing Enabled:
```
📊 On-device processing enabled - initializing sync_tiers and ChromaDB collection...
📊 Attempting to import ChromaDB...
📊 ChromaDB imported successfully
📊 Creating ChromaDB client...
📊 Initialized ChromaDB client
📊 Created new ChromaDB collection: tier0_goals_okrs
📊 Using embeddings from server response...
📊 Valid server embedding for item 0 (dim: 4096)
📊 Added 2 documents with local embeddings
📊 Client initialization completed successfully
```

### On-Device Processing Disabled:
```
📊 On-device processing disabled - using API-only mode
```

### Search with Local Enhancement:
```
📊 Using 3 tier0 items for search context enhancement
✅ Found 5 memories
🔗 Found 3 graph nodes
```

### Search without Local Enhancement:
```
📊 On-device processing disabled - using API-only search
✅ Found 5 memories
🔗 Found 3 graph nodes
```

## Dependencies

### Required for On-Device Processing:
```bash
pip install chromadb sentence-transformers psutil
```

### Optional (for better performance):
```bash
# For Apple Silicon
pip install mlx

# For NVIDIA GPU
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# For Intel XPU
pip install intel-extension-for-pytorch
```

## Troubleshooting

### ChromaDB Import Error:
```
📊 ChromaDB not available - install with: pip install chromadb
```
**Solution:** `pip install chromadb`

### Sentence Transformers Error:
```
📊 sentence-transformers not available - install with: pip install sentence-transformers
```
**Solution:** `pip install sentence-transformers`

### Platform Detection Issues:
```
📊 Platform detected as too old - skipping local embedding generation
```
**Solution:** Set `PAPR_ONDEVICE_PROCESSING=false` to use API-only mode

### Memory Issues:
```
📊 Insufficient RAM (6.2GB) - using API instead of local processing
```
**Solution:** Set `PAPR_ONDEVICE_PROCESSING=false` or upgrade hardware

## Performance Comparison

| Mode | Initial Setup | Search Speed | Memory Usage | API Calls |
|------|---------------|--------------|--------------|-----------|
| On-Device | 2-5s | Fast (0.1-0.5s) | High (1-2GB) | Low (1 per client) |
| API-Only | 0.1s | Medium (1-3s) | Low (50-100MB) | High (1 per search) |

Choose the mode that best fits your use case!
