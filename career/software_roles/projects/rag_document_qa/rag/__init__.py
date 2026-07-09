"""RAG document QA — a stdlib-only Retrieval-Augmented Generation pipeline.

The core pipeline (ingest, vectorstore, llm, pipeline, cli) runs on the Python
standard library only, so it is guaranteed to work offline with no pip installs.
Optional integrations (FastAPI, OpenAI, Anthropic, sentence-transformers) are
guarded by try/except and documented in the README.
"""

__version__ = "1.0.0"
