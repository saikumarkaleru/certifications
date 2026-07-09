# Q&A — Interest Rate Swaps

A practice bank built around the *why*. A swap looks like an exotic contract but it is nothing more than a **package of simpler things you already know** — a strip of forward rate agreements, or equivalently a long floating-rate bond financed by a short fixed-rate bond. Every valuation below is enforced by that identity: if the two lenses ever disagreed by more than rounding, one of them would be an arbitrage. Work each problem to the last decimal and watch the two methods meet.

---

## Section A — Concept Check

**A1. In one sentence, what is a plain-vanilla interest rate swap, and what is the single most important thing that does *not* change hands?**

It is a bilateral contract to exchange a stream of **fixed** interest payments for a stream of **floating** payments on an agreed **notional principal**, over a set life, at set intervals. The notional itself is never exchanged in a single-currency swap — it is only a scaling number used to compute the interest amounts, and since both legs share it, the principals would just cancel. Only the **net** interest difference moves each period.

**A2. Define "payer" and "receiver". Which one profits when rates rise?**

The **payer** pays fixed and receives floating (pay-fixed); the **receiver** pays floating and receives fixed. The **payer profits when rates rise** — the floating leg it receives grows while the fixed leg it pays stays put, so its position is like being short a fixed-rate bond (positive duration exposure to rising rates). The receiver is the exact mirror. A swap is strictly zero-sum: the receiver's value equals minus the payer's value at every instant.

**A3. Why is a fresh swap worth exactly zero at inception?**

Because the **fixed rate is chosen precisely so that the present value of the fixed leg equals the present value of the floating leg**. That break-even fixed rate is the **swap rate** (or par rate). With equal PVs, the net value is zero, so no money changes hands up front. Only afterwards, as market rates drift away from the swap rate, does one leg become worth more than the other and the swap acquires a positive value to one side and an equal, opposite negative value to the other.

**A4. State the two equivalent valuation lenses for a pay-fixed swap.**

**Lens A — pair of bonds:** V(pay-fixed) = B(float) − B(fixed). You are long a floating-rate bond (you receive floating) and short a fixed-rate bond (you pay fixed); notionals cancel at maturity. **Lens B — strip of FRAs:** each period's net cash flow is N(fᵢ − s)τᵢ, discounted and summed, where fᵢ is the forward rate implied by today's curve. The two are the same identity rearranged; they must reconcile to the penny.

**A5. "You can't value the floating leg because future LIBOR is unknown." Rebut it.**

You never forecast future floating rates. Two facts do the work: (1) **a floating-rate bond is worth par at every reset date** — its coupon resets to the market rate, so it re-prices to face value — and (2) any future floating coupon you *do* need is captured by the curve's **forward rates**, which are extracted from today's discount factors: fᵢ = (DFᵢ₋₁/DFᵢ − 1)/τᵢ. The curve already embeds the market's rate expectations, so no forecast is required.

**A6. Write the par swap rate formula and explain each piece intuitively.**

s = (1 − DFₙ) / Σ τᵢ DFᵢ. The **numerator (1 − DFₙ)** is the present value of the floating leg per unit of notional (a par floater is worth 1 today and returns DFₙ of principal value, so its coupon stream is worth the difference). The **denominator** is the **annuity factor** — the PV of receiving one unit of accrual each period. So the swap rate is simply *floating-leg PV divided by the annuity*: the level fixed coupon that makes the two legs' PVs equal.

**A7. What is the comparative-advantage motive, and why is the "saving" not pure arbitrage?**

When a strong borrower has a large edge in the fixed market and a weaker borrower has a smaller disadvantage in the floating market, each is cheapest in a different market. If each borrows where it is relatively best and then swaps into the rate *type* it actually wants, the "difference of the differences" in the two spreads can be shared. But part of that gain compensates the floating borrower for **rollover and credit-review risk** — floating quotes reset and embed the lender's option to re-price, whereas fixed is locked. So it is not a free lunch; the more robust rationale for swaps is exposure **transformation**, not arbitrage.

