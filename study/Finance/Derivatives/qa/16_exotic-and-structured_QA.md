# Q&A — Exotic Options and Structured Products

Practice bank for Chapter 16. Every question is followed by a full worked answer. Two running datasets recur: **(i) the barrier set** — a 1-year vanilla ATM call at ₹8.00, an up-and-out (H = 130) at ₹5.20, an up-and-in (H = 130) at ₹2.80; and **(ii) the note set** — a 5-year ₹1,000 Nifty capital-protected note, 6% continuously-compounded rate, 60% participation, ATM 5-year call costing ₹150 per note. The single organising idea throughout: **every structured product decomposes into a bond you can price plus an option package you can price.**

---

## Section A — Concept Check

**A1. Define an exotic option in one sentence, and give the three axes along which it departs from a vanilla.**

An exotic option is any option whose payoff depends on more than the terminal price of a single underlying at a single date. It extends the vanilla along three axes: **path dependence** (Asian, barrier, lookback — the trajectory matters), **discontinuity** (digital/binary — a step-function rule), and **multiple underlyings** (basket, rainbow, spread — correlation matters).

**A2. State in-out parity and explain why it must hold.**

For a common strike, barrier, and maturity: **knock-in + knock-out = vanilla**. It must hold because the two barrier options partition the set of all price paths into mutually exclusive, collectively exhaustive halves — those that touch the barrier (only the knock-in pays there) and those that never do (only the knock-out pays). Between them they reconstruct the vanilla's payoff on every path, so their premiums must sum to the vanilla's. It is the cleanest proof that exotics are re-slicings of vanilla value, not new money.

**A3. Why is a knock-out option cheaper than the equivalent vanilla?**

Because it forfeits payoff in an entire set of states — the paths where the barrier is touched. An option's premium is the discounted risk-neutral expectation of its payoff; removing payoff from some paths strictly reduces that expectation. The discount you pay less is exactly the value of the payoff in the knocked-out paths. Nothing is free — the cheapness *is* a hole in your protection.

**A4. Why does averaging make an Asian option cheaper than a vanilla?**

The payoff is driven by the average of many observations rather than one terminal price, and the variance of an average of positively-correlated observations is far lower than the variance of a single point. Lower effective volatility feeds directly into a lower option value. With monthly sampling over a year, an effective vol of ~30% can drop to ~17%, which is why an Asian can cost roughly half a comparable vanilla.

**A5. What makes barrier options a nightmare to hedge?**

The discontinuity at the barrier. An up-and-out call that is deep in the money is worth a great deal one tick below the barrier and *zero* the instant it is touched. Near the barrier and near expiry the **delta explodes and can flip sign**, so a hedger must trade violently and in large size around a knife-edge level. This is why barrier options carry wide bid-ask spreads and are often softened with **rebates** (small consolation cash on knock-out).

**A6. How do traders hedge a digital option, and why can't they hedge it cleanly?**

A digital pays a fixed lump if a condition holds, so its payoff is a step function and its delta spikes toward a Dirac impulse at the strike right before expiry — impossible to replicate exactly. Traders **super-replicate** with a tight **call spread**: long a call at K−ε, short a call at K+ε, scaled so the spread pays the notional over that narrow band. The width ε is the hedger's cushion; a tighter digital costs more to hedge and quotes a wider spread.

**A7. Why is a lookback the most expensive exotic?**

Because it removes all regret. A floating-strike lookback call pays S_T − min(S), letting you buy at the lowest price ever seen; a fixed-strike version pays max(S) − K, letting you sell at the highest. You always transact at the optimum point of the path, so the option captures the maximum possible favourable move — often 2–3× the vanilla premium. That cost is why lookbacks rarely appear in retail products.

**A8. Give the universal anatomy of a structured note.**

**Structured note = zero-coupon bond (the host) + option package (the engine).** The zero-coupon bond is bought at a discount and grows back to par at maturity, providing capital protection; the discount saved (par − bond cost) is the **option budget**, which the issuer spends on options to shape the upside while keeping a margin. To price or critique any note, strip it into these legs and price each.

**A9. Decompose an autocallable. In what sense is its coupon "sold volatility"?**

An autocallable = **short a down-and-in put** (the source of the enhanced coupon) + **a strip of digitals** (the conditional coupons) + an **autocall trigger** for early redemption. The investor is effectively *selling insurance*: the fat coupon is the premium collected on the short put. In calm markets you clip coupons; in a crash the knock-in put activates and you eat the full equity loss. The coupon is insurance premium, not interest.

**A10. Decompose a reverse convertible.**

Bond + **short put**. The investor receives a high fixed coupon, which is simply the put premium repackaged; in exchange, if the stock breaches a downside level, principal converts into shares and the investor absorbs the loss. It is the classic yield-enhancement trade — selling a put — wrapped as a note.

