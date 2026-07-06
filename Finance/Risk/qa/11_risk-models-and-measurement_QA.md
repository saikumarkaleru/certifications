# Q&A — Risk Models and Measurement

Practice bank for Chapter 11. Every question is followed by a full answer. Constants used throughout: Normal quantiles $z_{0.99}=2.326$, $z_{0.975}=1.960$, $z_{0.95}=1.645$; $\phi(2.326)=0.0267$, $\phi(1.960)=0.0584$; $\chi^2_1$ critical values 3.84 (5%) and 6.63 (1%).

---

## Section A — Concept Check

**A1. A risk model has three separable layers. Name them and say what "lives" in each.**

(1) **Marginal distributions** — the distribution of each individual risk factor; this is where *fat tails* live. (2) **Dependence structure** — how the factors co-move; this is where *correlation, copulas, and tail dependence* live. (3) **Aggregation and measurement** — combining layers 1 and 2 into a portfolio loss distribution and reading off a measure like VaR or ES; this is where *simulation and scenario analysis* live. Each layer can fail independently, so a model can get the marginals right and the dependence catastrophically wrong.

**A2. What single conceptual result lets us model the marginals and the dependence separately, and why is that both liberating and dangerous?**

**Sklar's theorem**: any joint distribution $F(x_1,\dots,x_n)=C\big(F_1(x_1),\dots,F_n(x_n)\big)$, where the $F_i$ are marginals and $C$ is a copula carrying *all* the dependence. It is *liberating* because you can fix fat tails without touching correlations and vice versa. It is *dangerous* because you can glue fat-tailed marginals onto a benign, no-joint-extremes dependence structure and fool yourself into thinking the model is conservative when it is structurally blind to joint crashes.

**A3. Why is the tail — not the mean or standard deviation — "the whole game" in risk modelling?**

Risk measures (VaR, ES) read the far left of the loss distribution: the 1% or 0.1% worst outcomes. The centre, where returns spend most of their time, almost never bankrupts anyone. So modelling effort is *asymmetric*: getting the tail shape right matters far more than fitting the body. A model can fit 99% of the data beautifully and still be worthless because it misprices the 1% that matters.

**A4. Why does the Normal distribution keep getting used even though returns are not Normal?**

Analytical convenience: it has one scale parameter (σ), it is closed under linear combinations (a portfolio of jointly-Normal assets is Normal, giving VaR a clean closed form), and correlation *fully* describes its dependence. But real returns are **leptokurtic** (excess kurtosis > 0 — fat-tailed, sharp-peaked) and show **volatility clustering** (calm and stormy periods bunch, so returns are not i.i.d. over time). Observed "5-sigma" days occur orders of magnitude more often than a Normal permits.

**A5. VaR is "not coherent." Which axiom does it violate, and what fixes it?**

VaR can violate **sub-additivity** — a portfolio's VaR can exceed the sum of its parts' VaRs, i.e. it can *penalise diversification*, which is incoherent. **Expected Shortfall (ES)**, the average loss in the worst $(1-\alpha)$ tail, is sub-additive (coherent) and tail-sensitive; it also captures how bad losses are *beyond* the quantile, which VaR ignores. Basel's FRTB replaced 99% VaR with **97.5% ES** for exactly these reasons.

**A6. "A higher correlation input will fix my model's tail risk." True or false, and why?**

**False** — if the model uses a **Gaussian copula**. The Gaussian copula has **zero tail dependence** at any correlation below 1: the probability of joint extreme losses vanishes in the tail no matter how high ρ is. To represent "everything crashes together" you must change the *copula family* (to Student-t or Clayton), not just raise the correlation number. This is the structural flaw behind the Gaussian-copula CDO failures.

**A7. Why is historical simulation not truly "assumption-free"?**

It drops the Normality assumption but replaces it with an equally strong one: **the chosen historical window represents the future.** It cannot produce any scenario worse than the worst day in its window, it weights stale data equally with fresh data, and a single crash in the window can dominate the tail. The assumption moved from "the distribution is Normal" to "the past repeats" — it did not disappear. This is why it must be complemented with stress testing.

