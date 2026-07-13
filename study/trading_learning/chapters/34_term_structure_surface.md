# Chapter 34: Term Structure & the Volatility Surface

In the last few chapters you learned that implied volatility (IV) is not a single number — it changes depending on *which strike* you look at. The 23000 put trades at a different IV from the 24500 call, and that pattern of IV-across-strikes is the **skew** or **smile**. But there is a second axis you have been quietly ignoring. IV also changes depending on *which expiry* you look at. The 24000 call expiring this Thursday and the 24000 call expiring three months from now almost never carry the same implied volatility, even though they share the same strike and the same underlying.

This second pattern — IV plotted **across expiries** — is the **term structure of volatility**. Stitch the two axes together (IV across strikes *and* across expiries) and you get the full **volatility surface**: a three-dimensional map of what the market is charging for uncertainty, at every strike, for every maturity. This chapter teaches you to read that map. It is the single most important tool a professional uses to decide *which expiry* to trade, not just which strike — and it is the foundation of calendar spreads, diagonal spreads, and almost every event-driven play on Nifty and Bank Nifty.

## Core concepts

### Why IV should depend on time at all

Start with intuition. Implied volatility is the market's forecast of how much the underlying will move, expressed as an **annualised** standard deviation of returns. The word "annualised" is doing a lot of work. A weekly option only cares about the next few days; a quarterly option cares about the next several months. Those are forecasts about *different windows of the future*, and there is no reason the future should look equally turbulent in every window.

Think of it like a weather forecast. "How stormy will the next three days be?" depends heavily on whether a specific cyclone is bearing down right now. "How stormy will the next six months be?" barely cares about the cyclone — you are averaging over many calm and many rough days, so you land near the long-run climate. Short-horizon forecasts are dominated by *what is happening now*; long-horizon forecasts revert to the *long-run average*. Volatility behaves exactly the same way, and that single fact explains almost everything about term structure.

### The shape: upward-sloping in calm, inverted in stress

In a **calm market**, the term structure usually slopes **upward**. Near-term IV is low because nothing scary is on the immediate horizon, so the next few days are expected to be quiet. Longer-dated IV is higher because the further out you look, the more unknown events can creep in — elections, global shocks, a bad earnings season, a war — and the market demands a higher premium to insure against that growing fog of uncertainty. So you might see something like:

- Current weekly (5 days to expiry): IV around 11%
- Current monthly (28 days): IV around 13%
- Next-month (56 days): IV around 14%
- Quarterly (90 days): IV around 15%

The curve rises gently from left to right. This is the "normal" or **contango** shape, and it is what you see most of the time on Nifty when India VIX is sitting low (say, 11-13).

In a **stressed market**, the term structure **inverts** — it slopes downward. When fear spikes, traders scramble for *immediate* protection. They are terrified of the next few days, not the next few months, because they expect (or hope) the panic will burn out. So near-term IV explodes above long-term IV:

- Current weekly: IV around 32%
- Monthly: IV around 26%
- Quarterly: IV around 21%

Now the curve falls from left to right — this is **backwardation**. A crashing market, a surprise RBI move, a global risk-off day: all of them slam the front of the curve up while the back end rises far less, because the market believes the storm is temporary and things will eventually calm down. This inversion is one of the most reliable tells that the market is in genuine stress rather than a routine wobble.

The intuition is the same weather logic in reverse: when a cyclone is directly overhead *right now*, the three-day forecast is far scarier than the six-month forecast.

![Figure: an upward-sloping IV term structure](figs/term_structure.png)

### Events create a local bump in the near-expiry IV

Here is where term structure gets practically useful for an Indian trader. Markets do not face uncertainty smoothly — it arrives in *lumps* on known dates. The Union Budget (1 February), RBI monetary policy decisions, big-bank quarterly results (HDFC Bank, ICICI, SBI for Bank Nifty), general election results, and US Fed decisions are all **scheduled events**. Everyone knows the date in advance.

