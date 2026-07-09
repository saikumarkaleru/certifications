# Q&A — Credit Analysis and Modeling

A practice bank for Chapter 32. Work each problem before reading the answer. All dollar figures are in millions (\$m) unless noted. Excel-reproducible steps are given for Section B; formulas are shown as they would be typed. Every answer self-checks where a reconciliation is possible.

---

## Section A — Concept-Check

**A1. What single question does a credit analyst answer, and how does it differ from the equity analyst's?**

The credit analyst asks *will I get my money back, on time, in full, even if things go badly?*; the equity analyst asks *what is this business worth to an owner?* Equity has unlimited upside and limited downside, so it centres on the base case and upside; debt has capped upside (par plus coupon) and severe downside (default), so it centres on the downside.

**A2. State the credit asymmetry and why it dictates the modeling posture.**

Debt's return is capped at par plus interest but its loss can be near-total in default. A lender right 95% of the time can still lose money if the 5% of defaults are large enough, because winners never pay extra to compensate. Since expected return is dominated by the tail, the model's centre of gravity is the *stressed* case and the *headroom* to covenants — not the base case.

**A3. Name the two distinct ways a company can fail its lenders.**

(1) **Liquidity default** — cannot make a scheduled interest or principal payment when due; a *flow* problem. (2) **Covenant breach / solvency default** — leverage or coverage crosses a contractual threshold, letting lenders accelerate or renegotiate; a *ratio* problem that can bite long before cash runs out.

**A4. Distinguish a leverage ratio from a coverage ratio, and give the flagship of each.**

Leverage is a **stock** measure — debt versus a year of earning power; flagship **Debt / EBITDA** ("how many years of EBITDA to repay all debt?"). Coverage is a **flow** measure — this period's cash versus this period's obligations; flagship **EBITDA / Interest** ("how many times can I pay the interest bill?").

**A5. Why do you need both lenses rather than just the tighter one?**

They fail in different weather. A firm on cheap fixed-rate debt can have comfortable coverage yet dangerous 6x leverage (exposed if EBITDA falls or it must refinance higher). A lightly levered firm on floating-rate debt can have low leverage yet thin coverage in a rate spike. A company can look safe on one lens and dangerous on the other.

**A6. Why is EBITDA the anchor for credit ratios, and what is its main weakness?**

EBITDA sits *above* interest, so it proxies the pre-financing, pre-tax cash pool available to pay lenders before financing choices. Weakness: it ignores capex, working-capital swings, and cash taxes, so it is **not** cash flow. A capex-heavy firm can show healthy EBITDA coverage yet be cash-negative — which is why DSCR and FCCR supplement it.

**A7. Write the DSCR formula and say what failure mode it tests.**

DSCR = CFADS / (Scheduled Principal + Cash Interest), where CFADS ≈ EBITDA − Cash taxes − Maintenance capex − ΔWorking capital. It tests the **liquidity-default** mode: 1.0x means cash exactly covers debt service with zero margin; below 1.0x the company must dip into reserves or draw the revolver to pay.

**A8. Maintenance versus incurrence covenants — one line each.**

**Maintenance** covenants are tested every period automatically (a passive tripwire hit just by a bad quarter); typical of bank/leveraged loans. **Incurrence** covenants are tested only when the company takes an action (issuing debt, paying a dividend, acquiring); typical of high-yield bonds. The "cov-lite" shift transfers protection from lenders to borrowers.

**A9. Define headroom and explain why it is the most decision-relevant output.**

Headroom is the distance between the stressed ratio and its covenant threshold — e.g. "EBITDA can fall 12.5% before we breach leverage." It answers "how wrong can I be and still be safe?" Because the lender is only exposed when hope fails, the size of the cushion, not the base-case point estimate, is what a credit committee decides on.

**A10. Why must PIK interest be treated differently from cash interest in the ratios?**

PIK (pay-in-kind) interest accretes onto principal instead of being paid in cash. It belongs in **leverage** (it grows the balance) but must be **excluded** from cash interest in DSCR and interest-coverage. Including it in cash coverage overstates the drain; dropping it from the balance understates leverage — track cash and PIK interest separately.

**A11. What is the sign convention for covenant flags, and why is getting it wrong dangerous?**

Leverage covenants are **maximums** (Actual < Limit is good); coverage and DSCR are **minimums** (Actual > Limit is good). Reversing the direction in an `IF` produces false-green cells — a silent error hiding a real breach. Test each flag by entering a breaching value and confirming it turns red.

**A12. Two companies have identical Debt/EBITDA of 5x; one is rated BBB, the other B. How?**

