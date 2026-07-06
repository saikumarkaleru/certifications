# Q&A — Introduction to Risk Management

A companion practice bank for Chapter 01. Every question is followed by a full answer. Work each one before reading the solution.

---

## Section A — Concept Check

**A1. Why is it wrong to say the goal of risk management is to "avoid risk"?**
Because the business model of every financial institution *is* the deliberate acceptance of risk in exchange for return. A bank earns by lending (accepting default risk), an asset manager by holding volatile assets, an insurer by writing uncertain claims. Remove the risk and you remove the profit. The goal is therefore to take the *right amount* of the *right risks* consciously, being *paid* for them, backed by enough capital to survive being wrong — not to eliminate risk. A zero-risk bank earns nothing and dies slowly.

**A2. State the four questions risk management must continuously answer.**
(1) *What can go wrong?* — identification. (2) *How badly, and how likely?* — measurement. (3) *Can we survive it, and is the reward worth it?* — appetite and capital. (4) *Who is watching, and what do we do about it?* — monitoring, mitigation, and governance.

**A3. Distinguish expected loss, unexpected loss, and catastrophic loss, and say how each is funded.**
Expected Loss (EL) is the average loss anticipated over many periods — a *cost of doing business*, priced into spreads/premiums and covered by provisions. Unexpected Loss (UL) is the volatility *around* the average — the true risk — absorbed by **capital** (economic and regulatory). Catastrophic/tail loss is the rare extreme beyond what capital is sized for — addressed by stress testing, contingency planning, and, as a last resort, the possibility of failure. Key point: EL should never surprise you; UL is why banks hold capital.

**A4. Explain the Knightian distinction between risk and uncertainty and the practical lesson.**
Risk is randomness with a *knowable/estimable* probability distribution — measurable, insurable, capital can be sized against it (e.g., default rates on a large loan book). Uncertainty is randomness whose distribution is *unknown or unknowable* — novel events, structural breaks — not directly measurable and resistant to conventional capital sizing. Practical lesson: **models handle risk; stress tests, buffers and judgment handle uncertainty.** Plugging a fabricated probability into a model to make uncertainty *look* like measurable risk (e.g., the 2008 assumption that national house prices could not fall together) is a classic, dangerous error.

**A5. List the five steps of the risk management process, in order, and note why it is a loop.**
Identify → Measure → Monitor → Mitigate → Report. It is a closed loop, not a line, because the risk landscape never stands still: reporting feeds fresh identification, and the environment keeps changing, so the cycle repeats forever.

**A6. Name the four risk treatments (the "4 T's") and give an example of each.**
Accept/tolerate — retain the risk and hold capital against it (a bank keeps diversified credit risk it is paid to take). Avoid/terminate — exit the activity (stop lending to an unacceptable sector). Reduce/mitigate — lower probability or impact (collateral, covenants, diversification, limits). Transfer/share — move it to a third party (insurance, hedging, securitization). Note that *accept* is a legitimate, deliberate, capitalized choice — not a failure.

**A7. Put the appetite hierarchy in the correct nesting order and define capacity vs appetite.**
Actual Exposure ≤ Limit ≤ Tolerance ≤ Appetite < Capacity. **Risk capacity** is the *maximum* risk the firm could bear before breaching regulatory minimums or failing — set by capital and liquidity, not preference. **Risk appetite** is the aggregate risk the board *wants* to take. Appetite must sit *below* capacity, leaving a safety margin; when appetite drifts up to capacity, the firm is flying without a buffer.

**A8. In the three lines of defence, who owns the risk, and why does independence increase across the lines?**
The **first line** — the business/operations that take the risk — *owns* it. The **second line** (risk management and compliance, led by the CRO) sets the framework and *challenges* the first line. The **third line** (internal audit) provides *independent assurance* that the first two work. Independence increases with distance from the money-making so that no single group both takes risk and judges whether it is acceptable. Barings collapsed partly because one person (Nick Leeson) controlled both trading and settlement, collapsing the separation of duties.

