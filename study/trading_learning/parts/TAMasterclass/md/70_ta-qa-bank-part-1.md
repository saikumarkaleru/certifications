# TA Question Bank Part 1 (Concepts & Indicators)

## What it is & why it works

This chapter is a structured question-and-answer drill covering the *conceptual foundations* of technical analysis and the *indicator toolkit* — the two areas that make up roughly half of any technical-and-derivatives research-analyst interview, and the half that separates a screen-watcher from someone who genuinely understands why price behaves the way it does.

The reason a question bank "works" as a learning tool is that recall under pressure is a different skill from recognition. You may nod along when you read that RSI is a bounded momentum oscillator, but an interviewer at a broking desk, a PMS, or a prop shop will ask *"RSI is at 78 on Reliance daily — are you short?"* and watch whether you reflexively say "yes, it's overbought" (the beginner trap) or "not on its own; in a strong uptrend RSI can stay above 70 for weeks — I'd want a bearish divergence plus a structure break first" (the professional answer). The market behaviour underneath every good answer is the same handful of truths: price is the net result of order flow; indicators are transformations of price and volume, so they *lag* and *repackage* information rather than create it; and every signal is a probability, not a promise. This bank trains you to answer from those truths rather than from memorised slogans.

The questions are written India-first — Nifty 50, Bank Nifty, Fin Nifty, real NSE names, rupee levels — because that is the vocabulary you will actually be tested in and trade in. Answers are graded in tone from "one-line crisp" to "full explanation" so you can see both what to say quickly and what to say when they push.

## The mechanics — how to use this bank

Each item follows a fixed shape: **Q** (the question as it is typically phrased), **A** (the answer a strong candidate gives), and where useful a **Why / trap** note that names the mistake weaker candidates make. Difficulty is tagged **[F]** foundational, **[I]** intermediate, **[A]** advanced.

| Tag | Level | What it tests |
|-----|-------|---------------|
| [F] | Foundational | Definitions, construction, default settings |
| [I] | Intermediate | Interpretation, context-dependence, combining |
| [A] | Advanced | Edge cases, failures, market-microstructure reasoning |

Work through it actively: cover the answer, say yours aloud, then compare. Track the ones you fumble and re-drill them. The India levels quoted assume a 2026 market where Nifty trades in a broad 23,000–27,000 zone and Bank Nifty around 50,000–58,000 — adjust the arithmetic, not the logic, if the market has moved.

### Block A — Dow Theory, trend & market structure

**Q1 [F]. State the six tenets of Dow Theory.**
A: (1) The averages discount everything; (2) the market has three trends — primary, secondary, minor; (3) the primary trend has three phases — accumulation, public participation, distribution; (4) the averages must confirm each other; (5) volume must confirm the trend; (6) a trend is assumed intact until a definitive reversal is signalled.
*Why it matters:* tenet 4 is the ancestor of modern index-vs-index confirmation — e.g., Nifty making a new high while Bank Nifty lags is a non-confirmation worth respecting.

**Q2 [F]. Define an uptrend in pure price-structure terms.**
A: A sequence of higher highs and higher lows. The trend is intact while each pullback low stays above the prior swing low; it is threatened when a higher-low fails and broken when a prior swing low is decisively taken out.

**Q3 [I]. Nifty rallies from 24,000 to 25,200, pulls back to 24,600, then to 24,900, then breaks below 24,600. What has changed structurally?**
A: The break of 24,600 (the prior higher-low) is the first lower-low — the first structural evidence that the uptrend's character has changed. It is not yet a confirmed downtrend, but it downgrades the trend from "buy dips" to "neutral / prove it". A confirmed reversal needs a subsequent lower-high followed by another lower-low.

**Q4 [I]. What is a "change of character" (CHoCH) versus a "break of structure" (BOS)?**
A: A BOS is continuation — price breaks the most recent swing point *in the direction of* the trend (new higher-high in an uptrend). A CHoCH is the first break *against* the trend — the first lower-low in an uptrend — signalling the trend may be ending. CHoCH warns; BOS confirms.

