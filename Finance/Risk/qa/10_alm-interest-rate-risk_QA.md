# Q&A — Asset-Liability Management and Interest-Rate Risk in the Banking Book

A practice bank for the ALM / IRRBB chapter. Work each question before reading the answer. Numerical answers are self-checked against the two master identities: the earnings lens `ΔNII ≈ GAP × Δr` (GAP = RSA − RSL) and the value lens `ΔEVE ≈ − D_GAP × A × Δy` (D_GAP = D_A − k·D_L, k = L/A).

---

## Section A — Concept-Check (short answer)

**A1. State the two master identities of ALM and name the lens each belongs to.**

- **Earnings lens:** `GAP = RSA − RSL`, and `ΔNII ≈ GAP × Δr`. Short horizon (≤ 1 year), measures the effect of a rate shock on *net interest income*.
- **Value lens:** `D_GAP = D_A − k·D_L` with `k = L/A`, and `ΔEVE ≈ − D_GAP × A × Δy`. Full-life horizon, measures the present-value effect on the *net worth* of the firm.

They answer different questions — a flow over a fixed window versus a present value over the whole book — and a bank can pass one while failing the other.

**A2. What is IRRBB and how does it differ from credit and trading-book market risk?**

IRRBB is the risk that the value or income of the bank's *accrual* (non-traded) positions moves because assets and liabilities reprice at different times and sensitivities. Unlike credit risk, nobody defaults; unlike trading-book market risk, no marked position moves — value changes purely from the *timing mismatch* between what the bank owns and owes. It is a Basel Pillar 2 risk.

**A3. Why does repricing timing — not maturity — determine rate sensitivity?**

Rate risk exists only when an item's *interest rate resets*. A 30-year floating-rate loan that resets monthly is rate-sensitive (behaves "short"); a 3-year fixed CD is not rate-sensitive until it matures (behaves "long"). Principal repayment timing is irrelevant to the spread; what matters is when the coupon/rate on the item changes.

**A4. Define RSA and RSL.**

**Rate-Sensitive Assets** are assets whose rate will reset within the chosen time bucket (floating loans, maturing fixed loans about to roll, short securities, reserves at market rate). **Rate-Sensitive Liabilities** are liabilities whose cost resets within the bucket (maturing CDs, money-market deposits, short-term/floating borrowings). Everything else is non-rate-sensitive for that bucket, including long fixed assets and non-maturity deposits.

**A5. Interpret the sign of the repricing gap.**

- **Positive gap (RSA > RSL) = asset-sensitive:** NII *rises* when rates rise, *falls* when rates fall.
- **Negative gap (RSA < RSL) = liability-sensitive:** NII *falls* when rates rise, *rises* when rates fall.
- **Zero gap = matched:** NII unchanged to a parallel shock.

The mnemonic: the side with the *larger* rate-sensitive balance drives the direction of the NII move.

**A6. What is the cumulative one-year gap and why is it the headline earnings number?**

Banks bucket the balance sheet (0–3m, 3–6m, 6–12m, …) and sum the gaps across all buckets up to the one-year horizon. The cumulative 1-year gap captures *everything that reprices within a year*, so `ΔNII(1yr) ≈ Cumulative 1-yr GAP × Δr` is the standard measure of near-term earnings-at-risk.

**A7. What is the duration gap and what does it drive?**

`D_GAP = D_A − k·D_L`, where D_A and D_L are the (modified) durations of assets and liabilities and `k = L/A` is the leverage factor. It drives the change in the economic value of equity: `ΔEVE ≈ − D_GAP × A × Δy`. A positive duration gap (the "normal bank": long assets, short funding) means EVE falls when rates rise.

**A8. Why does leverage amplify equity's sensitivity to rates?**

Because `ΔEVE` scales by *total assets A*, not by equity, while equity is a thin residual (`EVE = A − L`, often ~8–10% of A). So a rate move that shifts asset value by a few percent can shift the small equity base by tens of percent. A bank is effectively a leveraged bond portfolio.

**A9. What is duration immunisation of equity, and its limits?**

