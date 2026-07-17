# PCR, Max-Pain & OI-Based Support/Resistance

## What it is & why it works

Three derived metrics let you read the collective positioning of the entire options market at a glance: the **Put-Call Ratio (PCR)** tells you the *balance* of bets between puts and calls; **Max-Pain** tells you the price at which the largest number of option buyers lose money — the level toward which expiry tends to gravitate; and **OI-based support and resistance** tells you the specific strikes where writers have built walls. Together they convert the sprawling option chain into a compact map: a sentiment reading, a magnet, and a set of fences.

Each works for a distinct behavioural reason. **PCR works because it measures crowd positioning, and crowds at extremes are usually wrong.** When everyone has bought puts (high PCR), the fear is already in the market and there may be no one left to sell — a contrarian bullish signal. When everyone has bought calls (low PCR), greed is exhausted. **Max-pain works because option writers, who are net short the market's options, have both the incentive and, near expiry, the delta-hedging mechanics to nudge price toward the level where the most option premium expires worthless** — maximising their collective profit. It is less a conspiracy than an emergent gravity created by thousands of writers hedging toward the same worthless-expiry outcome. **OI-based S/R works** — as established in the option-chain chapter — because writers defend the strikes they've sold, and their hedging physically caps and cushions price.

The unifying insight is that options are a *zero-sum* market where the writing side is larger, better capitalised, and mechanically hedged. These three tools all read the same thing from different angles: where the well-funded side is positioned, and therefore where price is likely to be attracted (max-pain), where it will meet resistance and support (OI walls), and how lopsided the crowd's bets have become (PCR). For an Indian index trader living in the weekly-expiry cycle, this trio is daily bread.

## The mechanics

**Put-Call Ratio (PCR).** Two common forms:

- **PCR (OI)** = total put open interest ÷ total call open interest. The standard sentiment gauge.
- **PCR (Volume)** = total put volume ÷ total call volume. More intraday, noisier.

| PCR (OI) | Reading | Contrarian implication |
|---|---|---|
| < 0.7 | Call-heavy, greedy/bullish crowd | Caution; froth, possible top |
| 0.7 – 1.0 | Mildly bullish-to-neutral | Normal |
| 1.0 – 1.3 | Neutral-to-cautious | Normal-to-mild-fear |
| > 1.3 | Put-heavy, fearful crowd | Contrarian bullish; floor forming |
| > 1.5–1.8 | Extreme fear / heavy put writing | Strong contrarian long context |

Two cautions baked into the mechanics. First, PCR is *contrarian at extremes* but *confirming in the middle* — a rising PCR from 0.8 to 1.1 in a calm uptrend can simply mean put *writers* are confidently building a floor (bullish), not that fear is rising. You must know whether the puts are being *bought* (fear) or *written* (confidence). Second, absolute PCR levels drift with market structure; always read PCR relative to *its own recent range* for that instrument, not against a textbook 1.0.

**Max-Pain.** The strike at which the *total* value of all in-the-money options (the aggregate payout writers must make) is *minimised* — equivalently, where option buyers' aggregate loss is greatest. Computation, per expiry:

1. For each candidate expiry price (each strike), compute the total rupee value that would be owed to all call holders (for every lower strike) plus all put holders (for every higher strike), weighted by the OI at each strike.
2. The strike that produces the *smallest* total payout is the max-pain point.

In practice platforms compute it for you. Conceptually, max-pain sits near the strike with the heaviest *combined* call+put OI, because that's where writers have collected the most premium they'd like to keep. As expiry approaches, price tends to *drift toward* max-pain — the "pinning" effect. Early in a series max-pain is a weak, slow-moving magnet; on expiry day it can be a strong one, especially in the last hours as gamma pins price to the high-OI strike.

**OI-based support & resistance.** As detailed previously: the largest call-OI strike = resistance (ceiling), the largest put-OI strike = support (floor). The band between them is the expected range, and it usually brackets max-pain. Refresh continuously using change-in-OI to see walls shift.

A worked mini-computation for intuition. Suppose Nifty weekly OI is concentrated thus (contracts, simplified):

