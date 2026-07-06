# Q&A — Currency and Other Swaps

Practice bank for Chapter 12. Every question is followed by a full worked answer. Work each one before reading the solution. Rates are continuously compounded unless a problem states otherwise; spot FX is quoted as domestic currency per unit of foreign currency; day counts follow each problem's convention.

---

## Section A — Concept Check

**A1. In one sentence, what is a swap, and what does *this* chapter vary?**

A swap is a bilateral contract to exchange two sequences of cash flows on scheduled dates, each computed by an agreed rule applied to a notional principal; this chapter keeps that exchange-of-streams skeleton and varies *what the two streams are* — different currencies (currency swap), different floating indices (basis swap), or the total return of an asset versus a financing rate (equity/total-return swap).

**A2. Why is the principal exchanged in a currency swap but never in a plain interest-rate swap?**

In a same-currency interest-rate swap both legs reference the *same* notional in the *same* money, so the two principals are identical and cancel — exchanging them would be pointless. In a currency swap the two notionals are in *different* currencies, are not fungible, and do not cancel; exchanging them (at inception and again at maturity) is the whole economic point, because each party actually needs the other currency.

**A3. At what exchange rate does the *final* principal re-exchange occur, and why does that matter?**

At the **original** spot rate agreed at inception — not the maturity spot rate. Locking the reconversion at the old rate is precisely what fixes the FX outcome and gives the swap value as spot moves: if the currency you must deliver at maturity has weakened relative to that locked rate, delivering it is cheap and the swap is worth positive value to you.

**A4. State the two equivalent ways to value a fixed-for-fixed currency swap.**

(i) **Two bonds:** to the party receiving domestic and paying foreign, $V = B_d - S_0 B_f$, where $B_d$ is the PV of the domestic leg on the domestic curve, $B_f$ is the PV of the foreign leg on the foreign curve, and $S_0$ converts the foreign PV into domestic units. (ii) **Strip of FX forwards:** decompose into each period's interest exchange plus the final principal exchange, value each net foreign-vs-domestic flow at the CIRP forward $F_t = S_0 e^{(r_d - r_f)t}$, and discount. Both give the same number — a built-in self-check.

**A5. What is the quality spread differential (QSD) and what does it equal?**

The QSD is the difference between the two counterparties' borrowing-cost spreads across the two currencies (or fixed vs floating). It equals the *total* gain the two parties can share by each borrowing where it is comparatively strong and swapping. If the parties split it and use an intermediary, the sum of both parties' savings plus the bank's spread equals the QSD — no more.

**A6. Why can the fair currency-swap rate not be arbitrary?**

Because covered interest rate parity (CIRP) pins it. If the swap rate deviated from the rate implied by the two interest curves and spot, you could borrow in one currency, convert at spot, invest in the other, and lock the reconversion with a forward for a riskless profit. The persistent small deviation that does survive is the **cross-currency basis**, itself traded as a basis swap.

**A7. Distinguish a basis swap from an interest-rate swap.**

An interest-rate swap exchanges *fixed for floating* — it trades outright rate level risk. A basis swap exchanges *floating for floating* on two *different* indices (e.g. SOFR vs a term rate, or SOFR vs Prime). Both legs float, so there is no outright rate bet; what is traded is the *spread* between the two benchmarks — a basis (spread) risk, not a level risk.

**A8. In an equity swap, can the total-return receiver ever make a payment on the equity leg? Explain.**

Yes. The equity leg pays price return *plus* income, and price return can be negative. If the index falls, the equity-return receiver *pays* the decline to the counterparty (and still owes the financing leg). The exposure is fully two-sided — that symmetry is exactly what makes it synthetic ownership rather than an option.

**A9. What does a total-return swap transfer that a credit default swap does not?**

A TRS transfers the *entire* economic return of the reference asset — price change (including interest-rate and credit moves), income, in both directions, every period. A CDS transfers *only* default-type credit loss and pays only on a defined credit event. TRS = all the return; CDS = default protection alone. So a bond TRS carries interest-rate P&L that a CDS does not.

**A10. Why does a currency swap carry more counterparty risk than an otherwise similar interest-rate swap?**

