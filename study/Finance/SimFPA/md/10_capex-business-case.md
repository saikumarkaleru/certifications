# A Capex Business Case

## The ask

It's **10 August 2026**. The COO wants to buy a **warehouse-automation system** — conveyors, barcode scanning, a small WMS integration — to speed up despatch and cut manual handling. Quoted cost **Rs 40 lakh**, inside the FY2026-27 Rs 40 lakh capex budget. He claims it saves **Rs 12 lakh a year** in labour, error and rework over a **6-year** life, with a **Rs 4 lakh** salvage at the end.

The CFO drops it on your desk: *"Before this goes to the board on the 20th, run the appraisal. Payback, NPV, IRR at our 12% hurdle, and a sensitivity. One page, with a go/no-go and the risks. Don't just trust the Rs 12 lakh — tell me what happens if it's wrong."*

## What you're given

| Input (FY2026-27) | Value |
|---|---|
| Initial outlay (Year 0) | Rs 40,00,000 |
| Annual saving (pre-tax cash) | Rs 12,00,000 |
| Life | 6 years |
| Salvage (end of Year 6) | Rs 4,00,000 |
| Discount rate (WACC) | 12% |

For this appraisal the CFO says to keep it on a **pre-tax cash basis** (the board sees pre-tax project economics; tax shields are a second-order refinement noted separately). Cash flows are treated as arising at year-end.

## Build it — step by step

**Step 1 — lay out the cash-flow schedule.** In Excel, one column per year, Year 0 negative:

| Year | Cash flow | Formula |
|---|---|---|
| 0 | −40,00,000 | outlay |
| 1 | 12,00,000 | saving |
| 2 | 12,00,000 | saving |
| 3 | 12,00,000 | saving |
| 4 | 12,00,000 | saving |
| 5 | 12,00,000 | saving |
| 6 | 16,00,000 | 12,00,000 saving + 4,00,000 salvage |

**Step 2 — payback (simple).** Cumulative cash recovers the Rs 40 lakh outlay:

```
End Y1: -28,00,000   End Y2: -16,00,000   End Y3: -4,00,000   End Y4: +8,00,000
Payback = 3 + 4,00,000/12,00,000 = 3.33 years  (~3 yrs 4 months)
```

**Step 3 — discounted payback.** Discount each year at 12% (factor = 1/1.12^n), then re-cumulate:

| Year | CF | DF @12% | PV | Cum PV |
|---|---|---|---|---|
| 1 | 12,00,000 | 0.8929 | 10,71,429 | −29,28,571 |
| 2 | 12,00,000 | 0.7972 | 9,56,633 | −19,71,939 |
| 3 | 12,00,000 | 0.7118 | 8,54,136 | −11,17,802 |
| 4 | 12,00,000 | 0.6355 | 7,62,621 | −3,55,182 |
| 5 | 12,00,000 | 0.5674 | 6,80,912 | +3,25,730 |
| 6 | 16,00,000 | 0.5066 | 8,10,634 | +11,36,364 |

Discounted payback = 4 + 3,55,182/6,80,912 = **4.52 years** (~4 yrs 6 months).

**Step 4 — NPV.** Sum of PVs of Years 1–6 less the outlay. In Excel:

```
=NPV(12%, 12L,12L,12L,12L,12L,16L) - 40L
```

Sum of PV inflows = 10,71,429 + 9,56,633 + 8,54,136 + 7,62,621 + 6,80,912 + 8,10,634 = **Rs 51,36,364**.

```
NPV = 51,36,364 - 40,00,000 = Rs 11,36,364  (positive)
```

**Step 5 — IRR.** The rate where NPV = 0. In Excel, list CFs Year 0–6 and `=IRR(range)`. Solving:

```
At 12%: NPV = +11.36L ;  At 25%: NPV = -1.7L (approx)
IRR ≈ 23.4%
```

Well above the 12% hurdle. `=IRR({-40L,12L,12L,12L,12L,12L,16L})` returns **~23.4%**.

**Step 6 — sensitivity.** The soft number is the Rs 12 lakh saving, so I flex it and the discount rate. NPV (Rs lakh):

| Annual saving → | Rs 9 L | Rs 12 L | Rs 15 L |
|---|---|---|---|
| **Discount 10%** | +2.6 | +16.2 | +29.8 |
| **Discount 12%** | −1.2 | +11.4 | +23.9 |
| **Discount 14%** | −4.6 | +7.0 | +18.7 |

Break-even saving (NPV = 0 at 12%): the project needs roughly **Rs 9.7 lakh/yr** to clear the hurdle — a ~19% cushion below the Rs 12 lakh claim. Below that, or if the saving falls to Rs 9 L, the case turns negative.

## The deliverable

**CAPEX MEMO — Warehouse Automation System**
**To:** CFO / Board · **From:** FP&A · **Date:** 12 August 2026

