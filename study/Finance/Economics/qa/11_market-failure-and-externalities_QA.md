# Q&A — Market Failure and Externalities

A companion practice bank for the concept guide *Market Failure and Externalities*. Every question is followed by a full answer: Section A locks the definitions, Section B builds numerical fluency, Section C rehearses finance-interview framing, and Section D pressure-tests your reasoning against distractors.

---

## Section A — Concept-Check Questions

**A1. What single organising question does this chapter answer, and what benchmark defines "failure"?**

The question is: *when and why does the invisible hand fail, and what can be done about it?* The benchmark is the **First Fundamental Theorem of Welfare Economics** — a competitive equilibrium is Pareto efficient. A market "fails" precisely when its outcome departs from that ideal: the quantity traded diverges from the quantity that maximises total social welfare, destroying value. Failure is meaningful only against the efficient ideal it departs from.

**A2. Define market failure and name its four classic sources.**

Market failure is a free, competitive market producing an allocation that is **not Pareto efficient**, so there is avoidable **deadweight loss**. The four sources are: (1) **externalities**, (2) **public goods**, (3) **information asymmetry**, and (4) **market power** (monopoly/oligopoly). The unifying theme is a divergence between **private and social calculus** — each actor optimises against the costs and benefits they personally face, not those society faces.

**A3. Write the cost- and benefit-side identities that formalise an externality.**

- **MSC = MPC + MEC** (marginal social cost = marginal private cost + marginal external cost).
- **MSB = MPB + MEB** (marginal social benefit = marginal private benefit + marginal external benefit).

The market equates MPB with MPC because no one pays or is paid for the external terms; efficiency requires equating **MSB with MSC**. The gap between the two is the source of the misallocation.

**A4. State the sign rule linking the direction of an externality to over- or under-production.**

- **Negative externality** → an external cost exists → MSC > MPC (production) or MSB < MPB (consumption) → the market **over-produces**.
- **Positive externality** → an external benefit exists → MSB > MPB (consumption) or MSC < MPC (production) → the market **under-produces**.

Deadweight loss appears in either case, as a triangle over the range between the market quantity and the social optimum.

**A5. What is a Pigouvian tax, and how large should it be?**

A **Pigouvian tax** is a corrective tax on a negative externality that raises the private cost until **MPC + tax = MSC**, forcing the actor to *internalise* the spillover. It should equal the **marginal external cost at the efficient quantity**, not the amount that maximises revenue. Its symmetric counterpart, a **subsidy**, fixes a positive externality by lowering private cost until private incentives match social value.

**A6. State the Coase theorem and its critical precondition.**

The Coase theorem says that if **property rights are clearly assigned** and **transaction costs are zero**, private parties will bargain their way to the efficient outcome *regardless of who holds the right*. The initial allocation of rights determines who ends up richer, but not whether the outcome is efficient. The critical precondition is zero (or low) transaction costs — with millions of dispersed victims, hard-to-identify polluters, or strategic holdouts, bargaining collapses and intervention becomes the realistic instrument.

**A7. What two properties define a public good, and what failure do they cause?**

