# Q&A — Put-Call Parity

Practice bank for Chapter 07. Every question is followed by a full worked answer. Attempt each one on paper before reading the solution. All options are European on a non-dividend stock unless the question states otherwise, and rates are continuously compounded unless quoted differently.

---

## Section A — Concept Check

**A1. State put-call parity in its base form and name each of the four instruments.**

`C + K·e^(−rT) = P + S₀`. The left side is a *fiduciary call* — a long call plus a bond (cash `K·e^(−rT)`) that matures to exactly `K`. The right side is a *protective put* — a long put plus one share of stock. The four instruments tied together are the call `C`, the put `P`, the strike-bond `K·e^(−rT)`, and the spot `S₀`.

**A2. Why is parity called "model-free," and why does that matter?**

It is derived purely from the no-arbitrage principle: two portfolios that pay identically in every future state must cost the same today. Nowhere does the derivation invoke volatility, expected return, probabilities of up/down moves, or risk preferences. It matters because any correct pricing model — binomial, Black-Scholes, anything — must obey parity automatically, so parity becomes a fast, assumption-free consistency check on prices and on models.

**A3. Both parity portfolios are worth the same amount at expiry. What is it, and why?**

Both are worth `max(S_T, K)`. If `S_T > K`: the call pays `S_T − K` and the bond pays `K`, summing to `S_T`; on the other side the put expires worthless and the share is worth `S_T`. If `S_T ≤ K`: the call is worthless and the bond pays `K`; the put pays `K − S_T` and the share is worth `S_T`, summing to `K`. Two different mechanisms, one identical payoff of `max(S_T, K)`.

**A4. What does parity tell you about C and P — levels or difference?**

Only their *difference*, `C − P = S₀ − K·e^(−rT)`. Parity never pins the absolute level of either option; those levels require a volatility input and a model. This is the single most common misunderstanding — you can spot a parity violation and arbitrage it without ever knowing whether the call "should" cost 6 or 8.

**A5. Show that long call + short put (same strike, same expiry) is a synthetic forward.**

At expiry the combination pays `max(S_T − K, 0) − max(K − S_T, 0)`. If `S_T > K` that is `(S_T − K) − 0 = S_T − K`; if `S_T ≤ K` it is `0 − (K − S_T) = S_T − K`. Either way the payoff is `S_T − K` — a straight line with no kink, exactly a long forward struck at `K`. Consistently, its cost `C − P = S₀ − K·e^(−rT) = (F₀ − K)·e^(−rT)`.

**A6. When K equals the forward price F₀, how do C and P compare?**

They are equal, `C = P`. From `C − P = (F₀ − K)·e^(−rT)`, setting `K = F₀` gives `C − P = 0`. This "at-the-money-forward" identity is why desks quote straddles around the forward rather than the spot.

**A7. How does parity change for a stock paying discrete dividends with present value D?**

The stockholder in the protective-put portfolio collects `D` that the call holder does not, so you strip it out of the stock leg: `C + K·e^(−rT) = P + S₀ − D`, equivalently `C + D + K·e^(−rT) = P + S₀`. For a continuous dividend yield `q`, replace `S₀` with `S₀·e^(−qT)`.

**A8. Why is parity only an inequality for American options?**

American options can be exercised early, which breaks the clean payoff-matching (the two portfolios can be disturbed before `T`). For an American non-dividend stock you get a band, `S₀ − K ≤ C − P ≤ S₀ − K·e^(−rT)`, not an equation. Writing American parity as an equality is a classic trap.

**A9. Name the two arbitrage trades and when each is used.**

A *conversion* — long stock + long put + short call — is run when the call/bond side is rich (left side of parity too expensive). A *reversal* (reverse conversion) — short stock + short put + long call + lend — is the mirror, run when the put/stock side is rich. Both lock a profit at `t = 0` and net to zero at expiry.

**A10. What does parity imply about the Greeks of a call and put at the same strike?**

