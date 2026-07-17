# Mean-Reversion Statistics & Z-Score

Most retail traders trade momentum by instinct — they buy what is going up. Mean-reversion is the opposite temperament, and it is where statistics earns its keep. The idea is old and simple: a price series that has stretched unusually far from its own recent centre of gravity tends to snap back toward it. The hard part is defining "unusually far" with a number instead of a feeling. That number is the **z-score**, and in Indian markets — where Bank Nifty routinely over-extends intraday and index constituents oscillate around VWAP — a disciplined z-score framework turns a vague hunch ("this looks overdone") into a repeatable, risk-defined trade. This chapter builds the statistics from the ground up, applies it to Nifty and Bank Nifty with real rupee levels, and is honest about the two ways mean-reversion quietly kills accounts.

## What it is & the logic

A z-score measures how many standard deviations an observation sits away from the mean of its distribution. Formally, for a value `x` drawn from a series with mean `μ` and standard deviation `σ`:

```
z = (x − μ) / σ
```

If price is exactly at its mean, z = 0. If it is one standard deviation above, z = +1; two below, z = −2. Under a normal distribution, roughly 68% of observations fall within ±1σ, 95% within ±2σ, and 99.7% within ±3σ. So a reading of z = +2.5 is, statistically, a rare event — it should occur only about 0.6% of the time on one tail. A mean-reversion trader reasons: "This is a tail event; the base rate says it reverts; I will fade it."

The logic rests on a specific market-microstructure belief. Mean-reversion is not a law of physics — it is a consequence of **order-flow exhaustion**. When a stock rips 2.5σ above its 20-period mean in fifteen minutes, the buyers who were going to buy have largely bought. Liquidity providers, arbitrageurs, and options market-makers who are now short gamma begin to lean against the move. The absence of fresh marginal buyers, not some mystical gravity, is what pulls price back. This matters enormously, because it tells you *when the logic breaks*: during a genuine regime change — a Budget surprise, an RBI shock, an index rebalance, a large institutional program — fresh marginal flow keeps arriving, the exhaustion never happens, and the "cheap" 2σ deviation becomes a 4σ catastrophe. Mean-reversion works in **range/rotation regimes** and fails in **trend/news regimes**. Half of this chapter is really about telling those two states apart.

The centre of gravity (`μ`) can be many things, and the choice defines the strategy:

| Anchor for μ | What it captures | Typical India use |
|---|---|---|
| Rolling SMA (e.g. 20-bar) | Short-term fair value | Intraday index scalps |
| VWAP (session) | Volume-weighted fair value | Cash-equity & futures intraday |
| Anchored VWAP from event | Fair value since a catalyst | Post-results drift fade |
| Rolling mean of a spread | Relative value between two assets | Pairs (next chapter) |
| Bollinger middle band | SMA with a σ envelope | Retail-friendly visual z |

Bollinger Bands, which most readers already know, are literally a z-score chart in disguise: the bands are drawn at μ ± 2σ, so "price touching the upper band" *is* "z ≈ +2." What we add here is the discipline to compute z explicitly, condition it on regime, and size by it.

## Construction, rules & settings

### Rolling z-score, step by step

Choose a lookback window `N` (number of bars). For each new bar, using the last `N` closes:

1. Compute the rolling mean: `μ_t = (1/N) · Σ closes`.
2. Compute the rolling standard deviation `σ_t` (sample std, divide by N−1).
3. Compute `z_t = (close_t − μ_t) / σ_t`.

A worked Python snippet (pandas), the same code you would put behind a TradingView-style backtest:

```python
import pandas as pd

def rolling_z(close: pd.Series, n: int = 20) -> pd.Series:
    mu = close.rolling(n).mean()
    sd = close.rolling(n).std(ddof=1)
    return (close - mu) / sd

# entry/exit thresholds
z = rolling_z(df['close'], 20)
long_entry  = z < -2.0     # oversold
short_entry = z >  2.0     # overbought
exit_flat   = z.abs() < 0.3  # reverted to mean
```

### Settings and their trade-offs

| Parameter | Small value | Large value | India default |
|---|---|---|---|
| Lookback N | Twitchy, many signals, more noise | Sluggish, few signals, stale mean | 20 bars (intraday 5-min); 50–100 for daily swing |
| Entry z | 1.5 → frequent, lower edge/trade | 3.0 → rare, higher edge, may miss | ±2.0 to ±2.5 |
| Exit z | 0 → greedy full revert | ±1 → grabs partial, higher hit-rate | 0 to ±0.5 |
| Std type | ddof=1 sample | population | ddof=1 |

