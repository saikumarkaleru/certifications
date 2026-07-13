# Variance Analysis & Bridges

## What it is & where it's used

Variance analysis is the discipline of explaining *why* actual results differ from plan (budget), forecast, or prior period — and doing it in a way that points a manager to a decision. A "bridge" is the structured walk from one number to another (Budget Revenue → Actual Revenue, or LY EBITDA → TY EBITDA) broken into named, additive drivers: price, volume, mix, FX, rate, efficiency, one-offs.

If you only remember one thing: **a variance is useless until it's decomposed into a driver someone owns.** "Revenue is ₹40 lakh below plan" is a symptom. "Volume was fine but realised price fell ₹18/unit because we over-discounted the North region" is an action.

Where it's used and who's tested on it:

| Role | How variance analysis shows up |
|---|---|
| FP&A analyst | Monthly Budget-vs-Actual (BvA) deck, driver bridges, commentary |
| Business finance partner | Explaining a plant/region/product-line miss to the GM |
| Controller / R2R | Flux analysis at close (BS & P&L movement explanations) |
| Cost accountant (CA) | Standard costing variances (MPV, MUV, LRV, LEV, overhead) |
| Corporate strategy / IR | Bridging EBITDA/EPS growth for board and investor decks |

## The gap: why companies want this (and college didn't teach it)

College teaches the *formulas* — material price variance = (SP − AP) × AQ — as isolated exam sums. Industry needs the opposite skill: taking a messy actuals file plus a budget file, reconciling them to the last rupee, decomposing the gap into 4–6 drivers that **sum exactly** to the total variance, and writing three sentences a busy GM will act on.

The specific gaps:

- **Reconciliation, not calculation.** Real files don't tie. Actuals sit in the ERP at transaction grain; budget sits in a flat Excel by product-month. You must join them and prove the bridge foots.
- **Mix.** Almost no MBA course properly separates *volume* from *mix*. It's the driver managers most often get wrong, and the one interviewers probe.
- **Materiality & narrative.** A 40-line variance table is not analysis. Pros surface the 3 drivers that explain 80% of the gap and stay silent on noise.
- **Sign discipline.** Favourable/unfavourable (F/U) is not "positive/negative" — a cost overspend is a negative number but you must label it U. Getting this wrong in a board deck is career-limiting.

## What "proficient" looks like

A job-ready person, handed a budget file and an actuals extract, can unaided:

1. Reconcile both to the same grain and confirm totals tie to the GL.
2. Build a **price/volume/mix bridge** where the components sum exactly to (Actual − Budget).
3. Produce a **waterfall chart** in Excel or Power BI showing the walk.
4. Correctly label every variance F or U with the right sign convention.
5. Apply a materiality threshold (e.g. > ₹5 lakh or > 5%) and comment on only those.
6. Write commentary in the form **[Driver] → [₹ impact, F/U] → [root cause] → [action/owner]**.
7. Do it monthly on a repeatable, refreshable model — not a one-off hack.

## Hands-on: how to actually do it

### The decomposition formulas (memorise these)

For a single product, comparing Budget (B) to Actual (A):

```
Total Rev variance = (Aqty × Aprice) − (Bqty × Bprice)

Price variance  = (Aprice − Bprice) × Aqty
Volume variance = (Aqty − Bqty) × Bprice
```

Price + Volume = Total. That's the two-way split. Now add **mix** for a multi-product portfolio (the version employers actually want):

```
Volume variance = (Total Aunits − Total Bunits) × Budget avg price   ← pure size
Mix variance    = Σ [ (Actual mix% − Budget mix%) × Total Aunits × Bprice_i ]
Price variance  = Σ [ (Aprice_i − Bprice_i) × Aqty_i ]
```

Rate/efficiency (cost side, standard costing):

```
Material Price Var (MPV)  = (Std price − Act price) × Act qty
Material Usage Var (MUV)  = (Std qty − Act qty) × Std price
Labour Rate Var (LRV)     = (Std rate − Act rate) × Act hrs
Labour Efficiency (LEV)   = (Std hrs − Act hrs) × Std rate
```

### Excel — building the bridge

Assume `Actuals` and `Budget` tables keyed by Product. Pull budget values next to actuals:

```excel
=XLOOKUP([@Product], Budget[Product], Budget[Qty])          'budget qty
=XLOOKUP([@Product], Budget[Product], Budget[Price])        'budget price
```

Per-row driver columns:

```excel
Price var   =([@ActPrice]-[@BudPrice])*[@ActQty]
Volume var  =([@ActQty]-[@BudQty])*[@BudPrice]
Check       =[@PriceVar]+[@VolVar]-([@ActQty]*[@ActPrice]-[@BudQty]*[@BudPrice])   'must be 0
```

