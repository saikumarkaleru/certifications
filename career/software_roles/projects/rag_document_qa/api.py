"""OPTIONAL FastAPI app exposing the RAG pipeline over HTTP.

This file is optional to run. FastAPI/uvicorn are NOT required by the core
pipeline or tests. Install extras first:

    pip install fastapi uvicorn

Then run:

    uvicorn api:app --reload

Endpoints:
    POST /ingest  {"directory": "data"}          -> index a folder
    POST /query   {"question": "...", "top_k": 4} -> grounded answer + sources
    GET  /health                                  -> liveness probe

The import of FastAPI is guarded so that merely importing this module does not
crash in an environment without FastAPI installed; a clear error is raised only
if you actually try to build the app without the dependency.
"""
from __future__ import annotations

import os

try:
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel
    _FASTAPI_AVAILABLE = True
except ImportError:  # pragma: no cover - optional path
    _FASTAPI_AVAILABLE = False

from rag.llm import get_provider
from rag.pipeline import RAGPipeline
from rag.vectorstore import build_retriever


def create_app():
    """Build the FastAPI app. Raises a clear error if FastAPI is missing."""
    if not _FASTAPI_AVAILABLE:  # pragma: no cover - optional path
        raise ImportError(
            "FastAPI is not installed. Run: pip install fastapi uvicorn"
        )

    app = FastAPI(title="RAG Document QA", version="1.0.0")

    # A single in-memory pipeline for the process lifetime.
    state: dict[str, RAGPipeline] = {}

    def _pipeline() -> RAGPipeline:
        if "pipeline" not in state:
            state["pipeline"] = RAGPipeline(
                retriever=build_retriever(os.environ.get("RAG_BACKEND", "tfidf")),
                provider=get_provider(),
            )
        return state["pipeline"]

    class IngestRequest(BaseModel):
        directory: str = "data"
        chunk_size: int = 120
        overlap: int = 30

    class QueryRequest(BaseModel):
        question: str
        top_k: int = 4

    @app.get("/health")
    def health():
        return {"status": "ok"}

    @app.post("/ingest")
    def ingest(req: IngestRequest):
        try:
            pipe = _pipeline()
            pipe.index_directory(req.directory, req.chunk_size, req.overlap)
        except FileNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc))
        n_chunks = len(pipe.retriever.chunks)  # type: ignore[attr-defined]
        return {"status": "indexed", "chunks": n_chunks}

    @app.post("/query")
    def query(req: QueryRequest):
        pipe = _pipeline()
        try:
            answer = pipe.ask(req.question, top_k=req.top_k)
        except RuntimeError as exc:
            raise HTTPException(status_code=400, detail=str(exc))
        return answer.to_dict()

    return app


# uvicorn looks for a module-level ``app``. Only create it when FastAPI exists.
if _FASTAPI_AVAILABLE:  # pragma: no cover - optional path
    app = create_app()