Because the date is known, the expiry that *contains* that event will price in the extra expected move — and the expiries that do not contain it will not. This produces a **local bump** in the term structure right at the expiry that straddles the event.

Suppose RBI policy lands on a Friday. The weekly expiring the Thursday *before* it does not include the event, so its IV stays calm — say 12%. The weekly expiring the Thursday *after* it *does* include the RBI decision, so its IV is jacked up — say 18%. The monthly, which also contains the event but spreads it over many more days, sits in between — say 14%. So instead of a smooth upward slope you see a **spike** at one specific expiry:

- Pre-event weekly: 12%
- Post-event weekly (contains RBI): 18%  ← the bump
- Monthly: 14%

The reason the monthly IV rises *less* than the post-event weekly is dilution. An event adds a roughly fixed amount of *expected variance* (volatility squared times time). Pack that fixed lump of extra variance into a 4-day weekly and the *annualised* IV jumps a lot; spread the same lump across a 30-day monthly and the per-day impact is small, so annualised IV barely twitches. This is why event premium is always most concentrated, and most expensive, in the **nearest expiry that contains the event**.

### Combining skew and term structure: the volatility surface

Now combine the two dimensions. For each expiry you have a skew — a curve of IV across strikes (puts richer, calls cheaper, the classic equity-index skew from Chapter 33). And across expiries you have a term structure — a curve of IV across maturities. Lay every expiry's skew curve side by side, ordered by maturity, and you have built a **surface**:

`Implied volatility = f(strike, time-to-expiry)`

