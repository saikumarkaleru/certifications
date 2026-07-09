# Q&A — Time Value of Money

A mix of **theory** (with model answers and "how to say it in an interview") and **numerical problems** (fully solved, numbers self-verified). Work each before reading the answer.

---

## Theory questions

### Q1. Why is a rupee today worth more than a rupee tomorrow? Rank the reasons.

**Model answer.** The dominant reason is **opportunity cost / the productivity of capital**: a rupee today can be invested to earn a return, so it grows into more than a rupee tomorrow. Layered on top: **time preference** (people prefer consuming now, so must be paid to wait), **risk** (a future promise may not be honoured), and **inflation** (future rupees buy less). Crucially, even with zero inflation and zero risk, a *positive real interest rate* exists because real investment opportunities exist.

**How to say it in an interview.** "Chiefly opportunity cost — money today can be put to work and earn a return. Impatience, risk, and inflation add to it, but the core is that capital is productive, so a positive real rate exists even without inflation." *Leading with opportunity cost rather than inflation is the tell of a strong candidate.*

### Q2. Distinguish nominal, periodic, and effective annual rate.

**Model answer.** The **nominal (stated/APR) rate** is a quoting convention — the periodic rate times the number of periods per year; it ignores intra-year compounding. The **periodic rate** is nominal ÷ frequency (e.g. 12%/12 = 1% monthly) — the rate actually applied each period. The **effective annual rate (EAR)** is the true annual growth once compounding is included: $EAR=(1+r_{nom}/m)^m-1$. Only EAR is comparable across instruments with different compounding frequencies.

**Interview line.** "Nominal is a sticker price, periodic is what's actually applied each period, EAR is what you truly earn in a year. Never compare two rates of different frequency without converting both to EAR."

### Q3. Derive the present value of a perpetuity.

**Model answer.** $PV = \frac{C}{1+r}+\frac{C}{(1+r)^2}+\cdots$, an infinite geometric series with first term $a=\frac{C}{1+r}$ and ratio $x=\frac{1}{1+r}$ (with $|x|<1$). Sum $=\frac{a}{1-x}=\frac{C/(1+r)}{r/(1+r)}=\frac{C}{r}$. The infinite stream has a finite value because distant cash flows discount toward zero.

**Interview line.** "It's C over r — a convergent geometric series because 1/(1+r) is less than one. Note the first cash flow is one period out, so C/r values the perpetuity one period *before* the first payment."

### Q4. Why does more frequent compounding raise the effective rate, and why does it stop mattering eventually?

**Model answer.** More frequent compounding means interest is credited and starts earning interest sooner — more "interest on interest" — so the same nominal rate produces higher effective growth. But the marginal benefit shrinks with frequency: going annual→monthly adds far more than monthly→daily. The EAR converges to a ceiling, the **continuous-compounding limit** $EAR=e^{r}-1$, because $(1+r/m)^m \to e^r$ as $m\to\infty$.

**Interview line.** "Frequency helps because interest compounds sooner, but with diminishing returns — it saturates at the continuous limit e^r − 1. On 12% nominal, annual gives 12.00% and continuous only 12.75%."

### Q5. What is the Gordon Growth Model, when is it valid, and what breaks it?

**Model answer.** $PV=\frac{C_1}{r-g}$: value of a cash flow stream growing at constant $g$ forever, where $C_1$ is *next* period's cash flow. Valid only when $g<r$ and growth is genuinely perpetual and constant. It breaks (gives infinite/negative nonsense) when $g\ge r$; and it is *hyper-sensitive* to the $r-g$ spread, so small assumption changes swing value massively. In DCFs, $g$ should not exceed long-run nominal GDP growth or you imply the firm eventually becomes the whole economy.

**Interview line.** "C-one over r-minus-g, needs g below r. It's the standard terminal-value formula, and because it's so sensitive to the r-minus-g spread, you always sensitivity-table it."

### Q6. Ordinary annuity vs annuity due — which is worth more, and by exactly how much?

**Model answer.** The **annuity due** (payments at the *start* of each period) is worth more because every payment arrives one period earlier and is therefore discounted one period less. Precisely, $PV_{due}=PV_{ordinary}\times(1+r)$ and likewise for FV. Rent/leases are typically annuities due; loan EMIs and bond coupons are ordinary annuities.

**Interview line.** "Annuity due wins — cash comes a period sooner. It's exactly (1+r) times the ordinary annuity. Rent is a due; bond coupons are ordinary."

### Q7. In a DCF, what are the two most common terminal-value mistakes?

**Model answer.** (1) Using the *current* final-year cash flow in the numerator instead of the *next* year's — Gordon Growth needs $CF_{n+1}=CF_n(1+g)$. (2) Forgetting that the terminal value is dated at the *final explicit year*, so it must still be discounted back $n$ periods to today. A third: setting $g$ too high (≥ r, or above GDP).

**Interview line.** "Grow one more year in the numerator, and remember the TV sits at year n — it still needs discounting back to today. And keep g below r and below GDP."

