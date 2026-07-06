# Q&A — Securitization, ABS and MBS

Companion practice bank for Chapter 12. Every question is followed by a full answer. Unless stated otherwise, mortgage rates are quoted as **annual nominal rates compounded monthly** (monthly rate = annual/12), and prepayment follows the **PSA** convention.

---

## Section A — Concept Check

**A1. What two financial-engineering "moves" define securitization, and what does each accomplish?**
**Pooling** and **tranching**. Pooling gathers many small, similar cash-flow assets (mortgages, auto loans, card receivables) into a bankruptcy-remote SPV so that idiosyncratic, borrower-specific risk diversifies away and the pool's *aggregate* loss becomes far more predictable than any single loan's. Tranching then slices the pooled cash flows into priority-ordered claims — senior, mezzanine, equity — so the same collateral backs securities ranging from AAA to unrated, each priced to the exact risk a particular investor wants. Pooling manufactures predictability; tranching redistributes the remaining risk to its natural buyers.

**A2. Why can a securitization's senior tranche be rated AAA when the underlying loans are subprime?**
Because the rating reflects *structure*, not average collateral quality. The junior and mezzanine tranches sit beneath the senior and absorb losses first, so the senior is impaired only when cumulative pool losses are large enough to burn through everything below it — a rare, tail event. That subordinated cushion is the senior's credit enhancement. The rating is a statement about the *dollar buffer standing in front of the senior*, not about the borrowers. The 2008 lesson is that this only holds if default correlation is low; when defaults cluster, the cushion is consumed far faster than models assumed.

**A3. What is the cash-flow waterfall, and how does the order of *losses* relate to the order of *payments*?**
The waterfall is the contractual priority of distributions each period: fees first, then interest top-down (senior → mezzanine → junior), then principal, then reserve/OC top-ups, then residual excess spread to equity. Losses run in the *reverse* order — equity absorbs the first losses, then mezzanine, then senior. So cash flows down the stack top-first while losses eat up the stack bottom-first. This mirror image is exactly what lets the senior be safe and the equity be levered.

**A4. Why is prepayment "the defining risk" of MBS, and how is it different from a callable corporate bond's call risk?**
Mortgage borrowers can repay early — they move, refinance, or default (which, if insured, reaches the investor as a prepayment). This makes the *timing* of principal uncertain and rate-sensitive. It resembles a callable bond because the borrower holds a call option on their loan, but with a key difference: a corporate issuer exercises one call rationally at an optimal boundary, whereas millions of households prepay imperfectly and behaviourally. So MBS use empirical *prepayment models* (SMM/CPR/PSA) rather than a clean optimal-exercise rule.

**A5. Define SMM, CPR, and PSA and state how they relate.**
- **SMM (Single Monthly Mortality):** the fraction of the beginning-of-month balance *net of scheduled principal* that prepays in that month.
- **CPR (Conditional Prepayment Rate):** the annualized equivalent of SMM. They compound, not scale: $\text{SMM}=1-(1-\text{CPR})^{1/12}$ and $\text{CPR}=1-(1-\text{SMM})^{12}$.
- **PSA:** a benchmark ramp. 100 PSA means CPR rises 0.2% per month from 0.2% (month 1) to 6% (month 30), then stays flat: $\text{CPR}_t^{100\text{PSA}}=\min(6\%,\,0.2\%\times t)$. A speed of $X$ PSA scales this by $X/100$.

**A6. Distinguish contraction risk from extension risk.**
- **Contraction risk:** when rates *fall*, borrowers refinance, prepayments accelerate, WAL *shortens*, and investors get cash back precisely when reinvestment rates are low. Upside is capped.
- **Extension risk:** when rates *rise*, prepayments slow, WAL *lengthens*, and investors are stuck holding a below-market coupon longer.
The asymmetry — good news (falling rates) capped, bad news (rising rates) not — is the source of MBS **negative convexity**.

