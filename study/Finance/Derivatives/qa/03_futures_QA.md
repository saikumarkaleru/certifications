# Q&A — Futures Contracts

*Practice bank for Chapter 03. Every question is followed by a full answer. Work each one before reading the solution. Numerical answers are reconciled at least two independent ways.*

---

## Section A — Concept Check

**A1. In one sentence, what is a futures contract, and which single word separates it from a forward?**
A futures contract is an exchange-traded, standardised forward whose counterparty risk is removed by a central clearing house through daily mark-to-market and margining. The separating idea is *standardisation* — the exchange fixes everything except price, which is what creates fungibility, and fungibility is what makes liquidity, clearing and margining possible.

**A2. Which four problems of forwards does the future engineer away?**
Counterparty (default) risk, illiquidity, price opacity/search cost, and credit concentration. The future answers all four at once: novation and margining kill default risk; standardisation creates liquidity and an easy exit; the public order book gives price transparency; and central clearing with netting removes the web of bilateral IOUs.

**A3. What is novation and why does it leave the clearing house with no market risk?**
Novation is the legal splitting of one agreed trade into two contracts — buyer-versus-CCP and CCP-versus-seller — the instant it is struck. Because every long the CCP holds is matched by an equal short, its *net* market position is always zero. It therefore carries no directional (market) risk; its only exposure is the *credit* risk that a member defaults, which margin and a default fund cover.

**A4. Why does daily mark-to-market make the clearing house safe?**
In a forward, a loss builds silently for months, so the amount at risk on default grows large. MTM re-values every account each evening and moves the day's cash immediately, so the most a defaulter can owe is roughly *one day's* adverse move — a small figure the posted margin already covers. MTM converts one large, slow-building credit exposure into a stream of tiny, freshly-settled ones.

**A5. Distinguish initial, maintenance, and variation margin.**
Initial margin (IM) is the deposit required to open a position, sized to a worst-case one-to-two-day move. Maintenance margin (MM) is the floor, typically 70–80% of IM; breaching it is only the *trigger*. Variation margin is the cash top-up you must post when called — and it restores the account all the way back to **initial** margin, not merely back above maintenance.

**A6. State the cost-of-carry price and name the force that enforces it.**
$F_0 = S_0(1+r-q)^T$ (financial assets) or $S_0(1+r+u-y)^T$ for commodities with storage $u$ and convenience yield $y$. It is enforced by **arbitrage**: if the future is too rich you do cash-and-carry (buy spot, sell the future, carry to delivery); if too cheap, reverse cash-and-carry. Arbitrageurs trade until the gap closes.

**A7. Define basis, contango and backwardation.**
Basis = spot − futures ($S_0 - F_0$). When $F_0 > S_0$ (basis negative) the market is in **contango** — normal positive net carry. When $F_0 < S_0$ (basis positive) it is in **backwardation** — a convenience yield or supply squeeze. Contango is a statement about carrying costs, not a forecast of prices.

**A8. What is convergence and why must it happen?**
As expiry nears, $T \to 0$, the carry factor $(1+r-q)^T \to 1$, so $F_T \to S_T$ and basis → 0. It *must* happen because at the instant of expiry a future is deliverable spot; any gap would be an instant riskless arbitrage, so it cannot persist.

**A9. If futures and forwards have the same payoff, what actually differs?**
The *timing* of cash flows and the credit/margin plumbing — not the total P&L. A forward pays $S_T - F_0$ in one lump at maturity; a future pays it in daily MTM increments that *sum* to the same total. Add exchange vs OTC, standardised vs bespoke, CCP vs bilateral, and mandatory margin vs none.

**A10. What is basis risk?**
The uncertainty in the basis when a hedge is lifted *before* expiry. Convergence guarantees the basis is zero only *at* expiry; on any earlier date the basis is not perfectly predictable, so a hedge closed early carries residual risk. It is the main imperfection in real-world futures hedging.

---

## Section B — Numerical / Payoff Problems

### B1 — Margin account, day by day (with reconciliation)

A trader goes **long 1 crude oil future**. Lot = 1,000 barrels, quoted per barrel. Entry $F_0 = 80$. Initial margin = 10% of notional; maintenance = 75% of IM. Track four days.

**Setup.** Notional = 80 × 1,000 = **80,000**. IM = 10% × 80,000 = **8,000**. MM = 75% × 8,000 = **6,000**. Daily MTM = (today settle − prior settle) × 1,000 (positive sign because long).

