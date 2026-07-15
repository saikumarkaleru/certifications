# Index & Stock Futures: Specs, Margin, Basis, Rollover

## Why this matters

You already know options cold. Futures feel simpler — one linear instrument, no Greeks — and that simplicity is exactly the trap. A futures position is *pure leveraged delta*: a 1% move against a fully-margined Nifty future is not a 1% loss, it's roughly a 6-8% loss on your blocked margin. Retail traders treat one Nifty future like "a bit of index exposure" and get liquidated on a gap. The pro treats it as a financing-and-carry instrument: they know the basis, they know the roll cost, and they never carry a naked future through an event without sizing for the *notional*, not the margin. This chapter closes the gap between "I bought a future" and "I understand what I actually own."

## The essentials

*(Specs as of Jul 2026 — lot sizes are revised by NSE every few months to keep contract value near SEBI's ₹15-20L band; always verify the current lot on the NSE contract-specification page before trading. Rules change.)*

| Item | Nifty 50 Fut | Bank Nifty Fut | Stock Fut (e.g. RELIANCE) |
|---|---|---|---|
| Underlying | Nifty 50 index | Nifty Bank index | Single stock |
| Lot size (verify) | 75 | 35 | Stock-specific |
| Tick size | ₹0.05 | ₹0.05 | ₹0.05 |
| Expiry | Monthly, last Thu* | Monthly, last Thu* | Monthly, last Thu* |
| Settlement | Cash | Cash | Cash (physical for stock F&O since Oct-2019 — you take/give delivery if held to expiry) |
| Contracts live | 3 (near/next/far month) | 3 | 3 |

\*NSE has been shifting weekly/monthly expiry days (Nifty monthly moved around Tue/Thu in 2024-25). **Confirm the exact expiry day on your broker's contract note.**

**Margin.** F&O margin = **SPAN + Exposure**, blocked upfront (SEBI peak-margin fully enforced since Sep-2021 — no "we'll collect later"). SPAN is the exchange's worst-case one-day loss model; Exposure is an extra buffer (~2-3% of notional). Total initial margin on an index future runs ~**12-15%** of contract value; a volatile stock future can be 20%+. That implies **~7x leverage** at most for index — not the 50x day-trading fantasy.

**Mark-to-market (MTM).** Every day the exchange settles your position to the daily settlement price. Gains are credited, losses are **debited from your ledger the same day**. If the debit takes your account below maintenance margin, you get a margin call and the broker can square you off. MTM is real cash flow, not a paper number.

**Basis and cost of carry.** Basis = **Futures − Spot**. In a normal market the future trades at a small *premium* to spot because of cost of carry:

> Fair Futures ≈ Spot × (1 + r × t/365) − Dividends

where r is the financing rate and t is days to expiry. As expiry approaches, basis decays toward zero (convergence). A future trading *below* spot (backwardation) usually signals heavy dividends, borrowing stress, or aggressive short-selling.

**Open Interest (OI).** OI = number of outstanding contracts. Rising price + rising OI = fresh longs (trend confirmation). Rising price + falling OI = short-covering (weaker). Read OI *with* price, never alone.

## Worked example — MTM + rollover in rupees

**Setup (illustrative).** You go long **1 lot Nifty July future** at **24,000**, lot size **75**.

- Notional = 24,000 × 75 = **₹18,00,000**.
- Initial margin at ~13% ≈ **₹2,34,000** blocked.

**Daily MTM:**

| Day | Settle | Move | MTM cash (₹) |
|---|---|---|---|
| Entry | 24,000 | — | — |
| Day 1 | 24,120 | +120 | +9,000 credited |
| Day 2 | 23,950 | −170 | −12,750 debited |
| Day 3 | 24,200 | +250 | +18,750 credited |

Net after 3 days = +200 pts = **+₹15,000** on ₹2.34L margin ≈ **+6.4%** on capital from a **+0.83%** index move. That is leverage working *for* you — and it works identically against you.

**The rollover (last week of July expiry).** You want to keep the long into August. You don't "extend" — you **close July and open August** simultaneously (a calendar spread order to control slippage):

- July future = **24,180** (near expiry, basis nearly gone).
- August future = **24,255** (premium = cost of carry for the extra month).
- **Roll spread = 24,255 − 24,180 = 75 points.**

Rolling costs you **75 × 75 = ₹5,625** in spread, *plus* transaction costs on 2 legs. That 75-point premium is your annualised carry: 75 / 24,180 over ~30 days ≈ **0.31%/month ≈ 3.7% p.a.** — a sanity check that the roll is priced fairly and not distorted by a dividend or funding squeeze.

**Costs on the July exit (sell side, per Budget-2026 STT effective 01-Apr-2026 — verify):**
- STT on futures ~0.05% on sell notional: 0.0005 × 18,13,500 ≈ **₹907**.
- Plus brokerage (flat ~₹20/order at discount brokers), NSE txn charge, SEBI fee, stamp duty, and **18% GST on brokerage + txn**. Round-trip all-in on a Nifty future is typically **₹40-60 per lot** ex-STT — small vs notional, but it compounds if you overtrade.

## How pros do it / common mistakes

**Pros:**
- **Size on notional, not margin.** Risk is on ₹18L of Nifty, not ₹2.34L. One future ≈ ₹18,000 P&L per 1% move — decide if that fits your risk *before* entry.
- **Watch the basis as a signal.** An unusually rich or negative basis tells you about funding, dividends, or one-sided positioning before price does.
- **Roll early, not on expiry day.** Liquidity is best 3-5 sessions before expiry; rolling on the last day means fat spreads and gamma-driven whipsaw.
- **Track cumulative roll cost.** A long-term index long paying ~4% p.a. carry must beat that just to break even — often a reason to prefer the cash-market or an ETF for pure buy-and-hold.

**Classic retail errors:**
- Confusing margin with risk ("I only put in ₹2.3L") — then a 2% gap wipes 15% of margin overnight via MTM debit.
- **Forgetting physical settlement on stock futures.** Hold a stock future to expiry and you're obligated to give/take *full-value delivery* — a ₹18L cash obligation on a lot you meant to trade for ₹500. Square off or roll before expiry.
- Ignoring MTM cash flow and getting an unexpected margin call mid-week.
- Trading illiquid far-month or small-cap stock futures where the spread eats the edge.
- Reading OI as a standalone buy/sell signal.

## Checklist / drill

Before every futures entry:
- [ ] Confirmed **current lot size** on NSE (they change).
- [ ] Computed **notional** and my P&L per 1% move — does it fit my risk?
- [ ] Checked **SPAN+Exposure** margin and that I have a **buffer for MTM debits**, not just entry margin.
- [ ] Looked at **basis** (Fut−Spot) — normal premium, or a red flag?
- [ ] Checked **OI + price** together for confirmation.
- [ ] Set a stop in *points* and know the rupee loss it implies.
- [ ] For **stock futures**: a hard reminder to square/roll before expiry to avoid physical delivery.

**Drill:** Paper-trade one full expiry cycle on one Nifty lot. Each evening, log the settlement price, the MTM cash, your running ledger, and the near-vs-next basis. In the last week, execute a simulated roll and record the exact spread cost in rupees and its annualised %. Do this once and futures mechanics stop being abstract.
