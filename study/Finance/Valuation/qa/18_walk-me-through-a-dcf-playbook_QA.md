# Q&A — The Valuation Playbook: Walk Me Through a DCF / Value This Company

This bank mixes **theory** (model answers plus "how to say it in an interview") and **numerical problems** (fully solved, self-verified, reconciling). Work them out before reading the solutions.

---

## Theory Questions

### Q1. Walk me through a DCF. (The core prompt)

**Model answer.** A DCF values a company as the present value of the cash it will generate for all capital providers.

1. **Project unlevered free cash flow (FCFF):** start from EBIT, tax it to NOPAT (`EBIT × (1−t)`), add back D&A, subtract capex and the change in net working capital. Forecast 5–10 years.
2. **Discount at WACC** — the blended after-tax cost of debt and equity — because FCFF belongs to both.
3. **Add a terminal value** for cash beyond the horizon: Gordon growth (`FCFFₙ(1+g)/(WACC−g)`) or an exit EBITDA multiple; discount it back at the terminal-year factor.
4. **Sum** discounted FCFF and TV → **enterprise value.**
5. **Bridge to equity:** subtract net debt, preferred, minority interest; add non-operating assets.
6. **Divide by diluted shares** → intrinsic value per share, compared to the market price.

**How to say it:** Keep it to six moves and *end with a sanity check* — "and I'd confirm the terminal value isn't more than ~80% of EV and that my implied exit multiple matches where comps trade." That one line signals seniority.

---

### Q2. Why do you use FCFF and WACC rather than FCFE and cost of equity?

**Model answer.** Both are valid, but they answer different questions and must be kept internally consistent. FCFF is *unlevered* — it ignores capital structure, so it isolates operating performance and is capital-structure-neutral, which makes it cleaner for comparison and for firms whose leverage will change. Because FCFF belongs to all capital providers, it must be discounted at the blended rate (WACC), producing enterprise value. FCFE is levered (post-interest, post-debt-flows), belongs only to equity, and must be discounted at cost of equity, producing equity value directly. The industry default is FCFF/WACC because it separates the two things you want to reason about independently: how good the business is (operations) and how it's financed (capital structure).

**How to say it:** "Match the cash flow to its claimants. Unlevered cash, blended rate, enterprise value — the consistency *is* the method."

---

### Q3. How do you get from enterprise value to equity value, and then to per share?

**Model answer.** EV is the operating business's value, available to everyone. Strip out the senior claims and add what EV misses:

`Equity = EV − Net debt − Preferred − Minority interest − debt-like items (e.g. unfunded pensions) + non-operating assets (investments, associates).`

Net debt = total debt − cash. Then divide equity value by **diluted** shares (treasury method on in-the-money options and RSUs) for value per share.

**Trap flagged:** if you value with an *equity* multiple (P/E, P/B) you already have equity value — don't subtract net debt again.

---

### Q4. Your DCF disagrees with your comps by 30%. What do you do?

**Model answer.** The divergence is information, not noise. First check for mechanical errors (mismatched forward/trailing metrics, bridge mistakes). If it's real, ask which method's assumptions are more aggressive. If the DCF is *higher*, my growth/margin/terminal assumptions are more optimistic than what the market prices into peers — I either defend that with a specific, credible thesis or trim toward the market. If the DCF is *lower*, either the market is over-paying for the sector or my forecast is too conservative. I present a *range* spanning both and state explicitly what each end represents, rather than silently averaging.

**How to say it:** "I don't average away a 30% gap — that gap is the most interesting thing in the analysis. I interrogate it and tell you which assumption drives it."

---

### Q5. Why triangulate three methods instead of trusting the "best" one?

**Model answer.** Each method has a *structural* blind spot, and they're different, so the errors are partly independent. DCF's weakness is the terminal value and discount rate — the least observable inputs swing the answer most. Comps inherit any sector-wide mispricing. Precedents embed control premiums and go stale. When three methods with different blind spots converge, the agreement is unlikely to be coincidence — confidence rises. When they diverge, the pattern points to which assumption to question. It's the logic of three independent measurements: the intersection beats any single reading.

