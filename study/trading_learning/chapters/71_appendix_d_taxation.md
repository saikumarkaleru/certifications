# Appendix D: Indian F&O Taxation, Charges & Broker Mechanics

You can be the sharpest options strategist in the country and still go broke if you ignore two unglamorous things: the **tax man** and the **stack of charges** that nibbles every trade. A strategy that looks beautiful on a payoff diagram is a different animal once you subtract brokerage, taxes on the trade itself, exchange fees, and finally income tax on whatever profit survives. This appendix is the honest, money-plumbing chapter — the part most courses skip — written for the Indian trader on NSE F&O.

Two warnings before we start. First, every rate, threshold and rule below **changes** — almost every Union Budget tinkers with STT, surcharge, audit limits or slab rates. So treat all numbers as "currently about" and verify the live figure before you act. Second, this appendix is education, **not** professional tax advice. For anything that touches your actual return — audit applicability, how to book expenses, advance-tax calculation — sit with a **qualified Chartered Accountant (CA)**. A good CA costs a few thousand rupees a year and routinely saves multiples of that.

## How F&O trading is taxed in India

### F&O is *business income*, not capital gains

This is the single most important idea in the appendix, and most beginners get it wrong.

When you buy a share and sell it later, your profit is a **capital gain** (short- or long-term). But futures and options are **derivatives**, and the Income Tax Act treats gains and losses from trading them as **business income**. Specifically, the law says transactions in derivatives carried out on a recognised stock exchange are **non-speculative business income**. (Intraday *equity* trading — buying and selling the same shares the same day without delivery — is *speculative* business income, a separate bucket. F&O, even if you square off in five minutes, is **non-speculative**. The European, cash-settled nature of index options does not change this.)

Why should you care about a label? Because the label decides your tax rate, what you can deduct, and how losses are treated:

- **Taxed at your slab rate, not a flat rate.** F&O profit is added to your total income (salary, interest, rent, everything) and taxed at whatever **slab** you land in. There is no special concessional rate like the 15% short-term or 12.5% long-term capital-gains rates. If your total income puts you in the 30% bracket, your F&O profit is effectively taxed around 30% (plus surcharge and cess). If you are a student or homemaker with little other income, the same profit might be taxed at 5%, 10%, or not at all up to the basic exemption. So the *same* rupee of F&O profit costs different people very different tax.
- **You can deduct expenses.** Because it is a *business*, you can subtract the genuine costs of running it: brokerage and transaction charges, internet and phone bills (the trading portion), data/charting subscriptions, advisory fees, depreciation on the computer you trade from, a portion of rent if you trade from a dedicated space, even your CA's fee. Net business profit = trading P&L minus these expenses. Keep receipts.
- **Losses are valuable — set off and carry forward.** This is the silver lining of a bad year. A non-speculative F&O **loss** can be:
  - **Set off** in the same year against almost any other head of income *except salary* — for example against interest income, rental income, or other business income.
  - **Carried forward for up to 8 assessment years** if you could not fully absorb it. A carried-forward F&O loss can be set off in future years against any business income (speculative or non-speculative). So if you lose ₹3,00,000 this year and make ₹3,00,000 next year, you may pay little or no tax next year — but only if you filed your return on time and reported the loss. **Miss the return-filing deadline and you generally lose the right to carry the loss forward.** This is why even a loss-making year deserves a properly filed ITR.

### Turnover for F&O — the "absolute profit" method

To know whether you need a **tax audit**, you first need your **turnover** — and here F&O has its own peculiar definition that confuses everyone. Your turnover is **not** the notional value of contracts you traded (that would be astronomically large). For F&O the accepted method is **absolute profit**:

```
F&O turnover (absolute-profit method)
  = sum of the ABSOLUTE values of profit and loss on each trade
  = |P&L of trade 1| + |P&L of trade 2| + ... (losses counted as positive)
```

For **options**, the historically common practice also *added* the premium received on sale to this figure, though guidance has shifted over the years toward the cleaner absolute-profit number. This is exactly the kind of detail your CA should confirm against the current ICAI guidance note.

