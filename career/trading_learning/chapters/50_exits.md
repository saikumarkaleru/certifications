# Chapter 50: Exits — Profit Targets, Stop-Losses & Time Stops

Most beginners spend ninety percent of their energy on the *entry* — which strike, which expiry, bullish or bearish, the perfect moment to click "buy". They spend almost none on the *exit*. This is exactly backwards. Your entry decides whether you have a position; your **exit decides whether you make money**. Two traders can take the identical trade — same strike, same premium, same day — and one walks away with a profit while the other rides it to a loss, purely because of when and how they got out. The market does not pay you for being right; it pays you for *closing* while you are right.

Here is the single most important habit in this chapter, and arguably in the whole book: **plan your exits before you enter, not after.** Before you put on a trade you must already know three numbers — the price (or premium, or date) at which you take profit, the price at which you cut the loss, and the date by which you are out regardless. Decide all three when you are calm, neutral, and have no money on the line. Because the moment a position is live, your judgement is poisoned by hope, fear and the sunk-cost ache of a loss you don't want to "realise". A pre-written exit plan is the cold, sober version of you protecting the panicky, hopeful version of you from doing something stupid.

## Core concepts

### Why exits dominate entries

An option position is not a stock you can hold forever. It is a wasting asset with a deadline. Every day, theta (time decay) drains a long option and feeds a short one; near expiry, gamma (the rate at which delta changes) turns small moves into violent P&L swings. Because the instrument itself is changing under your feet, *when* you leave matters as much as *where* you entered.

Think of three traders who all bought the same Nifty call and watched it double. Trader A sold at the double and booked the win. Trader B held "for more", watched it round-trip back to the entry price, and broke even. Trader C held even longer, the move reversed, and the call expired worthless — a full loss on a trade that was once a 100% winner. Same entry, three completely different outcomes. The entry was *identical and good*; the exit was everything. This is why professionals obsess over exits and amateurs obsess over entries.

### The exit plan: three numbers, decided up front

For every single trade, write down before entry:

1. **Profit target** — where you take the win.
2. **Stop-loss** — where you cut the loss.
3. **Time stop** — the date/time by which you are flat no matter what.

If you cannot define all three before entering, you do not understand the trade well enough to be in it. These three together form a *bracket* around the position. Once it is on, your job shrinks to something almost mechanical: wait for one of the three to trigger, then act without negotiating with yourself.

### Profit targets — and the 50% rule for sellers

A profit target answers "how much is enough?" For a long-option *buyer*, the target is often a price level or a multiple of premium (e.g. exit if the option doubles). But the most famous, most studied profit-taking discipline lives on the *selling* side.

When you sell premium — a short put, a credit spread, an iron condor — your **maximum profit is the credit you collected**, and you only collect all of it if you hold to expiry and the options expire worthless. The well-known professional discipline is **not** to be greedy for that last rupee. Instead, **take profit at around 50% of maximum profit** — that is, buy the position back once it has lost about half of the credit you sold it for.

Why give up the other half? Three solid reasons:

- **The easy money comes first.** A short option's value decays fastest in the early-to-middle part of its life. Squeezing the last 50% means holding through the slow, grinding final stretch for a shrinking reward.
- **Gamma risk explodes near expiry.** As expiry approaches, a short option's gamma rises sharply; a calm position suddenly swings wildly on small underlying moves. Taking the 50% removes you *before* that danger zone — you collect the safe middle of the move and skip the treacherous end.
- **Win consistency and capital recycling.** Closing at 50% raises your hit-rate, frees margin sooner, and lets you redeploy into a fresh, full-premium trade. More frequent smaller wins with less tail risk usually beats fewer maximal wins with ugly late-expiry blow-ups.

A common refinement: take 50% of max profit *or* exit at a fixed number of days to expiry (say, 21 days left on a monthly), whichever comes first — combining a profit target with a time stop.

### Stop-losses for options — three flavours

A stop-loss answers "how wrong can I be before I admit it?" Stops on stocks are simple price triggers. Options are trickier because three different things can move your P&L — the underlying price, implied volatility, and time. So options traders use three distinct kinds of stop, often in combination.