Differentiating the identity — where `K·e^(−rT)` is deterministic — gives `Δ_C − Δ_P = 1` (non-dividend), `Γ_C = Γ_P`, and `Vega_C = Vega_P`. The call and put share identical gamma and vega, which is why a market-maker can run both on one hedged book. It also forces a call and put at the same strike/expiry to imply the *same* volatility.

---

## Section B — Numerical / Pricing Problems

**B1. Verify parity and detect any arbitrage.** `S₀ = 100`, `K = 100`, `T = 0.25`, `r = 6%` continuous, quoted `C = 8`, `P = 5`. Is there free money?

PV of strike: `K·e^(−rT) = 100·e^(−0.015) = 100·0.985112 = 98.5112`.

| Side | Expression | Value |
|---|---|---|
| Left (call + bond) | `8 + 98.5112` | 106.5112 |
| Right (put + stock) | `5 + 100` | 105.0000 |

The sides differ by `1.5112`, so parity is violated. The left (call + bond) is rich; the right (put + stock) is cheap. Sell rich, buy cheap: write the call (+8), buy the put (−5), buy the share (−100), borrow `98.5112`. Net cash today `= 8 − 5 − 100 + 98.5112 = +1.5112`, harvested risk-free. Fair prices need `C − P = S₀ − K·e^(−rT) = 1.4888`; the quoted `C − P = 3` is `1.5112` too wide — exactly the profit.

**B2. Confirm the B1 trade nets to zero at expiry.** Check `S_T = 120` and `S_T = 90`. The loan repays to `98.5112·e^(0.015) = 100 = K`.

| At expiry | Short call | Long put | Sell share | Repay loan | Net |
|---|---|---|---|---|---|
| `S_T = 120` | `−(120−100) = −20` | `0` | `+120` | `−100` | `0` |
| `S_T = 90` | `0` | `+(100−90) = +10` | `+90` | `−100` | `0` |

Both states net to exactly `0`. The `+1.5112` collected up front is therefore pure arbitrage — a textbook *conversion*.

**B3. Price a put from a call, no dividends.** `S₀ = 250`, `K = 260`, `T = 0.5`, `r = 8%` continuous, observed `C = 12`. Find the fair put.

`K·e^(−rT) = 260·e^(−0.04) = 260·0.960789 = 249.8051`. Rearranged parity: `P = C − S₀ + K·e^(−rT) = 12 − 250 + 249.8051 = 11.8051`. So `P ≈ 11.81`. Sanity: strike (260) sits above spot (250), so the put is somewhat in-the-money and the call somewhat out; yet the forward `F₀ = 250·e^(0.04) = 260.204` is just above `K`, making them nearly balanced, so `P ≈ C` — consistent with `11.81` vs `12`.

**B4. Same as B3 but with a dividend.** Now the stock pays `₹4` in two months (`t = 1/6` yr). Re-price the put and reconcile.

PV of dividend: `D = 4·e^(−0.08·(1/6)) = 4·e^(−0.013333) = 4·0.986755 = 3.9470`. Dividend parity `C + K·e^(−rT) = P + S₀ − D` gives `P = C + K·e^(−rT) − S₀ + D = 12 + 249.8051 − 250 + 3.9470 = 15.7521`, so `P ≈ 15.75`. The dividend lowers the effective stock leg, pushing the put up from 11.81 to 15.75. Reconcile with `C − P = (F₀ − K)·e^(−rT)` where `F₀ = (S₀ − D)·e^(rT) = (246.0530)·e^(0.04) = 246.0530·1.040811 = 256.0951`. Then `(256.0951 − 260)·0.960789 = (−3.9049)·0.960789 = −3.7521`, and directly `C − P = 12 − 15.7521 = −3.7521`. The two match — the put is internally consistent.

**B5. Solve for the implied risk-free rate.** `S₀ = 50`, `K = 50`, `T = 1`, `C = 6`, `P = 4`, no dividends. What continuously compounded `r` makes prices parity-consistent?

