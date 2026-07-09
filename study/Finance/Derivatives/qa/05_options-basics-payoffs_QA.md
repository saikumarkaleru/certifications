# Q&A — Options — Basics and Payoffs

Practice bank for Chapter 05. Every question is followed by a full worked answer. Work each one before reading the solution.

---

## Section A — Concept Check

**A1. In one sentence, what does an option buyer actually purchase, and what does the writer sell?**

The buyer purchases a *right without an obligation* — the right to transact at a fixed strike K by expiry T — while the writer sells that right and takes on the matching *obligation to perform if the buyer exercises*, in exchange for the premium received up front. The premium is the market price of that asymmetry.

**A2. Why can a long option's payoff never be negative at expiry, and what shape does this produce?**

Because the holder exercises only when it produces a positive cash flow and otherwise lets the option lapse, the payoff is floored at zero: max(S_T − K, 0) or max(K − S_T, 0). The floor on one side plus a linear slope on the other produces the kinked "hockey-stick" curve, with the kink at K. The *profit* line is that same shape shifted by the premium.

**A3. Distinguish payoff from profit. Can payoff be positive while profit is negative?**

Payoff is the option's value at expiry *before* accounting for the premium. Profit subtracts the premium (for a long) or adds it (for a short). Yes — a call whose S_T sits just above K has a small positive payoff but a negative profit if that payoff is smaller than the premium paid. Payoff and profit agree in sign only once S_T passes the breakeven (K + c for a call).

**A4. Write the four basic payoffs (long call, long put, short call, short put) in terms of S_T and K.**

Long call = max(S_T − K, 0). Long put = max(K − S_T, 0). Short call = −max(S_T − K, 0). Short put = −max(K − S_T, 0). The shorts are the exact mirror image of the longs — options are zero-sum between the two counterparties before premium.

**A5. Premium = intrinsic value + time value. Define each and state the sign of each.**

Intrinsic value is the payoff if exercised immediately: max(S − K, 0) for a call, max(K − S, 0) for a put — always ≥ 0. Time value is everything else, TV = Premium − IV — also ≥ 0 for a fairly priced option, reflecting the chance the option moves further into the money before expiry. At expiry time value collapses to zero and the premium equals pure intrinsic value.

**A6. Where is time value largest, and why?**

Time value peaks when the option is at-the-money (S ≈ K). That is the point of maximum uncertainty about which side of the strike the option finally lands, so the optionality is worth the most. Deep-ITM and deep-OTM options carry little time value — an ATM option's entire premium is time value because its intrinsic value is zero.

**A7. Fill the moneyness table: for a call and a put, when is each ITM, ATM, OTM?**

A call is ITM when S > K, ATM when S ≈ K, OTM when S < K. A put is ITM when S < K, ATM when S ≈ K, OTM when S > K. ITM means positive intrinsic value; ATM and OTM mean zero intrinsic value. Mnemonic: a call wants the market *up* through the strike; a put wants it *down* through the strike.

**A8. European vs American: which is worth more, and when is early exercise of an American call pointless?**

An American option is worth at least as much as an otherwise-identical European one (American premium ≥ European), because early exercise is an extra right you can decline. For a *non-dividend-paying* stock it is never optimal to exercise an American call early — you would forfeit the remaining time value and lose interest by paying K sooner — so that American call is worth exactly the European call. Early exercise matters mainly for puts and for calls on dividend-paying stocks.

**A9. Of the six premium drivers, which one raises both call and put premiums, and why?**

Volatility (σ). Higher dispersion means fatter tails on both sides, and because option payoffs are one-sided — loss floored at the premium, gain running — more uncertainty is always worth more to the holder, call or put. Hence trading options is often described as trading volatility.

**A10. State put–call parity and what it means economically.**

