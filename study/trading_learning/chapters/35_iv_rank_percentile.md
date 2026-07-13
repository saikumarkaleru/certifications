# Chapter 35: IV Rank & IV Percentile — Is Volatility Cheap or Rich?

You have learned (Chapter 25) that implied volatility — the market's forecast of future movement, baked into every option's premium — is the single biggest hidden lever on whether your trade makes or loses money. You have learned that you want to *buy* options when volatility is cheap and *sell* them when it is rich. There is just one problem nobody warned you about: the IV number on your screen, all by itself, tells you almost nothing about whether it is cheap or rich.

Suppose Nifty's implied volatility is **18%**. Is that high or low? You genuinely cannot say. For a sleepy large-cap during a calm year, 18% might be sky-high. For Bank Nifty in the middle of an election or a banking scare, 18% might be unusually *low*. An absolute IV number without context is like being told a stock trades at ₹500 — it means nothing until you know whether ₹500 is near its yearly high, its yearly low, or somewhere in between. This chapter gives you the two tools professionals use to supply that missing context: **IV Rank** and **IV Percentile**. They turn a meaningless raw number into a clear verdict — *cheap, rich, or in the middle* — relative to the underlying's own recent history.

## Core concepts

### Why the absolute IV number is not enough

Every underlying has its own personality. Volatility is not a universal constant; it is a property of the specific instrument, and each instrument lives in its own range. A stable index like **Nifty** typically lives in a low IV band — often around 10% to 16% in calm regimes, spiking only around big events. **Bank Nifty** is structurally more volatile (banks are leveraged, rate-sensitive, news-driven), so its band sits higher and swings wider. A single **mid-cap stock** might routinely carry 30%+ IV, while 30% on Nifty would signal genuine panic.

So the same IV number means completely different things on different underlyings. "Reliance IV is 25%" is only useful if you know where 25% sits in *Reliance's own* history. If Reliance has spent the year between 20% and 45%, then 25% is on the cheap side; if between 18% and 27%, it is expensive.

The fix is to stop looking at IV in absolute terms and ask a relative question: **"Where does today's IV sit compared to where this same underlying's IV has been over the past year?"** That single re-framing is the heart of the chapter. Two standard tools answer it — IV Rank and IV Percentile — and although they sound similar and often agree, they measure subtly different things.

### IV Rank: where you sit between the low and the high

**IV Rank** asks the simplest possible version of the question: between the lowest IV and the highest IV of the past year, where does today's IV fall? It places today's reading on a 0-to-100 scale stretched between the 52-week low and the 52-week high.

```
IV Rank = (current IV - 1yr low IV) / (1yr high IV - 1yr low IV) * 100
```

Read it like a thermometer with the bottom fixed at the year's coldest reading and the top at its hottest:

- **IV Rank = 0** means today's IV equals the lowest it has been all year. Volatility is at rock bottom — options are as cheap, relative to this underlying's own range, as they get.
- **IV Rank = 100** means today's IV equals the highest it has been all year. Volatility is at its peak — options are as rich as they have been.
- **IV Rank = 50** means today's IV sits exactly halfway between the year's low and high.

The beauty of IV Rank is that it is dimensionless and self-calibrating. You no longer need to remember that "18% is high for Nifty but low for Bank Nifty" — the formula bakes each underlying's own range into the answer. An IV Rank of 80 means "near the top of its own range" whether the underlying is Nifty, Bank Nifty, or HDFC Bank.

### IV Percentile: how often IV has been below today

**IV Percentile** asks a different question. Instead of "where do I sit between the extremes?", it asks: **"On what fraction of trading days over the past year was IV *below* where it is today?"**

```
IV Percentile = (number of trading days in past year with IV below today's IV) / (total trading days in past year) * 100
```

So an IV Percentile of 90 means that on 90% of the days in the last year, IV was lower than it is right now — today is in the top 10% of readings. An IV Percentile of 20 means IV was below today's level only 20% of the time — today is unusually low; on 80% of days it was higher.

The crucial difference from IV Rank: **IV Percentile counts days, so it is not distorted by a single freak spike.** IV Rank only cares about the highest and lowest points of the year — two numbers. If a one-day panic pushed IV to an extreme that then vanished, that single spike permanently raises the "1yr high" in the IV Rank formula, dragging every later IV Rank reading down even though IV has been normal since. IV Percentile is immune to this — that freak spike is one or two days out of ~250, so it barely moves the count.

