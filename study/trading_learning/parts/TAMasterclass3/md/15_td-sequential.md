# DeMark TD Sequential

Thomas DeMark spent decades as a consultant to some of the largest money managers on earth — Steven Cohen, Paul Tudor Jones, George Soros' funds — and the tools he built were designed to answer one specific question that most indicators dodge: **when is a trend exhausted?** Not "is the trend up or down" (any moving average tells you that), but "has the buying or selling reached the point where it is about to run out of fuel?" TD Sequential is his flagship exhaustion tool, and unlike almost every other indicator in technical analysis, it is **objective and mechanical** — every bar is either a count or it is not, with no eyeballing required. That objectivity is exactly why it survives in a book on advanced TA: it removes the discretion that ruins most reversal trading.

This chapter builds TD Sequential from scratch — the Setup, the Countdown, the qualifiers, the perfection rules — and then trades it on the Nifty and a couple of NSE names with real levels and rupees. Be warned up front: this is a **counter-trend** tool. It is designed to fade extended moves, which is statistically the hardest kind of trade to make money on. We will be honest about that throughout.

## What it is and the logic

Every trend, DeMark argued, is a battle between the crowd that is riding it and the "smart money" that is quietly distributing into that crowd. Near the end of a move, the trend still *looks* strong — price keeps making new highs — but the character of the buying degrades. Fewer new buyers arrive; the ones left are the last, most emotional, most trend-chasing participants. TD Sequential is a **bar-counting mechanism** that tries to fingerprint that degradation.

The core intuition is comparison across a fixed lookback. A healthy uptrend has today's close comfortably above the close of four bars ago, again and again. When price has closed higher than "four bars ago" for a long, uninterrupted run, the move is stretched — the population of buyers who were going to buy has largely bought. TD Sequential counts these comparisons in two stages:

1. **TD Setup** — a 9-bar phase that establishes that a directional move exists and is getting tired. This is the shorter-term signal.
2. **TD Countdown** — a 13-bar phase that begins after Setup completes and looks for the actual exhaustion point, comparing close against the low/high two bars ago. This is the higher-conviction signal.

A completed **Setup 9** flags a possible short-term turn or pause. A completed **Countdown 13** flags a possible more significant, tradeable reversal. The two work together — Countdown cannot even begin until a Setup has finished — so the tool has a built-in sequence, hence the name.

## Construction, rules and settings

TD Sequential uses **only price** — the open, high, low, close of each bar — and a handful of fixed integer comparisons. There are no smoothing parameters to over-fit, which is a major reason it is respected.

### TD Setup

A **bearish price flip** initiates a buy Setup; a **bullish price flip** initiates a sell Setup. A flip is simply a change in the very short-term momentum:

| Term | Definition |
|---|---|
| Bearish price flip | Close > close 4 bars ago, immediately after a bar whose close < close 4 bars ago |
| Bullish price flip | Close < close 4 bars ago, immediately after a bar whose close > close 4 bars ago |

Once flipped, you count:

| Setup type | Rule for each count bar | Completes at |
|---|---|---|
| **Buy Setup** | Close < close 4 bars earlier | 9 consecutive bars |
| **Sell Setup** | Close > close 4 bars earlier | 9 consecutive bars |

The count must be **consecutive**. If bar 5's close is not lower than the close 4 bars before it (in a buy Setup), the whole count resets to 1 on the next qualifying bar. This strictness is the point — it isolates genuinely persistent moves.

**Setup perfection.** A Setup is "perfected" — treated as higher quality — when a further condition on bars 8 and 9 is met:

- Buy Setup perfection: the low of bar 8 **or** bar 9 is less than or equal to the lows of bars 6 and 7. If not yet met at bar 9, perfection can occur on a later bar that finally undercuts those lows.
- Sell Setup perfection: the high of bar 8 or bar 9 is greater than or equal to the highs of bars 6 and 7.

An unperfected 9 often needs one more push before it turns.

### TD Setup Trend (TDST)

When a Setup completes, DeMark defines a **TDST support/resistance level**:

- **TDST support** (after a sell Setup, i.e. an up move) = the *true low* of the Setup (lowest low across bars 1–9, using true range where a gap exists).
- **TDST resistance** (after a buy Setup, i.e. a down move) = the *true high* of the Setup.

TDST lines act as intrabar decision levels: if a fresh Setup in the opposite direction breaks the prior TDST line on a closing basis, the trend is considered strong enough to *keep going* rather than reverse — a crucial filter we return to in "how to trade it."