**A8. What is the swap curve, and what does OIS discounting mean?**

The **swap curve** is the term structure of quoted par swap rates (1Y, 2Y, 5Y, 10Y, 30Y), **bootstrapped** sequentially into discount factors that then price the whole fixed-income complex. **OIS discounting** means cash flows are discounted on a risk-free **overnight-indexed** curve (SOFR/ESTR), kept separate from the index (forward-projection) curve. Two curves for two jobs: *project* the floating leg on the index curve, *discount* both legs on OIS. Full collateralisation is what makes OIS the correct discount rate.

**A9. What is DV01 and roughly how large is it?**

DV01 (dollar value of a basis point, a.k.a. PV01) is the change in swap value for a 1bp parallel shift in the curve. It is approximately the **annuity factor × notional × 0.0001** — essentially the DV01 of the fixed leg, because the floating leg has near-zero duration (it re-prices to par each reset). It is the number the dealer hedges, typically with bond futures.

---

## Section B — Numerical / Pricing Problems

**B1. Par swap rate on a flat curve.**

*Given:* 2-year annual-pay swap, N = $100M, zero curve flat at 3.00% (annual compounding).

Step 1 — Discount factors: DF₁ = 1/1.03 = 0.970874; DF₂ = 1/1.03² = 0.942596.
Step 2 — Annuity: A = 0.970874 + 0.942596 = 1.913470.
Step 3 — Par rate: s = (1 − DF₂)/A = (1 − 0.942596)/1.913470 = 0.057404/1.913470 = **0.030000 = 3.000%**.

*Reconcile:* On a flat 3% curve the par swap rate equals the flat rate. Check the legs: fixed-leg PV per unit = s·A = 0.03 × 1.913470 = 0.057404; floating-leg PV = 1 − DF₂ = 0.057404. Equal → V = 0 at inception. ✓

**B2. Value a seasoned pay-fixed swap TWO ways and reconcile.**

*Given:* Existing pay-fixed swap, 2 annual payments left, fixed rate **3.50%**, N = $100M, standing on a reset date, curve flat at **3.00%**. Use DF₁ = 0.970874, DF₂ = 0.942596 from B1.

*Lens A — as bonds.* V(pay-fixed) = B(float) − B(fixed).
Floating bond at a reset date = par = **$100.000M**.
Fixed bond: coupon = 100 × 0.035 = $3.5M/yr, plus $100M principal at year 2.

| Year | Cash flow ($M) | DF | PV ($M) |
|---|---|---|---|
| 1 | 3.5 | 0.970874 | 3.398059 |
| 2 | 103.5 | 0.942596 | 97.558686 |
| **Total** | | | **100.956745** |

V(pay-fixed) = 100.000000 − 100.956745 = **−$0.956745M**.

*Lens B — as FRAs.* Flat curve → every forward fᵢ = 3.000%. Net CF each year = N(f − s)τ = 100 × (0.03 − 0.035) × 1 = **−$0.5M**.

| Year | Net CF ($M) | DF | PV ($M) |
|---|---|---|---|
| 1 | −0.5 | 0.970874 | −0.485437 |
| 2 | −0.5 | 0.942596 | −0.471298 |
| **Total** | | | **−0.956735** |

V(pay-fixed) = **−$0.9567M**.

*Reconcile:* Lens A = −0.956745M; Lens B = −0.956735M. They agree to the rounding of the 6-dp discount factors (0.00001M gap). *Sign check:* you locked in paying 3.50% when the market is only 3.00%, so the pay-fixed side is under water — negative value is correct. The receiver's value is the exact mirror, **+$0.957M**. ✓

**B3. Comparative-advantage split — trace both firms' all-in cost.**

*Given:*

