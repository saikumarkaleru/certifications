# Managing Iron Condors & Short Strangles (Adjustments)

*India F&O supplement — written July 2026. Rules cited (STT on options ~0.1% on premium for sells, SEBI expiry/lot-size framework, SPAN+Exposure margin) reflect 2026 as understood at time of writing. **Verify current values with NSE/SEBI/your broker before trading** — expiry days, lot sizes and STT have all changed more than once in the last two years.*

## The idea

An iron condor and a short strangle are two ways of selling the same thing: **the market's fear premium**. You are short a call spread and short a put spread (condor), or naked short a call and a put (strangle). Both are delta-neutral-ish, short-vega, short-gamma, positive-theta positions. You get paid every day the index sits still and implied volatility bleeds down. You lose — sometimes brutally — when the index trends hard or when IV explodes.

For an experienced Indian options trader these are the bread-and-butter income structures on Nifty, Bank Nifty and Fin Nifty. They earn their keep in the **72–95% of trading days where the index does nothing dramatic**. The problem is never the winning days; it's that a single un-managed expiry-week trend or a gap can hand back three weeks of theta. So the *strategy* is trivial to describe and the *management* is the entire game. This chapter is about management: when to leave it alone, when to roll the untested side, when to convert, and when to take the loss and go home.

The honest framing up front: **selling premium is a strategy with a high win rate and a negatively-skewed payoff.** Most retail traders who blow up on Bank Nifty do it selling naked strangles into an expiry-day move or a Budget/RBI/US-CPI gap. The condor is the strangle with insurance bought — you cap the tail in exchange for a lower credit and a defined, financeable margin. If you cannot articulate, before entry, exactly what you will do at 1.5x and 2.5x the credit received, you are not trading a condor; you are writing a lottery ticket to the market.

