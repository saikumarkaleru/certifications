# Q&A — Alternatives in Portfolios

> Scope: Investments — Chapter 15 (Alternatives in Portfolios). Every question is followed by a full model answer. Rates are annual and in percent unless stated. Work each numerical yourself first. Sections: **A** concept-check · **B** numerical (step-by-step, reconciling) · **C** interview-style · **D** MCQs with reasoning.

---

## The chapter in one line

$$\sigma_p^2=w_A^2\sigma_A^2+w_B^2\sigma_B^2+2w_Aw_B\rho\sigma_A\sigma_B, \qquad \text{Commodity return}=\text{Spot}+\text{Roll}+\text{Collateral}$$

**One-line statement:** Alternatives earn their place not by beating equities but by adding an imperfectly correlated return stream plus an illiquidity premium — yet the reported diversification is partly a smoothing illusion, fees are high, and manager dispersion is enormous, so access and due diligence decide whether they help.

---

## Section A — Concept Check

**A1. Give the working definition of "alternatives" and the four features that unite the category.**
Alternatives are any investment that is not plain-vanilla listed equity, listed bonds, or cash. Four features unite them: (1) *different return drivers* — from illiquidity, complexity, active skill, operational control, or real assets rather than public-market beta; (2) *reduced liquidity* — capital often locked up for years, trading the option to sell tomorrow for higher expected return; (3) *higher, more complex fees* — "2 and 20" dwarfs an index fund's few basis points; (4) *enormous manager dispersion* — the top-to-bottom-quartile gap can be 15–20 points a year, so access and selection are the whole game.

**A2. What three structural problems pushed serious investors toward alternatives?**
First, the *correlation trap*: in the crises that matter most (2008, March 2020, the 2022 rate shock) stock-bond and cross-equity correlations spike toward one, so diversification evaporates when needed. Second, the *low-yield / high-valuation squeeze*: post-2008 bond yields collapsed toward zero while equity valuations climbed, cutting the 60/40's expected return below what pensions must earn. Third, the *shrinking public market*: US listed-company counts roughly halved from their 1996 peak and firms stay private longer, so much value creation now happens before a company lists — locking public-only investors out.

**A3. Explain the illiquidity premium and why it can persist.**
It is the extra expected return demanded for assets that cannot be sold quickly: of two assets with identical cash flows and risk, the locked-up one must be cheaper — hence higher expected return. It persists because (a) few investors can bear illiquidity — retirees and banks with daily redemption needs cannot, so the buyer pool is small and the asset must offer more to clear; (b) it enforces discipline — a locked-up investor cannot panic-sell at the bottom; (c) sourcing private assets needs specialised skill that limits competition. Estimates run 1–5% a year, but much of it decomposes into leverage, small-cap tilt, and sector bets rather than pure illiquidity.

**A4. What is "volatility laundering" and why must an allocator de-smooth?**
Private assets are appraised periodically, not priced daily. Appraisals lag and smooth true values, so reported volatility and correlations come out artificially low — the illusion nicknamed volatility laundering. A fund reporting 6% volatility may have true volatility near listed REITs' 18%. Part of the diversification in the raw data is a measurement artifact, so a sophisticated allocator *de-smooths* the return series before trusting the optimisation inputs.

**A5. Describe the PE fund structure and the J-curve.**
PE is a closed-end limited partnership with a ~10-year life. The manager is the General Partner (GP); investors are Limited Partners (LPs). LPs *commit* capital up front, but it is *called* gradually as deals are found and *distributed* back as companies are sold — uncalled money is a commitment, not idle cash. The J-curve is the shape of cumulative returns: early fees and losers depress returns before winners mature, so returns dip below zero first and rise later.