c + K·e^(−rT) = p + S₀. A call plus cash equal to the present value of the strike replicates the same expiry value, max(S_T, K), as a put plus the stock — so the two packages must cost the same today. Rearranged, c − p = S₀ − K·e^(−rT), which means long call + short put at the same strike = a synthetic long forward.

---

## Section B — Numerical / Payoff Problems

**B1. Long call, full reconciliation.** You buy one European call, K = 200, premium c = 8. Tabulate payoff and profit at S_T = 180, 200, 208, 220, 250. State max loss, breakeven, and check one row against theory.

Payoff = max(S_T − 200, 0); Profit = Payoff − 8; Breakeven = K + c = 208.

| S_T | Payoff | Profit |
|---|---|---|
| 180 | 0 | −8 |
| 200 | 0 | −8 |
| 208 | 8 | 0 |
| 220 | 20 | +12 |
| 250 | 50 | +42 |

Reconcile: below K = 200 the call lapses and loss is capped at the premium −8 (= max loss) ✓. Profit first hits zero at S_T = 208 = K + c ✓. At S_T = 220, profit = (220 − 200) − 8 = 12 ✓. Upside is unbounded — each rupee above 200 adds a rupee of profit.

**B2. Long put and the writer's mirror.** You buy a put, K = 60, premium p = 5. Give the long-put profit and short-put profit at S_T = 40, 55, 60, 75. State the long's max profit and breakeven; confirm zero-sum.

Payoff = max(60 − S_T, 0); Long profit = Payoff − 5; Short profit = 5 − Payoff. Breakeven = K − p = 55. Max profit at S_T = 0: (60 − 0) − 5 = 55.

| S_T | Payoff | Long put profit | Short put profit |
|---|---|---|---|
| 40 | 20 | +15 | −15 |
| 55 | 5 | 0 | 0 |
| 60 | 0 | −5 | +5 |
| 75 | 0 | −5 | +5 |

Reconcile: at S_T = 40 the holder buys at 40, exercises to sell at 60, gains 20, less the 5 premium = +15 ✓. Above K = 60 the put lapses; long loss capped at −5, short gain capped at +5 ✓. Breakeven 55 = 60 − 5 ✓. Every short-put figure is the exact negative of the long-put figure — zero-sum confirmed ✓.

**B3. Intrinsic / time-value split.** Stock at S = 500. A 480-strike call trades at 34; a 500-strike call at 18; a 520-strike call at 7. Split each into intrinsic and time value and label moneyness. Which has the most time value?

| Option | K | Premium | Intrinsic max(500−K,0) | Time value | Moneyness |
|---|---|---|---|---|---|
| Call | 480 | 34 | 20 | 14 | ITM |
| Call | 500 | 18 | 0 | 18 | ATM |
| Call | 520 | 7 | 0 | 7 | OTM |

Reconcile: every intrinsic value ≥ 0 and every time value ≥ 0, as arbitrage requires ✓. The ATM 500-strike call has the most time value (18) — maximum uncertainty about which side of the strike it lands ✓. The OTM 520 call's entire premium (7) is time value because its intrinsic value is zero ✓.

**B4. Breakevens and the exercise decision.** A trader holds a 100-strike put bought for 6 and a 100-strike call bought for 4, both on the same stock (a long straddle). At expiry S_T = 92. Which leg is exercised, what is each leg's profit, and what is the net?

At S_T = 92: the put is ITM (S_T < K), payoff = 100 − 92 = 8, profit = 8 − 6 = +2. The call is OTM (S_T < K), lapses, profit = −4. Net = +2 − 4 = −2. Only the put is exercised; the call is abandoned (you never exercise an OTM option — doing so would create a loss). The straddle's lower breakeven is K − (total premium) = 100 − 10 = 90, so at 92 the position is still slightly in the red, consistent with the −2 result ✓.

**B5. Put–call parity solve.** European options, same K = 150 and expiry. Call trades at c = 12, stock S₀ = 150, and PV(K) = K·e^(−rT) = 147. Find the arbitrage-free put price p.