Portfolio volume vs mix (SUMPRODUCT):

```excel
BudAvgPrice =SUMPRODUCT(Budget[Qty],Budget[Price])/SUM(Budget[Qty])
VolumeVar   =(SUM(Actuals[ActQty])-SUM(Budget[Qty]))*BudAvgPrice
MixVar      =SUMPRODUCT((Actuals[ActQty]/SUM(Actuals[ActQty])
             -Budget[Qty]/SUM(Budget[Qty]))*SUM(Actuals[ActQty])*Budget[Price])
```

F/U flag:

```excel
=IF([@TotalVar]>=0,"F","U")     'revenue: positive = Favourable
=IF([@CostVar]<=0,"F","U")      'costs:   spend below budget = Favourable
```

### The waterfall chart (native, Excel 2016+)

Select the bridge series (Start, +Price, +Volume, +Mix, End) → **Insert → Waterfall**. Right-click the Start and End columns → **Set as Total**. Colour F green, U red. Done — no float-column hacks.

### DAX (Power BI) measures

```dax
Price Var =
SUMX( VALUES(Sales[Product]),
    ([Actual Price] - [Budget Price]) * [Actual Qty] )

Volume Var =
( SUM(Actuals[Qty]) - SUM(Budget[Qty]) ) * [Budget Avg Price]

Total Var = [Actual Revenue] - [Budget Revenue]
Mix Var   = [Total Var] - [Price Var] - [Volume Var]   // plug so it foots
```

### SQL — reconcile actuals to budget at source

```sql
SELECT  b.product,
        b.qty              AS bud_qty,
        b.price            AS bud_price,
        a.qty              AS act_qty,
        a.price            AS act_price,
        (a.price-b.price)*a.qty                       AS price_var,
        (a.qty -b.qty )*b.price                       AS volume_var,
        a.qty*a.price - b.qty*b.price                 AS total_var
FROM        budget  b
LEFT JOIN   (SELECT product, SUM(qty) qty,
                    SUM(qty*price)/SUM(qty) price
             FROM invoices WHERE period='2026-06'
             GROUP BY product) a  ON a.product=b.product
ORDER BY ABS(a.qty*a.price - b.qty*b.price) DESC;      -- biggest miss first
```

### Python — reusable bridge function

```python
import pandas as pd

def revenue_bridge(bud, act):
    m = bud.merge(act, on="product", suffixes=("_b","_a"))
    m["price_var"]  = (m.price_a - m.price_b) * m.qty_a
    m["volume_var"] = (m.qty_a  - m.qty_b ) * m.price_b
    tot_var = (m.qty_a*m.price_a - m.qty_b*m.price_b).sum()
    bud_avg = (bud.qty*bud.price).sum()/bud.qty.sum()
    vol = (act.qty.sum()-bud.qty.sum())*bud_avg
    mix = tot_var - m["price_var"].sum() - vol
    return {"price": m.price_var.sum(), "volume": vol,
            "mix": mix, "total": tot_var}
```

## Worked example / mini-project

**Setup:** A mid-size Indian FMCG unit sells two SKUs. June 2026 budget vs actual:

| SKU | Bud Qty | Bud Price ₹ | Act Qty | Act Price ₹ |
|---|---|---|---|---|
| Premium | 10,000 | 250 | 9,000 | 260 |
| Value | 20,000 | 100 | 26,000 | 92 |

Budget revenue = 10,000×250 + 20,000×100 = ₹45,00,000
Actual revenue = 9,000×260 + 26,000×92 = ₹23,40,000 + ₹23,92,000 = ₹47,32,000
**Total variance = +₹2,32,000 (F)**

Now decompose:

**Price** = (260−250)×9,000 + (92−100)×26,000 = +90,000 − 2,08,000 = **−₹1,18,000 (U)**

**Portfolio volume** — budget avg price = 45,00,000 / 30,000 = ₹150. Total units: bud 30,000, act 35,000.
Volume = (35,000−30,000)×150 = **+₹7,50,000 (F)**

**Mix** = Total − Price − Volume = 2,32,000 − (−1,18,000) − 7,50,000 = **−₹4,00,000 (U)**

**Bridge (foots to +2,32,000):**

| Driver | ₹ | F/U |
|---|---|---|
| Budget revenue | 45,00,000 | |
| Price | −1,18,000 | U |
| Volume | +7,50,000 | F |
| Mix | −4,00,000 | U |
| **Actual revenue** | **47,32,000** | **F** |