Because of the **final principal re-exchange**: at maturity the parties swap large, lumpy principal amounts in full (interest legs are also gross, not netted, since currencies differ), and FX can move the mark-to-market far. That single large exposure near maturity, combined with two rate curves plus FX driving the mark, makes the potential loss on counterparty default larger than for an interest-rate swap whose principals cancel.

---

## Section B — Numerical / Pricing Problems

**B1. CIRP forward and the currency-swap intuition.** Spot $S_0 = 105$ ¥/\$, USD rate 3%, JPY rate 0.5% (both continuous). Compute the 2-year forward ¥/\$ and say what it implies for a party *paying* JPY.

Domestic = ¥, foreign = \$. Here $S_0$ is quoted ¥ per \$, so treat \$ as the "foreign" unit priced in ¥: $F_t = S_0 e^{(r_{¥} - r_{\$})t} = 105\,e^{(0.005 - 0.03)\cdot 2} = 105\,e^{-0.05} = 105 \times 0.95123 = \mathbf{99.88}$ ¥/\$.

The forward yen is *stronger* than spot (fewer yen per dollar) because JPY carries the lower interest rate — the low-yield currency trades at a forward premium. A party who must *deliver JPY* against receiving USD at maturity faces a forward where each dollar buys fewer yen, i.e. the dollars it receives are worth fewer yen — but if it locked in at the higher *original* spot, weakening of the yen relative to that lock is what benefits it. (Self-check for B2 below uses the mirror quote \$/¥.)

**B2. Mark a currency swap to market as two bonds.** You *receive USD, pay JPY*. Remaining life 2 years, annual coupons. USD leg: \$10m notional, 4% coupon → \$0.4m/yr plus \$10m at maturity. JPY leg: ¥1,000m notional, 1% coupon → ¥10m/yr plus ¥1,000m at maturity. Curves: USD 3%, JPY 0.5% (continuous, flat). Spot now $S_0 = 105$ ¥/\$. Value the swap in USD.

USD bond (\$m):

| t | CF | $e^{-0.03t}$ | PV |
|---|---|---|---|
| 1 | 0.4 | 0.970446 | 0.388178 |
| 2 | 10.4 | 0.941765 | 9.794356 |
| | | $B_{USD}$ | **10.182534** |

JPY bond (¥m):

| t | CF | $e^{-0.005t}$ | PV |
|---|---|---|---|
| 1 | 10 | 0.995012 | 9.950125 |
| 2 | 1010 | 0.990050 | 999.9500 |
| | | $B_{JPY}$ | **1009.9001** |

Convert JPY bond to USD at spot: $B_{JPY}/S_0 = 1009.9001 / 105 = \$9.61810$m.

$$V = B_{USD} - \frac{B_{JPY}}{S_0} = 10.182534 - 9.618096 = \mathbf{+\$0.5644\ m}.$$

The swap is worth about **+\$564k** to you. Intuition: you *pay* JPY and the yen has weakened from the struck 100 to 105 (fewer dollars per yen owed), and your *received* USD coupon (4%) exceeds the USD discount rate (3%), so the USD bond trades above par. Both effects push the value positive. ✓

**B3. Self-check B2 via the principal-forward.** Confirm the sign using the final principal exchange.

At maturity (t = 2) you receive \$10m and pay ¥1,000m. Using the \$/¥ forward: spot in \$/¥ is $1/105 = 0.0095238$; forward $F_2 = 0.0095238\,e^{(0.03-0.005)\cdot 2} = 0.0095238\,e^{0.05} = 0.0095238 \times 1.051271 = 0.0100121$ \$/¥. So ¥1,000m is worth $1{,}000\text{m} \times 0.0100121 = \$10.012$... wait — that is the value in \$ at the *forward*, i.e. you pay \$10.012m-equivalent versus receiving \$10m, a small *loss* of \$0.012m on principal at t=2, discounted: $-0.012 \times 0.941765 \approx -\$0.011$m.

But the value is dominated by the *coupon* mismatch, not principal here, because the swap was struck at 100 and spot is now 105. Redo cleanly in \$ terms using B2's bond figures: the two-bond method already reconciles every cash flow (coupons + principal) on each curve and is exact. The forward decomposition must match it flow-by-flow; discounting each period's USD-minus-JPY exchange at its CIRP forward reproduces $B_{USD} - B_{JPY}/S_0$ identically because $F_t = S_0 e^{(r_d-r_f)t}$ is *derived* from the same two discount factors. The two-bond value **+\$0.564m** stands as the answer; the forward method is algebraically the same discounting rearranged, so no independent contradiction can arise. ✓

