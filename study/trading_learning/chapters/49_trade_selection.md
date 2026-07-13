# Chapter 49: Trade Selection & Entry — Finding A+ Setups

Imagine a professional cricket batsman at the crease. The bowler sends down six balls an over, but the batsman does not swing at all six. He lets the wide ones go, blocks the dangerous ones, and waits — sometimes for several overs — until a loose ball arrives that he can put away for four. His edge is not that he hits harder than everyone else. His edge is *discipline about which balls to play*. The amateur, by contrast, swings at everything, gets bowled chasing a wide one, and walks back to the pavilion wondering what went wrong.

Options trading is exactly this game. The market bowls you dozens of "setups" a week — every strike, every expiry, every twitch of Nifty looks like an opportunity if you squint. The losing trader plays all of them. The professional has a pre-trade *checklist* that filters out the wides and the dangerous ones, and only swings when an **A+ setup** arrives: a trade where the direction, the volatility regime, the calendar, and the liquidity all line up in his favour. This chapter is that checklist. It turns "should I trade this?" from a feeling into a procedure — and teaches you the single most profitable skill in all of trading, which is the discipline of *waiting*.

## Core concepts

### What is an "A+ setup"?

An A+ setup is a trade where *every* box on your checklist is ticked at once — not three out of four, but all of them. Think of it as the alignment of four independent forces:

1. **A clear structural read of the underlying** — you can point to the trend and the key levels and say *why* you lean up, down, or sideways.
2. **A favourable volatility regime** — implied volatility (IV) is priced in your favour: cheap when you want to buy options, rich when you want to sell them.
3. **A clean event calendar** — you know what is coming (results, Budget, RBI policy, expiry) and you are deliberately either avoiding it or exploiting it, never blindsided by it.
4. **Healthy liquidity** — the strikes you want to trade have tight bid-ask spreads and real open interest, so you can get in and out at fair prices.

Most trades fail the test. That is the point. If you find that only one or two trades a week pass all four filters, the checklist is working. The amateur's mistake is to relax the standard until *something* qualifies every day; the professional's edge is to keep the standard high and **let unqualified trades go by, unplayed.**

### Filter 1 — the structural read of the underlying

Before you ever look at an option chain, look at the *underlying* — Nifty or Bank Nifty itself — on a price chart. You are answering one question: **what is the path of least resistance?** You do not need a hundred indicators; you need three honest observations.

- **Trend.** Is the index making higher highs and higher lows (uptrend), lower highs and lower lows (downtrend), or chopping sideways in a band (range)? A simple way to read this is the slope of a moving average — say the 20-day exponential moving average. Price above a rising average is an uptrend; price below a falling one is a downtrend; price weaving through a flat one is a range. Trade *with* the trend unless you have a specific, well-argued reason to fade it.
- **Key support and resistance levels.** These are the prices where the index has repeatedly turned before — round numbers (24,000 / 52,000), recent swing highs and lows, the previous day's high/low, and the prior week's range. Support is a floor where buyers tend to step in; resistance is a ceiling where sellers tend to appear. A bullish trade taken *just above* strong support has a natural place to put a stop and a clear target at the next resistance.
- **Confirming technicals.** A couple of simple tools sharpen the read: the Relative Strength Index (RSI) tells you if a move is overextended (above ~70 overbought, below ~30 oversold); volume tells you whether a breakout has conviction behind it. Keep it minimal — more indicators mostly add noise and false confidence.

The output of this filter is a single sentence you must be able to say out loud, for example: *"Nifty is in a mild uptrend, sitting just above 24,000 support, with RSI neutral at 55, so I lean mildly bullish with a target near 24,300 and a line in the sand at 23,850."* If you cannot say a sentence like that, you have **no directional read**, and you should stop here.

### Filter 2 — the IV regime (is volatility cheap or rich?)

A correct directional view can still lose money if you express it with mispriced options. The second filter asks: **are options expensive or cheap right now, relative to their own history?** The tool for this is **IV rank** (introduced in the volatility chapters), which places current IV on a 0–100 scale between its 1-year low and high:

