# Q&A — LBO Modeling — Structure and Mechanics

A practice bank for Chapter 30. Work each problem before reading the answer. All dollar figures are in millions (\$m) unless noted. Excel-reproducible steps are given for Section B.

---

## Section A — Concept-Check

**A1. In one sentence, what is an LBO?**

The purchase of a company using a large amount of borrowed money (debt) and a relatively small amount of the buyer's own equity, where the acquired company's own cash flows and assets service and repay that debt.

**A2. Name the three engines that generate the equity return in an LBO. Which is the least reliable and why?**

(1) Debt paydown (de-leveraging) — free cash flow converts lenders' claims into owner's equity. (2) EBITDA growth — a bigger business is worth more at the same multiple. (3) Multiple expansion — selling at a higher EV/EBITDA multiple than you paid. Multiple expansion is least reliable because it is a market-driven bet outside the sponsor's control; sponsors underwrite to a flat multiple and treat any expansion as upside.

**A3. Why does leverage amplify equity returns?**

Lenders hold a fixed, capped claim (principal plus interest). Equity is the residual — it gets everything left over. When the fixed claim is large relative to a small equity base, any change in enterprise value lands almost entirely on that small base, so a modest percentage change in EV becomes a large percentage change in equity value. Debt is a return amplifier, not just cheap financing.

**A4. What is the "tax shield" and why does it matter in an LBO?**

Interest on debt is tax-deductible; dividends to equity are not. Every dollar of interest reduces taxable income, so at a 25% tax rate \$100 of interest costs the company only \$75 after tax — the government subsidizes part of the borrowing cost. With debt at 4–6x EBITDA, this shield materially lifts the free cash flow available to repay principal.

**A5. Why is cash flow stability the single most important trait of a good LBO target?**

Because leverage cuts both ways. Interest is a fixed bill that does not shrink when EBITDA falls; unstable cash flows can leave the company unable to cover interest, breaching covenants or defaulting. Predictable, recurring cash flows with low capex safely support high leverage; cyclical, capex-heavy businesses do not.

**A6. Define MOIC and IRR, and state the exact relationship for a simple two-date deal.**

MOIC (Multiple of Invested Capital / cash-on-cash) = Exit Equity Value ÷ Initial Equity Invested. IRR is the annualized compound return that sets the NPV of the equity cash flows to zero. For a single entry outflow and single exit inflow: IRR = MOIC^(1/years) − 1.

**A7. Why can two deals with the same MOIC have very different IRRs?**

Because IRR is time-sensitive and MOIC is not. A 2.0x MOIC earned in 3 years (≈26% IRR) beats a 2.5x earned in 7 years (≈14% IRR). Getting your money back faster compounds to a higher annualized return, so IRR must always be reported alongside MOIC.

**A8. Order the capital structure from safest to riskiest and state the consequence of that order.**

Revolver → Senior Term Loan (1st lien) → Subordinated / high-yield notes → Mezzanine → Sponsor equity. This is the waterfall: in liquidation senior lenders are made whole before subordinated lenders see a dollar, and equity gets only the residual. Higher seniority = lower risk = lower rate; equity is riskiest and demands the highest return.

**A9. What is the difference between cash interest and PIK interest?**

Cash interest is paid out in cash each period. PIK ("pay-in-kind") interest is not paid in cash — it accretes onto the principal balance, which then compounds. PIK preserves cash for senior debt paydown but grows the junior balance over time.

**A10. Why is sponsor equity called "the plug"?**

Because Total Sources must equal Total Uses. You compute Total Uses, size the debt tranches off leverage multiples, and the equity contribution is whatever amount is left over to make the two sides balance: Equity = Total Uses − Total Debt Sources. It should never be hard-coded.

---

## Section B — Build / Computational Problems

Each problem is reproducible in Excel. Formulas shown as they would be entered.

**B1. Entry EV and equity check — base case.**

Given: LTM EBITDA = \$100; Entry multiple = 10.0x; Senior 4.0x; Subordinated 2.0x; bought debt-free; fees = 0.

Steps:
1. Entry EV = `100 * 10.0` = **\$1,000**.
2. Senior debt = `4.0 * 100` = \$400; Subordinated = `2.0 * 100` = \$200; Total debt = **\$600**.
3. Total Uses = EV + fees = `1,000 + 0` = \$1,000.
4. Sponsor equity (plug) = `Total Uses − Total Debt` = `1,000 − 600` = **\$400**.
5. Entry leverage = `600 / 100` = **6.0x**.