**Recommendation: GO.** The Rs 40 lakh warehouse-automation investment clears every test at the 12% hurdle.

| Metric | Result | Hurdle | Verdict |
|---|---|---|---|
| NPV @12% | **+Rs 11.36 lakh** | > 0 | Pass |
| IRR | **~23.4%** | > 12% | Pass |
| Simple payback | 3.33 yrs | < 4 yrs | Pass |
| Discounted payback | 4.52 yrs | < 6-yr life | Pass |
| Break-even saving | ~Rs 9.7 L/yr | vs Rs 12 L claimed | 19% cushion |

*Commentary: The project returns 23.4% against our 12% cost of capital and adds Rs 11.4 lakh of value in today's money. It recovers cash in about 3 years 4 months (4.5 on a discounted basis, comfortably inside the 6-year life). The economics only turn negative if annual savings fall below ~Rs 9.7 lakh — a 19% shortfall — so there is a reasonable buffer against optimism in the labour-saving estimate.*

**Risks & mitigants:**
- **Savings realisation** — Rs 12 L assumes headcount is genuinely redeployed/not backfilled. Mitigant: tie sign-off to a post-implementation labour-cost review at Year 1.
- **Implementation slip** — WMS integration with Tally could overrun; delayed go-live pushes Year-1 saving out and cuts NPV. Mitigant: fixed-price vendor SOW, hold 10% retention.
- **Volume dependency** — savings scale with despatch volume; a demand downturn (see Q1 volume miss) shrinks the benefit. Mitigant: the ~19% break-even cushion absorbs moderate slippage.
- **Salvage uncertainty** — Rs 4 L in Year 6 is small (PV ~Rs 2 L); immaterial to the decision.

**Ask:** approve Rs 40 lakh capex; release against a fixed-price SOW with a Year-1 savings audit.

## How it's reviewed

The CFO checks: (1) **sign convention** — outlay negative in Year 0, and NPV subtracts the outlay (a classic `=NPV()` error is including Year 0 *inside* the function, which wrongly discounts it one period). (2) **Salvage in the right year** — Rs 4 L sits in Year 6, added to that year's saving. (3) **IRR sanity** — 23.4% vs 12% hurdle, and that IRR and NPV agree in direction (both say go). (4) **Sensitivity honesty** — did you flex the *right* driver (the saving), and show the break-even? (5) **Hurdle rate** — 12% WACC, consistent with the appraisals elsewhere in the plan. (6) Payback used as a liquidity check, not the decision — NPV rules.

## Common mistakes & red flags

- **Including Year 0 inside `=NPV()`** — Excel's NPV assumes the first value is one period out. Correct form: `=NPV(rate, Y1:Y6) + Year0` (with Year 0 negative), or subtract the outlay outside.
- **Forgetting salvage** or putting it in the wrong period.
- **Using payback to decide** — payback ignores time value and everything after the payback year; it's a screen, not the verdict.
- **No sensitivity** — a single-point NPV hides that the case rests on an unaudited Rs 12 L claim. Always show break-even.
- **Double-counting depreciation as a cash outflow** — on a pre-tax cash basis depreciation is non-cash; the Rs 40 L is captured once, at Year 0. (If you build the after-tax version, depreciation re-enters only as a *tax shield*.)
- **Mismatched rate** — appraising at cost of debt (9.5%) instead of WACC (12%) flatters the NPV.

## On the job & in the interview

Capex appraisal is where FP&A protects the balance sheet. The board wants three things: does it create value (**NPV > 0**), does it beat our cost of capital (**IRR > WACC**), and how fast do we get our cash back (**payback**). NPV is the decision metric because it's in rupees and additive; IRR is the intuitive rate; payback is the liquidity comfort. The real skill is **sensitivity** — pressure-testing the one soft assumption.

**Q: "NPV says Rs 11 lakh, IRR says 23%. Which do you trust and why?"**
*A: NPV for the decision — it's an absolute rupee value of wealth created and it's additive across projects. IRR is a useful communication number (23% vs a 12% cost of capital), but it can mislead with non-conventional cash flows or when comparing projects of different scale. Here they agree, so it's an easy go; when they conflict, I follow NPV.*

**Q: "The COO's Rs 12 lakh saving — how do you protect the company if he's optimistic?"**
*A: I ran the break-even: the project still clears 12% down to about Rs 9.7 lakh a year, a 19% cushion. Below that it destroys value. So I'd recommend approval but tie the release to a fixed-price SOW and a Year-1 labour-cost audit — if the redeployment doesn't happen, we catch it before Year 2 and the salvage/exit is cheap.*

**Q: "Why 12% and not our 9.5% loan rate?"**
*A: We fund with a mix of debt and equity; equity holders demand more than 9.5%. The blended WACC (~12%) is the true opportunity cost of the capital tied up, so it's the right hurdle. Discounting at the debt rate alone would overstate NPV and wave through projects that don't actually cover the cost of the equity funding them.*
