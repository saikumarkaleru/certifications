# Ultimate Oscillator & Awesome Oscillator

## What they are & why they work

Two oscillators, two very different philosophies, both aimed at the same weakness in ordinary momentum indicators — the tendency to give false divergence signals because they look at only one timeframe.

The **Ultimate Oscillator (UO)**, created by Larry Williams in 1976, was his answer to a specific frustration: a single-period oscillator like a fast stochastic or a short RSI generates divergence signals that reverse the moment the lookback window rolls forward. Williams' fix was to blend **three different timeframes into one bounded oscillator**, weighting the shortest most heavily. Because it triangulates short-, medium- and long-term momentum simultaneously, a UO divergence is far more robust than a single-period one — it will not flip just because a few candles aged out of the window. That multi-timeframe robustness is exactly why UO is prized for spotting genuine, tradeable divergences.

The **Awesome Oscillator (AO)**, created by Bill Williams (no relation to Larry), takes almost the opposite approach: radical simplicity. It is the difference between a 5-period and a 34-period simple moving average of the *median price* — nothing bounded, nothing weighted by anything exotic, just a fast average minus a slow average plotted as a coloured histogram around a zero line. AO is essentially a MACD computed on median price with SMAs instead of EMAs, and it works because it makes the single most important thing — **whether short-term momentum is above or below longer-term momentum, and whether that gap is widening or narrowing** — visible at a glance through its green/red bars.

Why do both belong in an Indian trader's toolkit? Because they solve different problems. UO is your **precision divergence instrument** for calling turns in Nifty, Bank Nifty and large caps around events and at range extremes — the moments where a well-timed reversal trade pays best. AO is your **momentum-and-continuation gauge**, brilliant for reading the *acceleration* of a Bank Nifty intraday trend and for two specific pattern-based entries (the Saucer and the Twin Peaks) that time pullbacks and reversals. One tells you *the turn is coming*; the other tells you *the move still has thrust*.

## Mechanics, formulas & settings

### Ultimate Oscillator

UO is built on the concept of **Buying Pressure (BP)** and **True Range (TR)** over three windows.

For each period:
- **Buying Pressure = Close − min(Low, prior Close)**
- **True Range = max(High, prior Close) − min(Low, prior Close)**

