# Q&A — Multiples Deep Dive

A mix of theory (with model answers and "how to say it in an interview") and fully-solved numerical problems. All numbers are self-checked and reconcile.

---

### Q1 (Theory). What *is* a multiple, fundamentally?

**Answer.** A multiple is a ratio of value to a value driver — how many rupees of price you pay per rupee of a fundamental (earnings, EBITDA, sales, book). Fundamentally it is a **compressed DCF**: start from the constant-growth perpetuity `Value = CF/(r − g)`, divide both sides by a fundamental, and you get a multiple expressed purely in growth, risk and cash-conversion.

**Interview line:** "A multiple isn't a shortcut that avoids DCF — it *is* a DCF, compressed into one number. So a high or low multiple is only meaningful relative to what growth, returns and risk justify."

---

### Q2 (Theory). Equity multiples vs enterprise multiples — the rule.

**Answer.** Equity multiples put an equity value (price / market cap) over a flow that belongs to shareholders *after* financing — net income, book equity (P/E, P/B, PEG). Enterprise multiples put enterprise value over a flow that belongs to *all* capital providers *before* financing — EBITDA, EBIT, sales (EV/EBITDA, EV/EBIT, EV/Sales). **The numerator and denominator must be claimed by the same investors.** Market cap over EBITDA, or EV over net income, is a category error.

**Interview line:** "Match the claim. Equity claims over after-interest flows, whole-firm value over before-interest flows. Cross them and the ratio is meaningless."

---

### Q3 (Numerical). Build EV and compute the enterprise multiples.

**Given:** Price ₹150, shares 40 cr; debt ₹3,000 cr; cash ₹800 cr; preferred ₹200 cr; minority interest ₹100 cr; EBITDA ₹1,200 cr; D&A ₹300 cr.

**Solution.**
```
Market cap = 150 × 40 = ₹6,000 cr
EV = 6,000 + 3,000 + 200 + 100 − 800 = ₹8,500 cr
EBIT = 1,200 − 300 = ₹900 cr
EV/EBITDA = 8,500 / 1,200 = 7.08x
EV/EBIT   = 8,500 / 900   = 9.44x
```
**Reverse-check (EV → equity):** `8,500 − 3,000 − 200 − 100 + 800 = 6,000` ✅ matches market cap.

---

### Q4 (Theory). Why is EV/EBITDA the analyst's workhorse?

**Answer.** Three neutralities: (1) **capital-structure neutral** — EBITDA is before interest, so leverage doesn't distort it; (2) **accounting/D&A neutral** — before depreciation, so comparable across firms with different asset ages and depreciation policies; (3) roughly **tax neutral** — before tax. That makes it ideal for comparing companies with different financing, and for M&A/LBO where the buyer will change the capital structure anyway. **Caveat:** it ignores capex and working capital, so "EBITDA is not cash flow" — pair it with EV/EBIT or FCF for capital-heavy names.

---

### Q5 (Numerical). Same operations, different leverage — show P/E diverges but EV/EBITDA doesn't.

**Given:** Both firms: EBITDA ₹1,000 cr, D&A ₹200 cr, EBIT ₹800 cr, tax 25%, EV ₹8,000 cr. Firm U has no debt; Firm L has ₹4,000 cr debt @ 8%.

**Solution.**
```
Firm U: NI = 800 × (1−0.25) = 600; Equity = 8,000 − 0 = 8,000
        P/E = 8,000/600 = 13.3x ; EV/EBITDA = 8,000/1,000 = 8.0x
Firm L: Interest = 4,000×8% = 320; PBT = 800−320 = 480; NI = 480×0.75 = 360
        Equity = 8,000 − 4,000 = 4,000
        P/E = 4,000/360 = 11.1x ; EV/EBITDA = 8,000/1,000 = 8.0x
```
**Conclusion.** Identical EV/EBITDA (8.0x), different P/E (13.3x vs 11.1x). Leverage makes Firm L's P/E look cheaper but adds financial risk. EV/EBITDA neutralises financing — hence its use for cross-company comparison.

---

### Q6 (Numerical). Justified forward P/E and P/B from fundamentals.

**Given:** ROE 16%, Ke 11%, payout 45%.

**Solution.**
```
retention = 1 − 0.45 = 0.55
g = ROE × retention = 0.16 × 0.55 = 0.088 = 8.8%
Forward P/E = payout / (Ke − g) = 0.45 / (0.11 − 0.088) = 0.45 / 0.022 = 20.45x
P/B = (ROE − g)/(Ke − g) = (0.16 − 0.088)/(0.022) = 0.072/0.022 = 3.27x
Check: P/B = P/E × ROE ⇒ 20.45 × 0.16 = 3.27 ✅
```

---

### Q7 (Theory). Is more growth always worth a higher multiple?

**Answer.** No. `Forward P/E = payout/(Ke − g)` and `g = ROE × retention`. Growth lifts the multiple **only when ROE > Ke**. If ROE = Ke, growth is value-neutral — the justified P/B is exactly 1.0 and the P/E is the same with or without growth. If ROE < Ke, growth *destroys* value and should lower the multiple.

