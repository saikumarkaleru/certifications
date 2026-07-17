# Scalping & Intraday Timeframe Playbook

The intraday game is a different sport from swing trading, not a faster version of it. On a daily chart you have hours to think; on a 1-minute Bank Nifty options chart you have seconds, and the market will extract a full day's edge from you in a single careless afternoon. This playbook is about the *character* of the intraday timeframe in Indian markets — how the day is shaped, which setups actually pay, when to press and when to sit on your hands, and the ruthless risk discipline that separates the handful of profitable scalpers from the churning majority. It is India-first: Nifty and Bank Nifty on the NSE clock, real levels in rupees, and the option-chain reality that dominates modern intraday flow.

## The character of the intraday timeframe

Intraday trading lives on the 1-minute, 3-minute, 5-minute, and 15-minute charts, with the 15-minute providing structure and the 1-3 minute providing entry timing. The defining feature of this timeframe is **noise dominance**: on a daily chart, price movement is mostly signal (real supply/demand shifts); on a 1-minute chart, most bars are noise (spread, order-flow jitter, algo pinging). Your entire job as an intraday trader is to filter the few signal bars from the sea of noise, and to be flat before the noise costs you the signal's profit.

Three structural facts define the Indian intraday day:

**1. The day has a shape.** The NSE cash and F&O session runs 9:15 AM to 3:30 PM. That 375-minute window is not homogeneous — it has distinct personalities by clock:
- **9:15-9:45 (the open):** highest volatility, widest ranges, gap adjustments, overnight-news digestion. The most opportunity *and* the most traps. Amateurs get run over here; professionals often wait it out.
- **9:45-11:00 (the trend window):** the day's genuine directional move most often establishes here. If the day is going to trend, this is usually when it commits.
- **11:00-1:00 (the lunch lull):** volume drains, ranges compress, false breakouts multiply. The graveyard of intraday accounts — most money is lost buying/selling chop in this window. Best used for sitting flat or scalping a tight range with tiny size.
- **1:00-2:30 (the afternoon revival):** volume returns, European markets open (~1:30 PM IST), a second trend leg or a reversal of the morning move often develops.
- **2:30-3:30 (the closing hour):** position squaring, expiry-day fireworks, the sharpest option-premium moves. High opportunity, high risk; the last 15 minutes can be violent.

**2. Volatility clusters.** Big moves beget big moves and quiet begets quiet. The morning's range tells you the day's likely character. A wide, trending first hour signals a trend day worth pressing; a tight, overlapping first hour signals a range day where you fade extremes and never chase.

**3. Options premium is the real instrument.** Most Indian intraday volume is now in **Bank Nifty and Nifty weekly options**, not futures or cash. This changes everything: you are trading a *decaying, non-linear* instrument. An option's premium moves with the underlying (delta), but also bleeds with time (theta) and swells/shrinks with volatility (vega). An intraday options buyer is fighting theta all day; an options seller is collecting it but carries fat-tail gap risk. The scalper must read the *underlying's* chart (Bank Nifty spot/future) to time the option, because the option premium alone is too noisy and too corrupted by IV shifts to chart cleanly.

## Instrument selection & why Bank Nifty dominates

Bank Nifty is the intraday scalper's favourite for concrete reasons: it moves 300-600 points on an ordinary day and 800-1,500 on a volatile one, versus Nifty's tamer range; its weekly options are ultra-liquid with tight spreads; and its higher beta means an ATM option can double or halve in an hour. That same violence is why it destroys the undisciplined — the moves that make you also break you.

- **Bank Nifty options:** highest reward, highest risk, needs the tightest discipline. Fast theta on expiry day.
- **Nifty options:** calmer, tighter ranges, more forgiving for learning intraday structure. Better first instrument.
- **Fin Nifty:** thinner; its Tuesday expiry (subject to exchange scheduling) offers a dedicated expiry-scalp day but liquidity is lower.
- **Index futures:** linear (no theta/vega headache), best for pure price-action scalpers who want the chart to mean what it says. Larger margin, but no premium decay working against you.
- **Stock intraday:** reserve for names with genuine catalysts (results, news) and real volume — Reliance, HDFC Bank, and the day's high-volume movers. Illiquid stocks have killer spreads.

A practical rule: **learn structure on Nifty futures or Nifty options, then graduate to Bank Nifty once your risk discipline is proven.** Starting on Bank Nifty weekly options on expiry day is the most common way beginners blow up.

## Five intraday setups with exact rules

Each setup below states the trigger, stop, target, timeframe, and the regime in which it works. Do not run a range setup on a trend day or a trend setup on a range day — regime-matching is 80% of the edge.

### Setup 1 — Opening Range Breakout (ORB)

The classic. Mark the high and low of the first 15 minutes (9:15-9:30). A decisive break of that range signals the day's direction.

