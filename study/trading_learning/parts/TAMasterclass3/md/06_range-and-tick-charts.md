# Range Bars & Tick Charts

## What they are and the logic

Time-based charts — the 5-minute, the daily — carry a hidden assumption that most traders never question: that *every equal slice of clock time deserves equal space on the chart*. But markets do not deliver information at a constant rate. The first fifteen minutes after the NSE opens at 9:15, the moments around 3:20 pm when index option gamma peaks on expiry, an RBI policy release, a US CPI print landing at 6:00 pm IST — these carry a hundred times the tradeable information of a dead 1:30 pm lull. A time chart draws the dead lull and the frantic open at exactly the same width, spreading the important activity thin and inflating the noise. Range bars and tick charts fix this by throwing away the clock and letting *market activity itself* decide when a new bar is born.

**Range bars** print a new bar every time price travels a fixed distance. Set a Bank Nifty range bar to 50 points and a new bar appears each time price moves 50 points, no matter whether that takes four seconds or forty minutes. Every bar has *identical height* by construction — that is the defining property. A quiet market produces very few, very slow range bars; a fast market fires them off in rapid succession. The chart literally speeds up when the market speeds up and goes silent when the market sleeps.

**Tick charts** print a new bar every time a fixed number of *transactions* (ticks — individual trades, not price changes) have occurred. A 500-tick Nifty futures chart prints a new bar every 500 trades. Here the constant is *activity/participation*, not distance or time. When many traders are transacting — the open, a news spike — ticks accumulate fast and bars print quickly; in a lull, a single bar may take many minutes to fill. Tick charts are, in effect, a crude volume/activity clock.

The shared philosophy: both replace *time* as the x-axis constant with something that actually correlates with opportunity — distance moved (range) or number of trades (tick). The payoff is a chart where each bar carries roughly equal *information*, noise is compressed, and genuine momentum bursts become visually and mechanically obvious. These are intraday tools above all — the natural habitat of the Bank Nifty and Nifty futures scalper and the active MCX crude/gold trader.

## Construction, rules and settings

**Range bars — exact rules.** A range bar of size R is built tick by tick:

| Step | Rule |
|------|------|
| Open | New bar opens at the price where the previous bar closed. |
| Fill | Bar extends as price moves; its high−low is capped at R. |
| Close & new bar | The instant price moves R from the bar's open, the bar closes and a new bar opens at that closing price. |
| Direction | An up range bar closes at its high; a down range bar closes at its low (each bar is one-directional by construction). |

Key consequences: **every range bar has the same range R** (that's the point), bars have **no wicks** in the classic construction (price that reverses inside the bar doesn't create a tail — it just delays the close), and range bars **cannot gap intrabar** except across the overnight/session break. Because each bar is a fixed price distance, a run of same-colour range bars is an unambiguous, quantified momentum burst.

**Tick bars — exact rules.** A tick bar of size N:

| Step | Rule |
|------|------|
| Count | Increment a counter on every executed trade. |
| Close | When the counter hits N trades, close the bar and reset the counter. |
| OHLC | The bar's open/high/low/close are taken from those N trades. |

Tick bars *do* have variable range and can have wicks — they are ordinary OHLC bars whose only unusual feature is that they contain a fixed trade-count instead of a fixed time-slice. A 500-tick bar in a violent market may span 40 points; in a calm one, 6 points.

**Settings for 2026 Indian instruments** (indicative — always calibrate to current volatility with ATR):

| Instrument | Range bar size | Tick bar size | Use |
|------------|----------------|---------------|-----|
| Nifty futures | 15–25 pts | 300–500 ticks | Intraday momentum/scalp |
| Bank Nifty futures | 40–60 pts | 500–1000 ticks | Fast scalping |
| Fin Nifty | 25–40 pts | 300–500 ticks | Intraday swings |
| Reliance / large-cap | ₹4–8 | 200–400 ticks | Active intraday |
| MCX Crude | ₹15–25 | 300–500 ticks | Fast commodity scalp |
| MCX Gold | ₹80–150 | 300–500 ticks | Intraday trend |
| USDINR fut | 3–5 paise | 200–400 ticks | Low-vol, tighten |

