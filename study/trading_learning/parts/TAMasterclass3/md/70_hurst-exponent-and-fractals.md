# Hurst Exponent & Fractal Dimension

Most retail technical analysis silently assumes markets are either trending or ranging, and then argues endlessly about which one Nifty is doing "right now." The Hurst exponent turns that argument into a number. It is one of the few tools that actually measures **memory** in a price series — whether today's move makes tomorrow's move in the same direction more likely (persistence/trend), less likely (mean-reversion), or no more likely than a coin toss (random walk). Together with its cousin, the fractal dimension, it lets you classify a market's *character* before you decide whether to run a breakout system or a fade system on it. This chapter builds both from first principles, computes them on realistic Nifty and Bank Nifty data, and shows how to wire the result into a live TA workflow — honestly, including where the maths quietly lies to you.

## What it is and the logic

Harold Edwin Hurst was a British hydrologist who spent decades studying the Nile's flooding to size the Aswan dam reservoir. He needed to know how the range of water levels grew as he looked over longer and longer windows. If floods were independent year to year, the range should grow like the square root of time (√N). He found instead that it grew faster — roughly N^0.73. The Nile "remembered" wet and dry spells; good years clustered, bad years clustered. That exponent, later named after him, generalises to any time series, including price.

The core intuition is the **rescaled range**. Take a return series. Over a window of N bars, measure how far the cumulative path wanders (the range R) and divide by its standard deviation (S) to make it scale-free. For a pure random walk, R/S grows as N^0.5. If it grows faster, the series has positive autocorrelation across scales — trends persist. If slower, it snaps back — it mean-reverts.

The Hurst exponent **H** is that growth rate, and it lives on a clean 0-to-1 scale:

| H value | Behaviour | What it means for a trader |
|---|---|---|
| H = 0.5 | Random walk (Brownian) | No edge from direction memory; costs eat you |
| 0.5 < H < 1.0 | Persistent / trending | Momentum, breakouts, trend-following favoured |
| H → 1.0 | Strongly trending | Long smooth trends (rare in liquid equity indices) |
| 0 < H < 0.5 | Anti-persistent / mean-reverting | Fades, pairs, range/Bollinger reversion favoured |
| H → 0 | Extremely jagged | Every move reverses; scalp the noise |

The **fractal dimension D** is the same information wearing different clothes. A straight trending line is nearly 1-dimensional; a price scribble that fills a rectangle approaches dimension 2. Benoit Mandelbrot — who literally coined "fractal" and applied it to cotton and financial prices — showed the tidy relationship for these series:

**D = 2 − H**

So a trending market (H = 0.7) has low fractal dimension (D = 1.3): the line is relatively smooth and directional. A choppy mean-reverting market (H = 0.3) has high dimension (D = 1.7): the line is rough and space-filling. When you hear a quant say "the market got rougher," they mean D rose and H fell. This is the mathematical backbone behind Bill Williams' *Fractal* indicator and behind the "Fractal Dimension Index" (FDI) that some Indian TradingView traders overlay to gate their systems.

## Construction, rules and settings

There are three main estimators. Know all three, because they disagree and the disagreement is informative.

### 1. Classic Rescaled Range (R/S) analysis

For a price series, first convert to log returns r_t = ln(P_t / P_{t−1}). Then, for each window length n (say 10, 20, 40, 80, 160 bars):

1. Split the series into non-overlapping chunks of length n.
2. For each chunk: compute the mean m. Build the mean-adjusted cumulative deviate series Z_k = Σ_{i=1..k}(r_i − m).
3. Range **R** = max(Z) − min(Z) within the chunk.
4. Std dev **S** = standard deviation of the chunk's returns.
5. Rescaled range for the chunk = R/S. Average across all chunks of that n.
6. Repeat for every n.

Then regress **log(R/S) against log(n)**. The slope of that line is H. That's the whole trick — Hurst is a slope on a log-log plot.

| n (bars) | avg R/S | log₂(n) | log₂(R/S) |
|---|---|---|---|
| 10 | 3.0 | 3.32 | 1.58 |
| 20 | 4.6 | 4.32 | 2.20 |
| 40 | 7.4 | 5.32 | 2.89 |
| 80 | 11.9 | 6.32 | 3.57 |
| 160 | 19.0 | 7.32 | 4.25 |

Slope here ≈ (4.25 − 1.58) / (7.32 − 3.32) = 2.67 / 4.00 = **0.67** → a persistent, trending series.

### 2. Detrended Fluctuation Analysis (DFA)

R/S is biased on short, noisy, non-stationary series — exactly what intraday index data is. DFA is the robust upgrade and is what most serious desks actually run. Integrate the series into a cumulative "profile," slice it into windows, fit a local polynomial trend in each window, and measure the root-mean-square of the residual fluctuation F(n). Then F(n) ∝ n^α, and α is the DFA exponent, which maps to H (for stationary returns, α ≈ H). DFA's virtue is that it removes local trends before measuring roughness, so a drifting Nifty doesn't fool it into reporting false persistence.

