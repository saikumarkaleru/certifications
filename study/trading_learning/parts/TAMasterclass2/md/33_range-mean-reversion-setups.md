# Setups: Range & Mean-Reversion (5 setups)

Markets trend roughly a third of the time and chop the other two-thirds. Every trader who only knows how to buy breakouts and ride momentum is therefore fighting the tape for the majority of the calendar — getting whipsawed on false breakouts, buying the high of a range and selling the low, bleeding on stop after stop while the market goes nowhere. Range and mean-reversion trading is the antidote. It is the deliberate art of doing the *opposite* of the breakout trader: selling strength into resistance, buying weakness into support, and betting that price snaps back toward its average rather than escaping to a new one.

The core idea is that in the absence of a strong directional driver, price behaves like a rubber band anchored to a mean. Push it too far from the mean and a restoring force pulls it back — that force is the profit-taking of the traders who rode the move, the fresh entry of contrarians, and the simple statistical tendency of an oscillating series to revert. Mean-reversion is not a belief that the trend is wrong; it is a bet on *distance and speed*. When price stretches far from its anchor quickly, on fading momentum, without a fundamental catalyst, the odds favour a snap back.

The existential risk of this style is obvious and must be stated up front: **mean-reversion works beautifully until the range breaks, and when it breaks it can wipe out weeks of grinding profits in a single trend day.** The trader who sells every touch of resistance will eventually sell the one touch that becomes a breakout, and if he has no stop he is finished. Therefore the discipline that defines a professional range trader is not the entries — those are easy — but the ruthless acceptance that *the trade is wrong the moment the range is decisively breached.* Range trading is a game of taking many small, high-probability wins and cutting the occasional loser instantly before it metastasises into a trend.

**Regime is everything here — more than in any other style.** These setups have positive expectancy *only* in range-bound, low-directional, mean-reverting regimes and *negative* expectancy in trends. The single most important skill is regime identification. Practical filters: is the ADX low (below ~20-25), signalling no trend? Is price oscillating around a flat 20/50-DEMA rather than riding a steeply sloped one? Is the daily range contracting? Is India VIX moderate-to-low and stable? Is the market inside a well-defined horizontal box on the higher timeframe? If yes, mean-reversion is live. If ADX is rising above 25, the moving averages are fanning out and sloping, and price is making clean higher highs or lower lows — *stand down.* No range setup should ever be taken into an established trend.

## Setup 1 — Range Fade (Buy Support / Sell Resistance)

The purest range trade. A stock or index is trapped in a horizontal box — a clearly defined support floor and resistance ceiling that price has respected multiple times. The strategy is mechanical: sell near the top of the box, buy near the bottom, and take profit at the mean or the opposite boundary. You are being paid to provide liquidity to the impatient — selling to the breakout-chasers at the top, buying from the panic-sellers at the bottom.

The edge comes from the box being *proven* — the more times each boundary has been tested and held, the more traders anchor to it and the more likely the next touch also holds. A box with four or five touches per side is far more tradable than a fresh, unconfirmed range. The other half of the edge is the entry location: you buy *at* support, not near it, so your stop just below the floor is tiny relative to the move back to the ceiling.

**Worked India example.** Suppose ITC ranges between ₹460 support and ₹490 resistance for six weeks, touching each boundary three or four times. Price drifts down to ₹462. You buy near ₹463 with a stop below ₹457 (below the floor). Target is the mean around ₹475 for a partial and ₹488 near the ceiling for the rest. Risk is roughly ₹6; reward to the ceiling roughly ₹25 — a clean 3-4R fade.

| Element | Rule |
|---|---|
| Trigger | Price reaches a proven range boundary (buy near support ₹463 / sell near resistance ₹488) with a rejection candle |
| Entry | On the rejection candle at the boundary, or on a small confirmation move back toward the mean |
| Stop | Just beyond the boundary (below ₹457 for longs; above ₹493 for shorts) — tight |
| Target | T1 = mean/midpoint (₹475); T2 = opposite boundary (₹488) |
| Timeframe | Daily for multi-week boxes; 5/15-min for intraday ranges |
| Regime | ADX < 20-25, flat MAs, defined box — MANDATORY; never in a trend |

**Confluence.** The best fades occur where the range boundary aligns with other evidence: a VWAP band, a prior high-volume node, a round number, or a moving average flattening at the level. A rejection candle (pin bar, engulfing) at the boundary confirms buyers/sellers are defending it. Low and stable India VIX supports the range holding. In F&O names, the option chain is gold for range trades — the strikes with the maximum Call OI and maximum Put OI often mark the ceiling and floor of the expected range, and heavy writing at those strikes is smart money betting the boundary holds. Fade toward Max Pain.