`IV rank = (current IV - 52-week low IV) / (52-week high IV - 52-week low IV) * 100`

You can read the same regime quickly from **India VIX**, the index of Nifty implied volatility — a VIX near its yearly lows signals cheap options; a spiking VIX signals rich ones.

The discipline is mechanical:

- **High IV rank (say above 50) — options are RICH.** You are being paid fat premiums. This favours **selling** premium: credit spreads, iron condors, short strangles. You profit both from being right on direction *and* from that rich IV deflating back toward normal.
- **Low IV rank (say below 25) — options are CHEAP.** Premiums are thin. This favours **buying** options or using long-vega structures: long calls/puts, debit spreads, calendars. You profit if IV expands.

This is the rule **"sell high IV, buy low IV."** It is the filter that separates a directional view from a *tradeable* directional view. Being bullish does not automatically mean "buy a call" — if IV rank is 80, buying that call means paying a rich premium that an experienced trader is happily *selling* to you. In a rich regime, the disciplined way to be bullish is often to *sell* a put credit spread instead. The volatility regime decides *how* you express the view; never let it be an afterthought.

### Filter 3 — the event calendar

Options are pricing machines for *uncertainty*, and scheduled events are the biggest, most predictable lumps of uncertainty there are. The third filter forces you to look at the calendar *before* you enter, never after. The events that matter most in the Indian market:

- **Corporate results** — earnings season for individual F&O stocks (and the heavyweight names that move Bank Nifty, like HDFC Bank, ICICI, SBI).
- **The Union Budget** — usually 1 February; one of the largest single-day volatility events of the Indian year.
- **RBI monetary policy** — the bi-monthly rate decisions, which whip Bank Nifty around hardest.
- **Weekly and monthly expiry** — gamma and theta behave violently in the final hours; the last day is its own kind of event.
- **Macro prints and global cues** — domestic CPI/GDP, US Fed decisions, and overnight gaps from global markets.

There are two legitimate ways to use this filter, and one fatal way to ignore it:

- **Avoid the event.** If you have a calm, premium-selling trade on and a major event sits inside its life, IV will be inflated going in and can gap violently coming out. Often the right move is simply to *not* be in that trade across the event, or to choose an expiry that ends before it.
- **Exploit the event deliberately.** Events are also where the biggest opportunities live — but only if you *plan* for them. Before an event, IV inflates; after it, IV collapses (**IV crush**). A trader who understands this might *sell* the inflated premium and profit from the post-event crush, or, if IV is somehow still cheap, *buy* a straddle to own the move. The key word is *deliberately*.
- **The fatal mistake — being blindsided.** Buying a cheap-looking straddle the morning of RBI policy, not realising IV is already at rank 90, then watching the index move 250 points *and still losing* because IV crushed. The event was on the calendar in plain sight; the trader simply never looked.

The output of this filter is one sentence: *"The next major event is RBI policy in eight days; my weekly trade expires before it, so I am clear."* Or: *"Results are tomorrow — IV rank is 85 — I will sell premium to harvest the crush, not buy it."*

### Filter 4 — liquidity

The most beautiful setup on paper is worthless if you cannot get in and out at a fair price. The fourth filter is the one beginners skip and professionals never do, because it costs them real money on every single trade. Check three things on the option chain before you commit:

- **Tight bid-ask spread.** The bid is what buyers offer; the ask is what sellers want; the gap between them is a cost you pay twice (entering and exiting). On liquid Nifty/Bank Nifty weekly strikes near the money, this gap might be ₹0.50–₹2. On an illiquid far-out strike or a deep monthly, it can be ₹15–₹40 — meaning you start the trade already down a large chunk. **Trade where the spread is tight.**
- **Healthy open interest (OI) and volume.** Open interest is the number of live contracts at a strike; volume is how many traded today. High OI and volume mean many participants, which means you can transact size without moving the price. Thin OI means you may not find a counterparty when you desperately want out.
- **Stick to liquid strikes.** In practice this means: **Nifty and Bank Nifty index options, near-the-money strikes, in the current or next weekly/monthly expiry.** Avoid deep out-of-the-money "lottery ticket" strikes and far-dated months where liquidity dries up. The whole-rupee Nifty strikes (multiples of 50) and Bank Nifty strikes (multiples of 100) closest to spot are where the liquidity lives.

