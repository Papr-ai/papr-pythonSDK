# Technical Architecture: Automatic Memory Pressure Handling for CoreML on macOS

**Status:** Design Phase
**Created:** 2025-10-20
**Related:** agent.md Learning 8, Learning 13

## Overview

This design introduces automatic memory pressure detection and mitigation to prevent CoreML models from falling back to CPU execution (50s) instead of Apple Neural Engine (100ms) when the system is under memory pressure.

## Problem Statement

**Current Situation:**
- CoreML models run on ANE with ~100ms latency under normal conditions
- Under memory pressure (201M swapins/223M swapouts), models fall back to CPU with ~50s latency (500x degradation)
- Manual fix requires: clearing `~/Library/Caches/com.apple.CoreML`, restarting app, and running `sudo purge`
- No automatic detection or mitigation exists

**Root Cause:**
- macOS memory pressure from system caches, hidden processes, and swap activity
- CoreML compilation cache becomes stale or unusable under pressure
- ANE fails to allocate resources, forcing CPU fallback

## Key Insights from agent.md

**Learning 8: Memory Management for Core ML Quantization**
- macOS reports memory as "free" even when consumed by hidden processes and caches
- Heavy swap activity (184M swapins, 235M swapouts) indicates memory pressure
- Docker containers, IDE extensions, CoreML cache can consume significant RAM
- Cleanup required: Clear CoreML cache, clear app caches, force memory purge

**Learning 13: Alignment Restores FP16 Accuracy to ~FP32**
- Expected latency: ~106-145 ms/query on Apple Silicon with FP16
- This performance is only achievable when ANE is active
- Memory pressure prevents ANE usage, causing massive degradation

## Solution Design

### Components

#### 1. Memory Pressure Detector (`src/papr_memory/_memory_pressure.py`)
- Detect macOS memory pressure using `memory_pressure` command
- Parse swap activity from `vm_stat`
- Check available RAM and swap usage
- Provide cross-platform compatibility (no-op on non-macOS)

#### 2. CoreML Cache Manager (`src/papr_memory/_coreml_cache.py`)
- Locate CoreML cache directory (`~/Library/Caches/com.apple.CoreML`)
- Clear cache safely without affecting other applications
- Log cache size and clearing actions
- Handle permissions gracefully

#### 3. Model Loading Interceptor (in `src/papr_memory/resources/memory.py`)
- Check memory pressure before `ct.models.MLModel()` call
- Automatically clear CoreML cache if pressure detected
- Retry model loading after cache clear
- Fall back to API if issues persist

### Data Flow

```
1. User initiates search
   ↓
2. Memory pressure check (pre-flight)
   ↓
3a. Normal pressure → Load CoreML model → ANE execution (100ms)
   ↓
3b. High pressure → Clear CoreML cache → Retry load → ANE execution
   ↓
3c. Persistent issues → Fall back to API → Warn developer
```

## Implementation Plan

### Phase 1: Foundation (Memory Pressure Detection)
**Files:** `src/papr_memory/_memory_pressure.py`

**Tasks:**
1. Create memory pressure module with `is_macos()`, `get_memory_pressure_macos()`, `check_memory_pressure()`
2. Add swap activity parsing from `vm_stat`
3. Add logging and warnings for different pressure levels

**Acceptance Criteria:**
- Correctly detects memory pressure levels on macOS
- Detects >100M swap pages as pressure
- Clear, actionable warnings displayed

### Phase 2: Cache Management
**Files:** `src/papr_memory/_coreml_cache.py`

**Tasks:**
1. Create cache management module with `get_coreml_cache_dir()`, `get_cache_size()`, `clear_coreml_cache()`
2. Add permission handling
3. Add cache size reporting

**Acceptance Criteria:**
- Safely clears CoreML cache on macOS
- No crashes on permission denied
- Accurate size reporting in logs

### Phase 3: Integration
**Files:** `src/papr_memory/resources/memory.py`

**Tasks:**
1. Add `_load_coreml_model_with_pressure_check()` method
2. Integrate with existing model loading (replace line 703)
3. Add retry logic

**Acceptance Criteria:**
- Pressure check runs before every model load
- Existing code works unchanged
- Graceful degradation on failures

### Phase 4: Testing & Polish
**Tasks:**
1. Unit tests for memory pressure detection
2. Unit tests for cache clearing
3. Integration tests with real CoreML model
4. Update documentation (ENV_VARIABLES.md, agent.md, README.md)

**Acceptance Criteria:**
- >90% code coverage
- ANE stays active under simulated pressure
- Clear docs for developers