Then compute three averages of the ratio of summed BP to summed TR over the three lookbacks (Williams' defaults **7, 14, 28**):

- Avg7 = Σ(BP, 7) / Σ(TR, 7)
- Avg14 = Σ(BP, 14) / Σ(TR, 14)
- Avg28 = Σ(BP, 28) / Σ(TR, 28)

Finally, the weighted blend — the short window weighted 4×, the medium 2×, the long 1× — scaled to 0-100:

**UO = 100 × [ (4 × Avg7) + (2 × Avg14) + (1 × Avg28) ] / (4 + 2 + 1)**

The 4-2-1 weighting means the recent momentum dominates, but the medium and long windows anchor it so that divergences are stable. UO oscillates between 0 and 100; classic overbought is above 70, oversold below 30, though Williams' actual divergence rules (below) are stricter and more reliable than simple threshold trading.

**Settings:** the 7/14/28 default is excellent on the daily for Nifty and large caps. Intraday Bank Nifty traders sometimes compress to 5/10/20 on the 15-minute, but the classic settings are robust and I would not over-tinker.

### Awesome Oscillator

- **Median Price = (High + Low) / 2**
- **AO = SMA(Median Price, 5) − SMA(Median Price, 34)**

Plotted as a histogram: a bar is **green** if it is higher than the previous bar, **red** if lower — and this colour, not just the sign, is the heart of AO trading. Above zero means short-term momentum exceeds the longer-term baseline (bullish backdrop); below zero, bearish. AO has no fixed settings to fiddle with — 5 and 34 are canonical and part of Bill Williams' broader "Profitunity" trading system.

## Worked India example (levels & ₹)

**Ultimate Oscillator — a Nifty daily bullish divergence.** (Approximate reconstruction; verify on your chart.) Suppose Nifty sells off into a results-season scare from about 24,200 to 23,650, then after a weak bounce makes a *marginal new low* at 23,610. Price says "new low, downtrend intact." But the UO(7,14,28) which read about 22 at the first low now reads about 31 at the marginal new low — a **bullish divergence**. Williams' full rule requires three things for the buy: (1) a bullish divergence where the UO low stays above 30 on the second dip is not required, but crucially (2) the first UO low was below 30 (oversold), and (3) UO then rises *above the high it made between the two price lows*. When UO breaks that intervening peak — say it pushes above 45 — the buy triggers.

- **Entry:** 23,720 on the UO breakout above the intervening peak.
- **Stop:** below the marginal low, 23,590 — risk of 130 points.
- **Target:** the prior swing shelf around 24,200, then trail.

Nifty rallies to 24,280 over the following two weeks; from 23,720 to a trailed 24,180 exit is roughly 460 points of reward on 130 of risk — about 1:3.5. The strength of the UO version over a plain RSI divergence is that the multi-timeframe blend meant the signal did not evaporate on the choppy days between the two lows.

**Awesome Oscillator — a Bank Nifty intraday Saucer.** On a 15-minute Bank Nifty chart in an uptrending session (AO above zero), a mild pullback prints AO bars: two consecutive **red** bars (momentum cooling) followed by a **green** bar — all while AO stays above the zero line. That is the **Saucer buy**: it times a re-entry into the ongoing uptrend precisely when momentum stops decelerating and re-accelerates.

- Bank Nifty is at ₹51,000, AO above zero. The two red bars form as price dips to ₹50,880; the green bar prints as price ticks to ₹50,930.
- **Entry:** ₹50,940 on the green bar; **Stop:** ₹50,830 below the dip; **Target:** the session high ₹51,150 and trail. On one futures lot (15 units) a ₹210 favourable move is about ₹3,150 per lot before costs — a clean, repeatable intraday continuation trade.

## How to trade them — entry, stop, target

**Ultimate Oscillator setups**
- *UO divergence buy (Williams' rule):* bullish price/UO divergence where the first UO trough is below 30; enter when UO rises above the peak formed between the two price lows; stop below the price low; target prior resistance. The bearish mirror uses a UO trough/peak above 70.
- *Threshold reversal (simpler):* fade moves when UO crosses back below 70 (short-side warning) or back above 30 (long-side), best at established range boundaries with confluence.
- *Regime:* UO is a **counter-trend / turn-timing** tool — strongest at range extremes and late in trends. Do not fight strong trends with UO thresholds alone.

**Awesome Oscillator setups**
- *Zero-line cross:* AO crossing from below to above zero signals bullish momentum taking control (and vice-versa) — a trend-following entry, best filtered by higher-timeframe direction.
- *Saucer:* with AO on the same side of zero as the trend, two bars of counter-colour followed by a re-colour times the pullback re-entry (as in the Bank Nifty example above). A high-probability *continuation* signal.
- *Twin Peaks:* two peaks on the **same side of zero** where the second peak is lower (below zero, for a buy: two troughs, the second higher) with a colour flip between them — a reversal signal that works because it embeds a divergence within the histogram itself.
- *Regime:* AO is a **trend-and-momentum** tool; Saucer and zero-cross are pro-trend, Twin Peaks is the reversal exception.

For both, size positions so the stop (below/above the relevant swing) risks a fixed fraction of capital, and never take a fresh signal into a scheduled high-volatility event (RBI policy, Budget, big-cap results) without a hedge.

## Confluence (including OI)

- **UO + option chain:** a UO bullish divergence buy that lands at a Nifty strike defended by **heavy put writing** (a derivatives support floor, PCR turning up) is a top-tier long. A UO bearish divergence into a **call-writing wall** overhead is a top-tier short. Max Pain gives the gravitational context for expiry week.
- **AO + trend structure:** AO Saucers are only worth taking *in the direction of the higher-timeframe trend* — use the daily trend (or a 50-EMA on the 15-minute) as the filter for intraday Bank Nifty Saucers. AO zero-line crosses confirm breakouts of price ranges.
- **Cross-confirmation between the two:** a UO oversold divergence *and* an AO Twin Peaks bottom at the same price is a powerful combined reversal signal — one multi-timeframe momentum tool and one MA-difference tool agreeing.
- **Volume / delivery:** confirm AO breakouts with a volume expansion and, on stocks, a rising delivery percentage, to avoid hollow moves.
- **Support/resistance & Fibonacci:** signals landing at a prior swing, a round number (24,000; 51,000) or a 61.8% retracement carry more weight than signals in open space.

## Pitfalls

1. **Trading UO thresholds in strong trends.** Like all bounded oscillators, UO can sit "overbought" for a long time in a powerful Indian bull leg. Its threshold signals are for ranges and turns; use its stricter divergence rule and demand confluence before fading a trend.
2. **Ignoring the full UO divergence rule.** The naked "price up, UO down" divergence is weak; Williams' edge comes from the *complete* conditions (oversold first trough, then a break of the intervening peak). Skipping the confirmation break produces early, failing entries.
3. **AO's lag near turns.** AO is a difference of moving averages, so at genuine reversals it can be a beat late; the Twin Peaks pattern mitigates this but AO should not be the sole reversal trigger at a hard top or bottom.
4. **AO whipsaws in a range.** In sideways Nifty chop, AO oscillates around zero producing repeated false zero-crosses. Use AO for continuation only when a trend is clearly present.
5. **Both distort on gaps and expiry.** UO's True Range/Buying Pressure and AO's median price both jump on large overnight gaps (results) and on expiry-day volume mechanics. Read the first signal after such events cautiously.
6. **Over-optimisation.** The 7/14/28 (UO) and 5/34 (AO) defaults are well-chosen; changing them to make historical signals look perfect usually degrades live performance.
7. **Confusing their jobs.** UO is a turn-timer; AO is a thrust-gauge. Using AO to call major tops or UO to chase momentum inverts their strengths.

## Interview-ready summary

The Ultimate Oscillator and the Awesome Oscillator solve opposite problems with opposite philosophies. **Larry Williams' Ultimate Oscillator** blends three timeframes — Buying-Pressure-over-True-Range averages across 7, 14 and 28 periods, weighted 4-2-1 and scaled 0-100 — so that its divergence signals are robust and do not evaporate as a single-period window rolls forward; it is a **precision turn-timing tool**, best used with Williams' full divergence rule (oversold first trough, then a break of the intervening peak) at range extremes and late in trends. **Bill Williams' Awesome Oscillator** is deliberately simple — the 5-period minus 34-period SMA of median price, plotted as a green/red histogram around zero — and it is a **momentum-and-continuation gauge** whose colour-coded Saucer and Twin Peaks patterns and zero-line crosses time pullback re-entries and confirm thrust, mostly *with* the trend. In Indian markets UO excels at calling Nifty/Bank Nifty reversals around events and at support/resistance defended by option-chain put/call writing, while AO excels at reading the acceleration of Bank Nifty intraday trends. They are complementary: when UO's multi-timeframe divergence and AO's Twin Peaks agree at the same level, the reversal signal is strong. The common pitfalls — fading strong trends on thresholds, skipping UO's confirmation, trusting AO in a range, and distortion on gaps/expiry — are all managed by respecting each tool's job and demanding confluence. In one line: **the Ultimate Oscillator tells you the turn is real, the Awesome Oscillator tells you the move still has thrust — use each for the job it was built for.**