### 3. The generalised/Anis-Lloyd corrected Hurst

Short samples make raw R/S over-estimate H — a genuinely random series can print H ≈ 0.55-0.60 just from small-sample bias. The Anis-Lloyd correction supplies the *expected* R/S under the null of randomness, and you measure your series' H **relative to that expected line**. This is critical: never compare your H to the theoretical 0.5, always compare it to the small-sample-adjusted expected value for your N. The Python `hurst` package does this for you.

### Settings that matter for Indian data

- **Series**: use log returns, not raw prices. Raw prices are non-stationary and inflate H toward 1.
- **Minimum length**: R/S wants ≥ 200 points; ≥ 500 for a stable read. On daily Nifty that's ~2 years; on 5-min Bank Nifty that's ~a week of sessions.
- **Rolling window**: for a *live* regime read, compute H on a rolling window (e.g. last 100 daily bars) and watch it evolve. A single static H over 10 years is almost useless because the regime changes.
- **Intraday caveat**: the first and last 15 minutes on the NSE carry auction/opening effects that spike volatility and distort short-window R/S. Trim them or expect noise.

## Worked India example (levels and ₹)

Take Nifty 50 daily closes across a stretch that included the strong 2023 grind higher and the choppier phases around it. Suppose we compute a **rolling 120-day Hurst (Anis-Lloyd corrected)**:

- During the steady advance from ~18,000 to ~22,000, rolling H sat around **0.62-0.68**. Fractal dimension D = 2 − 0.65 = **1.35**. Reading: persistent/trending. A pullback to the 20-DMA is a *buy the dip*, not a *fade the rally*, because memory is positive — up-days beget up-days.
- During a sideways box, say Nifty oscillating 24,500-25,500 for weeks, rolling H dropped to **0.42-0.46**, D ≈ **1.56**. Reading: mildly mean-reverting. Here a Bollinger-band fade or a sell-the-top/buy-the-bottom of the range has statistical wind at its back, and breakout buys will mostly bleed on false starts.

Now Bank Nifty intraday. Bank Nifty is structurally *jumpier* than Nifty — heavier weight in a few HDFC/ICICI/SBI/Kotak/Axis names, bigger gaps, more violent HDFC-Bank-earnings-day moves. On 5-minute bars, Bank Nifty's intraday Hurst frequently prints **0.40-0.48** — it is a mean-reverting, whippy instrument intraday, which is exactly why so many "buy the breakout" intraday BankNifty option-buyers get chopped, while VWAP-reversion and fade-the-spike scalpers survive. On daily bars over a trend leg, the same index can read H ≈ 0.60. **Same instrument, opposite character at different timeframes** — this is the single most useful thing Hurst teaches an Indian trader.

Put a rupee frame on it. Suppose you trade one Bank Nifty futures lot (lot size 35, so at 52,000 that is ~₹18.2 lakh notional, roughly ₹63,000 SPAN+exposure margin). If intraday H = 0.44, you know the tape favours reversion: your edge is selling into 150-point spikes above VWAP and covering at VWAP, with a hard 80-point stop, *not* chasing the spike. If your rolling daily H climbs above 0.60 during a trending week, you switch the same capital to holding a directional swing with a trailing stop, because now continuation is the higher-probability bet.

## How to trade it

Hurst is a **meta-indicator** — it tells you *which* toolbox to open, not the exact entry. The disciplined workflow:

**Entry / system selection.** Compute rolling H on your trading timeframe.
- H > 0.55 (with D < 1.45): enable trend systems — Donchian/breakout, moving-average pullback, Supertrend continuation, momentum. Disable fades.
- H < 0.45 (with D > 1.55): enable mean-reversion — Bollinger fade, RSI-2, VWAP reversion, range scalps. Disable breakout chasing.
- 0.45 ≤ H ≤ 0.55: **stand down or halve size.** This is the random-walk zone where costs and slippage dominate any signal. On the NSE, with STT, exchange fees, GST, stamp duty and the bid-ask, a coin-toss market is a guaranteed slow loss.

**Stop.** The stop logic itself should respect H. In a low-H (jagged) market use *tight* stops and take reversion profits fast — moves don't extend. In a high-H (smooth) market give the trade room and trail, because runs persist. Using a tight scalp stop in a trending H=0.7 tape gets you stopped out of the very move you correctly predicted.

**Target / management.** High H → let winners run, use trailing stops (chandelier, Supertrend). Low H → fixed targets at the opposite band/mean, because the move will snap back before it extends. This single adaptation — matching your exit discipline to the measured H — often does more for a P&L than the entry signal itself.