Two calibration principles. For **range bars**, size R as a fraction of the instrument's ATR — roughly ATR(14, daily) ÷ 40 to 60 gives a usable intraday bar. Too small and you drown in bars and costs; too large and you lose the intraday granularity that justified leaving time charts. For **tick bars**, pick N so that a typical active-session bar prints every 30–90 seconds; then you get several bars per swing without micro-noise.

A critical data caveat for India: **tick charts are only as good as your data feed's definition of a "tick".** NSE disseminates data in snapshots, and many retail feeds (and TradingView's India data) do not deliver every individual trade — they deliver aggregated updates. A "tick" on such a feed may actually be a price-change or a snapshot, not a true trade. Range bars are more robust here because they depend only on price levels, which snapshot feeds capture faithfully, not on counting every transaction. **For most Indian retail traders, range bars are the more reliable of the two** precisely because true tick data is hard to get without a proper broker API (or exchange-grade feed).

## Worked India example (levels and ₹)

**Bank Nifty futures intraday, 50-point range bars.** Bank Nifty opens near **52,000** and consolidates in a tight 52,000–52,120 band for the first twenty minutes. On a 5-minute time chart this prints four full candles of indecisive chop. On the 50-point range bar chart it prints only **two or three slow bars** — the low activity is honestly represented as *little chart*, and there's nothing to trade. Good: the tool refuses to manufacture false structure out of a quiet range.

At 9:45 a buying burst hits. Price rips from 52,050 to 52,400 in four minutes. The range chart fires **seven consecutive up bars** (each 50 pts): 52,050→100→150→...→52,400. Seven same-colour, same-size bars in rapid succession is an unmistakable, *quantified* momentum thrust — 350 points of one-way travel with no opposing bar. That visual is far cleaner than the single fat 5-minute candle it would otherwise be buried in.

- **Entry.** Enter long on the *third* consecutive up range bar (momentum confirmed, not the first impulsive bar), near **52,150**.
- **Stop.** Place the stop below the low of the burst's origin, ~52,000 — risk ≈ 150 pts. In rupee terms, Bank Nifty futures lot is 15 units → 150 pts × 15 = **₹2,250 risk per lot**.
- **Management.** Trail the stop under each new up range bar. When the run finally prints its first *down* 50-pt bar (say closing 52,350 after the 52,400 print), that is the momentum break.
- **Exit.** Exit on the first down bar or on a two-down-bar confirmation near **52,300–52,350** → captured ~150–200 pts → 150 × 15 = **₹2,250 per lot**, roughly 1:1 to 1.3:1 on this leg, on a clean momentum scalp that lasted minutes.

Now the **tick-chart complement.** On a 750-tick Nifty futures chart, the same style of analysis reads participation directly: during the dead open, one 750-tick bar might take eight minutes to complete (few trades). When the CPI-driven burst hits, three 750-tick bars complete in under a minute — the *bar velocity* itself signals that real money has arrived. A scalper watching tick-bar velocity gets an activity signal a time chart cannot show: it is not just that price moved, but that *many participants* transacted to move it, which is the footprint of conviction rather than a thin-liquidity spike.

## How to trade them: entry, stop, target, management

**Entry.** The signature range/tick setup is the **momentum-burst continuation**: a run of N consecutive same-colour bars signals a real thrust; enter on the 2nd–3rd bar of the run (not the 1st, which is often a spike, nor the 5th, which is often exhaustion). Breakout entries are also cleaner here — a range-bar break of a consolidation high has a fixed, known size, so the breakout is unambiguous.

**Stop.** Range bars hand you quantified stops: risk = a fixed number of bars. "Stop 2 bars against me" on a 50-pt Bank Nifty chart is exactly 100 points — no ambiguity. This is a genuine advantage over time charts where candle sizes vary wildly. Place the stop below the origin of the burst or a fixed 2–3 bars back.

**Target.** Because bars are equal-sized, measured moves are trivial: if a consolidation was 6 bars wide, project a similar bar-count for the breakout leg. Take partials into the count target and trail the rest with a bar-based trailing stop (exit on the first opposing bar, or first two).

**Management.** (1) **Bar-count trailing** — move the stop under each new bar in a run; simple and mechanical. (2) **Velocity awareness on tick charts** — accelerating bar completion = conviction, decelerating = the move is tiring; use it to tighten stops near exhaustion. (3) **Session filtering** — the first 30 minutes (9:15–9:45) and the pre-close (2:45–3:20, plus expiry-day gamma) are where these charts earn their keep; midday, both go quiet and should be traded lightly or not at all.

