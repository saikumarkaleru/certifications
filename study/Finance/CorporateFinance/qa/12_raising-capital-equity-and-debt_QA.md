# Q&A — Raising Capital: Equity & Debt

A mixed bank of theory and numerical questions for equity research, credit, FP&A, and IB interviews. Numerical answers are fully worked and self-verified.

---

## Theory

### Q1. What is the fundamental difference between debt and equity as claims on a firm?

**Model answer.** Equity is a **residual, perpetual, control-bearing** claim: shareholders own whatever is left after all other claimants are paid, they never have to be repaid, they vote, and their payoff is unlimited on the upside but can go to zero. Debt is a **fixed, dated, senior, contractual** claim: lenders are promised specific cash flows on specific dates, rank ahead of equity in liquidation, do not vote, and their best case is simply getting repaid. Every hybrid — preferred stock, convertibles, mezzanine — sits on the spectrum between these two poles.

**How to say it:** "Equity is junior, permanent, and votes; debt is senior, dated, and contractual. Debt is cheaper because it's safer and tax-deductible; equity is the most expensive capital because it bears the most risk."

### Q2. Walk me through the IPO process.

**Model answer.** Appoint bookrunning banks → due diligence and draft prospectus (DRHP / S-1) disclosing business, financials, risk factors, use of proceeds → regulator reviews for disclosure (not merits) → roadshow to institutions → **book-building**: set a price band, collect bids, build the demand book → set offer price (with a deliberate underpricing discount), allocate shares favoring honest bidders → list and stabilize via the greenshoe. First-principles thread: the prospectus fights information asymmetry, the book-build discovers price, underpricing rewards honest demand.

### Q3. Primary vs secondary shares — who receives the proceeds, and what happens to dilution?

**Model answer.** **Primary** = newly issued shares; the **company** receives the cash and share count rises, diluting existing holders. **Secondary** = existing shares sold by current owners; the **selling shareholder** gets the cash and there is no change in share count or dilution. A single IPO can bundle a fresh issue (primary) with an offer for sale (secondary). Trap: only primary proceeds fund the company.

### Q4. Why are IPOs systematically underpriced?

**Model answer.** Four reasons worth naming: (1) **Winner's curse** — uninformed investors only get full allocations in bad deals, so issues must be underpriced on average to keep them participating; (2) **information revelation** — underpricing is the reward for institutions that reveal honest demand in book-building; (3) **certification / cascade** — a first-day pop marks a "hot" deal and reduces failed-offering risk; (4) **litigation risk** (US) — a low price reduces the chance of being sued. Underpricing is a real, often large, *implicit* cost to pre-IPO owners, separate from the explicit gross spread.

### Q5. Firm-commitment vs best-efforts underwriting.

**Model answer.** Firm-commitment: the bank **buys** the whole issue at a set price and resells, bearing the risk of unsold shares — the issuer's proceeds are guaranteed. Standard for major IPOs and bonds. Best-efforts: the bank only agrees to **try** to place the issue and bears no inventory risk. The bank's compensation is the **gross spread** = offer price − price paid to issuer, which splits into management fee, underwriting fee, and selling concession.

### Q6. What is a rights issue and why do firms use it instead of a public offer?

**Model answer.** A rights issue offers new shares **to existing shareholders pro rata** at a **discount**, in a fixed ratio, with the right usually tradable. It preserves existing holders' percentage ownership and value (if they exercise), is cheaper (little marketing, no need to court new investors), and avoids the adverse-selection signal of selling to outsiders. The discount is not free value — the price falls from cum-rights to the theoretical ex-rights price (TERP) by exactly the value of the right.

### Q7. Explain the pecking-order theory and why an equity issue often drops the share price.

**Model answer.** Myers-Majluf: because managers know more than the market, firms finance in the order **internal funds → debt → equity**. Managers tend to issue equity when they believe it is overvalued; rational investors anticipate this, so an equity (SEO) announcement is read as a signal of overvaluation and the price falls. Debt is far less information-sensitive, so it sends a much milder signal. This is why equity is treated as a last resort despite being non-repayable.

### Q8. Trade-off theory: how does a firm find its optimal leverage?

**Model answer.** Debt adds value through the **interest tax shield** (interest is tax-deductible) but raises **expected financial-distress and bankruptcy costs** as leverage rises. Optimal leverage is where the marginal tax benefit equals the marginal expected distress cost. Firms with stable cash flows and tangible, pledgeable assets can support more debt; volatile, asset-light firms can support less.

### Q9. QIP, FPO, and preferential allotment — distinguish them.

**Model answer.** All raise equity for a *listed* company. **FPO/SEO**: broad public offer via book-build, weeks, higher cost. **QIP**: shares placed only with Qualified Institutional Buyers under a regulated pricing formula — very fast (days), cheap, no retail; the global analogue is an accelerated bookbuild. **Preferential allotment / PIPE**: shares to specific named investors (a strategic partner, PE fund, promoter) at a regulated price, often with lock-in — fast and negotiated but concentrated.

