# Q&A — Enterprise Risk Management

A practice bank for the Enterprise Risk Management chapter. Work each question before reading the answer. Numerical answers are self-checked against the two-exposure aggregation identity σ_p = √(σ₁² + σ₂² + 2ρσ₁σ₂) and the appetite chain capacity ≥ appetite ≥ Σ limits.

---

## Section A — Concept-Check (short answer)

**A1. Define Enterprise Risk Management in one sentence, and identify the four load-bearing words.**

ERM is the **holistic, integrated, top-down management of an organisation's entire portfolio of risks, aligned with its strategy and governed from the board.** The four load-bearing words: **holistic** (every risk type — financial and non-financial, downside and missed-upside — is in scope), **integrated** (risks are aggregated so correlations and concentrations become visible), **top-down** (direction flows from board-set appetite down to unit limits), and **strategy-aligned** (risk is a lens on the strategy itself, not a compliance afterthought).

**A2. Why does siloed risk management fail? Give the four structural reasons and the signature symptom.**

Silos fail because: (1) **correlations are invisible** — risks driven by the same factor look independent inside separate silos; (2) **nobody owns the total** — each silo covers its patch, so the risk *portfolio* has no owner; (3) **risk is treated as a cost to minimise, not a resource to allocate**; and (4) **strategic and emerging risks fall through the cracks** because they belong to no single silo. The signature symptom: **every desk is within its limits, yet the whole firm collapses** (the 2007-style bank).

**A3. Distinguish risk capacity, risk appetite, risk tolerance, and risk limits.**

