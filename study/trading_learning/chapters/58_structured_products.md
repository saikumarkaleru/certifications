# Chapter 58: Structured Products — How Options Build Capital-Protected Notes

Walk into any bank's wealth-management desk in Mumbai and a relationship manager may pitch you a "market-linked" product: *"Get the upside of the Nifty, but your capital is fully protected — if the market falls, you get your money back."* It sounds like magic, a free lunch where you keep the gains and someone else eats the losses. It is not magic. It is options. Every capital-protected note ever sold is just two ordinary building blocks glued together and wrapped in a glossy brochure: a **safe bond** that quietly grows back to your principal, and a **call option** that buys you a slice of the upside. Once you can see those two parts, you can value the whole thing yourself — and decide whether the bank is offering you a fair deal or charging you handsomely for something you could assemble more cheaply.

This chapter teaches you to **decompose** a structured product the way an engineer reverse-engineers a gadget: pop the case, identify the components, price each one, and add them up. The skill matters because the entire structured-products industry depends on customers *not* doing this. The embedded option is invisible to the buyer but obvious to the issuer, and the gap between what you pay and what the parts are worth is where the fees live. By the end you will treat any "structured" or "market-linked" product as a puzzle you can solve with the option knowledge you already have.

## Core concepts

### The big idea: protection comes from a bond, upside comes from an option

A **structured product** (also called a structured note, or in India a **market-linked debenture, MLD**) is a single instrument whose return is *engineered* from simpler pieces — usually a fixed-income instrument plus one or more derivatives. The most common retail variety is the **capital-protected note** (CPN): a product that promises to return at least your original principal at maturity, plus some participation in the rise of an underlying like the Nifty 50.

The trick is an old one. Split your money into two jobs:

1. **The protection job.** Take *most* of your money and buy a safe instrument that is guaranteed to grow back to your full principal by maturity. A **zero-coupon bond** is perfect for this — a bond that pays no interest along the way but is sold at a discount and matures at face value. If you need ₹100 back in three years and rates allow it, you only need to put aside, say, ₹82 today; the bond does the rest by accreting to ₹100.

2. **The upside job.** Take the *leftover* money — the ₹18 you did not need for protection — and spend it on a **call option** on the Nifty. The call is the engine of upside: it costs little, can expire worthless (you only ever risk that ₹18), but if the Nifty rises it pays off and gives you equity-like gains.

Add the two together and you have manufactured the pitch exactly: at maturity the bond delivers your ₹100 back no matter what (capital protected), and the call delivers extra rupees if the index rose (market-linked upside). The worst case is that the market falls, the call expires worthless, and you simply get your ₹100 returned — you "lost" only the time value of money, not the rupees.

### The payoff decomposition

Write it as a formula. Let the note be on a notional principal `P`, linked to an index level. The note's value at maturity is:

`Note payoff = Zero-coupon bond + Call option`

`= P + (participation) * P * max(index return, 0)`

The bond term `P` is the floor — it never lets you fall below your principal. The call term is `0` if the index fell or was flat, and grows with the index if it rose. That `max(..., 0)` shape is the unmistakable fingerprint of a long call. The whole note is just **a riskless bond plus a long call**, the same payoff you would draw for a protective structure: a flat line at your principal, then a rising 45-degree-ish line once the index clears its starting point.

This is why capital protection is never free. The protection is *paid for by giving up yield*. Instead of earning the full bond interest in cash, you spend that interest on the option. Your "free" downside protection is funded out of the coupon you chose not to receive.

### The participation rate — why you don't get 100% of the move

Here is the part the brochure underplays. You almost never capture the **full** index move. If the Nifty rises 30%, your note might credit you only 18% or 20%. The fraction you actually capture is the **participation rate**:

`Participation rate = how much option exposure your budget can buy / full exposure`

The logic is pure arithmetic of a limited **option budget**. Return to the ₹100 note. Suppose the zero-coupon bond needed to grow back to ₹100 costs ₹82 today. That leaves ₹18 as the option budget. Now suppose a 3-year at-the-money Nifty call that gives full one-for-one participation on ₹100 of notional costs ₹25. You cannot afford it — you only have ₹18. So you buy `18 / 25 = 0.72`, i.e. **72% participation**. If the Nifty rises 30%, your note credits `0.72 * 30% = 21.6%`.

`Participation rate = option budget / cost of a full-participation call`

Three forces squeeze participation below 100%, and recognising them lets you predict whether a note will be generous or stingy:

