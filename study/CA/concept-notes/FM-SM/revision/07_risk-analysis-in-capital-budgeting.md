# Risk Analysis in Capital Budgeting

## Snapshot
A single-point NPV is a conditional statement ("if inputs hold, value is created") — it says nothing about likelihood, spread, or which assumption is fragile. Two honest responses to risk:
- **Charge for risk** (change the accept/reject rule): RADR, Certainty Equivalent.
- **Describe the spread** (understand outcomes): sensitivity, scenario, expected NPV + σ + CV, decision trees, simulation.

These are not rivals — a full appraisal does both. The question's data structure chooses the rung for you.

## Core concepts
- **Risk vs Uncertainty (Knight):** Risk = probabilities knowable (dice); Uncertainty = probabilities not reliably attachable. Sensitivity/scenario need no probabilities; expected NPV/simulation require them.
- **Probability sources:** objective (historical frequency), subjective (judgement), blend. The moment a question gives a probability, it has moved you into "risk" → full quantitative toolkit available.
- **Diversifiable vs non-diversifiable:** unsystematic/unique (machine breakdown, fire) diversifies away; systematic/market (GDP, interest, inflation) does not. Under CAPM a diversified owner is rewarded only for systematic risk. σ = total risk; β = systematic only.

## Key provisions / rules

| Concept | Formula |
|---|---|
| RADR | RADR = R_f + Risk premium; NPV = Σ CFₜ ÷ (1+RADR)ᵗ − CF₀ |
| Certainty Equivalent | NPV = Σ (αₜ × CFₜ) ÷ (1+R_f)ᵗ − CF₀ |
| CE coefficient | αₜ = Certain CF ÷ Expected risky CF (0 ≤ α ≤ 1) |
| CE–RADR reconciliation | αₜ = (1+R_f)ᵗ ÷ (1+RADR)ᵗ |
| RADR from α (year t) | RADRₜ = (1+R_f) ÷ αₜ^(1/t) − 1 |
| Expected cash flow | C̄F = Σ pᵢ × CFᵢ |
| Expected NPV | Σ C̄Fₜ ÷ (1+r)ᵗ − CF₀ |
| Standard deviation | σ = √[ Σ pᵢ (CFᵢ − C̄F)² ] |
| Coefficient of variation | CV = σ ÷ Expected value |
| σ of NPV (independent) | √[ Σ σₜ² ÷ (1+r)²ᵗ ] |
| σ of NPV (perfectly correlated) | Σ σₜ ÷ (1+r)ᵗ |
| Sensitivity margin (%) | NPV ÷ PV of the variable × 100 |
| Joint prob (tree terminal node) | product of branch probabilities along the path |

**RADR:** higher risk → higher premium → higher hurdle → lower NPV. Adjust *around* WACC (riskier project above WACC, safer below). Premium sources: managerial judgement, risk-class buckets, or CAPM [R_f + β(R_m − R_f)]. **Flaw:** forces risk to compound at a constant rate every year — over-penalises long/back-loaded projects. WACC-for-everything trap: over-accepts risky, wrongly rejects safe projects.

**CE:** separates time value (discount at R_f) from risk (αₜ in numerator, per year). Theoretically superior (each year its own α). **Lower α = more risk.** RADR *implicitly* assumes α falls with t (reconciliation formula). A **rising α** (risk falling over time — start-up) cannot be reproduced by any positive constant RADR → CE only honest tool. Constant RADR matches stated α's only if they decline in the exact geometric pattern.

| Feature | RADR | CE |
|---|---|---|
| What is adjusted | Discount rate (denominator) | Cash flows (numerator) |
| Rate used | Risk-free + premium | Risk-free only |
| Risk each year | Grows at compound rate | Set independently per year |
| Ease | Easy, board-friendly | Harder, subjective |
| Soundness | Weaker (mixes risk & time) | Stronger (separates) |

**Sensitivity analysis:** flex one input ±X%, hold rest constant; biggest NPV swing / thinnest break-even margin = most critical (guard it). Needs no probabilities. Denominator of margin = **whole-life PV of that variable's stream** (not one year's figure). Limits: moves variables in isolation (unrealistic — recession moves all together); tells what is sensitive, not how likely.

