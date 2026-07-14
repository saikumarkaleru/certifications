# Your First Week in FP&A: The Business, the Model, and the Data

## The ask

It's Monday, 6 April 2026. You've just joined Nirvana Traders & Services Pvt Ltd ("NTSPL"), Hyderabad, as the FP&A Analyst reporting to the CFO, Mrs. Rao. Ten minutes into your first 1:1 she says:

> "Before you touch a single formula, I need you to *understand the business*. By Friday I want a one-page map — how we make money, where the numbers live, and a walkthrough of the budget model you're inheriting. If you can't explain our revenue on the back of an envelope, you can't forecast it."

Deadline: Friday 10 April 2026, 5 pm. No new model. Just: learn the machine before you drive it.

## What you're given

A shared drive folder (`\\ntspl-fs01\Finance\FY27`), read access to Tally Prime, and a login to the sales CRM. The CFO drops three artifacts on your desk.

**1. The FY2026-27 approved budget (one-line summary the board signed off):**

| Line | FY2026-27 Budget |
|---|---:|
| Revenue | Rs 12.00 cr |
| — Goods | Rs 9.00 cr |
| — Services (AMC/install) | Rs 3.00 cr |
| COGS | Rs 8.40 cr |
| Gross profit (30%) | Rs 3.60 cr |
| Employee cost | Rs 1.08 cr |
| Other opex | Rs 0.78 cr |
| Depreciation | Rs 0.144 cr |
| EBIT | Rs 1.596 cr |
| Finance cost | Rs 0.09 cr |
| PBT | Rs 1.506 cr |
| PAT (~25%+cess) | ~Rs 1.11 cr |

**2. The revenue drivers behind those two lines:**

| Segment | Driver | Volume | Rate | Revenue |
|---|---|---:|---:|---:|
| Goods | units x ASP | 90,000 units | Rs 1,000 | Rs 9.00 cr |
| Services | AMC contracts x price | 250 contracts | Rs 1,20,000 | Rs 3.00 cr |