They form a top-down hierarchy. **Risk capacity** is the *maximum* risk the firm could bear before a hard constraint (insolvency, covenant breach) — a constraint, not a choice. **Risk appetite** is how much risk the firm *chooses* to take within that capacity — a board decision. **Risk tolerance** is the acceptable *variation* around a specific objective or metric ("credit losses may vary ±20% around plan"). **Risk limits** are the hard operational thresholds allocated to individual units (a desk's VaR ceiling). Capacity > appetite > tolerance > limits.

**A4. What are the three pillars ERM rests on?**

**Risk governance** (who is accountable — the board, the three lines of defence, the CRO mandate), **risk appetite** (how much and what kinds of risk we choose to take — the RAS and limit cascade), and **risk culture** (how people actually behave toward risk day to day — tone, incentives, escalation norms). Miss any one and the structure fails.

**A5. State the three lines of defence, and name the single most common governance error.**

**First line — the business**: the people who take the risk own it (identify, control, manage within limits). **Second line — risk & compliance**: independent oversight that sets the framework, aggregates the enterprise view, and challenges the first line. **Third line — internal audit**: independent assurance to the board that lines one and two work. The most common error: believing the **second line (the risk department) owns the risk**. It does not — the *business* owns the risk it creates; the risk function only oversees.

**A6. Why must the CRO have dual reporting lines, and to whom?**

The CRO reports directly to the **CEO** *and* has an unfettered line to the **Board Risk Committee**, with the committee (not the CEO alone) controlling the CRO's appointment, removal, and pay. Dual reporting exists because pre-2008, risk heads were buried under revenue-generating executives who could overrule or silence them. The direct board line protects the CRO from being muzzled by the very people whose risk-taking they must challenge.

**A7. Name the five components of the COSO 2017 ERM framework in order.**

(1) **Governance and Culture**; (2) **Strategy and Objective-Setting**; (3) **Performance**; (4) **Review and Revision**; (5) **Information, Communication, and Reporting**. The framework deliberately leads with governance and culture because everything downstream depends on them.

**A8. What is the single biggest message of the COSO 2017 update versus the 2004 cube?**

The 2017 revision moved ERM **away from a control-and-compliance checklist toward integration with strategy and the creation and preservation of value.** Risk consideration now begins *when strategy is chosen* — including the risk that the chosen strategy misaligns with the mission and the risk of implications flowing from the strategy. ERM became a value-creating strategic discipline, not a defensive compliance chore.

**A9. Give the two-exposure aggregation formula and explain what ρ = 1 versus ρ < 1 means for a firm.**

σ_portfolio = **√(σ₁² + σ₂² + 2·ρ·σ₁·σ₂)**. When **ρ = 1** (perfect correlation), it collapses to σ₁ + σ₂ — risks simply add, the signature of dangerous **concentration**. When **ρ < 1**, combined risk is strictly less than the sum — the **diversification** benefit. A silo implicitly assumes ρ = 1 with what it can see and ρ = 0 with what it cannot, and is almost never right about either; only enterprise aggregation gets ρ approximately correct.

**A10. Why is culture said to be "70% of ERM," and how is it diagnosed before losses appear?**

Because nearly every large risk failure — Barings, Enron, Lehman, the London Whale — had adequate formal controls that people bypassed, overrode, or gamed. Structure and appetite are necessary but never sufficient; risk lives in thousands of daily decisions the framework never touches. Culture is diagnosed through **leading indicators** — near-miss reporting rates, how limit breaches are handled, employee survey data, turnover in control functions, whether risk teams are seen as partners or police — because by the time it shows up in losses, it is too late.

---

## Section B — Numerical / Applied (full solutions)

**B1. The correlation silos miss.** A bank's market-risk silo reports a one-year 99% VaR of £120m on its MBS book; its credit silo reports £120m on its mortgage loan book. Both are driven by US house prices, so the true correlation is ρ = 0.9. Compute the true aggregate and compare to what each silo sees.

- σ_p = √(120² + 120² + 2 × 0.9 × 120 × 120)
- = √(14,400 + 14,400 + 25,920) = √54,720 ≈ **£234m**.

**Self-check.** Each silo sees £120m; the naive "diversified" instinct hopes the total sits well below £240m. But at ρ = 0.9 the aggregate is £234m — **essentially additive**, because the two "different" risks are nearly the same bet on housing. The concentration only appears when you add the pieces up, which no silo does. ✓

**B2. The diversification benefit.** The same bank instead pairs its £120m MBS book with a £120m European corporate loan book at ρ = 0.2. Compute the aggregate and the capital saved versus B1.

- σ_p = √(120² + 120² + 2 × 0.2 × 120 × 120) = √(14,400 + 14,400 + 5,760) = √34,560 ≈ **£186m**.
- Saving versus the concentrated pair = 234 − 186 = **£48m** of risk.

**Self-check.** Same £120m per silo in both cases, but genuine diversification (ρ = 0.2) cuts the aggregate from £234m to £186m — a £48m difference invisible to any silo. This is ERM's offensive payoff: seeing correlations lets the firm deliberately hold the *diversifying* book and free up capital. ✓

**B3. Negative correlation — partial hedge.** An insurer writes Florida hurricane cover with σ = £80m and buys a reinsurance-linked position with σ = £30m that pays out in the same storms, giving ρ = −0.6 against the hurricane book. Compute the net risk.

- σ_p = √(80² + 30² + 2 × (−0.6) × 80 × 30) = √(6,400 + 900 − 2,880) = √4,420 ≈ **£66.5m**.

**Self-check.** The net £66.5m is *below* the standalone hurricane risk of £80m — the negatively-correlated position partly cancels it, which is the whole point of a hedge. A silo looking only at the £80m book, or naively adding £80m + £30m = £110m, would both mis-state the true £66.5m. Negative ρ subtracts. ✓

**B4. Cascading a risk appetite statement.** "BuildCo" holds £600m of loss-absorbing capital. The board sets appetite at "no more than 20% of capital at risk over one year." The CRO must allocate the resulting economic-capital budget across four risk types. State the budget and check a proposed allocation of Operational £45m, Market/FX £30m, Credit £25m, Strategic £20m.

- Enterprise appetite = 20% × £600m = **£120m**.
- Proposed allocation sum = 45 + 30 + 25 + 20 = **£120m** — exactly equals appetite. ✓
- Buffer to capacity = 600 − 120 = **£480m** held against the truly unexpected.

**Self-check.** The chain holds: capacity £600m > appetite £120m = Σ limits £120m. The firm never allocates more appetite than the board authorised, and each unit limit is a deliberate *slice* of the enterprise total, not an isolated number. Had the allocation summed to, say, £140m, the CRO would be authorising £20m more risk than the board permits — a framework breach. ✓

**B5. Amber-trigger monitoring.** BuildCo's FX desk has a hard VaR limit of £10m and an amber-escalation trigger set at 80% of limit. Its VaR climbs to £8.4m. What status is it, and what must happen?

- Amber threshold = 80% × £10m = £8.0m. Current £8.4m > £8.0m but < £10m limit.
- Status = **amber** (breach of the escalation trigger, not yet the hard limit).
- Action: escalate to the CRO and Risk Committee *now*, **before** the £10m limit is breached — the point of amber is to act ahead of a loss, not after one.

**Self-check.** A well-built RAS maps every appetite statement to a metric with a green/amber/red threshold and an escalation path. £8.4m sits in the amber band (£8m–£10m), so the framework fires early. If the desk hit £10.2m it would be red — a hard breach requiring position reduction. ✓

**B6. Silo capital versus true aggregate.** Three silos each report £50m of standalone risk (σ = 50 each). Under the naive silo approach they are simply summed. Compute (a) the silo sum, (b) the true aggregate if all three are pairwise correlated at ρ = 0.3, and comment on over- or under-holding.

- (a) Silo sum = 50 + 50 + 50 = **£150m**.
- (b) For three equal exposures: σ_p = √(3 × 50² + 2 × 0.3 × 3 pairs × 50 × 50) = √(3 × 2,500 + 6 × 0.3 × 2,500) = √(7,500 + 4,500) = √12,000 ≈ **£109.5m**.

**Self-check.** The true diversified aggregate (£109.5m) is well below the silo sum (£150m), so a firm that simply adds silo numbers **over-holds capital against diversifiable risk** by ~£40m. The mirror danger (from B1) is that when ρ is near 1 the silo sum *understates* the true aggregate. Silos are wrong in both directions; only aggregation gets it right. Formula note: n equal exposures give σ_p = σ·√(n + n(n−1)ρ); here 50·√(3 + 6×0.3) = 50·√4.8 = 50 × 2.19 ≈ 109.5. ✓

---

## Section C — Interview-Style (model answers)

**C1. "Every desk was within its limits, so how did the bank fail?"**

Because nobody was adding it all up. Each silo measured one angle of what was, in reality, a single concentrated bet — the market team measured MBS price moves, the credit team measured mortgage defaults, the treasury measured repo funding, and in a housing crisis those three are the *same event* seen three ways, correlated near 1. The firm's true exposure was not three moderate risks that diversify away; it was one enormous position on US housing, invisible to anyone looking through a single-function lens. The lesson: **local prudence does not aggregate to global safety.** ERM's aggregation step exists precisely to surface the hidden concentration that every individual limit misses.

**C2. "Is ERM just about minimising risk?"**

No — that is the most common misconception. A firm that takes no risk earns no return and eventually dies. ERM's central shift is that **risk is a resource to be consciously chosen and allocated, not merely a cost to minimise.** The job is to take the *right* risks — the ones the firm is good at and well-capitalised for — in deliberate amounts it can survive, in service of board-endorsed objectives. ERM turns risk management from a brake into a steering wheel: defensively it caps the total and surfaces concentrations; offensively it lets the firm point its finite risk-bearing capacity at its highest risk-adjusted-return opportunities.

**C3. "Walk me through the three lines of defence and tell me who owns the risk."**

The first line is the business — trading desks, lending teams, plant managers — the people who *take* the risk and therefore *own* it; they identify, control, and manage exposures within their limits. The second line is risk and compliance: independent functions that set the framework, aggregate the enterprise view, monitor limits, and provide *effective challenge* to the first line — but they do **not** own the risk. The third line is internal audit, which reports to the Audit Committee rather than management and gives the board independent assurance that lines one and two actually work. Who owns the risk? **The business — always.** The failure mode this prevents is the poacher guarding the henhouse: a unit marking its own homework with no independent challenge or assurance.

**C4. "Distinguish risk appetite from risk capacity, and why the gap matters."**

Capacity is the *maximum* the firm could bear before hitting a hard constraint — the loss-absorbing capital before insolvency or a covenant breach. Appetite is *how much the firm chooses to take*, deliberately set below capacity by the board. The gap between them is the buffer for the truly unexpected — the stress event, the model error, the correlation that spikes to 1 in a crisis. A firm that sets appetite equal to capacity has no margin for being wrong, and it will eventually be wrong. Concretely: if a firm has £600m of capacity and sets appetite at £120m, the £480m gap is what keeps a bad year from becoming a fatal one. Appetite is a choice; capacity is a limit; the distance between them is survival.

**C5. "A firm has a CRO, VaR limits on every desk, and daily risk reports — yet it loses a billion on one book. What went wrong?"**

Structure was present but culture was absent — the 30%-framework-70%-behaviour problem. Trace it through the framework: a star trader builds an outsized position and his revenue-incentivised desk head waves it through; risk analysts notice the VaR model being tweaked to *lower* reported risk but are junior, underpaid, and dismissed as "not understanding the business," so effective challenge fails; and the tone from the top is "revenue is king," making challenge of a rainmaker career-limiting. Every structural box was ticked, yet the firm blew up because the culture hollowed the framework out — the Barings and London Whale pattern. **The finest framework on paper is theatre without a culture that makes challenge safe and prudent behaviour rewarded.**

**C6. "Why did ERM and the modern CRO rise to prominence after 2008?"**

The crisis exposed two gaps ERM directly answers. First, firms were catastrophically concentrated in correlated risks their silos could not see — mortgage default, MBS prices, and repo funding were one bet no single-function team aggregated; ERM's board-owned appetite and enterprise portfolio view are the response. Second, risk heads had been buried beneath revenue-generating executives who could overrule them, so warnings never reached the board; the modern independent CRO with dual reporting is the structural fix. Regulators then hard-wired the loop into rules — Basel's ICAAP for banks and Solvency II's ORSA for insurers are, in effect, *mandatory ERM*, forcing firms to run the appetite-capacity-aggregation loop and prove it to supervisors.

---

## Section D — MCQs (with reasoning)

**D1. Which word does NOT describe the core nature of ERM?**
A) Holistic  B) Integrated  C) Bottom-up  D) Strategy-aligned

