# Q&A — Model Risk

Practice bank for the Model Risk chapter. Every question is followed by a full answer. Reference facts used throughout: the two SR 11-7 sources of model risk (fundamental errors; incorrect or inappropriate use); the three components of a validation framework (conceptual soundness, ongoing monitoring, outcomes analysis); the three lines of defence; and the FRTB distinction between modellable and non-modellable risk factors.

---

## Section A — Concept Check

**A1. Define model risk precisely, and name its two root sources.**

Model risk is the potential for adverse consequences — financial loss, bad decisions, or reputational and regulatory damage — arising from **decisions based on incorrect or misused model outputs**. Following the Federal Reserve's SR 11-7, it has two root sources: (1) **the model may have fundamental errors** — wrong theory, wrong mathematics, coding bugs, or poor data — so it produces inaccurate outputs even when used as intended; and (2) **the model may be used incorrectly or inappropriately** — applied outside the conditions it was built for, fed the wrong inputs, or its results misunderstood. The crucial point is that a *perfectly correct* model still carries model risk through the second channel.

**A2. What is a "model" for governance purposes, and why does the definition matter?**

SR 11-7 defines a model as a quantitative method that applies statistical, economic, financial, or mathematical **theory, techniques, and assumptions** to process input data into quantitative estimates. The definition matters because it sets the **perimeter of the model inventory**: anything meeting it must be inventoried, tiered by materiality, and validated. Firms that define "model" too narrowly leave spreadsheets, vendor tools, and end-user computing applications ungoverned — which is exactly where uncontrolled model risk accumulates.

**A3. "All models are wrong, but some are useful." How does this shape the risk manager's job?**

The George Box aphorism reframes the goal. A model is a **deliberate simplification** of reality, so the question is never "is it correct?" (nothing is) but "**is it fit for its intended purpose, and do we understand where it breaks?**" The risk manager's job is therefore not to eliminate error but to (a) document the model's assumptions and limitations, (b) quantify the error it introduces, and (c) ensure it is only used where those errors are tolerable. Managing model risk is managing the *gap between the map and the territory*.

**A4. Distinguish model risk from parameter (estimation) risk.**

**Parameter risk** is uncertainty in the *inputs* to a chosen model — the estimated volatility, correlation, or default probability could be wrong because they are estimated from finite, noisy data. **Model risk** is broader: it includes parameter risk but also **structural risk** — the possibility that the entire model *form* is wrong (e.g. using a Gaussian copula when tail dependence exists, or Black–Scholes when volatility is stochastic). You can have perfect parameters in the wrong model. Structural error is the more dangerous of the two because it cannot be fixed by better estimation.

**A5. What are the three pillars of an effective model validation framework?**

(1) **Evaluation of conceptual soundness** — is the theory defensible, the methodology appropriate, and are the assumptions and limitations documented? This includes *developmental evidence* review. (2) **Ongoing monitoring** — process verification and benchmarking to confirm the model still works as markets and portfolios change; this catches degradation over time. (3) **Outcomes analysis** — comparing model outputs to actual realised results, the most direct of which is **backtesting**. A validation missing any pillar is incomplete: soundness without monitoring goes stale, and monitoring without outcomes analysis never confronts reality.

**A6. What does "effective challenge" mean, and what three things must a challenger have?**

Effective challenge is the *critical analysis by objective, informed parties who can identify model limitations and produce appropriate changes*. For it to be real, the challenger must have three things: **competence** (the technical skill to understand the model), **influence** (the standing and authority to force change), and **incentive/independence** (organisational separation so they are willing to say no). Strip away any one — a validator who is skilled but junior, or independent but under-resourced — and challenge becomes a rubber stamp. Effective challenge is the human mechanism that actually stops a bad model from shipping.

**A7. How do the "three lines of defence" allocate responsibility for model risk?**

**First line** — model owners, developers, and users — own the risk: they build, use, and self-test the model and are accountable for it. **Second line** — independent model validation / risk management — provides effective challenge, sets standards, maintains the inventory, and can block deployment. **Third line** — internal audit — does not re-validate models but assures the board that the *framework itself* is designed and operating effectively. The separation prevents the people who benefit from a model's approval from being the only ones checking it.

