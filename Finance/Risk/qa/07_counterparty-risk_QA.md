# Q&A — Counterparty Credit Risk

A practice bank for the Counterparty Credit Risk (CCR) chapter. Work each question before reading the answer. Numerical answers are self-checked against the core identities: exposure `E = max(V, 0)`, `CVA ≈ LGD × Σ EE(tᵢ)·D(tᵢ)·[S(tᵢ₋₁) − S(tᵢ)]`, and `EAD = 1.4 × Effective EPE`.

---

## Section A — Concept-Check (short answer)

**A1. What is counterparty credit risk, and how does it differ from ordinary loan credit risk?**

CCR is the risk that the counterparty to a bilateral contract (typically an OTC derivative) defaults *before final settlement* at a moment when the contract has *positive value to you*. It differs from loan credit risk on three counts: (1) the direction is bilateral and uncertain — either party can end up the creditor as the contract flips sign; (2) the exposure is stochastic and market-driven — it is the *replacement cost* of the contract, not a fixed principal; and (3) the horizon is long and the exposure profile evolves over the life of the trade. A loan has a known, roughly fixed exposure; a swap does not.

**A2. Why is exposure the *positive* part of value, `max(V, 0)`?**

Because default is asymmetric. If the contract value to you is positive (`V > 0`), the counterparty owes you and their default costs you that replacement value. If the value is negative (`V < 0`), you owe them — and default does *not* release you from paying; the administrator will still demand it. So a negative-value trade produces zero exposure, never a gain. You keep the downside and lose the upside, which is exactly why exposure has an option-like, convex shape.

**A3. Distinguish Current Exposure, Expected Exposure, and Potential Future Exposure.**

- **Current Exposure (CE)** is today's exposure, `max(V₀, 0)` — the loss if the counterparty defaulted right now.
- **Expected Exposure (EE)** is the *mean* of the exposure distribution at a future date `t`, `E[max(Vₜ, 0)]`. It is the key input to CVA.
- **Potential Future Exposure (PFE)** is a *high quantile* (e.g. 95th or 99th percentile) of the same distribution at `t` — the worst case within a confidence level, used for limits.

PFE ≥ EE always, because a high quantile of a distribution is at least its mean for a non-negative variable.

**A4. Why is the exposure profile of an interest-rate swap hump-shaped?**

Two opposing forces act over time. The **diffusion effect** widens the range of possible future values as rates wander from today's level, pushing exposure up roughly with √t. The **amortisation (roll-off) effect** shrinks the remaining cash flows as the trade nears maturity, pulling exposure down to zero at the end. Diffusion dominates early, amortisation dominates late, so exposure peaks somewhere around one-third to one-half of the tenor. An FX forward, by contrast, has a single exchange at maturity and no amortisation, so its exposure rises monotonically to the end.

**A5. What is CVA in one sentence, and why is it a real P&L item?**

CVA (Credit Valuation Adjustment) is the market value of expected loss from counterparty default: `Risky value = Risk-free value − CVA`. It is a real, daily-marked P&L item because it is computed off the counterparty's CDS spread — when that spread widens, CVA rises and the bank books a *CVA loss even with no default occurring*. Roughly two-thirds of 2008-era CCR losses were CVA mark-to-market moves, not realised defaults, which is why Basel III added a dedicated CVA capital charge.

**A6. Why does netting reduce exposure, and what is the exact difference in formula?**

Under a legally enforceable ISDA Master Agreement, all trades in a netting set collapse into one net claim on default. Exposure becomes the positive part of the *sum*, `max(ΣVᵢ, 0)`, rather than the *sum of the positive parts*, `Σ max(Vᵢ, 0)`. Because in-the-money and out-of-the-money trades offset, the net figure is smaller — often 50–90% smaller for a diversified book. The benefit is only recognised where close-out netting is legally enforceable in the counterparty's jurisdiction.

**A7. What residual risk remains even under a "perfect" daily collateral (CSA) agreement?**

The **margin period of risk (MPoR)** residual. Even with daily variation margin, there is a gap between the last margin call the counterparty honours and the moment you finally close out and re-hedge — typically ~10 business days for non-cleared trades. The portfolio can move against you during that window, and that residual is what **initial margin** is designed to cover. Collateral shrinks exposure to this residual (plus any threshold, MTA slack, and collateral haircuts) but never to zero.

**A8. Define wrong-way risk and give one specific-WWR example.**

Wrong-way risk is a *positive correlation between exposure and the counterparty's default probability* — the exposure rises precisely when the counterparty is most likely to default, making losses worse than an independence assumption implies. *General* WWR is macro-driven (e.g. buying EM sovereign protection from a bank in that same economy). *Specific* WWR is a structural link — e.g. taking the counterparty's own shares as collateral, or buying CDS protection on a firm from an entity in its own group. Regulators require WWR identification, and for specific WWR the exposure is set to the full loss with no netting benefit.

