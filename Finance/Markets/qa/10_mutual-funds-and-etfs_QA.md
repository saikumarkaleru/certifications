# Q&A — Mutual Funds and ETFs

Companion practice bank for Chapter 10. Every question is followed by a full answer. Section A checks the core concepts, B puts them to work on numbers and situations, C rehearses interview questions with model answers, and D sharpens judgement on the distinctions people get wrong.

---

## Section A — Concept Check

**A1. What single problem do mutual funds exist to solve, and how does pooling solve it?**

The problem is that a small investor individually cannot afford three things at once: **diversification, professional expertise, and access** to markets. Buying 50 stocks needs lakhs of rupees, reading annual reports needs full-time skill, and reaching US equities or gold bullion is nearly impossible alone. **Pooling** solves all three simultaneously — many small investors hand money to one vehicle, so collectively they can afford a diversified basket, a professional manager, and cheap market access. Each investor owns a proportional slice, so ₹500 buys exposure to the whole basket. Everything else in the chapter is a consequence of this one idea.

**A2. Define NAV and write its formula. When is it calculated?**

NAV (Net Asset Value) is the **per-unit price** at which you buy and redeem an open-ended fund. The formula is:

NAV = (Market value of securities + Cash − Liabilities and accrued expenses) ÷ Total units outstanding.

It is calculated **once every business day after markets close**, using the day's closing prices. That is why an open-ended fund transaction executes at end-of-day NAV, not at a live intraday price.

**A3. Why is a mutual fund described as a "pass-through vehicle"?**

Because the fund itself is not a company earning profits for shareholders — it is a **conduit**. It owns securities on behalf of unit holders and passes gains, losses, income, and risk straight through to them. When the underlying shares rise, the NAV rises and the investor benefits; when they fall, the investor bears it. The fund is a legal wrapper, not a profit centre.

**A4. Explain the three-tier trust structure and the single principle behind it.**

An Indian mutual fund is a **trust** under the Indian Trusts Act, governed by SEBI (Mutual Funds) Regulations, 1996, with three tiers: the **Sponsor** (promoter, e.g., SBI, who sets it up), the **Trustees** (legal owners of the assets who hold them in trust for investors and supervise the AMC), and the **AMC** (the operating company that employs fund managers and runs the schemes). The single principle is **separation**: the people who *decide* what to buy (AMC) never *hold* the assets (custodian) and do not *own* them (trustees do, on your behalf). This ring-fences your money — even if the AMC goes bankrupt, the assets belong to the trust, not the AMC's balance sheet.

**A5. What is the difference between an open-ended and a closed-ended fund?**

An **open-ended** fund continuously creates and cancels units on demand at NAV — the pool "breathes" as money flows in and out, and it has no maturity, giving full liquidity. A **closed-ended** fund issues a **fixed number of units** at launch (NFO) with a fixed maturity; to exit early you must sell on a stock exchange, often at a **discount to NAV**. A Fixed Maturity Plan is the classic closed-ended example.

**A6. In one sentence, what is an ETF, and what are its three defining differences from an index fund?**

An **ETF is a mutual fund scheme that trades on a stock exchange like a share.** The three differences from an index fund are: (1) it **trades live intraday** at real-time market prices, not at end-of-day NAV; (2) it **requires a demat account**, whereas an index fund is bought directly from the AMC; and (3) it uses the **Authorised Participant creation/redemption mechanism** to keep its market price tethered to NAV. Both are passive — the difference is the wrapper, not the strategy.

**A7. How does arbitrage keep an ETF's market price close to its NAV?**

Through **Authorised Participants (APs)** exploiting any gap. If a Nifty ETF trades at ₹250 while the underlying basket (iNAV) is worth ₹248, an AP buys the basket for ₹248, exchanges it "in-kind" with the fund for ETF units, and sells them at ₹250 — pocketing ₹2. That selling pushes the ETF price back down toward ₹248. At a discount the reverse happens. This constant arbitrage — a live application of the law of one price — keeps market price and NAV aligned.

**A8. What is the Total Expense Ratio (TER), and how is it charged?**

TER is the **annual fee** for running the fund, expressed as a percentage of assets, covering management, administration, marketing (in regular plans), and custody. It is **not billed separately** — it is quietly deducted daily from the fund's assets, so the NAV you see is already net of expenses. SEBI caps it on a sliding scale (bigger funds must charge less): active equity funds run roughly 1.0–2.25%, index funds 0.1–0.5%, and ETFs as low as 0.03–0.10%.

**A9. Distinguish Direct and Regular plans.**

