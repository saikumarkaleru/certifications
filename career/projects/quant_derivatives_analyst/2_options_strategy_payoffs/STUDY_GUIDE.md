# Study Guide — Options Strategy Payoffs & Risk Toolkit

Your cheat-sheet to defend this project. This is bread-and-butter F&O — play to
your desk experience. Everything here maps to code you can open and point at.

---

## 1. The 30-second pitch
> "I built an options strategy toolkit in Python. Everything is constructed from
> one `Leg`/`Position` abstraction, so 16 strategies — from a long call to an iron
> condor — are just different lists of legs. For each I compute the P&L both **at
> expiry and before expiry** (Black-Scholes gives the time value), the **net
> position Greeks**, the **probability of profit** from the lognormal terminal
> distribution, a **spot-versus-vol scenario grid**, and a **screener** that ranks
> every strategy by risk/reward and probability of profit. Strikes and premiums
> come from a live yfinance option chain, with an offline fallback so it always
> runs."

---

## 2. What it is
A decision tool, not just a payoff plotter. A payoff diagram tells you the *shape*
of a trade; this tells you the *odds and the risk*: how likely you are to profit
(POP), how much reward you get per unit of risk (risk/reward), what your net
directional and volatility exposure is (Greeks), and how the position behaves if
spot and implied vol both move (scenario grid). Then it ranks the whole menu.

---

## 3. THE key interview answer — "a strategy is a sum of legs"
> "Every option strategy, no matter the name, is just a sum of simple legs. A leg
> is one contract you buy or sell, described by four numbers: kind (call/put/
> stock), strike, signed quantity (+long/−short), and premium. Its payoff at
> expiry is `qty × intrinsic − qty × premium`. Because quantity is signed, the
> same formula handles shorts automatically: a short call has qty < 0, so
> `− qty × premium` becomes a positive number — the credit collected. Add the
> legs' payoffs and you get the strategy. That's why one `Position` class gives me
> payoff, Greeks, breakevens and POP for all 16 strategies for free."

That's the whole architecture. `legs.py` is the heart; everything else consumes it.

---

## 4. The Leg / Position abstraction (walkthrough of `legs.py`)
- **`Leg`** (a dataclass): `kind, qty, strike, premium`. Methods:
  - `intrinsic(S)` — value of the underlying instrument at expiry: call
    `max(S−K,0)`, put `max(K−S,0)`, stock `S`. Vectorised over a numpy grid.
  - `payoff_at_expiry(S)` — `qty × intrinsic − qty × premium` (P&L, not gross).
  - `entry_cashflow()` — `−qty × premium`: cash out (long) or in (short) at open.
  - `value_before_expiry(S,T,r,sigma,q)` — marks the leg with **BSM** for T > 0.
  - `greeks(...)` — per-leg Greeks × qty (stock: delta = qty, rest 0).
- **`Position`** = a list of legs plus the analytics a desk cares about. Every
  method just **loops over legs and sums**, proving the "sum of legs" idea:
  - `payoff_at_expiry`, `net_debit_credit`, `value_before_expiry`,
    `pnl_before_expiry` (current model value − cost paid → the smooth curve),
    `net_greeks`, `breakevens` (zero-crossings, linearly interpolated on a dense
    grid), `max_profit_loss` (with unbounded-tail flags via edge slope).

## Module map
- **`bsm.py`** — minimal Black-Scholes-Merton with dividend yield q; `norm_cdf`
  built from `math.erf` (no scipy). Prices + Greeks. Vega quoted per 1 vol point
  (÷100), theta per calendar day (÷365). Powers before-expiry P&L, net Greeks, POP.
- **`legs.py`** — the `Leg`/`Position` abstraction described above.
- **`library.py`** — 16 builder functions, each returning a `StrategySpec`
  (name, `Position`, market view, category: bullish/bearish/neutral/volatility).
  Strikes are derived from spot and snapped to available strikes.
- **`analytics.py`** — `probability_of_profit` (lognormal), `scenario_grid`
  (spot × vol matrix of before-expiry P&L), `screen_strategies` (ranks by a
  combined risk/reward × POP score).
- **`market_data.py`** — live yfinance snapshot → cache to `input/` → synthetic
  BSM-priced ladder, so `main.py` always runs.
