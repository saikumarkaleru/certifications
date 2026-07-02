# Autonomous Build Queue (state file — I read this to know what to build next)

**Mission:** Build concept-first + full-answer Q&A notes for all 6 CA Inter subjects, with Mermaid diagrams where they aid understanding. One consolidated `*_FULL.pdf` per subject, refreshed after each batch.

**Process each wake:** (1) if a batch just completed, mark it ✅ and rebuild that subject's FULL pdf; (2) launch the next ⬜ batch as a parallel workflow (6 chapters, concept→Q&A pipeline, agentType general-purpose, writing md/ and qa/); (3) ScheduleWakeup fallback ~1800s; (4) on final batch, build all FULL pdfs and report.

**Builder scripts (scratchpad):** `build_subject_pdf.py <subjectDir> <name> <outPdf> [prefixes]` (mermaid-enabled). Mermaid vendored at scratchpad/assets/mermaid.min.js.

**STYLE (reused every batch):** 10-part concept skeleton (Problem → Core Idea → Why → Full Technical Content [RMPD] → ≥3 worked examples → Presentation/Disclosure → Connections → Traps → Recap → Quick-Revision). Complete+Conceptual: all exam tech content, always with the "why". ICAI (AS / Act sections / IT & GST law), Rupees. No invented provisions; flag uncertain thresholds. Numerical examples must fully reconcile. **VISUALS: 2-5 valid Mermaid diagrams per chapter** (flowchart TD/LR decision trees & processes, timeline, graph), simple quoted labels, italic caption each. Q&A: every question followed by full model answer; Sections A concept / B computational (reconciling) / C past-paper style / D MCQ+reasoning.

---

## ACCOUNTING (dir: Accounting) — name "Advanced Accounting"
- ✅ B1: AS3, AS4, AS5, AS7, AS9, AS11
- ✅ B2: AS12, AS13, AS16, AS19, AS20, AS22
- ✅ B3: AS14, AS17, AS18, AS26, AS28, AS29 (with diagrams)
- ✅ B4: AS24, AS25, AS27, Company FS (Sch III), Pref Redemption, Buyback (with diagrams)
- ✅ B5: Bonus, Rights, ESOP, Underwriting, Debenture Redemption, Investment Accounts (with diagrams)
- ✅ B6: Amalgamation, Internal Reconstruction, Branch, Departmental, Consolidation, LLP (with diagrams)
**✅✅ ADVANCED ACCOUNTING COMPLETE — 40 chapters, FULL pdf built.**
*(Note: hand-written ch 01-04 + B1/B2 have no diagrams; optional later enrichment pass.)*

## LAW (dir: Law) — name "Corporate & Other Laws"
- ✅ B1: Preliminary, Incorporation, Prospectus, Share Capital, Deposits, Charges (qa/02 backfilled)
- ✅ B2: Mgmt & Administration, Dividend, Accounts, Audit & Auditors, LLP Act, General Clauses Act (with diagrams)
- ✅ B3: Interpretation of Statutes; FEMA 1999 (with diagrams)
**✅✅ CORPORATE & OTHER LAWS COMPLETE — 14 chapters, FULL pdf built.**

## COST (dir: Cost) — name "Cost & Management Accounting"
- ✅ B1: Intro, Material, Labour, Overheads, ABC, Cost Sheet (with diagrams)
- ✅ B2: Cost Systems + Reconciliation, Unit/Batch, Job/Contract, Process, Joint/By-product, Service (with diagrams)
- ✅ B3: Standard Costing, Marginal Costing, Budgets (with diagrams)
**✅✅ COST & MANAGEMENT ACCOUNTING COMPLETE — 15 chapters, FULL pdf built.**

## AUDIT (dir: Audit) — name "Auditing & Ethics"
- ✅ B1: Nature, Planning & Materiality, Risk/Internal Control, Evidence, Sampling & Analytical, Audit of FS Items (with diagrams)
- ✅ B2: Automated Env, Company Audit, Audit Report, Documentation & Quality, Ethics, Different Entities (with diagrams)
**✅✅ AUDITING & ETHICS COMPLETE — 12 chapters, FULL pdf built.**

## FM-SM (dir: FM-SM) — name "Financial Management & Strategic Management"
- ✅ B1: FM Scope, Financing & Markets, Ratio Analysis, Cost of Capital, Leverage, Capital Budgeting (with diagrams)
- ✅ B2: Risk in Cap Budgeting, Dividend, Working Capital, SM Intro, SM External, SM Internal (with diagrams)
- ✅ B3: SM Strategic Choices, Implementation & Evaluation, Functional/Digital (qa/13 backfilled)
**✅✅ FM & SM COMPLETE — 15 chapters, FULL pdf built.**

## TAXATION (dir: Taxation) — name "Taxation (Income Tax & GST)"
- ✅ B1: Basic Concepts, Residential Status, Salaries, House Property, PGBP, Capital Gains (with diagrams)
- ✅ B2: Other Sources, Clubbing/Set-off, Deductions VI-A, Advance Tax/TDS/TCS, Returns, Computation of TI (with diagrams)
- ✅ B3: GST Concept, Supply, Charge/RCM, Exemptions, Time of Supply, Value of Supply (with diagrams)
- ✅ B4: GST ITC, Registration, Tax Invoice/Notes, Payment, Returns (with diagrams)
**✅✅ TAXATION COMPLETE — 23 chapters, FULL pdf built.**
*(Income Tax: study the AY applicable to the exam; flag amendment-sensitivity. GST: ITC as the anti-cascade engine.)*

# 🎉 ALL 6 SUBJECTS COMPLETE — 119 chapters, ~3,000 Q&A. Build finished.

---
**✅ BUILD COMPLETE — all 6 subjects done. 0 batches remaining.** (119 chapters, ~3,000 Q&A, 6 consolidated PDFs.)
