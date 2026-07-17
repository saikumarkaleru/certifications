# Breakout Systems (Deep)

## Origin & idea

The breakout is the oldest systematic trade in the book, and it remains one of the most robust — precisely because it is unglamorous. The idea: price spends most of its life going nowhere, coiling inside ranges, and then occasionally *escapes* into a directional move. If you buy the escape from the top of a range (or sell the escape from the bottom), you position yourself at the start of the trends that produce almost all of a market's total return. The uncomfortable truth of markets is that a small number of large trending moves account for the bulk of profits, and breakout systems are engineered to be *in* those moves early — at the cost of being wrong often on the false ones.

The lineage is famous. Richard Donchian's channel breakout (buy an N-day high) is the granddaddy. Richard Dennis and William Eckhardt built the "Turtle" experiment on it in the 1980s, proving that mechanical breakout rules with disciplined risk could be taught to novices and produce spectacular returns. Toby Crabel formalised the "opening range breakout" and the observation that narrow-range days precede expansion days ("the NR7"). Every trend-following CTA that has compounded for decades — from the original Turtles to modern managed-futures funds — is, at its core, running a diversified breakout system.

The reason breakouts persist as an edge is structural and behavioural. A range is a temporary equilibrium between buyers and sellers. A break of that range means new information or new flow has tipped the balance — and crucially, stops sit just beyond the range. When price breaks a well-watched high, the buy-stops of shorts and the buy orders of breakout traders fire together, creating a self-reinforcing thrust. Momentum begets momentum. The behavioural cost is that this same visibility produces *false* breakouts — "bull traps" — where price pokes above the range, triggers stops, and reverses. A deep breakout system is really a machine for capturing the real breaks while surviving the false ones cheaply.

For Indian markets, breakouts are everywhere and very tradable: Nifty and Bank Nifty range for weeks then trend for weeks; individual F&O stocks break multi-month bases on results or sector rotation; the opening range on Bank Nifty is a day-trader's staple. This chapter goes past "draw a line and buy the break" into the deep mechanics: volatility-based triggers, false-breakout filtering, volume/breadth confirmation, and sizing that survives the whipsaws.

## The anatomy of a tradable breakout

Not all breakouts are equal. A deep system distinguishes them by four properties:

1. **The base quality.** The longer and tighter the consolidation before the break, the more meaningful the break. A 3-month tight base on a stock (like a classic Darvas box) breaking out is far higher-quality than a 3-day flag. Volatility contraction *before* expansion is the tell — Bollinger Band "squeezes," NR7 days, or a falling ATR into the break.
2. **The trigger level.** N-day high (Donchian), a horizontal resistance touched multiple times, a chart-pattern neckline, or the prior day's high (ORB). Multi-touch levels with more prior rejections give a cleaner, more-watched line.
3. **The confirmation.** Volume expansion on the break, a *close* beyond the level (not just an intraday poke), and breadth/relative-strength alignment. Confirmation is what filters traps.
4. **The follow-through.** Real breakouts hold above the broken level and extend; false ones fail back inside within a bar or two. How you handle the retest defines your entry style.

## Exact rules — a volatility breakout system for NSE

Here is a fully specified swing system usable on Nifty, Bank Nifty and top F&O stocks. It blends Donchian channels with a volatility filter and a false-breakout guard.

### Universe & vehicle

| Component | Choice |
|---|---|
| Instruments | Nifty, Bank Nifty, Fin Nifty; top ~40 liquid F&O stocks |
| Vehicle | Index/stock futures, or long call spreads (stocks: buy in cash / futures) |
| Timeframe | Daily for swing; 5–15 min for the intraday ORB variant |

### Signal construction

| Parameter | Value |
|---|---|
| Channel | 20-day Donchian high (long trigger) / 20-day low (short) |
| Squeeze filter | Only take breaks where ATR(10) has been *contracting* — i.e. current ATR < ATR 10 bars ago, OR a Bollinger squeeze (band width in the lowest 20% of its 6-month range) |
| Volume confirm | Breakout-day volume ≥ 1.5× the 20-day average volume |
| Entry | Buy on a **daily close** above the 20-day high (avoids intraday fakeouts) — or on a stop-order at high + 0.1×ATR for aggressive fills |
| Initial stop | Below the breakout bar's low, or entry − 2×ATR(10), whichever is tighter but not inside the base |
| Trailing exit | Exit on a close back below the 10-day Donchian low (chandelier-style trend follow) |
| False-break guard | If price closes back *inside* the range within 2 bars, exit immediately (−0.5R or less) |

