# Q&A — Comparable Company Analysis (Trading Comps)

A practice bank for Chapter 25. Work each problem before reading the answer. Section B problems are fully reproducible in Excel and every figure reconciles.

---

## Section A — Concept Check

**A1. In one sentence, what question does comparable company analysis answer?**
It answers "what would the market pay for this company today?" by valuing the target relative to what investors currently pay for similar publicly traded peers — a *relative*, market-anchored valuation, in contrast to the DCF's *intrinsic*, forecast-driven one.

**A2. Why express value as a multiple (a ratio) rather than an absolute dollar figure?**
A ratio strips out **scale**. Absolute value tells you a $2bn-revenue firm is worth more than a $200m one — which is uninformative. Expressing value as EV per dollar of EBITDA (or sales) normalises for size, so a $500m company and a $50bn company can legitimately inform each other's valuation.

**A3. State the equity-to-enterprise-value bridge.**
EV = Equity Value + Total Debt + Preferred Stock + Minority (Non-controlling) Interest − Cash & Equivalents. You add claims that rank ahead of or alongside common equity and subtract cash, a non-operating asset the buyer effectively recovers.

**A4. What is the single most important consistency rule in comps?**
The numerator and denominator must belong to the **same capital providers**. Enterprise Value (whole business) pairs only with **pre-interest** metrics (Revenue, EBITDA, EBIT). Equity Value (shareholders only) pairs only with **post-interest** metrics (Net Income, EPS, Book Value). Crossing them — EV/Net Income or Price/EBITDA — is the cardinal sin.

**A5. Why does EV/EBITDA pair with EV, but P/E pair with equity value?**
EBITDA is earned *before* interest is paid, so it belongs to all capital providers (debt + equity) → pair with EV. Net income is what remains *after* lenders are paid, so it belongs only to shareholders → pair with equity value.

**A6. When would you choose EV/Revenue over EV/EBITDA?**
When the target is early-stage, high-growth, or unprofitable, so EBITDA is negative and EV/EBITDA is meaningless. Its weakness: revenue says nothing about profitability — 3x sales means very different things at a 40% margin versus a 5% margin.

**A7. LTM versus forward multiples — define each and say which suits a high-growth firm.**
LTM (last twelve months) uses actual reported trailing results: backward-looking, no forecast risk. Forward (NTM / FY+1) uses analyst-consensus estimates: forward-looking. High-growth firms are almost always valued on **forward** multiples because the market prices their future, not their past.

**A8. Why prefer the median over the mean when summarising a peer set?**
The median is robust to outliers. A single peer at 40x can drag the mean into fantasy. If mean and median diverge sharply, an outlier is distorting the set — investigate before relying on the mean.

**A9. Give the LTM roll-forward formula.**
LTM metric = Most recent Fiscal Year + Latest Interim Stub − Comparable Prior-Year Stub. It adds the newest partial-year period and removes the same period from a year ago.

**A10. Why must the target be excluded from its own peer set (if it is public)?**
Otherwise you contaminate the peer statistics with the target's own current multiple — you would just be valuing it at its own market price (circularity), defeating the point of the exercise.

---

## Section B — Build / Computational Problems

### B1. Full EV/EBITDA comp — peers to implied share price (reconciling)

**Target "NovaData":** LTM EBITDA $500m; Net Debt $300m (debt $500m − cash $200m); diluted shares 80m.

**Peers (LTM, $mm):**

| Peer | Equity Value | Net Debt | EV | LTM EBITDA | EV/EBITDA |
|------|---:|---:|---:|---:|---:|
| Alpha | 7,200 | 800 | 8,000 | 800 | 10.0x |
| Beta | 4,000 | 500 | 4,500 | 450 | 10.0x |
| Gamma | 9,500 | 1,000 | 10,500 | 875 | 12.0x |
| Delta | 2,700 | 300 | 3,000 | 250 | 12.0x |
| Epsilon | 5,400 | 600 | 6,000 | 545 | 11.0x |

**Step 1 — verify one EV and one multiple.** Gamma: EV = 9,500 + 1,000 = 10,500; EV/EBITDA = 10,500 / 875 = **12.0x**. ✓

