# Chapter 52: Assignment, Expiry & Pin Risk

When you sell an option, you collect a premium up front, but you also sign up for an obligation: if the buyer decides to use their right, you must make good on the other side of the contract. The moment that obligation lands on you is called **assignment**. For most of an option's life it is just a distant possibility. But as expiry approaches and the underlying drifts toward your short strike, assignment stops being theoretical and becomes a live, money-moving event — and if you are careless about it, it can hand you a position you never wanted, a margin demand you cannot fund, or a tax bill that swallows your profit.

This chapter is written from the seller's chair, because that is where assignment risk lives. We will separate the two worlds that behave completely differently in India — cash-settled index options and physically-settled stock options — and then spend real time on the single nastiest situation a seller can face at expiry: **pin risk**, where the underlying closes so close to your short strike that you genuinely do not know whether you will be assigned, and you walk into the next session carrying an exposure you did not plan for. The good news is that almost all of this danger is avoidable with a few disciplined habits. The aim of this chapter is to make those habits second nature.

## Core concepts

### What assignment actually is

Every option is a contract between two parties. The **buyer** (long) holds a *right*; the **seller** (short, also called the writer) holds an *obligation*. When the buyer chooses to use their right, the contract is **exercised**. The exchange then picks a seller of that same option to fulfil the contract — that seller is said to be **assigned**.

- **Exercise** is what the *buyer* does (claim the payoff).
- **Assignment** is what happens to the *seller* (forced to deliver the payoff).

They are two ends of the same event. In India, retail traders are almost always on the receiving end — you sold a call or a put, the buyer's right finishes in-the-money, and you are assigned. The key questions are: *when* can it happen, and *what does it cost you* when it does?

### European vs American, and why "when" matters

The "when" depends on the **exercise style** of the contract.

- **European-style** options can be exercised *only at expiry*, never before. Indian **index** options — Nifty, Bank Nifty, FinNifty, Sensex — are European. As a seller, this means you can *never* be surprised by an early assignment mid-life. Assignment, if it comes, comes only on expiry day.
- **American-style** options can be exercised *any time up to* expiry. Indian **single-stock** options (Reliance, Infosys, HDFC Bank, and the rest of the F&O stock list) are American-style. In principle the buyer could exercise early.

Here is the practical nuance Indian traders must hold in their heads. Although stock options are *American* in style, in everyday practice early exercise is rare, because a buyer who exercises early throws away any remaining time value — they would almost always do better to *sell* the option in the market than exercise it. So in real life, even for stock options, the assignment drama overwhelmingly concentrates on **expiry day**. The style matters less for "early surprise" and far more for *what settlement looks like* — cash versus physical — which is the distinction that truly bites.

### Assignment on index options: it is just cash

For index options, assignment is painless in mechanism, because settlement is **cash**. No shares exist to deliver — you cannot hand someone "a Nifty." At expiry, the exchange computes the option's intrinsic value and simply **debits the seller and credits the buyer** that amount of cash. As the seller of an ITM index option, you do not deliver anything; the loss is just subtracted from your account.

The intrinsic value is measured against the **settlement price**, which for Indian index options is the **time-weighted average value of the underlying index over the last 30 minutes of trading on expiry day** (roughly 3:00 to 3:30 p.m.), not the final 3:30 tick. This averaging exists to stop a large player from jamming the index for one instant to swing crores of payoffs. As a seller it cuts both ways: a strike that looks safely OTM on the closing candle could still settle ITM if the 30-minute average sits on the wrong side.

```
Cash assignment loss to seller (per lot) = intrinsic value per unit * lot size
intrinsic value (short call) = max(settlement price - strike, 0)
intrinsic value (short put)  = max(strike - settlement price, 0)
```

So for an index seller, "assignment" is really just an automatic cash debit. There is no delivery obligation, no shares arriving in your demat, no multi-lakh cash demand. This is one reason index options are the natural home for most retail option *selling* in India.

### Assignment on stock options: a real cash-flow and margin event

