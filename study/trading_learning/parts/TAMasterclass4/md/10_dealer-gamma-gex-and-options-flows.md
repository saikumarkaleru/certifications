# Dealer Gamma (GEX) & Options-Flow Positioning

Options are no longer a sideshow in Indian markets — they *are* the market. On a typical 2026 session, Nifty and Bank Nifty weekly options turn over more notional than the entire cash market of the NSE. When a market's price discovery is dominated by options, the people who *sell* those options — the dealers, market-makers and institutional desks on the other side of every retail long — are forced to hedge in the underlying. Their hedging is mechanical, predictable, and large. Dealer gamma positioning tells you *which way that mechanical flow leans*, and therefore whether the index is likely to be pinned, mean-reverting, or prone to violent trending expansion. This chapter treats gamma exposure (GEX) as a breadth-of-positioning indicator: a way to read the hidden hand of the hedgers before it moves price.

## What it is & the logic

Every listed option has a **delta** (sensitivity of the option price to the underlying) and a **gamma** (the rate of change of that delta). A market-maker who sells you a Nifty call is *short* that call. To stay delta-neutral, he buys some Nifty futures against it. But as the index moves, his required hedge changes — that change is gamma.

The critical fact is the *sign* of the dealer's gamma, because it dictates the *direction* of his hedging trades:

- **Dealers long gamma (positive GEX):** As price rises, dealers must *sell* the underlying to stay neutral; as price falls, they must *buy*. Their hedging is **counter-trend** — it dampens volatility, compresses ranges, and pins price toward large strikes. Markets grind, chop, and mean-revert.
- **Dealers short gamma (negative GEX):** As price rises, dealers must *buy* more; as price falls, they must *sell* more. Their hedging is **pro-trend** — it amplifies moves, feeds momentum, and produces the fast, "gap-and-go" or "waterfall" sessions. Markets trend and expand.

The retail crowd in India is a persistent *buyer* of weekly out-of-the-money options (lottery-ticket calls and puts). That means dealers are usually *short* those OTM options and *long* the richer ATM structures institutions sell — the net can flip week to week, but the mechanism is always the same: **find the sign, and you know whether the tape wants to pin or to run.**

The logic connects to everything else in this volume. GEX is not a chart pattern; it is a map of *forced flow*. A support level defended by positive dealer gamma is far stronger than the same level with no gamma behind it, because dealers are mechanically buying dips there. The same level under negative gamma is a trapdoor.

## Construction & reading

You do not need to reprice the whole option chain yourself; NSE publishes open interest (OI) per strike, and that is the raw material. A workable desk approximation of gamma exposure per strike is:

```
GEX(strike) ≈ Gamma(strike) × OI(strike) × ContractMultiplier × Spot² × 0.01 × Sign
```

where **Sign = +1 for call OI and −1 for put OI** under the standard convention that dealers are long calls / short puts relative to the retail crowd (many desks flip this; the point is internal consistency, not the absolute label). Aggregate across all strikes to get **net GEX**. The zero-crossing of cumulative GEX as you sweep spot up and down is the **gamma flip level** — the single most important number.

In practice, retail traders in India build three readable quantities from the free NSE option chain:

**1. The Max-Pain / Max-OI wall.** The strike with the largest combined OI acts as a magnet under positive gamma. For Bank Nifty a 50,000 strike carrying 40–50 lakh shares of OI on expiry morning is a genuine pin candidate.

**2. The Put/Call OI structure.** Heavy put OI *below* spot and heavy call OI *above* spot is the classic "positive-gamma cage" — dealers defend both walls, price oscillates between them. When that structure inverts (calls building below spot, puts above), gamma has likely flipped negative and the cage is broken.

**3. The gamma flip estimate.** Sweep a hypothetical spot across strikes, recompute cumulative signed GEX, and mark where it crosses zero. Above the flip = positive-gamma regime (fade extremes). Below the flip = negative-gamma regime (respect momentum, cut fades).

| Regime | Dealer hedging | Volatility | Best tactic | Typical India session |
|---|---|---|---|---|
| Deep positive GEX | Counter-trend | Suppressed | Fade edges, sell premium, expect pin | Nifty ±0.3% range into expiry |
| Near flip (≈0) | Unstable | Rising | Reduce size, wait for break | Coiling before an event |
| Negative GEX | Pro-trend | Amplified | Trade breakouts, buy momentum, stop fading | Budget-day / RBI trend day |

A second layer is **charm and vanna** — how dealer hedges drift with *time* and *implied vol* even when spot is still. On expiry day in India (Nifty Thursday, Bank Nifty Thursday, Fin Nifty Tuesday historically, with the 2024–25 reshuffle to a single weekly-expiry-per-index regime you must confirm live), charm becomes enormous: OTM options bleed delta into the pin strike through the day, and the "3 pm pin" many traders observe is charm-driven dealer buying/selling toward max-OI.

## Worked India example

Take a Bank Nifty weekly expiry morning. Spot opens at 50,180. From the NSE option chain you tabulate OI (in lots) at the key strikes:

| Strike | Call OI (lots) | Put OI (lots) | Net signed OI | Note |
|---|---|---|---|---|
| 49,500 | 8,000 | 62,000 | −54,000 | Heavy put wall (support) |
| 49,800 | 12,000 | 38,000 | −26,000 | Secondary put support |
| 50,000 | 40,000 | 41,000 | ≈ 0 | Max-OI magnet / pin candidate |
| 50,200 | 34,000 | 15,000 | +19,000 | Call resistance forming |
| 50,500 | 58,000 | 6,000 | +52,000 | Heavy call wall (resistance) |