**1. By premium percentage.** Define the stop in terms of the option or spread's *price*. For a buyer: "exit if the premium falls to 50% of what I paid." For a credit seller: "exit if the loss reaches a multiple of the credit collected." A widely used seller's rule is to **stop out at roughly 2x the credit** — if you sold a spread for ₹60 and it now costs ₹120 to buy back, you are down one credit's worth (₹60) and you close. This caps the loss at a known multiple of the reward, even on defined-risk trades.

**2. By an underlying price level.** Define the stop where your *thesis is invalidated*, not where it merely hurts. You sold a bull put spread because you believed Nifty would hold above a support level — so the *level that breaks the thesis* is the stop. "If Nifty closes below 23,800 support, I'm out" is cleaner and more honest than an arbitrary rupee figure, because it is tied to the reason you entered. When the chart says you were wrong, you leave.

**3. By the Greeks.** The professional's stop. Instead of (or alongside) a price trigger, you cap a *risk measure*: "close or adjust if position delta exceeds X" (too directional), "reduce if short gamma rises beyond my comfort as expiry nears", or "exit if a vega spike pushes the mark-to-market loss past my limit." Greek-based stops manage the *true* exposure rather than a single price snapshot — they recognise that a flat underlying can still lose through an IV spike (short vega), or that an approaching expiry has quietly made the position far riskier (rising gamma).

### Time stops — get out before the danger zone

A time stop is a deadline: "I will be flat by this date/time regardless of P&L." It exists because the final days before expiry are uniquely hazardous for option *sellers*:

- **Gamma explodes.** Near expiry, an at-the-money short option's delta can flip from near-zero to near-1 on a small move. Your position whips around violently; a quiet trade becomes a grenade.
- **Pin risk.** If the underlying sits right at your strike into expiry, you face uncertainty about whether it finishes in or out of the money. (For Indian *index* options this is a pure cash-settlement P&L coin-flip; for physically-settled *stock* options it can mean an unwanted delivery obligation.)
- **Theta you've already mostly earned.** By the last day or two you have already captured the bulk of the decay you came for. Staying exposes you to all the gamma/pin downside for a sliver of remaining reward.

So sellers commonly set a time stop — "out by Wednesday on a Thursday-expiry weekly", or "close all short premium at 21 days to expiry on monthlies" — to step off the field *before* the most dangerous quarter of the game. Buyers use time stops too, but in the opposite spirit: a long option bleeds theta fastest near expiry, so a buyer whose thesis hasn't played out cuts the position rather than donating the last of the premium to decay.

### The danger of hope: never ride defined-risk to max loss

Here is the most expensive bad habit in options trading: a defined-risk trade goes against you, and instead of taking the planned stop you *hope*. "It's only a small spread, the max loss is capped anyway, I'll just let it ride and maybe it comes back." This is how a manageable ₹4,000 loss becomes the full ₹10,500 max loss.

The trap is that **defined risk is not a reason to skip the stop — the cap is a worst case, not a target.** Your stop-loss exists precisely so you almost never reach max loss. A trader who takes a stop at one credit's worth loses a controlled, recoverable amount; a trader who "lets it ride to max loss because it's capped anyway" loses two-to-three times as much *per losing trade*, and in credit-spread math (small wins, larger losses) that difference is the entire line between profit and ruin. Hope is not a strategy. Define the stop, and take it.

### Mechanical rules vs discretion

Should exits be **mechanical** (a fixed rule: always close at 50% profit, always stop at 2x credit, always out at 21 days) or **discretionary** (judged trade by trade)?

For the vast majority of traders — and certainly every beginner — **mechanical wins.** Mechanical rules are backtestable, remove emotion, and protect you from the in-the-moment hope/fear that destroys discretion. The whole point of writing exits before entry is to make them mechanical: the live, emotional you simply executes what the calm, planning you decided.

Discretion has a place, but it is *earned* — a seasoned trader may widen a stop because an event has passed and IV is collapsing in their favour, or take profits early because a news shock looms. But discretion practised by a losing or inexperienced trader is almost always just *rationalised hope*. The honest rule: be mechanical until you have years of data proving your discretion adds value. Even then, keep the time stop and the catastrophic stop hard and non-negotiable.

### Buyers vs sellers: opposite exit philosophies

Exits differ fundamentally depending on whether you bought premium or sold it, because the two have mirror-image P&L shapes.

