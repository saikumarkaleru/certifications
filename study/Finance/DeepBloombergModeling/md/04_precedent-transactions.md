# Building a Precedent Transactions Analysis

## What you'll be able to do

Build a precedent-transactions (deal comps) valuation: source relevant M&A deals from CapIQ Transactions or Mergermarket, screen them to a defensible set, pull the transaction value and target financials at the time of each deal, compute transaction multiples (EV/EBITDA, EV/Sales, EV/EBIT), read the control premium implied, adjust for timing/synergies, and apply the median to your target to imply an acquisition value. You'll know exactly why precedent multiples sit *above* trading comps and when to trust them. Worked on an Indian IT-services target.

## The drill — step by step

**1. Understand what you're building.** Trading comps (Chapter 3) value a company as an independent public entity. Precedent transactions value it as an *acquisition target* — what real buyers actually paid to gain control. Deal multiples embed a **control premium** (typically 20–40% over the undisturbed price) and often **synergies**, so they run higher. Use precedents when the question is "what would someone pay to buy this?"

**2. Source the deals.** In **CapIQ → Transactions** (or **Mergermarket**), screen the M&A database on:

- **Industry** of the target (BICS/GICS = IT Services)
- **Geography** (India targets; add global IT-services deals as reference, flagged)
- **Date** — last 3–5 years only; older deals reflect a different rate/valuation regime
- **Deal size** band comparable to your target
- **Stake** — control deals (>50%, ideally 100%); exclude minority stakes, they don't carry a control premium
- **Deal status** — completed (or announced), not rumoured/withdrawn
- **Consideration** — note cash vs. stock (stock deals can inflate headline value)

Bloomberg equivalent: `MA <GO>` (M&A / deal search) and `EVTS`. Each deal record gives announced date, target, acquirer, deal value, stake, and often the target's LTM financials at announcement.

**3. Pull the inputs per deal.** For each transaction you need the **Transaction Enterprise Value (TEV)** — offer equity value + target net debt assumed — and the **target's LTM financials at the announcement date** (revenue, EBITDA, EBIT). Critical: use the financials as they were *at the time of the deal*, not today's. CapIQ Transactions usually stores these; otherwise pull the target's LTM as of the announcement quarter.

**4. Compute transaction multiples.**

| Multiple | Formula |
|---|---|
| EV/EBITDA | TEV ÷ target LTM EBITDA at announcement |
| EV/Sales | TEV ÷ target LTM revenue |
| EV/EBIT | TEV ÷ target LTM EBIT |

Same claimant-consistency rule as trading comps — TEV over pre-interest metrics.

**5. Read the control premium.** Where the target was public, premium = (offer price per share ÷ undisturbed price ~1 day/1 month before announcement) − 1. Record it; the median premium is itself a data point ("deals in this space cleared at ~25–30% premia").

**6. Adjust for timing and synergies.**
- **Timing / regime:** a 2021 deal struck at peak multiples over-states today's fair value in a higher-rate 2026 environment. Weight recent deals more; note the vintage.
- **Synergies:** strategic buyers pay up for cost/revenue synergies embedded in the price. That's why a *strategic* precedent multiple can overshoot standalone value — flag strategic vs. financial-sponsor deals; sponsor deals are cleaner "no-synergy" reads.
- **Deal structure:** all-stock deals at a frothy acquirer price inflate headline TEV; note consideration mix.

**7. Summarise and apply.** Take **min/25th/median/75th/max** of each transaction multiple; **lead with the median**. Apply to the target's *current* LTM metric:

- Implied TEV = median deal EV/EBITDA × target LTM EBITDA
- Implied equity = Implied TEV − target net debt (+ net cash)
- Implied price = Implied equity ÷ diluted shares

**Worked example — a mid-cap Indian IT-services target, illustrative deals:**

