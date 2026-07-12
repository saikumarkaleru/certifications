# Chapter 22 — AS 22: Accounting for Taxes on Income

## Snapshot
Tax expense in the P&L must match the accounting profit above it, not the accident of cash tax the return demanded. AS 22 recognises the tax effect of an item in the same period as the item. **Tax Expense = Current Tax + Deferred Tax.** Deferred tax arises only from **timing differences** (which reverse), never from permanent differences.

## Core concepts
- **Current tax** = tax payable on the year's *taxable income* per the Income-tax Act (straight off the return).
- **Deferred tax** = tax effect of **timing differences** — differences between accounting and taxable income that *originate in one period and are capable of reversal* in later periods.
- **Permanent differences** — enter only one computation, ever; never reverse → NO deferred tax; only shift the effective rate. Examples: income-tax penalties, disallowed donations/CSR, Sec. 40A disallowances, exempt agricultural income, tax-free interest/dividends.
- **Timing differences** — same amount hits both computations in different periods → deferred tax. Examples: depreciation (book SLM vs tax WDV block); Sec. 43B items (bonus, PF, gratuity, bank interest, statutory dues — allowed only on payment); provisions (doubtful debts, warranty); unabsorbed depreciation & carried-forward business losses.
- Acid test: *"Does the same amount eventually appear on the other side?"* Yes = timing; No = permanent. **Recurring ≠ reversing** (a penalty every year is a fresh permanent difference each year).
- AS 22 uses the **liability method** (re-measures on rate change) computed on the **timing-difference / income-statement** lens (not Ind AS 12's balance-sheet temporary-difference lens). No OCI: periodic movement → P&L; only opening transition adjustment → revenue reserves.

## Key provisions / rules
**Direction — write timing difference as (Tax deduction − Book):**

| Situation | Taxable income today | Future tax | Balance |
|---|---|---|---|
| Tax dep > Book dep; 43B expense allowed now | Lower | Higher | **DTL** |
| Book dep > Tax dep; provisions disallowed now; c/f losses | Higher | Lower | **DTA** |

- **DTL — recognised in full, always.** Prudence: never hide a future obligation. No certainty test.
- **DTA — conditional:**
  - **Tier 1 (reasonable certainty)** for ordinary timing differences: recognise to the extent of reasonable certainty of sufficient future taxable income (convincing evidence: existing profitable operations, firm orders, track record).
  - **Tier 2 (virtual certainty + convincing evidence)** for **unabsorbed depreciation / carried-forward losses** — stricter, because a loss history makes future profits doubtful. Virtual certainty needs almost-assured concrete evidence (e.g. signed binding long-term contract). A mere forecast/turnaround hope is NOT enough. Test each layer on its own tier.
  - **Convincing evidence = yes:** signed non-cancellable long-term contracts, firm binding order books, durable existing profits. **= no:** management budgets, "industry recovering," unsigned deals, cost-cut plans not executed, optimism.
- **P&L charge for the year = movement in cumulative deferred-tax balance × rate**, not the isolated year's difference.
- **Review each balance-sheet date:** write down a DTA when realisation no longer certain; reverse the write-down when certainty returns; recognise a previously-unrecognised DTA in the year certainty first arrives (no restatement of the earlier year).

**Measurement:**
- Rates **enacted or substantively enacted** by the balance sheet date; use the rate expected at *reversal*. Do not anticipate un-enacted future changes. A post-year-end rate change is generally a non-adjusting event — disclose, don't re-measure.
- **Average rate** across slabs; include **surcharge + cess**; use the actual/opted concessional rate that will tax the reversing rupee.
- **NO discounting** of DTA/DTL.
- **Rate change → re-measure the entire existing balance** at the new rate; effect goes to current-year P&L (in full, not spread).
- **MAT credit is NOT deferred tax** — shown separately as "MAT Credit Entitlement" (Guidance Note).

**Depreciation — the flagship:** book and tax depreciation write off the *same total* over life (differ only in pattern), so the cumulative difference reverses to zero → guaranteed timing difference. Revaluation: extra book depreciation on revalued portion has no tax match → timing difference (contrast Ind AS 12).

## Journal entries
```
Create DTL:   P&L A/c            Dr    to  Deferred Tax Liability
Reverse DTL:  Deferred Tax Liab. Dr    to  P&L A/c
Create DTA:   Deferred Tax Asset Dr    to  P&L A/c
Reverse DTA:  P&L A/c            Dr    to  Deferred Tax Asset
Current tax:  P&L A/c            Dr    to  Provision for Tax
```
Sign rule: create/increase DTL → Dr P&L (more expense); create/increase DTA → Cr P&L (less expense); reversals flip.

## Worked mini-example
PBT 5,00,000; book dep 40,000, tax dep 1,00,000; rate 25%.
- Taxable income = 5,00,000 + 40,000 − 1,00,000 = 4,40,000; current tax = 1,10,000.
- Timing diff = 60,000 (tax dep > book) → DTL = 25% × 60,000 = 15,000.
- Total tax = 1,10,000 + 15,000 = 1,25,000 → ÷ 5,00,000 = **exactly 25%** (deferred tax normalised the rate). PAT = 3,75,000.

Rate-change (Ex 4): DTL 3,00,000 at 30% (diff 10,00,000). Rate falls to 25%: required 25%×10,00,000 = 2,50,000 → ₹50,000 **credit** to P&L on the *whole* opening balance. Fresh diff 2,00,000 × 25% = 50,000 charge. Net Year-4 deferred tax = 0; closing DTL = 3,00,000 (= 25% × 12,00,000). Trap: applying 25% only to the new layer.

## Disclosures
- **Break-up of major components** of the deferred-tax balance by type (depreciation, doubtful debts, 43B items, c/f losses) — shown separately, not a single net number.
- **Nature of the evidence** supporting a DTA where there is unabsorbed depreciation / carry-forward losses (basis for virtual certainty) — mandatory, heavily tested.
- Transition/first-adoption: accumulated deferred-tax balance adjusted against **revenue reserves**, not current P&L.

**Balance-sheet presentation:** net DTA or DTL as a single **non-current** figure per *enterprise* (Schedule III). Offset DTA vs DTL only if legally enforceable right of set-off AND same governing tax law. Never net against current tax (advance tax / provision). Do NOT cross-net separate group entities — a group may show both a net DTA and a net DTL.

## Exam traps & must-remember
- Never defer a permanent difference (penalty, exempt income, CSR); strip permanents first.
- Get direction right: (Tax − Book) positive = DTL, negative = DTA.
- No DTA on c/f losses without virtual certainty + stated evidence.
- Don't confuse reasonable vs virtual certainty (virtual only for unabsorbed dep & c/f losses).
- Never discount; never net against current tax; deferred tax is non-current.
- Re-measure the *whole* balance on a rate change (effect to current P&L).
- Review DTA yearly; recognise previously-unrecognised DTA when certainty arrives (no restatement).
- MAT credit ≠ DTA. Recurring ≠ reversing. Don't cross-net group DTA/DTL.

## One-line recall
- Tax Expense = Current Tax + Deferred Tax; deferred tax only on reversing (timing) differences.
- DTL always in full; DTA only on reasonable certainty (virtual certainty + evidence for unabsorbed dep / c/f losses).
- Measure at enacted/substantively-enacted rate incl. surcharge & cess; never discount; re-measure entire balance on rate change.
- Depreciation is the classic timing difference (book vs tax patterns sum to the same total).
- Present net, non-current, per enterprise; disclose components + evidence for loss-based DTA.
- Sanity check: no permanent differences ⇒ (Current + Deferred) ÷ PBT = statutory rate.