### Q10. Bonds vs syndicated bank loans — when does a company choose each?

**Model answer.** **Bonds** tap a deep public investor base, usually offer lower rates for large, long-tenor amounts, and carry looser *incurrence* covenants — but need a rating, public disclosure, and are hard to renegotiate; typically fixed-rate. **Syndicated loans** are private, faster, prepayable, and renegotiable, but usually floating-rate, senior secured, shorter, and carry *maintenance* covenants tested every quarter. Investment-grade firms lean on bonds; leveraged deals use Term Loan B plus high-yield bonds, with a revolver for working capital.

### Q11. What is a greenshoe / over-allotment option and what is it for?

**Model answer.** It is the underwriter's option to sell up to ~15% additional shares beyond the base deal and buy them back in the aftermarket. It lets the bank **stabilize** the price for a limited window (~30 days): if the stock falls, the bank covers its short by buying in the market (supporting the price); if it rises, the bank exercises the option to deliver the extra shares. It is a legal price-support mechanism.

### Q12. How should flotation (issuance) costs be treated in a project valuation?

**Model answer.** As a **one-time cash outflow that increases the initial investment** — not as a permanent addition to the discount rate. If you need `A` net and flotation is a fraction `f` of gross proceeds, raise `Gross = A / (1 − f)` and add the cost to the project's Year-0 outlay. Bumping the WACC would incorrectly penalize every future year's cash flow.

### Q13. Maintenance vs incurrence covenants — why does the distinction matter to a credit analyst?

**Model answer.** **Maintenance** covenants (typical of bank loans) are tested every quarter regardless of any action — e.g., Net Debt/EBITDA must stay below a threshold — so a deteriorating borrower breaches quickly, giving lenders early control. **Incurrence** covenants (bonds and "cov-lite" loans) are tested only when the borrower takes a specific action, such as raising new debt or paying a dividend. Cov-lite structures give borrowers more rope and lenders less early warning, which matters enormously in a downturn.

### Q14. Why do investment banks get paid ~7% on a US IPO — what are you paying for?

**Model answer.** Three things: **risk-bearing** (in firm-commitment the bank owns unsold shares), **certification** (the bank stakes its reputation that the deal is fairly priced, bridging information asymmetry), and **distribution** (access to a broad, dispersed institutional and retail investor base plus research coverage and aftermarket stabilization). A direct listing skips the spread but forgoes guaranteed proceeds, stabilization, and certification.

---

## Numerical

### Q15. IPO proceeds, spread, and underpricing.

A company IPOs **8m primary** and **2m secondary** shares at **₹300**, gross spread **6%**, day-one close **₹360**. Compute (a) deal size, (b) company vs seller proceeds before fees, (c) net-to-company after spread, (d) underpricing % and money left on the table.

**Solution.**
(a) Shares = 8m + 2m = 10m; deal = 10m × 300 = **₹3,000m**.
(b) Company (primary) = 8m × 300 = **₹2,400m**; sellers (secondary) = 2m × 300 = **₹600m**.
(c) Spread on primary = 6% × 2,400 = ₹144m → net to company = **₹2,256m**.
(d) Underpricing = (360 − 300)/300 = **20%**; money left on the table = (360 − 300) × 10m = **₹600m**.
*Check:* explicit spread (₹144m to company) is dwarfed by the ₹600m implicit underpricing — the intended lesson. ✓

### Q16. Rights issue — TERP, value of a right, wealth neutrality.

A firm has **200m shares at ₹120**. It does a **1:5 rights issue at ₹90**. Find (a) new shares and cash, (b) TERP, (c) value of a right per existing share, (d) verify wealth neutrality for a holder of 500 shares who sells the rights.

**Solution.**
(a) New shares = 200m/5 = **40m**; cash = 40m × 90 = **₹3,600m**.
(b) TERP = (200m×120 + 40m×90)/(240m) = (24,000m + 3,600m)/240m = 27,600m/240m = **₹115**.
(c) Right per existing share = (Cum − Sub)/(n+1) = (120 − 90)/(5+1) = 30/6 = **₹5**.
(d) Holder of 500: before = 500×120 = ₹60,000. After selling rights: keeps 500 shares at TERP 115 = ₹57,500; sells 500/5 = 100 rights. Value per *new* share right = TERP − Sub = 115 − 90 = ₹25; per existing share = ₹25/5 = ₹5, so 500 shares' rights = 500×5 = ₹2,500. Total = 57,500 + 2,500 = **₹60,000.** Unchanged. ✓

### Q17. EBIT–EPS break-even (debt vs equity).

A firm needs **₹200m**, has **20m shares**, tax **30%**, no existing debt. Plan D: debt at **9%** (₹18m interest). Plan E: issue **4m shares at ₹50**. Find the indifference EBIT and interpret.

