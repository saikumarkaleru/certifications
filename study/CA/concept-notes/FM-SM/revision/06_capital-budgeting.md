# Capital Budgeting (Investment Decisions)

## Snapshot
Deciding which long-term assets to buy. Inputs = incremental, after-tax, cash flows (not profit). Yardstick = NPV (wealth in ₹). Decision categories dictate the technique:
- **Accept–reject (independent):** accept every NPV > 0 (⇔ IRR > k ⇔ PI > 1). NPV & IRR never conflict.
- **Mutually exclusive:** pick one; NPV vs IRR can disagree (scale/timing).
- **Capital rationing:** budget capped; select combination maximising total NPV (PI's home).
- **Replacement / abandonment:** incremental analysis; economic life may be < physical life.

Examiner signals the box in the first 2 lines ("only one of…" = mutually exclusive; "funds limited to ₹X" = rationing).

## Core concepts
- **Cash not profit; incremental not total; after-tax; post opportunity cost.** Goal = maximise shareholder wealth.
- **k = cost of capital (WACC)** = opportunity cost = reinvestment assumption. NPV reinvests interim flows at k (neutral, defensible); IRR reinvests at IRR (often unrealistic) — the deep reason NPV beats IRR.
- **Five cash-flow rules:** (1) incremental (with-minus-without); (2) ignore sunk costs; (3) include opportunity costs; (4) include working capital (out at start/on rise, recovered at end, untaxed, not depreciated); (5) ignore financing flows (interest/dividend) in the cash line — they live in k (else double-count).
- **Depreciation:** non-cash; enters only via tax. Add back after computing tax.
- **Cannibalisation/erosion:** lost contribution on old product = incremental outflow. Complementary lift = inflow.

## Key provisions / rules

**After-tax operating cash flow build-up**
| Line | Item |
|---|---|
| PBDT | Sales − cash operating costs |
| PBT | PBDT − Depreciation |
| Tax | PBT × t |
| PAT | PBT − Tax |
| CF | PAT + Depreciation |

| Item | Formula |
|---|---|
| After-tax operating CF | PBDT × (1 − t) + Depreciation × t |
| Depreciation tax shield | Depreciation × t |
| SLM depreciation | (Cost − Salvage) ÷ Life |
| WDV depreciation | Rate × opening WDV each year (front-loaded shields → higher PV) |
| Initial outlay | Asset + Installation + Initial WC + Opportunity cost |
| Terminal inflow | Salvage (net of tax) + WC recovered |

**Tax on salvage (4 cases)**
| Case | Treatment |
|---|---|
| Salvage = book value | No tax; salvage enters gross |
| Salvage > book value | Profit = Salvage − BV; net salvage = Salvage − t×(Salvage − BV) |
| Salvage < book value | Loss saves tax; net salvage = Salvage + t×(BV − Salvage) |
| Salvage = 0, BV > 0 | Terminal loss = BV; tax saving = BV × t |

**Techniques**
| Technique | Formula | Rule | Time value |
|---|---|---|---|
| Payback (even) | Initial Investment ÷ Annual CF | ≤ target | No |
| Payback (uneven) | Completed yrs + (Unrecovered ÷ next-yr CF) | ≤ target | No |
| Discounted Payback | Accumulate PV of CFs till outlay recovered | ≤ target | Yes |
| ARR | Avg Annual PAT ÷ Avg Investment × 100 | ≥ target | No |
| NPV | Σ CFₜ ÷ (1+k)ᵗ − Investment | > 0; highest | Yes |
| IRR | Rate where NPV = 0 | > k | Yes |
| MIRR | (Terminal Value of inflows ÷ PV of outflows)^(1/n) − 1 | > k | Yes |
| PI | PV of inflows ÷ Investment = 1 + NPV/Investment | > 1 | Yes |
| EAC | Total PV of costs ÷ PVIFA(k, life) | Lowest EAC wins | Yes |

- **Avg Investment (ARR)** = (Cost − Salvage) ÷ 2 + Salvage + Additional WC. (Salvage & WC at full value; depreciable part halved.) ICAI default = average investment (state basis).
- **IRR interpolation:** IRR = L + [NPV_L ÷ (NPV_L − NPV_H)] × (H − L). Bracket L,H tightly (2–3% apart) around zero.
- **Payback reciprocal** (1 ÷ payback) ≈ IRR for long, even-cash-flow projects.
- **Discounted payback within life ⇒ NPV > 0** (sufficient condition).
- **PI for rationing:** valid only if projects divisible & single-period. Indivisible → test feasible combinations for max total NPV.

**Special decisions**
- **Replacement:** Year-0 = New cost − after-tax proceeds of old asset (add tax saving if sold below BV; deduct tax if above). Operating = incremental CF; **incremental depreciation = new dep − old dep forgone** (drives shield). Terminal = incremental salvage. (The two "old-asset-forgone" legs earn/lose marks.)
- **Unequal lives (mutually exclusive):** EAC (NPV ÷ PVIFA of own life; lowest cost / highest benefit wins) or replacement-chain over LCM of lives. EAC preferred.
- **Abandonment:** find optimal year — compare "value if abandoned now" vs "PV of (next year CF + next year salvage)".

**NPV vs IRR conflict** — only for mutually exclusive. Roots: **scale** and **timing** (reinvestment rate). Resolve: trust NPV. Confirm via **incremental IRR** = IRR of (Large − Small) CFs; if > k, bigger-NPV project wins. **Fisher crossover rate** = incremental IRR = rate where the two NPVs are equal. **Multiple/no IRR:** non-conventional flows (>1 sign change) → use NPV or MIRR.

## Worked mini-example
Plant ₹20,00,000 + WC ₹3,00,000 = ₹23,00,000 outlay. Life 4 yr, salvage ₹2,00,000, SLM, t = 30%, k = 12%.
- Depreciable base = 20,00,000 − 2,00,000 = 18,00,000; dep = ₹4,50,000/yr.
- Operating CFs (PBDT×0.70 + 4,50,000×0.30): Yr1 6,25,000; Yr2 7,65,000; Yr3 8,35,000; Yr4 6,60,000.
- Terminal Yr4: salvage 2,00,000 (= BV → no tax) + WC 3,00,000 = 5,00,000. Yr4 total = 11,60,000.
- PV @12%: 5,58,125 + 6,09,705 + 5,94,520 + 7,37,760 = 25,00,110.
- **NPV = 25,00,110 − 23,00,000 = ₹2,00,110 > 0 → Accept.**

Variation A: salvage ₹3,50,000 > BV 2,00,000 → profit 1,50,000, tax 45,000, net salvage 3,05,000 (depreciation schedule unchanged — still based on expected ₹2,00,000).

## Exam traps & must-remember
1. Deducting a **sunk cost** (past feasibility study) — ignore it.
2. Forgetting **opportunity cost** of owned land/building/old asset that could be sold.
3. **Subtracting interest** from cash flows — never; it's in k.
4. Treating **depreciation as cash outflow** — only tax effect is cash.
5. Omitting **WC recovery** in final year; or depreciating/taxing WC.
6. **Tax on salvage** only if salvage ≠ book value. Machine depreciated to nil but sold for scrap = taxable profit.
7. Using **PAT instead of CF** (forgetting add-back of depreciation).
8. Ranking mutually exclusive by **IRR/PI** (scale illusion) — NPV decides; confirm with incremental IRR.
9. **Multiple/no IRR** on non-conventional flows — use NPV/MIRR, don't interpolate blindly.
10. Mixing **nominal/real** — ICAI problems are nominal.
11. **ARR base** — average vs initial; default average, state it.
12. **Wrong depreciable base** — SLM on (Cost − Salvage), not Cost.
13. Comparing **unequal-life** projects on raw NPV — use EAC.
14. Replacement — dropping the **old-asset-forgone** legs (after-tax sale + incremental depreciation).
15. **Incremental WC** when WC = % of rising sales — outflow only the year-on-year increase; recover accumulated balance at end.
16. **Interpolating IRR** over too wide a bracket.
17. **Loss-year tax** = saving only if firm has other taxable profits; else deferred.
18. **WDV terminal balancing charge/allowance** almost always arises (BV ≠ salvage) — tax it.

## One-line recall
- Cash not profit; incremental not total; sunk gone, opportunity counts.
- Depreciation only for tax, then add it back; WC out at start, back at end, untaxed.
- Tax the salvage only if it differs from book value; SLM base = Cost − Salvage.
- NPV rules; when in doubt, ask "am I richer today?" IRR reinvests at IRR (flatters); NPV reinvests at k (honest).
- Unequal lives → annualise (EAC); replacement → incremental (incl. incremental depreciation).
- Rationing: divisible → rank PI; indivisible → best feasible combination by total NPV.