---

## Section B — Numerical / Applied (full solutions)

**B1. Expected loss on a single loan.**
A loan has EAD = ₹2,00,00,000 (₹2 crore), one-year PD = 3%, and expected recovery of 55% on default. Compute the annual expected loss and the minimum spread (in %) needed just to cover it.

*Solution.* LGD = 1 − recovery = 1 − 0.55 = 0.45.
EL = PD × LGD × EAD = 0.03 × 0.45 × 2,00,00,000 = 0.0135 × 2,00,00,000 = **₹2,70,000**.
Minimum credit spread = EL / EAD = 2,70,000 / 2,00,00,000 = **1.35%**. The loan must earn at least 1.35% purely to cover credit losses, on top of funding cost, operating cost, and a target return on capital.
*Check (probability-weighted route):* loss-in-default = 0.45 × ₹2 crore = ₹90,00,000; × PD 0.03 = ₹2,70,000. ✓ Both routes reconcile.

**B2. Portfolio expected loss.**
A bank holds 500 independent loans, each with EAD = ₹10,00,000, PD = 1.5%, recovery = 55%. Find total annual expected loss.

*Solution.* LGD = 0.45. Per-loan EL = 0.015 × 0.45 × 10,00,000 = 0.00675 × 10,00,000 = ₹6,750.
Portfolio EL = 500 × 6,750 = **₹33,75,000 (₹33.75 lakh)**.
*Note:* this is the *expected* (priced-in) figure, not the risk. If defaults were perfectly correlated all 500 could default together; independence makes the realised loss far more predictable. The volatility around ₹33.75 lakh is the unexpected loss that capital must cover.

**B3. Parametric VaR at two confidence levels and a 10-day horizon.**
An equity portfolio worth V = ₹20 crore has daily return volatility σ = 2%. Compute 1-day 95% VaR, 1-day 99% VaR, and 10-day 99% VaR. (z₉₅ = 1.645, z₉₉ = 2.326.)

*Solution.* VaR = z × σ × V.
1-day 95%: 1.645 × 0.02 × 20,00,00,000 = 0.0329 × 20,00,00,000 = **₹65,80,000 (₹65.8 lakh)**.
1-day 99%: 2.326 × 0.02 × 20,00,00,000 = 0.04652 × 20,00,00,000 = **₹93,04,000 (₹93.04 lakh)**.
10-day 99% (square-root-of-time rule): 93,04,000 × √10 = 93,04,000 × 3.162 = **₹2,94,19,248 ≈ ₹2.94 crore**.
*Interpretation:* on ~99 days in 100 the portfolio should not lose more than ₹93.04 lakh in a day; VaR gives the *threshold*, not the size of the tail beyond it. Higher confidence and longer horizon both raise the number — which is why a VaR figure is meaningless without its confidence level and horizon stated.

**B4. VaR limit utilisation and a breach.**
A trading book worth ₹15 crore has σ = 1.2% daily. The board's market-risk tolerance is a 1-day 99% VaR limit of ₹45 lakh. (a) Compute current VaR and limit utilisation. (b) If new positions raise σ to 1.3%, does the desk breach the limit?

*Solution.* (a) VaR = 2.326 × 0.012 × 15,00,00,000 = 0.027912 × 15,00,00,000 = **₹41,86,800 (₹41.87 lakh)**. Utilisation = 41,86,800 / 45,00,000 = **93.0%** — inside the limit, but little headroom.
(b) New VaR = 2.326 × 0.013 × 15,00,00,000 = 0.030238 × 15,00,00,000 = **₹45,35,700 (₹45.36 lakh)**. Since ₹45.36 lakh > ₹45 lakh, the desk **breaches** the limit, triggering escalation to the second line. This shows measurement (Step 2) feeding monitoring (Step 3) against tolerance — the framework working as one machine.

