# Volume Profile & Market Profile (POC, Value Area)

## What it is & why it works

Almost every chart a beginner draws is a study of price against *time*: the x-axis is the clock, and each candle asks "what did price do in this five minutes?" Volume Profile and Market Profile rotate the question ninety degrees. They ask "*at which prices* did the most business get done?" — mapping activity against price on the vertical axis instead of against time on the horizontal one. The result is a horizontal histogram running up the right side of the chart, fat where a lot of volume traded and thin where price passed through quickly.

Why does this matter? Because markets are auctions, and an auction's whole purpose is to discover the price at which the most buyers and sellers agree to transact — *value*. Prices where enormous volume changed hands are prices the market has collectively accepted as fair; both sides were willing to do size there. Prices that show a thin sliver of volume are prices the market *rejected* — it visited briefly, found no agreement, and left. This distinction is the entire edge. High-volume nodes act as magnets and support/resistance because they are crowded with participants who have positions, memory and break-even levels there. Low-volume nodes act as fast zones — price tends to move quickly through a vacuum because there is nothing (no resting interest, no trapped traders) to slow it down.

**Volume Profile** is the modern, volume-based version: it literally sums traded volume at each price. **Market Profile** is the original, invented by J. Peter Steidlmayer at the Chicago Board of Trade in the 1980s, and it uses *time* at price as a proxy for acceptance — it builds a "TPO" (Time-Price-Opportunity) letter chart where each 30-minute bracket that trades at a price drops a letter there, and prices touched in many brackets grow fat. Volume Profile answers "where did the *most size* trade"; Market Profile answers "where did price spend the *most time*." In liquid Indian instruments the two usually agree, and most traders today lean on Volume Profile because NSE volume data is clean and granular. The concepts — Point of Control, Value Area, high- and low-volume nodes — are shared vocabulary across both.

The deep reason this works in India specifically: Nifty, Bank Nifty and liquid large-caps are auction machines with immense participation, so their profiles are statistically meaningful. When ₹40,000 crore of Bank Nifty futures-and-options notional transacts in a session, the price where the bulk of it clustered is not noise — it is a genuine, defended reference that the same participants will remember and react to tomorrow.

## The mechanics

Three terms do 90% of the work. Learn them precisely.

**Point of Control (POC).** The single price level with the highest traded volume (or, in Market Profile, the most TPOs) over the chosen period. It is the histogram's fattest row — the auction's "fairest price," where buyers and sellers agreed most. The POC is the strongest magnet and the strongest support/resistance on the profile. A "naked" or "virgin" POC is a POC from a prior session that price has not since revisited — these act as unfinished-business magnets and price often returns to them.

**Value Area (VA).** The contiguous range of prices around the POC that contains **70%** of the period's total volume (one standard deviation, by convention). Its upper edge is the **Value Area High (VAH)** and its lower edge the **Value Area Low (VAL)**. Value Area is where the market considers price "fair." Above VAH price is expensive relative to accepted value; below VAL it is cheap. The 70% is computed by starting at the POC and adding the larger of the two adjacent rows repeatedly until 70% of volume is enclosed.

**High-Volume Nodes (HVN) and Low-Volume Nodes (LVN).** An HVN is a local bulge — a shelf of heavy trade that acts as support/resistance and tends to stall and range-bind price. An LVN is a local pinch — a thin zone the market rejected; price moves fast through LVNs, and LVNs make excellent stop-placement lines and breakout confirmation points because acceptance on the other side of an LVN signals a genuine shift.

**Profile types by anchor:**

| Profile | Anchor | Use |
|---|---|---|
| Session Volume Profile | Each trading day | Intraday reference; today's developing VA |
| Composite / Visible Range (VRVP) | User-selected range (a swing, a consolidation, a quarter) | Swing & positional S/R, big-picture value |
| Fixed Range | Two chosen dates | Analyse a specific move or base |
| Naked POCs | Prior sessions' POCs | Unfilled magnets |

**Market Profile shape vocabulary** (the "day types"):

- **D-shape / Normal day:** fat balanced bell around a central POC — a balanced, range-bound, two-sided auction. Fade the edges toward the POC.
- **P-shape:** fat at the top, thin tail at the bottom — short-covering or the pause after a rally; bullish then balancing. Fat area is acceptance, thin lower tail is rejection.
- **b-shape:** fat at the bottom, thin tail up — long liquidation; bearish then balancing.
- **Trend day (thin, elongated profile):** narrow profile with the POC migrating in the trend direction — one-timeframe, directional; do not fade.
- **Double-distribution / B-shape:** two separate fat clusters joined by a thin LVN — the market found two different areas of value in one session; the LVN between them is a decisive line.