Parity: `C − P = S₀ − K·e^(−rT)` → `6 − 4 = 50 − 50·e^(−r)` → `2 = 50(1 − e^(−r))` → `1 − e^(−r) = 0.04` → `e^(−r) = 0.96` → `r = −ln(0.96) = 0.040822`, i.e. about `4.08%`. Check: `50·e^(−0.040822) = 50·0.96 = 48`, so `S₀ − K·e^(−rT) = 50 − 48 = 2 = C − P` ✓.

**B6. Build a synthetic long stock and verify its cost.** Using B1 data (`C = 8`, `P = 5`, `K·e^(−rT) = 98.5112`), construct synthetic long stock and compare its cost to `S₀`.

Synthetic stock `= C − P + K·e^(−rT)` (long call, short put, lend PV of `K`). Cost `= 8 − 5 + 98.5112 = 101.5112`. The actual share costs `100`. The synthetic is `1.5112` dearer — the same `1.5112` mispricing from B1, seen from another angle. Fairly priced, the synthetic would cost exactly `S₀ = 100`.

**B7. Continuous dividend yield.** `S₀ = 400`, `K = 410`, `T = 0.5`, `r = 5%`, dividend yield `q = 2%`, `C = 15`. Find the fair put.

Dividend-yield parity: `C + K·e^(−rT) = P + S₀·e^(−qT)`. Compute `K·e^(−rT) = 410·e^(−0.025) = 410·0.975310 = 399.8770`; `S₀·e^(−qT) = 400·e^(−0.01) = 400·0.990050 = 396.0199`. Solve `P = C + K·e^(−rT) − S₀·e^(−qT) = 15 + 399.8770 − 396.0199 = 18.8571`, so `P ≈ 18.86`. Direction check: strike above spot and a low net-carry forward → put richer than call, `18.86 > 15` ✓.

**B8. FX parity.** A EUR call struck at `K = 1.10` USD/EUR, `T = 1`, spot `S₀ = 1.08`, domestic (USD) rate `r_d = 4%`, foreign (EUR) rate `r_f = 3%`, call `C = 0.035` USD. Find the put.

Garman-Kohlhagen parity: `C + K·e^(−r_d T) = P + S₀·e^(−r_f T)`. `K·e^(−r_d T) = 1.10·e^(−0.04) = 1.10·0.960789 = 1.056868`; `S₀·e^(−r_f T) = 1.08·e^(−0.03) = 1.08·0.970446 = 1.048082`. Solve `P = C + K·e^(−r_d T) − S₀·e^(−r_f T) = 0.035 + 1.056868 − 1.048082 = 0.043786`, so `P ≈ 0.0438` USD.

**B9. Reconcile parity inside a binomial model.** `S₀ = 100`, up to `110` or down to `95` in `T = 0.25`, `r = 6%` continuous, `K = 100`. Price call and put, then check parity.

`e^(rT) = e^(0.015) = 1.015113`. Risk-neutral prob `p = (e^(rT) − d)/(u − d) = (1.015113 − 0.95)/(1.10 − 0.95) = 0.065113/0.15 = 0.434087`. Call payoffs: up `10`, down `0` → `C = e^(−rT)·p·10 = 0.985112·4.34087 = 4.2763`. Put payoffs: up `0`, down `5` → `P = e^(−rT)·(1−p)·5 = 0.985112·2.829565 = 2.7876`.

| Side | Value |
|---|---|
| `C + K·e^(−rT) = 4.2763 + 98.5112` | 102.7875 |
| `P + S₀ = 2.7876 + 100` | 102.7876 |

They agree to rounding — the binomial model satisfies parity automatically. Synthetic forward `C − P = 4.2763 − 2.7876 = 1.4887`, matching `S₀ − K·e^(−rT) = 100 − 98.5112 = 1.4888` ✓.

**B10. American parity band.** `S₀ = 30`, `K = 30`, `T = 0.5`, `r = 10%`, American options, no dividends. Give the allowed range for `C − P`, and flag a quote of `C − P = 2` as arbitrage or not.

