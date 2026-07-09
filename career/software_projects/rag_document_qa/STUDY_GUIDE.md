# Study Guide — RAG Document QA

A defensible, line-by-line explainable guide to this project. Read this before
an interview; you should be able to explain every design choice below.

---

## 30-second pitch

"I built a Retrieval-Augmented Generation system that answers questions from a
document collection and cites its sources. The whole core pipeline — ingestion,
a TF-IDF retriever I wrote in pure Python, prompt grounding, and an LLM provider
interface — runs on the standard library with no API key, so it's fully
reproducible offline. Real LLMs (OpenAI, Anthropic), dense embeddings, and a
FastAPI service are optional plug-ins behind clean interfaces. It ships with
sample docs and 25 unit tests."

---

## How the pipeline works (walkthrough)

1. **Ingest** (`rag/ingest.py`): read every `.txt`/`.md` file, strip Markdown
   and collapse whitespace (`clean_text`), then split into **overlapping**
   word-based chunks (`chunk_text`). Each `Chunk` records its source file, index,
   and word span so we can cite it later.
2. **Index** (`rag/vectorstore.py`): `TfidfRetriever.fit` tokenises each chunk,
   computes document frequencies, builds smoothed IDF weights, and stores a
   sparse TF-IDF vector plus its L2 norm per chunk.
3. **Retrieve**: `query` vectorises the question the same way and ranks chunks by
   **cosine similarity**, returning the top-k `(chunk, score)` pairs.
4. **Ground** (`rag/pipeline.py`): `build_prompt` formats the retrieved chunks as
   a numbered context block `[1] … [2] …` and wraps them in an instruction that
   says "answer only from this context, cite `[n]`, say you don't know
   otherwise."
5. **Generate** (`rag/llm.py`): the selected `LLMProvider` turns the prompt into
   an answer. The default `MockLLM` is deterministic and extractive (no network);
   `OpenAIProvider` / `AnthropicProvider` call real APIs when configured.
6. **Return**: an `Answer` object with the text, the provider name, and the list
   of cited `Source`s (marker, source file, score, text).

---

## Key design decisions

- **Stdlib-only core.** Guarantees the demo and tests run offline. TF-IDF is a
  genuinely strong lexical baseline, so this isn't a toy — it's the right default.
- **Two interfaces, `Retriever` and `LLMProvider`.** Dependency inversion: the
  pipeline depends on abstractions, so swapping TF-IDF → embeddings or Mock →
  OpenAI touches one line, not the pipeline.
- **Guarded optional imports.** Heavy/networked dependencies are imported inside
  the provider/retriever that needs them, so importing the package never fails.
- **Citations by construction.** Every retrieved chunk gets a `[n]` marker and is
  returned as a structured source, making answers auditable.

---

## Core concepts (be ready to explain each)

**Chunking.** Long docs are split into passages of a few hundred words. Too big →
the relevant sentence is diluted by noise; too small → an answer spanning
sentences gets split and never retrieved whole.

**Overlap.** Consecutive chunks share N words (here `chunk_size - overlap` is the
stride). This keeps ideas near a boundary present in both neighbours so they
aren't lost at retrieval time. Typical: 100–200 word chunks, 10–30% overlap.

**TF-IDF.** Term Frequency × Inverse Document Frequency. TF = how often a term
appears in a chunk (normalised by length); IDF = `log((1+N)/(1+df)) + 1`,
down-weighting common terms and up-weighting rare, informative ones. Fast,
transparent, no training. Weakness: exact-lexical, so "car" ≠ "automobile".

**Dense embeddings.** A neural encoder maps text to a fixed vector where
semantically similar text is nearby, capturing meaning beyond exact words. Cost:
model download + encoding + vector storage. Often used after TF-IDF, or hybrid.

**Cosine similarity.** `dot(a,b) / (|a|·|b|)` — the angle between two vectors,
0 (unrelated) to 1 (same direction). Length-invariant, so it isn't biased by
chunk length. Used by both TF-IDF and embedding retrievers here.

**Grounding.** Constrain the model to answer only from retrieved context, not its
parametric memory. Implemented via the prompt instruction + context block.

**Citations.** Numbered markers tying each claim to a source chunk; the user can
verify rather than trust. The single biggest practical advantage over a bare LLM.