### Position sizing (the Turtle method, adapted)

The Turtles sized by volatility so every position risked the same fraction of capital regardless of the instrument's noise. Adopt it:

Position size = (Risk% × Capital) / (2 × ATR(10) × point value)

with Risk% = 0.5–1.0% per trade. This automatically gives you smaller positions in wild instruments (Bank Nifty) and larger in calmer ones (Nifty), equalising risk.

## Worked India example

Reliance has spent eleven weeks grinding in a tight ₹2,780–₹2,900 box after a big prior run — a textbook high-tight base. ATR has been steadily contracting; the Bollinger bands are pinched (squeeze). The 20-day Donchian high sits at ₹2,900.

On a Tuesday, a strong results reaction drives the stock to close at ₹2,948 — a decisive close above the ₹2,900 line. Volume prints 2.1× the 20-day average (well past the 1.5× filter). Every condition aligns:

- Close above 20-day high (₹2,948 > ₹2,900). ✔
- Prior ATR contraction / squeeze. ✔
- Volume 2.1× average. ✔

**Entry:** buy on the close at ₹2,948 (or next-open). Say ₹10 lakh capital, 1% risk = ₹10,000.
- ATR(10) ≈ ₹45. Initial stop = entry − 2×ATR = 2,948 − 90 = ₹2,858 (comfortably below the breakout, back inside the base — a close there means the breakout failed).
- Point (rupee) risk per share = 2,948 − 2,858 = ₹90.
- Size = ₹10,000 / ₹90 ≈ 111 shares (round to the F&O lot / cash quantity you can hold). Notional ≈ ₹3.27 lakh.

**Management:** the stock follows through, running to ₹3,150 over three weeks. You trail using the 10-day Donchian low, which ratchets up to ₹3,020, then ₹3,090. When a pullback finally closes below the 10-day low at ₹3,080, you exit. Result: in ≈ ₹90 risk you captured ₹132 (2,948 → 3,080) — roughly +1.5R, and if the trend had extended further, more. The system's whole profitability rests on these occasional multi-R runners paying for the losers.

**The false-break case you must budget for:** an alternative Tuesday, Reliance pokes to ₹2,915 intraday but *closes* at ₹2,884 — back inside the box. Because your rule requires a *close* above ₹2,900, you never entered. That single rule — close-based confirmation — filters out a large fraction of the intraday bull traps that punish naive stop-order breakout buyers. And in the case where you *did* enter on a close of ₹2,948 but the next two days collapsed back to close ₹2,870 (inside the range), your false-break guard fires: exit immediately for a small loss (~−0.5R), long before the −1R stop.

## The opening-range breakout (intraday variant)

For Bank Nifty day-traders, the ORB is a workhorse. Rules:

| Parameter | Value |
|---|---|
| Opening range | High/low of the first 15 minutes (9:15–9:30) |
| Trigger | Break of the 15-min range high (long) / low (short) with a 5-min close beyond |
| Filter | Range width must be "normal" — skip if the first 15-min range is already >1.2× the typical ORB (day already exhausted) |
| Stop | Opposite side of the opening range |
| Target | 1× to 2× the opening-range width, or trail with a 5-min swing |
| Time stop | Flat by 3:00 pm; no new ORB trades after 1:00 pm |

Bank Nifty's opening range on a typical day might be 200–350 points; a clean break with a 5-min close, on above-average early volume, targets a 1–2× extension. The India-specific caution: weekly-expiry-day ORBs are distorted by option gamma and often mean-revert into the range — trade the ORB more selectively on expiry days.

## Backtest / edge notes & realistic costs

Breakout / trend-following systems have a *characteristic, uncomfortable* return profile that you must internalise before trading one:

- **Low win rate.** Real breakout systems win only ~35–45% of trades. Most breakouts fail or fizzle. You will be wrong more often than right.
- **Large winners, small losers.** Profitability comes entirely from asymmetry: the average winner is 2–4× the average loser. A handful of big trends per year (or per instrument) carry the whole equity curve.
- **Painful drawdowns and long flat stretches.** In range-bound years the market hands you a string of small breakout losses ("chop"). This is the tax you pay to be present for the big moves. Turtles endured 30–50% drawdowns; you must size so your version is survivable.

