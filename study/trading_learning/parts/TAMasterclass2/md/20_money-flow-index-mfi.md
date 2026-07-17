# Money Flow Index (MFI)

## What it is & why it works

The Money Flow Index (MFI) is a bounded momentum oscillator that answers a single, valuable question that price-only indicators cannot: **is the money moving into this instrument or out of it?** Developed by Gene Quong and Avrum Soudack, MFI is often described as "volume-weighted RSI," and that description is exactly right. Where the ordinary Relative Strength Index measures the ratio of up-closes to down-closes using price alone, MFI multiplies each period's price by that period's volume before doing the same up-versus-down accounting. The result oscillates between 0 and 100 and gives you a reading of buying pressure that respects conviction — a 2% up-day on huge Bank Nifty volume counts far more than a 2% up-day on a thin, holiday-week session.

Why does weighting by volume matter in the Indian context? Because our markets are dominated by episodic participation. FII program buying, mutual-fund SIP inflows on the first week of the month, expiry-day unwinding, and event-driven spikes (RBI policy, Budget, results) all produce moves where **volume is the tell, not price**. A stock like Adani Ports can drift up 1% on nothing, then rip 4% on ten times average volume when an index-inclusion rumour hits. Price momentum indicators treat both moves as "up." MFI does not — it inflates the second move and largely ignores the first. That is why MFI shines at spotting the moments when smart money is genuinely committing capital versus when price is merely wandering.

The core logic rests on a behavioural truth: sustainable trends are funded. A rally that keeps making higher highs while MFI keeps making lower highs is a rally running on fumes — the price is being marked up but the money flowing in is thinning. That negative divergence is MFI's single most powerful signal, and because it embeds volume, it tends to be earlier and cleaner than the equivalent RSI divergence.

## Mechanics, formula & settings

MFI is built in four steps. Understanding them makes the signals intuitive rather than magical.

**Step 1 — Typical Price (TP).** For each period, compute the average of high, low and close:

TP = (High + Low + Close) / 3

The typical price is a more honest "where did trading happen" number than the close alone, especially on a wide-range Nifty candle where the close can be an accident of the last thirty seconds.

**Step 2 — Raw Money Flow (RMF).** Multiply typical price by the period's volume:

RMF = TP × Volume

This is the rupee-weighted "how much money changed hands and at what level" figure. For an index, "volume" is the exchange-reported traded volume of the constituents (or futures volume when you apply MFI to a futures chart).

**Step 3 — Money Flow Ratio.** Over a lookback window (default 14 periods), classify each period as *positive* if today's TP is higher than yesterday's TP, and *negative* if it is lower. Sum the positive RMF and the negative RMF separately, then form the ratio:

Money Flow Ratio = (14-period Positive Money Flow) / (14-period Negative Money Flow)

**Step 4 — Money Flow Index.**

MFI = 100 − [100 / (1 + Money Flow Ratio)]

That final formula is identical in shape to RSI's; the only difference is that the inputs are volume-weighted money flows rather than simple price changes.

**Settings that matter for Indian markets:**

- **Length 14** is the default and works well on the daily Nifty/Bank Nifty charts. It gives roughly two-and-a-half trading weeks of memory.
- **Length 9** for swing traders who want faster turns on the daily, or for intraday work on 15-minute Bank Nifty charts around events.
- **Length 20-21** for positional traders filtering out expiry-week noise on large caps.
- **Overbought/oversold thresholds:** the classic 80/20 is stricter than RSI's 70/30 because volume-weighting pushes readings to extremes less often — when MFI does hit 80 or 20, it means something. In strong Indian bull phases (say, the 2023-24 midcap run), consider shifting the oversold band up to 30-40 for buy-the-dip logic, because pullbacks in a powerful uptrend rarely drag MFI all the way to 20.

