# Candlestick Anatomy & How to Read a Candle

## What it is & why it works

A Japanese candlestick is the single most information-dense way to display one period of price action. Where a line chart shows only the close and a bar (OHLC) chart shows the four prices as thin ticks, a candlestick fuses the **open, high, low and close** into a shape whose *body* and *wicks* can be read at a glance — and, crucially, whose colour tells you instantly who won the period, buyers or sellers.

The technique traces back to Munehisa Homma, an 18th-century rice trader in Osaka who tracked the Dojima rice market and realised that price was driven as much by the *emotion* of the crowd as by supply and demand of rice itself. Steve Nison introduced the method to the West in the 1990s, and today every NSE trader watching Nifty on TradingView, Zerodha Kite or a broker terminal is reading candles whether they know the vocabulary or not.

Why does a candle *work* as a signal? Because a single candle is a compressed record of a **battle**. The open is where the period started; the close is where it ended after buyers and sellers fought all session. The distance and direction between open and close (the body) measures who won and by how much. The wicks — the thin lines above and below — mark the *furthest ground each side captured before being pushed back*. An upper wick is territory bulls reached and then surrendered; a lower wick is territory bears reached and then surrendered. So a candle is not just "price data" — it is a map of **rejection, acceptance, conviction and exhaustion**.

The behavioural logic is what gives candles predictive edge. Markets are auctions. When Bank Nifty spikes 250 points intraday and then closes back near where it opened, leaving a long upper wick, that wick is a footprint: real sellers stepped in with size at those higher prices and overwhelmed the buyers. The next period often opens with those sellers still in control. Candlesticks let you *see* that footprint. They do not predict the future with certainty — no tool does — but they tilt probability by revealing the balance of aggression that produced the print.

The reason candles beat line charts for a serious trader is **context of the close**. A stock can close up 1% for the day, and the line chart shows a friendly rising dot. The candle might reveal that the stock opened up 2.5%, ran to +3%, and then sold off all afternoon to close at +1% on a long red body — a bearish distribution day disguised as a green line. Only the candle exposes the intraday war.

## The mechanics

Every candle has four inputs and four visible parts. Let us define them precisely.

**The four prices**
- **Open (O):** the first traded price of the period.
- **High (H):** the highest price traded in the period.
- **Low (L):** the lowest price traded in the period.
- **Close (C):** the last traded price of the period.

**The four visible parts**
- **Real body:** the thick rectangle between the open and close. Its *length* measures the net directional move; its *colour* tells direction.
- **Upper wick (upper shadow):** the thin line from the top of the body to the high.
- **Lower wick (lower shadow):** the thin line from the bottom of the body to the low.

**Colour convention (India / TradingView default)**

| Candle | Condition | Meaning | Common colour |
|---|---|---|---|
| Bullish | Close > Open | Buyers won the period | Green (or white/hollow) |
| Bearish | Close < Open | Sellers won the period | Red (or black/filled) |
| Neutral | Close ≈ Open | Indecision (doji) | Either / grey |

For a **green candle**: the *bottom* of the body is the open, the *top* is the close. For a **red candle** it is inverted — the *top* of the body is the open, the *bottom* is the close. This inversion trips up beginners constantly, so internalise it: on a red candle, price started at the top and ended at the bottom.

**Anatomy proportions — the three ratios that matter**

The information is not in absolute rupees but in the *proportions* of body to wicks. Three ratios encode almost everything:

1. **Body / total range** = |Close − Open| ÷ (High − Low). Near 1.0 = a decisive marubozu (all body, no wicks); near 0 = a doji (all indecision).
2. **Upper wick / total range** = (High − max(O,C)) ÷ (High − Low). Large = rejection of higher prices (bearish pressure at the top).
3. **Lower wick / total range** = (min(O,C) − Low) ÷ (High − Low). Large = rejection of lower prices (bullish pressure at the bottom).

**A worked construction**

Suppose in one 15-minute candle Reliance trades:
- Open ₹1,420
- High ₹1,432
- Low ₹1,418
- Close ₹1,429

Total range = 1432 − 1418 = ₹14. Body = |1429 − 1420| = ₹9, and since close > open it is **green**. Upper wick = 1432 − 1429 = ₹3. Lower wick = 1420 − 1418 = ₹2. Body/range = 9/14 = 0.64 — a solidly bullish candle with a modest upper wick showing minor rejection near the high but a strong close in the top third of the range. A trader reads: *buyers were in control, closed strong, only slight selling at the top — bullish continuation likely.*

**Timeframe scales the meaning**

The identical anatomy means different things on different clocks. A doji on a 1-minute Nifty chart is noise; the same doji on the weekly Nifty chart after a 2,000-point rally is a market-moving warning. Always state the timeframe when reading a candle. As a rule, **higher timeframe candles carry more weight** because they aggregate more participants and more capital.

