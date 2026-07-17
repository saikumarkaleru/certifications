# ZigZag, Fractals & Auto-Pivots

Structure is the skeleton of technical analysis. Before you draw a trendline, count an Elliott wave, spot a double bottom, or measure a Fibonacci retracement, you first have to answer a deceptively simple question: *where are the swing highs and swing lows?* Human eyes do this instantly but inconsistently — two traders looking at the same Nifty chart will mark different pivots, and the same trader will mark them differently on a Monday than on a Friday. Three tools automate this pivot-detection so that structure becomes objective, repeatable, and codeable: the **ZigZag** indicator, which connects significant swings and filters out noise; **Williams Fractals**, which flag local turning points bar-by-bar; and **auto-pivot** systems, which compute mathematical support/resistance levels (classic/Camarilla/Fibonacci pivots) automatically each session. Together they form the plumbing beneath most other analysis. This chapter builds each, applies them to real NSE and MCX instruments, and — critically — confronts the one thing beginners get wrong about ZigZag: **it repaints.**

## Part A — The ZigZag Indicator

### What it is and why it works

The ZigZag draws straight lines connecting significant swing highs to significant swing lows, ignoring every price move smaller than a chosen threshold. Its entire purpose is *noise reduction for structure*: by discarding minor wiggles it reveals the underlying sequence of higher-highs/higher-lows (uptrend) or lower-highs/lower-lows (downtrend) at a glance. It is not a signal generator you trade off directly — it is a *labelling* tool that makes waves, patterns and Fibonacci anchoring objective.

The mechanism is a single filter: the **deviation threshold**, expressed as a percentage (or in ATR/points in some versions). The ZigZag only records a new pivot when price has reversed by at least that threshold from the last pivot. Set it to 5% and any retracement smaller than 5% is invisible; the line runs straight through it. Raise it to 10% and only the big swings survive; lower it to 2% and finer structure appears. This one knob controls the *degree* of the structure you see — which maps directly onto Elliott Wave's concept of degree and onto choosing swing size for Fibonacci.

### The repaint problem — read this twice

Here is the single most important fact about the ZigZag, and the reason it is misused constantly: **the last leg of the ZigZag repaints.** The most recent pivot is *provisional*. Suppose the ZigZag has drawn a line up to a new high at Nifty 25,300 and is currently drawing the line back down. If price falls 4% it looks like a confirmed swing high — but if price instead reverses and pushes to 25,450, the ZigZag *erases* the down-leg and extends the up-leg to the new high. The pivot you thought was fixed *moves*. This means:

- You can **never** build a trading signal on the *forming* ZigZag leg. Backtests that do so are fantasy — they "know" the pivot only in hindsight.
- Every confirmed (older) pivot is stable and reliable; only the final, live leg is provisional.
- ZigZag is a **descriptive/analytical** tool for marking confirmed structure, Fibonacci anchors, and pattern recognition — *not* an entry trigger.

Any strategy or YouTube video promising ZigZag "buy at the low, sell at the high" signals is either naive or dishonest about repainting. Respect this and ZigZag becomes invaluable; ignore it and it will flatter you in backtests and ruin you live.

### Settings

TradingView's built-in ZigZag uses a deviation percentage (default 5%) and a "depth" (minimum bars between pivots, default ~10). For the **Nifty daily**, 3–5% deviation captures the meaningful swings. For **Bank Nifty 15-min intraday**, a smaller 0.5–1% or an ATR-based setting suits the tighter ranges. For a **weekly** view of a large-cap, 8–10% isolates only major swings. There is no universal number — the threshold *defines the degree of structure you want to study*.

### Worked India example (levels & ₹)

Take **Nifty 50** weekly over a multi-month up-trend, with ZigZag deviation set to 6%. The indicator cleanly connects the sequence: a low at 23,800, up to a high at 25,100, back to a higher low at 24,400, up to 25,900, back to 25,200, up to 26,600. Because the small 2–3% intra-swing wobbles are filtered, the higher-highs/higher-lows sequence is unmistakable — the trend structure is *objective*. Now anchor a Fibonacci retracement to the last confirmed leg, 25,200 up to 26,600 (a 1,400-point leg). The 38.2% retracement sits at 26,065 and the 61.8% at 25,735. When Nifty later pulls back, those ZigZag-defined Fibonacci levels become your watch-list of demand zones — and because the swing points were chosen mechanically, another analyst using the same 6% setting would draw the *same* levels. That reproducibility is the entire value proposition. (Levels here are illustrative reconstructions — verify exact pivots on a live chart.)

### How to use it

| Use case | How |
|---|---|
| Trend structure | Read the HH/HL vs LH/LL sequence at a glance |
| Fibonacci anchoring | Attach retracement/extension to confirmed ZigZag legs |
| Pattern spotting | ZigZag makes double tops/bottoms, H&S, wedges pop out |
| Elliott degree | Adjust deviation to isolate the wave degree you're counting |
| What NOT to do | Never signal off the live, unconfirmed final leg |

