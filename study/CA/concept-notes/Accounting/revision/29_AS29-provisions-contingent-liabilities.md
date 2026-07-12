# AS 29: Provisions, Contingent Liabilities & Contingent Assets

## Snapshot
Draws the boundary through uncertainty about whether/when/how much money moves. Answers: when to **record** (provision), when to **disclose** (contingent liability), when to touch a **gain** (contingent asset — almost never). Prudence with limits: anticipate losses, never anticipate profits. Also defines what is NOT a provision (depreciation, doubtful debts, accruals).

## Core concepts
Two dials: (1) does a **present obligation** even exist? (2) probability of outflow.

**Threshold ladder:** Remote (<~5-10%) < Possible (not probable) < **Probable (>50%, "more likely than not")** < Virtually certain (~100%).

| Word | Outflow (loss) | Inflow (gain) |
|---|---|---|
| Remote | Ignore (no note) | Ignore |
| Possible | Contingent liability (disclose) | Ignore |
| Probable | **Provision (record)** | Contingent asset (disclose in Board report) |
| Virtually certain | (ordinary liability) | Recognise the asset |

Loss: disclose at *possible*, record at *probable*. Gain: disclose at *probable*, record at *virtually certain* — always one rung stricter.

**Definitions:** Provision = liability of *uncertain timing or amount* (substantial estimation). Contingent liability = (a) possible obligation, OR (b) present obligation not recognised because outflow not probable or not reliably measurable — **never recorded**, notes only. Contingent asset = possible asset from past events. Obligation = **legal** (contract/statute) OR **constructive** (past practice/published policy creating valid expectation in others).

## Key provisions / rules
**RECOGNITION — provision needs ALL 3:**
1. **Present obligation** (legal or constructive) from a **past (obligating) event** — "no realistic alternative" to settle; future conduct you can still change is NOT an obligating event.
2. **Probable** outflow (>50%).
3. **Reliable estimate** (fails only in extremely rare cases).

If any fails → contingent liability (disclose, unless remote) or nothing.

