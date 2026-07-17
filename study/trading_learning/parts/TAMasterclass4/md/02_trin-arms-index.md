# TRIN (Arms Index)

Most breadth indicators count *how many* stocks are advancing. TRIN does something cleverer: it compares how many stocks are advancing to *where the volume is going*. In a genuinely healthy rally, the up-stocks should be absorbing the lion's share of the day's volume — buyers are committing capital, not just nudging prices up on thin trade. When a rally rises on lots of advancers but the volume is quietly piling into the *decliners*, the market is hollow. TRIN catches exactly that mismatch. It is a lie-detector for rallies and selloffs.

Richard Arms designed the index in 1967, which is why it is formally the **Arms Index** — TRIN is short for "TRading INdex." It is one of the very few indicators that is *inverted*: low readings are bullish, high readings are bearish. That inversion trips up beginners constantly, so anchor it now — **TRIN below 1 is buying pressure, TRIN above 1 is selling pressure** — and the rest follows.

## What it is and the logic

TRIN is a ratio of two ratios. Numerator: the advance/decline ratio by *number of stocks*. Denominator: the advance/decline ratio by *volume*.

> **TRIN = (Advances / Declines) / (Advancing Volume / Declining Volume)**

Think about what this measures. If advancing stocks are also attracting a *proportionally* large share of volume — money flowing where the up-moves are — the denominator is large and TRIN falls below 1. If, instead, the advancers are many but the volume is concentrated in the *decliners* (heavy selling into a nominally up-day), the denominator shrinks and TRIN rises above 1. So:

- **TRIN < 1.0** → volume is favouring advancing stocks → real buying → **bullish** for the day.
- **TRIN = 1.0** → volume is evenly distributed relative to the up/down split → neutral.
- **TRIN > 1.0** → volume is favouring declining stocks → real selling → **bearish** for the day.

The counter-intuitive power move is at the *extremes*, where TRIN becomes a mean-reversion / capitulation gauge. A TRIN spike to very high readings (2.0, 3.0 and above) means volume is *panic-dumping* into decliners — everyone is selling everything at once. That is what a capitulation bottom looks like. Extreme fear is, historically, a buy signal. Conversely, a very low TRIN (0.40 and below) means euphoric, indiscriminate buying — a short-term top warning. **TRIN is a contrarian tool at its extremes and a confirmation tool in its middle range.**

## Construction and reading

The math is trivial; the data discipline is everything. Each day you need four numbers for your chosen universe (say the full NSE or the Nifty 500):

| Input | Description |
|---|---|
| Advancing issues | Count of stocks closing up |
| Declining issues | Count of stocks closing down |
| Advancing volume | Total traded volume in the up stocks |
| Declining volume | Total traded volume in the down stocks |

**Worked calculation.** Suppose on the NSE broad universe today: 1,200 advances, 800 declines; advancing volume 900 crore shares, declining volume 1,500 crore shares.

- A/D ratio (issues) = 1200 / 800 = **1.50**
- Up-vol / Down-vol = 900 / 1500 = **0.60**
- TRIN = 1.50 / 0.60 = **2.50**

Read this carefully. More stocks went *up* than down (breadth looked positive, A/D = 1.5), yet TRIN is a very bearish 2.50 — because the *volume* was overwhelmingly in the down-stocks. This is the hidden distribution the index-watcher misses: a nominally positive-breadth day that was actually heavy selling. If Nifty closed green on such a day, be suspicious of the strength.

Now a healthy day: 1,400 advances, 600 declines; advancing volume 2,000 crore, declining volume 700 crore.

- A/D = 1400/600 = 2.33
- Up-vol/Down-vol = 2000/700 = 2.86
- TRIN = 2.33 / 2.86 = **0.82** → below 1, volume confirming the advance. Genuine strength.

### The reading table

| TRIN | Condition | Bias |
|---|---|---|
| Below 0.50 | Extreme greed / overbought | Contrarian bearish; top watch |
| 0.50 – 0.80 | Strong buying pressure | Bullish |
| 0.80 – 1.20 | Neutral / balanced | No edge |
| 1.20 – 2.00 | Selling pressure | Bearish |
| 2.00 – 3.00 | Heavy selling / fear | Contrarian bullish begins |
| Above 3.00 | Panic / capitulation | Strong contrarian buy watch |

**Intraday vs. closing TRIN.** TRIN can be tracked live through the session and read at the close. Intraday, an *opening* TRIN spike above 2 that then falls through the day shows panic being absorbed by buyers — bullish. An intraday TRIN that starts near 1 and climbs steadily into the close shows distribution building — bearish, and a warning that a green open may not hold. The closing print is the one to log for your historical extremes.

**Smoothing — the moving-average TRIN.** A single day's TRIN is noisy. Many traders track a **5-day** and **10-day moving average of TRIN** to filter it. The moving-average version shifts the extreme thresholds: a 10-day TRIN above ~1.20–1.30 signals a sustained oversold market (bullish for a swing bounce), while a 10-day TRIN below ~0.85 signals sustained overbought (top risk). The smoothed version is far more useful for swing timing; the raw daily version is for spotting single-day capitulation.

## Worked India example

Picture a sharp Nifty selloff. Over a week, Nifty falls from 24,800 to 23,600 — a nasty 4.8% drop on global risk-off, FII selling, and a weak rupee. Retail is terrified; social media is full of "market crash" posts. You want to know: is this the flush, or is there more pain coming?

Track the daily closing TRIN through the decline:

