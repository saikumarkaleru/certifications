# Portfolio Heat & Correlation Risk

Most retail traders manage risk one trade at a time. They size each position at "1% of capital," feel disciplined, and then wonder why a single bad session took out 6% of their account. The answer is almost always the same: they were running eight positions that were secretly the *same* trade. Portfolio heat and correlation risk are the two ideas that separate a trader who survives a bad week from one who is wiped out by it. This chapter is about seeing your book as one organism, not a collection of independent bets.

## The principle: your real risk is the sum, not the slice

**Portfolio heat** is the total amount of your capital that is currently exposed to loss across all open positions, measured at your stops. If you have five trades open, each risking 1% (distance from entry to stop, times position size, as a fraction of equity), your portfolio heat is 5%. That is the amount you would lose if every stop got hit today.

The mistake is treating that 5% as if it were five independent coin flips. It is not. On a red day in the Indian market, when FIIs dump index futures and the Nifty gaps down 1.5%, your long in Reliance, your long in HDFC Bank, your long in L&T, and your long in Tata Motors do *not* fail independently. They fail together, because they share a common driver: broad market beta. Your "diversified" five-position book behaves, on a bad day, like one large position. The 5% heat you thought was spread out arrives all at once.

Correlation risk is the formal name for this. Two positions are correlated when they tend to move together. When correlation is high and positive, stacking positions does not diversify risk — it *concentrates* it while giving you the comforting illusion of spread. The single most expensive lesson in trading is discovering, on the worst possible day, that your book was one trade wearing five costumes.

There is a hard, non-negotiable arithmetic reason this matters: the math of drawdown recovery is brutal and non-linear. Lose 10% and you need 11.1% to get back. Lose 25% and you need 33%. Lose 50% and you need a 100% gain just to break even. Portfolio heat control exists to keep you on the gentle, recoverable part of that curve — because the market does not care how good your setups are if a correlated cluster of them fails simultaneously and puts you in a hole you cannot climb out of.

## The method: heat budgeting with a correlation overlay

The system has three layers: a per-trade risk cap, a total-heat cap, and a correlation-adjusted cap that groups related positions. You apply all three at once, and the *most restrictive* one wins.

### Layer 1 — per-trade risk (R)

Define one unit of risk, R, as a fixed fraction of current equity. For most serious retail accounts, R = 0.5% to 1.0%. On a Rs 10,00,000 account at 1%, R = Rs 10,000. Every trade risks one R (or a fraction) from entry to stop. This is your atom of risk. You never think in shares or lots first; you think in R, then back into quantity.

Position size formula:

`Quantity = (Equity x R%) / (Entry price − Stop price)`

Example: buy Tata Motors at Rs 980, stop at Rs 948 (Rs 32 risk per share). R = Rs 10,000. Quantity = 10,000 / 32 = 312 shares. Capital deployed = 312 x 980 = Rs 3,05,760, but *risk* is only Rs 10,000. Notice the gap: capital deployed and risk are completely different numbers, and heat is measured on risk, never on capital.

### Layer 2 — total portfolio heat cap

Set a hard ceiling on the sum of all open R. A sensible band for a discretionary swing trader:

| Trader state | Max total heat | Meaning |
|---|---|---|
| Building / uncertain | 2–3% | 2–3 full positions |
| Normal conditions | 4–6% | 4–6 full positions |
| Aggressive / high conviction, calm tape | 6–8% | ceiling — never routine |
| Post-drawdown recovery | 1–2% | forced de-risking |

If your cap is 6% and you already have 6 positions each at 1R, you are full. A seventh setup, however beautiful, does not get taken until you close something. This is the rule that hurts the most and saves the most. The market always offers another setup; it does not always offer another account.

### Layer 3 — the correlation overlay (the part everyone skips)

This is where you stop fooling yourself. Group your positions into **correlation clusters**, and cap the heat *per cluster*, not just per position.

For the Indian market, a practical clustering scheme:

| Cluster | Typical members | Why they move together |
|---|---|---|
| Banks / Financials | HDFC Bank, ICICI, Axis, SBI, Bajaj Finance, Bank Nifty | Rate cycle, credit, FII flows; ~35% of Nifty |
| IT / Exporters | TCS, Infosys, Wipro, HCL Tech | USDINR, US demand, Nasdaq |
| Autos | Maruti, Tata Motors, M&M, Bajaj Auto | Rural demand, rates, commodity input costs |
| Metals / Commodities | Tata Steel, JSW, Hindalco, Vedanta | Global growth, China, LME/MCX |
| Energy / Oil & Gas | Reliance, ONGC, BPCL, IOC | Crude, refining margins |
| FMCG / Defensives | HUL, ITC, Nestle, Britannia | Inverse to risk-on; low beta |
| Index longs | Nifty / Bank Nifty / Fin Nifty futures & options | Pure market beta |

**Rule:** total heat inside any single cluster must not exceed roughly half your total-heat cap. If your total cap is 6%, no cluster carries more than 3%. Three longs in HDFC Bank, ICICI, and Axis at 1R each are *not* three positions — they are one 3R bet on Indian financials, and they hit your cluster ceiling by themselves.

There is a subtler layer still: **index beta.** Every long equity position carries hidden Nifty beta. A high-beta name like Tata Motors (beta ~1.3) risking 1R is really risking more like 1.3R when the *whole market* moves against you, because on a market-wide down day it falls more than the index. A defensive like HUL (beta ~0.6) risking 1R behaves like 0.6R of market exposure. You can build a crude beta-weighted heat number:

`Beta-adjusted heat = Σ (position R x position beta)`

If you are long five high-beta names each at 1R, your nominal heat is 5% but your beta-adjusted heat against a market crash is closer to 6.5%. That is the number that actually shows up on a gap-down morning.

### The negative-correlation credit

Correlation cuts both ways. A short in Bank Nifty against a long in TCS are *negatively* correlated in some regimes (rupee weakness helps IT, hurts import-heavy financials sentiment). A genuinely hedged pair can carry *more* combined heat because the positions partially offset. But be honest and conservative here: correlations are unstable, and in a genuine liquidity crisis (March 2020, or any sharp FII-exit day) *everything* correlates to 1 and even your hedges can gap against you. Give yourself only partial credit for a hedge — treat a -0.5 correlated pair as maybe 30% offsetting, not 100%. Never let a theoretical hedge tempt you into gross exposure you could not survive if the correlation broke.

## Worked example: the "diversified" book that wasn't

It is a Tuesday in 2026. Nifty is at 24,800, grinding up for three weeks, low VIX (~11). You feel good and your account is Rs 10,00,000, R = Rs 10,000 (1%). Over four sessions you accumulate:

| # | Position | Direction | Entry | Stop | Risk (R) | Cluster | Beta |
|---|---|---|---|---|---|---|---|
| 1 | HDFC Bank | Long | 1,720 | 1,690 | 1.0R | Financials | 1.0 |
| 2 | ICICI Bank | Long | 1,250 | 1,228 | 1.0R | Financials | 1.1 |
| 3 | Axis Bank | Long | 1,180 | 1,158 | 1.0R | Financials | 1.2 |
| 4 | Bajaj Finance | Long | 9,400 | 9,220 | 1.0R | Financials | 1.4 |
| 5 | Tata Motors | Long | 980 | 948 | 1.0R | Autos | 1.3 |
| 6 | Reliance | Long | 2,980 | 2,930 | 1.0R | Energy | 1.0 |

Nominal portfolio heat: 6.0R = 6%. Feels within a normal cap. But look through the correlation lens.

**Financials cluster:** positions 1–4 = 4.0R. That is *two-thirds* of the entire book in one sector — a sector that is ~35% of the Nifty and the primary vehicle for FII flows. A cluster cap of 3% is already breached by a full 1R. This book is not "six diversified longs." It is a leveraged bet on Indian banks, with a small auto and energy garnish.

**Beta-adjusted heat:** every position is long, every beta is ≥1.0. Σ(R x beta) = (1.0 + 1.1 + 1.2 + 1.4 + 1.3 + 1.0) = 7.0. Against a broad market decline, the book behaves like 7% heat, not 6%.

Now the trigger. Wednesday morning, a weak US CPI print overnight, the RBI signals a hawkish pause, and FIIs sell. Nifty gaps down 1.6% and keeps sliding; Bank Nifty falls 2.3% (financials lead the decline, as they usually do on FII-exit days). By 10:15 a.m. all four bank stops are hit — not one at a time over days as you imagined, but together, in twenty minutes, all with slippage past your stop because everyone's stops sat in the same zone. Tata Motors (high beta) is also stopped. Reliance holds.

