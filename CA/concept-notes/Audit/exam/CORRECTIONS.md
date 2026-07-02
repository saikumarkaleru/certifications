# Auditing & Ethics — Accuracy Review: Corrections & Caveats

**Scope of this review.** This is a **spot-review, not an exhaustive audit.** I read six of the thirteen chapter files in full, deliberately choosing the most error-prone (those dense with SA numbers, Companies Act section numbers, statutory thresholds, and worked computations):

- `02_audit-strategy-planning-materiality.md`
- `03_risk-assessment-internal-control.md`
- `05_audit-sampling-analytical-procedures.md`
- `08_company-audit.md`
- `09_audit-report.md`
- `11_professional-ethics-and-independence.md`

Chapters 00, 01, 04, 06, 07, 10 and 12 were **not** reviewed and are not vouched for here.

**Headline finding.** Across the six chapters I found **zero hard technical errors** — no wrong SA numbers, no wrong section numbers, no wrong formulas, no miscomputations, no conceptually inverted statements. Every SA reference (200, 210, 220, 230, 240, 265, 315, 320, 330, 402, 450, 500, 510, 520, 530, 570, 580, 600, 700, 701, 705, 706, 710, 720; SQC 1) and every Companies Act section (132, 134(5)(e), 138, 139–148, 164(2), 177, 185, 186, 188, 192, 197, 447; CARO 2020) is used correctly. All the worked numbers check out (verified below). The notes also **responsibly self-flag** most figures that periodically change with "confirm in current ICAI material."

The items below are therefore **caveats / verify-before-exam points**, not corrections of errors. I list them so you know exactly which figures are load-bearing and what the currently-correct values are. Confidence ratings tell you how sure I am.

---

## Verified computations (all correct)

Recording these so you can trust the worked examples:

- **Ch 05, Scenario A** — projection `(₹1,600 / ₹2,00,000) × ₹1,00,00,000 = ₹80,000`. **Correct.**
- **Ch 02, Scenario 1** — `0.75% × ₹520 cr = ₹3.9 cr`. **Correct.**
- **Ch 02, Scenario 3** — `5% × ₹9 cr = ₹45 lakh`; performance materiality `75% × ₹1.5 cr = ₹1.125 cr`. **Correct.**
- **Ch 08, Scenario A** — firm 2 terms × 5 yrs = 10-yr cap; 11 yrs breaches it. **Correct.**

---

## Caveats & verify-points (no confirmed errors — these are watch-items)

