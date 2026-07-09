"""Vector store / retriever.

The DEFAULT retriever is a pure-Python TF-IDF vectoriser with cosine
similarity — no numpy, no pip, works fully offline. An abstract ``Retriever``
interface makes the backend pluggable so a real embeddings model
(``sentence-transformers``) can be swapped in later without touching the
pipeline. That optional backend is ``EmbeddingRetriever`` at the bottom of this
file, guarded by try/except.
"""
from __future__ import annotations

import json
import math
import re
from abc import ABC, abstractmethod
from collections import Counter
from pathlib import Path

from .ingest import Chunk

_TOKEN_RE = re.compile(r"[a-z0-9]+")

# A small English stop-word list. Removing these focuses TF-IDF on content words.
STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "has",
    "he", "in", "is", "it", "its", "of", "on", "that", "the", "to", "was",
    "were", "will", "with", "this", "these", "those", "or", "but", "if",
    "then", "than", "so", "such", "can", "could", "would", "should", "do",
    "does", "did", "not", "no", "yes", "you", "your", "we", "our", "they",
    "their", "i", "me", "my", "which", "who", "whom", "what", "when", "where",
    "how", "why", "there", "here", "into", "over", "under", "about",
}


def tokenize(text: str) -> list[str]:
    """Lower-case, split into alphanumeric tokens, drop stop-words."""
    return [t for t in _TOKEN_RE.findall(text.lower()) if t not in STOP_WORDS]


class Retriever(ABC):
    """Pluggable retriever interface.

    Any backend (TF-IDF, embeddings, external vector DB) implements ``fit`` and
    ``query`` so the RAG pipeline can stay backend-agnostic.
    """

    @abstractmethod
    def fit(self, chunks: list[Chunk]) -> "Retriever":
        ...

    @abstractmethod
    def query(self, question: str, top_k: int = 4) -> list[tuple[Chunk, float]]:
        """Return the ``top_k`` most relevant ``(chunk, score)`` pairs."""
        ...


class TfidfRetriever(Retriever):
    """Pure-Python TF-IDF + cosine similarity retriever (stdlib only)."""

    def __init__(self) -> None:
        self.chunks: list[Chunk] = []
        self._doc_vectors: list[dict[str, float]] = []
        self._doc_norms: list[float] = []
        self._idf: dict[str, float] = {}
        self._fitted = False

    # ---- fitting -------------------------------------------------------
    def fit(self, chunks: list[Chunk]) -> "TfidfRetriever":
        self.chunks = list(chunks)
        n_docs = len(self.chunks)
        if n_docs == 0:
            self._fitted = True
            return self

        # Document frequency per term.
        doc_freq: Counter[str] = Counter()
        tokenized_docs: list[list[str]] = []
        for chunk in self.chunks:
            tokens = tokenize(chunk.text)
            tokenized_docs.append(tokens)
            for term in set(tokens):
                doc_freq[term] += 1

        # Smoothed inverse document frequency.
        self._idf = {
            term: math.log((1 + n_docs) / (1 + df)) + 1.0
            for term, df in doc_freq.items()
        }

        # Per-document TF-IDF vectors and their L2 norms.
        self._doc_vectors = []
        self._doc_norms = []
        for tokens in tokenized_docs:
            vec = self._vectorize(tokens)
            self._doc_vectors.append(vec)
            self._doc_norms.append(_norm(vec))

        self._fitted = True
        return self

    def _vectorize(self, tokens: list[str]) -> dict[str, float]:
        """Turn a token list into a sparse TF-IDF vector (term -> weight)."""
        if not tokens:
            return {}
        counts = Counter(tokens)
        total = len(tokens)
        vec: dict[str, float] = {}
        for term, count in counts.items():
            idf = self._idf.get(term)
            if idf is None:
                continue  # unseen term at query time contributes nothing
            tf = count / total
            vec[term] = tf * idf
        return vec

    # ---- querying ------------------------------------------------------
    def query(self, question: str, top_k: int = 4) -> list[tuple[Chunk, float]]:
        if not self._fitted:
            raise RuntimeError("TfidfRetriever.query called before fit()")
        if not self.chunks:
            return []

        q_vec = self._vectorize(tokenize(question))
        q_norm = _norm(q_vec)
        if q_norm == 0.0:
            return []

        scored: list[tuple[Chunk, float]] = []
        for chunk, d_vec, d_norm in zip(self.chunks, self._doc_vectors, self._doc_norms):
            if d_norm == 0.0:
                continue
            sim = _cosine(q_vec, q_norm, d_vec, d_norm)
            if sim > 0.0:
                scored.append((chunk, sim))

        scored.sort(key=lambda pair: pair[1], reverse=True)
        return scored[:top_k]

    # ---- persistence (handy for a real deployment) ---------------------
    def save(self, path: str | Path) -> None:
        payload = {
            "chunks": [c.to_dict() for c in self.chunks],
            "idf": self._idf,
        }
        Path(path).write_text(json.dumps(payload), encoding="utf-8")


