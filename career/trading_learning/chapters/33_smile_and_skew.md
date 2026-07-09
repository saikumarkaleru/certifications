# Chapter 33: The Volatility Smile & Skew

Black-Scholes hands you a single number — implied volatility — and asks you to believe it describes the whole option chain. One sigma, plugged into one formula, supposedly prices every strike from the deep out-of-the-money put to the far out-of-the-money call. It is a beautiful idea. It is also wrong, and the market has known it is wrong since at least the crash of October 1987.

If you actually back out the implied volatility from real Nifty option prices, strike by strike, and plot those IVs against the strike, you do not get a flat line. You get a curve. Sometimes it smiles — both wings lifted above the middle. More often, for an equity index like Nifty, it droops to the right: the low strikes (the puts) carry fat implied volatilities, and the high strikes (the calls) carry thin ones. That tilt is the **volatility skew**, and learning to read it is one of the cleanest windows a trader has into what the market is actually afraid of. This chapter is about that curve — why it exists, why equity indices lean the way they do, and what it tells you that the spot price alone never will.

## Core concepts

### The flat-vol assumption, and why reality breaks it

Recall from Chapters 19 and 20 that the Black-Scholes-Merton model assumes the underlying's returns are **lognormally distributed** with a single, constant volatility. Under that assumption, every option on Nifty — regardless of strike — should imply the *same* volatility, because they are all driven by the same underlying with the same sigma. Plot IV against strike and you should see a horizontal line.

The market disagrees. When you compute the IV implied by each traded option's actual price (the IV that, fed into Black-Scholes, reproduces the quoted premium), you find that different strikes imply *different* volatilities. The pattern is stable, repeatable, and economically meaningful. It has two canonical shapes:

- **The smile.** IV is lowest near at-the-money and rises as you move to either wing — both deep OTM puts and deep OTM calls trade at higher IV than the at-the-money options. Plotted, it looks like a smile. This shape dominates in currencies (USD/INR options often smile) and many commodities, where a big move in *either* direction is feared roughly equally.

- **The skew (or smirk).** IV rises sharply as you move *down* in strike toward the OTM puts, and falls as you move up toward the OTM calls. The left side is lifted, the right side is pressed down — a lopsided smirk. This is the shape that dominates **equity indices**, including Nifty and Bank Nifty.

![Figure: a symmetric volatility smile](figs/vol_smile.png)

The figure above shows the symmetric case: implied volatility plotted against strike, dipping to a minimum around the at-the-money level and curving up on both sides. The horizontal dashed line is what Black-Scholes naively predicts — one flat volatility for all strikes. The gap between that flat line and the real curve is the entire subject of this chapter. Each point on the curve is a *separate* IV backed out from a *separate* option price; the smile is what you get when you connect them.

### Why a smile exists at all: fat tails

The deepest reason the curve is not flat is that **real returns are not lognormal.** Lognormal returns produce thin tails — extreme moves are assumed to be vanishingly rare. But markets actually deliver "fat tails": crashes, gaps, and melt-ups happen far more often than a bell curve predicts. A 5-sigma daily move should occur roughly once every several thousand years under the normal assumption; equity markets serve one up every few years.

OTM options are pure bets on the tails — a far OTM put only pays if the market falls a long way, a far OTM call only if it rises a long way. Because the *real* probability of those large moves is higher than the model assumes, the market prices those wing options *richer* than Black-Scholes with a single ATM volatility would suggest. To make the model reproduce that richer price, you must feed it a *higher* IV. So the wings imply higher volatility than the middle — and that is the smile: the market bolting fat tails onto a thin-tailed model by raising the volatility input exactly where the model most underprices reality.

### Why equity indices skew instead of smiling

If fat tails were symmetric, indices would smile like currencies do. They do not — they skew, with the *downside* wing far more lifted than the upside. Three reinforcing forces explain why Nifty's left tail is feared more than its right.

**1. Crash fear (asymmetric tails).** Equity indices fall faster than they rise. Bull markets grind up over months; crashes happen in days — think March 2020, where Nifty lost a third of its value in a few weeks, or the gap-downs around major shocks. The probability distribution of index returns is **negatively skewed**: the left tail is longer and fatter than the right. The market knows this, so it pays up more for downside protection than for upside lottery tickets. Higher demand and higher real tail-risk on the put side both push OTM put IV above OTM call IV.

