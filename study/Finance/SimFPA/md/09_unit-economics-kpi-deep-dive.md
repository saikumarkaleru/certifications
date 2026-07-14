# Unit Economics & KPI Deep-Dive

## The ask

It's **20 July 2026**. The CFO forwards you an email chain with the Managing Director. The MD has been reading about "unit economics" and SaaS-style LTV/CAC metrics, and he wants to know, in his words: *"For every box we sell and every AMC we sign, what do we actually make — and how many do we need to sell before we stop losing money? Give me the per-unit picture and the two or three numbers I should watch every month."*

The CFO wants a one-pager by **Thursday 23 July**: goods contribution per unit, services contribution per contract, the company break-even, a customer-acquisition (CAC) vs lifetime-value (LTV) read on the AMC book, and a **KPI tree** that shows how these roll up to the Rs 12.00 cr revenue and Rs 1.11 cr PAT already in the FY2026-27 budget. Each KPI must name the action it drives — no vanity metrics.

## What you're given

The budget anchors, pulled from the approved FY2026-27 plan:

| Line | Goods | Services | Total |
|---|---|---|---|
| Revenue | 9.00 cr | 3.00 cr | 12.00 cr |
| Volume driver | 90,000 units | 250 AMC contracts | — |
| Unit price | ASP Rs 1,000 | Rs 1,20,000 / contract | — |
| Gross margin % | 25% | 45% | 30% |
| Gross profit | 2.25 cr | 1.35 cr | 3.60 cr |

Fixed cost base (below gross profit) from the budget:

| Fixed / period cost | FY2026-27 |
|---|---|
| Employee cost | Rs 1.08 cr |
| Other opex | Rs 0.78 cr |
| Depreciation | Rs 0.144 cr |
| Finance cost | Rs 0.09 cr |
| **Total fixed** | **Rs 2.094 cr** |

AMC book facts from the CRM (Tally + a HubSpot export): 250 live contracts, average tenure ~4 years (retention ~75%/yr, so churn ~25%), and the sales/marketing spend attributable to *winning new AMC customers* this year is about **Rs 18 lakh** for **~60 new logos**.

## Build it — step by step

