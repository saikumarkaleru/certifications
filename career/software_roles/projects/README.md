# Software Portfolio Projects

Seven real, **verified** projects backing the IT/software resumes in `../resumes/`. Each has a
`README.md` (build/run) and a `STUDY_GUIDE.md` (design rationale + ~20 interview Q&A to defend it).
Build artifacts (venvs, `node_modules`, `build/`, DBs) are git-ignored — recreate with the commands
in each project's README.

| Project | Stack | Backs roles | Verified |
|---------|-------|-------------|----------|
| **low_latency_order_book** | C++20, CMake, pybind11, Python WebSocket + web GUI | C++/Low-Latency, Quant Dev, SDE, Backend | Compiles clean (g++ 15.2); **56/56 test assertions**, ctest 1/1; demo + micro-benchmark run |
| **resilient_microservices_ecommerce** | FastAPI microservices, Docker, Kubernetes, Jenkins | DevOps/SRE, Backend, Full-Stack | **13/13 pytest** (3 services); `docker compose config` valid; 8 k8s manifests parse |
| **rest_api_service** | FastAPI, SQLAlchemy, JWT, pytest, Docker | Backend, SDE | **16/16 pytest**; deps install + smoke test green |
| **data_pipeline_etl** | Python (stdlib), SQLite, SQL, unittest | Data Engineer | Pipeline runs E2E (32→21 rows), **13/13 quality**, idempotent, **20/20 tests**, SQL analytics run |
| **fullstack_web_app** | React + Vite, FastAPI, SQLite, Docker | Full-Stack, Backend | Backend **12/12 pytest**; frontend `npm run build` succeeds |
| **rag_document_qa** | Python (stdlib), TF-IDF retrieval, FastAPI, OpenAI/Anthropic | AI/GenAI Engineer | Runs offline w/ mock LLM (no key); **25/25 tests**; grounded answers with cited sources |
| **llm_agent_toolkit** | Python (stdlib), ReAct agent, tool calling, FastAPI | AI/GenAI Engineer | Runs offline w/ mock LLM (no key); **30/30 tests**; solves multi-step tasks with tools |

## How to run (quick)
- **RAG Q&A (no installs needed):** `cd rag_document_qa && python -m rag.cli ingest data && python -m rag.cli ask "what is RAG?"` (then `python -m unittest discover -s tests`)
- **LLM Agent (no installs needed):** `cd llm_agent_toolkit && python -m agent.cli "what is 12*(3+4)?"` (then `python -m unittest discover -s tests`)
- **Order book:** `cd low_latency_order_book && cmake -S . -B build && cmake --build build && ctest --test-dir build`
- **REST API:** `cd rest_api_service && python -m venv .venv && .venv/Scripts/pip install -r requirements.txt && .venv/Scripts/pytest`
- **ETL (no installs needed):** `cd data_pipeline_etl && python etl/pipeline.py && python -m pytest`
- **Microservices:** `docker compose up` (or per-service `pip install -r requirements.txt && pytest`)
- **Full-stack:** backend `uvicorn app.main:app`; frontend `npm install && npm run dev`

> These are genuine, defensible projects — study each `STUDY_GUIDE.md` before interviews so you can
> explain the design decisions and trade-offs, not just the features.

## Suggested: publish to GitHub
Pushing these to a public GitHub (one repo each, or a portfolio monorepo) and adding the links to your
resumes is the single biggest credibility boost for a fresher software application.