def _norm(vec: dict[str, float]) -> float:
    return math.sqrt(sum(w * w for w in vec.values()))


def _cosine(
    a: dict[str, float], a_norm: float, b: dict[str, float], b_norm: float
) -> float:
    # Iterate over the smaller vector for efficiency.
    if len(a) > len(b):
        a, b = b, a
    dot = sum(w * b.get(term, 0.0) for term, w in a.items())
    denom = a_norm * b_norm
    return dot / denom if denom else 0.0


# ---------------------------------------------------------------------------
# OPTIONAL: real dense-embeddings backend. Import is guarded so the core
# pipeline never depends on it. Requires: pip install sentence-transformers
# ---------------------------------------------------------------------------
class EmbeddingRetriever(Retriever):
    """Optional dense retriever backed by sentence-transformers.

    Kept behind the same ``Retriever`` interface so it is a drop-in replacement
    for ``TfidfRetriever``. Not imported at module load; the heavy dependency is
    only touched when this class is actually instantiated.
    """

    def __init__(self, model_name: str = "all-MiniLM-L6-v2") -> None:
        try:
            from sentence_transformers import SentenceTransformer  # type: ignore
        except ImportError as exc:  # pragma: no cover - optional path
            raise ImportError(
                "EmbeddingRetriever requires sentence-transformers. "
                "Install with: pip install sentence-transformers"
            ) from exc
        self._model = SentenceTransformer(model_name)
        self.chunks: list[Chunk] = []
        self._embeddings = None

    def fit(self, chunks: list[Chunk]) -> "EmbeddingRetriever":  # pragma: no cover
        self.chunks = list(chunks)
        texts = [c.text for c in self.chunks]
        self._embeddings = self._model.encode(texts, normalize_embeddings=True)
        return self

    def query(self, question: str, top_k: int = 4):  # pragma: no cover
        q = self._model.encode([question], normalize_embeddings=True)[0]
        scored = []
        for chunk, emb in zip(self.chunks, self._embeddings):
            sim = float(sum(a * b for a, b in zip(q, emb)))  # cosine (normalised)
            scored.append((chunk, sim))
        scored.sort(key=lambda pair: pair[1], reverse=True)
        return scored[:top_k]


def build_retriever(backend: str = "tfidf", **kwargs) -> Retriever:
    """Factory: return a retriever for the requested backend.

    ``backend='tfidf'`` (default) is the stdlib-only path. ``backend='embedding'``
    uses the optional sentence-transformers backend.
    """
    backend = backend.lower()
    if backend == "tfidf":
        return TfidfRetriever()
    if backend in {"embedding", "embeddings", "sentence-transformers"}:
        return EmbeddingRetriever(**kwargs)
    raise ValueError(f"unknown retriever backend: {backend!r}")
