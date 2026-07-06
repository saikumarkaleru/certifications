# Q&A — The PP&E and Depreciation Schedule

Practice bank for Chapter 12. Work each question before reading the answer. This chapter's engine is a single roll-forward — Closing = Opening + Capex − Depreciation — so the build problems are all about wiring that corkscrew correctly, keeping one number in one place, and watching three statements pull from it. Every number below is built so you can reproduce it cell-for-cell in Excel and watch it tie.

---

## Section A — Concept Checks (test the WHY)

**A1. Why does one physical asset base show up as three different numbers on three different statements?**

Because each statement asks a different question about the same machines. The cash flow statement asks *how much cash left the building this year* — so it shows the full **capex**. The income statement asks *what expense should be matched against this year's revenue* — so it shows only this year's **depreciation** slice. The balance sheet asks *what is still on the books* — so it shows **net PP&E**, the cost not yet depreciated. Same reality, three lenses: cash out now, cost recognised gradually, value remaining. The schedule exists to keep those three views of one asset base permanently reconciled.

**A2. Why model net PP&E with a roll-forward instead of forecasting the balance directly?**

Because a balance is not an independent fact — it is the accumulation of flows. Net PP&E today equals every dollar ever invested minus every dollar ever depreciated. Guessing the closing balance directly means guessing the sum of all history; rolling it forward (Opening + Capex − Depreciation) reconstructs it from this year's two flows on top of a known starting point. Modelling the stock directly also severs it from your assumptions, so a change in capex wouldn't move it. The roll-forward is the bridge from last year's stock to this year's, and it is the reason the model stays alive.

**A3. Why is depreciation a non-cash expense, and why does that single fact split capex and depreciation onto different statements?**

The cash left when the asset was bought — that outflow is capex, and it happens once, up front. Depreciation never moves cash; it is only the accounting act of spreading that already-spent cost across the years the asset earns revenue (the matching principle). Because the cash event and the expense recognition happen at different times, they must live on different statements: capex as an investing outflow when paid, depreciation as a matched expense spread over the asset's life. Confusing the two — expensing capex, or treating depreciation as a payment — is the root of most beginner errors.

**A4. Why must every opening balance after the first be a formula (`=prior closing`) rather than a typed number?**

Because that link *is* the corkscrew, and it is what guarantees no value leaks between years. If openings are hard-keyed, this year's opening ignores last year's capex and depreciation entirely — the schedule stops being a roll-forward and becomes four disconnected snapshots. Only `Opening = prior Closing` enforces that whatever ended last year starts this year exactly, so a change to any early assumption ripples all the way down the timeline.

**A5. Why key depreciation off the *opening* balance rather than the *closing* balance in a % method?**

Because opening is already fixed from last year, so there is no circularity: opening → depreciation → closing, a clean one-way chain. If you key depreciation off closing, you create a genuine loop — closing depends on depreciation, which depends on closing — and Excel throws a circular-reference error. Keying off opening (or a fixed gross base) keeps the logic acyclic and auditable.

**A6. Why should long-run capex be at least equal to depreciation for a going concern?**

Because capex is the tap and depreciation is the drain. If the drain permanently exceeds the tap, the tub empties — net PP&E shrinks toward zero and eventually goes negative, which is impossible in reality. Capex below depreciation means the company is consuming its asset base faster than it replaces it, i.e. quietly liquidating. Sometimes that is deliberate (a wind-down), but as a default it is a red flag that your capex assumption is too low.

**A7. Why does capex never unbalance the balance sheet, even though it is a large cash movement?**

Because capex is an asset *swap*, not an asset *creation*. Cash falls and net PP&E rises by the identical amount, both on the asset side, so total assets are unchanged and the sheet still balances with no plug. Depreciation is the mirror image: it lowers net PP&E on the asset side and, via reduced net income, lowers retained earnings on the equity side by the same amount — both sides fall together. The roll-forward is what makes both of these self-balance automatically.

---

## Section B — Build / Computational Problems

Convention for all builds: outflows are stored **negative** and the closing line is a literal `=SUM(opening, capex, depreciation)`, so the arithmetic reads itself.

**B1. The basic net roll-forward.** A company ends 2024 with net PP&E of **500**. Revenue: 2025 = 2,000; 2026 = 2,400; 2027 = 2,880. Capex = 6% of revenue. Depreciation = 10% of opening net PP&E, no depreciation on current-year capex. Build the schedule and give the three closing balances.