**Pitfalls.** The fade's nemesis is the boundary that becomes a breakout — you buy support and it slices through. The only defence is the tight stop *just* beyond the boundary, taken without hesitation. Never average down into a breaking range. Second pitfall: fading a range that is quietly compressing (narrowing) — that is a coil about to break, not a stable box, and fades inside tightening ranges are traps. Third: the first touch of a brand-new range boundary is unproven; the highest-odds fades are the third-plus touches.

## Setup 2 — Bollinger Band Reversion

Bollinger Bands wrap price in a channel set two standard deviations above and below a 20-period moving average. By construction, price spends roughly 90% of its time inside the bands, so a tag of the outer band is a statistically stretched condition. In a *ranging* market, a touch of the upper band means price is stretched high relative to its recent mean and tends to revert toward the middle band (the 20-MA); a touch of the lower band means it is stretched low and tends to bounce. The trade is to fade the band tag back to the mean.

The crucial refinement — the one that separates winners from losers — is that a band tag is only a fade signal when the bands are *flat and horizontal* (ranging). When the bands are expanding and price is "walking the band" (repeatedly tagging the upper band as it trends up), fading is suicidal. Band-walking is the signature of a strong trend and must never be faded. So the setup is: bands flat, price tags outer band, momentum not confirming further, fade to the middle band.

**Worked India example.** Nifty is chopping sideways with flat Bollinger Bands, middle band (20-DMA) at 24,500, upper band at 24,750, lower band at 24,250. Price pushes to 24,745, tagging the upper band, while RSI stalls near 60 (not overbought-extreme, momentum fading). You short near 24,740, stop above 24,800 (a close outside the band), target the middle band at 24,500.

| Element | Rule |
|---|---|
| Trigger | Price tags the outer band while bands are flat/horizontal (ranging) |
| Entry | On the band tag with a rejection candle (short upper band ~24,740 / long lower band) |
| Stop | On a *close* beyond the band (above ~24,800) — an intrabar poke is fine |
| Target | Middle band / 20-MA (24,500); optionally the opposite band |
| Timeframe | Any; commonly 15-min intraday and daily swing |
| Regime | Flat, non-expanding bands — ranging only; NEVER fade a band-walk |

**Confluence.** Pair the band tag with an oscillator (RSI or Stochastic) at an extreme *and* diverging — price tags the upper band on a lower RSI high, confirming the stretch is running out of fuel. A rejection candle right at the band adds precision. The %B indicator (>1 means price closed outside the upper band) and BandWidth (low BandWidth confirms the flat, tradable regime) formalise the read. On the option chain, a band tag that coincides with a high-OI resistance strike is a doubly-confirmed fade.

**Pitfalls.** The number-one account-killer is fading the band-walk in a trend. If price has tagged the upper band three sessions in a row and the bands are *widening*, that is a trend, not an overbought signal — fading it is stepping in front of a train. Always check band *slope* and *width* first. Second pitfall: using a band tag as a standalone signal without regime and momentum confluence — bands describe *stretch*, not *reversal*; something must confirm the reversion is beginning.

## Setup 3 — VWAP Reversion (Intraday Mean-Reversion)

VWAP (Volume-Weighted Average Price) is the intraday anchor around which institutional order flow pivots — it is the price at which the average share traded today changed hands, and large funds benchmark their executions to it. On a *balanced, non-trending* session, price oscillates around VWAP: stretch too far above and sellers (funds selling above their benchmark) push it back; stretch too far below and buyers step in. The VWAP reversion trade fades extensions away from VWAP back toward it, ideally using standard-deviation bands around VWAP to define "too far."

This is a bread-and-butter intraday setup for Nifty, Bank Nifty, and liquid stocks, but only on *rotational* days. The key filter is the character of the open and the early session. Is price chopping across VWAP repeatedly (balanced, faded)? Or did it open, run one direction, and never look back (trend day, do not fade)? On a rotational day, fading the outer VWAP band back to VWAP is high-probability; on a trend day the same trade is a slaughter.

**Worked India example.** Bank Nifty opens flat and spends the morning oscillating around VWAP at 51,600. By 11:30 it stretches up to the upper VWAP band (2 SD) at 51,780 on fading momentum, having already reverted twice earlier. You short near 51,770, stop above 51,830 (beyond the band), target VWAP at 51,610. Risk ~60 points, reward ~160 — a clean rotational fade.

