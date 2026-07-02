# Deepening Pass — Autonomous (2× depth on every concept chapter)

**Goal:** expand every concept chapter to ~2× depth (more worked examples, edge cases, exam variations, deeper reasoning, extra diagrams) — no padding, keep existing correct content + structure + diagrams. Then rebuild each subject's single `*_FULL.pdf`.

**Marker:** a deepened chapter's first line is `<!-- v2-deep -->`. Un-deepened chapters lack it.

**Loop each wake:**
1. Find the next up-to-6 concept chapters (exclude `00_` cheat-sheets) WITHOUT the marker, in subject order Accounting → Law → Cost → Audit → FM-SM → Taxation:
   `grep -L "v2-deep" <subject>/md/*.md | grep -v "/00_"`
2. Launch the deepen workflow (scriptPath reuse) with args `{dir, files:[...]}`.
3. When a subject's chapters are all deepened, rebuild that subject's `*_FULL.pdf` with `build_subject_pdf.py`.
4. ScheduleWakeup ~1800s. If agents fail with session limit, reschedule ~3600s and wait.
5. When ALL 119 chapters carry the marker, rebuild all 6 PDFs and report done.

**Totals:** Accounting 40 · Law 14 · Cost 15 · Audit 12 · FM-SM 15 · Taxation 23 = **119 chapters (~20 batches of 6).**

Progress: ✅ **Accounting done (40/40, PDF rebuilt 23MB)** · 🟡 Law in progress · ⬜ Cost, Audit, FM-SM, Taxation. (40/119 chapters deep.)
