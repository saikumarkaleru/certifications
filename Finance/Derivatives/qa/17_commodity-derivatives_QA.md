# Q&A — Commodity Derivatives

Practice bank for Chapter 17. Every question is followed by a full worked answer. Work each one before reading the solution. Rates are continuously compounded unless stated otherwise; the cost-of-carry model used throughout is $F_0 = S_0\,e^{(r+u-y)T}$, where $r$ is the risk-free rate, $u$ is storage cost as a rate, and $y$ is convenience yield.

---

## Section A — Concept Check

**A1. In one sentence, what fundamental need do commodity derivatives serve?**

They transfer *unavoidable* price risk from those who bear it involuntarily — producers who are structurally long the physical good and consumers who are structurally short it — to speculators, index investors and arbitrageurs willing to hold that risk for an expected return, so producers and consumers can lock a price today and plan, borrow and invest with certainty.

**A2. Why does the cost-of-carry model for a commodity have two extra terms that a stock-index future does not?**

Because a physical commodity, unlike a financial asset, is costly to *hold* and confers a benefit from being held. Storage cost $u$ (warehousing, insurance, spoilage) adds to carry and pushes the future *up*; convenience yield $y$ (the insurance value of having inventory on hand) subtracts from carry and pulls the future *down*. A stock index has effectively $u=0$ and $y=0$ (a dividend yield $q$ plays the role of a negative carry instead).

**A3. Distinguish contango from backwardation in one line each, and give the parameter condition for each.**

**Contango** = upward-sloping curve, futures above spot, occurs when $r+u>y$ (carry dominates convenience). **Backwardation** = downward-sloping curve, futures below spot, occurs when $y>r+u$ (convenience dominates carry).

**A4. A farmer is "naturally long" wheat. Explain what that means and how the hedge is constructed.**

The farmer owns a growing crop, so their wealth *rises and falls with the price of wheat* — an exposure that came bundled with farming, not chosen. To hedge, the farmer *sells* wheat futures (a short hedge), taking a position that gains exactly when prices fall — precisely when the physical crop loses value. The two legs move oppositely and cancel, leaving a locked-in price.

**A5. Why is the arbitrage that pins commodity futures to spot *one-sided*?**

Cash-and-carry (buy the physical spot, store it, sell the future, deliver at expiry) enforces the *upper* bound on $F$ — if futures are too high anyone can do this for riskless profit. The reverse (short the physical, buy the future) requires *borrowing* the commodity, which for a consumable good in short supply is often impossible. That asymmetry means the lower bound is soft, which is exactly where large convenience yields and persistent backwardation live.

**A6. What is roll yield and what determines its sign?**

Roll yield is the return earned or paid when rolling an expiring futures contract into a later-dated one, arising from the futures price converging to spot over time. In **backwardation** the deferred contract is cheaper, so you roll from high to low and earn a **positive** roll yield; in **contango** the deferred contract is more expensive, so you roll from low to high and pay a **negative** roll yield.

**A7. Decompose the total return of a fully-collateralised long commodity index.**

Total return ≈ **Spot return + Roll yield + Collateral (risk-free) return.** The spot term is the change in the commodity price; the roll term is the curve-shape effect from rolling futures; the collateral term is the T-bill interest earned on cash backing the futures. This is why an oil ETF can *fall* over a decade while spot oil *rises* — a persistent negative roll can swamp the spot gain.

**A8. Why is "normal backwardation" not the same as "backwardation"?**

They live on different axes. **Backwardation** compares $F$ to the *current* spot $S$ ($F<S$). **Normal backwardation** (Keynes) compares $F$ to the *expected future* spot ($F<E[S_T]$), arising because net-short hedgers pay a risk premium to net-long speculators. A market can be in contango yet still display normal backwardation, and vice versa.

**A9. What is basis, and name the three sources of basis risk.**

Basis = spot price of the *thing you hold* − futures price of the *contract you trade*. Basis risk (the risk that this gap moves) arises from **grade/quality** mismatch (durum wheat hedged with soft red winter wheat), **location** mismatch (West Texas oil priced against Brent), and **timing** mismatch (your sale date not aligning with contract expiry).

**A10. Why does a futures-based ETF not simply track the commodity's spot price, but a physically-backed gold ETF nearly does?**

A futures-based ETF must repeatedly roll contracts, so it tracks spot return *plus roll yield plus collateral return* — in persistent contango the roll drag can pull it away from spot badly. Gold stores cheaply and does not spoil, so a physically-backed gold ETF simply holds bars and tracks spot minus a small storage fee, with no roll mechanism to distort it.

---

## Section B — Numerical / Applied Problems