**Solution.** EPS(D) = [(EBIT − 18)(0.70)]/20; EPS(E) = [(EBIT)(0.70)]/24.
Set equal, cancel 0.70: (EBIT − 18)/20 = EBIT/24 → 24(EBIT − 18) = 20·EBIT → 24EBIT − 432 = 20EBIT → 4EBIT = 432 → **EBIT\* = ₹108m**.
EPS at break-even: EPS(E) = 108×0.70/24 = 75.6/24 = **₹3.15**; EPS(D) = (108−18)×0.70/20 = 90×0.70/20 = 63/20 = **₹3.15.** ✓
**Interpretation:** above ₹108m EBIT, debt gives higher EPS (leverage helps); below it, equity is better; equal at ₹108m.

### Q18. Bond pricing (discount and premium).

A **4-year, ₹1,000 face, 6% annual-coupon** bond. Price it if the required yield is (a) 8%, (b) 5%.

**Solution.** Coupon = ₹60/yr.
(a) At 8%: 1.08⁴ = 1.36049 → 1.08⁻⁴ = 0.73503. Annuity factor = (1 − 0.73503)/0.08 = 0.26497/0.08 = 3.3121. PV coupons = 60×3.3121 = ₹198.73; PV par = 1000×0.73503 = ₹735.03. **Price = ₹933.76** (discount, since yield > coupon). ✓
(b) At 5%: 1.05⁴ = 1.21551 → 1.05⁻⁴ = 0.82270. Annuity factor = (1 − 0.82270)/0.05 = 0.17730/0.05 = 3.5460. PV coupons = 60×3.5460 = ₹212.76; PV par = 1000×0.82270 = ₹822.70. **Price = ₹1,035.46** (premium, since yield < coupon). ✓
Confirms the inverse price–yield relationship.

### Q19. Flotation-cost gross-up.

A firm needs **₹250m net** from an equity issue with all-in flotation cost **f = 5%** of gross proceeds. How much must it raise gross, and how much is the flotation cost?

**Solution.** Gross = Net/(1 − f) = 250/(1 − 0.05) = 250/0.95 = **₹263.16m**. Flotation cost = 263.16 − 250 = **₹13.16m** (= 5% of gross 263.16 ✓). Treat the ₹13.16m as an upfront outflow added to the project's Year-0 investment — not as a WACC add-on.

### Q20. Yield decomposition and credit spread.

A 5-year corporate bond yields **7.4%**. The 5-year government benchmark yields **5.0%**. (a) What is the credit spread? (b) If the market's estimated default probability is 3% per year with a 40% loss-given-default, is the spread roughly compensating for expected loss, and what does the residual represent?

**Solution.**
(a) Credit spread = 7.4% − 5.0% = **2.4% (240 bps)**.
(b) Rough annual expected credit loss ≈ PD × LGD = 3% × 40% = **1.2% (120 bps)**. The spread (240 bps) is about double the pure expected loss (120 bps). The residual ≈ 120 bps compensates for **risk premium (unexpected loss / default risk aversion) and a liquidity premium** — investors demand more than the mathematically expected loss to hold risky, less-liquid paper. This "credit spread puzzle" (spreads exceed expected losses) is a good line to drop in a credit interview. ✓

### Q21. Syndicated loan economics — arranger fee and final hold.

A ₹5,000m term loan is arranged by an MLA that underwrites the full amount, earns a **1.5% upfront arrangement fee**, and syndicates **₹4,000m** to other banks (passing them a **1.0%** participation fee on their commitments), keeping the rest on its own book. Compute (a) MLA's gross arrangement fee, (b) fees paid away to participants, (c) MLA's net fee, (d) MLA's final hold.

**Solution.**
(a) Gross arrangement fee = 1.5% × 5,000 = **₹75m**.
(b) Paid to participants = 1.0% × 4,000 = **₹40m**.
(c) MLA net fee = 75 − 40 = **₹35m**.
(d) Final hold = 5,000 − 4,000 = **₹1,000m** on its own book.
*Interpretation:* the arranger earns a spread by underwriting the whole amount at 1.5% and selling most of it down at 1.0%, keeping the 0.5% differential on the ₹4,000m (= ₹20m) **plus** the full 1.5% on the ₹1,000m it retains (= ₹15m) → ₹35m net. ✓ (Cross-check: 20 + 15 = ₹35m.)

### Q22. Effective cost of an IPO (spread + underpricing combined).

Using Q15's figures (offer ₹300, close ₹360, 8m primary shares, 6% spread on primary), estimate the company's **effective cost of capital raised** relative to what the shares were "worth" on day one.

**Solution.** Company primary raise (gross) = 8m × 300 = ₹2,400m; net after 6% spread = ₹2,256m. Market value of those 8m shares at the day-one close = 8m × 360 = ₹2,880m.
Effective cost = 1 − (net received / day-one market value) = 1 − 2,256/2,880 = 1 − 0.7833 = **21.7%** of the shares' day-one value was "lost" to spread + underpricing combined.
Decompose: underpricing alone on primary = (360 − 300) × 8m = ₹480m; spread = ₹144m; total ≈ ₹624m ≈ 21.7% of ₹2,880m. ✓
*Line:* "The headline 6% spread understates the true cost of going public — add first-day underpricing and the effective cost here is over 20%."
