# IT & Banking/Financials Sector TA

Two engines drive the Nifty 50: financials and IT. Together they routinely account for more than half of the index weight — Bank Nifty constituents plus HDFC Bank, ICICI Bank, and their peers form roughly 35-38% of the Nifty, while the IT pack (TCS, Infosys, HCL Tech, Wipro, Tech Mahindra, LTIMindtree) adds another 12-14%. If you understand how these two sectors *breathe* technically, you understand most of what moves the index. This chapter is a technical playbook for both — their distinct chart personalities, the levels that matter, the setups that repeat, and the confluences (including option-chain and global-cue overlays) that separate a high-probability trade from a coin-flip.

## Why these two sectors behave so differently

Banking and IT are almost mirror images in what drives them, and that shows up on the chart.

**Financials are domestic, rate-sensitive, and flow-sensitive.** Bank Nifty is the single most FII-dominated liquid index in India. When foreign money enters or exits India, it enters and exits through the largest, most liquid names — and those are private banks. So Bank Nifty is a *proxy for FII risk appetite*. It trends hard, whips violently on RBI policy and credit-cycle news, and has a beta well above 1.0 versus the Nifty. Its intraday range is the widest of any major index — 1.0-1.5% moves are routine, 2%+ on event days. Technically this means: cleaner trends when they run, but more false breakouts and stop-hunts because of the leverage and the crowd.

**IT is global, currency-sensitive, and defensive.** Indian IT earns 60-90% of revenue in USD (mostly US and Europe BFSI/retail clients). So an IT chart is really trading three things at once: the US economy (client tech budgets), USDINR (a weaker rupee is a tailwind to reported margins), and the Nasdaq/US tech sentiment. IT is a *low-beta, defensive* sector in India — when Nifty falls on domestic worries, money rotates *into* IT; when global tech sells off, IT underperforms even a rising Nifty. IT stocks trend more smoothly, respect moving averages better, and gap on results and on quarterly guidance far more than on any Indian macro print.

The practical takeaway: **you trade Bank Nifty for momentum and range; you trade IT for trend and rotation.** Applying the same setup to both is a beginner error.

## Bank Nifty: the technical character

Bank Nifty (spot roughly in the 48,000-52,000 zone in this era, with heavyweight constituents HDFC Bank, ICICI Bank, SBI, Axis, Kotak, plus PSU names) is the trader's index. Key structural facts you must internalise:

- **HDFC Bank + ICICI Bank alone are ~50%+ of Bank Nifty.** If these two disagree, the index chops. The cleanest Bank Nifty trends happen when both large privates move together. Always glance at the two heavyweights before trusting a Bank Nifty breakout.
- **PSU banks (SBI, PNB, Bank of Baroda, Canara) are a separate animal** — they run in sharp, news-driven bursts (recap, dividend, credit-growth data) and can diverge from the private-bank-led index for weeks. The PSU Bank index is worth a separate chart.
- **Weekly options expiry concentrates gamma.** Bank Nifty weekly expiry (historically Wednesday, subject to NSE's calendar) turns the last two hours into an option-driven magnet toward the highest open-interest strike. Pure price TA gets overridden by "max-pain" pinning on expiry afternoons — respect that.

### Worked Bank Nifty example (approximate reconstruction — verify on your charts)

Suppose Bank Nifty has been ranging between **48,200 support** and **49,600 resistance** for three weeks on the daily chart. The 20-DEMA is flattening at ~48,900, the 50-DEMA rising at ~48,400. RSI on the daily is oscillating 45-58 — classic range.

On a Monday, the index opens at 49,100 and pushes to 49,650, tags the range top, and closes at 49,580 — a bullish marubozu-ish daily candle on above-average volume. Simultaneously, in the option chain, the 49,500 call sees heavy *short covering* (OI falling as price rises through it) and fresh put writing appears at 49,000 and 49,200 — put writers are defending the breakout. This is the confluence: price breakout **+** call unwinding **+** put writing beneath.

The trade: enter long on a retest of **49,600** (old resistance becoming support) the next morning, or on a 15-minute close back above 49,650 if it gaps up. Stop below **49,300** (below the breakout candle's midpoint and below the fresh put-writing base). First target **50,200**, second **50,600** — measured move roughly equal to the 1,400-point range added to the breakout. If HDFC Bank and ICICI Bank are both green and above their own 20-DEMAs, conviction is high. If only one is participating, size down.

Outcome pattern: these range-breakout-with-OI-confirmation trades on Bank Nifty resolve within two to four sessions or they fail fast — Bank Nifty does not dawdle. The stop is tight *because* the index is fast; you accept a higher stop-out rate in exchange for large winners.

## The Bank Nifty setups that repeat

| Setup | Trigger | Stop | Target | Timeframe | Best regime |
|---|---|---|---|---|---|
| Range-break + OI confirm | Daily close beyond 3-week range top/bottom **with** call unwinding / put writing (or reverse) | Beyond breakout candle midpoint | Measured move = range width | Daily, hold 2-4 days | Trending FII flows |
| Opening-range breakout (ORB) | 15-min close above/below first 15-min bar high/low | Other side of the 15-min bar | 1.5-2x the ORB range | Intraday 15-min | Trend days, event days |
| VWAP reclaim | Price loses VWAP, then reclaims it on rising volume in second half | Prior swing low below VWAP | Day's high / prior day high | Intraday 5-15 min | Choppy-to-trend transition |
| Heavyweight divergence fade | Bank Nifty makes new high but HDFC+ICICI do NOT confirm | Above the false-breakout high | Return to range mid | Intraday/daily | Range / distribution |
| Expiry max-pain pin | Price drifts toward highest-OI strike after 1:00 pm on expiry | 150-200 pts adverse | The max-pain strike | Expiry-day afternoon | Low-event expiry |
| Policy-day compression break | Tight 30-min consolidation pre-RBI, break on the announcement candle | Opposite end of the coil | 1x the coil width, trail rest | Event intraday | RBI/Budget days |

**On the expiry pin:** this is not pure TA, it is options mechanics, but ignoring it costs money. When Bank Nifty is inside a low-news week and hovering near a strike with enormous combined call+put OI, the market makers who are short those options hedge in a way that dampens moves and pulls price toward that strike into the close. Fading extensions away from max-pain on Wednesday afternoon is a real edge — but it evaporates instantly if a genuine macro headline hits.

## IT sector: the technical character

The IT index (Nifty IT) is led by TCS and Infosys — together well over half the index — followed by HCL Tech, Wipro, Tech Mahindra, and LTIMindtree. Character notes:

- **IT respects moving averages beautifully.** TCS and Infosys daily charts hold the 50-DEMA for months in an uptrend and reject cleanly off the 200-DEMA. This makes IT ideal for classic trend-following: buy pullbacks to rising 20/50-DEMA, not breakouts.
- **Results and guidance are the whole game.** Four times a year (mid-Jan, mid-April, mid-July, mid-Oct — TCS reports first, kicking off Indian earnings season), IT stocks gap 3-8% on results, deal TCV, margin commentary, and *forward guidance*. Nine-tenths of an IT stock's annual range is created around four candles. Position sizing must respect this — never carry a big IT position naked through results unless that IS your thesis.
- **USDINR is the silent partner.** A rupee depreciating from, say, 83 to 85 to the dollar quietly lifts reported IT margins and is a background tailwind; a sharply strengthening rupee is a headwind. Overlay USDINR on your IT chart.
- **Nasdaq is the overnight tell.** IT often opens gap-aligned with the previous night's Nasdaq/US tech close. A big Nasdaq up-night frequently gives IT a gap-up that fades if there is no domestic follow-through — a known intraday fade setup.

### Worked IT example (approximate reconstruction — verify on your charts)

Infosys is in a daily uptrend, price ~1,560, above a rising 50-DEMA at ~1,510 and 20-DEMA at ~1,540. It has been consolidating in a tight 1,540-1,590 flag for two weeks after a run from 1,450. RSI cooled from 72 to 56 during the flag — a healthy reset, not a breakdown.

Results are three weeks away, so this is a pre-earnings continuation trade, not an earnings gamble. The setup: buy the pullback into the 20-DEMA / flag-support confluence at **~1,540-1,545**, with a stop below the 50-DEMA and the flag low at **1,505**. Target the flag's measured move: the pole was roughly 110 points (1,450→1,560), so project ~110 points from the ~1,545 breakout for a **~1,655** target, trailing with the 20-DEMA thereafter.

Confluence checklist that would raise conviction: TCS also basing above its 50-DEMA (sector alignment); USDINR stable-to-weak (margin tailwind intact); Nasdaq not in a fresh downtrend. If all three align and the Nifty IT index itself is above its 20-DEMA, this is a textbook low-drama trend trade — the kind IT gives you and Bank Nifty rarely does.

## The IT setups that repeat

| Setup | Trigger | Stop | Target | Timeframe | Best regime |
|---|---|---|---|---|---|
| DEMA pullback continuation | Bounce off rising 20/50-DEMA in an established uptrend | Below the next-lower DEMA | Prior swing high, then trail on 20-DEMA | Daily, hold days-weeks | Trending IT / weak rupee |
| Post-results gap-and-go | Gap up on results holds above the gap for first 60-90 min | Below the gap-fill / opening 15-min low | 1.5x opening range, trail | Intraday→swing | Positive earnings surprise |
| Post-results gap-fade | Big gap up on IN-LINE results (no guidance raise) stalls at open | Above the opening spike high | Prior close (gap fill) | Intraday | "Sell the news" quarters |
| Nasdaq gap-fade | IT gaps up purely on Nasdaq strength, no domestic bid, fades VWAP | Above opening high | VWAP / prior close | Intraday | Sentiment gaps |
| Sector-rotation entry | Nifty falls on domestic news, IT green and outperforming | Below the day's IT-index low | Continuation as defensive bid persists | 1-3 days | Risk-off rotation |
| 200-DEMA reversion buy | Quality large-cap IT tags rising 200-DEMA after overreaction | Below 200-DEMA with buffer | Reversion to 50-DEMA | Daily swing | Panic dips in bull market |

**On post-results behaviour:** the single most useful distinction is *guidance vs. print*. Indian IT can beat on the quarter's numbers and still fall 5% if forward revenue guidance is cut or margin commentary is cautious — that is the gap-fade quarter. Conversely a soft quarter with a *raised* guidance and strong deal pipeline (TCV) gaps up and runs. You cannot read this from price alone in the first thirty seconds; wait for the first 15-minute candle to *close* and see whether the gap holds or fills. Chasing the opening tick on results is how accounts die.

## Relative strength: the rotation trade between the two

The highest-quality sector trade is not long or short in isolation — it is the *ratio*. Build a simple relative-strength line: Nifty IT / Nifty Bank (or each sector index / Nifty 50). When the IT/Bank ratio is rising, capital is rotating defensive/global; when it falls, capital is rotating into domestic cyclicals and risk-on.

Practically:
- **Ratio turning up from a base** → overweight IT longs, lighten or fade Bank Nifty rallies. This often coincides with FII selling, a weakening rupee, or global risk-off — all IT tailwinds and banking headwinds.
- **Ratio rolling over from a top** → overweight Bank Nifty longs, take profits in IT. This coincides with FII inflows, rate-cut hopes, strong credit growth, risk-on.

Overlay the ratio's own 20-week moving average and treat crosses as regime signals, not intraday triggers. This single chart tells you *which* of the two playbooks above to run this month.

## Confluence layers to stack

For **Bank Nifty**, rank confluences in this order of reliability:
1. **Heavyweight agreement** (HDFC Bank + ICICI Bank aligned with the index move) — non-negotiable.
2. **Option-chain OI** — put writing under a breakout, call unwinding through resistance; the reverse for breakdowns. PCR extremes and shifts in max-pain.
3. **India VIX** — a falling VIX supports trend-continuation longs; a spiking VIX warns of whipsaw and favours reducing size.
4. **FII cash + index-futures positioning** — sustained FII buying underpins Bank Nifty uptrends; heavy short build-up in index futures warns of downside.

For **IT**, rank confluences:
1. **Sector alignment** (TCS + Infosys both on the same side of their 50-DEMA).
2. **USDINR direction** — weak/stable rupee = tailwind; sharp strength = caution.
3. **Nasdaq / US tech trend** — the overnight and multi-week backdrop.
4. **Results calendar proximity** — flat-out avoid fresh naked swing entries in the final week before a stock's own results unless the results ARE the trade.

## Pitfalls specific to each sector

**Bank Nifty pitfalls:**
- *Trusting the index over the heavyweights.* A Bank Nifty "breakout" carried by a single PSU spike while HDFC and ICICI are red is a trap — it fails intraday.
- *Ignoring expiry mechanics.* Running a momentum-breakout system into Wednesday afternoon fights the max-pain pin and bleeds.
- *Over-leveraging the wide range.* Because Bank Nifty moves 1-1.5% routinely, the naive trader takes full-size positions and gets stopped by normal noise. Size for the *volatility*, not the capital.
- *Fading RBI/Budget compression too early.* Pre-event coils can break either way and run far; wait for the announcement candle to close before committing.

**IT pitfalls:**
- *Chasing the opening results tick.* The first tick lies; the first 15-minute close tells the truth.
- *Forgetting the rupee.* A great-looking IT breakout can stall because the rupee suddenly strengthened, erasing the margin thesis.
- *Applying Bank Nifty aggression to IT.* IT rewards patience — buying pullbacks to rising DEMAs — and punishes breakout-chasing with slow bleed.
- *Mistaking a defensive bid for a bull run.* IT can rise simply because the rest of the market is falling (rotation). When the market bottoms and risk-on returns, that defensive IT bid unwinds and money rotates back to banks.

## Interview-ready summary

Financials and IT together dominate the Nifty, but they are technical opposites. **Bank Nifty** is the high-beta, FII-driven, domestic momentum index — widest intraday range, cleanest trends when HDFC Bank and ICICI Bank agree, but prone to false breakouts and expiry-day max-pain pinning. Trade it with range-breakouts confirmed by option-chain OI (put writing beneath, call unwinding above), opening-range breakouts on trend days, and VWAP reclaims — always cross-checking the two heavyweights, India VIX, and FII positioning. **IT** is the low-beta, USD-earning, defensive-and-global sector — it respects moving averages, trades on results and forward *guidance* far more than on Indian macro, and lives or dies with USDINR and the Nasdaq. Trade IT with DEMA-pullback continuations and disciplined post-results setups (wait for the first 15-minute close to judge gap-and-go versus gap-fade), and use it as the rotation counterweight to banks via the IT/Bank relative-strength ratio. The master skill is knowing *which* playbook the current regime demands: rising IT/Bank ratio in risk-off, weak-rupee, FII-outflow conditions; rising banks in risk-on, rate-cut, FII-inflow conditions. Match the tool to the tape and both engines of the Nifty become readable.