Two refinements every serious desk uses:

**1. Half-life sizing of N.** Instead of guessing N, estimate the mean-reversion speed. Fit an Ornstein–Uhlenbeck / AR(1) model to the series: regress the daily change `Δx_t` on the prior level `x_{t−1}`. The slope `−λ` gives a **half-life** of reversion `= ln(2) / λ`. If Bank Nifty's intraday deviation from VWAP has a half-life of ~22 minutes, then on a 5-minute chart your natural N is roughly 20–25 bars — the data, not a round number, chooses the window. If the half-life is negative or huge, the series is *trending*, and mean-reversion should not be traded at all.

**2. Robust z (median/MAD).** Standard deviation is itself blown up by the very outliers you are trying to trade, so a single gap can crush your σ estimate and hide subsequent signals. Use the **modified z-score**:

```
z_robust = 0.6745 · (x − median) / MAD
```

where MAD is the median absolute deviation. This is far more stable across Indian expiry-day gyrations and gap opens.

## Worked India example (levels & ₹)

Take **Bank Nifty on a 5-minute chart**, a normal rotational session (no RBI, no results-heavy day). Spot opens near 48,000. By 11:15 the index has run to 48,540 on a fast squeeze. We compute the rolling 20-bar z-score:

- 20-bar mean `μ` = 48,190
- 20-bar σ = 140 points
- Current close = 48,540
- `z = (48,540 − 48,190) / 140 = +2.5`

A +2.5σ intraday stretch with no news and declining up-tick volume is a textbook fade. But we do **not** short the index outright — a naked Bank Nifty future carries roughly ₹15/point, so a 150-point adverse spike is ₹2,250 per lot before you blink. Instead we structure it as an F&O trade suited to mean-reversion:

**Trade construction (fade the overbought spike):**

| Element | Level / choice | Rupee math |
|---|---|---|
| Signal | z = +2.5 at 48,540, no catalyst | — |
| Instrument | Sell 48,600 CE (slightly OTM), 1 lot = 15 | Premium received ≈ ₹190 → ₹2,850 |
| Target | Revert to μ ≈ 48,190 (z→0) | CE decays to ≈ ₹90 → book ₹1,500 |
| Stop | z pushes to +3.3 (≈ 48,650 close) i.e. σ-expansion / trend | Exit CE near ₹300 → −₹1,650 |
| Time stop | Half-life ≈ 20 min; if no revert in 45 min, flat | — |

Notice the stop is defined in **z-space** (a +3.3 reading), not just in points. The reason: if σ itself is expanding, the same point-move is a smaller z, meaning volatility is regime-shifting and the reversion thesis is dead. Exiting on z = +3.3 is exiting on "the statistics stopped being true," which is exactly the right trigger.

A cash-equity version: **HDFC Bank** trades at ₹1,700, session VWAP ₹1,684, 30-min σ ₹6.20. A push to ₹1,715 gives `z = (1,715 − 1,684)/6.2 = +5.0` — an extreme reading. Fade toward VWAP: short at ₹1,715, target ₹1,690 (₹25/share ≈ ₹13,750 on a 550-share lot equivalent), hard stop ₹1,723 (z ≈ +6.3). Note that a z of +5 in a liquid large-cap almost always means a block print or index-flow — check the tape before trusting the number.

## How to trade it (entry, stop, target, management)

**Entry.** Wait for z to *cross back* through your threshold rather than trading the instant it is breached. If z prints +2.6 and you short immediately, you are catching a falling knife in reverse — the move can extend to +3.5. The professional entry is: z exceeds +2.0, then the *next bar closes with z falling* (e.g. +2.6 → +2.1). You are now trading confirmed exhaustion, not hope. This single rule dramatically improves the hit-rate at the cost of a few points of edge.

**Stop.** Two layers. (a) A **z-stop**: exit if z expands by ~0.8–1.0σ beyond entry (2.5 → 3.4). (b) A **structure stop**: exit if price closes beyond the prior swing that defined the range. Whichever hits first. Never use a fixed rupee stop alone — mean-reversion stops must breathe with volatility.

**Target.** Default to z = 0 (the mean). Aggressive traders take partial at z = 0 and trail the rest for an overshoot to the opposite band, but overshoots are the exception; booking at the mean is where the base-rate edge lives. A useful rule: **target the mean, not the opposite extreme.** Expecting +2.5 to travel all the way to −2.5 is asking the market to hand you a full range rotation, which is greedy.