| Element | Rule |
|---|---|
| Trigger | Price reaches the upper/lower VWAP standard-deviation band on a balanced (rotational) session |
| Entry | On the band tag with a rejection candle (short upper band 51,770 / long lower band) |
| Stop | Beyond the VWAP band (above 51,830) — small |
| Target | VWAP itself (51,610); scale rest at the opposite band |
| Timeframe | Intraday only — 1/5-min; VWAP resets each session |
| Regime | Rotational/balanced day (price crossing VWAP repeatedly); NEVER on a trend day |

**Confluence.** The strongest VWAP fades occur when the VWAP band tag coincides with a prior day's level (PDH/PDL), the day's opening range boundary, or a round number. Declining India VIX and a quiet global backdrop favour rotational days. Watch the first hour: multiple VWAP crosses = rotation = fade; a one-way opening drive that holds above/below VWAP all morning = trend = do not fade. On index options, VWAP reversion pairs with intraday option-chain shifts — if price stretches to a heavily Call-written strike and stalls at the upper VWAP band, the fade is doubly confirmed.

**Pitfalls.** The classic disaster is fading a trend day. The morning you must be most careful is a strong-open-and-hold session — price stays pinned above VWAP, every "overbought" band tag is just the trend catching its breath, and each fade is a fresh loss. The regime filter (is price crossing VWAP or riding one side?) is the entire game. Second pitfall: fading into the first 15 minutes when VWAP is still forming and unstable, or into a known event (RBI policy, expiry-day gamma) — let VWAP settle and avoid event windows.

## Setup 4 — Oscillator Extreme Reversion (Stochastic/RSI-2)

Oscillators like Stochastics and short-period RSI (the "RSI-2" popularised for mean-reversion) measure how stretched price is over a short lookback. In a ranging market, extreme oscillator readings mark short-term exhaustion: a deeply oversold reading means sellers have pushed too hard too fast and a bounce is due; a deeply overbought reading means the opposite. The setup buys deep oversold and sells deep overbought — *within a range* — for a quick reversion pop.

RSI-2 (a 2-period RSI) is the sharpest tool here: it swings to true extremes (below 5 or above 95) far more decisively than the standard 14-period. A well-known systematic filter combines it with trend: only take *long* RSI-2 oversold signals when price is above its 200-DMA (i.e., buy short-term dips within a longer uptrend), and only take *short* signals below the 200-DMA. This marries mean-reversion (short-term) with trend (long-term) and dramatically improves the hit rate over blind fading.

**Worked India example.** HDFC Bank is in a broad uptrend, trading above its rising 200-DMA at ₹1,620, but pulls back sharply over three days to ₹1,655. The 2-period RSI plunges below 5 (deeply oversold). Because price is above the 200-DMA, the long signal is valid. You buy near ₹1,656; exit when RSI-2 crosses back above 60-70, or price reclaims a short MA (the 5-DMA), typically a bounce to ₹1,690+ within a few sessions.

| Element | Rule |
|---|---|
| Trigger | Oscillator hits a deep extreme (RSI-2 < 5 for longs / > 95 for shorts; Stochastic < 20 / > 80) |
| Entry | At the extreme with a stabilising candle (buy ₹1,656 dip) — align with 200-DMA trend filter |
| Stop | Below the swing low of the dip (below ₹1,635) — structural |
| Target | Exit on oscillator normalising (RSI-2 > 60-70) or reclaim of the 5-DMA (~₹1,690) |
| Timeframe | Daily for swing (RSI-2 method); intraday variants on 5/15-min |
| Regime | Ranging or pullbacks-within-trend; use the 200-DMA filter to pick direction |

**Confluence.** Combine the oscillator extreme with a horizontal support/resistance level or a moving average that price is testing — an RSI-2 oversold reading *at* the rising 50-DMA is far better than one in mid-air. A bullish rejection candle at the extreme confirms the turn. Bullish divergence (price lower low, oscillator higher low) at the extreme is a strong additional signal. Keep the 200-DMA trend filter as your directional gatekeeper — it is the single biggest improver of this setup's odds.