| Firm | Fixed | Floating |
|---|---|---|
| AAA | 4.00% | LIBOR + 0.10% |
| BBB | 5.20% | LIBOR + 0.70% |

Step 1 — Total gain = differential of differentials = (5.20 − 4.00) − (0.70 − 0.10) = 1.20% − 0.60% = **0.60%**.
Step 2 — AAA borrows where it is strongest (fixed 4.00%); BBB borrows where it is least-bad (floating LIBOR + 0.70%).
Step 3 — Swap: BBB pays AAA **4.35% fixed**; AAA pays BBB **LIBOR**.

| | AAA (wants floating) | BBB (wants fixed) |
|---|---|---|
| Pays on real debt | 4.00% | LIBOR + 0.70% |
| Receives on swap | 4.35% | LIBOR |
| Pays on swap | LIBOR | 4.35% |
| **All-in** | **LIBOR − 0.35%** | **5.05%** |
| Direct cost | LIBOR + 0.10% | 5.20% |
| **Saving** | **0.45%** | **0.15%** |

*Reconcile:* Savings sum to 0.45% + 0.15% = **0.60%** — exactly the differential of differentials. ✓ (A dealer in the middle would skim a few bp, so the two firms share slightly less than 0.60% in practice.)

**B4. Par swap rate and forwards on an upward-sloping curve.**

*Given:* 3-year annual swap. Zero rates: 3.00%, 3.50%, 4.00% (annual compounding).

Step 1 — Discount factors: DF₁ = 1/1.03 = 0.970874; DF₂ = 1/1.035² = 0.933511; DF₃ = 1/1.04³ = 0.888996.
Step 2 — Annuity: A = 0.970874 + 0.933511 + 0.888996 = 2.793381.
Step 3 — Par swap rate: s = (1 − DF₃)/A = (1 − 0.888996)/2.793381 = 0.111004/2.793381 = **3.974%**.

Note s = 3.974% sits *below* the 3-year zero (4.00%): the fixed coupon is paid across all three years including the cheaper early ones, so the par rate is a PV-weighted blend, not the terminal zero.