Parity: c + K·e^(−rT) = p + S₀ ⇒ p = c + K·e^(−rT) − S₀ = 12 + 147 − 150 = 9. Check via c − p = S₀ − PV(K): 12 − 9 = 3 and 150 − 147 = 3 ✓. The put is worth 9. Any market price away from 9 would open a conversion/reversal arbitrage.

**B6. Importer's asymmetric hedge.** Spot USDINR = 83.00. Importer owing USD 1m buys a USD call at K = 83.50, premium 0.40/USD. Compute the net effective cost per USD if USDINR ends at (a) 86.00, (b) 81.00, and contrast with a forward at 83.50.

(a) At 86.00 he exercises, buying dollars at 83.50; net cost = 83.50 + 0.40 = 83.90/USD — a firm ceiling. (b) At 81.00 he lets the option lapse (forfeits 0.40) and buys spot at 81.00; net cost = 81.00 + 0.40 = 81.40/USD. A forward would have locked him at ~83.50 in *both* states. The option caps the bad case near 83.90 yet lets him keep the cheap 81.40 upside — the participation a forward cannot give — for the 0.40 premium. That premium is precisely the price of the asymmetry ✓.

**B7. Short call risk.** You write a 300-strike call for premium 10. Give profit at S_T = 290, 310, 340, and state max gain and max loss.

Short call profit = 10 − max(S_T − 300, 0). At 290: 10 − 0 = +10. At 310: 10 − 10 = 0. At 340: 10 − 40 = −30. Max gain = premium = +10 (whenever S_T ≤ 300). Max loss = unlimited as S_T → ∞. Breakeven = K + c = 310 ✓. This is the mirror of a long call: capped reward, unbounded risk — the writer is selling insurance.

---

## Section C — Interview-Style Questions with Model Answers

**C1. "A client says options are just cheaper leverage on a forward. Correct him."**

A forward is symmetric: it gives the full upside and forces the full downside in equal measure, and costs nothing up front. An option is *asymmetric*: for a premium paid today, the buyer keeps the favourable tail but truncates the unfavourable one — loss floored at the premium, gain left running. So an option is not merely a cheaper forward; it is a forward with the down-leg (for a call buyer) sliced off and sold back. From put–call parity, long call + short put = the forward — the option isolates one leg. The premium is the price of that truncation, i.e. the price of optionality, not just leverage.

**C2. "Why does volatility raise the price of both calls and puts? Isn't more risk bad?"**

For a symmetric instrument, more dispersion is a wash. But an option's payoff is one-sided: the holder's loss is capped at the premium while the gain runs. Under that convex, floored payoff, a wider distribution adds value on the favourable tail without matching cost on the unfavourable tail — which is already truncated at the premium. That holds for a call (open upside) and symmetrically for a put (open downside toward zero), so higher σ lifts both. Traders therefore treat a long option as a long-volatility position.

**C3. "Explain intrinsic and time value to a non-technical portfolio manager, and what happens to each as expiry nears."**

Think of the premium as two envelopes. The first, intrinsic value, is cash you would collect if you exercised right now — for a call, how far spot sits above the strike (never less than zero). The second, time value, is what you pay for the *possibility* that things move further your way before expiry — it is the price of hope and uncertainty. As expiry approaches, that uncertainty shrinks: the time-value envelope thins out and empties to zero exactly at expiry (theta decay), leaving only intrinsic value. That is why an out-of-the-money option, whose entire value is time value, decays to nothing if the move never comes.

**C4. "When would you never exercise an American call early, and why does that matter for pricing?"**

On a non-dividend-paying stock you never exercise an American call early. Exercising throws away the remaining time value and forces you to pay the strike now rather than later, forgoing interest on that cash — you are strictly better off selling the option or holding it. Because the early-exercise right is worthless in that case, the American call is worth exactly the same as the European call, and you can price it with European tools. Early exercise only earns its keep for American puts (getting the strike cash sooner) and for calls on dividend-paying stocks (capturing a dividend). This tells you where the American/European premium gap can and cannot open up.

