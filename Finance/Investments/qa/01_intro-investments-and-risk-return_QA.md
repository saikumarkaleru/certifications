# Q&A — Introduction to Investments and the Risk-Return Trade-off

A practice bank for Chapter 01. Every question is followed by a full answer. Formulas match the chapter; numerical answers are self-verified.

---

## Section A — Concept-Check Questions

**A1. State the classic (Reilly–Brown) definition of an investment and name the three things the future payments must compensate for.**

An investment is the current commitment of money (or other resources) for a period of time in the expectation of future payments that compensate the investor for (a) the *time* the funds are committed (time value), (b) the *expected inflation* over that time (purchasing-power protection), and (c) the *uncertainty* of the future payments (risk). The first two together form the nominal risk-free rate; the third is the risk premium.

**A2. Break the required return into its layers and identify which layer is "where the craft of investing lives".**

Required Return = Real risk-free rate + Inflation premium + Risk premium. The real risk-free rate compensates for pure time; the inflation premium protects purchasing power; together they equal the nominal risk-free rate (roughly a T-bill yield). The **risk premium** — compensation for uncertainty — is where the entire craft lives, because portfolio theory is fundamentally a debate about how big that premium should be and how it should be measured.

**A3. Why must expected reward scale with risk? Give the two-part economic argument.**

(1) *Risk aversion:* most investors, faced with two assets of equal expected return, prefer the less uncertain one — a consequence of the diminishing marginal utility of wealth (losing ₹1 lakh hurts more than gaining ₹1 lakh pleases). (2) *Market clearing:* if a risky and a safe asset offered the same expected return, risk-averse investors would dump the risky one; its price falls until its expected return rises enough to compensate holders. Prices adjust until every asset offers a premium proportional to its undiversifiable risk.

**A4. Distinguish systematic from unsystematic risk and state which one is rewarded, and why.**

Systematic (market) risk — recessions, rate shocks, wars — hits all assets at once and cannot be diversified away; it is **rewarded** with a premium. Unsystematic (specific) risk — a factory fire, a CEO scandal — is idiosyncratic and cancels out across a large portfolio; it earns **no** premium, because an investor could have eliminated it for free through diversification. The market never pays you for risk you could have avoided at no cost.

**A5. Why is diversification called "the only free lunch in finance"?**

Because combining many imperfectly-correlated assets removes unsystematic risk *without* reducing expected return. You lower total volatility for free — no return is sacrificed. It is a genuine improvement in the risk-return profile, unlike almost everything else in finance where more return demands more risk.

**A6. Distinguish investment, speculation, and gambling.**

Investment rests on fundamental analysis and intrinsic value over a medium-to-long horizon, taking calculated risk for a positive expected value (the risk premium). Speculation rests on timing/momentum/information edge over a short horizon; its expected value is positive only if the edge is real. Gambling rests on chance, has an instant horizon, and *manufactures* risk that need not exist, with a typically negative expected value (the house edge). Key nuance: investment and speculation deal with *pre-existing* economic risk; gambling creates risk purely for the wager.

**A7. State Benjamin Graham's test for distinguishing an investment from a speculation.**

"An investment operation is one which, upon thorough analysis, promises safety of principal and an adequate return. Operations not meeting these requirements are speculative." The two pillars are *thorough analysis* and *safety of principal plus adequate return*.

**A8. Is cash risk-free? Explain the subtlety.**

Only in *nominal* terms. In *real* terms cash reliably loses purchasing power to inflation, so its risk is subtle but real — inflation (purchasing-power) risk. Every asset trades one risk for another; cash minimises price volatility but maximises exposure to inflation erosion.

**A9. List the five steps of the investment management process and explain why it is a loop.**

(1) Set the investment policy (the IPS — objectives and constraints); (2) analyse securities and markets; (3) construct the portfolio (asset allocation, then selection); (4) evaluate performance (return, risk, attribution); (5) rebalance/revise. It is a continuous feedback loop because performance evaluation feeds back into policy revision — prices move, circumstances change, so the cycle returns to step 1.

**A10. What are the two objectives and the classic constraints in an IPS? Give the mnemonic.**

The two objectives are Return requirement and Risk tolerance (mnemonic R-R). The constraints are Liquidity, Legal/regulatory, Time horizon, Taxes, and Unique circumstances (mnemonic L-L-T-T-U).

**A11. Risk tolerance has two components. Name them and state the rule when they conflict.**

*Ability* (the financial capacity to absorb losses) and *Willingness* (psychological comfort with losses). When they conflict, the adviser generally respects the **lower** of the two, while educating the client. High net worth (high ability) does not imply high willingness.