- **Interest rates.** Higher rates make the zero-coupon bond *cheaper* (it discounts more), leaving a bigger option budget and a higher participation rate. This is why capital-protected notes are attractive to issuers when rates are high and almost impossible to build when rates are near zero — there is no coupon to spend on options.
- **Maturity.** Longer maturities give the bond more time to accrete from a smaller starting amount, freeing up more budget. A 5-year note can offer far higher participation than a 1-year note. (This is also why CPNs are typically multi-year — a 1-year note simply has too little discount to fund a meaningful call.)
- **Volatility.** Higher implied volatility makes the call *more expensive*, shrinking how much participation the budget buys. When India VIX is high, the same option budget buys less upside.

Issuers also tune participation by changing the option type: using **out-of-the-money** calls (cheaper, so higher headline participation but you only benefit after a threshold), adding a **cap** (selling away gains above some level to fund more participation below it — turning the long call into a call spread), or using **Asian/averaging** features that lower the option cost.

### The hidden costs: fees, spreads, and the issuer's margin

Now the honest part. The decomposition above assumed every component was bought at fair market price. In reality the issuer inserts its margin at each step, and because the parts are invisible to you, you cannot see where:

- **The structuring fee / sales load.** A slice of your principal — often 1% to 5% upfront, sometimes more for long-dated retail notes — is skimmed before any bond or option is bought. That directly lowers your option budget and therefore your participation.
- **Option mispricing.** The issuer "sells" you the embedded call at its own marked-up price (often using a higher implied volatility than the market), pocketing the difference. You never see a price quote for the option, so you cannot tell.
- **Bid-ask and replication costs.** Even an honest desk must hedge, and hedging costs are passed to you.

### Credit risk — protection is only as good as the issuer

The phrase "capital protected" hides a crucial caveat: **protected by whom?** The zero-coupon bond at the core of the note is an *unsecured promise of the issuer*. If the issuer (a bank, NBFC, or finance company) defaults, your "protected" principal can vanish — the protection is only as strong as the issuer's balance sheet. There is no separate guarantee fund standing behind it the way deposit insurance backs a bank FD. The famous global example is Lehman Brothers: investors who held "100% capital-protected" notes issued by Lehman discovered in 2008 that capital protection means nothing once the guarantor is insolvent. So a structured note carries **credit risk** that a plain equity or index position does not. Always ask: who is the issuer, and what is their rating?

### Why decomposition lets you judge fair vs expensive — and replicate it yourself

Here is the payoff of this whole chapter. Because you can decompose the note, you can **price it independently**:

1. Price the zero-coupon bond yourself: `PV = P / (1 + r)^T`, using the issuer's credit-appropriate yield.
2. Price the embedded call yourself using Black-Scholes (Chapter 20) and the *market* implied volatility.
3. Add them. If the sum of the fair parts is meaningfully more than what you would receive for your money, the note is **expensive** — you are overpaying for the wrapper.

And often you can **replicate it more cheaply**: simply buy a safe bond (a government security, AAA bond, or even a bank FD) for the protection leg, and use a small portion of your money to buy index call options on the NSE directly. You get the same payoff shape, you see every price, you keep the fees, and — importantly — you can split your credit risk (government bond for protection) rather than betting your whole principal on one finance company. The catch is operational: building it yourself requires an F&O account, rolling options at each expiry (Indian index options are short-dated, so a 3-year horizon means many rolls), and the discipline to manage it. The note's value-add is *convenience and a single long-dated wrapper*, not financial alchemy. You are paying for packaging.

### The Indian context: market-linked debentures (MLDs)

In India the dominant structured product is the **market-linked debenture (MLD)** — a debenture (corporate bond) whose returns are linked to an underlying such as the Nifty, a government-security yield, or a basket. Issued mostly by NBFCs and corporates and historically sold to high-net-worth investors (the minimum ticket has traditionally been large, around ₹10 lakh and reduced over time by SEBI), MLDs come in capital-protected and non-protected ("principal at risk") varieties. Conceptually they are exactly what this chapter describes: a bond component plus an embedded option payoff.

A few India-specific points to understand conceptually (rules change, so verify the current position before acting):

- **Taxation changed materially.** MLDs were historically popular largely because of a *tax* edge: if listed and held beyond a year, gains were taxed as long-term capital gains at a low rate, far below the slab rate applied to interest from an FD. The Finance Act 2023 removed this advantage — gains on MLDs are now generally taxed as **short-term capital gains at the investor's slab rate** regardless of holding period. Much of the historical appeal of MLDs was this tax arbitrage, not the option payoff itself; once it was withdrawn, the products became markedly less attractive. This is a vivid lesson: a structured product's appeal is often driven by tax or regulatory quirks rather than genuine financial value.
- **Regulation.** SEBI regulates the issuance, listing, and disclosure of MLDs and has tightened norms over time — mandatory listing, third-party valuation, and reduced minimum denomination to improve transparency and access. The embedded-option valuation must be disclosed, which in principle lets a careful investor do the decomposition this chapter teaches.
- **Liquidity.** MLDs are thinly traded. Selling before maturity often means accepting a poor secondary-market price, so treat the stated maturity as the real horizon.