| Strike | Call OI | Put OI |
|---|---|---|
| 24,600 | 5 | 40 |
| 24,700 | 10 | 55 |
| 24,800 | 25 | 60 |
| 24,900 | 55 | 25 |
| 25,000 | 60 | 8 |

Largest put OI is at 24,800 → **support**. Largest call OI is at 25,000 → **resistance**. The heaviest combined OI clusters around 24,800–24,900, so **max-pain ≈ 24,800–24,900**. PCR (OI) = total puts (188) ÷ total calls (155) ≈ **1.21** — mildly put-heavy, a cautious-but-supported floor near 24,800. One consistent story from three tools.

## Reading it — a worked India example

Take a Nifty weekly cycle running Monday to Thursday, spot opening Monday at 24,850.

**Phase 1 — Monday's map.** You pull the weekly chain. PCR (OI) reads 1.15 — mildly bullish-to-neutral, and importantly it has *risen* from 0.95 on Friday because put *writers* have been building the 24,700 and 24,800 puts (OI up, premium down — writing, not fear-buying). Max-pain computes to 24,800. OI walls: put wall 24,700 (floor), call wall 25,200 (ceiling). The story: a supported market expected to range roughly 24,700–25,200, gravitating toward 24,800–24,900 by Thursday.

**Phase 2 — Tuesday's drift.** Spot dips to 24,780, tags the 24,700 put-wall region, and holds — put writers there defend, buying futures as their short puts gain delta. PCR ticks up to 1.25 as more puts are written into the dip; this is *confident writing*, not panic, confirmed by falling put premiums relative to the small spot move. The floor is real. You note max-pain has crept up to 24,850 as call writing thins near the money.

**Phase 3 — Wednesday's squeeze.** A positive global cue lifts spot to 25,050. The 25,000 call writers, caught short, begin covering (call OI falling, premium rising). Resistance at 25,000 dissolves and price pushes to 25,120, nearing the 25,200 call wall. PCR falls toward 0.95 as calls get bought into the rally — the crowd turning greedy. Max-pain, however, still sits near 24,900. That divergence — price at 25,120 but max-pain magnet at 24,900 — is your Thursday warning: expiry gravity is *below* spot.

**Phase 4 — Thursday's pin.** Expiry morning, spot opens 25,050. Through the session, the pull toward max-pain (24,900) and the still-solid 25,200 ceiling combine: rallies fail at 25,150, dips get bought at 24,900. In the final two hours, gamma pins price to the 24,900–24,950 pocket — the high combined-OI strike — and Nifty settles at 24,930, within a whisker of the max-pain the chain flagged on Tuesday. A trader who faded the 25,150 failed highs toward the 24,900 magnet, respecting the 25,200 wall as a stop, had a clean expiry-day edge.

## Trading it

**Setup A — contrarian reversal on PCR extreme.** When PCR (OI) hits an extreme *for that instrument's own range* and price sits at a tested chart level:

- *Long trigger:* PCR very high (say >1.5) after a sell-off, at a support shelf, with a reversal candle and VIX rolling over. The crowd is maximally hedged/fearful; the squeeze fuel is upside.
- *Short trigger:* PCR very low (<0.7) after a strong rally, at resistance, with momentum divergence. Greed exhausted.
- *Stop:* Beyond the chart level that defines the extreme (below support for longs).
- *Target:* Mean-reversion toward the range middle / opposite wall.
- *Caveat:* PCR extremes can persist in trends; use as *context*, and require price confirmation before entry.

**Setup B — expiry-day pin (max-pain fade).** On expiry afternoon, when spot sits *away* from max-pain and no fresh trend/event is driving:

- *Entry:* Fade moves *away* from max-pain back toward it — short the failed rallies above max-pain, buy the dips below it — using tight structures given expiry gamma.
- *Stop:* Beyond the nearest OI wall (the fences that bracket max-pain).
- *Target:* The max-pain strike itself.
- *Note:* This works *only* on expiry day and only absent a strong directional catalyst; a trending expiry ignores max-pain entirely.

**Setup C — trade within OI walls.** The bread-and-butter range trade: sell strength into the call wall, buy weakness at the put wall, targeting the opposite wall or the middle — exactly the OI-fade playbook, with PCR telling you which wall is better defended and max-pain telling you the drift bias.

