# Advanced Scenario Q&A + Greeks/Formula Cheat-Sheet

*India F&O, 2026. A rapid-fire desk reference for the experienced options trader/derivatives-research analyst. All rules/figures date-stamped — verify current STT (~0.10% on options sell premium; ~0.125% on ITM exercise intrinsic), SEBI lot sizes, expiry calendar, and SPAN parameters on NSE/your broker before trading.*

## The idea

This chapter is the desk-side quick reference: the scenario questions a senior trader or an interview panel throws at you, answered the way a practitioner answers — with the reasoning, the number, and the India-specific caveat. It also consolidates the Greeks and pricing relationships you should be able to recall and apply under pressure, in ₹ terms on Nifty/Bank Nifty. It earns its keep in two moments: the interview/viva where you must demonstrate you *understand* the machinery, and the live trade where you need the relationship (say, how much vega you'll lose if VIX drops 2 points) in your head, not in a spreadsheet.

The organising principle: options P&L is driven by the Greeks, and the Greeks are just partial derivatives of the option price with respect to spot, time, and vol. If you can decompose any trade into its net delta/gamma/theta/vega and reason about how each moves, you can answer almost any scenario question. The rest is India-specific plumbing — STT, SPAN, weekly expiries, lot sizes.

## The mechanics — the Greeks/formula cheat-sheet

**Black-Scholes intuition (you rarely compute it by hand, but you must know what drives it).** An option price = intrinsic value + time value. Time value is a function of volatility, time to expiry, and rates. The Greeks are its sensitivities:

| Greek | Definition (∂price/∂…) | Sign for long call / long put | Rule-of-thumb behaviour |
|---|---|---|---|
| **Delta (Δ)** | ∂V/∂S | + / − | ATM ≈ ±0.5; deep ITM → ±1; deep OTM → 0. Also ≈ risk-neutral P(expire ITM) |
| **Gamma (Γ)** | ∂Δ/∂S | + / + | Peaks ATM, explodes near expiry. Long options long gamma |
| **Theta (Θ)** | ∂V/∂t | − / − | Time decay; accelerates near expiry for ATM; sellers positive theta |
| **Vega (ν)** | ∂V/∂σ | + / + | Peaks ATM, larger for longer-dated. Buyers long vega |
| **Rho (ρ)** | ∂V/∂r | + / − | Small for weeklies; matters for long-dated |

**Key relationships to recall:**

- **Put-call parity:** C − P = S − K·e^(−rT) (forward-adjusted). On Indian index options (European, cash-settled), this holds up to costs/dividends. It's how you spot synthetic mispricings: a synthetic long (long call + short put same strike) ≈ long forward.
- **ATM straddle price ≈ 0.8 × S × σ × √T** (rough) — lets you back out the market's expected move. If a Nifty weekly ATM straddle costs ₹250 with spot 24,000, the market is pricing roughly a ±1% move into expiry.
- **Delta of a spread** = sum of leg deltas (short leg negative). **Vega/gamma/theta of a book** = weighted sum across all legs × lots × lot size.
- **Gamma-theta trade-off:** long gamma ⟺ negative theta, and vice-versa. You cannot be long gamma and collect theta; the market prices them as opposites. Sellers earn theta and pay it back via gamma on big moves.
- **Vega-theta for calendars:** a calendar is long vega (net) and positive theta — the one common structure that gets both, because the short front-month decays faster than the long back-month.
- **Charm (delta decay):** delta drifts as time passes even with spot flat — matters for hedging into expiry.
- **Vanna:** ∂delta/∂vol — why skew changes reshape your delta when IV moves. Relevant on event days.

**India-specific plumbing:**

| Item | 2026 status (verify) |
|---|---|
| Index options settlement | Cash-settled, European style |
| Nifty lot / strike step | 75 / 50 |
| Bank Nifty lot / strike step | 30 / 100 |
| Weekly expiries | Rationalised by SEBI 2024–25 — limited weeklies per exchange; **verify calendar** |
| STT on options (sell) | ~0.10% of premium (verify) |
| STT on ITM exercise | ~0.125% of intrinsic settlement value (verify) — square off ITM to avoid |
| Margin | SPAN + Exposure, portfolio-based, dynamic with VIX |
| India VIX | 30-day model-free implied vol on Nifty; the vol anchor |

## Worked trade — Greeks arithmetic you should do in your head

**Nifty 24,000, weekly ATM 24,000 CE priced ₹150, delta 0.52, gamma 0.0012, theta −₹8/day (per share), vega ₹9 (per vol pt), lot 75.**

- **Per lot:** premium ₹150 × 75 = ₹11,250. Delta 0.52 × 75 = **39 "share-deltas"** → a 100-pt Nifty move ≈ +₹3,900 on this call (before gamma).
- **Gamma add:** on a 100-pt move, delta rises by 0.0012 × 100 = 0.12 → new delta ~0.64; the *average* delta over the move is ~0.58, so actual gain ≈ 0.58 × 100 × 75 ≈ **+₹4,350** — gamma makes the up-move earn more than linear.
- **Theta:** holding overnight costs −₹8 × 75 = **−₹600/day.**
- **Vega:** if VIX drops 1 point, lose ₹9 × 75 = **−₹675**; if it rises 2 points, gain **+₹1,350.**

This is the whole game in one option: you're long delta, long gamma (up-move convexity), paying theta (₹600/day rent), long vega (₹675/vol-pt). Every scenario question is just asking which of these dominates.

## Management — the scenario Q&A (rapid-fire)

**Q1. Nifty gaps up 2% overnight and you're short a straddle. What happened to your Greeks and P&L?**
Short gamma means your delta swung sharply negative (you're now effectively short the market after a rally) — you lose on the up-move and lose *faster* as it extends. If VIX also spiked, your short vega compounds the loss. SPAN margin likely rose. Action: hedge delta with futures immediately, then decide whether to roll the tested short strike. This is the short-gamma-into-a-gap failure mode.

**Q2. You expect Nifty to stay flat for two weeks. Two ways to earn, and their risks?**
(a) Short strangle/iron condor — positive theta, negative vega/gamma; risk is a breakout or VIX spike. (b) Calendar spread — positive theta *and* long vega; risk is a large move away from the strike. If you fear a vol spike, prefer the calendar (long vega cushions). If you fear only a breakout, the condor's defined risk is cleaner. Never naked short if the tail isn't sized.

**Q3. India VIX is at 11 (multi-year low). How does that change your bias?**
Cheap IV favours *buyers* (spreads, calendars long the back month, long vol into events) and warns *sellers* that premium is thin and the downside skew is under-priced. But cheap IV can stay cheap and bleed a buyer via theta — low VIX alone isn't a buy signal; you need a catalyst. Also: low VIX often precedes vol expansion, so short-vol books should be *smaller* here, not larger.

**Q4. Explain why an iron condor needs far less margin than a short strangle.**
SPAN is portfolio-based and worst-case. The condor's long wings cap the loss, so the worst-case scenario in SPAN's grid is bounded (width − credit); margin is a fraction. The naked strangle's worst case is unbounded, anchoring a huge margin, which also *rises* as VIX rises. Same directional/theta view, far better capital efficiency and a defined tail.

**Q5. You sold a Nifty weekly put spread; spot is now near your short strike on Wednesday. Adjust?**
The short put is near ATM → short gamma is biting, delta turning long against you. Options: (a) roll the whole put spread down and out for a credit if thesis holds; (b) roll the *untested* call side down to collect more credit and recentre; (c) take the defined loss. Do **not** keep rolling the tested put side further down into a falling market — that's the over-adjustment trap. Square off before expiry to avoid ITM exercise STT.

**Q6. What's the "pin" and can you trade it?**
Near expiry, dealer delta-hedging concentrates spot toward the strike with the most open interest ("max pain" gravity). It's real *only close to expiry* and is soft. You can lean on it (e.g., sell an ATM iron fly expecting a pin) but size for the day it breaks — pins fail on trend/gap days.

**Q7. Your book is theta +₹9,000/day. What are you implicitly short?**
Gamma and vega. Positive theta is financed by negative gamma (you lose on big moves) and negative vega (you lose on vol spikes). The ₹9,000/day is rent the market pays you for taking those risks; the bill comes on a gap + VIX-spike day. Manage the aggregate vega/gamma, not just theta.

**Q8. Why do index puts trade at higher IV than equidistant calls?**
Equity index skew: crash risk is bid because indices gap down harder than up, and institutions buy downside protection. The put-skew is the market's honest pricing of the fat left tail — a standing warning to short-vol sellers that the downside is where the pain concentrates.

**Q9. Convert a long call into a spread mid-trade — why and how?**
If the underlying has moved your way and IV is now high, sell a higher strike against your long call to (a) lock in gains, (b) reduce theta/vega exposure, (c) recover premium. You cap upside but de-risk. It's a way to "take money off the table" without fully exiting — common on a winning directional option that's run into rich IV.

**Q10. A calendar spread — when does it lose?**
When the underlying makes a large move *away* from the strike (both options move toward all-intrinsic/all-cheap, collapsing the time-value differential) or when back-month IV *falls* (you're long vega). It wins on a still underlying with firming back-month IV. It's a vol + pin bet, not a directional one.

**Q11. Estimate the market's expected weekly move on Nifty.**
Use the ATM straddle: expected move ≈ ATM straddle price. If 24,000 straddle = ₹250, market prices ~±₹250 (~±1%) by expiry (one standard-deviation-ish). Compare to your own forecast to decide buy/sell vol.

**Q12. VIX spikes but your book is vega-neutral — are you safe?**
Safer on the *vega* axis, but a VIX spike usually accompanies a spot move, so your gamma exposure still matters. Vega-neutral protects the mark against pure vol re-pricing; it doesn't protect against the directional move that often triggers the vol spike. Check net gamma too.

## Risk & sizing — the numbers to keep in your head

- **Sizing:** lots = (capital × 1%) / max-loss-per-lot. Never size off available margin.
- **Vega cap:** net book vega such that a +5 VIX-point shock costs ≤ ~2% of capital.
- **Gamma cap:** net gamma such that a 2% overnight gap costs ≤ ~3% of capital after first-morning hedge.
- **Margin utilisation:** ≤ 60% normal, ≤ 40% when VIX elevated (dry powder for SPAN hikes).
- **Cost drag:** a 4-leg round trip = up to 8 executions; STT on sells + txn + 18% GST can eat a third of a thin credit — size per lot, don't over-leg.
- **The tail number:** always compute worst realistic overnight gap (Nifty −4%, VIX +8) at your size *before* the trade. If it exceeds your pain threshold, cut size now.

**Honest risk statement:** SEBI studies show most individual F&O traders lose money, concentrated among naked-option sellers and undersized-buffer books. The Greeks don't lie — positive theta is negative gamma and vega — and the tail arrives most years. Respect the skew, size for the gap, and keep dry powder.

## Pitfalls & interview-ready summary

**Pitfalls:**
- **Reciting Greek definitions without the ₹ arithmetic** — an interviewer wants "₹675 per vol-point on this lot," not "vega is sensitivity to volatility."
- **Forgetting the gamma-theta / vega-theta trade-offs** — every income strategy is short something.
- **Treating low VIX as a buy signal** — cheap vol can bleed you via theta without a catalyst.
- **Ignoring the ITM-exercise STT** — square off ITM legs before expiry.
- **Quoting old lot sizes / expiry rules** — SEBI changed both in 2024–25; verify 2026 figures.
- **Managing single-trade Greeks, not book Greeks** — aggregate exposure is what a vol spike hits.

**Interview-ready summary:** The Greeks are the partial derivatives of option price w.r.t. spot (delta/gamma), time (theta), and vol (vega/rho); every scenario reduces to which dominates. Recall the core relationships: ATM straddle ≈ expected move, put-call parity for synthetics, gamma-theta and vega-theta trade-offs, and that positive theta is always financed by negative gamma and vega. Do the arithmetic in ₹ per lot on Nifty (lot 75) and Bank Nifty (lot 30) — a 100-point move, a 1-vol-point IV change, a day of decay — in your head. Layer on India plumbing: European cash-settled index options, SPAN + Exposure margin that rises with VIX, STT on sells and on ITM exercise, rationalised 2026 weekly expiries, and the persistent index put-skew that prices the fat left tail. Size off risk not margin, cap net book vega and gamma against defined shock scenarios, and respect that the market pays theta as rent for the tail that most F&O losers under-price. Verify all 2026 figures before trading.