Reading this: puts dominate below spot, calls dominate above, and the 50,000 strike is a balanced magnet essentially *at* spot. This is a textbook **positive-gamma cage** between the 49,500 put wall and the 50,500 call wall, with 50,000 as the pin.

Your gamma-flip estimate: because put OI below spot is signed negative but represents dealers being *short* puts (they buy dips to hedge), and call OI above is where dealers are *short* calls (they sell rallies), the whole 49,500–50,500 corridor is positive-gamma. The flip only appears if spot breaks *below* 49,500, where the put wall's protective hedging exhausts and dealers flip to selling into weakness.

**The trade plan that falls out of this:**

- Base case (70% of such mornings): price oscillates 49,900–50,250 and drifts toward 50,000 by afternoon as charm pins it. Tactic: sell the 50,000 straddle *only if you are experienced and hedged*, or simply fade pushes to 50,200 with tight stops, targeting 50,050.
- Break case: a decisive 15-minute close below 49,500 on volume means the put wall broke, gamma likely flipped negative, and dealer selling now *feeds* the fall. Tactic: stop fading immediately, flip to short with a target at 49,200 then 49,000, because the counter-trend cushion is gone.
- Upside break case: a close above 50,500 chews through the call wall; dealers who were short those calls now chase delta by buying futures, producing a squeeze toward 50,800. Tactic: buy the breakout, do not short into it.

The single most expensive retail mistake is fading the 50,500 breakout "because it looks extended" — under a broken call wall that is precisely when dealer hedging turns into your enemy. GEX tells you *the same chart level means opposite things in the two regimes.*

## How to use it for bias & timing

GEX is a **filter and a regime map**, not a standalone signal. Use it three ways:

1. **Set your playbook before the open.** Positive-gamma day → you are a mean-reversion trader: fade edges, expect the range, keep targets modest, sell premium if skilled. Negative-gamma day → you are a momentum trader: trade breakouts, widen targets, never fade, and expect the range to expand 1.5–2×.

2. **Grade your support/resistance.** A chart level that coincides with a heavy same-direction OI wall *and* positive dealer gamma is A-grade — trade toward it and fade against it with confidence. A level with no OI behind it is just a line.

3. **Time the volatility.** As spot approaches the gamma flip, *reduce size*. The flip zone is where the market's character changes mid-session; it is the highest-uncertainty region. The best trend days of 2026 — post-Budget, post-RBI-surprise, post-global-gap — almost all began with spot pushing through the flip into negative gamma, where every dealer hedge poured fuel on the fire.

Combine with the breadth and intermarket tools elsewhere in this volume: negative GEX *plus* deteriorating advance-decline *plus* a DXY spike is a high-conviction trend-down setup; positive GEX *plus* flat breadth is the "sit on your hands, sell theta" day.

## Pitfalls

- **You cannot see true dealer positioning.** NSE OI does not label who is long or short each option. The call-long/put-short convention is a *heuristic* that fails when institutions are net long puts (hedged portfolios) or when a large directional player dominates a strike. Treat GEX sign as a *probability tilt*, never a certainty.
- **OI is stale intraday.** NSE disseminates OI with a lag and it settles overnight. Your gamma map is freshest at the open and decays through the day as new flow arrives. Rebuild it, don't trust yesterday's cage.
- **Expiry compression distorts everything.** On expiry day gamma is enormous and localised; a strike can pin hard for hours then release violently in the last 30 minutes as it goes worthless. Do not confuse a mid-day pin with a durable level.
- **Regime can flip *inside* the session.** A morning positive-gamma cage becomes a negative-gamma trend the instant a wall breaks. Static analysis kills accounts — re-read the sign after every wall break.
- **India-specific plumbing changes.** Expiry-day schedules, lot sizes, and the single-weekly-expiry rules have been revised repeatedly by SEBI/NSE in 2024–2026. Always confirm the *current* expiry calendar and lot size before sizing a gamma trade; a stale assumption about which index expires on which day is a portfolio-level error.
- **Over-fitting the max-pain narrative.** Max-pain is a *tendency*, not a law. On event days it is routinely violated. Never hold a losing position "because it should pin to max-pain."

## Interview-ready summary

Dealer gamma exposure (GEX) reads the *forced hedging flow* of options market-makers. When dealers are **long gamma (positive GEX)**, they hedge counter-trend — selling rallies, buying dips — which **suppresses volatility and pins price** toward heavy-OI strikes; trade it as mean-reversion, fade the edges, sell premium. When dealers are **short gamma (negative GEX)**, they hedge pro-trend — buying strength, selling weakness — which **amplifies moves**; trade it as momentum, respect breakouts, never fade. The **gamma flip** is the spot level where net signed GEX crosses zero and the market's character inverts; reduce size near it. In India you approximate all of this from the free NSE option-chain OI: put walls below and call walls above spot form a positive-gamma cage between max-OI strikes; a decisive break of a wall signals a likely flip to negative gamma, where dealer hedging turns from cushion to accelerant. GEX is a regime filter that grades your support/resistance and sets whether today is a fade day or a run day — it is not a standalone buy/sell signal, the dealer sign is a probability heuristic (OI is unlabelled and stale intraday), and expiry-day charm dynamics plus SEBI's evolving expiry rules demand you rebuild the map live rather than trust yesterday's.
