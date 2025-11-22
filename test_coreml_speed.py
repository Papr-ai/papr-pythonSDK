#!/usr/bin/env python3
"""
Enhanced CoreML performance test with ANE detection
Tests different compute unit configurations to verify ANE usage
"""

import os
import platform
import time
import numpy as np

# Set the CoreML model path
coreml_model_path = os.environ.get(
    "PAPR_COREML_MODEL",
    "/Users/shawkatkabbara/Documents/GitHub/papr-pythonSDK/coreml/Qwen3-Embedding-4B-FP16-Final.mlpackage"
)

print("🧪 CoreML Performance Test with ANE Detection\n")
print(f"Model: {coreml_model_path}\n")

# System info
print("="*60)
print("📱 System Information")
print("="*60)
print(f"Platform: {platform.system()}")
print(f"Machine: {platform.machine()}")
if platform.system() == "Darwin":
    print(f"macOS: {platform.mac_ver()[0]}")
    if platform.machine() == "arm64":
        print("✅ Apple Silicon detected - ANE available")
    else:
        print("⚠️  Intel Mac - ANE availability depends on T2 chip")
print()

try:
    import coremltools as ct
    from transformers import AutoTokenizer

    print("="*60)
    print("🔬 Testing Different Compute Unit Configurations")
    print("="*60)
    print()

    # Load tokenizer once
    print("📦 Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-Embedding-4B")
    print("✅ Tokenizer loaded\n")

    # Prepare test input
    test_text = "This is a test query for measuring inference speed"
    enc = tokenizer(
        [test_text],
        padding="max_length",
        max_length=32,
        truncation=True,
        return_tensors="np",
    )
    feed = {
        "input_ids": enc["input_ids"].astype(np.int32),
        "attention_mask": enc["attention_mask"].astype(np.int32),
    }

    # Test configurations
    configs = [
        (ct.ComputeUnit.ALL, "ALL (CPU + GPU + ANE)", "Lets CoreML choose best compute unit"),
        (ct.ComputeUnit.CPU_AND_NE, "CPU_AND_NE (CPU + ANE only)", "Forces ANE usage, excludes GPU"),
        (ct.ComputeUnit.CPU_AND_GPU, "CPU_AND_GPU (no ANE)", "GPU only, for comparison"),
        (ct.ComputeUnit.CPU_ONLY, "CPU_ONLY", "CPU only, slowest option"),
    ]

    results = {}

    for compute_unit, name, description in configs:
        print(f"{'='*60}")
        print(f"Testing: {name}")
        print(f"Description: {description}")
        print(f"{'='*60}")

        try:
            # Load model with specific compute unit
            print("Loading model...")
            load_start = time.time()
            mlmodel = ct.models.MLModel(coreml_model_path, compute_units=compute_unit)
            load_time = time.time() - load_start
            print(f"✅ Model loaded in {load_time:.2f}s")

            # Try to get configuration info
            try:
                config = mlmodel.get_spec()
                print(f"   Model compute_units attribute: {compute_unit}")
            except:
                pass

            # Warmup runs (CoreML compilation happens here)
            print("\n🔥 Warmup (3 iterations)...")
            for i in range(3):
                _ = mlmodel.predict(feed)
                print(f"   Warmup {i+1}/3 completed")

            # Timed runs
            print("\n⏱️  Timed runs (10 iterations)...")
            timings = []
            for i in range(10):
                start = time.perf_counter()
                out = mlmodel.predict(feed)
                duration = (time.perf_counter() - start) * 1000  # ms
                timings.append(duration)
                if i < 3:  # Show first 3
                    print(f"   Run {i+1}: {duration:.2f}ms")

            avg_time = np.mean(timings)
            std_time = np.std(timings)
            min_time = np.min(timings)
            max_time = np.max(timings)

            print(f"\n📊 Results:")
            print(f"   Average: {avg_time:.2f}ms (±{std_time:.2f}ms)")
            print(f"   Min: {min_time:.2f}ms")
            print(f"   Max: {max_time:.2f}ms")

            results[name] = {
                'avg': avg_time,
                'std': std_time,
                'min': min_time,
                'max': max_time,
                'unit': compute_unit
            }

            # Clean up
            del mlmodel

        except Exception as e:
            print(f"❌ Error testing {name}: {e}")
            results[name] = None

        print()

    # Summary
    print("="*60)
    print("📊 PERFORMANCE COMPARISON")
    print("="*60)
    
    valid_results = {k: v for k, v in results.items() if v is not None}
    
    for name, res in valid_results.items():
        print(f"{name:35s}: {res['avg']:7.2f}ms (±{res['std']:.2f}ms)")

    print()

    # Analysis
    print("="*60)
    print("🔬 ANE USAGE ANALYSIS")
    print("="*60)

    if all(k in valid_results for k in ["CPU_AND_NE (CPU + ANE only)", "CPU_AND_GPU (no ANE)"]):
        ane_time = valid_results["CPU_AND_NE (CPU + ANE only)"]['avg']
        gpu_time = valid_results["CPU_AND_GPU (no ANE)"]['avg']

        print(f"\nANE Time:  {ane_time:.2f}ms")
        print(f"GPU Time:  {gpu_time:.2f}ms")
        print(f"Speedup:   {gpu_time/ane_time:.2f}x")

        if ane_time < 150:
            print("\n✅ ANE IS ACTIVE AND PERFORMING WELL!")
            print("   - Latency <150ms indicates ANE usage")
            print("   - This is optimal performance for FP16 models")
        elif ane_time < gpu_time * 0.9:
            print("\n✅ ANE IS FASTER THAN GPU")
            print(f"   - ANE provides {(gpu_time/ane_time - 1)*100:.1f}% speedup")
            print("   - Model is using ANE successfully")
        elif ane_time < gpu_time * 1.1:
            print("\n⚠️  ANE AND GPU HAVE SIMILAR PERFORMANCE")
            print("   - Difference is minimal")
            print("   - Both compute units work well for this model")
        else:
            print("\n❌ GPU IS FASTER THAN ANE")
            print(f"   - GPU is {(ane_time/gpu_time - 1)*100:.1f}% faster")
            print("   - Model may not be optimized for ANE")
            print("\n   Possible causes:")
            print("   1. Model has operations not supported by ANE")
            print("   2. Model needs reconversion with newer coremltools")
            print("   3. Model is too large for ANE")

    # Recommendations
    print("\n" + "="*60)
    print("💡 RECOMMENDATIONS")
    print("="*60)

    if valid_results:
        fastest = min(valid_results.items(), key=lambda x: x[1]['avg'])
        print(f"\n🏆 Fastest configuration: {fastest[0]}")
        print(f"   Average latency: {fastest[1]['avg']:.2f}ms")

        if "ALL" in fastest[0]:
            print("\n✅ Use ct.ComputeUnit.ALL in production")
            print("   - Lets CoreML choose optimal compute unit")
            print("   - Best overall performance")
        elif "CPU_AND_NE" in fastest[0]:
            print("\n✅ Use ct.ComputeUnit.CPU_AND_NE in production")
            print("   - Forces ANE usage")
            print("   - Best for FP16 models on Apple Silicon")

        # Check if model is using SDK correctly
        print("\n📝 For SDK usage in other repos:")
        print("   1. Ensure PAPR_ENABLE_COREML=true is set")
        print("   2. Ensure PAPR_COREML_MODEL points to correct model path")
        print("   3. Verify model is FP16 (this one is)")
        print("   4. Check that coremltools version matches (see below)")

    # Version info
    print("\n" + "="*60)
    print("📦 VERSION INFORMATION")
    print("="*60)
    print(f"coremltools: {ct.__version__}")
    
    try:
        import transformers
        print(f"transformers: {transformers.__version__}")
    except:
        pass

except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()
