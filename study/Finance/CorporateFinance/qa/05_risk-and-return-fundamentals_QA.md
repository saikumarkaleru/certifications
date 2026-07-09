# Q&A — Risk & Return Fundamentals

A mixed bank of theory and numerical questions for equity research, credit, FP&A, and IB interviews. Numerical answers are fully worked and self-checked. For theory, each answer includes a model answer plus a crisp "say it like this" line.

---

## Theory

### Q1. Why do we use standard deviation to measure risk instead of just average deviation from the mean?

**Model answer.** Because plain deviations from the mean always sum to zero — the positive and negative deviations cancel by construction, so their average is useless. Squaring the deviations makes them all positive and also penalizes large misses more heavily than small ones, which matches how investors feel about big surprises. Averaging the squares gives *variance*; taking the square root gives *standard deviation*, which is back in the original units (%), so it's interpretable as "typical distance from the mean."

**Say it like this:** "Raw deviations cancel to zero, so we square them to get variance, then square-root to get a volatility number in the same units as returns."

---

### Q2. Explain systematic vs unsystematic risk and why only one is rewarded.

**Model answer.** Systematic (market) risk comes from macro forces — recessions, interest rates, inflation, geopolitics — that hit every company at once, so it can't be diversified away. Unsystematic (specific) risk comes from firm- or industry-level events — a lawsuit, a recall, a failed product — and washes out when you hold many names. Investors are only compensated for systematic risk, because unsystematic risk is something they can eliminate *for free* by diversifying; the market won't pay a premium for a risk you didn't have to bear.

**Say it like this:** "You only get paid for the risk you can't diversify away — that's the whole logic behind beta and CAPM."

---

### Q3. Why does diversification reduce risk — and what's its limit?

