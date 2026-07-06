# Q&A — Market Risk

*Practice bank for Chapter 03 (Market Risk). Every question is followed by a full answer. Attempt each before reading the solution. Numerical answers are reconciled at least two independent ways. z-values used: 1.645 (95%), 1.960 (97.5%), 2.326 (99%).*

---

## Section A — Concept Check

**A1. In one sentence, what is market risk, and what single word separates it from credit risk?**
Market risk is the risk that the mark-to-market value of positions falls because **market prices move** — rates, equities, FX, commodities. The separating word is *price*: market risk is about the price of what you *hold* moving, whereas credit risk is about a *counterparty* failing to pay. No default is needed for a market loss; a yield tick or an FX move is enough.

**A2. State the two-step chain at the heart of market-risk measurement.**
Loss ≈ **(how much the factor moves) × (how sensitive my position is to that factor)**, i.e. $\Delta P \approx \text{Sensitivity} \times \Delta(\text{Factor})$. The factor move is a property of the *market* (uncontrollable, estimated from history or implied vol); the sensitivity is a property of *your position* (known, computable, controllable by trading and hedging). You cannot stop rates moving, but you choose how much you lose when they do.

**A3. Name the four classic market-risk factor classes plus the two common extensions, and the primary sensitivity of each.**
Interest rate (DV01/duration), equity (delta/beta), foreign exchange (FX delta = net currency position), commodity (delta per commodity, plus basis). The two extensions carried within market risk in the trading book are credit spread (CS01/spread DV01) and volatility (vega).

**A4. Why measure market risk separately and more frequently than credit risk?**
Speed and two-sidedness. Credit losses crystallise over months; market losses crystallise in seconds — a trading book can lose a large fraction of capital between lunch and the close, so you cannot manage monthly what moves by the second. A loan pays par or less (one-sided), but a traded position can gain *or* lose and can be short as well as long, so the measurement must capture both directions and the netting between them.

**A5. Distinguish the trading book from the banking book, and say what the boundary decides.**
The trading book holds positions with *trading intent* (short-term profit / market-making); they are marked to market daily and attract market-risk capital. The banking book holds positions for yield or to maturity (loans, HTM bonds, deposits); they are accrual-accounted and carry credit risk plus IRRBB. The boundary is decided by *intent*, not by instrument type — the **same** bond can sit in either book — and it drives accounting (MTM vs accrual), capital treatment, and the risk lens (VaR vs earnings/economic-value sensitivity).

**A6. Define DV01 and give its relationship to modified duration.**
DV01 (PV01) is the money change in a position's value for a **1 basis point (0.01%)** parallel yield move: $\text{DV01} = D_{mod} \times P \times 0.0001$, where $P$ is the market (dirty) value. Duration measures the *percentage* price change per unit yield; DV01 converts that into *money per basis point*, which is what a desk actually hedges.

**A7. What is convexity and which way does it work for a plain bond holder?**
Convexity is the second-order (curvature) rate sensitivity: $\Delta P/P \approx -D_{mod}\,\Delta y + \tfrac12 C(\Delta y)^2$. For a plain bond $C > 0$, so duration *overstates* the loss on a rate rise and *understates* the gain on a rate fall — the correction helps the holder both ways, which is why long-convexity positions are prized.

**A8. Define VaR precisely, and state clearly what it is *not*.**
A 1-day 99% VaR of ₹5 crore means: on 99% of days the loss should not exceed ₹5 crore, and roughly 1 day in 100 it will exceed it. VaR is a *percentile* of the P&L distribution — a threshold. It is **not** the maximum or worst-case loss, and it says nothing about how bad the breach is once exceeded; that is Expected Shortfall's job.

**A9. What is Expected Shortfall and why did regulators move to it?**
Expected Shortfall (ES / CVaR) is the *average* loss given that VaR is breached — the mean of the tail beyond VaR. It is **coherent** (it respects diversification / sub-additivity, which VaR can violate for non-linear books) and it describes tail *depth*, not just a threshold. Basel's FRTB replaced VaR with **97.5% ES** for exactly these reasons.

