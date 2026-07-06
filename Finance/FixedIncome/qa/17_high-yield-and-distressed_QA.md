# Q&A — High-Yield and Distressed Debt

## Section A — Concept Check

**A1. Where is the line between investment grade and high yield, and why does it matter so much?**

The line sits at BBB−/Baa3 (last IG notch) versus BB+/Ba1 (first HY notch). It matters far more than any other adjacent-notch boundary because of *institutional plumbing*: many insurers, pension funds, and index mandates are restricted by regulation or contract to investment-grade paper. When an issuer is downgraded across the line (a "fallen angel"), a whole class of natural buyers is forced to sell. That forced selling, layered on top of genuine credit deterioration, makes the yield jump across BBB−/BB+ much larger than the jump between any two IG notches.

**A2. Why can't you treat the promised yield as the expected yield in high yield?**

Because default is a base-rate event, not a tail event. Roughly 3–5% of HY issuers default in an average year and 10%+ in a bad one. The promised yield only materializes if the company survives; the *expected* return is a probability-weighted blend of "you get paid the coupon" and "you fight over the wreckage in bankruptcy." So expected return = promised yield minus expected credit loss, not the promised yield itself.

**A3. State the credit-triangle relationship and explain what it represents.**

`s_breakeven ≈ λ × (1 − RR)`, where λ is the annual default probability (hazard rate) and RR is the recovery rate. It is the *break-even* (fair) spread that exactly covers expected credit loss and delivers zero risk premium. Any two of {spread, default rate, recovery} pin down the third. The amount the *market* spread exceeds this break-even is the credit risk premium plus liquidity compensation you are actually being paid to harvest.

**A4. Decompose the credit spread into its components.**

`s ≈ Expected Loss + Credit Risk Premium + Liquidity Premium`, where Expected Loss = PD × LGD = λ × (1 − RR). Expected loss is the break-even floor; the risk premium compensates for the uncertainty and correlation (recession-clustering) of losses; the liquidity premium compensates for hard-to-trade paper. In HY, all three pieces are large and all move a lot.

**A5. Why are default losses only partly diversifiable?**

Diversification removes *idiosyncratic* (single-name) risk, so a large book's loss converges to the average default rate. But it does not remove *systematic* risk: defaults cluster in recessions, and recoveries fall at exactly the same time (PD and LGD are positively correlated). A well-diversified HY book still suffers large correlated losses in a downturn — and that residual systematic risk is precisely what the credit risk premium pays for.

**A6. What is the fulcrum security, and why does the distressed investor care about it?**

The fulcrum security is the layer of the capital structure where enterprise value "runs out" — the claim that is only partly covered and therefore converts partly to cash/new debt and partly to the *new equity* of the reorganized company. It is the target of loan-to-own investing: buy it cheaply and emerge owning the recapitalized business. Locating it correctly is the whole game, because the layer just above it recovers 100% and the layer just below it may get nothing.

**A7. Why is high yield typically *less* rate-sensitive than same-maturity investment grade?**

Two reasons. First, the spread is so large that credit dynamics swamp small rate moves. Second, in risk-off episodes HY spreads *widen* while Treasuries *rally*, so the two effects partly offset — pushing HY's effective duration below that of same-maturity IG. HY's dominant risk is spread/credit, not rates; deep in distress it trades on enterprise value and behaves almost like equity.

**A8. Contrast incurrence and maintenance covenants, and explain why cov-lite is a late-cycle warning.**

An *incurrence* covenant is tested only when the company takes an action (issuing debt, paying a dividend). A *maintenance* covenant is tested every period regardless of action (e.g., leverage must stay below a threshold each quarter). Cov-lite loans strip out maintenance tests. This matters because a slowly deteriorating business can burn cash for quarters without tripping any incurrence test — the maintenance test would have caught it. Cov-lite prevalence rises in frothy markets, shifts leverage from lenders to sponsors, and tends to lower eventual recoveries; it is a classic late-cycle red flag.