Single-stock options are a different animal entirely. Since SEBI's 2019 rule, **all stock derivatives are physically settled**. An ITM stock option at expiry converts into an actual obligation to **deliver or receive shares** at the strike price, for the full lot quantity. If you are a *seller* who gets assigned, you must move real stock and real money:

- **Short call assigned (ITM):** you are obliged to *sell* at the strike — you must **give delivery** of the shares. If you do not already hold them, you must buy them in the market, and if you cannot, your position goes to the exchange **auction** with penalties.
- **Short put assigned (ITM):** you are obliged to *buy* at the strike — you must **take delivery**, paying `strike * lot size` in cash and receiving the shares into your demat.

The numbers are not small. A single lot of a stock option can represent five to fifteen lakh rupees of stock. Sell one ITM stock put and get assigned, and you may suddenly owe ₹8–10 lakh in cash to take delivery — for a trade where you collected only a few thousand rupees in premium. This is the core reason stock-option selling is dangerous for under-capitalised retail traders: the obligation is wildly out of proportion to the premium.

Because the exchange knows this delivery obligation is looming, it **ramps up margins through expiry week** on positions that could go to physical settlement — typically stepping up over the final four trading days until a likely-to-be-delivered position carries margin close to the full delivery value. An account that was comfortable on Monday can face margin calls by Wednesday or Thursday simply because the position is now near-the-money and delivery has become probable.

### Pin risk: the seller's expiry-day nightmare

Now the heart of the chapter. **Pin risk** is the danger that arises when the underlying expires *right at, or extremely close to,* your short strike — the price gets "pinned" to the strike. At that moment you face genuine uncertainty about whether your short option is in- or out-of-the-money, and therefore whether you will be assigned. You may end expiry not knowing your true position until settlement is finalised, and then discover you are holding an exposure you never intended.

The intuition: imagine you sold a 2,500 call on a stock and at the close the stock is sitting at 2,500.40 — forty paise ITM. Is the buyer going to exercise? Will the averaged/closing settlement land it ITM or OTM? You cannot be sure. If it settles ITM and you are assigned on a *physically*-settled stock option, you are now **short 250 shares** at the strike (you had to give delivery). Come Monday, the stock could gap up 4% on news, and you are nursing a fresh, unhedged short equity position that has nothing to do with your original plan.

Pin risk has two distinct flavours in India:

1. **Stock options (physical) — the dangerous kind.** Here pin risk creates a real *directional residual position*. If a leg of your spread is pinned and uncertainly assigned, you can wake up long or short actual shares, exposed to the weekend/overnight gap. This is the version that genuinely hurts.
2. **Index options (cash) — the milder kind.** Because settlement is pure cash on an averaged price, there is no leftover share position. The "risk" is narrower: uncertainty about the exact settlement debit, and the possibility that a strike you assumed was safe settles a few points ITM because of the 30-minute average. Unpleasant, but no surprise stock position to manage on Monday.

Pin risk is at its worst for **spreads on stock options**, where you might assume both legs cancel. Picture a bull put spread on a stock: short the higher-strike put, long the lower-strike put. If the stock pins right between them, your *long* put may finish OTM (worthless, no delivery) while your *short* put finishes barely ITM (assigned — you must take delivery and pay out lakhs). The protection you thought you had does not fire, and you are left holding the full obligation of the naked short leg. This "the wings didn't both trigger" outcome is the classic pin-risk trap.

```
Pin risk = uncertainty of assignment when underlying ~ short strike at expiry
For STOCK (physical): leftover residual share position + overnight gap exposure
For INDEX (cash):     uncertainty in the settlement cash debit only
```

### Expiry-day management: how professionals avoid all of this

The cleanest defence against assignment surprises, physical delivery, and pin risk is almost embarrassingly simple: **close the position in the market before expiry.** A position you have squared off has nothing left to be assigned — there is no obligation, no delivery, no pin. The professional habit is to manage out of risky expiry positions rather than let them go to settlement. Concretely:

- **Square off short ITM (or near-ITM) stock options before the broker's expiry-day cutoff.** Buy back the option you sold. You pay only the small premium-based STT and you eliminate the delivery obligation entirely. Do not let a near-the-money stock short ride into settlement hoping it lands OTM — that is pure pin-risk gambling with lakhs at stake.
- **Watch the final hour.** Most pin-risk damage is decided between 2:30 and 3:30 p.m. on expiry day. If your short strike is within a whisker of the spot as the close approaches, act — close it, or deliberately roll it — rather than freezing and hoping.
- **Know your broker's auto square-off backstop, but never rely on it.** Nearly every Indian broker auto-squares-off physically-settled stock F&O positions that the client has not closed by a published deadline (commonly some point in the afternoon, varying by how deep ITM the option is), often with an extra penalty, and executes at whatever market price prevails — possibly a poor one. Treat it as the fire alarm, not the plan. Outsourcing your exit to the risk engine means accepting an uncontrolled price and a charge.
- **The STT-on-exercise trap reinforces all of the above.** When an ITM option is *exercised/settled* rather than sold in the market, STT has historically been charged on a far larger base — tied to the settlement value, not the tiny premium. On a barely-ITM option, that exercise STT can be a large fraction of, or even exceed, your intrinsic gain. Buying back your short (or selling your long) in the market sidesteps this punitive STT. Tax alone justifies the square-off habit.

### Do-not-exercise instructions and close-to-the-money options

To protect *buyers* from accidentally triggering exercise STT and physical delivery on options that are only marginally ITM, the system has long offered **Do-Not-Exercise (DNE)** instructions for **close-to-the-money (CTM)** long options. By default, ITM options are **automatically exercised** at expiry — the holder need do nothing to claim the money, and the matched seller is automatically assigned. DNE is the switch that turns this off for marginal cases: a buyer holding a barely-ITM stock option can flag "do not exercise," forgoing the small intrinsic value to avoid a delivery obligation and an STT that would exceed it.

Why does this matter to *you as a seller*? Because it adds yet another layer of uncertainty to pin risk. If you are short a CTM stock option, whether you get assigned can depend on whether the matched long holders chose to exercise or filed DNE — something you cannot see or control. The exact CTM/DNE framework has been refined by the exchange over the years, so verify the current mechanism with your broker. The constant principle: **at the margin, assignment is uncertain, so do not leave yourself standing in that margin.** Close the position and the question disappears.

### Practical rules to never get surprised at expiry

1. **Always know which world you are in.** Index = cash, painless assignment. Stock = physical delivery, multi-lakh obligation. Check this *before* expiry week, not on expiry day.
2. **Treat near-the-money short stock options as live grenades in the final hour.** If spot is near your short strike at expiry, square off — do not gamble on which side of the strike it lands.
3. **Never let a stock-option spread "ride to settlement" assuming the legs net out.** Pin risk can fire one leg and not the other, leaving you with a naked delivery obligation.
4. **Mark your broker's expiry-day square-off cutoff in your calendar** and act well before it.
5. **Keep buffer cash in expiry week** to survive the margin ramp-up on any delivery-eligible position.
6. **Prefer index options for premium selling** if you cannot fund — or do not want — physical delivery. Most retail sellers should keep stock-option shorts small and close them early.

## Worked example (Rupees, Nifty cash & a stock-option pin)

### Example A — Nifty index short, cash assignment

**Setup.** It is weekly expiry. You sold (wrote) 2 lots of the **Nifty 24,000 call** earlier in the week, collecting a premium of ₹130. Lot size 75. Through the afternoon Nifty hovers near 24,070. The final 3:30 tick prints 24,090, but the **time-weighted average over 3:00–3:30 p.m. comes out to 24,055.**

**If you let it go to settlement (you are auto-assigned):**

Settlement uses the *averaged* price, 24,055, not the 24,090 print.