A worked feel for the contrast: an underlying sits at a calm 12% IV almost all year, except one chaotic week when IV briefly hit 40%. Today IV is 16%, modestly elevated.
- **IV Rank** = (16 - 12) / (40 - 12) * 100 ≈ **14** — looks low, because that lonely 40% spike stretched the top of the scale far away.
- **IV Percentile** might be **85**, because on the vast majority of days IV was below 16% — today really is on the high side relative to normal life.

When the two disagree, IV Percentile is usually the more trustworthy read of "is this elevated relative to a typical day", precisely because it is robust to outliers. (Note: Indian retail platforms vary in what they display — some show "IV Rank", some "IV Percentile", some mislabel one as the other — so always check which definition your tool uses.)

### How to use them: sell high, buy low

Once you can read these numbers, a clean default policy emerges, and it follows directly from the central fact about implied volatility: **IV mean-reverts.** Volatility does not trend forever. It is elastic — when it stretches high it tends to snap back down, and when it gets crushed to lows it tends to drift back up. Fear fades; calm gets interrupted. This pull toward a "normal" level is the engine behind the whole strategy.

**When IV Rank / IV Percentile is HIGH (say above ~70):** options are expensive relative to this underlying's own history. Premiums are fat. If IV is likely to mean-revert *downward*, you want to be the one *collecting* that rich premium and profiting as it deflates. This favours **selling premium** with defined-risk structures wherever possible:

- **Credit spreads** (bull put spread, bear call spread) — sell a richly priced option, buy a further one for protection.
- **Iron condors** — sell both a call spread and a put spread; a market-neutral way to harvest high IV with capped risk.
- **Short strangles / short straddles** — the purest premium-selling structures, but with large and (for naked strangles) effectively unlimited risk, so reserved for experienced traders with strict sizing.

You are short vega. As IV mean-reverts down, the options you sold lose value, and you buy them back cheaper — the IV crush works *for* you.

**When IV Rank / IV Percentile is LOW (say below ~30):** options are cheap relative to history. Premiums are thin. Selling them collects little and exposes you to an IV *expansion* (IV snapping back up), which hurts a short-vega position. So low IV favours either **buying options** to be long vega, or simply **waiting**:

- **Debit spreads** (bull call spread, bear put spread) — directional bets that are cheaper to put on when IV is low.
- **Long straddles / strangles** — near-pure long-volatility bets, attractive when IV is depressed and you expect it to rise (e.g., a quiet market before a known catalyst).
- **Doing nothing** — a completely legitimate "strategy". If IV is mediocre and nothing is mispriced, the professional often just waits for a better pitch.

You are long vega. If IV mean-reverts *up* (or a catalyst spikes it), your options gain value from the vega expansion, on top of any directional move.

**When IV Rank / IV Percentile is in the MIDDLE (~30–70):** there is no strong volatility edge either way. Trade on other merits (direction, structure) or stand aside. Do not force a premium-selling or premium-buying thesis when volatility itself is offering no signal.

The slogan to memorise: **sell high IV, buy low IV.** You are trying to be a volatility *contrarian* — selling fear when premiums are bloated, buying calm when premiums are cheap — and letting mean reversion do the work.

### Applying it to India VIX and to single stocks

You can apply the same ranking logic at two levels.

**Index level — India VIX.** India VIX (Chapter 25) is itself a tradable, observable measure of 30-day Nifty implied volatility, and the NSE publishes its full history, so you can compute an "IV Rank of India VIX" or simply eyeball where VIX sits in its own range. Historically it has spent long stretches in the low-to-mid teens, with sharp spikes (into the 20s, 30s, far higher in crises like March 2020) around elections, the Budget, RBI shocks, and global risk-off — followed by a reliable drift back down. When India VIX is near the bottom of its range, Nifty and Bank Nifty options are broadly cheap (favour buying); near the top, broadly rich (favour selling). VIX is your top-down read on the whole index-options market.