**Answer: C.** ERM is **top-down** — direction flows from board-set appetite down to unit limits. "Bottom-up" describes the *siloed* model ERM replaces, where each unit optimises locally and the firm overshoots collectively. A, B, and D are three of the four load-bearing words.

**D2. In the three lines of defence, who owns the risk?**
A) The risk management function  B) Internal audit  C) The business that takes it  D) The Chief Risk Officer

**Answer: C.** The first line — the business that creates the exposure — owns the risk. The risk function (A) and CRO (D) form the second line, which *oversees and challenges* but does not own. Internal audit (B) is the third line, providing independent assurance. Believing the risk department owns the risk is the single most common governance error.

**D3. Which correctly orders the risk appetite hierarchy from broadest to narrowest?**
A) Limits > tolerance > appetite > capacity  B) Capacity > appetite > tolerance > limits  C) Appetite > capacity > limits > tolerance  D) Tolerance > limits > appetite > capacity

**Answer: B.** Capacity (the maximum the firm *could* bear) sits at the top as a hard constraint; appetite (how much it *chooses*) sits below it; tolerance is the acceptable variation around a specific objective; and limits are the hard unit-level thresholds at the bottom. The board sets the top and it cascades down.

**D4. Two £100m exposures are perfectly correlated (ρ = 1). Their aggregate risk is:**
A) £100m  B) £141m  C) £200m  D) £0

