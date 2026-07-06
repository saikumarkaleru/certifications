# Q&A — Precedent Transaction Analysis

Practice bank for Chapter 26. Work every build problem in Excel yourself before reading the answer; the arithmetic is designed to reconcile to the penny.

---

## Section A — Concept Check

**A1. In one sentence, what question does precedent transaction analysis answer that trading comps cannot?**

"What would an acquirer have to pay to buy 100% of this company, including control?" Trading comps read prices off a market for small, minority, non-controlling stakes; precedent transactions read prices off actual completed acquisitions of whole companies, so they capture the control premium that trading comps structurally miss.

**A2. Why are transaction multiples usually higher than trading multiples for the same company?**

Because a deal price embeds three things a market share price does not: (1) the value of control (the right to change management, capital structure, strategy, and capture all cash flows); (2) expected synergies that a strategic buyer shares partly with the seller to win; and (3) auction/negotiation tension, where the winning bid is by definition the highest anyone was willing to pay. The gap between the two multiples is essentially the control premium plus embedded synergies.

**A3. What is the typical range for a control premium over the undisturbed price, and what is "undisturbed"?**

Roughly 20%–40% for public targets, higher in hot bidding wars. "Undisturbed" means the target's share price about one month before the deal was announced — before takeover rumors leaked and inflated the price.

**A4. State the iron rule of numerator–denominator consistency.**

An enterprise-value numerator must sit over a pre-financing, pre-interest metric (Revenue, EBITDA, EBIT). An equity-value numerator (offer price, equity purchase price) must sit over a post-interest metric (Net Income, EPS, Book Equity). EV/Net Income or Equity/EBITDA is meaningless.

**A5. Why should you never apply a precedent-transaction multiple and then add a separate control premium?**

Because the transaction multiple was computed on a control-inclusive deal price, so it already contains the premium. Adding another premium double-counts it — you would be putting a premium on a premium.

**A6. Median or mean — which do you lead with, and why?**

Median. Deal samples are small and right-skewed by the occasional strategic buyer who massively overpaid in an auction. The median resists that pull; the mean gets dragged toward the outlier.

**A7. Why must the denominator be measured "as of announcement" rather than today?**

The multiple must be internally contemporaneous: a deal price struck in, say, 2019 must be divided by the target's LTM metric available in 2019. Pairing an old deal price with today's EBITDA silently distorts the ratio.

**A8. Which is the conventional pricing point for a transaction multiple — announcement or completion?**

Announcement-date deal terms. Databases sometimes store completion values; know which convention your source uses and apply it consistently across the whole set.

**A9. A "nm" appears in your EV/EBITDA column. What does it mean and how did the model produce it?**

"nm" = not meaningful, the professional flag for a non-positive or absurd denominator (e.g., negative EBITDA). The build wraps each ratio in `=IF(denominator<=0,"nm",EV/denominator)` so the cell prints text instead of a nonsense or error value. Statistical functions like `MEDIAN` and `AVERAGE` skip text cells automatically.

**A10. Where does precedent transaction analysis usually plot on a football field, and relative to what?**

To the right (higher) of trading comps, because it embeds control and synergies. It typically marks the high end of the valuation range; trading comps mark a lower, minority-value floor.

---

## Section B — Build / Computational Problems

### B1 — One transaction multiple, end to end (with preferred and minority)

DeltaCo will acquire OmegaCo at **$75.00/share**. OmegaCo has **12m** diluted shares, **$90m** debt, **$20m** preferred, **$10m** minority interest, **$15m** cash, **LTM EBITDA $60m**, **LTM Revenue $250m**. Compute the deal EV/EBITDA and EV/Revenue.

**Answer.**
- Equity purchase price = 75.00 × 12 = **$900m**
- Deal EV = 900 + 90 + 20 + 10 − 15 = **$1,005m**
- EV/EBITDA = 1,005 / 60 = **16.8x** (16.75)
- EV/Revenue = 1,005 / 250 = **4.0x** (4.02)

