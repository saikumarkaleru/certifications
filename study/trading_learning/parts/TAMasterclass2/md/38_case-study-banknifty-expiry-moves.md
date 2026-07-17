# Case Studies: Bank Nifty Expiry-Week Moves

Bank Nifty is the trader's index. Where the Nifty 50 grinds, Bank Nifty *lunges* — a beta of roughly 1.2 to 1.5 on the broad market, dominated by a handful of heavyweight private and public-sector lenders (HDFC Bank, ICICI Bank, SBI, Axis, Kotak) whose combined weight makes the index swing hundreds of points on a single credit-policy headline or a large block deal. Nowhere is this personality more vivid than in the final days before weekly and monthly expiry, when the mechanics of options — gamma, theta decay, open-interest walls, max-pain gravitation and the frantic unwinding or rolling of positions — layer a second, purely structural force on top of the ordinary price action. Understanding expiry-week behaviour is not a nicety for the Bank Nifty trader; it is the core edge.

This chapter dissects three reconstructed expiry-week episodes: a pin-to-max-pain grind, an expiry-day trend-day breakout, and a gamma-squeeze reversal. All levels are **approximate reconstructions** for teaching. The Bank Nifty expiry cadence assumed here is the monthly-expiry structure that anchors the largest open interest; the same logic scales to whichever weekly cadence is live, but the biggest, cleanest effects cluster around the monthly expiry where OI is deepest. Verify every strike, level and OI figure on your own option chain before trading.

## Why expiry weeks behave differently

An ordinary trading day is a contest between buyers and sellers of the underlying. An expiry week adds a third player whose behaviour is *mechanical rather than directional*: the options market-maker who is short gamma and must hedge. As expiry approaches and time value bleeds out, the gamma of at-the-money options explodes. Market-makers who have sold those options must buy the underlying when it rises and sell when it falls to stay delta-neutral — or, if they are *long* gamma, do the opposite. This hedging flow can either *pin* the index to a heavy strike (short-gamma dealers suppressing volatility) or *amplify* a move into a runaway trend (when a big level breaks and dealers must chase). Reading which regime you are in is the whole game.

Three concepts recur throughout:

- **Max pain**: the strike at which the largest rupee value of options expires worthless, i.e. where option *buyers* lose the most and *sellers* keep the most premium. Bank Nifty has a well-documented tendency to gravitate toward this zone into expiry, because the net-short options community has both the incentive and, via hedging, the mechanical means to nudge it there in quiet conditions.
- **OI walls**: strikes with unusually large open interest. A heavy call OI strike acts as resistance (call sellers defend it); a heavy put OI strike acts as support (put sellers defend it). These are the "magnets and walls" of the expiry chart.
- **Gamma flip**: the price level above which dealers are long gamma (dampening moves) and below which they are short gamma (amplifying moves), or vice versa. Crossing it changes the market's entire character in minutes.

## Case Study 1 — The pin to max-pain (Bank Nifty ~48,000 zone)

### Context

Set this in a quiet expiry week with no major scheduled event — no RBI policy, no bank earnings cluster, VIX subdued. Bank Nifty had drifted into expiry week trading around 48,100. The option chain told a clear story: the 48,000 put and the 48,000 call both carried the heaviest OI on their respective sides, with 47,500 put and 48,500 call forming the next walls. Max pain computed to almost exactly 48,000. This is the textbook pin setup — a fat straddle strike with dealers short gamma around it, and no catalyst to force a breakout.

### The setup

When max pain, the heaviest call wall and the heaviest put wall all cluster at the *same* strike in a low-volatility, no-catalyst week, the highest-probability play is not directional — it is a *fade the extremes* range trade, or better, a short-premium options structure that profits from the pin itself.

| Element | Value (approx) |
|---|---|
| Instrument | Bank Nifty (fade extremes intraday, or short straddle/iron condor into expiry) |
| Regime | Low VIX, no catalyst, max-pain = 48,000 = fattest straddle |
| Upper wall | 48,500 (heavy call OI) |
| Lower wall | 47,500 (heavy put OI) |
| Range play | Sell rallies toward 48,400, buy dips toward 47,600 |
| Stop | 15-min close beyond the defended wall (>48,550 / <47,450) |
| Target | Reversion toward 48,000 |

### The trade, bar by bar

On Tuesday the index poked up to 48,380, right into the underside of the 48,500 call wall. Intraday OI data showed call *writing* increasing at 48,500 — sellers stepping in to defend the wall. That is the fade signal: short near 48,400 with a stop on a 15-minute close above 48,550. The index rolled over and drifted back to 48,050 by close — a clean reversion trade of roughly 330 points.

Wednesday it dipped to 47,620, into the 47,500 put wall, where put writing picked up (put sellers defending). Long near 47,650, stop below 47,450. It bounced back toward 48,000. The pin was working exactly as the chain predicted: every excursion toward a wall was rejected, and the index kept getting pulled back toward 48,000.

