# Custom Indicator Design Principles

Almost every technical indicator you use — RSI, MACD, Bollinger Bands, Supertrend — was once a *custom* indicator that one person built to answer one question. Welles Wilder built RSI because he wanted a bounded momentum measure that wouldn't run to infinity. John Bollinger wrapped a moving average in standard-deviation bands because a fixed-width channel ignored volatility. Once you internalise that indicators are just **question-answering machines built from price, volume, and time**, you stop being a passive consumer of TradingView's built-in list and start being able to design tools that fit *your* market, *your* timeframe, and *your* edge.

This chapter is a **method/design** chapter. It covers what an indicator actually is under the hood, the design principles that separate useful indicators from noise generators, the maths of the core building blocks, a worked India example where we design a custom volatility-normalised momentum oscillator on Nifty, how to code and test it in TradingView Pine, and an honest account of the traps — especially the biggest one, repainting and lookahead bias, that silently makes most homemade indicators worthless.

## What an indicator is & the logic

An indicator is a **transformation of the raw price/volume/time series into a new series** that is easier to read for one specific purpose. Everything you can build falls into a small number of transformation families:

| Family | Question it answers | Examples |
|---|---|---|
| Smoothers | "What is the underlying trend, stripped of noise?" | SMA, EMA, WMA, Hull, ALMA |
| Momentum / rate-of-change | "How fast is price moving, and is that speeding up or slowing?" | RSI, ROC, MACD, Stochastic |
| Volatility | "How much is price moving, regardless of direction?" | ATR, standard deviation, Bollinger width |
| Normalisers / oscillators | "Where is price *relative to* its own recent range?" | Stochastic, %B, z-score |
| Volume / flow | "Is there conviction behind the move?" | OBV, Force Index, CMF, VWAP |
| Composite / regime | "What environment are we in?" | ADX, Choppiness Index |

Good indicator design is mostly about **choosing the right family for your question and then normalising so the output is comparable across time and across instruments.** A raw momentum number of "+150 points" means one thing on Nifty at 24,000 and something entirely different on a ₹200 stock — so the first principle of design is almost always *normalisation.*

The second core idea: an indicator is a **filter** in the signal-processing sense. Smoothers are low-pass filters (they let the slow trend through, block fast noise). Momentum/difference operators are high-pass filters (they emphasise fast changes). Understanding this stops you making the classic beginner error of stacking three smoothed versions of the same thing and thinking you have three confirmations — you have one signal, filtered three times, with three times the lag.

## Design principles

### Principle 1 — Start from a question, not from a formula

Never begin with "let me combine RSI and ATR and see what happens." Begin with a sentence: *"I want to know when Bank Nifty momentum is strong relative to its own recent volatility, so a 200-point move in a calm week counts more than a 200-point move in an expiry-week storm."* That sentence dictates the maths: momentum in the numerator, volatility in the denominator. The formula falls out of the question.

### Principle 2 — Normalise so the output is bounded and comparable

An indicator you can't compare to its own history is useless. Two standard normalisation tools:

- **Range normalisation (Stochastic-style):** `(x − min) / (max − min)`, giving a 0–1 or 0–100 scale.
- **Z-score / standard-deviation normalisation:** `(x − mean) / std_dev`, giving units of "how many standard deviations from normal." A z-score of +2 means the same thing on Nifty, on Reliance, and on USDINR — that portability is gold.

### Principle 3 — Minimise lag, but respect the lag/smoothness trade-off

Every smoother trades **responsiveness against noise.** A 5-period EMA reacts fast but chops; a 50-period EMA is smooth but late. You cannot have both — this is not a limitation of any particular formula, it is a mathematical fact about causal filters. The art is choosing the *least* smoothing that still answers your question. Newer smoothers (Hull MA, ALMA, Jurik) reduce lag for a given smoothness by clever weighting, but they never eliminate the trade-off.

### Principle 4 — Prefer few free parameters

Every adjustable number (lookback length, threshold, smoothing factor) is a knob you can overfit. An indicator with one length parameter is robust; an indicator with six parameters can be tuned to look brilliant on any past chart and fail on the next one. Fewer knobs = more honest. (Chapter 26 is entirely about this danger.)

### Principle 5 — Causality: never use the future

