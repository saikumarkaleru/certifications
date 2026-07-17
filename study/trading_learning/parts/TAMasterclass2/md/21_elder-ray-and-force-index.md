# Elder Ray & Force Index

## What they are & why they work

Dr Alexander Elder, the trader-psychiatrist who wrote *Trading for a Living*, contributed two of the most practically useful indicators in the technical toolkit, and they are meant to be used together. **Elder Ray** measures the raw strength of buyers and sellers separately by comparing each session's high and low to a moving-average "consensus of value." **Force Index** measures the power behind each move by combining the *direction* of price change, the *size* of price change, and the *volume* driving it. Read together, they let you do something most indicators cannot: **distinguish between the trend (the tide) and the pullback (the wave), and buy the wave in the direction of the tide.**

The metaphor Elder used is the ocean. An Exponential Moving Average represents the market's evolving consensus of fair value — the tide. Bull Power and Bear Power (the two components of Elder Ray) measure how far the extremes of each candle stretch above and below that consensus — the reach of the buyers and the reach of the sellers. In an uptrend the tide is rising; the smart trade is to wait for a wave to briefly pull Bear Power (temporarily) into negative-and-recovering territory, then buy as the buyers reassert. Force Index, meanwhile, confirms whether the day's move had genuine muscle behind it or was a hollow drift.

Why do they work in Indian markets specifically? Because our trends are punctuated by sharp, fear-driven pullbacks — results shocks, global cues, F&O expiry unwinds — that shake out weak longs before the trend resumes. Elder's framework is built precisely to exploit this: it keeps you aligned with the dominant EMA-defined trend while giving a disciplined mechanism to enter *during* the scary pullback rather than chasing the breakout. For a Nifty or a quality large-cap in a structural uptrend, this "buy the dip that the herd is selling" edge is exactly where retail traders lose money and disciplined ones make it.

## Mechanics, formulas & settings

**Elder Ray.** Start with an EMA of the close — Elder's default is the **13-period EMA**. Then:

- **Bull Power = High − EMA(13)**
- **Bear Power = Low − EMA(13)**

Bull Power measures how far the buyers can push price above the consensus during the session (using the high). Bear Power measures how far the sellers can push it below the consensus (using the low). They are plotted as two histograms, usually beneath the price. In a healthy uptrend, Bull Power is positive and rising while Bear Power is negative but *shrinking* (becoming less negative) on pullbacks — sellers are losing their grip.

**Force Index.** Elder's raw Force Index for a single period is:

Force Index (1) = (Close today − Close yesterday) × Volume today

This raw value is jagged and hard to read, so it is almost always smoothed with an EMA:

- **Force Index (2-period EMA)** — a short-term signal for timing entries; it swings around the zero line and its crosses time pullback entries.
- **Force Index (13-period EMA)** — a medium-term reading of the trend's underlying power; useful for divergences and confirming the tide.

The three ingredients of Force Index each carry meaning. **Direction** (the sign of the close-to-close change) tells you who won the session. **Magnitude** (the size of the change) tells you by how much. **Volume** tells you how much force was behind it. A big up-close on huge volume produces a large positive Force Index — real buying power. A big up-close on thin volume produces a modest reading — suspect. This is why Force Index is such a good lie-detector for breakouts in Indian stocks, where a gap-up on low volume frequently fails.

**Settings for Indian markets:**
- Keep **EMA 13** for Elder Ray on the daily; it captures roughly a fortnight of consensus and suits Nifty/large-cap swings.
- Use **Force Index (2)** for entry timing and **Force Index (13)** for trend/divergence.
- On 15-minute Bank Nifty intraday charts, some traders drop Elder Ray's EMA to 8-9 and use Force Index (2) crosses for scalping pullbacks, but demand volume reliability — use the futures chart.
- For positional work on quality compounders (a HDFC Bank, a Titan), a 21-EMA Elder Ray filters expiry noise nicely.

## Worked India example (levels & ₹)

Take a reconstructed daily chart of **Reliance Industries** in an established uptrend — approximate levels to verify on your own chart. Reliance has been trending up from about ₹2,720 to ₹2,980, riding above a rising 13-EMA. The trend (the tide) is clearly up: the 13-EMA slopes upward, and Bull Power has been comfortably positive.

Now a global-cues wobble triggers a three-day pullback. Price slips from ₹2,980 to about ₹2,865, dipping to just below the 13-EMA. Here is the Elder Ray read: **Bear Power turns negative** — sellers have pushed the session low beneath the consensus of value, which is normal and even necessary for a good entry. But crucially, on the third down-day Bear Power prints a *higher low* than it did on the first down-day: the sellers' reach is contracting even as price grinds lower. That is the tell that the wave is losing energy against the tide.

The timing trigger comes from **Force Index (2)**. During the pullback it went firmly negative (down-closes on decent volume). On the fourth session Reliance closes up ₹18 on rising volume, and Force Index (2) crosses back above zero. Elder's rule fires: *in an uptrend, buy when Force Index (2) turns negative and then crosses back up, provided the trend EMA is rising.* 

- **Entry:** ₹2,884 on the Force Index (2) cross-up.
- **Stop:** below the pullback low, ₹2,858 — risk of ₹26.
- **Target:** retest and break of the prior high ₹2,980, then trail. 

Reliance resumes its trend and reaches ₹3,040 over the next nine sessions. From ₹2,884 to a trailed exit near ₹3,015 is about ₹131 of reward on ₹26 of risk — roughly 1:5. On a single Reliance futures lot the point value scales that into a meaningful rupee gain, and the beauty is that the entry was taken *while the herd was fearfully selling the dip.*