Band: `S₀ − K ≤ C − P ≤ S₀ − K·e^(−rT)`. Lower `= 30 − 30 = 0`. Upper `= 30 − 30·e^(−0.05) = 30 − 30·0.951229 = 30 − 28.5369 = 1.4631`. So `0 ≤ C − P ≤ 1.4631`. A quote of `C − P = 2` lies *above* the upper bound, so it violates the no-arbitrage band — the call is too rich relative to the put, and a reversal-type trade would profit.

---

## Section C — Interview-Style (with model answers)

**C1. "Explain put-call parity to me as if I'd never seen it."**

Model answer: Take a call plus enough cash to grow to the strike by expiry, and separately take a put plus one share. Walk to expiry in any world: both packages are worth `max(S_T, K)` — the higher of the final stock price or the strike. Because they pay identically in every state and there are no cash flows in between, they must cost the same today. That equality is `C + K·e^(−rT) = P + S₀`. No volatility, no forecasts — just the logic that identical payoffs command identical prices.

**C2. "How would you trade a parity violation, concretely?"**

Model answer: Compare the two sides. If `C + K·e^(−rT) > P + S₀`, the call/bond side is rich — I run a *conversion*: buy the share, buy the put, write the call, and borrow the PV of the strike. That nets positive cash today and expires to zero in every state, so the up-front cash is locked-in profit. If the put/stock side is rich instead, I do the mirror — a *reversal*: short the share, sell the put, buy the call, and lend. Either way I sell the expensive portfolio and buy the cheap one, and the terminal values cancel.

**C3. "Why doesn't parity depend on volatility, and why is that useful?"**

Model answer: The derivation only matches terminal payoffs and invokes no-arbitrage; it never asks how volatile the stock is or which way it drifts. That independence makes parity a universal sanity check. If I price a put with Black-Scholes and it doesn't satisfy `C − P = S₀ − K·e^(−rT)`, I know I have a bug regardless of what vol I used. It also forces the call and put at one strike to share a single implied volatility — if the market shows two different IVs there, something (borrow, dividends, stale quotes) is off, and that's tradeable.

**C4. "Give me the fastest sanity check that a put price is right, given the call."**

Model answer: Confirm `C − P = S₀ − K·e^(−rT)`, dividend-adjusted if needed (`S₀ − D` for discrete, `S₀·e^(−qT)` for a yield). It's one subtraction and one discount factor. If it holds, the pair is internally consistent; if it fails, at least one of the two prices is wrong. I don't need to re-run a full model — parity isolates the relationship between the two options.

**C5. "Someone tells you American put-call parity is C + K·e^(−rT) = P + S₀. React."**

Model answer: That equality is a *European* result. American options carry early-exercise rights that break the payoff-matching argument — the portfolios can be disturbed before expiry. For an American non-dividend stock the correct statement is a band, `S₀ − K ≤ C − P ≤ S₀ − K·e^(−rT)`, not an equation. Treating it as an equality is a common and costly error, especially once dividends make early exercise of the put or call attractive.

**C6. "Build me a synthetic long forward on the whiteboard and prove the payoff."**

Model answer: Long call, short put, same strike `K` and expiry. In the up state (`S_T > K`) the call pays `S_T − K` and the short put is worthless — net `S_T − K`. In the down state (`S_T ≤ K`) the call is worthless and the short put costs me `K − S_T` — net `S_T − K`. Same expression both ways, a straight line through `K` with no kink, which is exactly a forward struck at `K`. Its cost is `C − P = S₀ − K·e^(−rT) = (F₀ − K)·e^(−rT)`, the present value of the forward's moneyness.

---

## Section D — Multiple Choice (with reasoning)

**D1. Put-call parity for a European option on a non-dividend stock is:**
(a) `C + S₀ = P + K·e^(−rT)`; (b) `C + K·e^(−rT) = P + S₀`; (c) `C + K = P + S₀`; (d) `C − K·e^(−rT) = P + S₀`.