**A7. Why do MBS exhibit negative convexity, and what tools must you use to analyse them?**
An MBS is economically a bond *minus* a short call the borrower owns: $\text{Price}_{MBS}=\text{Price}_{option-free}-\text{Value}_{prepay option}$. As rates fall, the prepay option gains value and caps the bond's price appreciation, so the price-yield curve bends the "wrong" way (concave). Because cash flows move with rates, Macaulay/modified duration mislead. You must use **effective duration** (which can even go negative near the money) and **option-adjusted spread (OAS)**, which strips out the option cost to leave a clean, comparable spread.

**A8. What is WAL, and why is it quoted instead of maturity? How does it differ from duration?**
**Weighted Average Life** is the average time to receive a dollar of principal, weighting each principal payment by its size: $\text{WAL}=\frac{\sum_t t\cdot\text{Principal}_t}{\sum_t\text{Principal}_t}$. Because MBS/ABS principal arrives gradually and unpredictably, a single legal maturity is uninformative, so the market quotes WAL. It differs from duration in two ways: WAL is *undiscounted* and ignores interest, and it is a *maturity* concept, not a price sensitivity. WAL is always positive; effective duration of an MBS (or an IO strip) can be negative.

**A9. List the internal credit enhancements and rank them from first-consumed to most durable.**
From weakest (consumed first in stress) to strongest: **excess spread** (pool interest minus bond coupons and fees — the first income cushion), then **overcollateralization / reserve fund** (extra collateral or cash), then **subordination** (the junior tranche stack absorbing losses). External enhancement (monoline wraps, guarantees) sits outside the deal but adds counterparty risk. Subordination is the durable structural cushion; excess spread evaporates first.

**A10. What is a CMO, and what does a PAC/support structure achieve?**
A CMO (Collateralized Mortgage Obligation) re-carves the *same* pool cash flow to give investors different *timing* profiles. A **PAC (planned amortization class)** is promised a fixed principal schedule as long as prepayment stays inside a collar (e.g. 100–300 PSA); the **support (companion)** tranche absorbs the variance — soaking up excess principal when prepayments are fast and starving when slow. The PAC gets a near-guaranteed, bond-like WAL; the support carries amplified contraction *and* extension risk and is paid a wide spread. CMO structuring does not reduce total risk — it *reallocates* prepayment uncertainty from investors who cannot bear it to those paid to.

**A11. How did ABS CDOs amplify the 2008 crisis?**
An ABS CDO pools the *mezzanine tranches of many subprime MBS deals* and re-tranches them — securitization applied to securitizations. Its senior tranche depends on the *joint* behaviour of dozens of thin mezzanine slices. Rating models assumed those slices defaulted roughly independently, making the CDO senior look AAA. But subprime defaults were driven by a common factor — national house prices — so when prices fell, the mezzanine layers defaulted *together*, and the "AAA" CDO senior was wiped almost as fast as its equity. Re-tranching concentrated the very tail risk everyone had priced as diversifiable.

---

## Section B — Numerical Bond-Math Problems

### B1. Mortgage payment and first-month split

A $250,000 fixed-rate mortgage, 30 years (n = 360), annual rate 6% so monthly $i = 0.5\% = 0.005$.

**Step 1 — the level payment.** Using $M = P\cdot\frac{i(1+i)^n}{(1+i)^n-1}$. Compute $(1.005)^{360}$: $\ln 1.005 = 0.0049875$; $\times 360 = 1.79551$; $e^{1.79551}=6.02258$.
$$M = 250{,}000\times\frac{0.005\times 6.02258}{6.02258-1}=250{,}000\times\frac{0.0301129}{5.02258}=\boxed{\$1{,}498.88}$$

**Step 2 — split month 1.** Interest $=0.005\times 250{,}000=\$1{,}250.00$. Scheduled principal $=1{,}498.88-1{,}250.00=\$248.88$. Ending balance $=250{,}000-248.88=\$249{,}751.12$.

**Reconcile:** early payments should be overwhelmingly interest on a fresh 30-year loan — here $1{,}250$ of $1{,}498.88$ is interest (83%). ✓

### B2. CPR ⇄ SMM round-trip (self-verification)

