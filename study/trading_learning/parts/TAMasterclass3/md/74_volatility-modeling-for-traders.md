# Volatility Modeling for Traders

Direction is what beginners obsess over; volatility is what pays the professionals. A trader who is right about *where* Nifty is going but wrong about *how violently* it gets there will still blow up — stopped out by noise, or crushed selling options into an expansion. Volatility is the raw material of position sizing, of options pricing, of stop placement, and of regime detection. It is also, unlike price direction, genuinely *forecastable*: volatility clusters. Big days follow big days; calm follows calm. This chapter builds a working trader's toolkit for measuring and modeling volatility on Indian instruments — Nifty, Bank Nifty, individual NSE stocks, and MCX — moving from simple realised measures through EWMA and GARCH to the practical craft of trading the difference between implied and realised vol.

## What it is and the logic

Volatility is the *dispersion* of returns — how far, on average, an instrument moves around its mean, usually expressed as an annualised standard deviation in percent. When we say "Nifty vol is 12%," we mean its annualised standard deviation of returns is about 12%.

There are two fundamentally different things called "volatility," and confusing them is the classic rookie error:

- **Realised (historical) volatility (RV):** computed *backward* from actual price moves. It is a fact.
- **Implied volatility (IV):** extracted *forward* from options prices — the market's expectation of future volatility, embedded in premiums. It is an opinion. India VIX is the headline example: it is the 30-day forward implied vol of Nifty, derived from Nifty option prices.

The single most important empirical fact about volatility, and the reason it can be modeled at all, is **volatility clustering**: periods of high volatility persist, and so do periods of calm. A 3% down day in Nifty is very rarely followed by a placid 0.3% day; it is usually followed by more large days in both directions. This autocorrelation in the *magnitude* of returns (even though the *sign* of returns is nearly random) is what every volatility model is trying to capture. A second robust fact is the **leverage effect**: volatility rises more after down moves than after equal-sized up moves. Fear expands vol faster than greed. Indian equities show this strongly — India VIX spikes on selloffs, not on rallies of the same size.

## The methods and the maths

### 1. Close-to-close realised volatility

The simplest estimator. Take log returns r_t = ln(P_t / P_{t−1}) over the last n days, compute their standard deviation, and annualise:

> σ_daily = √[ (1/(n−1)) Σ(r_t − r̄)² ]
> σ_annual = σ_daily × √252

The √252 comes from there being ~252 trading days in an Indian year; volatility scales with the *square root* of time, not linearly. So a daily vol of 1% annualises to 1% × √252 ≈ 15.9%.

**Choosing n** is the usual trade-off: a 10-day window is reactive but jumpy; a 30-day window is the common default; a 252-day window gives a stable "background" vol. Close-to-close ignores intraday range entirely — a day that swung 3% but closed flat registers as zero, which badly understates true activity.

### 2. Range-based estimators (Parkinson, Garman-Klass)

Because a day's high-low range carries information the close throws away, range estimators are far more *efficient* (less noisy for the same number of days).

**Parkinson** uses only the high and low:

> σ²_P = (1 / (4 ln 2)) × [ln(H/L)]²

**Garman-Klass** adds open and close, and is roughly 8× more efficient than close-to-close:

> σ²_GK = 0.5·[ln(H/L)]² − (2ln2 − 1)·[ln(C/O)]²

For a trader eyeballing NSE daily bars, the practical takeaway is: **use the range, not just the close.** A single day's high-low on Bank Nifty tells you more about its current volatility than three closing prices.

### 3. EWMA (RiskMetrics)

Fixed windows have a nasty artefact: when a big day drops out of the window, vol jumps for no fresh reason ("ghosting"). The exponentially weighted moving average fixes this by weighting recent squared returns more and letting old ones fade smoothly:

> σ²_t = λ · σ²_{t−1} + (1 − λ) · r²_{t−1}

