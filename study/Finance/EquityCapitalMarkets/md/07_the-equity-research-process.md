# The Equity Research Process

## The Problem / Why this matters
An equity research analyst's job is to form and defend a **view on a stock** — is it worth more or less than the market says, and why? That view drives buy/sell/hold recommendations that clients act on. Knowing the end-to-end process — coverage, information gathering, modelling, valuation, thesis, and the recommendation — is exactly what an equity research or investment-analyst interview tests, often as "walk me through how you'd analyse a company."

## Core Idea
Equity research is a repeatable process: **understand the business → model its financials → value it → compare to the market price → form a thesis and recommendation → monitor.** The output is an investment view supported by a model and a written note.

## Why it works this way
Markets are mostly efficient, so to add value an analyst must either know something the market underappreciates or interpret known facts better. That requires deeply understanding the business and its drivers, building a defensible forecast, and translating it into a value that can be compared to the price — then articulating *why* the market is wrong.

```mermaid
graph TD
  A[Understand the business and industry] --> B[Gather information]
  B --> C[Build a financial model / forecast]
  C --> D[Value: DCF + multiples]
  D --> E[Compare to market price]
  E --> F[Form thesis: over/undervalued and why]
  F --> G[Recommendation: buy/sell/hold + target]
  G --> H[Monitor and update]
```

## Full technical content

**Step 1 — Understand the business & industry.** What does the company do, how does it make money (revenue model, unit economics), what's its competitive position and moat, who are its customers and competitors, and what drives the industry (see fundamental analysis).

**Step 2 — Gather information.** Annual reports/10-Ks, quarterly results and concalls, management guidance, industry data, channel checks, expert networks, competitor filings, and news. Rigorous, primary-source-driven.

**Step 3 — Build the model.** A three-statement model with a **driver-based forecast** (revenue drivers → costs → the three linked statements), producing the free cash flows and metrics valuation needs (see the modeling chapter).

**Step 4 — Value.** Intrinsic (DCF) and relative (comps/multiples), triangulated to a value range and a target price (see applied valuation).