An indicator must be computable using only data available *at the moment it prints.* This sounds obvious but is violated constantly (see repainting, below). If your calculation references `high` of a bar that hasn't closed, or centres a moving average (so it "sees" future bars), your backtest will look magical and your live trading will bleed.

### Principle 6 — Make it interpretable

If you can't explain in one sentence why the line goes up, you won't trust it at 9:20 a.m. when Bank Nifty gaps. Interpretability beats a marginally better backtest number, because you will actually *follow* an indicator you understand.

## The maths of the building blocks

A few formulas you will reuse endlessly.

**Simple Moving Average (SMA):**
```
SMA_n = (P_1 + P_2 + ... + P_n) / n
```

**Exponential Moving Average (EMA)** — weights recent data more, less lag:
```
α = 2 / (n + 1)
EMA_t = α · P_t + (1 − α) · EMA_(t−1)
```

**Average True Range (ATR)** — the workhorse volatility measure:
```
TR_t = max( High_t − Low_t,
            |High_t − Close_(t−1)|,
            |Low_t  − Close_(t−1)| )
ATR_n = EMA or RMA of TR over n periods
```

**Z-score** — normalisation to standard-deviation units:
```
z_t = (x_t − mean_n(x)) / stddev_n(x)
```

**Rate of Change (ROC)** — raw momentum:
```
ROC_n = (P_t − P_(t−n)) / P_(t−n) × 100
```

With just these five you can build a very large fraction of all useful indicators, including the custom one below.

## Worked India example — designing the "Volatility-Normalised Momentum" (VNM) oscillator

**The question:** *On Nifty and Bank Nifty, I want a momentum oscillator that automatically adjusts for volatility, so a strong reading in a quiet regime and a strong reading in a stormy regime are directly comparable — and I want it bounded so I can set fixed thresholds.*

**Design derivation:**
1. Momentum in the numerator → use ROC or the raw price change over `n` bars.
2. Volatility in the denominator → use ATR over the same `n`, so we measure momentum *in units of ATR.*
3. Normalise/bound → run a z-score, or squash with a fixed divisor, then clamp.

**The formula.** Let `n = 14`.
```
Raw_t   = Close_t − Close_(t−n)          # n-bar momentum, in points
VNM_t   = Raw_t / (ATR_14 × sqrt(n))     # momentum in volatility units
```
Dividing by `ATR × sqrt(n)` scales the n-bar move by the volatility we'd *expect* over n bars (volatility grows with the square root of time), so VNM is roughly dimensionless and stationary. Typical readings sit between −3 and +3.

**Interpretation & thresholds:**

| VNM reading | Meaning |
|---|---|
| > +2.0 | Strong up-momentum relative to current volatility — trend thrust |
| +0.5 to +2.0 | Healthy uptrend momentum |
| −0.5 to +0.5 | Neutral / range |
| −2.0 to −0.5 | Healthy downtrend momentum |
| < −2.0 | Strong down-thrust |

**Why this beats raw ROC on Indian indices:** In a calm January stretch Bank Nifty might move 300 points over 14 bars with ATR = 150; VNM = 300/(150·3.74) ≈ +0.53 — modest. During an expiry-week storm the *same* 300-point move with ATR = 500 gives VNM = 300/(500·3.74) ≈ +0.16 — correctly flagged as *unimpressive*, because in that volatility 300 points is noise. Raw ROC would score both moves identically and mislead you.

**Worked numbers on Nifty.** Suppose Nifty 14 bars ago closed at 23,700 and now closes at **24,180**. Raw = +480 points. ATR_14 = 180. `sqrt(14) ≈ 3.742`. VNM = 480 / (180 × 3.742) = 480 / 673.6 = **+0.71** — a healthy but not extreme uptrend reading. If instead ATR_14 were only 90 (very calm regime), VNM = 480/336.8 = **+1.43** — the same points move is now genuinely strong because volatility is low. The indicator is doing exactly the job we specified.

## Coding it in TradingView Pine (v5)

```pine
//@version=5
indicator("Volatility-Normalised Momentum (VNM)", overlay=false)

n   = input.int(14, "Lookback")
src = input.source(close, "Source")

raw   = src - src[n]                 // n-bar momentum in points
atrv  = ta.atr(n)                    // ATR over same window
vnm   = raw / (atrv * math.sqrt(n))  // volatility-normalised momentum

plot(vnm, "VNM", color=color.new(color.teal, 0), linewidth=2)
hline( 2.0, "Strong Up",   color=color.green)
hline( 0.5, "Up",          color=color.new(color.green, 60))
hline(-0.5, "Down",        color=color.new(color.red,   60))
hline(-2.0, "Strong Down", color=color.red)
hline( 0.0, "Zero",        color=color.gray)
```