```
Intrinsic per unit       = max(24,055 - 24,000, 0) = 55
Assignment debit per lot = 55 * 75 = ₹4,125
Two lots                 = ₹8,250 debited from your account
```

You collected `130 * 75 * 2 = ₹19,500` in premium. After the ₹8,250 assignment debit, your gross result is `19,500 - 8,250 = ₹11,250` profit before charges. Note there is **no share position** — index assignment is pure cash, automatically debited. Your "assignment" is invisible apart from the number on your statement. Also note the averaging helped you here: the 24,055 average gave a smaller debit than the 24,090 tick would have (`90 * 75 * 2 = ₹13,500`).

**The cleaner professional path:** rather than carry the short into settlement (and trigger the higher exercise STT on the settlement value), you buy back the 2 lots at, say, ₹62 around 3:20 p.m.:

```
Buy-back cost = 62 * 75 * 2 = ₹9,300
Gross profit  = 19,500 - 9,300 = ₹10,200 (before charges)
STT only on the small premium-based market trade.
```

Slightly less than the ₹11,250 settlement figure in this particular case, but you remove all settlement uncertainty and dodge the punitive exercise STT — a trade most professionals make happily, and one that is clearly better whenever the averaged settlement would have come in worse.

### Example B — Stock-option short, pin risk and physical delivery

**Setup.** You sold 1 lot of a **Reliance 2,900 call** (assume lot size 250 — confirm the live lot). You collected a premium of ₹35, so you received `35 * 250 = ₹8,750`. It is monthly expiry day and Reliance is dancing around **2,902** all afternoon — barely 2 points above your strike. You are *pinned.*

**The uncertainty.** Will it settle ITM? At 2,902 you are 2 points ITM, but it has dipped to 2,898 twice in the last hour. If it finishes OTM, your call expires worthless and you keep the full ₹8,750 — lovely. If it finishes ITM and you are **assigned**, this is a *physically-settled* stock option, so as the short-call writer you must **give delivery** of 250 Reliance shares at 2,900:

```
You must deliver  = 250 Reliance shares
You receive       = strike * lot size = 2,900 * 250 = ₹7,25,000
But you don't own the shares...
```

If you do not hold 250 Reliance shares, you are now effectively **short 250 shares** at 2,900. Over the weekend Reliance reports strong numbers and gaps up to 3,000 on Monday. To cover, you must buy 250 shares at ~3,000:

```
Cost to cover = 3,000 * 250 = ₹7,50,000
You received  = ₹7,25,000 (from delivering at the strike)
Loss on the residual short = 7,50,000 - 7,25,000 = ₹25,000
```

A ₹25,000 loss — nearly three times the ₹8,750 premium you collected — from a position you thought was a 2-point coin-flip. That is pin risk made concrete: a tiny, uncertain settlement decision left you holding an unhedged overnight share exposure that a gap turned into a real loss. And had you been unable to deliver the shares at all, the position would have gone to **auction** with penalties on top.

**What the disciplined trader does.** Seeing Reliance pinned at the strike at 2:45 p.m., you simply **buy back the call** to close, paying its near-intrinsic price of about ₹6:

```
Buy-back cost = 6 * 250 = ₹1,500
Net profit    = 8,750 - 1,500 = ₹7,250 (before charges)
No delivery obligation. No residual short. No weekend gap risk. No exercise STT.
```

You give up ₹1,500 of the premium to *guarantee* you keep the rest and erase every scrap of pin and delivery risk. For ₹1,500 of certainty against a potential ₹25,000 (or worse) surprise, this is one of the easiest decisions in trading. The trader who instead "let it ride" because it was *only just* ITM is the one who gets the Monday-morning shock.

## Common mistakes / risk note