**Q5 [A]. Why can market structure look bullish on the daily and bearish on the 15-minute at the same time, and how do you resolve it?**
A: Because trend is timeframe-relative — a daily higher-low can be, inside it, a completed 15-minute downswing. Resolve by defining a *trading timeframe* and a *trend timeframe* (e.g., trade the 15-min, filter by the daily). You take longs on the trading timeframe only when the higher timeframe structure agrees; counter-trend trades are smaller and quicker.

### Block B — Support, resistance, and levels

**Q6 [F]. Why does support/resistance work at all?**
A: Memory of order flow. At a level where buyers previously overwhelmed sellers, resting bids, trapped shorts covering, and fresh buyers who "missed it last time" cluster — creating repeatable demand. It works because participants anchor to prices, not because the number is magic.

**Q7 [I]. What is polarity / role reversal?**
A: Broken resistance becomes support and vice versa. When Bank Nifty spends weeks capped at 54,000 then breaks above, the trapped sellers and breakout buyers turn 54,000 into a demand shelf on the retest. It is the single most tradable S/R concept because it gives a defined-risk re-entry.

**Q8 [I]. How do you rate the strength of a level?**
A: By (a) number of touches, (b) volume at those touches, (c) recency, (d) timeframe it is visible on, and (e) how far price travelled away and returned. A round number like Nifty 25,000 that has been tested four times on high volume across two months is far stronger than an intraday pivot from yesterday.

**Q9 [A]. Why do round numbers and prior all-time highs behave as levels even with no "structure" there?**
A: Behavioural clustering: stop and limit orders congregate at psychologically round figures (25,000, 50,000) and at obvious reference prices (previous ATH), and option strikes at those levels concentrate open interest and hence dealer hedging flow — so the level becomes self-fulfilling through order placement, not chart history.

### Block C — Moving averages

**Q10 [F]. SMA vs EMA — the difference and the trade-off.**
A: SMA weights all n periods equally; EMA weights recent prices more via a smoothing factor (2/(n+1)). EMA turns faster (less lag) but whipsaws more; SMA is smoother but slower. Trend-followers lean EMA for responsiveness; those wanting a stable "line in the sand" lean SMA.

**Q11 [F]. Which moving averages does the Indian institutional crowd actually watch?**
A: 20-EMA (short swing), 50-DMA (intermediate trend), 100-DMA, and 200-DMA (the long-term bull/bear line). The 200-DMA on Nifty is a genuinely watched level — funds reference "Nifty above/below its 200-day" as a regime marker.

**Q12 [I]. What is a golden cross and a death cross, and what is the honest expectation?**
A: Golden cross = 50-DMA crosses above 200-DMA; death cross = the reverse. They are *lagging regime signals*, not entries — by the time they print, a big move has often happened. Honest expectation: they filter regime well (keep you long in bulls, out in bears) but produce poor, late, whipsaw-prone entries in sideways markets.

**Q13 [I]. How would you use a moving average as a dynamic stop in a trending stock?**
A: In a clean uptrend, e.g., an FMCG leader riding its 20-EMA, trail the stop below the 20-EMA (or below the low of the candle that closes under it). It keeps you in as long as the trend's momentum holds and exits you when the slope flattens — accepting that you give back some of the top.

**Q14 [A]. Why does a moving-average crossover system underperform in Nifty during range years?**
A: Because MAs are trend tools and a range has no trend — price oscillates around the average, generating repeated crosses that each lose a little (buy high, sell low, repeat). The fix is a regime filter (e.g., ADX > 20/25, or price range width) that switches the system off when no trend exists. This is the core reason "one indicator, all markets" fails.

### Block D — Momentum oscillators (RSI, Stochastic, CCI)

**Q15 [F]. How is RSI constructed?**
A: RSI = 100 − 100/(1+RS), where RS = average gain / average loss over n periods (default 14). It is bounded 0–100. Conventionally >70 overbought, <30 oversold — but see the trap below.

**Q16 [I]. RSI is 78 on Reliance daily in a strong uptrend. Short?**
A: No. In strong trends RSI can remain overbought for extended stretches — "overbought" measures momentum strength, not an imminent reversal. I would only consider a short on a *bearish divergence* (price higher high, RSI lower high) confirmed by a break of market structure. Absent that, an overbought RSI in an uptrend is often a sign of strength, not a sell.

