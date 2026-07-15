# Backtesting Properly (Bias, Costs, Walk-Forward)

## Why this matters — the pro vs retail gap this closes

A backtest is the closest thing trading has to a laboratory — and the easiest place to lie to yourself. Retail traders run a strategy over past Nifty data, see a smooth rising equity curve, and go live with real money; then the "edge" evaporates. The equity curve wasn't a discovery, it was a *reflection of the very data used to build it*, distorted by hidden biases and missing costs. Pros treat a backtest as an adversarial exercise: they assume it's flattering them and hunt for the reasons why. This chapter covers the four ways a backtest lies — dirty data, look-ahead bias, survivorship bias, and unrealistic costs — and the discipline that catches them: in-sample/out-of-sample splits and walk-forward testing.

## The essentials — the four lies and the two disciplines

**1. Data quality.** Garbage in, confident garbage out. Indian-market gotchas: unadjusted prices around **stock splits, bonuses, and dividends** (a 5:1 split looks like an 80% crash if unadjusted), **index reconstitution** (Nifty 50 changes members), holidays and special sessions (Muhurat trading), and bad ticks. Always use split/bonus-**adjusted** series for signals, but remember real trading uses *un*adjusted traded prices for cost/STT calculation.

**2. Look-ahead bias.** Using information the moment couldn't have had. The classic sins:
- Signalling on a candle's **close** but assuming you filled at that same close (you can only act on the *next* bar).
- Using the day's high/low to decide an entry that happens *before* the high/low formed.
- Using a fundamental number (quarterly result) on its period-end date rather than its *announcement* date.
- Survivorship-adjusted or restated data leaking future knowledge.
Rule: at decision time `t`, the system may only use data available *at or before* `t`, and fills happen at `t+1` open (or worse).

**3. Survivorship bias.** Backtesting today's Nifty 50 over ten years tests only the *winners* that survived into the index — the Yes Banks and DHFLs that collapsed are silently excluded, inflating returns. Use a **point-in-time** universe (the actual index constituents on each historical date), or accept your equity-strategy backtest is optimistic.

**4. Realistic costs and slippage (2026).** This is where most "edges" die. Model *every* line of the Indian cost stack, effective **01-Apr-2026** (Budget 2026 — *verify on your broker contract note; rules change*):

| Cost | Equity intraday | Equity delivery | Futures | Options |
|---|---|---|---|---|
| STT | 0.025% on sell | 0.1% buy + sell | ~0.05% on sell | ~0.15% on premium (sell) & on exercise |
| Brokerage | flat ~Rs 20/order (or 0 delivery) | often Rs 0 | ~Rs 20/order | ~Rs 20/order |
| Exchange txn + SEBI | small % of turnover | " | " | higher % on premium |
| GST | 18% on (brokerage + txn) | " | " | " |
| Stamp duty | on buy side | on buy side | on buy side | on buy side |
| **Slippage** | model it | model it | model it | model it — worst here |

**Slippage** is the gap between your assumed price and your real fill. For liquid Bank Nifty futures, model 1 tick (Rs 0.05 price step, but ~1–2 index points effective); for options and illiquid stocks, model far more. A backtest that fills at the mid-price is fiction — you cross the spread every time.

**Discipline 1 — In-sample (IS) vs out-of-sample (OOS).** Split your history. Build and tune the strategy on the IS portion (say 2015–2021). Then run it *once*, untouched, on the OOS portion (2022–2026). If OOS performance collapses, you overfit. The cardinal rule: **you get to look at the OOS data once.** Every time you peek and re-tune, OOS becomes IS and its honesty is spent.

**Discipline 2 — Walk-forward.** More robust than a single split. Optimise on a rolling window (e.g. 2 years), trade the next 3 months with those frozen parameters, then roll the window forward and repeat. Stitching the out-of-sample 3-month blocks together gives a realistic picture of how re-optimisation would actually have performed. If the walk-forward equity curve is far worse than the fully-optimised one, your edge is mostly curve-fit.

## Worked example — a backtest that lied, then told the truth

You test the Chapter-2 Bank Nifty opening-range system on 2019–2023 5-min data using a simple repo backtester (the project's Nifty/Bank Nifty backtest script — feed it OHLCV, define entry/stop/target functions, get a trade log and equity curve).

**First run (naive):** 620 trades, 44% win, gross CAGR 41%, smooth curve. Looks fantastic. Then you audit:

- **Look-ahead:** entries were filled at the *close* of the breakout candle. Fixing to the *next* 5-min open costs ~2–3 points average per entry. Win rate drops to ~41%.
- **Costs (2026):** ~Rs 1,300 all-in per round-trip lot (STT futures ~0.05% sell + brokerage + 18% GST). On 620 trades that's ~Rs 8.1 lakh of costs. Average gross win was Rs 11,550 and average gross loss Rs 8,400 (from Ch. 2 numbers) — subtract ~Rs 1,300 from *every* trade and expectancy falls hard.
- **Slippage:** add 2 index points (Rs 70/lot) each side → another ~Rs 140/trade.

**Post-audit:** 41% win, avg win ~Rs 10,100 net, avg loss ~Rs 9,800 net. Expectancy = `0.41 × 10,100 − 0.59 × 9,800 = 4,141 − 5,782 = −Rs 1,641 per trade.` **The strategy is a net loser.** The naive 41% CAGR was pure look-ahead-plus-zero-cost fantasy. Only the honest backtest saved you Rs 5L+ of live-money tuition.

**The fix path:** widen the target (fewer, bigger wins to overcome fixed costs), add a volatility filter, and re-validate on walk-forward — *not* by tweaking until the same 2019–2023 curve looks pretty again.

## How pros do it / common mistakes

**How pros do it:**
- Assume the backtest is lying and try to break it before the market does.
- Reserve OOS data and touch it *once*; prefer walk-forward.
- Model the full 2026 cost stack + slippage on the *actual* instrument.
- Prefer robustness (works across parameter ranges and sub-periods) over a peak result.
- Sanity-check trade count: 30 trades prove nothing; ~200+ across varied regimes (2020 crash, 2021 bull, 2022 chop) is the minimum for belief.

**Common mistakes / red flags:**
- A backtest with **no losing months** — nothing real is that clean; you've overfit or leaked future data.
- Re-running until OOS looks good (you just converted OOS to IS).
- Filling at close, mid, or ignoring slippage.
- Testing on today's index members (survivorship).
- Optimising 8 parameters on 3 years of data — more knobs than data.
- Reporting gross returns and quietly hoping costs "won't be that bad." In 2026 India, costs are *exactly* that bad.

## Checklist / drill

**Backtest-integrity checklist:**
- [ ] Prices split/bonus-adjusted; point-in-time universe (no survivorship).
- [ ] Signals use only data available at decision time; fills at next-bar open.
- [ ] Full 2026 cost stack modelled (STT/brokerage/txn/SEBI/GST/stamp) + explicit slippage.
- [ ] History split into IS and OOS; OOS run exactly once.
- [ ] Walk-forward performed; parameters frozen per window.
- [ ] ≥ ~200 trades spanning bull, bear, and sideways regimes.
- [ ] Result robust to ±10–20% parameter changes.

**Drill:** Take any backtest you already believe in. Add Rs 1,300/round-trip cost + 2 points slippage and re-run. Then hide the last 18 months, re-tune on the rest, and run that hidden slice once. If either step turns green to red, you found the truth *before* the market charged you for it.