**How to say it:** "Different blind spots, so I trust the overlap, not any one number."

---

### Q6. What is the single biggest driver of a DCF, and how do you keep it honest?

**Model answer.** The terminal value — typically 70–80% of enterprise value — and within it the spread `WACC − g`. A half-point move in WACC or g shifts the answer more than the entire explicit forecast. I discipline it three ways: (1) keep `g` below long-run GDP and well below WACC; (2) compute the **implied exit multiple** (`TV / terminal EBITDA`) and check it against sector trading multiples; (3) if using an exit multiple, back-solve the **implied perpetuity growth** and confirm it's economically sane.

---

### Q7. How would you value a company with negative earnings / no free cash flow?

**Model answer.** A near-term DCF is unreliable because all the value sits in the terminal state. So I lean on relative and path-based tools: EV/Sales or EV/Gross Profit against high-growth peers; a longer-dated DCF that explicitly models the path to profitability (when margins inflect, steady-state margin, reinvestment) under weighted scenarios; and precedent per-user or per-revenue metrics. I present scenarios and a range, not false precision — the value is a probability-weighted bet on reaching a profitable steady state.

---

### Q8. How does valuing a bank differ, and why?

**Model answer.** For financials, FCFF/WACC breaks down because debt is raw material, not just financing, and interest is operating income — you can't cleanly separate operating from financing cash. So I switch to equity-side methods: a **dividend discount model** or a **residual income / excess-returns model** discounted at cost of *equity*, and value on **P/B versus ROE** rather than EV/EBITDA. The insight: for a bank, leverage *is* the business, so you value the equity directly.

**How to say it:** "Different tool box — equity-side, cost of equity, P/B vs ROE. EV multiples don't work when leverage is the product."

---

### Q9. Precedent transactions come in highest of your three methods. Is that a red flag?

**Model answer.** No — it's expected and it's *confirming*. Precedents are prices paid to *acquire and control* businesses, so they embed a control premium (typically 20–40% over the undisturbed trading price) and often synergy expectations. They answer "what would someone pay to own this?" not "what does it trade for in the public market?" I'd worry if precedents came in *below* trading comps — that would suggest either stale/distressed deals or a currently frothy market. So precedents form the *takeout ceiling*, and I keep them conceptually separate from standalone value.

---

### Q10. You have ten minutes and a company name. Talk me through your approach.

**Model answer.** Frame the business in one sentence (how it makes money, what drives value). Then comps for a fast anchor — get revenue, a margin, and a peer multiple to bracket enterprise value. Then a rough intrinsic gut-check on FCFF. Critically, name the one or two assumptions the whole value hinges on. I'd deliver a defensible *range* and tell you exactly what would move it, rather than a precise number I can't defend. Front-load the assumptions that swing the answer; defer the ones that don't.

---

### Q11. What sanity checks do you run before quoting a DCF value?

**Model answer.** My battery: (1) **TV as % of EV** — flag if > 80–85%; (2) **implied exit multiple** vs sector; (3) **implied perpetuity growth** below GDP and below WACC; (4) **WACC − g** comfortably positive (≥ ~1.5%); (5) the *whole-DCF* **implied EV/EBITDA and P/E** vs comps; (6) **margin trajectory** justified by a mechanism; (7) **growth-reinvestment consistency**; (8) **bridge reconciliation** (signs, no double-counted cash, diluted shares); (9) the gut check — is the implied market cap sane for this company?

---

### Q12. How do you turn a valuation into a recommendation?

**Model answer.** Connect value to price. In equity research: a rating (Buy/Hold/Sell), a target price (intrinsic anchor or forward-multiple target), the upside/downside vs current price (`(Intrinsic − Price)/Price`), plus catalysts that close the gap and risks that widen it. In M&A: a value range for the board framed around the football field, with the negotiation posture. In credit: EV cushion over debt, coverage, and downside value. A valuation that stops at a number hasn't finished the job.