---

## Section B — Numerical / Applied

**B1. Break-even spread and risk premium.** A single-B bond trades at 500 bps over Treasuries. For its rating, λ = 4% and RR = 40%.

Solution. LGD = 1 − 0.40 = 0.60.
Break-even spread = λ × LGD = 0.04 × 0.60 = 0.024 = **240 bps**.
Risk premium + liquidity comp = market − break-even = 500 − 240 = **260 bps**.
Expected one-year excess return over Treasuries ≈ s − λ(1−RR) = 500 − 240 = **260 bps**. You are being paid 260 bps above the expected-loss floor to bear the uncertainty and correlation of the risk.

**B2. Portfolio reconciliation of the excess return.** Take 100 identical B bonds, $100 face, coupon = risk-free (4%) + 5% = 9%, λ = 4%, RR = 40%. Verify the excess-return estimate.

Solution.
- 96 survive: pay principal + coupon = 96 × $109 = $10,464.
- 4 default: recover 40% of face = 4 × $40 = $160 (assume they forfeit the coupon).
- Total ≈ $10,624 on $10,000 invested → return ≈ +6.24%.
- Risk-free was 4%, so excess ≈ **+2.24%**.

The linear formula gave 2.60%. The gap arises because defaulters also forfeit their coupon — a second-order effect the linear approximation omits, which makes the approximation slightly optimistic. The figures reconcile.

**B3. Cumulative default over five years.** λ = 4% constant. Find the 5-year survival and cumulative default probabilities, discrete and continuous.

Solution.
Discrete: Survival(5) = (1 − 0.04)^5 = 0.96^5 = 0.8154 → CDP(5) = 1 − 0.8154 = **18.5%**.
Continuous: Survival(5) ≈ e^(−λT) = e^(−0.20) = 0.8187 → CDP(5) = **18.1%**.
The two agree within a few tenths of a percent (as expected for small λ). Nearly a one-in-five chance that a *single* B bond defaults within five years — which is why single-name concentration in HY is dangerous and the asset class is played as a diversified book.

**B4. The fulcrum security and waterfall.** Company XYZ, capital structure by face value: Senior secured $300mm, Senior unsecured $400mm, Subordinated $200mm, Equity nil. Reorganized enterprise value = $550mm. Find each layer's recovery and identify the fulcrum.

Solution (apply absolute priority):
- Senior secured $300mm → fully covered, recovers 100% ($300mm). Remaining: 550 − 300 = $250mm.
- Senior unsecured $400mm claim → gets remaining $250mm → recovery = 250/400 = **62.5 cents**. Remaining: $0.
- Subordinated $200mm → **0 cents**. Equity → wiped out.

The **senior unsecured bond is the fulcrum** — value breaks here, so it converts partly to cash/new debt and partly to new equity.

**B5. The distressed trade and downside stress.** Senior unsecured from B4 trades at 45 cents. (a) Return if your $550mm EV is right. (b) Return if EV is only $400mm.

Solution.
(a) Buy $400mm face at 45 = $180mm invested; recover $250mm of value. Gain = $70mm → 70/180 = **+38.9%**. Equivalently (62.5 − 45)/45 = +38.9%.
(b) At EV = $400mm: secured takes $300mm, leaving $100mm for unsecured → recovery = 100/400 = 25 cents. Buying at 45 → (25 − 45)/45 = **−44.4%**.

The asymmetry — large upside if the EV estimate is right, large loss if it is low — is why distressed investing is valuation-driven credit work, not coupon clipping. The edge is entirely in estimating enterprise value and reading the waterfall correctly.

**B6. Solving the triangle for an implied default rate.** A senior unsecured HY bond trades at 700 bps. Assume the entire spread is expected loss (zero risk premium) and RR = 35%. What annual default rate is implied? Then, if the true λ is only 5%, what excess return are you being paid?

