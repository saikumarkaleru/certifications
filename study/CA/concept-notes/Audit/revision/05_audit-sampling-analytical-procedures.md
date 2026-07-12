# Audit Sampling & Analytical Procedures

## Snapshot

Two trust gaps the auditor cannot brute-force. (1) Volume gap — cannot examine 100% of large populations, yet the opinion must cover the whole: answered by **audit sampling (SA 530)** — test a representative subset and project. (2) Plausibility gap — item-by-item testing is myopic and misses misstatements visible only in relationships between numbers: answered by **analytical procedures (SA 520)** — build an independent expectation and chase unexpected differences. Sampling drills down; analytics steps back. Neither gives certainty: testing a subset leaves **sampling risk**; even 100% testing leaves **non-sampling risk**. Hence audit gives **reasonable, not absolute, assurance**. Both techniques share one move: the auditor manufactures an independent yardstick (projected error / expected value) and refuses to accept the client's number passively.

## Core concepts

- **Homogeneity precondition:** sampling assumes the subset resembles the whole. Where a population mixes wildly different values (20 corporate accounts of Rs 5 cr + 40,000 retail of Rs 200), fix by **stratification** — carve into homogeneous sub-groups and sample each. Mixed values in a question = stratification answer.
- **Analytics engine:** plausible relationships among financial and non-financial data persist unless something changed. Deviation from a well-built expectation = genuine business change (corroborate) OR misstatement in disguise. Power lies in **precision of the expectation** and **independence of the data** — non-financial data (kWh, headcount, tonnes, floor area) is gold because it sits OUTSIDE the manipulable ledger.
- **Incentive-compatibility lens:** every SA 530/520 requirement defeats a specific temptation (auditor's to do less, or management's to mislead). Naming the temptation scores higher than restating the rule.

## Key provisions / SAs

### SA 500 — Audit Evidence (parent that legitimises sampling)
Evidence must be **sufficient (quantity)** and **appropriate (quality = relevant + reliable)** — interdependent, NOT additive; more evidence cannot rescue poor-quality evidence.

Three ways to select items:
| Method | Note |
|---|---|
| **Selecting all items (100%)** | Small populations of large-value items, or cheap electronic re-performance (CAATs). Eliminates sampling risk. |
| **Selecting specific items** | Judgemental: high-value, all over threshold, unusual items. **Targeted testing, NOT sampling** — non-selected items had no chance → **cannot be projected**. |
| **Audit sampling** | <100%, all units have a chance of selection → conclude on entire population. |

**Reliability hierarchy:** external > internal; under effective control > not; obtained directly by auditor > indirect; documentary > oral; original > photocopy.

### SA 530 — Audit Sampling
Key definitions:
| Term | Meaning |
|---|---|
| Audit sampling | Procedures on <100% such that all units have a chance of selection; conclude on entire population |
| Population | Entire set concluded about; must be **complete and appropriate** |
| Sampling unit | Individual items (invoice, balance, rupee) |
| Sampling risk | Risk sample conclusion differs from whole-population conclusion; unavoidable; shrinks with sample size |
| Non-sampling risk | Wrong conclusion for reasons unrelated to size (unsuitable procedure, missed error); NOT fixed by size — fixed by planning/supervision/training |
| Tolerable misstatement | Amount set so actual misstatement does not exceed it; the benchmark; **<= performance materiality** |
| Tolerable rate of deviation | Benchmark for tests of controls |
| Anomaly | Misstatement demonstrably NOT representative; rare; must be proven |
| Statistical sampling | Random selection **AND** probability theory to measure risk |
| Non-statistical | Lacks either feature; risk judged not computed — **same rigour required** |

**Materiality chain:** overall materiality >= performance materiality >= tolerable misstatement. Setting tolerable near overall materiality destroys the cushion (design error).

