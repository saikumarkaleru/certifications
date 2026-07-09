# Q&A — Value Creation: ROIC vs WACC & EVA

A mixed bank of theory (with model answers and interview phrasing) and fully-solved numericals. All numbers are self-verified and internally consistent.

---

## Theory

### Q1. State the single governing rule of value creation and explain why it holds from first principles.

**Model answer.** A company creates shareholder value if and only if **ROIC > WACC**. First principles: investors have an opportunity cost — WACC is the return they could earn elsewhere at the same risk, so it's the minimum acceptable (hurdle) return. ROIC is what the firm actually earns on the capital tied up in operations (NOPAT / Invested Capital). If ROIC exceeds WACC, the firm earns a surplus over investors' opportunity cost on every rupee — genuine economic profit. If ROIC is below WACC, it's earning less than investors could get themselves, so it's destroying value even if it reports accounting profit.

**How to say it in an interview:** "Value is an arbitrage between what capital earns and what it costs. ROIC above WACC is the whole game."

---

### Q2. "Growth always creates value." True or false, and why?

**Model answer.** **False.** Growth is a *multiplier* of the ROIC-minus-WACC spread, not value in itself. If ROIC > WACC, growth amplifies value creation. If ROIC = WACC, growth is value-*neutral* — it adds size but not value (the growth term drops out of the value equation entirely). If ROIC < WACC, growth *destroys* value — the faster you grow, the more you burn. So growth's sign depends entirely on the spread.

**Interview line:** "Growth is fuel; the spread decides whether you're feeding a fire or a flood."

---

### Q3. Define EVA and explain why it can be negative when net income is positive.

**Model answer.** EVA = (ROIC − WACC) × Invested Capital = NOPAT − (WACC × Invested Capital). The second term is the *capital charge* — a charge for **all** capital, including equity. Net income only subtracts the cost of *debt* (interest); it never charges for equity capital. So a firm can report positive net income yet have negative EVA: it made an accounting profit but didn't earn enough to cover what equity holders demanded. EVA is true economic profit; net income is accounting profit.

**Interview line:** "Net income forgets that equity isn't free. EVA remembers."

---

### Q4. What is the difference between EVA and residual income?

**Model answer.** They're the same idea at different levels. **Residual income** works at the *equity* level: Net Income − (cost of equity × book equity). **EVA** works at the *firm* level: NOPAT − (WACC × invested capital). Residual income charges for equity capital only; EVA charges for all capital. Both subtract a charge for equity that accounting profit omits, then see what's left. EVA is essentially residual income applied to the whole capital structure.

---

### Q5. What is MVA and how does it connect EVA to the share price?

**Model answer.** Market Value Added = Market Value of the firm − Invested Capital = the present value of all future EVAs, discounted at WACC. It's the premium the market places over the capital sunk into the business. A firm trading well above invested capital is one the market expects to earn ROIC > WACC for years; a firm trading below invested capital is expected to destroy value. This is why the market "prices the spread, not the growth" — MVA capitalises the *durability and scale* of future economic profit.

---

### Q6. A company grew EPS 20% but its stock fell. Give the value-based explanation.

**Model answer.** EPS growth says nothing about value if the capital funding it earns below WACC. The firm likely grew by deploying capital into sub-WACC projects — accretive to EPS but destructive of economic value — or its ROIC fell below WACC / the spread narrowed. The market values economic profit (NOPAT minus a full capital charge), not accounting EPS, so it repriced the stock down despite the EPS headline. EPS accretion via cheap debt is financial engineering, not value creation.

---

### Q7. How do you improve a company's ROIC? Frame it with a decomposition.

**Model answer.** Use the DuPont decomposition: ROIC = (NOPAT/Sales) × (Sales/Invested Capital) = operating margin × capital turnover. Two levers: (1) raise **margin** via pricing, product mix, or cost efficiency; (2) raise **capital turnover** by cutting working capital (inventory days, receivable days), sweating fixed assets, or divesting low-return capital. Either lever, holding the other constant, raises ROIC — and you should only grow the parts of the business where ROIC already beats WACC.