**A8. Why is a model inventory tiered by materiality rather than validated uniformly?**

Validation is costly and scarce; not every model threatens the firm equally. **Tiering by materiality** — based on the size of exposure, complexity, and reliance placed on the model — lets the firm concentrate deep, frequent validation on high-tier models (e.g. the regulatory capital or trading VaR engine) while applying proportionate, lighter scrutiny to low-tier ones. Treating a small pricing spreadsheet like the capital model wastes resources; treating the capital model like a spreadsheet is negligent. Tiering aligns validation intensity with the harm a failure would cause.

**A9. What is "model overlay" or a management adjustment, and why is it a double-edged sword?**

An overlay is a manual adjustment applied *on top of* a model's raw output — for example, adding to a loss-provision estimate because management judges the model has not captured a new risk (as widely done for COVID-19 and post-pandemic inflation under IFRS 9 / CECL). It is **necessary** because it corrects for known model blind spots the model cannot yet see. It is **dangerous** because it can become an unauditable channel for smoothing results or hiding a broken model. Good practice makes overlays explicit, documented, governed, and *temporary* — an overlay that never expires is a signal the underlying model needs rebuilding.

**A10. What are non-modellable risk factors (NMRFs) under FRTB, and why does the distinction exist?**

Under the Fundamental Review of the Trading Book, a risk factor is **modellable** only if it has enough *real, observable* price observations (broadly, at least 24 per year with no 90-day gap). Factors failing this test are **non-modellable** and attract a separate, punitive **stressed-expected-shortfall capital add-on** computed via stress scenarios rather than the internal ES model. The distinction exists because model risk is highest exactly where **data is thin** — you cannot reliably calibrate or backtest a factor you rarely observe — so the regulator forces conservative, non-model treatment there rather than trusting a poorly-supported model.

---

## Section B — Numerical / Applied (with full solutions)

**B1. Sizing model risk from a pricing-model gap.** A desk holds a book of exotic options. Model A (a simple Black–Scholes proxy) values the book at **$100.0m**. Model B (a stochastic-volatility model the validators consider more accurate) values it at **$97.4m**. (a) What is the model-risk provision (the "prudent valuation" reserve) implied by the disagreement? (b) If the book has been marked at Model A's value, what is the P&L impact of switching to B?

Solution.
(a) The model-uncertainty reserve is the difference between the marked value and the more conservative defensible value: $100.0\text{m} - 97.4\text{m} = \mathbf{\$2.6m}$. This is held as an **Additional Valuation Adjustment (AVA)** for model risk so the book is not carried at an optimistic mark.
(b) Switching to Model B writes the book down by the same **$2.6m loss** (a 2.6% haircut). The number is not a market move — nothing in the world changed — it is *pure model risk crystallising*. This is why unreserved model uncertainty is a hidden short position in your own valuation.

**B2. Backtesting exceptions and the traffic-light multiplier.** A bank's 99% one-day VaR model recorded **7 exceptions over 250 trading days**. (a) How many exceptions are expected for a correct model? (b) Which Basel traffic-light zone is this, and what happens to the capital multiplier? (c) If the 10-day 99% VaR is $30m, quantify the capital difference between the resulting multiplier and the green-zone baseline of $k=3.0$.

Solution.
(a) Expected exceptions $= (1-0.99)\times 250 = 0.01\times250 = \mathbf{2.5}$.
(b) 7 exceptions falls in the **Yellow zone** (5–9 breaches). Basel raises the multiplier from the green-zone $k=3.0$ by a yellow-zone add-on; for 7 exceptions $k = 3.65$.
(c) Baseline charge $= 3.0\times30\text{m} = \$90\text{m}$. Yellow charge $= 3.65\times30\text{m} = \$109.5\text{m}$. Extra capital $= \mathbf{\$19.5m\ (+21.7\%)}$. A model that under-forecasts risk is punished with a mechanically larger capital charge — model quality converts directly into capital.

**B3. Kupiec proportion-of-failures test on the same result.** Test the B2 model (7 exceptions in 250 days, target $p=0.01$) with Kupiec's unconditional-coverage statistic against the $\chi^2_1$ critical values 3.84 (5%) and 6.63 (1%).

