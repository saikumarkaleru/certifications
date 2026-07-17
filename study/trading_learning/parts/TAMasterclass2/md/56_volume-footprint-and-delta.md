# Volume Footprint & Delta Analysis

## What it is & why it works

A candlestick tells you four numbers — open, high, low, close — and the total volume for the bar. It hides the most important thing: *who was aggressive*. Inside every green candle there were sellers; inside every red candle there were buyers. The **footprint chart** opens the candle up and shows you, at *each price level within the bar*, exactly how much volume traded on the **bid** (aggressive selling) versus the **ask** (aggressive buying). **Delta** is the running score of that battle: `Delta = aggressive buy volume − aggressive sell volume`. Footprint is the microscope; delta is the scoreboard.

Why this is powerful: price is the *outcome* of an auction, but delta and footprint are the *mechanism*. They let you see effort vs result. When price makes a new high but delta *doesn't* — buyers pushed harder for a smaller reward — that's weakening demand you can see *before* the reversal shows up in price. When price hammers a support and delta goes deeply negative but price *won't fall* — sellers are being *absorbed* by a bigger passive buyer — that's a bottom forming in real time. This "effort vs result" divergence is the core edge, and it's invisible on a normal chart.

The honest caveat: footprint requires **tick-by-tick, bid/ask-classified data**. In India this is available on platforms like GoCharting, Quantsapp, and some broker/vendor terminals for Nifty/Bank Nifty futures and liquid stock futures — but data quality varies, and for options and thin stocks the classification is unreliable. Footprint shines on **liquid futures** (Nifty, Bank Nifty, Fin Nifty, MCX gold/crude, USDINR) where the tape is dense and the bid/ask split is meaningful. It is a *precision* tool, not a *direction-from-scratch* tool — you use it to time and confirm setups your structure (Volume Profile, S/R, trend) has already located.

## Mechanics: reading the footprint

The footprint bar shows, for each price row inside the bar, two numbers: **bid volume × ask volume** (often displayed as `123 × 456`). Common footprint styles:

- **Bid × Ask (dual):** the raw aggressive-sell vs aggressive-buy at each price.
- **Delta footprint:** the *net* (ask − bid) at each price, colour-coded green/red.
- **Volume footprint:** total volume per price (like a per-bar volume profile).

Key readable objects:

- **Bar delta:** the bar's net (buy − sell aggression). A green candle with *negative* delta is a warning (it rose despite net aggressive selling — thin, unsupported).
- **Cumulative Delta (CVD):** delta summed across bars — the running order-flow trend. CVD making higher highs with price = healthy uptrend. CVD *diverging* from price = the tell.
- **Delta divergence:** price higher high, delta lower high (bearish) — or price lower low, delta higher low (bullish). The classic footprint reversal signal.
- **Point of Control (bar POC):** the price row with the most volume inside the bar — where that bar's business concentrated.
- **Imbalances:** a price row where buy (or sell) volume dwarfs the *diagonal* opposite (e.g., ask at this price ≫ bid at the price below, by a set ratio like 300%+). Stacked imbalances mark aggressive, one-sided pushes and create *support/resistance shelves*.
- **Absorption:** a price level with *huge* volume but *little price movement* — aggressive orders hitting a wall of passive liquidity. The market "should" have moved and didn't.
- **Exhaustion:** shrinking delta/volume at the extreme of a move — the aggressive side running out of fuel.
- **Unfinished auction (no-tail / poor high-low):** a bar's extreme with volume on *both* bid and ask (no zero-print single) — the auction didn't finish there; price tends to return.

## Worked India example (levels & ₹)