Take **month 10 at 200 PSA**. Base 100 PSA CPR $=0.2\%\times 10=2\%$; at 200 PSA, $\text{CPR}=2\times 2\%=4\%$.

**CPR → SMM:** $\text{SMM}=1-(1-0.04)^{1/12}=1-(0.96)^{0.083333}$. $\ln 0.96=-0.0408220$; $\times 0.083333=-0.00340183$; $e^{-0.00340183}=0.9966040$; **SMM $=0.0033961=0.33961\%$.**

**Round-trip SMM → CPR:** $\text{CPR}=1-(1-0.0033961)^{12}=1-(0.9966039)^{12}$. $\ln 0.9966039=-0.00340183$; $\times 12=-0.0408220$; $e^{-0.0408220}=0.960000$; CPR $=1-0.96=4.00\%$. ✓ The conversions are exact inverses, and note SMM $\times 12 = 0.4075\%$ would overstate the true monthly speed — CPR is *not* 12×SMM.

### B3. Dollar prepayment in a month

A pool has a **beginning balance of $180,000**, **scheduled principal of $200** this month, and prepays at **CPR = 6%**.

**Step 1 — SMM.** $\text{SMM}=1-(1-0.06)^{1/12}=1-(0.94)^{0.083333}$. $\ln 0.94=-0.0618754$; $\times 0.083333=-0.00515628$; $e^{-0.00515628}=0.9948570$; SMM $=0.0051430=0.51430\%$.

**Step 2 — prepayment dollars.** $\text{prepay}=\text{SMM}\times(\text{beginning balance}-\text{scheduled principal})=0.0051430\times(180{,}000-200)=0.0051430\times 179{,}800=\$924.71$.

**Step 3 — total principal to investors** $=$ scheduled $+$ prepay $=200+924.71=\boxed{\$1{,}124.71}$.

**Reconcile:** the SMM base correctly excludes the $200 of scheduled principal (that balance is already leaving), so we apply 0.51430% only to the $179,800 that could still prepay. ✓

### B4. Sequential-pay WAL, reconciled to the pool

**Pool:** $200m of principal returned over four years — Y1 $40m, Y2 $60m, Y3 $60m, Y4 $40m. Two sequential tranches: **A = $100m** (paid first), **B = $100m**.

**Allocate principal top-down:**

| Year | Pool principal | To A | A remaining | To B | B remaining |
|---|---|---|---|---|---|
| 1 | 40 | 40 | 60 | 0 | 100 |
| 2 | 60 | 60 | 0 | 0 | 100 |
| 3 | 60 | 0 | 0 | 60 | 40 |
| 4 | 40 | 0 | 0 | 40 | 0 |

**WAL of A** $=\dfrac{1(40)+2(60)}{100}=\dfrac{40+120}{100}=\dfrac{160}{100}=\boxed{1.60\text{ yrs}}$

**WAL of B** $=\dfrac{3(60)+4(40)}{100}=\dfrac{180+160}{100}=\dfrac{340}{100}=\boxed{3.40\text{ yrs}}$

**Pool WAL** $=\dfrac{1(40)+2(60)+3(60)+4(40)}{200}=\dfrac{40+120+180+160}{200}=\dfrac{500}{200}=2.50\text{ yrs}$

**Reconcile:** the size-weighted average of the tranche WALs must equal the pool WAL:
$$\frac{100(1.60)+100(3.40)}{200}=\frac{160+340}{200}=2.50\text{ yrs}\;✓$$
Same collateral, one 2.50-year average life, carved into a short 1.60-year A note (money funds) and a longer 3.40-year B note (insurers). A's WAL is also far *more stable* against prepayment shocks because B absorbs the timing tail.

### B5. Loss allocation and credit enhancement

**Structure:** $500m pool. Senior A = $400m, Mezzanine B = $60m, Equity C = $40m. Losses hit C, then B, then A.

**Credit enhancement (subordination) at close:**
- A: cushion below $= B+C = \$100m \Rightarrow 100/500 = \mathbf{20\%}$.
- B: cushion below $= C = \$40m \Rightarrow 40/500 = \mathbf{8\%}$.
- C: **0%** — first-loss.