**A11. What is an embedded derivative, and where does a structured product's real risk live?**

An embedded derivative is a derivative-like feature inside a host contract that is not itself a standalone derivative — a convertible bond's conversion option, a callable bond's call, a capped loan. Under IFRS 9 / Ind AS 109 it may require **bifurcation** (separate fair-value measurement) if it is "not closely related" to the host, though for financial-asset hosts IFRS 9 now classifies the whole instrument together. The analyst's point: the fair value and risk of a structured product live in the embedded options, not in the bond wrapper.

**A12. "Capital-protected means risk-free." Refute this precisely.**

Protection is a *promise by the issuer*, not a law of nature. A capital-protected note is an unsecured bond, so if the issuer defaults the protection evaporates — Lehman "minibond" holders discovered this in 2008. Beyond credit risk, "protection" typically ignores **inflation**, **illiquidity**, and the **opportunity cost** of the issuer margin and the forgone risk-free return. Protected principal is not the same as protected purchasing power or a good return.

---

## Section B — Numerical / Applied Problems

**B1. Verify in-out parity on the barrier set and interpret the split.**

Up-and-out (₹5.20) + up-and-in (₹2.80) = **₹8.00** = the vanilla. ✔ The barrier splits the vanilla's ₹8.00 into two mutually exclusive worlds: the knock-out captures value only in paths that never reach 130; the knock-in only in paths that do. The knock-out is cheaper by ₹2.80 (35% of the premium) precisely because it forfeits the deep-in-the-money paths that ran past 130. A bull expecting a *moderate* rise buys the up-and-out and pockets the ₹2.80 saving — but gets nothing if the stock spikes through 130.

**B2. Asian vs vanilla — quantify the saving.** A vanilla European call on S₀ = 100 (r = 5%, σ = 30%, T = 1) is worth ₹14.23. A monthly-averaged arithmetic Asian call, same strike, prices at ₹8.10. Express the saving and explain the mechanism.

Saving = 14.23 − 8.10 = **₹6.13**, so the Asian costs **8.10 / 14.23 ≈ 57%** of the vanilla. Mechanism: the average of 12 monthly prices has far lower variance than the single terminal price, dragging effective volatility from 30% down to roughly 17%; lower vol → lower call value. The geometric Asian (₹7.95) sits just *below* the arithmetic because by Jensen's inequality the geometric mean ≤ arithmetic mean, so it pays slightly less — and its closed form makes it a handy **control variate** to speed up the arithmetic Monte Carlo.

**B3. Price the capital-protection leg of the note set.** Find the cost of the zero-coupon bond that returns ₹1,000 in 5 years at 6% continuously compounded, and the resulting option budget.

Bond cost = 1000 × e^(−0.06×5) = 1000 × e^(−0.30) = 1000 × 0.7408 = **₹740.80**. Option budget = 1000 − 740.80 = **₹259.20**. So about 26% of the investor's money is available to buy upside; the remaining 74% is tied up simply reconstituting the principal.

**B4. Participation and issuer margin.** An ATM 5-year call costs ₹150 per ₹1,000 notional. (a) What participation could the budget theoretically buy at zero margin? (b) What does the promised 60% participation cost? (c) What is the issuer's gross margin?

(a) Max participation = 259.20 / 150 = **1.728 ≈ 173%** at zero margin. (b) Cost of 60% call = 0.60 × 150 = **₹90.00**. (c) Total hedging cost = bond 740.80 + option 90.00 = **₹830.80**; the note sold at ₹1,000, so gross margin = 1000 − 830.80 = **₹169.20 (16.9%)**. The headline "100% protected + 60% upside" conceals that ~17% of the investor's money never went to work, and that the issuer could have offered nearly three times the participation.

**B5. Note payoff schedule.** Upside paid = 0.60 × Nifty return × ₹1,000, floored at zero. Tabulate the note payoff for Nifty returns of −30%, 0%, +20%, +50%, +100%.

| Nifty return (5 yr) | Upside paid | Note payoff | Total return |
|---|---|---|---|
| −30% | floored at 0 | ₹1,000 | 0% |
| 0% | ₹0 | ₹1,000 | 0% |
| +20% | ₹120 | ₹1,120 | +12% |
| +50% | ₹300 | ₹1,300 | +30% |
| +100% | ₹600 | ₹1,600 | +60% |

The floor protects principal on the downside; the 60% participation caps how much of the rally the investor keeps.

**B6. Break-even against a plain deposit.** The same ₹1,000 in a 6% continuously-compounded deposit for 5 years. What does it grow to, and how far must the Nifty rise for the note to beat it?

