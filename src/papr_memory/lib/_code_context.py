"""Code context: sync a local code index with Papr Memory.

Code chunks are content-addressed: (your tenant, embed_model, blob_sha, chunk). Embed on device when you can and send
the vector; the server embeds otherwise. Paths are hints only: keep your own path -> blob_sha manifest and resolve
hits through it, so renames never re-embed and a stale path never points at the wrong file.

    from papr_memory import Papr
    from papr_memory.lib import CodeContext, git_blob_sha

    code = CodeContext(Papr(x_api_key=KEY), "papr-embed-code-1-0.6b")
    sha = git_blob_sha(source)
    if code.missing([sha]):
        code.add([{"content": source, "blob_sha": sha, "embedding": vec, "path_hint": "src/a.py"}])
    hits = code.search("where do we retry cloud sync", query_embedding=qvec, limit=10)
"""
from __future__ import annotations

import hashlib
from typing import Any, Dict, Iterable, List, Optional, Sequence, TypedDict, Union

MAX_BATCH = 256
MAX_SHAS = 5000


class CodeChunk(TypedDict, total=False):
    content: str
    blob_sha: str
    chunk: int
    line_start: int
    line_end: int
    language: str
    symbols: List[str]
    repo_id: str
    path_hint: str
    embedding: List[float]
    store_content: bool


def git_blob_sha(content: Union[str, bytes]) -> str:
    """git's blob id: sha1(b"blob <len>\\0" + content). Matches `git hash-object`."""
    data = content.encode("utf-8") if isinstance(content, str) else bytes(content)
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def _item(model: str, c: CodeChunk) -> Dict[str, Any]:
    start = c.get("line_start", 1)
    ctx = {
        "embed_model": model, "blob_sha": c["blob_sha"], "chunk": c.get("chunk", 0), "line_start": start,
        "line_end": c.get("line_end", max(1, start)), "language": c.get("language"), "symbols": c.get("symbols", []),
        "repo_id": c.get("repo_id"), "path_hint": c.get("path_hint"), "embedding": c.get("embedding"),
        "store_content": c.get("store_content", False),
    }
    return {"content": c["content"], "code_context": {k: v for k, v in ctx.items() if v is not None}}


def _hit(m: Dict[str, Any]) -> Dict[str, Any]:
    md = m.get("customMetadata") or {}
    return {
        "id": m.get("id"), "score": md.get("score"), "blob_sha": md.get("blob_sha"), "chunk": md.get("chunk", 0),
        "line_start": md.get("line_start", 1), "line_end": md.get("line_end", 1), "language": md.get("language"),
        "symbols": md.get("symbols", []), "repo_id": md.get("repo_id"), "path_hint": md.get("path_hint"),
        "content": m.get("content") or None,
    }


def _post(client: Any, path: str, body: Dict[str, Any]) -> Dict[str, Any]:
    res = client.post(path, body=body, cast_to=object)
    return res if isinstance(res, dict) else {}


class CodeContext:
    """Code index sync over the v1 memory routes. ``client`` is a ``Papr`` instance (or anything with ``post``)."""

    def __init__(self, client: Any, embed_model: str):
        self.client = client
        self.embed_model = embed_model

    def add(self, chunks: Sequence[CodeChunk]) -> Dict[str, List[Any]]:
        ids: List[str] = []
        errors: List[Dict[str, Any]] = []
        for i in range(0, len(chunks), MAX_BATCH):
            part = chunks[i:i + MAX_BATCH]
            res = _post(self.client, "/v1/memory/batch", {"memories": [_item(self.embed_model, c) for c in part]})
            for ok in res.get("successful") or []:
                ids += [d["memoryId"] for d in (ok.get("data") or [])]
            for e in res.get("errors") or []:
                errors.append({"index": -1 if e.get("index", -1) < 0 else e["index"] + i, "error": e.get("error")})
        return {"ids": ids, "errors": errors}

    def search(self, query: str, *, query_embedding: Optional[List[float]] = None, repo_ids: Optional[List[str]] = None,
               blob_shas: Optional[List[str]] = None, limit: int = 20, min_score: Optional[float] = None) -> List[Dict[str, Any]]:
        cs = {"embed_model": self.embed_model, "query_embedding": query_embedding, "repo_ids": repo_ids,
              "blob_shas": blob_shas, "limit": limit, "min_score": min_score}
        res = _post(self.client, "/v1/memory/search", {"query": query, "code_search": {k: v for k, v in cs.items() if v is not None}})
        return [_hit(m) for m in ((res.get("data") or {}).get("memories") or [])]

    def missing(self, blob_shas: Iterable[str]) -> List[str]:
        uniq = list(dict.fromkeys(s.lower() for s in blob_shas))
        out: List[str] = []
        for i in range(0, len(uniq), MAX_SHAS):
            res = _post(self.client, "/v1/memory/code/missing", {"embed_model": self.embed_model, "blob_shas": uniq[i:i + MAX_SHAS]})
            out += res.get("missing") or []
        return out

    def delete(self, blob_shas: Sequence[str]) -> None:
        for i in range(0, len(blob_shas), MAX_SHAS):
            _post(self.client, "/v1/memory/code/delete", {"embed_model": self.embed_model, "blob_shas": list(blob_shas[i:i + MAX_SHAS])})