**A8. Distinguish the three ways to build a portfolio loss distribution in one line each.**

(a) **Parametric/variance–covariance**: assume factors jointly Normal, compute $\sigma_P=\sqrt{w^\top\Sigma w}$, read $\text{VaR}=z_\alpha\sigma_P V$ — fast but wrong for options and fat tails. (b) **Historical simulation**: apply the last $N$ days of actual factor moves to today's book and read the empirical quantile — captures real fat tails and dependence but bounded by history. (c) **Monte Carlo**: specify marginals + copula, draw $M$ scenarios, fully revalue — handles non-linearity and arbitrary dependence but is costly and only as good as the assumed model.

**A9. What does reverse stress testing ask that ordinary stress testing does not?**

Ordinary stress testing asks "what do we lose in *this specific bad scenario*?" Reverse stress testing inverts it: "**what scenario would render us insolvent?**" — you solve for the state of the world that breaks the firm, then assess how plausible it is. It is valuable precisely because it surfaces vulnerabilities that the analyst would never have thought to test for directly.

**A10. Why does a backtest failure directly cost a bank money?**

Under Basel's Internal Models Approach, the market-risk capital charge is scaled by a multiplier $k$ tied to the number of VaR exceptions over 250 days. **Green zone** (0–4 breaches) gives $k=3.0$; **Red zone** (10+) gives $k=4.0$. A model that breaches too often is pushed toward higher $k$, mechanically raising required capital by up to a third. So model quality *is* capital — backtesting is not academic.

---

## Section B — Numerical / Applied (with full solutions)

**B1. Normal VaR and the ES calibration check.** A trading book worth **V = $50m** has daily σ = 2%, mean ≈ 0. Find (a) the 99% one-day VaR, (b) the 97.5% one-day ES, and confirm Basel's calibration claim that 97.5% ES ≈ 99% VaR under Normality.

Solution.
(a) $\text{VaR}_{99\%}=z_{0.99}\,\sigma V = 2.326\times0.02\times50\text{m}=2.326\times1\text{m}=\mathbf{\$2.326m}$.
(b) Normal ES: $\text{ES}_\alpha=\sigma\,\dfrac{\phi(z_\alpha)}{1-\alpha}V$. At α = 0.975, $\phi(1.960)=0.0584$:
$$\text{ES}_{97.5\%}=0.02\times\frac{0.0584}{0.025}\times50\text{m}=0.02\times2.338\times50\text{m}=\mathbf{\$2.338m}.$$
Check: $2.338m \approx 2.326m$ — within 0.5%. ✓ Basel calibrated 97.5% ES to sit right on top of 99% VaR *for Normal returns*; the two diverge only once tails fatten (see B2).

**B2. Fat-tailed VaR with a Student-t.** Same book (V = $50m, σ = 2%). Daily returns are better described by a Student-t with **ν = 6** degrees of freedom. The one-tailed 99% t-quantile is $t_{0.99,6}=3.143$. Find the fat-tailed 99% VaR and compare with the Normal result.

Solution. The raw t must be **scaled so its variance equals σ²**. A t with ν d.f. has variance $\frac{\nu}{\nu-2}$, so the scale factor is $\sqrt{\frac{\nu-2}{\nu}}=\sqrt{4/6}=\sqrt{0.6667}=0.8165$. Effective 99% multiplier $=3.143\times0.8165=2.566$.
$$\text{VaR}_{99\%}^{t}=2.566\times0.02\times50\text{m}=\mathbf{\$2.566m}.$$
Comparison: $2.566m$ vs the Normal $2.326m$ — about **10% more capital** at the *same* volatility and confidence. Both models agree on σ = 2%; the Normal is wrong only about *tail shape*, and the entire $0.24m gap lives in the 1% tail. That gap is the price of honestly representing fat tails.

**B3. Matching kurtosis to degrees of freedom.** Empirically, this desk's daily returns show **excess kurtosis of 3** (i.e. kurtosis = 6). Using the Student-t kurtosis formula, what ν reproduces this?