| Day | Settle | Change | MTM (×1,000) | Balance before | Call? | Deposit | Balance after |
|---|---|---|---|---|---|---|---|
| 0 | 80.0 | — | — | 8,000 | — | — | 8,000 |
| 1 | 77.5 | −2.5 | −2,500 | 5,500 | Yes (<6,000) | 2,500 | 8,000 |
| 2 | 79.0 | +1.5 | +1,500 | 9,500 | No | 0 | 9,500 |
| 3 | 76.0 | −3.0 | −3,000 | 6,500 | No (≥6,000) | 0 | 6,500 |
| 4 | 83.0 | +7.0 | +7,000 | 13,500 | No | 0 | 13,500 |

**Day 1 walk-through.** Start 8,000. Price falls 2.5 → MTM = −2.5 × 1,000 = −2,500 → balance 5,500, below the 6,000 floor. Margin call: restore to **initial** 8,000, so deposit = 8,000 − 5,500 = **2,500**.

**Note on Day 3.** Balance 6,500 is at or above 6,000, so *no* call even though the day lost money — maintenance is the trigger, not "any loss."

**Reconcile total P&L three ways.**
- *Method A — sum of daily MTM:* −2,500 + 1,500 − 3,000 + 7,000 = **+3,000**.
- *Method B — price move × lot:* (83 − 80) × 1,000 = **+3,000**. ✓
- *Method C — cash accounting:* deposited = 8,000 IM + 2,500 call = 10,500; final balance 13,500; gain = 13,500 − 10,500 = **+3,000**. ✓

All three agree: daily settlements, however jagged, sum to the plain $(S_T - F_0)\times$ lot a forward would have paid in one shot. MTM changes the *timing*, never the *total*.

### B2 — Fair price and cash-and-carry arbitrage

A non-dividend stock trades at $S_0 = 500$. Financing rate $r = 7\%$ p.a., $q = 0$, expiry $T = 6$ months = 0.5 yr.

**Fair price.** $F_0 = 500 \times (1.07)^{0.5}$. Now $(1.07)^{0.5} = \sqrt{1.07} = 1.03441$, so $F_0 = 500 \times 1.03441 = \mathbf{517.20}$.
*Check:* $1.03441^2 = 1.0700$ ✓. **Basis** = 500 − 517.20 = **−17.20** (negative → contango, consistent with $F > S$).

**Arbitrage.** Suppose the future actually quotes **525** — richer than fair. Cash-and-carry:
1. Borrow 500 at 7% for 6 months; buy one share spot.
2. Sell the future at 525.
3. At expiry deliver the share into the short, receive 525.
4. Repay the loan: 500 × 1.03441 = 517.20.

Riskless profit = 525 − 517.20 = **+7.80 per share**, no market risk. Arbitrageurs sell the future until it falls to 517.20 and the profit vanishes — the exact force pinning $F_0$ to cost of carry. (If instead the future were *below* 517.20, run it in reverse: short the share, invest the proceeds at 7%, buy the cheap future.)

### B3 — Index future with dividend yield, plus hedge reconciliation

An index stands at $S_0 = 18{,}000$. $r = 6\%$, dividend yield $q = 1.5\%$, $T = 3$ months = 0.25 yr.

**Fair price.** $F_0 = 18{,}000 \times (1 + 0.06 - 0.015)^{0.25} = 18{,}000 \times (1.045)^{0.25}$.
$(1.045)^{0.25}$: $\ln 1.045 = 0.044017$; × 0.25 = 0.011004; $e^{0.011004} = 1.011065$. So $F_0 = 18{,}000 \times 1.011065 = \mathbf{18{,}199.2}$ — a ~199-point premium (contango, net carry 4.5%).

**Hedge reconciliation.** A fund owns the index (worth 18,000) and shorts the future at 18,199.2 to lock a sale. Combined value = portfolio + short-future payoff = $S_T + (18{,}199.2 - S_T) = 18{,}199.2$ for *any* $S_T$. Two spot checks:
- Crash to $S_T = 16{,}000$: portfolio 16,000; short gains 18,199.2 − 16,000 = +2,199.2; total = **18,199.2**.
- Rally to $S_T = 20{,}000$: portfolio 20,000; short loses 18,199.2 − 20,000 = −1,800.8; total = **18,199.2**. ✓

