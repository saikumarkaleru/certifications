# Q&A — Derivatives Markets Overview

Companion practice bank for Chapter 09. Every question is followed by a full answer. Section A checks concepts, B applies them to numbers and situations, C rehearses interview questions with model answers, and D sharpens judgement on the tricky distinctions through MCQs with reasoning.

---

## Section A — Concept Check

**A1. What single idea defines a derivative, and why does the word "derived" carry the whole meaning?**

A derivative is a **contract whose value is derived from an underlying** asset, rate or index — it has no independent existence of its own. The word "derived" is load-bearing because it tells you the instrument is not a claim on an asset (the way a share or bond is); it is a bet, promise or insurance policy *about* the price of something else. A Nifty future is worth nothing in itself — it is worth exactly whatever its relationship to the Nifty index makes it worth. Kill the underlying and the derivative evaporates. Everything else — hedging, leverage, zero-sum payoffs — follows from this dependency.

**A2. What is the fundamental human problem derivatives were invented to solve?**

**Uncertainty about a future price.** A farmer, an exporter and an airline each face a price they cannot control but must live with — soybean at harvest, the rupee when the dollars arrive, crude when the fuel is bought. The instruments met earlier (shares, bonds, bills) are *claims on assets*; none of them let you fix, cap or insure a future price without owning the asset today. A derivative is the answer: a contract struck now that fixes, caps or insures the terms of a transaction that settles later, letting you transfer a risk you do not want to someone willing to bear it.

**A3. In what sense are derivatives "zero-sum," and why does that not make them useless?**

For every winner there is an equal-and-opposite loser: if the farmer's short soybean contract gains ₹10 lakh, whoever took the other side loses ₹10 lakh. Derivatives do not create or destroy wealth in aggregate — they **relocate** risk. They are not useless precisely because relocation is valuable: the farmer who cannot bear price risk hands it to a speculator who is paid to absorb it, or to a crusher with the opposite exposure. Both counterparties are better off even though no net wealth was manufactured. The value is in *who* ends up holding the risk, not in the sum of the payoffs.

**A4. Name the four questions that define any derivative, however exotic.**

(1) **What is the underlying?** — soybean, USD/INR, Nifty 50, the 10-year G-sec yield. (2) **What quantity and at what price?** — the contract size and the agreed price or rate. (3) **When does it settle?** — the expiry or maturity date. (4) **How does it settle?** — by physical delivery (the actual asset changes hands) or cash settlement (only the money profit/loss is exchanged). Answer these four and you have specified the contract completely.

**A5. Distinguish the two fundamental "shapes" a derivative can take.**

An **obligation** (forwards, futures, swaps) *binds* both parties to transact — the payoff is symmetric: you gain if the price moves your way and lose if it moves against you, with no choice. A **right without obligation** (options) lets the buyer transact but not compels it — the payoff is asymmetric: the buyer's loss is capped at the premium while the upside is open. The single question "must both parties transact, or may one choose?" separates the whole derivative universe into these two families.

**A6. Contrast forwards and futures on the key mechanical dimensions.**

A forward is a **customised, private (OTC)** agreement settled in a lump sum at maturity, carrying counterparty (default) risk and little liquidity. A future is that same forward **standardised and exchange-traded**, with three innovations that cure the forward's weaknesses: **standardisation** (fungible, hence liquid), a **clearing house / CCP** inserted between the parties (removing counterparty risk), and **daily mark-to-market margining** (losses settled every day so they can never snowball into an unpayable default). Say all four when asked: standardisation, clearing-house guarantee, daily MTM, liquidity.

**A7. Explain the asymmetry of options and why buying one is like buying insurance.**

An option gives the buyer the **right, not the obligation**, to buy (call) or sell (put) at a strike price, in exchange for an upfront **premium**. The buyer's maximum loss is that premium — known and capped — while the upside is large; the seller (writer) pockets the premium as maximum gain but bears potentially unlimited loss. This is exactly the structure of insurance: the buyer pays a small known premium for protection against a large adverse move, and the writer is the insurance company collecting steady premiums but paying out when disaster strikes.

**A8. What is a swap, and how does it differ from a forward?**

A swap is an agreement to **exchange a stream of cash flows** over time; a forward is a single future exchange. A swap is essentially a string of forwards. The classic is the **interest rate swap (IRS)**: two parties exchange interest on a notional principal, one paying fixed, the other floating (linked to MIBOR or SOFR). The notional itself is never exchanged — only the net interest difference changes hands each period. Swaps are OTC instruments used overwhelmingly by banks and large corporates.