**Hallucination mitigation.** (1) retrieve enough relevant context, (2) instruct
"say I don't know", (3) low temperature, (4) require citations. RAG reduces but
does not eliminate hallucination.

**Evaluation.** Retrieval: recall@k, MRR. Generation: faithfulness (every claim
supported by context) and answer relevance (addresses the question). A simple
offline harness = question/expected-answer pairs, check expected facts appear and
citations point to the right source.

---

## Interview Q&A (18)

**1. What problem does RAG solve?**
LLMs answer from frozen training weights — they can't use private/recent data and
can't cite. RAG injects retrieved, trustworthy context into the prompt, making
answers current, domain-specific, grounded, and auditable.

**2. Walk me through the flow.**
Ingest → chunk → index → (per question) retrieve top-k → build grounded prompt →
LLM generates → return answer + cited sources.

**3. Why did you build TF-IDF from scratch instead of using an embedding model?**
To guarantee an offline, dependency-free, deterministic core that's still a
credible retrieval baseline. Embeddings are a documented optional upgrade behind
the same interface.

**4. How does TF-IDF actually score a chunk?**
Each term's weight = TF (count/length) × IDF (rarity across chunks). Chunk and
query become sparse vectors; relevance = cosine similarity between them.

**5. Why IDF? What does the smoothing do?**
IDF down-weights ubiquitous words so rare, discriminative words dominate. The
`+1`s (`log((1+N)/(1+df))+1`) avoid division by zero and a zero weight when a term
appears in every doc.

**6. Why cosine similarity and not Euclidean distance?**
Cosine measures direction, not magnitude, so it isn't skewed by chunk length or
term-count scale. Two chunks about the same topic score high regardless of size.

**7. Why chunk at all? Why not embed whole documents?**
Retrieval and prompts need focused passages. Whole docs bury the answer in noise
and blow the context window. Chunking localises the signal.

**8. How do you choose chunk size and overlap?**
Trade-off: large chunks dilute, small chunks fragment. I default to ~120 words
with 30-word (25%) overlap. In production you'd tune against an eval set.

**9. What does overlap buy you concretely?**
An idea straddling a boundary appears in both neighbouring chunks, so it's still
retrievable as a unit instead of being cut in half.

**10. How does grounding reduce hallucination?**
The prompt supplies the facts and explicitly forbids answering beyond them and
tells the model to say "I don't know." It constrains the model to evidence.

**11. Does RAG eliminate hallucination?**
No. If retrieval misses or the model ignores instructions it can still err. RAG
reduces risk; citations + low temperature + refusal instructions push it lower.

**12. How are citations implemented here?**
Each retrieved chunk gets a `[n]` marker in the prompt and is returned as a
`Source` (marker, file, score, text). The answer references markers; the caller
can map each back to a document.

**13. How would you evaluate this system?**
Retrieval with recall@k / MRR on labelled query→chunk pairs; generation with
faithfulness and answer-relevance. Start with a small hand-built Q/expected-fact
set run through the pipeline.

**14. How do you swap in a real LLM?**
Set `LLM_PROVIDER=openai|anthropic` and the key; `get_provider` returns that
provider. Same grounded prompt, real generation. Imports are guarded.

**15. How do you swap in embeddings?**
`build_retriever("embedding")` returns `EmbeddingRetriever` (sentence-
transformers), which implements the same `Retriever` interface — the pipeline
doesn't change.

**16. What are the interfaces and why do they matter?**
`Retriever` (fit/query) and `LLMProvider` (generate). They invert dependencies so
backends are interchangeable and independently testable — clean, extensible.

**17. How is the MockLLM deterministic, and why does that matter for tests?**
It scores context sentences by word-overlap with the question and stitches the
top ones — pure function, no randomness/network. Tests assert exact behaviour and
run anywhere.

**18. What would you add for production scale?**
A real vector DB (FAISS/pgvector) with ANN search, hybrid lexical+dense retrieval
with re-ranking, incremental indexing, caching, streaming responses, and an
automated eval pipeline in CI.

**19. Biggest weakness of your current retriever?**
Pure lexical matching — no synonymy/semantics. "auto" won't match "car". That's
exactly what the embedding backend addresses.

**20. Where could this break and how would you guard it?**
Empty/garbage docs (handled: empty index → graceful "no info" answer),
out-of-vocabulary queries (return no sources rather than fabricate), oversized
context (cap top-k / truncate), and provider/key errors (guarded imports + clear
messages).