| Announced | Target | Acquirer | TEV (₹ cr) | LTM EBITDA (₹ cr) | EV/EBITDA | Premium |
|---|---|---|---|---|---|---|
| 2022 | Mid-cap IT co A | Global SI | 12,000 | 750 | 16.0x | 32% |
| 2023 | Digital eng. co B | PE sponsor | 6,500 | 480 | 13.5x | 26% |
| 2021 | ER&D services C | Strategic | 9,000 | 500 | 18.0x | 40% |
| 2024 | BPM/IT co D | Global SI | 7,200 | 540 | 13.3x | 24% |
| **Median** | | | | | **14.75x** | **29%** |

Apply the median 14.75x to a target with LTM EBITDA ≈ ₹900 cr and net cash ≈ ₹500 cr, ~50 cr diluted shares:
- Implied TEV = 14.75 × 900 ≈ **₹13,275 cr**
- Implied equity = 13,275 + 500 ≈ **₹13,775 cr**
- Implied price = 13,775 cr ÷ 50 cr ≈ **₹276/sh**

Note this sits above where trading comps (say median 11–12x) would land — that gap is roughly the control premium plus synergy value.

## The output

A one-page deal-comps sheet: one row per transaction (date, target, acquirer, stake, consideration, TEV, target LTM metric, each multiple, premium); a stats block leading with the median; a "vintage" column so recency is visible; and an implied-value block (TEV → equity → per-share) applied to your target's current metrics. Footnotes flag strategic-vs-sponsor and any all-stock deals. Usually shown as the *top* bar of the football field, above trading comps.

## Checks & gotchas

- **Point-in-time financials.** Use the target's EBITDA *as of the deal announcement*, not its latest — the multiple is a ratio of the price paid to what the buyer bought then. Mixing today's EBITDA with an old price is the classic error.
- **Stale deals.** Pre-2021 multiples reflect near-zero rates; don't average a 2019 deal against 2025 without weighting for regime.
- **Strategic vs. financial buyer.** Strategic multiples carry synergies; sponsor deals don't. Blending them without a flag over-states standalone value.
- **Minority vs. control.** A 15% stake purchase has no control premium — exclude it or you'll understate.
- **Consideration mix.** All-stock deals can inflate TEV if the acquirer's stock was rich at signing.
- **Thin data.** M&A in a niche can give you only 3–4 usable deals — say so; a precedent set of two is a range, not a valuation.
- **Deal value ≠ equity value.** TEV includes assumed net debt; don't quote it as the equity cheque.

## Interview drill

**Q: "Why do precedent transactions usually give a higher value than trading comps?"**
A: "Because deal prices include a control premium — buyers pay above the undisturbed market price to acquire control — and often synergies a strategic buyer expects to realise. Trading comps value the company as-is in the public market; precedents value it as an acquisition. The gap is roughly premium plus synergy."

**Q: "Which financials do you use for the target in a precedent multiple — current or at the time of the deal?"**
A: "At the time of the deal. The multiple is price-paid over what the buyer was buying, so I use the target's LTM figures as of the announcement date. Using today's financials against an old price gives a meaningless ratio."

**Q: "When are precedent transactions less reliable than comps?"**
A: "When deals are stale — struck in a very different rate or valuation regime — when the sample is tiny, or when the set mixes strategic and sponsor buyers with very different synergy assumptions. Deal data is also lumpy and lags; trading comps update daily. I'd caveat the range accordingly."

## Practise free

No paid deal database? Reconstruct precedents from public sources:
- **BSE/NSE announcements & SEBI SAST filings** — open-offer documents disclose offer price, stake and undisturbed price → compute the control premium directly.
- **Company press releases / investor decks** — acquirers publish deal value and target revenue/EBITDA; capture TEV and the metric.
- **VCCEdge / Tracxn (free tiers), news archives (Mint, ET, Business Standard, Reuters)** — India M&A deal terms.
- **Mergermarket / CapIQ Transactions** if you have campus/library access.
Drill: pick five real Indian IT/BPO acquisitions from the last four years, dig the TEV and target LTM EBITDA out of the press releases, build the exact table above, take the median, and imply a value for a listed mid-cap target — then compare it to where trading comps put the same company and explain the gap.