**Single-stock level.** For individual F&O stocks, you compute IV Rank / IV Percentile on *that stock's own* IV series. This is where the tool earns its keep, because stock IV is dominated by the **earnings cycle**: IV ramps up in the days before quarterly results and crushes the morning after. A stock can show a sky-high IV Rank purely because results are two days away — a *justified* high, not a free edge (more below). Single-stock IV Rank is essential because each stock's "normal" band differs; you cannot eyeball it the way you can a familiar index.

A practical workflow: check India VIX first for the market-wide weather, then the specific underlying's IV Rank for local conditions, *then* decide whether you are structurally a buyer or seller of premium on that name today.

### The discipline — and its limits

"Sell high IV, buy low IV" is a genuine, durable edge, but it is a *tendency*, not a law, and treating it as a law is how traders blow up. The single most important caveat:

**High IV is often high for a reason.** Implied volatility is the market's forecast of future movement, and sometimes the market is forecasting correctly — real, large risk is genuinely coming. A high IV Rank ahead of a national election result, a critical RBI decision, a company's earnings, or during a credit crisis is not a gift; it is the market *correctly* pricing a wide range of outcomes. If you sell that "expensive" premium and the feared move actually materialises — Bank Nifty gaps 1,500 points on a banking shock — your short-vega, short-gamma position can lose far more than the premium you collected. The premium was high because the danger was real.

So the discipline has rules of engagement:

- **Do not sell premium naked into a binary event you cannot withstand.** High IV Rank into earnings or an election is exactly when a *defined-risk* structure (iron condor, credit spread) matters most, so a surprise move cannot bankrupt you.
- **IV Rank tells you premium is rich; it does not tell you the move won't happen.** Mean reversion is the base rate, not a guarantee. You are collecting an edge that pays off *on average over many trades*, while any single trade can deliver the tail.
- **Low IV can persist, and can fall further.** Buying options because IV is "cheap" still bleeds theta every day while you wait for an expansion that may never come. Cheap can get cheaper, and a low-IV long-vega position dies slowly by time decay if the catalyst fizzles.
- **Position size around the regime.** Sell *less* size when the high IV reflects genuine event risk; the rich premium is compensation for that risk, not a free lunch.

The mature framing: IV Rank and IV Percentile tell you whether you are being *paid well* to take volatility risk, or *charged little* to own it. They do not tell you whether the risk will show up. You still have to ask, every time, *why* is IV where it is — and whether you can survive the case where the market's forecast turns out to be right.

## Worked example (₹, Nifty / Bank Nifty)

Let us compute both metrics on real-feeling numbers and turn them into a trade decision.

**Setup.** You are looking at Bank Nifty, spot around **52,000**. You pull up its implied volatility history for the past year and read off:

- **52-week low IV:** 11%
- **52-week high IV:** 31% (hit during a one-week banking scare months ago)
- **Current IV:** 17%
- Over the past ~250 trading days, IV was below 17% on **180** of those days.

There are no major scheduled events this week.

**Step 1 — Compute IV Rank.**

```
IV Rank = (current IV - 1yr low) / (1yr high - 1yr low) * 100
        = (17 - 11) / (31 - 11) * 100
        = 6 / 20 * 100
        = 30
```

IV Rank is **30**. On the low-to-high scale, today's 17% sits only 30% of the way up from the year's floor. That single 31% banking-scare spike stretched the top of the range, so 17% looks relatively modest.

**Step 2 — Compute IV Percentile.**

```
IV Percentile = (days with IV below today) / (total days) * 100
              = 180 / 250 * 100
              = 72
```

IV Percentile is **72**. On 72% of days this year, IV was *below* today's 17% — meaning today is actually on the higher side of a *typical* day.

**Step 3 — Reconcile the disagreement.** IV Rank (30) says "low-ish"; IV Percentile (72) says "high-ish". This is the classic outlier divergence: the lone 31% spike inflated the high used by IV Rank, dragging it down, while IV Percentile — which counts days — shows that relative to ordinary trading life, 17% is genuinely elevated. Here, IV Percentile is the more honest read of "is this rich versus a normal day", and it says *yes, modestly*. The raw absolute number (17%) told you none of this.