*Self-check:* numerator is EV, denominators are pre-financing (EBITDA, Revenue) — consistent. Note preferred and minority are **added** in the bridge (they are claims senior to or alongside common equity), cash is **subtracted**.

### B2 — Full comp set, statistics, and application (the core exercise)

You are valuing **ForgeCo**: **LTM EBITDA $130m**, **debt $220m**, **cash $20m**, **35m** diluted shares, currently trading at **$34/share**. Your six-deal comp set (deal EV given directly):

| Deal | Deal EV ($m) | LTM EBITDA ($m) | EV/EBITDA |
|---|---:|---:|---:|
| A | 1,100 | 100 | 11.0x |
| B | 1,000 | 80 | 12.5x |
| C | 1,560 | 120 | 13.0x |
| D | 1,260 | 90 | 14.0x |
| E | 1,705 | 110 | 15.5x |
| F | 1,190 | 70 | 17.0x |

**Task:** compute Min, Q1 (`QUARTILE.INC`), Median, Mean, Q3, Max; then apply the 25th / median / 75th multiples to ForgeCo and give an implied per-share range, midpoint, and control premium.

**Answer — statistics.** Sorted: 11.0, 12.5, 13.0, 14.0, 15.5, 17.0.
- Min = **11.0x**, Max = **17.0x**
- Median = average of 3rd and 4th = (13.0 + 14.0)/2 = **13.5x**
- Mean = (11.0 + 12.5 + 13.0 + 14.0 + 15.5 + 17.0)/6 = 83.0/6 = **13.83x**
- Q1 `=QUARTILE.INC(range,1)`: rank = 0.25×(6−1)+1 = 2.25 → 12.5 + 0.25×(13.0−12.5) = **12.625x**
- Q3 `=QUARTILE.INC(range,3)`: rank = 0.75×5+1 = 4.75 → 14.0 + 0.75×(15.5−14.0) = **15.125x**

**Answer — apply to ForgeCo.** Net debt = debt − cash = 220 − 20 = **$200m**.

| Case | Multiple | Implied EV ($m) | − Net Debt 200 | Implied Equity ($m) | ÷ 35m = Per share |
|---|---:|---:|---:|---:|---:|
| Low (Q1) | 12.625x | 1,641.25 | 200 | 1,441.25 | **$41.18** |
| Mid (Median) | 13.5x | 1,755.00 | 200 | 1,555.00 | **$44.43** |
| High (Q3) | 15.125x | 1,966.25 | 200 | 1,766.25 | **$50.46** |

- Implied range **$41.18 – $50.46**, midpoint (median) **$44.43**.
- Control premium at midpoint vs $34 = 44.43/34 − 1 = **30.7%** — squarely inside the 20%–40% band, a reassuring sanity check.

*Self-check on the mid case:* 13.5 × 130 = 1,755 EV; − 200 net debt = 1,555 equity; ÷ 35 = $44.43. Reconciles.

### B3 — Trading comps vs precedent transactions (isolating the premium)

Trading comps for ForgeCo's peer group give a median **EV/EBITDA of 10.0x**. What per-share value does that imply, and what is the deal-vs-trading premium at the precedent midpoint?

**Answer.**
- Trading EV = 10.0 × 130 = $1,300m; equity = 1,300 − 200 = $1,100m; ÷ 35 = **$31.43/share**
- Premium of precedent midpoint over trading value = 44.43 / 31.43 − 1 = **41.4%**

That ~41% gap is the control premium plus embedded synergies. Same company, same $130m EBITDA — the only difference is that transaction multiples price control and trading multiples do not.

### B4 — Capstone: the chapter's HydraTools build (verify honestly)

**HydraTools:** LTM EBITDA $95m, debt $180m, cash $25m, 30m shares, trading $40. Comp set (announcement-date):

