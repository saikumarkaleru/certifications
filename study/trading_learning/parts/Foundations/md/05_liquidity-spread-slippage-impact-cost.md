# Liquidity, Spread, Slippage & Impact Cost

## Why this matters

Most retail traders obsess over entry signals and ignore the tax that liquidity charges on every fill. That tax — the bid-ask spread, slippage on size, and impact cost — is invisible on a chart but very real in your P&L. A 40-tick edge means nothing if crossing the spread and moving the book costs you 15 ticks a round-turn. Pros treat liquidity as a first-class variable: they size to the book, not the other way around. The single biggest silent killer of retail option accounts is not being wrong on direction — it is trading illiquid strikes where the spread alone is 3–8% of premium, so you start every trade down several percent before the market has moved. This chapter closes the gap between "I bought it" and "I bought it at a price that leaves an edge."

## The essentials

**Bid, ask, spread, LTP.** The *bid* is the best price a buyer will pay; the *ask* (offer) is the best price a seller will accept. The gap is the *spread*. The *Last Traded Price (LTP)* is history — it tells you where the last trade printed, not where you can trade now. A market buy lifts the ask; a market sell hits the bid. If you only ever look at LTP, you will consistently be surprised by your fills.

**Depth (Market-By-Price).** Kite and most terminals show a 5- or 20-level depth window: quantity resting at each of the top five bids and five asks. Deep, evenly stacked book = liquid. A book where level 1 has 50 lots and level 2 gaps 3 rupees away = thin. Nifty and Bank Nifty near-the-money weekly options and the index futures are the deepest instruments on NSE; far OTM strikes, weekly options on single stocks, and illiquid cash stocks are where spreads explode.

**Volume vs Open Interest.** Volume is contracts traded today; OI is contracts outstanding. High volume = easy to get in and out. Low volume with wide spread = a trap.

**Impact Cost (NSE publishes this).** NSE literally computes and publishes *impact cost* per stock — the percentage cost of executing a defined order size (₹1 lakh for the Nifty basket) against the book, measured versus the mid-price. A stock qualifies for the Nifty 50 partly on having impact cost consistently under ~0.50%. Reliance or HDFC Bank might show impact cost of 0.02–0.05%; a small-cap might show 0.5–2%. This is the cleanest public liquidity metric in the Indian market — use it.

**VWAP / TWAP.** Volume-Weighted and Time-Weighted Average Price. Institutions benchmark their fills against VWAP; if you must trade size, slicing the order over time (TWAP) or along volume (VWAP) reduces impact versus one market order that eats five levels.

**Circuit limits / price bands.** NSE/BSE apply daily price bands (2%, 5%, 10%, 20%) on many cash stocks; F&O stocks and indices have dynamic bands and index-level market-wide circuit breakers (10%/15%/20% halt Nifty/Sensex). When a stock is stuck at upper/lower circuit there is *no* opposite-side liquidity — you cannot exit. Illiquid + circuit = trapped.

*(Rules as of July 2026 — verify on NSE/broker/SEBI; bands and lot sizes change.)*

## Worked example — the cost of crossing the spread

Take a **Bank Nifty weekly option**, lot size **15** (verify current lot on NSE — it has changed repeatedly). Say the 52000 CE shows:

- Bid ₹208.00 (qty 12 lots) / Ask ₹210.50 (qty 9 lots). LTP ₹209.
- Spread = ₹2.50, i.e. ~1.2% of premium.

You buy 5 lots at market → filled at ₹210.50. To exit immediately at market you hit ₹208.00. Round-turn spread cost = ₹2.50 × 15 × 5 = **₹187.50**, before a single charge and before the market moves. Add STT (~0.15% on sell premium, from 01-Apr-2026 — verify), exchange txn, SEBI, GST, stamp — realistically another ₹120–160. So you are down roughly **₹300+** the instant you're in, on 5 lots.

Now compare a **far OTM weekly** strike: bid ₹4.20 / ask ₹5.10. Spread ₹0.90 on a ₹4.65 mid = **~19%**. To break even the option must rise 19% just to cover the spread. This is why cheap OTM lottery tickets bleed: the spread eats you alive on entry and exit.

Contrast an **illiquid cash stock**: bid ₹742 (30 shares) / ask ₹749 (25 shares), spread ~0.9%. Buy 500 shares and you walk up through four levels — average fill ₹753, not ₹749. That extra ₹4 × 500 = **₹2,000 of slippage** from your own size. NSE's published impact cost for that stock would have warned you it was thin.

## How pros do it / common mistakes

**Pros:**
- Trade the **most liquid strike/instrument** that expresses the view — ATM/near-ATM index options, index futures — and avoid strikes with <1–2% spread.
- Use **limit orders at or inside the spread**, not market orders, unless speed is worth the tax.
- **Size to the book:** if level-1 ask has 9 lots, don't send 40 lots market.
- Check **NSE impact cost / average daily volume** before trading any cash name.
- Avoid the **first 1–2 minutes (9:15–9:17)** and the last minutes — spreads are widest and quotes gappy at the open.

**Retail mistakes:**
- Reading **LTP as if it's a tradeable price**.
- Buying **deep-OTM options** where the spread is 10–25% of premium.
- **Market orders on thin instruments**, then blaming the broker for a bad fill.
- Ignoring **circuit limits** and getting trapped with no exit.
- Averaging into an illiquid stock, then being unable to sell size without collapsing the price.

## Checklist / drill

Before any order, verify:
- [ ] Spread as a **% of price** (options: <2% near ATM; stocks: check NSE impact cost).
- [ ] **Depth at levels 1–3** covers my order size.
- [ ] **Avg daily volume** supports my intended size (rule of thumb: your order <1–2% of ADV).
- [ ] Not stuck near a **circuit band**; two-sided quotes exist.
- [ ] **Limit vs market** decided deliberately; market only when speed > cost.

**Drill:** For one week, before every trade, screenshot the depth window and record (a) mid-price, (b) your actual fill, (c) the round-turn spread cost in rupees. Sum it Friday. That number is your liquidity tax — most retail traders are shocked how large it is, and it changes which instruments you trade forever.
