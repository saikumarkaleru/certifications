# Chapter 9: Margins & Money — What It Costs to Buy vs Sell

Imagine two people standing at opposite ends of the same insurance contract. One person *buys* fire insurance on a house: she pays a small premium, and whatever happens, that premium is the most she can ever lose. The other person is the insurance *company* that *sold* her the policy: it pockets the premium up front, but if the house burns down it owes a fortune. The buyer's cost is small, fixed, and known the moment she signs. The seller's potential payout is large, variable, and frightening. No sensible regulator would let an insurance company write policies with empty pockets — it must keep large reserves to prove it can pay claims. Options work in exactly this way, and the reserve the seller must keep is called **margin**.

This single asymmetry — buyers pay a small premium that *is* their whole cost, sellers must lock up a large margin because their risk is big — governs how much capital you need, how much you can lose, and ultimately whether you survive in this game long enough to get good at it. This chapter is about the money plumbing: what it actually costs to take each side, why, and how to size your capital so a bad week does not end your trading career.

## Core concepts

### The fundamental asymmetry: premium vs margin

When you **buy** an option — a call or a put — you pay the seller the **premium**, and that is the end of your obligation. You hand over the cash, and you now own a *right*. You can never be asked for one more rupee. Your maximum loss is the premium, fixed and known from the first second.

```
Option buyer:
  Cost to enter   = premium * lot size   (paid in full, up front)
  Maximum loss    = the same premium     (capped, known in advance)
  Margin required = none beyond the premium itself
```