| Day | Nifty | TRIN | Read |
|---|---|---|---|
| Mon | 24,800 → 24,500 | 1.6 | Selling, orderly |
| Tue | 24,500 → 24,150 | 1.9 | Selling intensifying |
| Wed | 24,150 → 23,800 | 2.4 | Heavy selling, fear building |
| Thu | 23,800 → 23,600 | **3.6** | Panic — capitulation print |
| Fri | 23,600 → 23,900 | 0.9 | Buyers absorbing; reversal |

Thursday's TRIN of 3.6 is the tell. Volume gushed into decliners across the board — indiscriminate, everything-must-go selling. That is not the behaviour of a market with more orderly downside to give; it is the behaviour of a market *purging* its weak holders. Historically, single-day TRIN prints above 3 on the NSE cluster at or within a day of intermediate bottoms. The next day's collapse of TRIN back below 1, with Nifty reversing up off 23,600, confirms buyers stepped in aggressively.

The trade: you do not catch the falling knife on Wednesday. You *wait for the TRIN spike plus a price reversal signal*. When Thursday prints TRIN 3.6 and Friday opens weak but reverses to close green with TRIN sub-1, you have a capitulation-plus-confirmation combo. Enter long on Friday's close or Monday's follow-through, stop below Thursday's 23,600 low. The risk is defined (the panic low), and the reward is the mean-reversion bounce that typically follows a genuine flush — Nifty back to 24,600+ over the following two weeks.

The mirror case: a slow grind higher where the 10-day TRIN sinks below 0.80 and the daily TRIN prints 0.42 on a euphoric gap-up day. That is indiscriminate buying — the crowd chasing. It does not mean sell immediately, but it means the easy upside is spent; tighten stops, stop chasing, and watch for a price reversal to short or hedge.

## How to use it for bias and timing

1. **Confirm the day's move.** Nifty closes green — check TRIN. Below 1? The strength is real, volume backed it. Above 1 on a green close? Distribution; be sceptical, the move may not hold. This single check separates genuine trend days from bull-traps.

2. **Fade the extremes, with confirmation.** TRIN above 2.5–3.0 on a selloff is a capitulation *watch* — pair it with a price reversal (hammer, bullish engulfing on Nifty, reclaim of a level) before buying. TRIN below 0.5 is a euphoria warning — pair with a price rejection before selling. Never trade the TRIN extreme alone; it can extend.

3. **Use the 10-day average for swing regime.** Sustained 10-day TRIN above 1.2 = market oversold, favour long swing setups. Below 0.85 = overbought, favour caution/hedges.

4. **Read intraday TRIN for the day's character.** Falling TRIN through the session = buyers in control, buy dips. Rising TRIN into the close = distribution, protect longs.

5. **Combine with McClellan and A/D line.** TRIN is a *volume-weighted* breadth read; the McClellan is a *momentum* breadth read. When a McClellan positive divergence at a low coincides with a TRIN capitulation spike, the bottom signal is far stronger than either alone.

## Pitfalls

**The inversion trap.** Beginners see a high number and think "high = strong = bullish." Wrong. High TRIN = bearish (selling), low TRIN = bullish (buying). Burn this in.

**It is a short-term tool.** TRIN is primarily a daily/intraday gauge. A single day's reading has almost no bearing on the multi-week trend by itself. For anything beyond a swing bounce, use the smoothed version and combine with trend tools.

**Volume data must be clean and from one universe.** TRIN is only as good as your advancing/declining volume feed. Bad or partial NSE volume data (missing a big block, or mixing segments) corrupts the denominator badly, and because it is a ratio of ratios, small data errors get amplified. Use a consistent, reliable NSE breadth-and-volume source.

**One or two mega-cap volume spikes can distort it.** A single huge block deal in a Reliance or an Adani name can swing the advancing- or declining-volume total on a quiet day, throwing TRIN off. Cross-check extreme readings against whether a lone giant is responsible.

**Extremes can extend in a trending crash.** In a true bear market or a 2020-COVID-style waterfall, TRIN can print above 2 for *many consecutive days* — each looking like capitulation, each followed by more downside. The contrarian buy only works with price confirmation; do not average down into a persistent-high-TRIN environment on the assumption that "it must bounce now."

**Different universes give different scales.** TRIN on the full NSE, on the Nifty 500, and on just the Nifty 50 will not read identically. Pick one universe, learn *its* extreme thresholds empirically, and stick to it.

## Interview-ready summary

TRIN, the Arms Index, is the advance/decline ratio by number of stocks divided by the advance/decline ratio by volume: (Advances/Declines) ÷ (Up-Volume/Down-Volume). It is inverted — below 1.0 is bullish (volume favouring advancers, real buying), above 1.0 is bearish (volume favouring decliners, real selling), and 1.0 is neutral. Its unique value is exposing days where breadth and volume disagree: a green, positive-breadth day with TRIN above 1 is hidden distribution, warning that index strength is hollow. At the extremes it flips to a contrarian tool — a TRIN spike above 2.5–3.0 signals panic capitulation and, paired with a price reversal, marks intermediate bottoms; a TRIN below 0.5 signals euphoric buying and top risk. A 10-day moving average of TRIN smooths the noise for swing-timing (above ~1.2 oversold, below ~0.85 overbought). Intraday, falling TRIN means buyers in control, rising TRIN into the close means distribution. In India, compute it on a single stable NSE universe with clean volume data, beware single mega-cap block deals distorting the ratio, and always confirm capitulation extremes with price action rather than trading TRIN alone — in a genuine waterfall, high readings can persist for days.