The lock holds both ways and is independent of where spot finishes — the practical payoff of convergence.

### B4 — Notional, leverage, tick value and the return multiplier

A gold future has lot = 100 grams, quoted per gram, price = 6,000. Tick size = 1 per gram. Initial margin = 5% of notional.

- **Notional** = 6,000 × 100 = **600,000**.
- **Initial margin** = 5% × 600,000 = **30,000**.
- **Leverage** = notional / IM = 600,000 / 30,000 = **20×**.
- **Tick value** = tick size × lot = 1 × 100 = **100** per tick.

**Return multiplier.** Suppose price rises 3% to 6,180 (+180/gram). Profit = 180 × 100 = **18,000**. On the 30,000 margin that is 18,000 / 30,000 = **+60%**. Cross-check: leverage × underlying move = 20 × 3% = **60%** ✓. The same 20× multiplier applies to losses — a 5% adverse move (−300/gram = −30,000) wipes out the entire margin, which is precisely why daily MTM and margin calls exist.

---

## Section C — Interview-Style (model answers)

**C1. "Walk me through exactly how a clearing house removes default risk."**
Three mechanisms stacked. First, *novation*: the moment a trade is agreed, the CCP interposes itself, becoming buyer to every seller and seller to every buyer, so no participant faces another directly. Its net market position is always zero, so it has no directional risk. Second, *daily mark-to-market*: every evening gains and losses are settled in cash, so the CCP's exposure to any member never exceeds roughly one day's price move. Third, *margin and a default fund*: initial margin (sized to a worst-case one-to-two-day move) plus a mutualised default fund absorb even that residual, giving the CCP time to close out a defaulter's book using their own posted collateral as the cushion.

**C2. "A stock I'm short via futures fell today and I got a margin call. To what level do I top up, and why isn't it just back above maintenance?"**
You restore the account all the way to **initial** margin, not merely back above maintenance. Maintenance is only the *trigger*: the CCP wants a full one-to-two-day buffer at all times, and once your equity has eroded to the maintenance floor, only a top-up to the full initial level rebuilds that buffer. Restoring merely to maintenance would leave you one bad tick from breaching again. This "trigger at maintenance, restore to initial" distinction is a classic trap — get it exactly right.

**C3. "If futures and forwards have identical payoffs, why would their *prices* ever differ?"**
The economic payoff $S_T - F_0$ is identical, but a future settles daily while a forward settles once at maturity, so their cash flows have different *timing*. When interest rates are *correlated* with the underlying, that timing matters: a long future tends to receive variation-margin cash exactly when rates are high (reinvest at a good rate) and pay it when rates are low — a small systematic advantage that nudges the futures price slightly above the forward. This is the convexity / daily-settlement effect. When rates are constant or uncorrelated with the asset, the two prices are theoretically equal, and over short horizons they are treated as identical in practice.

**C4. "Explain convergence and why a hedger relies on it."**
Convergence is the fact that the basis (spot − futures) shrinks to zero as expiry approaches, because $F_T = S_T$ at delivery — a future *is* the deliverable asset at that instant, so any gap is instant arbitrage. A hedger relies on it because it guarantees that whatever basis exists today will vanish by delivery. So a position held to expiry locks in today's futures price with certainty regardless of where spot travels (see B3). The only slippage arises if the hedge is lifted *early*, when the basis is not perfectly predictable — that residual is basis risk.

**C5. "What is basis risk, and give a realistic source of it."**
Basis risk is the uncertainty in the basis when a hedge is closed before expiry. Sources: (1) *timing mismatch* — you must exit before the contract's delivery date, so convergence is incomplete; (2) *asset mismatch* (cross-hedging) — you hedge jet fuel with a crude future because no jet-fuel contract is liquid, and the two prices don't move one-for-one; (3) *location/quality mismatch* — the deliverable grade or delivery point differs from your actual exposure. In each case the hedge neutralises the bulk of the price risk but leaves a smaller, harder-to-forecast basis exposure.

**C6. "Is contango a bullish signal? Convince me either way."**
No — contango just means the futures price sits above spot, which normally reflects positive *net carry*: financing plus storage costs exceeding any income or convenience yield. It is an accounting statement about the cost of holding the asset to delivery, not a forecast that prices will rise. Futures prices are not unbiased predictors of future spot. You can have a steeply contangoed curve in a market everyone expects to fall, simply because carry is expensive. Reading contango as bullish confuses the cost-of-carry structure with a directional view.