Realised loss: four financials at slightly worse than 1R each (~1.15R with slippage) + Tata Motors at ~1.2R + Reliance still open. That is roughly 4x1.15 + 1.2 = 5.8R gone, ~5.8% of the account, in a single morning. You "risked 1% per trade" and lost nearly 6% in one hour, because the trades were never independent.

**How the overlay would have prevented it:** with a 3% financials cluster cap, you could hold at most three of the four bank longs — and honestly, you would hold *one or two* and express further financials conviction through Bank Nifty directly rather than stacking single names. The freed-up heat would go to genuinely uncorrelated exposure: a defensive (HUL), an IT name (Infosys, which actually *benefits* from the rupee weakness that hurt the banks), or simply cash. Same six slots, a fraction of the drawdown.

## Building it into your routine

A checklist you run *before* every new entry, not after:

**The pre-trade heat check (60 seconds):**

1. What is my current total open heat, in R? (Keep a live tally — a spreadsheet or a note.)
2. Which cluster does this new trade belong to? What is that cluster's current heat?
3. Does adding 1R breach either the total cap or the cluster cap? If yes, *stop* — the trade does not happen, or an existing position must be closed/reduced first.
4. What is this name's beta? Is my beta-adjusted heat still acceptable?
5. Am I adding correlation or reducing it? Is this a fifth long in a market I'm already max-long, or does it genuinely diversify / hedge?

**A weekly portfolio review:**

- Draw the cluster map. Colour every open position by cluster. If one colour dominates, you have hidden concentration — fix it before the market does.
- Recompute beta-adjusted heat against a −2% Nifty scenario. Ask literally: "If Nifty gaps down 2% tomorrow and every stop fills with slippage, how much do I lose? Can I take that number twice in a row and still function?"
- Check pairwise: are any two positions really the same trade? (Two PSU banks. Two IT largecaps. A stock and its sector index.) Collapse them.

**Regime awareness:** correlations rise when volatility rises. When India VIX spikes above ~18–20, *cut your total-heat cap*, because the diversification you're counting on is quietly evaporating — everything is starting to move together. In a genuine panic, plan for correlation = 1 across all equity longs and size as if your whole equity book were a single position.

**The event overlay:** around known binary events — RBI policy, Union Budget, monthly F&O expiry, US Fed decisions, major earnings for a heavily-weighted name — correlations spike and gaps widen. Reduce heat *into* these events, or explicitly accept overnight gap risk that can blow through stops. Your stop is a request, not a guarantee; on a gap it is filled at the open, wherever that is.

## Pitfalls

- **Confusing capital allocation with risk.** "Only 30% of my capital is deployed" tells you nothing about heat. A 30%-deployed book with tight stops on high-beta names can carry more heat than a 60%-deployed book of low-beta defensives.
- **Counting the hedge as free.** A hedge that relies on a stable correlation is not free insurance; in a crisis the correlation can invert. Give partial credit only.
- **Static caps in a changing regime.** A 6% cap that's fine in a low-VIX grind is reckless in a high-VIX, gap-prone tape.
- **Ignoring the index-future elephant.** One Nifty or Bank Nifty futures long can carry more beta-heat than five cash positions combined. Size it inside the same framework.
- **Cluster blindness in themes.** Sometimes correlation isn't sectoral — it's thematic. "Rate-sensitive" spans banks, autos, and real estate. "Rupee-weakness plays" spans IT and pharma. Map by *driver*, not just by GICS sector.
- **Adding heat to a losing book.** The temptation to "make it back" by adding positions after a drawdown is how a bad week becomes a blown account. Post-drawdown, your cap should *fall*, not rise.

## Interview-ready summary

Portfolio heat is the sum of all your open risk-to-stop, expressed as a percentage of equity — it is what you lose if every stop hits at once. The critical insight is that positions do not fail independently: correlated positions, especially within a sector cluster (Indian financials being the dominant one, at ~35% of the Nifty) or with shared beta, fail *together* on a bad market day, so a "diversified" six-position book can behave like a single 6R bet. The system to control this has three nested caps — per-trade R (0.5–1%), total heat (4–6% normal), and a per-cluster cap (roughly half the total) — with a beta-weighting overlay to capture hidden market exposure, all tightened when VIX rises and around binary events. Manage the book as one organism, keep drawdowns on the recoverable part of the curve, and remember: the market always offers another setup, but it does not always offer another account.
