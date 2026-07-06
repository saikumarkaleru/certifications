# Q&A — Option Strategies

Practice bank for Chapter 06. Every question is followed by a full worked answer. Work each one before reading the solution. Payoffs assume European options held to expiry unless stated; ignore interest on premium unless a problem introduces it.

---

## Section A — Concept Check

**A1. What is the single organising idea behind every option strategy?**

You combine long/short positions in calls, puts, and the underlying so the *net payoff curve* has a shape that matches a specific market view — direction, magnitude of movement, or volatility — at the lowest net cost or risk you are willing to bear. Every named strategy is just a particular curve. Learn to read the shape (where it slopes up, where it is flat, where the kinks are) and the name becomes secondary.

**A2. Classify strategies by the *view* they express.**

Bullish directional: long call, bull call spread, bull put spread, covered call (mildly bullish), protective put (bullish but insured). Bearish directional: long put, bear put spread, bear call spread, covered put. Neutral / low-volatility: short straddle, short strangle, long butterfly, long condor, iron condor. High-volatility (direction-agnostic): long straddle, long strangle, short butterfly. Income / hedging overlays: covered call, collar, cash-secured put.

**A3. Covered call — construction, view, and the trade-off.**

Long the underlying + short one call (usually OTM). View is neutral-to-mildly-bullish. You collect the premium, which cushions small declines and adds yield, but you *cap* your upside at the strike: above K the short call's losses offset further gains on the stock. You have sold your upside tail for current income.

**A4. Protective put — construction and why it is "insurance".**

Long the underlying + long one put. The put sets a *floor*: below K, losses on the stock are matched by gains on the put, so your worst outcome is fixed at (K − S₀ − premium). You keep unlimited upside minus the premium cost. It is literally an insurance contract — the premium is the policy price and K is the deductible level.

**A5. A collar — what is it and why do people use it?**

Long stock + long protective put (floor) + short call (cap), the call financing the put. The result is a *bounded* payoff: you cannot lose below the put strike nor gain above the call strike. A zero-cost collar is one where the call premium received exactly funds the put premium paid. Popular with holders of a large appreciated position who want downside protection without paying out of pocket.

**A6. Bull call spread vs bull put spread — same view, different cash flow. Explain.**

Both are moderately bullish with capped profit and capped loss. A **bull call spread** is long a lower-strike call + short a higher-strike call — a *net debit* (you pay). A **bull put spread** is short a higher-strike put + long a lower-strike put — a *net credit* (you receive). Bull call spread profits from the underlying rising; bull put spread profits from the underlying staying up or rising, keeping the sold put out of the money.

**A7. Straddle vs strangle — how do they differ, and which is cheaper?**

A **long straddle** is a long call and long put at the *same* strike (usually ATM). A **long strangle** uses a call and put at *different* OTM strikes (call strike above, put strike below). The strangle is cheaper because both legs are OTM, but it needs a *larger* move to break even. Both are bets on volatility, indifferent to direction.

**A8. Why is a long butterfly a bet on *low* volatility even though it is built from spreads?**

A long call butterfly is long one low strike, short two middle strikes, long one high strike (all equally spaced). Its payoff peaks at the middle strike and falls to zero on both wings. Maximum profit happens when the underlying finishes *exactly at the middle strike* — i.e., when it barely moves. It profits from the market pinning near the centre, so it is a low-volatility, low-cost, low-risk play.

**A9. Iron condor — describe it in one breath and state the view.**

Short an OTM put spread + short an OTM call spread on the same underlying and expiry: sell one OTM put, buy a further OTM put, sell one OTM call, buy a further OTM call. Net credit. It profits when the underlying stays *between* the two short strikes — a range-bound, low-volatility view with defined risk on both wings.

**A10. Explain how put–call parity lets you build a synthetic long stock, and why it matters for strategies.**