---

### Q8. Should invested capital include goodwill? 

**Model answer.** It depends on the question. **Include** goodwill to measure the return shareholders earned on what they actually *paid*, acquisition premiums and all — the right lens for judging whether M&A created value net of premiums. **Exclude** goodwill to measure the *operating* quality of the underlying assets and to compare against peers on a like-for-like basis. State which you're using and why; a good analyst reports both.

---

### Q9. Why is NOPAT (not net income) the right numerator for ROIC, and what error does this avoid?

**Model answer.** NOPAT = EBIT × (1 − t) is capital-structure-neutral — it ignores interest entirely, so it's the profit available to *all* capital providers, matching the "all invested capital" denominator and the "all-capital" WACC hurdle. Net income is *after* interest, so it's an equity-level figure and pairing it with total invested capital mismatches the "return to whom." Using NOPAT also avoids double-counting leverage: the debt tax shield is captured once, in WACC's after-tax cost of debt — subtracting interest from the numerator *and* using after-tax WACC would count it twice.

---

### Q10. Why does the ROIC-WACC spread fade over time, and how should a DCF reflect it?

**Model answer.** A positive spread (ROIC > WACC) is excess profit that attracts competition — rivals copy the product, undercut price, and bid the surplus away, dragging ROIC toward WACC. The spread's *duration* is set by the firm's competitive advantage (moat). A rigorous DCF therefore **fades** ROIC toward WACC over an explicit competitive-advantage period rather than assuming a permanent high spread. Perpetual excess returns in a model are a red flag.

---

### Q11. If ROIC = WACC, what is the firm worth, and what does that prove?

**Model answer.** Value = NOPAT / WACC, *independent of growth*. Starting from Value = NOPAT(1 − g/ROIC)/(WACC − g), setting ROIC = WACC makes the numerator NOPAT(WACC − g)/WACC, which divided by (WACC − g) gives NOPAT/WACC — g cancels out entirely. This is the mathematical proof that **value-neutral growth exists**: when the spread is zero, growth adds size but not a rupee of value.

---

## Numerical problems

### Q12. Basic EVA. EBIT = ₹800, tax rate = 25%, debt = ₹1,500, equity = ₹2,000, cash = ₹300, WACC = 10%. Compute NOPAT, invested capital, ROIC, spread, and EVA.

**Solution.**
- NOPAT = 800 × (1 − 0.25) = 800 × 0.75 = **₹600**.
- Invested capital = 1,500 + 2,000 − 300 = **₹3,200**.
- ROIC = 600 / 3,200 = **18.75%**.
- Spread = 18.75% − 10% = **+8.75%** → strong value creation.
- EVA = (0.1875 − 0.10) × 3,200 = 0.0875 × 3,200 = **₹280**.
- Cross-check: NOPAT − WACC×IC = 600 − 0.10×3,200 = 600 − 320 = **₹280**. ✓

---

### Q13. Value-neutral trap. A firm has NOPAT = ₹400, invested capital = ₹4,000, WACC = 10%. It plans an expansion adding ₹1,500 of capital that will earn incremental NOPAT of ₹135. Should it proceed?

**Solution.**
- Current ROIC = 400 / 4,000 = 10.0% — exactly WACC. Existing business is value-neutral.
- Incremental ROIC on expansion = 135 / 1,500 = **9.0%** < WACC 10%.
- Incremental EVA = (0.09 − 0.10) × 1,500 = −0.01 × 1,500 = **−₹15 per year**.
- Capitalised value destroyed ≈ 15 / 0.10 = **−₹150**.

**Verdict: reject.** The expansion grows NOPAT by ₹135 (a headline +33.75%) but earns below WACC, destroying ₹15/year (~₹150 of value). The firm should return the ₹1,500 to shareholders or find projects above 10%.