### Q8. What is continuous compounding and why do quants prefer it?

**Model answer.** It's the limit of compounding every instant: $FV=PV\,e^{rt}$, $PV=FV\,e^{-rt}$. Quants and derivatives pricing prefer it because $e^{rt}$ is analytically clean (trivial to differentiate/integrate), and continuously-compounded (log) returns are **additive across time and symmetric**, unlike discrete returns. Black–Scholes and most fixed-income analytics use it.

**Interview line.** "FV equals PV times e-to-the-rt. It's the instantaneous-compounding limit, and log returns add across periods — that's why option pricing uses it."

### Q9. Explain the Rule of 72.

**Model answer.** Doubling time ≈ $72/(\text{rate in \%})$. It approximates the exact $n=\ln 2/\ln(1+r)$. Since $\ln 2\approx0.693$, the exact numerator is ~69.3, but 72 is used because it has many divisors and better matches the compounding math in the common 6–10% band.

**Interview line.** "Seventy-two divided by the percentage rate — 12% doubles in ~6 years, 8% in ~9. It's ln 2 over ln(1+r) rounded to a friendly 72."

### Q10. What does it mean that early loan EMIs are "mostly interest"?

**Model answer.** Each EMI is constant, but its split changes. Interest each month = outstanding balance × periodic rate. Early on the balance is large, so most of the payment is interest and little reduces principal; as principal falls, the interest portion shrinks and the principal portion grows. This front-loading is why prepaying early — when balance and thus interest are highest — saves disproportionately.

**Interview line.** "The EMI is flat but the mix shifts — early payments are mostly interest because the balance is high, so early prepayment saves the most."

---

## Numerical problems

### Q11. Future and present value of a lump sum.

You deposit ₹2,00,000 at **7% p.a. compounded annually** for **10 years**.

**Solution.** $FV=200{,}000\times(1.07)^{10}$. $(1.07)^{10}=1.967151$. $FV=200{,}000\times1.967151=₹3{,}93{,}430$.
Check by discounting: $393{,}430/1.967151=₹2{,}00{,}000$. ✓
Doubling check via Rule of 72: $72/7\approx10.3$ years, so after 10 years you should be *just under* double — ₹3.93 lakh is just under ₹4 lakh. ✓

### Q12. Solve for the rate and the time.

An investment grows from **₹1,00,000 to ₹2,59,374 over 12 years.** What annual rate? Then how long to triple at that rate?

**Solution.** $r=(259{,}374/100{,}000)^{1/12}-1=(2.59374)^{1/12}-1$. Since $(1.08)^{12}=2.518170$ and $(1.0825)^{12}\approx2.594$, we get $r\approx8.25\%$. Let's verify with 8%: $(2.59374)^{1/12}$: $\ln 2.59374=0.953117$; ÷12 = 0.079426; $e^{0.079426}=1.08267$, so $r\approx8.27\%$.
Time to triple at 8.27%: $n=\ln 3/\ln(1.0827)=1.098612/0.079426=13.83$ years.

### Q13. Effective annual rate comparison.

Rank: **(A) 10.0% compounded annually, (B) 9.8% compounded monthly, (C) 9.7% compounded continuously.**

**Solution.**
- A: EAR = 10.000%.
- B: EAR $=(1+0.098/12)^{12}-1=(1.0081667)^{12}-1$. $12\times\ln1.0081667=12\times0.0081335=0.097602$; $e^{0.097602}-1=0.10252=$ **10.252%**.
- C: EAR $=e^{0.097}-1=0.101862=$ **10.186%**.

**Ranking: B (10.25%) > C (10.19%) > A (10.00%).** The lower-nominal monthly beats the higher-nominal annual — the lesson that frequency, not just the sticker rate, matters.

### Q14. Present value of an ordinary annuity.

What is the PV of **₹50,000 received at the end of each year for 8 years** at **9%**?

**Solution.** $PV=50{,}000\times\frac{1-(1.09)^{-8}}{0.09}$. $(1.09)^8=1.992563$, so $(1.09)^{-8}=0.501866$. Factor $=(1-0.501866)/0.09=0.498134/0.09=5.53482$.
$PV=50{,}000\times5.53482=₹2{,}76{,}741$.

### Q15. Future value of an annuity (SIP).

You invest **₹10,000 at the end of every month for 15 years** at **12% nominal, compounded monthly.** Final corpus?

**Solution.** Monthly rate $=0.01$; $n=180$. $(1.01)^{180}$: $180\times\ln1.01=180\times0.00995033=1.791060$; $e^{1.791060}=5.995802$.
$FV=10{,}000\times\frac{5.995802-1}{0.01}=10{,}000\times\frac{4.995802}{0.01}=10{,}000\times499.5802=₹49{,}95{,}802$.
Contributions were only 10,000 × 180 = ₹18,00,000; compounding added ₹31.96 lakh. ✓ (corpus ≈ 2.78× contributions, plausible at 12% over 15 yrs).