**A6. Distinguish IRR, MOIC/TVPI, DPI, and PME.**
IRR is the annualised return on irregular cash flows. MOIC (TVPI) is total value — realised plus unrealised — divided by paid-in. DPI is *cash actually distributed* divided by paid-in, capturing only realised gains. PME compares the fund to putting identical cash flows into a public index; PME > 1 means it beat the market. The trap is trusting IRR alone: it assumes reinvestment at the IRR and can be flattered by early distributions or subscription-line financing, so pair it with MOIC and DPI.

**A7. Name the main hedge-fund strategy buckets and their primary return drivers.**
Long/Short Equity (stock-picking, reduced net exposure); Global Macro (directional rate/currency/commodity bets, often crisis-friendly); Event-Driven / Merger Arbitrage (deal completion); Relative Value / Fixed-Income Arbitrage (convergence of small pricing gaps, leveraged); Managed Futures / CTA (trend momentum, "crisis alpha"); Distressed (troubled-company debt). "Hedge fund" labels a structure and fee model, not a single strategy or risk level.

**A8. Why is infrastructure prized by pension funds?**
Infrastructure — toll roads, airports, utilities, grids, pipelines, towers, renewables — typically enjoys monopolistic positions, long-lived contracts, and regulated or inflation-linked revenues, producing stable cash flows: a bond-like income profile with equity-like inflation protection, ideal for matching long-dated, inflation-linked liabilities. Brownfield (operating) assets are lower-risk and income-focused; greenfield (build-from-scratch) carries construction and demand risk for higher return.

**A9. Decompose a commodity futures investor's total return and explain roll yield.**
Total return = spot + roll yield + collateral. Spot is the physical price change. Roll yield arises because a position must be rolled to a later contract before expiry: you gain in *backwardation* (near above far, roll into cheaper contracts) and lose in *contango* (far above near). Collateral is the risk-free rate on the margin cash. Persistent contango has quietly destroyed returns for long-only commodity investors — being right about the physical price is not enough.

**A10. What is the "denominator problem"?**
When public markets crash, illiquid alternatives — appraised and slow to reprice — become an oversized *share* of a shrunken portfolio, pushing the alternatives weight above policy with no new commitments. This can force selling public assets at the bottom to rebalance or fund spending and capital calls. Hence the binding constraint is the *liquidity budget*.

**A11. Summarise the endowment (Yale/Swensen) model and its core claim.**
Associated with David Swensen at Yale, it is the blueprint for heavy alternatives use: long-horizon investors with no near-term liabilities are *paid* to bear illiquidity and should tilt hard toward private assets. Yale ran 30%+ in private equity and real assets for decades. The caveat: it depends on genuinely top-quartile access, which most investors lack.

---

## Section B — Numerical Problems

**B1. Buyout return with the three value levers.** A PE fund buys a company at an enterprise value of $500m ($300m debt, $200m equity). EBITDA is $50m (10x entry). Over five years EBITDA grows to $75m, $150m of debt is repaid (to $150m), and it exits at 11x. Find exit equity value, MOIC, and gross IRR.

**Step 1 — Exit enterprise value.** $11 \times 75 = \mathbf{\$825m}$.
**Step 2 — Exit equity value.** $825 - 150\text{ (remaining debt)} = \mathbf{\$675m}$.
**Step 3 — MOIC.** $675 / 200 = \mathbf{3.375\times}$.
**Step 4 — Gross IRR.** $3.375^{1/5} - 1$. $\ln 3.375 = 1.2164$; $/5 = 0.24328$; $e^{0.24328}=1.2754$ → **27.5% per year (gross)**.

**Reconcile — strip out leverage.** All-equity: equity in $500m, exit EV $825m → MOIC 1.65x, IRR $=1.65^{1/5}-1=10.6\%$. Leverage roughly doubled the equity IRR (10.6% → 27.5%) — the gap is leverage, not skill, which is why critics call much PE "outperformance" repackaged leverage and equity beta.

**B2. Diversification benefit of adding a CTA.** A 100% equity portfolio has E(R)=8%, σ=16%. Shift to 80% equity / 20% managed futures (CTA: E(R)=6%, σ=12%, correlation −0.1 with equities). Risk-free 2%. Find the blend's E(R), σ, and compare Sharpe-like ratios.

