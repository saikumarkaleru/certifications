# Order Types & Execution

## Why this matters

Two traders can have the identical view and identical instrument and still get opposite P&L — because one fired a market order into a thin option and paid ₹4 of slippage per lot, while the other worked a limit and got filled at his price. Execution is not an afterthought; on the intraday and options timeframes where retail Indians actually trade, the *order type* is often the difference between a strategy that clears costs and one that bleeds. Your TA book told you where to enter. This chapter is how to *actually get there* on Zerodha Kite and similar terminals: every order type, its current status in 2026 (SEBI/exchanges have discontinued some), and when a pro reaches for each. Get this wrong and even a good signal loses money to slippage and rejected orders.

## The essentials

**Market order.** Fills immediately at the best available price(s), walking the book if size exceeds top-of-book. Guarantees *fill*, not *price*. Deadly in illiquid options and at the open/close. On very liquid instruments (Nifty near-month, index futures) it's fine for small size.

**Limit order.** Fills only at your price or better. Guarantees *price*, not *fill* — it may sit unfilled or partially fill. The default professional tool. A buy limit *below* LTP waits; a buy limit *at/above* the ask executes marketable-limit style (fills up to your cap, protecting against runaway slippage).

**Stop-loss orders.** Triggered orders that stay dormant until price hits your trigger:

- **SL (stop-loss limit):** trigger price + limit price. On trigger it sends a *limit* order. Risk: in a fast move price gaps past your limit and you're **not filled** — the stop fails to protect.
- **SL-M (stop-loss market):** trigger only; on trigger it sends a *market* order — near-guaranteed exit. **Note:** SL-M is **disabled for options** on Indian exchanges (has been for years, to curb freak trades); use SL with a wide limit for option stops. Verify current status on your broker — rules change.

**GTT (Good-Till-Triggered).** A broker-side (not exchange) instruction that watches price for up to ~1 year and places the order when hit. Great for delivery entries/exits and target/stop on positional trades. It is *not* a resting exchange order — it only fires when the trigger is met, and single/OCO (one-cancels-other) variants exist.

**AMO (After-Market Order).** Placed when the market is closed (roughly after 3:30 PM to before pre-open next day); queued and released into the next session (often at/after pre-open). Useful for people who can't watch the 9:15 open — but you take opening-price risk.

**Iceberg / disclosed quantity.** Splits a large order into smaller visible legs so you don't reveal full size and don't get front-run. Kite's "iceberg" slices one big order into a chosen number of legs. Disclosed quantity (DQ) shows only part of your resting limit in the depth. Exchange minimums apply.

**Bracket & Cover orders (current status — verify).** SEBI/exchanges **discontinued Bracket Orders (BO) and Cover Orders (CO)** for most cases around 2020 during margin reforms; some brokers offer limited CO. Do **not** build a strategy assuming BO/CO exists — confirm on your broker in 2026. The modern equivalent is a normal entry plus a **GTT/SL** for target and stop, or the broker's basket/OCO feature.

**IOC vs Day (validity).**

- **Day:** rests until end of session, then cancels if unfilled.
- **IOC (Immediate-or-Cancel):** fills whatever it can *instantly*, cancels the rest — no resting. Used by fast traders to avoid leaving a stale order in the book.

## Worked example

Bank Nifty weekly 52,000 CE, LTP ₹300, quotes: bid ₹299.5 / ask ₹300.5, lot 35 (verify lot on NSE — it changes). You want long.

- **Market buy 1 lot:** you lift the ask and possibly walk up — say average ₹300.8. Cost = 300.8 × 35 = **₹10,528**. You paid ~₹0.3–1.0 of slippage over LTP: on 35 qty that's ₹10–35 gone before the trade even breathes.
- **Limit buy at ₹300.0:** you may get filled if an offer drops to 300, or you wait. If the market ticks up without you, you miss — but you never overpay. On a scalp where edge is ₹8–10, this discipline is the trade.
- **Stop:** you decide to exit if premium hits ₹250. SL-M is *blocked for options*, so you place an **SL** with trigger ₹252 and limit ₹245 (wide enough to fill in a fast drop). If you'd set the limit at ₹250 exactly and it gapped to ₹244, you'd sit unfilled and bleed.
- **Target via GTT:** set a single GTT sell at ₹360 so you don't babysit the screen.

Entry on Kite: select instrument → Buy → Quantity 35 → Product NRML/MIS → Order type LIMIT → Price 300 → Validity DAY → place. For the stop, a second order: Sell → SL → trigger 252 → limit 245.

## How pros do it / common mistakes

- **Default to limit; use market only in deep liquidity for small size.** In options and midcaps, market orders are a slippage tax.
- **Use marketable limits** (buy limit a tick or two above ask) to get near-instant fills *with* a price cap — best of both.
- **Know your stop's failure mode:** SL (limit) can miss in a gap; on options where SL-M is banned, set the limit generously below the trigger.
- **Don't assume BO/CO exist** — build target/stop with GTT/SL. Verify order-type availability on your broker for 2026; SEBI changes these.
- **Classic mistakes:** market order at 9:15:00 into the opening imbalance; SL-limit set at the exact trigger (never fills in fast moves); forgetting AMO releases at the *open* (gap risk); leaving a fat resting limit that gets front-run instead of using iceberg/DQ.
- **Red flag:** repeated "order rejected — SL-M not allowed" means you're using the wrong stop type for options.

## Checklist / drill

- [ ] Liquidity check: is the **spread** tight enough that a market order is safe? If not, **limit**.
- [ ] Chosen **stop type** correct for the segment (no SL-M on options)?
- [ ] Stop **limit set wide** enough to fill in a fast move?
- [ ] Target/stop placed as **GTT/OCO** so I'm not glued to the screen?
- [ ] **Validity** right — Day vs IOC — for my intent?
- [ ] For big size: **iceberg/DQ** to avoid showing my hand?

**Drill:** on paper (or a tiny 1-lot live), place the same entry three ways — market, limit-at-LTP, marketable-limit — and record actual fill price vs LTP for each across five trades. Tally the slippage. You will see, in rupees, why pros live on limits. (Costs/rules 2026 — verify on your broker; they change.)
