# Cointegration & Statistical Pairs (India)

Pairs trading is the oldest quant strategy that still works, and it is the natural home for everything the previous chapter taught about z-scores. Instead of betting on the *level* of one asset, you bet on the *relationship* between two — going long the cheap one and short the expensive one when their spread stretches, and collecting as the spread snaps back. The magic word that makes this rigorous rather than a hunch is **cointegration**: a precise statistical condition under which two individually wandering (non-stationary) price series are tethered together so that a particular combination of them is mean-reverting. In Indian markets — with HDFC Bank vs ICICI Bank, Reliance vs ONGC, Tata Motors vs Ashok Leyland, and the whole PSU-bank complex — cointegration is where statistical arbitrage meets a market with enough liquidity and enough sector clustering to actually trade it.

## Origin & idea

The technique traces to Morgan Stanley's quant desk in the mid-1980s (Gerry Bamberger, later Nunzio Tartaglia's group) and was put on firm theoretical footing by Engle and Granger, whose 1987 cointegration paper won a Nobel. The core insight is subtle and worth stating carefully. Two stock prices are almost always **I(1)** — integrated of order one, meaning they wander like random walks and their *levels* are non-stationary (they have no fixed mean to revert to; today's price is the best forecast of tomorrow's). You cannot mean-revert a random walk. But if two such series are driven by the same underlying economic forces — two private banks facing the same rates, the same credit cycle, the same regulator — then a *linear combination* of them may strip out the shared random-walk component and leave a **stationary, mean-reverting residual**. That residual is the spread you trade.

Correlation is *not* cointegration, and confusing the two is the single most expensive mistake in pairs trading. Correlation measures whether two series move *together day-to-day*; cointegration measures whether they stay *tethered over the long run*. Two stocks can be 95% correlated in daily returns and still drift permanently apart (correlation without cointegration → the spread trends, you get run over). Two stocks can have modest daily correlation yet be tightly cointegrated (the spread always comes home). You want the second property. Correlation is a short-term co-movement; cointegration is a long-term equilibrium.

## The maths (precise)

### Step 1 — Confirm both legs are I(1)

Each price series individually must be non-stationary in levels but stationary in first differences (returns). You test this with the **Augmented Dickey–Fuller (ADF)** test on each series (developed fully in Chapter 69). If either leg is already stationary, cointegration analysis does not apply.

### Step 2 — Engle–Granger two-step

Regress one price on the other (ordinary least squares):

```
P_A,t = α + β · P_B,t + ε_t
```

Here `β` is the **hedge ratio** — how many rupees of B you short per rupee of A. The residual series is the spread:

```
spread_t = P_A,t − β · P_B,t − α
```

Now run an **ADF test on the residual `ε_t`**. If the residual is stationary (ADF rejects the unit-root null, typically at 5%), the pair is **cointegrated** and the spread is tradable. Critical values for the cointegration test are *more negative* than standard ADF criticals (use Engle–Granger / MacKinnon critical values, because β was estimated), so don't use the vanilla ADF table.

### Step 3 — Johansen test (for robustness / multi-asset)

Engle–Granger is direction-dependent (regressing A on B vs B on A can give slightly different answers) and handles only one pair. The **Johansen test** treats the system symmetrically, estimates the number of cointegrating relationships via trace and maximum-eigenvalue statistics, and gives the cointegrating vector directly. For a clean two-stock pair, Engle–Granger is fine; for baskets (e.g. three PSU banks) use Johansen.

### Step 4 — Trade the spread's z-score

Convert the spread into the z-score of the previous chapter, using a rolling window:

```python
import statsmodels.api as sm
import pandas as pd, numpy as np

# hedge ratio via OLS
X = sm.add_constant(df['P_B'])
beta = sm.OLS(df['P_A'], X).fit().params['P_B']

spread = df['P_A'] - beta * df['P_B']
z = (spread - spread.rolling(60).mean()) / spread.rolling(60).std(ddof=1)

# ADF on spread → confirms tradability
from statsmodels.tsa.stattools import adfuller
pval = adfuller(spread.dropna())[1]   # want < 0.05
```