λ (the decay) is typically **0.94** for daily data (the RiskMetrics standard). Higher λ = smoother, slower; lower λ = twitchier. EWMA needs no window length — just one parameter — and it captures clustering because today's variance is anchored to yesterday's. It is the workhorse for practical intraday and swing risk.

### 4. GARCH(1,1)

EWMA has a flaw: it assumes volatility has no long-run anchor — its forecast for vol tomorrow equals vol today, forever. Reality is that volatility *mean-reverts*: after a VIX spike to 30, it drifts back toward its long-run average (~13–15 for Nifty). GARCH(1,1) adds exactly that:

> σ²_t = ω + α · r²_{t−1} + β · σ²_{t−1}

- **ω** sets the long-run variance: long-run σ² = ω / (1 − α − β).
- **α** = reaction to the latest shock (how much a big day today spikes vol).
- **β** = persistence (how long spikes linger).
- **α + β** = the persistence of volatility overall; for equity indices it is typically ~0.95–0.99, meaning shocks decay slowly.

EWMA is just GARCH with ω = 0 and α + β = 1 — a special case with no mean reversion. GARCH's superpower is a **term structure of volatility**: because it mean-reverts, it forecasts that if vol is currently *above* its long-run mean it will fall, and vice versa. That is directly tradeable against the options market. Variants worth knowing: **EGARCH** and **GJR-GARCH** add the leverage effect (asymmetry), so down moves raise the vol forecast more than up moves — realistic for Nifty.

## Worked India example (with a code snippet)

Imagine Bank Nifty over a recent stretch. On 17 July 2026 it sits near 56,500. Over the last 20 sessions daily log returns had a standard deviation of 0.95%, so:

> Realised σ_annual = 0.95% × √252 ≈ **15.1%**

Now suppose India VIX for Bank Nifty-equivalent options is quoting an implied vol of **19%**. The options market is pricing *more* future volatility than has recently occurred — an implied-realised **spread of ~4 points**. This is normal: implied usually trades above realised (the "variance risk premium" — option sellers demand a cushion). But when the gap gets *unusually* wide, it flags rich options; when implied dips *below* realised, options are cheap relative to actual movement.

A GARCH(1,1) fit on Nifty daily returns might yield ω = 0.000002, α = 0.09, β = 0.89. Then:

- Persistence α + β = 0.98 → shocks decay slowly.
- Long-run daily variance = ω / (1 − 0.98) = 0.0001 → daily σ = 1.0% → annualised ≈ **15.9%**.
- If today's vol is elevated at 22% annualised, GARCH forecasts a *decline* toward ~16% over the coming weeks — a mean-reversion signal.

A minimal Python sketch using the `arch` library:

```python
import numpy as np, yfinance as yf
from arch import arch_model

# Nifty daily closes -> log returns in %
px = yf.download("^NSEI", period="2y")["Close"].dropna()
ret = 100 * np.log(px / px.shift(1)).dropna()

# EWMA (lambda = 0.94)
lam = 0.94
var = ret.var()
ewma = []
for r in ret:
    var = lam * var + (1 - lam) * r**2
    ewma.append(np.sqrt(var * 252))   # annualised %

# GARCH(1,1)
model = arch_model(ret, vol="Garch", p=1, q=1, mean="Constant", dist="t")
res = model.fit(disp="off")
print(res.params)                     # omega, alpha[1], beta[1]
fc = res.forecast(horizon=10)         # 10-day-ahead variance path
print(np.sqrt(fc.variance.values[-1] * 252))
```

The output gives you a *forecast path* of volatility, not just a current reading — which is what you need to decide whether to sell or buy options into an event.

## How to use it in a trading workflow

**Position sizing (volatility targeting).** The most powerful use. Size each position so it contributes a fixed rupee risk regardless of how volatile the instrument is. If you risk ₹10,000 per trade and Bank Nifty's daily σ is 0.95% (≈ ₹537 per unit at 56,500), your stop and quantity flow from that. When vol doubles, you *halve* size to keep risk constant. This single rule prevents the classic mistake of taking the same lot size in a calm market and a violent one.