**Step 2 — summary statistics** of {10.0, 10.0, 11.0, 12.0, 12.0}: Mean = 55.0/5 = **11.0x**; Median (middle of sorted set) = **11.0x**; Min 10.0x, Max 12.0x. Mean = median → a clean, outlier-free set.

**Step 3 — apply the median (11.0x) to the target:**
- Implied EV = 11.0 × 500 = **$5,500m**
- Implied Equity = EV − Net Debt = 5,500 − 300 = **$5,200m**
- Implied Price = 5,200 / 80 = **$65.00**

**Step 4 — bracket a range with min/max:**
- At 10.0x: EV 5,000 → Equity 4,700 → 4,700/80 = **$58.75**
- At 12.0x: EV 6,000 → Equity 5,700 → 5,700/80 = **$71.25**

**Answer:** roughly **$59–$71 per share, midpoint ~$65.**

**Excel formulas** (Alpha in row 5, EV/EBITDA in column N, peers span rows 5:9):
`Equity =Price*Shares` · `NetDebt =Debt-Cash` · `EV =Equity+NetDebt` · `EV/EBITDA =EV/EBITDA` · `Median =MEDIAN(N5:N9)` · `ImpliedEV =11*500` · `ImpliedEquity =ImpliedEV-300` · `Price =ImpliedEquity/80`.

### B2. Net-cash reversal (EV/Revenue, unprofitable target)

**Target "CloudSprint":** EBITDA −$20m (so EV/EBITDA is useless); Revenue $400m growing 45%; **Net Debt −$150m** (net cash $150m); diluted shares 50m. Peer median EV/Revenue = 10.0x; growth-adjusted high end = 12.0x.

**At 10.0x:** Implied EV = 10.0 × 400 = $4,000m. Because the firm has **net cash**, equity is *higher* than EV: Equity = EV − Net Debt = 4,000 − (−150) = 4,000 + 150 = $4,150m. Price = 4,150/50 = **$83.00**.
**At 12.0x:** EV = $4,800m; Equity = 4,800 + 150 = $4,950m; Price = 4,950/50 = **$99.00**.

**Answer:** ~**$83–$99**. Key trap avoided: with net cash you *add* it back when bridging EV → equity; the sign of net debt flips.

### B3. Calendarisation + LTM scrubbing

**Peer "Meridian" (June 30 fiscal year-end).** FY2026 EBITDA (Jul-25–Jun-26) = $600m; FY2027 EBITDA (Jul-26–Jun-27) = $720m. EV = $7,260m.

Calendar 2026 = 6 months of FY2026 + 6 months of FY2027, so w = 0.5:
Calendar-2026 EBITDA = 0.5 × 600 + 0.5 × 720 = **$660m** → calendarised EV/EBITDA = 7,260 / 660 = **11.0x** (now comparable to December-year peers).

**Scrubbing.** Reported LTM EBITDA $650m includes a **$40m restructuring charge** (add back) and a **$15m building-sale gain** (remove): Normalised = 650 + 40 − 15 = **$675m**. True multiple = 7,260 / 675 = **10.8x**, versus 11.2x on reported EBITDA. Using unscrubbed EBITDA would have made the peer look ~0.4x more expensive and biased the target valuation upward.

*If the fiscal year ended in September instead:* calendar 2026 = 9 months from the FY ending Sep-2026 + 3 months from the next FY, so **w = 0.75**.

### B4. Build-it-yourself — Helios Materials (full reconciliation)

**Target "Helios":** LTM EBITDA $240m (includes a **$30m impairment** to add back and a **$10m insurance gain** to remove); Net Income $110m; Debt $400m; Cash $100m; diluted shares 60m.

**Peers (LTM, $mm):**

| Peer | Price | Shares | Debt | Cash | EBITDA | Net Inc |
|------|--:|--:|--:|--:|--:|--:|
| P1 | 40 | 100 | 600 | 150 | 520 | 250 |
| P2 | 25 | 80 | 300 | 100 | 300 | 150 |
| P3 | 60 | 50 | 500 | 200 | 360 | 160 |
| P4 | 18 | 120 | 250 | 80 | 210 | 95 |
| P5 | 33 | 90 | 450 | 120 | 400 | 180 |

**Step 1 — per-peer build** (Equity = Price×Shares; Net Debt = Debt−Cash; EV = Equity+Net Debt):

