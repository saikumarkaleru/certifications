# RAG Document QA

A Retrieval-Augmented Generation (RAG) document question-answering system.
Point it at a folder of documents, ask a question in natural language, and get
back an answer **grounded** in those documents with **citations** to the exact
source chunks.

The core pipeline runs on the **Python standard library only** — no `pip
install`, no API key, no internet. That makes it reproducible and easy to run
anywhere. Real-LLM providers (OpenAI, Anthropic), an HTTP API (FastAPI), and a
dense-embeddings retriever (sentence-transformers) are all **optional** drop-in
upgrades.

---

## What is RAG (in one paragraph)

A plain LLM answers from the frozen knowledge in its weights, so it cannot cite
sources and may hallucinate on private or recent data. RAG fixes this by adding
a **retrieval** step in front of **generation**: for each question we search an
index of document chunks, pull the most relevant ones, drop them into the prompt
as numbered context, and instruct the model to answer **only** from that
context. The result is grounded, auditable, and updatable just by changing the
documents.

```
question ─▶ [retriever] ─▶ top-k chunks ─▶ [prompt builder] ─▶ grounded prompt
                                                                     │
                                                                     ▼
                     answer + cited sources  ◀──────────────  [LLM provider]
```

---

## Architecture

| Module               | Responsibility                                                              |
| -------------------- | --------------------------------------------------------------------------- |
| `rag/ingest.py`      | Load `.txt`/`.md`, clean, chunk with word overlap, attach per-chunk metadata |
| `rag/vectorstore.py` | Pluggable `Retriever`; **default** pure-Python TF-IDF + cosine similarity    |
| `rag/llm.py`         | `LLMProvider` interface: **MockLLM** (default), `OpenAIProvider`, `AnthropicProvider` |
| `rag/pipeline.py`    | Orchestration: retrieve → build grounded prompt → generate → return answer + sources |
| `rag/cli.py`         | `ingest`, `ask`, and `demo` commands                                        |
| `api.py`             | **Optional** FastAPI app (`/ingest`, `/query`, `/health`)                   |
| `data/`              | 5 sample documents about RAG concepts                                        |
| `tests/`             | 25 `unittest` cases: chunking, retrieval, full pipeline                      |

Everything talks through two small interfaces — `Retriever` and `LLMProvider` —
so the retrieval backend and the LLM backend can each be swapped independently
without touching the pipeline.

---

## Quick start (zero dependencies, fully offline)

Requires only Python 3.10+ (developed and verified on 3.12 / 3.13).

```bash
# 1. Build an index from the sample docs
python -m rag.cli ingest data

# 2. Ask questions (uses the deterministic MockLLM — no API key needed)
python -m rag.cli ask "What is retrieval-augmented generation?"
python -m rag.cli ask "How does overlap help when chunking documents?"
python -m rag.cli ask "What is the difference between TF-IDF and dense embeddings?"

# JSON output (answer + structured sources)
python -m rag.cli ask "What is cosine similarity?" --json

# One-shot end-to-end demo (ingest + several questions)
python -m rag.cli demo data
```

Run the tests:

```bash
python -m unittest discover -s tests
```

Docker (also stdlib-only; the build runs the tests):

```bash
docker build -t rag-qa .
docker run --rm rag-qa
```

---

## Plugging in a real LLM

The system selects a provider from the `LLM_PROVIDER` env var (default `mock`).

**OpenAI**
```bash
pip install openai
export LLM_PROVIDER=openai
export OPENAI_API_KEY=sk-...
python -m rag.cli ask "What is retrieval-augmented generation?"
```

**Anthropic**
```bash
pip install anthropic
export LLM_PROVIDER=anthropic
export ANTHROPIC_API_KEY=sk-ant-...
python -m rag.cli ask "What is retrieval-augmented generation?"
```

Both providers use the **same grounded prompt** the MockLLM sees, with a system
message that instructs the model to answer only from the context, admit when it
doesn't know, and cite `[n]` markers. Imports are guarded, so the code never
fails to load when a package or key is absent — the error is raised only if you
explicitly select that provider.

See `.env.example` for all configuration options.

---

## Plugging in dense embeddings

The default retriever is pure-Python TF-IDF. To use semantic embeddings:

```bash
pip install sentence-transformers
```

```python
from rag.vectorstore import build_retriever
retriever = build_retriever("embedding")   # sentence-transformers backend
```

`EmbeddingRetriever` implements the same `Retriever` interface as
`TfidfRetriever`, so the pipeline is unchanged.

---

## Optional HTTP API

```bash
pip install fastapi uvicorn
uvicorn api:app --reload
```

```bash
curl -X POST localhost:8000/ingest -H 'content-type: application/json' \
     -d '{"directory": "data"}'

curl -X POST localhost:8000/query  -H 'content-type: application/json' \
     -d '{"question": "What is chunking?", "top_k": 3}'
```

`api.py` guards the FastAPI import, so importing the module never crashes in an
environment without FastAPI; the dependency is only required to actually serve.

---

## What runs offline vs. what needs setup

| Capability                                   | Requirement                          |
| -------------------------------------------- | ------------------------------------ |
| Ingest / chunk / retrieve / answer (MockLLM) | **Nothing** — stdlib only            |
| CLI (`ingest`, `ask`, `demo`) and all tests  | **Nothing** — stdlib only            |
| Real answers via OpenAI                       | `pip install openai` + `OPENAI_API_KEY` |
| Real answers via Anthropic                    | `pip install anthropic` + `ANTHROPIC_API_KEY` |
| Dense-embedding retrieval                     | `pip install sentence-transformers`  |
| HTTP API                                      | `pip install fastapi uvicorn`        |

See `STUDY_GUIDE.md` for RAG concepts and interview Q&A.
