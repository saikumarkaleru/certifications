# Belt Hold & Kicker Patterns

Most traders learn the "famous" candlesticks — the engulfing, the hammer, the doji, the morning star — and then stop. But the candlestick vocabulary is much larger, and two of its most underrated members are the **Belt Hold** and the **Kicker**. The Belt Hold (Japanese: *yorikiri*, a sumo term meaning to force your opponent out of the ring by the belt) is a single strong candle that opens at an extreme and closes at the other extreme. The Kicker (*keri ashi*) is a violent two-candle reversal built around a gap that flips sentiment overnight. Both are "shock" patterns — they work because they encode a sudden, one-sided imbalance of orders, not a gentle change of mind. In Indian markets, where gaps are frequent (result seasons, RBI policy, global cues, F&O expiry) and where index futures open with the weight of overnight SGX/GIFT Nifty already priced in, these two patterns show up constantly and are widely misread. This chapter goes deep on both.

## Part A — The Belt Hold

### What it is & why it works

A **Bullish Belt Hold** is a long white (green) candle that opens **at or very near its low** (no lower shadow, or a negligible one) and rallies all day to close near the high. Because the open is the low, every single buyer who entered that day is in profit by the close — there is no one trapped long and underwater, and every seller from the day is underwater. That is the psychological engine: a session where sellers never got a chance.

A **Bearish Belt Hold** is the mirror — a long black (red) candle that opens **at or very near its high** (no upper shadow) and falls all day to close near the low. Everyone who bought that day is trapped and losing; sellers dominate from the first tick.

The pattern "works" for the same reason a Marubozu works — it is essentially an opening Marubozu (a candle with no shadow on the opening side). The market voted decisively in one direction from the open and never looked back. When this appears after an extended move in the opposite direction, it flags exhaustion and a possible reversal. When it appears in the direction of the trend after a shallow pullback, it is a powerful continuation signal.

The key intuition: **the open being the extreme of the day is rare and meaningful.** On a normal day price probes both sides of the open. A belt hold day means one side seized control at 9:15 (or at the gap open) and held it to 15:30.

### Mechanics, settings & identification

Precise definition for a **Bullish Belt Hold**:
- Long real body (ideally larger than the average of the last 10-20 candles).
- Open == Low (or lower shadow < ~5-10% of the range).
- Upper shadow small (< ~25% of range) — some allow a modest upper shadow; a clean close-near-high is stronger.
- Appears after a downtrend or at support.

For a **Bearish Belt Hold**, invert: Open == High, no upper shadow, closes near low, appears after an uptrend or at resistance.

**Chartink / TradingView screening.** On Chartink you can approximate a bullish belt hold with a scan such as: `latest low = latest open` combined with `latest close > latest open * 1.02` (a 2%+ green body) and `latest volume > 1.5 * sma(volume,20)`. Because exchanges quote to two decimals, use a tolerance — e.g. `(latest open - latest low) / (latest high - latest low) < 0.08`. On TradingView Pine, the condition is `open == low` for daily bars, but in practice you should code `(open - low) <= (high - low)*0.08`.

**Timeframe sensitivity.** The pattern is most meaningful on the **daily** and **weekly** charts, and on the **opening 15-minute candle** of index futures, because the open there carries the overnight information gap. On a random 5-minute bar in mid-session, "open == low" happens often and means little. Weight the pattern by how "informative" the open is.

### Worked India example (levels & ₹)

Consider a reconstructed but realistic example on **Tata Motors** (verify the exact dates on your own chart). Suppose the stock has been sliding for three weeks from ₹1,050 down to ₹920 on weak auto-sales cues and FII selling. On a Monday, GIFT Nifty is flat, but Tata Motors gaps down slightly and opens at **₹918**, which turns out to be the day's low. Buyers step in from the first candle — perhaps a brokerage upgrade or bargain hunting — and the stock grinds up all day, closing at **₹951**, near the day's high of ₹954. The body is roughly ₹33 wide (about 3.6%), there is no lower shadow, and volume is 1.8x the 20-day average.

This is a textbook **bullish belt hold at support**. The prior downtrend, the location near a round number / prior demand zone (₹910-920), the fat body, and the volume surge all combine. It signals that the sellers who were in control for three weeks were overwhelmed the moment the market opened.

