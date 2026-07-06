# Q&A — Arbitrage and No-Arbitrage Pricing

Practice bank for Chapter 15. Every question is followed by a full worked answer; attempt each on paper first. Rates are continuously compounded and markets are frictionless (no costs, unlimited short-selling, one lending/borrowing rate) unless stated otherwise.

---

## Section A — Concept Check

**A1. Define arbitrage precisely, and distinguish the two textbook types.**

An arbitrage requires zero net investment yet cannot lose money and has a strictly positive probability of making money — a "free lunch." *Type 1*: a strategy costing nothing today with non-negative payoffs in every future state and a positive payoff in at least one. *Type 2*: a strategy with a strictly positive cash inflow today and non-negative payoffs in every state. Both are something for nothing; they differ only in whether the free money arrives now or later.

**A2. What is the no-arbitrage principle, and why is it the foundation of derivative pricing?**

The principle asserts that in a well-functioning market, prices adjust so that no arbitrage opportunity persists. It matters because it lets us price a derivative *without* forecasting the underlying, estimating expected returns, or knowing anyone's risk appetite. If we can build a portfolio of traded assets that replicates the derivative's payoff in every state, then to avoid arbitrage the derivative must cost exactly what the replicating portfolio costs. Price is pinned by replication, not by opinion.

**A3. State the Law of One Price and its relationship to no-arbitrage.**

Two assets (or portfolios) delivering identical cash flows in every state must trade at the same price today. It follows directly from no-arbitrage: if identical payoffs had different prices, you'd buy the cheap one, sell the dear one, pocket the difference now, and face perfectly offsetting flows later — a Type-2 arbitrage. No-arbitrage is slightly stronger (it also rules out dominated payoffs), but the two are used interchangeably.

**A4. Explain "replication" and why it produces a price rather than a value.**

Replication means building a portfolio of already-traded instruments (spot, bonds, other derivatives) whose payoff matches the target state-by-state at expiry. Because the payoffs are identical, the Law of One Price forces the derivative's *price* to equal the replica's *cost*. The output is a market-enforceable price — a level at which no arbitrageur can profit — not a subjective view of what the asset is "worth."

**A5. What is the cash-and-carry relationship, and what does it price?**

It prices a forward/future on an asset you can buy and store. Borrow cash, buy spot, carry to delivery, deliver against the forward. To rule out arbitrage the fair forward is `F₀ = S₀·e^(rT)` for a non-income asset — spot compounded at the cost of financing it. Income or convenience reduces carry: `F₀ = (S₀ − I)·e^(rT)` with income PV `I`, or `F₀ = S₀·e^((r−q)T)` with yield `q`, or `S₀·e^((r+u)T)` if storage cost `u` is added.

**A6. Distinguish "cash-and-carry arbitrage" from "reverse cash-and-carry."**

Cash-and-carry runs when the forward is *overpriced* (`F_mkt > S₀·e^(rT)`): short the forward, borrow and buy spot, carry, deliver — lock a riskless gain. Reverse cash-and-carry runs when the forward is *underpriced*: buy the cheap forward, short spot, invest proceeds at `r`, take delivery to close the short. Each exploits the mispricing from the opposite side; fair value is the price at which neither pays.

**A7. Why can no-arbitrage pricing ignore an asset's expected return and investors' risk preferences?**

A perfect replicating portfolio makes the two positions identical in every state — derivative and replica rise and fall together whatever the underlying is expected to do. The hedged combination is riskless, so only the riskless rate enters. Drift and risk aversion matter for *forecasting* a price path, but cancel out of a *relative* pricing argument tying the derivative to its underlying. This is the seed of risk-neutral valuation.

**A8. What is a risk-neutral probability, and is it a real-world forecast?**

A set of "as-if" probabilities under which every asset's expected return equals the riskless rate, so any derivative is priced as the discounted expectation of its payoff: `f = e^(−rT)·E^Q[payoff]`. It is emphatically *not* a forecast of actual likelihoods — it's a device that repackages the no-arbitrage/replication result. Its existence is equivalent to the absence of arbitrage (the First Fundamental Theorem).

**A9. State the two Fundamental Theorems of Asset Pricing in plain terms.**

*First*: a market is arbitrage-free iff there exists at least one risk-neutral (equivalent martingale) measure. *Second*: the market is complete (every payoff replicable) iff that measure is unique. Arbitrage-freeness gives you *a* consistent pricing measure; completeness gives you *the* price.

**A10. In practice, why do small "arbitrage" gaps appear and persist without being pure free lunches?**