**2. The leverage effect.** When a company's stock falls, its debt stays fixed, so its equity becomes a smaller slice of a more-leveraged capital structure — and a more-leveraged equity is mechanically more volatile. Aggregated across the index, this means **volatility tends to rise as the market falls** and fall as the market rises. Spot down, vol up; spot up, vol down — a persistent negative correlation between price and volatility. Options pricing bakes this in: low strikes (which pay off precisely in the falling-market, high-vol world) deserve higher implied volatility, while high strikes (which pay off in the rising, calming world) deserve lower IV. The leverage effect *is* the skew, expressed in option prices.

**3. Persistent hedging demand (supply and demand).** This is the most practical force, and arguably the dominant one in Nifty. Large, structural players — mutual funds, portfolio managers, insurers, FIIs with long cash positions — are **permanently long the market** and permanently want crash insurance. They are natural, price-insensitive *buyers* of OTM puts as portfolio hedges, month after month. Meanwhile there is no equivalent structural buyer of OTM calls; if anything, those same long-only holders *sell* OTM calls against their holdings (covered calls, Chapter 30) to earn yield. So the order flow is lopsided: persistent buying pressure on OTM puts lifts their price (and IV), persistent selling pressure on OTM calls depresses theirs. Even setting aside any model of the true distribution, **the supply-demand imbalance alone bends the curve into a skew.** The puts are expensive because everyone wants them; the calls are cheap because everyone is selling them.

![Figure: equity-index volatility skew](figs/vol_skew.png)

The figure above shows the equity-index reality: IV is high on the left (OTM puts), slopes down through the at-the-money level, and bottoms out or flattens on the right (OTM calls). This downward-sloping smirk is the everyday shape of the Nifty and Bank Nifty option chains. Notice how different it is from the symmetric smile — the asymmetry *is* the information. The steeper that left side, the more the market is paying for crash protection.

### Reading the Nifty skew as a sentiment gauge

Because the skew is built from demand for protection, its *shape* moves with fear, and you can read it like an instrument.

- **A steep skew** (puts trading at a large IV premium over calls, the left side sharply lifted) signals **elevated crash fear**. Hedgers are scrambling for downside protection, bidding puts up. A skew that *steepens* over a few sessions — even while spot is flat or only drifting — is a warning sign: smart, hedged money is paying up for insurance, often before a visible decline. Steepening skew is one of the few leading indicators of stress in the option market.

- **A flat (or flatter) skew** signals **complacency**. When few people are bidding for puts, the left wing sags toward the calls and the curve flattens. Flat skew with low India VIX is the fingerprint of a calm, risk-on market — which is also, historically, exactly when the market is most vulnerable to a surprise.

- **The skew can flatten or even invert at the top of euphoric rallies** in individual themes, where call demand briefly outruns put demand — but for the broad index, an inverted skew (calls richer than puts) is rare and short-lived.

So there are two distinct dials on the volatility dashboard. **India VIX** (Chapter 25) tells you the *overall level* of implied volatility — how expensive options are on average. **The skew** tells you the *shape* — how that fear is distributed across strikes, and specifically how much extra the market charges for downside versus upside. A trader who watches both reads a far richer picture than one who watches spot alone: VIX is the temperature, skew is which way the wind is blowing.

### Sticky-strike vs sticky-delta: how the smile moves with spot

Here is a subtlety that trips up even experienced traders. The skew is not a static painting — it lives on the strike axis, but the spot keeps moving underneath it. When Nifty moves from 24,000 to 24,200, what happens to the IV of the 24,000 strike? The answer depends on which *regime* the market is in, and there are two idealised models.

**Sticky-strike.** Each *strike* keeps its own implied volatility as spot moves. The 24,000 option still implies, say, 14% IV whether spot is at 23,900 or 24,100; the whole IV-by-strike curve stays nailed in place while spot slides along it. In this regime, an option's *moneyness* changes as spot moves (the 24,000 strike becomes more ITM as Nifty rises) and so does the IV you read off the fixed curve at that point. Sticky-strike tends to describe **calm, range-bound markets** where traders anchor their vol quotes to specific strike levels.

**Sticky-delta (sticky-moneyness).** The *shape* of the curve travels with spot. What stays constant is the IV at a given *moneyness* (e.g., "the ATM IV" or "the 25-delta put IV"), so as spot rises, the entire smile shifts right to keep the ATM point under the new spot. In this regime the *at-the-money* option keeps the same IV regardless of where Nifty is, because "at-the-money" is always re-centred on current spot. Sticky-delta tends to describe **trending or fast markets**, and it is the more common assumption for index options over larger moves.

