# Pairs Trading Strategy (India)

Pairs trading is the original market-neutral strategy: instead of betting on where the market goes, you bet on the *relationship* between two related instruments reverting to its historical norm. You buy the relatively cheap one and short the relatively expensive one, so a rally or a crash that lifts or sinks both legs roughly cancels out. What remains is the spread — and the wager that the spread, having stretched, will snap back. For an Indian trader with access to the deep NSE F&O universe (HDFC Bank vs ICICI Bank, Reliance vs ONGC, Tata Motors vs M&M, Nifty vs Bank Nifty), pairs trading offers a genuinely different return stream that does not care whether the Nifty is in a bull or bear phase. This chapter builds it as a complete, statistically-grounded system.

## Origin and idea

Pairs trading was pioneered at Morgan Stanley in the mid-1980s by a quantitative group under Nunzio Tartaglia, whose team noticed that certain pairs of stocks moved together so reliably that departures from their normal relationship were tradable. The insight is deceptively simple: two companies exposed to the same sector, economy, and risk factors should have prices that move in a stable long-run relationship. When something temporary — a block deal, an index rebalance, a news blip, liquidity — pushes them apart, the gap tends to close.

The idea rests on two statistical concepts:

- **Correlation** measures whether two series move *together* in the short run. High correlation is necessary but not sufficient — two stocks can be correlated yet drift apart permanently.
- **Cointegration** is the stronger, correct condition: even though each price is individually a random walk (non-stationary), a *linear combination* of the two — the spread — is **stationary**, meaning it oscillates around a stable mean and reliably reverts. Cointegration is what makes the reversion bet valid; correlation alone can betray you.

The strategy is **market-neutral** and **dollar- (rupee-) neutral**: by holding a long and a short of similar rupee value, the net exposure to the broad market (beta) is near zero. Your P&L comes from the spread, not from market direction. This is the appeal — and the discipline: you are trading a *relationship*, and your entire edge lives in that relationship continuing to hold.

## Exact rules

We define a mechanical, backtestable system for NSE. Everything is specified so it can be coded in Python (pandas + statsmodels) and executed on TradingView/broker terminals.

### Universe and pair selection

| Component | Rule |
|---|---|
| Universe | NSE F&O stocks (so both legs are shortable via futures) within the *same sector* |
| Candidate screen | Rolling 1-year correlation of daily returns > 0.80 |
| Cointegration test | Engle-Granger (ADF on residuals) or Johansen; require p-value < 0.05 over 1-year lookback |
| Fundamental sanity | Same sector, similar business/risk drivers (e.g., two private banks, two PSU oil names) |
| Liquidity | Both legs must have liquid, low-impact futures |
| Re-test cadence | Re-run cointegration monthly; drop pairs that fail |

### The spread and the signal

Define the hedge ratio **β** from an OLS regression of stock A on stock B:

**A_t = α + β · B_t + ε_t**, and the spread is **Spread_t = A_t − β · B_t** (the residual ε_t).

Convert the spread to a **z-score** over a rolling window (e.g., 60 trading days):

**z_t = (Spread_t − mean(Spread)) / stdev(Spread)**

| Component | Rule |
|---|---|
| Entry — short spread | z ≥ +2.0 → **short A, long β·B** (A is rich relative to B) |
| Entry — long spread | z ≤ −2.0 → **long A, short β·B** (A is cheap relative to B) |
| Exit — take profit | z reverts to 0 (spread back to mean) |
| Stop | z breaches ±3.0 (relationship stretching abnormally — possible regime break) |
| Time stop | Exit if no reversion within ~20 trading days (half-life guardrail) |
| Hedge sizing | Rupee-neutral using β: notional of A ≈ β × notional of B |
| Re-hedge | Recompute β on each monthly re-test; roll futures before expiry |

**Half-life check.** Fit the Ornstein-Uhlenbeck / AR(1) mean-reversion speed and estimate the spread's half-life. A half-life of 5–15 trading days is ideal; a half-life > 30 days means reversion is too slow to trade and the time stop will keep stopping you out. Reject pairs whose spread does not revert quickly.

### Filters

- Trade only pairs currently *passing* cointegration — a pair that decouples fundamentally (merger, fraud, regulatory action, sector re-rating) must be dropped, not doubled.
- Avoid entries into known idiosyncratic events on either leg (results, rating actions, index inclusion/exclusion).
- Cap capital per pair and diversify across 4–8 uncorrelated pairs to smooth equity.