**A9. State the three motives for entering any derivative position.**

**Hedging** — you already have an exposure and use the derivative to offset it, sacrificing upside to remove downside. **Speculation** — you have no underlying exposure and enter purely to profit from a price view, using leverage to amplify returns. **Arbitrage** — you exploit the same asset being priced differently in two places to lock in a near-riskless profit, and in doing so erase the mispricing. The instrument is identical across all three; what differs is whether you already hold the underlying and what you are trying to achieve.

**A10. Why is leverage described as the "double-edged sword" of derivatives?**

Because you trade a promise rather than buy the asset, you post only a small margin — perhaps 10% of notional — controlling a large exposure with little capital. This magnifies returns *and losses* equally: a 2% move in the underlying becomes a 20% swing on your margin. That efficiency is a virtue for a hedger (cheap protection) and a danger for a speculator (a 10% adverse move can wipe out the margin and force liquidation). The leverage is neutral; the outcome depends on how it is used.

**A11. What is the "basis," and what happens to it at expiry?**

The **basis** is the difference between the futures price and the spot price. As expiry approaches, the futures price and spot price must **converge** — the basis narrows toward zero — because at the moment of settlement a future *is* the spot. This convergence is central to how hedges perform: a hedge that relies on the basis behaving predictably can leave a residual gap (basis risk) if the two prices do not move perfectly together.

**A12. Why is most financial-derivative settlement done in cash rather than by physical delivery?**

Because many underlyings cannot be physically delivered — you cannot hand over "the Nifty 50," which is just a number. Cash settlement marks the contract against the actual index level at expiry and pays the difference in money. This lets participants take positions on prices they never intend to touch physically, and it is fully real: you receive or pay the exact monetary P&L. "Cash-settled" does not mean fake; it simply avoids the pointless movement of an asset that either does not exist physically or that neither party wants to handle.

---

## Section B — Applied / Scenario Questions

**B1. A farmer will harvest 100 tonnes of soybean in October. He locks a forward to sell at ₹4,000/tonne. Compute his outcome if October spot is (a) ₹3,500 and (b) ₹4,500, and state the real point of the hedge.**

(a) Spot ₹3,500: the open market would pay ₹3,50,000, but the forward locks ₹4,00,000 — the forward saved **₹50,000**. (b) Spot ₹4,500: the market would have paid ₹4,50,000, but he is bound to sell at ₹4,00,000, forgoing **₹50,000** of upside. Either way he receives **₹4,00,000** — the number he knew from day one. The point of the hedge is *not* to win; it is to convert an unbudgetable gamble into a fixed, plannable figure so a farmer can be a farmer, not a grain speculator.

**B2. Infosys will receive $100 million in 12 months. Spot is ₹86/$; the treasurer books a forward to sell at ₹85.50. Compute the outcome if the spot in 12 months is (a) ₹80 and (b) ₹90.**

(a) Spot ₹80: the open market gives only ₹800 crore, but the forward locks ₹855 crore — a **₹55 crore** saving versus doing nothing. (b) Spot ₹90: the market would have given ₹900 crore, but Infosys is bound to sell at ₹85.50 for ₹855 crore, "losing" **₹45 crore** of upside. In both cases the firm knew it would receive **₹855 crore** from the outset. The certainty is the deliverable; the win/loss versus the eventual spot is beside the point.

**B3. Nifty is at 24,000; one lot is 75 units. A speculator posts ₹1,80,000 margin and buys one lot. Compute the return on margin if Nifty moves (a) +2% and (b) −2%, and explain the leverage.**

Notional = 24,000 × 75 = **₹18,00,000**; margin ₹1,80,000 is ~10% ⇒ **~10× leverage**. (a) +2% ⇒ Nifty at 24,480, gain = 480 × 75 = **₹36,000 = +20%** on margin. (b) −2% ⇒ loss = **₹36,000 = −20%** on margin, and a further slide triggers a **margin call**; if unmet, the broker force-closes. A 2% market move became a 20% swing on capital — the leverage multiplier is exactly the reason ~90% of retail F&O participants lose money.

**B4. Spot Nifty = 24,000. Fair one-month futures (carry +0.5%) ≈ 24,120, but the future trades at 24,250. Describe the arbitrage and its market effect.**