The professional takeaway: in India, evaluate any MLD on the *post-2023* tax reality and on the decomposed economics, not on a historical pitch.

## Worked example (₹, Nifty)

A wealth desk offers Priya a **3-year, 100% capital-protected, Nifty-linked note** with a notional of **₹10,00,000**. The terms: at maturity she receives her ₹10,00,000 back, plus a participation in any rise of the Nifty from its starting level. Let us build and value it.

**Market inputs (assumed):**
- Issuer's 3-year zero-coupon yield: `r = 7%` per year (compounded annually).
- Nifty starting level: 24,000.
- A 3-year at-the-money Nifty call providing full 1-for-1 participation on the ₹10,00,000 notional costs **₹2,50,000** at fair market implied volatility.
- Upfront structuring fee charged by the desk: **2%** of notional.

**Step 1 — Size the protection leg (the zero-coupon bond).**
To guarantee ₹10,00,000 in 3 years at 7%, the desk must set aside today:

`PV = 10,00,000 / (1.07)^3 = 10,00,000 / 1.225043 = ₹8,16,298`

So about **₹8,16,298** buys the bond that accretes back to ₹10,00,000. This is the protection.

**Step 2 — Find the option budget.**
Priya pays ₹10,00,000. First the desk takes its 2% fee:

`Fee = 2% * 10,00,000 = ₹20,000`

Money left to invest: `10,00,000 - 20,000 = ₹9,80,000`.
After buying the bond: `9,80,000 - 8,16,298 = ₹1,63,702` is the **option budget**.

**Step 3 — Compute the participation rate.**
A full-participation call costs ₹2,50,000 but Priya's budget is only ₹1,63,702:

`Participation rate = 1,63,702 / 2,50,000 = 0.655 ≈ 65%`

So the note offers about **65% participation** in the Nifty's rise.

**Step 4 — Payoff at maturity, under scenarios.**

- **Nifty falls 20%** (to 19,200): the call expires worthless. Priya receives her **₹10,00,000** — capital protected. (Her real cost: 3 years of forgone ~7% yield, plus the ₹20,000 fee.)
- **Nifty flat** (24,000): call worthless again, she gets **₹10,00,000**.
- **Nifty rises 30%** (to 31,200): the note credits `0.655 * 30% = 19.65%`. Payoff `= 10,00,000 + 0.655 * 30% * 10,00,000 = 10,00,000 + 1,96,500 = ₹11,96,500`.
- **Nifty rises 50%**: credited `0.655 * 50% = 32.75%`, payoff **₹13,27,500** — versus ₹15,00,000 if she had held the index directly (but with full downside risk).

**Step 5 — Was it fair? Could Priya do it herself?**
The fair value of what she bought: bond (₹8,16,298) + 65% of a ₹2,50,000 call (₹1,63,702) = ₹9,80,000. She paid ₹10,00,000. The ₹20,000 gap is the fee — about 2%, plus whatever extra margin is hidden in how the desk priced the call's volatility. If Priya instead bought a 3-year AAA bond herself for ~₹8,16,000 and spent ~₹1,84,000 on Nifty calls she rolled herself, she could reach roughly **73% participation** (1,84,000 / 2,50,000) for the same ₹10,00,000 — capturing the fee for herself — at the cost of doing the work and managing the rolls. That difference, 65% versus 73%, *is* the price of the wrapper.

## Common mistakes / risk note

- **Believing "capital protected" means risk-free.** It protects *nominal* principal only, and only if the issuer stays solvent. You still bear (a) credit/default risk of the issuer, (b) inflation risk — getting ₹10 lakh back in 3 years is worth less in real terms, and (c) **opportunity cost** — that money could have earned a safe 7% in a bond, so "breaking even" is actually a real loss.
- **Ignoring participation below 100%.** Marketing shouts "Nifty-linked!" and whispers the participation rate. A 50% participation note in a market that rises 20% gives you 10% — barely better than the FD you gave up, with more risk.
- **Not pricing the embedded option.** If you cannot see a price for the call, assume the issuer marked it expensive. Demand the valuation disclosure (SEBI requires it for MLDs) and check it against market implied volatility.
- **Forgetting caps and knock-outs.** Many "enhanced participation" notes secretly *sell* away your upside above a level (a call spread) or knock out entirely if the index touches a barrier. High headline participation often means your upside is capped.
- **Treating MLDs as the old tax play.** Post-2023, the tax advantage that made Indian MLDs attractive is gone. Re-evaluate on current rules.
- **Overrating liquidity.** You are likely locked in until maturity at a fair-ish price. Size accordingly.

## Key takeaways