Check: Total Sources = 400 + 200 + 400 = 1,000 = Total Uses. `1,000 − 1,000 = 0` ✓

**B2. Exit and returns — base case (flat multiple).**

Given B1, plus: 5-year hold; EBITDA grows \$100 → \$130; cumulative debt paydown = \$300 (net debt \$600 → \$300); exit at 10.0x flat.

Steps:
1. Exit EV = `130 * 10.0` = **\$1,300**.
2. Net debt at exit = `600 − 300` = \$300.
3. Exit equity value = `1,300 − 300` = **\$1,000**.
4. MOIC = `1,000 / 400` = **2.5x**.
5. IRR = `2.5^(1/5) − 1` = **20.1%**. Verify in Excel with `=IRR({-400,0,0,0,0,1000})` = 20.1%.

**B3. Three-engine attribution — reconcile the \$600 gain.**

Decompose the \$400 → \$1,000 equity gain (+\$600) from B2:

| Source | Calculation | Contribution |
|---|---|---|
| EBITDA growth | (130 − 100) × 10.0 | +\$300 |
| Multiple expansion | (10.0 − 10.0) × 130 | +\$0 |
| Debt paydown | 600 − 300 | +\$300 |
| **Total gain** | | **+\$600** |

Reconciliation: starting equity \$400 + \$600 gain = **\$1,000** exit equity ✓. Half the value came from paydown, half from growth, none from multiple expansion.

**B4. Flex the exit multiple to 11.0x.**

Given B2 but exit at 11.0x:
1. Exit EV = `130 * 11.0` = \$1,430.
2. Exit equity = `1,430 − 300` = **\$1,130**.
3. MOIC = `1,130 / 400` = **2.83x**.
4. IRR = `2.825^(1/5) − 1` = **23.1%**.

Cross-check via attribution: multiple contribution = (11.0 − 10.0) × 130 = +\$130; exit equity = 1,000 + 130 = \$1,130 ✓. One turn of multiple lifted IRR by ~3 points.

**B5. Add financing fees.**

Given B1's structure but fees = 2.5% of EV; debt still \$600; same exit (EV \$1,300, net debt \$300).
1. Fees = `0.025 * 1,000` = \$25.
2. Total Uses = `1,000 + 25` = \$1,025.
3. Equity = `1,025 − 600` = **\$425** (fees raise the equity check).
4. Exit equity = `1,300 − 300` = \$1,000.
5. MOIC = `1,000 / 425` = **2.35x**; IRR = `2.353^(0.2) − 1` = **18.7%**.

Lesson: fees are a real use of cash — omitting them flatters the IRR (20.1% → 18.7% here).

**B6. Leverage vs. all-equity (same operations).**

Same company, EBITDA \$100 → \$130, exit EV \$1,300, fees \$25.

*Levered (from B5):* Equity \$425; \$300 paydown; exit net debt \$300; exit equity \$1,000; MOIC 2.35x; **IRR 18.7%**.

*All-equity:* Debt = 0; Equity = Total Uses = \$1,025. No interest paid, so more cash builds — assume \$375 cumulative cash, exit net debt = −\$375 (net cash).
1. Exit equity = `1,300 + 375` = \$1,675.
2. MOIC = `1,675 / 1,025` = **1.63x**; IRR = `1.634^(0.2) − 1` = **10.3%**.

Punchline: same operating performance → 18.7% levered vs. 10.3% unlevered. Leverage nearly doubles the equity return because the value creation lands on a \$425 base instead of a \$1,025 base.

**B7. Full build-it-yourself (Chapter exercise).**

Given: LTM EBITDA = \$80; Entry multiple = 9.5x; debt-free; fees = 2.5% of EV; Senior 4.0x; Subordinated 1.5x; 5-year hold; EBITDA → \$105; cumulative paydown = \$180; exit (a) 9.5x, (b) 10.5x.

Entry:
1. Entry EV = `80 * 9.5` = **\$760**.
2. Total debt = `(4.0 + 1.5) * 80` = 5.5 × 80 = **\$440** (leverage 5.5x).
3. Fees = `0.025 * 760` = **\$19**.
4. Total Uses = `760 + 19` = \$779.
5. Equity plug = `779 − 440` = **\$339**.
6. S&U check: Sources 440 + 339 = 779 = Uses ✓.

Exit net debt = `440 − 180` = \$260 (both cases).