**Pitfalls.** "Oversold" is not "reversing" — in a genuine downtrend, oscillators can sit pinned at oversold for days while price keeps falling ("oversold can stay oversold"). This is why the trend filter matters: buying oversold *below* a falling 200-DMA is fighting the tape. Second pitfall: no stop. Because the whole premise is "it's stretched, it'll snap back," it is tempting to average down when it doesn't — that is how mean-reversion accounts blow up. Set the stop below the swing structure and honour it. Third: mechanical exit — take the reversion pop and leave; oscillator setups are for quick moves, not trend rides.

## Setup 5 — Failed Breakout Fade (Range Reclaim)

Ranges spend most of their life inside their boundaries, but they constantly *fake* breakouts — price pokes above resistance or below support, sucks in breakout traders, then falls back inside the box. This failed breakout is a high-probability fade: the traders who bought the breakout are now trapped above (or below) a level that has reverted to being a wall, and their stop-loss covering pushes price back toward the opposite side of the range. It is the range-trading cousin of the reversal-chapter "spring," but here you are trading it *as a range continuation*, not a trend reversal.

The trigger is precise: price must break the boundary and then *close back inside the range.* The break lures the crowd; the reclaim traps them. You fade in the direction of the range — short the failed upside breakout, long the failed downside breakout — targeting the mean or the opposite boundary.

**Worked India example.** Suppose Infosys ranges between ₹1,780 and ₹1,850. On a positive global cue it spikes to ₹1,868, breaking ₹1,850 and triggering breakout buys. But the move has no follow-through; by afternoon it closes back at ₹1,842, inside the range. The upside breakout has failed. You short near ₹1,840 with a stop above ₹1,870 (the failed-breakout high), targeting the mean ₹1,815 and the ₹1,780 floor.

| Element | Rule |
|---|---|
| Trigger | Price breaks a range boundary then closes back *inside* the range (fails to hold the breakout) |
| Entry | On the reclaim close (short ₹1,840 after failed upside break; long after failed downside break) |
| Stop | Beyond the failed-breakout extreme (above ₹1,870) |
| Target | T1 = range mean (₹1,815); T2 = opposite boundary (₹1,780) |
| Timeframe | Daily and intraday; the reclaim close defines the signal |
| Regime | Established range; low ADX; NOT a genuine trend-starting breakout |

**Confluence.** A failed breakout is most convincing when the breakout occurred on *weak* volume (no real conviction) and the reclaim on *stronger* volume (trapped traders bailing). Divergence into the breakout high adds weight. In F&O, a failed upside breakout that stalls exactly at a heavily Call-written strike, followed by the reclaim, is a textbook trapped-longs fade. India VIX staying low throughout confirms this was noise, not a regime change.

**Pitfalls.** The obvious trap is mistaking a *real* breakout for a failed one — sometimes price closes back inside for a day and then breaks out again for real. The defence is the stop beyond the failed-breakout extreme; if it reclaims the breakout level, you are wrong and you are out. Never fight a breakout that keeps making higher closes above resistance on rising volume — that is a trend being born, and fading it is the cardinal sin of range trading. Discipline: the range is your friend only until it isn't, and the moment price holds outside on strength, you flip from fader to spectator.

## Interview-ready summary

Range and mean-reversion trading is the necessary complement to trend-following, because markets are range-bound most of the time and pure breakout traders bleed through the chop. The five setups form a complete rotational toolkit: the **Range Fade** sells proven resistance and buys proven support with tight boundary stops; **Bollinger Band Reversion** fades statistically stretched band tags back to the mean — but only when bands are flat, never on a band-walk; **VWAP Reversion** fades intraday extensions back to the institutional anchor on rotational (not trend) days; **Oscillator Extreme Reversion** buys deep-oversold and sells deep-overbought, sharpened by RSI-2 and gated by the 200-DMA trend filter; and the **Failed Breakout Fade** traps the breakout crowd and rides their covering back into the range. Three principles bind them all. First and above all, **regime identification is the entire edge** — every one of these setups is profitable in a range and lethal in a trend, so ADX, moving-average slope, band width, and VWAP behaviour must confirm a non-trending environment before any entry. Second, **stops are tight, structural, and absolute** — the trade dies the instant the range decisively breaks, and there is no averaging down, because one un-stopped trend day erases a month of grinding. Third, **take the reversion and leave** — these are high-frequency, small-target trades, scaling out at the mean and the opposite boundary, not trend rides. Overlay India-specific confluence — option-chain Max Pain and high-OI strikes marking the box, low and stable India VIX confirming rotation, VWAP bands for intraday structure — and range trading becomes a disciplined, repeatable business of collecting many small high-probability wins while cutting the rare loser instantly.