**Costs.** Swing breakouts are held days-to-weeks, so per-trade cost drag is modest, but the *low win rate means many trades*, so total costs add up. STT, slippage on the breakout bar (you're buying strength, often into a fast move, so expect adverse fills), and the bid-ask on stock options all matter. Realistic modelling: assume you get filled 0.1–0.3% worse than the trigger on liquid names, worse on illiquid ones — which is another reason to restrict the universe to the top ~40 F&O stocks and the indices.

**The core honesty:** breakout systems do not "predict." They accept being wrong most of the time in exchange for open-ended right-tail capture. If you cannot psychologically tolerate a 40% win rate and choppy losing streaks, you will abandon the system in exactly the flat period that precedes the big trend — which is how most people manage to lose money with a positive-expectancy system.

## Adaptations for NSE / F&O

- **Options to cap the false-break bleed.** Express a stock breakout with a *call debit spread* rather than futures: defined risk on the many false breaks, still strong participation on the runners, and cheaper than an outright call because a breakout doesn't need deep OTM lottery payoffs.
- **Gap handling.** Indian stocks gap hard on results. A breakout via an overnight gap above the level is common; decide in advance whether you chase gaps (higher slippage, some real trends) or require a normal close-through. Many pros take only gaps of moderate size and skip the 8%+ exhaustion gaps.
- **Index vs stock.** Index breakouts (Nifty/Bank Nifty) are cleaner and more liquid but produce fewer big multi-R runs than a strong single-stock trend; run both — the index for reliability, stocks for the occasional 3–5R monster.
- **Sector confirmation.** A stock breakout backed by its whole sector breaking out (e.g. a metal stock breaking with Nifty Metal breaking) has dramatically better follow-through odds.

## Confluence — separating real breaks from traps

- **Volume + breadth:** a break on heavy volume with the broader market and the stock's sector also strong is the highest-quality setup. A break on thin volume against a weak tape is a trap in waiting.
- **Volatility squeeze precedes expansion:** the best breaks come *out of* contraction (NR7, Bollinger squeeze). A break after price is already extended and volatile is late.
- **Retest holds:** many pros wait for the break, then buy the *retest* of the broken level as new support — fewer false signals, at the cost of missing the runaway ones that never retest. Choose your temperament.
- **Relative strength:** a stock making a new high while the index is only mid-range (leading the market) breaks out with the most conviction.

## Pitfalls

- **Chasing intraday pokes.** Buying a level the instant it's touched, with no close confirmation, is the fastest way to feed the trap-setters. Require a close (or a 5-min close intraday).
- **Widening stops after entry.** "It'll come back" turns a small −1R into a base-destroying loss. The false-break guard and hard stop are the system.
- **Over-sizing to compensate for the low win rate.** The single most common breakout-trader death: increasing size to "make back" a losing streak, then getting a normal-sized false break at 3× size. Fixed 0.5–1% risk, always.
- **Trading every base.** Not all bases resolve up. Demand the squeeze + volume + trend-alignment confluence; skip the low-quality setups even though it means fewer trades.
- **Quitting in the chop.** The flat, frustrating losing streak is *structural* and usually *precedes* the payoff trend. Abandoning the system there is self-sabotage.
- **Ignoring regime.** In a violently mean-reverting, headline-whipsawed market (news-driven chop), breakouts fail at an elevated rate. A simple regime read — is the index itself trending or ranging? — should throttle your aggression.

## Interview-ready summary

Breakout systems monetise the market's tendency to spend most of its time ranging and then escape into trends that produce the bulk of total return. The core rule set — Donchian/Turtle DNA — is: identify a tight base (volatility contraction, Bollinger squeeze, NR7), buy a *close* above the 20-day high (or the opening-range high intraday) confirmed by volume ≥ 1.5× average, place a stop just back inside the base (entry − 2×ATR), size by volatility so each trade risks a fixed 0.5–1% of capital, exit false breaks immediately if price closes back inside within two bars, and trail real breaks with a 10-day channel to let winners run. On NSE you run it on Nifty, Bank Nifty and the top ~40 F&O stocks — via futures, or via call debit spreads to cap the cost of the many false breaks. The defining, non-negotiable honesty is the return profile: a low win rate (~40%), small frequent losers, and a handful of large asymmetric winners that carry everything — which means the system's real edge is not the signal but the *discipline* to take every setup, cut every failure small, size for survivable drawdowns, and never quit during the choppy flat periods that structurally precede the big trends.