| Peer | Equity | Net Debt | EV | EV/EBITDA | P/E (Eq/NI) |
|------|--:|--:|--:|--:|--:|
| P1 | 4,000 | 450 | 4,450 | 8.56x | 16.00x |
| P2 | 2,000 | 200 | 2,200 | 7.33x | 13.33x |
| P3 | 3,000 | 300 | 3,300 | 9.17x | 18.75x |
| P4 | 2,160 | 170 | 2,330 | 11.10x | 22.74x |
| P5 | 2,970 | 330 | 3,300 | 8.25x | 16.50x |

**Step 2 — summary statistics.**
EV/EBITDA sorted {7.33, 8.25, 8.56, 9.17, 11.10}: Min 7.33x · 25th pctl (PERCENTILE.INC) **8.25x** · **Median 8.56x** · Mean **8.88x** · 75th pctl **9.17x** · Max 11.10x.
P/E: Median **16.50x**, Mean 17.46x.

**Step 3 — scrub the target.** Normalised EBITDA = 240 + 30 − 10 = **$260m**. Target Net Debt = 400 − 100 = **$300m**.

**Step 4 — EV/EBITDA valuation (median 8.56x):**
- Implied EV = 8.56 × 260 = **$2,225m**
- Implied Equity = 2,225 − 300 = **$1,925m**
- Implied Price = 1,925 / 60 = **$32.08**

**Step 5 — P/E valuation (median 16.50x):**
- Implied Equity = 16.50 × 110 = **$1,815m**
- Implied Price = 1,815 / 60 = **$30.25**

The two land close (~$30–32). They differ because P/E runs off net income, which is *after* interest and after the one-off items sitting in reported earnings, whereas EV/EBITDA runs off scrubbed, pre-financing EBITDA — leverage and non-recurring items drive the small gap.

**Step 6 — range (25th / 75th percentile EV/EBITDA):**
- At 8.25x: EV = 2,145 → Equity 1,845 → **$30.75**
- At 9.17x: EV = 2,383 → Equity 2,083 → **$34.72**

Range ≈ **$31–$35 per share**.

**Step 7 — forward stretch.** Peers' NTM EBITDA = LTM × 1.12; the EV (today's price) is unchanged, so each forward multiple = trailing ÷ 1.12. Median forward = 8.56 / 1.12 = **7.64x**. Target NTM EBITDA = 260 × 1.15 = $299m → Implied EV = 7.64 × 299 = $2,284m → Equity 1,984 → **$33.07**. Forward multiples are **lower** than trailing for growing companies simply because the denominator (next-year EBITDA) is larger while the price is the same.

> **Self-verification note:** the chapter's rough self-check anchor ("median near 10–11x, price ~$38–43") is an optimistic approximation. The exact arithmetic gives a **median of 8.56x** and a price near **$32**. Trust the reconciled numbers above — always let the arithmetic, not a memorised anchor, govern.

---

## Section C — Interview-Style Questions

**C1. Walk me through the equity-to-enterprise-value bridge and why each item is there.**
Start with equity value (price × diluted shares) — what common shareholders own. Add debt and preferred stock because those are senior claims on the same operating assets; add minority interest because the consolidated financials include a subsidiary the parent doesn't fully own, so EV must reflect the whole entity. Subtract cash because it's a non-operating asset — a buyer of the business effectively gets the cash back, lowering the net cost of the operations. The result, EV, is the value of the operating business to *all* capital providers.

**C2. Why is EV/EBITDA usually preferred over P/E?**
EV/EBITDA is **capital-structure-neutral** and largely tax-neutral. Two identical businesses financed differently will have very different P/E ratios (interest expense hits net income) but similar EV/EBITDA. That makes EV/EBITDA far better for comparing peers with different leverage or tax positions. P/E is distorted by capital structure, one-offs, and tax, and breaks entirely when earnings are negative. You'd still show P/E when peers have similar leverage and for investor familiarity.

**C3. Your DCF says $4.2bn but comps say $5.5bn. What do you do?**
I don't hide the gap — I investigate it. The gap is a research question. I'd check: are my DCF assumptions (terminal growth, WACC, margin trajectory) conservative relative to what the market is pricing into the peers? Is the target genuinely comparable to those peers on growth and margins, or am I applying a peer multiple to a slower-growing business? Is there a control premium or synergy story implied? I'd present both as a range on a football field and articulate *why* they differ rather than forcing them to agree.