---

### Q14. Same growth, different spread. Two firms each have NOPAT = ₹120 and grow at g = 5%; WACC = 9% for both. Firm X earns ROIC = 18%, Firm Y earns ROIC = 9%. Value each using the master formula.

**Solution.** Value = NOPAT × (1 − g/ROIC) / (WACC − g).
- **Firm X:** RR = 5%/18% = 0.2778. Value = 120 × (1 − 0.2778) / (0.09 − 0.05) = 120 × 0.7222 / 0.04 = 86.67 / 0.04 = **₹2,166.7**.
- **Firm Y:** ROIC = WACC = 9%. Value = NOPAT/WACC = 120 / 0.09 = **₹1,333.3** (growth term irrelevant). Check via formula: RR = 5%/9% = 0.5556; 120 × (1 − 0.5556)/0.04 = 120 × 0.4444/0.04 = 53.33/0.04 = 1,333.3. ✓

**Takeaway:** identical NOPAT, growth and WACC, but X (high spread) is worth ₹2,167 vs Y (zero spread) ₹1,333. For Y, its 5% growth adds nothing — it's worth exactly its no-growth value.

---

### Q15. Working-capital release. Meridian has sales ₹8,000, NOPAT margin 5% (NOPAT ₹400), invested capital ₹4,000, WACC 10%. A receivables program cuts invested capital to ₹3,200 with no change to sales or margin. Show the ROIC and EVA impact and the value created.

**Solution.**
- Before: ROIC = 400/4,000 = **10.0%**; EVA = (0.10 − 0.10)×4,000 = **₹0** (value-neutral).
- After: ROIC = 400/3,200 = **12.5%**; EVA = (0.125 − 0.10)×3,200 = 0.025×3,200 = **₹80**. Check: 400 − 0.10×3,200 = 400 − 320 = **₹80**. ✓
- EVA rose from ₹0 to ₹80/year. Capitalised (no growth): 80/0.10 = **₹800** of value — which equals the ₹800 of capital released, now freed to return to investors or redeploy above WACC.

**Takeaway:** a pure balance-sheet lever (fewer receivable days), with zero P&L change, moved the firm from value-neutral to value-creating.

---

### Q16. Residual income vs EVA. A firm has net income ₹250, book equity ₹2,000, cost of equity 12%. Separately: NOPAT ₹360, invested capital ₹3,000, WACC 10%. Compute residual income and EVA, and comment.

**Solution.**
- Residual income = Net income − kₑ × Equity = 250 − 0.12 × 2,000 = 250 − 240 = **₹10**.
- EVA = NOPAT − WACC × IC = 360 − 0.10 × 3,000 = 360 − 300 = **₹60**.
- Both positive → value is being created at both the equity and firm level. Residual income (₹10) is thin — the equity holders' 12% demand nearly consumes net income — while firm-level EVA (₹60) is healthier because the cheaper blended capital cost (10%) sets a lower bar. Different levels, same core idea: charge for equity, then measure what's left.

---

### Q17. MVA and implied market value. A firm has invested capital ₹5,000, current EVA ₹150, expected to grow EVA at 4% forever, WACC 12%. Find MVA and the implied firm value.

**Solution.**
- MVA = EVA₁ / (WACC − g). Next-year EVA = 150 × 1.04 = 156. MVA = 156 / (0.12 − 0.04) = 156 / 0.08 = **₹1,950**.
- Implied firm value = Invested capital + MVA = 5,000 + 1,950 = **₹6,950**.
- Firm trades at 6,950/5,000 = **1.39×** invested capital — the 39% premium is the capitalised value of its future economic profits.

---

### Q18. Reverse-engineer ROIC from growth and reinvestment. A firm reinvests 40% of its NOPAT (reinvestment rate 0.40) and grows NOPAT at 8%. What ROIC is implied? If WACC is 10%, is growth creating value?