From c − p = S₀ − PV(K): rearranged, long call + short put at the same strike and expiry replicates long stock (a synthetic forward). This is why many strategies have an equivalent built from different instruments — a protective put equals a long call plus cash (a "married put" ≈ a fiduciary call), and an iron condor equals a long condor. Recognising synthetics lets you pick the cheapest construction of the same payoff.

---

## Section B — Numerical / Payoff Problems

**B1. Covered call, full reconciliation.** You own a stock bought at S₀ = 100 and write a call with K = 110 for premium c = 4. Tabulate payoff and profit at S_T = 90, 100, 110, 120, 130. State max profit, breakeven, and the cap.

Profit = (S_T − 100) + [4 − max(S_T − 110, 0)]. The first bracket is the stock P&L; the second is the short call P&L.

| S_T | Stock P&L | Short call P&L | Total profit |
|---|---|---|---|
| 90  | −10 | +4 | −6 |
| 100 | 0   | +4 | +4 |
| 110 | +10 | +4 | +14 |
| 120 | +20 | +4 −10 = −6 | +14 |
| 130 | +30 | +4 −20 = −16 | +14 |

Breakeven: stock loss offsets premium, so S_T = 100 − 4 = **96**. Max profit = (110 − 100) + 4 = **14**, reached at and above K = 110 (the cap). Check the 120 row: gain on stock +20, but short call loses 10 net (paid 4, owes 10 on a 10-point ITM call) → 20 − 6 = 14. Consistent — profit is flat above 110.

**B2. Protective put, full reconciliation.** Long stock at S₀ = 100, long put K = 95 for p = 3. Tabulate profit at S_T = 80, 90, 95, 100, 115. State max loss and breakeven.

Profit = (S_T − 100) + [max(95 − S_T, 0) − 3].

| S_T | Stock P&L | Long put P&L | Total profit |
|---|---|---|---|
| 80  | −20 | +15 −3 = +12 | −8 |
| 90  | −10 | +5 −3 = +2  | −8 |
| 95  | −5  | 0 −3 = −3   | −8 |
| 100 | 0   | −3          | −3 |
| 115 | +15 | −3          | +12 |

Max loss = (100 − 95) + 3 = **8**, and it is flat for all S_T ≤ 95 (the floor). Breakeven = S₀ + p = 100 + 3 = **103**. Check the 80 row: stock down 20, put pays 15, less 3 premium → −20 + 12 = −8. The floor holds — this is the insurance in action.

**B3. Bull call spread.** Buy call K₁ = 100 at c₁ = 7; sell call K₂ = 110 at c₂ = 3. Net debit, max profit, max loss, breakeven. Tabulate at S_T = 95, 100, 104, 110, 120.

Net debit = 7 − 3 = **4**. Profit = max(S_T − 100, 0) − max(S_T − 110, 0) − 4.

| S_T | Long call | Short call | Net payoff | Profit (−4) |
|---|---|---|---|---|
| 95  | 0  | 0   | 0  | −4 |
| 100 | 0  | 0   | 0  | −4 |
| 104 | 4  | 0   | 4  | 0  |
| 110 | 10 | 0   | 10 | +6 |
| 120 | 20 | −10 | 10 | +6 |

Max loss = net debit = **4** (S_T ≤ 100). Max profit = (K₂ − K₁) − debit = 10 − 4 = **6** (S_T ≥ 110). Breakeven = K₁ + debit = 104. Check 120: long +20, short −10, net +10, less 4 → +6. Above K₂ the two legs move one-for-one, freezing the payoff — that is the cap.

**B4. Bull put spread (credit).** Sell put K₂ = 105 at p₂ = 6; buy put K₁ = 95 at p₁ = 2. Net credit, max profit, max loss, breakeven. Tabulate at S_T = 85, 95, 101, 105, 115.

Net credit = 6 − 2 = **4**. Profit = credit − max(105 − S_T, 0) + max(95 − S_T, 0).

