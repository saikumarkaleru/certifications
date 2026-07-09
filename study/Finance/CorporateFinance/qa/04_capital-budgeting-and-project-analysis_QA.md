# Q&A — Capital Budgeting & Project Analysis

A mixed bank of theory and numerical questions. Theory answers include a model answer plus a crisp "how to say it in an interview" line. Numericals are fully worked and self-verified.

---

## Theory

### Q1. What is the single principle that governs which cash flows belong in a capital budgeting analysis?

**Model answer.** The **incremental / with-vs-without principle**: include exactly those cash flows that differ between the world in which the firm undertakes the project and the world in which it does not. A cash flow that occurs either way is irrelevant. This one rule generates all the special cases — sunk costs (occur either way → exclude), opportunity costs (a resource is diverted from another use → include), cannibalization (existing profits fall because of the project → include as a cost), and side-benefits/spillovers (other products gain → include).

**How to say it:** "I ask one question of every line item — does this cash flow change because we said yes? If not, it's out. Incrementality, with-vs-without, is the whole game."

---

### Q2. Why do we use cash flows rather than accounting profit, and after tax rather than pre-tax?

**Model answer.** Shareholders can only spend cash, not earnings. Accounting profit spreads costs over time (depreciation), recognizes revenue before cash arrives (receivables), and generally breaks the timing between profit and cash — so it is the wrong measure of *when* value is delivered. Capital budgeting undoes accrual accounting to find the actual timing of cash. After-tax because tax is a real outflow to the government, and because non-cash items like depreciation still affect cash *through* the tax they shelter. Pre-tax analysis systematically overstates value.

**How to say it:** "Profit is an opinion, cash is a fact, and the taxman takes a real cut — so I model incremental after-tax cash, timed to when it actually moves."

---

### Q3. Explain the depreciation tax shield. If depreciation isn't cash, why does it affect NPV?

**Model answer.** Depreciation is a non-cash expense, so to convert accounting profit to cash we add it back. But depreciation is **tax-deductible** — it lowers taxable income, so it reduces the tax bill by `Depreciation × tax rate`. That tax saving is a genuine cash inflow. So depreciation affects value only through this shield. Two consequences: (i) accelerated depreciation is valuable because it pulls the shield forward in time (higher PV); (ii) the shield exists only if the firm has taxable profits to shelter.

**How to say it:** "Depreciation isn't cash, but it's a tax deduction — so it saves `dep × tax rate` in cash. That shield is the only way depreciation touches NPV."

---

### Q4. Distinguish sunk cost, opportunity cost, and how each is treated.

**Model answer.** A **sunk cost** is already incurred and unrecoverable — it does not change with the decision, so it is **excluded** (e.g., R&D or a feasibility study already paid for). An **opportunity cost** is the value of the best alternative use of a resource the project consumes — even a resource the firm already owns — and it is **included** at market value, after tax (e.g., renting out or selling an owned building instead of using it). The trap connecting them: a historical cost that is partly recoverable is not fully sunk; the recoverable portion is an opportunity cost of continuing.

**How to say it:** "Sunk costs are backward-looking and out; opportunity costs are the forward value you give up and are in — at market, after tax, never book."

---

### Q5. What is cannibalization, and when should you NOT deduct cannibalized sales?

**Model answer.** Cannibalization (erosion) is when a new product steals sales from the firm's existing products. Because we evaluate incrementally, the lost **contribution margin** on those existing sales is a real cost of the new product and is subtracted. The exception: only deduct sales the firm would *realistically have retained.* If those customers were going to defect to a competitor's new product anyway, the sales were leaving regardless — they are not incremental to *your* launch decision, so deducting them would wrongly penalize the project.

**How to say it:** "Subtract the lost margin on existing sales the new product steals — but only sales we'd otherwise have kept. Sales a rival would've taken anyway aren't incremental."

---

### Q6. How is working capital handled, and what's the most commonly forgotten piece?

