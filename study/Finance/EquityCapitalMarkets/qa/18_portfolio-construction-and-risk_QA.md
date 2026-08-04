# Q&A — Portfolio Construction & Risk

Theory and worked numerical problems on diversification, risk decomposition, and risk-adjusted performance.

---

### Q1. Worked — two-asset portfolio volatility.
*Stock A: 25% volatility. Stock B: 18% volatility. Correlation between A and B: 0.2. Portfolio is 60% A, 40% B.*

**Model answer.**
```
σp² = w_A² σ_A² + w_B² σ_B² + 2 w_A w_B ρ σ_A σ_B
    = 0.6² × 0.25² + 0.4² × 0.18² + 2 × 0.6 × 0.4 × 0.2 × 0.25 × 0.18
    = 0.36 × 0.0625 + 0.16 × 0.0324 + 0.48 × 0.2 × 0.045
    = 0.0225 + 0.005184 + 0.00432
    = 0.032004
σp = √0.032004 ≈ 17.89%
```
The portfolio's volatility (≈17.9%) is below the simple weighted-average volatility of the two holdings (0.6×25 + 0.4×18 = 22.2%) — the gap between 22.2% and 17.9% is the diversification benefit, arising directly from the correlation being well below 1.

---

### Q2. Why can't systematic risk be diversified away, no matter how many additional uncorrelated stocks are added to a portfolio?

**Model answer.** Systematic risk represents exposure to broad market/economic factors (interest rates, GDP growth, systemic shocks) that affect essentially all stocks simultaneously to some degree — since virtually every stock has some positive correlation to the overall market, adding more holdings can eliminate the *company-specific* (unsystematic) portion of risk that's genuinely uncorrelated across names, but it cannot eliminate the shared, market-wide component that every stock carries. This is precisely why systematic risk (measured by beta) is the risk that's compensated with a risk premium — it's the risk investors are stuck bearing collectively no matter how they diversify within the equity asset class.

---

### Q3. Worked — Sharpe ratio decision.
*Fund X: 22% return, 18% volatility. Fund Y: 16% return, 9% volatility. Risk-free rate: 6%.*

**Model answer.**
```
Sharpe X = (22 − 6) / 18 = 16/18 ≈ 0.89
Sharpe Y = (16 − 6) / 9 = 10/9 ≈ 1.11
```
Fund Y has the higher Sharpe ratio despite the lower raw return — it delivers more excess return per unit of total risk taken. An investor could, in principle, lever Fund Y (e.g. via borrowing) to match Fund X's volatility level and would expect to end up with a higher return than Fund X at that same risk level, which is the practical implication of comparing Sharpe ratios rather than raw returns alone.

---

### Q4. Distinguish alpha from beta with a worked numerical example, and explain why conflating the two is a serious analytical error.
*A fund returns 19% in a year when the market returned 10%, risk-free rate is 5%, and the fund's beta is 1.5.*

**Model answer.**
```
CAPM-expected return = Rf + β(Rm − Rf) = 5% + 1.5 × (10% − 5%) = 5% + 7.5% = 12.5%
Alpha = Actual return − CAPM-expected return = 19% − 12.5% = +6.5%
```
The fund's 19% return looks impressive, but 12.5 percentage points of it are simply explained by taking on 1.5x the market's systematic risk (beta exposure) — anyone could have replicated most of that 19% by leveraging a passive index fund to a 1.5 beta, at much lower fees. Only the 6.5% alpha represents genuine skill (return not explained by market exposure). Conflating a high raw return achieved mostly through high beta with genuine investment skill is a serious error — it leads to overpaying active-management fees for what is, economically, just leveraged market exposure available far more cheaply.

---

### Q5. When would an analyst use the Treynor ratio instead of the Sharpe ratio to evaluate a fund's risk-adjusted performance, and why does the choice matter?

**Model answer.** Sharpe ratio uses total risk (standard deviation, σ), making it the right choice when evaluating a portfolio as a standalone investment (all of an investor's risk exposure). Treynor ratio uses only systematic risk (beta), making it the right choice when evaluating a portfolio as *one component* of a broader, diversified overall portfolio — since in that context, the fund's unsystematic/idiosyncratic risk may already be diversified away by the investor's other holdings, and what matters is how efficiently the fund generates excess return per unit of the market risk it does contribute. Using Sharpe when Treynor is appropriate (or vice versa) can lead to incorrectly favouring a fund with low idiosyncratic risk but poor systematic-risk-adjusted returns, or the reverse.

---

### Q6. Worked — information ratio and what it signals about consistency.
*Fund A: active return (vs benchmark) averaging 4% annually, with a tracking error of 8%. Fund B: active return averaging 2.5% annually, with a tracking error of 2%.*

**Model answer.**
```
IR_A = 4 / 8 = 0.50
IR_B = 2.5 / 2 = 1.25
```
Despite Fund A's higher average active return (4% vs 2.5%), Fund B has the much higher information ratio — its outperformance is far more *consistent* relative to how much it deviates from the benchmark. Fund A's higher average return comes with much more volatile/inconsistent relative performance (a high tracking error), meaning an investor experiences a bumpier ride of over- and under-performance to earn that average, whereas Fund B delivers steadier, more reliable outperformance per unit of active risk taken — a meaningfully different (and often more prized by institutional allocators) quality than Fund A's higher but less consistent alpha.

---

### Q7. What's the trade-off in choosing a concentrated, high-conviction portfolio (e.g. 15-20 positions) versus a broadly diversified one (e.g. 100+ positions)?

**Model answer.** A concentrated portfolio allows each position to genuinely reflect the manager's highest-conviction ideas and lets real skill (analytical edge) show up meaningfully in returns if the manager's calls are good — but it also carries more idiosyncratic risk per position, since fewer holdings mean any single stock-specific negative surprise has a larger portfolio-level impact, and the overall portfolio's realised volatility can deviate more sharply from the benchmark. A broadly diversified portfolio diversifies away most idiosyncratic risk (per the diversification math in Q1-Q2), producing smoother, more benchmark-like returns — but if a manager is genuinely skilled at stock selection, over-diversifying dilutes that skill's impact toward benchmark-like ("closet indexing") returns while still charging active-management fees, itself a well-known problem the chapter flags.

---

### Q8. Why does rebalancing a portfolio back to target weights function as a disciplined "sell high, buy low" mechanism, even without any explicit market-timing view?

**Model answer.** As asset prices move, a position that has appreciated becomes an overweight relative to its original target allocation, and a position that has declined becomes an underweight. Rebalancing back to target weights mechanically requires trimming the now-overweight (appreciated, "expensive" relative to target) position and adding to the now-underweight (declined, "cheap" relative to target) position — enforcing a disciplined sell-high/buy-low pattern purely through the rebalancing rule itself, without requiring the manager to have any specific forecasting view on which asset will outperform next. This also controls risk by preventing any single position's appreciation from silently growing the portfolio's concentration and risk profile beyond its intended target.