**Step 4 — Choose a strategy.** Two metrics — one leaning "rich" (Percentile 72), one "neutral-to-cheap" (Rank 30) — with **no scheduled event** to justify a fear premium. Net read: premium is somewhat rich relative to a normal day, with no obvious real-risk catalyst — a measured environment to **sell premium with defined risk**. You choose a **Bank Nifty iron condor**: sell an out-of-the-money call spread and an out-of-the-money put spread, collecting the elevated premium with both wings capping your loss. You are short vega and market-neutral; if IV mean-reverts toward its low-teens norm and Bank Nifty stays in a range, the position profits as premiums deflate.

**Step 5 — Size for the caveat.** Because IV Rank is only 30 (not screaming-rich), you keep size modest — there is an edge here, but not a fat one. Crucially, had this same 17% come *the day before a major RBI policy decision*, the high IV would be a *justified* event premium: you would widen the wings, cut size further, or stand aside rather than sell cheap-looking insurance against a real shock. Same numbers, different context, different decision — exactly the discipline these metrics are meant to support, not replace.

## Common mistakes / risk note

- **Judging IV by its absolute number.** "18% IV, that's high" is meaningless without the underlying's own range. Always rank it. 18% can be a screaming sell on calm Nifty and a relative *buy* on stormy Bank Nifty.
- **Using only IV Rank when a freak spike has poisoned the range.** A single panic day permanently lifts the "1yr high" and suppresses every later IV Rank reading. When IV Rank looks oddly low but the market feels jumpy, check IV Percentile — it is robust to outliers and often the truer signal.
- **Selling rich premium blindly into events.** The most dangerous mistake. High IV Rank before earnings, elections, or RBI policy is the market *correctly* pricing real risk. Selling naked premium there can deliver a catastrophic loss when the feared move actually lands. Use defined-risk structures and cut size into binary events.
- **Buying cheap IV and ignoring theta.** Low IV Rank makes long options attractive *only if* IV expands or a move comes. While you wait, theta bleeds you daily. "Cheap" can stay cheap for months; long vega is not a free option, it is a wager you are paying carry on.
- **Forgetting mean reversion is a base rate, not a guarantee.** IV Rank gives you an edge that pays *on average across many trades*. Any single trade can hand you the tail. Size and diversify so that the inevitable bad outcome is survivable.
- **Trusting your platform's label blindly.** Some Indian tools show IV Rank, some IV Percentile, and some mislabel one as the other or use a lookback different from 52 weeks. Know which metric and which window you are actually reading.

## Key takeaways

- The **absolute IV number is not enough** — you must judge it relative to the underlying's *own* recent history. Each instrument has its own volatility personality.
- **IV Rank** places today's IV on a 0–100 scale between the 52-week low and high: `IV Rank = (current IV - 1yr low) / (1yr high - 1yr low) * 100`. 0 = cheapest of the year, 100 = richest.
- **IV Percentile** = the percentage of trading days in the past year that IV was *below* today's level. It counts days, so it is **robust to one-off spikes** that distort IV Rank.
- When the two disagree, a lone outlier spike is usually the cause; **IV Percentile is typically the more reliable read** of "elevated versus a normal day".
- **Sell high IV, buy low IV.** High IV Rank/Percentile favours *selling* premium (credit spreads, iron condors, short strangles) to harvest mean reversion down; low IV favours *buying* options (debit spreads, long straddles) or waiting.
- Apply it at two levels: **India VIX** for the whole index-options market, and **single-stock IV Rank** for individual F&O names (dominated by the earnings cycle).
- The discipline's limit: **high IV is often high for a real reason.** A justified event premium is not free money. Use defined risk, cut size into binary events, and always ask *why* IV is where it is.

## Practice problems

1. **Why context matters.** Two underlyings both show an implied volatility of exactly 22% today. Underlying A is a stable large-cap that has spent the year between 18% and 27% IV. Underlying B is a volatile mid-cap that has spent the year between 20% and 60% IV. For each, is 22% relatively rich or cheap? Explain why the same number means opposite things.

2. **Compute IV Rank (numeric).** Nifty's 52-week low IV is 10%, its 52-week high IV is 24%, and current IV is 19%. Compute the IV Rank. Does this favour buying or selling premium, all else equal?

3. **Compute IV Percentile (numeric).** Over the past 250 trading days, a stock's IV was below today's level on 45 of them. Compute the IV Percentile. Is today's IV high or low relative to a typical day this year?