**Expected return.** $0.8(8)+0.2(6)=6.4+1.2=\mathbf{7.6\%}$.
**Variance** (in %²): equity $0.8^2\cdot16^2=0.64\cdot256=163.84$; CTA $0.2^2\cdot12^2=0.04\cdot144=5.76$; cross $2(0.8)(0.2)(-0.1)(16)(12)=-6.144$. Sum $=163.456$ → $\sigma=\sqrt{163.456}=\mathbf{12.79\%}$.
**Sharpe-like ratios.** All-equity $(8-2)/16=\mathbf{0.375}$; blend $(7.6-2)/12.79=\mathbf{0.438}$.

**Reconcile.** We gave up 0.4 pp of return but cut volatility 16% → 12.8%; risk fell far more than return, so risk-adjusted return rose ~17% (0.375 → 0.438). The negative correlation did the work (cross term −6.14). The whole case for alternatives in one calculation: they need not out-earn equities, only diversify them.

**B3. Contango destroys a commodity gain.** An investor holds oil futures. Spot rises $70 → $75 over the year. The curve is in contango: each of 12 monthly rolls costs a $1.50 premium. Collateral earns 2% on the $70 notional. Estimate total return.

**Spot return.** $(75-70)/70=+7.14\%$ → in dollars on $70, +$5.00.
**Roll drag.** $12\times1.50=\mathbf{-\$18}$ (roughly, relative to spot).
**Collateral.** $2\%\times70=+\$1.40$.
**Net dollars.** $5.00-18.00+1.40=-\$11.60$ → about **−16.6%** on $70.

**Reconcile.** Despite a 7% rise in the physical price, the *investor's* futures position loses heavily once roll losses net out — even the 2% collateral leaves a clear loss. The shape of the futures curve can dominate the spot move, precisely why long-only commodity index products disappointed through the 2010s.

**B4. Capital calls and the J-curve.** An LP commits $10m. Calls: Y1 $3m, Y2 $3m, Y3 $2m ($8m called, $2m never drawn). Distributions: Y4 $4m, Y5 $9m. Year-5 residual NAV $1m. Compute paid-in, DPI, TVPI, and describe the cash-flow shape.

**Paid-in capital.** $3+3+2=\mathbf{\$8m}$ (the uncalled $2m is not paid-in).
**Total distributed.** $4+9=\mathbf{\$13m}$.
**DPI.** $13/8=\mathbf{1.625\times}$ (realised cash back per dollar in).
**TVPI.** $(13+1)/8=14/8=\mathbf{1.75\times}$ (adds the $1m residual NAV).

**Reconcile the J-curve.** Net LP cash flow: −3, −3, −2, +4, +9 — negative three years, then positive, tracing the J. TVPI (1.75x) exceeds DPI (1.625x) only by the unrealised residual; most value is already distributed — healthy versus a fund whose TVPI is mostly NAV.

**B5. Sizing to a liquidity budget (denominator problem).** A $100m portfolio holds $30m alternatives (appraised, flat) and $70m public equity. Public equity falls 40%. Find the new alternatives weight.

**After the crash.** Public equity $70m\times0.60=\$42m$; alternatives still $30m (appraised, unmoved). Total $=\$72m$. Alternatives weight $=30/72=\mathbf{41.7\%}$ — up from 30% with no new commitments. Restoring 30% means selling illiquid stakes (only at a discount, if at all) or accepting the drift.

**Reconcile.** The denominator problem in numbers: a 40% equity crash pushed alternatives from 30% to 41.7% purely through the shrinking denominator. Size illiquid commitments so this over-weighting never forces a bottom-of-market sale.

**B6. Fee drag over a fund's life.** A fund earns 15% gross annually over 5 years on $100, charging 2% of assets a year plus 20% carry on profit above cost (ignore hurdle; carry once at exit on net-of-management-fee profit). Estimate net MOIC and the fee share of gross gains.