**Sampling risk — two faces (pair by consequence):**
- False-comfort risks say "fine" when it isn't → endanger the **opinion (effectiveness)**: **over-reliance** (controls) and **incorrect acceptance** (details). These are the dangerous ones.
- False-alarm risks say "problem" when there isn't → only waste **effort (efficiency)**: **under-reliance** and **incorrect rejection**.
- Confidence level + sampling risk = 100%; raising confidence raises sample size.

**What drives sample size (learn direction):**
- Controls — sample size UP with: intended reliance, expected deviation rate, desired confidence. DOWN with: tolerable rate of deviation. Population size: negligible (large populations).
- Details — sample size UP with: RMM, desired assurance, expected misstatement. DOWN with: tolerable misstatement, other substantive procedures for same assertion, stratification. Population size: negligible.
- **Asymmetry trap:** higher **tolerable** → smaller sample (more slack); higher **expected** → larger sample (less buffer). Opposite directions. If expected >= tolerable, sampling is pointless — test in full / seek correction.

**Selection methods:**
| Method | Note |
|---|---|
| Random | Every item equal chance; pure statistical |
| Systematic | Interval = population / sample; random start, every nth. **Danger:** periodic pattern coinciding with interval → biased |
| Monetary Unit Sampling (MUS)/value-weighted | Sampling unit = the rupee; big items far likelier. Auto-stratifies by value; catches **overstatement**; **blind to understatement / zero/negative balances** — poor for completeness |
| Haphazard | No conscious bias but not structured random; **non-statistical only** |
| Block | Contiguous block (all of March). Generally inappropriate — correlated items carry little independent info; cannot project |

**Untestable items (critical distinction):**
- Document lost / procedure can't be applied → test a **replacement item** (never just skip — a missing document may itself be the misstatement).
- Item cannot be tested AND no alternative → treat as **deviation (controls) / misstatement (details)**. Do NOT replace it — burying an untestable item understates the error rate. Rule: replace an item you *chose not to test*; never bury one you *could not test*.

**Evaluating results (heart of SA 530):**
1. Investigate **nature and cause** of every error — look for patterns (one clerk, year-end) signalling systematic failure/fraud.
2. **Anomaly** only if provably non-representative with high certainty (e.g., fixed one-day glitch), incl. examining more items to confirm. Assume representative unless proven otherwise.
3. **Project** misstatement to population (details). Anomaly added at actual, NEVER projected. For **controls, the sample deviation rate IS the projected rate** (no separate projection).
4. **Compare** projected (+ anomalous) vs tolerable. Comfortably below with buffer → acceptable. Close/exceeds → extend sample, alternative procedures, ask management to investigate/correct, re-evaluate.

**Projection methods:**
- **Ratio (value-weighted):** (misstatement / value of sample) x total population value. Use when error rate roughly constant across values.
- **Difference (per-item):** (misstatement / no. of sample items) x no. of population items. Use when error is a constant amount per item.
- Same found error projects to very different figures → choice of basis is a documented judgement.
- **Buffer judgement:** "projected < tolerable" is NOT automatic pass; a thin buffer (Rs 19L vs Rs 20L) means true figure could breach — extend.

### SA 520 — Analytical Procedures
**Definition:** evaluations of financial information through analysis of plausible relationships among financial AND non-financial data, including investigation of fluctuations inconsistent with other info or differing from expected values by a significant amount.

