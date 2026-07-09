# Q&A — Building the Projected Income Statement

Practice bank for Chapter 10. Work each question before reading the answer. The income statement is a **waterfall assembled under accounting rules**, so these problems test three things at once: the *order* of the lines, the *base* each line is computed on, and the *links* that reach into other schedules. Every number is built so you can reproduce it cell-for-cell in Excel and watch each subtotal tie.

---

## Section A — Concept Checks (test the WHY)

**A1. Why is the income statement described as a "funnel of sieves" rather than a free-form list of numbers?**

Because the order is load-bearing, not cosmetic. Revenue is poured in at the top and each sieve below catches exactly one category of cost — direct costs, then operating costs, then financing costs, then tax — letting the rest fall through. The "you can only catch it once" rule means every cost belongs to one and only one sieve, and the fixed order means each subtotal (gross profit, EBITDA, EBIT, pre-tax income) is a genuine, comparable measure. Reorder the sieves and every subtotal below the swap becomes meaningless, and every downstream number — EPS, retained earnings, valuation — inherits the distortion.

**A2. Why do we bother computing intermediate subtotals instead of one giant subtraction from revenue to net income?**

Because each subtotal answers a *different stakeholder's question*. Gross profit asks "is the product itself viable?" EBITDA asks "how much cash-like operating earnings does the core business throw off, before financing and accounting choices?" EBIT asks "how profitable are operations after the real cost of using up long-lived assets?" Pre-tax income asks "what's left after lenders?" and net income asks "what accrues to shareholders?" One giant subtraction would give the right bottom line but destroy every lens in between — and those lenses are what analysts, lenders, and valuation multiples actually use.

**A3. Why must EBITDA sit physically ABOVE the depreciation line in the layout?**

Because EBITDA is *by definition* earnings **before** interest, taxes, depreciation, and amortization. If your "EBITDA" row sits below the D&A line, you have subtracted depreciation and therefore computed EBIT — you've mislabeled it. The layout enforces the definition: D&A appears on its own row *between* EBITDA and EBIT so that EBITDA − D&A = EBIT is visible and true. A structural check follows for free: EBITDA must always be ≥ EBIT, and the gap must equal D&A.

**A4. Why is interest expense a LINK to the debt schedule rather than an assumption typed on the income statement?**

Because interest is an *output* of the debt schedule (rate × average debt balance), not an independent judgment. If you hardcode it, the model won't respond when debt or rate assumptions change, and — worse — the interest tax shield will be wrong because tax is computed on pre-tax income, which sits below interest. Linking it also deliberately creates the model's central circularity (interest → net income → cash → debt → interest), which is intentional and managed with iterative calculation, not something to avoid by hardcoding.

**A5. Why is tax computed on pre-tax income (EBT) and never on EBIT or net income?**