| Element | Rule |
|---|---|
| Trigger | 5-min close beyond the 9:15-9:30 high (long) or low (short), on volume above the opening bars |
| Stop | Opposite side of the opening range (or 0.4% of the underlying) |
| Target | 1× to 2× the opening-range height; trail with 20-EMA on 5-min |
| Timeframe | 5-min for the range, 1-min for entry |
| Regime | Trend day; skip on a flat/inside-day open |

*Worked example:* Bank Nifty opens, and 9:15-9:30 prints a range of 48,600-48,850 (250 pts). At 9:42 a 5-min candle closes at 48,910 on rising volume. Buy the 48,900 CE (or long the future). Stop if Bank Nifty falls back below 48,600 (range low). Target 1 = range height projected = 48,850 + 250 = 49,100; target 2 = 49,350. On the option, a 250-point Bank Nifty move can take an ATM CE from ₹180 to ₹320 — but manage it on the *underlying's* levels, not the premium's wiggles.

### Setup 2 — VWAP Reversion / Rejection

VWAP (volume-weighted average price) is the intraday fair-value line and the institutional benchmark. Price tends to revert to it in ranges and respect it as support/resistance in trends.

| Element | Rule |
|---|---|
| Trigger | In a range: price stretches ~0.5-0.7% from VWAP into a prior level, prints a reversal candle → fade back to VWAP. In a trend: price pulls back *to* VWAP and rejects → enter with the trend |
| Stop | Beyond the reversal candle / the stretch extreme (range) or below VWAP by a buffer (trend) |
| Target | VWAP (range fade) or the prior swing/1× risk (trend continuation) |
| Timeframe | 3-5 min |
| Regime | Range day for reversion; trend day for the pullback version |

*Worked example:* Nifty is ranging. VWAP sits at 24,180. Price pushes to 24,290 (a prior resistance, ~0.45% above VWAP) and prints a bearish engulfing 5-min candle. Short toward VWAP. Stop above 24,305. Target 24,190. Clean 90-point fade with a 25-point stop — 3.6R on a textbook range day.

### Setup 3 — Trend Pullback (20-EMA ride)

On a trend day, the 20-EMA on the 5-min chart is the trend's rail. Buy dips to it in an uptrend, sell rallies to it in a downtrend.

| Element | Rule |
|---|---|
| Trigger | Price in a clear 5-min uptrend (higher highs/lows, above VWAP) pulls back to the rising 20-EMA and prints a bullish reversal bar |
| Stop | Below the pullback low / below the 20-EMA by a buffer |
| Target | Prior high, then trail the 20-EMA; exit on a decisive EMA break |
| Timeframe | 5-min |
| Regime | Trend day only |

The discipline: only take pullbacks *with* the established trend, and only after the trend is confirmed (usually post-9:45). Every counter-trend "it's too far" fade on a trend day is a donation.

### Setup 4 — Range Fade (support/resistance scalp)

On a lunch-lull range day, the day builds a clear intraday box. Buy the floor, sell the ceiling, tiny size, quick exits.

| Element | Rule |
|---|---|
| Trigger | Third+ touch of a well-defined intraday support/resistance with a rejection candle |
| Stop | Just beyond the level (tight — 0.2-0.3%) |
| Target | The opposite side of the range, or half-range for a scalp |
| Timeframe | 3-5 min |
| Regime | Range/lunch-lull day; abandon instantly on a range-break with volume |

The killer here is the eventual breakout: after fading a range four times profitably, the fifth is the real break that gives it all back. **The moment a range boundary breaks on volume, stop fading — flip to the ORB/breakout playbook or stand aside.**

### Setup 5 — Expiry-Day Theta / Momentum Scalp

On weekly expiry (Nifty Thursday, Bank Nifty and others per the exchange calendar), ATM/OTM option theta accelerates violently into the close, and the underlying often pins toward max-pain.

| Element | Rule |
|---|---|
| Trigger (momentum) | Sharp directional 5-min break with volume before ~2 PM → buy ATM option for a fast delta scalp |
| Trigger (decay, advanced) | Range-bound underlying near max-pain → sell OTM premium, defined-risk only, exit before the close |
| Stop | Tight — expiry premium moves fast both ways; a fixed rupee stop per lot |
| Target | Quick — take the move and get out; theta punishes holding |
| Timeframe | 1-5 min |
| Regime | Expiry day only; know where max-pain and heavy OI walls sit |

*Worked example:* It's expiry Thursday. Nifty is pinned near 24,000 where the heaviest call and put OI sit (max-pain magnet). A 1:45 PM breakout closes above 24,050 on volume. Buy the 24,050 CE at ₹28; a 60-point pop takes it to ₹55 in fifteen minutes — book it. Do *not* hold hoping for more: past 3 PM, if the move stalls, that ₹55 becomes ₹15 as theta and IV crush collapse the premium. Expiry-day options buying is a smash-and-grab, not a hold.