| Cumulative pool loss | Equity C ($40m) | Mezz B ($60m) | Senior A ($400m) | Impaired |
|---|---|---|---|---|
| $30m | −$30m → $10m | intact | intact | C only |
| $40m | wiped | intact | intact | C exactly exhausted |
| $70m | wiped | −$30m → $30m | intact | C, B partially |
| $100m | wiped | wiped | intact | A whole (full 20% used) |
| $110m | wiped | wiped | −$10m → $390m | A takes first loss |

**Reading it:** Senior A stays money-good until cumulative losses exceed **20%** ($100m) — exactly its subordination. At $110m (22%) of losses, A loses $110m − $100m = $10m, recovering $390m of $400m, i.e. **97.5 cents**. Tranching turned a mixed pool into a $400m security that survives a 20% loss event untouched — the mechanical basis of its AAA. ✓

---

## Section C — Interview-Style Questions with Model Answers

**C1. "Explain to me why an MBS is negatively convex."**
*Model answer:* "An MBS is a bond minus a call the borrower owns — the right to prepay. When rates fall, an ordinary bond's price rises, but here borrowers refinance, so principal comes back early and the price appreciation is capped; the prepay option I'm short is gaining value against me. When rates rise, prepayments slow and I'm stuck with a low coupon longer — extension. So my upside is limited and my downside isn't, which bends the price-yield curve concave: negative convexity. Practically, that's why I use effective duration and OAS, not modified duration, and why MBS trade at a spread to Treasuries to pay me for that short option."

**C2. "Walk me through how a AAA tranche can sit on subprime loans. Where does the safety come from?"**
*Model answer:* "The safety is structural subordination, not collateral quality. Say a $500m pool has $40m of equity and $60m of mezzanine beneath a $400m senior. The senior only takes a dollar of loss after cumulative pool losses exceed $100m — 20% of the pool. Historically a 20% cumulative loss is a deep-tail event, so the senior earns AAA. The critical assumption is that defaults are weakly correlated, so that 20% cushion is enough. In 2008 that assumption broke: national house prices fell, defaults correlated, losses blew past 20%, and 'AAA' tranches took hits. So I'd always stress the correlation assumption, not just the headline enhancement number."

**C3. "A PAC bond and its support bond come from the same pool. Which would you buy and why?"**
*Model answer:* "It depends on my mandate. The PAC has a promised principal schedule that holds as long as prepayment stays inside its collar, say 100–300 PSA, so it behaves almost like a bullet bond with a stable WAL — good for a liability-matching insurer who hates timing surprises, and it trades at a tight spread. The support tranche is the shock absorber: it eats excess principal when prepayments are fast and gets starved when slow, so it carries amplified contraction *and* extension risk. I'd buy the support only if I'm paid a wide enough spread and I have a view — say, that prepayments will stay moderate. The key point is that structuring didn't destroy the timing risk; it concentrated it in the support so the PAC could shed it."

**C4. "Why does CPR compound rather than just multiply SMM by 12?"**
*Model answer:* "Because prepayment is a survival process, not additive. Each month a fraction SMM of the *remaining* balance prepays, so after 12 months the surviving fraction is $(1-\text{SMM})^{12}$, and the annual prepaid fraction is $1-(1-\text{SMM})^{12}$. Multiplying by 12 would double-count — it ignores that the balance shrinks each month, so there's less left to prepay later. CPR is therefore always a bit *less* than 12×SMM. It's the same compounding logic as an annual return built from monthly returns."

**C5. "What went wrong in 2008 from a securitization-structure standpoint?"**
*Model answer:* "A chain of failures. Origination degraded to no-doc 'liar' loans under an originate-to-distribute model where originators kept no skin in the game. Rating agencies, paid by issuers and using low-correlation models, stamped AAA on senior tranches. ABS CDOs then re-securitized the mezzanine slices of subprime MBS — re-tranching already-thin risk and stacking correlation exposure everyone assumed away. The whole tower was funded short-term through repo and ABCP conduits, so it was a maturity mismatch on top of a credit problem. When house prices fell nationwide, defaults correlated, subordination was consumed, senior tranches took losses, mark-to-market collapsed, funding ran, and forced selling spread the fire. The post-crisis fixes — risk-retention rules, better correlation modelling, transparency, less rating reliance — target exactly those links."