**Answer: C.** At ρ = 1 the formula √(100² + 100² + 2×1×100×100) = √40,000 = £200m — risks simply add. This is the concentration case. Option B (£141m) is the ρ = 0 diversified answer √20,000; a silo that assumes independence when the true ρ is 1 would dangerously understate the risk.

**D5. The COSO 2017 ERM framework leads with which component?**
A) Performance  B) Information, Communication and Reporting  C) Governance and Culture  D) Review and Revision

**Answer: C.** COSO deliberately places **Governance and Culture** first because everything downstream — strategy, performance, review, reporting — depends on it. The five components in order are Governance & Culture; Strategy & Objective-Setting; Performance; Review & Revision; Information, Communication & Reporting.

**D6. The biggest shift in COSO's 2017 ERM update was to:**
A) Add more detailed control checklists  B) Integrate ERM with strategy and value creation  C) Replace the CRO with a committee  D) Mandate a specific VaR model

**Answer: B.** The 2017 revision reframed ERM from a control-and-compliance checklist toward integration with strategy and the creation and preservation of value — the "strategy risk" framing. It did the opposite of A. C and D are not part of COSO at all; COSO is a conceptual framework, not a modelling mandate.

**D7. Which statement about the Chief Risk Officer is correct?**
A) The CRO owns all of the firm's risk  B) The CRO reports only to the CEO  C) The CRO owns the framework and the portfolio view, and reports to both CEO and Board Risk Committee  D) The CRO sits in the first line of defence

