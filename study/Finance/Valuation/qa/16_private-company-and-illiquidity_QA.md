# Q&A — Private Company Valuation & Illiquidity

A mix of **theory** (with model answers and interview phrasing) and **fully solved numerical problems** (numbers self-verified and reconciling). Work the numericals with pen and paper before reading the solution.

---

## Section A — Theory & concept

### Q1. Why can't you value a private company exactly the way you value a public one?

**Model answer.** The *valuation framework* is identical — value is the present value of expected cash flows discounted at a risk-adjusted rate, or a multiple of earnings. What differs is the **information the market gives you for free**. For a public firm you observe the price, a regression beta, the float, and a market capital structure. For a private firm none of these exist, and reported earnings are distorted by owner-specific items. So private valuation adds three tasks: **build** the discount rate from public proxies, **normalize** the earnings, and **adjust** the answer for control and marketability.

**Interview line:** "Same DCF machinery — I just have to manufacture the inputs the market would otherwise hand me, and adjust for who's buying and how illiquid the stake is."

---

### Q2. Explain the "levels of value" and where public comps sit.

**Model answer.** Four levels, high to low: **strategic/synergistic value** (a specific buyer's synergies), **financial control value**, **marketable minority value**, and **non-marketable minority value**. You move *up* from minority to control by adding a **control premium**; you move *down* from marketable to non-marketable by subtracting a **DLOM**. Public-company trading multiples sit at the **marketable-minority** level — a listed share is liquid and represents a minority slice. That's the anchor: if you're valuing control, add a premium; if valuing a private minority, subtract DLOM.

**Interview line:** "Comps give me marketable-minority value. Everything else is an adjustment up for control or down for illiquidity."

---

### Q3. Why do we add a size premium and a company-specific premium on top of CAPM?

**Model answer.** CAPM prices only **systematic risk** and assumes the investor is **fully diversified**, so idiosyncratic risk is free. But the typical private-company owner — a founder or a concentrated PE/family holder — is *not* diversified, and small closely held firms have historically earned returns above raw CAPM (the size effect). The size premium captures that empirical excess; the company-specific premium captures key-person risk, customer concentration, thin financials, and limited access to capital. Together they patch the gap between CAPM's diversified-investor assumption and the concentrated reality of private ownership.

**Interview line:** "CAPM assumes diversification the private owner doesn't have — the premia are the price of concentration and small size."

---

### Q4. What is a bottom-up beta and why unlever then relever?

**Model answer.** A bottom-up beta is built from public comparables rather than a regression of the (non-existent) private stock. **Beta reflects business risk plus financial leverage.** Business/asset risk is shared across firms in the same industry, but leverage is firm-specific. So you **unlever** each comp's equity beta to isolate the pure asset beta, take the median, then **relever** at the *private firm's own* target capital structure. This transplants the shared business risk while respecting the target's own leverage.

**Formulas:** βu = βL / [1 + (1 − t)(D/E)]; βL = βu × [1 + (1 − t)(D/E)].

---

### Q5. What is the single most important normalization adjustment, and how is it done?

**Model answer.** **Owner (officer) compensation.** Founders set their own pay for tax reasons, so reported profit is not the business's true earning power. You restate comp to what a hired executive doing the same job would cost. Adjustment = **actual owner comp − arm's-length replacement comp**: if the owner overpays himself, add the excess back to EBITDA (earnings were understated); if he underpays, deduct the shortfall. After comp: personal expenses run through the business, above/below-market related-party rents, and one-off items.

---

### Q6. Distinguish the discount for lack of control from the discount for lack of marketability.

**Model answer.** **Lack of control (minority discount):** a minority holder can't set dividend policy, compensation, capital allocation, or force a sale — so a minority interest is worth less per share than a control interest. It's the mirror of the control premium: MD = 1 − 1/(1 + CP). **Lack of marketability (DLOM):** even a stake you fully control or that has clear economic value is worth less if you can't sell it quickly, cheaply, and at a certain price. They're *separable*: a stake can lack control, lack marketability, or both. Order of operations: adjust for control/minority **first**, then apply DLOM.

---

### Q7. Why is a control interest worth more per share than a minority interest?

**Model answer.** Because control is the **power to direct the cash flows** — set dividends, set compensation, decide capital allocation, lever up, and choose whether and when to sell. A controller can *unlock* value a minority holder is stuck watching. That extra optionality and command over cash flow is what the control premium pays for. Empirically, average control premiums in M&A run ~20–40% over pre-announcement (marketable-minority) prices.

---

### Q8. How do you think about the *magnitude* of a DLOM?

**Model answer.** Empirical anchors: restricted-stock studies imply ~10–35%; pre-IPO studies ~30–50%; a practitioner working range is **15–35%** for a typical private minority. Conceptually, DLOM ≈ the cost of a **protective put** guaranteeing you could sell at today's price over the expected holding period — so it rises with **volatility** and **expected holding period** and falls when a sale is more imminent or more certain. A *control* interest gets a smaller DLOM (5–15%) because the owner can force a sale.

---

### Q9. How does a VC value a pre-profit startup? Name the methods.

**Model answer.** Standard DCF fails (negative near-term cash flows, huge uncertainty). VCs use: **(1) VC method** — forecast an exit value in year 5 as exit multiple × exit metric, discount at a 30–60% target return to get post-money, back out ownership and adjust for dilution. **(2) First Chicago** — probability-weight success/sideways/failure scenarios. **(3) Scorecard/Berkus/comparable-round** — benchmark pre-revenue deals against typical valuations by stage and region. **(4) Real-options view** — staged financing is a series of call options with abandonment rights, which is why it beats committing all capital upfront.

---

### Q10. Give the pre-money / post-money identities.

**Model answer.** Post-money = Pre-money + New investment. Investor ownership % = Investment / Post-money. Founder retained % = Pre-money / Post-money. Example: ₹138cr pre + ₹20cr investment = ₹158cr post; investor owns 20/158 = 12.66%; founders keep 138/158 = 87.34%.

---

### Q11. Why can't you just multiply the whole-company equity value by your ownership percentage for a private minority stake?

**Model answer.** Because the whole-company value is typically a **control or marketable** value, while your slice is a **non-marketable minority**. A pro-rata share overstates what you'd actually get: you have no control to unlock value and you can't sell the stake without time, cost, and price uncertainty. You must step down the levels-of-value chart — stay at the minority level (no control premium) and then apply a DLOM.

---

### Q12. Where does key-person risk go in the model?

**Model answer.** Two legitimate homes: (a) raise the **company-specific risk premium** in the discount rate, or (b) apply an explicit **haircut to normalized earnings** to reflect the value that leaves with the founder. Pick one — don't do both for the same risk, or you double-count. If the founder holds the customer relationships or the technical IP in his head, a buyer may also structure an **earn-out** to bridge the gap rather than pay full value upfront.

---

## Section B — Numerical problems (fully solved)

### Q13. Unlever and relever a beta.

Comparable firm: levered beta 1.40, D/E = 0.80, tax 25%. Private target's target D/E = 0.30, tax 25%. Find the target's relevered beta.

**Solution.**

Unlever: βu = 1.40 / [1 + (1 − 0.25)(0.80)] = 1.40 / [1 + 0.60] = 1.40 / 1.60 = **0.875**.

Relever at target D/E 0.30: βL = 0.875 × [1 + (0.75)(0.30)] = 0.875 × [1 + 0.225] = 0.875 × 1.225 = **1.072**.

**Answer: relevered beta ≈ 1.07.**

---

### Q14. Cost of equity and WACC for a private firm.

Using the relevered beta 1.07 from Q13: Rf = 7%, ERP = 6%, size premium = 3%, company-specific premium = 1%. Target D/(D+E) = 23.08% (i.e., D/E 0.30). Pre-tax cost of debt 10%, tax 25%. Find Re and WACC.

**Solution.**

Re = 7% + 1.07 × 6% + 3% + 1% = 7% + 6.43% + 3% + 1% = **17.43%**.

Weights: D/E = 0.30 → E = 1, D = 0.30, D+E = 1.30. So E weight = 1/1.30 = 76.92%, D weight = 0.30/1.30 = 23.08%.

After-tax Rd = 10% × 0.75 = 7.5%.

WACC = 0.7692 × 17.43% + 0.2308 × 7.5% = 13.41% + 1.73% = **15.14%**.

**Answer: Re ≈ 17.4%, WACC ≈ 15.1%.**

---

### Q15. Normalize EBITDA.

Reported EBITDA ₹18cr. Founder's salary in P&L ₹4.0cr; market replacement ₹1.2cr. Rent to owner's trust ₹3.0cr; market rent ₹1.8cr. One-off insurance *gain* in EBITDA ₹0.7cr. Personal travel/cars in expenses ₹0.4cr. Compute normalized EBITDA.

**Solution.**

| Item | Adjustment |
|---|---|
| Reported EBITDA | 18.0 |
| Add back excess owner salary (4.0 − 1.2) | +2.8 |
| Add back above-market rent (3.0 − 1.8) | +1.2 |
| Remove one-off insurance **gain** | −0.7 |
| Add back personal expenses | +0.4 |
| **Normalized EBITDA** | **21.7** |

**Answer: ₹21.7 crore.** Note the insurance *gain* is subtracted (it inflated reported EBITDA); the personal expenses are added back (they depressed it).

---

### Q16. Control premium ↔ minority discount.

(a) A sector shows a 35% average control premium — what minority discount does it imply? (b) An appraiser uses a 20% minority discount — what control premium is that?

**Solution.**

(a) MD = 1 − 1/(1 + 0.35) = 1 − 1/1.35 = 1 − 0.7407 = **25.9%**.

(b) CP = 1/(1 − 0.20) − 1 = 1/0.80 − 1 = 1.25 − 1 = **25.0%**.

**Answer: (a) 25.9% minority discount; (b) 25.0% control premium.** They are reciprocals, not equal to the input.

---

### Q17. Non-marketable minority value from public comps.

Public comps: EV/EBITDA = 9.0×. Target normalized EBITDA ₹30cr; net debt ₹50cr. You hold **10%**, a passive minority. DLOM = 30%. Value your stake.

**Solution.**

EV = 9.0 × 30 = 270. Equity (marketable minority, 100%) = 270 − 50 = 220.

Your pro-rata marketable-minority value = 10% × 220 = 22.0 (no control premium — you're a minority).

Apply DLOM: 22.0 × (1 − 0.30) = **15.4**.

**Answer: ₹15.4 crore.**

---

### Q18. Control acquisition of a private firm.

Same firm as Q17 (marketable-minority equity = 220). A strategic buyer acquires **100% control**. Sector control premium 30%; control-level DLOM 10%. Value the acquisition (ignore unique synergies).

**Solution.**

Control value = 220 × (1 + 0.30) = 286.

Apply modest control-level DLOM: 286 × (1 − 0.10) = **257.4**.

**Answer: ₹257.4 crore.**

**Reconciliation with Q17:** the *same company* is worth ₹257.4cr to a 100% control buyer but the trapped 10% minority is worth only ₹15.4cr (vs a naïve pro-rata of 10% × 286 = 28.6cr control-basis, or 10% × 220 = 22cr minority-basis before DLOM). The spread is exactly the control and marketability discounts at work.

---

### Q19. Capitalized cash flow (single-stage) valuation.

Normalized FCFF next year ₹12cr; WACC 14%; long-run growth 4%; net debt ₹25cr; surplus non-operating land at fair value ₹8cr. Find equity value.

**Solution.**

EV = FCFF / (WACC − g) = 12 / (0.14 − 0.04) = 12 / 0.10 = 120.

Equity = EV − net debt + non-operating assets = 120 − 25 + 8 = **103.0**.

**Answer: equity value ₹103 crore.**

---

### Q20. VC method with dilution.

A VC invests ₹15cr in a startup. Year-5 exit forecast: net income ₹40cr at an exit P/E of 15×. Target return 45%/yr. Expected retention after future rounds = 75%. Find (a) post-money today, (b) ownership needed before dilution, (c) initial ownership grossed up for dilution, and (d) verify the money multiple.

**Solution.**

Exit equity value = 15 × 40 = 600.

(a) Post-money = 600 / (1.45)^5. (1.45)^5 = 1.45²=2.1025; ×1.45=3.0486; ×1.45=4.4205; ×1.45=6.4098. So post-money = 600 / 6.4098 = **93.6**.

(b) Ownership needed = 15 / 93.6 = **16.03%**.

(c) Grossed up for 75% retention = 16.03% / 0.75 = **21.37%**.

(d) Check: 21.37% initial diluted to 75% = 16.03% at exit → 16.03% × 600 = ₹96.2cr. Money multiple = 96.2 / 15 = **6.41×**, which equals (1.45)^5 = 6.41×. IRR target met — internally consistent.

**Answer:** post-money ≈ ₹93.6cr; ownership before dilution ≈ 16.0%; grossed-up initial stake ≈ 21.4%.

---

### Q21. First Chicago (scenario) valuation.

Three scenarios for a startup's equity value today (already discounted): Success ₹500cr @ 25% probability; Sideways ₹120cr @ 45%; Failure ₹0 @ 30%. Find the probability-weighted value and the VC's stake value for a 12% holding.

**Solution.**

Weighted value = 0.25 × 500 + 0.45 × 120 + 0.30 × 0 = 125 + 54 + 0 = **179.0**.

VC's 12% stake = 0.12 × 179 = **21.5**.

**Answer: expected equity value ₹179 crore; the 12% stake ≈ ₹21.5 crore.** The heavy failure weight is why the expected value sits far below the success case — the essence of the First Chicago method.

---

### Q22. Full mini-case: reported vs normalized valuation gap.

A founder-run firm reports EBITDA ₹20cr. Normalization adds back ₹5cr (excess comp ₹3cr + personal/one-offs ₹2cr) → normalized EBITDA ₹25cr. Comps trade at EV/EBITDA 8×. Net debt ₹30cr. The buyer takes 100% control; control premium 25%, control-level DLOM 8%. (a) What equity value does *reported* EBITDA imply on a marketable-minority basis? (b) What is the final control value on *normalized* EBITDA? (c) How much of the value gap is due to normalization alone?

**Solution.**

(a) Reported: EV = 8 × 20 = 160; equity = 160 − 30 = **130** (marketable minority).

(b) Normalized marketable-minority: EV = 8 × 25 = 200; equity = 200 − 30 = 170. Control value = 170 × 1.25 = 212.5; after 8% DLOM = 212.5 × 0.92 = **195.5**.

(c) Normalization's effect at the marketable-minority level = 170 − 130 = **₹40cr** (i.e., ₹5cr EBITDA × 8× multiple). Carried through the control premium and DLOM, the ₹5cr of add-backs is worth 40 × 1.25 × 0.92 = **₹46cr** of final value.

**Answer:** (a) ₹130cr; (b) ₹195.5cr; (c) normalization alone adds ₹40cr at the comp level (₹46cr after control/DLOM) — showing that on private deals, the *normalization* often moves the number more than the discount-rate debate. Get the earnings right first.

---

**Study tip.** In interviews, the private-company edge is *sequence discipline*: normalize earnings → build the discount rate from comps → value → bridge EV to equity → adjust for control → apply DLOM. State the sequence out loud and you'll never fumble the order-of-operations trap.