**Close is king**

The single most important price is the **close**, especially the higher-timeframe close. Institutions, funds and algorithms mark positions to the close; option settlement in India references closing/settlement prices; and a close beyond a level is what confirms a breakout. Intraday, price can pierce a level ten times — but the *close* relative to that level is what a disciplined trader acts on.

## Reading it — a worked India example

Let us read a real-style sequence on the **Nifty 50 daily chart**, phase by phase, the way a research analyst would narrate it in a morning note.

**Phase 1 — the setup (context).** Nifty has rallied from 24,800 to 25,450 over eight sessions, a clean uptrend of higher highs. The last three daily candles are green with small wicks — healthy. But the index is now pressing into a prior supply zone at 25,450–25,500 where it topped out three weeks ago. Context matters more than any single candle: we are at resistance, in an extended move.

**Phase 2 — the warning candle.** The next day Nifty opens at 25,440, spikes to a high of 25,510 (a marginal new high, tapping the supply zone), then sells off to close at 25,395 — *below its own open*. The candle is **red**, with:
- Upper wick = 25,510 − 25,440 = 70 points (large)
- Body = 25,440 − 25,395 = 45 points (red)
- Lower wick = 25,395 − 25,388 (low) = 7 points (tiny)

Body/range ≈ 45/122 = 0.37; upper wick/range ≈ 0.57. This is a candle with a **long upper shadow at resistance after an extended rally** — textbook rejection. The narration: *bulls pushed to a new high, hit the supply zone, and got slammed; sellers closed price near the low. The close is red and below the open — a distribution footprint.* This is not a "sell everything" candle on its own, but it flips the short-term bias from long-only to cautious.

**Phase 3 — confirmation.** The following session Nifty opens at 25,380 and closes at 25,270 on a full-bodied red candle (body/range ≈ 0.8), a near-marubozu down day. Two red closes off resistance, the second with strong body, confirm that the balance of aggression has shifted to sellers. A swing trader who was long from 25,000 now has explicit evidence to book profits or trail stops tighter.

**Phase 4 — measuring the aftermath.** Over the next four sessions Nifty drifts to 24,950, roughly the base of the prior consolidation — a 550-point round trip that the single warning candle telegraphed at the top. In rupees, a trader long 1 lot of Nifty (25 qty) who exited on the confirmation close near 25,270 instead of riding to 24,950 saved roughly 320 points × 25 = **₹8,000 per lot** versus doing nothing. That is the practical payoff of reading candle anatomy: not prophecy, but earlier, evidence-based exits.

## Trading it

You rarely trade *one* candle in isolation, but candle anatomy gives you the precise trigger, stop and target framework that every candle-based setup shares.

**Entry trigger — the "break of candle" rule.** For a bullish signal candle (say a strong green rejection candle off support), the standard entry is a **break above the high of the signal candle**. For a bearish signal candle, entry is a **break below its low**. This ensures the market confirms the candle's message with follow-through rather than you anticipating. On the Nifty warning candle above, a short trigger would be a break below the candle's low of 25,388.

**Stop-loss.** Place the stop on the *other side* of the signal candle plus a buffer. For the short: stop just above the rejection high of 25,510, say 25,530 (buffer for wick noise). Risk = 25,530 − 25,388 = 142 points. Keep stops beyond the *wick*, not the body — the wick already marks where the losing side gave up, so a move past it invalidates the read.

**Target / measured move.** Three approaches, use whichever the chart offers:
1. **Structure target:** the nearest prior support/demand zone — here 24,950.
2. **Measured move:** projecting the height of the preceding range downward.
3. **Risk multiple:** a minimum 1.5–2R target. With 142 points risk, a 2R target is 25,388 − 284 = 25,104.

**Scenario A — clean win.** Trigger fills at 25,385 on the break. Price trends to 24,960; you exit at your structure target for ~425 points, roughly 3R. On 1 Nifty lot that is 425 × 25 = **₹10,625 gross**, against risk of ~₹3,550. This is the ideal: a decisive candle, clean follow-through.

**Scenario B — chop / stop-out.** Price triggers the short at 25,385, dribbles to 25,340, then reverses and grinds back up through 25,510 to stop you at 25,530. Loss ≈ 145 points × 25 = **₹3,625**. The lesson: a rejection candle at resistance *tilts* odds but does not guarantee — you must accept the stop as a cost of doing business.

**Scenario C — partial / manage.** Price triggers, runs to 25,200 (near 2R), then stalls. You book half, move the stop on the rest to breakeven (25,385), and let it run. If it resumes down to 24,960 you bank the rest; if it whips back you lose nothing on the second half. This scale-out honours the candle's edge while protecting against its uncertainty.