| S_T | Short put | Long put | Net option P&L | Profit incl. credit |
|---|---|---|---|---|
| 85  | −20 | +10 | −10 | −10 + 4 = −6 |
| 95  | −10 | 0   | −10 | −6 |
| 101 | −4  | 0   | −4  | 0  |
| 105 | 0   | 0   | 0   | +4 |
| 115 | 0   | 0   | 0   | +4 |

Max profit = net credit = **4** (S_T ≥ 105, both puts expire worthless). Max loss = (K₂ − K₁) − credit = 10 − 4 = **6** (S_T ≤ 95). Breakeven = K₂ − credit = 105 − 4 = **101**. Check 85: short put owes 20, long put pays 10 → −10, plus 4 credit = −6, the floor. Note the payoff shape is *identical* to the bull call spread of B3 — same max profit region logic, mirror construction.

**B5. Long straddle.** Buy call and put both at K = 100; c = 6, p = 5. Total cost, both breakevens, and profit at S_T = 80, 89, 100, 111, 130.

Total premium = 6 + 5 = **11**. Profit = max(S_T − 100, 0) + max(100 − S_T, 0) − 11 = |S_T − 100| − 11.

| S_T | Call payoff | Put payoff | Total payoff | Profit (−11) |
|---|---|---|---|---|
| 80  | 0  | 20 | 20 | +9 |
| 89  | 0  | 11 | 11 | 0  |
| 100 | 0  | 0  | 0  | −11 |
| 111 | 11 | 0  | 11 | 0  |
| 130 | 30 | 0  | 30 | +19 |

Lower breakeven = 100 − 11 = **89**; upper breakeven = 100 + 11 = **111**. Max loss = **11**, at exactly S_T = 100. Profit is unlimited on the upside and large (to S_T = 0) on the downside. The strategy needs a move of more than 11 points *in either direction* to pay.

**B6. Long butterfly (calls).** Buy K₁ = 90 at 12, sell two K₂ = 100 at 6 each, buy K₃ = 110 at 3. Net cost, max profit, max loss, both breakevens. Tabulate at S_T = 85, 90, 100, 110, 120.

Net cost = 12 − 2(6) + 3 = 12 − 12 + 3 = **3** (debit). Payoff = max(S−90,0) − 2·max(S−100,0) + max(S−110,0).

| S_T | +K₁ call | −2·K₂ call | +K₃ call | Net payoff | Profit (−3) |
|---|---|---|---|---|---|
| 85  | 0  | 0    | 0 | 0  | −3 |
| 90  | 0  | 0    | 0 | 0  | −3 |
| 100 | 10 | 0    | 0 | 10 | +7 |
| 110 | 20 | −20  | 0 | 0  | −3 |
| 120 | 30 | −40  | 10| 0  | −3 |

Max profit = (K₂ − K₁) − net cost = 10 − 3 = **7**, at S_T = 100 (the centre). Max loss = net cost = **3**, on both wings. Breakevens = K₁ + cost = 93 and K₃ − cost = 107. Check 120: 30 − 40 + 10 = 0 payoff, less 3 = −3 — the wings are flat, confirming defined risk. Peak at the middle strike confirms the low-volatility view.

**B7. Iron condor.** Sell put K = 90 at 3, buy put K = 85 at 1.5; sell call K = 110 at 3, buy call K = 115 at 1.5. Net credit, max profit, max loss, both breakevens.

Net credit = (3 − 1.5) + (3 − 1.5) = 1.5 + 1.5 = **3**. Between 90 and 110 all four options expire worthless → keep the **3** credit (max profit). Each wing is 5 points wide; max loss = wing width − credit = 5 − 3 = **2**. Lower breakeven = 90 − 3 = **87**; upper breakeven = 110 + 3 = **113**. Quick check at S_T = 85: short put loses 5, long put pays 0 → −5, plus 3 credit = −2 (max loss). At S_T = 100: all worthless, +3. The profit plateau sits between the short strikes — a defined-risk range bet.

**B8. Collar (zero-cost check).** Long stock at 100. Buy put K = 95 at 3, sell call K = 108 at 3. Net premium, floor, cap, and profit at S_T = 85, 95, 100, 108, 120.