Solution.
Implied λ = s / (1 − RR) = 0.07 / 0.65 = 0.1077 = **~10.8%**. The market is pricing (under the no-premium assumption) roughly an 11% annual default rate.
If true λ = 5%: break-even = 0.05 × 0.65 = 0.0325 = 325 bps. Expected excess ≈ 700 − 325 = **375 bps**. You are being paid 375 bps above the expected-loss floor — attractive *if* your 5% default view is correct.

---

## Section C — Interview Style

**C1. "Walk me through why a wider spread is not automatically a better deal."**

Model answer. A wider spread reflects a higher perceived risk — more expected loss, more uncertainty, or less liquidity. Whether it is a good deal depends entirely on how it compares to the break-even spread implied by the true default and recovery outlook. Use the credit triangle: fair spread ≈ λ × (1 − RR). If the market spread exceeds that break-even by more than the risk premium I require, it is cheap; if not, it is expensive despite looking fat. At the depth of a recession, spreads can be enormous and *still* not wide enough if defaults are about to spike, or so wide that they overpay. The question is never the spread level in isolation — it is spread *versus* break-even, and where we sit in the credit cycle.

**C2. "A bond yields 9%. Is that my expected return?"**

Model answer. No — 9% is the *promised* yield, the ceiling you reach only if nothing defaults. Expected return is promised yield minus expected credit loss = yield − λ × (1 − RR). If λ is 4% and recovery is 40%, expected loss is about 2.4%, so expected return is closer to 6.6%. Credit is actuarial: you earn the coupon on the survivors and eat the losses on the defaulters. Quoting the yield as the expected return is the single most common error in high yield.

**C3. "How would you analyze a high-yield name you'd never seen before?"**

Model answer. I run a structured checklist. (1) Leverage — Debt/EBITDA, gross and net, and its trend. (2) Coverage — interest coverage (EBITDA/interest) and fixed-charge coverage including capex and scheduled amortization. (3) Cash — FCF conversion (FCF/EBITDA) and liquidity runway (cash plus revolver availability over the burn rate). (4) The maturity wall — when does the debt come due and can it be refinanced? (5) The covenant package — incurrence versus maintenance, and is it cov-lite? (6) My position in the capital structure and seniority — what would I recover if it defaults? (7) Finally, spread versus break-even — am I actually paid for the risk? The first six size the probability and severity of default; the last one tells me whether the price compensates me.

**C4. "Explain the mental model that a high-yield bond is a short put on the firm's assets."**

Model answer. As a lender I collect a premium — the spread — in exchange for absorbing losses if the firm's asset value falls below its debt. That payoff is exactly a short put on enterprise value: capped upside (I get my coupon and principal back), and a long tail of losses if the firm's value craters. In good times I clip the premium; in bad times the put is exercised against me across many names at once, because defaults cluster. This is the Merton view. Deep in distress the bond trades on enterprise value and behaves almost like equity — the put is deep in the money. Distressed investing is what happens then: the game becomes valuing the wreckage and standing in the right place in the priority line to claim it.

**C5. "Why do PD and LGD move together, and why does that make bad years worse?"**

Model answer. Defaults cluster in recessions, and recoveries are countercyclical: when many firms default at once, asset values are depressed, buyers are scarce, and forced sales happen into a weak market — so recoveries fall exactly when default rates spike. That positive correlation means a naive model treating PD and LGD as independent understates tail losses. In a bad year you get hit twice: more names default *and* each recovers less. This is a core reason the credit risk premium exists and why HY losses are lumpy rather than smooth.

**C6. "What is the difference between distressed and defaulted, and why does it matter for strategy?"**