**Model answer.** Growth ties up cash in net working capital (inventory + receivables − payables). An **increase** in NWC is a cash outflow, a **decrease** is an inflow. NWC is typically funded at the start of the period it supports (often modeled at year 0 and incrementally thereafter). The most-forgotten piece is the **terminal recovery**: at project end, inventory is run down and receivables collected, so the entire NWC is added back as a final inflow. Forgetting it understates NPV.

**How to say it:** "Fund working capital up front as sales ramp, invest only the incremental change each year, and — the bit people forget — recover the whole balance at the end."

---

### Q7. What discount rate should you use, and why is the financing source irrelevant?

**Model answer.** Use the **opportunity cost of capital for the project's own risk** — the return investors could earn on an equally risky alternative. If the project has firm-average risk, the firm's WACC is a fair proxy; if it's riskier or safer, adjust. The financing source is irrelevant because every project draws on the firm's whole capital pool and because the cost of capital compensates investors for *risk*, not for how a particular deal happened to be funded. Funding a risky project with cheap debt does not make it safe. (The debt tax shield is already captured in WACC's after-tax cost of debt, so cash flows stay unlevered.)

**How to say it:** "The rate follows the *use* of the money, not the *source*. Project risk sets the hurdle — WACC only if the project is average-risk, adjusted otherwise."

---

### Q8. NPV vs IRR — when can IRR mislead?

**Model answer.** NPV is the correct rule: it's in currency, additive, and always maximizes wealth. IRR misleads in four ways: (1) **multiple or no IRR** when cash flows change sign more than once; (2) the **reinvestment assumption** that interim cash flows earn the IRR (usually too optimistic); (3) **scale blindness** — a 100% return on ₹1 lakh beats a 20% return on ₹1 crore by IRR but not by wealth; (4) **mutually exclusive ranking conflicts** with NPV. Use MIRR or, better, just use NPV to decide.

**How to say it:** "NPV to decide, IRR to communicate. IRR can multiply, assume rich reinvestment, and ignore scale — so on mutually exclusive projects I trust NPV."

---

### Q9. Explain equivalent annual cost and when you must use it.

**Model answer.** EAC converts a project's whole-life cost (the PV of its costs) into a constant annual amount with the same present value: `EAC = PV of costs / annuity factor(r, n)`. You must use it when comparing **mutually exclusive projects with different lives** (or deciding **replacement timing**), because a raw NPV comparison is apples-to-oranges — the shorter-lived asset gets replaced sooner. Compare per-year EACs and choose the lowest. It assumes indefinite replacement with an identical asset, which should be flagged if technology or need will change.

**How to say it:** "Different lives break raw NPV comparison. EAC levels each project into a per-year cost assuming replace-forever, and you pick the lowest — perfect for equipment choice and replacement timing."

---

### Q10. Distinguish sensitivity, scenario, and break-even analysis.

**Model answer.** **Sensitivity** flexes one input at a time to see which driver NPV is most sensitive to — it ranks the variables (tornado chart) but ignores correlation and probability. **Scenario** flexes several correlated inputs together into consistent stories (base/best/worst), capturing that in a downturn volume, price, and margin fall together — giving realistic downside and, with probabilities, an expected NPV. **Break-even** finds the input value at which NPV = 0, giving the margin of safety. Sensitivity says *where the risk is*; scenario says *how bad it can get*; break-even says *how much room you have.*

**How to say it:** "Sensitivity finds the key driver one variable at a time; scenario bundles correlated variables for a realistic downside; break-even tells me how far a variable can move before value disappears."

---

### Q11. What's the difference between accounting break-even and NPV break-even, and which is higher?

**Model answer.** **Accounting break-even** is the sales level at which operating profit — including depreciation — equals zero: `Q = (Fixed cash costs + Depreciation) / (Price − Variable cost)`. **NPV (financial) break-even** is the sales level at which NPV = 0, i.e., the project also earns the cost of capital on the invested funds. NPV break-even is **higher**, because clearing accounting break-even only recovers cost and depreciation; it does not compensate investors for the time value and risk of their capital. A project can be accounting-profitable yet value-destructive.

**How to say it:** "Accounting break-even zeroes book profit; NPV break-even also earns the cost of capital — so it's the higher, value-relevant bar. Above accounting BE but below NPV BE still destroys value."

---

### Q12. Why prefer NPV over payback, and does payback ever have a legitimate use?

**Model answer.** Payback ignores all cash flows after the cutoff and (in simple form) the time value of money, so it can reject high-NPV long-dated projects and accept poor short ones — it's not a value measure. But it has legitimate secondary uses: as a quick **liquidity/risk screen** (how long is capital exposed), which matters for credit analysis and for firms that are cash-constrained or operating in fast-changing/high-uncertainty environments where distant cash flows are barely forecastable.

**How to say it:** "Payback isn't a value rule — it's blind to everything past the cutoff. I use it only as a liquidity and risk screen alongside NPV, never to decide."

---

## Numerical

### Q13. After-tax salvage value.

Equipment cost ₹80 lakh, depreciated straight-line to zero over 8 years. It is sold at the end of **year 5** for ₹40 lakh. Tax rate 30%. What is the after-tax salvage cash flow?

**Solution.**
- Accumulated depreciation over 5 years = (80/8) × 5 = 10 × 5 = 50. **Book value = 80 − 50 = 30.**
- Gain on sale = 40 − 30 = 10. Tax on gain = 10 × 0.30 = 3.
- After-tax salvage = 40 − 3 = **₹37 lakh.**

*Check with formula:* `Sale − t(Sale − Book)` = 40 − 0.30(40 − 30) = 40 − 3 = 37. ✓

---

### Q14. Incremental free cash flow for one year.

A project adds ₹200 lakh revenue and ₹120 lakh cash operating costs, has ₹30 lakh depreciation, requires a ₹15 lakh increase in NWC this year, and no CapEx this year. Tax rate 25%. Incremental FCF?

**Solution.**
- EBIT = 200 − 120 − 30 = 50. Tax = 50 × 0.25 = 12.5. NOPAT = 37.5.
- Add back depreciation: 37.5 + 30 = 67.5.
- Less ΔNWC: 67.5 − 15 = **₹52.5 lakh.**

*Check via tax-shield form:* (200−120)(1−0.25) + 30×0.25 − 15 = 80×0.75 + 7.5 − 15 = 60 + 7.5 − 15 = 52.5. ✓

---

### Q15. Full NPV with opportunity cost and sunk cost.

A firm considers a 3-year project. CapEx ₹150 lakh (straight-line to zero over 3 years). Revenue ₹180 lakh/yr, cash costs ₹90 lakh/yr. It will use an owned machine that could otherwise be **rented out for ₹12 lakh/yr** (opportunity cost). A ₹20 lakh feasibility study is already done. Salvage 0. No working capital. Tax 25%, discount rate 10%. NPV?

**Solution.**
- ₹20 lakh study = sunk → exclude. Rent forgone ₹12 lakh/yr = opportunity cost → include.
- Depreciation = 150/3 = 50/yr.
- Pre-dep operating profit = 180 − 90 − 12 (opportunity) = 78.
- FCF (tax-shield form) = 78×(1−0.25) + 50×0.25 = 58.5 + 12.5 = **71/yr.**
- Annuity factor A(10%,3) = [1 − 1.1^−3]/0.10 = (1 − 0.7513)/0.10 = 2.4869.
- PV inflows = 71 × 2.4869 = 176.57. **NPV = 176.57 − 150 = ₹26.57 lakh > 0 → accept.**

*Check:* year-by-year DFs 0.9091, 0.8264, 0.7513 → 71×(0.9091+0.8264+0.7513)=71×2.4868=176.56. ✓

---

### Q16. Equivalent annual cost, different lives.

Machine X: cost ₹60 lakh, life 4 years, running cost ₹18 lakh/yr. Machine Y: cost ₹100 lakh, life 6 years, running cost ₹12 lakh/yr. Discount rate 12%, ignore tax. Which is cheaper on an EAC basis?

**Solution.**
- A(12%,4) = [1 − 1.12^−4]/0.12 = (1 − 0.6355)/0.12 = 3.0373.
- A(12%,6) = [1 − 1.12^−6]/0.12 = (1 − 0.5066)/0.12 = 4.1114.

**Machine X:** PV costs = 60 + 18×3.0373 = 60 + 54.67 = 114.67. EAC = 114.67/3.0373 = **₹37.76 lakh/yr.** (Or 60/3.0373 + 18 = 19.76 + 18 = 37.76 ✓)

**Machine Y:** PV costs = 100 + 12×4.1114 = 100 + 49.34 = 149.34. EAC = 149.34/4.1114 = **₹36.32 lakh/yr.** (Or 100/4.1114 + 12 = 24.32 + 12 = 36.32 ✓)

**Decision:** Y's EAC (36.32) < X's (37.76) → **choose Machine Y.** Raw PV-of-costs comparison (114.67 vs 149.34) would wrongly favour X — that's the trap EAC fixes.

---

### Q17. NPV break-even volume.

A project sells at ₹800/unit, variable cost ₹500/unit, fixed cash costs ₹60 lakh/yr, over 5 years. CapEx ₹200 lakh (straight-line to zero over 5 yrs, no salvage, no NWC). Tax 25%, discount rate 10%. Find (a) accounting break-even units and (b) NPV break-even units.

**Solution.**
- Contribution/unit = 800 − 500 = ₹300. Depreciation = 200/5 = 40 lakh/yr.
- **(a) Accounting BE:** 300Q = fixed + dep = 60,00,000 + 40,00,000 = 1,00,00,000 → Q = 33,333 units.
- **(b) NPV BE:** A(10%,5) = (1 − 1.1^−5)/0.10 = (1 − 0.6209)/0.10 = 3.7908.
  Required annual FCF = 200,00,000 / 3.7908 = 52,76,459.
  FCF(Q) = (300Q − 60,00,000)(0.75) + 40,00,000×0.25 = 225Q − 45,00,000 + 10,00,000 = 225Q − 35,00,000.
  Set 225Q − 35,00,000 = 52,76,459 → 225Q = 87,76,459 → **Q ≈ 39,006 units.**

**Interpretation:** NPV break-even (~39,000) exceeds accounting break-even (~33,333) because NPV must also earn the 10% cost of capital on the ₹200 lakh. ✓

---

### Q18. Sensitivity — impact of a cost overrun.

Using Q17's base at Q = 50,000 units: base FCF = 225×50,000 − 35,00,000 = 1,12,50,000 − 35,00,000 = 77,50,000 → NPV = 77,50,000×3.7908 − 2,00,00,000 = 2,93,78,700 − 2,00,00,000 = **₹93.79 lakh.** Now variable cost rises 10% (₹500 → ₹550). New NPV?

**Solution.**
- New contribution/unit = 800 − 550 = 250. At 50,000 units contribution = 1,25,00,000.
- Pre-dep profit = 1,25,00,000 − 60,00,000 = 65,00,000.
- FCF = 65,00,000×0.75 + 40,00,000×0.25 = 48,75,000 + 10,00,000 = 58,75,000.
- NPV = 58,75,000 × 3.7908 − 2,00,00,000 = 2,22,71,850 − 2,00,00,000 = **₹22.72 lakh.**

**Interpretation:** a 10% variable-cost rise cut NPV from ₹93.8 lakh to ₹22.7 lakh — a ~76% drop. NPV is highly sensitive to variable cost (high operating leverage on margin), so procurement/cost control is the key risk to manage. ✓

---

### Q19. Scenario analysis with probabilities → expected NPV.

A project has three scenarios: Best NPV +₹300 lakh (prob 0.25), Base +₹120 lakh (prob 0.50), Worst −₹150 lakh (prob 0.25). Compute expected NPV and comment.

**Solution.**
- E[NPV] = 0.25×300 + 0.50×120 + 0.25×(−150) = 75 + 60 − 37.5 = **₹97.5 lakh.**
- Positive expected NPV → accept on an expected-value basis, but note a 25% chance of a ₹150 lakh loss. Whether that downside is bearable depends on the firm's risk capacity; a large possible loss relative to firm size might warrant staging the investment (a real-option/decision-tree approach) to cap the downside.

**How to say it:** "Expected NPV is positive at ₹97.5 lakh, but there's a one-in-four chance of losing ₹150 lakh — I'd size or stage the project so that tail is survivable." ✓

---

### Q20. WACC as the discount rate.

A firm is 40% debt, 60% equity (market values). Cost of equity 15%, pre-tax cost of debt 9%, tax 30%. A proposed project has firm-average risk. What hurdle rate, and what if the project were materially riskier?

**Solution.**
- After-tax cost of debt = 9% × (1 − 0.30) = 6.3%.
- WACC = 0.60×15% + 0.40×6.3% = 9.0% + 2.52% = **11.52%.**
- For a firm-average-risk project, discount at ~11.52%. If the project is materially **riskier** than the firm's typical business, WACC understates the required return — use a **higher, project-specific rate** (e.g., via a comparable "pure-play" beta), otherwise you'll accept value-destroying projects. Financing mix of *this* deal doesn't change the answer.

**How to say it:** "11.5% WACC works only because the project is average-risk. Off-risk projects need their own rate — I'd lever a pure-play comparable's beta, not just use the firm WACC." ✓

---

### Q21. Cannibalization adjustment.

A firm launches Product B expected to earn ₹90 lakh/yr contribution. But B will cannibalize Product A: ₹40 lakh/yr of A's sales shift to B, and A's contribution margin is 45%. Of that ₹40 lakh, the firm judges ₹15 lakh would have been lost to a competitor anyway. What incremental annual contribution should enter B's NPV?

**Solution.**
- Cannibalized A sales that were genuinely retainable = 40 − 15 = ₹25 lakh (the ₹15 lakh was leaving regardless).
- Lost A contribution = 25 × 45% = ₹11.25 lakh.
- Incremental contribution from B = 90 − 11.25 = **₹78.75 lakh/yr.**

**Interpretation:** naively deducting the full ₹40 lakh of sales (×45% = ₹18 lakh) would understate B by ₹6.75 lakh/yr — you must strip out sales the competitor would have taken anyway. ✓

---

### Q22. Replacement decision using EAC (real-world framing).

An old truck can be kept for 2 more years with running cost ₹9 lakh/yr, then scrapped for ₹0; keeping it forgoes selling it today for ₹5 lakh. A new truck costs ₹40 lakh, lasts 8 years, running cost ₹4 lakh/yr, no salvage. Discount rate 10%, ignore tax. On EAC logic, is the new truck justified now?

**Solution.**
- **New truck EAC:** A(10%,8) = (1 − 1.1^−8)/0.10 = (1 − 0.4665)/0.10 = 5.3349.
  PV costs = 40 + 4×5.3349 = 40 + 21.34 = 61.34. EAC = 61.34/5.3349 = **₹11.50 lakh/yr.**
- **Keeping the old truck (next 2 years):** the relevant cost includes the ₹5 lakh opportunity cost of not selling now, plus ₹9 lakh/yr running.
  PV of keeping = 5 (forgone sale, today) + 9×A(10%,2). A(10%,2) = (1 − 1.1^−2)/0.10 = (1 − 0.8264)/0.10 = 1.7355.
  PV = 5 + 9×1.7355 = 5 + 15.62 = 20.62 over 2 years. EAC = 20.62/1.7355 = **₹11.88 lakh/yr.**

**Decision:** old-truck EAC (₹11.88 lakh/yr) > new-truck EAC (₹11.50 lakh/yr) → **replace now.** The new truck's lower running cost, spread over 8 years, beats nursing the old one even after accounting for the ₹5 lakh opportunity cost. Note how close it is — small changes in running cost or the sale value would flip it, so this is a natural sensitivity candidate. ✓

---

*End of Q&A bank — 22 questions (12 theory, 10 numerical), all figures self-verified.*
