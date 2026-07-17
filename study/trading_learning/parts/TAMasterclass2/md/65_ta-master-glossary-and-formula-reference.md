# TA Master Glossary & Formula/Indicator Reference

This is the reference desk of the whole masterclass. Everywhere else in these two volumes you were reading a story — a pattern, a setup, a case study. Here you get the dictionary and the calculator side-by-side, so that when a term flashes past on a TradingView screen, a Chartink scan, an option-chain analytics page, or in a fast-moving trading-desk conversation, you know exactly what it means, how it is computed, what default settings the Indian market community actually uses, and what edge (if any) it carries.

The chapter is organised as a working reference, not as prose to read once. Skim it now to know what lives where; bookmark it and return whenever a word or formula is unclear. Levels quoted for Nifty (around 24,000–25,000), Bank Nifty (around 51,000–54,000), and stock examples are 2025-2026-realistic reconstructions — use them to calibrate the *shape* of a calculation, then read live values off your own charts.

A word of honesty before the definitions: none of these formulas are magic. Every indicator is a transformation of the same four numbers — open, high, low, close — plus volume. An oscillator cannot know the future; it only re-expresses the past in a way your eye reads faster. Treat the reference as vocabulary, and treat *price, level, and risk* as the grammar.

## How to read the formula notation

Throughout, `C` = close, `O` = open, `H` = high, `L` = low, `V` = volume of the current bar. A subscript denotes how many bars back: `C₁` is the previous close, `Cₙ` is `n` bars ago. `Σ` means sum over the lookback window. `n` is the period/length. "SMA(x, n)" is the simple moving average of series `x` over `n` bars; "EMA(x, n)" is the exponential version. The EMA smoothing constant is `k = 2 / (n + 1)`, and `EMAₜ = Cₜ·k + EMAₜ₋₁·(1 − k)`. "Prev" means the previous bar's value of that same indicator.

---

## Part A — Core price & structure vocabulary

**Bar / candle.** One unit of time rendered as O-H-L-C. On a 15-minute chart each candle is 15 minutes of trade. The *body* is O-to-C; the *wicks/shadows* are the extremes beyond the body.

**Trend.** A sequence of higher highs and higher lows (uptrend) or lower highs and lower lows (downtrend). The formal Dow definition; everything else is decoration.

**Swing high / swing low.** A local peak/trough with lower/higher bars on both sides (commonly a 3- or 5-bar fractal). The raw material of structure, Fibonacci anchors, and stop placement.

**Support / resistance.** A price zone where prior demand (support) or supply (resistance) reversed price. Zones, not lines — treat a 30–40 point band on Nifty, not a single tick.

**Breakout / breakdown.** Price closing beyond a defined level. "Close beyond" is the honest test; an intrabar poke that closes back inside is a *fakeout*.

**Retest.** Price returning to a broken level to confirm it now acts in the opposite role (old resistance becomes support). The retest entry is lower-risk than the breakout entry because the stop is tighter and the level is proven.

**Gap.** Open away from the prior close. In Indian equities gaps form overnight (no continuous session) and are common on Nifty/Bank Nifty at 9:15 after SGX Nifty / GIFT Nifty moves. Types: common, breakaway, runaway/measuring, exhaustion.

**Range / consolidation.** Sideways price between a floor and ceiling; ATR contracts. Precedes expansion (the coil).

**Pivot.** Both a swing point *and* a calculated level — see Pivot Points in Part C.

**VWAP anchor.** The volume-weighted average price; the intraday "fair value" line most institutional desks trade around (Part C).

**Liquidity.** Depth of resting orders. Nifty options and index futures are deep; many mid/small-cap stocks are thin after 3:00 PM and around results — slippage vocabulary matters as much as pattern vocabulary.

---

## Part B — Candlestick vocabulary (quick lookup)

Single-bar and multi-bar names you will see cited in scans and commentary. Full mechanics are in Volume I; this is the fast dictionary.