## Technical Decisions

### Decision 1: Automatic vs Manual Cache Clearing
**Chosen:** Automatic with manual override option

**Rationale:**
- Developer experience: No manual intervention needed
- Performance: Prevents 500x degradation automatically
- Safety: Cache clearing is safe (CoreML recompiles)
- Based on agent.md Learning 3: "Core ML Caches Compiled Models Aggressively"

### Decision 2: Platform Detection Strategy
**Chosen:** Explicit macOS checks, no-op on other platforms

**Rationale:**
- Memory pressure tools are macOS-specific
- Won't break Linux/Windows
- No overhead on non-macOS platforms

### Decision 3: Pressure Thresholds
**Chosen:** 40% free = WARN, 20% free = CRITICAL, >100M swap pages = WARN

**Rationale:**
- Based on agent.md Learning 8: 201M swapins caused issues
- macOS "free" memory is misleading (includes compressed/purgeable)
- Conservative thresholds prevent false negatives

### Decision 4: No sudo Required
**Chosen:** Use user-accessible cache clearing only

**Rationale:**
- Can't run sudo without password
- `~/Library/Caches/com.apple.CoreML` is user-writable
- `sudo purge` helps but not required (per agent.md Learning 8)

## Key Code Changes

### New File: `src/papr_memory/_memory_pressure.py`

```python
def check_memory_pressure() -> Dict[str, Any]:
    """
    Cross-platform memory pressure check.

    Returns memory pressure info dict with:
    - level: "normal" | "warn" | "critical"
    - free_percent: float (0-100)
    - swap_used_gb: float
    - page_ins: int
    - page_outs: int
    - reason: str
    """
```

### New File: `src/papr_memory/_coreml_cache.py`

```python
def clear_coreml_cache(force: bool = False) -> bool:
    """
    Clear CoreML compiled model cache.

    This is safe - CoreML will recompile models on next load.
    The recompilation happens once and is cached again.

    Based on agent.md Learning 3.
    """
```

### Modified: `src/papr_memory/resources/memory.py`

```python
def _load_coreml_model_with_pressure_check(self, coreml_path: str) -> object:
    """
    Load CoreML model with automatic memory pressure handling.

    Prevents ANE fallback to CPU by clearing CoreML cache
    if memory pressure is detected before loading.

    Based on agent.md Learning 8 and Learning 13.
    """
    # Check memory pressure before loading
    pressure_info = check_memory_pressure()

    # Clear cache if memory pressure detected
    if should_clear_coreml_cache(pressure_info):
        log_memory_pressure_warning(pressure_info)
        clear_coreml_cache()

    # Load the model
    return ct.models.MLModel(coreml_path, compute_units=ct.ComputeUnit.ALL)
```

## Success Metrics

1. **Performance:** ANE latency maintained <150ms under memory pressure
2. **Reliability:** <1% fallback to CPU execution in production
3. **Developer Experience:** Zero manual intervention required
4. **Compatibility:** 100% backward compatible with existing code
5. **Transparency:** Clear logging of all automatic actions

## Example Usage

```python
# Before (manual intervention required)
# Developer notices slow performance (50s)
# Developer runs: rm -rf ~/Library/Caches/com.apple.CoreML
# Developer restarts app
# Developer runs: sudo purge
# Performance restored (100ms)

# After (automatic)
from papr_memory import Papr

client = Papr(x_api_key=os.environ["PAPR_MEMORY_API_KEY"])

# First search (model loading)
# ⚠️  Memory pressure detected: Low free memory (35.2%)
#    Clearing CoreML cache as precaution...
# ✅ CoreML cache cleared successfully (1.2 GB freed)
# Loading CoreML model...
# ✅ CoreML model loaded successfully
# Search: 105ms  ← ANE performance maintained!
```

## References

- **agent.md Learning 3:** Core ML Caches Compiled Models Aggressively
- **agent.md Learning 8:** Memory Management for Core ML Quantization
- **agent.md Learning 13:** Alignment Restores FP16 Accuracy to ~FP32
- **Apple Documentation:** [Core ML Performance](https://developer.apple.com/documentation/coreml/core_ml_api/reducing_the_size_of_your_core_ml_app)

## Next Steps

1. Implement Phase 1 (Memory Pressure Detection)
2. Implement Phase 2 (Cache Management)
3. Implement Phase 3 (Integration)
4. Add comprehensive tests
5. Update agent.md with Learning 14: Automatic Memory Pressure Handling
6. Deploy to production and monitor metrics

---

**Last Updated:** 2025-10-20
**Status:** Design Complete, Ready for Implementation