The mirror case: a Bank Nifty **bearish Force Index divergence**. Bank Nifty pushes to a new high near ₹51,400 but the Force Index (13) makes a conspicuously lower high than it did at the prior ₹51,000 peak — the power behind the advance is fading even as price extends. Combined with Bull Power failing to make a new high, this warned of the exhaustion that preceded a ₹2,000-point retracement.

## How to trade them — entry, stop, target

**Setup 1 — Elder's buy-the-pullback (the signature trade).**
- *Trigger:* Trend EMA(13) rising (tide up) → Bear Power negative but making a higher low → Force Index (2) crosses back above zero.
- *Stop:* Below the pullback swing low.
- *Target:* Prior swing high, then trail with the 13-EMA or a chandelier stop.
- *Regime:* Trending markets only. This is the core, high-probability application.

**Setup 2 — Elder's sell-the-rally (mirror image).**
- *Trigger:* Trend EMA(13) falling → Bull Power positive but making a lower high → Force Index (2) crosses back below zero.
- *Stop:* Above the rally swing high.
- *Target:* Prior swing low. Use in confirmed downtrends only.

**Setup 3 — Force Index divergence for exits/reversals.**
- A bearish divergence between price (higher high) and Force Index (13) (lower high) is a warning to book longs or tighten stops. A bullish divergence (price lower low, Force Index higher low) flags exhaustion of a decline. Treat divergences as *early warnings* requiring price confirmation, not standalone entries.

**Setup 4 — Zero-line and new-extreme reads.**
- Force Index (13) crossing above zero after a base can confirm a new uptrend's power. Force Index (2) reaching a *new multi-week extreme* on a breakout confirms genuine institutional participation — very useful for filtering false breakouts in Indian midcaps.

Risk management: size so that the distance from entry to the pullback low is a fixed fraction (say 0.5-1%) of capital. Because Elder entries sit close to the pullback low, stops are tight and reward-to-risk is naturally favourable — the whole point of his method.

## Confluence (including OI)

- **Option-chain / OI:** An Elder buy-the-dip in Nifty that lands right at a strike stacked with **heavy put writing** (a derivatives-defined support floor) is a premium setup — the cash structure (rising EMA, recovering Bear Power) and the options structure (put writers defending the level) agree. A bearish Force Index divergence that coincides with **aggressive call writing** overhead reinforces a top. Watch the PCR and Max Pain for the broader tilt.
- **Volume Profile / delivery %:** Force Index is a volume tool; pairing it with a rising delivery percentage on a stock confirms the buying is by holders, not day-traders. An entry at a High Volume Node adds a structural floor.
- **Multiple timeframe (Elder's Triple Screen):** Elder designed these indicators to sit inside his Triple Screen system — trend on the weekly (or higher timeframe), Force Index (2)/Elder Ray for entry timing on the daily, and precise execution on an intraday chart. Use the weekly trend as the tide filter for Nifty/Bank Nifty and take daily Force Index (2) entries only in that direction.
- **Support/resistance:** Bear Power turning up exactly at a prior swing low or a round number, with Force Index (2) crossing up, is stronger than a signal in open space.

## Pitfalls

1. **Using Elder Ray entries against the trend.** The system is explicitly a *pullback-in-a-trend* tool. Taking Bear-Power-recovery buys in a downtrend, or Bull-Power-fade sells in an uptrend, inverts the edge and produces losses. Always let the EMA slope define the tide first.
2. **Force Index needs trustworthy volume.** On the cash index the synthetic volume weakens the signal; use Nifty/Bank Nifty **futures**. On illiquid stocks the Force Index is noise.
3. **Force Index (1) is unusably jagged.** Never trade the raw single-period Force Index; always smooth it (2 for timing, 13 for trend). Beginners who read the raw line get whipsawed.
4. **Divergences fire early.** A Force Index (13) divergence can appear well before price tops. Treat it as a reason to tighten stops, not to reverse blindly into a strong Indian trend.
5. **Expiry and gap distortion.** Weekly-expiry volume surges and overnight results gaps inflate Force Index artificially. Discount signals on expiry sessions and read the first post-gap Force Index cautiously.
6. **Two EMAs, one trap.** If your Elder Ray EMA and your trend filter disagree because you set different lengths, you can get conflicting reads. Keep the framework internally consistent (13 for both, or a deliberate weekly/daily split as in Triple Screen).

## Interview-ready summary

Elder Ray and Force Index are complementary tools from Dr Alexander Elder built around one EMA-defined "consensus of value." Elder Ray splits into **Bull Power (High − EMA)** and **Bear Power (Low − EMA)**, measuring how far buyers and sellers can stretch price beyond consensus each session. Force Index — **(Close − prior Close) × Volume**, smoothed by a 2-period EMA for timing and a 13-period EMA for trend — measures the *power* of a move by combining its direction, magnitude and volume, making it an excellent lie-detector for hollow, low-volume breakouts common in Indian midcaps. Used together, they implement Elder's signature edge: identify the trend (tide) via the rising or falling EMA, then buy a pullback when Bear Power is negative but making a higher low and Force Index (2) crosses back above zero — entering *while the herd is fearfully selling the dip*, with a tight stop below the pullback low and a naturally strong reward-to-risk. In a downtrend the logic mirrors for shorts. Force Index divergences serve as early exhaustion warnings. The tools demand reliable volume (use futures for indices), must be traded *with* the trend not against it, and pay off best when confluent with option-chain support/resistance (put/call writing), volume profile and multi-timeframe structure. In one line: **the EMA is the tide, Elder Ray and Force Index measure the waves, and the disciplined trader rides the wave in the direction of the tide.**
