# Q&A — Operational Risk

A practice bank for the Operational Risk chapter. Work each question before reading the answer. Numerical answers are self-checked against the Basel identities: BIA capital = 0.15 × avg positive gross income; SMA capital = BIC × ILM with ILM = ln(e − 1 + (LC/BIC)^0.8) and LC = 15 × 10-year average annual loss.

---

## Section A — Concept-Check (short answer)

**A1. State the Basel definition of operational risk verbatim, and name the two boundary clauses.**

"The risk of loss resulting from inadequate or failed internal processes, people and systems, or from external events." The two boundary clauses: **legal risk is included** (fines, penalties, settlements, failed-contract costs), and **strategic and reputational risk are excluded** from the regulatory capital definition. The subtlety is that an operational *event* (say a data breach) can *cause* reputational damage, but only the direct operational loss counts for capital.

**A2. What are the four sources of operational risk (PPSE), and which produces the largest single losses?**

**People, Processes, Systems, External events.** *People* — human error, negligence, and deliberate wrongdoing (fraud, rogue trading) — is the single richest source of large, spectacular losses. Note the distinction between "most spectacular single event" (internal fraud) and "largest aggregate dollar loss" (conduct and processing — see A5).

**A3. Why is operational risk described as "pure downside," and how does that differ from market and credit risk?**

Market and credit risk are risks a firm *takes on purpose* to earn a spread — there is an upside, and you can price, hedge, and earn a return for bearing them. Operational risk has **no upside**: nobody gets paid to be defrauded or to suffer a system outage. It is embedded in everything the firm does, pervasive rather than localised to one book, and offers no compensating return.

**A4. Describe the shape of the operational-loss distribution and say which part drives capital.**