Solution. Observed rate $\hat p = 7/250 = 0.028$. The likelihood-ratio statistic is
$$LR_{uc} = -2\ln\!\left[\frac{(1-p)^{T-x}p^{x}}{(1-\hat p)^{T-x}\hat p^{x}}\right].$$
- Under $p=0.01$: $243\ln(0.99)+7\ln(0.01) = 243(-0.010050)+7(-4.60517) = -2.442 - 32.236 = -34.678$.
- Under $\hat p=0.028$: $243\ln(0.972)+7\ln(0.028) = 243(-0.028399)+7(-3.575551) = -6.901 - 25.029 = -31.930$.
$$LR_{uc} = -2\big(-34.678 - (-31.930)\big) = -2(-2.748) = \mathbf{5.50}.$$
Decision: $3.84 < 5.50 < 6.63$, so we **reject at 5% but not at 1%**. Consistent with the Yellow-zone verdict of B2 — statistically the model is under strain but not decisively broken. The test and the supervisory rule agree: watch it closely.

**B4. Expected number of firms breaching by chance.** A regulator oversees **100 banks**, each running a *genuinely correct* 99% VaR model, over 250 days. (a) What is the expected number of exceptions per bank, and its standard deviation? (b) Roughly how many of the 100 banks would you expect to land in the Yellow zone (≥5 exceptions) purely by chance?

Solution.
(a) Exceptions $\sim \text{Binomial}(250, 0.01)$. Mean $= 250\times0.01 = 2.5$; SD $= \sqrt{250\times0.01\times0.99} = \sqrt{2.475} = \mathbf{1.573}$.
(b) $P(X\ge 5)$ for a Poisson/Binomial with mean 2.5 is about **0.11** (using Poisson: $P(X\le4)\approx0.891$, so $P(X\ge5)\approx0.109$). Across 100 correct models, that is roughly $\mathbf{11\ banks}$ in the Yellow zone by pure luck. The lesson for model risk governance: backtesting exceptions are noisy, so a single Yellow result is *not* proof of a bad model — you must weigh it against the base rate of false alarms before condemning a model.

**B5. Benchmarking two challenger models.** During validation, the champion model estimates portfolio 99% VaR at **$12.0m**. Two independent challenger models produce **$14.5m** and **$15.2m**. (a) What does the benchmark spread reveal? (b) If realised outcomes over the next quarter breach the $12.0m level far more often than 1% of the time, what is the validator's conclusion?

Solution.
(a) Both challengers sit **20–27% above** the champion ($14.5/12.0 = 1.21$; $15.2/12.0 = 1.27$). Consistent disagreement in the *same direction* is a red flag that the champion may be **systematically under-stating risk** — benchmarking has surfaced a possible structural bias that a single model in isolation would never reveal.
(b) Outcomes analysis (backtesting) then *confirms* what benchmarking suspected: excessive breaches mean the champion under-forecasts the tail. The validator escalates — the champion should be recalibrated or replaced, and in the interim a conservative overlay (or use of the challenger level) applied. This is the two pillars working together: benchmarking flags, outcomes analysis proves.

**B6. Vendor-model input error.** A firm licenses a third-party credit model. The vendor's default model was calibrated on data with an average PD of 2%, but the firm's actual portfolio has an average PD of 5%. Expected loss per $100m of exposure is $EL = PD \times LGD \times EAD$ with LGD = 40%. (a) What EL does the mis-applied model report? (b) What is the true EL, and what is the model-risk understatement?

Solution.
(a) Using the vendor's calibration PD: $EL = 0.02\times0.40\times100\text{m} = \mathbf{\$0.8m}$.
(b) Using the firm's true PD: $EL = 0.05\times0.40\times100\text{m} = \mathbf{\$2.0m}$. Understatement $= 2.0 - 0.8 = \mathbf{\$1.2m}$, i.e. the model reports only **40%** of the true expected loss. Nothing is wrong with the vendor's mathematics — this is SR 11-7's *second* source of model risk: a correct model **used outside its calibration domain**. The fix is not a better model but a re-calibration to the firm's own portfolio, and a control that flags when input distributions drift from the calibration set.