**Q17 [I]. Explain RSI divergence and give the two types.**
A: Divergence = price and oscillator disagree. *Regular bearish:* price makes a higher high, RSI a lower high → weakening momentum, possible top. *Regular bullish:* price a lower low, RSI a higher low → selling exhausting, possible bottom. *Hidden* divergences signal continuation instead (hidden bullish: price higher low, RSI lower low — trend likely resumes).

**Q18 [A]. Why is divergence a "warning" and not a "signal", and how do pros trade it?**
A: Because momentum can diverge for a long time before price actually turns — a divergence in a runaway trend can print three times and be wrong each time. Pros treat it as a *condition* that raises alertness, then require a *trigger* (structure break, trendline break, a reversal candle at resistance) before acting, with the stop beyond the extreme.

**Q19 [I]. Stochastic vs RSI — when do you prefer each?**
A: RSI measures the magnitude of recent gains vs losses; Stochastic measures where the close sits within the recent high–low range. Stochastic is more sensitive and better in *ranges* (fast %K/%D crosses at band edges); RSI is steadier and better for *trend and divergence*. In a choppy Nifty range I lean Stochastic; for trend momentum and divergences, RSI.

**Q20 [F]. What is the centreline (50) significance on RSI?**
A: The 50 line is the momentum midpoint. Bulls tend to defend RSI above 40–50; bears cap it below 50–60. Using RSI-50 as a trend filter (long only when RSI > 50) is often more robust than the 30/70 extremes.

### Block E — MACD

**Q21 [F]. Define MACD's three components.**
A: MACD line = 12-EMA − 26-EMA; Signal line = 9-EMA of the MACD line; Histogram = MACD − Signal. Defaults are 12/26/9.

**Q22 [I]. What do a zero-line cross and a signal-line cross each tell you?**
A: MACD crossing the *zero line* means the 12-EMA crossed the 26-EMA — a trend/regime shift. MACD crossing the *signal line* is a faster momentum trigger within the trend. Zero-line = slower, more reliable direction; signal-line = quicker, noisier entries.

**Q23 [I]. Why is the histogram the leading part of MACD?**
A: The histogram measures the *gap* between MACD and signal — its shrinking is the earliest hint that momentum is decelerating, often before the lines actually cross. A rising histogram with a shrinking topmost bar warns that an up-move is losing thrust.

**Q24 [A]. MACD is a lagging indicator built from EMAs — so how can traders claim it "leads"? Reconcile.**
A: The *lines* lag (they are EMAs of price). What can lead is the *rate of change of the histogram* and *MACD divergence versus price* — both are second-order signals about momentum, which peaks before price. So MACD lags price levels but its momentum-of-momentum can front-run turning points. Claiming MACD "leads price" outright is wrong; claiming its histogram slope leads price momentum is defensible.

### Block F — Volatility & bands (Bollinger, ATR, Keltner)

**Q25 [F]. How are Bollinger Bands built?**
A: Middle band = 20-SMA; upper/lower = middle ± 2 standard deviations of the last 20 closes. The bands widen with volatility and contract when it falls.

**Q26 [I]. What is a Bollinger "squeeze" and why do traders watch it?**
A: A squeeze is an unusually narrow band width — low volatility, coiling. Because volatility is mean-reverting and cyclical, extended low volatility tends to precede an expansion (a big directional move). The squeeze doesn't give direction, only "a move is likely soon" — you pair it with structure/breakout logic for the direction.

**Q27 [I]. "Price tagging the upper band is a sell." True?**
A: False as stated. In a strong trend price "walks the band" — repeatedly closing near the upper band is a sign of strength, not a reversal. The band edge is a *statistical envelope*, not a S/R level; mean-reversion at the band only works in ranges, confirmed by a failure to make progress.

**Q28 [F]. What is ATR and one core use?**
A: Average True Range — the average of the True Range (the greatest of high−low, |high−prev close|, |low−prev close|) over n periods (default 14). Core use: sizing stops to volatility, e.g., stop at 1.5×ATR below entry, so the stop adapts to how much the instrument actually moves.