A useful mental rule: **if you cannot exit a position as easily as you entered it, you do not have a position — you have a trap.**

### The pre-trade checklist (run this every single time)

Put the four filters together with sizing and an exit, and you have the full A+ checklist. If any line cannot be filled, the trade is not A+ and you pass:

1. **Structural read:** trend (up/down/range) + key level + one technical. Can I say the one-sentence view?
2. **IV regime:** IV rank high (sell) or low (buy)? Does my expression match?
3. **Calendar:** what is the next event, and am I avoiding it or exploiting it on purpose?
4. **Liquidity:** tight spread, healthy OI, liquid strike?
5. **Strategy alignment:** does the structure (from the Chapter 37 framework) match all of the above?
6. **Size:** lots = (capital * risk%) / (max loss per lot), risking 1–2% of capital.
7. **Exit plan:** my profit-target and stop-loss, decided *now*, before entry.

If all seven are green, it is an A+ setup. If even one is amber, it is a B trade — and B trades are how accounts die by a thousand cuts.

### Aligning the strategy with the read

The checklist feeds directly into the strategy-selection framework of Chapter 37 (view x volatility x risk). The four filters *are* the inputs to that framework:

- **Filter 1 (structural read)** supplies the **directional view** — bullish, bearish, neutral, or unsure-on-direction.
- **Filter 2 (IV regime)** supplies the **volatility view** — whether to buy or sell premium.
- **Filter 3 (calendar)** and **Filter 4 (liquidity)** decide *whether to trade at all* and *which expiry/strikes* to use.

So a bullish read in a *cheap* IV regime points to a **long call or bull call (debit) spread**; the same bullish read in a *rich* IV regime points instead to a **bull put (credit) spread**. A neutral read with rich IV points to an **iron condor**; a neutral read with cheap IV points to a **long butterfly** or **calendar**. The checklist does not replace the strategy map — it *fills it in*. You never start from "I want to trade an iron condor"; you start from the four filters and let the structure fall out.

### The discipline of waiting — and the curse of overtrading

Everything above is the *technical* half of trade selection. The harder half is *behavioural*, and it is where most of the 9-in-10 retail F&O traders SEBI studies are talking about actually lose their money. **Overtrading is the number one retail killer.** Not bad strategy, not the wrong Greek — simply trading too often, too big, on setups that were never A+.

Why is it so deadly?

- **Costs compound.** Every trade pays brokerage, STT, exchange fees, and the bid-ask spread. Twenty mediocre trades a week can bleed a small account dry on costs alone, *even if the trades break even on price.*
- **Mediocre setups have no edge.** A B trade is, by definition, a coin flip with costs attached — and a coin flip minus costs is a guaranteed slow loss.
- **Boredom and revenge are not strategies.** Most overtrading comes from emotion: boredom ("the market's quiet, let me do *something*"), revenge ("I'll make that loss back right now"), or FOMO ("everyone's making money on this move"). None of these is on the checklist, because none of them is an edge.

The professional's secret is uncomfortable: **most of the time, the correct trade is no trade.** Sitting in cash, waiting, is an active, skilled decision — it is the batsman leaving the wide ball. A useful self-imposed rule for a developing trader is a hard cap, for example *"no more than two new positions a week, and only A+ setups,"* which physically forces selectivity until it becomes a habit. You will be astonished how much your results improve simply by *not* taking the B trades. (Later in the book we will build your own screening tools to surface A+ setups automatically — but the discipline must come first; a screener only helps a trader who is willing to wait.)