## Confluence

- **Volume / VWAP.** A range-bar momentum burst that unfolds away from VWAP with rising volume is a trend day forming; one that stalls at VWAP is likely mean-reverting. VWAP is the natural anchor for intraday range/tick trading.
- **Option chain / OI (index).** On Nifty/Bank Nifty a range-bar thrust through a heavy call-writing strike, confirmed by intraday call OI unwinding, is a high-conviction breakout — the range chart shows the thrust, the OI shows the fuel.
- **Order flow / footprint.** Range and tick bars pair beautifully with cumulative delta and footprint charts (covered elsewhere in this volume) because both are activity-native, not time-native — they speak the same language.
- **Higher-timeframe level.** Use a daily/hourly time chart to mark the key levels (PDH/PDL, S/R, round numbers), then drop to range/tick bars to *time* the entry at those levels.

Do not add three oscillators to a tick chart; on activity-based bars, oscillator periods (e.g. "14") mean "14 bars", which is a wildly variable amount of time — momentum oscillators behave erratically. Prefer volume, VWAP, OI and price structure.

## Pitfalls

**1. Tick-data quality in India.** As noted, true trade-by-trade tick data is not reliably available on many retail feeds; a "500-tick" bar on a snapshot feed is not what the textbook means. If you cannot get genuine tick data (via a proper broker API), prefer **range bars**, which need only accurate price levels.

**2. Backtesting is treacherous.** Range and tick bars are constructed *from* the tick stream, so historical backtests require true tick history, which is scarce and expensive for Indian instruments. Backtests built on reconstructed range bars from 1-minute OHLC are approximations and can badly misstate intrabar behaviour (a 1-min candle hides the path price took inside it). Treat range/tick backtests with extra skepticism and validate forward.

**3. Overnight gaps and session breaks.** Range bars assume continuous price; the overnight gap between 3:30 pm close and 9:15 am open (and lunch-free but news-driven jumps) breaks the fixed-range assumption — the first bar of the day can exceed R. Handle the open specially; don't treat the gap bar as a normal signal.

**4. Costs kill the small-size trader.** Because these charts fire many bars, they tempt overtrading. On Indian instruments the all-in cost stack — brokerage, STT/CTT, exchange txn charges, GST, stamp duty, slippage — is brutal for high-frequency scalping. A 15-point Nifty range-bar system that looks profitable gross can be firmly negative net. Size R and N large enough that average winners dwarf the round-trip cost.

**5. Whipsaw in chop.** Range bars in a tight range flip colour bar-to-bar, generating constant false burst signals. The tool shines in trending/volatile phases and hurts in balance; combine with a range/trend filter (e.g. only trade bursts that occur away from VWAP or after a level break).

**6. Parameter over-fitting.** Sliding R or N until yesterday looks perfect produces fragile settings. Anchor R to ATR and N to a target bar-frequency, and re-check when volatility regimes shift (VIX spikes, event days).

**7. Misreading equal-size as equal-time.** Just as with Kagi/TLB, distance along a range chart is not elapsed time. Seven range bars might be four minutes or forty. Never infer duration from bar count.

## Interview-ready summary

Range bars and tick charts replace the clock as the chart's organising constant with *market activity*. A **range bar** closes every time price travels a fixed distance R, so every bar is the same height, has no wicks, and a run of same-colour bars is a quantified momentum burst; the chart automatically speeds up in volatile phases and goes silent in quiet ones. A **tick bar** closes every N trades, making it an activity clock whose bar-velocity reveals participation and conviction. Both compress noise, give clean fixed-size stops and measured moves (a decisive edge over variable time-candles), and suit intraday momentum trading on Nifty/Bank Nifty/Fin Nifty futures and active MCX contracts. The honest caveats are decisive: genuine tick data is hard to get in India (favour range bars), backtesting needs scarce true-tick history and is easily misleading, overnight gaps break the fixed-range assumption, and the many-bars temptation makes Indian transaction costs the real enemy. The one-line essence: *time charts give every minute equal space; range and tick charts give every unit of real activity equal space — so the chart is loud when the market is, and quiet when it isn't.*