**Sizing.** Size up in the regime that matches your system; size down or flat in the neutral zone. Some desks scale position size linearly with |H − 0.5|: the further from randomness, the more the tape "means it."

## Confluence

Hurst is powerful precisely because it is orthogonal to price-pattern tools — it measures *texture*, not level or direction. Combine it with:

- **ADX / Choppiness Index.** ADX > 25 and H > 0.55 agreeing is a strong "trend confirmed, deploy breakouts" signal. When ADX and Hurst disagree, trust the neutral read and reduce risk.
- **India VIX.** Rising VIX often coincides with H dropping intraday (panic = whippy, mean-reverting chop). A VIX spike above ~18-20 with intraday H < 0.45 says "fade the extremes, don't chase."
- **Volatility regime / ATR.** Low-H markets in high ATR are the classic option-*seller's* paradise (Bank Nifty theta strategies); high-H markets favour option *buyers* riding directional persistence.
- **Timeframe stack.** Read H on daily *and* intraday. Daily H = 0.62 (trend) but intraday H = 0.44 (chop) is the textbook "trending market you must still enter on intraday reversion pullbacks" situation.

## Pitfalls

**H is not a crystal ball; it's a rear-view mirror.** It measures the *recent* character of the series over your window. Regimes flip — a breakout day can end a mean-reverting fortnight in an hour, and your rolling H won't confirm the flip until bars later. Never treat a stale H as a forecast.

**Small-sample bias is real and dangerous.** Compute H on 40 bars and a random series will happily hand you 0.6 and a false trend narrative. Always use the Anis-Lloyd correction and demand adequate length. If your window is short, distrust any H within ±0.1 of the expected value.

**Estimator disagreement.** R/S, DFA, and wavelet-based Hurst can differ by 0.05-0.10 on the same data. That's not a bug; it means the answer is genuinely uncertain near 0.5. Treat a single decimal as spurious precision. Report ranges, not points.

**Non-stationarity and structural breaks.** Corporate actions, index reconstitutions (Nifty rebalances), expiry-day mechanics, and news gaps all inject jumps that R/S misreads. DFA helps but doesn't cure it. Around Nifty/Bank Nifty monthly expiry, intraday Hurst readings are especially unreliable.

**The 0.5 boundary is fuzzy, not sharp.** Real liquid indices spend most of their life in a mushy 0.45-0.55 band. Don't over-trade tiny excursions. The tool earns its keep at the extremes.

**Overfitting the window.** If you tune the lookback until H "confirms" what you already wanted to do, you've built a horoscope, not an indicator. Fix the window by out-of-sample logic, not by hindsight.

## Worked estimation snippet

A compact, honest way to get H in a real workflow (Python, pandas + the `hurst` package which applies the small-sample correction):

```python
import numpy as np, pandas as pd
from hurst import compute_Hc   # pip install hurst

# nifty = daily close series (pandas Series)
prices = nifty.dropna().values
# rolling 120-day Hurst on log-price levels (compute_Hc handles the R/S internally)
window = 120
H_series = []
for i in range(window, len(prices)):
    seg = prices[i-window:i]
    H, c, data = compute_Hc(seg, kind='price', simplified=True)
    H_series.append(H)

H_now = H_series[-1]
D_now = 2 - H_now
regime = ("TREND" if H_now > 0.55 else
          "MEAN-REVERT" if H_now < 0.45 else "NEUTRAL/RANDOM")
print(f"Hurst={H_now:.2f}  FractalDim={D_now:.2f}  Regime={regime}")
```

Note `kind='price'` vs `kind='change'`: use `'price'` for a price level series (it differences internally) and `'change'` if you pass returns directly. Getting this wrong is the most common mistake and flips your read.

## Interview-ready summary

The **Hurst exponent H** measures long-memory in a price series via the growth rate of the rescaled range on a log-log plot: R/S ∝ N^H. **H = 0.5 is a random walk; H > 0.5 is persistent/trending; H < 0.5 is anti-persistent/mean-reverting.** The **fractal dimension D = 2 − H** says the same thing geometrically — trending markets are smooth (low D), choppy markets are rough (high D). Estimate it with rescaled-range analysis or, better, DFA, always with the Anis-Lloyd small-sample correction, on log returns over ≥ 200 bars, and read it *rolling* so you track regime change. In Indian markets the killer insight is timeframe-dependence: **Bank Nifty is often mean-reverting intraday (H ≈ 0.44) but trending on daily bars (H ≈ 0.60)** — so you fade intraday spikes yet swing-trade the daily trend. Use H as a meta-indicator that selects your toolbox (breakout vs fade), sizes your risk (stand down near 0.5), and tunes your exits (run winners when H is high, take quick reversion profits when H is low). Its honest limits: it is backward-looking, biased on short samples, estimator-dependent, and useless as a precise forecast — a compass for market character, not a map of the next tick.