Why does the distinction matter? Because it changes your **effective delta.** Suppose you are long a call. Under sticky-strike, when spot rises your strike's IV is unchanged, so your P&L is roughly the textbook delta. But under sticky-delta with a downward skew, as spot rises the whole curve slides up with it — and since the curve slopes downward, the IV at your now-lower-moneyness strike *falls*. A falling IV (you are long vega) works against you, partially offsetting your delta gain. The reverse happens on the way down: as spot falls, the curve slides down, the IV at your strike *rises*, and the vega gain cushions your delta loss. The net effect is that the skew makes your real, vol-adjusted delta **different from the Black-Scholes delta** — and getting this wrong is how delta-hedged books quietly bleed. Most index desks run somewhere between the two regimes and adjust their delta hedges for the skew dynamics rather than trusting the raw model delta.

### Practical implications: the wings are mispriced by a flat model

Everything above converges on one trading reality: **a single-volatility (flat-vol) model misprices the wings.** If you price a Nifty option chain with one ATM IV plugged into Black-Scholes for every strike, you will *underprice* the OTM puts (the model's thin left tail ignores crash risk and hedging demand) and *overprice* the OTM calls relative to where they actually trade. Any strategy built on that flat assumption is systematically wrong at exactly the strikes where the wings live.

The most important consequence for a retail seller: **OTM puts on Nifty look gloriously expensive, and there is a reason they are expensive.** The fat IV on a far OTM put is not a free gift the market left on the table; it is the price of insuring against the exact crash that put pays off in. Selling that put harvests the skew premium — and most months it works, because most months there is no crash. But the months it fails are the months the market gaps down, IV explodes (the leverage effect drives vol up precisely as you are losing on direction), and the very skew that made the put look rich now makes your loss far larger than a flat model predicted. **You are being paid the skew premium to underwrite tail risk.** That can be a genuine, professional edge — insurers earn it for a living — but only if you size for the tail, not for the average month. Selling the rich downside wing without respecting why it is rich is one of the classic ways to blow up an account.

## Worked example (₹, Nifty)

Let us read a real-shaped Nifty skew off the chain. Suppose Nifty spot is **24,000**, weekly expiry, and India VIX is around 14%. You pull the option chain and back out the implied volatility for each strike. A typical equity-index skew might look like this:

| Strike | Moneyness | Implied Volatility |
|--------|-----------|--------------------|
| 23,000 | Far OTM put | 19.5% |
| 23,500 | OTM put | 16.0% |
| 23,800 | Near OTM put | 14.8% |
| 24,000 | At-the-money | 14.0% |
| 24,200 | Near OTM call | 13.3% |
| 24,500 | OTM call | 12.6% |
| 25,000 | Far OTM call | 12.0% |

**Step 1 — Confirm the shape.** Read the IV column top to bottom. It falls monotonically from 19.5% on the far OTM put down to 12.0% on the far OTM call, passing through 14.0% at-the-money. That downward slope *is* the skew: the puts imply higher volatility than the calls. Plot it and you would see the left-lifted smirk of `vol_skew.png`, not a flat line and not a symmetric smile.

**Step 2 — Quantify the skew.** A common single-number summary is the IV difference between a downside strike and an equidistant upside strike. Here the 23,500 put (500 points OTM) implies 16.0% while the 24,500 call (also 500 points OTM) implies 12.6%. The skew is:

`skew ≈ put-wing IV - call-wing IV = 16.0% - 12.6% = 3.4 percentage points`

That 3.4-point gap is the market's premium for downside over upside at this width. If, over the next two sessions, that gap widened to 5 or 6 points while spot barely moved, the skew is **steepening** — fear is rising, hedgers are bidding puts harder — and you would read that as a caution flag even before any fall shows up in the index.

**Step 3 — Price the mispricing of a flat model.** Suppose a naive trader prices the whole chain at the single ATM IV of 14.0%. For the 23,500 put, they are using 14.0% when the market trades it at 16.0% — they would compute a premium that is *too low*. Say that put has a vega of about ₹5 per IV point. The flat-vol model undervalues it by roughly:

`mispricing ≈ vega * IV gap = 5 * (16.0 - 14.0) = 5 * 2 = ₹10 per unit`

So the flat model thinks the 23,500 put is worth about ₹10 less than its market price. A trader who believes the flat model would conclude the put is "overpriced" and happily sell it — without realising they are simply selling crash insurance at the market's fair (skew-adjusted) rate and pocketing the skew premium, tail risk and all.

**Step 4 — The sticky-delta delta adjustment.** You are long the 24,000 call. Nifty rallies 200 points to 24,200. Under sticky-delta the curve slides right, so the IV *at your strike* drifts down from 14.0% toward the old 24,200 reading of ~13.3% — a ~0.7-point IV drop. With a call vega of about ₹8, that is a vega drag of `8 * 0.7 ≈ ₹5.6` working *against* your delta gain. Your realised, skew-adjusted profit is a touch less than the raw delta promised — small here, but across thousands of lots on a delta-hedged book, ignoring it is how the skew quietly eats your edge.

## Common mistakes / risk note

- **Believing the one-IV-fits-all picture.** Beginners read a single "IV" off a generic quote and assume it applies to every strike. It does not. Each strike has its own implied volatility; the OTM puts on Nifty almost always imply meaningfully higher vol than the OTM calls. Pricing or comparing options without respecting the skew leads to systematically wrong valuations at the wings.

- **Selling "expensive" OTM puts without respecting the tail.** The rich IV on a far OTM Nifty put is compensation for real crash risk and relentless hedging demand — not a market error. Selling it harvests the skew premium most months, but in a gap-down the loss is amplified by both direction *and* a vol spike (leverage effect), exactly when you can least afford it. Size for the crash, not the average week; naked short puts carry large, sometimes account-ending, risk.

- **Confusing the smile with the skew.** A symmetric smile (both wings up) and a downward skew (left wing up, right wing down) carry different information. Currencies smile; equity indices skew. Expecting Nifty to behave like a symmetric smile will mislead you about which wing is rich.

- **Ignoring how the smile moves with spot.** Assuming the textbook Black-Scholes delta is your true delta ignores sticky-strike vs sticky-delta dynamics. Under a downward skew in a sticky-delta regime, rallies drag your strike's IV down and sell-offs push it up, shifting your effective delta away from the model number. Delta-hedged positions that ignore this leak money.

- **Reading the level (VIX) but not the shape (skew).** India VIX tells you how expensive options are on average; the skew tells you how that fear is distributed and whether it is concentrated on the downside. A flat skew with low VIX (complacency) and a steepening skew with rising VIX (fear building) are very different worlds. Watch both dials.

## Key takeaways

- Black-Scholes assumes one constant volatility for all strikes, predicting a **flat** IV-vs-strike line. Real markets show a **curve** — proof the single-volatility assumption is wrong.
- Plotting IV against strike gives a **smile** (both wings up, symmetric — common in currencies) or, for equity indices, a downward **skew/smirk** (OTM puts richer than OTM calls).
- The smile exists because real returns have **fat tails**; the equity-index **skew** exists because of **crash fear** (negatively skewed returns), the **leverage effect** (vol rises as the market falls), and **persistent hedging demand** for OTM puts.
- **Read the Nifty skew as sentiment**: a steep/steepening skew signals rising crash fear (often a leading warning); a flat skew signals complacency. VIX is the level of fear, skew is its distribution across strikes.
- **Sticky-strike** (each strike keeps its IV; calm markets) vs **sticky-delta** (the curve travels with spot; trending markets) changes your effective, vol-adjusted delta away from the raw Black-Scholes number.
- A **flat-vol model misprices the wings** — it underprices OTM puts and overprices OTM calls. Selling rich OTM puts harvests the **skew premium** but underwrites real tail risk; size for the crash.

## Practice problems

1. **Spot the shape.** You back out IVs for three Nifty strikes around spot 24,000: the 23,500 put implies 16%, the 24,000 ATM implies 14%, and the 24,500 call implies 12.5%. Is this a smile or a skew? What single fact about equity-index returns most directly explains the shape?

2. **Why so lopsided (conceptual).** Currency options (USD/INR) tend to show a roughly symmetric smile, while Nifty shows a downward skew. Give two reasons equity indices skew toward the puts that do not apply equally to currencies.

3. **Quantify and interpret (numeric).** On Monday the Nifty 23,500 put implies 15.5% and the 24,500 call implies 12.5%. On Wednesday, with spot essentially unchanged, the put implies 18.0% and the call implies 12.0%. Compute the skew (put-wing minus call-wing IV) on each day. What is the skew doing, and what does it suggest about market sentiment?

4. **Flat model mispricing (numeric).** A trader prices the entire Nifty chain at one ATM IV of 14%. The market trades the 23,000 put at an IV of 19%. If that put has a vega of about ₹4 per IV point, by roughly how much does the flat-vol model misprice it, and in which direction (under or over)?

5. **Sticky-delta delta (conceptual + numeric).** You are long a Nifty 24,000 call in a sticky-delta regime with a downward skew. Nifty falls 150 points. Qualitatively, does the IV at your strike rise or fall, and does that vega effect help or hurt your (losing) position? If the IV at your strike rises 0.6 points and your vega is ₹8, estimate the vega P&L.

6. **The seller's dilemma.** A far OTM Nifty put implies 20% IV while the ATM implies 13%. A friend says, "That put is obviously overpriced — 20% is way too high, I'm going to sell a bunch of them for easy premium." What is the flaw in calling it "overpriced," and what is the real risk being taken on?

## Solutions

1. **A skew.** The IV falls monotonically from 16% (OTM put) through 14% (ATM) to 12.5% (OTM call) — the left wing is lifted and the right is pressed down, the classic downward equity-index smirk, not a symmetric smile. The fact that most directly explains it: equity-index returns are **negatively skewed** — markets crash down faster than they rally up, so the left (downside) tail is fatter, and the market charges more implied volatility for the puts that pay off in those crashes.

2. Two equity-specific forces (any two): (a) **Crash fear / negative skew** — indices fall far faster than they rise (crashes happen in days, rallies grind over months), so the downside tail is fatter and OTM puts command higher IV; currencies can move sharply in either direction, so their tails are more symmetric. (b) **The leverage effect** — as equity prices fall, firms become more leveraged and their equity more volatile, creating a persistent negative price-vol correlation that lifts low-strike IV; this mechanism is specific to leveraged equity, not currencies. (c) **Structural hedging demand** — long-only funds and FIIs permanently buy OTM index puts for crash insurance while selling OTM calls for yield, a lopsided order flow that bends the curve; currency markets have buyers and sellers on both sides more evenly.

3. Monday skew = `15.5 - 12.5 = 3.0` points. Wednesday skew = `18.0 - 12.0 = 6.0` points. The skew has **steepened** sharply — it doubled — even though spot barely moved. This means hedgers are aggressively bidding up downside protection (puts) relative to calls: **crash fear is rising**. A steepening skew with flat spot is a classic leading warning sign that hedged money is paying up for insurance, and a trader would treat it as a caution flag about building downside risk, even before any visible decline.

4. The market trades the put at 19% IV; the flat model uses 14% — a gap of `19 - 14 = 5` IV points. With vega ≈ ₹4 per point, the mispricing is about `4 * 5 = ₹20` per unit. The flat-vol model **underprices** the OTM put by roughly ₹20 (it ignores the skew's fat downside, so it values the put too cheaply). A trader trusting the flat model would wrongly think the put is overpriced and sell it — actually just selling crash insurance at the market's fair, skew-adjusted rate.

5. Under sticky-delta with a downward skew, when spot **falls** the whole IV curve slides down with it; because the curve slopes downward, the IV at your (now higher-moneyness) strike **rises**. You are long the call, hence **long vega**, so a rising IV is a **gain** that partially cushions the delta loss from the falling spot. Vega P&L ≈ `vega * IV change = 8 * 0.6 = +₹4.8` per unit. So the vega effect *helps* your losing position — your skew-adjusted delta loss is a bit smaller than the raw Black-Scholes delta would predict.

6. The flaw: "overpriced" assumes every strike should imply the same volatility (the flat-vol fallacy). It should not. A far OTM Nifty put *correctly* trades at a higher IV than the ATM because of the skew — fat downside tails, the leverage effect, and relentless hedging demand. The 20% is the market's fair price for **crash insurance**, not an error. The real risk in selling it: you are **underwriting tail risk**. Most months no crash comes and you keep the premium, but in a gap-down you lose on direction *and* the IV spikes further (leverage effect) precisely as you are losing — so the loss is amplified far beyond what the rich premium suggests. The skew premium is real compensation, but it must be sized for the crash, not the average week; naked short puts carry large, potentially account-ending risk.