The rating blends **financial risk** (the ratios) with **business risk** (cyclicality, competitive position, scale, cash-flow stability). A stable regulated utility earns a better rating at 5x than a cyclical commodity producer because its cash flows are far more predictable and can safely carry more leverage. Ratios set the centre; business risk moves the mapping.

---

## Section B — Build / Computational Problems

We use **Aster Components** throughout so the numbers reconcile. Year 0 base inputs:

- EBITDA \$250m (Revenue \$1,250m × 20% margin); D&A \$60m → EBIT \$190m
- Term Loan \$600m at 7.5% (amortizes 8%/yr = \$48m), Senior Notes \$200m at 9.0% fixed → Total Debt \$800m; Cash \$40m
- Cash taxes \$30m; Capex \$55m; ΔWorking capital \$8m
- Covenants: Max Net Leverage 3.50x, Min Interest Coverage 3.00x, Min DSCR 1.20x

**B1. Compute cash interest, gross leverage, and net leverage.**

1. Cash interest = `600*0.075 + 200*0.09` = 45 + 18 = **\$63.0m**.
2. Gross leverage = `800/250` = **3.20x**.
3. Net leverage = `(800−40)/250` = 760/250 = **3.04x**.

Check: the 0.16x gross-to-net gap = 40/250 = cash-to-EBITDA ✓.

**B2. Compute interest coverage, EBIT coverage, CFADS, debt service, and DSCR.**

1. Interest coverage = `250/63` = **3.97x**; EBIT coverage = `190/63` = **3.02x**.
2. CFADS = `250 − 30 − 55 − 8` = **\$157m**.
3. Debt service = Principal + Cash interest = `48 + 63` = **\$111m**.
4. DSCR = `157/111` = **1.41x**.

Check: interest is 63/250 = 25.2% of EBITDA, so coverage = 1/0.252 = 3.97x ✓.

**B3. Covenant results and headroom in turns (base case).**

All three clear: Net Leverage 3.04x vs ≤3.50x (0.46x headroom); Interest Coverage 3.97x vs ≥3.00x (0.97x); DSCR 1.41x vs ≥1.20x (0.21x). Excel flags: `=IF(NetLev>MaxLev,"BREACH","OK")`, `=IF(Cov<MinCov,"BREACH","OK")`, `=IF(DSCR<MinDSCR,"BREACH","OK")` — note the sign flip on the first versus the last two.

**B4. Debt capacity at the 3.50x net-leverage covenant. Is leverage or coverage binding?**

1. Max net debt = `3.50 * 250` = \$875m; add back cash \$40m → gross capacity ≈ **\$915m**.
2. Current gross debt \$800m → additional capacity ≈ **\$115m**.
3. Coverage check on the extra \$115m: at blended rate 63/800 = 7.875%, extra interest ≈ \$9.06m → interest \$72.06m; new coverage = `250/72.06` = **3.47x**, still above 3.00x.

Coverage still clears at full leverage capacity, so **leverage is binding** and genuine capacity is ~\$115m ✓.

**B5. EBITDA headroom — how far can EBITDA fall before each covenant breaks (debt, cash, interest and the taxes+capex+ΔWC block held constant)? Which binds first?**

Fixed non-financing block = Taxes + Capex + ΔWC = `30 + 55 + 8` = \$93m, so CFADS = EBITDA − 93.

1. **Leverage:** `760 / EBITDA* = 3.50` → EBITDA* = \$217.1m → decline **13.1%**.
2. **Coverage:** `EBITDA* / 63 = 3.00` → EBITDA* = \$189.0m → decline **24.4%**.
3. **DSCR:** `CFADS* / 111 = 1.20` → CFADS* = \$133.2m → EBITDA* = `133.2 + 93` = \$226.2m → decline **9.5%**.

**Binding covenant = DSCR, at a 9.5% decline.** Teaching point: DSCR is tightest because it includes principal, so it can bind *before* leverage even though leverage looked closest in "turns" — check all three in cash terms. Check: EBITDA 226.2 → CFADS 133.2 → DSCR 133.2/111 = 1.20x ✓.

**B6. Average-balance interest on the Term Loan for Year 1 vs the opening-balance method.**

Given: Opening \$600m, mandatory amortization 8% = \$48m, no sweep → Closing \$552m, rate 7.5%.

1. Opening-balance interest = `600 * 0.075` = **\$45.0m**.
2. Average balance = `(600 + 552)/2` = \$576m → average-balance interest = `576 * 0.075` = **\$43.2m**.

The average-balance method is \$1.8m lower because it credits the in-year paydown. Excel: `=Rate*(Opening+Closing)/2`. Trade-off: it is more accurate but adds circularity (interest depends on closing balance, which can depend on a sweep); opening-balance is simpler and circularity-free.

