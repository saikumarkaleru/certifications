"""Document ingestion: load, clean, and chunk text with overlap.

Stdlib only. Reads ``.txt`` and ``.md`` files from a directory, normalises
whitespace, and splits each document into overlapping word-based chunks. Each
chunk carries metadata (source path, chunk index, char span) so the pipeline
can cite exactly where an answer came from.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Iterable

# File extensions we know how to read as plain text.
SUPPORTED_SUFFIXES = {".txt", ".md", ".markdown"}


@dataclass
class Chunk:
    """A single retrievable chunk of text plus provenance metadata."""

    text: str
    source: str          # relative path of the source document
    chunk_index: int      # position of this chunk within its document
    start_word: int       # word offset where the chunk begins
    end_word: int         # word offset where the chunk ends (exclusive)

    @property
    def chunk_id(self) -> str:
        return f"{self.source}#{self.chunk_index}"

    def to_dict(self) -> dict:
        d = asdict(self)
        d["chunk_id"] = self.chunk_id
        return d


def clean_text(raw: str) -> str:
    """Normalise a raw document into clean prose.

    - strips Markdown heading markers, emphasis and code fences,
    - collapses runs of whitespace,
    - drops empty lines.
    """
    text = raw.replace("\r\n", "\n").replace("\r", "\n")
    # Remove fenced code blocks entirely (```...```): they are usually not prose.
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    lines = []
    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        # Strip common Markdown leading tokens: #, >, -, *, digits.
        line = re.sub(r"^#{1,6}\s*", "", line)      # headings
        line = re.sub(r"^>\s*", "", line)            # blockquotes
        line = re.sub(r"^[-*+]\s+", "", line)        # bullet markers
        line = re.sub(r"^\d+\.\s+", "", line)        # numbered lists
        # Strip inline emphasis / inline-code markers but keep the words.
        line = line.replace("**", "").replace("`", "").replace("*", "")
        lines.append(line)
    text = " ".join(lines)
    # Collapse any remaining whitespace runs.
    text = re.sub(r"\s+", " ", text).strip()
    return text


def chunk_text(
    text: str,
    source: str,
    chunk_size: int = 120,
    overlap: int = 30,
) -> list[Chunk]:
    """Split cleaned ``text`` into overlapping word-based chunks.

    ``chunk_size`` and ``overlap`` are measured in words. A sliding window steps
    forward by ``chunk_size - overlap`` words each time, so consecutive chunks
    share ``overlap`` words. Overlap avoids splitting an answer across a hard
    boundary and losing it at retrieval time.
    """
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must satisfy 0 <= overlap < chunk_size")

    words = text.split()
    if not words:
        return []

    step = chunk_size - overlap
    chunks: list[Chunk] = []
    idx = 0
    start = 0
    while start < len(words):
        end = min(start + chunk_size, len(words))
        piece = " ".join(words[start:end])
        chunks.append(
            Chunk(
                text=piece,
                source=source,
                chunk_index=idx,
                start_word=start,
                end_word=end,
            )
        )
        idx += 1
        if end == len(words):
            break
        start += step
    return chunks


def iter_documents(directory: str | Path) -> Iterable[tuple[str, str]]:
    """Yield ``(relative_path, raw_text)`` for each supported doc under ``directory``."""
    root = Path(directory)
    if not root.exists():
        raise FileNotFoundError(f"ingest directory not found: {root}")
    for path in sorted(root.rglob("*")):
        if path.is_file() and path.suffix.lower() in SUPPORTED_SUFFIXES:
            rel = path.relative_to(root).as_posix()
            yield rel, path.read_text(encoding="utf-8", errors="replace")


def ingest_directory(
    directory: str | Path,
    chunk_size: int = 120,
    overlap: int = 30,
) -> list[Chunk]:
    """Load, clean and chunk every supported document under ``directory``."""
    all_chunks: list[Chunk] = []
    for rel, raw in iter_documents(directory):
        cleaned = clean_text(raw)
        all_chunks.extend(chunk_text(cleaned, rel, chunk_size, overlap))
    return all_chunks