- **`main.py`** — 7-step orchestrator printing a summary at each step.

---

## 5. Expiry vs before-expiry P&L (the time-value point)
- **At expiry**: payoff is the kinked, piecewise-linear intrinsic curve.
- **Before expiry**: every option still has *time value*, so `pnl_before_expiry`
  marks each leg with BSM at T > 0 and subtracts the cost paid. The result is a
  **smooth, curved** line sitting above (for long options) the expiry payoff. The
  vertical gap between the two curves *is* the remaining time value. `main.py`
  Step 3 prints both for a long straddle; `time_value_overlay.png` draws them.

---

## 6. Interview Q&A (practice out loud)

**Q: Why is every strategy "just a sum of legs"?**
A: "Each leg has a payoff at expiry equal to `qty × intrinsic − qty × premium`,
and signed quantity handles long vs short automatically. Portfolios are additive,
so summing leg payoffs gives the strategy. One `Position` class then reuses the
same math for payoff, Greeks, breakevens and POP across all 16 strategies."

**Q: How do you compute probability of profit, and what does it assume?**
A: "Under Black-Scholes the terminal price S_T is lognormal — `ln(S_T)` is normal
with mean `ln S0 + (r − q − σ²/2)T` and std `σ√T`. I find the expiry breakevens,
figure out which spot intervals are profitable by testing the P&L sign, and
integrate the lognormal density over those intervals using the normal CDF of
`ln(S_T)`. The key assumption I'd flag is the drift: I use the **risk-neutral**
drift `r − q` for internal consistency with the pricing model. A desk might plug
in a real-world drift or their own view — that only shifts the drift term."

**Q: Expiry P&L vs before-expiry P&L — what's the difference and why does it
matter?**
A: "At expiry the P&L is the kinked intrinsic payoff. Before expiry there's still
time value, so I mark the legs with BSM — the curve is smooth and sits above the
expiry payoff for long options. It matters because you rarely hold to expiry:
you manage the position on the smooth curve, and time value plus vol changes drive
your daily P&L."

**Q: What do the net Greeks tell a desk?**
A: "Net delta is directional exposure — shares-equivalent. Net gamma is how fast
that delta changes, i.e. re-hedging risk. Net vega is exposure to implied vol —
positive for straddles/strangles, negative for condors and covered calls. Net
theta is daily time decay — short-vol trades earn it, long-vol trades pay it.
Together they summarise the whole position's risk in four numbers."

**Q: Iron condor vs iron butterfly — what's the trade-off?**
A: "Both are short-volatility, defined-risk credit trades. The condor sells an OTM
put spread and an OTM call spread, so it has a **wide profit zone** between the two
short strikes but a **smaller credit**. The butterfly sells the put and call at the
**same ATM strike**, so it collects a **bigger credit** but has a **narrow profit
zone** — it needs the stock to pin near that strike. Condor for range-bound,
butterfly for a strong pin view."

**Q: How does the screener rank strategies?**
A: "Two headline numbers: risk/reward = max profit / |max loss|, and POP. I score
each as `min(risk_reward, 5) × POP` — capping risk/reward so one lottery-ticket
ratio doesn't dominate — and sort best-first. Unbounded-loss trades (like the 1×2
call ratio) get an undefined risk/reward and are pushed down, so the ranking
rewards a strategy that has *both* a good payoff ratio and a good chance of
working."

---

## 7. Honest simplification to own in an interview
The **calendar spread** is a true two-expiry trade, but the `Leg` model uses one
expiry T. I model it as a single-expiry approximation (long call financed by a
credit) that captures the right economics — debit, long vega, benefits from
near-term decay — and I **flag it** rather than fake a two-expiry payoff. Saying
"here's the simplification and why" is stronger than pretending it's exact.

---

## 8. Vocabulary to know cold
Leg, position, long/short, premium, intrinsic value, time value, payoff at expiry
vs before expiry (mark-to-market), breakeven, net debit/credit, spread (vertical),
straddle, strangle, butterfly, iron condor, iron butterfly, collar, covered call,
protective put, ratio spread, calendar spread, delta / gamma / vega / theta, net
Greeks, long vs short volatility, probability of profit (POP), risk/reward,
lognormal terminal distribution, risk-neutral drift, capped vs unbounded risk.
