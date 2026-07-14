# Actuals Arrive: Variance Analysis and Commentary

## The ask

It's Wednesday, 8 July 2026. Q1 (Apr-Jun) is closed in Tally. The CFO pings you at 9:10 am:

> "Q1 revenue came in at Rs 2.70 crore against Rs 2.85 crore budget — we're Rs 15 lakh light, minus 5%. The board call is Friday. I need a variance bridge that tells me *why*: is it price, volume, mix, or margin? And two paragraphs of commentary I can read out. Don't just tell me we missed — tell me what it means for the full year."

Deadline: Thursday 9 July, noon. This is the deliverable that makes or breaks your reputation — anyone can subtract two numbers; FP&A explains the gap.

## What you're given

**Q1 budget vs actual dump (from Tally + CRM):**

| Metric | Budget Q1 | Actual Q1 |
|---|---:|---:|
| Goods units | 22,500 | 21,000 |
| Goods ASP | Rs 1,000 | Rs 1,020 |
| Goods revenue | Rs 2.25 cr | Rs 2.142 cr |
| Services revenue | Rs 0.75 cr | Rs 0.75 cr |
| **Total revenue** | **Rs 2.85 cr** | **Rs 2.70 cr** |
| Gross margin % | 30.0% | 28.5% |
| Opex | (budget) | +Rs 5 lakh over |

*Note:* goods actual revenue = 21,000 x Rs 1,020 = Rs 2,14,20,000 ≈ Rs 2.142 cr. With services flat at Rs 0.75 cr, total = Rs 2.892 cr — but the reported actual is Rs 2.70 cr. The residual Rs 19 lakh is a small returns/credit-note and cut-off adjustment booked to goods; for the price-volume bridge we decompose the goods gap using the clean unit and ASP figures and reconcile the remainder as an "other/adjustment" bucket.

## Build it — step by step

The core tool is the **price-volume-mix (PVM) decomposition**. For the goods segment, the total goods variance splits cleanly into a volume effect and a price effect.

**Step 1 — Set the identity.** Revenue = Units x Price. The variance between actual and budget decomposes as:

```
Volume variance = (Actual units − Budget units) × Budget price
Price variance  = (Actual price − Budget price) × Actual units
```

(Using budget price for volume and actual units for price is the standard convention so the two pieces sum exactly to the total variance — no cross-term left over.)

**Step 2 — Volume effect (goods).**

```
Volume var = (21,000 − 22,500) × Rs 1,000
           = (−1,500) × 1,000
           = −Rs 15,00,000   (unfavourable Rs 15 lakh)
```

We sold 1,500 fewer units; at the budgeted Rs 1,000 each, that's Rs 15 lakh of lost revenue.

**Step 3 — Price effect (goods).**

```
Price var = (Rs 1,020 − Rs 1,000) × 21,000
          = 20 × 21,000
          = +Rs 4,20,000   (favourable Rs 4.2 lakh)
```

We charged Rs 20 more per unit on the 21,000 units actually sold — a Rs 4.2 lakh cushion.

**Step 4 — Net goods variance.**

```
Net goods = −15,00,000 + 4,20,000 = −Rs 10,80,000
```

Check: budget goods 2.25 cr − actual clean 2.142 cr = −Rs 10.8 lakh. Ties exactly.

**Step 5 — Services and mix.** Services landed on plan (Rs 0.75 cr), so no volume/price variance there. **Mix effect**: because goods (25% GM) fell and services (45% GM) held, the *share* of high-margin services rose — that partially props up blended margin, but the absolute goods shortfall still drags total revenue.

**Step 6 — Margin and opex bridges.** Gross margin came in at 28.5% vs 30.0% budget — 150 bps light. On Rs 2.70 cr actual revenue that's a gross-profit drag of:

```
Margin var = 2.70cr × (28.5% − 30.0%) = 2.70cr × (−1.5%) = −Rs 4.05 lakh
```

Driven by input-cost inflation on goods plus the mix/return noise. Opex ran Rs 5 lakh over budget (early hires pulled forward from the Q4 plan).

**Step 7 — Reconcile the headline.** Revenue bridge from budget Rs 2.85 cr to actual Rs 2.70 cr:

```
Budget revenue                       2.850 cr
Goods volume        −0.150 cr
Goods price         +0.042 cr
Other/returns adj   −0.042 cr
Services            0.000 cr
= Actual revenue                     2.700 cr
```

## The deliverable

**Q1 FY27 Revenue Variance Bridge (waterfall)**

| Step | Rs cr | Running total |
|---|---:|---:|
| Budget revenue | | 2.850 |
| Goods volume (−1,500 u × Rs 1,000) | (0.150) | 2.700 |
| Goods price (+Rs 20 × 21,000 u) | 0.042 | 2.742 |
| Other / returns & cut-off adj | (0.042) | 2.700 |
| Services (on plan) | 0.000 | 2.700 |
| **Actual revenue** | | **2.700** |