**Q29 [A]. Two stocks, same ₹500 price. Stock A has ATR ₹6, Stock B ATR ₹22. How does this change position sizing for a fixed ₹5,000 risk?**
A: Stop distance scales with ATR. If both use a 1.5×ATR stop: A's stop ≈ ₹9 → size ≈ 5,000/9 ≈ 555 shares; B's stop ≈ ₹33 → size ≈ 5,000/33 ≈ 151 shares. Same rupee risk, very different share counts — ATR-based sizing equalises risk across instruments of different volatility, which is exactly why desks use it rather than a fixed percentage stop.

### Block G — Volume & volume-based tools

**Q30 [F]. State the basic volume-confirms-trend principle.**
A: Healthy trends show expanding volume in the direction of the trend and contracting volume on counter-trend pullbacks. A breakout on rising volume is more trustworthy than one on thin volume; a rally on shrinking volume warns of exhaustion.

**Q31 [I]. What is VWAP and why do institutions care intraday?**
A: Volume-Weighted Average Price — cumulative (price×volume)/cumulative volume from the session open. It is the day's "fair value" benchmark; execution desks are measured against it. Price above VWAP = buyers in control intraday; institutions defend VWAP as a mean-reversion and add-on reference. It resets daily, so it's an intraday tool.

**Q32 [I]. What does OBV (On-Balance Volume) attempt, and its main flaw?**
A: OBV adds the day's volume when price closes up and subtracts it when price closes down, building a cumulative line meant to reveal accumulation/distribution before price. Its flaw: it treats a +0.1% and a +5% close identically (it only uses the sign), so it's a crude proxy — divergence between OBV and price is its most useful read.

**Q33 [A]. Volume on NSE cash is only part of the picture in 2026 — why, and what do you add?**
A: Because a large share of activity is in F&O and index derivatives, and cash volume misses hedging and delivery nuance. Add: *delivery percentage* (high delivery on an up-move = genuine accumulation vs intraday churn), and *futures/options OI* to see where positional money is building. Cash volume alone can under-read institutional positioning that shows up in OI.

### Block H — Ichimoku, ADX, and trend-strength tools

**Q34 [F]. Name Ichimoku's five lines.**
A: Tenkan-sen (9), Kijun-sen (26), Senkou Span A and Senkou Span B (which form the Kumo/cloud, plotted 26 ahead), and Chikou Span (close plotted 26 back).

**Q35 [I]. Give a one-line Ichimoku regime read.**
A: Price above the cloud = bullish regime; below = bearish; inside = no-trade / transition. Bullish confirmation stacks: price above cloud, Tenkan above Kijun, Chikou above price, and a green (Span A > Span B) forward cloud.

**Q36 [I]. What does ADX measure and how do you read its level (not direction)?**
A: ADX (Average Directional Index) measures *trend strength*, not direction. Rough map: <20 no/weak trend (range), 20–25 trend emerging, >25 trending, >40 strong trend. Direction comes from +DI vs −DI. Key discipline: use ADX to decide *whether* to use trend tools at all.

**Q37 [A]. ADX is rising from 15 to 30 while price chops sideways. Contradiction?**
A: Not necessarily — ADX rises when directional movement (DI spread) increases, and it can begin rising at the *start* of a breakout before the trend is visually obvious, or during a volatile range with wide swings. It lags and is smoothed. The resolution: pair rising ADX with the DI cross and price structure; rising ADX + fresh BOS = a real trend starting.

### Block I — Regime, correlation, and cross-market