When does it earn its keep? Sell condors/strangles when **IV is elevated relative to realised** (India VIX in the upper half of its recent range, say 14–20+, and the ATM IV of the expiry richer than the realised vol you're actually seeing), when there is **no scheduled binary event** inside the expiry you can't stomach, and when the index is **range-bound or mean-reverting**. Stand aside — or buy premium instead — when VIX is crushed to 10–11 (you're being paid nothing to hold unlimited-ish risk) or when a known catalyst (Union Budget, monetary policy, national election result, a large-cap earnings-heavy week for Bank Nifty) sits inside your window.

## The mechanics

Take Nifty with weekly expiry (as of 2026 Nifty weekly expiry is **Tuesday**; Bank Nifty is monthly-only after SEBI's 2024–25 rationalisation of weekly contracts — **verify the current expiry calendar**, this has changed repeatedly). Lot size Nifty = **75**; Bank Nifty = **35** (again, verify — lots were revised upward in late 2024).

**Short strangle** = sell 1 OTM call + sell 1 OTM put, same expiry. Undefined risk on both sides. Margin is SPAN + Exposure, benefiting from the two-sided offset (a strangle is margined roughly like the larger of the two naked legs plus a bit, not the sum).

**Iron condor** = short strangle + buy a further-OTM call and a further-OTM put as wings. Defined risk. Max loss = (width of the wider spread − net credit) × lot. Margin collapses to roughly the max-loss of one side, so a condor needs a *fraction* of the strangle's margin.

The Greeks of a symmetric, delta-neutral condor at entry:

| Greek | Sign | What it means for you |
|---|---|---|
| Delta | ~0 | Directionally flat *at entry only*; drifts as price moves |
| Gamma | Negative | Delta moves *against* you as price runs — the core danger |
| Theta | Positive | You earn time decay daily; peaks in the last 2–4 days |
| Vega | Negative | You profit if IV falls, lose if IV rises |

The tension is **gamma vs theta**. You are paid theta to absorb gamma risk. As expiry approaches both intensify: theta accelerates (good) but so does gamma (bad) — near expiry a short option near the money has vicious gamma, so a small move produces a large delta swing. This is why the last two days of a weekly are where careless strangle-sellers die.

**Strike selection** is usually done by delta. A common construction: sell the ~16-delta call and ~16-delta put (roughly the 1-standard-deviation strikes, implying ~68% chance price stays inside at expiry, ~84% each side individually). Wings bought 200–300 points further out on Nifty (or 500–700 on Bank Nifty). More conservative sellers use 10-delta shorts (higher win rate, smaller credit); aggressive intraday sellers push to 20–30 delta for fatter premium and more management.

Position sizing rule of thumb for a defined-risk condor: risk **1–2% of capital as max loss per condor**, and never let total short-vega across the book imply a loss greater than ~5–6% of capital on a 3-vol-point spike in India VIX.

## Worked trade

**Setup (illustrative, Nifty spot 24,600, ~9 days to weekly expiry, India VIX ≈ 15).**

We sell a symmetric iron condor around spot. ATM IV ≈ 13.5%. One standard deviation over 9 days ≈ 24,600 × 0.135 × √(9/365) ≈ 24,600 × 0.135 × 0.157 ≈ **±520 points**. So ~1-SD strikes are near 24,080 and 25,120. Round to tradable strikes.

| Leg | Strike | Action | Premium (₹) | Delta |
|---|---|---|---|---|
| Put wing | 23,800 PE | Buy | 42 | +0.09 |
| Short put | 24,100 PE | Sell | 78 | +0.17 |
| Short call | 25,100 CE | Sell | 74 | −0.16 |
| Call wing | 25,400 CE | Buy | 40 | −0.08 |

**Net credit** = (78 + 74) − (42 + 40) = **₹70 per share**.
Lot = 75 → **credit ₹5,250 per lot**.
Spread width = 300 pts each side. **Max loss** = (300 − 70) × 75 = **₹17,250 per lot**.
Max profit = ₹5,250 per lot (if 24,100–25,100 holds at expiry).
Breakevens: 24,100 − 70 = **24,030** on the downside; 25,100 + 70 = **25,170** on the upside.
Net delta ≈ (+0.09 + 0.17 − 0.16 − 0.08) = **+0.02 per share** — essentially flat. Net vega negative; net theta positive (roughly +₹550–700/day/lot early on, accelerating).

**Costs matter and India's are non-trivial.** On a condor you trade 4 legs in and (often) 4 legs out. Approximate round-trip frictions per lot:
- Brokerage: discount brokers ~₹20/order × 8 orders ≈ ₹160.
- STT: charged on the **sell side of options at ~0.1% of premium** (2026 — verify), plus STT on any in-the-money exercised long options at settlement (this is the nasty one — an ITM long option settled at expiry attracts STT on *intrinsic/settlement value*, not premium; never let long wings expire ITM without accounting for it).
- Exchange txn charges, GST (18% on brokerage + txn charges), SEBI turnover, stamp duty.

Realistically budget **₹250–450 round-trip per lot** in total frictions on a Nifty condor. Against a ₹5,250 max credit that's ~5–8% of gross — meaningful, and the reason you don't trade condors for ₹15 of edge.

**Margin:** a defined-risk 300-wide condor needs roughly the one-side max-loss as margin (~₹17,000–20,000 including exposure), so on ₹1,00,000 capital you could hold ~4–5 lots — but *don't*, because correlated tail risk stacks. The naked strangle version (short 24,100 PE + 25,100 CE, no wings) would collect more (~₹152 × 75 = ₹11,400) but demand **₹1.1–1.4 lakh SPAN+exposure per lot** and expose you to unlimited loss on a gap.

## Management

Management is where the P&L actually lives. Rules, in priority order:

**1. Profit target — take it early.** For a premium seller the marginal theta at the end is not worth the tail risk. A standard discipline: **close the whole condor at 50% of max credit.** Here that's +₹2,625/lot. At 50% captured you've realised most of the theta with the least remaining gamma; redeploy into a fresh, wider, higher-credit position. Greedy sellers holding for the last 20% repeatedly get caught by an expiry-day whip that turns a +80% winner into a max loss in one afternoon.

**2. The untested-side roll (the workhorse adjustment).** Say Nifty drifts up to 24,950 with 5 days left. The call side (25,100 CE) is now tested — its delta has grown to ~−0.34 and the position delta is now meaningfully short (say −0.11/share). The put side (24,100 PE) is now nearly worthless. **Roll the untested put spread up**: buy back the cheap 23,800/24,100 put spread and re-sell a higher put spread, e.g. 24,300/24,600, collecting fresh credit. This does two things: it books the put-side profit, and it **re-centres delta toward zero** and adds credit that widens your call-side breakeven. You've effectively followed price up. The risk: you narrow the profit tent, so if the index now reverses hard *down*, the newly-raised put side is closer to the money.

**3. Roll the tested side out/away (defensive).** If price keeps pressing the call side and it breaches, you can roll the *tested* short call up and out to the next expiry for a credit, buying time and distance. On defined-risk condors people also **roll the whole call spread up** (25,100/25,400 → 25,300/25,600) if they can do it for a net credit or scratch — but be careful: rolling a losing tested side for a debit just enlarges max loss. Golden rule: **only roll the tested side if you can do it for a credit or flat.** If it costs a debit, you're throwing good money after bad; prefer to take the defined loss.

**4. Delta-band management.** Many systematic sellers manage by a delta band rather than by price. Rule: whenever net position delta exceeds, say, **±0.25 per share (per lot)**, neutralise — roll the untested side, add a small opposite-delta spread, or buy/sell a few points of the index future to flatten. This keeps the position honest to its "neutral income" thesis and prevents a slow directional drift from becoming a directional bet you never chose.

**Scenario grid** (from our entry, condor short 24,100/25,100, credit ₹70):

| Scenario | What happens | Action |
|---|---|---|
| **Index flat, IV drops** (VIX 15→12) | Best case. Vega + theta both pay. Position at +40–60% in 3–4 days | Close at 50%, redeploy |
| **Slow drift up to 24,950** | Call side tested, delta short, still inside tent | Roll put spread up for credit; re-centre delta |
| **Sharp move to 25,180 (breaks BE)** | Call side ITM, near max loss on that side; put side worthless | Take defined loss OR roll call spread up-and-out for credit if available; do NOT add size |
| **Gap event, VIX 15→22** | Vega loss dominates even if price inside tent — mark-to-market ugly though expiry value may still be fine | If defined-risk and thesis intact, hold to theta; if naked strangle, this is where you cover a side immediately |
| **Expiry day, pinned between shorts** | Gamma maximal; pin risk | Close early; do not gamble the last ₹15 of theta against expiry-day whipsaw |

**IV up vs IV down is as important as price.** A condor can be *green on price and red on the screen* because vega repriced against you. Distinguish mark-to-market pain (vega) from terminal risk (where price is vs your strikes). If price is comfortably inside and only IV spiked, the calm move is to hold — IV mean-reverts and theta will grind it back — provided your risk is defined and financeable. A naked strangle does not give you that luxury: a vega spike balloons your MTM *and* your margin (SPAN reprices), potentially forcing a liquidation at the worst moment.

## Risk & sizing

**Max loss.** Defined-risk condor: known and capped at (width − credit) × lot = ₹17,250/lot here. This number, times the number of lots, is your true position risk — size so total condor max-loss across the book is a tolerable fraction (≤ ~10–15%) of capital, remembering multiple index condors are *correlated* (Nifty and Bank Nifty crash together).

**Naked short strangle: the tail is the whole story.** There is no cap. A 24,100/25,100 naked strangle collecting ₹152 has a downside that, on a 1,000-point gap down (a bad-news Monday), could lose ₹900+ intrinsic on the put — ~₹67,000/lot against ₹11,400 collected — a **6:1 loss vs the entire credit**, and that's not even a tail event by Bank Nifty standards. Bank Nifty has moved 3–5% intraday on RBI and global risk-off days. **This is the single most common way Indian option sellers blow up.** If you sell naked, you MUST (a) size tiny, (b) have hard stop-loss discipline (cover a side at 2–2.5x the credit received on that leg), and (c) never sell naked through a scheduled binary event.

**Margin mechanics under stress.** SPAN margin is scenario-based; when VIX spikes, the exchange widens the scan range and your margin requirement *rises* exactly when your MTM is falling. Naked sellers face margin calls and forced square-offs at the worst prices. The condor's defined risk means its margin is far more stable — a structural reason to prefer condors for anyone not running a desk with deep capital.

**Portfolio Greeks.** Aggregate across the book: total net delta (keep within a band you chose deliberately), total vega (this is your real exposure — a short-premium book is a short-vol book; know your ₹ P&L per 1-point move in India VIX), total gamma (your overnight/gap vulnerability), and total theta (your daily "salary"). A healthy income book has theta comfortably positive, vega negative but sized so a 3–4 point VIX spike is survivable, and gamma small enough that an overnight gap doesn't exceed your daily theta by more than a few multiples.

**The uncomfortable truth about the edge.** Short vol has positive expectancy *only if* you (1) sell when IV > realised (a genuine variance risk premium exists), (2) actually manage the tail, and (3) don't over-lever. Strip out any one and the negative skew eats you. The variance risk premium on Nifty is real but thin; it is easily erased by one un-cut Bank Nifty trend day per quarter.

## Pitfalls & interview-ready summary

**Pitfalls:**
- **Holding for max profit.** The last 20% of credit carries most of the gamma risk. Take 50%.
- **Rolling the tested side for a debit.** That's averaging into a loser. Only roll for credit/flat; otherwise take the defined loss.
- **Selling naked to save margin.** You're not saving risk, only capital — and converting a capped loss into an uncapped one. On Bank Nifty especially, buy the wings.
- **Ignoring vega.** A green-on-price condor can be deep red on a VIX spike; know whether your pain is terminal (price) or mark-to-market (vol).
- **Expiry-day pin gambling.** Weekly expiry gamma is savage. Close early.
- **Event blindness.** Budget, RBI policy, election counts, US CPI/FOMC — a strangle sold into these is a coin-flip, not an income trade.
- **STT on ITM longs at settlement.** Let a long wing expire ITM and you can eat surprise STT on settlement value — square off ITM legs.
- **Correlation blindness.** Three index condors are one big short-vol bet, not diversification.

**Interview-ready summary:** *An iron condor is a short strangle with defined-risk wings — short call spread plus short put spread — that harvests the variance risk premium: positive theta, negative vega, negative gamma, delta-neutral at entry. You size by max loss (width minus credit), enter when IV exceeds realised with no binary event inside the window, and manage mechanically: take profit at ~50% of credit, roll the untested side toward price to re-centre delta and add credit, roll the tested side only for a credit, keep net delta inside a chosen band, and close before expiry-day gamma. The strangle is the same trade without insurance — more credit, far less margin efficiency, and an uncapped tail that, on a Bank Nifty gap, is the classic Indian retail blow-up. The whole edge is thin and negatively skewed, so it survives only with disciplined tail management and modest leverage.*