---

## Section D — Multiple-Choice (with reasoning)

**D1. A margin call is triggered when account equity falls below the ______ margin, and must be restored to the ______ margin.**
A) initial; maintenance  B) maintenance; initial  C) maintenance; maintenance  D) variation; initial
**Answer: B.** Maintenance is the floor that triggers the call; the top-up (variation margin) restores the balance to the full initial margin. A and C invert or under-fund the buffer.

**D2. The clearing house's net market position in the contracts it clears is:**
A) net long  B) net short  C) always zero  D) it varies with the market
**Answer: C.** Every long it holds via novation is matched by an equal short, so its directional (market) position is exactly zero. It bears only credit risk on members, not price risk — eliminating A, B and D.

**D3. For an equity index with $r > q$, the fair futures price relative to spot is:**
A) below spot (backwardation)  B) equal to spot  C) above spot (contango)  D) indeterminate
**Answer: C.** $F_0 = S_0(1+r-q)^T$; with $r > q$ the carry factor exceeds 1, so $F_0 > S_0$ — contango. Backwardation (A) would need $q > r$ or a convenience yield.

**D4. Which statement about futures vs forwards is FALSE?**
A) Futures settle P&L daily; forwards settle at maturity.
B) Futures are standardised; forwards are customised.
C) Futures carry more counterparty risk than forwards.
D) Futures are more liquid than forwards.
**Answer: C.** It is reversed — futures carry *less* counterparty risk because of novation and daily margining. A, B and D are all true distinctions.

**D5. At the exact moment of expiry, the basis (spot − futures) equals:**
A) the cost of carry  B) zero  C) the initial margin  D) the tick value
**Answer: B.** Convergence forces $F_T = S_T$, so basis = 0. Any non-zero value would be an instant riskless arbitrage.

**D6. Initial margin is best described as:**
A) a non-refundable fee for trading  B) the premium paid to the seller
C) a refundable performance bond  D) the maximum possible loss
**Answer: C.** Margin is returned (adjusted for P&L) on close-out, so it is neither a fee (A) nor a premium (B) — futures have no premium. It does not cap loss (D); futures losses are unbounded.

**D7. A future has notional 600,000 and initial margin 30,000. The embedded leverage is:**
A) 5×  B) 10×  C) 20×  D) 50×
**Answer: C.** Leverage = notional / initial margin = 600,000 / 30,000 = 20×. A 1% move in the underlying moves margin equity ~20%.

**D8. The sum of all daily mark-to-market cash flows on a long future held to expiry equals:**
A) the initial margin  B) $(S_T - F_0) \times$ lot  C) zero  D) the total margin calls paid
**Answer: B.** MTM only redistributes the *timing* of the payoff; the daily amounts sum exactly to the forward-equivalent total $(S_T - F_0)\times$ lot, as reconciled in B1.

**D9. A cash-and-carry arbitrage is executed when the futures price is:**
A) below its cost-of-carry fair value  B) above its cost-of-carry fair value
C) equal to spot  D) equal to the basis
**Answer: B.** When the future is *rich*, you buy spot (borrowing to finance), sell the overpriced future, and carry to delivery for a riskless profit. A cheap future calls for the reverse trade.

**D10. Which is NOT a source of basis risk?**
A) Closing the hedge before expiry  B) Hedging one asset with a related but different future
C) A mismatch in deliverable grade or location  D) Holding the hedge to expiry against the exact underlying
**Answer: D.** Holding to expiry against the identical underlying is the one case where convergence drives basis to zero, eliminating basis risk. A, B and C all leave residual basis exposure.

---

## Self-Verification Log

- **B1** total P&L reconciled three ways (sum of MTM, price×lot, cash accounting) = +3,000 across all. ✓
- **B2** $\sqrt{1.07} = 1.03441$ confirmed by squaring (1.0700); arbitrage profit 525 − 517.20 = 7.80. ✓
- **B3** $(1.045)^{0.25} = 1.011065$ via ln/exp; hedge nets to 18,199.2 for both a crash and a rally. ✓
- **B4** leverage 20× cross-checked against the 3%→60% return multiplier. ✓
- All MCQ answers trace directly to chapter statements (margin trigger/restore, novation net-zero, cost of carry, convergence, MTM summation). ✓