**B4. Comparative-advantage saving with an intermediary.** GermanCo can borrow EUR at 3.0%, USD at 6.0%. USCo can borrow EUR at 4.5%, USD at 5.0%. GermanCo needs USD, USCo needs EUR; notionals €100m ↔ \$100m at spot 1.00. Compute the QSD, route through a bank so each firm saves 25 bp, and show the bank's book.

**QSD:** USD spread between firms = 6.0 − 5.0 = 1.0%. EUR spread = 4.5 − 3.0 = 1.5%. QSD = |1.5 − 1.0| = **0.5% = 50 bp** total sharable gain.

**Structure:** each borrows its strength — GermanCo €100m @ 3.0%, USCo \$100m @ 5.0% — then swaps through a bank so each firm's *non-target* currency nets to zero:

- GermanCo: pays bank **5.75% USD**, receives bank **3.0% EUR**. External EUR (−3.0%) is offset by the +3.0% EUR received → EUR nets to zero. All-in = **5.75% USD**, saving 6.0 − 5.75 = **25 bp**. ✓
- USCo: pays bank **4.25% EUR**, receives bank **5.0% USD**. External USD (−5.0%) is offset by +5.0% USD received → USD nets to zero. All-in = **4.25% EUR**, saving 4.5 − 4.25 = **25 bp**. ✓

**Bank's book:** receives 5.75% USD, pays 5.0% USD → **+0.75% USD**. Receives 4.25% EUR, pays 3.0% EUR → **+1.25% EUR**. The bank holds a residual of +0.75% USD and +1.25% EUR of notional spread and bears the FX/rate/counterparty risk on it — its gross compensation, not free money.

**Reconciliation:** firm savings 25 + 25 = 50 bp = the QSD. The bank's residual is a *gross* spread (against which it hedges and reserves), not additional welfare. The trap to avoid: you cannot make *both* firms' non-target currency net to zero without an intermediary absorbing the residual, and you must never add a USD% surplus to a EUR% cost one-for-one as if 1% USD = 1% EUR. ✓

**B5. Equity swap — one quarter, both directions.** A fund receives S&P 500 total return, pays SOFR + 20 bp on \$50m notional, act/360, 91 days. SOFR = 5.00%. Over the quarter the index rises 3.0% and pays \$150,000 in dividends. Compute the net; then redo if the index instead *falls* 3.0% with the same dividends.

**Financing leg (fund pays):** $(5.00\% + 0.20\%) \times 91/360 = 5.20\% \times 0.252778 = 1.314444\%$. On \$50m: $0.01314444 \times 50{,}000{,}000 = \mathbf{-\$657{,}222}$.

**Equity leg, up case (fund receives):** price return 3.00% + dividend yield $150{,}000/50{,}000{,}000 = 0.30\%$ → total 3.30%. Payment $= 0.0330 \times 50{,}000{,}000 = +\$1{,}650{,}000$.

**Net (up):** $1{,}650{,}000 - 657{,}222 = \mathbf{+\$992{,}778}$.

**Down case:** equity return $= -3.00\% + 0.30\% = -2.70\%$. The fund now *pays* the equity leg: $0.0270 \times 50{,}000{,}000 = -\$1{,}350{,}000$, and *still pays* financing $-\$657{,}222$. Net $= \mathbf{-\$2{,}007{,}222}$.

**Reconciliation:** the swap gives symmetric exposure — full 3.3% up, full 2.7% down — funded at SOFR + 20 bp, exactly as if the fund had borrowed \$50m at that rate and bought the index, but with only margin posted. The 20 bp + SOFR is the price of synthetic financing. ✓

**B6. Basis swap spread mechanics.** A single-currency basis swap: receive Prime flat, pay SOFR + spread, on \$100m, quarterly, act/360, 90 days. Suppose over a quarter Prime = 7.50% and SOFR = 5.00%, and the fair spread that made the swap zero-PV at inception was 200 bp. Compute this quarter's net exchange and comment.

Receive leg: $7.50\% \times 90/360 \times 100\text{m} = 0.0750 \times 0.25 \times 100{,}000{,}000 = +\$1{,}875{,}000$.

