# Volume Basics, OBV & Accumulation/Distribution

## What it is & why it works

Volume is the number of shares or contracts traded in a given period. It is the only truly *non-price* input on a standard chart — every other indicator is a transformation of price, but volume measures *conviction*: how many participants were willing to act at these levels. Price tells you *where* the market went; volume tells you *how much force* moved it there. This is why every serious technician treats volume as the second dimension of the tape, and why the oldest maxim in the craft — "volume precedes price" — has survived a century of market evolution.

The behavioural logic is straightforward. A price move on heavy volume means large, committed participants — often institutions — are transacting; the move has fuel and is more likely to continue. The same price move on thin volume means few participants care; it can reverse easily because there is no weight behind it. A breakout above resistance on 3× average volume is a different animal from a breakout on 0.6× volume — the first is demand overwhelming supply, the second is a drift that will likely fail. In Indian markets, where delivery-versus-intraday volume matters, a breakout backed by rising *delivery* percentage is even more telling: it means buyers are taking actual shares, not just churning intraday.

Raw volume, though, is noisy and hard to compare across days. Two families of indicators distil it into a running measure of buying versus selling pressure:

**On-Balance Volume (OBV)**, introduced by Joe Granville in 1963, is a cumulative running total that adds the day's entire volume on up-closes and subtracts it on down-closes. Its genius is simplicity and its premise is Granville's belief that "volume is the steam that drives the train" — that smart-money accumulation shows up in OBV *before* it shows up in price. When OBV rises while price is flat or falling, someone is quietly accumulating; when OBV falls while price holds up, distribution is underway. OBV turns volume into a leading indicator of the *balance of pressure*.

**Accumulation/Distribution Line (A/D)**, developed by Marc Chaikin, refines OBV's crude "up day / down day" logic. Instead of assigning the whole day's volume to the close direction, it looks at *where within the bar's range* the close landed. A close near the high means buyers dominated the session (volume is accumulated); a close near the low means sellers dominated (volume is distributed). This handles the common case where a stock gaps up, sells off all day, and still closes green — OBV would count that as pure accumulation, but A/D correctly recognises the intraday distribution.

Together, volume, OBV, and A/D let a trader answer the question that price alone cannot: *is this move real?* They are the confirmation layer that separates high-probability setups from traps.

## The mechanics

**Reading raw volume.** Plot volume as a histogram beneath price and compare each bar to a moving average of volume (commonly 20-period). The relative reading is what matters:

| Volume vs 20-avg | Interpretation |
|---|---|
| > 2× average | Climactic / high conviction (breakout or exhaustion) |
| 1.2–2× average | Above-average participation, confirms the move |
| ~1× average | Normal |
| < 0.7× average | Thin; moves suspect, prone to reversal |

The Wyckoff/VSA principle: a move should be *confirmed* by volume. Up-bars on rising volume and down-bars on falling volume = healthy uptrend. Up-bars on *falling* volume = weak, tiring advance.

**On-Balance Volume (OBV).** A running cumulative total:

| Today's close vs yesterday | OBV update |
|---|---|
| Close > prior close | OBV = prior OBV + today's volume |
| Close < prior close | OBV = prior OBV − today's volume |
| Close = prior close | OBV unchanged |

The *absolute* value of OBV is meaningless (it depends on the arbitrary start point). Only its *slope and divergences* matter. You read the trend of the OBV line and whether it confirms or diverges from price.

**Accumulation/Distribution Line (A/D).** Three steps per bar:

1. **Money Flow Multiplier (MFM):**
   MFM = [ (Close − Low) − (High − Close) ] / (High − Low)
   This ranges from −1 (close at the low) to +1 (close at the high). Close in the middle → near 0.

2. **Money Flow Volume:** MFV = MFM × Volume

3. **A/D Line:** A/D = prior A/D + MFV (cumulative)

The refinement over OBV is that A/D weights volume by *where the close sits in the range*, capturing intraday buying/selling pressure that OBV's binary close-vs-close logic misses.

**A note on Chaikin Money Flow (CMF).** The same MFM logic, but summed over a fixed window (usually 20 or 21 days) and divided by total volume, producing a bounded oscillator between −1 and +1. Above 0 = net accumulation, below 0 = net distribution. CMF is the oscillator cousin of the cumulative A/D line and is popular for spotting shifts without the drift of a cumulative line.