**Three points in the audit:**
| Stage | Mandatory? |
|---|---|
| Risk assessment (planning, SA 315) | **Yes — required** |
| Substantive procedure (SA 520.5) | **Optional** (auditor's choice) |
| Overall review near end (SA 520.6) | **Yes — required** |

Precision bar: broad/directional at risk assessment; **precise enough to substitute for detailed testing** when substantive.

**Substantive analytics — four conditions (SA 520.5):**
1. **Suitability** for the assertion (good for predictable relationships — interest, payroll; poor for volatile/discretionary/unrelated items — litigation provisions).
2. **Reliability of data** — source, comparability, nature, controls. Deadly trap: expectation built from the same weak system as the audited figure proves nothing → prefer independent/non-financial data.
3. **Precise expectation** — precise enough to catch a material misstatement. Vague ("about the same") detects nothing.
4. **Acceptable difference** set **in advance** — stops rationalising whatever turns up.

**Precision levers:** (a) **disaggregation** (monthly/product/location — strongest, offsetting errors cancel in annual totals); (b) stable relationship; (c) reliable independent data; (d) predictive/reasonableness model over trend.

**Toolkit by strength (least to most precise):** trend analysis < ratio analysis < budget comparison < reasonableness/predictive test. Predictive test from independent non-financial data at disaggregated level = gold standard. Caution: a figure landing exactly on budget is a red flag (management steering actuals), not comfort.

**Investigating results (SA 520.7):** when significant deviation — (1) inquire of management, (2) **corroborate** with other evidence, (3) further procedures if not corroborated/inadequate. Management's explanation is a **hypothesis, not evidence**. A fluent explanation is not a corroborated one. Default posture toward an unexplained significant fluctuation is suspicion (possible fraud, link SA 240).

### Assertions & directional testing (SA 315)
| Assertion | Better tested by |
|---|---|
| Occurrence/Existence | Sampling → vouching (record → document); MUS for overstatement |
| Completeness | Analytics + tracing (document → record); sampling for understatement |
| Accuracy/Valuation | Recomputation + reasonableness tests |
| Cut-off | Targeted selection around year-end |
| Rights & Obligations | Tests of details (title deeds, confirmations) |

**The one-sentence rule:** *you can only catch what is in the population you sample.* Sample the ledger → find overstatement/existence/occurrence. Sample the real world (dispatch records, supplier statements, GRNs, post-year-end payments) and trace IN → find understatement/completeness. Assets/income overstate → vouch ledger outward; liabilities/expenses understate → trace source documents inward. Vouching recorded purchases can NEVER detect unrecorded purchases.

## Exam traps & must-remember

- **Non-statistical is NOT casual** — SA 530 applies fully; only difference is risk measured vs judged. Representativeness + projection mandatory in both.
- **Random selection alone is not statistical** — needs random selection AND probability theory.
- **Failure to project** — the number in the sample is never the number in the population.
- **Confusing projection methods** — ratio scales by value, difference by item count; document the basis.
- **Over-using "anomaly"** — rare, requires proof of non-representativeness + testing more items. It's the escape hatch the Standard bolts shut.
- **Replacement vs deviation** — replace an item you chose not to test; treat an untestable item (no alternative) as a deviation.
- **Population size drives sample size** — FALSE for large populations; assurance from sample size not the ratio (soup-tasting).
- **Tolerable vs expected** move sample size in OPPOSITE directions.
- **Tolerable set too high** — must be <= performance materiality.
- **Sampling vs non-sampling risk** — only sampling risk shrinks with size.
- **MUS catches overstatement, not understatement** — zero/understated item has no rupees, escapes.
- **Analytics mandatory at risk assessment + overall review, optional as substantive** — frequently reversed.
- **Accepting uncorroborated explanations** — SA 520.7 requires corroboration; exact-on-budget is a flag not comfort.
- **Block/haphazard** — block inappropriate (correlated); haphazard non-statistical only.
- **Specific-item selection is NOT sampling** — cannot project; small-value tail (where structured fraud hides just under the threshold) left unexamined.
- **Documentation (SA 230):** an experienced auditor with no prior connection must be able to re-perform the judgement — capture reasoning, not just numbers. Projected misstatements feed SA 450 uncorrected-misstatement schedule.

## One-line recall

- Sampling (SA 530) closes the volume gap; analytics (SA 520) close the plausibility gap; both give reasonable not absolute assurance.
- Every unit must have a chance of selection — that is what licenses projection.
- Anomaly = a proof, not a label; assume errors are representative and project them.
- Tolerable shrinks the sample; expected grows it; population size barely matters for large populations.
- Analytics mandatory at risk assessment + final review, optional as substantive; a vague expectation can never be violated.
- You cannot sample the ledger to find what was left out of the ledger — match technique to the direction of the lie.
- Management's explanation is a hypothesis, not evidence — corroborate it.