Solution. For ν > 4, t-kurtosis $=3+\dfrac{6}{\nu-4}$. Set equal to 6:
$$3+\frac{6}{\nu-4}=6 \;\Rightarrow\; \frac{6}{\nu-4}=3 \;\Rightarrow\; \nu-4=2 \;\Rightarrow\; \boxed{\nu=6}.$$
Interpretation: the same ν = 6 used in B2 is not arbitrary — it is pinned by the observed tail heaviness. Lower ν = fatter tails; as ν → ∞ the t collapses to the Normal (excess kurtosis → 0).

**B4. Historical-simulation VaR and ES as order statistics.** A desk has **500 days** of P&L. The six worst daily P&Ls (in $m) are: **−9.2, −7.4, −6.1, −5.5, −4.9, −4.3**. Find the 99% VaR and 99% ES, and comment on the tail.

Solution. The 99% VaR is the loss at the $(1-0.99)\times500 = 5\text{th}$ worst outcome.
- **99% VaR** = 5th-worst loss = **$4.9m** (the least-bad of the worst 1%).
- **99% ES** = average of the losses *at least as bad as VaR*, i.e. the worst 5:
$$\text{ES}_{99\%}=\frac{9.2+7.4+6.1+5.5+4.9}{5}=\frac{33.1}{5}=\mathbf{\$6.62m}.$$
Comment: ES ($6.62m) > VaR ($4.9m) always, because ES averages the tail VaR merely bounds. The ratio 6.62/4.9 = **1.35**, well above the ≈1.15 you would get under Normality — a quantitative fingerprint that this empirical tail is **fatter than Normal**, obtained with no distributional assumption. (Note the 6th-worst value, −4.3, is irrelevant to a 99% measure on 500 days; only the worst 5 enter.)

**B5. Kupiec proportion-of-failures backtest.** A 99% one-day VaR model produced **8 exceptions in T = 250 days**. Test it with Kupiec's unconditional-coverage statistic and reconcile with Basel's traffic light.

Solution. Expected exceptions $=0.01\times250=2.5$; observed $\hat p=8/250=0.032$. With $p=0.01$:
$$LR_{uc}=-2\ln\!\left[\frac{(0.99)^{242}(0.01)^{8}}{(0.968)^{242}(0.032)^{8}}\right].$$
Log-likelihoods:
- Under $p=0.01$: $242\ln(0.99)+8\ln(0.01)=242(-0.010050)+8(-4.60517)=-2.432-36.841=-39.273$.
- Under $\hat p=0.032$: $242\ln(0.968)+8\ln(0.032)=242(-0.032520)+8(-3.44202)=-7.870-27.536=-35.406$.
$$LR_{uc}=-2\big(-39.273-(-35.406)\big)=-2(-3.867)=\mathbf{7.73}.$$
Decision: $7.73 > 6.63$, so we **reject the model at the 1% level** ($\chi^2_1$). But Basel's traffic light puts 8 exceptions in the **Yellow zone** (5–9), meaning *increased scrutiny and a scaled multiplier* rather than outright rejection. The lesson: the pure statistical test and the supervisory rule can disagree at the margin — Kupiec says "reject," Basel says "watch closely and add capital." Both agree the model is under strain.

**B6. Basel capital impact.** Continue B5. Suppose the bank's 10-day 99% VaR is **$40m** and, before any add-ons, capital = $k \times$ VaR. Compare the charge in the Green zone ($k=3.0$) with a Red-zone outcome ($k=4.0$).

Solution.
- Green: $3.0\times40\text{m}=\$120\text{m}$.
- Red: $4.0\times40\text{m}=\$160\text{m}$.
Difference = **$40m of extra capital (+33%)** purely because the model breached too often. This is the concrete mechanism by which "model quality is capital": the same VaR number attracts a one-third larger charge when backtesting fails.

**B7. Gaussian copula rank correlation.** Two factors are joined by a Gaussian copula with linear correlation **ρ = 0.7**. Compute Kendall's τ using $\tau=\frac{2}{\pi}\arcsin(\rho)$, and state the tail dependence.

