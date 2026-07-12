# Cost of Capital

## Snapshot
Cost of capital = minimum return a project must earn to leave firm value unchanged = the **hurdle rate**. WACC (Ko) is the blended cost of the whole capital pool; projects must beat it to create value. Build WACC bottom-up: each component cost, then weighted blend.

## Core concepts
- **Three equivalent definitions:** financing view (return demanded by suppliers), opportunity-cost view (next-best return of equal risk), break-even view (return keeping share price unchanged).
- **Component decomposition:** K = r₀ (riskless) + b (business-risk premium) + f (financial-risk premium). Equity carries both premiums fully → dearest.
- **Explicit cost** (cash paid: interest/dividend) vs **implicit cost** (opportunity, e.g. retained earnings: zero explicit, real implicit).
- **Ordering (self-check):** Kd < Kp < Kr ≤ Ke. Interest is tax-deductible; dividends are not → compute Kd post-tax.
- **Pooling principle:** use pooled target-structure WACC, not the specific cheap source funding a project (financing is fungible).
- **Average** (existing pool) vs **marginal** (next rupee raised) — new projects use marginal.

## Key provisions / rules

| Source | Formula | Notes |
|---|---|---|
| Irredeemable debt | Kd = I(1−t) ÷ NP | tax shield on interest only |
| Redeemable debt | Kd = [I(1−t) + (RV−NP)/n] ÷ [(RV+NP)/2] | premium term NOT tax-adjusted |
| Debt by YTM | Kd = L + [NPV_L ÷ (NPV_L − NPV_H)] × (H − L) | exact/interpolation when demanded |
| Term loan | Kd = rate × (1−t) | no premium/discount |
| Zero-coupon bond | Kd = (RV/NP)^(1/n) − 1 (pre-tax) | discount accretes; tax per problem |
| Irredeemable preference | Kp = PD ÷ NP | no (1−t) |
| Redeemable preference | Kp = [PD + (RV−NP)/n] ÷ [(RV+NP)/2] | no (1−t) |
| Equity — Gordon | Ke = D₁/P₀ + g | D₁ = D₀(1+g); use NP for fresh issue |
| Equity — CAPM | Ke = Rf + β(Rm − Rf) | only systematic risk priced |
| Equity — Bond yield + premium | Ke = firm's debt yield + risk premium | fallback |
| Equity — Earnings yield | Ke ≈ E/P | only under zero growth + full payout |
| Retained earnings | Kr = Ke | opportunity cost; NOT free |
| Retained (with adj.) | Kr = Ke(1−tp)(1−b) | only if personal tax/brokerage given |
| WACC | Ko = Σ (component cost × weight) | all costs post-tax |
| Break point | (Amount of cheaper source) ÷ (weight of that source) | — |

- **Growth rate:** g = (D_now/D_past)^(1/n) − 1 (count *intervals*, not data points); or g = b × r (retention × ROE).
- **Weights hierarchy (for financing decision): marginal/target > market > book.** Market weights preferred because they reflect today's opportunity cost; book weights are historical/sunk. Retained earnings folded into equity's market value.
- **Post-tax throughout** — WACC discounts post-tax cash flows; never mix pre-tax Kd or market weight with book cost.
- **Tax-shield caveat:** worthless if firm has no taxable profit → use pre-tax coupon.
- **Marginal cost of capital (MCC):** WACC of incremental funds; build tranche-by-tranche across break points (can rise OR fall). Pair MCC schedule with Investment Opportunity Schedule → optimal capital budget at the crossing.
- **Sanity test:** WACC lies between lowest and highest component cost.

## Worked mini-example
Fresh-capital WACC with retained-earnings break point. Target: Equity 50%, Pref 10%, Debt 40%; tax 30%. Retained earnings ₹15,00,000. Ke(retained)=18.00%, Ke(fresh)=18.71%, Kp=12.04%, Kd=7.69%. Raise ₹50,00,000.
- Break point = 15,00,000 ÷ 0.50 = **₹30,00,000**.
- MCC first ₹30L (retained equity): 0.50×18.00 + 0.10×12.04 + 0.40×7.69 = **13.28%**.
- MCC beyond ₹30L (fresh equity): 0.50×18.71 + 0.10×12.04 + 0.40×7.69 = **13.64%**.
- Weighted for full ₹50L: (30×13.28 + 20×13.64)/50 = **13.42%** → hurdle for the raise; a 13% project is rejected.

## Exam traps & must-remember
1. Forgetting tax shield on debt — only **interest** gets it, never preference/equity dividends.
2. Do NOT tax-adjust the redemption premium/discount term (RV−NP)/n.
3. Retained earnings NOT free → Kr = Ke.
4. Use **D₁ (= D₀(1+g))**, not D₀, in Gordon.
5. Fresh issues use **net proceeds** (net of flotation), not market price → fresh equity > retained.
6. Book vs market weights: use market if given; fold retained earnings into equity market value.
7. Ke < Kd is impossible — signals an error.
8. New project on new money → hurdle is **marginal** cost, not historical WACC.
9. CAPM premium = β(Rm − Rf) added to Rf; not β × Rm.
10. Weights must sum to 1.0000 (show totals row).
11. Miscounting growth period n (year 0 to 5 = 5 intervals).
12. Never mix pre-tax cost with market weight, or book weight with market cost.
13. MCC does not only rise — a later cheaper tranche can lower a step.
14. Loss-making firm → no tax shield → use pre-tax coupon.
15. DDT abolished post-2020 — only gross up preference dividend if problem says so.
16. Earnings yield E/P = Ke only at zero growth + full payout.

## One-line recall
- Cost of capital = hurdle rate; beat WACC/MCC → create value, else destroy.
- Kd < Kp < Kr ≤ Ke; interest tax-deductible so Kd = I(1−t).
- Redeemable: [annual cost] ÷ [average funds]; premium term not tax-adjusted.
- Gordon Ke = D₁/P₀ + g; CAPM Ke = Rf + β(Rm−Rf); Kr = Ke (opportunity cost, not free).
- Weights: marginal > market > book; all costs post-tax; WACC lies between extremes.
- Break point = cheap source ÷ its weight; build MCC schedule tranche-by-tranche.