**Gross.** $100\times1.15^5=\mathbf{\$201.14}$ → gross profit $101.14$.
**Management fee.** ~2% of $100 for 5 years $=\$10$.
**After mgmt fee.** $201.14-10=\$191.14$ → profit above cost $=\$91.14$.
**Carry.** $20\%\times91.14=\$18.23$. **Net to LP.** $191.14-18.23=\mathbf{\$172.91}$ → net MOIC $1.729\times$.
**Fee share of gross gains.** $(10+18.23)/101.14=\mathbf{27.9\%}$.

**Reconcile.** Even on a strong 15% gross return, ~28% of gross profit went to fees, dragging the LP's compound return from 15% gross to $1.729^{1/5}-1=11.6\%$ net — confirming the chapter's "a third or more of gross gains."

---

## Section C — Interview-Style Questions

**C1. "Why add alternatives at all if, after fees, average private equity has only matched public equity?"**
Model answer: Because the case was never that they out-earn equities. They add an *imperfectly correlated* return stream plus an illiquidity premium, improving *risk-adjusted* return and pushing the efficient frontier up and to the left. A CTA returning less than equities but negatively correlated can still raise the portfolio's Sharpe ratio — the 80/20 example where 0.4 pp of return bought a 3-point cut in volatility. But "average" hides everything: top-to-bottom-quartile dispersion runs 15–20 points a year, so buying the label without top-quartile access can underperform an index fund. The value is conditional on access and selection.

**C2. "A private real-estate fund reports 6% annual volatility and near-zero correlation with equities. Would you trust those numbers in your optimiser?"**
Model answer: No — not as reported. Private assets are appraised, not market-priced, so valuations lag and smooth true values, mechanically understating volatility and correlation — volatility laundering. A fund reporting 6% may have true volatility closer to listed REITs at 18%. Fed raw into a mean-variance optimiser it looks like a free lunch and gets massively over-allocated. So I de-smooth the appraisal series first — unsmoothing the return autocorrelation — then optimise. Treating the reported diversification as real is one of the most common and expensive mistakes in the field.

**C3. "Walk me through your due-diligence checklist for a first-time allocation to a buyout GP."**
Model answer: Five headings. *Track record* through multiple cycles with the same team, weighting realised DPI over paper TVPI. *Team stability and alignment*: is the GP investing personal money (skin in the game), and is there key-person risk? *Repeatable edge*: did returns come from a durable operational playbook or just leverage, multiple expansion, and a rising market — decompose a past deal. *Fees and terms*: management fee, carry, hurdle, high-water mark, clawback. *Operational due diligence*: independent administrator, auditor, custody, valuation policy — the Madoff lesson is that fraud hides in operations, not the thesis. And insist on vintage diversification so it is not one big timing bet.

**C4. "Commodities are up because oil is up — so a long commodity index should be winning, right?"**
Model answer: Not necessarily, because you earn the *futures* return, not spot. Total return is spot plus roll yield plus collateral. In contango — far contracts above near — every monthly roll sells a cheaper expiring contract and buys a dearer later one, bleeding roll yield. In the worked case, spot rose 7% but 12 rolls at a $1.50 premium produced a net loss even after collateral. So the right question is not "is oil rising?" but "what is the shape of the futures curve?"

**C5. "How would you size an alternatives allocation for a corporate pension versus a large endowment?"**
Model answer: The number flows from liquidity tolerance and governance capacity, not a target return. An endowment or sovereign fund — perpetual horizon, no near-term liabilities, strong access — can run 40–60%+, the Yale model. A pension has long liabilities but real liquidity needs (benefit payments) and governance limits, so 15–30% is typical. The binding constraint is the *liquidity budget*: never commit so much to illiquids that a crash makes you a forced seller at the bottom. I would stress-test the denominator problem — model a 40% equity drawdown and check capital calls and spending stay fundable. For the pension I would lean toward infrastructure and private credit, whose long, inflation-linked cash flows match the liabilities.

