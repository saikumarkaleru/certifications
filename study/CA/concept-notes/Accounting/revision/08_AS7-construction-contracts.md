# Chapter 08 — AS 7: Construction Contracts

## Snapshot
- Governs the **contractor's** accounting for contracts that straddle **more than one accounting period** (bridge, dam, ship, building, pipeline, refinery), plus services directly related to construction and demolition/restoration.
- Core: recognise revenue, cost and profit **as you build** (Percentage-of-Completion Method, POCM) — matching activity to reporting periods. Completed-contract method is **NOT permitted**.
- Applies to an asset built **to a customer's specification** under a specifically negotiated contract.

## Core concepts
- **Two pricing types:** Fixed price (cost-overrun risk on contractor) and Cost plus (reimbursed cost + margin/fee; risk on customer). Reliability gate differs for each.
- **POCM** = recognise cumulative profit = (stage % × total expected profit), then back out prior years. Rate of earning is smooth; rupees of work per year is uneven.
- **Prudence asymmetry:** profits gradually by stage; a **foreseeable loss is booked in full, immediately**, whatever the stage.
- Estimate revisions = **change in accounting estimate (AS 5) → prospective**, never restate prior years.

## Key provisions / rules

### Accounting unit — combine / segment (decide FIRST)
- **Segment** one contract into each asset when ALL: (i) separate proposals per asset, (ii) each separately negotiated & acceptable/rejectable, (iii) costs & revenues of each identifiable.
- **Combine** several contracts as one when ALL: (i) negotiated as single package, (ii) so interrelated they are one project with an overall margin, (iii) performed concurrently/continuously.
- **Additional asset** = separate contract if EITHER significantly different in design/technology/function OR priced without regard to the original price.
- Why it matters: **loss test (Rule C) is per unit.** Combined → loss on one leg offsets profit on other. Separate → loss provided in full, NO offset.

### Contract revenue (measurement)
= Initial agreed amount **+ variations + claims + incentives** (each only if **probable + reliably measurable**) **− probable penalties/liquidated damages**.
- **Variation:** customer-instructed scope change; include when customer approval probable + measurable (can reduce revenue too).
- **Claim:** reimbursement contractor seeks; include only when negotiations advanced enough that acceptance is probable + measurable.
- **Incentive:** early-completion bonus; include when contract sufficiently advanced that meeting standard is probable + measurable.
- Updated every period (up or down); revisions = AS 5 prospective.

### Contract costs (the cost base)
- **(1) Directly related:** site labour & supervision, materials used, depreciation of plant used on contract, moving plant/materials to & from site, plant hire, design directly related, estimated rectification/warranty, third-party claims. Directly-attributable income (sale of surplus material, plant disposal) **deducted**.
- **(2) Allocable general:** insurance, general design/technical, construction overheads — on **systematic & rational** basis at **normal level of activity**; borrowing costs if AS 16 met.
- **(3) Specifically chargeable to customer** per contract terms.
- **EXCLUDED (period costs):** non-reimbursable general admin, selling costs, unallocated R&D, depreciation of **idle** plant not used on contract.
- **Pre-contract (bid) costs:** capitalise only if separately identifiable + reliably measurable + winning contract probable. Once expensed, **never reinstated** (one-way ratchet).

### Recognition — the three rules
- **Rule A — reliable estimate → full POCM.** Recognise revenue AND cost by stage.
  - *Fixed price gate (ALL):* total revenue measurable; economic benefits probable; cost-to-complete AND stage measurable; contract costs identifiable/measurable.
  - *Cost plus gate (BOTH):* benefits probable; costs identifiable & measurable.
- **Rule B — outcome NOT reliably estimable → zero-profit.** Revenue = **recoverable costs incurred**; costs expensed as incurred → **no profit** (irrecoverable cost → immediate loss). Switch to Rule A **prospectively** when uncertainty clears. If recovery not probable at all (void/litigated/condemned/insolvent) → revenue **nil**, all costs expensed.
- **Rule C — expected loss → book WHOLE loss immediately.** When total cost > total revenue, recognise full loss now, **irrespective of** stage, work commenced, or profit on other contracts. **Overrides A and B** (test C last, but it wins). Foreseeable loss = total estimated cost − total revenue.

### Stage of completion
- **Cost-to-cost:** Stage % = Costs for work performed to date ÷ Total estimated costs.
  - EXCLUDE from costs-to-date: materials **delivered but not yet used**, **advances to subcontractors** for unperformed work. Keep numerator/denominator consistent.