**A12. What is human capital and how does it shape a young investor's asset mix?**

Human capital is the present value of future earnings. For a young person it is large and bond-like (a relatively safe stream of future salary). Because so much of her total wealth is already "safe", she can afford more equity risk in her financial portfolio. As human capital depletes with age, the financial portfolio should tilt toward bonds — the logic behind lifecycle/target-date funds.

**A13. Explain the difference between the arithmetic and geometric mean and when to use each.**

The arithmetic mean is the simple average of periodic returns; it is the best estimate of *next period's* return. The geometric mean is the compound growth rate — what your money actually did over the whole span. Geometric ≤ arithmetic always, with the gap widening as volatility rises ($\bar{R}_{geom} \approx \bar{R}_{arith} - \tfrac{1}{2}\sigma^2$). Use geometric to report realised past performance (compounded wealth); use arithmetic to forecast a single future period.

---

## Section B — Numerical Problems (Full Step-by-Step Solutions)

**B1. Holding Period Return and its decomposition.** You buy a share at ₹800. A year later it trades at ₹880 and paid a ₹24 dividend. Compute the HPR and split it into capital-gain yield and income yield.

*Solution.*
$$HPR = \frac{(P_1 - P_0) + D_1}{P_0} = \frac{(880 - 800) + 24}{800} = \frac{80 + 24}{800} = \frac{104}{800} = 0.13 = 13.0\%$$
Capital-gain yield = 80/800 = 10.0%; income yield = 24/800 = 3.0%.
*Reconciliation:* 10.0% + 3.0% = 13.0%. ✓

**B2. Expected return, variance, standard deviation, and CV under scenarios.** A stock's next-year return depends on the economy:

| State | Probability | Return |
|---|---|---|
| Boom | 0.30 | +25% |
| Normal | 0.50 | +10% |
| Recession | 0.20 | −15% |

Compute E(R), σ², σ, and the coefficient of variation.

*Solution.*
$$E(R) = 0.30(25) + 0.50(10) + 0.20(-15) = 7.5 + 5.0 - 3.0 = 9.5\%$$
Deviations from mean: Boom 25 − 9.5 = 15.5; Normal 10 − 9.5 = 0.5; Recession −15 − 9.5 = −24.5.
$$\sigma^2 = 0.30(15.5)^2 + 0.50(0.5)^2 + 0.20(-24.5)^2$$
$$= 0.30(240.25) + 0.50(0.25) + 0.20(600.25) = 72.075 + 0.125 + 120.05 = 192.25$$
$$\sigma = \sqrt{192.25} = 13.87\%$$
$$CV = \frac{\sigma}{E(R)} = \frac{13.87}{9.5} = 1.46$$
So the stock carries about 1.46 units of risk per unit of expected return.
*Reconciliation:* probabilities sum to 0.30 + 0.50 + 0.20 = 1.00. ✓ $\sqrt{192.25} = 13.87$ since $13.87^2 = 192.4$ (rounding). ✓

**B3. Comparing two funds with the Sharpe ratio.** The risk-free rate is 6%. Fund X returns 11% with σ = 10%; Fund Y returns 18% with σ = 22%. Which is more efficient?

*Solution.*
$$\text{Sharpe}_X = \frac{11 - 6}{10} = \frac{5}{10} = 0.50$$
$$\text{Sharpe}_Y = \frac{18 - 6}{22} = \frac{12}{22} = 0.545$$
Fund Y has the higher Sharpe ratio (0.545 > 0.50), so **Y** delivers more excess return per unit of total risk and is the more efficient engine.
*Reconciliation via leverage:* lever X up to Y's 22% volatility, a factor of 22/10 = 2.2. X's excess return scales to 2.2 × 5% = 11%, giving a total of 6% + 11% = 17% — *less* than Y's 18% at the same risk. This confirms Y dominates X here. ✓ (Which fund a given client holds still depends on risk tolerance; Y is merely the more efficient engine.)

**B4. Arithmetic vs geometric mean.** A fund returns +40% in year 1 and −30% in year 2. Compute both means and reconcile against actual wealth.

*Solution.*
$$\bar{R}_{arith} = \frac{40 + (-30)}{2} = \frac{10}{2} = +5\%$$
$$\bar{R}_{geom} = \sqrt{(1+0.40)(1-0.30)} - 1 = \sqrt{1.40 \times 0.70} - 1 = \sqrt{0.98} - 1 = 0.98995 - 1 = -1.01\%$$
*Reconciliation:* ₹100 → ₹140 (up 40%) → ₹140 × 0.70 = ₹98 (down 30%). Ending wealth ₹98 is a loss, so the true compound rate must be negative: $\sqrt{0.98} - 1 = -1.01\%$ per year. ✓ The arithmetic mean (+5%) overstates reality; the geometric mean (−1.01%) tells the truth about wealth. The gap arises because volatility is high.