**A10. State the square-root-of-time rule and its key assumption.**
$\text{VaR}_h = \text{VaR}_1 \times \sqrt{h}$: to scale a 1-day VaR to an $h$-day horizon, multiply by $\sqrt{h}$. It is valid only when returns are **i.i.d.** (independent, identically distributed, zero autocorrelation). Volatility clustering and mean-reversion break it, so it is an approximation, not a law.

**A11. Name the three VaR methods in one line each.**
Parametric (variance-covariance) — assumes normal factor returns, fast, poor for options. Historical simulation — replay actual past factor moves through today's book, captures fat tails, but bounded by the sampled history. Monte Carlo — simulate scenarios from an assumed process and full-revalue, most flexible for non-linearity, computationally heavy.

**A12. Why is "delta-hedged" not the same as "risk-free"?**
A delta hedge removes first-order price risk *instantaneously only*. Gamma (delta drifts as the price moves), vega (volatility risk), theta (time decay), and basis risk all remain, so the book must be continuously re-hedged. A static delta hedge is safe for one instant and one small move, not over time or over a large move.

---

## Section B — Numerical / Applied

### B1 — Bond DV01, rate shock, and a convexity check

**Setup.** A desk holds ₹100 crore face of a bond priced at par (₹100), modified duration 7.0, convexity 60. Rates rise 40 bp.

**Step 1 — DV01.** Market value $P$ = ₹100 crore.
$$\text{DV01} = D_{mod} \times P \times 0.0001 = 7.0 \times 100{,}00{,}00{,}000 \times 0.0001 = ₹7{,}00{,}000 \text{ per bp.}$$

**Step 2 — Duration-only loss for 40 bp.**
$$\text{Loss} \approx 40 \times 7{,}00{,}000 = ₹2{,}80{,}00{,}000 = ₹2.80\text{ crore.}$$
Cross-check via percentages: $-D_{mod}\,\Delta y = -7.0 \times 0.0040 = -2.80\%$ of ₹100 crore = ₹2.80 crore. **Reconciles.**

**Step 3 — Convexity correction.**
$$\tfrac12 C(\Delta y)^2 = 0.5 \times 60 \times (0.0040)^2 = 0.5 \times 60 \times 0.000016 = 0.00048 = 0.048\%.$$
Convexity is positive so it *reduces* the loss: net ≈ $-2.80\% + 0.048\% = -2.752\%$ → **₹2.752 crore**.

**Interpretation.** Linear says ₹2.80 crore; convexity trims it to ₹2.752 crore. For a 40 bp *fall*, the gain would be $2.80\% + 0.048\% = 2.848\%$ — convexity helps both ways.

### B2 — Single-position parametric VaR (95% and 99%)

**Setup.** An equity position worth ₹40 crore has a daily return volatility of 1.8%. Horizon 1 day.

**Step 1 — Daily P&L volatility in money.**
$$\sigma_{P\&L} = 40\text{ cr} \times 1.8\% = ₹0.72\text{ crore.}$$

**Step 2 — VaR at each confidence.**
$$\text{VaR}_{95} = 1.645 \times 0.72 = ₹1.184\text{ crore.}$$
$$\text{VaR}_{99} = 2.326 \times 0.72 = ₹1.675\text{ crore.}$$

**Interpretation & check.** Ratio $2.326/1.645 = 1.414$, and $1.675/1.184 = 1.415$. **Reconciles** — the 99% number is larger simply because the threshold sits further into the tail, not because the day is "worse."

### B3 — Two-asset portfolio VaR with a diversification check

**Setup.** Position A: equity, ₹50 crore, daily vol 2.0%. Position B: bond, ₹50 crore, daily vol 0.8%. Correlation ρ = 0.30. Confidence 99%, horizon 1 day.

**Step 1 — Standalone P&L vols.**
$$\sigma_A = 50 \times 2.0\% = ₹1.00\text{ cr}, \qquad \sigma_B = 50 \times 0.8\% = ₹0.40\text{ cr.}$$

**Step 2 — Portfolio P&L vol.**
$$\sigma_P = \sqrt{\sigma_A^2 + \sigma_B^2 + 2\rho\sigma_A\sigma_B} = \sqrt{1.00^2 + 0.40^2 + 2(0.30)(1.00)(0.40)}$$
$$= \sqrt{1.00 + 0.16 + 0.24} = \sqrt{1.40} = ₹1.1832\text{ crore.}$$