They are two versions of the **same scheme** — same portfolio, same manager. A **Regular plan** pays a commission to the distributor, baked into a higher TER. A **Direct plan** (bought straight from the AMC or a platform like Zerodha Coin or MF Central) has no commission, so its TER is lower and its NAV grows faster — typically ~0.5–1% higher return per year for the identical portfolio.

**A10. What is a SIP, and why is it a method rather than a product?**

A SIP (Systematic Investment Plan) is investing a **fixed amount at fixed intervals** (usually monthly) into a fund, automatically. It is a *method*, not a product, because you can run a SIP into almost any open-ended scheme — it describes *how* you invest, not *what* you buy. Its power comes from **rupee cost averaging** (fixed rupees buy more units when NAV is low, fewer when high), **discipline** (it automates saving and resists the urge to stop when markets fall), and **affordability** (starts at ₹100–500).

---

## Section B — Applied / Scenario Questions

**B1. A fund owns securities worth ₹500 crore, holds ₹5 crore cash, and owes ₹1 crore in expenses, with 42 crore units outstanding. Compute the NAV.**

Net assets = 500 + 5 − 1 = **₹504 crore**. NAV = 504 ÷ 42 = **₹12.00 per unit**. That ₹12 is the price at which an investor buys or redeems a unit that day.

**B2. You invest ₹50,000 in a fund at NAV ₹1,250. Two years later NAV is ₹1,700 and you redeem after the exit-load window. Compute units, final value, and gain.**

Units allotted = 50,000 ÷ 1,250 = **40 units**. Value at redemption = 40 × 1,700 = **₹68,000**. Gain = 68,000 − 50,000 = **₹18,000**, a **36% absolute return**. No exit load applies (past the window). Long-term capital gains tax on equity applies above the ₹1.25 lakh annual exemption.

**B3. You invest ₹6,000 a month for three months at NAVs of ₹100, ₹75, and ₹120. Show that your average cost beats the average NAV.**

Units bought: 6,000/100 = 60; 6,000/75 = 80; 6,000/120 = 50 → total **190 units** for ₹18,000.
Simple average NAV = (100 + 75 + 120) / 3 = **₹98.33**.
Your actual average cost = 18,000 ÷ 190 = **₹94.74 per unit**.
Because you bought *more* units in the cheap month (80 at ₹75) and *fewer* in the dear month (50 at ₹120), your effective cost (₹94.74) is below the simple average price (₹98.33). That gap is the mechanical benefit of rupee cost averaging.

**B4. Two funds both earn 12% gross on ₹10 lakh over 25 years. Fund A charges TER 2.0%, Fund B charges 0.3%. Roughly how much does the fee gap cost?**

Fund A nets ~10% → ₹10 lakh × 1.10^25 ≈ **₹1.08 crore**. Fund B nets ~11.7% → ₹10 lakh × 1.117^25 ≈ **₹1.55 crore**. The 1.7% annual fee difference silently costs about **₹47 lakh** over 25 years. Costs compound against you exactly as returns compound for you — the single strongest argument for low-cost passive investing.

**B5. A Nifty ETF trades at ₹252 on the exchange while its iNAV is ₹250. Is it at a premium or discount, and what will an Authorised Participant do?**

It trades at a **₹2 premium** to fair value. The AP buys the underlying basket of Nifty stocks for ₹250 per creation unit, delivers it in-kind to the fund in exchange for new ETF units, and sells those units on the exchange at ₹252 — capturing ₹2 risk-free. That selling supply pushes the ETF price back down toward ₹250, closing the premium.

**B6. Priya wants Nifty 50 exposure via a monthly ₹5,000 SIP and no demat account. Rahul wants the lowest possible cost and intraday control. Which vehicle suits each?**

**Priya → a Nifty 50 Index Fund (Direct)**: no demat needed, SIP-friendly, transacts at day-end NAV, TER ~0.20%. It automates everything she wants. **Rahul → a Nifty ETF (e.g., Nifty BeES) through a demat account**: TER as low as ~0.05% and live intraday pricing, but he must place orders himself, pay brokerage, and watch the market-price-vs-iNAV gap in illiquid moments. Both get essentially identical underlying exposure; the choice is convenience/automation versus cost/control.

**B7. An investor redeems an equity fund 8 months after buying, with a 1% exit load, when the value is ₹1,20,000. What does the load cost, and why does it exist?**

The exit load is 1% of ₹1,20,000 = **₹1,200**, deducted from redemption proceeds (net ≈ ₹1,18,800). It exists to **discourage short-term churning** and to protect long-term holders from bearing the transaction costs generated by others' quick redemptions. Equity funds commonly charge 1% within one year; liquid funds have near-zero loads because their whole purpose is short-term parking.

