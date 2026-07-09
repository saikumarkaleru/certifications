# Career Workspace — Saikumar Kaleru

Personal career-preparation workspace for **quantitative / technical finance roles**
(equity research, FP&A, quant & derivatives, risk, technical research), with a focus on
Indian markets (NSE, Nifty / Bank Nifty) alongside US equities and options.

This root folder is **not** a single git repo. Two subfolders are independent GitHub repos
(see below); everything else is unversioned local content.

## Top-level layout

| Folder | What's in it |
|--------|--------------|
| `interview_prep/` | Interview & study prep. `sources_md/` = the 7 markdown source docs (1,064-Q finance Q&A, TRA handbook, study guides, formula/mnemonic sheets, project defenses); `study_pdfs/` = their compiled PDFs (`Finance_Interview_QnA.pdf`, `Technical_Research_Study_Guide.pdf`). |
| `learn/` | Technical-analysis study-guide builder — Python + matplotlib/yfinance generating annotated charts (`img/`) and the illustrated PDF. |
| `projects/` | Role portfolios (Python, live `yfinance` data, unit tests, PDF/Excel outputs): `equity_research_analyst/`, `financial_analyst_fpa/`, `quant_derivatives_analyst/`, `risk_analyst/`, and `software dev team/` (a LangGraph multi-agent SDLC orchestrator). |
| `role_resumes/` | Five role-tailored resumes built from HTML sources (`source/*.html` → PDF), plus `references/` (final resumes, NISM certs, credentials) and `archive/` (older versions). **Git repo.** |
| `trading_learning/` | Self-authored 71-chapter options-trading book + 200-strategy encyclopedia, rendered to a 24 MB PDF. **Git repo.** |

## Git repos

| Folder | Remote |
|--------|--------|
| `role_resumes/` | https://github.com/saikumarkaleru/Resumes.git |
| `trading_learning/` | https://github.com/saikumarkaleru/trading_learning.git |

## How the pieces relate

- `interview_prep/sources_md/` (markdown) → compiled PDFs in `interview_prep/study_pdfs/`.
- `learn/` builds the technical-analysis study guide from the markdown sources and writes the
  PDF into `interview_prep/study_pdfs/`.
- `trading_learning/` assembles and renders the standalone options book.
- `projects/` holds one self-contained portfolio project per target role, each defensible
  with real data and tests.

## Build entry points

- **TA study guide:** `python learn/build_illustrated_handbook.py`
  (reads `interview_prep/sources_md/`, writes to `interview_prep/study_pdfs/`).
- **Options book:** `python trading_learning/assemble_book.py` then
  `python trading_learning/render_book.py` (figures: `make_figures.py`; strategies:
  `strat_engine.py`).
- **Portfolio projects:** each has its own `main.py`, e.g.
  `python projects/equity_research_analyst/1_dcf_valuation/main.py`.