Solution. $\arcsin(0.7)=0.7754$ rad. $\tau=\frac{2}{\pi}(0.7754)=0.6366\times0.7754=\mathbf{0.494}.$
So a strong linear correlation of 0.7 corresponds to a rank concordance of ~0.49. Crucially, the **lower tail dependence $\lambda_L=0$** for the Gaussian copula at any ρ < 1: despite ρ = 0.7 and τ = 0.49, the model assigns *vanishing* probability to joint extreme losses. Swapping to a Student-t copula (same ρ, finite ν) would give $\lambda_L>0$ and restore joint-crash risk — the number that matters for a credit portfolio.

---

## Section C — Interview-Style (with model answers)

**C1. "Walk me through why risk models failed in 2008."**

Model answer: It was a failure of every layer at once. **Marginals** were thin-tailed (Normal), so extreme moves were treated as near-impossible. **Dependence** used the Gaussian copula, which has *zero tail dependence* and structurally cannot represent correlated defaults. **Calibration** was backward-looking on a benign window, so the models had never "seen" a crisis. Then two feedback effects amplified it: **procyclicality** (low measured risk justified high leverage) and **endogeneity** (everyone used the same models, hit limits together, and was forced into correlated selling — the models *created* the correlation they later measured). And wrapping it all, a **governance** failure: no effective challenge to the assumptions. The lesson is that fat tails and tail dependence are not refinements — they are the phenomenon.

**C2. "A trader says his desk's VaR is $2m, so that's the most he can lose in a day. Correct him."**

Model answer: That is the single most common VaR error. VaR is a **quantile, not a maximum**. "99% VaR of $2m" means that on the worst 1% of days he loses *at least* $2m — the loss beyond that threshold is unbounded and is exactly what VaR is silent about. To know how bad it gets when the threshold breaks, use **Expected Shortfall** — the average of the tail beyond VaR, always larger. VaR tells you the door; ES tells you what's behind it. And both assume normal markets, so neither covers a gap or liquidity hole — that's what stress testing is for.

**C3. "You have three VaR methods. How do you choose?"**

Model answer: I choose by the two questions that actually differentiate them. First, *is the book linear and are the factors close to Normal?* If yes, **parametric variance–covariance** is fast and adequate. If the book has options or the factors are fat-tailed, parametric breaks, so I move on. Second, *do I trust my historical window to represent the future?* If the window is rich and relevant, **historical simulation** gives me real fat tails and real dependence with no distributional assumption. If I distrust the window — because it's too calm, too short, or the world has changed — I use **Monte Carlo** with explicitly chosen marginals and a copula, which lets me inject fat tails and tail dependence deliberately. Whichever I pick, I *always* complement it with stress and reverse-stress tests, because those probe the tail without relying on the very assumptions that fail in the tail.

**C4. "Sell me on Expected Shortfall over VaR — then tell me its catch."**

Model answer: ES wins on two counts. It is **coherent** — specifically sub-additive — so it never penalises diversification, whereas VaR can. And it is **tail-sensitive**: it averages the whole tail rather than reading a single point, so it responds to *how* fat the tail is, not just where the quantile sits. That's why FRTB moved to 97.5% ES. The catch is **backtesting**: ES is not "elicitable" in the simple way a quantile is, so it's harder to validate against realised outcomes. In practice regulators police an ES-based charge using VaR-based backtesting — an accepted awkwardness. So ES is the better *measure* but the harder thing to *check*, and a mature framework holds both facts at once.

**C5. "How does your model risk governance actually stop a bad model from shipping?"**

Model answer: Through the three lines of defence and the doctrine of **effective challenge** from SR 11-7. The **first line** — developers and model owners — build the model and self-test it. The **second line** — independent validation and risk — must be competent, empowered, and separate enough to say *no*: they check conceptual soundness (is the theory and math right?), run ongoing monitoring (backtesting, benchmarking against alternatives, sensitivity analysis), and do outcomes analysis. The **third line** — internal audit — assures the board that the process itself works. The point of effective challenge is that a validator who is junior, captured, or under-resourced is worthless; the person questioning the model must genuinely be able to block it. Everything sits on a model inventory tiered by materiality, with documented assumptions and limitations. Governance answers a different question from the math: the math says what the risk *is if the model is right*; governance says *whether to believe the model at all*.