*Case (a), 9.5x:* Exit EV = `105 * 9.5` = \$997.5; exit equity = `997.5 − 260` = **\$737.5**; MOIC = `737.5 / 339` = **2.18x**; IRR = `2.176^(0.2) − 1` = **16.8%**.

*Case (b), 10.5x:* Exit EV = `105 * 10.5` = \$1,102.5; exit equity = `1,102.5 − 260` = **\$842.5**; MOIC = `842.5 / 339` = **2.49x**; IRR = `2.485^(0.2) − 1` = **20.0%**.

Attribution for (b): growth = (105 − 80) × 9.5 = \$237.5; multiple = (10.5 − 9.5) × 105 = \$105.0; paydown = \$180.0; total gain = **\$522.5**. Reconcile: equity net of fees. Note starting equity \$339 includes the \$19 of fees; the \$522.5 gain applies to the \$320 pre-fee enterprise-equity (760 − 440 = \$320). Check: 320 + 522.5 = \$842.5 exit equity ✓. (Fees are a one-time cash drag captured in the higher entry equity; the three engines act on the \$320 enterprise-equity base.)

**B8. Solve backward for the maximum entry multiple (valuation floor).**

A sponsor needs at least a 20% IRR over 5 years. Given EBITDA \$100 → \$130, exit at 10.0x flat, \$300 paydown, fees ignored. What is the highest entry EV (and multiple) the sponsor can pay?

1. Required MOIC for 20% over 5 yr = `1.20^5` = **2.488x**.
2. Exit equity is fixed = 1,300 − 300 = \$1,000.
3. Max entry equity = `1,000 / 2.488` = **\$402**.
4. With debt \$600, max Total Uses = `402 + 600` = \$1,002, so max EV ≈ \$1,002 → max entry multiple = `1,002 / 100` = **~10.0x**.

This is the sponsor's ceiling — a strategic buyer able to accept a lower return can generally outbid it, which is why LBO analysis sets a valuation floor.

---

## Section C — Interview-Style Questions (with model answers)

**C1. "Walk me through a basic LBO."**

"A sponsor buys a company using mostly debt and a small equity check. First I set entry assumptions — LTM EBITDA and an entry multiple give me Enterprise Value. I size the debt tranches as multiples of EBITDA and build Sources and Uses, where sponsor equity is the plug that makes sources equal uses. Over the hold, the company's free cash flow pays down debt while EBITDA grows. At exit I apply an exit multiple to exit-year EBITDA for a new EV, subtract remaining net debt to get exit equity, and compute MOIC = exit equity ÷ entry equity and IRR = MOIC^(1/years) − 1. Returns come from debt paydown, EBITDA growth, and any multiple expansion."

**C2. "What makes a company a good LBO candidate?"**

"Stable, predictable, recurring cash flows to safely service fixed interest; low capex so cash flow is free to pay down debt; a defensible market position; and ideally some operational upside or an under-levered balance sheet. Think subscription software or a distribution business. Cyclical or capital-hungry businesses are poor candidates because leverage amplifies their downside."

**C3. "All else equal, does using more debt always increase the IRR?"**

"More leverage increases IRR in the base case because it shrinks the equity base and magnifies the return on it — plus interest is tax-deductible. But it is not free: more debt means a larger fixed interest bill, less cash for paydown or growth, tighter covenants, and much higher default risk if EBITDA disappoints. There's a practical ceiling set by what lenders will provide and what the cash flows can safely cover. So more debt raises base-case IRR but also raises the probability of a zero."

**C4. "A sponsor pays 10x and exits at 10x with no EBITDA growth. Can they still make money?"**

"Yes — through debt paydown alone. Even with flat EBITDA and a flat multiple, enterprise value is unchanged but net debt has fallen because free cash flow repaid principal. A smaller slice of the same EV is owed to lenders, so a larger slice belongs to equity. That de-leveraging is the most reliable return engine and can produce a solid IRR by itself."

**C5. "Why do sponsors assume a flat exit multiple in the base case?"**

"Because multiple expansion is a market-driven bet they don't control. Underwriting a deal that only works if they sell at a higher multiple than they paid is speculation, not a plan. Assuming a flat — or even contracting — multiple forces the deal to work on paydown and operational improvement, which they can influence. Any expansion is then treated as upside, not as the thesis."

**C6. "What's the difference between how a DCF and an LBO value the same company?"**