The future is rich versus its 24,120 fair value. The arbitrageur simultaneously **buys the spot basket at 24,000** and **sells the future at 24,250**. At expiry spot and future converge, so the ~130-point gap (net of the carry already priced in) is captured near-risklessly. The very act of buying spot and selling futures pushes the two prices back toward parity — which is *why* such gaps are small and fleeting in liquid markets: arbitrageurs compete them away.

**B5. An airline fears crude rising from $70. It buys $75-strike crude calls at a $3/barrel premium. Compute the effective outcome if crude goes to (a) $100 and (b) $60.**

(a) Crude $100: the airline exercises, capping its effective cost near **$75 + $3 = $78/barrel** — saving about **$22/barrel** versus the market. (b) Crude $60: it lets the option lapse, loses only the **$3 premium**, and buys fuel cheaply (effective ~$63). The option behaves as insurance: a small known premium caps a catastrophic spike while leaving the airline free to enjoy cheap fuel if prices fall — unlike a future, it does not force the airline to surrender the favourable move.

**B6. A company has a floating-rate loan of ₹500 crore and fears rates rising. How does an interest rate swap help, and how much principal is actually at risk?**

The company enters a **pay-fixed / receive-floating IRS** on a ₹500 crore notional. Its floating loan interest is now offset by the floating leg it receives, and it pays a predictable fixed rate instead — it has "swapped into fixed," converting an uncertain liability into a plannable one. The **principal is never exchanged**: only the net interest difference changes hands each period. So the ₹500 crore notional is *not* the amount at risk — the exposure is merely the interest differential between fixed and floating, a small fraction of the notional.

**B7. Reliance trades at ₹1,400. You buy a one-month ₹1,450 call for a ₹30 premium. Compute your profit/loss if Reliance ends at (a) ₹1,600 and (b) ₹1,420, and identify the break-even.**

(a) ₹1,600: you exercise — the option is worth ₹1,600 − ₹1,450 = ₹150 intrinsic; minus the ₹30 premium = **₹120 net profit** per share. (b) ₹1,420: below the ₹1,450 strike, so you let it lapse and lose only the **₹30 premium**. Break-even is **strike + premium = ₹1,480**; above that you are in net profit, between ₹1,450 and ₹1,480 you recover part of the premium, and at or below ₹1,450 you lose the full ₹30. Downside capped, upside open — the defining option asymmetry.

**B8. A trader writes (sells) the same ₹1,450 Reliance call for ₹30. Describe his payoff and why his risk profile is the mirror of the buyer's.**

The writer receives ₹30 upfront — his **maximum gain**. If Reliance stays at or below ₹1,450 the call lapses and he keeps the ₹30. If Reliance rises he must deliver at ₹1,450 while the stock is worth more: at ₹1,600 he loses ₹150 − ₹30 = **₹120**; at ₹1,800 he loses ₹320; the loss grows without limit. His payoff is the exact mirror of the buyer's — capped gain, potentially unlimited loss. This is why "buying an option is risky" is a myth: the buyer's loss is capped; the *writer* carries the open-ended risk.

**B9. A jet-fuel hedger has no jet-fuel future available and hedges with crude futures instead. What risk remains, and what is it called?**

**Basis risk.** Jet fuel and crude are correlated but not identical — refining margins ("crack spreads") move independently, so the prices do not track perfectly. If crude falls but refining margins widen, the fuel price may not fall as much and the crude hedge under-compensates. The hedge removes most of the price risk but leaves a residual gap between the hedging instrument and the actual exposure. That gap is basis risk, inherent whenever you hedge one thing with a proxy for it.

---

## Section C — Interview-Style Questions with Model Answers

**C1. "In one sentence, what is a derivative, and what does it actually do for the economy?"**

*Model answer:* "A derivative is a contract whose value is derived from an underlying asset, rate or index, and what it does for the economy is relocate risk — it lets a farmer, exporter or airline hand a price risk they cannot bear to a speculator or an opposite hedger who can, so real businesses can plan through uncertainty rather than gamble on it." Give the tight definition, then pivot to the *function* — risk transfer — which is what lifts the answer above a textbook recital.

**C2. "Walk me through the difference between a forward and a future. Don't just say 'one is standardised.'"**