---

## Numerical Problems

### Q13. Full DCF to per share (self-contained).

A company: FCFF for years 1–5 = ₹120, ₹135, ₹150, ₹165, ₹180 (₹ cr). WACC = 11%, terminal growth = 3%. Net debt = ₹300, minority interest = ₹40, non-operating investments = ₹60. Diluted shares = 20 cr. Find intrinsic value per share (end-of-year discounting).

**Solution.**

Terminal value at year 5: `TV = 180 × 1.03 / (0.11 − 0.03) = 185.4 / 0.08 = 2,317.5.`

Discount factors at 11%: y1 0.9009, y2 0.8116, y3 0.7312, y4 0.6587, y5 0.5935.

| Year | CF | Factor | PV |
|------|-----|--------|-----|
| 1 | 120 | 0.9009 | 108.1 |
| 2 | 135 | 0.8116 | 109.6 |
| 3 | 150 | 0.7312 | 109.7 |
| 4 | 165 | 0.6587 | 108.7 |
| 5 | 180 | 0.5935 | 106.8 |
| TV | 2,317.5 | 0.5935 | 1,375.5 |

Sum PV(FCFF) = 108.1 + 109.6 + 109.7 + 108.7 + 106.8 = **542.9.**
PV(TV) = **1,375.5.**
**EV = 542.9 + 1,375.5 = ₹1,918.4 cr.**
Equity = 1,918.4 − 300 − 40 + 60 = **₹1,638.4 cr.**
Per share = 1,638.4 / 20 = **₹81.9.**

**Sanity:** TV/EV = 1,375.5/1,918.4 = **72%** (fine). WACC − g = 8% (comfortable). ✓

---

### Q14. EV-to-equity bridge with net cash.

A company has EV of ₹4,000 cr, total debt ₹500, cash ₹900, preferred ₹0, minority ₹100, investments in associates ₹150. It has 40 cr basic shares and 5 cr in-the-money options struck at ₹80 while the stock trades at ₹120. Find equity value and diluted per-share value.

**Solution.**

Net debt = 500 − 900 = **−400** (net *cash* of 400).
Equity = EV − Net debt − Preferred − Minority + Investments = 4,000 − (−400) − 0 − 100 + 150 = 4,000 + 400 − 100 + 150 = **₹4,450 cr.**

Treasury method on options: net new shares = 5 × (120 − 80)/120 = 5 × 0.3333 = **1.667 cr.**
Diluted shares = 40 + 1.667 = **41.667 cr.**

Per share = 4,450 / 41.667 = **₹106.8.**

**Note the two traps handled:** net cash is *added* (equity > EV), and dilution *raises* the share count, lowering per-share value from a naïve 4,450/40 = ₹111.3 to ₹106.8. ✓

---

### Q15. Terminal value: Gordon vs exit multiple, and the implied cross-check.

Year-5 FCFF = ₹200, year-5 EBITDA = ₹450. WACC = 10%, g = 4%. (a) Gordon TV and its implied exit multiple. (b) If instead you used an 8x exit multiple, what perpetuity growth does it imply?

**Solution.**

(a) `TV = 200 × 1.04 / (0.10 − 0.04) = 208 / 0.06 = ₹3,466.7.`
Implied exit multiple = 3,466.7 / 450 = **7.7x.**

(b) 8x exit → TV = 8 × 450 = ₹3,600. Back-solve g from `3,600 = 200(1+g)/(0.10 − g)`:
`3,600(0.10 − g) = 200(1+g)` → `360 − 3,600g = 200 + 200g` → `160 = 3,800g` → `g = 0.0421 = 4.21%.`