**A9. What is the alpha factor and where does it appear?**

Alpha is a regulatory multiplier of **1.4** applied to the loan-equivalent exposure to gross it up for correlation, granularity, and model uncertainty. It appears in the Basel internal-model EAD, `EAD = 1.4 × Effective EPE`, and in SA-CCR, `EAD = 1.4 × (Replacement Cost + PFE add-on)`.

**A10. How does a CCP reduce counterparty risk, and what new risk does it create?**

A central counterparty *novates* each trade into two, standing between the members and guaranteeing performance. It reduces risk through multilateral netting across all members, disciplined daily/intraday variation margin, risk-sensitive initial margin, mutualised default-fund contributions, and a default waterfall. But it *transforms* rather than eliminates the risk: the CCP becomes a systemically critical single point of failure ("too big to fail"), members bear default-fund and assessment risk from others' failures, and posting large cash initial margin creates liquidity/basis risk.

---

## Section B — Numerical / Applied (full solutions)

**B1. Exposure with sign flip.** A single swap has mark-to-market value to you of `−4.0 m` today. What is your current exposure? If tomorrow rates move and the value becomes `+6.0 m`, what is the exposure then?

Today: `E = max(−4.0, 0) = 0`. You owe the counterparty, so their default costs you nothing — but you still owe the 4.0 m. Tomorrow: `E = max(+6.0, 0) = 6.0 m`. **Exposure went from 0 to 6.0 m** purely on a market move, illustrating the stochastic, sign-flipping nature of CCR. ✓

**B2. Netting benefit.** Four trades under one ISDA Master with Counterparty X, values to you (in m): +18, −11, +5, −4. Compute gross exposure, net exposure, netting benefit, and netting factor.

Gross (sum of positive parts): `18 + 0 + 5 + 0 = 23.0 m`.
Net (positive part of the sum): `ΣVᵢ = 18 − 11 + 5 − 4 = 8.0 m`, so `max(8, 0) = 8.0 m`.
Netting benefit `= 23 − 8 = 15.0 m`.
Netting factor `= 8 / 23 = 0.348`.

**Check:** the factor lies in [0,1], and netting removed ~65% of gross exposure — plausible for a book with large offsetting positions. ✓

**B3. Collateralised exposure.** Continue B2. Counterparty X has posted **5.0 m** cash collateral. The CSA has **Threshold = 1.0 m** and **MTA = 0.5 m**. Compute the collateralised exposure.

`Collateralised exposure = max(Net MTM − Collateral + Threshold + MTA, 0)`
`= max(8.0 − 5.0 + 1.0 + 0.5, 0) = max(4.5, 0) = 4.5 m`.

**Check:** exposure fell 23.0 → 8.0 (netting) → 4.5 (collateral). Each tool strictly reduced exposure; the residual is the net value above collateral plus the contractual threshold/MTA slack. Consistent. ✓

**B4. CVA on a netting set.** A 4-year netting set with Counterparty Y. Discounted expected exposures at year-ends (in m): EE(1)=6, EE(2)=8, EE(3)=5, EE(4)=2. Y's flat CDS spread is 300 bps; recovery R = 40%, so LGD = 0.60. Compute CVA.

**Step 1 — hazard rate and survival.** `λ = spread / LGD = 0.03 / 0.60 = 0.05` per year. `S(t) = exp(−0.05·t)`.

| t | S(t) | Marginal PD = S(t−1)−S(t) |
|---|---|---|
| 0 | 1.00000 | — |
| 1 | 0.95123 | 0.04877 |
| 2 | 0.90484 | 0.04639 |
| 3 | 0.86071 | 0.04413 |
| 4 | 0.81873 | 0.04198 |

**Step 2 — expected loss per bucket (EE × marginal PD):**

| t | EE | Marginal PD | EE × PD |
|---|---|---|---|
| 1 | 6 | 0.04877 | 0.29262 |
| 2 | 8 | 0.04639 | 0.37112 |
| 3 | 5 | 0.04413 | 0.22065 |
| 4 | 2 | 0.04198 | 0.08396 |
| **Σ** | | | **0.96835** |

**Step 3 — apply LGD:** `CVA = 0.60 × 0.96835 = 0.5810 m ≈ $581,000`.

**Check:** Crude cross-check — total 4-year default prob `= 1 − S(4) = 0.18127`; times a representative EE of ~5.25 m times LGD 0.60 ≈ `0.181 × 5.25 × 0.60 = 0.571 m`, same order of magnitude as the bucketed 0.581 m. ✓