Deposit grows to 1000 × e^(0.30) = **₹1,350**, a +35% return with near-zero risk. The note beats it only when 0.60 × Nifty return > 35%, i.e. **Nifty return > ~58%** over five years. Below that, the "protected" investor earns *less than a bank deposit* while bearing the issuer's **credit risk** and the **opportunity cost** on the ₹169.20 margin. This is the chapter's punchline, made numerical.

**B7. Static replication of a digital via a call spread.** A cash-or-nothing call pays ₹100 if S_T > 100. You hedge with a call spread using strikes 99 and 101. How many spreads replicate the digital, and what is the residual risk?

The 99/101 call spread pays 0 below 99, rises linearly to ₹2 (the strike gap) at 101, and pays ₹2 above 101. To deliver the digital's ₹100 notional you buy **100 / 2 = 50 spreads** (long 50 calls at 99, short 50 at 101), which pay ₹100 for any S_T ≥ 101. Residual risk lives in the transition band 99–101: if the stock settles inside it, the call spread pays less than the digital's full ₹100 (a hedge shortfall) — but if it settles just below 100 the call spread *over-delivers* relative to the digital's zero. The narrower the strikes, the tighter the replication but the larger the position and cost. The hedger is deliberately **super-replicating** to stay on the safe side of the step.

---

## Section C — Interview-Style Questions with Model Answers

**C1. "Walk me through how you'd value and critique a capital-protected note you're handed at par."**

I decompose it. The note is a zero-coupon bond plus an option package. First I price the bond: par discounted at the issuer's funding rate — in our example ₹1,000 at 6% for 5 years is ₹740.80, so ₹259.20 is the option budget. Then I price the embedded option: the promised 60% participation on an ATM call costing ₹150 is ₹90. Bond plus option is ₹830.80, so the issuer baked in a ₹169.20, or 16.9%, gross margin. That immediately tells me two things: the participation could have been far higher — up to ~173% at zero margin — and roughly a sixth of my money is dead weight covering fees and spread. Finally I stress the payoff: the note only beats a plain 6% deposit if the Nifty rises more than about 58% over five years, and even the "protected" principal is an unsecured claim on the issuer. So my critique is: decompose, expose the margin, quantify the break-even, and name the credit risk. That habit — decompose before you opine — is the whole skill.

**C2. "A client wants cheaper downside protection and is sure the stock won't crash below a level. What do you sell them, and what's the catch?"**

A knock-out — specifically a down-and-out put. It's a vanilla put that dies if the stock falls to the barrier, so it's cheaper than the vanilla because it forfeits payoff in exactly the deep-crash paths the client swears are impossible. In-out parity makes the pricing transparent: down-and-out plus down-and-in equals the vanilla, so the discount is precisely the value of the down-and-in they're giving up. The catch is the hole: if the client is wrong and the stock does breach the barrier, their protection vanishes at the worst possible moment — right when they needed it. And near the barrier the option's delta goes haywire, so it's expensive and awkward for me to hedge, which widens the spread they pay. Cheapness is never free; it's the price of a real gap in the payoff.

**C3. "Why do you say an autocallable's coupon is not income? A retail investor sees a 9% coupon and thinks it's a bond."**

Because that coupon is sold volatility, not interest. Inside an autocallable the investor is short a down-and-in put and long a strip of digital coupons. The fat coupon is the premium collected for writing that put — the investor is selling crash insurance and being paid for it. In a calm or rising market the note autocalls early, they clip coupons, and it looks like a wonderful bond. But if the underlying breaches the knock-in barrier at maturity, the put activates and they absorb the full equity downside — principal and all. A real bond pays you interest and returns your principal regardless of equity moves; an autocallable's "coupon" is contingent and is the exact compensation for a tail risk they've unknowingly underwritten. Calling it income confuses a premium for a yield.

**C4. "Which is riskier, an Asian option or a vanilla? Most people assume the exotic."**

Most people are wrong here, and it's a good tell. An Asian is usually *less* risky and cheaper than the vanilla, because averaging reduces volatility — the average of many observations has lower variance than a single terminal price, so effective vol falls from, say, 30% to 17% and the premium roughly halves. "Exotic" just means a non-standard payoff, not a more dangerous one. It also hedges certain exposures *better*: a treasurer converting FX steadily all quarter is genuinely exposed to the average rate, so an average-rate option matches the real risk more tightly than a vanilla struck on one terminal date, and it resists end-of-period manipulation. The genuinely sharp-risk exotics are the barriers, digitals, and short-option structures — not the averaging ones. So I'd never equate "exotic" with "risky"; I'd price the specific payoff.

**C5. "Give me the single biggest hidden risk in a structured product and how you'd flag it to a client."**

