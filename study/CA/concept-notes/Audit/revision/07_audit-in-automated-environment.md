# Chapter 07 — Audit in an Automated Environment (Revision)

## Snapshot
Books now live inside computer systems (ERP/SAP/Oracle/Tally/banking core). The trust gap is unchanged, but the risk relocates into three reservoirs — **logic, access, data**. Errors become **systematic** (same wrong rule on every transaction, one-directional, doesn't self-cancel like random manual error), leave **no visible paper trail**, and multiply at **huge volume/speed** — so IT risk is **pervasive** (a general-control weakness hits many assertions at once). Response: move the audit into the computer — understand IT (SA 315), test the foundation (ITGCs) before the transaction guards (application controls), audit **through** not **around**, and use **CAATs/data analytics** on the full population.

## Core concepts

**Three verbs kept distinct (SA 315/330):**
- **Understand** (SA 315) — mandatory on *every* audit, even with no planned reliance. Can't assess risk in a system you don't understand.
- **Evaluate design + determine implementation** (SA 315) — is the control *capable* and does it *exist/is in use*? A walkthrough answers this.
- **Test operating effectiveness** (SA 330) — does it work *throughout the period*? Only if you intend to **rely**.
- Trap: "I did a walkthrough" (design + implementation) ≠ "I tested the control" (operating effectiveness).

**Two control layers (fail differently):**
- **IT General Controls (ITGCs)** — environment-wide plumbing; do NOT process transactions; they make application controls *dependable*. **Weak ITGCs ⇒ cannot rely on ANY automated application control.** Domains:
  - **Access security / logical access** — authentication ("are you who you claim?") + authorisation ("what may you do?"). Enforces **segregation of duties** (SoD migrates from bodies to roles; test access-matrix for toxic combinations). Watch **privileged/superuser** access (can commit AND conceal).
  - **Change management** — request→test→approve→migrate; **separation of dev/test/prod**; developers no standing production access; emergency/"firefighter" changes reviewed after the fact.
  - **Program development / SDLC** — new systems correctly built, tested, authorised.
  - **IT operations** — job scheduling, batch, incident/monitoring; jobs complete, on time, not missed/duplicated.
  - **Backup, recovery & business continuity** — protects **existence & completeness** of records (ransomware/disk failure = scope + going-concern issue, not just IT hygiene).
- **Application controls** — transaction-level, within one process. Ensure **completeness, accuracy, validity, authorisation**. Three flavours: **automated / manual / IT-dependent manual**.

**Point of reliance (the strategic choice per class of transactions):** controls-reliance strategy (test once, cover the year — only if ITGCs hold) vs substantive strategy (always available, but in high-volume world executed *with* the computer via CAATs). No ITGC-free island: even substantive work trusts a data extract that depends on ITGCs.

**Benefit of consistency:** an automated control is **deterministic** — one successful test is evidence about every execution in the period, **but only because change-management ITGC guaranteed the code didn't change**. Remove change management and the extrapolation collapses.

**IT-dependent manual control (the trap flavour):** a human acts *on the basis of a system-generated report* (e.g., manager reviews "exceptions over ₹1 lakh"). Only as reliable as the **report's completeness/accuracy** (Information Produced by the Entity — IPE). A diligent human reviewing a silently-incomplete report reviews a lie. Must ALSO test the report/query + ITGCs.

**Around vs through vs with:**
- **Around** = black box; test inputs & outputs only, *assume* processing correct. OK only for simple, low-volume systems with strong visible audit trail. Failure mode: reconciliation only catches errors that BREAK the input-output relation; a wrong-but-uniform rule (e.g., interest at 5.9% vs 6.0%) reconciles perfectly and is still wrong. **Reconciliation tests the arithmetic of the process, not the correctness of the rules.**
- **Through** = open the box, test processing/logic/programmed controls. Needed for complex/high-volume/paper-less/automated systems.
- **With** = using the computer as a tool (CAATs, analytics). Decide **per class of transactions**, not one blanket verdict.

## Key provisions / SAs
- **SA 315** — Identifying and Assessing Risks of Material Misstatement through Understanding the Entity and Its Environment. **Anchor.** Requires understanding the **information system + how the entity uses IT**, and the **controls including ITGCs and application controls**. Introduces **"risks arising from the use of IT"** (unauthorised access, unauthorised changes, reliance on inaccurate systems).
- **SA 330** — The Auditor's Responses to Assessed Risks. If relying on automated controls, must test those controls AND the **ITGCs** supporting their **continued effective operation throughout the period**.
- **SA 240** — Fraud. Automated fraud via access/data manipulation; **journal-entry testing** best done via CAATs on full population.
- **SA 500** — Audit Evidence. Electronic evidence reliability depends on **controls over its preparation/maintenance** (→ ITGCs).
- **SA 402** — Using a Service Organisation. Outsourced IT/cloud ERP/third-party payroll: understand those controls, often via **service auditor's report (SOC 1 / Type 2)**; auditor still owns the opinion.
- **SA 620** — Using the Work of an Auditor's Expert. IT specialist; evaluate competence, objectivity, work.
- **SA 230** — Audit Documentation. CAAT design, data source + integrity checks, parameters, results — all re-performable.
- **SA 265** — Communicating Deficiencies. Significant ITGC/application-control weaknesses reported to those charged with governance.
- **SA 530** — Audit Sampling. 100% testing removes *sampling* risk; sampling stays relevant where full-population testing is impractical.
- **Fact-pattern → SA map:** outsourced processing → **402**; IT specialist → **620**; journal/override testing → **240**; electronic-evidence reliability → **500**; spine is always **315 (understand) + 330 (respond)**.

**Application control types (by stage):**
- **Input** — validation/format/range/**check digit**, mandatory fields, existence check vs master, batch control totals. (Accuracy, Validity)
- **Processing** — run-to-run totals, reasonableness/limit checks, sequence/**completeness (control & hash totals)**, **3-way match PO+GRN+invoice**, correct **configuration** (tax rates, credit limits — wrong config = systematic error). (Completeness, Accuracy, Authorisation)
- **Output** — output-to-input reconciliation, restricted distribution, exception reports reviewed. (Completeness, Confidentiality)
- **Duplicate checks** (same invoice+vendor) prevent double-count.
- **Master-data integrity:** "vendor must exist in master" is worthless if fake vendors can be added — controls over *who changes master data* sit at the app/general boundary and are a frequent weak point.

**CAATs (Computer-Assisted Audit Techniques):**
- **Test data** — *dummy* txns (valid AND invalid) through the *client's* program → tests programmed **controls/logic**. Must not corrupt live data.
- **Integrated Test Facility (ITF)** — dummy entity embedded in the *live* system, txns run alongside real ones then **reversed** → tests under real conditions; highest contamination risk.
- **Parallel simulation** — auditor's *independent* program re-processes *real* client data, compares → tests **processing accuracy**.
- **Embedded audit facility / SCARF** — audit routines baked into live system continuously capture unusual/**transient** transactions to an audit log → continuous auditing ("flight recorder").
- **Generalised Audit Software (GAS)** — IDEA/ACL; sort, filter, total, stratify, sample, recompute, find gaps/duplicates on full population. Workhorse for substantive testing.
- **Utility software / SQL scripts** — ad-hoc extraction.
- **Direction hook:** *Test data = fake data through real program (controls); Parallel simulation = real data through auditor's program (accuracy).*
- **Use-considerations:** IT skill/expertise (may need SA 620 expert) · availability & compatibility of tools · impracticability of manual tests · effectiveness & efficiency · timing (transient data) · data integrity / don't corrupt live systems · cost-benefit & client cooperation · **prove extract completeness first**.

**Data analytics (ADA):** discover patterns/deviations/anomalies over the **whole population**. Uses: 100% testing · **journal-entry testing (SA 240)** — weekend/holiday/after-hours postings, unusual users, round sums, just-below approval limits, unusual accounts/narrations · 3-way match · duplicate & gap detection · revenue cut-off · ageing/recomputation · **Benford's Law** (leading digit 1 ≈ 30%, falls to ~4.6% for 9; flags — does NOT prove — fraud; does NOT apply to constrained data: capped, sequential, assigned-ID, floor/ceiling fields).

## Exam traps & must-remember
- "Automated control worked in walkthrough, so rely on it" — **WRONG without ITGCs** (esp. change management). Reliance is conditional.
- Confusing layers: "passwords restrict payroll module access" = **ITGC (access security)**; "payroll rejects negative hours" = **application (input) control**.
- "Auditing around always/never acceptable" — neither; only OK for simple systems with strong visible trail.
- Test data on a live system can **corrupt real records** — mention safeguard (copy, or reverse via ITF); feed **both valid AND invalid** cases (the control's job is to reject).
- CAAT/analytics exceptions are **leads to investigate, not conclusions**. Garbage in, garbage out.
- Swapping test data ↔ parallel simulation = instant mark loss.
- "100% testing eliminates audit risk" — no, only **sampling risk for that test**; **data-completeness risk** (the extract may be incomplete — reconcile counts/control totals to source/TB first) and **non-sampling/judgement risk** remain.
- IT-dependent manual control: never conclude on the human step alone — test the report's completeness/accuracy (IPE).
- Benford's on constrained/capped/sequential data = meaningless.
- Master-data integrity often the real weak point.
- Outsourcing (cloud/SaaS) does NOT remove auditor responsibility — SA 402, SOC/Type 2.
- Name the right SA: anchor is **SA 315 + SA 330**; there is no fictional "SA on IT."
- Answer computer effects as **audit impacts tied to a risk** (loss of trail, systematic error, automated controls, pervasive IT, volume), not as computer features.
- Pervasiveness: a general-control weakness undermines reliance on *every* automated control — reassess the whole plan, not one line.
- **Systematic-error multiplier:** 50,00,000 accounts, ₹40,000 avg balance, rate 6.00% vs mis-configured 5.95% = ₹20 error/account (immaterial, invisible to sample) × 50,00,000 = **₹10 crore** aggregate. One-directional systematic error doesn't wash out → must recompute the whole population (parallel simulation/GAS), not sample 25.

## One-line recall
- Trust gap unchanged; risk relocates into **logic · access · data** — errors go systematic, paperless, vast, pervasive.
- **SA 315 understand → SA 330 respond**; test **ITGCs first → then application controls → reduce substantive**.
- **Weak ITGCs ⇒ no reliance on any automated control ⇒ substantive (CAATs).**
- "Benefit of consistency": test once = cover the year, **only because change-management ITGC held**.
- **Test data = fake/real program (controls); Parallel simulation = real/auditor's program (accuracy);** ITF = dummy entity live+reversed; SCARF = continuous; GAS = full-population workhorse.
- 100% testing kills **sampling** risk only — prove the **extract is complete/reliable** first; analytics gives leads, not conclusions.