*Model answer:* "Economically they are the same bet — an obligation to transact at a fixed future price — but mechanically they differ on four points. Standardisation: a future has fixed sizes and expiries, making it fungible and liquid, whereas a forward is bespoke. Counterparty risk: a clearing house steps between the two sides of a future and guarantees it, so default risk is removed; a forward carries the full default risk of the other party. Settlement of P&L: a future is marked to market *daily*, so losses can never snowball, while a forward settles in one lump at maturity. Margining: futures require initial and maintenance margin, forwards usually none. The daily mark-to-market is the linchpin — it is what makes the clearing house's guarantee credible."

**C3. "A client says options are too dangerous. How do you respond?"**

*Model answer:* "It depends entirely on which side you are on. If you *buy* an option, your maximum loss is the premium — small, known and capped — and buying a put is one of the safest ways to protect a portfolio, exactly like insurance. The unlimited risk lives with the option *writer*, who collects the premium but must pay out when the market moves sharply against them. So: buying options for protection reduces your risk; writing naked options can indeed be very dangerous. Conflating the two sides is the most common retail mistake."

**C4. "Why do we even allow speculators? Aren't they just gambling?"**

*Model answer:* "Speculators are essential because they take the other side of the hedger's trade. When the farmer wants to sell his price risk, someone must buy it — and hedgers with the exact opposite exposure rarely appear in the precise size and moment needed. Speculators fill that gap: they provide **liquidity**, so hedgers can transact instantly, and they aid **price discovery**, because their competing views on future prices get aggregated into the futures curve. That gambling is what makes the market deep enough for genuine hedgers to use. Remove speculators and the farmer has no one to sell his risk to."

**C5. "Explain how the 2008 crisis was, in part, a derivatives crisis — and what changed afterward."**

*Model answer:* "It was largely an *OTC* crisis, not an exchange-traded one. A web of privately negotiated credit default swaps — insurance against mortgage-bond defaults — was unregulated, opaque and uncollateralised, so nobody knew who owed whom. When Lehman and AIG wobbled, the whole chain froze because counterparty risk was suddenly everywhere and invisible. The reform response — the G20 Pittsburgh agreement of 2009, implemented via Dodd–Frank in the US and EMIR in Europe — imported the safety features of exchanges into the OTC world: central clearing of standardised OTC derivatives, mandatory reporting to trade repositories, and margining. The lesson was not to ban derivatives but to make the opaque, unmargined corner transparent and collateralised."

**C6. "You're a treasurer. Why might you choose an OTC forward over an exchange-traded currency future?"**

*Model answer:* "Because my exposure is rarely a round, standardised size falling on an exchange expiry date. If I will receive $87.3 million on the 19th of a month, no listed future matches that notional or date, so futures leave a residual mismatch and force me to over- or under-hedge and roll positions. An OTC forward with my bank can be struck for the exact amount and date, giving a perfect hedge with no basis risk and no daily margin calls. The trade-off is counterparty risk to the bank and no public price — but for a treasury managing a specific dated cash flow, the customisation usually outweighs the transparency and CCP protection of the future."

**C7. "Give me the cost-of-carry model and tell me what it means intuitively."**

*Model answer:* "Futures price is approximately spot times (1 + r − d) to the power T, where r is the financing cost of holding the asset, d is any yield or dividend it pays, and T is the time to expiry. Intuitively, buying the asset today and holding it must cost the same as buying a future on it — otherwise there is free money. Holding today means paying financing r but earning dividend d; the future avoids both, so it must trade at spot grossed up by net carry, r minus d. If it doesn't, arbitrageurs do cash-and-carry — buy spot, sell the rich future — until parity returns. The basis is exactly this carry, and it converges to zero at expiry."

**C8. "Close the interview: sum up the whole philosophy of derivatives in a sentence or two."**

*Model answer:* "Derivatives don't create or destroy risk — they relocate it from those who don't want it to those who do; leverage is what makes that transfer efficient, and, in the wrong hands, dangerous. Get that one idea and everything else — why 90% of retail F&O traders lose money, why 2008 happened, and why a farmer can finally sleep at night — is the same story told from different seats."

---

## Section D — MCQs with Reasoning

**D1. The value of a derivative comes primarily from:**
(a) The creditworthiness of the exchange
(b) An underlying asset, rate or index
(c) The dividends it pays
(d) Its face value

**Answer: (b).** A derivative is by definition a contract whose value is *derived* from an underlying — a commodity, currency, stock, index or rate. It pays no dividends of its own (c), has no meaningful face value like a bond (d), and while the exchange/CCP guarantees settlement, that is not the *source* of value (a).

