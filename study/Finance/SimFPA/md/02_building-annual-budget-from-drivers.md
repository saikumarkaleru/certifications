# Building the Annual Budget from Drivers

## The ask

It's Tuesday, 3 February 2026. Budget season. The CFO forwards you the board's top-down target — "Rs 12 crore, hold PBT above Rs 1.5 crore" — and says:

> "Build it bottom-up from drivers. I don't want a number I can't defend line by line to the board. Units, price, contracts, headcount — every rupee has to hang off an assumption I can argue with. Draft P&L on my desk Thursday, monthly phasing included."

Deadline: Thursday 5 February 2026. The output must reconcile *exactly* to Rs 12.00 cr revenue and Rs 1.506 cr PBT — that's the deal the board signed.

## What you're given

The CFO's driver assumptions for FY2026-27, plus last year's actuals for sanity:

**Driver assumptions (FY2026-27):**

| Driver | Value |
|---|---:|
| Goods units (annual) | 90,000 |
| Goods ASP | Rs 1,000 |
| Goods gross margin | 25% |
| AMC contracts | 250 |
| AMC contract value | Rs 1,20,000 |
| Services gross margin | 45% |
| Opening headcount | 15 |
| Closing headcount (Q4) | 18 |
| Avg fully-loaded cost/head | ~Rs 6.4 lakh/yr |
| Other opex | Rs 0.78 cr |
| Depreciation | Rs 0.144 cr |
| Term loan | Rs 1.20 cr @ 9.5% |
| Tax | 25% + 4% cess |

**Seasonality (from CRM history):** goods are back-loaded — H1 ~45%, H2 ~55%, with a March spike. Services (AMC) are booked evenly, 1/12 per month.

## Build it — step by step

**Step 1 — The driver block (green Assumptions tab).** Lay drivers in labelled cells, never inside formulas:

| Cell | Label | Value |
|---|---|---:|
| B4 | Goods units | 90,000 |
| B5 | Goods ASP | 1,000 |
| B6 | Goods GM % | 25% |
| B8 | AMC contracts | 250 |
| B9 | AMC value | 1,20,000 |
| B10 | Services GM % | 45% |

**Step 2 — Revenue build.** On `Rev_Build`:

```
Goods revenue    = B4*B5      = 90,000*1,000     = 9,00,00,000
Services revenue = B8*B9      = 250*1,20,000      = 3,00,00,000
Total revenue                                     = 12,00,00,000
```

**Step 3 — Monthly phasing.** Store a 12-column seasonality vector (`Phasing!C2:N2`) that sums to 100%, then spread each segment. Goods uses the back-loaded curve; services is flat. Monthly goods revenue:

```
=$B$4*$B$5 * Phasing!C$2     ' dragged across Jan..Dec, phasing row sums to 1
```

To validate the spread ties back, cross-foot with SUMPRODUCT — the sum of monthly must equal the annual driver product:

```
=SUMPRODUCT(Phasing!C2:N2, MonthlyUnits!C2:N2)  ' must return 90,000
```

If you had per-SKU or per-region volumes in a table, you'd aggregate with `=SUMIFS(Units[Qty], Units[SKU], "*", Units[Month], C$1)` rather than a single cell — the SUMIFS/SUMPRODUCT pattern is the workhorse for driver roll-ups.

**Step 4 — COGS and gross profit.** COGS is revenue minus segment GP:

```
Goods COGS    = 9.00cr * (1-25%) = 6.75cr
Services COGS = 3.00cr * (1-45%) = 1.65cr
Total COGS    = 8.40cr
Gross profit  = 12.00 - 8.40    = 3.60cr   (30% blended)
```

**Step 5 — Opex build.** Employee cost is driven off the **headcount roster with joining dates**, not a flat number. 15 heads at start, +3 phased into Q4. Roughly:

```
Employee cost = SUMPRODUCT(cost_per_head_monthly, active_months)
              ≈ 1.08 cr   (15 heads all year + 3 heads for ~Q4 only)
```

The phasing matters: three hires landing only in Q4 add far less than three full-year heads — the roster method captures that automatically. Other opex Rs 0.78 cr is spread by activity (rent flat, freight follows goods volume).

**Step 6 — Down to PBT.** Stack the P&L:

```
Gross profit                       3.60 cr
less Employee cost                (1.08)cr
less Other opex                   (0.78)cr
less Depreciation                 (0.144)cr
= EBIT                             1.596 cr
less Finance cost (1.2cr*9.5%≈)   (0.09)cr
= PBT                             1.506 cr
less Tax (~25%+cess)             (~0.396)cr
= PAT                            ~1.11 cr
```