### Entry tactics — getting filled without giving money away

Once a setup passes the checklist, *how* you enter matters. Sloppy entries hand free money to the market maker.

- **Use limit orders, not market orders.** A market order says "fill me at any price" and on an options book that can mean a terrible price, especially when the spread is wide. A **limit order** lets you specify the price you will accept — typically aim to get filled near the *mid-price* (halfway between bid and ask), not by crossing the full spread.
- **Do not chase.** If the index has already run 200 points in your direction, the easy part of the move is gone and you are now buying at the worst price, often into a pullback. The setup was *before* the move, not after it. A missed trade costs you nothing; a chased trade costs you real money. There is always another bus.
- **Scale in (and out).** You do not have to put the whole position on at once. Entering in two or three tranches lets you build into a level rather than betting everything on a single tick, and averages your entry price. Equally, scaling *out* — booking part of the position at the first target and trailing the rest — locks in gains while keeping upside. Scaling is how professionals manage uncertainty about *exact* timing.
- **Mind the time of day.** The opening minutes (9:15–9:30) are noisy with overnight-gap volatility and wide spreads; the close is rushed. Many disciplined index traders prefer to enter once the open settles, when spreads tighten and the day's character is clearer.

## Worked example (₹, Nifty/Bank Nifty)

It is a Wednesday morning. **Nifty is at 24,050.** Let us run a single setup through the full checklist and see whether it earns a place — and which trade it becomes.

**Filter 1 — structural read.** On the daily chart, Nifty has made higher highs and higher lows for three weeks and sits just above the **24,000 round-number support**, with the 20-day EMA rising beneath price. RSI is a neutral 56 — trending, not overbought. The previous swing high (resistance) is near **24,350**. *Read: mild uptrend, leaning bullish, target ~24,300, line in the sand below 23,900.* **Green.**

**Filter 2 — IV regime.** India VIX is elevated and the weekly options carry an **IV rank of about 68** — options are RICH. The "sell high IV" rule says: express this bullish view by *selling* premium, not buying it. A long call here would mean paying inflated premium and fighting potential IV crush. **Green, with a clear instruction: sell premium.**