**Nifty futures — a delta-divergence short at resistance (approximate reconstruction; verify on your platform's footprint).**

Context: Nifty futures rallying through the morning. Volume Profile / structure marks **overhead resistance at 24,880** (a prior-day VAH and a naked VPOC). Structure says "resistance zone"; footprint will tell us whether buyers can *break* it or are *exhausting* into it.

The tape:

- Nifty pushes from 24,820 to **24,872** on a strong bar: bar delta **+9,500**, stacked *buy* imbalances up the right side — genuine aggressive buying. Healthy so far.
- Next push to **24,884**, just above resistance: the bar makes a *higher high* in price, but bar delta is only **+3,100**, and CVD prints a *lower high* than the prior swing. **Effort rose in price, result in delta shrank** — a bearish delta divergence right into a known resistance level.
- The *very next* bar wicks to **24,890** with heavy volume at the high but a *negative* delta (**−4,200**) and volume on *both* bid and ask at the extreme — **absorption + unfinished auction**. Aggressive buyers are being soaked up by a passive seller; the high is being defended.
- **Trade (footprint short):** enter short on the break back below 24,870 (re-entry into value), confirmed by CVD rolling over. **Stop** above the absorption high, ~24,900 (if buyers *accept* above 24,890, the seller has been overwhelmed — thesis dead). Risk ~30 points.
- **Targets:** intraday VWAP / session POC at **24,810** (first), then the morning value-area low at **24,760** (second).
- **Outcome:** with demand exhausted and a seller absorbing, price rolls back to 24,810 (book half, +60), then slides to 24,765 (book rest, +105). Reward ~60–110 vs ~30 risk → ~2–3.6:1.

The lesson: *structure* found the level (24,880 resistance); *footprint/delta* proved it would hold this time — the divergence said demand was weakening, the absorption + unfinished auction said a passive seller was defending, and the CVD roll-over gave the trigger. Shorting resistance blind is a coin-flip; shorting it *with a visible exhaustion-and-absorption signature* is a trade.

## How to trade it (entry / stop / target)

Footprint/delta is a **timing and confirmation** layer. Four repeatable applications:

**1. Divergence reversal (at a known level).**
- Location: price at established support/resistance (VPOC, VAH/VAL, prior day high/low).
- Trigger: price makes a new extreme, delta/CVD makes a *weaker* extreme (divergence) — ideally plus absorption at the extreme.
- Stop: just beyond the absorption extreme. Target: the mean (VWAP/POC), then the opposite value edge.

**2. Absorption reversal.**
- Location: price grinding into a level, delta strongly one-way, but price *stalls*.
- Read: the aggressive side is being absorbed by passive liquidity. Enter *against* the absorbed aggressors once price reclaims the level.
- Stop: beyond the absorption zone (if the wall is broken, absorption failed).

**3. Imbalance-shelf continuation.**
- Stacked buy (or sell) imbalances create a support (resistance) shelf. On a pullback *to* that shelf, if delta turns back in the trend direction and imbalances re-appear, enter *with* the trend.
- Stop below the shelf; target the prior swing / measured extension.

**4. Delta confirmation of a breakout.**
- On an Initial-Balance or range breakout, demand the *breakout bar* to show strong same-direction delta and buy/sell imbalances. A breakout on *weak or opposite* delta is a trap — stand aside or fade. This one filter kills a huge fraction of false breakouts.

Sizing discipline: because footprint gives tight stops (just beyond an absorption extreme), it *increases* position size for the same rupee risk — its main practical benefit. But keep stops honest; a "tight" stop that sits inside noise just gets you tapped out.

## Confluence (including OI)

- **Volume Profile:** footprint is the intrabar cousin of the profile. Trade footprint signals *at* VPOC / VAH / VAL — a divergence at a naked VPOC is far stronger than one in open air.
- **Option chain OI (the India edge):** delta shows *aggression*; OI shows *positioning*. When footprint absorption at Nifty 24,880 coincides with heavy Call writing at the 24,900 strike, two independent lenses agree that a passive seller is defending that zone — high conviction. Conversely, aggressive buy-delta breaking through a strike where Call writers are being forced to unwind (OI falling as price rises) is a *short-covering squeeze* signature — go with it.
- **VWAP:** delta divergences that occur *at* the upper/lower VWAP band are doubly located; VWAP is often the first delta-reversal target.
- **CVD vs price on the higher timeframe:** a persistent CVD downtrend under a rising price (distribution) warns that intraday longs are swimming against the deeper flow.
- **Cumulative delta across the session** confirms day type: strongly trending CVD = trend day (trade continuation, don't fade divergences too eagerly); flat, oscillating CVD = rotational day (divergences at extremes are gold).

## Pitfalls

1. **Bad or misclassified data.** Footprint lives or dies on accurate bid/ask tick data. On illiquid stocks, options, or a laggy feed, the bid/ask split is garbage and every signal is noise. Restrict footprint to liquid futures with a reliable vendor.
2. **Fading a trend on every divergence.** In a strong trend, delta divergences appear repeatedly and *fail* — price keeps grinding. Divergences are for *rotational* contexts and *established levels*, not for fading a freight-train trend day. Check CVD/day type first.
3. **Confusing delta with price.** Delta can be negative while price *rises* (absorption of sellers, then squeeze) — that's often *bullish*, not bearish. Read delta *relative to price behaviour* (effort vs result), never in isolation.
4. **Spoof-driven false absorption.** A large passive order that gets pulled can fake an absorption read. Confirm with *executed* volume staying heavy and price genuinely refusing to move, not just a big number flashing in the DOM.
5. **Over-trading the micro.** Footprint tempts you to react to every bar. It is a *confirmation* tool for structurally located setups, not a signal generator to trade in a vacuum. No level, no trade.
6. **Ignoring absolute liquidity / time of day.** Early-morning and pre-close bars have distorted volume; lunch-hour tape is thin and delta is unreliable. Weight signals by session context.
7. **Chasing after the imbalance is spent.** Stacked imbalances mark where aggression *already happened*; entering after the move is exhausted, not at the shelf on a pullback, is late. Trade the *retest*, not the spike.

## Interview-ready summary

Footprint and delta open up the candle to show *who was aggressive* at each price: **bid volume = aggressive selling, ask volume = aggressive buying**, and **delta = ask − bid** is the running scoreboard, with **cumulative delta (CVD)** tracking the order-flow trend across bars. The central edge is **effort vs result**: when price makes a new extreme but delta/CVD makes a weaker one (**divergence**), demand or supply is fading before price shows it; when price refuses to move despite heavy one-sided aggression (**absorption**), a larger passive player is defending a level and a reversal is brewing; and **stacked imbalances** build the support/resistance shelves you trade pullbacks into. The four playbooks — divergence reversal, absorption reversal, imbalance-shelf continuation, and delta-confirmation of breakouts — are all *timing/confirmation* overlays on levels that Volume Profile and structure have already located; the discipline is "**no level, no trade.**" Footprint's practical payoff is *tighter, better-justified stops* (just beyond an absorption extreme), which lets you size up for the same risk. It works best on **liquid Indian futures** (Nifty, Bank Nifty, MCX, USDINR) with clean tick data, is unreliable on thin stocks and options, and is at its most powerful when the aggression it reads (delta/footprint) *confluences* with the positioning the option chain shows (OI, writer walls, max-pain) — aggression and positioning agreeing is as high-conviction as intraday reads get.