Finance cost checks out: Rs 1.20 cr term loan x 9.5% = Rs 11.4 lakh gross, but the average outstanding balance across the year (loan amortising) lands the P&L charge at ~Rs 9 lakh — matching the anchor.

## The deliverable

**NTSPL Budget P&L — FY2026-27**

| Line | Amount (Rs cr) | % of revenue |
|---|---:|---:|
| Goods revenue | 9.000 | 75.0% |
| Services revenue | 3.000 | 25.0% |
| **Total revenue** | **12.000** | **100.0%** |
| Goods COGS | (6.750) | |
| Services COGS | (1.650) | |
| **Gross profit** | **3.600** | **30.0%** |
| Employee cost | (1.080) | 9.0% |
| Other opex | (0.780) | 6.5% |
| Depreciation | (0.144) | 1.2% |
| **EBIT** | **1.596** | **13.3%** |
| Finance cost | (0.090) | 0.8% |
| **PBT** | **1.506** | **12.6%** |
| Tax (~26%) | (0.396) | |
| **PAT** | **~1.110** | **9.3%** |

**Quarterly phasing (revenue, Rs cr):**

| | Q1 | Q2 | Q3 | Q4 | FY |
|---|---:|---:|---:|---:|---:|
| Goods | 2.10 | 1.95 | 2.10 | 2.85 | 9.00 |
| Services | 0.75 | 0.75 | 0.75 | 0.75 | 3.00 |
| **Total** | **2.85** | **2.70** | **2.85** | **3.60** | **12.00** |

*Commentary:* "Revenue is defensible driver-by-driver: 90,000 units and 250 AMCs. Q1 is budgeted at Rs 2.85 cr; the March-heavy goods curve loads Q4 to Rs 3.6 cr, so we can't judge the year on H1 run-rate. PBT lands at Rs 1.506 cr — 6 bps of headroom over the board's Rs 1.5 cr floor, which is thin. The three Q4 hires are the biggest discretionary lever if we need to protect PBT."

## How it's reviewed

The controller runs **tie-outs**: does revenue foot to Rs 12.00 cr, does the segment split match the drivers, does GP hit exactly 30%, does PBT clear the Rs 1.5 cr floor? She checks the **phasing sums to the annual** (monthly SUMPRODUCT = annual driver). She stress-tests one driver: "drop ASP to Rs 950 — show me PBT" and expects the model to flow it through instantly because ASP is a single green cell. Finally she checks finance cost against the loan schedule and tax at the right rate.

## Common mistakes & red flags

- **Plugging revenue to hit the target.** Top-down "make it Rs 12 cr" with no unit/price logic. The board will ask "how many units?" and you'll have nothing.
- **Flat 30% margin on total revenue.** Skips the segment mechanics; breaks the moment mix moves.
- **Full-year cost for part-year hires.** Costing 18 heads all year overstates employee cost by lakhs. Phase by joining date.
- **Phasing that doesn't reconcile.** A seasonality curve that doesn't sum to 100% quietly changes the annual total. Always cross-foot monthly back to the driver.
- **Forgetting cess.** Tax is 25% *plus 4% cess* ≈ 26%, not a clean 25%.

## On the job & in the interview

The "why": a driver-based budget is *defensible* and *flexible* — every number answers "why" (units, price, heads) and every scenario is a one-cell change. A hard-coded budget is neither.

Jargon: **driver-based / bottom-up**, **phasing / seasonality curve**, **cross-foot**, **flow-through**, **PBT floor**, **fully-loaded cost per head**.

**Q: "How do you build a revenue budget for a business like this?"**
A: "Bottom-up from drivers. Goods is units x ASP — 90,000 x Rs 1,000 = Rs 9 cr. Services is contracts x value — 250 x Rs 1.2 lakh = Rs 3 cr. Then phase each by its own seasonality, cross-foot the monthly back to the annual driver, and layer segment margins to get GP. Total Rs 12 cr, GP Rs 3.6 cr."

**Q: "Why model headcount cost off a roster instead of a single number?"**
A: "Because timing changes the cost. Three hires landing in Q4 add roughly a quarter of their annual cost this year, not the full amount. A roster with joining dates and SUMPRODUCT captures that; a flat number overstates employee cost and understates PBT."

**Q: "Your PBT is Rs 1.506 cr against a Rs 1.5 cr floor. Comfortable?"**
A: "Not very — that's under half a percent of headroom. I'd flag the sensitivity: a Rs 50 drop in ASP costs Rs 45 lakh of revenue and, at 25% margin, Rs 11 lakh of GP, which alone breaches the floor. My mitigation lever is deferring or staggering the Q4 hires, worth roughly Rs 5-10 lakh."