**B8. An investor picks a "dividend/IDCW" plan expecting extra income on top of growth. Explain why this is a misunderstanding.**

An IDCW payout is **carved out of the fund's own NAV** — when the fund pays ₹5 per unit, the NAV drops by ₹5. It is **your own capital returned**, not a bonus generated on top of it, and post-2020 it is taxed in the investor's hands at slab rate. For an investor who does not need periodic cash, a **Growth plan** is usually better because the money stays invested and compounds instead of being paid out and taxed.

---

## Section C — Interview-Style Questions (with model answers)

**C1. "Walk me through what happens to my money from the moment I invest in an open-ended fund."**

*Model answer:* You send money and receive **units at that day's NAV**, which mints new units and expands the pool. The money joins the pool and the **fund manager deploys it** into the scheme's mandated securities. The portfolio's value then moves daily with market prices, and each evening the **NAV is recalculated** as (assets − liabilities) ÷ units. When you redeem, the fund **cancels your units** at the prevailing NAV, shrinks the pool, and pays you out minus any exit load and tax. The key point is that you always transact **directly with the fund at NAV** — never with another investor.

**C2. "ETF versus index fund — when would you recommend each?"**

*Model answer:* Both are passive and track the same index, so the underlying exposure is identical; the difference is the wrapper. I'd recommend an **index fund** for a hands-off investor running SIPs — no demat account, automated monthly investing, and transaction at day-end NAV, so no worrying about intraday spreads. I'd recommend an **ETF** for someone who already has a demat account and wants the **lowest expense ratio** and **intraday trading control**, provided they're comfortable placing orders and checking that the market price is close to iNAV, since thin liquidity can open a premium or discount. In short: index fund for convenience and automation, ETF for cost and control.

**C3. "Why is the three-tier trust structure safer than handing money to an individual portfolio manager?"**

*Model answer:* Because it **separates decision-making from custody and ownership**. The AMC decides what to buy, but a SEBI-registered **custodian physically holds** the securities and the **trustees legally own** them on the investors' behalf, with at least two-thirds of trustees independent. No one who makes investment decisions ever touches the assets. So even if the AMC becomes insolvent, investor money is **ring-fenced in the trust** and cannot be seized by the AMC's creditors. With an individual manager, the person choosing investments also controls the money — a structural conflict the trust model eliminates. This protects against fraud and misappropriation, though not against market losses.

**C4. "Most active funds underperform their benchmark. Why, and does active management still have a role?"**

*Model answer:* Two reasons. First, **costs** — an active fund charging 1.5–2% must beat the index by that margin every year just to break even, and few do consistently after fees (SPIVA reports document this globally and increasingly in India). Second, **market efficiency** — in liquid, well-researched markets, prices already reflect available information, so durable stock-picking edges are rare and hard to identify in advance. That said, active management still has a role in **less-efficient corners** — small-caps, credit and debt, and emerging themes — where information gaps are larger and a skilled manager can genuinely add value. My default for a core equity allocation would be low-cost passive, with active used selectively where inefficiency justifies the fee.

**C5. "Explain rupee cost averaging to a first-time investor and why timing the market is a trap."**

*Model answer:* When you invest a **fixed rupee amount** every month, the same amount automatically buys **more units when the price is low and fewer when it's high**. Over time your average cost per unit ends up **below the average price**, without you predicting anything. Trying to time the market — waiting for the "bottom" — is a trap because it requires being right twice (when to exit and when to re-enter), and the emotional pull is exactly backwards: people stop buying when markets fall, which is precisely when units are cheapest. A SIP removes that decision entirely: it invests mechanically on the same date regardless of mood, converting volatility from an enemy into a mild advantage.

**C6. "A client says 'this fund has a NAV of ₹10, so it's cheaper than the one at ₹500 — better value.' How do you respond?"**

*Model answer:* I'd gently correct the premise. **NAV is not like a stock price** — a low NAV doesn't mean the fund is cheap or has more room to grow. NAV simply reflects how long the fund has existed and how much it has already appreciated. What matters is the **percentage return** going forward, which is identical whether you hold 100 units of a ₹10 fund or 2 units of a ₹500 fund for the same ₹1,000 invested — a 10% rise makes both worth ₹1,100. The right basis for choosing is the strategy, the expense ratio, the track record, and the risk level, not the level of the NAV.

---

## Section D — Multiple-Choice Questions (with reasoning)

**D1. NAV of an open-ended fund is calculated:**
A) Every second, live during trading hours
B) Once every business day after markets close
C) Only when an investor redeems
D) Weekly