Setting `D_GAP = 0`, i.e. `D_A = k·D_L`, so `ΔEVE ≈ 0` for a small parallel shift. Limits: it protects *equity value only* (not earnings), only against *small, parallel* moves, and it leaks through convexity, yield-curve twists (steepeners/flatteners), basis risk between indices, and embedded optionality (prepayments, deposit runoff). It is a first-order static hedge that must be rebalanced.

**A10. What is the Basel IRRBB outlier test?**

A supervisory flag: a bank is an outlier if the maximum ΔEVE loss across the **six prescribed shock scenarios** (parallel up/down, steepener, flattener, short-rate up/down) exceeds **15% of Tier 1 capital**. Banks must also model non-maturity deposits with caps on assumed behavioural life to prevent gaming.

**A11. Why must a bank monitor both ΔNII and ΔEVE?**

They can disagree because they cover different horizons. A 10-year fixed bond funded by 1-year deposits shows a *near-zero 1-year gap* (safe on earnings) but a *huge duration gap* (EVE devastated by a rate rise). The 12-month earnings model is blind to risk living beyond its horizon — exactly the blindness that felled Silicon Valley Bank. Basel therefore mandates both.

**A12. Why are non-maturity deposits (NMDs) the hardest ALM judgement?**

They have no contractual maturity, yet core balances are behaviourally *sticky* and their rate passes through only partially (low beta). Banks must model them as a blend of short and multi-year tranches. Getting the effective duration and beta wrong distorts *both* the repricing gap and the EVE calculation, so it is the single largest modelling call in ALM — which is why Basel caps the assumed behavioural life.

**A13. What is the standardised gap and why is it more realistic than the plain gap?**

The plain gap assumes every RSA and RSL moves 1-for-1 with the market rate. In reality betas differ — a savings deposit might move only 0.5× the policy rate while a loan moves 1.0×. The standardised gap weights each item by its rate beta before differencing, giving a truer ΔNII.

**A14. Give the modified-duration relationship and define its terms.**

`ΔP/P ≈ − D_mod × Δy`, where `D_mod = D_Macaulay / (1 + y)`. D_mod is the percentage price change per unit change in yield; the minus sign captures the inverse price-yield relationship for fixed-rate instruments.

**A15. What is Funds Transfer Pricing and how does it relate to ALM?**

FTP is the internal mechanism that charges each business unit for the rate and liquidity risk embedded in its products, transferring that risk to a central Treasury/ALM desk. Origination units keep a clean credit spread; the rate mismatch is pooled centrally where it is measured against ALCO limits and hedged.

---

## Section B — Numerical / Applied (full solutions)

**B1. Basic repricing gap and ΔNII.** RSA = ₹600 cr, RSL = ₹700 cr. Find the gap, classify the bank, and compute ΔNII for a +150 bps parallel shock.

GAP = RSA − RSL = 600 − 700 = **−₹100 cr** → **liability-sensitive**.
ΔNII ≈ GAP × Δr = (−100) × (+0.015) = **−₹1.5 cr**. NII falls by ₹1.5 cr when rates rise 150 bps.

*Cross-check from flows:* extra interest earned = 600 × 0.015 = +₹9 cr; extra interest paid = 700 × 0.015 = +₹10.5 cr; net = 9 − 10.5 = −₹1.5 cr. ✓

**B2. Symmetry / falling rates.** Same bank, rates *fall* 150 bps. What happens to NII?

ΔNII = (−100) × (−0.015) = **+₹1.5 cr**. A liability-sensitive bank *gains* when rates fall, because its cheaper funding reprices down faster than its asset yields. ✓

**B3. Gap ratio and relative gap.** Total assets = ₹1,000 cr, RSA = 600, RSL = 700. Compute the gap ratio and relative gap.

Gap ratio = RSA / RSL = 600 / 700 = **0.857** (< 1 confirms liability-sensitive).
Relative gap = GAP / Total Assets = −100 / 1,000 = **−10%** of assets.

**B4. Cumulative gap across buckets.** A bank reports these bucket gaps (₹ cr): 0–3m: +40; 3–6m: −90; 6–12m: −60; 1–2y: +30. Find the cumulative 1-year gap and ΔNII for +100 bps.