**B7. Cash sweep with the `MIN` cap, and identify the circularity.**

Given: after mandatory amortization the Term Loan is \$552m; excess cash for prepayment is \$30m.

1. Sweep = `=MIN(30, 552)` = **\$30m**.
2. Closing balance = `552 − 30` = **\$522m**.

The circularity: interest → balance → sweep → cash → interest. Enable iterative calculation (~100 iterations) or use a **circ switch** that zeroes the sweep to break the loop while debugging. Never paste a hardcoded interest number over a broken circularity.

**B8. FCCR for Aster, given operating lease payments \$10m and preferred dividends \$5m.**

FCCR = (EBITDA − Capex − Cash taxes) / (Cash interest + Scheduled principal + Leases + Pref div).

1. Numerator = `250 − 55 − 30` = \$165m.
2. Denominator = `63 + 48 + 10 + 5` = \$126m.
3. FCCR = `165/126` = **1.31x**.

FCCR is lower than DSCR (1.41x) because it loads more fixed charges (leases, preferred) into the denominator and subtracts capex — the broadest, most conservative coverage test. Always confirm the exact FCCR definition in the credit agreement.

**B9. Downside stress — recession case. Flag every covenant and test for true liquidity default.**

Stress: EBITDA falls 18% to `250*0.82` = **\$205m**; floating Term Loan rate rises to 9.5% (Notes fixed 8→ still 9.0%); cash taxes fall to \$22m on lower profit; capex \$55m and ΔWC \$8m held; principal \$48m.

1. Stressed interest = `600*0.095 + 200*0.09` = 57.0 + 18.0 = **\$75.0m**.
2. Net leverage = `760/205` = **3.71x → BREACH** (limit 3.50x).
3. Interest coverage = `205/75` = **2.73x → BREACH** (limit 3.00x).
4. CFADS = `205 − 22 − 55 − 8` = **\$120m**; debt service = `48 + 75` = **\$123m**.
5. DSCR = `120/123` = **0.98x → BREACH** (limit 1.20x, and **below 1.0x**).

All three breach (base → downside: leverage 3.04x→3.71x, coverage 3.97x→2.73x, DSCR 1.41x→0.98x). **Liquidity verdict:** DSCR of 0.98x is **below 1.0x** — the year's cash flow (\$120m) does *not* cover debt service (\$123m), a \$3m shortfall. Aster faces a genuine **liquidity default** and must draw the revolver or dip into reserves — worse than a pure covenant breach. The 9.5% DSCR headroom from B5 predicted it: the 18% shock far exceeds the 9.5% cushion ✓.

---

## Section C — Interview-Style Questions (with model answers)

**C1. "Walk me through how you'd size the debt for a new leveraged loan."**

Take the lower of two capacity lenses. **Leverage-based:** sustainable EBITDA × the maximum multiple the market tolerates for this credit and sector — say 4.5x × \$120m = \$540m. **Coverage-based:** the CFADS the business can dedicate to debt service, checked to support the resulting interest and amortization with a DSCR cushion (typically 1.10x–1.30x). The binding capacity is whichever bites first. Then stress it — I only lend the amount that still clears covenants in a realistic *downside*, not the base case. A number that works only if nothing goes wrong is the wrong number.

**C2. "Debt/EBITDA looks fine at 3x but you're worried. What do you look at next?"**

Debt/EBITDA is a stock ratio that ignores cash reality, so I pull the cash-based coverage — DSCR and FCCR — because a capex-heavy or high-tax business can carry 3x on paper yet be cash-thin after maintenance capex, working capital, and taxes. I'd also check the maturity wall (near-term refinancing?), the fixed-versus-floating mix, and whether the debt is gross or net of restricted cash. A clean leverage number with a 1.05x DSCR and a floating-rate book heading into a hiking cycle is not a safe credit.

**C3. "Why do lenders care more about the downside than the base case?"**

The payoff is asymmetric: my upside is capped at par plus coupon however well the company does, while my downside is default and recovery of cents on the dollar. My expected return is dominated by the tail, not the middle. The base case tells me what management hopes; only the downside can actually hurt me. So the real analysis is the stressed case and the headroom to the covenants — the distance between the stressed ratios and the lines in the sand.

**C4. "A borrower wants to switch from maintenance covenants to cov-lite. What changes for you?"**

I lose my early-warning tripwire. Maintenance covenants test leverage and coverage every quarter automatically, forcing a deteriorating borrower back to the table while it's still weak — exactly when I want leverage over it. Cov-lite (incurrence-only) bites only when the borrower takes an action like raising debt or paying a dividend, so the company can decline substantially without tripping anything. I'd price that lost protection into a wider spread or decline it — it's a transfer of value from lender to borrower and sponsor.