---

## Section D — MCQs (with reasoning)

**D1. The Gaussian copula's defining weakness for credit risk is that it has:**
(a) negative correlation; (b) zero tail dependence; (c) infinite variance; (d) non-uniform marginals.

**Answer: (b).** Its lower tail dependence $\lambda_L=0$ for any ρ < 1, so it cannot represent joint extreme losses ("everyone defaults together") regardless of the correlation input. (d) is definitionally wrong — every copula has uniform marginals. (a) and (c) are unrelated to the copula's tail behaviour.

**D2. Under Normal returns, which pairing is calibrated to give roughly equal risk numbers?**
(a) 99% VaR and 99% ES; (b) 95% VaR and 99% ES; (c) 99% VaR and 97.5% ES; (d) 97.5% VaR and 99% ES.

**Answer: (c).** As shown in B1, 97.5% ES ≈ 99% VaR under Normality — the basis for FRTB's switch. (a) is wrong because ES > VaR at the *same* confidence always. (b) and (d) mismatch the calibration levels.

**D3. A Student-t distribution with ν = 5 compared with the Normal has:**
(a) thinner tails and lower VaR; (b) fatter tails and higher VaR; (c) identical tails; (d) fatter tails but lower VaR.

**Answer: (b).** Lower ν means fatter tails (kurtosis $=3+\frac{6}{\nu-4}=9$ at ν = 5, vs 3 for Normal), pushing the tail quantile — and hence VaR — higher once variance is matched. (d) is internally contradictory; (a) and (c) reverse or deny the fat-tail fact.

**D4. Historical simulation VaR cannot produce a loss worse than:**
(a) the mean loss; (b) the parametric VaR; (c) the worst observation in its window; (d) the ES.

**Answer: (c).** It replays actual past moves, so its maximum possible loss is the worst day in the sample window — the core limitation that makes stress testing necessary. The other options are unrelated bounds.

**D5. A 99% one-day VaR model shows 12 exceptions in 250 days. Basel places this in the:**
(a) Green zone, $k=3.0$; (b) Yellow zone; (c) Red zone, $k=4.0$; (d) unclassified.

**Answer: (c).** 10 or more exceptions is the Red zone (model rejected/overhaul), multiplier $k=4.0$. Green is 0–4, Yellow is 5–9. Expected breaches for a true model are only ~2.5, so 12 is a decisive failure.

**D6. Kendall's τ and Spearman's ρ are preferred over Pearson correlation because they:**
(a) are always larger; (b) depend only on the copula and survive non-linear transforms; (c) require Normality; (d) measure only linear dependence.

**Answer: (b).** Rank correlations depend on the ranks (the copula), not the marginals, so they survive monotone non-linear transforms and don't assume Normality. (d) describes Pearson correlation; (c) is false and (a) is not generally true.

**D7. In Monte Carlo risk estimation, increasing the number of paths reduces:**
(a) model error; (b) simulation (sampling) error only; (c) both equally; (d) neither.

**Answer: (b).** More paths shrink *sampling* error but do nothing to *model* error — a billion paths of the wrong marginals/copula is "precisely wrong." Choosing the model right is a separate problem from running it long enough.

**D8. Extreme Value Theory's key advantage over historical simulation is that it can:**
(a) avoid all assumptions; (b) estimate quantiles beyond the range of observed data; (c) eliminate model risk; (d) guarantee sub-additivity.

**Answer: (b).** Fitting a Generalised Pareto Distribution to exceedances over a high threshold lets EVT extrapolate a principled tail *beyond* the worst observed loss — what historical simulation cannot do. It still carries assumptions and model risk, so (a) and (c) overclaim; (d) confuses EVT with the coherence of ES.

---