4. **When the two disagree.** A stock spent almost the whole year around 14% IV, except one crisis week when IV briefly hit 50%. Today IV is 20%. Its IV Rank works out to about 17, but its IV Percentile is about 88. Which metric better describes whether IV is elevated *right now*, and why are they so far apart?

5. **Strategy choice.** Bank Nifty's IV Rank is 85 and its IV Percentile is 82, with a major RBI monetary policy decision due in two days. A friend says, "IV is super rich — let's sell a naked short strangle and collect that fat premium." What is right and what is dangerous about this plan, and how would you modify it?

6. **Low IV decision.** Nifty's India VIX is near a multi-month low and its IV Rank is 15. You have no strong directional view and no known catalyst this month. What does the IV picture suggest about selling premium here, and what are your reasonable options?

## Solutions

1. **A is rich; B is cheap.** For Underlying A, 22% sits in the upper part of its 18%–27% range — IV Rank = (22 - 18) / (27 - 18) * 100 ≈ 44, and more tellingly it is well above its floor, so 22% is relatively *rich* for A; premium-selling is favoured. For Underlying B, 22% sits near the *bottom* of its 20%–60% range — IV Rank = (22 - 20) / (60 - 20) * 100 = 5, so 22% is *cheap* for B; buying premium (or waiting) is favoured. The same absolute number is rich on one and cheap on the other because each underlying has its own volatility range. This is precisely why the absolute IV figure is useless without ranking it against the instrument's own history.

2. `IV Rank = (19 - 10) / (24 - 10) * 100 = 9 / 14 * 100 ≈ 64`. An IV Rank of about **64** is moderately high — current IV sits roughly two-thirds of the way up its yearly range. All else equal, this leans toward **selling premium** (the options are on the richer side relative to history), preferably with a defined-risk structure. It is elevated but not extreme, so size accordingly and check whether any event is driving it.

3. `IV Percentile = 45 / 250 * 100 = 18`. An IV Percentile of **18** means IV was below today's level on only 18% of days this year — equivalently, IV was *higher* than today on 82% of days. So today's IV is **low** relative to a typical day. This favours **buying** options (long vega) or waiting, rather than selling cheap premium. Selling here would collect little and expose you to an IV expansion back toward the year's more common, higher levels.

4. **IV Percentile (88) better describes the present.** They diverge because of the single 50% crisis-week spike. IV Rank only uses the year's high and low: that lone 50% reading became the "1yr high", stretching the top of the scale so far that today's 20% looks like only 17% of the way up — IV Rank is dragged artificially low by one outlier. IV Percentile counts days: since the stock spent almost the whole year around 14% and is now at 20%, IV is above where it was on ~88% of days, correctly flagging today as genuinely elevated. When a freak spike has poisoned the range, trust IV Percentile — it is robust to outliers, while IV Rank is distorted by the two extreme points.

5. **What's right:** IV Rank 85 and IV Percentile 82 both confirm premium is genuinely rich versus history, and rich premium is, in principle, attractive to a seller. **What's dangerous:** the high IV is largely *justified* — a major RBI decision in two days is a real binary catalyst, and the market is correctly pricing a wide range of outcomes. A **naked short strangle** has effectively unlimited risk; if Bank Nifty gaps hard on a policy surprise, the loss can dwarf the premium collected, and IV could even spike *further* before the event. **How to modify:** do not sell naked into the event. Use a **defined-risk iron condor** (buy protective wings so the maximum loss is capped), cut the position size sharply to reflect the real event risk, consider waiting until *after* the decision when the IV crush has occurred and the binary risk is gone, or simply stand aside. The rich premium is compensation for genuine danger, not free money.

6. With India VIX near multi-month lows and IV Rank at **15**, options are **cheap** relative to Nifty's own history. Premium-selling is *unattractive* here: you would collect thin premium while exposing yourself to an IV *expansion* (volatility snapping back up) that would hurt a short-vega position. Reasonable options: (a) **do nothing** — a perfectly legitimate choice when volatility offers no selling edge and you have no view; (b) if you expect volatility to rise, **buy** a long-vega structure such as a long straddle or a debit spread to profit from an IV expansion — but respect that you will bleed theta while you wait and that cheap IV can stay cheap or fall further. With no catalyst and no directional view, patience is usually the professional's answer: wait for IV to richen before becoming a seller, or for a clear setup before becoming a buyer.