**B5. Required return from its layers.** The real risk-free rate is 2%, expected inflation is 5%, and the equity risk premium for a stock is 6%. What nominal return should the investor require, using both the simple (additive) and the exact (multiplicative) Fisher approach for the risk-free portion?

*Solution.*
Simple/additive: Required return = 2% + 5% + 6% = **13%**.
Exact nominal risk-free rate via Fisher: $(1 + 0.02)(1 + 0.05) - 1 = 1.071 - 1 = 7.1\%$, then add the 6% premium → 7.1% + 6% = **13.1%**.
*Reconciliation:* the additive approximation (7% nominal risk-free) understates the exact figure (7.1%) by the cross-term 0.02 × 0.05 = 0.1%. The two agree to first order. ✓

**B6. Two-scenario probability weighting (breakeven check).** A ₹1,000 investment will be worth ₹1,300 with probability 0.6 or ₹700 with probability 0.4 in one year. Find the expected value, the expected return, and state whether it beats a 6% risk-free alternative.

*Solution.*
$$E(\text{Value}) = 0.6(1300) + 0.4(700) = 780 + 280 = ₹1{,}060$$
$$E(R) = \frac{1060 - 1000}{1000} = 6.0\%$$
The expected return equals the 6% risk-free rate exactly. Since this asset carries risk (outcomes range from −30% to +30%) yet offers *no* excess return over the risk-free rate, a risk-averse investor should **reject** it — it fails to pay a risk premium.
*Reconciliation:* probabilities 0.6 + 0.4 = 1.0. ✓ Expected value ₹1,060 → 6% return, matching the risk-free rate, so risk premium = 6% − 6% = 0. ✓

---

## Section C — Interview-Style Questions with Model Answers

**C1. "A fund returned 20% last year. Is that good?"**

Model answer: "I can't judge return without risk and a benchmark. Twenty percent is impressive if it came with low volatility and beat a relevant index; it's unremarkable if the fund took 35% volatility in a year the index itself rose 25%. Give me its standard deviation and the risk-free rate and I'll compute its Sharpe ratio — excess return per unit of risk — and compare it to its benchmark. The rule is: never judge a return without its risk, and never judge a risk without its horizon."

**C2. "Why is there a risk-return trade-off at all? Couldn't markets just misprice it away?"**

Model answer: "It survives because it's an equilibrium, not an accident. Investors are risk-averse due to diminishing marginal utility of wealth, so they demand extra expected return to hold riskier assets. If a risky asset ever offered the same expected return as a safe one, investors would sell it, its price would fall, and its expected return would rise until it again compensated for its risk. Crucially, only *undiversifiable* (systematic) risk is priced — diversifiable risk earns nothing because it can be removed for free. So mispricing gets arbitraged back toward a premium proportional to systematic risk."

**C3. "Walk me through building a portfolio for a 28-year-old software engineer versus a 62-year-old retiree."**

Model answer: "I'd start from objectives and constraints — the IPS. The 28-year-old has a long time horizon, large bond-like human capital, low near-term liquidity needs, and can absorb drawdowns, so her return objective is growth and her risk tolerance is high — an equity-heavy allocation. The retiree has a short-to-medium horizon, depleted human capital, high liquidity needs for living expenses, and low tolerance for losses he can't recover from, so his objective is income plus capital preservation — a bond-heavy, more conservative mix. The horizon and human capital do most of the work in setting the equity/bond split; taxes and any unique circumstances fine-tune it."

**C4. "Is speculation just a polite word for gambling?"**

Model answer: "No. Speculation analyses *pre-existing* economic risk — a company's fortunes, a commodity's supply — and can carry positive expected value if the speculator has a real edge; it also performs a genuine function by providing liquidity and bearing risk others avoid. Gambling *manufactures* risk that needn't exist purely for the wager, and typically has negative expected value because of the house edge. The line between investor and speculator is really a spectrum of holding period and analytical basis, not a moral one."

**C5. "You keep saying cash is risky. Explain that to a client who thinks cash is the safest thing they own."**