Cumulative 1-yr gap = 40 + (−90) + (−60) = **−₹110 cr** (buckets up to 12 months only; the 1–2y bucket is excluded).
ΔNII(1yr) ≈ −110 × 0.01 = **−₹1.1 cr**. The bank is liability-sensitive within a year.

**B5. Duration gap and ΔEVE.** A = ₹1,000 cr, D_A = 4.0; L = ₹900 cr, D_L = 1.5. Find k, the duration gap, and ΔEVE for a +100 bps shock.

k = L/A = 900/1,000 = 0.9.
D_GAP = D_A − k·D_L = 4.0 − 0.9 × 1.5 = 4.0 − 1.35 = **2.65 years** (positive → EVE falls when rates rise).
ΔEVE ≈ − D_GAP × A × Δy = − 2.65 × 1,000 × 0.01 = **−₹26.5 cr**.

Equity's economic value drops from ₹100 cr to ₹73.5 cr — a **26.5% hit from a 1% rate move**. That is leverage amplification.

**B6. Reconcile B5 leg by leg.** Rebuild the ΔEVE from the asset and liability value changes separately.

ΔPV(assets) = − D_A × A × Δy = − 4.0 × 1,000 × 0.01 = **−₹40 cr**.
ΔPV(liabilities) = − D_L × L × Δy = − 1.5 × 900 × 0.01 = **−₹13.5 cr**.
ΔEVE = ΔA − ΔL = (−40) − (−13.5) = **−₹26.5 cr**. ✓ Matches B5 exactly.

**B7. Immunise the balance sheet.** Using B5 (D_A = 4.0, k = 0.9), find (a) the asset duration that immunises equity holding D_L = 1.5, and (b) the liability duration that immunises holding D_A = 4.0.

Immunisation requires D_GAP = 0, i.e. D_A = k·D_L.
(a) Target D_A = k·D_L = 0.9 × 1.5 = **1.35 years** (slash asset duration, e.g. swap long fixed loans to floating).
(b) Target D_L = D_A / k = 4.0 / 0.9 = **4.44 years** (fund with much longer-dated liabilities).

*Verify (a):* ΔA = −1.35 × 1,000 × 0.01 = −13.5; ΔL = −1.5 × 900 × 0.01 = −13.5; ΔEVE = −13.5 − (−13.5) = **0**. ✓

**B8. The two lenses disagree (the SVB trap).** A bank funds a 10-year fixed-rate bond (₹1,000 cr, D_A = 8.0) entirely with 1-year deposits (₹900 cr, D_L = 1.0) that roll at the same spread. Compute (a) the 1-year repricing gap and ΔNII for +200 bps, and (b) the duration gap and ΔEVE for +100 bps. Equity = ₹100 cr.

(a) Within the 1-year bucket both the bond rate and the deposit rate are fixed → RSA ≈ 0, RSL ≈ 0 → **gap ≈ 0**, so **ΔNII ≈ 0**. The earnings model says "safe."
(b) k = 900/1,000 = 0.9. D_GAP = 8.0 − 0.9 × 1.0 = **7.1 years**. ΔEVE = − 7.1 × 1,000 × 0.01 = **−₹71 cr** — 71% of the ₹100 cr equity wiped out. The value model screams "danger."

Both are correct: they answer different questions. The 12-month earnings model is blind to the 9 years of exposure beyond its horizon. This is precisely what felled Silicon Valley Bank. ✓

**B9. Net interest margin.** A bank earns NII of ₹48 cr on earning assets of ₹1,200 cr. Compute the NIM. If a +200 bps shock cuts NII by ₹4 cr (unchanged asset base), what is the new NIM?

NIM = NII / earning assets = 48 / 1,200 = **4.0%**.
New NII = 48 − 4 = 44 cr → new NIM = 44 / 1,200 = **3.67%**. The 33 bps compression is the earnings-at-risk expressed as a margin.

**B10. Back out the shock.** A bank's duration gap is 3.0 years, assets ₹2,000 cr, and a rate move produced ΔEVE = −₹30 cr. What parallel shock occurred?

ΔEVE = − D_GAP × A × Δy → Δy = − ΔEVE / (D_GAP × A) = − (−30) / (3.0 × 2,000) = 30 / 6,000 = 0.005 = **+50 bps**.