Worked illustration: suppose over the year you make +₹40,000 on some trades and -₹25,000 on others. Your net profit is ₹15,000, but your **turnover** is |40,000| + |25,000| = **₹65,000**. Note how an active trader who churns a lot can have a small net P&L but a large turnover — turnover measures *activity*, not profit.

### Tax audit — when you need a CA to sign off

A **tax audit** (under section 44AB) means a CA formally examines your books and certifies them. Whether you need one depends on your turnover and your profit margin, and the thresholds have been **raised over the years** — so state them conceptually and check the current limit:

- If turnover is below a certain limit (currently in the range of a few crore rupees, and **higher still — up to about ₹10 crore — when nearly all your receipts and payments are digital**, which trading inherently is), audit is generally **not** required just on size.
- Audit can also get triggered through the **presumptive-taxation** interaction: if you had opted into presumptive taxation in the past and then declare profits lower than the presumptive rate (or a loss) while your income exceeds the basic exemption, an audit may apply. Because F&O margins are thin and many traders show losses, this clause historically pulled a lot of traders into audit even at modest turnover.

The honest summary: **do not eyeball this.** The audit rules are a maze of interacting sub-clauses that change with each Budget. Tell your CA your turnover, your net profit/loss, your other income, and your digital-transaction percentage, and let them determine applicability. Getting it wrong risks penalties.

### Maintaining books and paying advance tax

Two housekeeping duties follow from "F&O is a business":

- **Maintain books of account.** At minimum, keep your broker's **P&L statement, contract notes, ledger, and bank statements**. Your broker (Zerodha, Upstox, Angel One, etc.) provides a consolidated **tax P&L report** each year — download it; it is the backbone of your filing. Keep your expense bills alongside.
- **Pay advance tax.** Because there is no employer deducting TDS on your trading gains, the law expects you to pre-pay your estimated tax in **four instalments** through the year (commonly by 15 June, 15 September, 15 December and 15 March, in cumulative percentages). If your total tax liability for the year exceeds a small threshold (currently about ₹10,000) and you skip or underpay these instalments, you are charged **interest** (sections 234B/234C). Estimating advance tax on volatile trading income is genuinely hard — another reason to involve a CA, who will usually true it up at year-end.

The return itself is filed using **ITR-3** (the form for individuals with business/professional income); the simpler ITR-1/ITR-2 cannot capture F&O business income.

## The full stack of charges on an options trade

Now to the costs that hit *every* trade, before income tax even enters the picture. When you place an options order, you are not just paying brokerage. A whole stack of statutory and exchange charges rides along, and for a small-edge, high-frequency trader this stack is often the difference between profit and loss. Let us name every layer.

### The layers, one by one

1. **Brokerage.** What your broker charges to execute. **Discount brokers** charge a **flat fee per order** — currently around **₹20 per order** (or a tiny percentage, whichever is lower), the *same* whether you trade one lot or fifty. Full-service brokers charge a percentage and cost much more. Note "per order," not per lot: one order that fills 10 lots is still one brokerage charge.
2. **Securities Transaction Tax (STT).** A central tax on the trade, and for options it has **two faces**:
   - On a normal option **buy and sell**, STT is levied **only on the SELL side**, and **on the premium** (not the strike, not the notional). The rate is small — **currently about 0.1% of the sell-side premium** for options (this rate has been hiked in recent Budgets, so verify). Crucially, you pay STT when you *sell to close*, whether you are squaring off a long or a short.
   - **The expiry trap — STT on exercise of ITM options.** If you hold an option until expiry and it finishes **in-the-money (ITM)**, it is **exercised**, and STT on exercise is charged on the **intrinsic value at a much higher rate — currently about 0.125%**, and historically it was levied on a base far larger than the premium. The infamous result: traders who let a cheap ITM option get auto-exercised at expiry instead of selling it a minute before close have been hit with an STT bill **larger than the option's entire value**. **Lesson: square off ITM options before expiry rather than letting them be exercised, unless you have specifically checked the math.** For cash-settled index options this trap is less brutal than it once was, but the principle — exercise STT is punitive — still guides good practice.