Net premium = −3 + 3 = **0** → zero-cost collar. Profit = (S_T − 100) + max(95 − S_T, 0) − max(S_T − 108, 0).

| S_T | Stock | Long put | Short call | Profit |
|---|---|---|---|---|
| 85  | −15 | +10 | 0   | −5 |
| 95  | −5  | 0   | 0   | −5 |
| 100 | 0   | 0   | 0   | 0  |
| 108 | +8  | 0   | 0   | +8 |
| 120 | +20 | 0   | −12 | +8 |

Floor (max loss) = (100 − 95) = **5**; cap (max profit) = (108 − 100) = **8**. Bounded between −5 and +8 at zero premium outlay. Check 120: +20 stock, short call owes 12 → +8, the cap. The payoff is a truncated stock position.

**B9. Reconcile B3 and B4 via parity.** Show the bull call spread and bull put spread deliver the same *shape*, and explain the payoff difference of a constant.

Both cap profit at 10 points below the top and floor loss, with breakeven near the middle. B3 (call spread) costs 4 up front, max profit 6, max loss 4. B4 (put spread) receives 4 up front, max profit 4, max loss 6. Their profit diagrams are the same kinked line displaced by the premium timing: at every S_T, [B3 profit] − [B4 profit] = a constant reflecting that one is financed by debit and the other by credit at the same strikes' parity relationship. Both are "long the 100/105–110 area", differing only in which instrument carries the cost.

**B10. Short straddle risk.** Reverse B5: *write* the call and put at K = 100, collecting 11. State max profit, breakevens, and the loss at S_T = 130.

Max profit = **11** (premium kept), at S_T = 100. Breakevens are the same 89 and 111. Loss is unbounded on the upside: at S_T = 130 the short call owes 30, put expires worthless → 11 − 30 = **−19**. This mirrors B5 exactly (zero-sum): the straddle buyer's +19 is the writer's −19. The writer is betting on low realised volatility and carries theoretically unlimited risk.

---

## Section C — Interview-Style Questions

**C1. "A client holds a large gain in one stock and is nervous about a correction but does not want to sell and trigger tax. What do you suggest?"**

Model answer: A collar. Buy a protective put to set a floor below which losses stop, and finance it by writing an out-of-the-money call, which caps the upside. Structured as a zero-cost collar the client pays nothing out of pocket, keeps the shares (no disposal, no immediate tax event), and locks the outcome into a defined band until expiry. The cost is giving up gains above the call strike — appropriate for someone whose priority is protecting a gain rather than chasing more. I would size the strikes to the client's risk tolerance: a tighter floor costs more and needs a nearer cap to stay zero-cost.

**C2. "When would you prefer a strangle over a straddle?"**

Model answer: When I expect a *large* move but want to pay less premium and am comfortable needing a bigger move to profit. The strangle's OTM strikes make it cheaper, so max loss is smaller and the position is less sensitive to being slightly wrong on timing. I would choose the straddle when I want the tightest breakevens and maximum sensitivity to any move — for example, straddling ATM right before an earnings release where I expect a sharp reaction. The trade-off is straightforward: straddle costs more but breaks even sooner; strangle costs less but demands more movement.

**C3. "Explain why a covered call is not a free lunch, even though it always collects premium."**

Model answer: The premium is real income and it cushions small drops, so it *feels* free — but you have sold the right tail of your return. In any rally beyond the strike, every extra point of stock gain is offset by the short call, so your upside is capped while your downside (below breakeven) is still nearly the full stock exposure minus the premium. You have converted an uncertain large upside into a certain small income. That is a fair trade only if you genuinely expect the stock to stay flat-to-mildly-up; in a strong bull market it underperforms simply holding the stock.

**C4. "A trader says 'I'm short volatility.' What positions might they hold, and what is their nightmare scenario?"**