**B5. RAROC and the hurdle rate.**
A lending desk generates annual revenue (net of funding) ₹80,00,000, operating costs ₹20,00,000, expected loss ₹15,00,000, and consumes economic capital of ₹1,50,00,000. The bank's cost of equity (hurdle) is 15%. Compute RAROC and state whether the desk creates value.

*Solution.* RAROC = (Revenue − Costs − EL) / Economic Capital = (80,00,000 − 20,00,000 − 15,00,000) / 1,50,00,000 = 45,00,000 / 1,50,00,000 = **30%**.
Since 30% > 15% hurdle, the desk **creates shareholder value** — it earns twice its cost of capital per unit of risk. Had RAROC fallen below 15%, the desk would be *destroying* value despite being profitable in accounting terms — a signal invisible without risk quantification. This is the concrete meaning of risk management "enabling intelligent risk-taking": it makes return-*per-risk* visible so capital flows to where it works hardest.

---

## Section C — Interview Style (model answers)

**C1. "In one minute, why does risk management matter?"**
"Finance makes money by taking risk, so the job is never to avoid it but to take the right risks knowingly. Risk management does three things. First, it protects capital and solvency — it ensures we hold enough buffer for unexpected losses and never bet more than that buffer can absorb, so a bad year is survivable, not fatal. Second, and the part people miss, it *enables* intelligent risk-taking: by putting every exposure in a common unit, it shows return-per-unit-of-risk, so we take more risk where we're paid for it and less where we're not — it's a profit-optimisation function, not the department of no. Third, it's a licence to operate: Basel, Solvency II, rating agencies and depositors all demand it. In short — price for the expected loss, hold capital for the unexpected loss, stress-test for the tail."

**C2. "Walk me through the difference between expected and unexpected loss and how each is managed."**
"Expected loss is the average I anticipate — for credit it's PD times LGD times EAD. It's a *cost*, not a risk: I price it into the spread and cover it with provisions, so it should never surprise me. Unexpected loss is the volatility *around* that average — the amount a bad year exceeds the mean. I can't price it away because I don't know when it hits, so I hold capital against it. That's the whole reason banks carry capital. Beyond capital sits the catastrophic tail, which I handle with stress tests and contingency plans. Confusing the two — treating the average as the risk — is exactly how firms end up under-capitalised."

**C3. "What is VaR, and what are its limitations?"**
"One-day 99% VaR of ₹X means on 99% of days losses stay at or below ₹X, and on about one day in a hundred we expect to lose more. Parametrically it's z times sigma times position value. Its limitations: it's a *threshold*, not a worst case — it says nothing about *how bad* the other 1% gets, so a firm can meet its VaR and still be wiped out in the tail. It also assumes a distribution (often normal) that understates fat tails, and it's not sub-additive in general, so it can mis-reward concentration. That's why we complement it with Expected Shortfall — the average loss *given* VaR is breached — and with stress testing. And a VaR number is meaningless without its confidence level and horizon."

**C4. "Explain the three lines of defence and why the CRO reports to the board."**
"The first line is the business — traders, lending officers — who *take* and therefore *own* the risk, managing it within limits day to day. The second line is independent risk and compliance: it sets the framework, methodologies and limits, aggregates and monitors risk firm-wide, and *challenges* the first line. The third line is internal audit, giving the board objective assurance that the first two actually work. Independence rises as you move away from the money. The CRO heads the second line and typically reports to the board risk committee, not only the CEO, so that the person challenging risk-taking can't be overruled by the person whose bonus depends on taking it. That independence is the whole point — Barings failed because one person ran both trading and settlement."

**C5. "A profitable business line has a RAROC below the firm's hurdle rate. What do you do?"**
"Accounting profit and value creation aren't the same thing. If RAROC — profit net of expected loss over economic capital — is below the cost of equity, the line is *destroying* shareholder value even though it shows a profit, because the capital tied up would earn more elsewhere. I'd first check the inputs: is economic capital right, is expected loss stale, is there a pricing or cost problem I can fix to lift the numerator? If it can be re-priced or made more capital-efficient, do that. If not, it's a candidate for shrinking or exiting and reallocating that capital to higher-RAROC uses. The discipline here is that we allocate capital on return-per-risk, not on absolute profit."