Model answer: "Cash is the safest in *nominal* terms — the number in the account won't fall. But in *real* terms it reliably loses. At 6% inflation, ₹100 today buys only about ₹94 of goods next year and ₹88 the year after. So cash quietly guarantees a loss of purchasing power. It minimises price volatility but maximises inflation risk. Every asset trades one risk for another; cash's trade is low volatility for guaranteed real erosion, which is exactly why we don't hold a retirement corpus entirely in cash."

**C6. "Should I report a fund's past performance using the arithmetic or the geometric mean?"**

Model answer: "Geometric, for reporting realised performance — it's the compound growth rate that reflects what actually happened to invested wealth, and it's always less than or equal to the arithmetic mean. The classic trap: +50% then −40% averages to +5% arithmetically but is actually −5.1% geometrically, because ₹100 becomes ₹90. Use the arithmetic mean only when you're forecasting a single future period's expected return, not when you're describing multi-period compounded results."

---

## Section D — Multiple-Choice Questions (with Reasoning)

**D1. The risk premium compensates an investor primarily for:**
(a) the time value of money  (b) expected inflation  (c) the uncertainty of future payments  (d) transaction costs

**Answer: (c).** Time value and inflation are captured by the real risk-free rate and the inflation premium respectively (together the nominal risk-free rate). The risk premium is the third, separate layer compensating for *uncertainty*. (a) and (b) are the other two layers; (d) is not a component of required return in this framework.

**D2. Which risk is rewarded with a premium in an efficient market?**
(a) unsystematic risk  (b) systematic risk  (c) total risk  (d) all risk equally

**Answer: (b).** Only systematic (undiversifiable, market-wide) risk earns a premium. Unsystematic risk (a) can be diversified away for free, so the market pays nothing for it. Total risk (c) includes the unrewarded unsystematic portion, so it is not the correct priced measure.

**D3. Two assets have equal standard deviation. Asset P has E(R) = 12%, Asset Q has E(R) = 9%. A risk-averse investor prefers:**
(a) Q, because lower return means lower risk  (b) P, because for equal risk it offers more return  (c) is indifferent  (d) cannot say without beta

**Answer: (b).** With equal risk (σ), the risk-averse investor prefers the higher expected return, so Asset P dominates. (a) confuses return with risk; risk here is already equal. Beta (d) isn't needed because total risk is explicitly stated equal and the question compares on that basis.

**D4. A fund earns 14% with σ = 16%; the risk-free rate is 6%. Its Sharpe ratio is:**
(a) 0.875  (b) 0.50  (c) 0.36  (d) 1.14

**Answer: (b).** Sharpe = (14 − 6)/16 = 8/16 = 0.50. (a) wrongly divides return by σ without subtracting Rf (14/16). (c) and (d) don't correspond to the correct excess-return-over-risk calculation.

**D5. The geometric mean return is:**
(a) always greater than the arithmetic mean  (b) equal to the arithmetic mean when volatility is zero  (c) the best estimate of next period's return  (d) unaffected by volatility

**Answer: (b).** When every period's return is identical (zero volatility), the two means coincide. Otherwise geometric < arithmetic, so (a) is false. (c) describes the arithmetic mean. (d) is false — the gap between the means widens with volatility ($\approx \tfrac{1}{2}\sigma^2$).

**D6. When ability and willingness to take risk conflict, the adviser should generally:**
(a) use ability, since it is objective  (b) use willingness, since the client is always right  (c) use the lower of the two  (d) average the two

**Answer: (c).** The prudent default is the lower of ability and willingness (while educating the client), so the plan doesn't exceed either the client's financial capacity or psychological comfort. Averaging (d) or picking one unconditionally (a, b) can leave the investor over-exposed relative to one dimension.

**D7. Which statement about diversification is correct?**
(a) it reduces expected return  (b) it eliminates all risk  (c) it reduces unsystematic risk without reducing expected return  (d) it reduces systematic risk

**Answer: (c).** Diversification removes idiosyncratic (unsystematic) risk while leaving expected return intact — the "free lunch." It does not touch systematic (market) risk (d, false) and does not reduce expected return (a, false); no strategy eliminates *all* risk (b, false).

**D8. An asset returns ₹1,200 with probability 0.5 and ₹800 with probability 0.5 on a ₹1,000 stake. Its expected return is:**
(a) 0%  (b) 10%  (c) 20%  (d) −10%

**Answer: (a).** E(Value) = 0.5(1200) + 0.5(800) = 600 + 400 = ₹1,000, so E(R) = (1000 − 1000)/1000 = 0%. The symmetric ±20% payoffs cancel. Since the asset carries real risk for zero expected excess return, a risk-averse investor would reject it.

---

*End of Q&A bank. Every formula matches Chapter 01; all numerical answers reconciled.*