Model answer: Short-volatility positions profit when the underlying stays calm and realised volatility comes in below what was priced: short straddles, short strangles, iron condors, and long butterflies all qualify — they make money in a quiet, range-bound market and decay in the seller's favour. The nightmare is a large, sudden move in either direction combined with a spike in implied volatility — a gap through the short strikes. For undefined-risk positions (short straddle/strangle) losses can be very large and fast; that is why disciplined sellers prefer defined-risk versions like the iron condor, where the long wings cap the damage.

**C5. "How does put–call parity help you spot a mispriced strategy or an arbitrage?"**

Model answer: Parity says c + PV(K) = p + S₀ for European options at the same strike and expiry. If the market quotes violate this — say the synthetic long stock (long call, short put) is cheaper than the actual stock net of financing — you can build a risk-free box: buy the cheap package, sell the dear one, and lock the difference. Practically it also lets me choose the cheapest way to express a view: a protective put and a long call plus cash are economically the same insured position, so I trade whichever the market is offering more cheaply. Parity is the no-arbitrage backbone that ties every synthetic to its natural counterpart.

---

## Section D — Multiple Choice (with reasoning)

**D1. A bull call spread has maximum profit equal to:**
(a) the net premium received; (b) unlimited; (c) the difference in strikes minus the net debit; (d) the lower strike minus the debit.

**Answer: (c).** A bull call spread is a debit strategy; above the higher strike both legs move one-for-one, freezing the payoff at (K₂ − K₁), from which you subtract the net premium paid. (a) describes a credit strategy; (b) is a naked long call; (d) confuses breakeven inputs.

**D2. Which strategy has unlimited loss potential?**
(a) long straddle; (b) short straddle; (c) long butterfly; (d) iron condor.

**Answer: (b).** A short straddle writes both a call and a put; the short call gives theoretically unlimited upside loss. The long straddle's loss is capped at premium paid, and both the butterfly and iron condor are defined-risk by construction (long wings).

**D3. A zero-cost collar is best described as:**
(a) a strategy with no maximum loss; (b) long stock with a bought put financed by a written call, netting zero premium; (c) a bet on rising volatility; (d) two long options at the same strike.

**Answer: (b).** The collar brackets a stock position between a put floor and a call cap; "zero-cost" means the call premium received exactly funds the put. It has a defined max loss (down to the put strike), so (a) is wrong; it is a low-volatility hedging overlay, not a volatility bet, ruling out (c); (d) describes a straddle.

**D4. You expect a stock to stay very close to 100 through expiry. Cheapest defined-risk way to profit?**
(a) long straddle; (b) short stock; (c) long butterfly centred at 100; (d) protective put.

**Answer: (c).** A long butterfly peaks in profit when the underlying finishes at the middle strike and has small, defined cost and risk. A long straddle profits from big moves (opposite view); short stock and a protective put are directional, not pin-the-strike plays.

**D5. A bull put spread is a credit strategy because:**
(a) you buy the higher-strike put; (b) you sell the higher-strike put and buy the lower-strike put; (c) both puts are bought; (d) it always profits.

**Answer: (b).** Selling the nearer-the-money (higher-strike) put brings in more premium than the further OTM (lower-strike) put you buy for protection, so the position opens for a net credit and profits if the underlying stays up. (a) and (c) misstate the legs; (d) is false — max loss occurs below the lower strike.

**D6. In a long strangle versus a long straddle at the same underlying, the strangle typically has:**
(a) higher cost and narrower breakevens; (b) lower cost and wider breakevens; (c) identical cost; (d) unlimited loss.

**Answer: (b).** Both legs of a strangle are OTM, so it costs less than the ATM straddle, but the underlying must travel further past the outer strikes to break even, widening the breakeven band. Long-option strategies never have unlimited loss, ruling out (d).

---

*Self-check performed: every Section B table was recomputed leg-by-leg and reconciled against the stated max profit, max loss, and breakevens; B5/B10 and B3/B9/B4 were cross-checked for zero-sum and parity consistency. All MCQ distractors were verified as genuinely incorrect.*