A practical caveat unique to MFI: **its dependence on volume makes it only as good as the volume data.** On the cash Nifty index itself, "volume" is a synthetic constituent aggregate; many traders prefer to apply MFI to the **Nifty or Bank Nifty futures** chart, where the traded contract volume is clean and directly meaningful. On individual NSE stocks the cash volume is reliable. On MCX gold or crude, use the continuous futures volume.

## Worked India example (levels & ₹)

Consider a reconstructed Bank Nifty daily sequence — the kind of setup that recurs around monthly expiries. Treat the exact figures as an approximate reconstruction to verify on your own TradingView chart.

Bank Nifty has rallied from roughly ₹47,800 to ₹51,200 over three weeks into the monthly expiry. The index prints a fresh higher high at 51,200, and again at 51,450 four sessions later — clean, bullish price action that has retail chasing calls. But look at the MFI(14) on the daily: at the 51,200 high it read about 82; at the 51,450 high it read only 71. **Price made a higher high; MFI made a lower high.** That is a bearish divergence, and because MFI weights volume, it is telling you the second push to 51,450 was made on lighter money — the marking-up was happening on lower participation, likely short-covering and thin volume rather than fresh institutional buying.

The confirmation arrives when MFI, having peaked around 82 and rolled over, crosses back below the 80 line even as price is still near its highs. A trader watching this would tighten stops on longs, and an aggressive trader would look for a short trigger. Two sessions later Bank Nifty breaks the minor swing low at ₹51,050 on rising volume, and MFI is now falling through 60. Over the next eight sessions the index retraces the whole final leg back to ₹49,300 — a ₹2,150 move, worth roughly 2,150 points, which on one Bank Nifty futures lot (15 units) is about ₹32,250 per lot before costs. The MFI divergence gave the earliest structural warning, ahead of the price break.

Now flip it. A few weeks later Bank Nifty sells off from ₹49,300 toward ₹47,600 in a sharp two-day flush on results-season fear. Price makes a marginal new low at 47,600, but MFI(14) which had bottomed near 18 on the first flush now reads 27 on the second — a **bullish divergence**, money flowing out at a decelerating rate. When MFI crosses back above 20 and price reclaims ₹47,900, a long with a stop under 47,600 targeting the ₹49,300 shelf offered roughly a 1:2.5 reward-to-risk trade.

## How to trade it — entry, stop, target

MFI is a **timing and confirmation tool**, not a standalone trend engine. Use it inside a structure you already understand.

**Setup A — Divergence reversal (the flagship).**
- *Trigger:* Price makes a higher high (or lower low) while MFI makes the opposite. Enter only on the *confirmation* — MFI crossing back through the 80 line (for shorts) or 20 line (for longs), plus a price break of the nearest swing level.
- *Stop:* Just beyond the extreme price high/low that produced the divergence. In the Bank Nifty example, a short's stop sits a little above 51,450.
- *Target:* The origin of the diverging leg, or the prior consolidation shelf; scale out at 1:1 and trail the rest.
- *Timeframe/regime:* Best in range-bound or late-trend conditions. Divergences fail repeatedly in the meat of a strong trend, so demand confluence.

**Setup B — Oversold reclaim in an uptrend (buy-the-dip).**
- *Trigger:* In a confirmed uptrend (price above rising 50-DMA), MFI dips to 20-30 on a pullback, then crosses back above 30.
- *Stop:* Below the pullback low.
- *Target:* Prior high, then trail with the 20-DMA.
- This is the higher-probability MFI trade because you are trading *with* the trend and using MFI only to time the entry.

**Setup C — Failure swing / 80-cross exit.**
- Use MFI crossing down through 80 purely as a **stop-tightening signal** on existing longs even when you have no divergence. It reliably flags the moment buying pressure has become exhausted.

Position sizing should respect the reality that MFI signals cluster around events. Never take a fresh MFI divergence short into an RBI policy or Union Budget without hedging — the volume spike that fires the signal can reverse violently.

## Confluence (including OI)

MFI becomes far more trustworthy when it agrees with other evidence:

- **Option-chain / OI:** A bearish MFI divergence on Nifty that coincides with **heavy call writing** building at the strike just overhead (rising call OI, falling price of those calls) is a high-conviction combination — both the derivatives desk and the cash-money flow are saying "supply here." Conversely, a bullish MFI divergence at a level where **puts are being written aggressively** (put OI stacking as a support floor) is a strong long confluence. The Max Pain level and the Put-Call Ratio give context: an MFI oversold-reclaim buy near a strong put-writing support with PCR turning up is one of the cleanest positional longs in Nifty.
- **Volume Profile:** MFI divergences that occur at a High Volume Node (a price shelf where lots of business was done) or at the edge of the Value Area carry more weight.
- **Support/resistance & round numbers:** A bullish MFI reclaim exactly at a psychological Nifty level (24,000; 24,500) or a prior swing low is more reliable than one floating in mid-air.
- **RSI cross-check:** When both RSI and MFI diverge together, but MFI diverges *more* (because volume is confirming the exhaustion), take the signal seriously. When RSI diverges and MFI does not, the "distribution" may be an illusion of price with money still supporting it.
- **Delivery percentage:** On single stocks, pair MFI with NSE delivery-percentage data. A rally with rising MFI *and* rising delivery percentage is real accumulation; rising MFI on high volume but low delivery is often intraday churn.

## Pitfalls

1. **Divergence is not a timing signal by itself.** In a runaway trend — think the relentless 2023 legs in Nifty or a parabolic Adani-group move — MFI can diverge for many sessions while price keeps climbing. Traders who short the first divergence get run over. Always wait for the confirmation cross and a price-structure break.
2. **Bad or synthetic volume corrupts the reading.** Applying MFI to the cash index, to illiquid smallcaps, or to the first fifteen minutes of a stock that gapped on news gives noisy, misleading values. Prefer futures volume for indices and liquid names for stocks.
3. **Expiry-day distortion.** On Nifty/Bank Nifty weekly expiry days, volume explodes for mechanical reasons (rollover, settlement) that have nothing to do with directional conviction. MFI can spike or crater artificially. Discount MFI signals generated on expiry sessions.
4. **Threshold rigidity.** Blindly using 80/20 in every regime is a mistake. In powerful bull markets MFI may never reach 20 on dips; in dead ranges it may oscillate 40-60 for weeks producing nothing. Adapt bands to the regime.
5. **Gap risk.** Because typical price uses high/low/close, a large overnight gap (common in Indian stocks after results) creates a distorted TP and a jumpy money-flow classification. Interpret the first post-gap reading with caution.
6. **Over-optimisation.** Do not curve-fit the length to make past divergences look perfect. Stick to 14 (or 9 for faster work) and let confluence do the filtering.

## Interview-ready summary

The Money Flow Index is a volume-weighted RSI: it computes typical price times volume, separates positive from negative money flow over a 14-period window, and expresses the ratio on a 0-100 scale using the same formula as RSI. Because it embeds volume, it measures *conviction*, not just direction — making it especially well-suited to Indian markets where episodic institutional flows, SIP inflows and event-driven volume spikes dominate. Its flagship signal is divergence: price making a new extreme while MFI fails to, warning that the move is no longer funded. The highest-probability application, however, is trading *with* an established trend — using MFI's 20-30 oversold reclaim to time buy-the-dip entries — rather than fighting the trend on the first divergence. Standard bands are 80/20, stricter than RSI's 70/30 because volume-weighting reaches extremes less often. Confluence with option-chain OI (call/put writing), volume profile, delivery percentage and price structure is what converts an MFI signal from interesting to actionable. Its main failure mode is premature divergence signals in strong trends and corrupted readings from synthetic index volume or expiry-day distortion — both managed by demanding confirmation and applying the tool to clean futures/liquid-stock volume. In one line: **MFI tells you whether the trend has money behind it, and the honest trader waits for it to confirm rather than predict.**
