# The Order Book, DOM & Matching Engine

## Why this matters

Most retail traders watch a single number — the Last Traded Price — and imagine that's "the price." It isn't. Behind the LTP sits an order book: a live ledger of every resting buy and sell, stacked by price. The exchange's matching engine turns that book into fills using a rigid, public rule — **price-time priority**. Traders who can't read the book place limit orders that never fill, get shocked by slippage, mistake spoofed size for real support, and misjudge how much they can trade without moving price. Your TA book reads the *chart*; this chapter reads the *tape and depth* — the microstructure one level below the candle. On intraday and options timeframes, where the edge is thin, reading the DOM (Depth of Market) is a genuine pro skill that separates disciplined execution from donating to the spread.

## The essentials

**Bid, ask, spread.**

- **Bid** = highest price a buyer will pay right now.
- **Ask (offer)** = lowest price a seller will accept.
- **Spread** = ask − bid. To buy immediately you pay the ask; to sell immediately you hit the bid. The spread is a real, recurring cost — cross it twice per round trip.
- **LTP** = the price of the *last completed trade* — historical, between bid and ask. A rising LTP with buys lifting the ask is different from a rising LTP on one stale print.

**Market depth (Level-2 / 20-depth).** Indian exchanges publish the best five price levels on each side by default (Level-2). NSE also offers a **20-depth** feed showing 20 levels each side — pros use it to see size deeper in the book. Each row shows price, quantity, and (sometimes) number of orders.

**The matching engine — price-time priority.** Continuous auction. Rules:

1. **Price priority:** a better-priced order matches first (higher bid / lower ask).
2. **Time priority:** at the *same* price, the order entered *earlier* fills first (FIFO queue).

So a limit order joins the back of the queue at its price. A market/marketable order consumes the opposite side from the best price outward until filled. This is why a limit *at* the bid may sit forever behind a huge queue, while a limit *at* the ask fills instantly.

**How a fill happens.** When an incoming buy's price ≥ resting sell's price, they match at the **resting order's price** (passive order sets the price). Large incoming orders "walk the book," filling successive levels at worse prices — that's slippage, and the DOM lets you *estimate it before you click*.

**Iceberg / hidden size.** Some resting size is disclosed-quantity or iceberg: only a slice shows; as it fills, a fresh slice reappears at the same price. On the DOM this looks like a level that *keeps refilling* no matter how much trades through it — a clue that a big, patient player is there.

## Worked example — a depth snapshot

Nifty near-month future, tick ₹0.05, lot per current NSE spec (verify). Snapshot:

| Bids (buy) | Qty | | Asks (sell) | Qty |
|---|---|---|---|---|
| 24,600.00 | 1,800 | | 24,600.15 | 900 |
| 24,599.95 | 2,400 | | 24,600.20 | 1,500 |
| 24,599.90 | 3,100 | | 24,600.30 | 2,200 |
| 24,599.85 | 1,200 | | 24,600.40 | 1,700 |

- **Spread** = 24,600.15 − 24,600.00 = **₹0.15** (3 ticks) — reasonably tight.
- **Market buy 900:** lifts the ₹24,600.15 ask exactly (900 available) → fill at 24,600.15. No walk.
- **Market buy 2,000:** takes 900 @ 24,600.15, then 1,100 @ 24,600.20. Average ≈ 24,600.18 — you slipped ~₹0.03 past the touch. On a bigger order you'd walk further.
- **Limit buy 500 @ 24,600.00:** joins the *back* of the 1,800 already queued at the top bid. 1,800 ahead of you must trade first before you fill — you may wait, or the market moves away and you miss.
- **Reading intent:** the ₹24,599.90 level keeps refilling to ~3,100 after prints go through it — likely iceberg/large buyer; a possible short-term floor. But size can be pulled (spoof-like) — never treat displayed depth as a guarantee.

**Estimating impact before clicking:** sum ask quantities until they cover your order; the last price you touch is your worst fill. That's your pre-trade slippage estimate — a habit that saves real rupees.

## How pros do it / common mistakes

- **Pros read the spread and depth before choosing order type.** Tight spread + deep book → market for small size is fine. Wide spread + thin book → work a limit.
- **They estimate walk-the-book slippage** from the DOM for their size, especially in options where a 5-lot market order can jump two strikes' worth of ticks.
- **They watch the queue.** Joining a huge queue at the bid means low fill odds; a marketable limit jumps ahead at a tiny cost.
- **They treat displayed size skeptically.** Depth can be pulled in milliseconds; refilling levels *may* be real icebergs *or* bait. Confirm with the tape (actual prints), not just resting quotes.
- **Classic mistakes:** trading off LTP alone and ignoring the spread; placing a limit at the touch and assuming instant fill (you're behind the queue); reading a big single-level bid as guaranteed support; sizing a market order without checking how many levels it will eat.
- **Red flag:** in illiquid options, a 5-level DOM with tiny quantities and ₹2+ spreads — any market order there is a self-inflicted loss.

## Checklist / drill

- [ ] Note the **spread** (ask − bid) before every order — is it acceptable vs my edge?
- [ ] For my size, **sum the opposite-side depth** — how many levels will I walk?
- [ ] If placing a limit at the touch, **how big is the queue ahead** of me?
- [ ] Is a refilling level a real **iceberg** or spoof? Confirm on the tape.
- [ ] Thin/wide DOM → switch from market to **limit**.

**Drill:** open the 20-depth (or Level-2) on Nifty future and one illiquid stock option side by side for 10 minutes. For a hypothetical 3-lot market order on each, compute the expected average fill by walking the visible asks; note the spread. Compare the two instruments' impact cost in rupees. Repeat until estimating slippage from the DOM is automatic. (Market data/specs 2026 — verify lot and depth feed on NSE/your broker; rules change.)