**B1. Core short hedge, both scenarios.** In April a farmer expects 50,000 bushels of wheat in September. The September future trades at \$6.00/bushel; one contract = 5,000 bushels. Show the effective price if spot at harvest is (A) \$5.20 and (B) \$6.90. Assume zero basis (futures converge to spot).

The farmer sells 50,000 / 5,000 = **10 contracts short**.

**Scenario A (spot \$5.20):** cash sale 50,000 × 5.20 = \$260,000; futures gain (6.00 − 5.20) × 50,000 = +\$40,000. Total = \$300,000 → **\$6.00/bu**.

**Scenario B (spot \$6.90):** cash sale 50,000 × 6.90 = \$345,000; futures loss (6.00 − 6.90) × 50,000 = −\$45,000. Total = \$300,000 → **\$6.00/bu**.

**Verification:** both scenarios net exactly the locked futures price of \$6.00 (\$300,000). The hedge removed *both* tails — the \$45,000 of "lost upside" in B is not a failure but the symmetric price of certainty. ✓

**B2. Cost of carry — gold (contango).** Gold spot \$2,000/oz, $r=5\%$, storage $u=1\%$, convenience yield $y\approx 0$. Compute the 1-year future and identify the curve shape.

$$F_0 = 2000\,e^{(0.05+0.01-0)\times 1} = 2000\,e^{0.06} = 2000 \times 1.061837 = \mathbf{\$2{,}123.67}.$$

Since $r+u=0.06 > y=0$, we have $F>S$ → **contango**, exactly as expected for an investment metal with cheap storage and no shortage premium. ✓

**B3. Roll drag from B2.** The investor buys the 1-year gold future at \$2,123.67. Six months later spot is *unchanged* at \$2,000. What is the now-6-month future worth, and what roll effect has occurred?

$$F_{0.5} = 2000\,e^{0.06\times 0.5} = 2000\,e^{0.03} = 2000 \times 1.030455 = \$2{,}060.91.$$

The contract the investor holds has fallen from \$2,123.67 to \$2,060.91 — a loss of **≈ \$62.76/oz** — even though spot never moved. This is the contango roll drag: the future *converges down* toward an unchanged spot. Over repeated rolls this is the drag that erodes long-only commodity index returns. ✓

**B4. Cost of carry — crude in a supply shock (backwardation).** Crude spot \$90, $r=5\%$, $u=2\%$, but refiners are desperate so $y=15\%$. Compute the 1-year future and confirm the curve shape.

$$F_0 = 90\,e^{(0.05+0.02-0.15)\times 1} = 90\,e^{-0.08} = 90 \times 0.923116 = \mathbf{\$83.08}.$$

Sign check: $r+u-y = 0.05+0.02-0.15 = -0.08 < 0$, so $F<S$ → **backwardation** ($83.08 < 90$). An index investor rolling long here buys the cheaper deferred contract and, as it rises toward spot, earns a **positive** roll yield. ✓

**B5. Consumer hedge with a call option (keeping upside).** An airline needs 1,000,000 gallons of jet fuel in three months. The relevant future is \$2.50/gal. It buys calls struck at \$2.60 for a premium of \$0.08/gal. Find the effective cost if fuel goes to (A) \$3.00 and (B) \$2.20, and state the price ceiling.

Premium paid = 0.08 × 1,000,000 = \$80,000.

**Scenario A (\$3.00):** buy fuel 1,000,000 × 3.00 = \$3,000,000; call payoff (3.00 − 2.60) × 1,000,000 = +\$400,000; plus premium −\$80,000. Net = 3,000,000 − 400,000 + 80,000 = **\$2,680,000 → \$2.68/gal**.

**Scenario B (\$2.20):** buy fuel 1,000,000 × 2.20 = \$2,200,000; call expires worthless; plus premium −\$80,000. Net = 2,200,000 + 80,000 = **\$2,280,000 → \$2.28/gal**.

**Ceiling = strike + premium = 2.60 + 0.08 = \$2.68/gal.** Verification: above \$2.60 the airline never pays more than \$2.68, yet in the falling case it still benefits (\$2.28). The \$0.08 premium is precisely the price of keeping the downside benefit that a plain future would have surrendered. ✓

**B6. Minimum-variance cross-hedge ratio.** An airline hedges jet fuel using heating-oil futures. The correlation between jet-fuel and heating-oil price *changes* is $\rho = 0.90$; $\sigma_S$ (jet fuel) = 0.030, $\sigma_F$ (heating oil futures) = 0.025 per gallon. It must cover 4,200,000 gallons; one heating-oil contract = 42,000 gallons. Find the hedge ratio and the number of contracts.

$$h^* = \rho\,\frac{\sigma_S}{\sigma_F} = 0.90 \times \frac{0.030}{0.025} = 0.90 \times 1.20 = \mathbf{1.08}.$$

