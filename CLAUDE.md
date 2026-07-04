# Project Rules (CA prep workspace)

## Rule 1 — ONE PDF per subject (absolute)
There must be **exactly one consolidated PDF per subject** — the six `*_FULL.pdf` files in `CA/concept-notes/`:
- `Advanced-Accounting_FULL.pdf`
- `Corporate-and-Other-Laws_FULL.pdf`
- `Cost-and-Management-Accounting_FULL.pdf`
- `Auditing-and-Ethics_FULL.pdf`
- `Financial-Management-and-Strategic-Management_FULL.pdf`
- `Taxation-Income-Tax-and-GST_FULL.pdf`

**Whatever new material is generated** (notes, Q&A, MCQs, mocks, model answers, exam strategy, weightage maps, revision plans, cheat-sheets, flashcards, planning docs, anything) — **fold it INTO that subject's single PDF.** 

- **NEVER create a separate, standalone, or extra PDF** (no 7th PDF, no per-chapter PDFs, no per-topic PDFs).
- Global/cross-subject content (study method, spaced-revision, 30-day plan) is prepended into **every** subject PDF, not made into its own file.
- After generating anything, rebuild the affected subject PDF(s) with `scratchpad build_subject_pdf.py` and confirm the count under `CA/concept-notes/*.pdf` is still exactly **6**.

Editable Markdown sources (`md/`, `qa/`, `exam/`, `flashcards/`, and the `_*.md` planning files) may exist as many files — the **one-PDF-per-subject rule applies to PDFs only.**
