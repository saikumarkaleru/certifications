# Corporate Actions & Events That Move Prices

## Why this matters

A corporate action is not a "news event" you react to — it is a mechanical, pre-scheduled change to the number of shares, the price, or the dividend. The exchange adjusts your position for you; the tape shows a price "gap" that isn't a real move. Retail traders lose money here in two silly ways: (1) they see a stock "crash" 50% on the ex-split date, panic, and sell into a non-event; or (2) they buy a stock *for* the dividend, not realising the price drops by exactly the dividend on the ex-date, and then pay tax on that dividend on top. Pros treat corporate actions as accounting, not alpha — but they *do* trade the second-order effects: the F&O ban list, index rebalancing flows, buyback tenders, and the volatility crush after results. This chapter covers the mechanics so you never get faked out, plus where the genuine edge lives.

(Rules and rates below are as of July 2026 — always verify on the NSE/BSE circular, your broker, and SEBI, because rules change.)

## The essentials

**Key dates.** Every corporate action has: the **record date** (you must be a shareholder on the depository — NSDL/CDSL — books this day to be eligible) and the **ex-date** (the first day the stock trades *without* the entitlement). With T+1 settlement (2026), the ex-date and record date are usually the **same day** — buy on or after the ex-date and you are *not* eligible. To be eligible you must buy on or before the day *before* ex-date.

| Action | What changes | Price effect on ex-date | F&O impact |
|---|---|---|---|
| **Cash dividend** | Company pays ₹X/share | Price drops ~₹X | Futures/strikes NOT adjusted for ordinary dividend; already priced in |
| **Stock split** | Face value cut (₹10→₹1), share count up | Price divides by ratio | Futures price & strikes adjusted by ratio; lot size scaled up |
| **Bonus** | Free shares (e.g. 1:1) | Price divides accordingly | Same — strikes/lot adjusted |
| **Rights issue** | Buy new shares at discount | Price drops toward ex-rights value | Adjusted via ratio factor |
| **Buyback** | Company repurchases shares | Support near buyback price | No direct F&O adjustment |

**Dividends and F&O.** NSE does *not* adjust futures or option strikes for **ordinary** dividends — the market already discounts them, and futures trade at a slight discount reflecting expected dividends. But for an **extraordinary dividend** (defined as >2% of the stock's market price), NSE *does* adjust strikes and futures on the ex-date. Know which one you're facing.

**Splits and bonuses** are pure re-denomination — your wealth is unchanged. NSE issues an adjustment circular: the futures price, every option strike, and the lot size are all rescaled so your position value is identical before and after.

**Results/earnings.** Not a corporate action, but the biggest scheduled single-stock event. Implied volatility ramps into the result and **crushes** immediately after (the "IV crush") — this is why buying naked options into results usually loses even when you guess direction right.

**Index rebalancing.** NSE reviews the Nifty 50 semi-annually. When a stock is added, index funds and ETFs must buy it (and sell the deleted one) at the close on the effective date — a large, forced, predictable flow.

**F&O ban ("securities in ban period").** When the market-wide open interest in a stock's derivatives crosses **95% of the market-wide position limit (MWPL)**, the exchange bans *fresh* positions — you may only *reduce* existing ones. Entering a new position in a banned stock attracts a penalty. Ban lists are published daily by NSE after market hours.

**F&O inclusion/exclusion.** SEBI's criteria (median quarter-sigma order size, market-wide position limit ≥ ₹1,500 crore, average daily delivery value, etc., as revised 2024–25) decide which stocks have derivatives. Exclusion forces traders to unwind — a slow bleed of open interest.

## Worked example — an ex-date adjustment on a bonus

Suppose **TATA-EX Ltd** (illustrative) trades at ₹2,400. Lot size 200 (contract value ₹4,80,000). The company declares a **1:1 bonus**, ex-date 20-Jul-2026. You hold **1 long futures lot** bought at ₹2,400.

On the ex-date NSE applies an adjustment factor of **2** (for 1:1, you get one extra share per share):

- **Adjusted futures price** = ₹2,400 / 2 = **₹1,200**
- **Adjusted lot size** = 200 × 2 = **400 shares**
- **New contract value** = ₹1,200 × 400 = **₹4,80,000** — identical.

Your P&L is untouched. The chart shows a "50% crash" from ₹2,400 to ₹1,200 — a data artifact, not a loss. Every option strike doubles in count and halves in price too: a ₹2,500 call becomes a ₹1,250 call with double the lots.

**Dividend contrast.** Now say instead the company pays an **ordinary dividend of ₹40** (1.7% of price — under the 2% threshold). Ex-date, the cash stock opens near **₹2,360** (₹2,400 − ₹40). NSE does **not** adjust the futures or strikes — because the futures already traded ~₹40 cheaper than "spot minus carry" in anticipation. A retail trader who shorted the future the day before "to catch the ₹40 drop" captures **nothing** net of costs: on a ₹4,80,000 futures short, STT on futures (~0.05% on sell, from 01-Apr-2026) alone is ~₹240, plus exchange txn charges, GST, and stamp duty — the "free ₹40" was never free.

## How pros do it / common mistakes

- **Never trade a dividend for the dividend.** Price drops by the payout and you pay tax on the dividend at slab rate. The classic retail "dividend capture" is a losing trade after STT and tax.
- **Don't panic on ex-split/ex-bonus gaps.** Confirm the NSE adjustment circular before assuming a real move. Your broker's average price should auto-adjust; if it doesn't, raise a ticket, don't sell.
- **Respect the F&O ban list.** Trying to enter a banned stock's futures/options gets rejected or penalised. Pros watch stocks *approaching* ban (85–95% MWPL) — entry into ban often marks a squeeze top or capitulation bottom because no fresh positions can be built.
- **Trade the rebalance flow, not the news.** Additions are usually leaked/anticipated; the real, mechanical buying is the closing auction on the effective date. Pros position ahead and exit into the forced flow.
- **Fear the IV crush, don't fight it.** Into results, option sellers (spreads, iron condors — from your options book) harvest the elevated IV; naked buyers usually donate it.
- **Buybacks:** a **tender-route** buyback at a premium to market has a defined **acceptance ratio** — retail shareholders get a reserved quota, often with high acceptance. This is a genuine, low-risk edge (buy in market, tender the reserved portion), but size it for the acceptance ratio, not 100% acceptance.

## Checklist / drill

Before you trade any single stock this week, run this:

1. **Any corporate action pending?** Check the NSE "Corporate Actions" page — dividend, split, bonus, rights, buyback, ex-date.
2. **Is the ex-date within my holding window?** If yes, will the "gap" be adjusted (split/bonus) or real-but-priced (dividend)?
3. **Extraordinary dividend (>2%)?** If yes, expect strike/futures adjustment.
4. **On the F&O ban list today?** Check NSE's daily ban list *before* placing a derivatives order.
5. **Results date?** If within 5 trading days, assume elevated IV and plan for the post-result crush.
6. **Index review due?** Note effective dates for Nifty/Bank Nifty reconstitution.

**Drill:** Pull last quarter's NSE bonus/split circulars for any three stocks. For each, write the pre- and post-adjustment futures price, lot size, and contract value, and confirm the contract value is unchanged. Do it until the "crash that isn't a crash" never fools you again.

*(All rates/thresholds as of July 2026 — verify on NSE/BSE circulars, SEBI, and your broker; rules change.)*
