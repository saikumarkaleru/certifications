# Intraday Tactics: Entries, Stops, Targets, Time-of-Day

## Why this matters

A good system (ORB, VWAP, momentum) tells you *what* to trade. Tactics tell you *how* to execute it — where exactly to enter, where the stop truly belongs, how to scale out, and *when* in the session the setup is even valid. This is the layer where retail traders quietly lose the edge their system gave them: they enter late, place stops where everyone else's stops are (so they get hunted), take profit too early on winners and hold losers, and trade the dead noon hours out of boredom. The pro's edge is precision and time-awareness. The Indian session has a distinct rhythm — the open is violent, mid-day is a trap, the close is its own game — and trading each hour the same way is a slow bleed.

## The essentials

Session 09:15–15:30 IST. Rules/rates as of July 2026 — verify on NSE/broker.

**Time-of-day map (typical, not guaranteed):**

| Window | Character | What works |
|---|---|---|
| 09:15–09:20 | Auction noise, wild ticks | *Wait.* Don't trade the first print. |
| 09:20–10:30 | Highest volatility & volume; trends are born | ORB, gap-and-go, momentum — your best window |
| 10:30–11:30 | First trend matures or reverses | VWAP pullback entries, trend continuation |
| 11:30–13:30 | **Mid-day chop** — thin, range-bound, stop-hunts | VWAP mean-reversion *only*; mostly sit out |
| 13:30–14:45 | Trend resumes / afternoon move | continuation, VWAP trend |
| 14:45–15:20 | Positioning into close; MTM squaring | close-momentum plays for pros; no fresh late entries for beginners |
| 15:20–15:30 | Square-off scramble | exit intraday; avoid new risk |

**Entries — be precise:**
- Enter on the **break-and-close** of your level (5-min close), or on a **retest** of the broken level (lower risk, sometimes you miss). Never chase 0.4% *after* the move.
- Use **limit or stop-limit** orders near your level; market orders on illiquid names bleed the spread.

**Stops — where they belong:**
- Put the stop where the *setup is proven wrong*, not at a round rupee amount. For an ORB long, that's below the range/breakout candle. For a VWAP long, below VWAP.
- Avoid the **obvious cluster** (exactly at the round number or the visible swing low) — market-makers hunt those. Give it a few ticks of buffer.
- The stop defines your **rupee risk**, and rupee risk must be ≤1–2% of capital. Size the position *from* the stop, never the reverse.

**Targets & exits:**
- **Measured move** (range width projected) or **prior swing / VWAP band** as first target.
- **Scale out:** book half at 1st target (locks the trade to breakeven or better), trail the rest with VWAP or a moving stop. This beats all-or-nothing exits emotionally and mathematically.
- Move stop to breakeven only after a *real* buffer, not the instant you're 5 points green (that just gets you stopped on noise).

**Index vs stock behaviour:** Nifty/Bank Nifty are smoother, mean-revert more, and respect VWAP; single stocks trend harder and gap on stock-specific news but can be manipulated intraday and have wider spreads. RS leaders move *before* the index confirms.

## Worked example: a full session plan

Capital ₹3,00,000; max risk **1% = ₹3,000/trade.** Trading a liquid F&O stock, say Reliance (illustrative; **verify current F&O lot size on NSE** — say lot ~250, tick ₹0.05).

**09:15–09:30:** Reliance opens 2,940, prior close 2,935 (small gap up). Opening range: high **2,952**, low **2,930**. Nifty flat-to-green. I wait.

**09:41:** 5-min candle closes **2,955**, above range high, volume above the morning average, and Reliance is up +0.7% vs Nifty +0.2% (RS leader). **Long entry 2,956.**
- Stop below breakout candle low / range high: **2,944** (12 pts risk).
- Position size: ₹3,000 ÷ 12 = 250 shares = **1 lot.** Rupee risk ≈ 12 × 250 = ₹3,000. ✓
- Target 1: measured move = range width 22 pts → **2,977**; Target 2: trail with VWAP.

**10:05:** hits 2,977. **Book 125 shares** (+₹2,625 gross), move stop on the rest to **2,956 (breakeven).** Now the trade cannot lose.

**10:40:** trails up, VWAP rising under price. Trend stalls; trailing stop at **2,970** hit at 11:15 on the remaining 125 → +₹1,750 gross. **Total gross ≈ ₹4,375.**

Costs (intraday equity, sell-side STT 0.025% from 01-Apr-2026): on ~₹7.4 L turnover per side, brokerage (~₹40), STT ~₹185 on sell, exchange txn + SEBI + stamp + **18% GST** → all-in ≈ **₹450–550.** **Net ≈ ₹3,850.** One clean trade > 1% of capital, risking 1%.

**Mid-day 11:30–13:30:** market goes sideways, VWAP flat. **No trades** — I don't manufacture setups in chop. This is where the discipline is.

**No fresh entries after 14:45.** Done for the day after one A+ trade.

## How pros do it / common mistakes

**Pros:**
- Trade the **first 90 minutes** hard and the **noon hours** barely at all.
- Predefine entry/stop/target *in rupees* before clicking; the order is placed, not agonized over.
- **Scale out** to bank certainty and let a runner run.
- Accept 1–2 quality trades a day. Flat is a position.

**Retail mistakes / red flags:**
- **Revenge trading:** stopped out, immediately re-enter bigger to "get it back." This is how a ₹3,000 loss becomes ₹15,000. If you're angry, you're done for the day.
- **Over-trading the chop** — 8 trades between 12 and 1:30, all costs, no edge.
- Stops at round numbers / obvious lows → hunted.
- Widening the stop when price approaches it ("just give it room") — the cardinal sin.
- Booking winners at +₹500 but holding losers to -₹5,000 (inverted R:R).
- Moving to breakeven on 3 points of noise, getting shaken out before the real move.

## Checklist / drill

**Before each trade:** entry level ✓, stop level (where setup is wrong, buffered off the cluster) ✓, position size from rupee risk ≤1% ✓, target(s) + scale-out plan ✓, time-of-day appropriate ✓, R:R ≥ 2:1 after costs ✓.

**Hard rules card:**
- [ ] Max **2 losing trades** → stop for the day.
- [ ] Max **3 trades** total per session (beginner).
- [ ] No entries 09:15–09:20 or after 14:45.
- [ ] Never widen a stop. Ever.
- [ ] Never re-enter within 10 min of a stop-out (breaks the revenge loop).

**Drill:** For 10 sessions, log every trade with its *time-of-day bucket* and outcome. Tally net P&L by bucket. Almost everyone finds the 11:30–13:30 bucket is negative. Then simply stop trading that window — an instant edge with zero new skill.

*Rates, lot sizes, and rules as of July 2026 — verify on NSE/your broker/SEBI; they change.*