Real markets have frictions the idealized argument assumes away: bid-ask spreads, transaction and financing costs, short-sale constraints, margin and collateral, taxes, and execution/liquidity risk. A quoted gap must exceed the round-trip cost of these before it is exploitable. Observed "mispricings" that stay inside the no-arbitrage band are therefore consistent with arbitrage-free pricing — the band has width because the trade is not actually costless.

---

## Section B — Numerical / Applied

**B1. Fair forward on a non-income asset.** `S₀ = 50`, `r = 8%` continuous, `T = 1`. Find the no-arbitrage forward price.

`F₀ = S₀·e^(rT) = 50·e^(0.08·1) = 50·1.083287 = 54.16`. The one-year forward should trade at **54.16**.

**B2. Detect and exploit an overpriced forward.** Same data as B1 but the one-year forward is quoted at `F_mkt = 56`. Show the arbitrage and the profit at maturity.

Fair value is 54.16, so the forward is rich by `56 − 54.16 = 1.84`. Run cash-and-carry:

| t = 0 | Cash flow |
|---|---|
| Borrow 50 at 8% | +50 |
| Buy asset spot | −50 |
| Short the forward at 56 | 0 |
| Net today | 0 |

At `T = 1`: deliver the asset, receive 56; repay the loan `50·e^(0.08) = 54.16`. Riskless profit `= 56 − 54.16 = **1.84**` per unit, with zero investment and zero risk. The trade pushes the forward down toward 54.16.

**B3. Underpriced forward — reverse cash-and-carry.** `S₀ = 50`, `r = 8%`, `T = 1`, but `F_mkt = 52`. Show the trade.

Fair value 54.16 > 52, so the forward is cheap by 2.16. Short spot, invest proceeds, buy the forward:

At `t = 0`: short-sell the asset for +50, invest 50 at 8%, go long the forward at 52 (costs nothing). Net today 0. At `T`: investment grows to `50·e^(0.08) = 54.16`; take delivery under the forward for 52 and return the borrowed asset to close the short. Profit `= 54.16 − 52 = **2.16**`, riskless.

**B4. Forward with discrete income.** A stock at `S₀ = 100` pays a `2.00` dividend in 6 months. `r = 6%`, `T = 1`. Find the fair one-year forward.

PV of the dividend: `I = 2·e^(−0.06·0.5) = 2·0.970446 = 1.9409`. Then `F₀ = (S₀ − I)·e^(rT) = (100 − 1.9409)·e^(0.06) = 98.0591·1.061837 = **104.12**`. The income the carrier collects lowers the net cost of carry, so the forward is below the no-income value `100·e^0.06 = 106.18`.

**B5. Forward with a continuous yield.** An index at `S₀ = 4,000` pays a continuous dividend yield `q = 2%`. `r = 5%`, `T = 0.5`. Find the fair futures level.

`F₀ = S₀·e^((r−q)T) = 4000·e^((0.05−0.02)·0.5) = 4000·e^(0.015) = 4000·1.015113 = **4,060.45**`. Net carry is `r − q = 3%` annualised.

**B6. Two-state single-period replication (no probabilities).** A stock trades at `S₀ = 100`; in one period it is either `120` (up) or `90` (down). `r = 0` per period. Price a call with strike `K = 100` by replication.

Payoffs: `C_u = 20`, `C_d = 0`. Hold `Δ` shares and `B` in cash to replicate:
`120Δ + B = 20` and `90Δ + B = 0`. Subtract: `30Δ = 20 → Δ = 2/3`. Then `B = −90·(2/3) = −60`. Cost of the replica `= Δ·S₀ + B = (2/3)·100 − 60 = 66.67 − 60 = **6.67**`. No-arbitrage call price is **6.67**, obtained without any probability of up/down.

**B7. Same tree via risk-neutral probabilities — confirm the answer.** Use B6's data to find the risk-neutral probability `q` and re-price the call.

With `r = 0`, the stock must have expected return 0 under `Q`: `q·120 + (1−q)·90 = 100 → 30q = 10 → q = 1/3`. Call price `= e^(−rT)·E^Q[C] = 1·[(1/3)·20 + (2/3)·0] = 20/3 = **6.67**`. Identical to the replication price — the two methods are the same result wearing different clothes.

**B8. Put via put-call parity as a no-arbitrage cross-check.** From B6/B7 (`S₀ = 100`, `K = 100`, `r = 0`, `C = 6.67`), price the matching put.

Parity with `r = 0`: `C − P = S₀ − K = 100 − 100 = 0`, so `P = C = **6.67**`. Verify by replication: `P_u = max(100−120,0)=0`, `P_d = 10`; `120Δ+B=0`, `90Δ+B=10 → 30Δ = −10 → Δ = −1/3`, `B = 40`; cost `= −(1/3)·100 + 40 = **6.67**`. Consistent.