**C5. "Walk me through how a long put is insurance on a portfolio."**

Hold the underlying and buy a put at strike K. If the asset falls below K, the put pays K − S_T, offsetting your loss — the insurance payout — and the premium is the insurance cost. The gap between spot and strike acts like a deductible: you absorb losses down to K, the policy covers you beyond. Above K the put lapses and you keep full upside, minus the premium. So a protective put floors your value at K − premium while leaving upside intact — textbook insurance, and writing the put is selling that insurance.

---

## Section D — Multiple Choice (with reasoning)

**D1. A long call has premium 5 and strike 100. At S_T = 103, the position's profit is:**
A) +3 B) −2 C) +5 D) 0

**Answer: B.** Payoff = max(103 − 100, 0) = 3; profit = 3 − 5 = −2. The payoff is positive but below the premium, so profit is still negative — S_T has not reached breakeven (105). This is the classic payoff-vs-profit trap.

**D2. Which position has unlimited loss potential?**
A) Long call B) Long put C) Short call D) Short put

**Answer: C.** A short (naked) call must deliver at K no matter how high S_T rises, so its loss is unbounded as S_T → ∞. Long call and long put have loss capped at the premium; a short put's loss is large but bounded (max K − p, when S_T = 0).

**D3. An option is at-the-money. Its premium is entirely:**
A) Intrinsic value B) Time value C) Half each D) Zero

**Answer: B.** At ATM the intrinsic value is ~0 (S ≈ K), so the whole premium is time value. This is also where time value is at its maximum.

**D4. Raising the risk-free rate r, all else equal, tends to:**
A) Raise both call and put premiums B) Lower both C) Raise the call, lower the put D) Lower the call, raise the put

**Answer: C.** A higher r lowers the present value of the strike you will pay (helping the call) and reduces the present value of the strike you will receive (hurting the put). Contrast this with volatility, which raises both.

**D5. For a put with strike 60 and premium 4, the breakeven price at expiry is:**
A) 64 B) 60 C) 56 D) 4

**Answer: C.** Put breakeven = K − p = 60 − 4 = 56. Below 56 the put is profitable; between 56 and 60 the payoff is positive but smaller than the premium; above 60 it lapses.

**D6. A non-dividend stock's American call, relative to the European call of same strike and expiry, is worth:**
A) Strictly more B) Strictly less C) Exactly the same D) Cannot say

**Answer: C.** Since early exercise is never optimal for a call on a non-dividend stock, the early-exercise right adds nothing, so the American and European calls have equal value. (In general American ≥ European; here equality holds.)

**D7. Which single factor, increasing, raises a call premium but lowers a put premium the most directly through moneyness?**
A) Volatility B) Spot price S C) Time to expiry D) Dividends

**Answer: B.** A higher spot pushes the call deeper ITM (premium up) and the put deeper OTM (premium down). Volatility and time tend to raise both; dividends lower the call and raise the put but act through the forward price rather than spot directly.

**D8. You write a put, strike 50, premium 6. Your maximum possible loss is:**
A) 6 B) 44 C) 50 D) Unlimited

**Answer: B.** Worst case is S_T = 0: short-put profit = 6 − max(50 − 0, 0) = 6 − 50 = −44. So max loss = 44 (= K − p), large but bounded — unlike a short call.

---

## Self-Verification Notes

- Long payoffs floored at zero and profits floored at ±premium beyond the strike — B1, B2, B7.
- Zero-sum verified numerically in B2 (short = −long every row).
- Breakevens as K + c / K − p throughout: B1, B2, B4, B7, D5, D8.
- Put–call parity cross-checked both forms in B5.
- Payoff-vs-profit trap in D1; moneyness / time-value logic in B3 and D3.