**Step 3 — 1-day 99% VaR.**
$$\text{VaR} = 2.326 \times 1.1832 = ₹2.752\text{ crore.}$$

**Step 4 — Diversification benefit.** Standalone VaRs: $\text{VaR}_A = 2.326 \times 1.00 = 2.326$; $\text{VaR}_B = 2.326 \times 0.40 = 0.930$. Sum = ₹3.256 crore > ₹2.752 crore.
$$\text{Benefit} = 3.256 - 2.752 = ₹0.504\text{ crore.}$$
Because ρ = 0.30 < 1, combined VaR is below the sum — sub-additivity as expected. **Reconciles.**

**Step 5 — Scale to 10 days.**
$$\text{VaR}_{10} = 2.752 \times \sqrt{10} = 2.752 \times 3.162 = ₹8.70\text{ crore.}$$

### B4 — Expected Shortfall from VaR (normal case)

**Setup.** Same portfolio as B3: $\sigma_P = ₹1.1832$ crore, normal P&L, confidence 99%.

**Formula.** For a normal loss distribution, $\text{ES}_c = \sigma_P \times \dfrac{\phi(z_c)}{1-c}$, where $\phi$ is the standard-normal density. At 99%, $z = 2.326$, $\phi(2.326) = \dfrac{1}{\sqrt{2\pi}}e^{-2.326^2/2} = 0.3989 \times e^{-2.705} = 0.3989 \times 0.0669 = 0.02669$.

**Compute.**
$$\text{ES}_{99} = 1.1832 \times \frac{0.02669}{0.01} = 1.1832 \times 2.669 = ₹3.158\text{ crore.}$$

**Interpretation & check.** ES (₹3.158 cr) > VaR (₹2.752 cr) — always true, since ES averages the tail *beyond* the VaR threshold. The ES multiplier 2.669 exceeds the VaR multiplier 2.326, confirming ES sits deeper in the tail. **Reconciles.**

### B5 — Expected loss vs VaR: don't confuse them

**Setup.** A ₹200 crore bond position has a daily P&L volatility of ₹1.5 crore and an *expected* daily P&L of zero (a fair, unbiased mark). Find the 99% VaR and contrast it with "expected loss."

**Solution.**
$$\text{VaR}_{99} = 2.326 \times 1.5 = ₹3.489\text{ crore.}$$
Expected daily P&L is **zero**, so the *expected* loss is nil — on an average day you neither make nor lose. VaR is a *tail* quantity: it answers "how bad is a bad (1-in-100) day," a completely different question from "what do I expect on a typical day." Reporting the mean when asked for VaR (or vice-versa) is a classic error: the mean describes the centre, VaR describes the tail.

### B6 — Beta hedge with index futures

**Setup.** A portfolio worth ₹20 crore has beta 1.25 to the Nifty. Nifty = 24,000; lot = 50 units, so one contract notional = 24,000 × 50 = ₹12,00,000. Hedge to beta 0.

**Step 1 — Beta-adjusted exposure.** $1.25 \times 20 = ₹25$ crore.

**Step 2 — Contracts to short.**
$$N = \frac{\beta \times V}{\text{Futures notional}} = \frac{25{,}00{,}00{,}000}{12{,}00{,}000} = 208.3 \Rightarrow \textbf{short 208 contracts.}$$

**Step 3 — Check with a 2% market drop.** Nifty 24,000 → 23,520.
- Portfolio loss ≈ $1.25 \times (-2\%) \times 20 = -₹0.50$ crore.
- Futures gain (short) = $208 \times 50 \times (24{,}000 - 23{,}520) = 208 \times 50 \times 480 = +₹49{,}92{,}000 \approx +₹0.499$ crore.
- Net ≈ **−₹0.001 crore**, essentially flat; the residual is rounding 208.3 → 208. **Reconciles.**

**Target-beta variant.** To move to β_T instead of 0: $N = \dfrac{(\beta_T - \beta_P)\,V}{\text{Futures notional}}$. Going from 1.25 to 0.50: $N = (0.50 - 1.25)\times 20/12{,}00{,}000 \times 10^7 = -125$ → short 125 contracts.

### B7 — FX VaR

