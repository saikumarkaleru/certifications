# Ratio Spreads & Backspreads in Practice

*India F&O supplement — written July 2026. STT (~0.1% on option sells), SEBI expiry/lot-size framework and SPAN+Exposure margining reflect 2026 as understood at time of writing. **Verify current lot sizes, expiry days and STT with NSE/SEBI/your broker before trading.***

## The idea

A ratio spread and a backspread are the same skeleton viewed from opposite ends. In both you trade an **unequal number of long and short options** at two strikes on one side of the market. The ratio determines everything:

- **Ratio spread (front-ratio):** you are *net short* options — e.g. buy 1 call, sell 2 further-OTM calls (1×2). You collect premium (often for a credit or near-zero cost), you're **short vega, short gamma, positive theta**, and you have an **unlimited-risk tail** on the naked extra short. It's a "I think it drifts toward that strike but not far past it" trade.
- **Backspread (ratio backspread):** you are *net long* options — e.g. sell 1 call, buy 2 further-OTM calls (1×2 the other way). You pay a debit (or structure for a small credit), you're **long vega, long gamma, negative theta**, and you have **unlimited profit** on a big move in your favour with a *defined, often small, loss* if nothing happens. It's a "I think a big move is coming, and I want to be long convexity cheaply — or free" trade.

So the two are mirror bets on **realised movement and on vol**. The ratio spread sells convexity and skew; the backspread buys them. Both exploit the **volatility skew** — the fact that OTM puts (and, in some indices, OTM calls) trade at different IVs than ATM — which lets you finance the extra long or extra short cheaply.

Where do these earn their keep for an Indian F&O trader? The **put ratio backspread** is a genuinely useful crash-insurance-with-a-kicker structure: because Nifty/Bank Nifty put skew is steep (downside puts are expensive), you can *sell one expensive near-ATM put and buy two cheaper further-OTM puts* — often for a net credit — giving you a position that makes money on a violent down-move, loses a bounded amount in a moderate drift down, and keeps the credit if the market rises. That's a rare "get paid to hold crash insurance" profile, and it's structurally financed by the very skew that makes naked put-selling dangerous.

The **call ratio spread** (buy 1, sell 2 higher calls) is the classic "I'm mildly bullish but think upside is capped near resistance" income trade — you profit most if the index drifts up to the short strike, but the naked extra short call means a runaway rally hurts. Given Indian indices *can* gap up on global risk-on or a surprise policy, that upside tail is real and must be respected.

## The mechanics

**Call ratio spread 1×2 (net short):**
- Buy 1 call at K1 (lower).
- Sell 2 calls at K2 (higher).
- Usually structured for a **credit or zero cost**.
- Max profit at K2 at expiry = (K2 − K1) + net credit.
- **Upside is unlimited-loss** above the upper breakeven (one of the two short calls is uncovered).
- Downside: if it all expires worthless you keep the credit (or lose the small debit).