**D2. Which feature is unique to futures and absent in forwards?**
(a) An obligation to transact
(b) A fixed price agreed today
(c) Daily mark-to-market settlement through a clearing house
(d) A future settlement date

**Answer: (c).** Both instruments share the obligation (a), the fixed agreed price (b) and a future date (d) — they are economically the same bet. What distinguishes a future is the machinery of standardisation, a clearing house, and **daily mark-to-market margining**, which forwards lack.

**D3. An option buyer's maximum loss is:**
(a) Unlimited
(b) The strike price
(c) The premium paid
(d) The notional value

**Answer: (c).** The defining asymmetry of options: the buyer risks only the upfront premium, while retaining large upside. Unlimited loss (a) belongs to the option *writer*, not the buyer. The strike (b) is the transaction price, not the loss; the notional (d) is not at risk to the buyer.

**D4. In an interest rate swap, the notional principal is:**
(a) Exchanged at the start and returned at maturity
(b) Never exchanged; only net interest flows change hands
(c) Paid by the fixed-rate payer only
(d) The maximum amount at risk

**Answer: (b).** In a plain-vanilla IRS the notional is purely a reference figure for calculating interest; it is never exchanged, and only the net interest differential is paid each period. It is therefore *not* the amount at risk (d) — a classic confusion. (Currency swaps, by contrast, may exchange principal, but the question specifies an interest rate swap.)

**D5. A hedger, unlike a speculator, is characterised by:**
(a) Using leverage
(b) Already holding an underlying exposure that the derivative offsets
(c) Trading only on exchanges
(d) Always making a profit

**Answer: (b).** The distinguishing fact is whether you already carry the underlying exposure. A hedger has one and uses the derivative to offset it; a speculator has none and takes the position purely for a view. Both may use leverage (a) and both may trade on exchanges (c). Hedging removes risk but does not guarantee profit (d) — indeed it deliberately forgoes upside.

**D6. Indian *index* options (Nifty, Bank Nifty) are:**
(a) American-style and physically delivered
(b) European-style and cash-settled
(c) American-style and cash-settled
(d) European-style and physically delivered

**Answer: (b).** Indian index options are **European** (exercisable only at expiry) and **cash-settled** (you cannot deliver an index — the money P&L is exchanged). Single-*stock* derivatives in India differ: they are delivery (physically) settled, and stock options are American-style. Knowing this split is a common interview check.

**D7. The 2008 financial crisis was amplified primarily by:**
(a) Exchange-traded futures with daily margining
(b) Opaque, unmargined OTC derivatives such as credit default swaps
(c) A ban on derivatives trading
(d) Excessive use of Nifty options

**Answer: (b).** The crisis was largely an OTC problem: unregulated, opaque, uncollateralised CDS meant no one could see who owed whom, so a single failure froze the whole chain. Exchange-traded, margined futures (a) were precisely the *safe* corner whose features reforms later imported into the OTC world. There was no ban (c), and Indian index options (d) are irrelevant to a US crisis.

**D8. Approximately what fraction of individual F&O traders in India lose money, per SEBI's 2024 study, and what is the root cause?**
(a) About 10%, due to high brokerage
(b) About 50%, due to taxes
(c) About 90%, driven by leverage magnifying losses
(d) About 30%, due to poor internet connectivity

**Answer: (c).** SEBI's 2024 study found roughly **90% of individual F&O traders lose money**. The root cause is **leverage**: a small margin controls a large notional, so ordinary adverse moves are magnified into large losses, and margin calls force liquidation at the worst moments. This is why SEBI has tightened the segment with larger lot sizes, fewer weekly expiries and upfront premium collection.

**D9. In India, which regulator oversees a corporate's OTC currency forward booked with its bank?**
(a) SEBI
(b) RBI
(c) MCX
(d) The clearing corporation

**Answer: (b).** OTC interest-rate and currency derivatives — the domain of banks and corporates — fall under the **RBI**. SEBI (a) regulates exchange-traded equity, index, currency and commodity derivatives. MCX (c) is an exchange, not a regulator, and the clearing corporation (d) guarantees settlement but does not regulate. Note the split: an *exchange-traded* currency future is SEBI's, but an *OTC* currency forward is RBI's.

---

*End of Q&A bank for Chapter 09 — Derivatives Markets Overview.*