---

## Section D — Multiple Choice (with reasoning)

**D1. The illiquidity premium exists primarily because:**
(a) illiquid assets are always higher quality · (b) the pool of investors able to bear long lock-ups is small, so the asset must price cheaper to clear · (c) regulators mandate it · (d) illiquid assets have lower risk
**Answer: (b).** A small eligible buyer pool forces a lower price and higher expected return.

**D2. "Volatility laundering" refers to:**
(a) money laundering via hedge funds · (b) appraisal-based valuations smoothing returns so reported volatility and correlation look artificially low · (c) using derivatives to hide leverage · (d) tax evasion on carry
**Answer: (b).** Periodic appraisals lag true values, understating volatility and correlation — an artifact that must be de-smoothed.

**D3. A commodity futures investor in a persistently contangoed market will, all else equal:**
(a) earn the full spot return · (b) lose roll yield each time the position is rolled forward · (c) gain roll yield · (d) earn only the collateral return
**Answer: (b).** In contango the far contract is dearer, so rolling sells cheap and buys dear — a roll loss. Backwardation is the reverse.

**D4. Which metric captures only cash actually returned to LPs?**
(a) TVPI · (b) IRR · (c) DPI · (d) MOIC
**Answer: (c).** DPI = distributions ÷ paid-in, realised cash only. TVPI/MOIC include unrealised NAV; IRR can be flattered by early cash.

**D5. The J-curve in private equity describes:**
(a) rising then falling leverage · (b) cumulative returns that are negative early (fees and losers) and positive later (as winners mature) · (c) the shape of the futures curve · (d) fund size over time
**Answer: (b).** Early fees and write-downs depress returns before winners are realised.

**D6. Adding a low- or negatively-correlated alternative to an equity portfolio improves risk-adjusted return mainly because:**
(a) it always has higher expected return · (b) the variance cross-term stays small or negative, cutting portfolio volatility by more than it cuts return · (c) it eliminates all risk · (d) it removes fees
**Answer: (b).** Low ρ shrinks or negates the variance cross term, so volatility falls faster than return.

**D7. The "denominator problem" for an alternatives allocation means:**
(a) fees grow faster than returns · (b) when public markets crash, slow-to-reprice illiquid assets become an oversized share of a shrunken portfolio · (c) IRR is hard to compute · (d) carry is charged twice
**Answer: (b).** The public denominator shrinks in a crash, pushing the appraised illiquid weight above target.

**D8. "2 and 20" with a high-water mark means:**
(a) a flat 22% fee · (b) 2% of assets annually plus 20% of profits, with performance fees paid only on new gains above the prior peak · (c) 2% carry and 20% management · (d) fees only in profitable years
**Answer: (b).** The high-water mark charges carry only on profits above the previous high.

**D9. Much of private equity's historical "outperformance" is best explained by:**
(a) pure manager alpha only · (b) leverage, small-cap tilt, and sector bets, plus top-quartile selection · (c) low fees · (d) daily liquidity
**Answer: (b).** Decomposition shows leverage and beta do much of the work; repeatable alpha is concentrated in top-quartile GPs. (Listed REITs are the mirror caution — equity-like short-run despite giving property fundamentals long-run.)

---

### Self-check log
B1: MOIC 3.375x, IRR 27.5%; unlevered 10.6% → leverage ~doubles it ✓. B2: σ 12.79% (cross term −6.144); Sharpe 0.375 → 0.438 ✓. B3: net −$11.6 despite +7% spot ✓. B4: paid-in $8m, DPI 1.625x, TVPI 1.75x, cash flow −3/−3/−2/+4/+9 ✓. B5: 30/72 = 41.7% ✓. B6: net MOIC 1.729x, fees 27.9% of gross profit ✓.
