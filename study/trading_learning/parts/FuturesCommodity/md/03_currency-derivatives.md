# Currency Derivatives (USDINR & Cross Pairs)

## Why this matters

Almost every retail F&O trader ignores the currency segment, then wonders why their imported-input stock, their IT exporter, or their gold trade moved "for no reason." The reason was usually USDINR. Currency derivatives are the cleanest, most macro-driven market on NSE — no company-specific noise, tight spreads, small lot sizes (₹1,000 per lot notional-per-point is tiny), and the rupee's slow, trending, RBI-managed behaviour makes it a distinct skill from index scalping. The pro uses currency futures for two things: a low-cost macro expression (view on the dollar, crude, or flows) and a genuine hedge for real forex exposure. This chapter covers what the options/TA books never touch — the FX-specific mechanics and drivers.

## The essentials

*(As of Jul 2026 — verify on NSE currency-derivatives page/SEBI/RBI; rules change.)*

**Pairs & specs.** NSE offers futures and options on **USDINR, EURINR, GBPINR, JPYINR**, plus USD cross-pairs (EURUSD, GBPUSD, USDJPY).

| Item | USDINR future |
|---|---|
| Lot size | **USD 1,000** |
| Quotation | ₹ per 1 USD (e.g. 83.50) |
| Tick size | **₹0.0025** (0.25 paise) → **₹2.50 per tick per lot** |
| 1 paisa move (₹0.01) | = **₹10 per lot** |
| Expiry | Monthly (+ some weekly); last **~2 working days before month-end** |
| Trading hours | **9:00 – 17:00** (note: longer than equity's 9:15-15:30) |
| Settlement | **Cash-settled in ₹**, referenced to the RBI reference rate |

Key contrasts with equity F&O:
- **Hours run to 5:00 pm** — currency keeps trading after the cash equity close, catching afternoon global cues.
- **Notional per lot is small** (USD 1,000 ≈ ₹83,500), so margins are a few thousand rupees — accessible, but don't over-lot to "make it interesting."
- **Purpose-restriction, historically:** SEBI/RBI have periodically required an **underlying exposure** for positions beyond a threshold (the "no naked FX beyond USD limit" rules of 2024). **Check the current per-client limit and any underlying-exposure declaration requirement with your broker before scaling up** — this rule has been tightened and loosened repeatedly.

**What drives INR:**
- **RBI action** — the RBI actively smooths the rupee via spot/forward intervention; INR trends more than it whips. Expect managed, one-directional drifts, not equity-style volatility.
- **Crude oil** — India imports ~85% of its crude; higher Brent = wider trade deficit = **rupee weakness** (USDINR up).
- **FII/FPI flows** — foreign buying of Indian equities/bonds brings dollars in → rupee strength; outflows → weakness. Watch the daily FII cash figure.
- **DXY (US Dollar Index)** — global dollar strength (Fed hikes, risk-off) lifts USDINR.
- **US-India rate differential & inflation** — structurally, higher Indian inflation implies gradual rupee depreciation over years (why USDINR trends up over the long run).

## Worked example — a USDINR trade

*(Illustrative.)* Brent has jumped from $78 to $88 and the Fed just signalled higher-for-longer (DXY rising). Both point to **rupee weakness** → you go **long USDINR**.

- Buy **10 lots USDINR July future @ 83.50**. Lot = USD 1,000 → notional = 10 × 1,000 × 83.50 = **₹8,35,000**.
- Margin at ~2-3% ≈ **₹20,000-25,000** blocked.
- **Move:** rupee weakens to **84.00** over two weeks (+0.50, i.e. +50 paise).
- P&L = 0.50 × 10 lots × (₹10 per paisa... careful) → per lot, ₹0.50 move = 50 paise × ₹10/paisa = **₹500/lot**; ×10 = **₹5,000**. Wait — recompute cleanly: ₹1 move on 1 lot = 1,000 USD × ₹1 = ₹1,000. A ₹0.50 move = **₹500/lot**; ×10 lots = **+₹5,000** on ~₹22,000 margin ≈ **+22%**.

**Costs** are low: no STT on currency derivatives (currency is outside the equity STT regime — verify), just brokerage + exchange txn + SEBI fee + **18% GST** + stamp duty. Round-trip on 10 lots is typically **under ₹100** — one of the cheapest segments on NSE.

**As a hedge instead:** a small exporter expecting **USD 10,000** in 60 days fears the rupee *strengthening* (fewer rupees per dollar). They **sell 10 USDINR futures @ 83.50**, locking the rate. If USDINR falls to 82.50, their export receipt is worth ₹10,000 less per rupee move... the future gains ₹1 × 10 lots × 1,000 = **+₹10,000**, offsetting the lower conversion. Risk removed for a few thousand in margin.

## How pros do it / common mistakes

**Pros:**
- **Trade the macro thesis, not the tick.** USDINR moves in slow, RBI-managed trends — swing/positional horizons fit far better than 1-minute scalps.
- **Cross-check three drivers** (crude, DXY, FII flow) before a directional bet; when all three align, conviction is high.
- **Respect intervention.** When USDINR approaches a level the RBI has been defending, expect a wall — don't fight the central bank into a round number.
- **Use the extra hours** (till 5 pm) to react to European-session and afternoon crude moves the equity crowd misses.
- Use currency futures to **hedge real exposure** (foreign fees, remittances, export receipts) — the intended, low-cost use.

**Classic retail errors:**
- Over-lotting because margins are tiny — small notional per lot tempts 50+ lots and turns a calm market into a big P&L swing.
- Trading USDINR like Bank Nifty — expecting 1% intraday whips that rarely come in a managed currency.
- Ignoring the **underlying-exposure / position-limit rules** and getting positions restricted or flagged.
- Forgetting that a *strong* equity rally (FII inflows) often means USDINR *drifts down* — currency and equity views must be consistent.

## Checklist / drill

Before a currency trade:
- [ ] Thesis names the **driver**: crude, DXY, FII flow, RBI, or rate differential.
- [ ] Checked all three of **crude / DXY / FII** for alignment or conflict.
- [ ] Confirmed **current lot size, tick value (₹10/paisa/lot)**, and margin.
- [ ] Sized so a normal move is a **pre-decided rupee risk** — resisted over-lotting.
- [ ] Checked **position limit / underlying-exposure** requirement with broker.
- [ ] Noted **RBI intervention zones** near round numbers.
- [ ] For a hedge: matched lots to actual **USD exposure** and the timeframe.

**Drill:** For 10 trading days, each morning log Brent, DXY, and the prior day's FII cash figure, then predict USDINR's direction for the day and mark it against the close. You'll quickly learn which driver is dominant in the current regime — that's the real skill in FX.