**Reconciliation:** the Gordon method at 4% growth implies 7.7x; the 8x exit multiple implies 4.2% growth. The two methods are consistent and mutually validating — both land near 4% growth / ~8x. If they'd diverged wildly (say Gordon implied 15x), that would flag an over-optimistic `g`. ✓

---

### Q16. Comps: apply a multiple and bridge.

Peers trade at a median EV/EBITDA of 10.0x. Target EBITDA (forward) = ₹350 cr, net debt ₹600, minority ₹0, no non-op assets, 25 cr shares. Also give the range at 8.5x–11.5x.

**Solution.**

Implied EV = 350 × 10.0 = **₹3,500 cr.**
Equity = 3,500 − 600 = **₹2,900 cr.**
Per share = 2,900 / 25 = **₹116.0.**

Range:
- 8.5x → EV 2,975 → equity 2,375 → **₹95.0.**
- 11.5x → EV 4,025 → equity 3,425 → **₹137.0.**

So comps imply **₹95–₹137, midpoint ₹116.** ✓

---

### Q17. Triangulation and football field.

For one company you have: DCF ₹110 (range ₹98–₹122 on WACC sensitivity); trading comps ₹116 (range ₹95–₹137); precedents 12x EBITDA on ₹350 EBITDA, net debt ₹600, 25 cr shares. Build the precedent per-share value and reconcile all three; state a standalone anchor and a takeout ceiling.

**Solution.**

Precedents: EV = 12 × 350 = 4,200; equity = 4,200 − 600 = 3,600; per share = 3,600/25 = **₹144.0.** (Range 11x–13x → EV 3,850–4,550 → equity 3,250–3,950 → **₹130–₹158.**)

| Method | Low | Point | High |
|--------|-----|-------|------|
| DCF | 98 | 110 | 122 |
| Trading comps | 95 | 116 | 137 |
| Precedents | 130 | 144 | 158 |

**Reading:** DCF (₹110) and comps (₹116) overlap heavily in the **₹98–₹137** band and agree around **₹110–₹116** — that's the standalone public-market value; I'd anchor **~₹113.** Precedents sit clearly higher at ₹130–₹158, the expected control-premium ceiling — that's the **takeover** number, not the trading value. 

**Statement:** "Standalone I value it **₹98–₹137, anchoring ~₹113** where DCF and comps converge. A strategic buyer could justify **₹130–₹158** on ~12x precedents. Two numbers, two questions." ✓

---

### Q18. Two-minute pressure valuation.

"₹800 cr revenue, 30% EBITDA margin, growing 15%, ₹100 cr net debt, 40 cr shares. Peers: 12x EV/EBITDA. Value it fast."

**Solution.**

EBITDA = 30% × 800 = **240.**
EV = 12 × 240 = **2,880.**
Equity = EV − net debt = 2,880 − 100 = **2,780.**
Per share = 2,780 / 40 = **₹69.5.**

**Say it:** "About ₹2.88k cr enterprise value at 12x, less ₹100 cr net debt, so ~₹2.78k cr equity — roughly **₹69–₹70 a share**. The swing variable is whether 15% growth is durable; at 12x the market's paying for a few years of it. If growth halves, the multiple compresses and so does the value." ✓

---

### Q19. Sensitivity: WACC and g on the same DCF.

Using year-5 FCFF = ₹180 and a base of WACC 11% / g 3% (from Q13, TV = ₹2,317.5), recompute the terminal value if (a) WACC falls to 10%, (b) g rises to 4% (WACC back to 11%), (c) both (WACC 10%, g 4%). Comment on TV sensitivity.

**Solution.**

Base (11%/3%): `180×1.03/(0.11−0.03) = 185.4/0.08 = 2,317.5.`
(a) 10%/3%: `180×1.03/(0.10−0.03) = 185.4/0.07 = 2,648.6` (+14.3%).
(b) 11%/4%: `180×1.04/(0.11−0.04) = 187.2/0.07 = 2,674.3` (+15.4%).
(c) 10%/4%: `180×1.04/(0.10−0.04) = 187.2/0.06 = 3,120.0` (+34.6%).