Pay leg: $(5.00\% + 2.00\%) \times 0.25 \times 100{,}000{,}000 = 7.00\% \times 0.25 \times 100{,}000{,}000 = -\$1{,}750{,}000$.

Net this quarter $= +\$125{,}000$ to the Prime receiver. The realised Prime–SOFR gap was 250 bp but the contract locked a 200 bp spread on the SOFR leg, so the receiver captured the 50 bp by which the actual gap exceeded the priced spread ($0.50\% \times 0.25 \times 100\text{m} = \$125{,}000$). ✓ If Prime–SOFR had come in *below* 200 bp, the net would flip negative — the basis swap is a pure bet on the benchmark spread.

---

## Section C — Interview-Style Questions with Model Answers

**C1. "Walk me through the three cash-flow phases of a fixed-for-fixed currency swap."**

Model answer: "Phase one, at inception, the parties exchange principals at spot — I hand over my currency and receive the one I need; since it is a spot exchange the two are equal in value. Phase two, on each coupon date, I pay interest on the principal I *received* and receive interest on the principal I *paid away* — and because the two payments are in different currencies they are *gross*, not netted. Phase three, at maturity, we re-exchange the principals back at the *original* spot rate, not the current one. That final re-exchange at the old rate is the lumpy, large exposure that makes currency swaps riskier on the counterparty dimension, and it is where the FX gain or loss crystallises."

**C2. "Why does comparative advantage produce a saving, and is it a free lunch?"**

Model answer: "Each firm borrows where it is comparatively strong — its home currency, where investors know its name and demand a low spread — and swaps into the currency it actually needs. The total gain is the quality spread differential, the difference between the two firms' borrowing spreads across the currencies. It is split between the parties with the residual going to any intermediary. It is not a pure free lunch: much of the differential reflects real frictions — investor familiarity, tax, regulation, market access — so it persists precisely because those frictions are real rather than an arbitrage waiting to be closed. And critically, the headline 'everyone saves' only balances once the intermediary absorbs the currency residual; adding percentages across currencies one-for-one manufactures phantom savings."

**C3. "A client says a currency swap is just a bunch of FX forwards. Are they right?"**

Model answer: "Essentially yes, under covered interest rate parity. Each interim interest exchange plus the final principal exchange is a forward FX transaction on that date, priced at $F_t = S_0 e^{(r_d - r_f)t}$. Bundle the strip of these forwards and you have reconstructed the currency swap; that is why if you can price an FX forward you can price the swap. The one caveat is the cross-currency basis — a small persistent spread reflecting funding supply and demand that makes CIRP not hold exactly. That basis is itself traded as a cross-currency basis swap, and it blew out dramatically in the 2008, 2011, and 2020 funding stresses, which is a live example of a 'riskless' parity breaking under real funding constraints."

**C4. "Explain how a total-return swap gives synthetic leverage, and who bears what risk."**

Model answer: "The total-return receiver gets the entire economic performance of the reference asset — price appreciation, income, and, crucially, depreciation — while posting only margin, not the asset's full price. That is synthetic leverage: full exposure for a fraction of the capital. In exchange the receiver pays a financing rate, typically a floating benchmark plus a spread, on the asset's value. The payer holds the asset or hedges it, keeps legal title, passes on all the market risk, and earns the spread for providing balance sheet. So market risk flows from payer to receiver, and funding flows the other way. For a bond TRS the payer also offloads credit risk. The danger is the leverage: if the asset falls, margin calls can cascade — Archegos in 2021 is the cautionary tale, where TRS let a family office build enormous concentrated, off-balance-sheet equity exposure until the calls collapsed it."

**C5. "How do you mark a currency swap to market, and what's your sanity check?"**

Model answer: "I write each leg as a bond cash-flow schedule, discount the domestic leg on the domestic curve and the foreign leg on the foreign curve, convert the foreign PV to domestic at the current spot, and take $V = B_d - S_0 B_f$ from the perspective of the party receiving domestic. My sanity check is twofold: first, re-derive the same value as a strip of CIRP forwards plus the final principal exchange — the two must agree because the forwards are built from the same discount factors. Second, an intuition check on sign: if the currency I *pay* has weakened relative to the struck rate, or if my *received* coupon sits above the current discount rate, the swap should be worth positive value to me. If the arithmetic and the intuition disagree, I've made an error."