**B11. Outlier-test check.** Tier 1 capital = ₹500 cr. Across the six Basel scenarios the worst ΔEVE is −₹90 cr. Is the bank an outlier?

Threshold = 15% × Tier 1 = 0.15 × 500 = ₹75 cr. Worst loss ₹90 cr > ₹75 cr → **yes, the bank is a supervisory outlier** and would face heightened scrutiny / potential capital add-ons. The ratio is 90/500 = 18% of Tier 1.

**B12. Standardised (beta-weighted) gap.** RSA = ₹600 cr with asset beta 1.0; RSL = ₹700 cr with deposit beta 0.6. Compute the standardised gap and ΔNII for +100 bps, and compare to the plain-gap answer.

Standardised gap = (RSA × β_A) − (RSL × β_L) = (600 × 1.0) − (700 × 0.6) = 600 − 420 = **+₹180 cr**.
ΔNII ≈ 180 × 0.01 = **+₹1.8 cr** — the bank actually *gains* on a rate rise once low deposit betas are accounted for.

Contrast: the plain gap is 600 − 700 = −100 cr → −₹1.0 cr. The sticky, low-beta deposits flip the sign: the bank looks liability-sensitive on paper but is asset-sensitive in behaviour. This is why betas matter. ✓

**B13. Convexity leak on an "immunised" book.** A bank has D_GAP = 0 but its assets have far higher convexity than its liabilities. Qualitatively, what happens to EVE for a *large* parallel move, and why doesn't immunisation protect it?

Duration is a first-order (linear) approximation. With D_GAP = 0 the linear term vanishes, so *small* moves leave EVE unchanged. For a *large* move the second-order term dominates: `ΔEVE ≈ −D_GAP·A·Δy + ½·(C_A·A − C_L·L)·Δy²`. Immunisation only neutralised the linear channel; convexity, yield-curve twists, and optionality still leak through — so it is not a risk-free hedge.

---

## Section C — Interview-Style (with model answers)

**C1. "Explain interest-rate risk in the banking book to a board member in thirty seconds."**

Model answer: "We take in short-term deposits and lend long-term at fixed rates — that maturity transformation is our business, but it's also a bet. If rates rise, our deposits reprice up quickly while our fixed loans keep earning the old rate, so our margin gets squeezed. We measure that two ways: the near-term hit to income, and the hit to the firm's net worth if we marked everything to market. We keep both inside board-approved limits and hedge the rest with swaps. Nobody has to default for us to lose money — the timing mismatch alone does it."

**C2. "What's the difference between the earnings lens and the value lens, and why keep both?"**

Model answer: "The earnings lens uses the repricing gap to estimate the change in net interest income over the next twelve months — a short-horizon flow measure, ΔNII ≈ gap × Δr. The value lens uses the duration gap to estimate the change in economic value of equity over the *whole* life of the book, ΔEVE ≈ −D_GAP × A × Δy. We keep both because they can disagree: a long fixed asset funded short shows a near-zero one-year gap yet a massive duration gap. Passing one is not passing the other, which is why Basel mandates both."

**C3. "A bank has a negative repricing gap. What does that mean and how would you hedge it?"**

Model answer: "Negative gap means rate-sensitive liabilities exceed rate-sensitive assets — the bank is liability-sensitive, so net interest income *falls* if rates rise. To hedge, I'd pay fixed and receive floating on an interest-rate swap, which converts floating funding into synthetic fixed, or converts fixed assets into synthetic floating — either way it offsets the exposure. Alternatives: buy interest-rate caps for asymmetric protection, or reshape the balance sheet by issuing longer-term deposits to lengthen liability duration. The choice depends on cost, accounting treatment, and the bank's rate view."

**C4. "How can a bank look completely safe on net interest income yet be dangerously exposed?"**

Model answer: "Its risk lives beyond the twelve-month gap window. If it holds long-duration fixed-rate assets funded with short deposits, the one-year gap is near zero — near-term NII barely moves — but the duration gap is enormous, so a rate rise hollows out the economic value of equity. That is exactly what happened to Silicon Valley Bank: safe Treasuries, so no credit problem, but funded with hot uninsured deposits. When rates rose 500 bps the bonds lost about fifteen billion of value and the bank was gone. The earnings model waved it through; the value model would have caught it."

