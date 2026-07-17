# Supertrend & Parabolic SAR

## What it is & why it works

Supertrend and the Parabolic SAR belong to the same family: **volatility-based trailing-stop-and-reverse (SAR) systems** that live directly on the price chart and are, at every instant, either long or short. There is no neutral. They print a single line (or a series of dots) that sits *below* price in an uptrend and *above* price in a downtrend, flipping sides only when price closes through it. That flip is both an exit from the old side and an entry into the new. Because the line is derived from volatility, it self-adjusts — it hugs tight in calm markets and gives more room in violent ones.

Supertrend is the more popular of the two in Indian retail and prop desks — it is the default overlay on almost every Zerodha Kite, Upstox, TradingView and Chartink chart you will see traded on Nifty and Bank Nifty. Its logic is built on the **ATR (Average True Range)**: the line is anchored a fixed number of ATRs away from a mid-price band, and it *ratchets* — in an uptrend the line can only move up or hold, never fall, so it behaves like a mechanical trailing stop that locks in trend gains and never loosens.

The Parabolic SAR (Stop And Reverse), Wilder's 1978 creation, achieves the same "always in the market, trailing stop" behaviour by a different mechanism: an **accelerating** dot series. The dots start slow after a reversal and speed toward price as the trend extends, on the theory that a healthy trend should keep making new extremes; when it stalls, the accelerating dots catch price and flip. The parabola shape — dots curving faster and faster toward price — is where the name comes from.

Why do they work? Because trends persist more often than random, and the hardest discipline in trend-following is *staying in* and *knowing when to leave*. Both tools mechanise that discipline. They convert the fuzzy question "is the trend still on?" into a hard, objective line: price above it → long; price below → short. They remove the temptation to exit early on a wiggle (the line gives volatility-scaled room) and remove the temptation to overstay (the line eventually catches you). The market behaviour they exploit is **trend continuation punctuated by regime change** — and their fatal flaw, correspondingly, is the *range*, where there is no trend to follow and the line flips back and forth, chopping the account.

## The mechanics

**Supertrend.** Two parameters: the ATR **period** (default 10) and the **multiplier** (default 3). Construction:

```
HL2         = (High + Low) / 2                     (the basic mid-price)
Basic Upper = HL2 + (Multiplier × ATR)
Basic Lower = HL2 − (Multiplier × ATR)
```

These basic bands are then made "sticky" so the line only tightens, never loosens, within a trend:

- **Final Upper Band** = if Basic Upper < previous Final Upper *or* previous close > previous Final Upper, then Basic Upper; else keep previous Final Upper.
- **Final Lower Band** = if Basic Lower > previous Final Lower *or* previous close < previous Final Lower, then Basic Lower; else keep previous Final Lower.

The **Supertrend line** itself is whichever band is active:
- If the trend is **up**, Supertrend = Final Lower Band (line under price).
- If the trend is **down**, Supertrend = Final Upper Band (line over price).
- The trend **flips to down** when close crosses below the Final Lower Band; **flips to up** when close crosses above the Final Upper Band.

The key behaviours: the line is `Multiplier × ATR` away from mid-price, so **wider ATR = wider line = more room**; and the ratcheting rule means in an uptrend the lower band can rise or hold but never fall, so your effective stop only improves.

Tuning the two knobs is the whole game:

| Setting | Behaviour | Best for |
|---|---|---|
| (10, 3) default | Balanced | Daily Nifty/stocks, positional |
| (7, 2) or (7, 1.5) | Tight, sensitive, flips fast | 5–15 min intraday scalps |
| (10, 2) | Moderately tight | Intraday swing |
| (14, 3) or (10, 4) | Wide, few flips, rides long | Strong daily/weekly trends |

Lower multiplier and period → more signals, earlier entries, more whipsaws. Higher → fewer, later, cleaner signals that ride longer but give back more at turns.

**Parabolic SAR.** Parameters: the **Acceleration Factor (AF)** start (default 0.02), step (0.02) and max (0.20). The recursion:

```
SAR_tomorrow = SAR_today + AF × (EP − SAR_today)
```

where **EP** (Extreme Point) is the highest high reached so far in the current uptrend (or lowest low in a downtrend). Each new extreme bumps AF up by the step (0.02) to a cap of 0.20 — that is the "acceleration": the more the trend extends, the faster the dot chases price. When price crosses the SAR, the system **reverses**: SAR resets to the prior EP, AF resets to 0.02, and the dots flip to the other side. Two safeguards: SAR can never move into the current or prior bar's range (it can't jump ahead of price), and a new extreme resets EP.

