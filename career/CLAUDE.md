# Project Rules — career repo

## Hard Rule #1: Projects must be MEDIUM level (not easy, not flagship-hard)

All portfolio projects (in `projects/`) must be **medium difficulty**:

- **NOT easy** — no single-file, hard-coded, ~150-line toy scripts.
- **NOT flagship-hard** — no research-grade complexity the candidate cannot
  personally explain (e.g. Heston/SABR calibration, CVA/xVA Monte-Carlo,
  cohort SaaS operating models).
- **MEDIUM means:** real/live data (e.g. `yfinance`), a `src/` package with a
  few modules, genuine analytical depth (multiple methods, sensitivity/scenario,
  validation), unit tests, and clean Excel/PDF/chart output — while staying
  **fully explainable line-by-line** by the candidate.
- Every project keeps a `STUDY_GUIDE.md` (30-sec pitch, walkthrough, interview
  Q&A) so it is defensible in an interview.
- Target size: roughly **300–700 lines** across a small module structure.

Rule of thumb: impressive enough that an interviewer takes it seriously, simple
enough that the candidate (MBA Finance, ex-F&O desk, Python/SQL) can defend every
line after reading the study guide.

## Hard Rule #2: Resumes must read as human-written, not AI-generated

All resumes (in `resumes/finance/`, `resumes/business_dev/`,
`resumes/software/`) must follow these rules:

- **Plain, human language.** No AI-tell filler or buzzwords. Ban words/phrases like
  "polyglot", "spearheaded", "leveraged", "seamlessly", "production-grade",
  "results-driven", "passionate", "synergy", "at the heart of", "directly applicable
  to", "mirroring the ... discipline of", "sharpening ... skills central to".
- **No em-dashes (—) or en-dashes (–) anywhere.** Use commas, periods, "to" for date
  ranges (e.g. "May 2022 to Jan 2024"), or "|" as a separator. Keep hyphens only in
  proper names/IDs (e.g. NISM Series-XV, Reg. No.). Avoid hyphenated buzzword
  compounds where a plain phrase works.
- **Short, concrete bullets** that start with plain verbs (Built, Wrote, Managed,
  Improved, Set up). No flowery connective clauses.
- **Fill a full single A4 page** (no half-empty page) but **never spill to a second
  page**. Fill with real content (skills, coursework, project detail), not fluff.
- **Truthful only.** No invented employers, titles, dates, or metrics. NISM Series
  X-A is shown as "pursuing".
- **No "Additional Information" section** (languages / location / availability). Use
  that space for a stronger **Projects** section instead: every project gets 2-3
  concrete, specific bullets.
- Sources are HTML in each track's `source/` folder; render to PDF with headless
  Chrome. `resumes/software/source/Software_Engineer_SDE.html` is the reference
  for the approved plain style.