Notes on this code that embody the design principles above:
- `src[n]` and `ta.atr(n)` use only **closed, past bars** — causal, no lookahead (Principle 5). On the live/forming bar Pine recomputes as the bar develops; to avoid an indicator that *repaints intrabar*, drive any alerts/signals off confirmed bars using `barstate.isconfirmed`.
- **One free parameter** (`n`) plus the source (Principle 4). Resist the urge to add separate lengths for momentum and ATR unless testing proves it necessary.
- The output is **bounded and interpretable** with fixed hlines (Principles 2 and 6).

## How to trade a custom indicator (workflow)

A custom indicator earns its place only inside a workflow:

1. **Define the signal precisely.** e.g. *"Go long when VNM crosses above +0.5 while the daily trend (50-EMA) is up; exit when VNM crosses below 0."*
2. **Add confluence, don't replace it.** VNM is a momentum filter — combine with the trend context (a 50/200 EMA regime) and with structure (support/resistance, prior swing). Momentum without trend context whipsaws.
3. **Forward-test on paper first.** A new indicator must survive out-of-sample bars you did not look at while designing it (Chapter 26 explains why).
4. **Define risk in the indicator's own terms where possible.** Because VNM is in ATR units, an ATR-based stop pairs naturally — e.g. stop at 1.5 × ATR below entry.

## Confluence

Custom indicators are strongest when each measures a *different* dimension. A robust homemade cockpit uses one from each family: a **trend** tool (EMA stack), a **momentum** tool (VNM), a **volatility** tool (ATR or Bollinger width to spot squeezes), and a **volume/flow** tool (VWAP or Force Index for intraday conviction). Because these are near-orthogonal, their agreement is real confirmation — unlike three smoothed momentum lines that always agree because they're the same information filtered three ways.

## Pitfalls

1. **Repainting / lookahead bias — the cardinal sin.** Any reference to a not-yet-closed bar, or use of `request.security` without proper `lookahead_off` and offset handling, makes the historical plot lie. The backtest is gorgeous; live trading is a graveyard. Always validate that your indicator computes identically on the last bar in real time as it does in history.
2. **Curve-fitting the parameters** to make one chart look perfect (whole of Chapter 26).
3. **Redundant inputs / false confluence.** Stacking correlated smoothers and calling their agreement "confirmation."
4. **Ignoring volatility regime.** A fixed-point threshold that works at Nifty 18,000 breaks at Nifty 26,000; always normalise (which is exactly what VNM does).
5. **Over-smoothing into uselessness.** Chasing a pretty, lag-free-looking line by piling on smoothing until the signal arrives after the move is over.
6. **Optimising the indicator, ignoring costs and slippage.** A signal that flips every few bars looks great in a frictionless backtest and dies on brokerage, STT and spread — especially in options.
7. **Not testing across instruments and regimes.** An indicator tuned only on 2023–24 Bank Nifty may fail on a range-bound Nifty year or on a stock; test across bull, bear, and sideways periods.

## Interview-ready summary

A custom indicator is a purpose-built transformation of price/volume/time that answers one specific question, drawn from a small set of families — smoothers (low-pass filters), momentum/rate-of-change (high-pass), volatility, normalisers, and volume/flow. Good design follows a discipline: **start from a one-sentence question, pick the matching family, normalise the output** (z-score or range-scaling) so it's bounded and comparable across time and instruments, **minimise lag while respecting the lag/smoothness trade-off, keep free parameters few**, and above all keep the calculation **causal** — never referencing future or unclosed bars, the root of repainting. Illustrated by building VNM, a volatility-normalised momentum oscillator = n-bar price change divided by (ATR × √n), which makes a 480-point Nifty move read as strong or weak depending on the prevailing volatility regime, coded in eight lines of Pine with a single lookback parameter. Custom indicators earn their keep only inside a workflow with trend context, confluence from orthogonal families, forward-testing, and honest accounting for costs — and the number-one way they secretly fail is repainting/lookahead bias.