**Management & sizing by z.** Size the position *inversely* to how much risk the stop implies, and you can also scale in: a partial clip at z = 2.0, a second at z = 2.5, capping total risk. Because reversion trades have high hit-rates but small average wins, position sizing and cost control decide profitability more than signal quality.

## Confluence — what makes a z-signal trustworthy

A z-score in isolation is a blunt instrument. Stack it with:

- **VWAP & bands.** A z = −2 that coincides with the lower VWAP standard-deviation band and a prior-day value-area low is far stronger than a z = −2 in open air.
- **Market-profile / value area.** Reversion works inside balanced (bell-shaped) profiles; fade signals near value-area extremes, stand aside on trend-day profiles.
- **Breadth & OI.** For index fades, check advance/decline and futures OI. Rising price + falling OI = short-covering exhaustion (great to fade); rising price + rising OI = fresh longs (dangerous to fade).
- **RSI/CCI divergence.** A z-extreme with a momentum divergence (price higher, RSI lower) is the classic confluence — but remember RSI is itself a bounded oscillator that already encodes a form of mean-reversion, so treat it as confirmation, not a second independent vote.
- **Time of day.** In India, 09:15–09:45 and 14:45–15:15 carry the most trend risk (opening auction, closing/expiry flows). The clean reversion window is roughly 10:30–14:00.

## Backtest & edge notes with realistic costs

A mean-reversion z-strategy typically shows a **high win-rate (60–75%) but low reward-to-risk (0.6–0.9)**. That profile is brutally sensitive to costs. On Bank Nifty options, per-round-trip you pay brokerage, STT (on the sell side of options, ~0.1% of premium and 0.125% on exercised ITM), exchange charges, GST, and — most importantly — the **bid-ask spread and slippage**, which on fast reversion entries can be 2–5 points. A strategy that looks like it earns 8 points/trade gross can net 2 points after friction. Two disciplines protect the edge:

1. **Trade liquid instruments only** — Nifty, Bank Nifty, Fin Nifty, top-15 F&O stocks — where spreads are 1 tick.
2. **Backtest with realistic fills**: assume you get filled at the *worse* side of the bar, add fixed slippage, and subtract full charges. If the edge survives that, it is real. Also **walk-forward** it: fit N and thresholds on 2022–2023, test untouched on 2024–2025. A z-strategy that needs re-optimising every quarter is curve-fit noise.

## Pitfalls — the two ways this kills accounts

**1. Trading reversion in a trend (the fatal error).** The whole framework assumes stationarity — a stable mean to revert to. On a trend day, the mean itself is marching, so every "2σ overbought" fade adds to a losing short as the index grinds higher. This is why the ADF/stationarity tests in Chapter 69 are not academic decoration — they are the *filter that tells you whether z-scores are even meaningful today*. Rule: no reversion trades when the daily/hourly series fails a stationarity check or when price is trending cleanly above a rising 200-EMA on your operating timeframe.

**2. Naked selling without defined risk.** Reversion trades tempt you to sell options for premium and "wait it out." One 4σ event — a gap, an RBI intermeeting move, a global risk-off — and an undefined short pays for a year of small wins. Always define the loss: spreads over naked, z-stops always honoured, and hard position limits. Reversion strategies have a fat left tail; your job is to amputate it.

Other traps: (a) **σ instability** — recompute robustly (MAD) so one gap doesn't blind you; (b) **overfitting thresholds** — ±2.0 that mysteriously becomes ±2.37 after optimisation is fitted; (c) **survivorship in the mean** — an anchored VWAP from a stale event drifts meaningless; refresh anchors.

## Interview-ready summary

- **Z-score** = (price − rolling mean) / rolling std; it counts standard deviations from fair value. ±2σ ≈ a 5% tail event; that rarity is the tradable edge.
- Mean-reversion works because of **order-flow exhaustion in range regimes**, and *fails* in trend/news regimes when fresh marginal flow keeps arriving.
- Pick the lookback N from the **half-life** of an AR(1)/OU fit, not a round number; use **robust (median/MAD) z** to survive gaps.
- Trade the **cross-back** through the threshold, target the **mean (z=0)**, stop in **z-space** (σ expansion) not just rupees, and honour a **time stop** near the half-life.
- India specifics: Bank Nifty/Nifty 5-min, VWAP anchors, clean window ~10:30–14:00, use **defined-risk option spreads**, trade only liquid names, and net-of-cost the backtest brutally.
- The two killers are **fading a trend** and **naked undefined selling**; the stationarity tests of the next chapters are the mandatory pre-filter that keeps you honest.