## Confluence — stacking the odds

No single setup is enough; intraday edge comes from stacking confirmations so that when three align you press size and when they conflict you pass.
- **VWAP** — above = bullish bias, below = bearish. Trade longs above VWAP, shorts below; fade the far stretches.
- **Opening range & prior-day levels** — yesterday's high/low/close, today's opening range, and the prior swing points are the intraday skeleton. Reactions at these levels are your highest-quality signals.
- **Volume** — a breakout without a volume surge is a fake. Demand expansion on the trigger bar.
- **Option OI walls & max-pain** — heavy call OI above is resistance; heavy put OI below is support. A break *through* an OI wall with unwinding accelerates. Max-pain is the pin magnet, especially near expiry.
- **India VIX** — rising VIX means bigger ranges (favour momentum/breakout, widen stops); falling VIX means compression (favour range-fade, smaller targets).
- **Market breadth & heavyweights** — for index scalps, watch HDFC Bank/ICICI/SBI for Bank Nifty and Reliance/HDFC Bank for Nifty; the index can't trend if its heavyweights are dead.

When VWAP bias, an OI-wall break, and a volume surge all point the same way, that's a press-size trade. When VWAP says up but you're at a call wall on falling VIX, that's a pass.

## Risk management — the only thing that keeps you alive

Setups are commodities; survival is the edge. The intraday timeframe punishes leverage and emotion faster than any other.
- **Fixed rupee risk per trade:** risk a small, fixed amount (e.g. 0.5-1% of capital) per trade. Your stop distance sets your lot size, never the reverse.
- **Daily max loss (the circuit breaker):** set a hard rupee loss limit for the day — e.g. 3% of capital or three consecutive losers — and *stop trading* when hit. Log off. The single biggest destroyer of intraday accounts is revenge-trading a bad morning into a catastrophic afternoon.
- **Daily max trades:** cap the count. Overtrading in the lunch lull is death by a thousand cuts.
- **No averaging down:** adding to a losing intraday position is a swing-trader habit that kills scalpers. Your stop is your stop.
- **Time stops:** if a trade hasn't worked within a few bars, exit. Intraday trades should move quickly; dead trades bleed theta and tie up attention.
- **Flat by 3:20 unless deliberately carrying:** don't get caught in the closing-auction chaos by accident.
- **Match size to regime and clock:** biggest size in the 9:45-11:00 and 1:00-2:30 trend windows; smallest or zero in the lunch lull.

## Pitfalls

- **Trading the lunch lull like it's the open.** The 11-1 chop generates the most false signals and the most losses. Sit out or size down hard.
- **Chasing option premium instead of reading the underlying.** The premium is corrupted by theta and IV; chart the Bank Nifty/Nifty *spot or future* and use it to time the option.
- **Fighting theta as a buyer with no time stop.** Holding a losing long option "to recover" while decay eats it is the classic expiry-day account-killer.
- **Ignoring regime.** Running range fades on a trend day (getting steamrolled) or breakout chases on a range day (getting whipsawed) — the same setup that prints on the right day loses on the wrong one.
- **Over-leverage on Bank Nifty.** The lot notional is large and the moves are fast; two bad trades at oversized lots erase a week.
- **No daily loss limit.** Revenge trading after a red morning is how a small loss becomes a disaster.
- **Slippage and spread denial.** On thin instruments and fast markets your fill is worse than your signal; only trade liquid instruments and account for the spread in your R:R.

## Interview-ready summary

Intraday trading in India runs on the 9:15-3:30 NSE clock, which has a distinct **shape**: a volatile open (9:15-9:45), the main trend window (9:45-11:00), a treacherous lunch lull (11-1), an afternoon revival (1-2:30), and a fast close (2:30-3:30). The dominant instrument is **Bank Nifty and Nifty weekly options** — decaying, non-linear instruments that force you to read the *underlying's* chart to time the option, fighting theta as a buyer and fat-tail risk as a seller. The five workhorse setups are the **Opening Range Breakout** (trend days), **VWAP reversion/rejection**, the **20-EMA trend pullback** (trend days), the **range fade** (lunch-lull range days), and the **expiry-day theta/momentum scalp** — each valid only in its matching regime. Edge comes from stacking confluence: VWAP bias, opening range and prior-day levels, a volume surge, option OI walls and max-pain, and India VIX for range sizing. But the real survival edge is **risk discipline** — fixed rupee risk per trade, a hard daily max-loss circuit breaker, no averaging down, time stops, and matching size to the clock. The setups are commodities; the daily loss limit and regime-matching are what keep a scalper solvent.