---

## Section D — MCQs (with reasoning)

**D1. Expected loss on a loan is best described as:**
A) A risk to be hedged  B) A cost to be priced in and provisioned  C) The 99th-percentile loss  D) Capital held against volatility
**Answer: B.** EL is the *average* anticipated loss — a cost baked into spreads and covered by provisions. It is not the risk (that's unexpected loss, C/D describe the tail and capital), and it isn't hedged away (A).

**D2. Under the Knightian distinction, a genuinely novel, first-of-its-kind shock with no historical data is best handled by:**
A) Parametric VaR  B) A fabricated PD plugged into a model  C) Stress testing, buffers and judgment  D) Insurance
**Answer: C.** This is *uncertainty*, not risk — the distribution is unknowable, so models (A) and priced probabilities (B) don't apply, and it is generally uninsurable (D). Buffers, scenarios and judgment are the tools.

**D3. Which ordering of the appetite hierarchy is correct?**
A) Capacity ≤ Appetite ≤ Tolerance ≤ Limit ≤ Exposure
B) Exposure ≤ Limit ≤ Tolerance ≤ Appetite < Capacity
C) Appetite ≤ Capacity ≤ Tolerance ≤ Exposure ≤ Limit
D) Limit ≤ Exposure ≤ Tolerance ≤ Capacity ≤ Appetite
**Answer: B.** Actual exposure nests inside enforceable limits, inside per-risk tolerance, inside board appetite, which must sit strictly below the maximum survivable capacity.

**D4. A 1-day 99% VaR of ₹5 crore means:**
A) The maximum the firm can ever lose in a day is ₹5 crore
B) On ~1 day in 100, losses are expected to exceed ₹5 crore
C) The firm loses ₹5 crore every 100 days
D) Average daily loss is ₹5 crore
**Answer: B.** VaR is a threshold breached with 1% probability; it is explicitly *not* a worst case (A), not a certainty (C), and not the mean (D).

**D5. If 1-day 99% VaR is ₹40 lakh, the 4-day 99% VaR under the square-root-of-time rule is:**
A) ₹40 lakh  B) ₹80 lakh  C) ₹160 lakh  D) ₹10 lakh
**Answer: B.** VaR(T) = VaR(1) × √T = 40 × √4 = 40 × 2 = ₹80 lakh.

**D6. Under the three lines of defence, who OWNS the risk a trading desk creates?**
A) Internal audit  B) The risk management function  C) The trading desk itself (first line)  D) The regulator
**Answer: C.** The business that takes the risk owns it. The second line (B) challenges, the third line (A) assures, and the regulator (D) supervises from outside.

**D7. Which is NOT one of the four risk treatments?**
A) Accept  B) Avoid  C) Amplify  D) Transfer
**Answer: C.** The 4 T's are Accept (tolerate), Avoid (terminate), Reduce (treat), and Transfer (share). "Amplify" is not a treatment.

**D8. A desk earns more absolute profit than another but has a lower RAROC. The correct interpretation is:**
A) It is unambiguously the better desk  B) It generates less return per unit of risk-capital  C) RAROC is irrelevant to capital allocation  D) It must be loss-making
**Answer: B.** RAROC measures return per unit of economic capital; a lower RAROC means capital works less hard there, even if absolute profit is higher — which is precisely why capital allocation follows RAROC, not raw profit.

---

*End of Q&A bank. Formulas to reproduce cold: EL = PD × LGD × EAD (LGD = 1 − recovery); VaR = z × σ × V (z₉₅ = 1.645, z₉₉ = 2.326); VaR(T) = VaR(1) × √T; RAROC = (Revenue − Costs − EL) / Economic Capital.*