"A DCF discounts unlevered free cash flow at WACC to get enterprise value — it's an intrinsic, capital-structure-neutral view. An LBO tracks the levered equity cash flows explicitly under a specific debt package and solves for the equity IRR given a purchase price. Same underlying cash flows, but the LBO asks 'what return will my equity earn at this price with this leverage?' rather than 'what is this business intrinsically worth?' The tax shield that lowers WACC in a DCF is the same shield that boosts LBO free cash flow."

**C7. "Your model shows a 25% IRR. What would make you distrust it?"**

"I'd check whether it leans on multiple expansion, whether financing fees and cash taxes are included, whether debt was sized off LTM rather than forward EBITDA, and whether the paydown and interest are internally consistent rather than hard-coded. Then I'd stress the downside — if a single soft year breaches a covenant or misses interest, the base-case IRR is meaningless. A high IRR that depends on optimistic and uncontrollable assumptions isn't a real 25%."

---

## Section D — Common-Error Spotting

For each, identify the error and give the correction.

**D1.** "Entry EV is \$1,000, so the sponsor's equity check is \$1,000 minus the \$600 of new debt = \$400. But there's also \$150 of existing target net debt we're refinancing, which I'll ignore since it's the seller's problem."

Error: Ignoring existing net debt. Existing debt must be refinanced at close — it's a use of cash. On a cash-free, debt-free deal you either bridge EV to equity purchase price (EV − existing net debt) for the seller's equity, and separately fund the refinancing of old debt in Uses. Omitting it understates Total Uses and the equity check. Always walk EV → less net debt → equity, and account for the refinancing.

**D2.** "Total Uses came to \$1,025 and my debt is \$600, so I'll just type \$425 into the equity cell to move on."

Error: Hard-coding the plug. Equity must be a formula: `= Total Uses − Total Debt Sources`. Hard-coding breaks the balance the moment any input changes and hides errors. Keep an explicit check cell `= Total Sources − Total Uses` conditionally formatted red when non-zero.

**D3.** "The company will grow EBITDA to \$130 by exit, and lenders will lend 4x senior, so senior debt = 4 × 130 = \$520 at close."

Error: Sizing debt off forward/exit EBITDA. Leverage is a multiple of LTM (or defined pro-forma) EBITDA at close, i.e. 4 × 100 = \$400. Using the \$130 forward number inflates debt by \$120 and correspondingly understates the equity check.

**D4.** "We assume the exit multiple rises from 10x to 12x — that's what gets us to a 25% IRR, so the deal works."

Error: Treating multiple expansion as the plan. If the deal only clears the target return via multiple expansion, it's too expensive. Base case must assume a flat (or conservative) multiple; expansion is upside only.

**D5.** "The mezzanine tranche has 12% PIK interest, so I'll subtract 12% × balance from free cash flow each year as a cash interest cost."

Error: Modeling PIK as a cash outflow. PIK interest does not leave the company — it accretes onto the debt balance, which then compounds. It should increase the mezz principal, not reduce cash flow. Modeling it as cash understates both free cash flow and the debt balance.

**D6.** "Deal X returns 3.0x over 8 years; Deal Y returns 2.0x over 3 years. X has the higher multiple, so X is the better deal."

Error: Judging MOIC without time. Convert to IRR: X = 3.0^(1/8) − 1 ≈ 14.7%; Y = 2.0^(1/3) − 1 ≈ 26.0%. Y compounds far faster and is the better deal. Always report IRR alongside MOIC.

**D7.** "Interest depends on the debt balance and the balance depends on cash flow after interest — that's circular, so I'll just hard-code interest at \$40 a year to avoid the loop."

Error: Dodging the interest circularity by hard-coding. The interest ↔ debt-balance ↔ cash-flow loop is genuine and central to the debt schedule; hard-coding interest makes paydown and returns wrong as soon as assumptions flex. Resolve it properly with Excel iterative calculation (File → Options → Formulas → Enable iterative calculation) or a circularity switch.

**D8.** "The base-case IRR is 22% and the business is a cyclical steelmaker levered at 6.5x, so it's a great deal."

Error: Over-levering an unstable, capex-heavy business and looking only at the base case. High leverage on cyclical cash flows is a default waiting to happen — one bad year can breach a covenant or miss interest even though the base case looks great. Stress the downside before signing off; a great base-case IRR that hides fragility is not a great deal.

---

*Self-verification: all IRRs recomputed as MOIC^(1/n) − 1 and cross-checked against the chapter's worked examples (B2 = 20.1%, B5 = 18.7%, B6 = 10.3%, B7a = 16.8%, B7b = 20.0%). Every S&U table balances to zero; every attribution reconciles to exit equity.*