**B7. Materiality tiering by exposure-weighted error.** Three models each carry an estimated valuation-error rate of 3%, on exposures of $2,000m (Model X), $150m (Model Y), and $8m (Model Z). Rank them for validation priority by dollar error at risk.

Solution. Dollar error $=$ exposure $\times$ error rate:
- Model X: $2{,}000\text{m}\times0.03 = \mathbf{\$60m}$.
- Model Y: $150\text{m}\times0.03 = \mathbf{\$4.5m}$.
- Model Z: $8\text{m}\times0.03 = \mathbf{\$0.24m}$.
Priority order **X ≫ Y ≫ Z**. Although all three share the *same* error *rate*, the materiality — the harm a failure causes — spans a factor of 250. Tiering directs the scarce validation budget to Model X, where an identical modelling flaw does 250 times the damage. This is why materiality, not model complexity alone, drives the validation calendar.

---

## Section C — Interview-Style (with model answers)

**C1. "What is model risk, and why is it not just 'the risk the model is wrong'?"**

Model answer: Model risk is the risk of loss or bad decisions from relying on model outputs — but the naive version, "the model is wrong," misses half of it. SR 11-7 splits it into two sources: **fundamental errors** in the model (bad theory, bugs, poor data) *and* **incorrect or inappropriate use** — running the model outside its intended domain, feeding it wrong inputs, or misreading its results. The second source means a *flawless* model still carries model risk. So managing it is not only about building better models; it is about controlling assumptions, use, inputs, and interpretation across the model's whole life. The mindset is: every model is a simplification with a domain of validity, and risk lives at the edge of that domain.

**C2. "Walk me through how you would validate a new pricing model before it goes live."**

Model answer: I work the three pillars. First, **conceptual soundness**: I review the developmental evidence — is the theory appropriate for this product, are the assumptions and limitations documented, does the math check out, and is the data representative? Second, before it can go live I run **process verification and benchmarking**: I re-implement or compare against an independent challenger model and known analytical cases to confirm it does what it claims. Third, I set up **outcomes analysis** — a backtesting and P&L-attribution plan so that once live, model output is continuously compared to realised results. Throughout, the deliverable is not a yes/no but a documented statement of the model's *limitations and safe operating range*, plus any conditions or overlays required for approval. And critically, I must have the independence and authority to withhold approval — validation without the power to say no is theatre.

**C3. "Give me a real example where model risk caused a disaster, and name the specific failure."**

Model answer: Two canonical ones. **LTCM (1998)**: models assumed relationships would mean-revert and treated correlations as stable; when Russia defaulted, correlations went to one and liquidity vanished — the model's *assumption* of stable, diversifiable relationships was the structural error, amplified by leverage. **The 2008 Gaussian-copula CDO losses**: the copula had *zero tail dependence*, so it structurally could not represent correlated defaults; raising the correlation input could never fix a model that was blind to joint crashes by construction. The common thread is **structural model risk** — not a bad parameter but the wrong model *form* — combined with a governance failure to challenge the assumption. More recent and mundane: the 2012 "London Whale," where a spreadsheet VaR model with a copy-paste and a divide-by-sum-instead-of-average error understated risk. Disasters come from both exotic structural flaws and boring operational ones.

**C4. "How do you manage the model risk you cannot eliminate?"**

Model answer: You can never drive model risk to zero, so you *bound and reserve* it. First, **quantify** it — through benchmark spreads, sensitivity analysis, and comparison of alternative model outputs, so you have a dollar range for the uncertainty. Second, **reserve** against it — hold a model-uncertainty valuation adjustment (an AVA under prudent valuation) so the book is not marked at an optimistic single point. Third, **constrain use** — restrict the model to its validated domain with hard controls that flag inputs drifting outside calibration. Fourth, **overlay** with documented, temporary management adjustments where the model has a known blind spot. And fifth, **monitor** continuously so degradation is caught early. The philosophy is the same as market risk: you don't eliminate the exposure, you measure it, limit it, reserve for it, and watch it.

**C5. "Your validation team keeps signing off models that later fail. Diagnose the governance problem."**