Everything from Chapter 67 — entry at |z| ≥ 2, exit at z → 0, z-space stops — now applies to `spread` instead of a single price. The crucial upgrade is that pairs trading is **market-neutral**: you are long one leg and short the other, so a Nifty-wide crash that drags both stocks down leaves the spread roughly unchanged. You have hedged out market beta and are trading pure relative value.

### Half-life and hedge-ratio maintenance

Estimate the spread's **half-life** from an OU/AR(1) fit (as in Ch. 67) to choose the rolling window and the maximum holding period. And critically, **β drifts** — the economic relationship evolves, so re-estimate the hedge ratio on a rolling basis (e.g. rolling 90-day OLS) or via a Kalman filter, which updates β continuously as new data arrives. A stale β from six months ago is a common source of "the spread stopped reverting" losses.

## Worked India example (levels & ₹)

Take the canonical Indian pair: **ICICI Bank (P_A)** and **HDFC Bank (P_B)**, two large private banks with shared macro drivers. Suppose over the last year:

- ICICI ≈ ₹1,180, HDFC ≈ ₹1,700
- Rolling OLS hedge ratio β ≈ 0.62 (₹0.62 of HDFC moves per ₹1 of ICICI)
- ADF on the residual: p-value 0.02 → **cointegrated at 5%**, tradable
- Spread half-life ≈ 9 trading days → use a ~40–60 day rolling z window, max hold ~3 weeks

Today the spread stretches: ICICI has underperformed HDFC and the spread z-score prints **−2.3** (ICICI cheap relative to HDFC). The trade:

| Leg | Action | Size logic | Rupee exposure |
|---|---|---|---|
| ICICI (cheap) | **Buy** futures, 1 lot = 700 | Full notional | 700 × ₹1,180 = ₹8,26,000 |
| HDFC (rich) | **Sell** futures, β-matched | 700 × 0.62 ≈ 434 → round to 1 lot HDFC (550) | 550 × ₹1,700 = ₹9,35,000 |

The notionals are matched *approximately*; in practice you round to whole lots and accept a small residual beta, or trade cash-and-futures to fine-tune. The spread is entered at z = −2.3.

**Exit / target.** Book when z reverts to 0 (spread back to fair). If ICICI rallies ₹22 and HDFC is flat, the long leg earns 700 × ₹22 = ₹15,400; typically both legs contribute as the spread closes. A realistic net capture per reversion is ₹8,000–15,000 per unit after the short leg's offset.

**Stop.** Two triggers, whichever first: (a) **z-space stop** — spread pushes to z = −3.3 (structural divergence); (b) **cointegration-break stop** — if a rolling ADF re-test starts *failing* (p-value drifts above 0.10), the tether is breaking and you exit regardless of z, because the mean you are betting on has ceased to exist. This second stop is what separates disciplined stat-arb from stubborn averaging-down.

**Time stop.** If the spread has not reverted within ~2× the half-life (≈ 18 trading days), close it. A spread that overstays its half-life is signalling a regime change in the relationship — perhaps a bank-specific event (an NPA shock, a management change, an M&A rumour) has permanently repriced one leg.

Other genuinely cointegrated Indian candidates worth researching (always re-test, never assume): **SBI vs Bank Nifty PSU basket**, **Reliance vs Nifty Energy**, **Tata Steel vs JSW Steel**, **ACC vs Ambuja** (same promoter group — often tightly tethered), **GAIL vs ONGC**. Pairs cluster by sector and by shared fundamental drivers; that is not a coincidence, it is the economic reason cointegration exists.

## Backtest & edge notes with realistic costs

Pairs trading's edge profile is **market-neutral, high-hit-rate, capacity-limited, and cost-sensitive** — you pay two legs of friction on every entry and exit. In India specifically:

- **Two-sided costs.** Every trade is four executions (buy A, sell B, then reverse). STT, brokerage, exchange fees, GST, and stamp duty apply to each. On stock futures STT is on the sell side; the spread you capture must clear roughly 2× a single-stock's round-trip friction.
- **Short-leg mechanics.** You cannot freely short delivery equity in India beyond intraday; sustained shorts must be via **stock futures** (which limits the universe to F&O-eligible names, ~180 stocks) or via the SLB (securities lending & borrowing) mechanism, which is thin for many names. This is why practical Indian pairs trading lives almost entirely in the **F&O stock universe** and index-constituent space.
- **Financing/roll.** Holding a spread across an expiry means rolling both futures legs — cost and slippage each month. Keep holding periods inside the half-life to minimise rolls.
- **Backtest hygiene.** (1) Select the pair on an **in-sample** window and confirm cointegration *out-of-sample* — a pair that is cointegrated only in-sample is data-mined. (2) Beware **multiple-testing bias**: if you scan 500 stocks pairwise you test ~125,000 pairs, and by chance ~6,000 will "pass" a 5% cointegration test with no real relationship. Guard against this by (a) restricting candidates to economically sensible, same-sector pairs *before* testing, and (b) demanding cointegration to persist across multiple sub-periods. (3) Use **realistic fills** and full costs; net-of-cost a pairs edge is often 40–60% smaller than gross.

Realistically, a well-run Indian stat-arb pairs book targets a modest Sharpe (1–1.5) with low market correlation — its value is *diversification and stability*, not spectacular returns. It shines precisely when directional strategies suffer.

## Adaptations for NSE / F&O

- **Trade the pair with options for defined risk.** Instead of two futures legs, express a spread view via a long call spread on the cheap leg and a long put spread on the rich leg — caps loss if cointegration breaks catastrophically (a merger, a fraud).
- **Index-vs-constituent** relative value: e.g. Bank Nifty vs an over/under-weighted constituent basket, or Nifty vs Nifty futures basis (calendar).
- **Sector-basket cointegration** via Johansen: build a stationary combination of three or four PSU banks and trade the basket's z-score; more robust than a single fragile pair.
- **Intraday pairs** on 5-min bars for liquid same-sector large-caps — faster half-lives, more turnover, but costs bite harder; only viable in the most liquid names.

## Pitfalls

1. **Correlation ≠ cointegration.** The number-one error. Two 95%-correlated stocks can still drift apart forever. Always run the ADF-on-residual test, not just a correlation number.
2. **Cointegration is not permanent.** Relationships break — a merger, a regulatory shock, an accounting fraud (think of any bank that suddenly reprices on an NPA revelation). Monitor a **rolling cointegration p-value** and exit when the tether fails; do not "wait for reversion" that will never come. This is how pairs desks blow up: averaging into a spread whose economic basis has vanished.
3. **Hedge-ratio drift.** A static β from months ago mis-hedges you into net market exposure. Re-estimate (rolling OLS or Kalman filter).
4. **Data-mining / multiple testing.** Scanning thousands of pairs guarantees false positives. Start from economic logic, confirm out-of-sample, demand cross-period stability.
5. **Liquidity & short constraints.** The Indian short-selling reality confines you to F&O names; illiquid legs give slippage that eats the spread. Trade only names where both legs are liquid.
6. **Fat-tail divergence risk.** A spread can go from −2σ to −5σ before (if ever) reverting — the classic LTCM lesson. Size small, define risk, and respect the cointegration-break stop.

## Interview-ready summary

- **Cointegration**: two individually non-stationary (I(1)) price series whose *linear combination* is stationary and mean-reverting; that combination is the tradable spread.
- **Correlation ≠ cointegration** — correlation is short-term co-movement; cointegration is a long-run equilibrium tether. You need the second.
- Method: confirm both legs are I(1) (ADF) → **Engle–Granger** OLS to get hedge ratio β and residual → **ADF on the residual** (Engle–Granger criticals) to confirm cointegration → trade the residual's **z-score** exactly as in mean-reversion; use **Johansen** for baskets.
- The trade is **market-neutral**: long the cheap leg, short the β-matched rich leg; a market-wide move cancels, you capture relative value.
- India specifics: live in the **F&O stock universe** (short-selling constraint), match notionals with whole lots, use realistic **two-sided costs**, and mind expiry rolls.
- Exits: z → 0 target, **z-space stop** at |z| ≈ 3.3, a **cointegration-break stop** when the rolling ADF p-value fails, and a **time stop** at ~2× the half-life.
- Killers: mistaking correlation for cointegration, treating cointegration as permanent, stale hedge ratios, and data-mining thousands of pairs. Pairs trading is a *diversifier* — modest Sharpe, low market correlation, disciplined risk.
