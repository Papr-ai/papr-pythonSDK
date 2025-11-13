#!/usr/bin/env python3
"""
Quick test to diagnose CoreML performance issues
"""

import os
import time
import numpy as np

# Set the CoreML model path
coreml_model_path = "/Users/shawkatkabbara/Documents/GitHub/papr-pythonSDK/coreml/Qwen3-Embedding-4B-FP16-Final.mlpackage"

print("🧪 CoreML Performance Test\n")
print(f"Model: {coreml_model_path}\n")

try:
    import coremltools as ct
    from transformers import AutoTokenizer

    print("1️⃣ Loading CoreML model...")
    load_start = time.time()

    # Load with ALL compute units (ANE + GPU + CPU)
    mlmodel = ct.models.MLModel(coreml_model_path, compute_units=ct.ComputeUnit.ALL)

    load_time = time.time() - load_start
    print(f"   ✅ Model loaded in {load_time:.2f}s\n")

    # Check compute units
    print("2️⃣ Checking compute configuration...")
    print(f"   Compute units: {mlmodel.compute_unit}\n")

    # Load tokenizer
    print("3️⃣ Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-Embedding-4B")
    print("   ✅ Tokenizer loaded\n")

    # Test inference
    test_text = "This is a test query"

    print("4️⃣ Testing inference (first run - may include compilation)...")
    first_run_start = time.time()

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

    print("   Running prediction...")
    out = mlmodel.predict(feed)

    first_run_time = time.time() - first_run_start
    print(f"   ✅ First run: {first_run_time:.2f}s\n")

    # Test second run (should be cached/compiled)
    print("5️⃣ Testing inference (second run - should be faster)...")
    second_run_start = time.time()

    out = mlmodel.predict(feed)

    second_run_time = time.time() - second_run_start
    print(f"   ✅ Second run: {second_run_time:.2f}s\n")

    # Extract embedding
    print("6️⃣ Checking output...")
    for key, value in out.items():
        arr = np.asarray(value)
        print(f"   Output '{key}': shape={arr.shape}, dtype={arr.dtype}")

    print("\n" + "="*60)
    print("📊 Performance Summary:")
    print("="*60)
    print(f"Model load time:      {load_time:.2f}s")
    print(f"First inference:      {first_run_time:.2f}s")
    print(f"Second inference:     {second_run_time:.2f}s")
    print(f"Expected (ANE/GPU):   <1.0s per inference")

    if second_run_time > 5.0:
        print("\n⚠️  WARNING: Inference is too slow!")
        print("   Possible issues:")
        print("   1. Model not using Neural Engine (ANE)")
        print("   2. Model conversion issue")
        print("   3. Model needs recompilation")
        print("\n   Try:")
        print("   - Check model was converted with correct CoreML tools version")
        print("   - Verify model uses ANE-compatible operations")
        print("   - Reconvert model if needed")
    else:
        print("\n✅ Performance looks good!")

except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()