Issuer credit risk. A "capital-protected" note is an unsecured claim on the issuer, so the protection is only as good as the issuer's solvency — Lehman minibond holders learned that their guaranteed principal was worth nothing when the guarantor failed. I'd flag it by refusing to let the word "protected" stand alone: I'd show the client that their principal is a bond they're lending to the bank, price in the issuer's credit spread, and put it alongside the opportunity cost — in our example ~17% of their money is issuer margin and they underperform a plain deposit unless the index rallies nearly 60%. Complexity and the framing "your capital is safe" is exactly what regulators like SEBI, MiFID II, and FINRA target for mis-selling, so naming credit risk, illiquidity, and opportunity cost explicitly is both the honest and the compliant thing to do.

---

## Section D — Multiple Choice (with reasoning)

**D1. Which of these is NOT path-dependent?**
(a) Asian (b) barrier (c) lookback (d) digital

**Answer: (d) digital.** A cash-or-nothing digital pays on a condition tested at the *terminal* date only — S_T > K — so it does not depend on the trajectory. Asians depend on the average path, barriers on whether a level was touched, and lookbacks on the max or min of the path; all three are path-dependent. (Some digitals are structured as one-touch/barrier-style, but the plain terminal digital in the chapter is not.)

**D2. In-out parity states that, for matching terms, knock-in + knock-out equals:**
(a) zero (b) the vanilla option (c) twice the vanilla (d) the rebate

**Answer: (b) the vanilla option.** The two barriers partition all price paths into touch/no-touch halves, so together they reconstruct the vanilla payoff on every path and their premiums sum to the vanilla's — 5.20 + 2.80 = 8.00 in the running set.

**D3. An Asian option is cheaper than a comparable vanilla primarily because:**
(a) it has a shorter maturity (b) the average has lower variance than the terminal price (c) it carries no credit risk (d) it is American-style

**Answer: (b).** Averaging suppresses volatility — the variance of an average of correlated observations is well below that of a single point — so effective vol and hence the premium fall. Maturity and exercise style are unchanged; the pricing effect is purely the variance reduction from averaging.

**D4. The delta of a digital option, just before expiry and near the strike, is best described as:**
(a) zero (b) exactly 1 (c) a large spike approaching a Dirac impulse (d) negative and constant

**Answer: (c).** The step payoff means value jumps from 0 to the notional across an infinitesimal price band at the strike, so the slope — the delta — blows up into a near-impulse there. This is why digitals can't be hedged cleanly and are super-replicated with a tight call spread.

**D5. Which exotic is typically the most expensive relative to a vanilla?**
(a) up-and-out call (b) average-price Asian (c) floating-strike lookback (d) cash-or-nothing digital

**Answer: (c) floating-strike lookback.** It removes all regret by settling against the best price seen over the life, capturing the maximum favourable move — often 2–3× the vanilla. The barrier and Asian are *cheaper* than vanilla; the digital is typically cheap too.

**D6. A reverse convertible note is best decomposed as:**
(a) zero-coupon bond + long call (b) bond + short put (c) bond + long put (d) two long calls

**Answer: (b) bond + short put.** The investor receives a high coupon (the put premium) in exchange for absorbing downside if the stock breaches a level and converts to shares. A bond + long call (a) is the capital-protected note, not the reverse convertible.

**D7. In the capital-protected note of the running example (₹1,000 par, 6% for 5 yr, ATM call ₹150, 60% participation), the issuer's approximate gross margin is:**
(a) ₹90 (b) ₹169 (c) ₹259 (d) ₹740

**Answer: (b) ₹169.** Bond cost ₹740.80 + 60% participation call (0.60 × 150 = ₹90) = ₹830.80 hedging cost; par ₹1,000 − ₹830.80 = **₹169.20** gross margin. ₹259 is the total option budget (before margin), ₹90 the option actually bought, ₹740 the bond leg.

**D8. "Capital-protected" most importantly still exposes the investor to:**
(a) no risk at all (b) unlimited upside (c) issuer credit (default) risk (d) margin calls

**Answer: (c) issuer credit risk.** The note is an unsecured claim on the issuer; if the issuer defaults, the protection is worthless (Lehman minibonds). There are no margin calls on a fully-paid note, and the upside is capped by the participation rate, not unlimited.

---

*Self-check performed: in-out parity verified (5.20 + 2.80 = 8.00); the bond leg recomputed as 1000 × e^(−0.30) = 740.80 with option budget 259.20; participation arithmetic (259.20/150 = 1.728; 0.60 × 150 = 90) and issuer margin (1000 − 830.80 = 169.20) reconciled against Chapter 16 Example 3; deposit break-even 1000 × e^(0.30) = 1350 and the ~58% Nifty threshold confirmed; the digital call-spread replication (100/2 = 50 spreads on a 99/101 pair) checked for payoff at and beyond the strikes.*