Gallons to hedge in futures terms = 4,200,000 × 1.08 = 4,536,000. Contracts = 4,536,000 / 42,000 = **108 contracts (long, since the airline is a consumer)**. The ratio exceeds 1 because heating oil is *less* volatile than jet fuel, so each futures gallon offsets less risk and more must be traded. The imperfect $\rho=0.90$ is the residual cross-hedge basis risk that cannot be removed. ✓

**B7. Contango vs backwardation — index return decomposition.** Over a year, spot crude rises 8%. The investor holds a rolling futures position. Collateral earns 5%. In scenario (A) the curve was in contango costing 6% of roll drag; in scenario (B) it was in backwardation adding 4% of roll gain. Compute total return each way.

Using Total ≈ Spot + Roll + Collateral:

- **(A) Contango:** 8% − 6% + 5% = **+7%**.
- **(B) Backwardation:** 8% + 4% + 5% = **+17%**.

Same 8% spot move, a 10-percentage-point swing in outcome driven entirely by curve shape. Verification: this is the concrete reason two ETFs on the "same" commodity can diverge wildly — roll yield, not spot, often dominates. ✓

---

## Section C — Interview-Style Questions with Model Answers

**C1. "Explain to a non-specialist why a farmer would sell a contract at \$6.00 and then feel fine when wheat rallies to \$8.00."**

Model answer: "The farmer isn't trying to *win* on the futures — they're buying certainty. In April they had no idea whether September wheat would be \$4 or \$8, and they'd already spent on seed, diesel and land. Selling futures at \$6 locked that price for the whole crop. When wheat rallies to \$8, the crop is worth \$2 more but the short future loses \$2 — they net \$6, exactly as planned. A hedge is symmetric: it removes the windfall *and* the wipeout. Judging it by the futures P&L alone is a category error — you have to look at the physical and the future together."

**C2. "What is convenience yield, really? Is it a cash payment?"**

Model answer: "No, it's not a cheque. Convenience yield is the *benefit of physically holding* the commodity that a futures holder doesn't get. If you run a refinery, having crude in your tank right now means you never have to halt production over a supply hiccup — that's insurance value, an optionality. We model it *like* a dividend that the physical holder receives, because it lowers the net cost of carry, but it's implied — backed out of observed prices — not paid in cash. When inventories get dangerously low, that insurance value spikes, spot gets bid up relative to futures, and the curve tips into backwardation. So convenience yield is the market's price of physical availability."

**C3. "A client says: 'Oil has doubled over ten years, so an oil ETF must have doubled too.' How do you respond?"**

Model answer: "Almost certainly not, and the reason is roll yield. A commodity ETF can't store barrels, so it holds futures and rolls them forward every month. If the oil curve is in contango — which it often is — each roll means selling a cheaper expiring contract and buying a more expensive deferred one, a persistent drag. The ETF's return is spot *plus* roll yield *plus* collateral interest, and in sustained contango the roll drag can be so large the ETF falls even while spot rises. Only a physically-backed metal ETF — gold or silver, which store cheaply — comes close to tracking spot. So: never assume a futures ETF tracks the commodity."

**C4. "Walk me through the difference between contango, backwardation, and normal backwardation."**

Model answer: "Contango and backwardation describe the *shape of the curve today* — futures versus *current* spot. Contango is up-sloping, futures above spot, which happens when storage and financing costs beat convenience yield. Backwardation is down-sloping, futures below spot, when convenience dominates — typically a tight, shortage market. Normal backwardation is a different comparison entirely: it's Keynes's idea that futures sit below the *expected future* spot, because producers who are net short pay a risk premium to speculators for taking the price risk. The trap is thinking they're opposites — they're on different axes. A market can be in contango relative to today's spot yet still be in normal backwardation relative to expected spot. Interviewers love catching people who conflate the two."

**C5. "How would you hedge jet fuel when there's no liquid jet-fuel futures contract, and what's the catch?"**

Model answer: "I'd cross-hedge using the most correlated liquid contract — heating oil or crude, both refined products or feedstock that move closely with jet fuel. I'd size it with the minimum-variance hedge ratio, $h^* = \rho\,\sigma_S/\sigma_F$, which scales the position by the correlation and the ratio of volatilities. The catch is basis risk: jet fuel and heating oil aren't identical, so the correlation is below one, and the leftover — the 'crack' between the products, plus location and timing mismatches — can't be hedged away. I'd also align the contract expiry just after my cash-flow date to minimise timing basis. So the honest answer is: a cross-hedge dramatically reduces risk but never eliminates it, and I'd size and monitor that residual explicitly."

---

## Section D — Multiple-Choice Questions with Reasoning

**D1.** Under the cost-of-carry model $F_0 = S_0 e^{(r+u-y)T}$, an increase in convenience yield $y$, all else equal:

A) raises the futures price  B) lowers the futures price  C) leaves it unchanged  D) raises storage cost

**Answer: B.** Convenience yield enters with a *minus* sign — it is a benefit of holding the physical that reduces net carry, pulling the future *down* toward (or below) spot. A rising $y$ pushes the curve toward backwardation. A confuses it with storage $u$; C ignores the term's sign; D conflates two independent parameters.

**D2.** A commodity is in backwardation. A long index investor rolling the position will:

A) earn a positive roll yield  B) pay a negative roll yield  C) earn nothing from the roll  D) be forced to take delivery

**Answer: A.** In backwardation the deferred contract is *cheaper* than the expiring one, so rolling sells high and buys low → **positive** roll yield. B describes contango; C is wrong because the curve shape guarantees a roll effect; D is false — rolling is precisely how investors *avoid* delivery.

**D3.** Which statement about a producer's short hedge is correct?

A) It profits when prices rise  B) It converts an uncertain future selling price into a known one  C) It eliminates the physical crop  D) It only protects against price rises

**Answer: B.** A short hedge locks the selling price symmetrically — the gain or loss on the short future offsets the change in the physical's value, yielding a *known* price. A is false (the short future *loses* when prices rise, offset by the crop gaining); C confuses hedging price risk with the crop itself; D reverses the direction — a producer fears price *falls*.

**D4.** The upper bound on a commodity futures price is enforced by cash-and-carry arbitrage, but the lower bound is "soft" because:

A) storage is free  B) you cannot easily short/borrow a scarce physical commodity  C) exchanges cap prices  D) convenience yield is always zero

**Answer: B.** Reverse arbitrage (short physical, buy future) needs *borrowing* the commodity, which for a consumable in shortage is often impossible — so the lower bound cannot be forced, letting backwardation and large convenience yields persist. A is false (storage costs money); C is invented; D contradicts the whole point.

**D5.** An investor observes that a crude-oil ETF fell 20% over a period when spot oil was flat. The most likely cause is:

A) a stock split  B) negative roll yield in a contango market  C) positive convenience yield  D) the collateral return

**Answer: B.** With spot flat, the loss must come from the roll: in contango the ETF repeatedly sells low and buys high, bleeding value — the classic contango drag. A is irrelevant to commodities; C would push toward backwardation (a *tailwind*, not a drag); D (T-bill interest) is positive and small, not a 20% loss.

**D6.** "Normal backwardation" refers to a futures price that is below:

A) the current spot price  B) the expected future spot price  C) the strike price  D) the storage cost

**Answer: B.** Normal backwardation (Keynes) compares $F$ to the *expected future* spot, reflecting a risk premium paid by net-short hedgers to speculators. A is ordinary backwardation (a different axis); C and D are unrelated quantities.

**D7.** The minimum-variance hedge ratio $h^* = \rho\,\sigma_S/\sigma_F$ exceeds 1 when:

A) the correlation is negative  B) the spot exposure is more volatile than the futures, and correlation is high  C) storage costs are high  D) the market is in contango

**Answer: B.** $h^*>1$ requires $\rho\,\sigma_S/\sigma_F > 1$ — most naturally when $\sigma_S>\sigma_F$ (the thing hedged is more volatile than the futures) and $\rho$ is near 1, so more futures are needed per unit of exposure. A would make $h^*$ negative; C and D are unrelated to the ratio's formula.

**D8.** Which pairing of commodity and typical curve shape is correct?

A) Gold — usually backwardation  B) Oil in a supply shock — contango  C) Gold — usually contango  D) Oil in a glut — backwardation

**Answer: C.** Gold has cheap storage and negligible convenience yield, so $r+u>y$ → usually **contango**. A reverses this. Oil in a *shock* has high convenience → backwardation (so B is wrong), and oil in a *glut* has storage dominating → contango (so D is wrong).

---

*Self-verification notes: B1's both scenarios net exactly the \$6.00 locked price, confirming symmetric hedging. B2 ($F=\$2{,}123.67$, contango) and B4 ($F=\$83.08$, backwardation) are confirmed by the sign of $r+u-y$ (+0.06 vs −0.08). B3's roll drag (−\$62.76 with spot unchanged) demonstrates contango convergence. B5's ceiling equals strike + premium = \$2.68, verified against both fuel scenarios. B6's $h^*=1.08>1$ because $\sigma_S>\sigma_F$, giving 108 contracts. B7's 10-point outcome swing on identical spot confirms roll yield's dominance. Formulas used: $F_0=S_0e^{(r+u-y)T}$, Total return ≈ Spot + Roll + Collateral, $h^*=\rho\,\sigma_S/\sigma_F$, call ceiling = strike + premium.*