**Step 1 — Goods contribution per unit.** ASP is Rs 1,000, gross margin 25%, so unit cost = Rs 750 and **contribution per unit = Rs 250** (this equals gross profit per unit because there's no separately variable selling cost per box). In Excel I lay it as a driver block:

```
ASP            =1000
GM%_goods      =0.25
Unit_cost      =ASP*(1-GM%_goods)      -> 750
Contrib_unit   =ASP-Unit_cost          -> 250
Contrib_margin =Contrib_unit/ASP       -> 25%
```

Total goods contribution = 90,000 × 250 = **Rs 2.25 cr** — ties to budget gross profit for goods.

**Step 2 — Services contribution per contract.** Price Rs 1,20,000, margin 45%, so variable delivery cost = Rs 66,000 and **contribution per contract = Rs 54,000**. Across 250 contracts = Rs 1.35 cr — ties out.

**Step 3 — Blended contribution & break-even.** The company sells a mix, so I compute a **weighted contribution margin**, not a simple average:

```
Blended CM% = Total contribution / Total revenue
            = 3.60 cr / 12.00 cr = 30%
```

Break-even revenue = Fixed cost ÷ blended CM%:

```
BE_revenue = 2.094 / 0.30 = Rs 6.98 cr
```

To express it in **goods-equivalent units** if the whole gap were closed with boxes, contribution needed above services = fixed cost less services contribution:

```
Fixed to cover by goods = 2.094 - 1.35 = 0.744 cr
BE goods units          = 74,40,000 / 250 = 29,760 units
```

So at the current AMC book, NTSPL breaks even at **~29,760 boxes/year** (~33% of the 90,000 plan) — a comfortable margin of safety.

**Margin of safety** = (12.00 − 6.98) / 12.00 = **41.8%**. Revenue can fall 41.8% before NTSPL hits break-even.

**Step 4 — CAC and LTV on the AMC book.**

```
CAC = New-AMC S&M spend / New logos = 18,00,000 / 60 = Rs 30,000 per customer
Annual contribution/contract        = Rs 54,000
Avg lifetime (yrs) = 1/churn = 1/0.25 = 4 years
LTV (undiscounted)  = 54,000 x 4      = Rs 2,16,000
LTV:CAC             = 2,16,000 / 30,000 = 7.2x
CAC payback (months)= 30,000 / (54,000/12) = 6.7 months
```

A LTV:CAC of **7.2x** and a **~7-month** payback is healthy (the rule of thumb is LTV:CAC ≥ 3x and payback < 12 months). If anything it signals NTSPL is *under-investing* in AMC acquisition — there's room to spend more to win logos.

**Step 5 — the KPI tree.** I model revenue as `Volume × Price × Margin`, so each leaf is an operational lever a manager can move.

## The deliverable

**Unit economics summary — FY2026-27**

| Metric | Goods | Services |
|---|---|---|
| Price (ASP) | Rs 1,000/unit | Rs 1,20,000/contract |
| Variable cost | Rs 750 | Rs 66,000 |
| **Contribution/unit** | **Rs 250** | **Rs 54,000** |
| Contribution margin | 25% | 45% |
| Annual volume | 90,000 | 250 |
| Total contribution | Rs 2.25 cr | Rs 1.35 cr |

**Company economics:** blended CM 30% · fixed cost Rs 2.094 cr · **break-even Rs 6.98 cr** (~29,760 goods units) · margin of safety **41.8%** · AMC **LTV:CAC 7.2x**, payback 6.7 months.

**KPI tree (how the numbers roll up):**

```
                       PAT Rs 1.11 cr
                             |
              EBIT Rs 1.596 cr  =  Contribution 3.60cr - Fixed 2.094cr(- Fin cost in PBT)
             /                              \
   Goods contribution 2.25cr        Services contribution 1.35cr
      /        |        \                 /        |        \
  Units    ASP Rs1,000  CM% 25%      Contracts  Price Rs1.2L  CM% 45%
  90,000                              250
     |          |          |            |          |           |
  demand/    pricing    input cost   retention   pricing    delivery
  coverage   discipline  & mix       + new logos            efficiency
```

**Analyst commentary:** *Goods carry the volume but the thin 25% margin means price discipline and input cost are the swing factors — a Rs 20 ASP slip on 90,000 units is Rs 18 lakh of contribution gone. Services are the profit engine per rupee (45% CM, 7.2x LTV:CAC); with a sub-7-month payback we are arguably starving AMC growth. Recommend the MD treat **AMC net-adds** and **goods ASP realisation** as the two board-level KPIs.*

**KPI → action map:**

| KPI | Owner | Drives the action |
|---|---|---|
| Goods ASP realisation (actual vs Rs 1,000) | Sales | Tighten discount approvals; protect contribution |
| Goods units vs plan | Sales | Pipeline coverage, channel expansion |
| Gross margin % (goods) | Procurement | Renegotiate input cost, manage product mix |
| AMC net-adds (new − churned) | Services | Fund acquisition (payback only 6.7 mo) |
| AMC retention % | Services | Renewal calls, SLA quality → protect LTV |
| CAC & LTV:CAC | FP&A | Set the S&M budget ceiling |

## How it's reviewed

The CFO's checks: (1) **tie-out** — goods contribution Rs 2.25 cr + services Rs 1.35 cr = Rs 3.60 cr = budget gross profit; break-even and unit numbers must reconcile to the approved plan, not float free. (2) **Blended vs simple margin** — she'll confirm you weighted the CM by revenue mix (30%), not averaged 25% and 45% to a wrong 35%. (3) **CAC definition** — is the Rs 18 lakh *only* new-logo acquisition spend, or does it wrongly include renewal/delivery cost? (4) **LTV conservatism** — did you use churn-implied lifetime and flag that it's undiscounted? (5) Every KPI has a named owner and action.

## Common mistakes & red flags

- **Averaging the two margins** to 35% instead of revenue-weighting to 30% — overstates profitability and understates break-even.
- **Treating depreciation/finance cost as variable** — they're fixed; putting them in the per-unit cost double-counts and distorts contribution.
- **Vanity LTV** — using revenue (Rs 1.2 L) not contribution (Rs 54k) in LTV inflates it ~2.2x. LTV must be a *margin* figure.
- **Ignoring churn** in lifetime — assuming contracts last forever gives an infinite LTV.
- **Confusing gross margin with contribution margin** — here they coincide for goods, but the moment a per-unit selling/logistics cost appears they diverge; keep the definitions explicit.
- **KPIs with no action** — "revenue" alone isn't a KPI you can act on; decompose to volume/price/margin so someone can *do* something.

## On the job & in the interview

Unit economics is how FP&A turns a P&L into levers. The CFO doesn't act on "gross profit fell"; she acts on "ASP slipped Rs 20 and units missed 1,500." The **contribution margin** (price − variable cost) is the number that scales with volume; **fixed cost ÷ CM% = break-even**; **margin of safety** tells you how much cushion you have; **LTV:CAC and payback** tell you whether growth spend pays.

**Q: "We sell goods at 25% margin and services at 45%. What's the blended margin and why can't I just average them?"**
*A: You weight by revenue, not count. 9cr×25% + 3cr×45% = 2.25 + 1.35 = 3.60cr on 12cr = 30%. A simple average (35%) assumes an equal revenue split, which we don't have — goods are 75% of revenue and drag the blend down toward 25%.*

**Q: "Our AMC LTV:CAC is 7x. Good news?"**
*A: It's healthy — above the 3x bar with a ~7-month payback. But a very high ratio often means we're under-spending on acquisition. Given the short payback, I'd model spending more to win logos: as long as incremental payback stays under ~12 months and we can deliver the SLA, growth is accretive. I'd watch retention closely because LTV is only as good as the churn assumption.*

**Q: "How many boxes to break even?"**
*A: Fixed cost Rs 2.094cr, blended CM 30% → break-even revenue Rs 6.98cr. Holding the 250 AMC contracts, goods must cover Rs 0.744cr of fixed cost at Rs 250/unit contribution = ~29,760 units, about a third of our 90,000 plan. Margin of safety is ~42%.*