**Setup.** A firm is long USD 10 million against INR. USD/INR = 83.00. The daily volatility of USD/INR returns is 0.5%. Find the 1-day 95% VaR in INR.

**Step 1 — INR value of the position.** $10{,}000{,}000 \times 83.00 = ₹83$ crore.

**Step 2 — Daily P&L vol.** $83 \times 0.5\% = ₹0.415$ crore.

**Step 3 — 95% VaR.** $1.645 \times 0.415 = ₹0.683$ crore.

**Interpretation.** A 1% move in USD/INR changes the position by 1% of ₹83 crore = ₹0.83 crore, so FX delta here is 1:1 with the INR value — the sensitivity is simply the net currency position measured in the base currency.

---

## Section C — Interview-Style (Model Answers)

**C1. "A trader tells you his book is fine because the notional is small. What's your response?"**
Notional tells me almost nothing about risk — *sensitivity* does. A ₹500 crore swap can carry less risk than a ₹50 crore bond, because risk is DV01 and net delta, not the size of the ticket. Derivatives let a desk take huge notional exposure for tiny cash outlay, so I'd ask for the DV01, the net delta, the vega, and the VaR — the sensitivities and their statistical roll-up — before I'd form any view on whether the book is "fine."

**C2. "Walk me from a single position to a firm-wide VaR number."**
Every position, however complex, is a function of a handful of risk factors. First I *decompose* it into factor exposures — a bond onto the yield curve, an option onto spot/vol/rate. Second I translate each exposure into a *sensitivity*: DV01, delta, beta, vega, plus gamma/convexity for curvature. Third I bring in the factors' *statistics* — volatilities and correlations. Because the P&L is then a linear combination of factor moves, its variance follows from the sensitivities and the covariance matrix; VaR is simply a percentile of that distribution. Historical and Monte Carlo VaR reprice the *same* positions under, respectively, replayed real moves and simulated scenarios. So the spine is: factor → sensitivity → loss distribution → percentile.

**C3. "Why did the industry move from VaR to Expected Shortfall?"**
Two reasons. First, VaR only marks a *threshold* — it is silent on how bad the loss is once breached, so two books with identical VaR can have wildly different tail depth. ES averages the tail beyond VaR and captures that. Second, VaR is **not sub-additive** for general (non-linear, optioned) portfolios: combined VaR can exceed the sum of parts, which perversely penalises diversification and can be gamed. ES is coherent — it always respects diversification. Basel's FRTB codified the switch at 97.5% ES, added liquidity-horizon scaling, and hardened the trading/banking book boundary.

**C4. "Your VaR model passed backtesting all year, then blew through the limit five days running in a crisis. What happened?"**
Almost certainly the model was calibrated on calm-period data, and in a crisis two things changed at once. Volatilities jumped — big moves cluster, so yesterday's vol underestimated today's. And correlations converged toward 1: in a risk-off episode, diversification evaporates exactly when you need it, so the offsetting positions the VaR relied on all moved the same way. VaR by construction describes *normal* days; it understates the tail. That's precisely why we hold **Stressed VaR** (calibrated to a stress window), run **stress tests and scenario analysis**, and report **ES** — the tools designed for the regime VaR misses.

**C5. "Explain why a delta-hedged options book can still lose money fast."**
Delta hedging removes first-order price risk for one instant and one small move only. What remains is gamma — as the underlying moves, delta itself changes, so a book that was neutral becomes directional between re-hedges. If the desk is *short* gamma (has sold options), every large move hurts and re-hedging locks in losses — "picking up pennies in front of a steamroller." On top of gamma sit vega (a vol spike revalues the options) and theta (time decay), plus basis risk if the hedge instrument isn't the exact underlying. So "delta-hedged" is a snapshot, not a state of safety.

**C6. "How is the market-risk loss chain related to the credit-risk expected-loss formula?"**
They're structurally the same idea: turn a stochastic driver into a money loss. Market risk: Loss ≈ sensitivity × factor move. Credit risk: Expected Loss = PD × LGD × EAD — probability of default times loss-given-default times exposure-at-default. Both convert an uncertain event into an expected or potential loss. The two disciplines actually overlap on traded corporate bonds via credit-spread risk (CS01), which is a *market* sensitivity to a *credit* factor. The difference is speed and accounting: market losses are marked to market daily; credit losses accrue over months.