**C5. "Why does a 1% rate move hit equity by 20–30%?"**

Model answer: "Leverage. The ΔEVE formula scales by *total assets*, not by equity — ΔEVE ≈ −D_GAP × A × Δy. Equity is a thin residual, often eight to ten percent of assets, so the same rupee change in asset value is a large fraction of the small equity base. A bank is essentially a leveraged bond portfolio wearing a deposit franchise; duration acts on the whole portfolio but lands entirely on the sliver of equity."

**C6. "What's the single hardest judgement call in ALM, and why?"**

Model answer: "Modelling non-maturity deposits. Contractually they're withdrawable on demand, so you'd call them instantly rate-sensitive. Behaviourally they're sticky: core balances stay for years and their rate passes through only partially, a low beta. So we model them as a blend of short and multi-year tranches. This one assumption drives *both* the repricing gap and the EVE duration, so getting it wrong corrupts every downstream number — which is why Basel caps the assumed behavioural life."

**C7. "What is duration immunisation and what are its blind spots?"**

Model answer: "Immunisation means setting the duration gap to zero — D_A = k·D_L — so a small parallel rate shift leaves the economic value of equity unchanged. Its blind spots: it protects *value*, not earnings; it works only for *small, parallel* moves; and it leaks through convexity for large moves, through yield-curve twists like steepeners and flatteners, through basis risk when assets and liabilities track different indices, and through embedded optionality like mortgage prepayments and deposit runoff. It's a first-order static hedge that has to be rebalanced as rates and the curve move — not a set-and-forget riskless position."

**C8. "Walk me through the Basel IRRBB framework."**

Model answer: "It's a Pillar 2 standard from 2016. Banks compute both ΔEVE and ΔNII under six prescribed shock scenarios — parallel up/down, steepener, flattener, short-rate up/down. The supervisory outlier test flags a bank if the worst ΔEVE loss across those six exceeds fifteen percent of Tier 1 capital, and it caps non-maturity-deposit behavioural life so banks can't game a flattering number. Unlike Pillar 1 market risk it sets no rigid capital charge; it drives supervisory dialogue and potential add-ons."

**C9. "Are rising rates good or bad for a bank?"**

Model answer: "It depends entirely on the balance sheet, so I'd resist a blanket answer. A liability-sensitive bank — negative gap — is hurt on near-term income when rates rise. But a bank with sticky, low-beta deposits can actually see its net interest margin *expand*, because asset yields reprice faster than deposit costs. And separately, over the value horizon, almost every maturity-transforming bank has a positive duration gap, so rising rates reduce the economic value of equity regardless of the earnings picture. So the honest answer is: name the horizon and show me the balance sheet's betas and durations first."

---

## Section D — MCQs (with reasoning)

**D1. A bank has RSA = ₹500 cr and RSL = ₹650 cr. It is:**
A) Asset-sensitive B) Liability-sensitive C) Matched D) Immunised

**Answer: B.** GAP = 500 − 650 = −₹150 cr < 0 → more funding reprices than assets → liability-sensitive → NII falls if rates rise. "Immunised" refers to a zero *duration* gap, not the repricing gap, so D is wrong.

**D2. Which item is rate-sensitive within a 6-month bucket?**
A) A 10-year fixed-rate mortgage B) A floating-rate loan resetting monthly C) A building D) Equity

**Answer: B.** Rate sensitivity is about *when the rate resets*, not maturity. The floating loan resets inside the bucket; the fixed mortgage's rate is locked for years; buildings and equity carry no interest rate. Classic maturity-vs-repricing trap.

**D3. ΔNII ≈ GAP × Δr. A bank with a positive gap of +₹200 cr experiences a −50 bps shock. ΔNII is:**
A) +₹1.0 cr B) −₹1.0 cr C) +₹0.1 cr D) −₹0.1 cr

**Answer: B.** ΔNII = (+200) × (−0.005) = −₹1.0 cr. An asset-sensitive bank *loses* income when rates fall, because its larger rate-sensitive asset base reprices down. Sign discipline is the point.

**D4. The duration gap formula is:**
A) D_A − D_L B) D_A − k·D_L, k = L/A C) D_A + k·D_L D) k·D_A − D_L