Because EBT is the legally correct tax base: it is what remains after lenders are paid, and interest is tax-deductible. Taxing EBIT ignores the interest tax shield and overstates tax (you'd be taxing money that was already paid to lenders pre-tax). Taxing net income is circular nonsense — net income is *defined* as EBT minus tax, so you'd need the answer to compute the input. Always: `Tax = EBT × effective rate`.

**A6. Why use the effective tax rate from recent history rather than the statutory rate?**

Because the rate a company actually pays diverges from the headline statutory rate due to permanent differences, tax credits, foreign-rate mixing, and similar items. The recent historical effective rate (tax expense ÷ pre-tax income over 2–3 years) captures the company's real tax profile. You can nudge it toward statutory if you expect the special items to fade — but that is a documented judgment, made in a visible, blue, labeled assumption cell, never a number buried inside the tax formula.

**A7. Why does font-color coding (blue input, black formula, green cross-sheet link) matter enough to call it the single most important modeling habit?**

Because color encodes the *source* of every number, letting a reviewer read the model's logic at a glance without clicking into each cell. Blue instantly flags what is a changeable assumption; green flags what depends on another schedule; black flags derived arithmetic. When a number looks wrong, color tells you immediately whether to check an assumption, a linked schedule, or a formula — turning an audit of the whole sheet into a targeted trace up one wire.

**A8. Why should margins fall monotonically as you read down the statement, and what does it mean if one rises?**

Because with a costs-positive convention every line below revenue only *subtracts*, so each successive subtotal must be a smaller fraction of revenue than the one above it. Gross margin ≥ EBITDA margin ≥ EBIT margin ≥ net margin, always. If a margin *rises* going down, a cost has been added instead of subtracted — a sign-convention error — and you've found a bug purely from the margin trend, before checking a single formula.

---

## Section B — Build / Computational Problems

Reproduce each in Excel. Costs-positive convention throughout ($ in millions).

**B1. Single-year build with two operating cost lines.**
Given: Revenue 800.0; COGS 62% of revenue; SG&A 15% of revenue; R&D 5% of revenue; D&A 30.0 (linked); interest expense 18.0 (linked); interest income 2.0 (linked); effective tax rate 27%. Build the full waterfall and self-check with margins.

**Answer.**

| Line | Formula | Result |
|---|---|---|
| Revenue | link | 800.0 |
| COGS | 800 × 62% | 496.0 |
| **Gross profit** | 800 − 496 | **304.0** |
| SG&A | 800 × 15% | 120.0 |
| R&D | 800 × 5% | 40.0 |
| **EBITDA** | 304 − 120 − 40 | **144.0** |
| D&A | link | 30.0 |
| **EBIT** | 144 − 30 | **114.0** |
| Interest expense | link | 18.0 |
| Interest income | link | 2.0 |
| **Pre-tax income** | 114 − 18 + 2 | **98.0** |
| Income tax | 98 × 27% | 26.46 |
| **Net income** | 98 − 26.46 | **71.54** |

Self-check via margins: gross 304/800 = 38.0%; EBITDA 144/800 = 18.0%; EBIT 114/800 = 14.25%; net 71.54/800 = 8.94%. Margins fall monotonically ✓, and EBITDA − D&A = 144 − 30 = 114 = EBIT ✓.

**B2. Two-year projection from growth and margin assumptions.**
Given: Year-0 revenue 1,500.0, growing 6% per year; COGS 58% of revenue; SG&A 20% of revenue; D&A 50, 55; interest expense 20, 17; interest income 3, 3; tax rate 25%. Build Years 1–2 and confirm the formulas copied correctly.

**Answer.**

| Line | Year 1 | Year 2 |
|---|---|---|
| Revenue (×1.06) | 1,590.0 | 1,685.4 |
| COGS (58%) | 922.2 | 977.5 |
| **Gross profit** | **667.8** | **707.9** |
| SG&A (20%) | 318.0 | 337.1 |
| **EBITDA** | **349.8** | **370.8** |
| D&A | 50.0 | 55.0 |
| **EBIT** | **299.8** | **315.8** |
| Interest expense | 20.0 | 17.0 |
| Interest income | 3.0 | 3.0 |
| **Pre-tax income** | **282.8** | **301.8** |
| Income tax (25%) | 70.7 | 75.4 |
| **Net income** | **212.1** | **226.3** |

Self-check: revenue 1,500 × 1.06 = 1,590 ✓; 1,590 × 1.06 = 1,685.4 ✓. EBITDA margin Year 1 = 349.8/1,590 = 22.0%; Year 2 = 370.788/1,685.4 = 22.0% — identical, confirming the ratio-driven formulas copied across without drift ✓. Net income grows 226.3/212.1 − 1 = 6.7%, faster than revenue's 6%, because interest expense is falling (deleveraging lifts the bottom line) — exactly the insight the waterfall surfaces.

**B3. Effective tax rate from history, then apply it.**
Historicals: Year −2 pre-tax 200.0, tax 46.0; Year −1 pre-tax 220.0, tax 52.8. Forecast pre-tax income is 240.0. Compute the two-year average effective rate, then forecast tax and net income.

**Answer.** Implied rates: 46.0/200.0 = 23.0%; 52.8/220.0 = 24.0%. Two-year average = (23.0% + 24.0%)/2 = **23.5%**. Forecast tax = 240.0 × 23.5% = **56.4**; net income = 240.0 − 56.4 = **183.6**. The 23.5% belongs in a single blue, labeled assumption cell that every forecast year's tax formula references — never typed as `*0.235` inside the formula.

**B4. Reconciling — back into a clean EBITDA when D&A is embedded.**
A historical statement reports Revenue 1,000, COGS 650 (which *includes* 20 of depreciation), SG&A 150 (which includes 10 of depreciation). Total D&A is 30. Compute a clean EBITDA two independent ways and reconcile.

**Answer.**
Method 1 (add D&A back to reported EBIT): Reported EBIT = 1,000 − 650 − 150 = 200. EBITDA = EBIT + D&A = 200 + 30 = **230**.
Method 2 (strip D&A out of the cost lines first): Clean COGS = 650 − 20 = 630; clean SG&A = 150 − 10 = 140; EBITDA = 1,000 − 630 − 140 = **230**.
Both give 230 ✓. This is why models usually *pull D&A out* onto its own line: it makes EBITDA and EBIT both explicit and prevents the classic double-count (subtracting the same 30 once inside COGS/SG&A and again on a separate D&A row).

**B5. Loss year — the tax-benefit edge case.**
Forecast pre-tax income is −50.0 with a 25% rate. Compute tax and net income (a) letting the flat rate flow through, and (b) flooring tax with `=MAX(0, EBT) × rate`. Explain the difference.

**Answer.**
(a) Flat rate: tax = −50 × 25% = **−12.5** (a tax *benefit*); net income = −50 − (−12.5) = **−37.5**. This implicitly assumes the loss immediately shields other income or generates a refund.
(b) Floored: `MAX(0, −50) = 0`, so tax = 0; net income = **−50.0**. This assumes no benefit today — closer to reality when the loss becomes a net-operating-loss (NOL) carryforward that only shields *future* taxable income. Neither is universally correct; the point is to decide deliberately and flag the assumption, because the two answers differ by 12.5 on a 50 loss.

**B6. Spot the operating-leverage effect (semi-fixed cost).**
Revenue 2,000 growing 8%; COGS 55% of revenue; SG&A is semi-fixed at 250 in Year 0 growing only 5% per year; D&A 80; interest 30; interest income 4; tax 26%. Compute Year 1, then state what happens to EBIT margin over time and why.

**Answer.** Year 1: Revenue = 2,000 × 1.08 = 2,160.0; COGS = 2,160 × 55% = 1,188.0; gross profit = 972.0; SG&A = 250 × 1.05 = 262.5; EBITDA = 972 − 262.5 = 709.5; EBIT = 709.5 − 80 = 629.5; pre-tax = 629.5 − 30 + 4 = 603.5; tax = 603.5 × 26% = 156.9; net income = 603.5 − 156.9 = **446.6**. EBIT margin Year 1 = 629.5/2,160 = 29.1%. Because SG&A grows at 5% while revenue grows at 8%, the cost base shrinks *as a share of revenue* each year, so EBIT margin **expands** — operating leverage. Test of a live model: change SG&A growth to 8% and the EBIT margin should go flat, proving the formula is driven by the assumption cell rather than hardcoded.

---

## Section C — Interview-Style Questions (with model answers)

**C1. "Walk me through an income statement from top to bottom."**
Model answer: "Start with revenue. Subtract COGS to get gross profit — that tells you whether the product itself is viable. Subtract operating expenses like SG&A and R&D to get EBITDA, the cash-like operating earnings before financing and accounting choices. Subtract depreciation and amortization to get EBIT, or operating income, which respects the real cost of using up long-lived assets. Below EBIT you leave operating territory: subtract interest expense and add interest income to get pre-tax income. Apply the effective tax rate to pre-tax income for tax expense, and what remains is net income — the profit belonging to shareholders. The discipline is that everything above EBIT is operating and everything below is financing, non-operating, or tax."

**C2. "Why is EBITDA so popular in valuation, and what does it deliberately ignore?"**
Model answer: "EBITDA strips out three things that differ across companies for reasons unrelated to core operating performance: interest, which reflects a financing choice; taxes, which reflect jurisdiction and structure; and depreciation and amortization, which are non-cash allocations of past capital spending. Removing them makes EBITDA the cleanest apples-to-apples comparison of operating earnings, which is why EV/EBITDA is a headline multiple. Its blind spot is exactly its convenience: by ignoring D&A it ignores the real cost of maintaining a capital-intensive asset base, so for a heavy-capex business EBIT or free cash flow is fairer. EBITDA is not a cash flow measure — it ignores working capital and capex entirely."

**C3. "If I increase a company's debt, walk me through what happens to net income."**
Model answer: "More debt raises interest expense on the debt schedule, which flows into the income statement and lowers pre-tax income. Lower pre-tax income means lower tax — the interest tax shield — so tax falls by interest × tax rate. Net income falls, but by *less* than the gross interest increase, precisely because of that shield. Concretely, an extra 10 of interest at a 25% rate cuts pre-tax income by 10 and tax by 2.5, so net income falls by 7.5. And because interest links to the debt schedule while the debt schedule depends on cash generated from net income, this change also triggers the model's circularity."

**C4. "Where do one-time items go, and why does it matter?"**
Model answer: "Below EBIT, in the non-operating section. Items like a legal settlement, a gain on an asset sale, or an FX effect are not part of the repeatable operating engine, so placing them below EBIT keeps EBIT and EBITDA reflecting true recurring earning power. If you left a one-time gain above EBIT, you'd inflate operating margin and mislead anyone using that margin to forecast or value the business. In a projection you typically forecast one-time items as zero in future years, because you don't forecast next year's lawsuit."

**C5. "Your model's income statement won't calculate — you get a circular reference warning. What's going on and is it a bug?"**
Model answer: "It's usually intentional, not a bug. Interest expense links to the debt schedule; the debt balance depends on how much cash is available to repay debt; available cash depends on net income; and net income depends on interest. That's a genuine loop. You resolve it by enabling iterative calculation — File, Options, Formulas — typically 100 iterations at a max change of 0.001. Professionals also wire a circularity-breaker switch: a cell that forces interest to a hardcoded value when set to zero, so if the model spirals into #REF! or #VALUE! errors you can reset it, then flip the switch back on. If the circularity appeared unexpectedly, I'd check I hadn't accidentally referenced a downstream cell, but the interest–debt loop itself is expected."

---

## Section D — Common-Error Spotting (what is wrong?)

**D1. Broken formula — EBITDA below D&A.**
```
EBITDA   D15 = D12 - D13 - D14 - D16   ' D16 is depreciation
EBIT     D17 = D15 - D16
```
**What's wrong:** D&A (D16) is subtracted inside the EBITDA line *and* again to get EBIT — a double count, and the "EBITDA" number is actually below-D&A. EBITDA is *before* D&A by definition. Fix: `D15 = D12 - D13 - D14` (operating opex only), then `D17 = D15 - D16`. Check afterward that EBITDA ≥ EBIT with the gap equal to D&A.

**D2. Wrong tax base.**
```
Income tax   D22 = D17 * D$8      ' D17 is EBIT, D8 is the tax rate
```
**What's wrong:** Tax is applied to EBIT, ignoring interest. That overstates tax by taxing money already paid to lenders pre-tax and destroys the interest tax shield. Fix: tax the pre-tax income line: `D22 = D21 * D$8`.

**D3. Hardcode buried in a formula.**
```
Income tax   D22 = D21 * 0.25
```
**What's wrong:** The 25% rate is invisible and unauditable — nobody can see or globally change it, and it can silently differ from the rate used elsewhere. Fix: put the rate in a labeled blue cell (say D8) and reference it: `D22 = D21 * D$8`.

**D4. Sign-convention drift.**
```
Pre-tax income   D21 = D17 + D18 + D19    ' D18 = interest expense, stored positive
```
**What's wrong:** Under costs-positive convention, interest expense (D18) must be *subtracted*. Adding it makes pre-tax income larger than EBIT — impossible when a cost is deducted. Symptom: pre-tax income exceeds EBIT and the pre-tax margin rises above the EBIT margin. Fix: `D21 = D17 - D18 + D19` (subtract expense, add income).

**D5. Interest hardcoded instead of linked.**
```
Interest expense   D18 = 25
```
**What's wrong:** The number won't move when debt or rate assumptions change, so the tax shield and net income are wrong under any scenario, and the intended debt–interest circularity never forms. Fix: `D18 = -Debt_Schedule!D30` (or link to the debt schedule's total interest). A hardcode is only acceptable as a clearly flagged blue placeholder before the debt schedule exists.

**D6. Formula inconsistency across columns.**
```
SG&A   E13 = E10 * E$6     ' Year 1: % of revenue
       F13 = 198           ' Year 2: hardcoded over the copied formula
```
**What's wrong:** Year 2's SG&A was typed over as a constant, so it no longer responds to revenue — the number-one source of silent model errors. Fix: restore the copied formula `F13 = F10 * F$6` and arrow across the row watching the formula bar, or use Show Formulas, to confirm every column is structurally identical.

**D7. Depreciation double-counted across schedules.**
```
COGS   D11 = -D10*D$5           ' pulled from historicals that already include D&A
D&A    D16 = -PPE_Schedule!D40  ' full depreciation shown again on its own line
```
**What's wrong:** If the historical COGS ratio already embeds depreciation and you also show a separate D&A line, that depreciation is subtracted twice, understating EBIT and net income. Fix: decide once — either strip D&A out of the COGS ratio (recommended, so EBITDA/EBIT are clean) or leave it in and don't show a separate D&A line. Never both.

**D8. Percent-of-revenue applied to a fixed cost.**
```
Rent   D14 = D10 * D$7    ' rent modeled as % of revenue
```
**What's wrong:** Rent is a fixed (or semi-fixed) cost; modeling it as a percent of revenue makes it grow with sales, so as revenue rises the *real* fixed cost is overstated and, conversely, EBIT margin is held artificially flat when it should expand with operating leverage. Fix: model rent as prior year × (1 + a small growth rate), e.g. `D14 = C14 * (1 + D$7)`, and eyeball the margin trend for a plausible operating-leverage story.

---

*End of Chapter 10 Q&A bank. If your B-section builds tie to the stated self-checks and you can spot every D-section error on sight, you can assemble a fully-linked projected income statement: links and light arithmetic, one sign convention, every assumption visible and labeled.*