**B5. Wrong-way risk adjustment.** Reuse B4. Exposure and Y's default are positively correlated; model WWR with an alpha multiplier of 1.3 on the expected-loss sum. New CVA?

`CVA_WWR = 1.3 × 0.5810 = 0.7553 m ≈ $755,000`.

**Check:** WWR *increases* CVA (581k → 755k, +30%), which is directionally correct — wrong-way risk always worsens counterparty risk because the large exposure and the default coincide. Right-way risk (multiplier < 1) would reduce it. ✓

**B6. Basel EAD.** The netting set of B4 has Effective EPE = 5.0 m. Compute the internal-model EAD, and compare to the single-date peak EE.

`EAD = alpha × Effective EPE = 1.4 × 5.0 = 7.0 m`.

**Check:** EAD (7.0 m) exceeds Effective EPE (5.0 m) by the 1.4 buffer, and here happens to equal the single-date peak EE (8.0 m)? No — 7.0 < 8.0. EAD sits above the *average* exposure but below the single worst date, exactly as intended: it is a loan-equivalent capturing the *average* exposure grossed up for correlation, not the worst point. Consistent with `EPE ≤ EEPE ≤ EAD ≤ peak PFE`. ✓

**B7. Loss given default on a derivative.** A swap is worth +10 m to you when the counterparty defaults. Recovery is 30%. What is your loss?

Loss `= (1 − R) × max(V, 0) = (1 − 0.30) × 10 = 0.70 × 10 = 7.0 m`. You recover `0.30 × 10 = 3.0 m` from the estate and must replace the swap at market cost 10 m, net loss 7.0 m. ✓

---

## Section C — Interview-Style (model answers)

**C1. "Why isn't the exposure of an interest-rate swap equal to its notional?"**

Because exposure is *replacement cost*, not principal. In a swap, the notional is never exchanged — only net interest flows are. What you can lose on the counterparty's default is the cost of replacing the contract at current market rates, i.e. the positive mark-to-market value, `max(V, 0)`. An at-market swap starts life worth roughly zero to both sides, so initial exposure is near zero. The notional only *scales the potential* future exposure by determining how large the value swings can be, but it is not itself the amount at risk. Saying "exposure equals notional" would overstate the risk by orders of magnitude.

**C2. "Walk me through how you'd compute an exposure profile."**

The standard method is Monte Carlo simulation. First, choose risk-factor models — Hull–White for interest rates, geometric Brownian motion for FX or equity. Second, simulate thousands of scenario paths of those risk factors out to the longest trade maturity on a time grid. Third, at every grid date on every path, reprice every trade in the netting set and apply the netting and collateral rules to get the netted, collateralised value `Vₜ`. Fourth, take `Eₜ = max(Vₜ, 0)` on each path. Finally, across paths at each date: the mean gives EE, the chosen high quantile gives PFE, and time-averaging the running-max EE gives Effective EPE. It is computationally heavy — banks reprice millions of trade-scenario combinations nightly — which is why XVA and exposure engines are major infrastructure investments. For a lighter regulatory number, SA-CCR approximates EAD as `1.4 × (Replacement Cost + PFE add-on)` without full simulation.

**C3. "Explain CVA to a non-technical stakeholder, and why the desk can lose money on it without any default."**

CVA is the price of the risk that the people we trade derivatives with might not pay us. A derivative traded with a shaky counterparty is worth less than the identical trade with a rock-solid one, and CVA is exactly that discount — the expected cost of their possible default. The subtle part: we don't wait for a default to recognise it. We mark CVA every day using the market's own read on that counterparty's creditworthiness — their CDS spread. If the market suddenly thinks the counterparty is riskier, their spread widens, our expected default cost rises, and we book a CVA loss that day — even though nobody has defaulted and no cash has changed hands. That daily volatility, not actual defaults, drove most of the counterparty losses in 2008, which is why regulators now hold capital specifically against CVA swings.

**C4. "What's wrong-way risk, and why do risk managers lose sleep over it?"**

Wrong-way risk is when your exposure to a counterparty grows at exactly the moment that counterparty becomes more likely to default — the two are positively correlated. The classic example is taking a company's own stock as collateral: if the company gets into trouble, its stock falls, your collateral evaporates, and your exposure balloons, all simultaneously. Another is buying credit protection on a country from a bank domiciled in that country — a sovereign crisis hits both the protection you're owed and the bank that owes it. It matters because it breaks the comforting assumption that exposure and default are independent. Under independence you'd average a moderate exposure against a moderate default probability, but WWR makes the *big* exposure and the default land together, fattening the tail of the loss distribution. Ignore it and you systematically understate CVA and economic capital.

**C5. "A CCP guarantees both sides of every trade. Does that mean central clearing eliminates counterparty risk?"**