---

## Section D — Multiple Choice (with Reasoning)

**D1.** In a cash-flow waterfall, losses are absorbed in which order?
A) Senior → mezzanine → equity  B) Equity → mezzanine → senior  C) Pro-rata across all tranches  D) Mezzanine → equity → senior
**Answer: B.** Cash flows down the stack senior-first, but *losses* run in reverse — equity is first-loss, senior is last. This mirror image is what lets the senior be AAA while the equity is levered.

**D2.** A pool prepays at SMM = 0.5% per month. The approximate CPR is:
A) exactly 6.0%  B) slightly below 6.0%  C) slightly above 6.0%  D) 0.5%
**Answer: B.** $\text{CPR}=1-(1-0.005)^{12}=1-0.99^{... }=5.84\%$, which is below 12×0.5%=6.0% because the balance shrinks each month. CPR is always less than 12×SMM.

**D3.** At 150 PSA, the CPR in month 20 is:
A) 4%  B) 6%  C) 9%  D) 3%
**Answer: B.** Base 100 PSA CPR in month 20 $=0.2\%\times 20=4\%$; at 150 PSA, $1.5\times 4\%=6\%$. (Note the base is still on its ramp at month 20 — it caps at 6% only at month 30 — so no cap binds here.)

**D4.** When interest rates fall sharply, an MBS holder most directly faces:
A) Extension risk  B) Contraction risk  C) Credit risk  D) Higher WAL
**Answer: B.** Falling rates trigger refinancing, prepayments accelerate, WAL shortens (contraction), and cash returns when reinvestment rates are low. Extension risk (A, D) is the rates-rise case.

**D5.** An interest-only (IO) strip typically has:
A) Large positive duration  B) Zero duration  C) Negative duration  D) The same duration as the pool
**Answer: C.** Fast prepayment destroys the balance the IO earns interest on, so the IO *loves* slow prepayment (high rates) and *hates* fast prepayment (low rates). Its price therefore *rises* when rates rise — negative duration. The PO is its mirror, with large positive duration.

**D6.** The senior tranche of a $500m deal with $40m equity and $60m mezzanine below it has a credit enhancement of:
A) 8%  B) 12%  C) 20%  D) 100%
**Answer: C.** Subordination below the senior $=40+60=\$100m$; $100/500=20\%$. The senior is untouched until cumulative losses exceed 20% of the pool.

**D7.** In a PAC/support CMO, the support (companion) tranche exists primarily to:
A) Provide external credit insurance  B) Absorb prepayment timing variability so the PAC gets a stable schedule  C) Increase the pool's total cash flow  D) Guarantee the senior's principal
**Answer: B.** The support soaks up excess principal when prepayments are fast and is starved when slow, stabilizing the PAC's WAL. It redistributes *timing* risk; it neither adds cash flow (C) nor provides credit protection (A, D).

**D8.** An ABS CDO of subprime mezzanine tranches was especially dangerous because:
A) It held only Treasury collateral  B) It re-tranched already-thin risk whose defaults were highly correlated  C) It had no senior tranche  D) It removed all prepayment risk
**Answer: B.** Pooling mezzanine slices whose defaults share a common driver (national house prices) meant the layers defaulted together, so the CDO's "AAA" senior was wiped almost as fast as its equity — correlation was the hidden switch.

---

*Self-verification note:* Every numerical result in Section B was cross-checked — the mortgage payment by confirming the interest/principal split reconciles to $M$; the CPR⇄SMM conversion by a full round-trip back to 4.00%; the dollar prepayment by confirming the SMM base excludes scheduled principal; the sequential WALs by rebuilding the pool WAL as their size-weighted average (2.50 yrs); and the loss table by confirming the senior's first loss occurs exactly at its 20% subordination. All figures reconcile to within rounding.