**Specific rules:**
- **Future operating losses:** NO provision (no past event; test assets for AS 28 impairment instead).
- **Onerous contract** (unavoidable cost > benefit): provide the **least net cost of exit** = lower of (cost to fulfil) and (penalty to cancel). Impair dedicated assets first.
- **Restructuring:** provision only if **detailed formal plan + valid expectation raised** (announcement/implementation started) **before** year-end → constructive obligation. Board decision alone is not enough. Provide only **direct** costs; NOT retraining/relocating *continuing* staff, marketing, new systems, or future operating losses.
- **Warranties:** provision required (sale = obligating event).
- **Reimbursements:** separate asset **only when virtually certain**, capped at provision amount; P&L may be shown net, B/S gross.
- **Repairs/refurbishment of own assets:** NO provision.
- **Decommissioning/site restoration:** provision at **present value**, capitalised into asset (AS 10); discount **unwinds** as finance cost.
- **Refund under published policy:** provision (constructive obligation).
- **Guarantee for third party's borrowing:** contingent liability while default only possible; becomes provision if default probable.
- **Contingent asset:** never recognised; disclose (Board's report) only if inflow **probable**; recognise as asset when **virtually certain**.
- A *new/draft law* rarely creates a present obligation for future compliance (obligating event is your own future operation, avoidable).

**MEASUREMENT = best estimate** to settle at B/S date:
- **Large population** (warranties) → **expected value** (probability-weighted).
- **Single obligation** (one lawsuit) → **most likely outcome** (adjust if outcomes cluster higher/lower).
- Take account of risks/uncertainties but no **excessive** provisions.
- Future events reflected only with sufficient objective evidence; new legislation only when **virtually certain to be enacted**.
- Do **NOT** deduct expected asset-disposal gains.
- **Discount** to PV when time value material, **pre-tax** rate; unwind each year.
- Measure **pre-tax** (tax effects → AS 22).

**Review each B/S date:** adjust to current best estimate; **reverse** if outflow no longer probable; **use provision only for its original purpose** (anti-concealment rule). Change in a *capitalised* provision's estimate adjusts the **asset**, not P&L.

**Provision vs Accrual vs Reserve:** Provision = uncertain liability, **charge against profit** (AS 29). Accrual = near-certain liability (little estimation, not AS 29). Reserve = **appropriation of profit** (equity, not AS 29).

**Scope-out:** financial instruments at fair value; ordinary executory contracts (unless onerous); items under other AS (taxes-AS 22, retirement benefits-AS 15, construction losses-AS 7, leases).

## Journal entries
| Event | Entry |
|---|---|
| Create provision | Dr Expense / Cr Provision |
| Spend later | Dr Provision / Cr Bank (up to provision) |
| Excess over provision | Dr Expense / Cr Bank |
| Reverse (no longer needed) | Dr Provision / Cr Income |
| Reimbursement (virtually certain) | Dr Receivable (≤ provision) / Cr Expense |
| Unwind discount | Dr Finance Cost / Cr Provision |
| Decommissioning | Dr Asset (PPE) / Cr Provision |
| Contingent liability | **No entry** |
| Contingent asset (virtually certain) | Dr Asset / Cr Income |

## Worked mini-example
**Warranty:** 40,000 cars; 75% no repair, 20% minor @₹1,000, 5% major @₹4,000.
Expected/car = 0.75×0 + 0.20×1,000 + 0.05×4,000 = **₹400**. Provision = 40,000 × 400 = **₹1.60 crore**. Dr Warranty Expense / Cr Provision.

**Decommissioning:** restoration ₹80,00,000 in 5 yrs @8%. Initial provision = 80,00,000 / 1.08⁵ = **₹54,44,839** (Dr Asset / Cr Provision). Year-1 unwind = 8% × 54,44,839 = ₹4,35,587 (Dr Finance Cost / Cr Provision) → ₹58,80,426 = 80L/1.08⁴. ✓ If future estimate later revised, re-measure to PV of new estimate over remaining years; the estimate change rides with the **asset**, only unwinding hits finance cost.

## Disclosures
- **Provision (each class):** movement table — opening + additions + increase from unwinding/rate change − amounts used − unused reversed = closing; plus nature, expected timing, uncertainties, expected reimbursement. (No comparatives required.)
- **Contingent liability (each class, unless remote):** brief description of nature; estimate of financial effect; uncertainties; possibility of reimbursement.
- **Contingent asset:** not recognised; if inflow **probable**, disclose brief description + estimate in **Board's report** (not usually the notes); if only possible/remote → no disclosure.
- **Seriously prejudicial exemption** (extremely rare): may omit detail but must disclose general nature of dispute + fact of non-disclosure + reason.
- Balance sheet: Provisions under liabilities (current/non-current per Schedule III); reimbursement shown as separate asset, not netted.

## Exam traps & must-remember
- "Provision" for depreciation/doubtful debts = asset adjustment, NOT AS 29.
- Future operating losses → no provision (consider AS 28).
- Board decision alone ≠ obligation; need announcement/valid expectation before year-end; direct costs only.
- Reimbursement = separate asset (virtually certain, ≤ provision); B/S gross, P&L may be net.
- Contingent asset at 80% "probable" → disclose only, never recognise.
- Remote contingent liability → disclose nothing.
- Single obligation → most likely outcome, NOT expected value.
- Discount long-dated provisions and unwind each year.
- Use provision only for its original purpose.
- "Probable" = >50%, not "highly probable".
- Ignore expected asset-disposal profits in measurement.
- Constructive obligation (published refund policy) counts even without legal duty.
- Capitalised provision's estimate change → adjust asset, not P&L.
- Provisions are pre-tax.
- **AS 4 link:** post-year-end evidence of a condition existing at year-end = adjusting event → can convert contingent liability into a provision. Proposed dividends not provided.

## One-line recall
- Provision needs: present obligation from past event + probable outflow (>50%) + reliable estimate.
- Traffic light: remote=ignore, possible=disclose, probable=record.
- Gains are one rung stricter: recognise only when virtually certain.
- Measure = expected value (population) / most likely (single); PV if material, pre-tax.
- Reimbursement = separate asset if virtually certain, capped at provision.
- Use each provision only for its own purpose; reverse if no longer probable.