| Acquirer/Target | Offer/sh | Shares (m) | Debt | Cash | EBITDA | Equity | Deal EV | EV/EBITDA |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Titan/Orion | 62 | 18 | 120 | 20 | 70 | 1,116 | 1,216 | 17.4x |
| Vega/Lyra | 45 | 22 | 90 | 15 | 66 | 990 | 1,065 | 16.1x |
| Nova/Sirius | 88 | 14 | 200 | 30 | 105 | 1,232 | 1,402 | 13.4x |
| Atlas/Rigel | 33 | 25 | 150 | 40 | 60 | 825 | 935 | 15.6x |
| Comet/Vela | 71 | 20 | 175 | 35 | 118 | 1,420 | 1,560 | 13.2x |

**Statistics (EV/EBITDA):** sorted 13.2, 13.4, 15.6, 16.1, 17.4 → Median **15.6x** (15.583), Mean **15.1x**, Q1 **13.4x** (13.352), Q3 **16.1x** (16.136).

**Apply** (EBITDA 95, net debt 180 − 25 = 155, 30 shares):
- Q1: 13.352 × 95 = 1,268.4 EV → 1,113.4 equity → **$37.11**
- Median: 15.583 × 95 = 1,480.4 EV → 1,325.4 equity → **$44.18**
- Q3: 16.136 × 95 = 1,532.9 EV → 1,377.9 equity → **$45.93**

Midpoint control premium vs $40 = 44.18/40 − 1 = **10.4%** — *below* the textbook 20%–40% band, and the low case ($37.11) actually dips beneath the current $40 price. **This is the lesson of task 6: do not force the data into the expected band.** The two lowest multiples (Nova 13.4x, Comet 13.2x) belong to the two *largest* targets by EBITDA (105 and 118) — a size discount, since bigger deals often trade at lower multiples. Two honest readings follow: (a) if HydraTools is closest in size/profile to those large deals, they are your best comps and the analysis is telling you HydraTools is already near fully valued with little takeover upside; or (b) if the market price of $40 already reflects takeover speculation, the "undisturbed" price is lower and the true premium is wider. Either way, the correct move is to investigate comparability, not to invent a higher multiple. Trimming the two low deals only lifts the median to ~16.1x (~$45.94, premium ~15%), still short of 20% — confirming the signal is real, not a single outlier.

---

## Section C — Interview-Style Questions

**C1. Walk me through how you'd value an acquisition target using precedent transactions.**

Screen for 6–15 completed M&A deals of businesses comparable in industry, size, geography, and margin/growth profile. For each, pull the announcement-date deal terms and build the equity-to-EV bridge: equity purchase price = offer/share × fully diluted shares, then EV = equity + debt + preferred + minority − cash. Divide each deal's EV by the target's LTM EBITDA (and Revenue, EBIT as relevant), flagging non-positive denominators as "nm." Take the median and the 25th–75th percentile range, discarding true outliers after reading the story behind each deal. Apply the median and quartile multiples to my target's LTM EBITDA to get implied EV, subtract my target's net debt to reach equity value, and divide by diluted shares for a per-share range. I'd present that alongside trading comps and a DCF on a football field, and note that the transaction range sits above trading comps by roughly the control premium.

**C2. Why would a strategic buyer pay a higher multiple than a financial sponsor for the same target?**

A strategic (corporate) buyer can realize synergies a financial buyer cannot: eliminate duplicate overhead, gain procurement scale, cross-sell into a wider distribution network. Those synergies raise the price the strategic can justify, and competitive tension lets the seller capture part of that value. A sponsor (PE fund) has no operating overlap, so it relies on financial engineering and standalone cash flows and typically caps its bid lower. That's why, if my client is a sponsor, I'd weight sponsor-led precedents over strategic mega-deals.

**C3. Your precedent range and your DCF disagree sharply. How do you reconcile them?**