No — it transforms it rather than eliminating it. Clearing genuinely reduces bilateral risk through multilateral netting, disciplined daily variation margin, risk-sensitive initial margin, and mutualised loss-sharing via a default waterfall. But three new risks appear. First, the CCP itself becomes a systemically critical single point of failure — if it fails, the whole market is exposed, which is why CCPs are now heavily stress-tested and regulated. Second, as a clearing member you bear default-fund and assessment risk: if another member defaults and blows through their margin, your mutualised contribution absorbs part of the loss. Third, initial margin must be posted in cash or high-quality liquid assets, so clearing converts credit risk into a liquidity and funding demand. So the honest answer is: clearing concentrates and mutualises counterparty risk into a well-managed hub, but the risk doesn't vanish.

---

## Section D — MCQs (with reasoning)

**D1. The exposure of an OTC derivative to a defaulting counterparty is best described as:**
A. The notional of the contract
B. `max(V, 0)`, the positive part of the mark-to-market value
C. The absolute value `|V|`
D. The sum of all future cash flows

**Answer: B.** Exposure is the replacement cost, and only when the contract is in-the-money to you (`V > 0`) does default cost you anything. A gives the notional, which is never at risk in full; C would wrongly count a trade you *owe* on as exposure; D ignores the netting of flows and the `max` transform.

**D2. Under a legally enforceable netting agreement, exposure across a netting set equals:**
A. `Σ max(Vᵢ, 0)`
B. `max(Σ Vᵢ, 0)`
C. `Σ Vᵢ`
D. `max(Vᵢ)` over all trades

**Answer: B.** Netting takes the positive part of the *sum* of values. A is the *gross* (no-netting) figure; the difference between A and B is the netting benefit. C ignores that a net-negative set gives zero exposure, and D is meaningless.

**D3. Which statement about CVA is correct?**
A. CVA is only realised if the counterparty actually defaults
B. CVA increases when the counterparty's CDS spread widens
C. CVA raises the value of a derivative above its risk-free value
D. CVA is unaffected by the exposure profile

**Answer: B.** CVA is marked daily off the CDS spread, so a wider spread means higher expected default cost and a CVA loss with no default — refuting A. C is backwards: `Risky value = Risk-free value − CVA`, so CVA *reduces* value. D is false because CVA is driven directly by the EE profile.

**D4. The classic hump-shaped exposure profile of an interest-rate swap results from:**
A. Amortisation dominating early and diffusion late
B. Diffusion dominating early and amortisation (roll-off) late
C. A single cash exchange at maturity
D. Wrong-way risk

**Answer: B.** Early on, diffusion widens the value distribution faster than cash flows roll off, so exposure rises; later, amortisation dominates and exposure falls to zero at maturity. A reverses the forces. C describes an FX forward (monotone profile, not hump). D is unrelated to profile shape.

**D5. In the Basel internal-model approach, Exposure at Default equals:**
A. Effective EPE
B. 1.4 × Effective EPE
C. Peak PFE
D. Current Exposure

**Answer: B.** The alpha factor of 1.4 grosses up the loan-equivalent Effective EPE for correlation and granularity. A omits alpha; C is the worst-case single point, not the regulatory EAD; D captures only today's exposure.

**D6. Taking the counterparty's own equity as collateral is an example of:**
A. Right-way risk
B. General wrong-way risk
C. Specific wrong-way risk
D. Basis risk

**Answer: C.** There is a structural link between the collateral value and the counterparty's own default — as it approaches default its stock collapses, so the collateral fails exactly when needed. That structural, name-specific link makes it *specific* WWR; general WWR (B) is macro-driven without a direct structural tie.

**D7. Even under a daily-margined CSA, residual exposure remains because of:**
A. The notional of the trades
B. The margin period of risk
C. The netting factor
D. The alpha multiplier

**Answer: B.** Between the last honoured margin call and final close-out (~10 business days bilaterally), the portfolio can move against you; that residual is covered by initial margin. A, C, and D are unrelated to the collateral gap.

**D8. In a CCP default waterfall, which resource is consumed first?**
A. Surviving members' default-fund contributions
B. The CCP's own capital (skin in the game)
C. The defaulting member's initial margin
D. Recovery tools and assessments

**Answer: C.** The waterfall consumes the defaulter's own resources first — initial margin, then their default-fund contribution — before touching the CCP's capital, then surviving members' mutualised fund, and finally recovery tools. This "defaulter pays first" ordering is the core of the mutualisation design.

---

*Self-verification note.* All numerical answers were recomputed and cross-checked: exposures satisfy `E = max(V, 0)`; netting factors lie in [0, 1]; CVA figures were sanity-checked against the crude `(1−S(T)) × representative-EE × LGD` bound; and `EAD = 1.4 × Effective EPE` sits between average and peak exposure. Formulas match the chapter's core identities.