**Comment:** a single one-point move in either WACC or g swings the terminal value ~14–15%; moving both swings it ~35%. Since TV is the bulk of EV, this is *the* reason the WACC−g spread dominates a DCF and must be sanity-checked. Note WACC−g shrinks from 8% to 6% in case (c), and the value inflates non-linearly. ✓

---

### Q20. Implied multiple cross-check on a full DCF.

A DCF gives EV = ₹6,300 cr. The company's forward EBITDA = ₹700 cr and forward net income = ₹380 cr, net debt = ₹800, 100 cr shares. What EV/EBITDA and P/E does the DCF imply, and how do you use them?

**Solution.**

Implied EV/EBITDA = 6,300 / 700 = **9.0x.**
Equity = 6,300 − 800 = 5,500; per share = 55.0. EPS = 380/100 = ₹3.80.
Implied P/E = 55.0 / 3.80 = **14.5x** (equivalently equity value / net income = 5,500/380 = 14.5x). ✓

**Use:** compare these implied multiples to where peers trade. If comparable food companies trade at ~9x EV/EBITDA and ~15x P/E, this DCF is *consistent with the market* — strong cross-validation. If the DCF implied 20x EBITDA against a 9x peer set, I'd need a specific thesis for the premium or I'd revisit my growth/terminal assumptions. This is the most powerful single sanity check: it forces the intrinsic and relative worlds to reconcile.

---

### Q21. Mid-year convention effect.

Take FCFF y1–y5 = ₹120,135,150,165,180 and WACC 11% (from Q13). Recompute the PV of the *explicit* FCFF using the mid-year convention (exponent t−0.5) and compare to the end-of-year sum of ₹542.9.

**Solution.**

Mid-year factors at 11%: exponent 0.5,1.5,2.5,3.5,4.5 → 1.11^−0.5 = 0.9492, ^−1.5 = 0.8551, ^−2.5 = 0.7704, ^−3.5 = 0.6940, ^−4.5 = 0.6252.

| Year | CF | Mid-year factor | PV |
|------|-----|-----------------|-----|
| 1 | 120 | 0.9492 | 113.9 |
| 2 | 135 | 0.8551 | 115.4 |
| 3 | 150 | 0.7704 | 115.6 |
| 4 | 165 | 0.6940 | 114.5 |
| 5 | 180 | 0.6252 | 112.5 |

Mid-year sum = 113.9 + 115.4 + 115.6 + 114.5 + 112.5 = **571.9** vs end-of-year **542.9** — about **+5.3%.**

**Comment:** mid-year discounting assumes cash arrives mid-period rather than at year-end, so each flow is discounted for half a year less, lifting PV by roughly `(1+WACC)^0.5 − 1 ≈ 5.4%`. Apply it consistently — decide deliberately how the terminal value is treated and state your convention. ✓

---

### Q22. Net-debt sign and equity-multiple trap combined.

An analyst values a company two ways. (a) EV/EBITDA of 9x on EBITDA ₹500, then bridges with net debt of ₹700. (b) P/E of 15x on net income ₹250. The company has 50 cr shares. Reconcile the two equity values and identify any error.

**Solution.**

(a) EV = 9 × 500 = 4,500; equity = 4,500 − 700 = **3,850**; per share = 3,850/50 = **₹77.0.**
(b) Equity (P/E is an *equity* multiple) = 15 × 250 = **3,750**; per share = 3,750/50 = **₹75.0.** *No net-debt bridge* — that would be double-counting.

**Reconciliation:** the two land close (₹77 vs ₹75), which is reassuring — the EV and equity multiples are roughly consistent given this capital structure. **The trap:** if the analyst had subtracted net debt from the P/E-derived equity value (3,750 − 700 = 3,050 → ₹61), that would be flat wrong — P/E already delivers equity value. Only EV multiples require the net-debt bridge. ✓

---

*End of Q&A bank.*