- **Doji** — O ≈ C; indecision. Variants: *dragonfly* (long lower wick), *gravestone* (long upper wick), *long-legged* (both wicks).
- **Hammer / Hanging Man** — small body, long lower wick ≥ 2× body, tiny upper wick. Bullish at support (hammer) / bearish warning at top (hanging man).
- **Shooting Star / Inverted Hammer** — mirror of the above with the long wick on top.
- **Marubozu** — full body, no wicks; one side dominated the whole bar. Strong momentum signature.
- **Engulfing (bull/bear)** — current body fully engulfs prior body. The single most-used 2-bar reversal.
- **Harami** — small body inside prior large body; momentum stalling.
- **Piercing / Dark Cloud Cover** — close pushes past the midpoint of the prior opposite candle.
- **Morning Star / Evening Star** — 3-bar reversal: big candle, small-bodied pause, big opposite candle.
- **Three White Soldiers / Three Black Crows** — three strong same-direction bodies; trend confirmation or exhaustion depending on context.
- **Tweezer top/bottom** — two bars sharing near-identical highs/lows.

Rule that overrides all names: a candlestick pattern only counts at a *level* and *with* a volume or OI story. A hammer in the middle of nowhere is noise.

---

## Part C — Indicator reference (formula, settings, use)

### Moving Averages

**SMA(n)** = `Σ(C over n) / n`. The plain average. Default long-term references in India: 20, 50, 100, 200. The 200-DMA on Nifty is the single most-watched line for "bull vs bear market."

**EMA(n)** = `Cₜ·k + EMAₜ₋₁·(1 − k)`, `k = 2/(n+1)`. Reacts faster than SMA. Popular sets: 9/21 EMA for intraday scalps on Bank Nifty; 20/50 EMA for swing.

**WMA / HMA.** Weighted MA front-loads recent bars. Hull MA (HMA) = `WMA(2·WMA(n/2) − WMA(n), √n)` — smooth and low-lag; used by momentum swing traders who want fewer whipsaws than EMA.

**Golden / Death Cross.** 50-DMA crossing above/below the 200-DMA. Slow, famous, and better as regime context than as a timing trigger.

**Worked use.** Nifty at 24,800 trading above a rising 20-EMA (≈24,600) and 50-EMA (≈24,300), with 200-DMA (≈23,400) below and rising = clean uptrend; buy dips to the 20-EMA, not breakouts into thin air.

### MACD

**Formula.** `MACD line = EMA(C,12) − EMA(C,26)`; `Signal = EMA(MACD,9)`; `Histogram = MACD − Signal`. Default (12,26,9).

**Reads.** Line crossing signal = momentum turn; histogram flipping sign = the same, one bar earlier; zero-line crosses = trend bias; *divergence* (price higher high, MACD lower high) = weakening thrust.

**Pitfall.** MACD is an unbounded trend-follower; it lags and whipsaws in ranges. Best paired with a level, not traded raw.

### RSI (Relative Strength Index)