| Indicator | Volume assigned by | Output | Best for |
|---|---|---|---|
| Raw volume | — | Histogram | Confirming individual bars/breakouts |
| OBV | Close direction (all-or-nothing) | Cumulative line | Trend confirmation, divergence |
| A/D Line | Close position in range × volume | Cumulative line | Intraday pressure, subtle distribution |
| CMF | Close position in range × volume | Bounded oscillator (−1 to +1) | Timing pressure shifts |

## Reading it — a worked NSE stock example

Take Reliance Industries on the daily chart through a realistic accumulation-to-breakout sequence (illustrative levels around ₹1,380–₹1,500).

**Phase 1 — Quiet accumulation.** Reliance drifts sideways between ₹1,380 and ₹1,410 for six weeks. Price looks dead. But OBV is quietly *rising* — on the marginally-up days, volume is heavier than on the down days, so the cumulative line grinds higher. The A/D line rises too, because closes keep landing in the upper half of each day's range (MFM positive). This is the classic tell: price flat, OBV and A/D climbing = *someone is accumulating* while retail sees "nothing happening." Delivery percentage on the NSE bhavcopy is elevated — buyers are taking shares.

**Phase 2 — The breakout.** Reliance closes at ₹1,432, above the ₹1,410 ceiling, on volume 2.4× its 20-day average — a decisive, high-conviction break. OBV spikes to a new high, *confirming* the breakout. Because OBV had already been rising through the base, this breakout was pre-signalled; the volume simply released the pressure that OBV had been showing. A breakout that OBV confirms (both make new highs together) is high-probability.

**Phase 3 — The trend.** Reliance advances to ₹1,485 over three weeks. Up-days print above-average volume, pullback-days print light volume — textbook healthy trend. OBV rises in lockstep; A/D keeps making new highs. Nothing to worry about; the pressure remains bullish.

**Phase 4 — The divergence warning.** Reliance pushes to a new price high of ₹1,500, but this time OBV makes a *lower* high than it did at ₹1,485, and the A/D line flattens. Price is up, but the volume-pressure behind it is fading — a **bearish divergence**. On the up-days near ₹1,500, volume is thinner; on down-days it's picking up. The A/D multiplier is turning negative as closes slip toward the lower half of the daily range. Distribution is beginning under the cover of a new high. This is the smart money selling into strength while price still looks strong — invisible on the price chart alone.

**Phase 5 — Confirmation of the top.** Reliance rolls over from ₹1,500 to ₹1,455 on rising volume (heavy down-days), and OBV breaks its rising trendline. The divergence that warned in Phase 4 is now confirmed by price. A trader who trusted the OBV/A/D divergence trimmed or exited near ₹1,495; one who watched price alone is still holding at ₹1,455.

## Trading it

**Setup A — Volume-confirmed breakout.**
- *Entry:* Price closes above resistance on volume ≥ 1.5–2× the 20-day average, with OBV also making a new high (confirmation). Reliance long at ₹1,432.
- *Stop:* Below the breakout level / base low (₹1,405), or below the breakout candle's low.
- *Target:* Measured move from the base height (base ₹1,380–₹1,410 = ₹30 → first target ₹1,462), then trail.
- *Filter:* If the breakout comes on *below*-average volume, skip it or size down — unconfirmed breakouts are the most common trap.

**Setup B — Accumulation entry (OBV/A/D leads price).**
- *Context:* Price ranging/flat, OBV and A/D rising = stealth accumulation.
- *Entry:* Buy within the range near support, anticipating the breakout, or wait for the confirmed break. This is earlier and higher-reward but requires the volume divergence to be clear.
- *Stop:* Below the range low.
- *Target:* The eventual breakout target; the pre-positioning captures the base.

**Setup C — Divergence exit / short.**
- *Context:* Price new high, OBV/A/D lower high (bearish divergence) — Phase 4 above.
- *Action:* Trim longs, tighten stops; for a short, wait for price *confirmation* (OBV trendline break + price breaking a swing low) before entering, since divergences can persist. Short Reliance on the break below ₹1,470 with the OBV trendline already broken.
- *Stop:* Above the divergent high (₹1,505).
- *Target:* Prior support / measured move down.

**Management across scenarios:**
- *Volume expands in trend direction:* stay in, trail.
- *Volume dries up on the trend, expands on counter-moves:* trend is tiring; tighten stops.
- *Climactic volume spike (3–5× average) after a long move:* possible exhaustion/blowoff — take partial profits; do not chase.

## Confluence

- **Volume + price patterns.** Every breakout pattern — triangle, flag, cup-and-handle, range — demands volume confirmation. A triangle breakout on expanding volume is tradeable; on thin volume it's a likely fakeout. Volume is the *first* confluence filter for any pattern trade.