## Worked India example

**Pair: ICICI Bank (A) vs HDFC Bank (B)** — two large private banks, high correlation, historically cointegrated.

Suppose over the past year daily-return correlation is 0.87 and Engle-Granger gives p = 0.02 (cointegrated). OLS hedge ratio **β = 0.9**: for every 1 share of ICICI, hedge with 0.9 "units" of HDFC exposure. The 60-day spread has mean 0 and standard deviation of ₹18.

Today: ICICI = **₹1,320**, HDFC = **₹1,700**.
Spread = 1,320 − 0.9 × 1,700 = 1,320 − 1,530 = **−₹210**. Suppose the rolling mean of the spread is −₹174 and stdev ₹18, so:

**z = (−210 − (−174)) / 18 = −36 / 18 = −2.0** → **long-spread signal**: ICICI is *cheap* relative to HDFC. **Long ICICI, short HDFC.**

**Sizing (rupee-neutral).** Allocate ₹5,00,000 per leg.
- Long ICICI: 500,000 / 1,320 ≈ **379 shares** (in practice, whole futures lots — use the nearest lot count; illustrative here).
- Short HDFC hedged by β: target β-scaled notional ≈ ₹4,50,000 → 450,000 / 1,700 ≈ **265 shares** short.

**Outcome — reversion (the base case).** Over the next 8 trading days the spread reverts toward its mean. Say ICICI rises to ₹1,352 (+₹32) while HDFC rises only to ₹1,712 (+₹12). New spread = 1,352 − 0.9 × 1,712 = 1,352 − 1,540.8 = −₹188.8, z ≈ −0.8; continue toward mean and exit at z ≈ 0.

- ICICI long P&L: 379 × (1,352 − 1,320) = 379 × 32 = **+₹12,128**.
- HDFC short P&L: 265 × (1,700 − 1,712) = 265 × (−12) = **−₹3,180**.
- **Net ≈ +₹8,948** on ~₹5,00,000 deployed per leg — and crucially, *both stocks rose*. A directional long-ICICI trader made money too, but a market-neutral book would have profited even if both banks had *fallen*, as long as ICICI fell less than HDFC (the spread narrowed).

**Outcome — the stop (the risk case).** If instead ICICI kept underperforming — say a bank-specific concern — and the spread stretched to z = −3.0 rather than reverting, the system exits at the stop. The relationship may be breaking (the pair decoupling), and the discipline is to take the small controlled loss, not to average down into a widening spread. This is where undisciplined pairs traders are destroyed: adding to a "cheap" leg that is cheap *for a reason*.

## Backtest, edge notes and realistic costs

**What the edge looks like.** A well-constructed Indian pairs book typically shows a **high win rate** (many small mean-reversion wins) with occasional larger losses when a pair decouples — the opposite profile of trend following. Sharpe ratios can be attractive *because* returns are market-neutral (low correlation to Nifty), which is the real prize: a return stream that diversifies a directional portfolio.

**Costs are the strategy's biggest enemy.** Pairs trading is a two-legged, relatively high-turnover strategy, and every entry/exit pays costs on *both* legs:

- **Brokerage + exchange + GST + SEBI + stamp** on both legs, both directions.
- **STT** — on futures it applies on the sell side; using stock futures for both legs keeps STT manageable versus shorting cash (which needs SLB/intraday).
- **Impact cost / bid-ask** — real on the smaller leg; stick to liquid pairs.
- **Futures roll cost** — pairs held across expiry must be rolled, paying the spread and any basis; positive/negative cost of carry differs between the two legs and can quietly erode edge.
- **Financing / margin** — two futures positions consume margin on both legs (partly offset by exchange-recognised spread margins for certain pairs).

A z ≥ 2 signal that reverts to 0 might capture, say, a 1.5–2σ move (≈ ₹27–36 on an ₹18-σ spread); if round-trip costs on both legs consume ₹5–8 of that, the *net* edge is thinner than the gross backtest suggests. **Always backtest net of realistic costs and roll assumptions** — a pairs strategy that looks brilliant gross and mediocre net is the norm, not the exception.

**Backtesting cautions specific to pairs:**