**Step 5 — Form the thesis.** The core argument: *why* the stock is mispriced. A good thesis is **differentiated** (a view the market doesn't fully hold), **specific**, and **falsifiable** (you can say what would prove you wrong). Identify the **catalysts** that will close the value gap and the **risks**.

**Step 6 — Recommendation.** Buy / Hold / Sell (or Overweight/Neutral/Underweight) with a **target price** and time horizon, and the expected return vs the current price.

**Step 7 — Write and communicate.** The research note (initiation or update) and verbal pitch to clients/PMs; then **monitor** results, news and thesis, updating the view as facts change.

**The analyst's edge — three sources of alpha:**
| Edge | Description |
|---|---|
| **Informational** | Knowing a fact the market hasn't priced (rare, and insider info is illegal) |
| **Analytical** | Interpreting known facts better (better model/insight) |
| **Behavioural/time-horizon** | Exploiting others' biases or short-termism |

Most legitimate edge is **analytical** and **behavioural**.

**Quality markers of good research:** a clear, differentiated thesis; a defensible model with sensible assumptions; explicit catalysts and risks; and intellectual honesty (state what would make you wrong).

## Channel checks and primary research in equity analysis
Public filings and models only go so far — the highest-conviction theses are usually backed by **channel checks**: primary research into a company's own ecosystem, run with the same rigour as market research (Part 3-4 of the market-research literature, directly transferable).
- **Supplier checks** — calling/meeting key suppliers to gauge order volumes, pricing trends, and capacity utilisation ahead of the company's own disclosure (a leading indicator of revenue).
- **Distributor/dealer checks** — for consumer and auto companies, calling a sample of dealers/distributors across regions to triangulate real sell-through (not just sell-in, which a company can inflate near quarter-end by stuffing the channel).
- **Customer/end-user surveys** — for B2C names, small structured surveys on brand awareness, repeat-purchase intent, or switching behaviour (identical methodology to Part 5 of market research: sample size, question design, bias avoidance all apply directly).
- **Expert networks** — paid platforms connecting analysts to former employees, industry consultants, or specialists for one-off calls; must be used within strict compliance boundaries (no MNPI — material non-public information — can be solicited or used).
- **Job-posting and hiring-trend analysis** — a company rapidly hiring in a new geography/function is a public, legal signal of expansion plans, cross-checked against management commentary.
- **Store-check/footfall studies** — for retail/QSR names, physically observing footfall and average transaction patterns at a sample of outlets — the equity-research analogue of a market-research "intercept" study (see Market Research, Part 5.6).

**Compliance boundary (tested in every legitimate research role's onboarding)**: any of the above crosses a hard legal line the moment it solicits or knowingly uses **material non-public information** — a supplier confirming "volumes are up" is a legitimate industry read; a supplier disclosing an unreleased quarterly number is insider information, and using it is a criminal offence under India's SEBI (Prohibition of Insider Trading) Regulations. A research analyst must be able to draw this line without hesitation.

## A full worked research note — "TechCo India Ltd" (illustrative)
Walking one company through the entire pipeline end to end is the single best interview-prep exercise for this chapter.

**Business understanding**: TechCo is a mid-cap Indian IT-services company, ₹8,500 crore revenue, historically 14% EBITDA margin, growing 12% p.a., trading at 18x forward P/E vs a peer group average of 22x.

**Model (driver-based, simplified)**: Revenue = existing client base (95% retention) × average contract growth (8%) + new client wins (4% incremental) = ~12% revenue CAGR over the forecast window. Margin: assume 100bps expansion over 3 years from offshore-mix shift and utilisation improvement, taking EBITDA margin from 14% to 15% (this single assumption is the crux of the thesis — see below).

**Valuation**: DCF using WACC 11.5% (cost of equity via CAPM ~13%, pre-tax cost of debt ~8.5%, D/E modest) and a terminal growth rate of 5% (nominal, in line with long-run Indian GDP-growth assumptions for a mature IT-services business) yields an intrinsic value of ₹1,150/share. Cross-check via relative valuation: applying the peer-average 22x forward P/E (rather than the stock's own 18x) to next-year EPS implies ₹1,190/share — the two methods converge within ~3.5%, a strong triangulation (Part 7.2 of the Market Research handbook's triangulation principle applies identically here).

**Thesis**: the market is pricing TechCo at a discount to peers (18x vs 22x) because of a perceived margin ceiling; the analyst's differentiated view is that the offshore-mix shift already underway (visible in headcount-location disclosures) will close 100bps of the gap over 3 years, which the market is not yet modelling — this, not revenue growth (already well understood and priced), is the source of edge.

**Catalysts**: next two quarters' margin prints beating consensus; management commentary on offshore-mix % at the next earnings call; a peer re-rating event that draws attention to the sector's margin trajectory.

**Risks**: wage inflation offsetting the offshore-mix benefit; a large client loss (client-concentration risk — check top-5-client revenue % in the filings); rupee appreciation compressing margins (a genuine India-specific IT-services risk worth naming explicitly, since revenue is often dollar-denominated while costs are rupee-denominated).

**Recommendation**: Buy, target ₹1,150-1,190 (DCF/comps range), current price ₹1,000, implying ~15-19% upside over a 12-month horizon; position sized moderately given single-driver (margin) thesis concentration.

**What would falsify this thesis**: two consecutive quarters of flat or declining offshore-mix % in management disclosures, or a margin miss attributed to wage inflation exceeding the offshore benefit — the analyst commits, in writing, to downgrading on either signal.

## Worked examples

**Example 1 — the process end to end.** Analyst covers an FMCG firm. Understands the business (rural distribution moat); models revenue off volume × price with margin expansion from premiumization; DCFs it and cross-checks EV/EBITDA vs peers → intrinsic ₹1,200 vs market ₹1,000. Thesis: the market underrates margin expansion from premiumization (differentiated view); catalyst: next two quarters of margin beats; risk: rural slowdown. Recommendation: **Buy, target ₹1,200, +20%.**

**Example 2 — differentiated vs consensus thesis.** Two analysts value the same stock at ₹1,000, exactly the market price, agreeing with consensus. Neither adds value — a research view is only useful when it *differs* from the price and has a reason. The job is to find and defend the gap.

**Example 3 — thesis falsification.** An analyst's Buy rests on a new product driving 15% volume growth. She states: "If the first two quarters show under 8% volume growth, the thesis is broken and I'll downgrade." That falsifiability is what separates research from cheerleading.

## How it is tested in interviews
- **"Walk me through how you'd analyse a company / research a stock."** — Recite: understand the business → gather info → model → value (DCF + comps) → compare to price → form a differentiated thesis with catalysts and risks → recommend with a target → monitor.
- **"What makes a good investment thesis?"** — "Differentiated from consensus, specific, with clear catalysts and risks, and falsifiable — you can state what would prove you wrong."
- **"Where does an analyst's edge come from?"** — "Mostly analytical (better interpretation) and behavioural (exploiting short-termism/biases); informational edge is rare and insider info is illegal."
- **"How do you decide buy vs sell?"** — "Compare intrinsic value/target to the market price; the gap and catalysts drive the rating and expected return."

## Traps & common mistakes
- Producing a view that **matches consensus/price** — it adds no value.
- A model with no **thesis** — data without a differentiated argument.
- No **catalysts** (why does the gap close?) or **risks** (what if you're wrong?).
- Not stating what would **falsify** the thesis — a recipe for holding losers.
- Chasing **informational edge** into insider-trading territory.

## First-principles recap
- Research = understand → model → value → compare to price → thesis → recommend → monitor.
- Value is only added when your view **differs from the market**, with a reason.
- A good thesis is differentiated, specific, catalyst-driven, and **falsifiable**.
- Edge is mostly analytical and behavioural.
- The output is a rating, a target price, and a defensible note.

## Quick-reference
| Step | Output |
|---|---|
| Understand business | Revenue model, moat, drivers |
| Model | Driver-based 3-statement forecast |
| Value | DCF + multiples → target |
| Thesis | Why mispriced + catalysts + risks |
| Recommendation | Buy/Hold/Sell + target + horizon |
| Edge | Analytical + behavioural |