**C5. "How does a credit rating connect to cost of capital and valuation?"**

The rating drives the **cost of debt** (lower rating, wider spread, higher interest), which feeds **WACC**. Adding leverage initially lowers WACC because debt is cheaper and interest is tax-deductible — but only to a point. As leverage rises, default risk pushes the cost of debt, then equity, up faster than the tax shield helps, and WACC turns back up. Credit analysis locates that turning point. The optimal capital structure minimizes WACC without pushing the rating into distress, and a lower WACC lifts the DCF value.

**C6. "You've stressed EBITDA down 20%. What else should move in the downside, and why?"**

Two things people forget. First, the **revolver gets drawn** — in a downturn cash burn taps the revolver, so debt *rises* precisely when EBITDA falls, hitting leverage on both numerator and denominator. Second, **floating rates may rise**, so interest climbs even as coverage capacity shrinks. Working capital can swing against you and refinancing may be unavailable. A naive "cut EBITDA, hold everything else" stress is too kind — a credible downside lets the balance sheet and rate assumptions respond to the scenario, not just the P&L.

**C7. "Quick read: net leverage 3.5x, EBITDA/interest 3.6x — what rating band and why?"**

Squarely **BB** — upper high-yield. Leverage in the 3–4.5x band and coverage in the 3–4x band map to BB: leveraged but comfortably serviceable, not investment grade (sub-2x, 8x-plus coverage) and not distressed. The business-risk overlay shifts it a notch either way — a stable diversified issuer could stretch to BB+/BBB−, a small cyclical single-product name could sit at BB−. Ratios set the centre; qualitative risk moves the notch.

---

## Section D — Common-Error Spotting

For each, identify the error and give the fix.

**D1.** *An analyst reports "leverage is 3.04x, comfortably inside the 3.50x covenant" — but the agreement defines the covenant on gross debt. The analyst used net debt.*

**Error:** mismatching the covenant's debt definition; net 3.04x vs gross 3.20x can differ by a full turn in some deals, turning a real breach into a false "OK." **Fix:** match the exact numerator the agreement specifies; recompute on gross debt (3.20x) here.

**D2.** *A model shows EBITDA/interest of 4x and concludes "plenty of cash to service its debt."*

**Error:** treating EBITDA as cash flow — it ignores capex, working capital, cash taxes, and principal, so a capex-heavy firm can post 4x coverage yet be cash-negative. **Fix:** cross-check with DSCR and FCCR (which include principal, capex, taxes) and conclude on cash coverage.

**D3.** *A covenant flag reads `=IF(DSCR > MinDSCR, "BREACH", "OK")` and always shows OK.*

**Error:** reversed sign. DSCR is a *minimum* covenant — a breach is when Actual is **below** the limit. **Fix:** `=IF(DSCR < MinDSCR,"BREACH","OK")`, then test with a sub-limit value to confirm it turns red.

**D4.** *A modeller stresses EBITDA down 20% but holds the revolver balance and floating rate fixed, reporting the ratios "hold up fine."*

**Error:** static balance sheet in the downside — in a real downturn the revolver draws (debt rises) and floating rates may rise (interest rises), both worsening ratios beyond a P&L-only cut. **Fix:** let the revolver auto-draw when cash goes negative and let the rate respond to the scenario.

**D5.** *A model puts \$12m of PIK interest in the cash-interest line for DSCR and excludes the accreted PIK from the debt balance for leverage.*

**Error:** double-wrong PIK — including it in cash coverage understates coverage; excluding it from the balance understates leverage. **Fix:** exclude PIK from cash interest but include the accreted PIK in the debt balance; track the two separately.

**D6.** *A pitch states "at 5x leverage this issuer is clearly sub-investment-grade" for a regulated water utility.*

**Error:** over-trusting the grid without the business-risk overlay — a stable regulated utility can be investment grade at 5x where a cyclical producer at 3x is high-yield. **Fix:** apply the business-risk judgment before quoting an implied rating.

**D7.** *The interest line is a hardcoded blue-input number and the cash-sweep row is empty; the builder "turned off iterative calc because it threw a circular reference error."*

**Error:** breaking the circularity by hardcoding instead of resolving it — the sweep no longer responds and interest is stale the moment any assumption changes. **Fix:** re-enable iterative calculation (~100 iterations) with a **circ switch** to toggle the sweep for debugging, and drive interest with a live formula (`=Rate*(Open+Close)/2`).

---

*Build the Corvus Logistics model from §10 to convert this practice into fluency: reading teaches the logic, only building teaches credit.*