The practical contrast: **Supertrend gives constant volatility-scaled room (multiplier × ATR); Parabolic SAR gives shrinking room** as the trend ages, because the accelerating AF pulls the dot ever closer to price, so SAR exits trends earlier and is far twitchier in ranges. Most Indian traders prefer Supertrend for exactly this reason, using SAR as a secondary confirmation.

## Reading it — a worked Nifty example

Nifty daily, using Supertrend (10, 3). Assume Nifty has been trending up and Supertrend has been a rising line beneath price for two weeks, currently at **23,650** while spot trades 24,100 — the line is roughly `3 × ATR` (ATR ≈ 150, so ≈450 points) below price, and it has ratcheted up steadily, each day either rising or holding.

**Phase 1 — riding.** Price pulls back intraday to 23,900, then 23,780 — both above the 23,650 line, so no flip; the trend stays long and you hold. Note how the line's ratchet means even though price dipped, the stop never loosened; it sat firm at 23,650 having locked in earlier gains. This is Supertrend doing its core job: absorbing normal pullback noise (a 450-point buffer scaled to current volatility) without shaking you out.

**Phase 2 — the flip.** A weak global session gaps Nifty down and it *closes* at 23,500, below the 23,650 line. Supertrend flips: the line jumps to *above* price (to the Final Upper Band, say 24,050) and turns red; the system is now short from ~23,500. Crucially the signal is on a **close**, not an intraday poke — an intraday spike to 23,600 that recovers to close at 23,800 would *not* flip the line. This close-based rule is what stops most false flips.

**Phase 3 — the new downtrend.** Over the next week Nifty falls to 22,900. The Supertrend line ratchets *down* from 24,050 to 23,300, staying above price, giving the short room while locking in the decline. ATR expanded during the fall (volatility rose), so the line sat a bit wider — the tool automatically loosened to accommodate a faster market.

**Phase 4 — the range trap.** Suppose instead of trending, Nifty then chops between 22,900 and 23,300 for two weeks. Now Supertrend becomes a menace: price closes at 23,320 (flip to long), then 22,950 (flip to short), then 23,280 (flip long) — three whipsaw flips in eight sessions, each a small loss plus costs. Overlaying Parabolic SAR here would be even worse: the SAR dots would flip almost every bar. This phase is the honest lesson — **these tools are trend tools; in a range they systematically lose**, and the fix is not a better setting but a *regime filter* (see Confluence) that switches them off.

## Trading it

**Core mechanical system (Supertrend).** Long when price closes above the line and it turns green; the line *is* your trailing stop — exit and reverse short when price closes below it. Because it's stop-and-reverse, you are always in a position. Most discretionary traders soften this: they *take* the entry signal but manage exits with additional logic rather than blindly reversing on every flip.

Concrete Nifty trade on the Phase-2 flip:
- **Entry:** short on close at 23,500 when the line flips above price.
- **Stop:** the Supertrend line itself — 24,050 initially (≈550 points). The stop is dynamic; as the line ratchets down each day, so does your risk.
- **Target / management:** trail with the line. As Nifty falls to 22,900, the line drops to 23,300, then lower. You give back one ATR-band at the eventual reversal but capture the bulk of a ~600-point move against a defined risk. There is no fixed profit target in a pure Supertrend trade — the tool's philosophy is "ride until the flip."

**Scenario A — clean trend:** the flip leads into a sustained move; you ride the line for the whole leg, exiting only on the reverse flip. Best case; this is where the system earns its keep.

**Scenario B — immediate whipsaw:** you short at 23,500, price closes back at 23,700 two days later, flipping you long for a ~200-point loss. Unavoidable with a raw system; the defence is the ADX/regime filter and position sizing, not prediction.

**Scenario C — partial-book hybrid:** enter on the flip, book half at a measured target (e.g. 1.5× initial risk) and trail the rest on the Supertrend line. This smooths the equity curve and is how most desks actually run it, sacrificing some runner upside for fewer full-round-trip give-backs.

**Parabolic SAR usage:** best as a *trailing stop for an already-established position* rather than a standalone entry engine, precisely because its accelerating dots exit trends early. Many traders enter on another signal and trail the runner with SAR dots, exiting when a dot is breached — capturing the meat of a trend while the acceleration protects late-stage gains.

## Confluence

The single most important companion is a **trend/range filter — ADX**. Run Supertrend or SAR *only when ADX > 20–25*; when ADX is below 20, disable them entirely, because that is the range regime where they whipsaw. This one filter transforms Supertrend from a coin-flip into a genuine edge. On Bank Nifty intraday, gating Supertrend (7, 2) signals by ADX>20 cuts the majority of losing chop trades.

