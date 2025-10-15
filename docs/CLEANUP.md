# Papr SDK Cleanup Guide

## 🧹 ChromaDB Data Cleanup

The Papr SDK stores ChromaDB data locally for fast on-device search. This data persists after package uninstall and should be cleaned up manually.

## 📍 Data Locations

### Default Locations
- **ChromaDB**: `./chroma_db` (current directory)
- **Custom Path**: Set via `PAPR_CHROMADB_PATH` environment variable

### Other Papr Data
- **Cache**: `~/.cache/papr`
- **Config**: `~/.papr`
- **Custom**: `./papr_data`, `./papr_cache`

## 🛠️ Cleanup Methods

### 1. Command Line Cleanup
```bash
# Clean ChromaDB data only
papr-cleanup

# Clean all Papr data
papr-cleanup --all
```

### 2. Python API Cleanup
```python
from papr_memory._cleanup import cleanup_chromadb, cleanup_all_papr_data

# Clean ChromaDB only
cleanup_chromadb()

# Clean all Papr data
cleanup_all_papr_data()
```

### 3. Application Integration
```python
import atexit
from papr_memory._cleanup import cleanup_chromadb

# Register cleanup on application exit
atexit.register(cleanup_chromadb)

# Your application code
client = Papr(x_api_key="your-key")
```

## ⚠️ Important Notes

### **Automatic Cleanup on Uninstall**
✅ **ChromaDB data is automatically cleaned up** when you uninstall the package:
```bash
pip uninstall papr_memory
# ChromaDB data is automatically removed
```

### **Manual Cleanup (Optional)**
If you want to clean up before uninstalling:
```bash
# Clean up manually (optional)
papr-cleanup

# Then uninstall
pip uninstall papr_memory
```

### **Data Safety**
- **ChromaDB Data**: Contains your tier0 embeddings and search index
- **Cache Data**: Temporary files and model cache
- **Config Data**: SDK configuration and settings

### **Custom Paths**
```bash
# Set custom ChromaDB path
export PAPR_CHROMADB_PATH="/custom/path/to/chromadb"
papr-cleanup
```

## 🔄 Development Workflow

### **Testing**
```bash
# Clean up after testing
papr-cleanup --all
```

### **Production**
```python
# Clean up on application shutdown
try:
    client = Papr(x_api_key="your-key")
    # ... your code
finally:
    from papr_memory._cleanup import cleanup_chromadb
    cleanup_chromadb()
```

## 📊 Cleanup Commands

| Command | Purpose | Data Removed |
|---------|---------|--------------|
| `papr-cleanup` | ChromaDB only | ChromaDB data directory |
| `papr-cleanup --all` | All Papr data | ChromaDB, cache, config |
| `python -c "from papr_memory._cleanup import cleanup_chromadb; cleanup_chromadb()"` | Programmatic | ChromaDB data directory |

## 🚨 Troubleshooting

### **Permission Errors**
```bash
# Make sure you have write permissions
sudo papr-cleanup
```

### **Custom Paths**
```bash
# Check current ChromaDB path
echo $PAPR_CHROMADB_PATH

# Set custom path
export PAPR_CHROMADB_PATH="/your/custom/path"
papr-cleanup
```

### **Manual Cleanup**
```bash
# Remove ChromaDB directory manually
rm -rf ./chroma_db

# Remove all Papr data
rm -rf ./chroma_db ~/.cache/papr ~/.papr
```