- Also: surveys of work performed; completion of physical proportion (only if units comparable).
- **NEVER** use progress billings or cash received as the stage measure.

### Mechanics each period
- Cumulative revenue = Stage % × Total contract revenue
- Current revenue = Cumulative revenue − revenue booked in prior periods
- Current expense = Stage % × Total cost − prior expense (= actual cost of work done in period)
- Current profit = current revenue − current expense
- Self-check: **cumulative profit must = Stage % × total expected profit** (profit years); **= full expected loss** the instant it turns loss-making.

### Balance sheet (per contract, then aggregate — do NOT net one number)
- **Due FROM customer (asset)** = (Costs + Recognised profit − Recognised loss) − Progress billings, where positive (earned > billed).
- **Due TO customer (liability)** = Progress billings − (Costs + Recognised profit − Recognised loss), where positive (billed > earned).

## Journal entries
```
Contract WIP A/c            Dr   To Bank / Payables        (costs incurred)
Contractee/Customer A/c     Dr   To Contract Revenue (P&L) (revenue by stage)
Contract Revenue A/c        Dr   To Contract Costs / To Contract P&L (match, book profit)
Expected Loss A/c           Dr   To Provision for Foreseeable Loss (full expected loss, Rule C)
```

## Worked mini-example (Rule C — the loss override)
Fixed price ₹200 lakh. End Yr 1: cost incurred ₹90 lakh; total estimated cost now ₹230 lakh.
- Total cost 230 > revenue 200 → **loss ₹30 lakh**, Rule C triggered — whole loss hits Yr 1.
- Stage = 90 ÷ 230 = 39.13%; Revenue = 39.13% × 200 = ₹78.26 lakh.
- Cumulative P&L must show −30: Total expense = 78.26 + 30 = ₹108.26 lakh.
- Provision for future loss = 108.26 − 90 = **₹18.26 lakh**.
- P&L Yr 1: Revenue 78.26 − Cost 90 − Provision 18.26 = **Net loss 30.00**.
- Trap: weak answer books only 90 − 78.26 = 11.74 loss. AS 7 demands the full 30 now.
- If a **profitable** contract turns loss-making (Rule A → C), the current year must **reverse prior profit AND front-load the whole remaining loss** (cumulative = full expected loss).

## Disclosures
- Contract revenue recognised in the period.
- Methods used to determine contract revenue recognised.
- Methods used to determine stage of completion.
- For contracts in progress: aggregate (costs incurred + recognised profits − recognised losses) to date; advances received; retentions.
- Present gross amount **due from** customers (asset) and **due to** customers (liability).
- Contingencies (AS 29): warranties, penalties, disputed claims.
- **Retention** = earned & billed but withheld till defect-liability lapses (asset). **Advance** = paid before work done (liability). Disclosed separately.

## Exam traps & must-remember
- **Loss-override (most common):** check total cost vs total revenue BEFORE stage arithmetic; book entire foreseeable loss now.
- Never compute stage from billings or cash received — those only feed the due-from/to line.
- Exclude un-installed materials & subcontractor advances from cost-to-date numerator (they stay as WIP asset).
- Don't slip period costs (non-reimbursable admin, selling, unallocated R&D, idle-plant depreciation) into contract cost.
- Unapproved variation/claim → NOT revenue until probable + measurable.
- On new estimate, recompute cumulative on new figure, subtract prior — don't keep old percentage.
- Balance-sheet due-from/due-to computed **per contract**; aggregate positives and negatives separately.
- Completed-contract method is a distractor — not allowed.
- Rule B "no profit" can still show a loss if some cost is irrecoverable.
- Forgetting to reverse prior-year profit when contract turns loss-making loses marks.
- Missing a combine/segment decision changes the loss provision entirely.
- Delay penalty probable → reduce total revenue first (may flip into Rule C).
- Rule B → Rule A switch and all estimate revisions are **prospective** — never reopen a prior year.

## One-line recall
- Earn as you build: POCM mandatory; completed-contract banned.
- Gradual profit, immediate full loss — Rule C overrides A and B.
- Stage % = work-performed cost ÷ total cost; exclude unused materials & advances; never use billings.
- Revenue = price + variations/claims/incentives (probable + measurable) − penalties.
- Fix the unit (combine/segment) before anything — it decides loss offset.
- Due from/to customer = (costs + profit − loss) − billings, per contract; earned vs billed.
- Estimate change = AS 5 prospective catch-up in current year.