**Interview line:** "Growth is only worth paying for above the cost of capital. Below it, growth burns value."

---

### Q8 (Numerical). Prove growth is value-neutral when ROE = Ke.

**Given:** Ke 12%, payout 30%, and (a) ROE 12%, (b) ROE 20%.

**Solution.**
```
(a) ROE = Ke = 12%: g = 0.12 × 0.70 = 0.084
    P/E = 0.30/(0.12 − 0.084) = 0.30/0.036 = 8.33x
    P/B = (0.12 − 0.084)/(0.036) = 1.00x  ← exactly 1
    Compare a zero-growth version (payout 100%, g=0): P/E = 1.0/(0.12) = 8.33x — same!
(b) ROE = 20%: g = 0.20 × 0.70 = 0.14
    P/E = 0.30/(0.12 − 0.14) = 0.30/(−0.02) → negative denominator
```
In (a) growth adds nothing (P/E identical to no-growth case; P/B = 1). In (b) the model breaks because g > Ke — a signal that constant-growth Gordon can't handle super-normal growth; you'd need a two-stage model. **Lesson:** value comes from the ROE–Ke *spread*, not growth per se.

---

### Q9 (Theory). When do you use EV/EBIT instead of EV/EBITDA?

**Answer.** When **capital intensity differs materially** across the comp set. EV/EBITDA ignores D&A and thus flatters capex-heavy businesses. EV/EBIT keeps D&A in the denominator — and D&A is a rough proxy for maintenance capex — so the capital-intensity difference *shows up* in the multiple. Two firms on the same EV/EBITDA but different capex will differ on EV/EBIT, and the capital-light one is genuinely cheaper on a cash basis.

---

### Q10 (Numerical). Two firms, same EV/EBITDA, different capex — which is cheaper?

**Given:** Both EV ₹10,000 cr, EBITDA ₹2,000 cr (EV/EBITDA 5.0x). Firm A: D&A ₹200 cr. Firm B: D&A ₹800 cr (capital-heavy).

**Solution.**
```
Firm A: EBIT = 2,000 − 200 = 1,800 → EV/EBIT = 10,000/1,800 = 5.56x
Firm B: EBIT = 2,000 − 800 = 1,200 → EV/EBIT = 10,000/1,200 = 8.33x
```
Same EV/EBITDA (5.0x), but Firm B is far pricier on EV/EBIT (8.33x vs 5.56x) because its heavy D&A/capex means less EBITDA becomes cash. **Firm A is genuinely cheaper.**

---

### Q11 (Numerical). Forward vs trailing multiple.

**Given:** EV ₹6,000 cr; trailing EBITDA ₹500 cr; expected growth 20%.

**Solution.**
```
Trailing EV/EBITDA = 6,000/500 = 12.0x
Forward EBITDA = 500 × 1.20 = 600
Forward EV/EBITDA = 6,000/600 = 10.0x
Relationship: Forward = Trailing/(1+g) = 12.0/1.20 = 10.0x ✅
```
A peer at 11x trailing looks cheaper than this 12x — but on forward this firm (10x) is cheaper. Never compare one firm's forward to another's trailing.

---

### Q12 (Theory). Why do banks trade on P/B, not EV/EBITDA?

**Answer.** For a bank, debt (deposits/borrowings) is a raw material of the business, not just financing — so "enterprise value" and EBITDA are meaningless. Book value is marked near fair value, so it's economically meaningful, and it links directly to returns: `P/B = (ROE − g)/(Ke − g)`. A bank earning ROE above Ke trades above book; below Ke, below book. The framework is **P/B versus ROE** (plus P/E).

---

### Q13 (Numerical). Bank P/B from ROE.

**Given:** Bank ROE 14%, Ke 10%, growth 5%.

**Solution.**
```
P/B = (ROE − g)/(Ke − g) = (0.14 − 0.05)/(0.10 − 0.05) = 0.09/0.05 = 1.80x
```
If ROE fell to 10% (= Ke): `P/B = (0.10−0.05)/(0.10−0.05) = 1.0x`. A bank earning only its cost of equity is worth exactly book value.

---

### Q14 (Theory). How do you value a lossmaking company?

**Answer.** Earnings and often EBITDA are negative, so the denominators break. Move up the income statement to a positive, less-manipulable driver: **EV/Sales**, **EV/Gross Profit**, **EV/ARR**, or a sector operational metric (EV/subscriber, EV/MAU). EV/Sales implicitly assumes a target margin — `EV/Sales = EV/EBIT × margin` — so anchor it to the margin the business can realistically reach at scale, and triangulate with a DCF.

---

### Q15 (Numerical). EV/Sales hides the margin — reconcile.

**Given:** Company X: EV ₹4,000 cr, revenue ₹1,600 cr, EBIT margin 12.5%. Peer Y: EV/Sales 0.8x, EBIT margin 5%.