### TD Countdown

Only after a Setup 9 completes does Countdown begin. Countdown compares the **close** to the **low or high two bars ago**, and — critically — the bars **need not be consecutive**:

| Countdown type | Rule for each count | Completes at |
|---|---|---|
| **Buy Countdown** | Close ≤ low 2 bars earlier | 13 |
| **Sell Countdown** | Close ≥ high 2 bars earlier | 13 |

You tick off 1 through 13 as qualifying bars appear, ignoring non-qualifying bars in between. Because Countdown allows gaps between counts, a Countdown 13 can take many bars — often 15 to 40+ — to complete, which is why it identifies a more mature exhaustion than the 9-bar Setup.

**Countdown 13 qualifier ("bar 8 rule").** DeMark added a condition to filter weak 13s: the low of Countdown bar 13 must be **less than or equal to the close of Countdown bar 8** (for a buy Countdown; reverse for sells). If bar 13 arrives but the qualifier is not met, it is deferred to "13+" until a bar satisfies it.

**Countdown cancellation / recycling.** Countdown is cancelled if price closes back through the TDST line in the opposite direction, or if a new Setup in the *same* direction forms and "recycles" the count. Recycling is a common source of frustration — a strong trend keeps generating fresh Setups that reset the Countdown, which is actually the tool telling you the trend is too strong to fade yet.

## Worked India example — Nifty 50 daily

Consider a Nifty 50 daily downtrend into a swing low (levels illustrative but realistic for a 2024-style correction). Nifty has fallen from about 22,100 toward 21,300 over three weeks.

**Step 1 — the flip.** After several days of closes *below* the close four bars earlier, a day finally closes at 21,540, which is *above* the close four bars back (21,510). That is a bullish price flip and it arms a **sell Setup** — but note we are in a downtrend, so what we actually want here is a **buy Setup** to call the bottom. The relevant flip for a bottom is the bearish price flip that begins the down-leg's buy Setup. Let us track it properly.

Going into the low, price has been closing lower than four bars prior repeatedly:

| Buy Setup bar | Date (illustrative) | Close | Close 4 bars ago | Qualifies? |
|---|---|---|---|---|
| 1 | Day A | 21,830 | 21,910 | Yes |
| 2 | Day B | 21,760 | 21,880 | Yes |
| 3 | Day C | 21,690 | 21,845 | Yes |
| ... | ... | ... | ... | ... |
| 7 | Day G | 21,420 | 21,690 | Yes |
| 8 | Day H | 21,360 | 21,610 | Yes |
| 9 | Day I | 21,315 | 21,540 | Yes → **Setup 9** |

Buy Setup completes at 21,315. Check perfection: is the low of bar 8 or bar 9 ≤ the lows of bars 6 and 7? Bar 9's low is 21,290, below both bars 6 and 7 lows (≈ 21,470 and 21,410). **Perfected.** The TDST resistance line is set at the true high of the Setup — say 21,955.

**Step 2 — Countdown.** From Setup bar 9 onward, we count bars whose close ≤ low two bars earlier. Nifty grinds sideways-to-down for another three weeks; qualifying bars appear intermittently. Suppose Countdown reaches 12 with price around 21,150, then a capitulation bar closes at 21,080, and its low (21,020) is ≤ the close of Countdown bar 8 (21,190). That satisfies the bar-8 qualifier: **buy Countdown 13** prints at 21,080.

We now have a perfected Setup 9 *and* a qualified Countdown 13 clustered near the low — the strongest configuration TD Sequential offers.

## How to trade it — entry, stop, target, management

TD Sequential gives a **signal bar**, not a market order. DeMark's own preference was to wait for confirmation rather than buy the 13 blindly.

**Entry approaches (buy example):**

| Method | Trigger | Character |
|---|---|---|
| Aggressive | Buy on the close of the 13 bar (21,080) | Earliest, worst average price, most false starts |
| TD confirmation | Buy when a later bar closes above the close two bars earlier (a short-term up-flip) | DeMark's default; misses the exact low but filters |
| Price-flip confirm | Buy on the first bullish structural flip after 13 | Most conservative |

**Stop.** DeMark's specific stop for a buy is a rupee amount below the **true low of the 13 bar** (or the lowest low of the Countdown), sized by the true range of that bar. Practically, on our Nifty example: 13-bar low 21,020, subtract that bar's true range (say 130 points) → stop **20,890** on a closing basis. If Nifty closes below 20,890 the exhaustion thesis is void.