**Supertrend + moving average.** Take Supertrend long signals only when price is above the 50- or 200-EMA (i.e. trade the flip only in the direction of the higher-timeframe trend). A green Supertrend flip *below* a falling 200-EMA is a counter-trend bounce to distrust. This higher-timeframe alignment is the cheapest quality upgrade available.

**Multi-timeframe Supertrend.** A robust desk technique: use Supertrend on two or three timeframes (e.g. daily for bias, 15-min for entry). Go long on the 15-min flip only when the daily Supertrend is also green. This filters intraday noise against the dominant trend.

**Supertrend + option-chain / OI (the F&O layer).** For a Bank Nifty or Nifty intraday trader this is where confluence pays. A Supertrend buy flip that coincides with **call writers unwinding at the nearest strike** (call OI falling as price rises — short-covering fuel) and **fresh put writing at the strike below** (support being built) is a high-conviction long: price action, the trailing system and options positioning all agree. Conversely, a Supertrend flip *into* a heavy OI wall — e.g. a bullish flip right beneath a strike with massive call open interest acting as resistance — is a low-quality signal likely to stall and reverse; the option chain warns you the flip is running into a ceiling. On expiry day, when max-pain pinning and gamma flatten price into a range, both Supertrend and SAR misfire badly — the OI structure (huge writing at ATM) itself signals "range, switch these tools off."

**Supertrend + ATR/structure for stops.** Since Supertrend *is* an ATR construct, it pairs naturally with ATR-based position sizing: the distance from price to the line is your risk in points, so lots = (rupee risk budget) ÷ (points to line × point value). Wider line (high ATR) → fewer lots.

## Pitfalls & false signals

**The range is death.** Both systems are pure trend tools and *systematically lose in sideways markets* — repeated flips, each a small loss plus brokerage, STT and slippage that compound. This is not fixable by tuning; it requires a regime filter (ADX) to switch the tool off. Never run a naked Supertrend/SAR system through a chop without a filter.

**Curve-fitting the settings.** It is trivially easy to optimise the multiplier/period on past data so every flip looks perfect in hindsight, then watch it fall apart live. Stick to robust defaults (10, 3 daily; 7, 2 intraday) and change them only with out-of-sample evidence. A setting that only works on one instrument in one period is a mirage.

**Lag at reversals — you always give back a band.** By design, Supertrend exits `multiplier × ATR` after the top, so you never sell the high; you return roughly one full band at every turn. That give-back is the price of staying in the trend — accept it, don't try to pre-empt the flip, or you forfeit the tool's whole benefit.

**Parabolic SAR in low-volatility drift.** SAR's acceleration makes it flip constantly in slow, quiet, gently-drifting markets — it needs strong, persistent trends to shine and is notoriously bad in choppy or gently ranging conditions. Don't use SAR as a primary entry in a low-ATR environment.

**Intraday-close ambiguity.** Supertrend flips on close — but "close" of *which* bar? On a 5-min chart a flip can appear then vanish as the bar finishes. Always act on the *completed* bar's close; acting on an unclosed bar is a common source of phantom signals.

**Gaps and events.** Budget day, big earnings and expiry gaps can flip the line on an open that immediately reverses. Filter signals around known events, or size down.

**Blindly reversing.** The pure "stop and reverse" rule keeps you always in the market — including into obvious chop. Most professionals do *not* auto-reverse; they take the exit but require independent confirmation (structure, ADX, OI) before entering the opposite side.

## Interview-ready summary

"Supertrend and Parabolic SAR are volatility-based trailing stop-and-reverse systems — a single line on the chart that's below price in an uptrend and above it in a downtrend, flipping only on a close through it, so you're always either long or short. Supertrend anchors the line a multiplier times ATR from mid-price (default 10, 3) and ratchets so the stop only tightens; that's why it's the retail standard on Nifty and Bank Nifty in India. Parabolic SAR does the same job with accelerating dots that chase price faster as the trend ages — great as a trailing stop, twitchier as an entry. Both exploit trend persistence and both die in ranges, giving repeated whipsaw flips. So the non-negotiable companion is a regime filter: I only trust Supertrend when ADX is above 20–25, align it with the higher-timeframe EMA and, on Nifty F&O, confirm the flip against option-chain OI — a buy flip with call-writers unwinding and fresh put-writing below is high conviction; a flip into a call-OI wall I fade. The line is my trailing stop, so risk is objective and I trail rather than target. The honest caveat: I always give back one ATR-band at the turn — that's the cost of staying in the trend, and it's a probabilities game, not a certainty."
