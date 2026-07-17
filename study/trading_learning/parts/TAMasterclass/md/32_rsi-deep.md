# RSI (Deep): Beyond Overbought/Oversold

Most retail traders learn exactly one thing about the Relative Strength Index: buy below 30, sell above 70. That single rule is responsible for more blown-up accounts in trending Indian stocks than almost any other indicator misuse. RSI at 80 in a stock like Trent or a rampaging Bank Nifty is not a sell signal — it is a signature of strength. This chapter treats RSI the way a serious technical and derivatives research analyst treats it: as a normalised momentum oscillator whose real edge lies in divergence, range shifts, failure swings, midline behaviour, and confluence with structure and option-chain data — not in two arbitrary horizontal lines.

## What it is & why it works

RSI, developed by J. Welles Wilder in 1978, measures the **speed and magnitude of recent price changes** and compresses them onto a bounded 0–100 scale. The word "relative" is often misread — it is not comparing one stock to another (that is *comparative* relative strength). It is comparing a stock's average up-moves to its average down-moves *over itself*, over a lookback window (default 14 periods).

The market behaviour it captures is the ebb and flow of buying versus selling pressure. When buyers dominate, up-closes outweigh down-closes, average gain rises relative to average loss, and RSI climbs. When sellers take over, the reverse happens. Because it is normalised, RSI lets you compare the *momentum condition* of Reliance today with its condition three months ago, or with Nifty's — even though the rupee moves are vastly different.

Why does it "work"? Not because 70 and 30 are magic. It works because momentum is auto-correlated in the short run (strength tends to persist) but mean-reverting at extremes (moves exhaust). RSI quantifies where in that cycle we sit. More importantly, because RSI is derived from price but moves differently from price, the two can **disagree** — and that disagreement (divergence) is where RSI earns its keep. A price making a higher high while RSI makes a lower high tells you the second push was made with less force: fewer buyers, smaller up-candles, waning conviction. That is a genuine, non-obvious piece of information you cannot read off price alone.

The honest framing: RSI is a probability tool. It tilts odds; it does not deliver certainty. In a strong trend it will scream "overbought" for weeks while price keeps rising. Treating it mechanically is a losing strategy. Treating it as one input into a structured, context-aware process is where the edge lives.

## The mechanics

**The formula.** RSI is built in two steps.