### 1. Chapter 03 (Risk & Internal Control) → "AR = IR × CR × DR" presented as a literal multiplicative formula
- **As written:** "audit risk is broken into components that behave like a multiplication chain … AR = IR × CR × DR", with "DR = AR ÷ RMM."
- **Correct position:** This is the standard **ICAI teaching model** and is accepted in exam answers — so keep using it. Caveat: the **revised SA 315 (2021)**, effective in India for periods beginning on/after 1 April 2023, assesses **inherent risk and control risk separately at the assertion level** and de-emphasises a single combined RMM / literal arithmetic. Treat the multiplication as a *conceptual* relationship, not a formula SA 200 mandates. The chapter *does* note the SA 315 revision elsewhere, so this is minor.
- **Confidence:** High (that it's a conceptual model, not literal); the note is not wrong for exam purposes.

### 2. Chapter 08 (Company Audit) → Section 141(3)(d) monetary thresholds
- **As written:** relative may hold securities up to **face value ₹1,00,000**; indebtedness limit **₹5,00,000**; guarantee limit **₹1,00,000**.
- **Correct position:** **These match the current Companies (Audit and Auditors) Rules, 2014.** Confirmed correct as at review date. Just be aware these live in the *Rules*, not the bare Act, so they can be amended — verify closer to exam.
- **Confidence:** High (currently correct).

### 3. Chapter 08 (Company Audit) → Rotation-class thresholds left blank
- **As written:** rotation applies to "listed companies and certain large public/private companies (thresholds by paid-up capital / borrowings — confirm current limits)."
- **Correct position (for your notes):** Rule 5 currently sets rotation for: all **listed** companies; **unlisted public** companies with paid-up capital ≥ **₹10 crore**; **private** companies with paid-up capital ≥ **₹50 crore**; and **any** company (other than OPC/small) with **public borrowings from banks/FIs/public deposits ≥ ₹50 crore**. The note correctly leaves the number out and flags it; supplied here for completeness.
- **Confidence:** High (values current); note itself is not wrong.

### 4. Chapter 08 (Company Audit) → Audit ceiling of "more than 20 companies"
- **As written:** disqualified if holding audits of "more than 20 companies (the ceiling — with specified exclusions)."
- **Correct position:** Correct (s.141(3)(g)). The "specified exclusions" from the count are **OPC, small companies, dormant companies, and private companies with paid-up capital < ₹100 crore**. Correctly stated in principle; exclusions supplied here for exam recall.
- **Confidence:** High (correct).

### 5. Chapter 09 (Audit Report) → IFC operating-effectiveness private-company exemption
- **As written:** "certain private companies are exempted (notably … small/one-person and specified private companies meeting turnover/borrowing conditions) — confirm the current exemption thresholds."
- **Correct position (for your notes):** Per MCA notification dated 13 June 2017, reporting on IFC **operating effectiveness** under s.143(3)(i) does not apply to a private company that is a **OPC or small company**, OR has **turnover < ₹50 crore** (latest audited FS) **and** aggregate **borrowings < ₹25 crore** from banks/FIs/any body corporate at any point in the FY. Note is correct to flag; values supplied.
- **Confidence:** High (values current); note not wrong.

### 6. Chapter 09 (Audit Report) → KAM "mandatory for listed entities"
- **As written:** "KAM is mandatory for audits of listed entities … (Under the Companies Act framework, also confirm applicability thresholds in current ICAI material)."
- **Correct position:** Correct. SA 701 applicability is triggered for **listed entities** (and where law/regulation requires, or the auditor elects). There is **no separate Companies-Act turnover/size threshold** that expands mandatory KAM beyond listed entities — so the "confirm applicability thresholds" hedge, while harmless, could mislead a student into hunting for a numeric threshold that doesn't exist. Answer for the exam: **listed entities.**
- **Confidence:** Medium-High.

---

## Overall reliability — per reviewed chapter

- **Chapter 02 — Audit Strategy, Planning & Materiality:** **Very reliable.** SA 300/320/450/315/330 correctly deployed; benchmark ranges (PBT ~5%, revenue ~0.5–1%, assets ~1–2%, net assets ~1–5%) are the standard indicative ranges and are correctly flagged as judgement-based (SA 320 fixes no numbers). Performance-materiality 50–75% and the risk↔materiality inverse relationship are stated correctly. All arithmetic correct. **Use with confidence.**

- **Chapter 03 — Risk Assessment & Internal Control:** **Very reliable.** Audit-risk model, five COSO components, inherent limitations, ToC vs substantive logic, "substantive for every material item," significant-risk rules (current-year testing; tests of details required), and the "test at least once every third year" reliance rule are all correct. Only caveat: treat AR = IR × CR × DR as conceptual, not literal (item 1). **Use with confidence.**

- **Chapter 05 — Audit Sampling & Analytical Procedures:** **Very reliable — the strongest chapter.** SA 500/530/520 definitions, sampling-risk directions (over-reliance / incorrect acceptance = effectiveness), sample-size drivers (incl. the "population size is negligible for large populations" point), anomaly rule, projection logic, the "mandatory at risk assessment + overall review, optional as substantive" point, directional testing, and the four SA 520.5 gates are all correct. Worked projection verified. **No caveats.**

- **Chapter 08 — Company Audit:** **Very reliable.** All timelines correct (first auditor: Board 30 days / members 90 days at EGM; Govt C&AG 60 days; casual vacancy 30 days, resignation → members within 3 months; removal = special resolution + Central Government + ADT-2 within 30 days + special resolution within 60 days of approval). Forms ADT-1/2/3/4, fraud threshold ₹1 crore, cost-auditor separation, branch-audit logic all correct. Thresholds correctly self-flagged (items 2–4). **Use with confidence.**

- **Chapter 09 — Audit Report & Opinions:** **Very reliable.** SA 700 element order (Opinion-first, 2018 redesign), the SA 705 2×2 matrix (adverse ← disagreement only; disclaimer ← inability only; qualified for either when not pervasive), SA 706 EOM/OM distinction, SA 701 KAM funnel and exclusions (no KAM on a disclaimer), CARO 2020 = 21 clauses with correct clause content, s.143 statutory matters, and IFC reporting are all correct. Minor caveats at items 5–6. **Use with confidence.**

- **Chapter 11 — Professional Ethics & Independence:** **Very reliable.** Five fundamental principles correct; independence correctly treated as a *separate* requirement (not a sixth principle); five threats with correct mechanisms; safeguards framework; confidentiality's "disclose *and* use" plus exceptions; contingent-fee prohibition for assurance; s.141/144/139(2) as the legal backstop — all correct. Cross-refs to Ch 08 thresholds consistent. **Use with confidence.**

---

## Bottom line

For the six chapters reviewed, this material is **technically sound and exam-safe.** I found **no wrong section/SA numbers, no wrong formulas, no wrong thresholds, and no computation slips.** The only action items are the **six verify-caveats above**, most of which the notes already flag themselves — and for those I've supplied the currently-correct figures so you don't have to hunt for them. Because thresholds in the *Rules* (s.141 limits, rotation classes, IFC exemption) do get amended, do a final cross-check against the latest ICAI study material and Companies (Audit and Auditors) Rules before the exam.

*Reminder: chapters 00, 01, 04, 06, 07, 10, 12 were outside this spot-review and should be checked separately.*