**Answer: B.** NAV uses the day's closing prices and is struck once after market close; open-ended transactions execute at that end-of-day figure. Live intraday pricing (A) describes an ETF's *market* price, not a fund's NAV.

**D2. In the three-tier structure, which entity legally owns the fund's assets on behalf of investors?**
A) The AMC
B) The Sponsor
C) The Trustees
D) The Custodian

**Answer: C.** The **trustees** legally own the assets in trust for unit holders and oversee the AMC. The AMC (A) only manages, the sponsor (B) sets it up, and the custodian (D) physically holds/safekeeps securities — a deliberate separation so no single party both decides and owns.

**D3. Which is NOT a defining feature of an ETF versus a plain index fund?**
A) Trades intraday at market prices
B) Requires a demat account
C) Uses Authorised Participants for creation/redemption
D) Actively tries to beat the index

**Answer: D.** Most ETFs are **passive** — they track an index, not beat it. A, B, and C are all genuine ETF distinctions. Active management is the opposite of what a typical index ETF does.

**D4. The Total Expense Ratio is charged to the investor by:**
A) A separate annual invoice
B) A one-time fee at purchase
C) Daily deduction from the fund's assets, reflected in NAV
D) Only when the fund outperforms

**Answer: C.** TER is **quietly deducted daily** from fund assets, so the published NAV is already net of it — there is no separate bill. That invisibility is exactly why investors underestimate its long-term drag.

**D5. Compared with a Regular plan, a Direct plan of the same scheme has:**
A) A different portfolio and manager
B) A lower TER and higher NAV growth
C) A higher commission built in
D) A guaranteed higher return regardless of the fund

**Answer: B.** Same portfolio and manager, but the Direct plan **strips out distributor commission**, so its TER is lower and NAV compounds faster — typically ~0.5–1% more per year. It is not a "guaranteed" higher return in absolute terms (D is too strong); it is a lower-cost version of the identical fund.

**D6. Rupee cost averaging results in an average cost per unit that is:**
A) Always equal to the average NAV
B) Lower than the simple average NAV when prices fluctuate
C) Always higher than the average NAV
D) Irrelevant to the number of units bought

**Answer: B.** Because fixed rupees buy more units at low prices and fewer at high prices, the weighting pulls the **effective cost below the simple average price** whenever NAV fluctuates (as B3 demonstrated: ₹94.74 vs ₹98.33). Only if the price never moved would they be equal.

**D7. A closed-ended fund investor who wants to exit before maturity must:**
A) Redeem units directly with the AMC at NAV
B) Wait — early exit is impossible
C) Sell the units on a stock exchange, possibly at a discount to NAV
D) Convert to an open-ended fund first

**Answer: C.** Closed-ended units are fixed in number and not redeemable on demand; the exit route is the **secondary market**, where the price can trade at a discount (or premium) to NAV. This liquidity difference is the core disadvantage versus open-ended funds.

**D8. An ETF trading below its iNAV (at a discount) is corrected when an Authorised Participant:**
A) Buys ETF units in the market and redeems them in-kind for the underlying basket
B) Issues new units to the public
C) Lowers the fund's TER
D) Waits for the NAV to fall to the market price

**Answer: A.** At a discount, the AP **buys the cheap ETF units** and redeems them with the fund for the more-valuable underlying basket, profiting from the gap. That buying pressure lifts the ETF price back toward iNAV. It is the mirror image of the premium-arbitrage in B5.

**D9. Which statement about mutual fund risk is correct?**
A) The trust structure guarantees against market losses
B) Equity fund NAVs cannot fall more than 10%
C) The structure protects against fraud and misappropriation, not market losses
D) Mutual funds are as safe as bank fixed deposits

**Answer: C.** The trust/custodian separation ring-fences money against theft and AMC insolvency, but **NAV still moves with markets** — equity funds can fall 30%+ in a crash. "Mutual fund investments are subject to market risks" is a substantive warning, not a formality.

**D10. Which regulator governs Indian mutual funds, and how does its style compare with the US SEC?**
A) RBI; both are purely disclosure-based
B) SEBI; SEBI is more prescriptive (categories, TER caps), the SEC leans on disclosure
C) SEC; SEBI has no role in India
D) AMFI; it is the statutory regulator

**Answer: B.** **SEBI** regulates Indian mutual funds under the 1996 Regulations and is comparatively **prescriptive** — rigid scheme categories, hard TER caps, a mandatory risk-o-meter. The **US SEC** (Investment Company Act, 1940) leans more on **full disclosure**, allowing funds more latitude but demanding they disclose it. AMFI (D) is an industry self-regulatory body, not the statutory regulator.

---

*End of Q&A — Mutual Funds and ETFs.*