**The three-part Market Profile logic** you should be able to recite: the **Initial Balance (IB)** is the range of the first hour (first two 30-min brackets); **range extension** beyond the IB signals fresh directional conviction from longer-timeframe participants; and **value migration** day-over-day (higher value vs lower value vs overlapping value) tells you whether the auction is trending up, down or balancing.

## Reading it — a worked India example

Take Nifty over a realistic multi-day stretch and read the composite and session profiles together.

**The composite (three-week base).** Nifty has been chopping between 24,400 and 24,900 for three weeks. Drop a Visible-Range Volume Profile over the whole base. It prints a fat POC at **24,650** — the price where the bulk of three weeks' trade agreed. The Value Area runs VAL **24,520** to VAH **24,780** (70% of volume). Above 24,780 and below 24,520 the histogram thins out fast — those are the LVN edges of the base. Read: 24,650 is the gravitational centre; 24,520–24,780 is "fair"; the market is balanced and rotational until it accepts price outside this range on volume.

**Session 1 — rotation inside value.** Nifty opens at 24,700, inside value. The Initial Balance forms 24,660–24,740. Price rotates: it tags VAH 24,780, gets sold back toward POC 24,650, tags VAL-ish 24,560, gets bought back to POC. This is a textbook D-shape balanced day. The trade all day is *fade the value-area edges toward the POC*: short near VAH, long near VAL, target the POC magnet. Nifty closes at 24,660, right on the composite POC — maximum agreement, unfinished business resolved.

**Session 2 — the breakout attempt and the LVN test.** Strong global cues; Nifty gaps to 24,830, *above* the composite VAH of 24,780, into the low-volume zone above the base. This is the decision point. Two outcomes:
- *Acceptance:* price holds above 24,780, builds a fresh little HVN at 24,850–24,880, and the developing session value migrates higher. The LVN vacuum above the base lets price travel fast — Nifty runs to 24,980. The breakout is real; the old VAH (24,780) now flips to support.
- *Rejection:* price pokes to 24,830, finds no volume acceptance (thin TPOs, quick reversal), and slides back *inside* value below 24,780. This is a failed breakout / "look above and fail," and the highest-probability target is a full rotation back to the POC 24,650 — because once the market rejects the excursion it seeks its fairest price again.

**Session 3 — naked POC magnet.** Suppose two days ago there was a session POC at 24,900 that price spiked away from and never revisited — a naked POC. When Nifty finally trades back up into 24,890 today, expect a reaction *at* that naked POC: it is unfinished business, a shelf of resting interest that either caps the move (resistance) or, once cleared on volume, releases price higher.

Notice how the profile turned an abstract "range" into a precise toolkit: a magnet (POC 24,650), a fair band (24,520–24,780), vacuum zones above and below where moves accelerate, and a specific failed-breakout target. That is the difference between "Nifty is range-bound" and a tradeable map.

## Trading it

Volume Profile gives you two families of trade — **reversion inside balance** and **breakout/continuation out of balance** — plus precise levels for both.

**Trade 1 — Value-Area fade (balanced/D-shape days).**
- *Setup:* price is inside a well-formed Value Area, opens inside value, no strong trend.
- *Entry:* short a tag/rejection of VAH, long a tag/rejection of VAL. E.g., short Nifty at 24,775 on a rejection wick at VAH.
- *Stop:* just beyond the VA edge into the LVN, say 24,810 (a clean acceptance beyond the edge kills the fade). Risk ≈ 35 points.
- *Target:* the POC (24,650), ~3.5R. This is the classic "80% rule" reversion: price returning inside value from an excursion tends to traverse to the POC.

**Trade 2 — Value-Area breakout / LVN acceptance (imbalance days).**
- *Setup:* price pushes beyond VAH/VAL into an LVN and *accepts* (holds, builds new volume) rather than snapping back.
- *Entry:* on confirmation of acceptance above VAH — e.g., a 15-min close above 24,780 that holds on the retest. Because the zone above is an LVN vacuum, entries are clean and follow-through fast.
- *Stop:* back inside value, below the old VAH / into the LVN, say 24,740 (loss of acceptance = failed breakout).
- *Target:* the next HVN above, or a measured move equal to the value-area width. Old VAH becomes your trailing support.

**Trade 3 — Naked POC magnet play.** When price is drifting toward an unfilled prior POC in a vacuum, target that POC as your objective; when it arrives, watch for reaction and either fade it (reversion) or trade acceptance through it (continuation). The naked POC is both a magnet to trade *toward* and a decision level to trade *at*.

**Trade 4 — Failed breakout reversal.** A "look above VAH and fail" that returns inside value is a high-conviction short back to the POC (and vice versa at VAL). Entry on the re-entry candle inside value, stop above the failure high, target POC.

**Management principles:** POC and HVNs are where you *take profit* (moves stall at heavy volume); LVNs are where you place *stops* and confirm *breakouts* (moves accelerate through vacuums). Always scale out at the first HVN/POC magnet — expecting price to blast through a heavy node is fighting the auction. On breakout trades, once the old value-area edge flips and holds, trail your stop under it.