**Scenario analysis:** internally consistent whole states (pessimistic / most likely / optimistic), every variable set together — captures correlation. Attach probabilities → becomes a coarse 3-point expected NPV.

**Expected NPV, σ, CV:** σ = absolute risk in ₹ (same units as CF, being √variance). **CV = risk per rupee of return** — correct comparator when sizes/means differ; lower CV better. σ ranks only when means equal. CV meaningless if mean near zero/negative — often compute CV on expected *cash flow* (safely positive); state base. **Independent** cash flows → variances add (discount factor squared); **perfectly correlated** → std devs add (plain factor). Correlated gives larger σ (no year-to-year cancelling).

**Decision trees:** decision nodes (squares, you choose), chance nodes (circles, nature decides). **Fold back right→left:** expected value at chance nodes, **maximum** at decision nodes. Replace a negative continuation branch with **₹0 (abandon)**. Multiply conditional probabilities along the branch (joint prob); terminal joint probs sum to 1. Discount future flows to PV before folding if raw flows + rate given. Captures value of flexibility (seed of real options).

**Simulation (Monte Carlo, Hertz 1964):** assign a probability distribution to each input, sample repeatedly (draw → compute NPV → repeat thousands), plot NPV distribution. Gives mean, σ, and **P(NPV < 0)**. Handles many correlated variables. Data-hungry, model-dependent; does not itself make the decision.

## Worked mini-example
CE vs RADR. Outlay ₹6,00,000; CF ₹3,00,000/yr for 3 yrs; α = 0.90, 0.80, 0.70; R_f = 6%, RADR = 12%.
- **CE:** certain CFs 2,70,000 / 2,40,000 / 2,10,000 × PVF@6% (0.9434/0.8900/0.8396) = 2,54,718 + 2,13,600 + 1,76,316 = 6,44,634. NPV = **₹44,634**.
- **RADR:** 3,00,000 × PVF@12% (0.8929/0.7972/0.7118) = 7,20,570. NPV = **₹1,20,570**.
- **Why differ:** RADR-implied α = (1.06/1.12)ᵗ = 0.946 / 0.896 / 0.848 — gentler than management's stated 0.90/0.80/0.70. Management more cautious than 12% reflects → lower CE NPV. Methods reconcile only when stated α = RADR-implied α.

## Exam traps & must-remember
1. **σ vs CV:** equal means → rank by σ; different means/sizes → must use CV.
2. **Wrong σ_NPV formula:** "independent" → √(Σ σₜ²/(1+r)²ᵗ) (square the factor); "perfectly correlated" → Σ σₜ/(1+r)ᵗ (plain). ~73% gap.
3. **CE discount rate = risk-free**, never RADR (double-counts risk).
4. **RADR direction:** higher risk → higher rate → lower NPV. Premium is *added*.
5. **α direction:** lower α = more risk; rising α impossible under any positive constant RADR.
6. Sensitivity finds the **most dangerous to mis-estimate**, not "the good" variable.
7. **Tree fold-back right→left:** expected value at circles, **maximum** at squares (you control decisions — don't average).
8. Negative continuation branch → replace with **₹0 (walk away)**, not the negative number.
9. Probabilities sum to 1; joint prob of terminal node = product along path.
10. Expected NPV may be a value that never actually occurs — it's a long-run average.
11. **Salvage under RADR** is discounted at the RADR (only CE discounts anything at R_f).
12. Sensitivity margin denominator = whole-life PV of the variable's stream.
13. σ is in rupees (√variance); variance is ₹² — don't quote it as "the risk."
14. WACC-for-everything ignores that riskier projects need a higher hurdle.

## One-line recall
- RADR punishes the rate; CE punishes the cash flow. Only CE discounts at the risk-free rate.
- σ is risk in rupees; CV is risk per rupee. Equal means → σ; different means → CV.
- Independent years cancel (variances add, factor squared); correlated years compound (σ's add).
- Lower α = more risk; a rising α needs CE (no constant RADR can make it).
- Tree: fold back right→left, max at squares, expected at circles, ₹0 for abandon.
- Simulation = scenario analysis with scenarios turned up to infinity; gives P(NPV < 0).