## Part B — Williams Fractals

### What it is and why it works

Bill Williams' Fractal is a simple, *non-repainting* (once confirmed) pattern for marking local swing points. An **up-fractal** (a swing high) is a bar whose high is higher than the two bars on either side of it — five bars total, the middle one highest. A **down-fractal** (swing low) is the mirror: a bar whose low is lower than the two bars on each side. When the pattern completes, TradingView plots a small up- or down-arrow above/below the middle bar.

Why it works: it is a minimal, objective definition of "a local turn happened here." Because a fractal requires two bars *after* the pivot to confirm, it inevitably confirms **two bars late** — you know the swing high existed only once two lower-high bars have printed to its right. That lag is the price of objectivity, and unlike the ZigZag's live leg, a *confirmed* fractal never repaints: the two-bars-later confirmation locks it.

### Settings and mechanics

The standard fractal is 5-bar (2 bars each side). Some platforms let you widen to 7 or 9 bars for more significant, rarer pivots (more bars each side = stronger swing, later confirmation). Fractals are frequently combined with **Alligator** (Williams' three smoothed MAs) in his original method, but standalone they are most useful as *automatic swing-point markers* feeding other tools.

### Worked India example (levels & ₹)

Take **Gold on MCX** (the ₹/10g contract) on the daily during a pullback. Suppose gold dips and prints a down-fractal — a bar with a low of ₹71,200 that is lower than the two bars before and the two after. Two days later the fractal confirms (the two right-side bars have higher lows). That ₹71,200 down-fractal is now an *objective, locked swing low*. A structure trader treats a subsequent **break of the most recent up-fractal** as a trend-continuation trigger: if the last confirmed up-fractal (swing high) sits at ₹72,400, a daily close above ₹72,400 signals the pullback is over and the up-trend resumes. Entry ₹72,450, stop below the ₹71,200 fractal low, target measured from the prior leg. The fractals did the swing-marking for you, objectively — no eyeballing.

Fractals also give a clean **trailing-stop rule**: in a long, trail your stop just below each *new* confirmed down-fractal as the up-trend prints higher swing lows. Each fractal is a structural shelf; using them as a ratchet keeps your stop mechanical and honest.

### How to trade it

| Element | Rule |
|---|---|
| Swing marking | Up-fractal = swing high; down-fractal = swing low (5-bar) |
| Breakout entry | Close beyond the last confirmed opposite fractal in trend direction |
| Trailing stop | Ratchet stop to each new confirmed fractal on the trend side |
| Filter | Trade fractal breaks only with the higher-timeframe trend |
| Caveat | Confirms 2 bars late; a fractal alone is not a reason to trade |
| Timeframe | Any; higher timeframes give more meaningful fractals |

### Pitfalls

- **Too many fractals.** On noisy intraday charts 5-bar fractals appear constantly, most meaningless. Widen to 7/9 bars or filter by higher-timeframe context.
- **The 2-bar lag.** In fast markets the confirmation delay means the "swing" is old news by the time it's marked. Accept it or use a smaller-degree tool for timing.
- **Not directional.** A fractal marks a turn; it says nothing about whether the turn matters. Always combine with trend and location.

## Part C — Auto-Pivots (Classic, Fibonacci, Camarilla)

### What they are and why they work

Pivot points are *mathematically computed* support and resistance levels derived from the prior period's High, Low and Close. They plot automatically at the start of each session, giving intraday traders a pre-built map of likely reaction levels *before the day begins*. They work partly because the math is sensible (they cluster around the prior range's centre and edges) and partly through **self-fulfilling behaviour** — a huge number of traders and algos watch the same pivot levels, so price genuinely reacts at them. On the NSE, daily pivots computed from the prior day's OHLC are among the most-watched intraday levels for Nifty and Bank Nifty.

### The three families and their formulas

**Classic (Floor) Pivots.** The central pivot and three levels each side:

```
Pivot (PP) = (High + Low + Close) / 3
R1 = 2*PP - Low          S1 = 2*PP - High
R2 = PP + (High - Low)   S2 = PP - (High - Low)
R3 = High + 2*(PP - Low) S3 = Low - 2*(High - PP)
```

The PP is the day's presumed equilibrium; above it favours bulls, below favours bears. The **Central Pivot Range (CPR)** — the band between PP and the two levels TC = (PP-BC)+PP and BC = (High+Low)/2 — is hugely popular among Indian intraday traders: a *narrow* CPR signals a trending day ahead, a *wide* CPR signals a rangebound day.

**Fibonacci Pivots.** Same PP, but the support/resistance levels are set at Fibonacci ratios of the prior range:

```
R1 = PP + 0.382*(H-L)   S1 = PP - 0.382*(H-L)
R2 = PP + 0.618*(H-L)   S2 = PP - 0.618*(H-L)
R3 = PP + 1.000*(H-L)   S3 = PP - 1.000*(H-L)
```

**Camarilla Pivots.** Nick Scott's version pulls the key levels *tighter* around the close, making them well-suited to mean-reversion intraday trading:

```
R4 = Close + (H-L)*1.1/2     S4 = Close - (H-L)*1.1/2
R3 = Close + (H-L)*1.1/4     S3 = Close - (H-L)*1.1/4
```

The Camarilla H3/L3 (R3/S3) are classic fade levels — price often reverses off them in ranges; a break of H4/L4 signals a breakout/trend day. TradingView plots all three families as built-in "Pivot Points" indicators with a "type" dropdown.

### Worked India example (levels & ₹)

Take **Bank Nifty** intraday. Suppose yesterday's OHLC was High 51,600, Low 50,900, Close 51,200. Compute classic pivots:

```
PP = (51,600 + 50,900 + 51,200)/3 = 51,233
R1 = 2*51,233 - 50,900 = 51,566
S1 = 2*51,233 - 51,600 = 50,866
R2 = 51,233 + 700 = 51,933
S2 = 51,233 - 700 = 50,533
```

Today Bank Nifty opens at 51,280 (just above PP) — mild bullish bias. It rallies to R1 at 51,566, stalls, and pulls back to PP at 51,233, which holds. A pivot trader treats **PP-hold after an R1 rejection** as a long-again entry, targeting R1/R2, stop below PP. The CPR that day was moderately narrow, hinting at a trend-lean, and indeed the second push takes out R1 and runs toward R2 at 51,933. The levels were on the chart at 9:15 a.m. — no drawing, no guessing. (Illustrative; recompute from actual prior-day OHLC.)

### Confluence, including OI

Pivots become powerful when they *stack* with other evidence:

- **Pivot + option OI.** This is the highest-value confluence for Indian index intraday. If classic **S1 at 50,866 coincides with the strike holding the largest put OI (50,900 PE)**, you have a mathematical support *and* a structural writer-defended floor at the same place — a far stronger long zone than either alone. Likewise R2 lining up with heavy call OI is a stiffer ceiling. Always overlay the pivot map on the option chain.
- **Pivot + prior-day levels + round numbers.** When PP sits near a psychological round level (51,000) and yesterday's close, the confluence thickens.
- **CPR width as a regime read.** Narrow CPR → expect a trend day → favour breakout tactics at R1/S1. Wide CPR → expect chop → favour fading Camarilla H3/L3.
- **Fractal/ZigZag + pivot.** A confirmed fractal swing low landing exactly on S1 is a clean, objective reversal setup.

### Pitfalls

- **Blind fading.** Pivots are reaction *zones*, not walls. On a strong trend day price slices through R1, R2, R3 without pausing. Never fade a pivot against a powerful trend or on gap-and-go days.
- **Wrong session basis.** For NSE index intraday use the *prior day's* OHLC; using weekly or a wrong session shifts every level. Match the pivot period to your trading horizon.
- **Gap days.** A large opening gap can leave price starting beyond R2/S2, making the near levels irrelevant. Re-read the map when the open is extreme.
- **Over-crowded chart.** Plotting classic + Fibonacci + Camarilla + CPR all at once is 20 lines of clutter. Pick one family (CPR + classic is a common Indian combo) and keep it clean.

## How the three tools fit together

These are the *structure engine* beneath everything else, and they layer naturally by role. **Auto-pivots** give you the day's static map before the open — the levels to watch. **Williams Fractals** confirm, objectively and without repaint, *when* a swing turn has actually printed at or near those levels — the event. **ZigZag** steps back and shows the *degree and sequence* of the confirmed structure across the whole chart, and provides clean, reproducible anchors for Fibonacci and pattern work — the context. A disciplined workflow: use ZigZag on the daily/weekly to read trend structure and place Fibonacci; use fractals to mark and trail objective swing points; and use pivots-plus-OI to define the precise intraday zones where you actually pull the trigger.

The unifying discipline across all three is *honesty about what is confirmed*. ZigZag's final leg is provisional — never trade it. Fractals confirm two bars late — respect the lag. Pivots are probabilistic reaction zones — not guarantees. Used with that honesty, and stacked with volume, trend and option-chain OI, they turn the subjective art of "where are the swings" into an objective, repeatable foundation for every other technique in this book.

## Interview-ready summary

*ZigZag connects significant swing highs and lows, filtering moves smaller than a deviation threshold (e.g., 5%) to reveal objective trend structure and provide reproducible Fibonacci/pattern anchors — but its final leg repaints, so it is analytical, never a live signal. Williams Fractals mark local swing points using a 5-bar pattern (middle bar highest/lowest); once confirmed they don't repaint but they lag two bars, and they serve as objective swing markers, breakout triggers and trailing-stop shelves. Auto-pivots (Classic/CPR, Fibonacci, Camarilla) compute support/resistance from the prior period's OHLC, plotting a reaction map before the session — most powerful on Indian indices when stacked with option-chain OI, where a pivot and a writer-defended strike coincide. All three automate the skeleton of price structure; all demand honesty about what is confirmed versus provisional.*
