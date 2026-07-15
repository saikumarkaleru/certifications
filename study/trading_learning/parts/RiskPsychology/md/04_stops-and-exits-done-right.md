# Stops & Exits Done Right

## Why this matters — the pro vs retail gap this closes

Retail traders obsess over entries — the perfect candlestick, the exact indicator cross. Pros know the uncomfortable truth: **exits determine your P&L far more than entries.** Two traders can take the identical entry; one exits at +0.3R in fear, the other lets it run to +3R and cuts losers at −1R — over a year, one is broke and one is up. Your entry sets the *risk*; your exits set the *reward and the actual loss*. This chapter is about the machinery of getting out — hard, mental, trailing, time and structure stops — and the discipline that separates a plan from a hope.

## The essentials — types of stops and how to place them

**1. Hard stop (SL order at the exchange).**
A live stop-loss order resting on NSE/BSE. It executes without you. Use it whenever you cannot watch the screen, on overnight F&O, and on anything gap-prone. Downside: it's visible to the tape and can be triggered by a wick. Use **SL-Limit** to control fill price, but know a fast move can skip past a limit; **SL-Market** guarantees exit but not price.

**2. Mental stop.**
A level you'll act on manually. Only viable if you are disciplined *and* watching. The retail graveyard is full of "mental stops" that got widened at the moment of truth. For beginners: use hard stops.

**3. Trailing stop.**
Moves in your favour only, never against. Trail by a fixed distance, by ATR (e.g. 2×ATR), or by structure (below each higher-low in an uptrend). It locks in profit while giving the trade room. This is how you turn a +1R winner into a +3R winner.

**4. Time stop.**
"If the trade hasn't worked within X bars/by time T, exit." Essential for **intraday and options** where theta bleeds premium. A Bank Nifty option that's gone nowhere by 13:00 is costing you time-decay every minute — a time stop cuts dead trades before the stop-loss even triggers.

**5. Structure-based stops (the pro default).**
Place the stop where your *thesis is wrong*, from price structure — below the swing low, below the demand zone, beyond the breakout base — **not** at a round rupee amount or a fixed "20 points." Then size to that stop (previous chapter). Structure stops respect the market; arbitrary stops feed it.

**6. Avoiding stop-hunting zones.**
Liquidity clusters just below obvious swing lows and round numbers (Nifty 24,000; Bank Nifty 48,000). Placing your stop *exactly* at the obvious low invites the wick that takes you out before the move resumes. Pros place stops a **buffer beyond** structure (e.g. 0.2–0.3×ATR past the low), accepting slightly more risk to avoid being the liquidity.

**7. Scaling out & breakeven.**
- **Scale out:** book part (say half) at +1R or +1.5R, let the rest run on a trail. Reduces regret and smooths equity, at the cost of some upside.
- **Move to breakeven:** once price reaches ~+1R, trail the stop to entry so the trade can't become a loser. Do this *after* it has proven itself — moving to breakeven too early gets you wicked out of good trades.

## Worked example — a full exit plan

**Bank Nifty futures long. Capital ₹5,00,000, 1R = ₹5,000. Lot size 35 (verify on NSE — lot sizes change).**

- Entry: **48,000**, on a breakout above a base.
- Structure stop: last swing low **47,880**, plus a 40-point buffer beyond the obvious level → hard SL at **47,840** (160 points).
- Risk/lot = 160 × 35 = **₹5,600 ≈ 1.1R** → take **1 lot** (2 lots = 2.2R, too big).
- **Time stop:** if not up at least +40 points by 30 minutes, exit — the breakout failed to follow through.

**Managing the trade:**
1. Price reaches **48,160** (+160 pts = +1R). → **Scale out half** (book ~₹2,800 on part-size logic) and **move stop to breakeven 48,000.** Trade is now risk-free.
2. Price runs to **48,320** (+2R). → Trail stop under the new higher-low, say **48,180**, locking in profit.
3. Price hits **48,480** (+3R) then reverses; trail at 48,300 gets hit. → Exit remainder at **+2.6R.**

**Result:** blended ~ +1.8R to +2R (≈ +₹9,000–10,000 gross, less ~₹200 charges) instead of the retail outcome — panic-booking the whole thing at +0.4R (₹2,000) or, worse, widening the stop when it dipped and eating −2R. **Same entry, triple the result — purely from exit mechanics.**

## How pros do it / common mistakes

**Pros:**
- Define the exit plan (stop, target, trail rule, time stop) *before* entering, in writing.
- Use hard stops beyond structure with a buffer, not on the obvious level.
- Cut losers at exactly −1R, every time, no negotiation.
- Let winners run via trailing/structure stops; scale out to manage emotion, not to cap the trade prematurely.
- Use time stops on theta-decaying option longs.

**Retail errors & red flags:**
- **Widening the stop** as price approaches — converts −1R into −3R; the classic account-killer.
- **No stop at all** on naked option shorts — one gap = catastrophic loss.
- **Booking winners at +0.3R** (fear) while letting losers run (hope) — the exact inverse of an edge.
- **Stops on the obvious round number** — donating to the stop-hunt.
- Moving to breakeven *instantly*, getting wicked out, then watching the trade run without you.
- Ignoring theta: holding a flat option long "hoping" while premium bleeds to zero.

## Checklist / drill

**Exit checklist (write before entry):**
- [ ] Hard stop level from *structure* + buffer beyond the obvious low/high.
- [ ] Rupee risk at that stop ≤ 1R; size set accordingly.
- [ ] First target / scale-out level (≥ +1R) defined.
- [ ] Rule to move to breakeven (after ~+1R, not before).
- [ ] Trailing rule (ATR or structure) for the runner.
- [ ] Time stop for intraday/options ("out by HH:MM if flat").

**Drill:** For your next 15 trades, log the exit *reason* (hit stop / hit target / trailed out / time stop / discretionary panic). Tally them. If "discretionary panic" appears more than twice, your exits — not your entries — are the leak. Fix that before touching your strategy. *You are paid for how you get out, not how you get in.*