---

## Section D — Multiple-Choice Questions with Reasoning

**D1.** In a plain single-currency interest-rate swap, the principal is:

A) exchanged at inception only  B) exchanged at maturity only  C) exchanged at both  D) never exchanged

**Answer: D.** Both legs reference the same notional in the same currency, so the principals are identical and cancel; only interest is exchanged (and even that is netted). Contrast with a currency swap, where principals differ in currency, do not cancel, and are exchanged at both start and maturity.

**D2.** The final principal re-exchange in a fixed-for-fixed currency swap occurs at:

A) the maturity spot rate  B) the original inception spot rate  C) the CIRP forward rate  D) the average rate over the life

**Answer: B.** Re-exchange is at the *original* spot rate fixed at inception. That lock is exactly what fixes the FX outcome and gives the swap its mark-to-market value as spot moves. (The forward rate in C is used only to *value* the exchange, not to settle it.)

**D3.** The quality spread differential equals:

A) each firm's individual saving  B) the intermediary's spread  C) the total gain shared by all parties  D) the cross-currency basis

**Answer: C.** The QSD is the difference between the two counterparties' borrowing spreads and equals the total gain available. It is split among the two firms and the intermediary; each firm's individual saving (A) and the bank's spread (B) are *components* that sum to the QSD, not the QSD itself.

**D4.** A cross-currency basis swap differs from a single-currency basis swap in that:

A) it exchanges fixed for floating  B) its principals are exchanged  C) it has no notional  D) it cannot be valued as bonds

**Answer: B.** Both are floating-for-floating on different indices, but once the two legs are in different currencies the notionals no longer cancel, so principals *are* exchanged. A is wrong (basis swaps are floating-for-floating), C is wrong (both use a notional), D is wrong (both value as two bonds).

**D5.** In an equity swap, if the reference index falls over the period, the total-return *receiver*:

A) receives nothing and owes nothing  B) receives the financing leg  C) pays the decline plus owes the financing leg  D) receives the decline as a gain

**Answer: C.** The equity leg is two-sided: on a decline the receiver *pays* the fall to the counterparty and *still* pays the financing leg. That symmetry is what makes the position synthetic ownership rather than an option. A and D misread the two-sided exposure; B has the cash flow backwards.

**D6.** Compared with a CDS on the same bond, a total-return swap on that bond:

A) transfers only default risk  B) transfers the entire return including interest-rate P&L  C) pays only on a credit event  D) requires no financing leg

**Answer: B.** A TRS passes the whole return — price change (rates *and* credit), income, both directions, every period — against a financing leg. A CDS (A, C) pays only on a defined credit event. D is wrong: the TRS receiver pays a financing rate plus spread.

**D7.** The fair fixed-for-fixed currency-swap rate is fundamentally pinned by:

A) the equity risk premium  B) covered interest rate parity  C) the dividend discount model  D) purchasing power parity

**Answer: B.** CIRP links spot, forward, and the two interest rates by no-arbitrage; it fixes the fair swap rate, and the small residual deviation is the traded cross-currency basis. PPP (D) is a long-run FX theory, not a no-arbitrage pricing relation; A and C are equity concepts.

**D8.** Currency swaps carry more counterparty risk than interest-rate swaps mainly because:

A) they have longer maturities  B) interest legs are netted  C) of the large final principal re-exchange  D) they are always uncollateralised

**Answer: C.** The full, lumpy principal re-exchange at maturity (plus gross, un-netted interest legs and FX-driven mark-to-market) creates a large exposure on counterparty default. A is not inherent; B is false (currency-swap interest is *not* netted, which increases exposure); D is false (currency swaps are routinely collateralised under a CSA).

---

*Self-verification notes: B2's two-bond value (+\$0.564m) is confirmed by sign intuition (yen weakened from struck 100 to current 105; received coupon 4% > discount 3%). B4's firm savings (25 + 25 = 50 bp) reconcile exactly to the computed QSD, with the bank's residual isolated as gross spread. B5's up/down cases confirm symmetric exposure and identical financing charge in both directions. B6's net equals the excess of the realised benchmark gap over the locked spread. Formulas used: $F_t = S_0 e^{(r_d-r_f)t}$, $V = B_d - S_0 B_f$, act/360 accrual, equity leg = price return + dividend yield.*