- A capital-protected note = **zero-coupon bond (returns your principal) + call option (gives upside)**. Decompose every structured product into these parts.
- The payoff is `principal + participation * max(index return, 0)` — the unmistakable shape of a bond plus a long call.
- The **participation rate** is below 100% because the option budget is limited: `budget / cost of full-participation call`. Higher rates and longer maturities raise it; higher volatility and fees lower it.
- Protection is **funded by forgone yield** — it is never free. Your worst case is getting principal back having earned nothing in real terms.
- Watch the **hidden costs**: structuring fees, marked-up option volatility, and the **credit risk** of the issuer (capital protection dies if the issuer defaults).
- You can often **replicate** a note yourself — safe bond plus exchange-traded index calls — capturing the fee and controlling your credit exposure, at the cost of operational effort.
- In India, **MLDs** are the main structured product; the Finance Act 2023 removed their tax edge, so judge them on decomposed economics, not the old pitch.

## Practice problems

1. **(Conceptual)** Explain in one or two sentences why a capital-protected note cannot be built profitably when interest rates are near zero.

2. **(Numeric)** A 5-year, 100% capital-protected note has notional ₹5,00,000. The issuer's 5-year zero-coupon yield is 8% annually. How much must be set aside today for the protection leg, and what is the option budget if there are no fees?

3. **(Numeric)** Using your answer to Problem 2, suppose a 5-year full-participation Nifty call on the ₹5,00,000 notional costs ₹1,60,000. What is the participation rate? If the Nifty rises 40% over the 5 years, what does the investor receive?

4. **(Conceptual)** Two otherwise identical capital-protected notes are offered, one when India VIX is 12 and one when India VIX is 22. Which offers the higher participation rate, and why?

5. **(Conceptual)** A note advertises "120% participation in the Nifty." Knowing that the issuer's budget cannot normally buy more than 100% of a plain call, what feature has the issuer most likely added to push participation above 100%? What does the investor give up?

6. **(Numeric / judgement)** A 3-year note on ₹2,00,000 charges a 4% upfront fee. The 3-year zero-coupon yield is 7%, and a full-participation call costs ₹52,000. Compute the participation rate. Then compute it for a fee of 1%. By how many percentage points does the higher fee cut participation?

## Solutions

**1.** With rates near zero, the zero-coupon bond needed to return your full principal costs almost the entire principal (there is little discount). That leaves essentially no option budget, so there is nothing left to buy the upside call. Capital protection is funded by forgone interest, and at zero rates there is no interest to forgo.

**2.** Protection leg: `PV = 5,00,000 / (1.08)^5`. `(1.08)^5 = 1.469328`, so `PV = 5,00,000 / 1.469328 = ₹3,40,292`. Option budget = `5,00,000 - 3,40,292 = ₹1,59,708`.

**3.** Participation rate `= 1,59,708 / 1,60,000 = 0.998 ≈ 100%` (the high rate and long 5-year maturity nearly fully fund the call). On a 40% Nifty rise the investor receives `5,00,000 + 0.998 * 40% * 5,00,000 = 5,00,000 + 1,99,600 = ₹6,99,600` — close to the full uncapped upside, plus full principal protection.

**4.** The note issued when India VIX is **12** offers the higher participation rate. Lower implied volatility makes the embedded call **cheaper**, so the same option budget buys a larger fraction of full participation. When VIX is 22 the call costs more and the budget buys less upside. (This is why capital-protected notes are easier to make attractive in calm markets — and why you should be suspicious of generous-looking notes launched when volatility is high.)

**5.** The issuer has most likely added a **cap** on the upside — i.e. sold away the investor's gains above some index level (turning the long call into a call spread). Selling that upper call brings in premium that funds extra participation on the lower portion. The investor gives up all gains above the cap, so "120% participation" applies only up to a ceiling; in a strong bull market the capped note can badly underperform the index. (Other budget-stretching tricks: using out-of-the-money calls with a threshold, or averaging/Asian features.)

**6.** With a 4% fee: fee `= 0.04 * 2,00,000 = ₹8,000`; investable `= ₹1,92,000`. Protection leg `= 2,00,000 / (1.07)^3 = 2,00,000 / 1.225043 = ₹1,63,260`. Option budget `= 1,92,000 - 1,63,260 = ₹28,740`. Participation `= 28,740 / 52,000 = 0.553 ≈ 55%`.

With a 1% fee: fee `= ₹2,000`; investable `= ₹1,98,000`. Option budget `= 1,98,000 - 1,63,260 = ₹34,740`. Participation `= 34,740 / 52,000 = 0.668 ≈ 67%`.

The higher fee cuts participation by about `67% - 55% = 12 percentage points`. This shows how directly upfront fees eat into your upside: a 3-percentage-point difference in fee translated into roughly a 12-point loss of participation, because the option budget is the thin residual left after the bond — small changes to it swing the upside a lot.