Step 1 — capex = 6% × revenue: `120.0, 144.0, 172.8`.

Step 2 — roll it forward; depreciation = 10% × that year's *opening*:

| Line | 2025 | 2026 | 2027 |
|---|---:|---:|---:|
| Opening net PP&E | 500.0 | 570.0 | 657.0 |
| (+) Capex | 120.0 | 144.0 | 172.8 |
| (−) Depreciation (10% × opening) | (50.0) | (57.0) | (65.7) |
| **Closing net PP&E** | **570.0** | **657.0** | **764.1** |

Verify the corkscrew: 500 + 120 − 50 = **570.0** → becomes 2026 opening; 570 + 144 − 57 = **657.0** → becomes 2027 opening; 657 + 172.8 − 65.7 = **764.1**. Each opening equals the prior closing and each depreciation is exactly 10% of that year's opening (50, 57, 65.7). Capex exceeds depreciation every year, so net PP&E grows — consistent with a growing business.

**B2. Half-year convention on the same data.** Re-run B1 but depreciate opening plus *half* of current-year capex: `Deprec = 10% × (Opening + 0.5 × Capex)`.

| Line | 2025 | 2026 | 2027 |
|---|---:|---:|---:|
| Opening | 500.0 | 564.0 | 644.4 |
| (+) Capex | 120.0 | 144.0 | 172.8 |
| (−) Depreciation | (56.0) | (63.6) | (73.08) |
| **Closing** | **564.0** | **644.4** | **744.12** |

2025 deprec = 10% × (500 + 0.5 × 120) = 10% × 560 = **56.0**; close = 500 + 120 − 56 = **564.0**. 2026 deprec = 10% × (564 + 72) = 10% × 636 = **63.6**; close = 564 + 144 − 63.6 = **644.4**. 2027 deprec = 10% × (644.4 + 86.4) = 10% × 730.8 = **73.08**; close = 644.4 + 172.8 − 73.08 = **744.12**. Half-year charges more depreciation than B1 (it captures new assets), so each closing sits below B1's — the schedule is faithfully reflecting the more realistic timing.

**B3. Straight-line depreciation waterfall.** Same data as B1, but depreciate on a straight-line, 10-year life, zero salvage basis: the existing 500 base depreciates at 500/10 = 50/year, and each capex vintage depreciates at capex/10, full-year in the year of spend.

| Depreciation source | Annual | 2025 | 2026 | 2027 |
|---|---:|---:|---:|---:|
| Existing base (500/10) | 50.0 | 50.0 | 50.0 | 50.0 |
| 2025 capex (120/10) | 12.0 | 12.0 | 12.0 | 12.0 |
| 2026 capex (144/10) | 14.4 | — | 14.4 | 14.4 |
| 2027 capex (172.8/10) | 17.28 | — | — | 17.28 |
| **Total depreciation** | | **62.0** | **76.4** | **93.68** |

Roll-forward with the waterfall depreciation:

| Line | 2025 | 2026 | 2027 |
|---|---:|---:|---:|
| Opening | 500.0 | 558.0 | 625.6 |
| (+) Capex | 120.0 | 144.0 | 172.8 |
| (−) Depreciation | (62.0) | (76.4) | (93.68) |
| **Closing** | **558.0** | **625.6** | **704.72** |

Verify: 500 + 120 − 62 = **558.0** ✓ → 558 + 144 − 76.4 = **625.6** ✓ → 625.6 + 172.8 − 93.68 = **704.72** ✓. In Excel the waterfall is a triangular grid — each vintage starts only in its own year (the diagonal), and you `SUM` down each year's column.

**B4. Gross PP&E and accumulated depreciation, with a disposal.** Start 2025 with gross PP&E **900** and accumulated depreciation **400** (net = 500, matching B1–B3). Capex 120 (2025) and 144 (2026). Use the straight-line depreciation from B3 (62.0, then 76.4). In 2026 the company sells an asset that originally cost **60** with **25** of accumulated depreciation (net book value 35). Build both roll-forwards and derive net PP&E.

Gross:

| Line | 2025 | 2026 |
|---|---:|---:|
| Opening gross | 900.0 | 1,020.0 |
| (+) Capex | 120.0 | 144.0 |
| (−) Disposal at cost | — | (60.0) |
| **Closing gross** | **1,020.0** | **1,104.0** |

Accumulated depreciation:

| Line | 2025 | 2026 |
|---|---:|---:|
| Opening accumulated | 400.0 | 462.0 |
| (+) Depreciation for year | 62.0 | 76.4 |
| (−) Accum. on disposal | — | (25.0) |
| **Closing accumulated** | **462.0** | **513.4** |

