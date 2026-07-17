# Dominant-Cycle Detection & Cycle Tools

Markets do not move in straight lines. They breathe — expanding and contracting, rallying and pulling back — in rhythms that sometimes repeat with surprising regularity, and at other times dissolve into noise. The discipline of **cycle analysis** tries to isolate the dominant rhythm present in a price series *right now*, measure its length, and use it to anticipate the next high or low. This is a genuinely advanced corner of technical analysis. Done naively it becomes astrology-with-charts; done rigorously — with proper filtering, out-of-sample honesty, and confluence — it becomes one more probabilistic edge in the toolkit. This chapter treats it as the latter.

We will build up the logic, the maths (kept precise but usable), concrete India-first worked examples on Nifty and Bank Nifty, John Ehlers' modern cycle toolset (the workhorses that TradingView traders actually run), and a candid list of pitfalls.

## What it is & the logic

A **cycle** is a component of price movement that oscillates with an approximately fixed period — say, a 20-bar swing on a daily Nifty chart, meaning roughly 20 trading days from one significant low to the next. Real price is a *superposition* of several cycles of different lengths plus a trend plus random noise. Cycle analysis assumes that at any given moment one cycle carries most of the swing energy — the **dominant cycle** — and that if we can measure its current period, we can project the timing (not necessarily the price) of the next turning point.

Two ideas anchor the whole field:

1. **Time, not price.** A cycle tool primarily answers *when*, not *how far*. If the dominant cycle is 18 bars and the last swing low was 9 bars ago, the tool says "a swing high is due about now." Price targets still come from your other tools (Fibonacci extensions, measured moves, ATR bands).
2. **Cycles are non-stationary.** The dominant period on Nifty is not a fixed constant. It drifts — 16 bars this quarter, 22 bars next quarter — as volatility regimes change. So the useful tools *adapt*: they re-measure the period continuously rather than assuming a hardcoded number. This single insight separates the modern Ehlers school from the old fixed-length "this market has a 40-day cycle" folklore that repeatedly blew up.

The honest framing: cycles are strongest in **ranging or gently trending markets** and weakest in strong trends and event-driven gaps. The RBI policy shock, a US CPI print, a Budget-day gap — none of these respect your 18-bar rhythm. So cycle work is a *conditional* edge, switched on when the market is oscillating and switched off (or heavily de-weighted) when it is trending or gapping.

## Construction, rules & settings

### Detecting a period: three families of method

**(a) Visual / manual cycle lines.** The oldest method. You mark two adjacent significant lows, measure the bar-count between them, then step that same count forward repeatedly to project future low windows. Most charting platforms have a "Cycle Lines" drawing tool. Crude, subjective, but a legitimate starting point and still used by many discretionary traders for a first read.

**(b) Spectral methods (Fourier / DFT).** Decompose the series into sine waves of many frequencies and find which frequency has the largest amplitude (power). The **Discrete Fourier Transform** of a de-trended price series gives a power spectrum; the peak of that spectrum is the dominant frequency, and its reciprocal is the dominant period. Classic in theory but clumsy on markets: the DFT assumes a stationary signal over the whole window and has poor resolution on the short windows traders care about.

**(c) Adaptive / recursive filters (the Ehlers school).** John Ehlers, an engineer who brought DSP (digital signal processing) into trading, built estimators that update the dominant period bar-by-bar with far less lag than an FFT. The main ones — the **Homodyne Discriminator**, the **Dual Differentiator**, and the **Phase Accumulation** method — all try to measure the *instantaneous* period. These are what serious cycle traders run today, and TradingView's community library is full of Ehlers implementations.

### A precise but usable recipe: bandpass + measurement

Before you measure a cycle you must remove what is not a cycle: the slow trend and the fast noise. A **bandpass filter** does exactly this — it passes a band of periods (say 10–48 bars) and rejects everything shorter and longer. Ehlers' bandpass filter, in a form you can code in Pine Script or Python, is:

```
// Inputs: Period (center), Bandwidth (e.g. 0.3)
alpha  = ... (from bandwidth & period)
beta   = cos(2*pi / Period)
gamma  = 1 / cos(2*pi*Bandwidth / Period)
alpha  = gamma - sqrt(gamma*gamma - 1)

BP = 0.5*(1 - alpha)*(price - price[2])
   + beta*(1 + alpha)*BP[1]
   - alpha*BP[2]
```

The output `BP` is a clean oscillator centred on zero, containing mostly the cycle energy near the center period. Its zero-crossings correspond to cycle midpoints and its peaks/troughs to cycle extremes.

To *measure* the period rather than assume it, the **Homodyne Discriminator** takes the analytic signal (in-phase `I` and quadrature `Q` components, the quadrature being roughly the signal shifted 90 degrees), computes the phase from bar to bar, and infers the period from the rate of phase change:

```
Period = 360 / (phase_change_per_bar in degrees)
```