Model answer: That is almost always a breakdown of **effective challenge**, and I'd check its three ingredients. **Competence** — are the validators technically able to understand the models, or are they out of their depth on the complex ones? **Influence** — do they actually have the standing and authority to block a model, or can the business override them? **Independence and incentive** — are they organisationally separate and free from pressure, or are they captured by the desk whose revenue depends on approval? A rubber-stamp pattern usually means at least one is missing — commonly influence: validators who *can* identify limitations but can't force change. I'd also check the **three lines of defence** are intact and that internal audit is assuring the *framework*, not just individual models. And I'd look at incentives — if validators are rewarded for throughput rather than for catching problems, they will optimise for sign-offs.

---

## Section D — MCQs (with reasoning)

**D1. According to SR 11-7, the two sources of model risk are:**
(a) market risk and credit risk; (b) fundamental errors and incorrect/inappropriate use; (c) parameter risk and liquidity risk; (d) coding bugs and data errors.

**Answer: (b).** The model may have fundamental errors, *or* it may be used incorrectly — the second source means even a correct model carries risk. (d) names only sub-types of the first source; (a) and (c) name other risk categories entirely.

**D2. The three components of a sound model validation framework are:**
(a) pricing, hedging, and reporting; (b) first, second, and third lines of defence; (c) conceptual soundness, ongoing monitoring, and outcomes analysis; (d) VaR, ES, and stress testing.

**Answer: (c).** These are SR 11-7's three validation pillars. (b) is the *governance* structure, not the validation framework; (a) and (d) are model uses and measures, not validation components.

**D3. "Effective challenge" of a model requires the challenger to have:**
(a) a PhD; (b) competence, influence, and incentive/independence; (c) veto power only; (d) access to the source code only.

**Answer: (b).** All three together — skill to understand, standing to force change, and independence/incentive to say no. Any one alone (e.g. veto power without competence) is insufficient. (a) and (d) are neither necessary nor sufficient.

**D4. A model produces a perfect valuation but is applied to a portfolio outside its calibration range. This is:**
(a) not model risk, since the model is correct; (b) parameter risk only; (c) model risk from inappropriate use; (d) market risk.

**Answer: (c).** This is SR 11-7's second source — correct model, wrong use. (a) is the classic mistake: a correct model *still* carries model risk through misuse. B6 quantifies exactly this case.

**D5. Under Basel's backtesting traffic light, a 99% VaR model with 10+ exceptions in 250 days lands in the:**
(a) Green zone, $k=3.0$; (b) Yellow zone; (c) Red zone, model rejected; (d) unclassified.

**Answer: (c).** Ten or more exceptions is the Red zone (multiplier $k=4.0$, model overhaul). Green is 0–4, Yellow is 5–9. Expected breaches for a correct model are only ~2.5.

**D6. Non-modellable risk factors (NMRFs) under FRTB arise mainly because:**
(a) the factor is too volatile; (b) there are too few real price observations to calibrate reliably; (c) the factor is illiquid to trade; (d) the regulator dislikes internal models.

**Answer: (b).** Modellability turns on having enough *observable* prices (broadly ≥24/year, no 90-day gap). Sparse data means the factor cannot be reliably calibrated or backtested, so it gets a conservative stressed-ES add-on. Volatility and tradability are related but not the defining test.

**D7. Benchmarking a champion model against independent challenger models primarily tests:**
(a) whether the model is coded correctly; (b) whether the model's outputs are reasonable relative to credible alternatives; (c) realised P&L; (d) regulatory capital.

**Answer: (b).** Benchmarking is a form of *ongoing monitoring* that flags systematic bias when alternatives consistently disagree (see B5). Comparing to realised results is *outcomes analysis* (c), a different pillar; (a) is process verification.

**D8. A management overlay on a model's output should ideally be:**
(a) permanent and undocumented; (b) explicit, documented, governed, and temporary; (c) applied silently to smooth earnings; (d) larger than the model output.

**Answer: (b).** Overlays correct known model blind spots but must be transparent and time-limited, or they become an unauditable channel for manipulation. An overlay that never expires signals the underlying model needs rebuilding. (a) and (c) describe exactly the abuse to avoid.

---