When you **sell** (or "write") an option, the picture flips. You *receive* the premium, which feels like free money. But you have taken on an *obligation*: if the market moves against you, you must pay the buyer whatever the option is worth at expiry, and that amount can be many times the premium you collected (as Chapter 8 showed, a sold option's loss can be very large, and for a naked call, theoretically unlimited). Because the exchange and your broker cannot let you take on that obligation with empty pockets, they force you to deposit a large sum of cash or collateral that stays frozen for as long as the position is open. That frozen deposit is **margin**.

```
Option seller:
  Cash received   = premium * lot size   (credited up front)
  Maximum loss    = large / potentially unlimited
  Margin required = a big deposit (SPAN + Exposure), locked until you exit
```

So the buyer's "cost" and the seller's "cost" are completely different animals. The buyer's cost is a *payment* she will never see again unless the trade works. The seller's margin is a *blocked deposit* — he still owns that money, it is just held hostage as proof he can honour the trade. Confusing these two is one of the most common beginner errors.

### What margin actually is, and why it exists

Margin is a good-faith deposit that guarantees you can meet your obligations. The buyer needs none beyond the premium because she has no further obligation — she already paid everything she could ever owe. The seller needs a lot because tomorrow he might owe a great deal.

In India this is run through a system called **SPAN** (Standard Portfolio Analysis of Risk), the margining engine used by the NSE's clearing corporation. You do not need to compute SPAN by hand — your broker's margin calculator does it — but you must understand what it is *trying* to do. The margin a seller posts has two main parts:

1. **SPAN margin.** The clearing corporation simulates a set of "what if" scenarios — what if the index jumps up, what if it crashes, what if volatility spikes — and asks: *under the worst plausible one-day scenario, how much could this position lose?* That worst-case loss, roughly, is the SPAN margin. It is risk-based: a position that can lose a lot is charged a lot.

2. **Exposure margin.** An additional cushion on top of SPAN, a few percent of the contract's notional value, to cover the gap between "worst plausible day" and "genuinely catastrophic day." Think of it as a second airbag.

```
Total seller margin = SPAN margin + Exposure margin
```

The deep idea: **margin is sized to the risk, not to the premium.** A seller who collects a tiny ₹5 premium on a far-out-of-the-money option still posts heavy margin, because even a small premium hides a large tail risk. The exchange does not care what you were paid; it cares what you could lose.

### Roughly how much margin to sell one Nifty or Bank Nifty lot

Beginners always want a number, so here is the honest one: to sell **one naked lot** of a Nifty or Bank Nifty index option, you should expect to block **about ₹1 to ₹1.5 lakh** of margin. That is the right mental anchor.

But treat that figure as *conceptual*, not fixed, because margin moves with risk, and risk moves with volatility:

- **It rises when volatility rises.** When India VIX (the index that measures expected market volatility) spikes — during a crash or an election result — SPAN's worst-case scenarios get wider, so the margin to hold the *same* lot can jump sharply, sometimes overnight.
- **It scales with notional.** Bank Nifty's per-lot margin is generally in a similar ballpark to Nifty's, but the exact figure tracks each contract's notional and volatility. Read your broker's live margin calculator before you trade — never assume.
- **It changes with regulation.** SEBI and the exchanges periodically revise margin formulas and add special cushions (for example, extra "expiry-day" margins on short options near expiry). So "about ₹1–1.5 lakh per lot" is a *2020s-era* anchor, not a law of nature.

Contrast this with **buying** that same lot: if the option premium is, say, ₹150 on a 75-unit Nifty lot, you pay `150 * 75 = ₹11,250` — and you are done. The buyer needs roughly a tenth of the capital the naked seller needs for the same strike, because the buyer carries a fraction of the risk.

### The big margin benefit of hedging: spreads vs naked selling

Here is one of the most important practical facts in all of options trading, and most beginners discover it too late. If you sell an option *and simultaneously buy a cheaper, further-out option* to cap your risk — that is, you trade a **spread** rather than a naked short — your margin can fall dramatically.

Why? Because SPAN is a *portfolio* risk engine. It does not look at your sold option in isolation; it looks at your *whole position's* worst-case loss. A naked short call can lose without limit, so SPAN charges a big margin. But a **bull call spread** or **bear call spread** — where the long option you also hold puts a hard ceiling on your loss — has a *capped, known* maximum loss. SPAN sees that the worst case is now small and bounded, so it charges far less margin.

A concrete intuition:

- **Naked short:** sell one Bank Nifty call. Worst case is enormous, so margin is roughly **₹1–1.5 lakh**.
- **Defined-risk spread:** sell that same call but also buy a higher-strike call to cap the loss. The maximum the spread can lose might be only ₹15,000–₹30,000, so the margin can drop to roughly that bounded loss — often a *fraction* of the naked-short margin.

The lesson is double-barrelled. Hedging not only *limits your loss* (good for survival), it also *frees up capital* (good for returns on the capital you do deploy). This is why professional retail option sellers in India overwhelmingly trade **defined-risk spreads** rather than naked shorts: the same view, a hard floor under the loss, and a much smaller margin block. The exchange literally rewards you for hedging.

### SEBI's peak-margin framework, in plain terms

In the past, a sneaky game was possible. If margin was checked only at the *end* of the day, an aggressive trader could take a giant intraday position with very little money, as long as it was squared off before the closing snapshot. The system never "saw" the dangerous moment, leaving brokers exposed when markets gapped.

To stop this, SEBI introduced the **peak-margin** framework. Instead of one end-of-day check, the clearing corporation now takes **several random snapshots during the trading day** (historically around four random times) and records your margin requirement at each snapshot. Your obligation for the day is based on the **highest (peak)** of those intraday snapshots — not the comfortable end-of-day number.

In plain English: **you must have the full required margin in your account at every moment, not just at the close.** You can no longer briefly over-leverage during the day and tidy up before the bell. If a random snapshot catches you short of margin, you face a penalty. This was phased in deliberately (starting at a fraction of the requirement and ramping up to 100%) specifically to curb the reckless intraday leverage that was wiping out retail traders. The practical effect for you: size your positions as if you are being watched at all times — because you are.

### Mark-to-market and margin calls

A seller's risk does not wait politely until expiry. The exchange settles gains and losses **every single day** through a process called **mark-to-market** (MTM). At the end of each trading day, your open positions are revalued at the day's settlement price, and the change is settled in cash:

- If the market moved your way, profit is credited to your account.
- If it moved against you, the loss is **debited** from your account that same day.

This daily truing-up means a seller cannot just sit on a losing position and "hope" — the losses are taken from his account day by day, in real money. If those debits eat into his deposit so that he no longer has enough to cover the required margin, he gets a **margin call**: a demand from the broker to deposit more funds immediately to restore the margin.

If he does not (or cannot) meet the margin call, the broker has the right to **forcibly square off** (close) his positions to protect itself — often at the worst possible moment, in a fast-moving market, at whatever price is available. This is how leveraged traders get wiped out: not by a single catastrophic tick, but by an adverse move that triggers MTM losses, a margin call they cannot meet, and a forced liquidation that locks in the damage. The buyer, by contrast, faces no margin call ever — she already paid her maximum loss up front, so there is nothing more to demand from her.

### Leverage: the double-edged sword

Everything above is really about **leverage** — controlling a large economic exposure with a small amount of capital. Recall from Chapter 7 that one Nifty lot controls roughly ₹18 lakh of index. Whether you buy or sell, you wield leverage, and it cuts both ways with brutal symmetry.

- For the **buyer**, leverage means a modest index move can multiply the premium several times over — but the same leverage means options routinely lose 100% of the premium when the move does not come in time.
- For the **seller**, a small margin can earn a steady stream of premiums — until one violent move produces a loss many times the premium collected and possibly larger than the margin posted, triggering MTM debits and margin calls.

Leverage does not change the *odds* in your favour; it amplifies whatever outcome occurs, including ruin. This is precisely why SEBI's own studies have repeatedly found that roughly **9 in 10 retail F&O traders lose money** — leverage lets them take positions far larger than their capital can survive, so a normal losing streak becomes a fatal one.

### Sizing capital so you survive

The professional's first job is not to make money — it is to *not go broke*, because a trader who blows up cannot compound. A few capital-sizing principles follow directly from the margin mechanics above:

1. **Never deploy all your margin.** If selling one lot blocks ~₹1.25 lakh, do *not* hold an account with exactly ₹1.25 lakh. A volatility spike can raise the margin requirement, and an adverse MTM move can debit your balance — both at once. Keep a large **free-cash buffer** (many professionals keep 30–50% of capital unblocked) precisely so a margin call never forces you out at the worst moment.
2. **Size by worst-case loss, not by premium or by margin.** Before any trade, ask: "If this goes maximally against me, how many rupees do I lose, and is that a survivable fraction of my account?" A common discipline is to risk only a small percentage (1–2%) of total capital on any single trade.
3. **Prefer defined-risk structures.** Spreads cap the loss *and* cut the margin — they let you survive being wrong, which naked selling does not.
4. **Respect volatility.** When India VIX is high, margins are high and moves are large; the same lot count is far riskier. Cut size when volatility rises.

Survival is the whole game. Leverage will happily lend you the rope; capital sizing is how you avoid hanging yourself with it.

## Worked example (₹, Nifty/Bank Nifty)

Assume current approximate values: Nifty lot size 75, Bank Nifty lot size 30, naked index-option seller margin about ₹1.25 lakh per lot.

**Trade A — The buyer.** You are bullish and **buy 1 lot of the Nifty 24,000 weekly call at a premium of ₹150.** Nifty spot is 24,000.

Step 1 — What it costs to enter:
```
Cost = premium * lot size = 150 * 75 = ₹11,250  (paid in full)
```
That ₹11,250 is the *entire* cost and *also* your maximum loss. No margin is blocked beyond this; no one can ever demand more.

Step 2 — Outcomes at expiry:
- If Nifty settles at 23,800 (below the strike), the call expires worthless. You lose the full **₹11,250**, not one rupee more. No margin call ever arrives.
- If Nifty settles at 24,400, intrinsic value = `24,400 - 24,000 = 400` per unit. Payoff = `400 * 75 = ₹30,000`. Net profit = `30,000 - 11,250 = ₹18,750`. Your ₹11,250 stake nearly tripled — leverage working *for* you.

**Trade B — The naked seller.** You think Nifty will stay flat or rise, so you **sell 1 lot of the Nifty 24,000 weekly put at a premium of ₹150.**

Step 1 — Cash and margin. Take the put premium as ₹140:
```
Premium received = 140 * 75 = ₹10,500   (credited up front, your maximum profit)
Margin blocked   ≈ ₹1,25,000            (SPAN + Exposure, locked until you exit)
```
Notice the asymmetry immediately: to *earn* a maximum of ₹10,500 you must *lock up* about ₹1.25 lakh. The buyer in Trade A controlled the same lot for ₹11,250 and could lose only that; you, the seller, have frozen ten times as much capital.

Step 2 — A bad day (mark-to-market in action). Suppose Nifty falls and the put's value rises from ₹140 to ₹240 by the day's close. MTM debits your account that evening:
```
Daily MTM loss = (240 - 140) * 75 = 100 * 75 = ₹7,500 debited today
```
That ₹7,500 is taken from your balance in real cash. If the slide continues and your free funds run low, you get a **margin call** to top up — or the broker squares you off.

Step 3 — Expiry outcome. Suppose Nifty settles at 23,600. Intrinsic value of the put = `24,000 - 23,600 = 400` per unit:
```
Payoff owed = 400 * 75 = ₹30,000
Net result  = premium - payoff = 10,500 - 30,000 = -₹19,500
```
You collected ₹10,500 but lost ₹30,000 of value — a **net loss of ₹19,500**, larger than the premium you ever stood to make, on a single 400-point move. That is the seller's bargain: small fixed gain, large variable loss, big margin block.

**Trade C — The hedged seller (spread).** Now sell the same Nifty 24,000 put for ₹140 **but also buy the Nifty 23,800 put for ₹80** to cap your risk — a bull put spread.

```
Net premium received = (140 - 80) * 75 = 60 * 75 = ₹4,500   (lower max profit)
Maximum loss         = (strike gap - net premium) * lot
                     = (200 - 60) * 75 = 140 * 75 = ₹10,500  (hard-capped)
Margin blocked       ≈ the capped loss, often ~₹10,000–15,000 (a fraction of ₹1.25 lakh)
```
By giving up some premium (₹4,500 instead of ₹10,500), you converted an unbounded risk into a maximum loss of ₹10,500 *and* cut your margin from ~₹1.25 lakh to a small fraction of it. Even in the disastrous 23,600 settlement, your loss is capped at ₹10,500 instead of running to ₹19,500 and beyond. Same directional view; survivable risk; a tenth of the capital tied up. This is why professionals hedge.

## Common mistakes / risk note

- **Thinking the seller's margin is the seller's cost.** Margin is a *blocked deposit*, not a payment — you still own it. But it is *capital that cannot work elsewhere*, and an adverse move can erode it through MTM. Treat margin as committed risk capital, not free money.
- **Selling options with a bare-minimum account.** Holding exactly the required margin and no buffer is how a volatility spike or one bad MTM day triggers a forced square-off. Always keep a large free-cash cushion.
- **Believing "premium received" is yours to keep.** It is yours *only if the trade works*. Until expiry it is exposed to losses many times its size. The credit on entry flatters beginners into over-selling.
- **Ignoring intraday peak-margin.** You cannot briefly over-leverage and square off before close — random snapshots catch the peak, and shortfalls draw penalties. Be funded at all times.
- **Naked selling for the "high probability."** Selling options wins often but small and loses rarely but large. Without a hedge, a single tail event can wipe out months of premium and more than your margin. The defined-risk spread exists precisely to remove this ruin risk.
- **The honest risk.** Leverage is the reason roughly 9 in 10 retail F&O traders lose money. It does not improve your odds — it magnifies every outcome, including the ones that end your account. Respect margin, size for survival, and prefer capped-risk structures.

## Key takeaways

- **Buyers pay premium; that premium is their entire cost and entire maximum loss** — no margin, no margin calls, ever.
- **Sellers receive premium but must post margin (SPAN + Exposure)** because their risk is large or unlimited; margin is sized to *risk*, not to the premium collected.
- Selling one naked Nifty or Bank Nifty lot blocks roughly **₹1–1.5 lakh** of margin — a *conceptual* anchor that rises with volatility (India VIX) and changes with SEBI rules.
- **Hedging into a spread slashes margin** because SPAN charges on the *bounded* worst-case loss — defined risk frees capital and caps losses at once.
- **SEBI's peak-margin framework** uses random intraday snapshots, so you must be fully margined at all times, not just at the close.
- **Mark-to-market settles gains/losses daily**; running short of margin triggers a **margin call** and possible forced square-off.
- **Leverage cuts both ways**; survival comes from keeping a free-cash buffer, sizing by worst-case loss, and respecting volatility.

## Practice problems

1. **(Conceptual.)** In one or two sentences, explain why an option *buyer* needs no margin beyond the premium while an option *seller* must post a large margin. Tie your answer to each side's obligation.

2. **(Numeric.)** Nifty lot size is 75. You buy 2 lots of a call at a premium of ₹120. What is your total cost to enter, and what is your maximum possible loss? How much *additional* margin must you post?

3. **(Numeric.)** You sell 1 naked Bank Nifty put and receive a premium of ₹300 (lot size 30). Your broker blocks ₹1.3 lakh of margin. State (a) your maximum profit, and (b) the ratio of margin blocked to maximum profit. What does that ratio tell you about the trade's risk/reward asymmetry?

4. **(Conceptual / numeric.)** Explain why selling a put *and* buying a lower-strike put (a bull put spread) requires far less margin than selling the put naked. If the naked margin is ₹1.25 lakh and the spread's maximum loss is ₹12,000, roughly what order of magnitude would you expect the spread's margin to be?

5. **(Numeric.)** You sold a Nifty option for ₹100 (lot 75). By the day's close its value has risen to ₹160. Compute today's mark-to-market debit. If your account had only a thin buffer above the required margin, what is the likely consequence?

6. **(Conceptual.)** A friend says, "I checked my margin at 3:25 pm and it was fine, so SEBI's peak-margin rule can't touch me." Explain why this reasoning is flawed.

## Solutions

**1.** A buyer has *no further obligation* after paying the premium — she has already paid the most she could ever owe — so there is nothing to secure with margin. A seller has taken on an *open obligation*: if the market moves against him he must pay the buyer an amount that can far exceed the premium received. Margin is the good-faith deposit the exchange demands to guarantee he can meet that potentially large obligation; it is sized to his risk, not to his premium.

**2.** Cost to enter = `120 * 75 * 2 = ₹18,000`, paid in full. As a buyer, that ₹18,000 is also your **maximum loss** (the calls expire worthless if Nifty finishes at or below the strike). **No additional margin** is required — the premium *is* the whole cost; there are no margin calls for a buyer.

**3.** (a) Maximum profit = premium received = `300 * 30 = ₹9,000` (kept only if the put expires worthless). (b) Ratio of margin to max profit = `1,30,000 / 9,000 ≈ 14.4`. You are locking up roughly **fourteen times your best-case profit** as margin. The ratio signals a sharp asymmetry: a small capped gain against a large (potentially much larger than the margin) loss — the classic option-seller's bargain, and why naked selling demands heavy capital.

**4.** Naked selling leaves an *unbounded* worst-case loss, so SPAN charges a large margin against that tail. Adding a long lower-strike put puts a *hard floor* under the loss; the position's worst case becomes the bounded difference `(strike gap - net premium) * lot`. SPAN, being a portfolio risk engine, charges against this *bounded* worst case, so the margin collapses to roughly the size of the maximum loss. With a max loss of ₹12,000, expect the spread's margin to be of the order of **₹12,000–₹20,000** — roughly a *tenth* of the ₹1.25 lakh naked margin. Hedging both caps the loss and frees capital.

**5.** MTM debit = `(160 - 100) * 75 = 60 * 75 = ₹4,500`, taken from your account in cash this evening. With only a thin buffer, the debit plus a possibly *higher* margin requirement (the option's risk has grown) can push your balance below the required margin, triggering a **margin call**. If you cannot top up promptly, the broker may **forcibly square off** the position — often at a poor price — locking in the loss. This is the mechanism by which under-funded sellers get knocked out.

**6.** SEBI's peak-margin framework does **not** rely on a single end-of-day (or any single chosen-time) check. The clearing corporation takes **several random snapshots during the trading day** and bases your obligation on the **highest** margin observed across them. A position that looked fine at 3:25 pm could have been short of margin at 11:40 am or 1:15 pm, and *that* peak is what counts. The rule exists precisely to stop traders from over-leveraging intraday and tidying up before a chosen moment — you must be fully margined at *all* times, not just when you happen to look.