1. For each period, compute the change from the previous close. If positive, that is the period's *gain* (loss = 0). If negative, the absolute value is the *loss* (gain = 0).
2. Compute the average gain and average loss over the lookback (Wilder's default = 14).

The first average is a simple mean of the first 14 gains and losses. Every subsequent value uses Wilder's smoothing (a modified exponential average):

```
Average Gain = [(Prev Avg Gain × 13) + Current Gain] / 14
Average Loss = [(Prev Avg Loss × 13) + Current Loss] / 14
```

Then:

```
RS  = Average Gain / Average Loss
RSI = 100 − (100 / (1 + RS))
```

A worked micro-example: if over 14 days the average gain is ₹6 and the average loss is ₹3, RS = 2, and RSI = 100 − (100/3) = 66.7. If losses vanish entirely (a relentless run), Average Loss → 0, RS → infinity, RSI → 100. If gains vanish, RSI → 0.

**Key structural facts.**

| Property | Implication |
|---|---|
| Bounded 0–100 | Enables cross-instrument, cross-time comparison |
| Wilder smoothing | RSI is "sticky" — reacts slower than a raw ratio, filters noise |
| Uses closes only | Intraday spikes/wicks are ignored; the close is the vote that counts |
| 50 is the pivot | Above 50 = average gains > average losses (net bullish momentum) |

**Settings that matter for India.**

| Setting | Effect | Use case |
|---|---|---|
| RSI(14) | Wilder default, balanced | Swing trading, daily charts — the standard |
| RSI(9) | Faster, more signals, noisier | Short-term traders, 15-min Bank Nifty scalps |
| RSI(21)/RSI(25) | Slower, smoother | Positional/weekly charts, filtering out chop |
| OB/OS at 70/30 | Default | Range-bound or normal conditions |
| OB/OS at 80/20 | Wider bands | Strong trends, high-beta stocks (Adani names, PSU banks in a run) |
| Midline 40–60 zone | Trend filter | The real workhorse — explained below |

**The most under-used setting: the 40/50/60 framework.** Constance Brown and Andrew Cardwell reframed RSI around the midline. In a **bull trend**, RSI tends to oscillate between roughly **40 and 80–90**, with 40–50 acting as support on pullbacks. In a **bear trend**, RSI oscillates between roughly **10–20 and 60**, with 50–60 acting as resistance on bounces. So a break of RSI below 40 (having previously held it) can flag a *character change* long before price confirms — this is the "range shift," Cardwell's central insight and the reason to move beyond 70/30.

## Reading it — a worked India example

Let us walk through **Bank Nifty on the daily chart** across a realistic sequence, phase by phase, with levels and momentum readings. (Levels are illustrative but in the realistic 2024–25 range where Bank Nifty traded roughly ₹46,000–₹54,000.)

**Phase 1 — Trend establishment.** Bank Nifty bottoms near ₹46,200 after a correction. On the reversal, RSI(14) — which had been pinned near 28 (a genuine oversold in a *ranging* phase) — pushes up through 50 and then tags **72** as the index rallies to ₹49,500. A naïve trader shorts here: "overbought." Wrong read. The RSI has just made its *first* thrust above 70 after establishing a higher low in price. In Cardwell's framework, the first move to overbought after a base often *confirms* a new uptrend rather than ending it.

**Phase 2 — Range shift up.** The index pulls back to ₹48,300. Critically, RSI does **not** revisit 30 — it bottoms at **43** and turns up. This is the bullish range shift: momentum is now living in the 40–80 band. That 43 hold is your tradeable tell that the trend is intact. Price resumes to ₹51,800, RSI tags **78**.

**Phase 3 — The divergence warning.** Weeks later Bank Nifty grinds to a marginal new high of ₹52,400, but RSI this time peaks at only **68** — a *lower* high versus the prior 78 while price made a *higher* high. This is **bearish (negative) divergence**: the new price high was achieved with less momentum. It is a warning, not a trigger. Note it, tighten stops, watch for structure to break.

**Phase 4 — Confirmation and range shift down.** On the next decline, RSI slices through 40 — the level that held all through the uptrend — and reaches **34**, while price breaks the prior swing low at ₹51,100. Now the divergence has *confirmed*: momentum band has shifted from bullish (40–80) toward bearish (potentially 20–60). The subsequent bounce to ₹51,600 stalls with RSI capping at **58** (a bearish-range rejection near 60). That failed bounce, with RSI unable to reclaim 60, is a high-quality short setup — momentum, structure and range shift all agree.

Notice what did the work: not "70 = sell." It was divergence, the 40-line break, and the 60-line rejection — the deep RSI toolkit.

## Trading it

RSI is a *timing and confirmation* tool, best deployed around structure, not in a vacuum. Here are precise, scenario-based playbooks.

**Setup A — Bullish divergence reversal (mean-reversion into a level).**
- *Context:* Price at a known support (prior swing low, VWAP, a demand zone) in a stock like HDFC Bank near ₹1,620.
- *Signal:* Price makes a lower low (₹1,608) but RSI makes a higher low (32 → 38). Positive divergence.
- *Entry trigger:* Do **not** buy on the divergence alone. Wait for confirmation — a close back above the prior candle's high, or RSI crossing back above 40/50. Enter at, say, ₹1,628.
- *Stop:* Below the divergence low, ₹1,600 (below ₹1,608 with buffer). Risk ≈ ₹28.
- *Target:* First target the recent swing high / measured mid-range, ₹1,684 (2R). Trail the rest with a break of RSI below 45.

**Setup B — Trend pullback entry (the professional's bread-and-butter).**
- *Context:* Established uptrend (price above rising 50-EMA), e.g., Trent pulling back within an uptrend.
- *Signal:* In a bull trend, buy the *dip* when RSI falls into the **40–50 support zone** and turns up — not when it hits 30 (it rarely will in a strong trend).
- *Entry:* On RSI turning up from ~45 with a bullish candle at structural support.
- *Stop:* Below the pullback swing low.
- *Target:* Prior high, then trail. This lets you participate in trends instead of fighting them — the single biggest upgrade over the 30/70 approach.

**Setup C — Failure swing (Wilder's own signal, no price reference needed).**
- *Bearish failure swing:* RSI pushes above 70, pulls back to (say) 65, rallies again but **fails to exceed** the prior 70+ peak, then breaks below the intervening 65 trough. That breakdown is the sell trigger — RSI itself, not price, generates it.
- *Bullish failure swing:* mirror image below 30.
- These are cleaner in ranging instruments; use tighter stops.

**Position sizing and management.** Whatever the setup, define risk in rupees first. If Bank Nifty short risk is 250 points and you trade one lot (15 units), that is ₹3,750 risk — size so this is ≤1–1.5% of capital. Move stop to breakeven at 1R. Never widen a stop because "RSI is still oversold."

## Confluence

RSI alone is mediocre. RSI at a confluence is potent. Stack these:

**With price structure & S/R.** A bullish RSI divergence *at* a tested support (or a Fibonacci 61.8% retracement) is far higher-probability than divergence in mid-air. Structure tells you *where*; RSI tells you *when strength is returning*.

**With moving averages / trend.** Use the 50-EMA (or 200-EMA on daily) to set direction, then trade RSI signals *only in that direction*. In an uptrend, take Setup B longs and ignore RSI "overbought." In a downtrend, short RSI rejections at 60 and ignore "oversold." This one filter removes most bad RSI trades.

**With MACD.** RSI catches momentum exhaustion; MACD confirms the momentum-of-momentum turn via its signal-line cross and histogram. When RSI divergence coincides with an MACD histogram rolling over, conviction rises.

**With volume.** A breakout with RSI thrusting above 60 on *expanding* volume is trend-worthy. The same RSI move on thin volume is suspect.

**With the option chain / OI (the India F&O edge).** This is where a derivatives research analyst adds real value. Suppose Nifty is grinding to a new high but RSI shows bearish divergence. Now look at the option chain: if the **highest Call OI** sits just above at, say, the 24,500 strike (a wall of resistance where call writers are confident), and **PCR is low/falling** (bearish tilt), the divergence gets powerful corroboration — smart money is positioned for a cap. Conversely, a bullish RSI divergence at support that coincides with heavy **Put writing** (Put OI building at a strike, PCR rising, put writers defending a floor) is a high-conviction long. Use **Max Pain** and OI walls to define your targets/stops, and RSI divergence to time the entry. Momentum (RSI) + positioning (OI) + structure (S/R) agreeing is the three-legged stool of a strong setup.

**With multiple timeframes.** Confirm the higher timeframe first. A daily uptrend with daily RSI in its 40–80 band, then a 15-minute bullish RSI divergence at intraday support, gives you a low-risk timed entry aligned with the bigger trend.

## Pitfalls & false signals

**1. Trading 70/30 mechanically in a trend.** The cardinal sin. In strong Indian trends (PSU bank runs, defence/railway stocks in a theme rally), RSI can hold above 70 for weeks. Shorting each "overbought" print is a fast way to lose. Fix: use the 40–80 / 20–60 range framework and trade with the trend.

**2. Divergence in a powerful trend is a trap.** RSI can diverge repeatedly while price keeps trending — a "persistent divergence." Each new leg makes a lower RSI high, yet price marches on. Divergence is a *warning that needs confirmation* (a structure break, a range-line break), never a standalone reversal trade. Pros wait for the 40-line/60-line break to confirm the divergence has "activated."

**3. RSI on the wrong timeframe/instrument.** RSI(14) on a 1-minute chart of an illiquid smallcap is noise. Match settings to timeframe; demand liquidity.

**4. Ignoring the range shift.** Failing to notice when RSI stops holding 40 (bull) or 60 (bear) means you miss the earliest sign of trend change. Watch midline behaviour, not just the extremes.

**5. Parameter over-fitting.** Endlessly tweaking the length to make past signals look perfect produces a curve-fit that fails live. Stick to 14 (or 9/21 with a clear rationale) and let confluence do the filtering.

**6. Confusing RSI with comparative strength.** RSI(14) is internal momentum; it says nothing about whether the stock is outperforming Nifty. For relative *sector* strength, use RS ratio/ratio charts, not RSI.

**7. Gaps and events.** Post-result gaps, budget-day moves, or RBI-policy spikes can send RSI to extremes that reflect a one-off repricing, not sustainable momentum. Treat post-event RSI extremes with caution for a session or two.

## Interview-ready summary

"RSI is Wilder's bounded momentum oscillator — RSI = 100 − 100/(1+RS), where RS is the ratio of Wilder-smoothed average gains to average losses over 14 periods. It's normalised 0–100, so it lets me compare momentum conditions across instruments and time. The rookie use is 70/30 overbought/oversold, but that's actively harmful in trends — in a bull market RSI oscillates roughly 40–80 and holds 40 on dips; in a bear market it oscillates 20–60 and caps at 60 on bounces. So the real signals are: **range shifts** (when RSI stops respecting its trend band — an early character change), **divergence** (price making a new high/low that RSI doesn't confirm — a warning to be activated by a structure break), **failure swings**, and **midline behaviour**. I never trade RSI in isolation — I anchor it to structure and the higher-timeframe trend, and in Indian F&O I cross-check momentum against option-chain positioning: bearish RSI divergence into a heavy Call-OI wall with a falling PCR is a far stronger short than divergence alone. RSI tilts probabilities; it doesn't remove risk — so every signal gets a defined stop and size."
