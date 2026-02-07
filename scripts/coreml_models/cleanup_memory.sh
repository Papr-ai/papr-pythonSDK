#!/bin/bash
# Memory cleanup script for preparing INT8 quantization

echo "🧹 Memory Cleanup for INT8 Quantization"
echo "========================================"
echo ""

# Check current memory
echo "📊 Current Memory Status:"
vm_stat | perl -ne '/page size of (\d+)/ and $size=$1; /Pages\s+free[^\d]+(\d+)/ and printf("  Free: %.2f GB\n", $1 * $size / 1073741824);'
echo ""

# 1. Docker containers (optional - skipped by default to keep services running)
echo "1️⃣  Docker Containers:"
if docker ps --format "table {{.Names}}\t{{.Status}}" 2>/dev/null | grep -q "Up"; then
    echo "   Found running containers:"
    docker ps --format "   - {{.Names}} ({{.Status}})"
    echo ""
    echo "   ⏭️  Keeping Docker running (services need to stay up)"
    echo "   💡 Tip: If quantization fails due to OOM, you can stop Docker temporarily with:"
    echo "      docker stop \$(docker ps -q)"
else
    echo "   ℹ️  No Docker containers running"
fi
echo ""

# 2. Clear Core ML caches
echo "2️⃣  Core ML Caches:"
COREML_CACHE=~/Library/Caches/com.apple.CoreML
if [ -d "$COREML_CACHE" ]; then
    CACHE_SIZE=$(du -sh "$COREML_CACHE" 2>/dev/null | cut -f1)
    echo "   Found Core ML cache: $CACHE_SIZE"
    rm -rf "$COREML_CACHE" 2>/dev/null
    echo "   ✅ Core ML cache cleared"
else
    echo "   ℹ️  No Core ML cache found"
fi
echo ""

# 3. Clear ChromaDB
echo "3️⃣  ChromaDB:"
if [ -d "chroma_db" ]; then
    CHROMA_SIZE=$(du -sh chroma_db 2>/dev/null | cut -f1)
    echo "   Found ChromaDB: $CHROMA_SIZE"
    rm -rf chroma_db
    echo "   ✅ ChromaDB cleared"
else
    echo "   ℹ️  No ChromaDB found"
fi
echo ""

# 4. Clear Python caches
echo "4️⃣  Python Caches:"
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null
echo "   ✅ Python caches cleared"
echo ""

# 5. Clear old Core ML models (keep latest)
echo "5️⃣  Old Core ML Models:"
if [ -d "coreml" ]; then
    ls -lh coreml/ 2>/dev/null | grep "mlpackage" | awk '{print "   - " $9 ": " $5}'
    echo ""
    read -p "   Keep existing models? (y/n): " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Nn]$ ]]; then
        rm -rf coreml/*.mlpackage 2>/dev/null
        echo "   ✅ Old models removed"
    else
        echo "   ⏭️  Keeping existing models"
    fi
else
    echo "   ℹ️  No Core ML models directory found"
fi
echo ""

# 6. Force memory purge (macOS)
echo "6️⃣  Purging inactive memory..."
sudo purge 2>/dev/null && echo "   ✅ Memory purged" || echo "   ⚠️  Needs sudo for purge (skip with Ctrl+C)"
echo ""

# Final memory status
echo "📊 Final Memory Status:"
vm_stat | perl -ne '/page size of (\d+)/ and $size=$1; /Pages\s+free[^\d]+(\d+)/ and printf("  Free: %.2f GB\n", $1 * $size / 1073741824);'
memory_pressure | grep "System-wide memory free percentage"
echo ""

echo "✅ Cleanup complete!"
echo ""
echo "🚀 Ready to run INT8 quantization:"
echo "   python scripts/convert_qwen_coreml.py --hf Qwen/Qwen3-Embedding-4B --out ./coreml/Qwen3-Embedding-4B-INT8.mlpackage --int8"