**Solution.**
- g = RR × ROIC → ROIC = g / RR = 0.08 / 0.40 = **20%**.
- ROIC 20% > WACC 10% → spread +10% → **growth is strongly value-creating.** Each reinvested rupee earns double its cost, so the firm's 8% growth adds substantial value.

---

### Q19. Full valuation with the master formula. NOPAT = ₹500, ROIC = 16%, g = 6%, WACC = 11%. Value the firm, then split into assets-in-place and value-of-growth.

**Solution.**
- Reinvestment rate = g/ROIC = 6%/16% = 0.375. FCFF₁-equivalent factor (1 − RR) = 0.625.
- Value = 500 × 0.625 / (0.11 − 0.06) = 312.5 / 0.05 = **₹6,250**.
- **Value of assets in place** (no growth) = NOPAT/WACC = 500/0.11 = **₹4,545.5**.
- **Value of growth** = 6,250 − 4,545.5 = **₹1,704.5** (positive because ROIC 16% > WACC 11%).

**Takeaway:** ~27% of this firm's value comes from profitable growth; the rest is the steady-state operating profit capitalised. Had ROIC = WACC, value-of-growth would be zero.

---

### Q20. Spread narrowing. Last year: NOPAT ₹450, invested capital ₹3,000, WACC 10%. This year: NOPAT ₹520, invested capital ₹4,000, WACC 10%. Did value creation improve? Use EVA.

**Solution.**
- Last year: ROIC = 450/3,000 = 15.0%; EVA = (0.15 − 0.10)×3,000 = 0.05×3,000 = **₹150**.
- This year: ROIC = 520/4,000 = 13.0%; EVA = (0.13 − 0.10)×4,000 = 0.03×4,000 = **₹120**.
- NOPAT *grew* 15.6% (450→520) and the firm got bigger, yet **EVA fell from ₹150 to ₹120** because ROIC dropped from 15% to 13% — the spread narrowed from 5% to 3%. 

**Takeaway:** growing NOPAT while diluting ROIC can *reduce* value creation. This is exactly the "EPS up, stock down" pattern — the market watches the spread, not the growth.

---

### Q21. Cost-of-capital sensitivity. A firm earns ROIC = 12% on invested capital of ₹6,000. Compare EVA at WACC = 9% versus WACC = 13%.

**Solution.**
- At WACC 9%: EVA = (0.12 − 0.09) × 6,000 = 0.03 × 6,000 = **+₹180** (value-creating).
- At WACC 13%: EVA = (0.12 − 0.13) × 6,000 = −0.01 × 6,000 = **−₹60** (value-destroying).
- Same operating performance (ROIC 12%), opposite verdicts. 

**Takeaway:** value creation is *relative* to the cost of capital. A 12% ROIC is excellent for a low-risk utility (WACC 9%) but value-destructive for a risky venture (WACC 13%). Never judge ROIC in isolation — always against WACC.

---

### Q22. Buyback vs sub-WACC growth (capital allocation). A firm has ₹1,000 of surplus cash. Option A: invest in a project earning 8%. Option B: return it to shareholders (who can earn WACC elsewhere). WACC = 11%. Which creates more value?

**Solution.**
- Option A EVA = (0.08 − 0.11) × 1,000 = −0.03 × 1,000 = **−₹30/year**; capitalised ≈ −30/0.11 = **−₹273** of value destroyed.
- Option B: returning cash lets shareholders earn their 11% opportunity cost — value-neutral to them (they get their money and redeploy at WACC), so **₹0 destroyed** relative to the hurdle, and ₹273 *better* than Option A.

**Verdict: return the cash.** Investing below WACC to look "growth-oriented" destroys value; the disciplined move is the buyback/dividend. This is the capital-allocation punchline of the whole chapter: **don't grow below your cost of capital — give the money back.**