**C4. A peer trades at 25x EBITDA while the rest of the set is at 11x. What do you do?**
First, understand *why*. It usually signals the peer isn't truly comparable — much faster growth, a pending acquisition, a temporarily depressed (near-zero) EBITDA that inflates the ratio, or one-time items I failed to scrub. I'd either exclude it as a non-comparable, or normalise its EBITDA if the distortion is a scrubbing issue. Either way I default to the **median** so the outlier doesn't swing my central estimate, and I document the decision.

**C5. When are two companies in the same industry *not* comparable?**
When they differ on the drivers that actually move multiples — chiefly **growth**, then margins, size, business model, and end markets. A 45%-growth SaaS firm and a 3%-growth legacy software licensor are both "software," but growth alone justifies a multiple that's multiples apart. "Same SIC code" is a screening start, not a comp set; judgement on comparability is where the rigor lives.

**C6. Why do precedent-transaction multiples usually exceed trading comps?**
Precedents come from actual M&A deals, whose prices embed a **control premium** (typically 20–40%) — buyers pay extra to control the company and often for expected synergies. Trading comps price a *minority stake at the current market*. So precedents value control; trading comps value a marginal share. Precedents generally sit above trading comps on the football field.

**C7. Should you add back stock-based compensation to EBITDA?**
There's no single right answer, but there's a right *discipline*: be **consistent across every company** in the set, including the target. Many analysts do *not* add SBC back, treating it as a real economic cost of paying employees. Whatever convention you pick, apply it identically to peers and target — inconsistency is what makes the multiple meaningless.

---

## Section D — Common-Error Spotting

**D1.** *"The target has EV of $6bn and net income of $400m, so EV/Net Income = 15x."*
**Error:** mismatched numerator/denominator — EV (whole business) paired with net income (shareholders only, post-interest). The cardinal sin. Use EV with EBITDA/EBIT/Revenue, or use Price/Equity Value with net income (P/E).

**D2.** *Analyst applies an EV/EBITDA multiple, gets Implied EV = $5,500m, and reports that as the equity value / divides straight by shares for price.*
**Error:** forgot to reverse the bridge. An EV multiple gives *enterprise* value; you must subtract net debt (and preferred, minority) to reach equity value before dividing by diluted shares. Here Equity = 5,500 − 300 = $5,200m, not $5,500m.

**D3.** *A net-cash company: "Net Debt is −$150m, so Equity = EV − 150 = EV minus 150."*
**Error:** sign flip. Equity = EV − Net Debt = EV − (−150) = EV **+ 150**. With net cash, equity value exceeds enterprise value; you add the cash back.

**D4.** *Comp uses basic shares outstanding to compute equity value.*
**Error:** must use **diluted** shares via the treasury stock method. Ignoring in-the-money options and convertibles understates the share count and overstates price per share.

**D5.** *Peer set mixes a December-fiscal-year firm's "FY2026E" with a June-fiscal-year firm's "FY2026E" directly.*
**Error:** no calendarisation. December-FY2026 (Jan–Dec 2026) and June-FY2026 (Jul-2025–Jun-2026) cover different periods. Convert each to a common calendar year by weighting the two overlapping fiscal years before comparing.

**D6.** *Analyst scrubs the peers' EBITDA for restructuring and impairments but applies the multiple to the target's raw, reported EBITDA.*
**Error:** inconsistent normalisation. If you clean the peers, you must clean the target identically (and vice versa). Here the target's reported $240m must be normalised to $260m before the multiple is applied, or the whole comparison is apples-to-oranges.

**D7.** *"The mean of the set is 14x (one peer is at 40x), so I'll value the target at 14x."*
**Error:** letting an outlier drive the central estimate through the mean. Default to the **median**; a 40x peer signals a non-comparable name to exclude or a scrubbing problem to fix.

**D8.** *The target is public and the analyst leaves it inside its own comp set.*
**Error:** circularity. The target's own multiple contaminates the peer statistics, so you'd be valuing it at its own current price. Always exclude the target from its own peer group.