3. **Exchange transaction charges.** A fee the **NSE** levies on the premium turnover (both buy and sell side), currently a small fraction of a percent of premium value. The exchange periodically revises these.
4. **SEBI turnover fee.** A tiny regulator's levy on turnover — currently around **₹10 per crore** of premium turnover. Almost negligible on small trades, but it is on the bill.
5. **Stamp duty.** A state levy, now uniform across India, charged on the **BUY side** only, currently around **0.003% of premium** for options. Small, but present on every purchase.
6. **GST (Goods and Services Tax).** Charged at **18%**, but **only on the sum of (brokerage + exchange transaction charges + SEBI fee)** — *not* on STT or stamp duty. So GST is a tax-on-the-fees, not on the trade value. It quietly inflates your real brokerage cost by 18%.
7. **DP (Depository Participant) charges.** These apply to **delivery** in the demat account — relevant for F&O mainly when a **stock option is physically settled** at expiry and shares actually move into or out of your demat. A flat per-scrip charge (currently roughly ₹13–₹20 per scrip on the sell/debit side) applies. Index options are cash-settled, so DP charges do not arise there.

### Worked rupee example — a Nifty option round-trip

Let us total the stack on one realistic round-trip. Assume Nifty is near 24,000, lot size is **75**, and you **buy** one lot of a weekly call at a premium of **₹100** and **sell** it the same day at **₹120**. (Lot sizes change — currently Nifty is around 75 — so adjust to the live value.)

```
Trade size:
  Buy:  premium 100 * 75 = ₹7,500  turnover
  Sell: premium 120 * 75 = ₹9,000  turnover
  Gross profit on the option = (120 - 100) * 75 = ₹1,500
```

Now the charges (using "currently about" rates — illustrative, verify live):

```
Brokerage:        ₹20 (buy order) + ₹20 (sell order)          = ₹40.00
STT:              0.1% on SELL premium only = 0.001 * 9,000    = ₹9.00
Exchange txn:     ~0.035%(*) on (7,500 + 9,000) = 0.00035*16,500 ≈ ₹5.78
SEBI fee:         ₹10 per crore on 16,500 turnover            ≈ ₹0.02
Stamp duty:       0.003% on BUY = 0.00003 * 7,500             ≈ ₹0.23
GST:              18% on (brokerage + exch txn + SEBI)
                  = 0.18 * (40 + 5.78 + 0.02) ≈ 0.18 * 45.80   ≈ ₹8.24
                  ------------------------------------------------------
Total charges (round-trip)                                    ≈ ₹63.27

Net profit = gross 1,500 - charges 63.27                       ≈ ₹1,436.73
```

(*) Exchange transaction-charge rates vary and are revised periodically; use your broker's brokerage calculator for the live figure.

On this *profitable* trade, charges ate about **4% of the gross profit** — annoying but survivable, because the edge (₹1,500) was large relative to the ₹63 cost. Now flip the lesson: imagine you were **scalping** for a 2-point move, gross profit (2 * 75) = ₹150. The **same ~₹63 of charges** would devour **42% of your gross**, and on a losing or break-even day the charges are pure deduction. This is precisely why **high-frequency, small-edge retail trading gets quietly bled to death by costs** even when the trader's directional calls are roughly 50/50. The market does not need to beat you — the charge stack does.

And remember: the ₹63 above is *before* income tax. If this is one of many profitable trades and you land in the 30% slab, roughly another 30% of the net is owed to the government at year-end. Always think in **after-cost, after-tax** terms.

## Broker mechanics — margins, snapshots, MTM and settlement

The last piece of plumbing is *how the broker holds your money and manages risk* while a position is open. Chapter 9 covered margin conceptually; here is the operational reality on an Indian retail platform.

### Margin: what buyers and sellers post