**Structuring with options.** In a supported, put-heavy range (high-but-confident PCR, clear walls), an **iron condor** sold outside the two walls, centred near max-pain, aligns your position with all three signals at once — you profit if price stays inside the fences and drifts to the magnet. Book at ~50% max profit; never carry naked short legs into the final expiry-day gamma.

## Confluence

- **PCR + max-pain + walls in agreement.** The strongest read is when a put-heavy PCR, a max-pain near the current range middle, and clear OI walls all describe the *same* supported range. That is a high-confidence "sell the fences, expect a drift to max-pain" week (Setup C + iron condor).
- **PCR extreme + chart support + VIX spike.** A very high PCR after a crash, at a tested support, with India VIX spiking and rolling over, is a textbook capitulation long — sentiment, price structure, and volatility all aligned (see the VIX chapter).
- **Max-pain divergence + failed highs.** When price runs above a max-pain that stays put, and rallies start failing on the chart, the expiry magnet plus price rejection form a clean fade (Phase 3–4 above).
- **PCR direction vs price.** Rising PCR while price rises = put writers confidently underpinning the advance (healthy). Rising PCR while price *falls* = fear-buying of puts (caution, potential capitulation nearing). The *combination* of PCR direction with price direction is more informative than PCR's level.
- **Volume-PCR for intraday, OI-PCR for positional.** Use volume PCR to sense today's flow, OI PCR for the standing structure.

## Pitfalls & false signals

- **PCR level in isolation is meaningless.** The same PCR of 1.3 can be bullish (confident put writing) or bearish (panic put buying) depending on *how* the puts got there. Always check whether puts are being *written* (OI up, premium down) or *bought* (OI up, premium up). This is the number-one PCR error.
- **PCR baselines drift.** There is no universal "overbought" PCR. Read it against the instrument's own recent range; a 1.1 that is extreme for one regime is neutral in another.
- **Max-pain is a weak magnet until expiry day.** Early in a series it barely matters and moves as OI builds. Treating it as a precise target on Monday is a mistake; its pull is a late-week, and especially expiry-afternoon, phenomenon.
- **Max-pain gets overridden by trends and events.** A strong directional move, a news gap, or an event blows straight through max-pain — writers get run over rather than pinning price. Never fade a genuine trend toward max-pain "because the number says so."
- **Walls shift; refresh them.** OI-based S/R is a live reading, not a fixed weekly fact. Writers roll strikes; a ceiling can migrate. Re-read change-in-OI through the session.
- **Expiry gamma is dangerous.** The pin that helps you fade can also whip violently in the last hour. Size small, define risk, and never hold naked short options into the close hoping for a pin.
- **Illiquid instruments distort all three.** In thin single-stock options, PCR, max-pain, and walls are dominated by a few players and are unreliable. Trust these tools most in Nifty, Bank Nifty, and Fin Nifty where OI is deep.

The professional filter: use PCR as a *sentiment thermometer* (contrarian only at genuine extremes, always cross-checked with whether puts are written or bought), treat max-pain as a *late-cycle magnet* that trends and events can nullify, and treat OI walls as *live, shifting* fences — never as guarantees. All three are probability-shifters layered onto price, not signals to be traded blindly.

## Interview-ready summary

"These three tools compress the whole option chain into a usable map. PCR — put OI over call OI — is my sentiment thermometer: extreme readings are contrarian because a maximally-hedged crowd has no one left to push price further, but I always check whether the puts were *written* (confident floor-building, bullish) or *bought* (fear), because the level alone is ambiguous. Max-pain is the strike where the most option premium expires worthless, and because writers are the larger, delta-hedged side, price tends to gravitate there — a weak magnet early in the series that becomes a real pin on expiry afternoon, unless a trend or event overrides it. OI-based support and resistance are the walls: largest put OI is the floor, largest call OI is the ceiling, and the band between them, usually bracketing max-pain, is the expected range. My highest-conviction week is when all three agree — a put-heavy-but-confident PCR, a max-pain near the range middle, and clear walls — which I trade as a range, often with an iron condor sold outside the walls and centred on max-pain. The honest caveat: PCR baselines drift and are meaningless in isolation, max-pain only bites late and gets run over by trends and events, and the walls shift continuously — so these are probability tools layered on price, never standalone signals."