**Gross-profit bridge:**

| Step | Rs lakh |
|---|---:|
| Budget GP (Q1, 30% × 2.85cr) | 85.5 |
| Revenue shortfall effect (30% × −15L) | (4.5) |
| Margin-rate effect (−1.5% × 2.70cr) | (4.05) |
| **Actual GP (≈28.5% × 2.70cr)** | **≈76.95** |

*Commentary (CFO-ready):*

> "Q1 revenue of Rs 2.70 cr is Rs 15 lakh (−5%) below the Rs 2.85 cr budget. The miss is a **volume problem, not a pricing problem**: we shipped 21,000 units against 22,500 planned — a Rs 15 lakh volume drag — only partly offset by Rs 4.2 lakh of favourable pricing, as ASP held at Rs 1,020 versus Rs 1,000 budgeted. That pricing strength tells us demand, not competitiveness, is the constraint. Services delivered exactly to plan (Rs 0.75 cr), confirming the recurring book is solid.
>
> "Gross margin of 28.5% is 150 bps below plan, split between input-cost inflation on goods and the revenue de-leverage. Opex ran Rs 5 lakh over on hires pulled forward from the Q4 plan. **Outlook:** the annual budget is back-loaded (Q4 goods Rs 2.85 cr on the March spike), so a 5% Q1 volume miss does not yet threaten the Rs 12 cr full-year number — *if* Q2 volume recovers. But two levers are now tight: the Rs 1.506 cr PBT floor has almost no headroom, and pulling opex forward has spent some of it early. Recommendation: hold the Q4 hires until Q2 volume confirms recovery, protecting ~Rs 5 lakh of PBT."

## How it's reviewed

The CFO checks that the **bridge foots** — every piece sums to the Rs 15 lakh headline with no plug. She checks the **convention** (budget price on the volume leg, actual units on the price leg) so volume and price don't double-count. She checks that **favourable and unfavourable signs are right** (fewer units = unfavourable; higher price = favourable). And she reads the commentary for a *causal story with an action*, not a restatement of the table. The killer question: "so what do we do about it?"

## Common mistakes & red flags

- **Reporting the net without the split.** "Goods down Rs 10.8 lakh" hides that volume (−15) and price (+4.2) are pulling in opposite directions — completely different management responses.
- **Double-counting the cross-term.** Using actual price on the volume leg AND actual units on the price leg over-attributes. Pick one convention and make the legs sum to the total.
- **Confusing margin-rate and margin-value.** A 150 bps rate drop and a revenue-driven GP fall are two different effects; separate them.
- **No outlook.** A variance with no forward read is a history lesson. Always answer "what does this mean for the full year."
- **Ignoring back-loading.** Judging the Rs 12 cr year off a soft Q1 when the budget itself put only 24% of goods in Q1 and 32% in Q4.

## On the job & in the interview

The "why": variance analysis is where FP&A earns its seat — it converts a Rs 15 lakh gap into a decision (hold the hires, chase volume, defend price). The decomposition isolates *controllable* (price, opex) from *market* (volume) causes.

Jargon: **price-volume-mix (PVM)**, **favourable/unfavourable (F/U)**, **bridge / waterfall**, **rate vs volume effect**, **de-leverage**, **plug**.

**Q: "Q1 revenue missed by Rs 15 lakh. Is that good or bad news, and why?"**
A: "Mixed, but structurally okay. The miss is entirely volume — 1,500 units at Rs 1,000, Rs 15 lakh — while price was actually *favourable*, ASP up Rs 20 for +Rs 4.2 lakh. Favourable price means we're not losing on competitiveness; we're demand-constrained. Given the budget is March-heavy, a 5% Q1 volume dip is recoverable, so I'd frame it as a demand watch-item, not a pricing crisis."

**Q: "Walk me through a price-volume decomposition."**
A: "Revenue is units times price, so the variance splits two ways: volume variance is the unit change times *budget* price, and price variance is the price change times *actual* units. Holding one factor at budget and the other at actual makes the two legs sum exactly to the total with no residual. Here: volume (21,000−22,500)×1,000 = −15 lakh; price (1,020−1,000)×21,000 = +4.2 lakh; net −10.8 lakh on goods."

**Q: "The margin also dropped to 28.5%. How do you separate that from the revenue miss?"**
A: "Two effects. The revenue shortfall costs GP at the budgeted 30% rate — 30% of the Rs 15 lakh miss is Rs 4.5 lakh. Separately, the *rate* fell 150 bps, which on Rs 2.70 cr of actual revenue is another Rs 4.05 lakh of GP. Splitting them tells management whether to chase volume or attack input costs — here, both."