- **OBV/A/D + trendline.** Draw a trendline on the OBV line itself. An OBV trendline break often precedes the price trendline break — an early exit or entry signal.

- **Divergence + momentum oscillators.** When OBV divergence coincides with an RSI or MACD divergence at the same price high, the reversal signal is far stronger than either alone. Triple divergence (price, momentum, volume) is a high-conviction reversal flag.

- **VWAP (intraday).** Volume-weighted average price is the intraday institutional benchmark. Price reclaiming VWAP on rising volume with OBV turning up is a strong intraday long; rejection at VWAP on volume is a short. Bank Nifty intraday traders lean heavily on VWAP-plus-volume.

- **Option-chain / OI (India-specific, and critical).** In F&O, *volume* and *open interest* tell different stories and must be combined:
  - Rising price + rising OI + rising volume = fresh **long build-up** (strong bullish).
  - Rising price + falling OI = **short covering** (bullish but less durable — the fuel is buy-backs, not new longs).
  - Falling price + rising OI = fresh **short build-up** (strong bearish).
  - Falling price + falling OI = **long unwinding**.

  Pairing cash-market OBV/A/D with futures OI transforms the read. If Reliance's OBV is rising in a base *and* futures OI is building with price, accumulation is confirmed across both cash and derivatives — a high-conviction long. If a breakout comes with heavy volume but OI is *falling*, it may be short covering that fizzles rather than a fresh trend. On index options, a rally where OBV rises and the highest-OI Call strike sees OI *unwinding* (call writers covering) is genuine strength.

## Pitfalls & false signals

1. **OBV's all-or-nothing flaw.** OBV assigns the *entire* day's volume based only on close-versus-prior-close. A day that gaps up, distributes all session, and closes marginally green counts as full accumulation — misleading. This is exactly the case A/D or CMF handles better by weighting on close-in-range. Cross-check OBV with A/D.

2. **Divergences can persist.** A bearish OBV divergence can run for weeks while price keeps rising. Divergence is a *warning*, not a timing signal — always wait for price confirmation (trendline/swing break) before acting, or you short strength repeatedly and lose.

3. **Volume-data quirks.** Expiry days, index rebalancing, block deals, and F&O rollover weeks distort volume. A "volume spike" on Bank Nifty expiry Thursday isn't the same signal as one on a normal day. Futures volume also splits across contract months near expiry. Always know the calendar.

4. **Absolute OBV/A/D values are meaningless.** They depend on the arbitrary starting point. Only slope, trend, and divergence matter — never the raw number.

5. **Thin-stock unreliability.** In illiquid small-caps, a single large order can spike volume and OBV without representing broad conviction. Volume analysis is most reliable on liquid names (Nifty 50, liquid F&O stocks).

6. **Climactic volume misread as continuation.** A huge volume spike after an extended move is often *exhaustion* (a selling or buying climax), not confirmation of more to come. Context — where in the trend the spike occurs — decides its meaning.

7. **Ignoring delivery vs traded volume (India).** High traded volume with low delivery percentage can be intraday churn, not genuine accumulation. Checking delivery % on the NSE bhavcopy sharpens the read.

## Interview-ready summary

"Volume is the only non-price input on the chart — it measures conviction. The core principle is that a price move on heavy volume has fuel and is likely to continue, while a move on thin volume is suspect; 'volume precedes price.' I confirm every breakout against a volume average — I want 1.5 to 2× the 20-day average, ideally with rising delivery percentage in Indian cash markets. Two indicators distil volume into buying-versus-selling pressure. **OBV** — On-Balance Volume — is a cumulative line that adds the whole day's volume on up-closes and subtracts it on down-closes; its slope and divergences matter, not its absolute value, and it often leads price, so rising OBV in a flat base signals stealth accumulation. Its flaw is the all-or-nothing logic. **The A/D line** fixes that: it weights each day's volume by where the close sits in the bar's range — close near the high accumulates, close near the low distributes — so it catches intraday distribution that OBV misses; Chaikin Money Flow is its bounded oscillator version. The highest-value pattern is **divergence**: price makes a new high but OBV or A/D makes a lower high, revealing distribution under the cover of strength before price rolls over — but divergences persist, so I wait for price confirmation. In Indian F&O I always pair cash-market volume and OBV with futures *open interest* — rising price with rising OI and volume is fresh long build-up, whereas a breakout on falling OI is just short covering that may fizzle. Volume doesn't predict with certainty; it tells me whether the move I'm seeing is backed by real force or is a trap."