**Model answer.** Portfolio variance depends on the *covariance* between assets, not just their standalone variances. As long as assets aren't perfectly positively correlated ($\rho < 1$), their idiosyncratic surprises partially offset, so combined volatility falls below the weighted average of individual volatilities. The limit: in an equally weighted portfolio, as the number of assets grows, portfolio variance converges to the *average covariance* among the assets — the individual-variance term vanishes (that's unsystematic risk gone) but the shared covariance remains (that's systematic risk, the floor).

**Say it like this:** "Diversification cancels firm-specific risk because $\rho < 1$, but it bottoms out at the average covariance, which is market risk you can't escape."

---

### Q4. What is the efficient frontier, and how does adding a risk-free asset change the picture?

**Model answer.** The efficient frontier is the upper-left boundary of all achievable risky portfolios — each point gives the maximum expected return for its level of risk (or minimum risk for its return). Portfolios below it are dominated. Introduce a risk-free asset and you can draw a straight line from $R_f$ to any risky portfolio; the best such line is tangent to the frontier at the *market portfolio*. That tangent line is the Capital Market Line, and its slope is the market's Sharpe ratio. A key consequence — two-fund separation — is that every investor holds the *same* risky portfolio and just varies how much they mix it with cash.

**Say it like this:** "Efficient frontier is the best risky-only menu; add a risk-free asset and the best menu becomes a straight line — the CML — tangent at the market portfolio."

---

### Q5. CML vs SML — what's the difference?

**Model answer.** The Capital Market Line plots expected return against *total* risk (standard deviation), and only *efficient* portfolios lie on it — it's a portfolio-construction tool. The Security Market Line (from CAPM) plots expected return against *systematic* risk (beta), and *every* asset, efficient or not, lies on it in equilibrium — it's an asset-pricing tool. An inefficient stock sits *below* the CML but still *on* the SML.

**Say it like this:** "CML is return vs total risk for efficient portfolios; SML is return vs beta for every security."

---

### Q6. What does the Sharpe ratio measure, and what are its limitations?

**Model answer.** Sharpe ratio = (portfolio return − risk-free rate) / total volatility — excess return per unit of total risk, i.e., reward-to-risk. It lets you compare strategies with different risk levels on equal footing; higher is better. Limitations: (1) it uses total SD, so it penalizes *upside* volatility as if it were bad; (2) it assumes roughly normal returns, so it flatters strategies with fat tails or negative skew (e.g., selling options looks great until it blows up); (3) it's sensitive to the measurement period and can be gamed by smoothing returns. Sortino (downside deviation) and Treynor (beta) address parts of this.

**Say it like this:** "Excess return per unit of total risk — clean, but it treats good volatility as risk and assumes normal returns."

---

### Q7. Arithmetic vs geometric mean — which do you use for expected return?

**Model answer.** Arithmetic mean is the unbiased estimate of a *single future period's* expected return, so it's what you use as a forward-looking input (e.g., estimating an equity risk premium for one period ahead). Geometric mean is the *actually realized* compound annual growth over a multi-period history, so it describes past performance. Geometric is always ≤ arithmetic, and the gap is roughly half the variance — the "volatility drag" on compounded wealth.

**Say it like this:** "Arithmetic for next-period expectations, geometric for realized compounding — and geometric is always lower by about half the variance."

---

### Q8. A stock is very volatile on its own but you're told adding it *reduces* your portfolio's risk. How?

**Model answer.** What matters for portfolio risk isn't a stock's standalone volatility but its *covariance* with the rest of the portfolio. If the stock has low or negative correlation with your existing holdings, its marginal contribution to portfolio variance can be small or even negative — its bad periods tend to coincide with your good periods. Gold miners or certain defensives can behave this way relative to a cyclical book.

**Say it like this:** "Risk contribution is about covariance, not standalone vol — a volatile but uncorrelated asset can lower total portfolio risk."

---

### Q9. Why is the portfolio return a simple weighted average but portfolio risk isn't?

**Model answer.** Expectation is a linear operator, so the expected value of a weighted sum of returns is just the weighted sum of expected returns — correlations don't enter. Variance is a *quadratic* operator: the variance of a sum includes cross-covariance terms ($2w_Aw_B\text{Cov}(A,B)$), so how the assets move together directly changes the total. That non-linearity is exactly what creates the diversification benefit.

**Say it like this:** "Expectation is linear so returns just add up; variance is quadratic so covariance terms make risk sub-additive."

---

### Q10. How do you annualize a daily or monthly volatility?

**Model answer.** Under the assumption that returns are independent across periods, variance scales linearly with time, so standard deviation scales with the *square root* of time. Multiply the periodic SD by $\sqrt{k}$ where $k$ is periods per year: $\sqrt{252}$ for daily, $\sqrt{12}$ for monthly. Returns (means) scale linearly with $k$; volatility scales with $\sqrt{k}$.

**Say it like this:** "Square-root-of-time — daily vol times $\sqrt{252}$, monthly vol times $\sqrt{12}$."

---

## Numerical

### Q11. Expected return, variance, and SD from a probability distribution.

An asset returns +25% (prob 0.30), +8% (prob 0.45), and −12% (prob 0.25). Find $E[R]$, variance, and SD.

**Solution.**
$E[R] = 0.30(25) + 0.45(8) + 0.25(-12) = 7.5 + 3.6 - 3.0 = \mathbf{8.1\%}$

Squared deviations weighted:
- Boom: $(25-8.1)^2 = 16.9^2 = 285.61;\ \times0.30 = 85.683$
- Base: $(8-8.1)^2 = (-0.1)^2 = 0.01;\ \times0.45 = 0.0045$
- Bear: $(-12-8.1)^2 = (-20.1)^2 = 404.01;\ \times0.25 = 101.0025$

$\sigma^2 = 85.683 + 0.0045 + 101.0025 = 186.69\ (\%^2)$
$\sigma = \sqrt{186.69} = \mathbf{13.66\%}$

---

### Q12. Two-asset portfolio return and risk.

Stock A: $E[R]=16\%$, $\sigma=24\%$. Stock B: $E[R]=9\%$, $\sigma=12\%$. Correlation $\rho=0.25$. Weights 70% A / 30% B. Find portfolio return and SD.

**Solution.**
Return: $E[R_P] = 0.70(16) + 0.30(9) = 11.2 + 2.7 = \mathbf{12.9\%}$

Variance:
- $w_A^2\sigma_A^2 = 0.49\times576 = 282.24$
- $w_B^2\sigma_B^2 = 0.09\times144 = 12.96$
- $2w_Aw_B\rho\sigma_A\sigma_B = 2(0.7)(0.3)(0.25)(24)(12) = 0.42\times0.25\times288 = 0.105\times288 = 30.24$

$\sigma_P^2 = 282.24 + 12.96 + 30.24 = 325.44 \Rightarrow \sigma_P = \sqrt{325.44} = \mathbf{18.04\%}$

*Check:* weighted-average SD would be $0.7(24)+0.3(12) = 16.8+3.6 = 20.4\%$. Portfolio's 18.04% < 20.4%, confirming the diversification benefit.

---

### Q13. Same two stocks, three correlations — quantify diversification.

Using A ($\sigma=24$) and B ($\sigma=12$), weights 70/30, compute $\sigma_P$ for $\rho = +1, 0, -1$.

**Solution.** Fixed: $w_A^2\sigma_A^2 = 282.24$, $w_B^2\sigma_B^2 = 12.96$, cross-coefficient $2w_Aw_B\sigma_A\sigma_B = 0.42\times288 = 120.96$.

- $\rho=+1$: $\sigma_P^2 = 282.24+12.96+120.96 = 416.16 \Rightarrow \sigma_P = 20.40\%$ (= weighted avg, as expected)
- $\rho=0$: $\sigma_P^2 = 282.24+12.96+0 = 295.20 \Rightarrow \sigma_P = 17.18\%$
- $\rho=-1$: $\sigma_P^2 = 282.24+12.96-120.96 = 174.24 \Rightarrow \sigma_P = 13.20\%$

*Check at $\rho=-1$:* $|w_A\sigma_A - w_B\sigma_B| = |16.8-3.6| = 13.2\%$. Matches. Volatility falls from 20.4% to 13.2% as correlation drops — same return, less risk.

---

### Q14. Minimum-variance weight for two assets.

Assets A ($\sigma_A=20\%$) and B ($\sigma_B=10\%$), $\rho=0.3$. Find the weight in A that minimizes portfolio variance.

**Solution.** The minimum-variance weight is
$$w_A = \frac{\sigma_B^2 - \rho\sigma_A\sigma_B}{\sigma_A^2 + \sigma_B^2 - 2\rho\sigma_A\sigma_B}$$
Numerator: $100 - 0.3(20)(10) = 100 - 60 = 40$
Denominator: $400 + 100 - 2(0.3)(200) = 500 - 120 = 380$
$w_A = 40/380 = \mathbf{0.1053}$ (≈10.5% in A, 89.5% in B)

*Check the resulting risk:* with $w_A=0.1053, w_B=0.8947$:
- $w_A^2\sigma_A^2 = 0.01109\times400 = 4.436$
- $w_B^2\sigma_B^2 = 0.8005\times100 = 80.05$
- cross $= 2(0.1053)(0.8947)(0.3)(200) = 2(0.09421)(60) = 11.305$
$\sigma_P^2 = 4.436+80.05+11.305 = 95.79 \Rightarrow \sigma_P = 9.79\%$, which is below B's own 10% — the MVP sits left of both assets, as it should.

---

### Q15. Sharpe ratio comparison.

$R_f = 5\%$. Fund X: $E[R]=14\%$, $\sigma=16\%$. Fund Y: $E[R]=9\%$, $\sigma=7\%$. Which has the better risk-adjusted return?

**Solution.**
Sharpe X $= (14-5)/16 = 9/16 = \mathbf{0.5625}$
Sharpe Y $= (9-5)/7 = 4/7 = \mathbf{0.5714}$

**Fund Y wins** (0.571 > 0.563) despite lower raw return — it earns slightly more excess return per unit of risk. On a risk-adjusted basis, Y is the marginally better building block, though the two are very close.

---

### Q16. CML — required risk for a target return, with leverage.

$R_f=3\%$. Market portfolio $M$: $E[R_M]=11\%$, $\sigma_M=15\%$. An investor targets $E[R_P]=15\%$. How much risk, and what's the position?

**Solution.**
CML slope (market Sharpe) $= (11-3)/15 = 8/15 = 0.5333$.
$15 = 3 + 0.5333\,\sigma_P \Rightarrow \sigma_P = 12/0.5333 = \mathbf{22.5\%}$

Weight in market: $15 = 11w + 3(1-w) = 3 + 8w \Rightarrow w = 12/8 = 1.5$.
So **150% in the market, borrowing 50% at $R_f$** (levered). Check: $\sigma_P = 1.5\times15 = 22.5\%$. Consistent. Sharpe unchanged: $(15-3)/22.5 = 0.5333$ — leverage moves you along the CML, not above it.

---

### Q17. Three-asset portfolio variance.

Weights $(0.4, 0.4, 0.2)$; SDs $\sigma_1=18\%, \sigma_2=14\%, \sigma_3=8\%$; correlations $\rho_{12}=0.5, \rho_{13}=0.2, \rho_{23}=0.3$. Find $\sigma_P$.

**Solution.** Covariances $\sigma_{ij}=\rho_{ij}\sigma_i\sigma_j$:
- $\sigma_{12}=0.5(18)(14)=126$
- $\sigma_{13}=0.2(18)(8)=28.8$
- $\sigma_{23}=0.3(14)(8)=33.6$

Variance terms:
- $0.16\times324=51.84$
- $0.16\times196=31.36$
- $0.04\times64=2.56$
- Subtotal $=85.76$

Covariance terms ($2w_iw_j\sigma_{ij}$):
- $2(0.4)(0.4)(126)=40.32$
- $2(0.4)(0.2)(28.8)=4.608$
- $2(0.4)(0.2)(33.6)=5.376$
- Subtotal $=50.304$

$\sigma_P^2 = 85.76 + 50.304 = 136.06 \Rightarrow \sigma_P = \sqrt{136.06} = \mathbf{11.66\%}$

*Check:* weighted-avg SD $= 0.4(18)+0.4(14)+0.2(8) = 7.2+5.6+1.6 = 14.4\%$. Portfolio 11.66% < 14.4%. Good.

---

### Q18. Historical mean, sample SD, and geometric return.

Yearly returns: +22%, +6%, −8%, +14%, −4%, +10%. Find arithmetic mean, sample SD, and geometric mean.

**Solution.**
Arithmetic: $(22+6-8+14-4+10)/6 = 40/6 = \mathbf{6.667\%}$

Deviations from 6.667 and squares:
- $22-6.667=15.333;\ ^2=235.11$
- $6-6.667=-0.667;\ ^2=0.44$
- $-8-6.667=-14.667;\ ^2=215.12$
- $14-6.667=7.333;\ ^2=53.78$
- $-4-6.667=-10.667;\ ^2=113.78$
- $10-6.667=3.333;\ ^2=11.11$
- Sum $=629.34$

Sample variance $= 629.34/(6-1) = 125.87 \Rightarrow$ sample SD $= \sqrt{125.87} = \mathbf{11.22\%}$

Geometric: $(1.22)(1.06)(0.92)(1.14)(0.96)(1.10)$
$= 1.22\times1.06 = 1.2932;\ \times0.92 = 1.18974;\ \times1.14 = 1.35631;\ \times0.96 = 1.30206;\ \times1.10 = 1.43227$
$G = 1.43227^{1/6} - 1 = 1.06158 - 1 = \mathbf{6.16\%}$

Geometric (6.16%) < arithmetic (6.667%), gap ≈ 0.51%, close to $\tfrac12\sigma^2 = \tfrac12(0.1122)^2 = 0.63\%$. Consistent volatility drag.

---

### Q19. Covariance and correlation from scenarios.

Two assets across three equally likely states:

| State | A | B |
|---|---|---|
| 1 | +20% | +5% |
| 2 | +5% | +12% |
| 3 | −10% | +1% |

Find the covariance and correlation.

**Solution.**
Means: $\bar A = (20+5-10)/3 = 5\%$; $\bar B = (5+12+1)/3 = 6\%$.

Deviation products (each prob 1/3):
- State 1: $(20-5)(5-6) = 15\times(-1) = -15$
- State 2: $(5-5)(12-6) = 0\times6 = 0$
- State 3: $(-10-5)(1-6) = (-15)(-5) = 75$

$\text{Cov}(A,B) = \frac{1}{3}(-15+0+75) = 60/3 = \mathbf{20}$

SDs:
- $\sigma_A^2 = \frac{1}{3}[(15)^2+0^2+(-15)^2] = \frac{1}{3}(225+0+225) = 150 \Rightarrow \sigma_A = 12.25\%$
- $\sigma_B^2 = \frac{1}{3}[(-1)^2+6^2+(-5)^2] = \frac{1}{3}(1+36+25) = 20.67 \Rightarrow \sigma_B = 4.55\%$

$\rho_{AB} = \frac{20}{12.25\times4.55} = \frac{20}{55.71} = \mathbf{0.359}$

Positive but modest correlation — the two would diversify each other reasonably well.

---

### Q20. Perfect-hedge weights ($\rho = -1$).

Asset A: $\sigma_A=30\%$. Asset B: $\sigma_B=18\%$. $\rho=-1$. What weights make the portfolio riskless, and verify?

**Solution.** With $\rho=-1$, $\sigma_P = |w_A\sigma_A - w_B\sigma_B|$. Set to zero:
$w_A\sigma_A = w_B\sigma_B$ with $w_B = 1-w_A$:
$w_A(30) = (1-w_A)(18) \Rightarrow 30w_A = 18 - 18w_A \Rightarrow 48w_A = 18 \Rightarrow w_A = 0.375$
So $w_A = \mathbf{37.5\%}$, $w_B = 62.5\%$.

*Verify via the shortcut formula* $w_A = \sigma_B/(\sigma_A+\sigma_B) = 18/48 = 0.375$. Matches.
*Verify risk:* $|0.375(30) - 0.625(18)| = |11.25 - 11.25| = 0\%$. Riskless, as intended.

---

### Q21. Two-stock vol, the classic quick-fire.

Two stocks each have 30% volatility and correlation 0.5. What's the volatility of a 50/50 portfolio?

**Solution.**
$\sigma_P^2 = (0.5)^2(30)^2 + (0.5)^2(30)^2 + 2(0.5)(0.5)(0.5)(30)(30)$
$= 0.25(900) + 0.25(900) + 2(0.25)(0.5)(900)$
$= 225 + 225 + 225 = 675$
$\sigma_P = \sqrt{675} = \mathbf{25.98\%}$

Say it fast: "About 26% — below 30% because $\rho<1$." (Note: for two equal-vol equal-weight stocks, $\sigma_P = \sigma\sqrt{(1+\rho)/2} = 30\sqrt{0.75} = 25.98\%$ — a handy shortcut.)

---

### Q22. Coefficient of variation to rank on risk-per-return.

Project P: $E[R]=20\%$, $\sigma=15\%$. Project Q: $E[R]=8\%$, $\sigma=5\%$. Which is riskier per unit of expected return?

**Solution.**
$CV_P = 15/20 = 0.75$
$CV_Q = 5/8 = 0.625$

Project **P has the higher CV (0.75 vs 0.625)**, so it carries more risk per unit of expected return, even though Q has the lower absolute volatility. CV is the right lens when comparing assets with different mean returns — but note it ignores the risk-free rate, unlike the Sharpe ratio, so for capital-allocation decisions Sharpe is usually preferred.

---

### Q23. Volatility drag on compounding.

An investment returns +40% one year and −30% the next. What's the arithmetic mean, the actual compound (geometric) return, and the ending wealth on ₹100?

**Solution.**
Arithmetic $= (40 - 30)/2 = \mathbf{5\%}$
Ending wealth: $100\times1.40\times0.70 = 100\times0.98 = ₹98$ — you *lost* money.
Geometric $= (0.98)^{1/2} - 1 = 0.98995 - 1 = \mathbf{-1.005\%}$

The arithmetic mean says +5% but you actually ended below where you started. This is the volatility drag: a positive average return can coexist with a negative compounded outcome when volatility is high. Interview line: *"Averages don't compound — volatility eats geometric returns."*