Picture a sheet of cloth floating above a grid. One edge is *strike* (deep OTM puts on the left to deep OTM calls on the right), the other is *time to expiry* (this week's expiry to the far quarterly). The *height* of the cloth at any point is the IV the market charges for that exact strike-and-maturity combination. Slice it along the strike axis at a fixed expiry and you recover that expiry's **skew**; slice it along the time axis at a fixed (usually at-the-money) strike and you recover the **term structure**.

A professional desk does not think in single IV numbers — it thinks about this whole surface, watching where it is locally rich (overpriced) and locally cheap (underpriced). Every relative-value options trade is, at bottom, a bet that one part of the surface is mispriced relative to another part.

### How the surface guides calendar and diagonal trades

The most direct application is the **calendar spread** (also called a time spread or horizontal spread). The structure: **sell a near-term option and buy a longer-term option at the same strike.** You sell the front month and buy the back month.

When does this make sense? Read it straight off the term structure. When the front of the curve is *rich* relative to the back — typically right before an event, when near-term IV has spiked into a local bump — you **sell the expensive near-term option and buy the cheaper far-term option**. You are short the inflated front-month vega and long the calmer back-month vega. After the event passes, the front-month IV collapses (the bump deflates), the option you sold loses value fast, and you keep the difference. The far-term leg you own barely moves because its IV was never inflated.

A **diagonal spread** is a calendar with the two legs at *different strikes* — it tilts the trade so you also take a directional or skew view, not just a pure time view. You might sell a near-term slightly-OTM call and buy a far-term further-OTM call, combining the term-structure edge with a mild directional lean.

The mechanics come from Greeks you already know:

- **Theta:** the near-term option you sold decays *faster* than the far-term option you own (decay accelerates near expiry — Chapter 24), so the net position usually earns theta day by day.
- **Vega:** the far-term option you own has *more* vega than the near-term option you sold (vega rises with time to expiry — Chapter 25), so a calendar is typically *net long vega* — it benefits if overall IV rises after you put it on.

That second point is a warning. A standard calendar does best when the underlying sits *near the strike* and overall volatility holds up or rises; it can lose if IV collapses across the *whole* curve, or if the underlying runs far from the strike. Selling a near-term event bump is the one classic setup where you may end up *short* net vega — because the front-month vega you sold is so inflated it outweighs the back-month vega you bought. Always check which way your net vega points before calling a calendar "safe."

### Event plays: sell the bump, or own the move

The local event bump gives you a clean choice. If you think the market is *overpricing* the event, you **sell** the inflated near-expiry premium (via a calendar, or a short straddle/iron condor on the event week) and collect the **volatility crush** when IV deflates the moment the news is out. This "IV crush" is reliable enough that selling Budget-day or results-day premium is a staple professional trade — but it carries large, sometimes undefined, risk if the move is bigger than priced.

If instead you think the event will move *more* than priced, you **buy** the near-expiry straddle. This is much harder: you are paying the inflated bump, so the move must be large just to break even, and if the market merely meets expectations the IV crush guts your long position even when direction was right.

### Reading Nifty / Bank Nifty term structure: weekly vs monthly

Indian index options give you an unusually rich term structure because of **weekly expiries**. Nifty and Bank Nifty (and other indices) have a weekly contract expiring most weeks, plus monthlies and a few quarterlies. That means the front of your term-structure curve is sampled finely — you can see the IV of *this* Thursday, *next* Thursday, the one after, then the monthly, then further out.

Practical reading rules for an Indian desk:

- **Weeklies are the most event-sensitive and the most theta-heavy.** With only a handful of days to expiry, the weekly's annualised IV swings violently around scheduled events and decays brutally fast afterward. This is why so much retail volume — and so many retail losses — concentrate in weekly options: the leverage and decay are both extreme.
- **Compare the current weekly's IV to the monthly's IV** to gauge near-term stress. Weekly IV well *above* monthly IV (front-end inverted) signals an event or fear concentrated in the next few days. Weekly IV well *below* monthly (normal upward slope) signals a calm patch right now.
- **Bank Nifty runs hotter than Nifty.** Bank Nifty is more concentrated (heavily weighted to a few large lenders) and structurally more volatile, so its whole surface sits at a higher IV and its event bumps — especially around bank results and RBI policy — are sharper than Nifty's.
- **India VIX is essentially one point on this surface** — it is a 30-day, near-the-money Nifty IV. It tells you the *level* of the curve around the monthly tenor but nothing about its *slope*. Two days with identical VIX can have completely different term structures: one calm-and-upward-sloping, one inverted with a fear spike in the front. Always look at the curve, not just the VIX print.

## Worked example (Rupees, Nifty)

It is late January. Nifty is at **24,000**. The Union Budget lands on **1 February (a Saturday this year)**, so the weekly expiring **Thursday 6 February** is the first expiry that *contains* the Budget. You pull the at-the-money (24000-strike) IVs off the screen:

| Expiry | Days to expiry | Contains Budget? | ATM IV |
|---|---|---|---|
| Thu 30 Jan (this week) | 4 | No | 11% |
| Thu 6 Feb (Budget week) | 11 | Yes | 19% |
| Thu 27 Feb (monthly) | 32 | Yes | 14% |
| Thu 27 Mar (next monthly) | 60 | Yes | 14.5% |

Read the curve. The 30 Jan weekly is calm at 11% — nothing happens before it expires. The 6 Feb weekly carries a fat **local bump at 19%** because it is the cheapest, most concentrated way to own the Budget move. The 27 Feb monthly also contains the Budget but dilutes it across 32 days, so its IV is only 14%. Beyond that the curve drifts gently up (14.5%) — the normal upward slope reasserting itself.

You judge the 19% Budget-week IV to be *too high* — your read is that recent Budgets have produced moves smaller than this premium implies. You decide to **sell the rich front-month bump and own a calmer back-month** with a calendar spread at the 24000 strike.

**The trade (per leg, ATM 24000 strike, Nifty lot size 75 — verify current lot size before trading):**

- **Sell** 1x 6 Feb 24000 call at 19% IV. With 11 days to expiry, suppose its premium is **₹230 per share**.
- **Buy** 1x 27 Feb 24000 call at 14% IV. With 32 days to expiry, suppose its premium is **₹330 per share**.

**Net debit** = 330 - 230 = **₹100 per share**, i.e. ₹100 * 75 = **₹7,500 per lot** (plus costs). This debit is your maximum loss if the position is closed with both legs at the same strike and things go badly.

**What happens after the Budget.** The Budget passes on 1 February with a move roughly in line with expectations. The IV crush hits the front leg hard: by Monday 3 February the 6 Feb 24000 call's IV collapses from 19% toward the calm-market ~11%, and with fewer days left its premium drops to, say, **₹120**. The back-month 27 Feb call still has 24 days to run and its IV barely moves (14% → 13.5%), so its premium eases only to about **₹300**.

Mark the position:

- Short 6 Feb call: sold at ₹230, now ₹120 → **+₹110** per share.
- Long 27 Feb call: bought at ₹330, now ₹300 → **−₹30** per share.
- **Net profit** ≈ 110 − 30 = **₹80 per share** = ₹80 * 75 = **₹6,000 per lot**, before brokerage, STT and other charges.

You captured most of the front-month IV crush while the back-month held its value — exactly what the term structure told you to do. Had Nifty instead *gapped* far from 24000 (say to 23,000 or 25,200), both calls would have moved away from the peak of the calendar's payoff and the trade could have lost up to the ₹7,500 debit. The calendar's sweet spot is the underlying finishing *near* the strike, with the event premium deflating as expected.

## Common mistakes / risk note

- **Treating IV as one number.** Beginners say "Nifty IV is 13%." There is no single Nifty IV — there is a whole surface. The 13% you saw is one slice (probably the monthly ATM, i.e. roughly India VIX). Always ask: *which strike, which expiry?*
- **Selling the event bump without respecting tail risk.** Selling inflated near-term premium works *most* of the time, which is exactly the trap. The Budget or RBI surprise that breaks the range can hand you a loss many times your collected premium. Short premium has large, sometimes undefined, risk — the high win rate hides a fat tail.
- **Forgetting a calendar is usually long vega.** Traders put on a calendar for the theta and get blindsided when IV collapses across the *whole* curve and the long back-month leg bleeds. Know your net vega before you trade.
- **Confusing the two crushes.** "IV crush" after an event deflates the *front-month bump* specifically. A broad market calm-down deflates the *entire surface*. A calendar wants the first and fears the second. They are not the same thing.
- **Over-trading weeklies.** The near-expiry weekly has the most violent IV swings and the fastest decay. It looks cheap in rupees and feels like a lottery ticket — which is precisely why so many retail traders lose money there. SEBI studies show roughly 9 in 10 retail F&O traders lose money, and crowded weekly-option punting is a big part of that statistic.
- **Mis-dating the event.** The whole trade rests on knowing *which* expiry contains the event. Get the date wrong — sell the pre-event weekly thinking it holds the Budget — and there is no bump to crush; you just sold cheap premium and own nothing useful.

## Key takeaways

- IV varies not only across **strikes** (skew) but across **expiries** (term structure). Both axes together form the **volatility surface**: IV as a function of strike and maturity.
- In **calm** markets the term structure slopes **upward** (near-term cheap, long-term richer); in **stress** it **inverts**, with near-term fear spiking above long-term IV.
- **Scheduled events** (Budget, RBI, results) create a **local bump** in the IV of the nearest expiry that *contains* the event; monthlies dilute the same event, so their IV rises far less.
- **Calendar spreads** sell rich near-term premium and buy cheaper far-term premium; they typically earn theta and are usually net long vega — read the entry straight off the term structure.
- **Diagonals** are calendars at different strikes, adding a directional or skew tilt.
- On Nifty/Bank Nifty, **weekly expiries** let you sample the front of the curve finely; compare weekly vs monthly IV to gauge near-term stress. **India VIX** is just the ~30-day ATM point — it gives you the level, not the slope.
- Bank Nifty's surface sits higher and bumps harder than Nifty's. And selling event premium, however reliable, carries large tail risk.

## Practice problems

1. **Conceptual.** Nifty's current weekly ATM IV is 28% while its quarterly ATM IV is 19%. Is the term structure upward-sloping or inverted, and what does that tell you about the market's mood right now?

2. **Conceptual.** RBI policy is scheduled for the Friday after this Thursday's weekly expiry. Which expiry — this week's weekly, next week's weekly, or the monthly — should carry the largest *local bump* in IV, and why does the monthly's IV rise less than the post-event weekly's?

3. **Numeric.** The 24000-strike Nifty options show: 6 Feb weekly IV = 20%, 27 Feb monthly IV = 14%. You sell the 6 Feb 24000 call for ₹250 and buy the 27 Feb 24000 call for ₹360 (lot size 75). What is your net debit per share and per lot? Is this position a calendar spread? Is it likely net long or net short vega from the *time-to-expiry* effect alone?

4. **Numeric.** After the event in Problem 3, the front-month call's IV crushes and its premium falls to ₹130, while the back-month call eases to ₹335 (underlying still near 24000). What is your profit per share and per lot, before costs?

5. **Conceptual.** A trader says, "India VIX is 13 today, same as last Tuesday, so the volatility picture is identical." Why might that statement be wrong even though VIX is unchanged?

6. **Conceptual + risk.** You are tempted to sell the Budget-week straddle to collect the IV crush. State one scenario where this "high-probability" trade produces a loss far larger than the premium you collected, and what that implies about position sizing.

## Solutions

1. The curve is **inverted** (downward-sloping): near-term IV (28%) is far above long-term IV (19%). Near-term fear sits well above the long-run level, which signals the market is in **stress right now** — traders are paying up for immediate protection but expect the turbulence to fade over the coming months. This backwardated shape is a classic stress tell rather than a routine quiet market.

2. **Next week's weekly** should carry the largest bump, because it is the *nearest* expiry that actually *contains* the RBI decision while packing that event's expected move into the fewest days. This week's weekly expires *before* the event, so it includes no RBI risk and stays calm. The monthly also contains the event, but it spreads the event's roughly fixed lump of extra expected variance across ~30 days instead of ~7, so on an *annualised* (per-day) basis the impact is diluted and its IV rises only modestly. Event premium concentrates in the nearest containing expiry.

3. **Net debit** = 360 − 250 = **₹110 per share**, and ₹110 * 75 = **₹8,250 per lot** (before costs). Yes — selling a near-term option and buying a longer-term option at the *same strike* (24000) is a textbook **calendar (time) spread**. From the time-to-expiry effect alone the position is **net long vega**, because the longer-dated 27 Feb option you bought has more vega than the shorter-dated 6 Feb option you sold. (The inflated front-month IV partly offsets this, but on the maturity effect alone, longer-dated = more vega = net long vega.)

4. Short 6 Feb call: sold ₹250, now ₹130 → **+₹120** per share. Long 27 Feb call: bought ₹360, now ₹335 → **−₹25** per share. **Net profit** = 120 − 25 = **₹95 per share** = ₹95 * 75 = **₹7,125 per lot**, before brokerage, STT and other charges. The front-month IV crush delivered the gain while the back-month leg held its value — the intended calendar outcome.

5. India VIX measures only **one point** on the volatility surface — roughly the 30-day, at-the-money Nifty IV. It captures the *level* of the curve near the monthly tenor but says nothing about its *slope* or the *skew*. Last Tuesday the term structure might have been calmly upward-sloping with no event nearby; today it could be inverted with a sharp bump in the next weekly because a Budget or RBI decision now sits just ahead. Same VIX, completely different near-term risk picture. Always read the whole curve, not the single VIX print.

6. Selling the Budget-week straddle collects the IV crush *only if* the realised move stays within the premium you sold. If the Budget delivers a genuine surprise — a large tax change, a fiscal shock — Nifty can gap several percent, blowing far past your breakevens. A short straddle has **theoretically unlimited loss on a big move** in either direction, so a single bad event can cost many multiples of the premium collected. The implication: never size short-premium event trades as if the high win rate were the whole story. Size for the *tail* — small enough lots, or define the risk with protective wings (turning the straddle into an iron condor/iron fly) — so one Budget surprise cannot wipe out months of collected premium.