**Non-rivalry** (one person's use doesn't reduce what's available to others) and **non-excludability** (non-payers cannot practically be prevented from consuming). Non-excludability creates the **free-rider problem**: every rational individual would rather enjoy the good while others pay, so it is under-provided or not provided at all — hence tax-funded public provision.

**A8. Fill in the 2×2 goods matrix by rivalry and excludability.**

| | Excludable | Non-excludable |
|---|---|---|
| **Rivalrous** | Private good (sandwich) | Common resource (ocean fish) |
| **Non-rivalrous** | Club good (toll road) | Pure public good (national defence) |

The bottom-left cell (rivalrous, non-excludable) generates the **Tragedy of the Commons**; the bottom-right generates the **free-rider problem**.

**A9. Distinguish adverse selection from moral hazard.**

Both are information-asymmetry failures; the key is **timing**. **Adverse selection** is *hidden information before* the trade — you don't know who you're dealing with (Akerlof's lemons: bad quality drives out good). **Moral hazard** is *hidden action after* the trade — behaviour changes once consequences are shifted onto others (an insured person becomes careless; a bailed-out bank takes reckless risk). "Selection" happens as people sort into a contract; "hazard" happens as they act within it.

**A10. Name the standard remedies for information asymmetry.**

- **Signalling** — the *informed* party credibly reveals quality via a costly action (warranties, degrees, dividends, insider equity).
- **Screening** — the *uninformed* party offers a menu that induces self-revelation (deductible-vs-premium insurance plans).
- **Disclosure and reputation** — audited accounts, credit ratings, brands.
- **Incentive alignment** — deductibles/co-pays, deferred bonuses and clawbacks, manager equity (skin in the game) — chiefly to curb moral hazard.

**A11. What is government failure, and why does it matter for the intervention case?**

Government failure is intervention that fails to improve on — or worsens — the market outcome, through poor information, **regulatory capture**, distortions, unintended consequences, or political delay. It matters because market failure establishes only a *potential* case for intervention. The honest test is **comparative**: does feasible real-world policy beat the imperfect market? Market failure is a *necessary but not sufficient* condition for acting.

**A12. Why is a pecuniary externality NOT a market failure?**

A true (technological) externality is an *uncompensated physical* spillover — pollution, congestion. A **pecuniary externality** merely affects others *through prices* (a new buyer bidding up house prices). The latter is just the price mechanism doing its coordinating job and reallocating surplus; no social cost is unpriced, so there is no efficiency loss. Only real, non-priced spillovers count as failure.

---

## Section B — Applied / Numerical Problems (with full solutions)

**B1. Finding the social optimum.** A chemical plant faces MPC = 10 + 2Q (₹) and the market demand (MPB) is P = 100 − 3Q. Each unit imposes a constant external cost of MEC = ₹10. Find (i) the market quantity, (ii) the socially optimal quantity, and (iii) the correct Pigouvian tax.

**Solution.**
(i) Market equates MPB = MPC: 100 − 3Q = 10 + 2Q → 90 = 5Q → **Q_market = 18**.
(ii) MSC = MPC + MEC = (10 + 2Q) + 10 = 20 + 2Q. Optimum where MSB = MSC: 100 − 3Q = 20 + 2Q → 80 = 5Q → **Q_social = 16**.
(iii) The tax should equal the marginal external cost, **₹10 per unit** — this shifts MPC up to MSC so the market itself chooses Q = 16.

**B2. Deadweight loss from over-production.** Using B1, quantify the deadweight loss of the unregulated market.

**Solution.** DWL is the triangle between MSC and MSB (=demand) over the over-produced range Q = 16 to 18. At each unit in that range MSC exceeds MSB; the gap is zero at Q = 16 and widens to (MSC − MSB) at Q = 18.
- At Q = 18: MSC = 20 + 2(18) = 56; MSB = 100 − 3(18) = 46. Gap = 56 − 46 = **₹10**.
- Base of triangle = 18 − 16 = 2 units; height = ₹10.
- **DWL = ½ × 2 × 10 = ₹10.** Those two units cost society more than they are worth.

**B3. Pigouvian tax revenue vs purpose.** In B1, after the ₹10 tax the market produces 16 units. How much tax revenue is raised, and why is that number *not* the point of the tax?

**Solution.** Revenue = tax × quantity = ₹10 × 16 = **₹160**. But the tax's purpose is corrective, not fiscal: it exists to move quantity from 18 to the efficient 16 by internalising the external cost. The revenue is a *by-product*. Setting the tax to maximise receipts would be a different (and generally inefficient) exercise — the "right" tax equals the marginal external cost, full stop.

**B4. Positive consumption externality.** Vaccination has MPB = 60 − 2Q and MPC (=supply) = 10 + 3Q, with a constant external benefit MEB = ₹15 per vaccination. Find the private and socially optimal quantities and the corrective subsidy.

**Solution.**
- Private market: MPB = MPC → 60 − 2Q = 10 + 3Q → 50 = 5Q → **Q_private = 10**.
- MSB = MPB + MEB = (60 − 2Q) + 15 = 75 − 2Q. Optimum: MSB = MSC(=MPC) → 75 − 2Q = 10 + 3Q → 65 = 5Q → **Q_social = 13**.
- The market **under-produces** (10 < 13). A per-unit **subsidy of ₹15** (the marginal external benefit) aligns private and social incentives, raising output to 13.

**B5. Coasean bargaining.** A factory's pollution imposes ₹8,000 of harm on a neighbouring laundry. The factory can install a filter for ₹5,000 that eliminates the harm. Show that the efficient outcome (filter installed) emerges regardless of who holds the property right, and state who pays in each case.

**Solution.** Efficiency requires the filter, because its cost (₹5,000) is below the harm avoided (₹8,000).
- **If the laundry has the right to clean air:** the factory must either stop the harm or compensate ₹8,000. It prefers the ₹5,000 filter. *Factory pays ₹5,000.*
- **If the factory has the right to pollute:** the laundry would pay up to ₹8,000 to remove ₹8,000 of harm; it happily pays the ₹5,000 filter cost (or pays the factory something between ₹5,000 and ₹8,000 to install it). *Laundry pays.*
Either way the filter is installed — the efficient outcome. Only the **distribution of wealth** (who bears the ₹5,000) depends on the initial right, exactly as Coase predicts.

**B6. Cap-and-trade least-cost abatement.** Two firms must jointly cut 10 tonnes of emissions. Firm A abates at ₹200/tonne, Firm B at ₹500/tonne. Compare (a) a uniform mandate of 5 tonnes each with (b) tradable permits, and show the cost saving.

**Solution.**
(a) Uniform mandate: cost = 5×200 + 5×500 = 1,000 + 2,500 = **₹3,500**.
(b) With trading, the cheap abater does more. Firm A cuts all 10 tonnes at ₹200 (₹2,000) and sells permits to B for the 5 tonnes B was required to cut. B pays A something between ₹200 and ₹500 per tonne rather than abating at ₹500. **Total abatement cost = ₹2,000** (plus a transfer that nets to zero across the two firms).
- **Society saves ₹3,500 − ₹2,000 = ₹1,500** by letting the market allocate abatement to the low-cost firm — the efficiency case for cap-and-trade.

**B7. Lemons unravelling.** A used-car market has equal numbers of "peaches" worth ₹6,00,000 and "lemons" worth ₹2,00,000 to buyers; only sellers know which is which. Peach owners won't sell below ₹5,00,000; lemon owners will sell for anything above ₹1,00,000. Show why the good cars may vanish.

**Solution.** Buyers can't tell types apart, so they pay at most the *expected* value: if both types are present in equal proportion, expected value = ½(6,00,000) + ½(2,00,000) = **₹4,00,000**. But peach owners require ₹5,00,000 — above ₹4,00,000 — so **they withdraw**. Now only lemons remain; rational buyers revise the expected value down to ₹2,00,000, the market price collapses toward the lemon value, and the mutually beneficial trades in good cars never happen. Bad quality has driven out good — adverse selection in action.

**B8. Insurance death spiral.** A health insurer sets premiums at the *average* claim cost of its pool. Healthy members cost ₹10,000/year, sick members ₹50,000/year, and the pool starts 50/50. Trace what happens when healthy members can freely exit.

**Solution.**
- Initial average = ½(10,000) + ½(50,000) = **₹30,000** premium.
- Healthy members (true cost ₹10,000) find ₹30,000 a bad deal and **drop out**. The pool tilts toward the sick.
- New average rises — say to ₹40,000 — driving out the next-healthiest tier, and so on.
- Premiums chase an ever-sicker pool upward: an **adverse-selection death spiral**. The remedy is to break the exit option — **mandatory participation** (compulsory pooling) or community rating with an individual mandate — so healthy members can't self-select out.

---

## Section C — Interview-Style Questions (with model answers)

**C1. "In one minute, what is market failure and why should a finance professional care?"**

Model answer: "Market failure is when a competitive market's outcome isn't Pareto efficient because prices don't capture all social costs and benefits — you get avoidable deadweight loss. There are four sources: externalities, public goods, information asymmetry, and market power. I care because almost every piece of financial regulation exists to fix one of them. Deposit insurance, disclosure rules, capital requirements, credit-rating oversight, insider-trading law — these aren't arbitrary; they're corrections for the exact failures that riddle financial markets. Market failure is the operating logic behind how markets are designed and policed."

**C2. "Explain the 2008 crisis through the lens of market failure."**

Model answer: "Two failures compounding. First, an **externality**: a leveraged, interconnected bank's private cost is its own possible failure, but its collapse freezes interbank lending, triggers fire sales, and forces bailouts — costs borne by the whole economy, so banks took *too much* systemic risk. Second, **information asymmetry**: mortgage-backed securities were Akerlof's lemons market at scale — investors couldn't see loan quality — and 'originate-to-distribute' added moral hazard because originators bore no default risk and stopped screening. When doubts surfaced, buyers couldn't tell good tranches from bad and refused to buy any; the market froze, exactly as adverse selection predicts. Basel III capital rules and risk-retention 'skin in the game' rules are the corrective responses."

**C3. "What is ESG investing in the language of externalities?"**

Model answer: "ESG is fundamentally a bet that negative externalities get **internalised**. A company that emits carbon imposes costs its share price historically ignored. ESG says those costs will progressively be priced in — through carbon taxes, emissions-trading schemes, litigation, and regulatory and consumer pressure — so 'dirty' assets carry a hidden liability and face **transition risk**. Carbon markets like the EU ETS are the explicit mechanism turning the externality into a balance-sheet cost. There's also an information-asymmetry angle: **greenwashing** is adverse selection — firms overstate sustainability and investors can't verify — which is why standardised disclosure like ISSB and TCFD matters, as a screening and signalling device."

**C4. "A bank takes reckless risk because it expects a bailout. Name and explain the problem, and the fix."**

Model answer: "That's **moral hazard** — hidden action after an implicit contract. 'Too big to fail' socialises losses while privatising gains, so the bank's private cost of risk is below the social cost and it over-produces risk. Deposit insurance creates the same dynamic: insured depositors stop monitoring the bank. The fix is layered — you keep the insurance, because it solves a genuine bank-run public-goods problem, but pair it with **capital requirements, supervision, and risk-based premiums**, plus a surcharge on globally systemic banks that acts as a Pigouvian tax on being big and connected. Intervention layered to fix the failure the first intervention created."

**C5. "Why can't the private market just provide financial stability itself?"**

Model answer: "Because financial stability is a **public good** — it's non-rival (my confidence in the system doesn't reduce yours) and non-excludable (you can't withhold stability from a non-contributing bank). That triggers the **free-rider problem**: every institution would rather others bear the cost of prudence and stability while it enjoys the benefit. So it's under-provided by the market, which is why the central bank and regulators must supply it — through lender-of-last-resort facilities, macroprudential policy, and stress testing. It's the same logic as national defence, just applied to the financial system."

**C6. "Coase says externalities can be solved without government. Do you buy it?"**

Model answer: "Partly — and it's often misquoted. Coase's real insight is that externalities are frequently a *property-rights* problem, not an inevitable case for a tax. With clear rights and low transaction costs, private bargaining reaches efficiency regardless of who holds the right — and cap-and-trade is exactly that operationalised: government *creates* a tradable right to pollute and lets bargaining allocate it. But the precondition is zero transaction costs, which breaks down for climate change and any case with millions of dispersed victims. So Coase doesn't mean 'leave it to the market' — it means diagnose whether the failure is a missing-rights problem, and intervene where bargaining is too costly."

**C7. "Give me the sophisticated version of 'markets fail, so government should step in.'"**

Model answer: "I'd resist that leap. Market failure is a *necessary but not sufficient* condition for intervention — it establishes only a *potential* welfare gain. The honest question is comparative: does feasible real-world policy actually beat the imperfect market? Because government fails too — regulators lack information, get captured by the industries they oversee, create distortions, and move slowly. A carbon tax at the wrong level, subsidies that get capitalised into prices, or bailouts that entrench moral hazard can leave society worse off. So the mature framing weighs an imperfect market against imperfect intervention, case by case, rather than measuring the market against a perfect ideal."

---

## Section D — Multiple-Choice Questions (with reasoning)

**D1.** A negative production externality means that at the market quantity:
A. MSC = MPC B. MSC > MPB C. MSC > MPC D. MSB > MSC

**Answer: C.** A negative externality adds an external cost, so social cost exceeds private cost: MSC = MPC + MEC > MPC. This wedge is why the market over-produces relative to the social optimum.

**D2.** The correct Pigouvian tax on a polluting firm equals:
A. The firm's total private cost B. The marginal external cost at the efficient quantity C. The amount that maximises tax revenue D. The firm's economic profit

**Answer: B.** The tax must internalise the spillover by setting MPC + tax = MSC, so it equals the marginal external cost at the efficient quantity. Revenue (C) is a by-product, not the objective.

**D3.** The Coase theorem's efficient outcome requires:
A. Government to assign the tax B. Clear property rights and zero transaction costs C. Equal wealth between the parties D. The polluter to hold the right

**Answer: B.** Coase requires well-defined property rights and negligible transaction costs; the outcome is then efficient *regardless* of who holds the right (ruling out D) and independent of the wealth distribution (ruling out C).

**D4.** A pure public good is best described as:
A. Rival and excludable B. Non-rival and excludable C. Rival and non-excludable D. Non-rival and non-excludable

**Answer: D.** A pure public good has both properties — national defence, a lighthouse. Non-rival + excludable (B) is a club good; rival + non-excludable (C) is a common resource; rival + excludable (A) is a private good.

**D5.** The "market for lemons" is an example of:
A. Moral hazard B. Adverse selection C. A public good D. The tragedy of the commons

**Answer: B.** Hidden quality *before* the trade causes bad cars to drive out good — adverse selection. Moral hazard (A) is hidden *action after* the contract, a different failure.

**D6.** A person drives more recklessly after buying full car insurance. This is:
A. Adverse selection B. A positive externality C. Moral hazard D. A pecuniary externality

**Answer: C.** Behaviour changes *after* the contract because the insured no longer bears the full consequences — the textbook definition of moral hazard.

**D7.** Which is a common resource (rivalrous but non-excludable)?
A. National defence B. A subscription streaming service C. An ocean fishery D. A private sandwich

**Answer: C.** A fishery is rival (one boat's catch reduces the stock) but non-excludable (hard to fence the ocean), producing the tragedy of the commons. Defence (A) is a pure public good; streaming (B) is a club good; a sandwich (D) is a private good.

**D8.** A positive consumption externality (e.g. vaccination) causes the market to:
A. Over-produce, corrected by a tax B. Under-produce, corrected by a subsidy C. Produce the efficient quantity D. Shut down entirely

**Answer: B.** With MSB > MPB, buyers ignore the external benefit and under-consume; a subsidy equal to the marginal external benefit raises output to the social optimum.

**D9.** A new buyer bidding up house prices in a neighbourhood is:
A. A negative externality requiring a tax B. A pecuniary externality, not a market failure C. Moral hazard D. A public-good problem

**Answer: B.** This works *through prices*, not an unpriced physical spillover, so it is a pecuniary externality — the price mechanism functioning normally — and is not a market failure.

**D10.** "Market failure justifies intervention" is best refined to:
A. Intervention always improves welfare B. Market failure is sufficient for intervention C. Market failure is necessary but not sufficient; intervention must beat the imperfect market D. Markets never fail

**Answer: C.** Because of government failure and regulatory capture, market failure establishes only a *potential* gain; the correct test is comparative — whether feasible policy actually outperforms the flawed market.

---

*End of practice bank. Cross-reference the concept guide's sections on the MPC/MSC wedge, the Coase theorem, the 2×2 goods matrix, and the adverse-selection/moral-hazard split to cement why this framework is the operating logic behind financial regulation, systemic-risk policy, and ESG.*