**Buyers (long options): cut losers fast, let winners run with a trailing stop.** A buyer has small, capped risk (the premium) but theoretically large reward. The math only works if the occasional big winner pays for the many small losers — which means you must *not* let winners turn into losers, and you must cut losers quickly before theta grinds them away. So:

- Cut losers fast: a tight stop (e.g. exit at −50% of premium, or when the underlying breaks your invalidation level), because a long option that's going wrong is being double-killed by direction *and* time decay.
- Let winners run, but protect them: use a **trailing stop** — as the option gains, ratchet your exit up so you lock in more of the gain while leaving room to run. This is how Trader A above keeps the win instead of round-tripping it like Trader B.

**Sellers (short options/spreads): take profits early, respect stops hard.** A seller has small, capped reward (the credit) but large risk. The math works only if you protect the many small wins from the occasional large loss. So:

- Take profits early: the 50%-of-max-profit rule. Don't be greedy for the last, slow, gamma-risky rupees.
- Respect stops without negotiation: stop at a defined multiple of the credit (e.g. 2x) and/or when the underlying breaches the level that invalidated your thesis. Because losses are bigger than wins by design, a single un-stopped loss can erase many wins — the seller cannot afford hope.
- Use a time stop: be out before the final gamma/pin danger zone.

In one line: **buyers run winners and kill losers; sellers bank winners early and never let losers run.**

## Worked example (₹, Nifty)

Let's apply all three exit types to concrete Nifty trades. Assume lot size **75**, weekly expiry on Thursday.

**Example A — Seller's 50% profit target.** You sell a Nifty bull put spread for a net credit of **₹60** (sell 23,800 put, buy 23,600 put), 200-point width. Max profit = ₹60/unit = **₹4,500/lot**; max loss = (200 − 60) = ₹140/unit = **₹10,500/lot**.