It is **severely fat-tailed and asymmetric**: a high-frequency, low-severity *body* (data-entry errors, small mis-payments — predictable, budgetable) and a low-frequency, high-severity *tail* (rogue trader, systemic cyber breach, class-action settlement — rare but can exceed a year's profit). Economic capital is driven almost entirely by the **tail**, which is why op-risk modelling borrows from actuarial science and extreme-value theory rather than the normal distribution of basic market VaR.

**A5. Name the seven Basel Level-1 event types, and say which two carry the largest aggregate losses.**

Internal fraud; External fraud; Employment practices & workplace safety; Clients, products & business practices (CPBP); Damage to physical assets; Business disruption & system failures; Execution, delivery & process management (EDPM). The two carrying the largest **aggregate** dollar losses are **CPBP (conduct/mis-selling)** and **EDPM (processing errors)** — these dwarf internal fraud by total value even though fraud produces the most headline-grabbing single events.

**A6. Why is there "no natural exposure measure" for operational risk, and how did regulators solve it?**

Credit risk has exposure-at-default; market risk has position sizes. Operational risk has no clean dollar exposure — the "exposure" is the whole firm. Regulators solved it pragmatically with a **proxy for the scale of activity**: gross income (BIA/TSA) or later the Business Indicator (SMA), on the logic that a bigger, busier firm has more operational surface area and therefore more to go wrong.

**A7. What are the four data elements that feed operational-risk measurement and management?**

**Internal loss data (ILD)** — the firm's own recorded loss history, the empirical backbone; **External loss data (ELD)** — peers' losses via consortia like ORX, used to populate tail events you have been lucky to avoid; **Scenario analysis** — structured expert workshops estimating rare, severe events; **Business environment and internal control factors (BEICF)** — forward-looking control indicators (KRIs, audit findings, turnover). These are the "AMA data elements."

**A8. What is the difference between a KRI and loss data, and why does it matter?**

A **KRI is leading** — a predictive metric with a threshold (staff turnover, aged reconciliation breaks, system downtime) that flags rising risk *before* a loss crystallises. **Loss data is lagging** — it records what has already happened. The whole point of a good framework is to act on the KRI before the loss books. A KRI that never moves before a loss is theatre; good practice correlates KRIs against actual losses to prove they are predictive.

**A9. Explain the Three Lines of Defence.**

**First line — the business**: owns and manages its own risks day-to-day and owns the controls. **Second line — risk management & compliance**: sets framework, policy, and appetite, and independently challenges the first line. **Third line — internal audit**: provides independent assurance to the board that lines one and two actually work. The board and risk committee sit above, setting appetite.

**A10. List the four responses to an identified operational risk (the 4 T's).**

**Treat/mitigate** (strengthen controls — maker-checker, automation, segregation of duties); **Transfer** (insurance or outsourcing — but you transfer the operation, not the accountability); **Terminate/avoid** (exit the product or process); **Tolerate/accept** (consciously retain within appetite because control costs more than it saves). The tool that identifies and rates the risk beforehand is the **RCSA** (Risk and Control Self-Assessment).

---

## Section B — Numerical / Applied (full solutions)

**B1. BIA with a loss year.** A bank reports gross income ($m): Year-1 = 900, Year-2 = −150, Year-3 = 750. Compute the Basic Indicator Approach capital charge.

**Rule:** drop any year with non-positive GI from *both* numerator and denominator; α = 0.15.
- Positive-GI years: Year-1 (900) and Year-3 (750). Year-2 is excluded entirely.
- n = 2.
- Average positive GI = (900 + 750) / 2 = 825.
- Capital = 0.15 × 825 = **$123.75m**.

**Self-check.** The common trap averages all three years and nets the loss: (900 − 150 + 750)/3 = 500 → 0.15 × 500 = $75m. That is wrong under BIA — negative years are *dropped, not netted*. Dropping the loss year raises the average (825 vs 500) and therefore raises capital. The rule deliberately prevents a bank from *lowering* its capital charge by having had a disastrous year. ✓

**B2. TSA with business lines.** In a given year a bank's gross income by business line is: Trading & sales (β = 18%) = 400; Corporate finance (β = 18%) = 200; Retail banking (β = 12%) = 500; Asset management (β = 12%) = 100. Compute that year's weighted β × GI total.

- Trading & sales: 0.18 × 400 = 72
- Corporate finance: 0.18 × 200 = 36
- Retail banking: 0.12 × 500 = 60
- Asset management: 0.12 × 100 = 12
- Weighted total = 72 + 36 + 60 + 12 = **$180m** for the year.

**Self-check.** Under TSA you sum across business lines *within* the year first, then floor that yearly total at zero, then average over three years. Here the total is positive so it is kept as 180. If this had come out negative, it would be floored to 0 for the year but the year would still count (divide by 3) — unlike BIA which drops it. ✓

**B3. TSA vs BIA — opposite treatment of a loss year.** A bank's weighted β × GI totals are: Year-1 = +140, Year-2 = −60, Year-3 = +100. Compute the TSA charge and contrast the mechanic with BIA.

- Year-1 = +140 → keep 140.
- Year-2 = −60 → **floored to 0** (kept in the average).
- Year-3 = +100 → keep 100.
- Capital = (140 + 0 + 100) / 3 = 240 / 3 = **$80m**.

**Self-check.** Under BIA the negative year would be *dropped* (divide by 2); under TSA it is *floored but retained* (divide by 3). Same data, different denominators — TSA is not simply "BIA with betas." The floor-and-keep mechanic drags the TSA average down relative to BIA's drop-the-year mechanic. ✓

**B4. LDA → expected annual loss.** A cell has frequency ~ Poisson(λ = 5 events/year) and severity ~ Lognormal(μ = 11, σ = 1.4) in log-dollars. Find the mean severity per event and the expected annual loss.

- Mean severity (lognormal) = exp(μ + σ²/2) = exp(11 + 0.98) = exp(11.98) ≈ **$159,000**.
- Expected annual loss = λ × mean severity = 5 × 159,000 ≈ **$795,000 per year**.

**Self-check.** Expected loss is the *body* of the distribution — what you provision and budget. It uses the mean severity, not a tail quantile. Multiplying frequency by mean severity is the correct construction for the aggregate mean of a compound-Poisson process. ✓

**B5. OpVaR tail vs mean.** For the cell in B4, estimate the 99.9th-percentile *single* loss (z₀.₉₉₉ ≈ 3.09) and comment on the ratio to mean severity.

- 99.9% single loss = exp(μ + σ·z₀.₉₉₉) = exp(11 + 1.4 × 3.09) = exp(15.326) ≈ **$4.53m**.
- Ratio to mean severity = 4.53m / 159k ≈ **28×**.

**Self-check.** A ~28× gap between the mean event and the 99.9% event is the signature of the lognormal's fat right tail — exactly why OpVaR is driven by the tail, not the average. Capital held ≈ OpVaR − expected loss; if the model returned capital only slightly above expected loss you would know the severity tail was mis-specified. ✓

**B6. Internal Loss Multiplier — average loss record.** A bank has BIC = $2,000m and a 10-year average annual operational loss of $133.33m, so LC = 15 × 133.33 = $2,000m. Compute the ILM and SMA capital.

$$ILM = \ln\!\left(e^{1} - 1 + \left(\tfrac{2000}{2000}\right)^{0.8}\right) = \ln(2.718 - 1 + 1) = \ln(2.718) = 1.00$$

Capital = BIC × ILM = 2,000 × 1.00 = **$2,000m**.

**Self-check.** When LC = BIC the ratio is 1, so ILM = ln(e) = 1 and capital equals BIC — the "average loss experience" anchor. Everything hinges on whether the bank's loss record is better or worse than average for its size. ✓

**B7. ILM — poor loss record.** Same bank, but its 10-year average loss worsens so LC = $4,000m (ratio LC/BIC = 2). Compute the new ILM, capital, and the surcharge versus B6.

- (LC/BIC)^0.8 = 2^0.8. ln 2 = 0.6931; × 0.8 = 0.5545; e^0.5545 ≈ 1.741.
- ILM = ln(e − 1 + 1.741) = ln(2.718 − 1 + 1.741) = ln(3.459) ≈ **1.241**.
- Capital = 2,000 × 1.241 = **$2,482m**.
- Surcharge = 2,482 − 2,000 = $482m, roughly **+24%** for a doubled loss record.

**Self-check.** A worse loss history raises capital, but only sub-linearly (loss doubled, capital up ~24%, not 100%) because the multiplier uses a 0.8 power and a log wrapper — deliberate dampening so a single bad decade does not explode capital. Monotonic and well-behaved. ✓

**B8. ILM — spotless record.** A bank with BIC = $2,000m has essentially no loss history, so LC → 0. Compute the ILM and capital, and state the floor intuition.

- With LC = 0: ILM = ln(e − 1 + 0^0.8) = ln(e − 1) = ln(1.718) ≈ **0.541**.
- Capital = 2,000 × 0.541 = **$1,082m**.

**Self-check.** A pristine record earns a discount to ~54% of BIC — the practical floor of the multiplier. The formula is symmetric around the average: it rewards a clean record and penalises a bad one, both capped in magnitude by the log. Note many national regulators simply set ILM = 1, switching off loss-history sensitivity entirely. ✓

---

## Section C — Interview-Style (model answers)

**C1. "Was Barings a market-risk failure or an operational-risk failure?"**

The loss showed up in derivatives P&L, so it *looks* like market risk — Nick Leeson's Nikkei futures positions. But the risk that actually *failed* was operational. Leeson ran both the trading desk and the back office, so there was **no segregation of duties**: he could book fictitious offsetting trades and hide the losses in an error account (the famous 88888). The root cause was a control failure — no maker-checker, no independent reconciliation, no supervision. The lesson interviewers want: **classify by root cause, not by the P&L line.** A rogue trader is an operational failure wearing a market-risk costume.

**C2. "Why did Basel III abolish the AMA?"**

The Advanced Measurement Approach let each bank build its own internal model to hit the 99.9%/1-year capital standard. In principle it was the most risk-sensitive method; in practice the models proved **inconsistent and impossible to compare** across banks — two firms with similar risk profiles could produce wildly different capital numbers depending on modelling choices, creating model risk and gaming incentives. Basel III (finalised 2017) scrapped AMA *and* the old BIA/TSA menu, replacing everything with the single non-modelled **SMA** formula, capital = BIC × ILM. The trade-off is explicit: **SMA sacrifices sensitivity for comparability and reduced model risk**, while keeping *some* risk sensitivity through the loss-history multiplier.

**C3. "How would you build a KRI framework for a trading operation?"**

I would start from the risks I am trying to see coming and pick *leading* indicators for each. For fraud/conduct: number of limit breaches, off-hours trading activity, cancel-and-correct rates, and trader-attestation lapses — the classic rogue-trading precursors. For processing: aged/failed settlements and reconciliation breaks open beyond X days. For systems: downtime minutes, change-failure rate, patch backlog. Each KRI needs a **green/amber/red threshold, a named owner, a fixed review cadence, and an escalation trigger**. Critically, I would **back-test each KRI against actual loss data** to prove it is predictive — a KRI that never moves before a loss is decorative and should be replaced. The output feeds the risk committee so we act before the loss books.

**C4. "Does outsourcing a process remove the operational risk?"**

No. Outsourcing **transfers the operation but not the accountability** — regulators hold the firm responsible for outsourced activities as if performed in-house. Worse, it *creates new risk*: **vendor/third-party risk**, concentration risk if many firms use the same provider, and the loss of direct control over the vendor's own control environment. So outsourcing is a *transfer* response under the 4 T's, but it must be paired with vendor due diligence, SLA monitoring (itself a KRI), exit planning, and continued board oversight. The one-liner: **you can outsource the process, never the accountability.**

**C5. "Walk me through how operational-risk capital is actually computed today under the SMA."**

Two ingredients. First the **Business Indicator (BI)** — an income proxy built from three components: an interest/lease/dividend component, a services component, and a financial (trading + banking book) component. The BI is mapped through a progressive marginal-coefficient schedule into the **Business Indicator Component (BIC)** — bigger banks attract higher marginal rates. Second the **Internal Loss Multiplier (ILM)** = ln(e − 1 + (LC/BIC)^0.8), where the **Loss Component LC = 15 × the average annual operational loss over 10 years**. Capital = **BIC × ILM**. When loss experience is average (LC = BIC), ILM = 1 and capital = BIC; a poor loss record pushes ILM above 1, a clean one below. National regulators may set ILM = 1 to remove loss-history sensitivity.

**C6. "Give me an operational-risk case that was purely a systems/change-management failure."**

**Knight Capital, 2012.** A botched software deployment — new code went live while dormant legacy code was accidentally reactivated on some servers — caused the firm's system to fire millions of erroneous orders into the market. It lost roughly **$440m in about 45 minutes** and effectively destroyed the firm. This is a textbook **event type 6/7** (business disruption/system failure and execution/process management) failure of **change management** — no proper deployment controls, no kill-switch, no reconciliation of what code was running where. It shows operational risk's tail can crystallise in minutes, not years.

---

## Section D — MCQs (with reasoning)

**D1. Which of the following is EXCLUDED from the Basel operational-risk capital definition?**
A) Legal risk  B) Reputational risk  C) External fraud  D) Failed internal processes