---

## Section D — MCQs (with reasoning)

**D1. A 1-day 99% VaR of ₹4 crore means:**
A) The book can never lose more than ₹4 crore.
B) The average loss is ₹4 crore.
C) On about 1 day in 100 the loss is expected to exceed ₹4 crore.
D) The loss is exactly ₹4 crore on 1% of days.

**Answer: C.** VaR is a percentile/threshold: losses stay within ₹4 crore on ~99% of days and breach it on ~1%. A is wrong (VaR is not a maximum). B confuses VaR with the mean. D is wrong — VaR bounds the tail probability, it does not fix the loss at exactly ₹4 crore.

**D2. Which sensitivity best captures the money impact of a 1 bp yield move on a bond?**
A) Beta  B) DV01  C) Vega  D) Delta

**Answer: B.** DV01 (= $D_{mod} \times P \times 0.0001$) is the money change per 1 bp move — precisely a bond desk's rate sensitivity. Beta is equity-to-index, vega is volatility sensitivity, delta is price sensitivity for an option/equity.

**D3. In the two-asset variance formula, lowering the correlation ρ (all else equal) will:**
A) Raise portfolio VaR  B) Lower portfolio VaR  C) Leave it unchanged  D) Make it negative

**Answer: B.** Portfolio vol is $\sqrt{\sigma_1^2 + \sigma_2^2 + 2\rho\sigma_1\sigma_2}$; the cross term falls as ρ falls, shrinking $\sigma_P$ and hence VaR. Lower correlation = more diversification = less risk. VaR can never be negative (D), and it is not invariant to ρ (C).

**D4. Expected Shortfall is preferred over VaR primarily because it:**
A) Is always smaller than VaR.
B) Ignores the tail.
C) Is coherent and measures the depth of the tail beyond VaR.
D) Requires no data.

**Answer: C.** ES is sub-additive (coherent) and averages losses *beyond* the VaR threshold, capturing tail severity. A is false — ES ≥ VaR. B is the opposite of the truth. D is false — ES needs at least as much data as VaR.

**D5. Which of these determines whether a bond sits in the trading or banking book?**
A) Its credit rating  B) Its maturity  C) The holder's intent  D) Its coupon

**Answer: C.** The boundary is about *intent* — held to profit from short-term price moves (trading, marked to market) vs held for yield/to maturity (banking, accrual). The **same** bond can sit in either book; rating, maturity and coupon are irrelevant to the classification.

**D6. Under the square-root-of-time rule, the 16-day VaR equals the 1-day VaR multiplied by:**
A) 16  B) 8  C) 4  D) 2

**Answer: C.** $\text{VaR}_{16} = \text{VaR}_1 \times \sqrt{16} = \text{VaR}_1 \times 4$. The rule scales with $\sqrt{h}$, not $h$, and holds under i.i.d. returns.

**D7. A desk that has *sold* options (is short gamma) will find that large underlying moves:**
A) Always help it.
B) Hurt it, and re-hedging tends to lock in losses.
C) Have no effect once delta-hedged.
D) Reduce its vega to zero.

**Answer: B.** Short gamma means delta moves *against* the desk as the underlying moves, so re-hedging means buying high and selling low — losses accumulate in big moves ("pennies in front of a steamroller"). Delta-hedging does not remove gamma (C is false), and being short options means short vega, not zero vega (D is false).

**D8. Parametric (variance-covariance) VaR is *least* reliable for:**
A) A cash bond portfolio.
B) A linear FX book.
C) An options portfolio with significant gamma.
D) A single equity holding.

**Answer: C.** Parametric VaR assumes normal factor returns and linear payoffs; it ignores fat tails and the curvature (gamma) of options, so it mismeasures optioned books. Linear positions (A, B, D) are where the normal/linear assumption is most defensible.

---

*Self-check: B1 (₹2.80 → 2.752 cr), B2 (z-ratio 1.414 ≈ 1.415), B3 (√1.40 = 1.1832; benefit ₹0.504 cr), B4 (ES multiplier 2.669 > VaR 2.326), B6 (−₹0.50 cr offset by +₹0.499 cr) all reconcile.*