**Answer: C.** The CRO owns the ERM *framework* and the aggregate portfolio view and provides independent challenge, with dual reporting to the CEO and the Board Risk Committee. The *business* owns the risk, so A is wrong (that abdication is the trap). B removes the board independence that protects the role. D is wrong — the CRO heads the *second* line.

**D8. A firm with a complete ERM framework — independent CRO, desk VaR limits, daily reports — still suffers a huge rogue-trading loss. The most likely root cause is:**
A) The VaR model was miscalibrated  B) A weak risk culture defeated the framework  C) The firm held too little capital  D) The appetite statement was not board-approved

**Answer: B.** When the entire structural apparatus exists yet the firm blows up, the failure is almost always cultural — deference to revenue, weak effective challenge, no psychological safety to report near-misses (the Barings / London Whale pattern). The chapter's central caveat: structure and appetite are necessary but not sufficient. ERM is roughly 30% framework and 70% culture.

**D9. ISO 31000 differs from COSO ERM chiefly in that it is:**
A) Bank-specific and capital-focused  B) Generic, principles-based, and universal to any organisation  C) A regulatory capital requirement  D) Concerned only with internal financial controls

**Answer: B.** ISO 31000 is a lighter, generic standard (principles, framework, and a plan-do-check-act process) applicable to any organisation of any size. COSO is more detailed and governance-heavy. Neither is itself a capital rule — that would be Basel's ICAAP or Solvency II's ORSA (C confuses the two). D describes COSO *Internal Control*, not ISO 31000.

**D10. A silo that ignores every risk outside its own patch is implicitly assuming, for those unseen risks, a correlation of:**
A) ρ = 0  B) ρ = 1  C) ρ = −1  D) ρ = 0.5

**Answer: A.** By ignoring other risks entirely, a silo behaves as if they are independent of its own — ρ = 0, capturing a full diversification benefit it has not verified. Conversely, when it can *see* an adjacent risk it often lumps it in additively (ρ = 1). It is almost never right about either; only enterprise aggregation estimates the true ρ.

---

## Recap of key relationships (self-verify against these)

- **ERM definition:** holistic, integrated, top-down, strategy-aligned management of the whole risk portfolio, governed from the board.
- **Why silos fail:** invisible correlations; hidden concentrations; nobody owns the total; strategic/emerging risks fall through the cracks. Signature: every desk within limits, whole firm collapses.
- **Three lines:** 1st = business (owns/takes risk); 2nd = risk & compliance (oversees/challenges); 3rd = internal audit (independent assurance). Business owns the risk.
- **Appetite chain:** capacity (max you *could* bear) ≥ appetite (how much you *choose*) ≥ tolerance (variation around an objective) ≥ limits (hard unit thresholds); Σ limits ≤ appetite.
- **Aggregation:** σ_p = √(σ₁² + σ₂² + 2ρσ₁σ₂); ρ→1 risks add (concentration), ρ<1 diversification benefit, ρ<0 partial hedge. For n equal exposures: σ_p = σ·√(n + n(n−1)ρ).
- **COSO 2017 — five components:** Governance & Culture; Strategy & Objective-Setting; Performance; Review & Revision; Information, Communication & Reporting. Message: integrate risk with strategy and value.
- **CRO:** owns framework + portfolio view; independent challenge; dual reporting to CEO and Board Risk Committee. Culture is 70% of ERM — structure alone is theatre.
