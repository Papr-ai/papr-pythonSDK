# CoreML FP16 Evaluation Summary (Qwen3-Embedding-4B)

## Configuration Used
- Model: `Qwen/Qwen3-Embedding-4B`
- CoreML Precision: FP16
- Pooling: attention-masked mean
- Last-N layers averaged: 4
- Fixed length: 32 (`padding='max_length'`, `max_length=32`)
- Normalization: L2
- Clamp: [-65504, 65504]

## Conversion Command
```bash
rye run python scripts/coreml_models/convert_qwen_coreml.py \
  --hf Qwen/Qwen3-Embedding-4B \
  --out ./coreml/Qwen3-Embedding-4B-FP16-Final.mlpackage \
  --fp16 --pooling mean --layers 4 --normalize --max-length 32
```

## Evaluation Command
```bash
PAPR_COREML_MAX_LENGTH=32 rye run python scripts/coreml_models/evaluate_accuracy.py \
  --coreml ./coreml/Qwen3-Embedding-4B-FP16-Final.mlpackage \
  --hf Qwen/Qwen3-Embedding-4B \
  --num-samples 20
```

## Results
- Average cosine similarity: ~1.000000 (≥ 0.999999)
- Average L2 distance: ~1e-3
- Accuracy preservation: ~100.0000%
- CoreML latency: ~106–145 ms/query (Apple Silicon)
- Speedup vs FP32: ~330–430× (first‑load FP32 baseline is very slow)

## Notes
- Accuracy losses seen earlier were due to pipeline mismatch (pooling/normalization/padding), not FP16 quantization.
- Ensure runtime tokenization exactly matches conversion.
- For reproducibility: set `TOKENIZERS_PARALLELISM=false` and `PAPR_COREML_MAX_LENGTH=32`.