For the options trader, the cleaner expression was a short iron condor — sell the 48,500 call and 47,500 put, buy the 48,700 call and 47,300 put as protection — collecting premium that decayed rapidly as expiry approached and the index stayed pinned. Theta was the tailwind; the defended walls were the risk boundaries.

### The outcome

Expiry Thursday opened near 47,950 and chopped in a tight 150-point band all day, settling at 48,010 — within a whisker of max pain. The directional fades netted roughly 300 points each; the iron condor expired near its maximum profit as both short strikes finished out-of-the-money. Everyone who bought a straddle that week hoping for a "big expiry move" lost their premium to theta.

### The lesson

**In a no-catalyst week with max pain and fat walls aligned, the market wants to pin — trade the reversion, not a breakout.** The mechanical edge is that dealers short gamma actively suppress volatility, and the net-short options community defends the walls. But the discipline is in the stop: a pin is a *probabilistic* tendency, not a law. If a 15-minute close breaks decisively through a defended wall on volume, the pin has failed — often because a catalyst appeared — and you must exit immediately, because a failed pin frequently becomes the trend-day of Case Study 2. Never marry the range.

## Case Study 2 — The expiry-day trend-day breakout (Bank Nifty ~44,800 → ~45,900)

### Context

The opposite regime. Set this on a monthly expiry Thursday that coincided with a *catalyst* — say a stronger-than-expected banking-sector cue, a positive surprise in a heavyweight's results the prior evening, or a supportive global open. Bank Nifty had been coiled in a tight 44,600–44,900 range for three sessions, with heavy call OI stacked at 45,000 — a wall that had capped every rally. The overnight cue was bullish and the index was indicated to open near 44,950, right underneath the 45,000 wall.

### The setup

An expiry day is the single most dangerous day to be short gamma. If a heavy call wall breaks *on expiry day*, the dealers who sold those 45,000 calls suddenly face exploding delta with hours to go — they must buy the underlying aggressively to hedge, which drives price higher, which increases the calls' delta further, which forces more buying. This reflexive loop is the **gamma squeeze**, and it produces the violent one-directional "trend days" that make expiry-day Bank Nifty legendary.

| Element | Value (approx) |
|---|---|
| Instrument | Bank Nifty (long via futures or long ATM/slightly-OTM calls) |
| Trigger | 15-min close and sustained trade above 45,050 (call-wall break) |
| Stop | Back below 44,850 (below the range and reclaimed wall) |
| Initial risk | ~200 points |
| Target | Next OI wall (45,500), then trail; stretch to 45,900 |
| Regime | Expiry day, bullish catalyst, call wall breaking → short-gamma squeeze |

### The trade, bar by bar

The index opened at 44,960, pressed the 45,000 wall in the first thirty minutes, and — crucially — the option chain showed call *unwinding* at 45,000 (sellers buying back their short calls) rather than fresh writing. That is the tell: the defenders were capitulating, not reinforcing. On the 15-minute close above 45,050 the long triggered. Because it was expiry day with the wall breaking, the position was expressed with long slightly-OTM calls (45,100 strike) to capture the convexity of the squeeze — though a futures long with a hard stop was the lower-risk expression.

What followed was textbook. As price pushed to 45,150, dealers short the 45,000 and 45,100 calls were forced to buy futures to hedge their ballooning delta. That buying lifted price to 45,300, forcing more hedging, lifting it to 45,500 — the next wall — where a brief pause occurred as some fresh call writing appeared. But the momentum and the catalyst overwhelmed it; 45,500 broke and the squeeze extended to 45,750. Each leg was faster than the last, the hallmark of reflexive gamma buying rather than ordinary directional demand.

The options position was now deep in the money with delta near 0.9 and had multiplied several times over from its morning premium. The trailing discipline for a squeeze is aggressive: on expiry day the move can reverse just as violently once the hedging is exhausted, so the stop was trailed to just below each new 15-minute higher-low.

### The outcome

The move stalled near 45,900 in the final hour as the squeeze exhausted itself — every dealer who needed to hedge had hedged, and fresh buyers dried up. A 15-minute close back below 45,720 triggered the trailing exit. Futures captured roughly 45,700 − 45,050 = **650 points** on a 200-point risk (~3.25R). The long calls did far better in percentage terms because their delta expanded from ~0.4 at entry to ~0.9, and the collapsing time value on expiry day was more than offset by the intrinsic gains — though this is precisely the double-edged sword: had the breakout failed, those same calls would have decayed toward zero by the close.

### The lesson

**When a heavy call wall breaks on expiry day with a catalyst and the sellers are unwinding rather than reinforcing, get long and let the gamma squeeze work — but trail tightly, because expiry-day moves exhaust and reverse fast.** The single most important read was distinguishing *fresh writing* (wall being defended → fade it, Case Study 1) from *unwinding* (wall being abandoned → ride the break, Case Study 2). Same chart level, opposite trades, and the option chain's OI change is what tells them apart. Note the risk asymmetry of expressing this with long options on expiry day: enormous convexity if right, near-total loss if wrong, so position size must be small and the stop mechanical.

## Case Study 3 — The gamma-flip reversal (Bank Nifty ~46,200 fake-down, then squeeze up)