**Solution.**
```
X: EV/Sales = 4,000/1,600 = 2.5x ; EBIT = 1,600×0.125 = 200 ; EV/EBIT = 4,000/200 = 20.0x
   Check: EV/Sales = EV/EBIT × margin = 20.0 × 0.125 = 2.5x ✅
Y: EV/EBIT = EV/Sales ÷ margin = 0.8 / 0.05 = 16.0x
```
On sales, Y (0.8x) looks vastly cheaper than X (2.5x). On earnings, X is on 20x and Y on 16x — the gap is far smaller, driven almost entirely by X's higher margin. **Never compare EV/Sales across different margin structures without converting.**

---

### Q16 (Theory + Numerical). PEG ratio — use and abuse.

**Answer.** `PEG = (P/E)/g%`, with ~1.0 as a rough "fair" line. Example: P/E 30x, EPS growth 25% → PEG = 30/25 = **1.2** (slightly rich). A stock at P/E 18x growing 20% → PEG = 0.9 (slightly cheap). **Abuses:** the 1.0 rule has no rigorous basis — it ignores risk and payout; it's hypersensitive to which growth figure you pick; and it unfairly punishes low-growth quality compounders. Treat it as a quick sanity check, not a valuation.

---

### Q17 (Theory). The "peak-earnings trap" in cyclicals.

**Answer.** For a cyclical (steel, autos, commodities), earnings peak at the top of the cycle, so P/E is *lowest* exactly when the stock is most dangerous, and *highest* at the trough when earnings are depressed. So the naïve "low P/E = cheap" rule inverts: you often **buy cyclicals on high P/E (trough earnings) and sell on low P/E (peak earnings)**. Better tools: normalised/mid-cycle earnings, EV/Sales, or price-to-book.

---

### Q18 (Numerical). Full EV bridge with all adjustments + P/E.

**Given:** Price ₹250, shares 20 cr; debt ₹2,500 cr; cash ₹500 cr; preferred ₹300 cr (dividend ₹24 cr); minority interest ₹200 cr; EBIT ₹800 cr; interest ₹150 cr; tax 25%.

**Solution.**
```
Market cap = 250 × 20 = ₹5,000 cr
EV = 5,000 + 2,500 + 300 + 200 − 500 = ₹7,500 cr
PBT = EBIT − interest = 800 − 150 = 650
Tax = 162.5 ; NI = 487.5
NI to common = 487.5 − 24 (preferred div) = 463.5
EPS = 463.5 / 20 = ₹23.18
Trailing P/E = 250 / 23.18 = 10.8x
EV/EBIT = 7,500 / 800 = 9.375x
```
**Reverse-check:** `EV − debt − preferred − MI + cash = 7,500 − 2,500 − 300 − 200 + 500 = 5,000` ✅ = market cap.

---

### Q19 (Theory). Why add minority interest and subtract cash in the EV build?

**Answer.** **Minority interest:** the parent consolidates 100% of a subsidiary's EBITDA/sales in the income statement even though it owns <100%. To keep the numerator (EV) consistent with a denominator that includes 100% of the sub's flow, you add back the minority's claim so EV reflects the *whole* enterprise. **Cash:** it's a non-operating asset whose returns (interest income) aren't in EBITDA/EBIT; a buyer effectively nets it against the purchase price. Removing it aligns EV with operating flows.

---

### Q20 (Theory). "Give me the drivers of EV/EBITDA and how each moves it."

**Answer.** `EV/EBITDA = (FCFF/EBITDA)/(WACC − g)`:
- **Growth (g) up → multiple up** (denominator shrinks).
- **WACC up (more risk) → multiple down.**
- **Cash conversion up → multiple up** — i.e. lower capex intensity, lower working-capital drag, lower cash tax mean more EBITDA becomes free cash.
So a capital-light, fast-growing, low-risk business earns a high EV/EBITDA; a capital-heavy, slow, risky one earns a low one. That's *why* software trades richer than steel — not sentiment, but cash-conversion math.

---

### Q21 (Numerical). Reconcile P/E, P/B and ROE (internal consistency).

**Given:** A stock trades at P/E 15x and P/B 2.4x.

**Solution.**
```
Implied ROE = P/B / P/E = 2.4 / 15 = 0.16 = 16%
```
Check against fundamentals: if this firm's actual trailing ROE is ~16%, the two multiples are internally consistent. If the reported ROE were, say, 25%, then either the P/B looks low relative to P/E (possible value in book) or earnings quality/normalisation needs a look. **The identity `P/B = P/E × ROE` is a fast consistency test on any comps table.**

---

### Q22 (Theory). "Walk me through choosing a multiple for a company." (Wrap-up)

**Answer.** "First, is it profitable? If not, EV/Sales or a sector operational metric. If yes: am I comparing across different capital structures? If so, an EV-based multiple, not P/E. Is it a financial firm? Then P/B against ROE. Does capital intensity differ a lot across peers? Then EV/EBIT to capture D&A, not just EV/EBITDA. Otherwise, EV/EBITDA and P/E are the defaults. Throughout, I keep the basis consistent — forward vs trailing, diluted shares, normalised earnings, comparable margins — because a multiple is only as good as the comparability behind it. And I always remember the multiple is a compressed DCF: I sanity-check whether the implied growth, returns and risk actually make sense."