- **Look-ahead bias:** compute β and the z-score mean/stdev only on data available *before* each signal — a rolling, walk-forward window, never the full-sample statistics.
- **Survivorship & selection bias:** picking today's best-cointegrated pair and testing it on the same history is data-snooping. Select pairs out-of-sample.
- **Non-stationary cointegration:** relationships that held for years break (e.g., a merger like HDFC–HDFC Bank, a PSU divestment, a sector re-rating). Re-test continuously.

## Adaptations for NSE and F&O

- **Use stock futures for both legs.** This solves the shorting problem cleanly (cash shorts need SLB or must be intraday), gives leverage, and lets you build the hedge in liquid, marginable instruments. Mind lot sizes — perfect rupee-neutrality is approximated by whole lots.
- **Index pairs:** **Nifty vs Bank Nifty** is a classic Indian spread (banks are ~a third of the Nifty). Trade the ratio; z-score the Bank Nifty / Nifty ratio and revert. Fin Nifty vs Bank Nifty is a closely-related sub-spread.
- **Exploit spread margins:** NSE offers margin benefits on certain recognised calendar/inter-commodity spreads; check whether your pair qualifies to reduce capital drag.
- **Roll discipline:** roll both legs together before expiry to avoid basis blow-ups; never let one leg expire while the other lives.
- **Sector clusters** rich in candidates: private banks (ICICI/Axis/HDFC/Kotak), PSU banks (SBI/BoB/PNB), IT (TCS/Infosys/Wipro/HCLT), autos (Tata Motors/M&M/Maruti), metals (Tata Steel/JSW/Hindalco), oil & gas (Reliance/ONGC/BPCL/IOC).
- **MCX cross-hedges** (e.g., gold vs silver ratio) extend the same z-score reversion logic to commodities for a diversified pairs book.

## Pitfalls

- **Trading correlation, not cointegration.** Two stocks can be 0.9 correlated yet drift apart forever. Correlation without a passing cointegration test is a trap; the spread must be *stationary*.
- **The decoupling / structural break.** The strategy's fatal risk: a pair that was cointegrated ceases to be, because of a merger, fraud, regulation, or re-rating. The "cheap" leg is cheap for a real reason and the spread never reverts. The z = ±3 stop and continuous re-testing exist precisely to survive this.
- **Averaging into a losing spread.** "It's even cheaper now" is how pairs accounts blow up. Respect the stop.
- **Under-costing the backtest.** Gross edges evaporate net of two-leg costs and rolls. Model them honestly.
- **Static hedge ratio.** β drifts; a stale hedge ratio leaves you with unintended directional (beta) exposure. Recompute periodically.
- **Over-optimising entry thresholds.** Curve-fitting z-entry to 2.3 because it backtested better is fragile. Robust reversion works across a band of thresholds.
- **Ignoring liquidity on the smaller leg.** Impact cost on the thinner stock silently taxes every trade.
- **Event blindness.** Entering just before results/rating actions on one leg turns a spread bet into a coin flip.

## Interview-ready summary

Pairs trading is a **market-neutral** strategy that longs the relatively cheap and shorts the relatively expensive of two related instruments, profiting from the **spread reverting to its mean** rather than from market direction. Its statistical foundation is **cointegration** — the spread (a β-weighted linear combination of the two prices) must be **stationary**, not merely correlated — validated by an Engle-Granger/ADF or Johansen test with a fast (5–15 day) reversion **half-life**. The mechanical system: screen same-sector NSE F&O pairs for correlation > 0.8, confirm cointegration, compute the OLS hedge ratio β and a rolling **z-score** of the spread, **enter at z = ±2** (short the rich, long the cheap, rupee-neutral via β), **exit at z = 0**, **stop at z = ±3**, and enforce a **time stop** at the half-life. In India it is executed with **stock futures on both legs** (solving the short-sell and margin problems), with **Nifty–Bank Nifty** as a canonical index spread. The strategy's virtue is a return stream **uncorrelated to the Nifty**; its dangers are **structural decoupling** (a once-cointegrated pair breaking permanently), **two-leg transaction and roll costs** that thin the gross edge, and the temptation to **average into a widening spread**. Discipline is everything: trade cointegration not correlation, size rupee-neutral, honour the z = ±3 stop, and re-test the relationship continuously.
