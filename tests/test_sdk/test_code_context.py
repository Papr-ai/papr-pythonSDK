import subprocess

from papr_memory.lib import CodeContext, git_blob_sha


class Fake:
    def __init__(self, responses=None):
        self.responses = responses or {}
        self.calls = []

    def post(self, path, *, body, cast_to=None):
        self.calls.append((path, body))
        r = self.responses.get(path)
        return r(body) if callable(r) else r


def test_git_blob_sha_matches_git():
    assert git_blob_sha("") == "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391"
    text = "export const beta = 2\n"
    try:
        git = subprocess.run(["git", "hash-object", "--stdin"], input=text.encode(), capture_output=True, check=True).stdout.decode().strip()
    except Exception:
        git = None
    if git:
        assert git_blob_sha(text) == git
    assert git_blob_sha(text.encode()) == git_blob_sha(text)


def test_add_builds_items_and_maps_results():
    f = Fake({"/v1/memory/batch": {"successful": [{"data": [{"memoryId": "p1"}]}], "errors": [{"index": 1, "error": "dimensions"}]}})
    out = CodeContext(f, "papr-embed-code-1-0.6b").add([
        {"content": "a", "blob_sha": "a" * 40, "embedding": [1.0, 0.0], "path_hint": "src/a.py"},
        {"content": "b", "blob_sha": "b" * 40},
    ])
    assert out == {"ids": ["p1"], "errors": [{"index": 1, "error": "dimensions"}]}
    cc = f.calls[0][1]["memories"][0]["code_context"]
    assert cc["embed_model"] == "papr-embed-code-1-0.6b" and cc["chunk"] == 0 and cc["store_content"] is False
    assert "embedding" not in f.calls[0][1]["memories"][1]["code_context"]  # None fields dropped -> server embeds


def test_add_batches_by_256_and_offsets_errors():
    n = {"i": 0}

    def resp(_b):
        n["i"] += 1
        return {"errors": [{"index": 3, "error": "x"}]} if n["i"] == 2 else {"successful": []}

    f = Fake({"/v1/memory/batch": resp})
    out = CodeContext(f, "m").add([{"content": str(i), "blob_sha": "c" * 40, "chunk": i} for i in range(300)])
    assert len(f.calls) == 2 and len(f.calls[1][1]["memories"]) == 44
    assert out["errors"][0]["index"] == 259


def test_search_maps_hits():
    f = Fake({"/v1/memory/search": {"data": {"memories": [{"id": "p1", "content": "", "customMetadata": {
        "score": 0.9, "blob_sha": "a" * 40, "chunk": 2, "line_start": 10, "line_end": 40, "path_hint": "x.py"}}]}}})
    hits = CodeContext(f, "m").search("q", query_embedding=[1.0], repo_ids=["r"], limit=5)
    assert hits[0]["line_start"] == 10 and hits[0]["content"] is None and hits[0]["path_hint"] == "x.py"
    assert f.calls[0][1]["code_search"] == {"embed_model": "m", "query_embedding": [1.0], "repo_ids": ["r"], "limit": 5}


def test_missing_dedupes_and_chunks():
    f = Fake({"/v1/memory/code/missing": lambda b: {"missing": b["blob_shas"][:1]}})
    shas = [format(i, "040x") for i in range(6000)]
    out = CodeContext(f, "m").missing(shas + [shas[0].upper()])
    assert len(f.calls) == 2 and len(out) == 2