- **Profit target (50%):** buy the spread back when it trades around **₹30** (you've captured half the ₹60 credit). Profit = (60 − 30) × 75 = **₹2,250/lot**. You're flat, the gamma-risky back half is someone else's problem, and your margin is freed for the next trade.
- Why not hold for the full ₹4,500? The extra ₹2,250 requires holding through the final days where a single adverse Nifty move, magnified by rising gamma, could flip the whole win into the ₹10,500 max loss.

**Example B — Seller's premium-% stop-loss (2x credit).** Same spread, sold for ₹60. Nifty starts sliding toward 23,800.

- **Stop trigger:** the spread now costs **₹120** to buy back (2x the credit). Loss = (120 − 60) × 75 = **₹4,500/lot**.
- You close *here*, taking a controlled ₹4,500 loss — not the ₹10,500 max loss. Note the symmetry: this 2x stop loses exactly one credit's worth of money (₹4,500), the same size as the 50% profit target's gain. Wins and stopped-losses are then comparable, which keeps a high-win-rate seller profitable.
- The hope-trap version: "it's only a ₹10,500 max loss, let it ride." If Nifty keeps falling below 23,600, you eat the full **₹10,500** — more than double the disciplined stop, and it takes nearly *five* of your ₹2,250 wins to repair.

**Example C — Stop by underlying level.** You sold that bull put spread because Nifty was holding the **23,850 support** zone. Your thesis-based stop: "if Nifty closes below 23,850, I'm wrong — exit." This is cleaner than a rupee figure because it's tied to *why* you entered. The day Nifty closes at 23,840, you're out, whatever the spread happens to be marked at — the chart told you the trade is invalid.

**Example D — Time stop.** It's Wednesday afternoon, one day before Thursday expiry. Your short 23,800 put spread is winning — Nifty sits at 24,050, the spread is worth ₹18. You *could* hold the last ₹18 to zero (another ₹1,350/lot), but overnight gamma/pin risk is now severe: a gap down through 23,800 at the open could swing this from a near-full win to a large loss in minutes. Your time-stop rule — "flat by Wednesday close" — has you buy it back at ₹18, booking (60 − 18) × 75 = **₹3,150/lot**. You traded ₹1,350 of potential reward for the elimination of a multi-thousand-rupee tail risk. That is a good trade.

**Example E — Buyer's trailing stop.** You buy a Nifty 24,000 call for **₹150** (₹11,250/lot), expecting a rally.

- **Hard stop (cut losers fast):** exit at ₹75 (−50% of premium) or if Nifty breaks below your invalidation level — whichever first.
- Nifty rallies; the call doubles to **₹300**. Instead of a fixed target, you start a **trailing stop** at ₹240. Nifty pushes on to ₹400, you trail the stop up to ₹330. Nifty reverses, the call falls back and hits your ₹330 trail — you're out at (330 − 150) × 75 = **₹13,500/lot** profit. The trailing stop let the winner run from ₹300 to ₹400-ish *and* protected you from giving it all back: the disciplined version of "let your winners run."

## Common mistakes / risk note

- **No exit plan at all.** Entering without pre-defined profit, stop and time exits is the cardinal sin. You will then exit on emotion — taking tiny profits in fear and holding losers in hope, the exact opposite of what works.
- **Riding a defined-risk trade to max loss out of "it's capped anyway".** The cap is a worst case, not a plan. Take the stop. Letting losers run is, statistically, what blows up credit-spread accounts.
- **Greed on the winning seller's trade.** Holding short premium for the last 10–20% of decay exposes you to maximum gamma/pin risk for minimal reward. Take the 50% and move on.
- **Round-tripping a winner.** A buyer who watches a doubled option collapse back to break-even (or worse) had no trailing stop. Protect winners as they grow.
- **Confusing a vega/IV blip with a thesis break.** A short-vega spread can show a paper loss on an IV spike while the underlying is still safely on the right side of your strike. Don't panic-stop on noise — but if the *price level* that invalidates your thesis breaks, do leave. Know which is which before you enter.
- **Ignoring costs and settlement at exit.** Every exit crosses bid-ask spreads and incurs STT, brokerage and exchange charges on the closing legs — these nibble a small ₹60 credit on both entry and exit. And remember Indian **index** options are European, cash-settled (clean to hold or close), while **stock** options are American and physically settled — a time stop matters even more there to avoid an unwanted delivery obligation.
- **Discretion you haven't earned.** "I'll just watch it" is usually rationalised hope. Be mechanical until proven otherwise.

## Key takeaways

- **Exits decide your P&L more than entries.** Plan all three exits — profit target, stop-loss, time stop — *before* you enter, while you're calm.
- **Sellers take profit early:** the ~50%-of-max-profit rule banks the easy decay, lifts win consistency, frees margin, and dodges the late-expiry gamma/pin danger zone.
- **Stop-losses for options come in three forms:** by premium percentage (e.g. 2x the credit), by an underlying price level (the level that invalidates your thesis), and by the Greeks (capping delta/gamma/vega risk).
- **Time stops get you out before expiry's danger zone** — exploding gamma and pin risk — for a small giveback in reward.
- **Never ride a defined-risk trade to max loss on hope.** The cap is a worst case; the stop keeps you from reaching it.
- **Be mechanical, not discretionary,** until you've earned the right to judgement — the whole point of pre-planned exits is to remove emotion.
- **Buyers vs sellers are mirror images:** buyers cut losers fast and trail winners; sellers bank winners early and respect stops without negotiation.

## Practice problems

1. **(Conceptual)** Three traders buy the identical Nifty call that briefly doubles. One ends up profitable, one breaks even, one takes a full loss. Explain how identical entries produce three outcomes, and what single discipline separates the winner from the other two.

2. **(Numeric)** You sell a Nifty iron-condor-style credit spread for a net credit of ₹80 (lot 75). You follow the 50%-of-max-profit rule. At what spread price do you exit, and what is your rupee profit per lot? What is the main risk you are deliberately giving up the remaining profit to avoid?

3. **(Numeric)** You sell a bear call spread for a ₹50 credit (200-point width, lot 75). Your stop is 2x the credit. (a) At what buy-back price do you stop out, and what is the rupee loss per lot? (b) If instead you "let it ride to max loss because it's capped", what is the max loss per lot? (c) How many 50%-profit wins (₹25/unit) does the un-stopped loss cost you to repair, versus the disciplined stop?

4. **(Conceptual)** Why do option *sellers* care so much about a **time stop** in the final days before expiry, while option *buyers* worry about time decay throughout the whole life of the trade? Name the two specific late-expiry dangers a seller's time stop is designed to avoid.

5. **(Application)** A trader buys a Nifty put for ₹120 expecting a fall. The put rises to ₹260. Describe a sensible *trailing-stop* exit, contrast it with a fixed profit target, and explain which buyer's principle ("cut losers fast" or "let winners run") each exit type serves.

6. **(Risk / discretion)** Your short bull put spread shows a mark-to-market loss two days after entry, even though Nifty has barely moved and is still comfortably above your short strike. Should this trigger your stop-loss? Explain, distinguishing a Greek/IV effect from a genuine thesis break.

## Solutions

**1.** The entry was identical and good, but P&L is determined at *exit*, not entry. The winner had a plan to bank or trail the gain (e.g. a trailing stop) and acted on it; the break-even trader held "for more" with no protection and let the option round-trip to its entry price; the full-loss trader held even longer with no exit and let theta plus a reversal take it to zero. The single separating discipline is **a pre-defined exit (profit target / trailing stop) executed mechanically.** Options are wasting assets, so *when* you leave decides everything — a 100% winner is only a winner if you close it.

**2.** Max profit = the ₹80 credit. The 50% rule means buying the spread back when it has lost half its value — i.e. when it trades around **₹40**. Profit = (80 − 40) × 75 = **₹3,000 per lot**. You give up the remaining ₹3,000 of potential profit chiefly to avoid the **exploding gamma and pin risk of the final days before expiry** (plus you free margin and lift win consistency). The last half of the credit is the slow, dangerous half.

**3.** 
- (a) 2x credit means buying back at **₹100** (twice the ₹50 credit). Loss = (100 − 50) × 75 = **₹3,750 per lot**.
- (b) Max loss = (width − credit) = (200 − 50) = ₹150/unit × 75 = **₹11,250 per lot**.
- (c) A 50% win banks ₹25/unit × 75 = ₹1,875/lot. The un-stopped max loss (₹11,250) costs **6 wins** to repair (11,250 ÷ 1,875 = 6); the disciplined stop (₹3,750) costs only **2 wins** (3,750 ÷ 1,875 = 2). Hoping instead of stopping triples the damage — from two wins' worth to six.

**4.** A seller has captured most of the decay (theta) they came for by the last day or two, so there's little reward left — but the *risk* spikes precisely then. The two specific late-expiry dangers are: **(1) exploding gamma** — an at-the-money short option's delta swings violently on small underlying moves, so a calm position becomes a grenade; and **(2) pin risk** — the underlying sitting at the strike into expiry creates in/out-of-the-money uncertainty (a cash-settlement coin-flip for index options, a possible delivery obligation for physically-settled stock options). The time stop steps the seller off the field *before* that danger zone. A *buyer*, by contrast, pays theta every single day the option is long — decay erodes a long option throughout its life, fastest near expiry — so the buyer's time concern is continuous, and a buyer's time stop is about not donating the last premium to decay if the thesis hasn't played out.

**5.** A fixed profit target would simply sell at a pre-chosen price (say ₹240) and be done. A **trailing stop** instead locks in gains while leaving room to run: e.g. once the put hits ₹260, set an exit at ₹220; if it climbs to ₹320, raise the exit to ₹280; you only sell when the put falls back to the current trail. The trailing stop serves **"let winners run"** — it captures more of a continuing move while protecting against a round-trip. (The *hard stop* on the downside — exit at, say, −50% of the ₹120 premium — serves the other principle, **"cut losers fast."**) A buyer needs both: cut quickly when wrong, trail to maximise when right.

**6.** **No — a mark-to-market loss with the underlying still safely above your short strike is most likely a Greek/IV effect, not a thesis break.** A credit spread is short vega, so an uptick in implied volatility (a news jitter, an approaching event) fattens your short option and shows a paper loss even with price flat; bid-ask/closing friction adds a little more. None of that means you were wrong about *direction*. Your stop should be tied to the **underlying price level that invalidates your thesis** — only if Nifty actually breaks below your short strike / support level do you leave. The lesson: distinguish *noise* (a vega/IV blip while the thesis is intact) from a *real* thesis break (the price level you defined is breached), and define which trigger you're using *before* entering so you don't panic-stop on noise — or, just as bad, rationalise a genuine break as "just IV."