**Stop placement.** Set stops as a multiple of current volatility (e.g. ATR, the range-based cousin of σ), not as a fixed rupee amount. A ₹200 stop on Bank Nifty is generous in calm weeks and instant death in a VIX spike. Volatility-scaled stops adapt automatically.

**Options: trade the implied-realised spread.** This is where volatility modeling directly makes money. Forecast realised vol (GARCH/EWMA), compare to implied (IV / India VIX):
- IV >> forecast RV → options are rich → favour *selling* premium (short straddles/strangles, credit spreads), sized carefully.
- IV << forecast RV → options are cheap → favour *buying* premium (long straddles ahead of expected expansion).

**Event vol.** Around RBI policy, Union Budget, or big earnings, IV inflates ("vol ramp") then collapses after the event ("IV crush"). Modeling the *normal* level of RV lets you judge whether the event premium is fair or excessive. Selling the crush is a known edge — and a known way to blow up if the event surprises.

**Regime detection.** A rising EWMA/GARCH vol, especially with India VIX breaking above ~18–20, signals a shift from trend-following conditions to whipsaw/mean-reversion conditions. Many systematic traders scale gross exposure inversely to forecast vol: full size in calm regimes, reduced size when vol expands.

## Confluence

- **VIX + price structure:** A VIX spike into a support test that then *fails to make a new high* while price holds is a classic capitulation-reversal tell.
- **Vol + breadth:** Rising realised vol with collapsing breadth = genuine stress; rising vol with firm breadth = healthy volatility of an advancing market.
- **Term structure:** When near-term IV exceeds longer-dated IV (backwardation in the vol curve), the market is pricing acute short-term fear — often a mean-reversion buy signal for the underlying once it stabilises.
- **Bollinger Band width / ATR:** These are chart-native volatility readouts; a "squeeze" (multi-month low band width) precedes expansion — a setup that GARCH would also flag as compressed variance likely to mean-revert upward.

## Honest limitations

Volatility models forecast *magnitude*, never *direction* — GARCH will tell you a big move is coming, not which way. They are also fitted to the past and can be blindsided by genuine regime breaks: a model calibrated in a calm year will badly underestimate a crash's first day. **Fat tails** are real — actual return distributions have far more extreme moves than a normal distribution predicts, which is why a Student-t GARCH is preferred and why you should never treat a "3-sigma event" as once-a-decade; on NSE they arrive far more often. GARCH parameters are unstable across samples, so treat forecasts as ranges. Implied-realised spread trades carry a brutal asymmetry: selling rich vol collects small premiums repeatedly and then, occasionally, a gap move (a bad Budget, a global shock) hands back months of gains in one session — the "picking up pennies in front of a steamroller" risk. Model the vol, but size for the tail you didn't model.

## Interview-ready summary

Volatility is the annualised standard deviation of returns and, unlike direction, it is forecastable because it clusters and mean-reverts. Realised (historical) vol is measured backward — best via range estimators like Garman-Klass rather than close-to-close, or smoothed with EWMA (λ = 0.94) — while implied vol is the market's forward expectation embedded in option prices, headlined by India VIX. GARCH(1,1), σ²_t = ω + α·r²_{t−1} + β·σ²_{t−1}, adds mean reversion (EWMA is the special case with no long-run anchor), giving a forecast term structure that says elevated vol should fall and vice versa. Traders use these to size positions to constant rupee risk (halve size when vol doubles), set volatility-scaled stops, and above all to trade the implied-realised spread — sell rich options when IV far exceeds forecast RV, buy cheap ones when it doesn't — while remembering that vol models forecast magnitude not direction, that fat tails make extremes common, and that selling volatility is profitable until the one gap that isn't.