**3. Where the data lives (the CFO's scribbled system map):**

| System | Owner | Holds | Refresh |
|---|---|---|---|
| Tally Prime (ERP) | Accounts (Suresh) | GL, actual P&L, AP/AR, inventory | Daily; locked at month close |
| Sales CRM | Sales head (Kiran) | Orders, units, ASP, AMC pipeline | Live |
| HR sheet (Excel) | Admin (Latha) | Headcount, CTC, joining dates | Monthly |
| Bank portal | CFO | Cash, term-loan balance | Daily |

## Build it — step by step

Your Friday deliverable is understanding, not a model — but the way you *acquire* that understanding is by reverse-engineering the inherited Excel file, `NTSPL_Budget_FY27.xlsx`.

**Step 1 — Map the money.** Two revenue engines. Goods is a **volume x price** business: 90,000 units x Rs 1,000. Services is a **contract count x annual value** business: 250 AMC x Rs 1,20,000. Memorise the identity:

```
Revenue = (Goods units x ASP) + (AMC contracts x contract value)
        = (90,000 x 1,000) + (250 x 1,20,000)
        = 9,00,00,000 + 3,00,00,000 = 12,00,00,000  (Rs 12.00 cr)
```

**Step 2 — Learn the margin shape.** Goods carry 25% gross margin, services 45%. Blended it lands at 30% only *because of the mix* (75% goods / 25% services). Prove it:

```
GP = 9.00cr x 25% + 3.00cr x 45% = 2.25cr + 1.35cr = 3.60cr  -> 30% of 12.00cr
```

Write that down — the day the mix shifts, the "30%" moves even if nothing else changes. This is the single most misunderstood number in the company.

**Step 3 — Open the model and label every tab.** A clean FP&A workbook follows the **inputs → calcs → outputs** discipline. You colour-code the tabs:

| Tab (colour) | Type | What's on it |
|---|---|---|
| `Assumptions` (green) | Input | Drivers: units, ASP, contracts, margins %, headcount plan, tax rate. The *only* place you type numbers. |
| `Rev_Build` (grey) | Calc | Revenue by segment, by month, from Assumptions |
| `Opex_Build` (grey) | Calc | Employee cost from HR roster; other opex |
| `P&L` (blue) | Output | Monthly + annual P&L, budget column |
| `Actuals` (grey) | Calc | Tally GL dump, mapped to P&L lines |
| `Variance` (blue) | Output | Budget vs actual bridge |
| `Dashboard` (blue) | Output | KPI tiles + charts |

The golden rule you confirm holds: **no hard-coded numbers inside calc or output tabs — every figure traces back to a green Assumptions cell.** You test one: click the goods-revenue cell on `Rev_Build` and it reads `=Assumptions!B4*Assumptions!B5`, not `=9000000`. Good — the model is a machine, not a picture of a machine.

**Step 4 — Trace one number end to end.** You pick employee cost. `Opex_Build` sums the HR roster with `=SUMPRODUCT(CTC_range, active_flag)` and phases it monthly; the annual total feeds `P&L!EmployeeCost` which reconciles to the Rs 1.08 cr budget line. You now know the *path*, so when it breaks you'll know where to look.

**Step 5 — Fix the KPI set.** From the CFO's board deck you extract the six numbers she actually reports:

| KPI | Definition | FY27 budget anchor |
|---|---|---:|
| Revenue | Goods + services | Rs 12.00 cr |
| Gross margin % | GP / revenue | 30% |
| EBITDA | EBIT + depreciation | Rs 1.74 cr |
| DSO | Debtors / revenue x 365 | 60 days |
| Headcount | Active employees | 15 → 18 by Q4 |
| Cash balance | Bank + cash | Rs 35 lakh (opening) |

## The deliverable

You produce a **one-page Business & Data Map** and a two-minute model walkthrough. The one-pager:

**NTSPL on one page (FY2026-27)**
- **Who we are:** Hyderabad trader of industrial electrical components (goods) plus installation & AMC (services).
- **How we make money:** Goods = 90,000 units x Rs 1,000 = Rs 9.0 cr (25% GM). Services = 250 AMC x Rs 1.2 lakh = Rs 3.0 cr (45% GM). Total Rs 12.0 cr, blended GM 30%.
- **What flows to the bottom:** GP 3.60 cr → less opex 1.86 cr, depreciation 0.144 cr → EBIT 1.596 cr → less finance cost 0.09 cr → PBT 1.506 cr → PAT ~1.11 cr.
- **Where the data lives:** Actuals in Tally (locked at close); drivers in CRM; people in the HR sheet; cash on the bank portal.
- **The model:** one workbook, Assumptions → builds → P&L/Variance/Dashboard. Green = type here, everything else is formulas.

*Commentary (analyst voice):* "NTSPL is a two-engine business. Goods drives scale and cash-cycle risk; services drives margin. The blended 30% is a mix artefact, not a floor — my forecasts have to model the two engines separately or the margin will lie to us."

## How it's reviewed

The CFO checks three things. **One — can you explain revenue without opening Excel?** She'll ask "what's our goods revenue and why" and expect "90,000 units at a thousand rupees, nine crore." **Two — do you understand the margin mechanics**, i.e. that 30% is mix-driven, not a constant. **Three — do you know where each number is born**, so month-end doesn't become an archaeology dig. She'll spot-check by asking "where does employee cost come from?" and expect "HR roster, SUMPRODUCT of CTC times active flag, on Opex_Build."

## Common mistakes & red flags

- **Treating the model as a picture.** Hard-coding a number into an output tab breaks the machine silently. Every output cell must trace to green.
- **Averaging the margin.** Saying "our margin is 30%" and applying it to any revenue mix. Goods and services must be modelled separately.
- **Not knowing the data lineage.** If you can't name the source system for a P&L line, you can't defend the number when it moves.
- **Confusing EBIT and EBITDA.** EBIT is 1.596 cr; add back depreciation 0.144 cr for EBITDA 1.74 cr. Interviewers love this trip-wire.
- **Ignoring the cash cycle on day one.** A goods-heavy trader lives and dies by DSO/DIO/DPO; note it early even if you're not modelling it yet.

## On the job & in the interview

The "why": FP&A exists to connect *drivers* (units, contracts, people) to *outcomes* (P&L, cash) so the business can steer, not just report. Your first-week job is to internalise the drivers so every later forecast is a lever pull, not a guess.

Jargon to own: **driver-based**, **inputs/calcs/outputs**, **single source of truth**, **data lineage**, **mix effect**, **tie-out**.

**Q: "Walk me through NTSPL's business model in 60 seconds."**
A: "Two engines. Goods — 90,000 units at Rs 1,000 ASP, Rs 9 cr, 25% gross margin — is a volume-and-price trading business with a working-capital tail. Services — 250 AMC contracts at Rs 1.2 lakh, Rs 3 cr, 45% margin — is recurring and high-margin. Blended revenue Rs 12 cr, gross margin 30%, EBIT Rs 1.6 cr, PBT Rs 1.5 cr. The strategic lever is shifting mix toward services to lift blended margin."

**Q: "Why is the blended gross margin 30% and not the average of 25% and 45% (35%)?"**
A: "Because it's revenue-weighted, and goods is three-quarters of revenue. 0.75x25% + 0.25x45% = 30%. If services grew to half the mix, blended margin would rise to 35% with no change in either segment's margin — that's why I forecast the segments separately."

**Q: "What would you check in an inherited model first?"**
A: "Structure and lineage. I confirm inputs/calcs/outputs separation, that outputs contain no hard-codes, and I trace one number — say employee cost — from the HR roster through the build to the P&L line and reconcile it to the Rs 1.08 cr budget. If that path is clean, I trust the machine."