**B9. Triangular (cross-rate) arbitrage.** Quotes: USD/EUR = 1.10 (1 EUR = 1.10 USD), USD/GBP = 1.25 (1 GBP = 1.25 USD), and EUR/GBP = 1.16 (1 GBP = 1.16 EUR). Is there arbitrage on 1,000,000 USD?

The consistent cross is `EUR/GBP = 1.25/1.10 = 1.1364` EUR per GBP. The market quotes 1.16, so GBP is dear in EUR terms — sell GBP for EUR, i.e. go USD → GBP → EUR → USD. Start with 1,000,000 USD: buy GBP `= 1,000,000/1.25 = 800,000 GBP`; convert to EUR `= 800,000·1.16 = 928,000 EUR`; convert to USD `= 928,000·1.10 = 1,020,800 USD`. Riskless gain `= **20,800 USD**` (2.08%), ignoring spreads.

**B10. No-arbitrage bound band with costs.** `S₀ = 50`, `r = 8%`, `T = 1`, round-trip transaction/financing friction of `0.80` per unit. Over what forward range is there *no* exploitable arbitrage?

Fair mid is `54.16` (B1). Cash-and-carry only pays if `F_mkt > 54.16 + 0.80 = 54.96`; reverse only pays if `F_mkt < 54.16 − 0.80 = 53.36`. So any quote in **[53.36, 54.96]** is arbitrage-free once frictions are respected — the "single fair price" becomes a band of width `2 × 0.80 = 1.60`.

**B11. Implied repo / cost-of-carry from a quoted forward.** `S₀ = 200`, one-year forward `F_mkt = 210`, no income. What continuous rate does the forward imply, and what if true `r = 6%`?

`F = S₀·e^(rT) → r_implied = ln(F/S₀)/T = ln(210/200)/1 = ln(1.05) = 0.04879 ≈ **4.88%**`. Since the true financing rate 6% exceeds the implied 4.88%, the forward is *cheap* relative to carry — a reverse cash-and-carry (short spot, invest at 6%, buy the forward) locks a gain.

---

## Section C — Interview Style

**C1. "How would you explain no-arbitrage pricing to a non-quant portfolio manager?"**

If I can build a basket of things you already trade — cash, the stock, a bond — that pays off exactly like the derivative in every possible future, the derivative has to cost the same as that basket. If it didn't, I'd buy the cheaper side, sell the dearer, and bank a guaranteed profit with no risk and no money down; traders would pile in until the gap closed. So the price isn't a forecast or an opinion — it's whatever level stops that free-money machine from running. That's why we can price options without predicting where the stock is going.

**C2. "Why doesn't the expected return of the stock appear in an option's no-arbitrage price?"**

Because the option is priced *relative* to the stock, not in isolation. When I build the replicating (or delta-hedged) portfolio, the option and the hedge move together one-for-one in each state, so the combination is riskless — its value doesn't depend on which way the stock actually drifts. The drift affects the *probability* of ending up here or there, but it moves the option and the hedge in lockstep, so it cancels. Only the financing rate on the hedge survives. Practically, this is what lets two traders who wildly disagree on the stock's direction still agree on the option's fair price.

**C3. "A junior tells you a futures price should equal the market's expected future spot. Correct them."**

That's a common conflation. The futures price is the *cost-of-carry* forward, `S₀·e^((r−q)T)` — set purely so cash-and-carry arbitrage can't run. It equals the expected future spot only under risk-neutrality with zero risk premium. In the real world, if the asset carries a risk premium, expected spot and futures differ (the normal-backwardation / contango debate). The clean statement: futures equals the *risk-neutral* expected spot, i.e. carry, not the *real-world* expected spot.

**C4. "Walk me through spotting and trading an overpriced stock-index future."**

First compute fair value: `F₀ = S₀·e^((r−q)T)` from the index, financing rate, and dividend yield; compare to the screen. If the future is above fair value beyond my round-trip costs, I run index-arbitrage cash-and-carry: sell the rich future, borrow cash and buy the basket of constituents spot, hold to delivery collecting dividends. At expiry I settle against the future and repay the loan; the locked gap is profit. I'd stress it for basket slippage, dividend-timing uncertainty, and financing assumptions — those frictions set how wide the mispricing must be before it's real.

**C5. "What could make a textbook arbitrage fail to be a free lunch in practice?"**

Frictions the model ignores. Bid-ask spreads mean I trade worse than the mid I computed from. Short-selling may be costly, size-limited, or subject to recall (a squeeze can force an unwind at a loss). Borrow and lend rates differ, and collateral/margin ties up capital. There's execution risk between legs and liquidity risk if I must exit early; taxes and settlement bite too. A nominal gap must clear all those costs first — inside that band the "arbitrage" is illusory. That's why real desks quote a no-arbitrage *band*, not a point.

