# On-Device Processing Setup

This guide explains how to enable and configure on-device memory processing with local embeddings.

## Installation

### Basic Installation (API-only)
```bash
pip install papr-memory
```

### With On-Device Processing
```bash
pip install papr-memory[ondevice]
```

This installs:
- `chromadb>=0.4.0` - Local vector database
- `sentence-transformers>=2.0.0` - Embedding models
- `psutil>=5.8.0` - System resource monitoring

### With CoreML (Recommended for Apple Silicon)
```bash
pip install papr-memory[ondevice,coreml]
```

Additional dependencies for optimized Mac performance:
- `coremltools>=7.0` - CoreML model conversion
- `transformers>=4.44` - HuggingFace transformers
- `torch==2.5.*` - PyTorch (pinned version)
- `huggingface_hub>=0.20.0` - Model downloading

## Configuration

Copy the `.env.example` to `.env` and configure:

```bash
cp .env.example .env
```

### Environment Variables

#### Required (for API access)
```bash
PAPR_MEMORY_API_KEY=your_papr_api_key_here
PAPR_BASE_URL=https://api.papr.ai
```

#### On-Device Processing (Optional)
```bash
# Enable local processing
PAPR_ONDEVICE_PROCESSING=true

# Maximum number of tier-0 memories to keep locally
PAPR_MAX_TIER0=30

# Sync interval in seconds
PAPR_SYNC_INTERVAL=30

# Skip server-side processing entirely (local-only mode)
PAPR_ONDEVICE_ONLY=false
```

#### CoreML Configuration (Apple Silicon)
```bash
# Enable CoreML acceleration
PAPR_ENABLE_COREML=true

# Optional: Path to pre-converted CoreML model
# If not specified, models auto-download from HuggingFace
PAPR_COREML_MODEL=/path/to/model.mlpackage
```

#### System Configuration
```bash
# Prevent tokenizer warnings
TOKENIZERS_PARALLELISM=false

# Optional: HuggingFace token for downloading models
HUGGINGFACE_HUB_TOKEN=your_hf_token_here
```

## Usage

```python
import os
from papr_memory import PaprMemory

# Initialize client
client = PaprMemory(
    api_key=os.environ.get("PAPR_MEMORY_API_KEY"),
    base_url=os.environ.get("PAPR_BASE_URL")
)

# Add memories - will be processed locally if PAPR_ONDEVICE_PROCESSING=true
response = client.memory.add(
    content="Your memory content here"
)

# Search memories - uses local embeddings if available
results = client.memory.search(
    query="What do I remember about...",
    max_memories=20
)
```

## How It Works

When `PAPR_ONDEVICE_PROCESSING=true`:

1. **Local Embedding Generation**: Text is embedded locally using:
   - CoreML models on Apple Silicon (fastest)
   - MLX models on Apple Silicon (alternative)
   - Sentence Transformers on other platforms (CPU/CUDA)

2. **Local Vector Storage**: Embeddings stored in ChromaDB locally

3. **Tiered Storage**:
   - Tier 0: Most recent/important memories kept locally
   - Older memories synced to server
   - Configurable with `PAPR_MAX_TIER0`

4. **Background Sync**: Periodically syncs with server (configurable with `PAPR_SYNC_INTERVAL`)

## Platform-Specific Notes

### Apple Silicon (M1/M2/M3)
- **Recommended**: Use CoreML for 3-5x faster embeddings
- Models auto-download on first run
- Requires `papr-memory[ondevice,coreml]`

### Linux/Windows
- Uses sentence-transformers with CUDA (if available) or CPU
- Requires `papr-memory[ondevice]`

### GPU Acceleration
- CUDA automatically detected on Linux/Windows
- MPS (Metal) automatically used on macOS

## Troubleshooting

### Import Errors
If you see `Import "sentence_transformers" could not be resolved`:
```bash
pip install papr-memory[ondevice]
```

### Model Download Issues
If models fail to download:
1. Check internet connection
2. Set `HUGGINGFACE_HUB_TOKEN` if using gated models
3. Manually specify model path with `PAPR_COREML_MODEL`

### Memory Issues
If running out of memory:
- Reduce `PAPR_MAX_TIER0` (default: 30)
- Use smaller embedding models
- Increase `PAPR_SYNC_INTERVAL` to sync less frequently

## Cleanup

To remove local data:
```bash
papr-cleanup
```

This removes ChromaDB and cached models.