**Q38 [I]. Why must a Nifty technician watch Bank Nifty and vice versa?**
A: Financials are the heaviest sector weight; Bank Nifty leads and confirms broad-market moves. A Nifty breakout that Bank Nifty refuses to confirm (Dow's confirmation tenet, modernised) is suspect. Divergence between the two is an early warning of a fragile move.

**Q39 [I]. What is India VIX and how does a technician use it?**
A: India VIX is the market's expected 30-day Nifty volatility from option prices. Technically it's a *contrarian sentiment gauge*: spikes (high fear) often mark capitulation lows; complacent lows can precede volatility expansion. It also sizes expectations — high VIX means wider stops and bigger ranges are normal.

**Q40 [A]. How does DXY / USDINR feed into an Indian equity technical view?**
A: A sharply rising DXY / weakening rupee is typically an FII-outflow signal and a headwind for Nifty, especially rate-sensitive and import-heavy sectors; a stable/weakening DXY is supportive. A technician uses it as a *confluence filter* — a bullish Nifty setup is higher-probability when USDINR isn't breaking out against the rupee simultaneously.

## Reading it — a worked drill on one chart

Take Bank Nifty, daily, over an eight-week stretch in 2026. Base at 51,000, it rallies to 55,500, pulls back to 53,200 (a higher-low), then to 54,000. Now apply the bank as a live reading:

**Phase 1 — structure (Q2–Q4):** Higher highs (55,500) and higher lows (53,200 above the 51,000 base) = confirmed uptrend. Character is "buy dips".

**Phase 2 — moving averages (Q11, Q13):** Price rides above a rising 20-EMA (~53,600) and well above the 50-DMA (~52,400). The trailing-stop logic: as long as daily closes hold the 20-EMA, the trend is intact.

**Phase 3 — momentum (Q16–Q18):** At the 55,500 high, RSI printed 74. On the retest attempt toward a new high, suppose price reaches 55,400 but RSI only makes 66 — a *regular bearish divergence*. Per Q18 this is a warning, not a signal.

**Phase 4 — volatility & volume (Q26, Q30):** Band width has narrowed into the 54,000–55,500 zone (a squeeze), and the last push to 55,400 came on lighter volume than the first (55,500) push — momentum and participation both thinning.

**Phase 5 — verdict:** Structure is still up, but three tools (divergence, volume contraction, squeeze) say the *next* move is likely to be volatile and the up-leg is tired. The professional read: stay long with the stop trailed to the 20-EMA / below 53,200, but don't add here, and be ready for either a squeeze-release breakout above 55,500 or a structure break below 53,200.

## Trading it — turning answers into a decision

The bank is only useful if it changes what you *do*. From the drill above:

- **If** Bank Nifty closes above 55,500 on expanding volume (squeeze resolves up, divergence negated): continuation long, stop below the breakout candle low (~54,900), measured target = squeeze range (55,500−54,000 = 1,500) projected → ~57,000.
- **If** it closes below 53,200 (structure break / CHoCH from Q4): the uptrend character breaks; exit longs, and a fresh short can be considered on a lower-high retest toward 54,000 with stop above 55,500, targeting the 51,000 base.
- **Management:** either way, the divergence (Q17) told you to tighten, not to reverse blindly. You never short a strong trend on RSI alone (Q16) — you wait for the level (53,200) to break.

## Confluence — stacking the answers

The single most repeated lesson across this bank: no indicator trades alone. The high-probability version of the drill stacks four *independent* families — structure (Block A), a level (Block B), momentum divergence (Block D), and volume/volatility (Blocks F–G) — plus a cross-market check (Block I: is Bank Nifty confirming Nifty, is India VIX complacent, is USDINR quiet?). When three-plus independent tools agree, the setup graduates from "a chart pattern" to "a research call". Add the option-chain read (covered in Part 2): a bearish divergence at 55,500 is far more actionable if 55,000-strike shows heavy call OI acting as a ceiling.

## Pitfalls & false signals

- **Overbought = sell** (Q16) — the most common beginner error; kills you in trends.
- **One indicator, all regimes** (Q14, Q36) — MA crossovers in ranges, mean-reversion at Bollinger bands in trends. Always regime-filter with ADX or structure.
- **Treating divergence as a trigger** (Q18) — it's a condition; wait for the break.
- **Reading cash volume in isolation** (Q33) — miss the OI story.
- **Ignoring index confirmation** (Q38) — a Nifty move Bank Nifty won't confirm is fragile.
- **Curve-fitting settings** — 14, 20, 50, 200 are standard because they're widely watched; exotic optimised parameters usually overfit past data.

## Interview-ready summary

Indicators are transformations of price and volume — they lag and repackage, they don't predict. Trend and structure come first (higher-highs/lows, BOS vs CHoCH), then a level, then momentum (RSI/MACD, with divergence as a *warning* not a signal), then volatility and volume for confirmation (ATR for stops, squeeze for timing, VWAP/OBV for participation), then regime and cross-market filters (ADX for whether-to-trend, Bank Nifty confirmation, India VIX, USDINR). The professional habit is to answer every "is X a buy/sell?" with "in what regime, confirmed by what, with the stop where?" — because in technical analysis the honest unit of an answer is a probability with a defined risk, never a certainty.
