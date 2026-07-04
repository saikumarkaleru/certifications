# Practice-Build Queue (Mocks 2–4 + Problem Drills)

Fold everything into the 6 subject PDFs (Rule 1 — no new PDFs).

## Track A — Mock Tests 2–4 (per subject → exam/MOCK_TEST_2..4.md)
- ✅ DONE — all 18 mocks written, folded into the 6 PDFs (count verified = 6).

## Track B — Chapter-wise Problem Drills (per subject → exam/PROBLEM_DRILLS.md, merged from parts)
- ✅ DONE — 45 graded problems per subject (270 total), folded into the 6 PDFs.

# ✅✅ BOTH TRACKS DONE. 6 PDFs, one per subject (Rule 1). Each has Mocks 1-4 + 45 problem drills.

**Builder:** `scratchpad/build_subject_pdf.py` exam list now includes PROBLEM_DRILLS + MOCK_TEST_2/3/4. Rebuild each subject PDF after its files land; confirm PDF count stays 6.
On session-limit failure: re-check disk (files may have been written before the failed return), reschedule ~3600s, resume only what's missing.
