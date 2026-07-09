"""The RAG pipeline: retrieve -> build grounded prompt -> generate -> cite.

This ties the pieces together:
1. ingest documents into chunks,
2. fit a retriever (default TF-IDF),
3. for a question, retrieve top-k chunks,
4. build a grounded prompt that includes numbered sources,
5. call the LLM provider (default MockLLM),
6. return the answer plus the cited source chunks.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from .ingest import Chunk, ingest_directory
from .llm import LLMProvider, get_provider
from .vectorstore import Retriever, build_retriever


@dataclass
class Source:
    """A cited source chunk returned alongside an answer."""

    marker: int          # the [n] citation number shown in the prompt
    chunk_id: str
    source: str
    score: float
    text: str

    def to_dict(self) -> dict:
        return {
            "marker": self.marker,
            "chunk_id": self.chunk_id,
            "source": self.source,
            "score": round(self.score, 4),
            "text": self.text,
        }


@dataclass
class Answer:
    """The result of a RAG query."""

    question: str
    answer: str
    sources: list[Source]
    provider: str

    def to_dict(self) -> dict:
        return {
            "question": self.question,
            "answer": self.answer,
            "provider": self.provider,
            "sources": [s.to_dict() for s in self.sources],
        }


PROMPT_TEMPLATE = """\
Answer the question using ONLY the numbered context below. If the answer is not
contained in the context, say you don't know. Cite the sources you use with
their [n] markers.

Context:
{context}

Question: {question}

Answer:"""


class RAGPipeline:
    """End-to-end RAG orchestration with a pluggable retriever and LLM."""

    def __init__(
        self,
        retriever: Retriever | None = None,
        provider: LLMProvider | None = None,
        top_k: int = 4,
    ) -> None:
        self.retriever = retriever or build_retriever("tfidf")
        self.provider = provider or get_provider()
        self.top_k = top_k
        self._indexed = False

    # ---- indexing ------------------------------------------------------
    def index_chunks(self, chunks: list[Chunk]) -> "RAGPipeline":
        self.retriever.fit(chunks)
        self._indexed = True
        return self

    def index_directory(
        self, directory: str | Path, chunk_size: int = 120, overlap: int = 30
    ) -> "RAGPipeline":
        chunks = ingest_directory(directory, chunk_size, overlap)
        return self.index_chunks(chunks)

    # ---- prompt construction ------------------------------------------
    @staticmethod
    def build_prompt(question: str, retrieved: list[tuple[Chunk, float]]) -> tuple[str, str]:
        """Build the grounded prompt. Returns ``(prompt, context_block)``."""
        blocks = []
        for i, (chunk, _score) in enumerate(retrieved, start=1):
            blocks.append(f"[{i}] (source: {chunk.source}) {chunk.text}")
        context = "\n\n".join(blocks)
        prompt = PROMPT_TEMPLATE.format(context=context, question=question)
        return prompt, context

    # ---- query ---------------------------------------------------------
    def ask(self, question: str, top_k: int | None = None) -> Answer:
        if not self._indexed:
            raise RuntimeError("pipeline is not indexed; call index_directory/index_chunks first")
        k = top_k or self.top_k
        retrieved = self.retriever.query(question, top_k=k)

        if not retrieved:
            return Answer(
                question=question,
                answer="I could not find relevant information in the provided documents.",
                sources=[],
                provider=self.provider.name,
            )

        prompt, context = self.build_prompt(question, retrieved)
        answer_text = self.provider.generate(prompt, question, context)

        sources = [
            Source(
                marker=i,
                chunk_id=chunk.chunk_id,
                source=chunk.source,
                score=score,
                text=chunk.text,
            )
            for i, (chunk, score) in enumerate(retrieved, start=1)
        ]
        return Answer(
            question=question,
            answer=answer_text,
            sources=sources,
            provider=self.provider.name,
        )


def save_answer(answer: Answer, path: str | Path) -> None:
    Path(path).write_text(json.dumps(answer.to_dict(), indent=2), encoding="utf-8")