### Q16. Annuity due vs ordinary.

Rework Q14 assuming the ₹50,000 arrives at the **start** of each year (annuity due).

**Solution.** $PV_{due}=PV_{ordinary}\times(1+r)=276{,}741\times1.09=₹3{,}01{,}648$. The due version is worth ₹24,907 more — exactly 9% more — because every payment lands a year earlier.

### Q17. Loan EMI and interest split.

Borrow **₹10,00,000** at **10.5% nominal, monthly**, over **15 years.** Find the EMI, total interest, and month-1 split.

**Solution.** $r=0.105/12=0.00875$; $n=180$. $(1.00875)^{180}$: $180\times\ln1.00875=180\times0.00871193=1.568147$; $e^{1.568147}=4.797607$.
$C=1{,}000{,}000\times\frac{0.00875\times4.797607}{4.797607-1}=1{,}000{,}000\times\frac{0.04197906}{3.797607}=1{,}000{,}000\times0.01105397=₹11{,}054$.
Total paid $=11{,}054\times180=₹19{,}89{,}720$; **interest = ₹9,89,720** (≈ the principal itself).
Month-1 interest $=1{,}000{,}000\times0.00875=₹8{,}750$; principal $=11{,}054-8{,}750=₹2{,}304$. So 79% of the first EMI is interest.

### Q18. Perpetuity and growing perpetuity.

(a) A preferred share pays **₹12/year forever**; required return **8%**. Value?
(b) A stock pays a dividend of **₹12 next year growing 5% forever**; required return **11%**. Value?

**Solution.**
(a) $PV=C/r=12/0.08=₹150$.
(b) $PV=C_1/(r-g)=12/(0.11-0.05)=12/0.06=₹200$.
The growth (b vs a) adds value, but note the higher discount rate in (b) partly offsets it — the net is still higher because g compounds forever.

### Q19. DCF terminal value (dating and discounting).

A firm's **year-5 free cash flow is ₹800 crore**, growing **4% forever** after; **WACC 12%.** Find the terminal value at year 5 and its present value today.

**Solution.** $TV_5=\frac{FCF_6}{r-g}=\frac{800\times1.04}{0.12-0.04}=\frac{832}{0.08}=₹10{,}400$ crore.
Discount back 5 years: $(1.12)^5=1.762342$; $PV=10{,}400/1.762342=₹5{,}901.2$ crore.
*Traps avoided:* used year-6 cash flow (not year-5) in the numerator, and discounted the TV back to today.

### Q20. Growing annuity (escalating salary savings).

You save an amount starting at **₹2,00,000 one year from now**, growing **6% per year**, for **20 years**, earning **10%.** PV today?

**Solution.** $PV=\frac{C_1}{r-g}\left[1-\left(\frac{1+g}{1+r}\right)^n\right]=\frac{200{,}000}{0.10-0.06}\left[1-\left(\frac{1.06}{1.10}\right)^{20}\right]$.
$\frac{1.06}{1.10}=0.963636$; $0.963636^{20}$: $20\times\ln0.963636=20\times(-0.037041)=-0.740823$; $e^{-0.740823}=0.476757$.
$PV=\frac{200{,}000}{0.04}\times(1-0.476757)=5{,}000{,}000\times0.523243=₹26{,}16{,}215$.

### Q21. Bond price as annuity + lump sum.

Price a **7-year bond, ₹1,000 face, 6% annual coupon, priced to yield 8%.**

**Solution.** Coupon ₹60/year for 7 years + ₹1,000 at year 7, discounted at 8%.
Annuity factor $=\frac{1-(1.08)^{-7}}{0.08}$. $(1.08)^7=1.713824$, $(1.08)^{-7}=0.583490$. Factor $=(1-0.583490)/0.08=5.206370$.
PV coupons $=60\times5.206370=₹312.38$. PV face $=1{,}000\times0.583490=₹583.49$.
**Price = ₹895.87.** Below par, because the 6% coupon is below the 8% yield — a discount bond. ✓

### Q22. Continuous compounding and rate conversion.

(a) ₹5,00,000 grows at **6% continuously** for **8 years** — final value?
(b) What annually-compounded effective rate equals 6% continuous?
(c) What continuously-compounded rate equals a 6% effective annual rate?

**Solution.**
(a) $FV=500{,}000\times e^{0.06\times8}=500{,}000\times e^{0.48}=500{,}000\times1.616074=₹8{,}08{,}037$.
(b) $r_e=e^{0.06}-1=0.061837=$ **6.184%**.
(c) $r_c=\ln(1.06)=0.058269=$ **5.827%**.
Sanity: continuous rates are always *below* their equivalent effective rates (6% cont ↔ 6.18% eff), consistent throughout. ✓

---

*Drill habit: for every problem, first fix the period and rate to the same unit, then decide whether it's a lump sum, annuity, or perpetuity, then discount and add. State those steps aloud in interviews.*