**Answer: (b).** The fiduciary call (call + PV of strike) equals the protective put (put + stock). (c) forgets to discount the strike — a future payment must be `K·e^(−rT)`. (a) and (d) swap or mis-sign the legs.

**D2. Put-call parity primarily determines:**
(a) the level of the call; (b) the level of the put; (c) the difference `C − P`; (d) the volatility.

**Answer: (c).** Parity fixes `C − P = S₀ − K·e^(−rT)` but says nothing about absolute levels, which need a model and a volatility input. That is exactly why an arbitrage can be spotted without pricing either option.

**D3. Long call plus short put at the same strike and expiry is equivalent to:**
(a) a long straddle; (b) a synthetic long forward; (c) a covered call; (d) a synthetic bond.

**Answer: (b).** The combined payoff is `S_T − K` in every state — a linear, kink-free forward payoff. A straddle is long call + long put (a volatility bet); a covered call is long stock + short call; a synthetic bond is a different combination entirely.

**D4. When the strike equals the forward price (K = F₀):**
(a) the call is worthless; (b) `C = P`; (c) `P > C` always; (d) parity fails.

**Answer: (b).** From `C − P = (F₀ − K)·e^(−rT)`, setting `K = F₀` gives `C − P = 0`. This at-the-money-forward equality is standard desk knowledge; parity holds regardless.

**D5. For a stock paying a dividend with present value D, parity becomes:**
(a) `C + K·e^(−rT) = P + S₀ + D`; (b) `C + K·e^(−rT) = P + S₀ − D`; (c) unchanged; (d) `C + D = P + S₀`.

**Answer: (b).** The stockholder collects `D` the call holder does not, so the stock leg is reduced by `D`. Equivalently `C + D + K·e^(−rT) = P + S₀`. (a) has the wrong sign; (c) ignores the dividend and is the classic phantom-arbitrage error.

**D6. For American options on a non-dividend stock, the parity relationship is:**
(a) an equality identical to the European case; (b) `S₀ − K ≤ C − P ≤ S₀ − K·e^(−rT)`; (c) `C − P = S₀`; (d) undefined.

**Answer: (b).** Early exercise turns the equality into a no-arbitrage band. The lower bound uses the undiscounted strike, the upper bound the discounted strike. (a) is the trap answer.

**D7. Parity implies which relationship between the Greeks of a same-strike call and put?**
(a) `Δ_C = Δ_P`; (b) `Γ_C = −Γ_P`; (c) `Vega_C = Vega_P`; (d) `Θ_C = Θ_P`.

**Answer: (c).** Differentiating the deterministic identity gives `Δ_C − Δ_P = 1` (not equal), `Γ_C = Γ_P` (not opposite), and `Vega_C = Vega_P`. Only (c) is correct; theta differs by the deterministic financing/discount terms.

**D8. The left side of parity, C + K·e^(−rT), is 106.5 and the right side, P + S₀, is 105.0. The correct arbitrage is:**
(a) buy call, buy bond, sell put, sell stock; (b) write call, buy put, buy stock, borrow PV(K); (c) do nothing, prices are fair; (d) buy two calls.

**Answer: (b).** The left (call/bond) side is rich, so sell it and buy the cheap right side — a conversion: write the call, buy the put, buy the share, and borrow the PV of the strike. This banks the `1.5` gap today and expires to zero. (a) buys the expensive side and sells the cheap side, losing money.

---

*Self-check performed: every Section B computation was recomputed with the stated discount factors (`e^(−0.015)=0.985112`, `e^(−0.04)=0.960789`, `e^(−0.025)=0.975310`, `e^(−0.01)=0.990050`, `e^(−0.05)=0.951229`) and cross-reconciled via `C − P = (F₀ − K)·e^(−rT)`. B1/B2 verified as a zero-netting conversion; B3/B4 checked for dividend consistency; B5 back-substituted; B9 confirmed the binomial model satisfies parity; B10 checked against the American band. All MCQ distractors were verified as genuinely incorrect.*