**C6. "Explain the link between no-arbitrage and the existence of a risk-neutral measure."**

They're two sides of one coin — the First Fundamental Theorem. If no arbitrage exists, you can always find positive "as-if" probabilities under which every asset's discounted price is a martingale (grows at the riskless rate); under them, any derivative's price is just the discounted expected payoff. Conversely, if such a measure exists, arbitrage is impossible — a zero-cost strategy has zero expected discounted payoff and so can't be uniformly positive. If the market is also complete (every payoff replicable), that measure is unique, which is what gives a single price rather than a range.

---

## Section D — MCQs (with reasoning)

**D1.** For a non-dividend asset with `S₀ = 80`, `r = 5%`, `T = 2`, the no-arbitrage forward price is closest to:
(a) 80.00 (b) 84.10 (c) 88.41 (d) 76.19

**Answer: (c).** `F₀ = 80·e^(0.05·2) = 80·e^(0.10) = 80·1.10517 = 88.41`. (a) ignores carry; (d) discounts instead of compounding; (b) uses `T = 1`.

**D2.** If a stock's forward trades *below* its cost-of-carry fair value, the arbitrage is to:
(a) buy the forward, short the stock, invest proceeds
(b) sell the forward, buy the stock with borrowed cash
(c) buy both the forward and the stock
(d) do nothing — it's fair

**Answer: (a).** Cheap forward → reverse cash-and-carry: long the underpriced forward, short spot, invest the short proceeds at `r`, take delivery to close. (b) is the trade for an *over*priced forward; (c) has no offsetting structure.

**D3.** Which statement about risk-neutral probabilities is TRUE?
(a) They are the market's best forecast of actual outcomes
(b) They make every asset's expected return equal the riskless rate
(c) They only exist if investors are literally risk-neutral
(d) They depend on each investor's utility function

**Answer: (b).** Under `Q`, discounted prices are martingales, so expected returns equal `r`. (a) confuses `Q` with real-world `P`; (c) misreads the device — it works regardless of true preferences; (d) is false, `Q` is preference-free given no arbitrage.

**D4.** A one-period binomial stock is 100 today, 110 up or 95 down, `r = 0`. The risk-neutral probability of an up-move is:
(a) 0.50 (b) 0.33 (c) 0.40 (d) 0.67

**Answer: (b).** `q·110 + (1−q)·95 = 100 → 15q = 5 → q = 1/3 ≈ 0.33`. The real-world probability is irrelevant.

**D5.** The Law of One Price is violated when:
(a) two assets with different payoffs have the same price
(b) two portfolios with identical state-by-state payoffs have different prices
(c) an asset's price rises over time
(d) a forward differs from the spot

**Answer: (b).** Identical payoffs must share one price; a gap is arbitrageable. (a) is fine — different payoffs can coincidentally cost the same; (c) is normal carry/drift; (d) is expected — forward and spot differ by cost of carry.

**D6.** Index at 5,000, `r = 4%`, dividend yield `q = 1.5%`, `T = 0.25`. Fair futures is closest to:
(a) 5,000 (b) 5,031 (c) 5,063 (d) 4,969

**Answer: (b).** `F = 5000·e^((0.04−0.015)·0.25) = 5000·e^(0.00625) = 5000·1.006270 = 5,031.3`. (c) forgets the dividend yield; (d) flips the sign of net carry.

**D7.** In a complete, arbitrage-free market, the risk-neutral measure is:
(a) non-existent (b) unique (c) infinitely many (d) equal to the real-world measure

**Answer: (b).** Second Fundamental Theorem: completeness ⇒ uniqueness of `Q`, which is why a single price exists. Incomplete arbitrage-free markets have many valid `Q`'s (a price *range*).

**D8.** The width of a real-world no-arbitrage band around fair forward value is driven mainly by:
(a) the volatility of the underlying
(b) the expected return of the underlying
(c) transaction, financing, and short-selling costs
(d) the maturity date alone

**Answer: (c).** Frictions determine how far price can stray before a trade clears its own costs. Volatility (a) and drift (b) don't enter the carry relation; maturity (d) scales the fair level, not the friction band.

---

*Self-check: forward formulas (B1–B5, D1, D6) recomputed; B6 replication and B7 risk-neutral pricing agree at 6.67; B8 verified via parity and replication; B9's 20,800 USD gain cross-checked against the 1.1364 consistent cross; each MCQ distractor traced to a specific error.*
