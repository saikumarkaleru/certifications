"""Command-line interface for the RAG system.

Usage:
    python -m rag.cli ingest <dir>        # build an index from a folder
    python -m rag.cli ask "question"      # query the index
    python -m rag.cli demo <dir>          # ingest + ask a few sample questions

The index is persisted as a small JSON file of chunks (default ``.rag_index.json``).
Because TF-IDF fitting is cheap, ``ask`` simply reloads the chunks and re-fits
the retriever — no heavyweight vector DB needed for a stdlib-only demo.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .ingest import Chunk, ingest_directory
from .llm import get_provider
from .pipeline import RAGPipeline
from .vectorstore import build_retriever

DEFAULT_INDEX = ".rag_index.json"


def _save_chunks(chunks: list[Chunk], path: str) -> None:
    payload = {"chunks": [c.to_dict() for c in chunks]}
    Path(path).write_text(json.dumps(payload), encoding="utf-8")


def _load_chunks(path: str) -> list[Chunk]:
    if not Path(path).exists():
        raise FileNotFoundError(
            f"index not found at {path!r}. Run `python -m rag.cli ingest <dir>` first."
        )
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    chunks = []
    for d in data["chunks"]:
        chunks.append(
            Chunk(
                text=d["text"],
                source=d["source"],
                chunk_index=d["chunk_index"],
                start_word=d["start_word"],
                end_word=d["end_word"],
            )
        )
    return chunks


def cmd_ingest(args: argparse.Namespace) -> int:
    chunks = ingest_directory(args.directory, args.chunk_size, args.overlap)
    if not chunks:
        print(f"No .txt/.md documents found under {args.directory!r}", file=sys.stderr)
        return 1
    _save_chunks(chunks, args.index)
    n_docs = len({c.source for c in chunks})
    print(f"Ingested {n_docs} document(s) -> {len(chunks)} chunk(s). Index: {args.index}")
    return 0


def _build_pipeline_from_index(args: argparse.Namespace) -> RAGPipeline:
    chunks = _load_chunks(args.index)
    retriever = build_retriever(args.backend)
    provider = get_provider(args.provider)
    pipeline = RAGPipeline(retriever=retriever, provider=provider, top_k=args.top_k)
    pipeline.index_chunks(chunks)
    return pipeline


def _print_answer(answer, show_sources: bool = True) -> None:
    print(f"\nQ: {answer.question}")
    print(f"A: {answer.answer}")
    if show_sources and answer.sources:
        print(f"\nSources (provider={answer.provider}):")
        for s in answer.sources:
            preview = s.text[:140] + ("..." if len(s.text) > 140 else "")
            print(f"  [{s.marker}] {s.source} (score={s.score:.3f}) {preview}")


def cmd_ask(args: argparse.Namespace) -> int:
    pipeline = _build_pipeline_from_index(args)
    answer = pipeline.ask(args.question)
    if args.json:
        print(json.dumps(answer.to_dict(), indent=2))
    else:
        _print_answer(answer)
    return 0


def cmd_demo(args: argparse.Namespace) -> int:
    # Ingest fresh, then answer a few canned questions end-to-end.
    chunks = ingest_directory(args.directory, args.chunk_size, args.overlap)
    if not chunks:
        print(f"No documents under {args.directory!r}", file=sys.stderr)
        return 1
    retriever = build_retriever(args.backend)
    provider = get_provider(args.provider)
    pipeline = RAGPipeline(retriever=retriever, provider=provider, top_k=args.top_k)
    pipeline.index_chunks(chunks)

    n_docs = len({c.source for c in chunks})
    print(f"Indexed {n_docs} document(s) / {len(chunks)} chunk(s) "
          f"[retriever={args.backend}, provider={provider.name}]")

    questions = args.questions or [
        "What is retrieval-augmented generation?",
        "How does chunking with overlap help retrieval?",
        "What is the difference between TF-IDF and dense embeddings?",
    ]
    for q in questions:
        answer = pipeline.ask(q)
        _print_answer(answer)
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="rag.cli", description="Stdlib-only RAG document QA")
    p.add_argument("--index", default=DEFAULT_INDEX, help="path to the index JSON file")
    p.add_argument("--backend", default="tfidf", help="retriever backend (tfidf|embedding)")
    p.add_argument("--provider", default=None, help="LLM provider (mock|openai|anthropic)")
    p.add_argument("--top-k", type=int, default=4, help="number of chunks to retrieve")
    p.add_argument("--chunk-size", type=int, default=120, help="chunk size in words")
    p.add_argument("--overlap", type=int, default=30, help="chunk overlap in words")

    sub = p.add_subparsers(dest="command", required=True)

    p_ingest = sub.add_parser("ingest", help="ingest a directory into an index")
    p_ingest.add_argument("directory", help="folder of .txt/.md documents")
    p_ingest.set_defaults(func=cmd_ingest)

    p_ask = sub.add_parser("ask", help="ask a question against the index")
    p_ask.add_argument("question", help="the question to answer")
    p_ask.add_argument("--json", action="store_true", help="print JSON output")
    p_ask.set_defaults(func=cmd_ask)

    p_demo = sub.add_parser("demo", help="ingest + ask sample questions end-to-end")
    p_demo.add_argument("directory", help="folder of .txt/.md documents")
    p_demo.add_argument("questions", nargs="*", help="optional custom questions")
    p_demo.set_defaults(func=cmd_demo)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