- **Forgetting that stock options are physically settled.** The single deadliest error. A seller assumes a stock short behaves like a Nifty short (cash) and is blindsided by a delivery obligation or a residual share position worth lakhs.
- **Letting a pinned short "ride to settlement."** When spot sits on your short strike at the close, assignment is a coin-flip you do not control — and for stock options the losing side hands you an overnight-gap-exposed share position. Close it.
- **Assuming spread legs always net out.** Pin risk can assign your short leg while your long (protective) leg finishes OTM and worthless, stripping away the hedge and leaving the full naked obligation. Spreads on stock options are *not* automatically safe at expiry.
- **Relying on the broker auto square-off.** It is a backstop that fires at an uncontrolled market price near a deadline, often with a penalty. Manage your own exit before the cutoff.
- **Ignoring expiry-week margin ramp-up.** Margins climb sharply over the last few days on delivery-eligible stock positions. Carry a cash buffer or get margin-called.
- **Letting a barely-ITM option go to exercise/settlement.** The exercise STT is charged on a large settlement-linked base and can exceed a small intrinsic value. Buying back in the market is tax-cheap; settling is tax-expensive.
- **The honest risk.** Assignment and expiry mechanics do not create edge — they create ways to *lose* edge you already had. A well-chosen short trade can be turned into a loss by an unmanaged pin, a physical delivery, an auction penalty, or exercise STT. SEBI studies show roughly 9 in 10 retail F&O traders lose money; sloppy expiry handling is one of the quiet contributors. Option selling carries large, sometimes undefined, risk — and assignment is the channel through which that risk is delivered.

## Key takeaways

- **Assignment is the seller's side of exercise** — the buyer claims their right, the exchange assigns a writer to honour it.
- **Index options are European and cash-settled:** assignment can only happen at expiry and is just an automatic cash debit on the 30-minute averaged settlement price — no shares, no delivery.
- **Stock options are American-style and physically settled:** assignment forces you to give or take real shares worth lakhs — a genuine cash-flow and margin event, with expiry-week margin ramp-up.
- **Pin risk** is the uncertainty of assignment when the underlying closes right at your short strike; for stock options it leaves you with a residual share position exposed to the overnight/weekend gap.
- **Pin risk is worst on stock-option spreads,** where one leg can be assigned while the protective leg expires worthless, exposing the full naked obligation.
- The universal defence is to **square off before expiry** — a closed position cannot be assigned, delivered, pinned, or hit with exercise STT.
- **Do-not-exercise / CTM** rules add assignment uncertainty at the margin; the broker auto square-off is a clumsy backstop, not a plan. **Watch the final hour and act.**

## Practice problems

1. **(Conceptual.)** Distinguish exercise from assignment. If you are short a Nifty put and the index closes well below your strike at expiry, which one happens to you, and what physically arrives in your account?

2. **(Conceptual.)** A trader sold a Bank Nifty call and, separately, an Infosys call, both finishing ITM at expiry. He expects both to simply debit cash from his account. Where is he wrong, and what must he do about the Infosys short before expiry?

3. **(Numeric — index cash assignment.)** You wrote 1 lot of the Nifty 23,500 put (lot 75) for a premium of ₹95. At expiry the final tick is 23,440 but the 3:00–3:30 time-weighted average is 23,470. If you let it settle, what is your assignment debit and your gross result before charges? How would it differ if settlement used the final tick?

4. **(Numeric — pin risk on a stock short.)** You sold 1 lot of a stock 1,500 call, lot size 600, collecting ₹20 premium. At expiry the stock is pinned at 1,501 (1 point ITM) and you are assigned. You do not own the shares. Over the weekend the stock gaps to 1,560. (a) What residual position do you hold after assignment? (b) What is your loss when you cover, net of the premium collected? (c) What single action before expiry would have avoided all of it, and roughly what would it have cost if the call traded at ₹3?

5. **(Conceptual.)** Explain why pin risk is far more dangerous on a physically-settled stock option than on a cash-settled index option, even when the intrinsic value at expiry is identical.

6. **(Conceptual.)** You hold a bull put spread on a single stock: short the 1,800 put, long the 1,750 put. The stock pins at 1,799 at expiry. Describe the pin-risk outcome and why your "defined risk" spread may not protect you as expected.

## Solutions