Now the bearish mirror on the index. Suppose **Bank Nifty** has rallied hard into an event — say, from 50,200 to 52,400 over two weeks ahead of an RBI policy. On policy day the futures open at **52,380** (the day's high), the RBI commentary disappoints on the liquidity front, and the index falls all session to close at **51,650**, near the low of 51,600. Open == high, no upper shadow, huge red body of ~730 points on heavy volume. That is a **bearish belt hold at resistance**, and it often marks the local top because it traps every trader who chased the pre-event rally.

### How to trade it — entry, stop, target

**Bullish belt hold (long):**

| Element | Rule |
|---|---|
| Trigger | Enter on a break **above the high** of the belt-hold candle on the next session (e.g. Tata Motors > ₹954), or buy the close if you are aggressive and the context (support + volume) is strong. |
| Stop | Just **below the low/open** of the belt-hold candle (< ₹918, say ₹910 to allow noise). The whole thesis is that the open was the low — if price breaks it, the pattern has failed. |
| Target 1 | Prior swing / measured move ≈ 1.5-2x the risk. If risk is ~₹40 (954 entry − 914 stop), T1 ≈ ₹1,030-1,050 area (prior consolidation). |
| Target 2 | Larger structural resistance or trail with a moving average / chandelier stop. |
| Timeframe | Daily-signal swing trade, hold days to weeks. |
| Regime | Best when the broader market (Nifty) is neutral-to-up; fighting a strong index downtrend lowers odds. |

**Bearish belt hold (short / exit longs):**

| Element | Rule |
|---|---|
| Trigger | Short on a break **below the low** of the candle (Bank Nifty < 51,600), or use it to exit/hedge longs immediately. |
| Stop | Above the **high/open** of the candle (> 52,400). |
| Target | Prior support / measured move; on an index use option structures — buy puts or a bear put spread rather than naked futures shorts to cap risk. |
| Timeframe | Daily swing; intraday on the 15-min for index. |
| Regime | Best after an extended rally into resistance or an event. |

A crucial discipline point: **the belt hold's extreme is your invalidation.** Because the pattern is defined by the open being the day's extreme, the moment price violates that extreme, the story ("one side controlled from the open") is objectively broken. This gives you an unusually clean, non-arbitrary stop — one of the reasons professionals like the pattern.

### Confluence (including OI)

- **Support/resistance & round numbers.** A bullish belt hold is far stronger when its low sits on a well-tested support or a psychological round number (₹900, 1,000; Nifty 24,000; Bank Nifty 50,000).
- **Volume.** A belt hold on above-average volume means real participation seized the open. On thin volume, be skeptical — it may be a low-liquidity artifact.
- **Trend context.** After an extended move it is a reversal; in the trend direction after a pullback it is continuation. Never trade it "naked" without context.
- **Option chain / OI.** For an index bullish belt hold near support, check whether the **Put OI** at that strike is large and rising (put writers defending the level — supportive) while **Call OI** overhead is being unwound. A bullish belt hold off Nifty 24,000 with heavy 24,000-PE writing and Call unwinding at 24,200 is high-conviction. For a bearish belt hold at resistance, look for heavy **Call writing** at that strike and Put unwinding below — smart money selling calls into the top confirms the reversal.
- **Confluence with other candles.** A belt hold that is also the second candle of an engulfing, or that forms the "kicker" gap discussed below, is doubly strong.

### Pitfalls

1. **Ignoring context.** A belt hold in the middle of a range is noise. It needs a trend to reverse or a pullback to resume.
2. **Gap-driven false extremes.** On a gap-down open that becomes a bullish belt hold, remember the open being the low is partly mechanical (the gap already displaced price). Judge the *body size and close location*, not just the open==low test.
3. **Chasing the close.** Buying the full belt-hold candle at its close means your stop (below the open) can be far away, hurting risk-reward. Waiting for the next-day break above the high often gives a tighter, cleaner entry.
4. **Small bodies.** A "belt hold" with a tiny body is just a small candle with no shadow — not a conviction move. Demand a body meaningfully larger than average.
5. **Index vs single stock.** On indices, the open is heavily conditioned by overnight global moves, so many opening candles technically qualify. Filter hard for size, volume and location.

### Interview-ready summary

A Belt Hold is a single long candle whose open is one extreme of the day and whose close is the other — a bullish belt hold opens at its low and closes near its high; a bearish one opens at its high and closes near its low. It signals that one side seized control from the very open and never surrendered it, so it flags reversals after extended moves and continuations after shallow pullbacks. Trade the break of the candle's high (bull) or low (bear), stop just beyond the opposite extreme (the open), and demand confluence with support/resistance, volume, and — on indices — a supportive shift in option-chain OI.

## Part B — The Kicker Pattern

### What it is & why it works

The **Kicker** is, statistically, one of the most powerful reversal patterns in the candlestick canon — and one of the rarest in clean form. It is a two-candle pattern:

- **Bullish Kicker:** a black (down) candle, followed by a **gap up** and a white (up) candle that opens *above* the prior candle's open, with **no overlap** of the two real bodies. Ideally both are marubozu-like (little shadow). Price literally gaps away from the down candle and runs.
- **Bearish Kicker:** a white (up) candle, followed by a **gap down** and a black candle that opens *below* the prior candle's open, no body overlap. The market gaps away from the up candle and collapses.

The defining feature that separates a kicker from an ordinary gap or an engulfing is that **the second candle opens on the opposite side of the first candle's open, leaving a gap between the two real bodies that is never filled during the two-candle sequence.** Sentiment did not gradually change — it *snapped*. Something happened (an earnings surprise, a policy, a merger, a guidance cut) that instantly repriced the asset and left the previous day's holders on the wrong side with no chance to react.

Why it works: a kicker represents an **information shock**. The overnight news is so decisive that market makers reprice the open far from yesterday's, and the day then trends in that new direction. Traders positioned the old way are trapped and forced to reverse, adding fuel. It is the purest candlestick expression of "regime change overnight."

### Mechanics & settings

Strict definition of a **Bullish Kicker**:
- Candle 1: bearish (red), preferably in a downtrend, ideally near-marubozu.
- Candle 2: bullish (green), **opens above Candle 1's open** — a gap up measured from open-to-open — and closes higher, ideally marubozu.
- The two real bodies **do not overlap**; there is a clean gap between C1's open and C2's open.
- Volume on C2 is heavy.

Purists insist the gap must be from **open of C1 to open of C2**, not merely close-to-open. This is what makes the kicker stronger than the engulfing: an engulfing can happen with the second candle opening *inside* the first; a kicker requires the second to open *beyond* the first candle's open on the far side. Unlike most reversal patterns, the kicker is considered valid **regardless of prior trend** — the shock is so strong that context matters less (though a kicker against the prevailing trend, reversing it, is the classic and most reliable form).

**India note on gaps.** Indian equities gap frequently: results (quarterly), block deals, sector news, and index moves. Index *futures* trade nearly continuously vs SGX/GIFT Nifty overnight, so pure gaps on Nifty futures are smaller; kickers are cleaner and more common on **cash-market stocks** and on the **daily equity chart**, where the 9:15 open reflects all overnight news at once.

### Worked India example (levels & ₹)

Reconstructed, realistic example — **Infosys** around results (verify dates on your chart). Suppose IT has been weak; Infosys drifts down and on Thursday prints a red candle from ₹1,540 open to ₹1,512 close (near marubozu, results due after market). After the close, Infosys reports a strong beat and raises FY guidance. Friday, the stock **gaps up and opens at ₹1,585** — well above Thursday's *open* of ₹1,540 — and runs to close at ₹1,624, a green near-marubozu on huge volume.

That is a textbook **bullish kicker**: Thursday red, Friday opens above Thursday's open with a clean gap between the bodies (₹1,540 top of C1 body vs ₹1,585 bottom of C2 body — a ₹45 gap), and Friday trends up all day. Everyone short into results is trapped; the guidance raise repriced the stock overnight. The measured expectation is a continuation higher over subsequent sessions as shorts cover and funds rebuild positions.

The bearish mirror — reconstructed **on a mid-cap after a guidance cut.** Say a chemicals mid-cap has rallied from ₹600 to ₹720. It prints a green candle Wednesday (open ₹705, close ₹718). After hours, management cuts margin guidance. Thursday it **gaps down, opens at ₹678** (below Wednesday's open of ₹705), and falls to close ₹652 — a red marubozu on heavy volume. That is a **bearish kicker at the top**: the gap between the bodies (705 to 678) never fills intraday, and the stock trends down. Every buyer from the rally's final leg is trapped.

### How to trade it — entry, stop, target

The kicker's power comes with a practical problem: **the move often happens on a large gap, so by the time you see the pattern, price has already jumped.** Your job is to enter without chasing and to place a stop that respects the pattern.

**Bullish Kicker (long):**

| Element | Rule |
|---|---|
| Trigger A (aggressive) | Buy intraday on C2 once it confirms it will hold above C1's open with strength — e.g. Infosys holding above ₹1,585 with a rising VWAP. |
| Trigger B (conservative) | Wait for a small pullback that **holds the gap** (does not fill into C1's body) and enter on the resumption. Buying the first higher-low after the kicker gives far better risk-reward. |
| Stop | Below the **gap / C1's open** (Infosys < ₹1,540) for the swing thesis, or below C2's low for a tighter intraday stop. A closed body inside the gap weakens the signal; a full gap fill invalidates it. |
| Target | Measured move (height of C2 projected up), next resistance, or trail with a moving average. Kickers on genuine news often trend for multiple sessions. |
| Timeframe | Daily swing. |
| Regime | Works in any regime because it is news-driven, but a bullish kicker with a supportive market is best. |

**Bearish Kicker (short / exit):**

| Element | Rule |
|---|---|
| Trigger | Short on a weak bounce that fails to fill the gap, or on a break of C2's low. |
| Stop | Above the **gap / C1's open**. |
| Target | Measured move down, prior support; on liquid names use put spreads to cap risk. |
| Timeframe | Daily swing. |

Golden rule: **the unfilled gap is the pattern.** If the gap fills — price trades back through into the first candle's body — the shock has been absorbed and the kicker has failed. Use gap fill as your invalidation.

### Confluence (including OI)

- **Volume & news.** A kicker should be accompanied by a clear catalyst (results, guidance, policy, block deal, upgrade/downgrade) and heavy volume. A kicker with no news and light volume is suspicious — possibly an operator-driven trap in an illiquid stock.
- **Gap that holds.** Confluence is the gap *not* filling in subsequent sessions; each day the gap survives, conviction grows.
- **Location.** A bullish kicker off a major support/round number, or a bearish kicker off resistance, is stronger.
- **Option chain / OI.** For a bullish kicker in an F&O stock, look at the futures OI: a strong up-move on **rising OI and rising price** = fresh longs building (bullish confirmation). Up-move on **falling OI** = short covering (can fade). On the option chain, aggressive **Put writing** at the new levels confirms buyers defending the gap. For a bearish kicker, price down + OI up = fresh shorts (strong); heavy **Call writing** overhead confirms sellers.
- **IV crush caveat.** After results, implied volatility collapses. If you express a kicker via options, buying premium the morning after results is often a losing trade even if you are directionally right — the IV crush eats you. Prefer spreads, or trade the underlying/futures.

### Pitfalls

1. **Chasing the gap.** The single biggest error. Buying at the top of a giant kicker candle leaves your stop (below the gap) very far away, wrecking risk-reward. Wait for a gap-holding pullback where possible.
2. **Gap fill = failure.** If the gap fills, exit. Don't rationalize — the informational shock has been neutralized.
3. **IV crush on options.** As above; directionally right, financially wrong. Match the instrument to the setup.
4. **Illiquid-stock traps.** In micro-caps, a "kicker" can be a manufactured gap with no follow-through. Demand liquidity, real news, and volume.
5. **Confusing kicker with engulfing.** An engulfing's second candle can open *inside* the first; a true kicker opens *beyond* the first candle's open, leaving a body gap. The distinction matters — kickers are stronger precisely because of that gap.
6. **Fading the shock too early.** Kickers on genuine fundamental repricing tend to trend. Trying to short a bullish kicker because "it's overbought" is a classic way to get run over.

### Interview-ready summary

A Kicker is a two-candle shock reversal: a candle of one colour, then a gap and a strong candle of the opposite colour that opens *beyond* the first candle's open, leaving an unfilled gap between the real bodies. It encodes an overnight information shock — results, guidance, policy — that reprices the asset instantly and traps everyone positioned the old way. It is powerful in any trend context, but strongest reversing the prior trend. Trade a gap-holding pullback rather than chasing, stop on a gap fill (the invalidation), confirm with news, volume and OI (fresh longs/shorts, put/call writing), and beware IV crush if you use options. Belt holds and kickers share one DNA — the open is where control was seized, and holding that open (or gap) is the whole trade.