**Formula.** `RS = avg gain / avg loss` over `n` (Wilder's smoothing); `RSI = 100 − 100/(1+RS)`. Default n = 14.

**Reads.** >70 overbought, <30 oversold — but in a strong Nifty uptrend RSI can sit at 65–80 for weeks; do not short strength on RSI alone. The higher-value signals are: *RSI divergence*, and the *range rule* (in bull regimes RSI holds 40–80, in bear regimes 20–60). Intraday scalpers drop to RSI(7) or RSI(9) for speed.

### Stochastic

**Formula.** `%K = 100·(C − Lₙ)/(Hₙ − Lₙ)`; `%D = SMA(%K, 3)`. Default (14,3,3); "full stochastic" adds a smoothing on %K.

**Use.** Range/mean-reversion oscillator; crossovers below 20 and above 80. Overused as a standalone; valuable as a *timing* filter inside a defined level.

### ADX / DMI

**Formula.** From +DI and −DI (directional movement) and ATR; `DX = 100·|+DI − −DI|/(+DI + −DI)`; `ADX = smoothed DX`. Default 14.

**The single most useful number for regime.** ADX < 20 = no trend (mean-reversion setups, avoid breakout systems). ADX 25–40 = trending (ride it, trail stops). ADX > 40 and turning = late/exhausting trend. +DI over −DI = up-bias. Bank Nifty trend days almost always show ADX rising through 25.

### Bollinger Bands

**Formula.** `Middle = SMA(C, 20)`; `Upper/Lower = Middle ± 2·σ(C, 20)`, where σ is the standard deviation of close over 20. Default (20, 2).

**Reads.** *Squeeze* (bands narrowing) = volatility contraction → expansion ahead; *band walk* (price hugging the upper band) = strong trend, not "overbought." %B = `(C − Lower)/(Upper − Lower)`. Bandwidth = `(Upper − Lower)/Middle`. The squeeze on daily Nifty before a big event (Budget, RBI, election result) is a classic coil.

### Keltner Channels

**Formula.** `Middle = EMA(C, 20)`; `Upper/Lower = Middle ± 2·ATR(10)`. ATR-based cousin of Bollinger. The **TTM squeeze** is defined as Bollinger Bands *inside* Keltner Channels — the tightest coils.

### ATR (Average True Range)

**Formula.** `TR = max(H−L, |H−C₁|, |L−C₁|)`; `ATR = Wilder-smoothed TR over n`, default 14. Pure volatility, no direction.

**The most under-used risk tool.** Size positions and set stops in ATR multiples. If Bank Nifty daily ATR ≈ 700 points, a 0.25×ATR intraday stop ≈ 175 points; a swing stop at 1.5×ATR ≈ 1,050 points. Two stocks with the same rupee price but different ATR need different position sizes for equal risk.

### Supertrend

**Formula.** `Basic upper = (H+L)/2 + m·ATR(n)`; `Basic lower = (H+L)/2 − m·ATR(n)`; the final band flips based on close. Default (10, 3) — period 10, multiplier 3. Intraday Bank Nifty crowds favour (10,2) or (7,2) for faster flips.

**Use.** A visual trailing-stop / trend filter that flips green↔red. Excellent as a *stay-in-the-trade* discipline; poor in chop (it flip-flops). Confluence with ADX filters out the chop flips.

### VWAP

**Formula.** `VWAP = Σ(typical price · V) / Σ V`, where typical price = `(H+L+C)/3`, summed from the session open (or from an *anchor* — anchored VWAP from a swing low, an event, or an earnings gap).

**Why it matters in India.** VWAP is the intraday institutional benchmark. Price above rising VWAP = intraday bulls in control; the *first pullback to VWAP* after a trend-day open is one of the highest-quality intraday longs on Nifty and Bank Nifty. Standard-deviation VWAP bands (±1σ, ±2σ) give mean-reversion targets.

### Pivot Points (floor pivots)

**Formula.** `P = (H+L+C)/3` (prior day). `R1 = 2P − L`, `S1 = 2P − H`, `R2 = P + (H − L)`, `S2 = P − (H − L)`, `R3 = H + 2(P − L)`, `S3 = L − 2(H − P)`. *Camarilla* and *Fibonacci pivots* are alternative weightings; CPR (Central Pivot Range) adds `BC = (H+L)/2` and `TC = 2P − BC` — a narrow CPR predicts a trend day, a wide CPR a range day. Hugely popular with Indian intraday traders.

### Fibonacci

**Retracement ratios.** 23.6%, 38.2%, 50% (not strictly Fib but used), 61.8% (the golden ratio), 78.6%. Drawn swing-low to swing-high (or reverse). The 61.8% and the 38.2–50% "golden pocket" are the most-watched pullback zones. **Extensions** for targets: 127.2%, 161.8%, 261.8%.

### Volume-family reference

- **OBV (On-Balance Volume)** = running total: `+V` if `C > C₁`, `−V` if `C < C₁`. Confirms/diverges from price via accumulation.
- **CMF (Chaikin Money Flow)** = `Σ(MFV) / Σ V` over n, where money-flow-volume `MFV = V·[(C−L) − (H−C)]/(H−L)`. Default 20. Above 0 = buying pressure.
- **MFI (Money Flow Index)** = RSI computed on `typical price · V` instead of price; default 14. A "volume-weighted RSI."
- **A/D Line (Accumulation/Distribution)** = running total of MFV. Trend of institutional participation.
- **Volume Profile / VPOC** = volume distributed by *price* rather than time; the **POC** (point of control) is the most-traded price, the **Value Area** the 70% band. India desks use it to find high-volume nodes (magnets) and low-volume nodes (fast-travel zones).

### Ichimoku Kinko Hyo (quick reference)

- **Tenkan-sen (9)** = `(H₉ + L₉)/2`
- **Kijun-sen (26)** = `(H₂₆ + L₂₆)/2`
- **Senkou A** = `(Tenkan + Kijun)/2`, plotted 26 ahead
- **Senkou B (52)** = `(H₅₂ + L₅₂)/2`, plotted 26 ahead
- **Chikou** = close plotted 26 behind
- The **Kumo (cloud)** between Senkou A and B is dynamic support/resistance; price above the cloud with a bullish twist is a full trend signal. Default (9,26,52).

### Other named oscillators (dictionary)

- **CCI (Commodity Channel Index)** = `(TP − SMA(TP,n)) / (0.015·mean deviation)`, default 20; ±100 thresholds.
- **Williams %R** = `−100·(Hₙ − C)/(Hₙ − Lₙ)`, default 14; inverted stochastic.
- **ROC / Momentum** = `100·(C − Cₙ)/Cₙ`; raw rate of change.
- **TRIX** = rate of change of a triple-smoothed EMA; slow, low-noise momentum.
- **Awesome Oscillator (AO)** = `SMA(median,5) − SMA(median,34)`, median = `(H+L)/2`.
- **Parabolic SAR** = accelerating stop-and-reverse dots; step 0.02, max 0.2. A trailing-stop tool.

---

## Part D — Chart patterns (dictionary with measured-move rules)

Each pattern's *measured move* is the projected target; treat it as a probability zone, not a promise.

**Reversal patterns**
- **Head & Shoulders / Inverse H&S** — three peaks, middle highest; neckline break. Target = neckline ± head-to-neckline height.
- **Double / Triple Top & Bottom** — equal peaks/troughs; break of the intervening pivot. Target = pattern height projected from the break.
- **Rounding Bottom / Cup & Handle** — long saucer plus a small pullback (handle). Target = cup depth from breakout.

**Continuation patterns**
- **Flag / Pennant** — sharp move (the pole), tight counter-trend consolidation, continuation. Target = pole height from breakout.
- **Triangles** — *ascending* (flat top, rising lows, bullish bias), *descending* (flat bottom, falling highs, bearish bias), *symmetrical* (neutral coil). Target = widest height projected from apex breakout.
- **Rectangle / Channel** — parallel range; trade edges or the breakout.
- **Wedge** — *rising wedge* (bearish, converging up-slopes), *falling wedge* (bullish). Counter-intuitive: they slope *against* their resolution.

**Bilateral / harmonic**
- **Broadening / Megaphone** — expanding volatility, higher highs and lower lows; hard to trade, favours the fade at extremes.
- **Harmonic patterns** — Gartley, Bat, Butterfly, Crab, Cypher — defined by specific Fibonacci ratios between legs XABCD, giving a "potential reversal zone." Precise and mechanical; low frequency.

---

## Part E — Options / OI vocabulary that meets TA

Because Indian retail trades heavily in Nifty/Bank Nifty/Fin Nifty options, TA is incomplete without option-chain language. These terms recur across the setup and case-study chapters.

- **OI (Open Interest)** — number of outstanding contracts. Rising OI + rising price = fresh longs (bullish build-up); rising OI + falling price = fresh shorts; falling OI = unwinding/covering. The four-quadrant read is a core confluence layer over any TA level.
- **PCR (Put-Call Ratio)** — `total put OI / total call OI`. High (>1.3) = heavy put writing / possible bullish contrarian; low (<0.7) = call-heavy. Sentiment gauge, best at extremes.
- **Max Pain** — the strike at which the largest number of options expire worthless; price is loosely "pulled" toward it into expiry. A magnet, not a law.
- **Support/Resistance from OI** — the strike with the highest put OI often acts as support; highest call OI as resistance. On expiry these can align with, or override, chart levels. Example: Nifty highest call OI at 25,000 and highest put OI at 24,500 frames the expected range.
- **IV / IV Rank / IV Percentile** — implied volatility and where it sits in its own range. High IV rank favours option *selling* strategies; low IV favours buying. IV crush after events (results, RBI, Budget) is a TA-adjacent risk every option buyer must respect.
- **Greeks (quick):** *Delta* (directional exposure / rough probability ITM), *Gamma* (rate of change of delta, spikes near-the-money on expiry), *Theta* (time decay, the option seller's income), *Vega* (sensitivity to IV). A charted breakout can be *right* and still lose money if theta/vega bleed it — the honest caveat behind every "buy the breakout call."
- **Option-chain confluence checklist:** does the chart level coincide with an OI wall? Is OI *building* in your direction on the move? Is IV about to be crushed by an event? Only then is the TA signal "option-clean."

---

## Part F — Risk, sizing & performance formulas (the honest part)

The indicators fill screens; these formulas keep accounts alive.

- **Risk per trade (₹)** = `Entry − Stop` (in points) × lot size × number of lots. Cap at **1–2% of capital** per trade. On a ₹5,00,000 account, 1% = ₹5,000 max risk.
- **Position sizing** = `Capital risk ₹ / (stop distance in points × point value)`. This is where ATR feeds directly into lots.
- **R-multiple** = `(Exit − Entry) / (Entry − Stop)`. Every trade measured in R makes strategies comparable across instruments. A +2R win and a −1R loss is the reference vocabulary of a trading journal.
- **Reward:Risk (RR)** = `(Target − Entry) / (Entry − Stop)`. Filter setups below ~1.5:1 unless win-rate is high.
- **Expectancy** = `(Win% × avg win) − (Loss% × avg loss)`, expressed in R = `Win%·avgR_win − Loss%·avgR_loss`. Positive expectancy is the *only* thing that matters over a sample; a 45%-win system at +2R/−1R is highly profitable.
- **Kelly fraction** = `W − (1−W)/RR`, where W = win probability. Full Kelly is too aggressive for discretionary trading; most professionals use *fractional* Kelly (¼–½) or simply cap at the 1–2% rule.
- **Maximum drawdown** — the largest peak-to-trough equity fall; the number that determines whether you can *stay* in the game psychologically.
- **Sharpe ratio** = `(return − risk-free) / σ of returns`; risk-adjusted performance. India risk-free ≈ the T-bill / repo rate, so a strategy's Sharpe must clear a ~6–7% hurdle before "outperformance" means anything.
- **Slippage & cost drag** — brokerage, STT (securities transaction tax, notably higher on the sell side and on option premium), exchange fees, GST, and stamp duty. Intraday-heavy option strategies can lose 15–30% of gross edge to costs; a formula-perfect backtest that ignores STT is a fiction.

---

## Part G — Regime & context vocabulary

- **Trending vs ranging** — decided by ADX and by structure (HH/HL vs overlapping bars). Match the tool to the regime: trend-followers (MA, Supertrend, MACD) in trends; oscillators (RSI, Stochastic, Bollinger fade) in ranges. Using a trend tool in a range, or vice versa, is the most common cause of a "the indicator failed" complaint.
- **Volatility regime** — measured by ATR and by India VIX. Rising VIX widens stops and shrinks size. Around 12–13 VIX markets grind; above 18–20 they whip; event days (RBI policy, Union Budget on Feb 1, quarterly results, US Fed, election results) spike it.
- **Session character (Indian equities, 9:15–15:30 IST)** — the *opening* 9:15–9:45 is volatile and driven by global cues (GIFT/SGX Nifty, US close, Asian markets); *mid-day* 11:00–13:30 often ranges and traps breakout traders; the *last hour* 14:30–15:30 sees genuine institutional positioning and the cleanest trends, especially on expiry Thursdays (weekly Nifty) and the monthly expiry.
- **Correlation** — Nifty and Bank Nifty are tightly linked but Bank Nifty is higher-beta; heavyweight moves (HDFC Bank, ICICI, Reliance, Infosys) drag the index. USDINR, crude, and US 10-year yields are the macro overlays. A "great chart setup" on a single stock can be overridden by an index or macro move.
- **Breadth** — advance/decline, % of stocks above 200-DMA, new highs vs new lows. Confirms whether an index move is broad or narrow-heavyweight-driven. A Nifty new high on weak breadth is a caution flag.

---

## Part H — Common myths, corrected (so the glossary tells the truth)

A reference that only defines terms would leave you over-confident. These corrections belong in the vocabulary itself:

1. **"Overbought means sell."** No — in a strong trend RSI stays overbought for weeks. Overbought means *momentum is strong*; it is a shorting signal only with divergence *and* a level *and* a regime that supports mean reversion.
2. **"Indicators predict."** They describe the past faster. Predictive value comes from *confluence at a level with a risk plan*, not from any single line crossing.
3. **"More indicators = more accuracy."** Correlated indicators (RSI, Stochastic, CCI, Williams %R are near-cousins) create false confidence. Pick one from each family: one trend, one momentum, one volatility, one volume — that is a complete, non-redundant dashboard.
4. **"The pattern guarantees the target."** Measured moves are probabilities. Roughly half of clean breakouts reach the full target; many stall at partial levels or fail entirely — which is exactly why the stop, not the target, defines the trade.
5. **"Backtest edge = live edge."** Costs (STT, slippage, brokerage), fills, and psychology erode it. An honest edge survives real Indian transaction costs and a losing streak.

---

## Interview-ready summary

If a desk asks you to *demonstrate command of technical analysis*, this is the compressed version of everything above:

- **Price and level first, indicators second.** Every indicator is a transform of O-H-L-C; none see the future. The edge is confluence at a proven level with a defined risk.
- **Know the four families and one tool from each:** trend (MA / Supertrend / MACD / ADX-for-regime), momentum (RSI / Stochastic — watch divergence, not just the 70/30 lines), volatility (ATR for sizing, Bollinger/Keltner for squeezes), volume (VWAP intraday, OBV/CMF/Volume-Profile for participation).
- **Formulas you can recite:** RSI = 100 − 100/(1+RS); MACD = EMA12 − EMA26, signal = EMA9; ATR = smoothed true range; VWAP = Σ(TP·V)/ΣV; Bollinger = SMA20 ± 2σ; Supertrend = HL2 ± multiplier·ATR; Pivot P = (H+L+C)/3.
- **Regime discipline:** ADX and India VIX tell you whether to trend-follow or fade; matching tool to regime is the biggest single skill.
- **Options literacy:** read OI build-up (four quadrants), PCR at extremes, max-pain magnet, highest-OI strikes as support/resistance, and respect IV crush and theta — a chart can be right and the option still lose.
- **Risk math above all:** 1–2% risk per trade, ATR-based sizing, think in R-multiples, demand positive expectancy = Win%·avgR_win − Loss%·avgR_loss, and subtract real STT/slippage before believing any edge.

Keep this chapter beside your charts. The rest of the masterclass teaches you to *see*; this one makes sure that when you name what you see, you name it exactly, compute it correctly, and price its risk honestly.