They answer different questions, so some gap is expected — precedents embed a control premium and current-market deal sentiment, while a DCF is intrinsic and cycle-neutral. First I'd check for mechanical errors: contemporaneous denominators, the EV/equity consistency rule, net-debt bridges. Then I'd interrogate the drivers: are my precedents from a frothy vintage with cheap debt, inflating multiples? Is my DCF terminal value using a defensible exit multiple (often itself calibrated from these precedents)? I'd present both as a range on the football field rather than collapsing them to one number, and explain which forces push each estimate high or low.

**C4. When is precedent transaction analysis unreliable?**

When the sector has few recent, comparable deals (small, unstable sample); when the market cycle has turned since the deals closed (boom-era multiples overstate a downturn buyer's willingness to pay); when the set is contaminated by distressed forced sales (too low) or must-have strategic bidding wars (too high); or when deal structures differ wildly (earnouts, stock-for-stock, contingent value rights) so the headline "price" isn't comparable. In those cases I'd lean more on trading comps and DCF and treat precedents as a directional high-end reference only.

**C5. A banker's fairness opinion lists ten precedent transactions. Can you just copy them?**

They're an excellent starting point — the banker already did comparability screening and defined "transaction value" — but I'd verify rather than copy blindly. Databases and bankers differ on whether deal value nets cash, includes assumed debt, or uses announcement vs completion pricing. I'd trace the highest-stakes multiples back to the primary filings (DEFM14A, tender documents) and confirm each fits my own bridge convention before relying on them.

---

## Section D — Common-Error Spotting

**D1. An analyst values a target with a 12.0x precedent-transaction median, gets an implied value, then multiplies by 1.30 "to add a control premium." What's wrong?**

Double-counting. The 12.0x came from control-inclusive deal prices, so the premium is already in the number. Multiplying by 1.30 premiums the premium and overstates value by ~30%. The fix is to apply the multiple and stop.

**D2. A model computes EV / Net Income to build a transaction multiple. Fix it.**

Inconsistent capital-structure sides. EV belongs to all capital providers (pre-interest), while Net Income is after interest and belongs only to equity. Use either EV/EBIT (both pre-interest) or Equity value/Net Income = P/E (both post-interest).

**D3. To value a 2024 deal's target, an analyst divides the 2019 announced deal price by the target's 2024 LTM EBITDA. What's the error?**

Numerator–denominator time mismatch. The 2019 deal price must be divided by the LTM EBITDA available at the 2019 announcement. Using 2024 EBITDA (likely grown) understates the multiple and corrupts the comp.

**D4. The implied EV comes out to $1,680m; the analyst reports equity value of $1,680m and a per-share of $67.20 on 25m shares. The target has $200m debt and $40m cash. What's missing?**

The equity bridge on the *target*. Implied equity = implied EV − net debt = 1,680 − (200 − 40) = 1,680 − 160 = $1,520m, giving $60.80/share, not $67.20. Skipping the net-debt subtraction overstates equity by the net-debt amount ($160m / $6.40 per share here).

**D5. A comp set of three deals — a distressed bankruptcy sale, a stock-for-stock merger of equals, and a hostile bidding war — is used to value a healthy target in a friendly sale. What's the problem, and what's the professional fix?**

Too few deals and non-comparable stories. Three deals across three radically different transaction contexts is not a comp set: the distressed sale prices too low, the bidding war too high, and a merger of equals may carry little or no premium. The fix is to expand to 6–15 deals that match business model, size, geography, and deal type (friendly, financial vs strategic), read the narrative behind each multiple, and flag or exclude true idiosyncratic outliers before taking the median.

**D6. An analyst reports a single point estimate of "$60.80 per share" from precedent transactions. Why is that poor practice?**

The method is inherently imprecise — small, skewed samples across different vintages and structures. A single number implies false precision. Report a range (25th–75th percentile), lead with the median, and let the football field show the spread against other methods.