Step 4 — Implied forwards (the floating leg's projected fixings):
f₁ = 1/DF₁ − 1 = **3.000%**; f₂ = DF₁/DF₂ − 1 = 0.970874/0.933511 − 1 = **4.002%**; f₃ = DF₂/DF₃ − 1 = 0.933511/0.888996 − 1 = **5.007%**.

Step 5 — Cross-check floating-leg PV via forwards:

| Year | fᵢ | DFᵢ | fᵢ·DFᵢ |
|---|---|---|---|
| 1 | 3.000% | 0.970874 | 0.029126 |
| 2 | 4.002% | 0.933511 | 0.037363 |
| 3 | 5.007% | 0.888996 | 0.044515 |
| **Total** | | | **0.111004** |

*Reconcile:* Σ fᵢ·DFᵢ = 0.111004 = 1 − DF₃ — the "floating-leg PV = 1 − DFₙ" shortcut holds without summing forwards. And fixed-leg PV = s·A = 0.039738 × 2.793381 = 0.111003. Legs match → V = 0 at the par rate. ✓

**B5. Transforming a liability — synthetic fixed cost.**

*Given:* AquaCorp has a floating loan at **LIBOR + 0.80%**. It enters a swap to **receive LIBOR** and **pay 3.50% fixed**.

| Cash flow | Direction | Rate |
|---|---|---|
| Real loan | pays | LIBOR + 0.80% |
| Swap | receives | LIBOR |
| Swap | pays | 3.50% |

Net = −(LIBOR + 0.80%) + LIBOR − 3.50% = the two LIBOR legs cancel exactly → **pays 3.50% + 0.80% = 4.30% fixed**.

*Reconcile:* AquaCorp converted a floating loan into a **synthetic fixed loan at 4.30%** with no refinancing — its interest bill no longer moves with rates. This transformation, not arbitrage, is the dominant real-world use of swaps. ✓

**B6. DV01 of a swap.**

*Given:* The 2-year swap of B1, N = $100M, annuity A = 1.913470.

Step 1 — DV01 ≈ A × N × 0.0001 = 1.913470 × 100,000,000 × 0.0001 = **$19,134.70 per basis point**.
Step 2 — Interpretation: a 1bp rise in the curve changes the swap's value by roughly $19k. For the pay-fixed party value *rises* on a rate increase (positive DV01 sign), because it is effectively short a fixed bond.

*Reconcile:* DV01 is dominated by the fixed leg — the floating leg re-prices to par each reset and carries near-zero duration, so almost all rate risk lives in the fixed annuity. A dealer would neutralise this ~$19k/bp with an offsetting position in bond futures. ✓

---

## Section C — Interview-Style (with model answers)

**C1. "Walk me through why a swap is worth zero on day one."**

*Model answer:* At inception nobody pays a premium, so the contract must be fair to both sides. The only free parameter is the fixed rate, set at the **par swap rate** — the level that makes the fixed leg's PV equal the floating leg's PV. Equal PVs means net value zero, exactly as a freshly-struck forward has zero value: the terms are calibrated to today's curve. The swap only *acquires* value later, when rates drift and one leg pulls ahead; that is why swaps are marked to market and collateralised daily.

**C2. "Two methods for valuing a swap. Do they ever give different answers?"**

*Model answer:* No — not economically. The bond method (long floater, short fixed bond) and the FRA-strip method (net of forward-versus-fixed each period, discounted) are the **same identity rearranged**. If I discount a floating bond's coupons using the very forward rates I would use in the FRA method, the floating bond collapses to par at each reset, and the two expressions become algebraically identical. Any numerical gap you see is pure rounding in the discount factors. I'd pick whichever the data hands me: par-rate/discount-factor data favours the bond lens, a quoted forward curve favours the FRA lens.

**C3. "A corporate treasurer has a floating loan and fears rising rates. What do you sell her, and what's the catch?"**

*Model answer:* A **pay-fixed swap**: she keeps her existing loan untouched but enters a swap to receive floating (offsetting the loan's floating coupon) and pay a fixed swap rate. The two floating legs cancel and she is left with a clean synthetic fixed cost — certainty on her interest bill. The catches: (1) she gives up the upside if rates *fall* — she is locked into the fixed rate, so a swaption or cap might suit her better if she wants protection with participation; (2) the swap introduces **counterparty/credit risk** and, if uncollateralised, funding and CVA considerations; and (3) basis risk if her loan's index or reset dates don't exactly match the swap's. If she wants a floor on the pain but keeps the gain, I'd pitch an interest-rate **cap** instead of a swap.

**C4. "Is the comparative-advantage saving real money, or an accounting illusion?"**

*Model answer:* Partly real, partly compensation for risk. The arithmetic gain — the difference between the fixed and floating credit spreads of the two firms — is genuine and gets shared. But it isn't a pure arbitrage: the floating borrower's rate resets periodically, and the lender retains an option to re-price or pull credit if the borrower deteriorates. The fixed borrower has no such exposure. So a chunk of the "saving" is really a premium the floating borrower earns for bearing rollover and credit-review risk. That's why sophisticated desks don't lean on comparative advantage as the reason to swap — the durable rationale is **transforming an exposure** you already have without refinancing it.

**C5. "Why did the market move to OIS discounting, and what problem did it solve?"**

*Model answer:* Pre-2008 desks discounted swap cash flows on LIBOR itself, implicitly assuming LIBOR was risk-free. The crisis blew that apart — LIBOR carried bank credit and liquidity risk, and the LIBOR-OIS spread widened sharply. For a **fully-collateralised** swap the cash flows are effectively risk-free and funded at the **overnight rate** paid on collateral, so the correct discount curve is OIS (SOFR/ESTR), not LIBOR. The fix splits the job: *project* floating on the index curve, *discount* everything on OIS — removing a systematic mispricing and aligning valuation with how collateral actually funds the trade.

---

## Section D — MCQs (with reasoning)

**D1. In a single-currency plain-vanilla swap, the notional principal is:**
(a) exchanged at inception (b) exchanged at maturity (c) exchanged at both (d) never exchanged.

**Answer: (d).** The notional is only a scaling factor for the interest calculation. Both legs share it, so the principals would cancel — they are omitted, and only net interest changes hands. (Currency swaps are the exception, where principal *is* exchanged because the two legs are in different currencies.)

**D2. A pay-fixed swap gains value when:**
(a) rates fall (b) rates rise (c) the curve is flat (d) volatility falls.

**Answer: (b).** The payer receives floating and pays a fixed coupon. When rates rise, the floating receipts grow while the fixed payments are stuck below market, so the position gains — it behaves like a short fixed-bond position with positive duration. It loses when rates fall.

**D3. The par swap rate equals:**
(a) DFₙ / Σ τᵢDFᵢ (b) (1 − DFₙ)/Σ τᵢDFᵢ (c) (1 + DFₙ)/Σ τᵢDFᵢ (d) 1 − DFₙ.

**Answer: (b).** Numerator (1 − DFₙ) is the floating-leg PV per unit notional; denominator Σ τᵢDFᵢ is the annuity factor. The ratio is the fixed coupon that equates the two legs' PVs. On a flat 3% curve this returns exactly 3% (verified in B1).

**D4. Immediately after a reset, a floating-rate bond is worth:**
(a) above par (b) below par (c) par (d) indeterminate.

**Answer: (c).** At the reset the coupon is set to the current market rate, so the bond re-prices exactly to face value — par. This is the key fact that lets you value the floating leg without forecasting future rates.

**D5. A 3-year $100M pay-fixed swap struck at 4% fixed, valued on a flat 3% curve, is worth approximately:**
(a) +$2.83M (b) −$2.83M (c) $0 (d) −$4.00M.

**Answer: (b).** Fixed bond PV ≈ $102.83M, floating bond = par = $100M, so V(pay-fixed) = 100 − 102.83 = **−$2.83M**. You are locked into paying 4% when the market is 3%, so the pay-fixed side is under water. The FRA lens gives the same figure. (The receiver's value is +$2.83M.)

**D6. Under modern practice, the two legs of a collateralised swap are:**
(a) discounted on different curves (b) projected and discounted on LIBOR (c) both discounted on the OIS curve, floating projected on the index curve (d) both discounted on the government curve.

**Answer: (c).** Two curves, two jobs: *project* the floating leg on the index/forward curve to get its coupons, then *discount both legs on the same OIS curve*. It is not "one curve per leg" — that is a classic interview trap.

**D7. The DV01 of a plain-vanilla swap is dominated by:**
(a) the floating leg (b) the fixed leg (c) the notional exchange (d) neither leg.

**Answer: (b).** The floating leg re-prices to par at each reset and carries near-zero duration, so almost all interest-rate sensitivity lives in the **fixed** leg's annuity. DV01 ≈ annuity × notional × 0.0001.

---

## One-Page Recap

- A swap = strip of FRAs = long floater − short fixed bond. Same object, two lenses, reconcile to the penny.
- Par swap rate: **s = (1 − DFₙ)/Σ τᵢDFᵢ**. Flat curve ⇒ s equals the flat rate.
- Value zero at inception; drifts as rates move. Floating leg = par at each reset; forwards from fᵢ = (DFᵢ₋₁/DFᵢ − 1)/τᵢ.
- Pay-fixed gains when rates rise; DV01 ≈ annuity × notional × 1bp. Receiver's value = − payer's; always zero-sum.
- Discount both legs on OIS; project floating on the index curve. Comparative-advantage gain is shared, not pure arbitrage.