**Filter 3 — calendar.** You check: the next RBI policy is 11 days away; no index-moving results today; today is *not* expiry day (that is tomorrow's monthly, but you will trade the *next* weekly, which expires cleanly with no event inside its life). **Green — clear runway.**

**Filter 4 — liquidity.** You pull up the weekly chain. The 23,900 and 23,700 puts (both near the money, multiples of 50) show **bid-ask spreads of about ₹1–₹1.50 and open interest in the lakhs of contracts.** Deeply liquid. **Green.**

**All four filters green — this is an A+ setup.** Now align the strategy. Bullish + rich IV + defined risk points (per the Chapter 37 map) to a **bull put spread** — sell a put credit spread below the market.

**Build it.** Sell the 23,900 put, buy the 23,700 put (a 200-point-wide spread, both below the 24,050 spot):

- Sell 23,900 put: collect about **₹125** per unit.
- Buy 23,700 put: pay about **₹62** per unit.
- **Net credit = 125 - 62 = ₹63** per unit. Nifty lot size is **75**.

**Per-lot economics.**

- Net credit per lot = `63 * 75 = ₹4,725` (maximum profit).
- Spread width = `23,900 - 23,700 = 200` points.
- Max loss per unit = `width - net credit = 200 - 63 = ₹137`; per lot = `137 * 75 = ₹10,275` (maximum loss).
- Breakeven = `23,900 - 63 = 23,837`. You profit as long as Nifty expires above 23,837 — comfortably below the 24,000 support you identified.

**Size it.** Capital ₹5,00,000, risking 2% = ₹10,000. `Lots = 10,000 / 10,275 = 0.97`, round down to **1 lot.** Two lots would risk ₹20,550 and break the rule, so you trade exactly one.

**Enter it.** You place a **limit order** on the spread aiming for the mid-price (a net credit near ₹63), rather than a market order that would cross both wide-ish spreads. The order does not fill at ₹63 immediately, so you wait two minutes and adjust to ₹61 — still a fair fill, and you do *not* chase it down to a poor price. Filled at ₹62 net.

**Plan the exit before walking away.** You decide *now*: take profit at roughly 50% of max (buy the spread back near ₹31 to bank about ₹2,300), and stop out if the loss reaches your ₹10,000 budget or if Nifty closes decisively below the 23,900 short strike. The trade was *selected by procedure* — four green filters, one structure, one lot, one planned exit — not grabbed on a hunch.

## Common mistakes / risk note

- **Lowering the bar until something qualifies.** The checklist only works if you let unqualified trades go. A trader who "needs" a trade today will always find an excuse to call a B setup an A+. Boredom is not a signal.
- **Skipping the liquidity filter.** Beautiful setups in illiquid strikes get eaten alive by the bid-ask spread on entry *and* exit. The spread is a guaranteed cost; OI is your escape hatch. Never ignore them.
- **Being blindsided by the calendar.** "I didn't know RBI was today" is not bad luck — it is a failure to look. Every event is published in advance. Check the calendar *before* entry, every time.
- **Overtrading — the silent killer.** Far more accounts die from too many mediocre trades than from a few bad ones. Costs and coin-flips compound. If you take only the A+ setups, you will trade far less than feels comfortable — that discomfort *is* the discipline working.
- **Chasing entries.** Buying after a 200-point run, crossing the full spread on a market order, doubling down to "make it back." The setup was before the move. A missed trade costs nothing; a chased one costs real money.
- **The honest truth.** SEBI studies show roughly nine in ten retail F&O traders lose money, and the common thread is over-frequency and poor selection, not exotic strategy errors. A boring, selective, checklist-driven trader who waits for A+ setups is already in a different league from the average participant.

## Key takeaways

- An **A+ setup** is one where *all four* filters align: a clear structural read, a favourable IV regime, a clean event calendar, and healthy liquidity. Three out of four is a pass, not a trade.
- **Structural read** gives direction (trend + key level + one technical); **IV regime** (IV rank / India VIX) decides whether to buy or sell premium — "sell high IV, buy low IV."
- **Always check the event calendar** (results, Budget, RBI, expiry) before entering — avoid the event or exploit it deliberately, never get blindsided.
- **Trade only liquid strikes** — tight bid-ask, healthy OI, near-the-money Nifty/Bank Nifty weeklies — because spreads are a cost you pay on the way in *and* out.
- The four filters feed directly into the Chapter 37 strategy framework; the same bullish view becomes a debit spread in cheap IV but a credit spread in rich IV.
- **Overtrading is the number one retail killer.** The most valuable skill is the discipline of *waiting* — most of the time, the right trade is no trade.
- **Enter with limit orders near mid-price, never chase, and scale in/out.** Plan your profit-target and stop-loss before you enter, while you are still calm.

## Practice problems

1. **(Conceptual)** A trader has a strongly bullish read on Bank Nifty: clear uptrend, price bouncing off support, RSI at 50. But IV rank is 82 (very rich). Should they buy a call or sell a bull put spread? Justify using the IV-regime filter.

2. **(Conceptual)** Explain why "I'm bored and the market is quiet, so I'll sell a small strangle for some income" is a checklist failure, even though selling premium in calm markets is a legitimate idea.

3. **(Application — calendar)** You want to hold a defined-risk, premium-selling weekly trade on Nifty. RBI policy is scheduled in four days, inside the life of the weekly you are considering. List two valid ways to handle this and one way that would be a mistake.

4. **(Numeric — liquidity cost)** A far-OTM Nifty strike shows a bid of ₹8 and an ask of ₹14; a near-the-money strike shows a bid of ₹120 and an ask of ₹121.50. For each, compute the bid-ask spread as a percentage of the mid-price. Which strike is tradeable, and why does this matter for round-trip cost?

5. **(Numeric — sizing)** Your capital is ₹4,00,000 and your rule is 1.5% risk per trade. An A+ Nifty bull put spread has a maximum loss of ₹8,200 per lot. How many lots can you trade, and what is the implication if the answer is below one lot?

6. **(Application)** Walk a setup through the four filters: Nifty is at 24,200 in a *sideways range* between 24,000 and 24,400; IV rank is 22 (cheap); no major events for two weeks; near-the-money strikes are liquid. Which filter combination is this, and which strategy family (aligned to Chapter 37) fits?

## Solutions

1. **Sell the bull put spread.** Both structures satisfy the bullish direction, so the IV-regime filter breaks the tie. With IV rank at 82, options are *rich*: buying a call means paying an inflated premium and exposing yourself to IV crush if volatility normalises — your volatility view works *against* a long option. Selling a bull put (credit) spread makes you the *seller* of that rich premium; you profit from the bullish drift *and* from rich IV deflating, with the long wing capping risk. "Sell high IV" applies.

2. **It fails Filters 1 and 3 and the overtrading rule, even if Filter 2 is fine.** Selling premium in a calm, rich-IV market is sound in principle — but "I'm bored" is not a structural read (Filter 1: no trend/level/technical view), there is no check that an event is not lurking (Filter 3), and the motivation is *boredom*, which is precisely the emotional driver behind overtrading. A legitimate idea expressed without the checklist and from emotion is still a B trade. The discipline is to wait for a calm market that *also* passes all four filters, not to manufacture a reason to trade.

3. **Two valid handlings:** (a) **Avoid it** — choose a weekly expiry that ends *before* the RBI announcement, so no event sits inside the trade's life; or (b) **Exploit it deliberately** — knowing IV will inflate into the event and crush afterwards, structure a defined-risk premium sale designed to harvest the post-event IV crush, sized for the gap risk. **The mistake:** entering a normal calm-market premium sale and simply *ignoring* the event — IV will be inflated going in and the index can gap violently coming out, blindsiding the position. The event is on the calendar; not looking is the error.

4. **Far-OTM strike:** mid = `(8 + 14)/2 = ₹11`; spread = `14 - 8 = ₹6`; as a % of mid = `6 / 11 = 54.5%`. **Near-the-money strike:** mid = `(120 + 121.50)/2 = ₹120.75`; spread = `121.50 - 120 = ₹1.50`; as a % of mid = `1.50 / 120.75 = 1.24%`. The near-the-money strike is tradeable; the far-OTM one is not. The spread is a cost paid on *both* entry and exit (round trip), so the far-OTM strike forces you to overcome a ~54% price gap just to break even on the spread — a brutal, hidden drag — whereas the liquid strike costs about 1%. This is why Filter 4 insists on liquid, near-the-money strikes.

5. **Risk budget = `4,00,000 * 0.015 = ₹6,000`.** `Lots = 6,000 / 8,200 = 0.73`, which rounds down to **0 lots.** The implication: even one lot (max loss ₹8,200) exceeds your ₹6,000 risk budget, so this trade is **too big for your account** — you must either find a tighter/cheaper structure (a narrower spread with a smaller per-lot loss) or skip the trade entirely. You never round *up* to one lot to force the trade in; that breaks the sizing rule and is exactly how a single bad trade does outsized damage.

6. **This is a *neutral / range* direction with a *cheap* IV regime, clean calendar, and good liquidity** — an A+ neutral setup, but on the *buy-vol* side of the IV filter. Because IV rank is only 22 (cheap), you do *not* sell premium (that would fight a likely IV expansion); instead you want a defined-risk, range-betting structure that benefits from cheap premium and rising IV. Per the Chapter 37 map, the fitting families are the **long butterfly** (buy it for a small known debit, max profit if Nifty pins near the body strike around 24,200) or a **calendar/diagonal spread**. The long butterfly is the cleaner defined-risk, beginner-appropriate choice: known small debit as maximum loss, profiting if the index stays range-bound near the body.