**Answer: B.** The liability duration is scaled by the leverage factor k = L/A because liabilities fund only a fraction of assets. Omitting k (option A) overstates the liability offset and is the most common error.

**D5. A bank has D_A = 5, D_L = 2, A = ₹1,000 cr, L = ₹900 cr. For a +100 bps shock, ΔEVE is closest to:**
A) −₹32 cr B) −₹30 cr C) −₹50 cr D) −₹18 cr

**Answer: A.** k = 900/1,000 = 0.9. D_GAP = 5 − 0.9×2 = 5 − 1.8 = 3.2. ΔEVE = −3.2 × 1,000 × 0.01 = −₹32 cr. Option C (−50) forgets to scale by k; D uses the wrong leg.

**D6. A zero repricing gap guarantees:**
A) Zero interest-rate risk B) Zero near-term NII sensitivity to a parallel shock, but EVE can still be exposed C) An immunised balance sheet D) Zero ΔEVE

**Answer: B.** A zero repricing gap neutralises near-term earnings only. The duration gap — and hence EVE — can be large (the 10-year-bond-funded-short case). This is the exact reason Basel requires both metrics.

**D7. Why does leverage amplify ΔEVE relative to the equity base?**
A) Because equity has high duration B) Because ΔEVE scales by total assets, while equity is a thin residual C) Because liabilities have zero duration D) Because of convexity

**Answer: B.** ΔEVE ≈ −D_GAP × A × Δy scales by *A*, but the hit lands on equity (≈ A − L), a small fraction of A. So a modest percentage move in assets is a large percentage move in equity. Convexity (D) is a second-order effect, not the amplification mechanism.

**D8. Under Basel IRRBB, a bank is a supervisory outlier if:**
A) ΔNII exceeds 15% of net income B) Maximum ΔEVE loss across six shock scenarios exceeds 15% of Tier 1 capital C) Any single ΔEVE exceeds 20% of CET1 D) The repricing gap exceeds 10% of assets

**Answer: B.** The 2016 standard's outlier test is on the *worst* ΔEVE across the six prescribed scenarios versus 15% of Tier 1. The other options mix up the metric, threshold, or capital base.

**D9. To hedge a liability-sensitive bank against rising rates, the classic swap is:**
A) Receive fixed / pay floating B) Pay fixed / receive floating C) Buy a floor D) Sell a cap

**Answer: B.** Paying fixed / receiving floating gains value when rates rise, offsetting the NII compression a liability-sensitive bank suffers. Receiving fixed (A) would double down on the exposure; a floor (C) protects against falling rates; selling a cap (D) adds risk.

**D10. The biggest modelling judgement in ALM is:**
A) The discount rate on Tier 1 capital B) The behavioural life and rate beta of non-maturity deposits C) The recovery rate on defaulted loans D) The trading-book VaR window

**Answer: B.** NMD behaviour drives both the repricing bucket and the EVE duration, and it's a judgement call, so Basel caps the assumed life. Recovery rate (C) is credit risk; VaR window (D) is trading-book market risk — different chapters.

**D11. Modified duration equals:**
A) D_Macaulay × (1 + y) B) D_Macaulay / (1 + y) C) D_Macaulay + y D) D_Macaulay − y

**Answer: B.** D_mod = D_Macaulay / (1 + y), giving ΔP/P ≈ −D_mod × Δy. Multiplying instead of dividing (A) inflates the sensitivity.

**D12. Immunisation (D_GAP = 0) fails to protect against all of the following EXCEPT:**
A) Small parallel shifts B) Yield-curve twists C) Convexity on large moves D) Deposit-runoff optionality

**Answer: A.** Immunisation is *designed* to neutralise small parallel shifts. It leaks on twists, convexity for large moves, basis, and optionality.

---

*Self-verification note.* Every numerical answer was rebuilt two ways where possible: repricing-gap ΔNII figures reconcile with the direct RSA/RSL interest-flow calculation (B1), and duration ΔEVE figures reconcile with the leg-by-leg ΔPV(assets) − ΔPV(liabilities) identity (B6/B7). Sign conventions follow: negative repricing gap = liability-sensitive = hurt by rising rates; positive duration gap = hurt by rising rates.