### Context

The most treacherous expiry pattern is the false breakdown that reverses into a squeeze — a "bear trap" engineered by the option structure. Set this mid-expiry-week with Bank Nifty around 46,300, a heavy put wall at 46,000 that had held for days, and a large concentration of put OI just below at 45,800. The index had been weak into the session on a soft global cue, and by midday it was probing 46,050, threatening the 46,000 put wall.

### The setup

Here the dealer positioning created a *gamma flip* near 46,000. Above it, dealers were long gamma and dampening moves; a decisive break below would flip them short gamma, and their hedging would briefly accelerate the fall — but the very heavy put OI at 46,000 and 45,800 meant put *sellers* had a strong incentive to defend, and if the breakdown failed to follow through, those puts would rapidly lose value, forcing put buyers to cover and triggering a snap-back squeeze *upward*. The setup was to watch the 46,000 break for follow-through: real breakdown or bear trap.

| Element | Value (approx) |
|---|---|
| Instrument | Bank Nifty (reversal long after failed breakdown) |
| Precondition | Probe below 46,000 put wall that fails to follow through |
| Trigger | Reclaim and 15-min close back above 46,050 |
| Stop | Back below the false-break low (45,920) |
| Initial risk | ~130 points |
| Target | 46,600, then 46,900 (next call wall) |
| Regime | Failed breakdown / bear trap → put-unwind squeeze |

### The trade, bar by bar

The index broke 46,000 and spiked down to 45,940 — stops below the wall were triggered, weak longs were flushed, and the intraday chart looked broken. But the follow-through never came. Within two 15-minute candles price was back at 46,010, and the option chain revealed the tell: put OI at 46,000 was *rising* (fresh put writing — sellers stepping in to defend), while the spike low showed no acceleration. The bear trap was forming.

The reclaim of 46,050 on a strong 15-minute close was the trigger. Long entered at 46,080, stop below 45,920 — a tight 130-point risk. What followed was the mirror of Case Study 2's squeeze, but powered by *put* dynamics: as price rose, the freshly written and previously bought puts lost value fast, put buyers covered, and dealers who had hedged the breakdown by shorting futures now had to buy them back, adding fuel. The index accelerated through 46,300, 46,500, and pressed toward 46,700.

### The outcome

The squeeze ran into the 46,900 call wall, where fresh call writing finally capped it near 46,820. A 15-minute close below 46,650 triggered the trailing exit. Entry 46,080, exit ≈46,660 — roughly **580 points** on a 130-point risk, a **~4.5R** trade born entirely from correctly reading a failed breakdown rather than joining it.

### The lesson

**A break of an OI wall that fails to follow through is one of the highest-probability reversal signals in expiry-week Bank Nifty — the trapped side becomes the fuel for the move in the opposite direction.** The discipline is patience: you do not short the initial break of 46,000, and you do not go long on the mere spike-down; you wait for the *reclaim* to confirm the trap. The confirming evidence was, again, in the OI change — fresh put writing on the defence. The wall level was identical whether it broke for real or trapped; the option chain's behaviour at the level is what separated the two.

## Cross-cutting principles for expiry-week Bank Nifty

**1. Read OI *change*, not just OI level.** The single most repeated lesson across all three cases: the same price level demands opposite trades depending on whether OI is being *added* (defence → fade/reversion) or *unwound* (abandonment → ride the break). Always look at the change in OI at the key strike, not just its absolute size.

**2. Identify the regime before choosing a strategy.** No-catalyst + aligned max-pain/walls → pin/reversion (short premium). Catalyst + wall breaking with unwinding → trend day (long the break, ride gamma). Failed break → reversal (fade the trap). Getting the regime right is 80% of the edge.

**3. Respect the gamma clock.** The closer to expiry, the more explosive the gamma effects and the faster moves exhaust. Expiry-day trends run hard but reverse hard; trail tighter as the clock winds down.

**4. Match the instrument to the play.** Pin/reversion → short straddle or iron condor, theta as tailwind, walls as risk boundaries. Squeeze/trend → long options for convexity but small size (expiry-day theta is brutal if wrong) or futures with a hard stop for a cleaner risk profile.

**5. Max pain is a tendency, not a guarantee.** It pins in quiet weeks and gets obliterated when a catalyst hits. Never hold a short-premium expiry position through an unhedged event.

## Interview-ready summary

Asked how you trade Bank Nifty into expiry, the professional answer: *"I start with the option chain, not the price chart. I locate max pain and the heaviest call and put OI walls, and I read the change in OI at those strikes to see whether they're being defended or abandoned. In a quiet, no-catalyst week where max pain and the walls align, I trade reversion — fade the extremes or sell premium via an iron condor — because dealers short gamma suppress volatility and the net-short community defends the walls. When a catalyst hits and a wall breaks on expiry day with the sellers unwinding, I flip completely and ride the gamma squeeze, trailing tightly because expiry moves exhaust fast. And when a wall breaks but fails to follow through, I treat the trapped side as fuel and trade the reversal on the reclaim. Same levels, opposite trades — the OI change tells me which."*