**Answer: B.** Reputational (and strategic) risk is explicitly excluded. Legal risk (A) is *included*; external fraud (C) and failed processes (D) are core sources. Trap: an operational event can *cause* reputational damage, but the reputational hit is not in the capital charge.

**D2. Under the BIA, a year with negative gross income is:**
A) Netted against positive years  B) Floored at zero but retained in the average  C) Dropped from both numerator and denominator  D) Multiplied by beta

**Answer: C.** BIA drops non-positive years entirely (divide by fewer years). Option B describes **TSA**, not BIA — that is the classic BIA/TSA confusion. Option D confuses BIA (no betas) with TSA.

**D3. Which two event types carry the largest AGGREGATE dollar losses in the industry?**
A) Internal fraud and damage to physical assets  B) CPBP and EDPM  C) External fraud and EPWS  D) System failure and internal fraud

**Answer: B.** Clients/Products/Business Practices (conduct, mis-selling, AML fines) and Execution/Delivery/Process Management (settlement and processing errors) dominate by total value. Internal fraud produces the most *spectacular single* events but not the largest aggregate — a common trap.

**D4. In the Loss Distribution Approach, frequency is typically modelled as ___ and severity as ___.**
A) Lognormal; Poisson  B) Poisson; Lognormal  C) Normal; Normal  D) Binomial; Uniform