Model answer. Defaulted means a payment was missed or a distressed exchange occurred. Distressed means the debt is *trading* at distressed levels — conventionally a spread above ~1000 bps or a price below ~70 — which frequently happens *before* any formal default and to companies that may never default. Much distressed investing is in bonds of stressed-but-not-defaulted issuers, betting either on a turnaround/refinancing or on a favorable restructuring outcome. The strategy differs: pre-default you may be underwriting a recovery or a coercive exchange; post-default you are negotiating a reorganization plan and locating the fulcrum. Conflating the two leads you to miss the pre-default opportunity set entirely.

---

## Section D — MCQs with Reasoning

**D1. The break-even (fair) credit spread is best approximated by:**
A. λ + RR  B. λ × (1 − RR)  C. λ × RR  D. (1 − λ) × RR

Answer: **B**. The credit triangle: break-even spread ≈ hazard rate × loss given default = λ × (1 − RR). A adds unrelated quantities; C multiplies by recovery instead of loss; D is not the expected-loss form.

**D2. Recoveries are described as countercyclical to default rates. This means:**
A. Recoveries rise when defaults rise  B. Recoveries and defaults are independent  C. Recoveries fall when defaults rise  D. Recoveries are fixed at 40%

Answer: **C**. When many firms default at once (recession), depressed asset values push recoveries down — PD and LGD are positively correlated, so bad years hit twice. A is backwards; B ignores the documented correlation; D is a modeling error (40% is only the long-run senior-unsecured average).

**D3. The fulcrum security is:**
A. The most senior secured claim  B. The layer where enterprise value runs out and which converts to new equity  C. Always the subordinated notes  D. The equity tranche

Answer: **B**. The fulcrum is where value "breaks" — partly covered, so it converts partly to new equity of the reorganized firm. The senior secured layer (A) is usually fully covered and recovers 100%; the fulcrum's identity depends on EV versus the waterfall, so it is not fixed at any layer (C, D wrong).

**D4. Relative to same-maturity investment-grade bonds, high-yield bonds typically have:**
A. Higher effective duration  B. Lower effective duration  C. Identical duration  D. Negative duration always

Answer: **B**. Credit dynamics dominate and, in stress, HY spreads widen while Treasuries rally, partly offsetting rate moves — lowering effective duration below same-maturity IG. HY's main risk is spread/credit, not rates.

**D5. Under the absolute priority rule, the correct payment order is:**
A. Equity → subordinated → senior unsecured → secured  B. Secured → senior unsecured → subordinated → equity  C. Senior unsecured → secured → equity → subordinated  D. Pro-rata across all claims equally

Answer: **B**. Secured creditors are paid first, then senior unsecured, then subordinated, with equity last (usually wiped out). The others violate the priority waterfall.

**D6. Cov-lite loan structures are a late-cycle warning sign primarily because they:**
A. Add maintenance tests that trip too often  B. Remove maintenance tests, delaying lender intervention and lowering recoveries  C. Raise coupons for lenders  D. Guarantee change-of-control puts

Answer: **B**. Cov-lite strips *maintenance* covenants (tested every period), so a deteriorating business can burn cash without tripping a test; lenders intervene later and recoveries tend to be lower. A misdescribes the mechanism; C and D are unrelated to the cov-lite definition.

**D7. A bond yields 10%, with λ = 5% and RR = 30%. Its approximate expected return is:**
A. 10.0%  B. 8.5%  C. 6.5%  D. 3.5%

Answer: **C**. Expected loss = λ × (1 − RR) = 0.05 × 0.70 = 3.5%. Expected return ≈ yield − expected loss = 10% − 3.5% = **6.5%**. A is the promised yield (the trap); B and D use wrong loss figures.

**D8. "Distressed" debt is conventionally defined by which market signal?**
A. Spread below 300 bps  B. Price above par  C. Spread above ~1000 bps or price below ~70  D. Rating of BBB−

Answer: **C**. The market convention for distressed is a spread wider than roughly 1000 bps or a price below about 70 — a level that can occur before any formal default. A and B describe healthy credit; D is the last investment-grade notch.