**Put ratio backspread 1×2 (net long puts):**
- Sell 1 put at K1 (higher, near-ATM, expensive).
- Buy 2 puts at K2 (lower, cheaper).
- Structured for **credit / zero / small debit** thanks to put skew.
- **Big down-move = large, escalating profit** (you're net long 1 extra put, and gamma builds as you fall).
- **Worst case is a bounded loss** in the "valley" — price finishing right at K2 — where the short K1 put is deep ITM and your two K2 puts are just worthless/ATM.
- **Up-move = keep the credit.**

Greeks contrast:

| | Front-ratio (net short) | Backspread (net long) |
|---|---|---|
| Net options | Short | Long |
| Delta | Directional toward the tent | Directional toward the big move |
| Gamma | **Negative** | **Positive** |
| Vega | **Negative** | **Positive** |
| Theta | **Positive** (you're paid to wait) | **Negative** (you bleed waiting) |
| Risk tail | **Unlimited** (naked extra short) | **Defined** (max loss in the valley) |
| Best when | Drift to short strike, IV falls | Big move + IV rises |

**The valley (backspread) and the cliff (ratio spread)** are the shapes to burn into memory. A 1×2 put backspread's payoff, left-to-right (low price → high price): high profit on the far left (deep down), sloping down to a **loss valley at the long strike K2**, then recovering to a flat small-credit profit on the right (up). A 1×2 call ratio spread: flat small credit on the left, rising to a **peak at the short strike K2**, then falling off a **cliff into unlimited loss** on the right.

**Margin.** The naked extra short in a front-ratio spread means **SPAN+Exposure margin like a short option** — this is *not* a defined-risk trade and the exchange margins it accordingly. A backspread, being net long with the short leg covered, is far lighter on margin (roughly the net debit plus a modest short-leg component). This asymmetry matters: ratio spreads tie up real margin *and* carry tail risk; backspreads are capital-light insurance.

**Skew is the financing.** The reason a put backspread can be a credit is that the one near-ATM put you sell is richer (higher IV) than the two OTM puts you buy — steep put skew means you sell high-IV and buy lower-IV. If skew ever flattens, the same structure costs a debit. Always check: *am I being paid by the skew, or am I paying through it?*

## Worked trade

**Trade A — Put ratio backspread on Bank Nifty (crash kicker for a credit).**

Bank Nifty spot 52,000, monthly expiry ~20 days out (Bank Nifty is monthly-only post-rationalisation — verify). India VIX ≈ 14, put skew steep. Lot = 35.

| Leg | Strike | Action | IV | Premium (₹) |
|---|---|---|---|---|
| Short put | 51,500 PE | Sell 1 | 16.5% | 520 |
| Long put | 50,500 PE | Buy 2 | 15.0% | 300 each = 600 |

**Net cost** = 520 − 600 = **−₹80 per share → a ₹80 debit** (×35 = ₹2,800/lot). (If skew were steeper you might do this flat or for a small credit; here it's a modest debit.)

Position: net **long 1 put** (2 bought − 1 sold), strike-shifted lower.
- **If Bank Nifty crashes to 49,000:** the two 50,500 puts are ₹1,500 ITM each = ₹3,000; the short 51,500 put is ₹2,500 ITM = −₹2,500; net intrinsic = ₹500/share ≈ **₹17,500/lot profit**, and it accelerates the further it falls (you own an extra put — gamma compounds). This is the crash kicker.
- **If Bank Nifty rises / stays above 51,500:** all puts expire worthless; you lose the ₹80 debit = **₹2,800/lot** (max loss on the upside is just the debit).
- **The valley — worst case — is price finishing right at 50,500:** short 51,500 put is ₹1,000 ITM = −₹1,000; both long 50,500 puts worthless; loss = ₹1,000/share − ... net **max loss ≈ (K1−K2) + debit = ₹1,000 + ₹80 = ₹1,080/share ≈ ₹37,800/lot**. *This* is the real risk of the backspread — a controlled drift down to exactly the long strike. It's bounded and known, but it's the largest number in the trade.

Greeks at entry: net delta slightly negative (bearish lean), **gamma positive**, **vega positive** (you *want* a vol spike — and crashes come with vol spikes, so vega and delta reinforce on the downside), **theta negative** (~−₹40/share/lot per day — you pay to wait).

**Trade B — Call ratio spread on Nifty (capped-upside income).**

Nifty 24,600, weekly expiry 7 days, VIX 12, mildly bullish but 25,000 is stiff resistance. Lot 75.

| Leg | Strike | Action | Premium (₹) |
|---|---|---|---|
| Long call | 24,700 CE | Buy 1 | 150 |
| Short call | 25,000 CE | Sell 2 | 82 each = 164 |

**Net credit** = 164 − 150 = **₹14/share → ₹1,050/lot credit.**
- **Max profit at 25,000 at expiry** = (25,000 − 24,700) + 14 = ₹314/share ≈ **₹23,550/lot.**
- **Downside:** below 24,700 everything expires worthless — keep the ₹14 credit (₹1,050/lot). No loss on the downside beyond zero (you got a credit).
- **Upper breakeven** = 25,000 + max-profit-per-share = 25,000 + 314 = **25,314**. Above this, the one naked short call runs **unlimited loss** — a 400-point Nifty rally to 25,700 loses ~₹386/share on the naked short net of the tent ≈ **−₹29,000/lot and climbing.**

Greeks: positive theta, negative gamma, negative vega, delta positive up to K2 then flipping sharply negative past it. **Costs:** ~₹250–400/lot round trip; STT on the two sold calls (small on premium) — but beware the **naked short call settling ITM** on a rally (STT on settlement value + the loss itself).

## Management

**Backspread management (Trade A):**

**1. If the move comes fast (your thesis hits).** Bank Nifty gaps down, VIX spikes — vega and gamma both pay. Don't be greedy: a backspread's profit is theoretically unlimited but the **valley risk re-emerges if price bounces back up to K2**. Rule: once the position is deep in profit, **roll the long strikes down** (take profit on the 50,500 puts, buy lower ones) to lock gains and re-establish a fresh crash kicker further out, or simply take profit on part and let a runner ride.

**2. If price drifts slowly toward the valley (K2).** This is the danger — slow bleed into max loss with theta working against you. If Bank Nifty is grinding toward 50,500 with time left, **close or restructure before you sit in the valley at expiry**. One fix: buy back the short K1 put (removing the escalating-loss leg) and hold the two long puts as a directional bet, or roll the whole structure down and out.

**3. If nothing happens (price rises/flat).** You lose the debit slowly to theta. Decide up front how long you'll finance the insurance — a backspread is a *dated* bet on a move; if the catalyst window passes, cut it and stop paying theta.

**Ratio spread management (Trade B) — the tail is the whole job:**

**1. The naked short is the enemy.** The single most important management rule: **define, before entry, the price at which you neutralise the naked short call.** E.g. "if Nifty trades 25,150 (approaching upper breakeven), I buy back one short call, converting the 1×2 into a 1×1 vertical (defined risk)." This caps the tail at the cost of the premium paid — cheap insurance against the blow-up.

**2. Roll up-and-out on a rally.** If price rises toward K2 early and you're still bullish, roll the short calls up (25,000 → 25,300) for a credit, widening the tent and pushing the cliff further away.

**3. Take profit near the peak.** Max profit sits exactly at K2 at expiry — a knife-edge you rarely hit precisely, and holding to expiry means sitting on the cliff-edge with expiry gamma. Take profit at 50–70% well before expiry; don't gamble the naked short through expiry day.

**Scenario grid:**

| Scenario | Ratio spread (net short calls) | Put backspread (net long puts) |
|---|---|---|
| **Big move in thesis direction** | Bad (naked short) — neutralise! | Great — roll longs down, bank profit |
| **Drift to short/long strike** | Best (peak at K2) — take profit | Worst (valley at K2) — restructure out |
| **Nothing happens (flat)** | Good — keep credit | Bad — bleed theta, cut if catalyst gone |
| **IV spikes** | Hurts (short vega) | Helps (long vega) |
| **IV crushes** | Helps (short vega) | Hurts (long vega) |

## Risk & sizing

**Ratio (front) spread — respect the unlimited tail.** The naked extra short means max loss is theoretically unlimited (calls) or very large (puts). **Never size a ratio spread as if it were the small credit you collected.** Size it by the loss at a *plausible stress move* — e.g. "what do I lose if Nifty gaps +2%?" — and keep that within your per-trade risk budget. Because it carries naked-short margin, it also ties up real SPAN. Treat it as a naked-short position with a hedge, not as a defined-risk income trade.

**Backspread — bounded loss, but know the valley.** Max loss is defined and occurs at the long strike at expiry (Trade A: ~₹37,800/lot). Size so that valley loss × lots is within budget. The upside/downside tail is *in your favour*, and the position is **long vega** — a natural portfolio hedge. A backspread is one of the few structures that *makes money when everything else in a long-biased book is crashing*, which is exactly its portfolio value.

**Portfolio Greeks and pairing.** These two are natural complements. A book that sells premium (condors, ratio spreads) is short vega/short gamma and vulnerable to crashes; overlaying a **put backspread as a financed tail hedge** converts some of that fragility into anti-fragility for a small carry cost. Consciously: run your income structures for the 90% of quiet days, and hold a backspread or two so the 10% crash day pays you instead of ruining you. Track aggregate delta, and especially aggregate gamma and vega — the ratio spread's *negative* gamma and the backspread's *positive* gamma partly offset, which is the point.

**The honest risk statement.** The ratio spread is a **negatively-skewed** trade dressed up as free income — most of the time you collect a small credit; occasionally the naked short detonates. It is *the* structure where undisciplined traders confuse "high win rate" with "positive expectancy" and get carried out on a gap. The backspread is **positively-skewed** — you pay a little most of the time and get a large payoff rarely — which is psychologically hard (a string of small losses) but is the correct shape for insurance and for betting on rare violent moves that Indian indices genuinely produce (RBI shocks, global risk-off, election surprises).

## Pitfalls & interview-ready summary

**Pitfalls:**
- **Sizing a ratio spread by its credit, not its tail.** The naked short can lose many multiples of the credit. Size by stress-move loss; pre-commit to a neutralisation price.
- **Holding a ratio spread's naked short through expiry day.** Expiry gamma on a naked short is how accounts vaporise. Take profit early.
- **Buying a backspread when skew makes it a debit.** If skew is flat, you're paying full price for the extra long — check that the skew is financing you.
- **Sitting in the backspread's valley.** Max loss is a slow drift to the long strike; restructure out before expiry if price is heading there.
- **Ignoring vega direction.** Ratio spread is short vega (hurt by vol spikes, which often accompany the very move that threatens the naked short — a double-whammy); backspread is long vega (helped by the spike). Know which side of vol you're on.
- **STT/settlement on ITM naked shorts.** A ratio spread's naked short settling ITM brings both the loss and STT on settlement value.
- **Treating either as "neutral".** Both are directional *and* convexity/vol bets — not delta-neutral income.

**Interview-ready summary:** *Ratio spreads and backspreads are the same two-strike, unequal-quantity skeleton read in opposite directions. A front-ratio spread (e.g. buy 1, sell 2 further-OTM) is net short options — positive theta, negative gamma and vega, often opened for a credit, with a peak profit at the short strike and an unlimited-loss cliff beyond it; you manage it by pre-committing to neutralise the naked short at a defined price and taking profit before expiry gamma. A ratio backspread (sell 1, buy 2 further-OTM) is net long options — negative theta, positive gamma and vega, financed by the vol skew for a credit or small debit, with a defined worst-case loss in the "valley" at the long strike and unlimited profit on a big move. In India the put backspread is especially useful: steep Nifty/Bank Nifty put skew lets you hold a crash kicker for near-zero carry, and its long-vega, long-gamma profile makes money exactly when a short-premium book is bleeding — so the two structures are natural portfolio complements. The ratio spread is negatively skewed (respect the tail and its naked-short margin); the backspread is positively skewed (insurance you must be willing to pay small losses to hold).*