**Answer: B.** Frequency (event count per year) is Poisson with parameter λ; severity (dollar size per event) is lognormal or a heavy-tailed distribution such as generalised Pareto for the tail. The two are convolved (usually by Monte Carlo) to get the aggregate annual loss and read off the 99.9th percentile.

**D5. When the Loss Component equals the Business Indicator Component (LC = BIC), the Internal Loss Multiplier equals:**
A) 0  B) 0.5  C) 1.0  D) 1.5

**Answer: C.** ILM = ln(e − 1 + (LC/BIC)^0.8) = ln(e − 1 + 1) = ln(e) = 1. This is the "average loss experience" anchor where capital = BIC exactly.

**D6. Operational-risk economic capital is held primarily against:**
A) Expected loss  B) The mean of the loss distribution  C) The tail (unexpected loss)  D) Gross income

**Answer: C.** Capital covers *unexpected* loss (OpVaR minus expected loss), on the assumption expected loss is already provisioned/priced. Confusing the mean (A/B) with the tail double-counts or under-counts. Gross income (D) is only a scale *proxy*, not what capital defends against.

**D7. Which control most directly addresses the Barings-type rogue-trader risk?**
A) Insurance  B) Segregation of duties / maker-checker  C) Higher gross-income capital  D) External loss data

**Answer: B.** Separating the initiator from the approver (and trading from back-office reconciliation) is the core preventive control that Barings lacked. Insurance (A) is a *transfer*, not prevention; capital (C) absorbs losses rather than preventing them; ELD (D) informs modelling, not day-to-day control.

**D8. A KRI differs from loss data because a KRI is:**
A) Lagging and backward-looking  B) Leading and predictive  C) A regulatory capital figure  D) Only used in the third line of defence

**Answer: B.** KRIs are leading metrics (turnover, aged reconciliation breaks, downtime) that flag rising risk *before* a loss. Loss data is the lagging record of what already happened. The whole point is to act on the KRI first.

---

## Recap of key formulas (self-verify against these)

- **BIA:** K = 0.15 × average *positive* GI (3 yr); drop non-positive years.
- **TSA:** K = avg over 3 yr of max(Σⱼ βⱼ × GIⱼ, 0); betas 12/15/18%; floor the yearly total, keep the year.
- **LDA:** compound Poisson(λ) of lognormal severities; mean severity = exp(μ + σ²/2); capital ≈ OpVaR₉₉.₉ − EL.
- **SMA:** K = BIC × ILM, ILM = ln(e − 1 + (LC/BIC)^0.8), LC = 15 × 10-yr avg loss; LC = BIC ⇒ ILM = 1.