**Targets.** Three natural target frameworks:

1. **TDST line.** The first objective for the counter-trend move is the opposing TDST — here the resistance at 21,955, roughly 875 points / ~4% of upside from a 21,080 entry.
2. **TD Risk / price projection.** DeMark projects a target by taking the true range of the Setup and adding it to the breakout of the TDST — a measured move.
3. **Prior swing / Fibonacci confluence.** In practice most traders simply target the previous consolidation or a 38.2–61.8% retracement of the down-leg.

**Management.** Because this is counter-trend, keep the first target modest and the stop tight. A common professional rule: bank half at the first quick pop (e.g., +1.5–2%), trail the remainder under successive TD Setup lows, and abandon the trade if a fresh buy Setup *recycles* (which would mean the down-trend is reasserting).

**F&O expression.** On the Nifty, a fresh Countdown 13 near a round level is a natural spot to buy a slightly OTM call debit spread rather than futures — the defined risk matches the "this might just be a bounce" honesty of a counter-trend signal. For a Bank Nifty 13 buy near, say, 47,200, a 47,500/48,500 bull call spread for a weekly expiry caps loss to the premium while capturing the TDST-line move. Selling puts is *not* advisable on a raw 13 because exhaustion signals fail often enough that undefined risk is reckless.

## Confluence

TD Sequential is far more reliable when the 9 and 13 land **on top of independent evidence**:

- **Support/resistance & round numbers.** A Nifty buy 13 at 21,080 sitting on a prior demand shelf near 21,000 is worth more than one floating in space.
- **Momentum divergence.** RSI or TD's own oscillators making a higher low while price makes a lower low, coincident with the 13, strongly corroborates exhaustion.
- **Volume/OI.** A capitulation volume spike on the 13 bar, or a peak in put OI at the strike below, marks where positioning is stretched.
- **Higher-timeframe alignment.** A daily buy 13 that occurs while the weekly is itself printing a buy Setup 8–9 is a "nested" signal — DeMark's most powerful configuration.
- **TDST break status.** If price is holding *above* the down-leg's TDST resistance on lower timeframes, the reversal has room; if the trend keeps breaking TDST lines, stand aside.

## Pitfalls

1. **It is counter-trend.** Fading strong trends is the graveyard of retail accounts. A 13 in a violent bear leg can be followed by three more 13s. Respect recycling.
2. **Recycling and cancellation confusion.** Beginners see a 13 and forget it can be cancelled by a TDST close-through or reset by a new same-direction Setup. Always check whether the count is still *live*.
3. **Perfection ignored.** An unperfected 9 turning point is weak. Insist on perfection for discretionary entries.
4. **Wrong timeframe.** On very low intraday timeframes (1–3 min Nifty), 9s and 13s fire constantly and mean little; the tool shines on 15-min, hourly, daily and weekly.
5. **Blind close-of-13 entries.** DeMark himself waited for confirmation. Buying every 13 at the close, with no filter, has an unimpressive hit rate.
6. **Charting differences.** TradingView, GoCharting and various NSE-data platforms implement Countdown qualifiers slightly differently (some ignore the bar-8 rule). Know exactly what your platform counts before you trade it.

## Interview-ready summary

TD Sequential is Tom DeMark's objective, price-only exhaustion indicator built in two stages. **TD Setup** counts 9 consecutive bars whose close is lower (buy) or higher (sell) than the close four bars earlier, after an initiating price flip; a Setup is *perfected* when bars 8/9 undercut (or exceed) the bars 6/7 extreme, and it defines a **TDST** support/resistance line. **TD Countdown** then counts to 13 bars — not necessarily consecutive — whose close is ≤ the low (buy) or ≥ the high (sell) two bars earlier, with a qualifier that bar 13's extreme relate to bar 8's close. A perfected 9 plus a qualified 13 near support/resistance, momentum divergence and higher-timeframe alignment marks probable trend exhaustion. Trade it counter-trend with confirmed entry, a stop beyond the 13 bar's true range, and the opposing TDST line as the first target. Its great virtue is objectivity; its great danger is that it fades trends, so recycling, cancellation and honest position sizing are non-negotiable. On Indian markets it works cleanly on Nifty/Bank Nifty daily and weekly charts and pairs naturally with defined-risk option spreads.