- **Option buyers** pay the **premium in full, up front** — `premium * lot size` — and that is their entire outlay. No additional margin, because their loss is capped at the premium.
- **Option sellers** must post a large **margin**, computed as **SPAN + Exposure**:
  - **SPAN margin** — the clearing corporation's worst-plausible-one-day-loss estimate for your position (risk-based; a riskier short pays more).
  - **Exposure margin** — an extra cushion (a few percent of notional) on top.
  Selling one lot of a Nifty option can block on the order of **₹1–1.5 lakh** of margin (it varies with volatility and strike). Spreads get **margin benefit** — because the long leg hedges the short leg, the netted margin is far smaller than for a naked short, which is one practical reason professionals trade defined-risk spreads.

### Peak-margin snapshots

SEBI tightened intraday-leverage rules with the **peak-margin** regime. Instead of checking your margin only at end of day, the clearing corporation takes **several random snapshots during the day** and requires that you had the **full required margin** at each snapshot. Your **peak** (highest) margin shortfall across these snapshots is what matters. The effect: brokers can no longer hand out large intraday leverage, and if you were under-margined at any random snapshot you face a **peak-margin penalty**. Practically — keep enough free cash that you are fully margined at *all* times, not just on average.

### MTM and auto square-off

- **Mark-to-Market (MTM).** Open positions are revalued continuously against the live price. Unrealised losses erode your available margin in real time. When your losses eat into the posted margin, you get a **margin call** — a demand to add funds.
- **Auto square-off.** If you do not meet the margin call (or if your account margin falls below the broker's maintenance threshold), the **broker's risk-management system (RMS) will forcibly close your positions** — often at the worst possible moment, in a fast-moving market, at whatever price it can get. Auto square-off also happens on **intraday product types (MIS)** near the session cut-off (commonly around 3:20–3:25 PM) if you have not exited. Treat auto square-off as a failure state, not a feature: it means you lost control of your own exit. Carry a buffer of free funds and exit on *your* terms.

### Physical settlement and expiry-week margins

For **stock** F&O (not index — index options are **cash-settled**), positions left open at expiry go to **physical delivery**: a long ITM call means you must take delivery of (and pay for) the full quantity of shares; a short ITM call means you must deliver them. The full contract value is suddenly real money.

To stop traders from sleepwalking into a delivery obligation they cannot fund, exchanges **ramp up margins through expiry week**. As expiry approaches, the margin on ITM and near-the-money stock-option positions is **progressively increased** (in steps over the final days), so that by expiry day you are essentially posting close to delivery-level margin. The practical rules:

- If you trade **stock options**, do not casually hold ITM positions into expiry unless you intend (and can fund) physical delivery. Watch your broker's expiry-week margin notices.
- **Index options (Nifty, Bank Nifty)** are **cash-settled** — no shares change hands, only the net cash difference — so physical-delivery margins do not apply, though the STT-on-exercise point (square off ITM before expiry) still deserves attention.

## The honest bottom line

Costs and taxes are not background noise — they are a structural headwind that every trade must overcome. Brokerage and the STT/exchange/GST stack quietly shrink each round-trip; the ITM-exercise STT trap can vaporise a careless expiry position; peak-margin and auto-square-off rules can force you out at the worst time; and at year-end, F&O profit is **business income taxed at your slab**, while losses — though painful — are an asset you can carry forward for **up to 8 years** *if you file on time*. Build all of this into your expectations *before* you trade, think in after-cost-after-tax rupees, keep clean books, and let a qualified CA handle the parts that move every Budget.

> **Disclaimer.** Tax laws, STT and stamp-duty rates, audit thresholds, margin rules, lot sizes and brokerage figures in India **change frequently** — often with each Union Budget or SEBI circular. Every number in this appendix is illustrative and stated as "currently about." Nothing here is tax, legal or investment advice. Before filing returns, computing turnover or audit applicability, or sizing margin, **consult a qualified Chartered Accountant and verify the current official rates** with SEBI, the NSE, and the Income Tax Department.