**1.** **Exercise** is the action the *buyer* takes; **assignment** is what happens to *you* as the seller when a buyer's right is used. Short a Nifty put that finishes ITM means you are **assigned**. Because Nifty is a **cash-settled index** option, nothing physical arrives — there are no shares. The exchange simply **debits cash** equal to `(strike - settlement price) * lot size` from your account, using the 30-minute averaged settlement price. Your "assignment" is purely a number on your statement; there is no delivery to manage.

**2.** Bank Nifty is an **index** option — **cash-settled** — so it does indeed just debit the intrinsic value in cash; nothing more to do. The Infosys call is a **single-stock** option — **physically settled**. As the assigned short-call writer he is obliged to **give delivery** of the full lot of Infosys shares at the strike. If he does not own them, he is effectively short the shares and risks an **auction** with penalties, plus he faced ramped-up expiry-week margin and the higher exercise STT. Unless he holds the shares and wants to sell them at the strike, he must **square off (buy back) the Infosys call in the market before his broker's expiry-day cutoff** to remove the delivery obligation.

**3.** Settlement uses the averaged price, 23,470.
```
Intrinsic = max(23,500 - 23,470, 0) = 30
Debit     = 30 * 75 = ₹2,250
Premium collected = 95 * 75 = ₹7,125
Gross result = 7,125 - 2,250 = ₹4,875 profit
```
If settlement used the final tick of 23,440: intrinsic = `23,500 - 23,440 = 60`, debit = `60 * 75 = ₹4,500`, gross result = `7,125 - 4,500 = ₹2,625`. The 30-minute average (23,470) is closer to the strike than the last tick (23,440), so the averaged settlement gave you a *smaller* debit and a better result here — a reminder that the averaged settlement, not the closing candle, governs the assignment amount.

**4.** (a) As the assigned short-call writer on a physically-settled stock option, you must **give delivery** of 600 shares at 1,500. Owning none, you are left **short 600 shares** at the 1,500 strike. (b) Covering after the gap to 1,560: cost to buy 600 shares = `1,560 * 600 = ₹9,36,000`; you received `1,500 * 600 = ₹9,00,000` for delivering at the strike; loss on the residual short = `9,36,000 - 9,00,000 = ₹36,000`. Net of the `20 * 600 = ₹12,000` premium collected, your net loss = `36,000 - 12,000 = ₹24,000`. (c) **Buying back the call before expiry** to close the short. At ₹3 it would have cost `3 * 600 = ₹1,800`, leaving a net profit of `12,000 - 1,800 = ₹10,200` and **zero** delivery, pin, or gap risk. Paying ₹1,800 to avoid a ₹24,000 loss is the entire lesson.

**5.** With identical intrinsic value, the *cash impact at expiry* is the same — but the **aftermath** is not. The **index** option is cash-settled: the loss is a one-time, fully-determined cash debit and the position is then **closed and gone**; there is nothing left to manage. The **stock** option is physically settled: assignment leaves you holding an **actual residual share position** (long or short the lot) at the strike. That position carries **overnight/weekend gap risk** — a news event before the next session can move the stock sharply, turning a marginal pin into a large loss (or requiring a forced market purchase, even an auction, to cover). So the danger is not the intrinsic value itself but the **lingering, directional, gap-exposed equity position** that only physical settlement creates.

**6.** The stock pins at 1,799, one point below your short 1,800 put — so your **short 1,800 put is ~1 point ITM and is assigned**, while your **long 1,750 put finishes well OTM and expires worthless**. The protective long leg does **not** fire. As the assigned short-put writer you must **take delivery** of the full lot at 1,800, paying `1,800 * lot size` in cash and receiving shares now worth only ~1,799 — and worse, you hold that long share position over the gap. Your "defined risk" spread assumed both legs would resolve together, but pin risk resolved only the short leg, stripping the hedge and leaving you with the full naked delivery obligation plus overnight exposure. The fix: **close the spread (at least the short leg) before expiry** rather than trusting the wings to net out at a pinned settlement.
