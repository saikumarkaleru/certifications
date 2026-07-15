# Performance Metrics That Matter

## Why this matters — the pro vs retail gap this closes

Ask a retail trader how his strategy performs and he'll quote one number: return, or win rate. Both are near-useless alone. A 90%-win-rate system can blow up (nine Rs 1,000 wins, one Rs 20,000 loss). A 300% backtest return means nothing if it took a 70% drawdown to get there — no human holds through that, and leverage would have killed the account first. Pros read a *panel* of metrics that together answer the only questions that matter: **How much do I make per rupee of risk? How bad does it get? Will I survive the bad stretch? Is the edge real or luck?** This chapter defines the metrics, shows how to compute them from a trade log, and explains why drawdown and expectancy sit at the top of the hierarchy.

## The essentials — the metrics, precisely

**Return & risk-adjusted return**
- **CAGR** (compound annual growth rate): `(Ending/Starting)^(1/years) − 1`. The headline, but blind to risk.
- **Sharpe ratio:** `(annualised return − risk-free) / annualised volatility of returns`. Return per unit of *total* volatility. Use India's risk-free ~6.5–7% (T-bill / repo neighbourhood, 2026 — *verify*). Sharpe > 1 is good, > 2 is excellent and rare for retail.
- **Sortino ratio:** like Sharpe but divides by *downside* deviation only (volatility of negative returns). Fairer, because upside "volatility" isn't a problem. Usually higher than Sharpe.
- **Calmar ratio:** `CAGR / max drawdown`. Return per unit of worst pain. Calmar > 1 is respectable; institutions love it because it speaks to survivability.

**Drawdown**
- **Max drawdown (MDD):** the largest peak-to-trough fall in equity, in %. This is the metric that decides whether you *survive*. A 50% drawdown needs a 100% gain just to recover. Most retail traders quit (or get margin-called) somewhere around 20–30%.

**Trade-level quality**
- **Win rate:** % of trades that profit. Alone, meaningless — must be read with payoff.
- **Avg win / Avg loss (payoff ratio):** average winning trade ÷ average losing trade.
- **Expectancy:** the master number — average rupees (or R) per trade: `(Win% × Avg Win) − (Loss% × Avg Loss)`. If this isn't positive *after 2026 costs*, nothing else matters.
- **Profit factor:** `gross profit / gross loss`. > 1 is profitable; 1.3–1.6 is solid; > 2 is suspiciously good (check for overfitting).
- **Exposure:** % of time capital is actually in the market. High return at 5% exposure is very different from the same return fully invested — it affects capital efficiency and how you'd deploy idle cash.

**The hierarchy.** Expectancy and max drawdown outrank everything. A positive net expectancy says the edge exists; a tolerable drawdown says you'll still be trading when it pays off. CAGR without drawdown context is a boast, not information.

## Worked example — reading one strategy's numbers

You backtest the Bank Nifty opening-range system (after the Chapter-3 honesty fixes) over 4 years on Rs 5,00,000 starting capital. The trade log yields:

- Trades: 480 | Wins: 197 (41.0%) | Losses: 283 (59.0%)
- Avg win (net of 2026 costs): **Rs 9,800** | Avg loss (net): **Rs 6,500**
- Ending equity: Rs 9,20,000 | Worst peak-to-trough equity fall: Rs 5,90,000 → Rs 4,60,000

**Compute the panel:**

- **Payoff ratio** = 9,800 / 6,500 = **1.51**.
- **Expectancy** = `0.41 × 9,800 − 0.59 × 6,500 = 4,018 − 3,835 = +Rs 183 per trade.` Positive but *thin* — over 480 trades that's ~Rs 87,800 gross of the picture, and it means a small rise in costs or slippage flips it negative. Fragile edge.
- **Profit factor** = gross profit / gross loss = `(197 × 9,800) / (283 × 6,500) = 19,30,600 / 18,39,500` = **1.05.** Barely above 1 — you're working very hard for a razor-thin edge.
- **CAGR** = `(9,20,000 / 5,00,000)^(1/4) − 1 = (1.84)^0.25 − 1 ≈ **16.5%**.` Attractive on its own.
- **Max drawdown** = (5,90,000 − 4,60,000) / 5,90,000 = **22.0%.** Painful — many would quit here.
- **Calmar** = 16.5% / 22.0% = **0.75.** Below 1: you're taking more drawdown than annual return. Marginal.
- **Sharpe** (assume annualised return 16.5%, annualised vol 18%, risk-free 6.5%) = `(16.5 − 6.5) / 18` = **0.56.** Modest — a lot of noise per unit of return.

**Verdict:** the 16.5% CAGR looks great in isolation, but profit factor 1.05, expectancy +Rs 183, Calmar 0.75 and Sharpe 0.56 together say: *thin, fragile edge with drawdowns bigger than its annual return.* One regime shift or a cost hike sinks it. The full panel told the truth the CAGR hid.

## How pros do it / common mistakes

**How pros do it:**
- **Read the panel, never one metric.** CAGR + Sharpe/Sortino + max DD + Calmar + expectancy + profit factor, always together.
- **Anchor on drawdown and expectancy first.** "Can I survive the worst stretch, and is each trade net-positive after 2026 costs?"
- **Read the equity curve visually:** slope (return), smoothness (consistency), and the depth *and length* of underwater periods. A curve that's flat/underwater for 14 months will break your discipline even if it ends higher — length of pain matters as much as depth.
- **Compare metrics IS vs OOS.** If Sharpe halves out-of-sample, the in-sample number was fitted.
- **Treat profit factor > 2 or a drawdown that looks too small as a red flag**, not a trophy — usually overfitting or a hidden bias.

**Common mistakes / red flags:**
- Quoting win rate alone ("I'm right 70% of the time") while ignoring that losses are 4× the wins.
- Celebrating CAGR while ignoring a 40% drawdown no human would hold through.
- Computing metrics on *gross* returns — in 2026 India, costs are the difference between +Rs 183 and −Rs 500 per trade.
- Ignoring the *duration* of drawdowns; a two-year flat patch ends most trading careers.
- Too-small a sample (30 trades) making every ratio meaningless noise.

## Checklist / drill

**Metrics review checklist — before trusting any strategy:**
- [ ] Expectancy computed *net of 2026 costs* and clearly positive with margin.
- [ ] Max drawdown known, in %, and within my personal survivable limit (define it — e.g. 20%).
- [ ] Sharpe and Sortino computed with a real India risk-free (~6.5–7%, *verify*).
- [ ] Calmar > 1 (or a conscious reason to accept less).
- [ ] Profit factor between ~1.3 and ~2 (below = weak, above = check for overfitting).
- [ ] Metrics compared IS vs OOS; no metric collapses out-of-sample.
- [ ] Equity curve inspected for drawdown *depth and length* and underwater duration.

**Drill:** Export your last 50–100 trades to a sheet. Compute win%, avg win, avg loss, expectancy, profit factor, and max drawdown of the running equity. Then plot the equity curve and mark the deepest and *longest* underwater stretch. Ask honestly: would you have kept trading through that stretch with real money? If the answer is no, your problem isn't the strategy — it's that you were about to trade a drawdown you can't emotionally afford.