**Management principle.** The candle that *triggered* you should keep "working." If, after a bearish trigger, the very next candle closes back *above* the signal candle's high with a strong green body, the setup is failing — the footprint got erased — and discretionary traders often exit early rather than wait for the hard stop.

## Confluence

A single candle is a weak signal; a candle *at a level, in a trend, with a reason* is a strong one. Stack these filters:

- **Location.** A rejection candle means far more at a defined support/resistance, a supply/demand zone, a round number (Nifty 25,000; Bank Nifty 52,000), a moving average (20/50/200 EMA), or a prior swing high/low. The Nifty warning candle above earned its weight because it printed *at a supply zone after an extended run*.
- **Trend context.** Bullish candles carry more edge in an uptrend or at the bottom of a range; bearish candles at the top. Fighting the higher-timeframe trend on a single candle is low-probability.
- **Volume.** A rejection or reversal candle backed by a **volume spike** signals real institutional participation, not a thin-liquidity fakeout. In stocks especially, a hammer on 3× average volume is far stronger than one on light volume.
- **Option-chain / OI confluence (F&O).** This is where Indian derivatives traders gain an edge. Suppose the Nifty rejection candle prints at 25,500 and the **option chain shows the heaviest call OI (open interest) at the 25,500 strike** — a well-defended call wall. The candle's rejection now aligns with a structural options ceiling: sellers of 25,500 calls (often institutions) are motivated to keep price capped. A bearish candle *at max-call-OI* is a high-confluence short. Conversely a bullish hammer at the strike carrying the **highest put OI** (a put wall / support) is a high-confluence long, because put writers defend that floor. Watch also **OI change intraday**: fresh call writing building at the strike where your bearish candle printed is real-time confirmation that smart money agrees with your read.
- **Multi-timeframe.** A bullish candle on the 15-minute chart that also sits on the daily 50-EMA is a two-timeframe agreement — trade it larger. A 5-minute candle against the daily trend and away from any level is a scalp at best.

The mental model: **each confluence factor is a vote**. One vote (a candle) is a coin flip. Four aligned votes — candle + level + trend + OI wall — is a setup worth real size.

## Pitfalls & false signals

- **Trading candles in a vacuum.** The commonest beginner error is reacting to a "nice green candle" with no level, no trend context and no volume. In the middle of a range, candles are mostly noise. *No location, no trade.*
- **Ignoring the close by acting intraday on an unfinished candle.** A candle is not confirmed until it closes. Traders repeatedly short a "big red candle" at 1:30 pm only to watch it close green. Wait for the period to close, or explicitly trade the lower timeframe with its own rules.
- **Fixating on colour, ignoring proportion.** A tiny green body with huge wicks is *indecision*, not strength — but colour-fixated traders read it as bullish. Always weigh body/range and wick ratios, not just red vs green.
- **Wick-hunting stops.** Placing stops just past the *body* rather than the *wick* gets you shaken out on normal noise, because wicks routinely probe beyond bodies. Respect the wick as the true rejection boundary.
- **Gap distortion (India-specific).** Indian equities and indices frequently **gap** at the open due to overnight SGX Nifty / GIFT Nifty moves and US markets. A daily candle's "open" may be far from the prior close, so the open/close relationship can be dominated by the gap rather than intraday conviction. Read gaps separately.
- **Illiquid stocks.** In low-volume small-caps, a single large order can paint a dramatic candle that means nothing about broad supply/demand. Candle reading assumes a genuine two-sided auction; thin names violate that assumption. Stick to liquid names — Nifty/Bank Nifty constituents, F&O stocks — for reliable candle behaviour.
- **Over-fitting single candles.** Pros treat one candle as a *hypothesis*, confirmed only by the *next* candle's follow-through. The way professionals filter false signals is simple: require the break-of-candle trigger, demand location and trend agreement, and accept that even a perfect setup loses a meaningful fraction of the time. The edge is in the aggregate, not the individual print.

## Interview-ready summary

*"A candlestick encodes one period's open, high, low and close as a body and two wicks. The body's colour tells me who won — green means close above open, red means close below — and its length measures conviction. The wicks mark ground the losing side reached and gave back: a long upper wick is rejection of higher prices, a long lower wick is rejection of lower prices. I read three ratios — body-to-range for conviction, and each wick-to-range for rejection. But no single candle is a trade; its meaning depends on **location, trend and volume**. My trigger is a break of the signal candle's high or low, my stop sits just beyond the opposing wick, and my target is the next structural level or a 2R multiple. In Indian F&O I add option-chain confluence — a bearish rejection candle at the max-call-OI strike, or a bullish hammer at the max-put-OI strike, is a high-probability setup because it aligns price action with where option writers are defending. The close, especially on the higher timeframe, is the price I respect most, because that is what institutions and settlement mark to. Candles tilt probability; they never guarantee — so I trade them with defined risk and let the edge play out over many trades."*