Net PP&E = gross − accumulated: 2025 = 1,020 − 462 = **558.0** (matches B3's 2025 close exactly — the two methods agree with no disposals). 2026 = 1,104 − 513.4 = **590.6**. The disposal removed net book value of 60 − 25 = 35, so 2026 net sits exactly 35 below B3's 625.6 (625.6 − 35 = 590.6). Everything ties.

**B5. `SLN` sanity check on a single asset.** A machine costs **500**, has a salvage value of **50**, and a useful life of **9 years**. Give the annual straight-line charge and the Excel formula.

`=SLN(500, 50, 9)` returns `(500 − 50) / 9 = 450 / 9 = ` **50.0** per year. Over 9 years that charges 9 × 50 = 450, leaving net book value 500 − 450 = **50**, exactly the salvage — the asset never depreciates below salvage, as it must not.

**B6. The liquidation trap (capex below depreciation).** A company opens 2025 with net PP&E of **1,000**, spends a flat **40** of capex each year, and depreciates at 10% of opening. Roll it forward three years and state what the trend reveals.

| Line | 2025 | 2026 | 2027 |
|---|---:|---:|---:|
| Opening | 1,000.0 | 940.0 | 886.0 |
| (+) Capex | 40.0 | 40.0 | 40.0 |
| (−) Depreciation | (100.0) | (94.0) | (88.6) |
| **Closing** | **940.0** | **886.0** | **837.4** |

Each year depreciation (100, 94, 88.6) exceeds capex (40), so net PP&E shrinks every period. Extended far enough it trends toward zero — the model is silently liquidating the asset base. Unless a wind-down is intended, capex is set too low.

**B7. From schedule to statement links.** Using B1's 2026 figures (capex 144.0, depreciation 57.0, closing net PP&E 657.0), state exactly which number each statement pulls and with what sign.

- Income statement: **depreciation 57.0** as an operating expense (reduces EBIT and pre-tax income).
- Cash flow — operations: **depreciation +57.0** as a non-cash add-back to net income.
- Cash flow — investing: **capex (144.0)** as an outflow (negative).
- Balance sheet: **net PP&E 657.0**, a direct link to the closing row.

Depreciation touches two statements (expense on the IS, add-back on the CFS); capex is the only real cash event; the balance sheet just reads the closing line.

---

## Section C — Interview-Style Questions (with model answers)

**C1. "Walk me through what happens to the three statements when capex increases by 100."**

On the **cash flow statement**, investing outflow rises by 100, so cash falls by 100 (ignoring the small extra depreciation for a moment). On the **balance sheet**, net PP&E rises by 100 and cash falls by 100 — an asset swap, so total assets and the balance are unchanged initially. Then depreciation on that new asset kicks in: say the first-year charge is 10. On the **income statement** depreciation rises 10, cutting pre-tax income by 10; at a 25% tax rate net income falls 7.5. On the **cash flow statement** that 10 of depreciation is added back and taxes fall by 2.5, so operating cash actually rises by 2.5 versus the no-capex case. On the **balance sheet** retained earnings fall 7.5 and net PP&E is 10 lower from depreciation, so both sides move together and it still balances. The clean headline: capex is an asset swap; its depreciation and tax shield are the only income and balance effects.

**C2. "Why is depreciation added back on the cash flow statement?"**

Because the cash flow statement starts from net income, and depreciation was subtracted to get net income even though it never used cash. To convert accounting profit back to cash you must undo every non-cash deduction — depreciation is the biggest. Adding it back doesn't mean depreciation "generates" cash; it means the cash never left in the first place. The actual cash event for those assets was capex, shown separately in investing.

**C3. "% of opening net PP&E versus a full straight-line waterfall — when do you use each?"**

The **% of opening** method is fast, stable, and self-adjusting: as the asset base grows, depreciation grows, and because it keys off the fixed opening balance there's no circularity. I use it for most operating models and quick forecasts. The **straight-line waterfall** gives each capex vintage its own life and diagonal-sums the layers — it's more faithful to how companies actually depreciate and how the note discloses it. I switch to it for valuation work, capital-intensive businesses, or whenever a reviewer will scrutinise the depreciation trend or asset lives. The trade-off is speed and simplicity against precision and auditability.

**C4. "Where does capex appear on the income statement?"**

It doesn't. Capex is an asset purchase, not an expense — it's capitalised on the balance sheet and only its *depreciation* ever hits the income statement, spread over the asset's life. Putting capex on the income statement double-counts the cost (once as capex, again as depreciation) and understates profit. This is the whole reason depreciation exists: to move the cost of a long-lived asset onto the income statement gradually rather than all at once.

**C5. "How do you know your PP&E schedule is right without checking every cell?"**

Three fast proofs. First, the **corkscrew ties**: every opening equals the prior closing — I can spot-check one and trust the chain because it's a copied formula. Second, **capex versus depreciation is sensible**: growing business, capex above depreciation; declining, below. Third and most important, the **balance sheet balances**: because the schedule feeds capex and depreciation into the cash flow and income statements and the closing line into the balance sheet, if any link is wrong or mis-signed the balance check goes non-zero immediately. A live balance check is a continuously evaluated proof that the whole schedule wired up correctly.

---

## Section D — Common-Error Spotting (what is wrong?)

**D1. Sign error in the roll-forward.**
```
Closing = SUM(Opening, Capex, Depreciation)   ' Depreciation stored as +50
```
**Wrong:** depreciation is stored positive, so `SUM` *adds* it and net PP&E balloons instead of falling. Fix: store depreciation as a negative (`=-50` or `=-rate*opening`) so the `SUM` is a literal roll-forward, or use `Opening + Capex − Depreciation` explicitly. The whole point of the negative-storage convention is that the arithmetic can't be misread.

**D2. Hard-keyed opening balance.**
```
D6 (2026 opening): 570   ' typed as a value
```
**Wrong:** the opening is a typed constant, not `=C10` (the 2025 closing). The corkscrew is broken — 2026 ignores everything that happened in 2025, and changing the 2025 capex assumption won't move 2026 onward. Fix: every opening after the first must be `=prior year's closing cell`. Only the first year's opening (last historical net PP&E) is a value/link.

**D3. Depreciation keyed off the closing balance.**
```
Depreciation 2025 = 10% * Closing_2025
Closing_2025 = Opening + Capex - Depreciation
```
**Wrong:** closing depends on depreciation, which now depends on closing — a genuine circular reference, and Excel throws an error (or a wrong iterative value). Fix: key depreciation off the *opening* balance (or a fixed gross base): `=10% * Opening_2025`. Opening is already fixed from last year, so the chain stays one-directional.

**D4. Capex deducted on the income statement.**
```
Income statement:  ... − Depreciation − Capex = Operating profit
```
**Wrong:** capex is not an expense; it's an asset purchase and never appears on the income statement. Deducting it double-counts (capex here, plus its depreciation) and understates profit. Fix: remove capex from the income statement entirely — it belongs in investing on the cash flow statement, and only its depreciation flows to the income statement.

**D5. Depreciation on the income statement but no add-back on the cash flow.**
```
Income statement:  Depreciation −57   ' linked
Cash flow (operations):  (no depreciation add-back)
```
**Wrong:** depreciation was subtracted to get net income but is a non-cash charge, so it must be added back in operating cash flow. Omitting the add-back understates operating cash by 57, cash is wrong, and the balance sheet won't balance. Fix: add depreciation back in cash flow from operations — it touches *two* statements, not one.

**D6. Capex shown as a positive in investing.**
```
Cash flow (investing):  Capex  +144
```
**Wrong:** capex is a cash *outflow*; shown positive it inflates cash by 288 versus reality (a 144 error doubled by the sign flip). Fix: capex is negative in investing (`=-144` or a link to a schedule row stored negative). Money spent on assets leaves the business.

**D7. Two separate depreciation calculations.**
```
Income statement depreciation:  = 10% * Opening        ' one formula
Schedule depreciation:          = SLN(base, 0, 10)     ' a different formula
```
**Wrong:** depreciation is computed twice by two different methods, so the IS figure and the schedule figure drift apart — the balance sheet stops balancing the moment they disagree. Fix: compute depreciation *once* in the schedule and link the income statement (and cash flow add-back) to that single cell.

**D8. Inconsistent capex-timing convention.**
```
2025 depreciation = 10% * Opening                    ' no current-year capex
2026 depreciation = 10% * (Opening + Capex)          ' full-year on new capex
```
**Wrong:** the convention changes between years, so the depreciation trend jumps for a reason unrelated to the business. Fix: pick one convention — no current-year, full-year, or the half-year middle ground `10% * (Opening + 0.5 * Capex)` — and apply it every forecast year, noting it in the assumptions block.