**Commentary a GM will act on:**
> Revenue beat plan by ₹2.3L (F), but the beat is low quality. Volume drove +₹7.5L as total units ran 17% ahead. This was more than offset by an adverse mix of −₹4.0L (growth came from Value SKU, up 30%, while Premium fell 10%) and adverse price of −₹1.2L (Value discounted ₹8/unit to move stock). **Action:** Sales to defend Premium volume and roll back Value discounting — current trajectory dilutes gross margin even as top line grows. Owner: Regional Sales Head.

Reproduce it: drop the four-row table into Excel, add the driver columns above, insert a Waterfall chart.

## How it's tested

**Interview questions:**
- "Revenue is up but margin is down — walk me through how you'd find why." (They want price/mix separation.)
- "Difference between volume and mix variance?" (The classic filter.)
- "This cost variance is +₹2L — favourable or unfavourable?" (Sign discipline trap.)
- "Your bridge doesn't foot. Where do you look first?" (Grain mismatch, missing SKUs, FX.)

**Practical assessments:**
- **Timed Excel test (45–60 min):** given `budget.xlsx` + `actuals.xlsx`, build a BvA with price/volume/mix bridge, a waterfall, and 3 bullets of commentary.
- **Flux/close case:** "Here's this month's P&L vs last month — explain every line moving > ₹5L." (Controller roles.)
- **Standard costing sum:** compute MPV/MUV/LRV/LEV and reconcile to total cost variance (CA/cost-accountant roles).
- **Take-home:** a data set where the naive two-way split hides a mix story — they check if you catch it.

## Common mistakes & how pros avoid them

| Mistake | Fix |
|---|---|
| Bridge doesn't foot to total | Add a `check = sum(drivers) − total` column; never ship until 0 |
| Confusing volume with mix | Volume = *size* at budget avg price; mix = *composition* shift. Compute volume first, plug mix |
| Wrong F/U sign on costs | Costs: under-spend = F. Revenue: over = F. Label explicitly, don't rely on sign |
| Commenting on everything | Set a materiality gate (₹ or %); comment on the top 3 drivers only |
| Cause with no action | Every comment ends in an action + owner, not just "due to lower volume" |
| Comparing apples to oranges | Reconcile grain/currency/period first; strip FX into its own bridge column |
| Double-counting price & mix | Price on Actual qty, mix as the plug — don't derive both independently |

## Learn-it roadmap & resources

**Time to proficiency: 4–6 weeks** part-time for someone with your accounting base.

- **Week 1:** Nail the formulas — two-way (price/volume), then three-way (add mix). Do 10 hand sums. Standard costing variances overlap directly with CA Cost material.
- **Week 2:** Rebuild the worked example in Excel; master XLOOKUP, SUMPRODUCT, native Waterfall.
- **Week 3:** Automate — the Python function above, or a Power BI model with the DAX measures. Learn to refresh, not rebuild.
- **Week 4:** Write commentary. Take any bridge and force yourself to 3 action-oriented bullets under a materiality gate.

**Resources:**
- CA Inter Cost & Management Accounting — the standard costing chapter *is* variance analysis (free, you already have it).
- CFI's *FP&A* and *Budgeting & Forecasting* courses (paid) — bridge and commentary templates.
- Leila Gharani / "Excel Off The Grid" YouTube — waterfall and dynamic bridges (free).
- Practice data: Kaggle "retail sales" sets; build BvA on them.
- **Certification signal:** CMA (US) or CIMA cover this deeply; for your target roles, a strong Excel bridge in your portfolio beats another cert.

## Quick-reference

```
Two-way:
  Price var  = (Aprice − Bprice) × Aqty
  Volume var = (Aqty − Bqty) × Bprice

Three-way (portfolio):
  Volume = (ΣAqty − ΣBqty) × Budget avg price
  Mix    = Total − Price − Volume        (plug, must foot)

Cost / standard costing:
  MPV = (Sp−Ap)×Aq   MUV = (Sq−Aq)×Sp
  LRV = (Sr−Ar)×Ah   LEV = (Sh−Ah)×Sr
```

| Item | Rule |
|---|---|
| F/U — revenue | Actual > Budget = F |
| F/U — cost | Actual < Budget = F |
| Foot check | Σ drivers − total = 0 (mandatory) |
| Materiality | comment only if > ₹5L or > 5% |
| Waterfall | Insert → Waterfall → Set first/last as Total |
| Commentary | Driver → ₹ impact (F/U) → root cause → action + owner |
| Volume vs mix | Volume = size @ budget avg price; Mix = composition shift |
```
```