## Confluence

Volume Profile is a value framework; it shines when other tools point to the same price.

- **POC + VWAP.** When the session POC and VWAP coincide, you have two independent volume-derived fair-value estimates agreeing — an exceptionally strong magnet and reversion target. A VWAP reclaim that also reclaims the developing POC is a high-conviction long.
- **Value-Area edges + option-chain OI (the India edge).** Map the Volume Profile onto the option chain. If the Value Area High sits right where the heaviest Call OI is stacked (say Bank Nifty VAH 48,780 lining up with the 48,800-strike Call wall), you have volume-based *and* options-based resistance at the same price — a premium short/fade zone. If VAL aligns with a fat Put-OI shelf (the 48,000 Put wall), that is double-defended support. Option sellers park size exactly where the auction found value, and the two datasets validating each other is as high-probability as intraday India trading gets.
- **LVN + breakout volume.** An LVN break *on a volume spike* is a genuine acceptance breakout; an LVN break on thin volume is a fakeout. Use volume to grade the break.
- **Naked POC + prior-day high/low + round number.** When a naked POC stacks with the previous day's high and a round number (e.g., 24,900), the confluence turns a single level into a wall.
- **Market Profile day type + trend tools.** A trend-day profile (thin, elongated, migrating POC) is your cue to switch off mean-reversion and switch on trend-following (VWAP-pullback longs, moving-average riding). A D-shape is your cue for the opposite. Reading the developing profile shape early tells you *which playbook* the day demands.
- **Value migration + higher-timeframe structure.** Three sessions of higher value (VA shifting up each day) confirming a higher-highs/higher-lows swing structure is a trend you hold; overlapping value day after day is a range you fade.

## Pitfalls & false signals

**The 70% Value Area is a convention, not a law.** Price does not owe you a reversion to the POC. On imbalance and trend days value *migrates* and fading the edges is how you get run over. The single most common Volume-Profile mistake is treating every VAH/VAL as a fade when the day is actually trending — always first ask "is the market balanced (D-shape) or imbalanced (trend/P/b)?" and pick reversion *only* in balance.

**Composite anchor choice changes everything.** Where you start and end a Visible-Range or Fixed-Range profile determines the POC and Value Area. Anchor sloppily and you get a POC that means nothing. Anchor to objective structure — a clear consolidation, a full swing, a quarter, from one major swing low to the next — not to arbitrary dates that happen to produce a convenient level.

**Session vs composite confusion.** Today's developing session POC is a short-term, still-forming reference; a three-week composite POC is a heavyweight structural level. Do not weight them equally. Structural composite levels win when they conflict with an intraday developing node.

**LVNs don't always accelerate.** The "price moves fast through vacuums" logic assumes a vacuum still exists. Markets fill in LVNs over time; an old LVN that has since accumulated volume is no longer thin. Read the *current* profile, not a stale one.

**Illiquidity breaks the tool.** In thin small-caps the profile is built from too few trades to be statistically meaningful — a couple of large prints create a fake POC. Volume Profile is a large-cap and index tool: Nifty, Bank Nifty, Fin Nifty, and liquid names where participation makes the histogram trustworthy.

**Market Profile's time-proxy can mislead on gappy, news-driven days.** TPO counts time, not size; on a day with one violent, huge-volume, short-duration spike, the TPO profile can understate where the real business happened. Cross-check with actual Volume Profile.

**Over-reading shape.** Not every profile is a clean D, P or b. Many days are messy hybrids. Force-fitting a textbook shape onto ambiguous data invites bias. When the shape is unclear, trade less and lean on cleaner levels (POC, prior VAH/VAL).

## Interview-ready summary

"Volume Profile flips the chart from price-over-time to volume-over-price — a horizontal histogram showing where the most business got done. The Point of Control is the highest-volume price, the auction's fairest level and its strongest magnet; the Value Area is the 70%-of-volume band around it that the market treats as fair, bounded by Value Area High and Low. High-volume nodes are shelves that stall price and where I take profit; low-volume nodes are vacuums that price rips through and where I place stops and confirm breakouts. On balanced D-shape days I fade the value-area edges back to the POC; on imbalance and trend days I trade acceptance beyond the edges through the LVN vacuum, because fading a trend is how you get run over. Market Profile is the original TPO version using time-at-price instead of volume, and it adds day-type vocabulary — D, P, b, trend, double-distribution — plus the Initial Balance and value-migration read. The India edge is overlaying the profile on the option chain: when the Value Area High lines up with a Call-OI wall and the Value Area Low with a Put-OI wall, I have volume-based and options-based support and resistance validating each other at the same price — and that confluence, not the profile alone, is where the high-probability trades live."