with heavy smoothing and clamping (typically clamp to 6–50 bars, and don't let the period change more than ~⅔ or +50% bar-to-bar). The clamping is not a cosmetic detail — it is what stops the estimator from chasing noise into absurd values.

### Settings that matter (and sane India defaults)

| Parameter | Typical range | India-first default | Note |
|---|---|---|---|
| Period clamp (min–max) | 6–50 bars | 8–40 (daily) | Nifty daily swing cycles cluster in the high-teens to ~40 days |
| Bandpass bandwidth | 0.1–0.5 | 0.3 | Lower = narrower/cleaner but laggier |
| Smoothing (pre-filter) | 2–6 bar | 4-bar Super Smoother | Removes intrabar noise before measurement |
| Timeframe | any | Daily for swing; 15-min for intraday index | Match cycle length to holding period |

**Rule of thumb for trading a measured cycle:** if the dominant period is `P`, expect a swing low roughly every `P` bars and a swing high roughly `P/2` bars after each low. Your "turn window" is not a single bar — give it `±15%` of `P` (so a 20-bar cycle → a ±3-bar window).

## Worked India example (levels & ₹)

Take **Nifty 50** on the daily chart across a hypothetical but realistic stretch. Suppose the Homodyne Discriminator, after smoothing and clamping, reports a **dominant period of ~20 trading days** — a very common reading for the index in a non-trending phase. Assume the following swing lows are visible: Nifty prints a low at **22,300** (call it bar 0), then a low near **22,750** at bar 20, and the estimator is still holding 20 as we approach bar 40.

Projection: the *next* cyclic low window is centred on **bar 40**, with a tolerance of about ±3 days (15% of 20). Between lows we expect a swing high near bar 30 — and indeed price tags **23,600** around bar 29 before rolling over.

Now we trade the *low* window, not blindly, but with confluence:

- **Time:** Bars 37–43 form the projected low window.
- **Bandpass oscillator:** the BP filter has crossed below zero and is curling up from a trough inside the window — a cycle bottom signal.
- **Price confluence:** 22,900 is the prior breakout shelf and the rising 50-DMA; the 61.8% retracement of the 22,750→23,600 leg sits at ~23,075. So a zone of **22,900–23,075** is the confluence band.
- **Entry:** On bar 41 Nifty dips to **22,950**, prints a bullish reversal candle, and the BP oscillator ticks up. Buy the index proxy (say a Nifty ETF, or express it in the futures / a bull call spread).
- **Stop:** Below the cycle-low window and structure — **22,760** (just under the last cyclic low). Risk ≈ 190 points.
- **Target:** The next cyclic *high* window is ~10 days out (P/2). Combine with a Fibonacci extension of the swing; project **23,700–23,850**. Reward ≈ 750–900 points → roughly **4:1** against 190 points of risk.
- **Management:** If price is not making progress by bar 46 (window + slack), the cycle has likely failed or lengthened — exit or tighten. Trail under swing lows as the up-leg develops.

For **Bank Nifty**, the same machinery runs faster and hotter. Bank Nifty's daily dominant cycle often measures shorter (frequently ~12–16 days) and its amplitude in points is far larger, so a measured 14-day cycle with the index near 50,000 might imply peak-to-trough swings of 1,500–2,500 points. Position sizing must respect that: the *same* cycle logic, but a wider stop in points and a smaller lot count so that rupee risk stays constant.

Intraday, drop to the **15-minute Bank Nifty** chart on an expiry-light day and the estimator might report a dominant period of ~26 bars (≈ 6.5 hours — essentially one-cycle-per-session). That is a common and tradeable intraday rhythm: a morning low, a midday high, an afternoon retest. But on trend days (a directional RBI or global open) the estimator's amplitude collapses and you should stand aside — which the tools themselves signal, as we will see.

## How to trade it (entry, stop, target, management)

1. **Confirm the market is cyclic before trading cycles.** Use an amplitude or "cycle strength" gauge (the magnitude of the bandpass output relative to price, or Ehlers' `Sinewave`/trend-mode flag). Low amplitude or a persistent trend flag = cycles off, don't trade timing.
2. **Trade *lows* in uptrends and *highs* in downtrends.** Align cycle timing with the higher-timeframe trend. Buying a projected cyclic low while the weekly trend is up is a high-quality setup; buying a cyclic low against a falling weekly trend is fighting the tape.
3. **Turn windows, not turn points.** Enter on a *confirmation* inside the window (reversal candle + oscillator curl), never on the calendar date alone.
4. **Stops go beyond the window.** If price keeps falling several bars past the projected low, the cycle has failed or the period has lengthened. That invalidation is precise and cheap.
5. **Targets from price tools, timing from cycle tools.** Project the opposite turn's *timing* from the cycle, but size the move with Fibonacci extensions, measured moves, or ATR.
6. **Right-translation is bullish.** In an uptrend, cyclic highs come *late* in the cycle (closer to the next low than the last low) — "right translation." In a downtrend, highs come early ("left translation"). The lean of the cycle is itself trend information.

## Ehlers' modern cycle toolset

A short field guide to the tools you will actually find and use:

- **Super Smoother filter:** a two-pole low-pass filter that removes noise with far less lag than an equivalent SMA/EMA. Use it as the pre-filter before any cycle measurement.
- **Bandpass filter (above):** isolates the cycle band; its output is the cleanest cycle oscillator available and its zero-crossings/extremes drive timing.
- **Homodyne Discriminator / Dual Differentiator:** the dominant-period *estimators*. Plot the measured period as a line — when it is stable and inside your clamp, cycles are reliable; when it slams into the clamp and stays there, the market is trending.
- **MESA / Autocorrelation Periodogram:** Ehlers' autocorrelation periodogram produces a heatmap of period vs. time — bright bands show which cycle length is dominant and when it shifts. This is the single most useful *diagnostic* display: you can literally watch Nifty's dominant period migrate from 18 to 30 bars over a quarter.
- **Sinewave Indicator / Cyber Cycle:** convert the measured cycle into lead/lag sine curves whose crossovers anticipate turns and, crucially, whose flatness flags "trend mode — no cycle."
- **MAMA/FAMA (MESA Adaptive Moving Average):** an adaptive MA whose speed is tied to the measured cycle phase; the MAMA/FAMA crossover is a lower-lag trend/cycle hybrid signal.

On TradingView, search the public library for "Ehlers" — implementations of every one of these exist in Pine Script and can be applied to Nifty, Bank Nifty, USDINR, or any MCX contract in seconds. Chartink is less suited (no bar-by-bar recursive filters), so cycle work lives on TradingView or in Python.

## Confluence

Cycle timing is at its best when stacked with independent tools:

- **Cycle low window + Fibonacci retracement + rising DMA** = the A-grade long, as in the worked Nifty example.
- **Cycle high window + bearish RSI divergence + prior supply zone** = high-quality short.
- **Cycle turn window + India VIX behaviour:** a cyclic low forming while India VIX spikes and then rolls over is a classic capitulation-then-relief setup on Nifty.
- **Cycle + OI / max pain (F&O):** if the projected cyclic low window coincides with the strike carrying heavy Put OI (a support shelf) near monthly expiry, the confluence of *time* (cycle), *price* (OI wall), and *event* (expiry pin) is strong.
- **Cycle + seasonality:** the next chapter's calendar effects. A cyclic low window that also lands in a historically strong seasonal window (say the pre-Budget or pre-Diwali drift) is doubly supported.

The rule: cycle timing *initiates* the idea; confluence *confirms* it; price tools *size* it. Never trade the clock alone.

## Pitfalls

- **Curve-fitting the period.** If you tune the lookback until past turns line up perfectly, you have fitted noise. The adaptive estimators exist precisely so you *stop* hand-picking a magic number. Always sanity-check on out-of-sample data.
- **Cycles in strong trends.** The number-one way to lose money here is buying "cyclic lows" all the way down a trend, or shorting "cyclic highs" up a runaway rally. Respect the trend-mode flag.
- **Event gaps.** Budget day, RBI policy, US CPI/FOMC, earnings, index-rebalance flows — these blow through any rhythm. Flatten or hedge cycle positions into scheduled events.
- **Over-precision.** Do not claim a turn "on Tuesday at bar 41." Use windows and confirmation. The tool gives a *neighbourhood*, not an appointment.
- **The 90-degree lag confusion.** The quadrature component inherently lags; treat every measured-turn signal as arriving *a bar or two late* and set entries/stops accordingly.
- **Period-halving/doubling artifacts.** Estimators sometimes lock onto a harmonic (half or double the true period). Cross-check the measured period against the visible swing count on the chart.
- **Sample size for validation.** A cycle "confirmed" over 20 bars is nothing. You want the pattern to persist across many cycles and multiple regimes before trusting it with size.
- **Backtest realism.** Include slippage, STT, brokerage, and the fact that many projected turns will be skipped in real time because confluence was absent. A cycle strategy that looks great ignoring costs and skips can be break-even after them.

## Interview-ready summary

Cycle analysis isolates the market's current dominant rhythm and uses it to anticipate the *timing* of the next turn — never the price, which comes from other tools. Because market cycles are non-stationary (the dominant period drifts with the volatility regime), the modern approach uses **adaptive DSP filters** — Ehlers' Super Smoother to de-noise, a **bandpass filter** to isolate the cycle band, and a **Homodyne Discriminator** to measure the instantaneous period bar-by-bar — rather than a hardcoded "40-day cycle." On **Nifty daily**, dominant periods commonly cluster in the high-teens-to-40-day range; **Bank Nifty** cycles run shorter and hotter. You trade *turn windows* (±15% of the period), enter only on confirmation inside the window with confluence (Fibonacci, DMA, OI walls, VIX, seasonality), take timing from the cycle but targets from price tools, and place stops just beyond the window so a failed cycle is cheap. The critical discipline is a **trend/cycle-mode filter**: cycles are a *conditional* edge that works in ranging markets and fails in strong trends and event gaps. Stated honestly, cycle work is real but modest — a probabilistic timing overlay, most powerful when it agrees with trend, structure, and the calendar, and dangerous the moment it is treated as a precise, standalone forecast.
