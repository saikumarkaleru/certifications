<!-- v2-deep -->

# Chapter 02 — Types of Financing & Financial Markets

## 1. The Problem — Where Will the Money Come From, and What Will It Cost You?

In Chapter 01 we established the mission of Financial Management: maximise shareholder wealth through three decisions — **invest, finance, distribute**. This chapter lives entirely inside the *second* decision: **financing**. The invest decision decides *what assets to buy*. But every asset — a factory, a fleet of trucks, a month's inventory — has to be *paid for*. The money to pay for it is called **capital**, and capital is never free and never neutral. Somebody hands it over, and in exchange they attach strings: a fixed interest cheque every quarter, a claim on your profits, a right to vote at your AGM, a deadline for repayment.

So the financing problem is not "can I find money?" It is: **"Of all the different pools of money I could tap, which mix leaves my shareholders richest and my company safest?"** Consider a concrete dilemma. Vishnu Steels needs ₹100 crore to build a new plant that will last 20 years. Vishnu's treasurer has offers:

- A bank will lend ₹100 crore at 9%, repayable over 3 years.
- Debenture-holders will lend ₹100 crore at 11%, repayable in 15 years.
- Equity investors will give ₹100 crore for shares — no repayment, no fixed return, but they now own a slice of the company and will demand ~16% return via dividends and capital gains.

Every one of these "works" in the narrow sense that cash arrives. But choosing wrong is fatal. Fund a 20-year plant with a 3-year bank loan and you must repay ₹100 crore before the plant has earned it back — you will be forced to refinance at the worst possible moment or sell the plant at a loss. Fund it entirely with 16% equity and you have starved shareholders of the cheaper 11% money that would have magnified their returns. Fund it with too much debt and one bad year of low profits leaves you unable to pay interest — and unpaid interest means insolvency.

The **source of finance matters** because each source carries a different bundle of four attributes, and getting the bundle wrong destroys value even when the project itself is sound.

**The deeper point — financing does not create value, it *distributes* it (and can leak it).** A subtle idea the examiner rewards in theory answers: in a perfect, tax-free, frictionless world, the *pie* (firm value) is fixed by the assets and how well they are run — how you *slice* the financing changes only who gets which slice, not the size of the pie (this is the seed of the Modigliani–Miller idea you meet in Capital Structure). Financing choice starts to *matter* for value only once we admit **real-world frictions**: (i) the **tax shield** on interest (debt leaks less to the taxman), (ii) **financial distress and bankruptcy costs** (too much debt makes the pie itself shrink), (iii) **flotation/issue costs**, (iv) **information asymmetry** (managers know more than investors, so issuing equity can signal "shares are overvalued" and depress the price), and (v) **agency costs**. Everything practical in this chapter — why debt is cheap, why over-borrowing is lethal, why firms prefer retained earnings first — is one of these frictions in disguise.

*Figure 1 — the four attributes that make the choice of source a real decision, not a formality.*

```mermaid
flowchart TD
    A["Choice of a source of finance"] --> B["Cost - what return must we pay"]
    A --> C["Risk - does it force fixed payments"]
    A --> D["Control - does it dilute owners' votes"]
    A --> E["Maturity - when must it be repaid"]
    B --> F["Wrong mix destroys shareholder value"]
    C --> F
    D --> F
    E --> F
```

## 2. The Core Idea — Money Has a Personality, and You Are Assembling a Team

Think of raising finance not as filling a bucket but as **hiring a team**. Each type of financier is a different kind of teammate with a different temperament and a different price.

- **The Debt-holder is a landlord.** You rent his money. He does not care whether you have a brilliant year or a terrible one — the rent (interest) is due on the first of the month, in full, or he evicts you (drags you toward insolvency). Because his return is fixed and legally enforceable, he takes little risk, so he charges a *low* rent. And a landlord never tells you how to run your business — no voting rights, no dilution of control. But he insists on a *lease term*: the money must be returned by a date.

- **The Equity-holder is a business partner.** She does not want rent; she wants a *share of the upside*. In a bad year she accepts nothing; in a great year she expects to get rich alongside you. Because she absorbs your risk — she is last in the queue if things go wrong — she demands a *high* return to compensate. And because she is a partner, she gets a *vote*: control is shared. But there is no repayment date — partnership capital is permanent.

- **The Preference-holder is a hybrid tenant-partner.** She takes a fixed dividend like rent, but only if profits allow, and she waits behind the landlord in the repayment queue. Middling risk, middling cost, usually no vote.

The art of financing is **assembling the right team for the job you're doing.** A long, patient project needs patient, permanent partners (equity) and long-lease landlords (long-term debt). A quick, self-liquidating job — like buying inventory you'll sell in two months — needs a short-term landlord (a bank overdraft) you can pay off the moment the cash comes in. This single instinct — *match the life of the money to the life of the asset* — is the **matching principle**, and it is the spine of this whole chapter.

**Two teammates the beginner overlooks — spontaneous financiers and internal financiers.** Not every teammate is recruited by a formal contract. **Spontaneous sources** (trade credit from suppliers, outstanding wages, accrued taxes) arrive *automatically* as the business operates — the supplier who lets you pay in 45 days is silently financing your inventory, for free, without a single negotiation. And the cheapest, most obedient teammate of all is your own retained profit — **internal financing** — which asks no issue cost, no dilution, and no fixed cheque, but which still carries the hidden price of the return your shareholders could have earned elsewhere. A complete answer classifies sources not only by maturity and ownership but by whether they are **negotiated vs spontaneous** and **internal vs external** — three cross-cutting lenses the examiner can attack from.

*Figure 1A — three cross-cutting lenses to classify any source, so a "classify the following" question can never surprise you.*

```mermaid
flowchart TD
    X["Any source of finance"] --> A1["By maturity - long medium short"]
    X --> A2["By ownership - owners funds vs borrowed funds"]
    X --> A3["By origin - internal vs external"]
    X --> A4["By effort - negotiated vs spontaneous"]
    A4 --> S1["Spontaneous - trade credit - accrued wages - accrued taxes"]
    A4 --> S2["Negotiated - equity - debentures - term loans - CP"]
```

## 3. Why It's Built This Way — Risk, Return, and the Queue

Everything about financing flows from one iron law of finance: **higher risk demands higher return.** A financier who bears more risk must be paid more, or he walks away. This single law, applied to the *queue of claims* on a company's cash and assets, explains why every source is priced the way it is.

Picture the company's cash flowing out each year, and imagine the claimants standing in a queue with buckets:

1. **Debt-holders** stand at the *front*. They are paid interest first, and in liquidation their principal is repaid first (especially if secured against assets). Standing first = low risk = they accept the *lowest* return. Bonus: interest is a business expense, so it is **tax-deductible**, making debt cheaper still to the company.
2. **Preference shareholders** stand in the *middle*. Paid after debt, before equity. Medium risk = medium return. Their dividend is *not* tax-deductible (it's an appropriation of profit, not an expense).
3. **Equity shareholders** stand at the *back*. They get only what's left — the "residual". In a bad year, nothing. In liquidation, they're paid last and often get zero. Highest risk = they demand the *highest* return.

*Figure 2 — the queue of claims. Position in the queue determines risk, which determines cost.*

```mermaid
flowchart LR
    P["Company profits and assets"] --> D["1 Debt-holders paid first - lowest cost - tax deductible"]
    D --> PR["2 Preference holders paid next - medium cost"]
    PR --> E["3 Equity holders paid last - residual - highest cost"]
    E --> R["Retained earnings ploughed back for owners"]
```

This queue explains a crucial and counter-intuitive fact that trips up beginners: **equity is the most expensive source of finance, not the cheapest.** Newcomers think "we don't pay interest on shares, so equity is free." Wrong. Equity holders bear the most risk and therefore demand the highest return (16–18% is typical vs 9–11% for debt). It just doesn't arrive as a contractual cheque — it arrives as the *expectation* of dividends plus capital appreciation, which management ignores at its peril.

So why not fund everything with cheap debt? Because the same fixed cheque that makes debt cheap also makes it **dangerous**. Interest must be paid whether you earn ₹100 crore or ₹1 crore. This is **financial risk** — the risk created by fixed financing charges. A little debt magnifies shareholder returns (financial leverage, Chapter on Leverage). Too much debt magnifies losses and can force insolvency. The financing decision is therefore a **balancing act** between the cheapness of debt and the safety of equity — a theme that recurs throughout FM.

**Digging one level deeper — three distinct "whys" hide inside the queue.** Beginners lump the debt-equity cost gap into one idea ("risk"). The examiner rewards students who separate the *three* independent reasons debt is cheaper:

1. **Priority of claim (lower business risk borne).** Being first in the queue for both interest and principal genuinely lowers the lender's exposure, so the *required* return is lower even before tax.
2. **Security / charge on assets.** A secured lender can seize pledged assets, lowering loss-given-default, so a secured debenture is cheaper than an unsecured one — risk, again, but a *different* slice of it.
3. **The tax shield — a pure government subsidy, not a risk effect at all.** Even if debt and equity bore *identical* risk, debt would still be cheaper *to the company* because interest is deducted before tax while dividends are not. This is why the exam almost always wants cost of debt stated **after tax**: Kd = i × (1 − t). Keep this reason mentally separate from the risk reasons — a favourite "explain why" question.

**A caution on the tax shield — it needs profits to exist.** The interest tax shield is only worth i × t *if the firm has enough taxable profit to absorb the deduction*. A loss-making firm, or one already sheltered by heavy depreciation and carried-forward losses, gets **no** tax benefit from more interest — yet still bears the full cash burden and default risk. This is the seed of the idea that there is an *optimal*, not infinite, level of debt.

## 4. Full Technical Content — The Complete Menu of Sources

We classify sources along two axes the examiner cares about: **maturity** (long-term vs short-term) and **ownership** (owners' funds vs borrowed funds). Study the map first, then each source in detail.

*Figure 3 — the classification of sources of finance by maturity and ownership.*

```mermaid
flowchart TD
    S["Sources of finance"] --> LT["Long-term - over 5 years"]
    S --> MT["Medium-term - 1 to 5 years"]
    S --> ST["Short-term - under 1 year"]
    LT --> LO["Owners funds - equity shares - preference shares - retained earnings"]
    LT --> LB["Borrowed funds - debentures - long-term loans - venture capital"]
    MT --> MB["Loans - leasing - hire purchase - public deposits"]
    ST --> SB["Trade credit - bank overdraft - cash credit - commercial paper - factoring"]
```

### 4.1 Long-term sources — Owners' Funds

**(a) Equity Share Capital.** The permanent risk capital of a company. Equity shareholders are the *real owners*. Key features and the reasoning behind each:

- **No fixed dividend, no repayment.** Because there is no contractual outflow, equity is the *safest source from the company's viewpoint* — it never forces insolvency. This is precisely why it is the *foundation* of the capital structure.
- **Voting rights → control.** Issuing new equity to outsiders **dilutes control** of existing owners. A promoter holding 60% who issues a big new tranche may drop below 51% and lose control — a decisive reason companies sometimes avoid equity even when it's available.
- **Highest cost.** As established, residual claimants demand the highest return.
- **Dividends are not tax-deductible** — paid out of post-tax profit.
- **No charge on assets**, so it preserves borrowing capacity for the future.

*Ways to raise equity:* IPO/FPO (public issue), **Rights issue** (offered to existing shareholders pro-rata, protecting their control), **Private placement/Preferential allotment**, **Bonus issue** (capitalising reserves — raises *no* new cash, only reshuffles the balance sheet), **Sweat equity** (to employees/directors for know-how), and **ESOPs**.

*Finer distinctions the exam tests on equity:*
- **Authorised vs Issued vs Subscribed vs Called-up vs Paid-up capital.** Authorised (the ceiling in the MoA) ≥ Issued ≥ Subscribed ≥ Called-up ≥ Paid-up. A company can raise more later up to the authorised limit without altering the MoA; beyond it, the ceiling must be raised. Paid-up is the money actually received. Know the descending order.
- **Face value vs Book value vs Market value vs Intrinsic value.** Face (par) value is fixed at issue (e.g. ₹10). Book value = net worth ÷ number of shares. Market value = traded price. Intrinsic value = present value of expected future cash flows. Examiners test that dividends and bonus ratios are on *face* value, not market value.
- **Share premium.** Shares issued above par create a **securities premium**, a capital reserve with restricted uses (e.g. issuing bonus shares, writing off preliminary/issue expenses) under the Companies Act 2013 — it is *not* distributable as dividend.
- **Rights issue mechanics and the value of a right.** A rights issue protects existing holders' proportional stake and lets them buy new shares below market, so the right itself has value. Cum-rights price falls to an **ex-rights (theoretical) price** after issue; the difference is the value of one right (a numerical you may be asked — see Example 6).

**(b) Preference Share Capital.** A hybrid — legally equity, behaviourally debt-like.

- **Preferential rights:** fixed rate of **dividend** *before* equity, and priority in **repayment of capital** on winding up. Hence the name.
- **Usually no voting rights** (regain votes if dividend unpaid for 2 years) — so it raises capital *without diluting control*. A key attraction.
- **Cheaper than equity** (lower risk than equity, ranks ahead) but **costlier than debt** (ranks behind debt; dividend not tax-deductible).
- **Types you must know:** *Cumulative* (unpaid dividends accumulate as arrears — the default) vs *Non-cumulative*; *Participating* (shares surplus profit beyond fixed rate) vs *Non-participating*; *Convertible* (into equity) vs *Non-convertible*; *Redeemable* (repaid on a date — the Companies Act 2013 requires preference shares be redeemable within **20 years**, except infrastructure companies) vs Irredeemable. In India, effectively all preference shares are redeemable.
- **Why "hybrid" is more than a label.** Preference sits between debt and equity on *every* attribute simultaneously: risk (medium), cost (medium), claim priority (middle), and control impact (usually none). This is exactly why it is the tool of choice when a promoter needs a large sum but refuses to dilute votes *and* wants to keep the debt ratio (and hence bankruptcy risk) down — preference adds no interest obligation that can force insolvency, because an unpaid preference dividend merely accumulates; it does not trigger default the way unpaid interest does. That single distinction — **skipped preference dividend = arrears, skipped debenture interest = default** — is the crux of many theory marks.

**(c) Retained Earnings (Ploughing back of profits).** Profits kept in the business instead of paid as dividend. This is **internal financing** — the others are external.

- Belongs to equity shareholders, so it is a form of **owners' funds**. It carries an **opportunity cost** equal to the return shareholders forgo — so it is *not free*, a classic exam trap.
- **Advantages:** no issue costs, no dilution of control, no fixed obligation, readily available, and it cushions dividends. Enables growth without depending on volatile markets.
- **Danger — over-capitalisation / careless investment:** because the money feels "free", managers may invest it in sub-par projects. And excessive retention starves shareholders of current dividends.
- **Cost slightly below fresh equity — and why.** The cost of retained earnings is marginally *lower* than the cost of a fresh equity issue for one reason only: retained earnings incur **no flotation (issue) costs** and, in some treatments, spare shareholders **personal tax and brokerage** they would pay on a dividend then reinvest. It is *not* cheaper because it is "internal" or "free" — same shareholders, same required return, minus the issue-cost saving. Expect this precise nuance in Cost of Capital.

### 4.2 Long-term sources — Borrowed Funds

**(d) Debentures / Bonds.** A debenture is a written acknowledgement of debt — the company borrows from the public in small units.

- **Fixed interest**, paid *whether or not profits are earned*; a legal obligation. **Interest is tax-deductible** → cheapest long-term source after adjusting for tax.
- **No voting rights → no dilution of control.** Debenture-holders are creditors, not owners.
- Often **secured** by a charge (fixed or floating) on assets → lower risk to lenders → lower rate.
- **Repayable** on maturity → creates *refinancing/redemption* pressure; a Debenture Redemption Reserve may be required.
- **Types:** Secured vs Unsecured (naked); Redeemable vs Irredeemable; Convertible (**FCD** fully / **PCD** partly convertible into equity) vs Non-convertible (NCD); Registered vs Bearer; Zero-coupon (issued at discount, no periodic interest).
- **Danger:** raises **financial risk**; too much interest burden can trigger insolvency in a downturn.

*Finer debenture distinctions worth marks:*
- **Fixed charge vs Floating charge.** A fixed charge attaches to a specific identifiable asset (land, building); a floating charge hovers over a changing pool (stock, receivables) and *crystallises* on default. Fixed-charge holders rank ahead of floating-charge holders on the assets charged.
- **Convertible debentures blend two cost logics.** A convertible pays low interest *because* it dangles the upside of conversion into equity — investors accept a coupon below a plain bond's. On conversion, debt turns into equity, cutting the interest burden but diluting control later. So a convertible is "cheap debt now, potential dilution later."
- **Zero-coupon and deep-discount bonds.** No periodic interest; the entire return is the gap between the discounted issue price and the redemption value. Useful when a firm wants no cash outflow until maturity (matching a project that pays off only at the end).
- **Bond-pricing intuition (link to valuation).** A bond's price = PV of coupons + PV of redemption, discounted at the market yield. When market yields *rise above* the coupon, the bond trades at a *discount*; when they *fall below*, at a *premium*. This inverse price–yield relationship underlies why "interest-rate risk" is the price paid for the safety of fixed income.

**(e) Term Loans (from banks / financial institutions).** Negotiated long/medium-term loans, typically for buying fixed assets. Repaid in instalments (EMIs) with interest, usually secured, often with **restrictive covenants** (limits on further borrowing, dividends). Interest tax-deductible. No dilution of control but tighter lender oversight than debentures.

*What covenants actually do — and why they matter for the exam:* covenants (minimum current ratio, cap on debt-equity ratio, ceiling on dividends, no further charge on assets without consent) exist to protect the lender from the borrower quietly increasing risk after the loan is drawn — an **agency cost of debt** control device. They are why a heavily-levered firm loses *financial flexibility*: it must ask permission to invest, borrow more, or raise dividends. This lost flexibility is a real, if invisible, cost of debt.

**(f) Venture Capital.** Long-term risk capital for **new, high-risk, high-growth** ventures (typically start-ups and tech) that cannot access conventional funding because they have no track record or collateral.

- The VC provides **equity or quasi-equity** and, crucially, **management expertise, mentoring and networks**. They take a stake and expect to **exit** (via IPO or sale) in 3–7 years with a very high return to compensate for high failure rates.
- **Stages of financing:** *Seed* (idea) → *Start-up* (product development) → *Early/First stage* (commercial production) → *Expansion/Second stage* (scaling) → *Later stage/Mezzanine/Bridge* (pre-IPO). You should be able to name these in order.
- **Methods:** equity participation, conditional loan (royalty on sales), income note (interest + royalty), participating debenture.
- **Why VC demands 30–50%+ returns — portfolio logic.** A VC funds ten start-ups knowing perhaps seven fail, two break even, and one becomes a multi-bagger. The required return on *each* deal must be high enough that the single winner pays for all the losers and still beats the market. This is why the arithmetic "cost" of VC looks brutal — it prices in a portfolio of expected failures, not the success of one firm. Contrast with a banker, who lends to many and expects almost all to repay, so charges a thin margin.

**(g) Other long-term routes.** *Loan syndication*, *Asset securitisation*, *International sources* — **ADRs** (American Depository Receipts), **GDRs** (Global Depository Receipts), **ECBs** (External Commercial Borrowings), and **FDI/FII**. ADR/GDR let an Indian company raise equity abroad; ECB is foreign-currency debt.

*Sharper on the international routes (a fertile MCQ zone):*
- **ADR** trades on a *US* exchange and is USD-denominated; **GDR** trades on *non-US* (e.g. European/London/Luxembourg) exchanges. Both are negotiable receipts held by a depository bank against underlying Indian shares — the Indian company raises **equity** without listing directly abroad.
- **ECB** is *debt* (foreign-currency loans/bonds from foreign lenders), governed by RBI/FEMA norms, carrying **currency risk** — if the rupee depreciates, the rupee cost of repaying a dollar loan rises. This exchange-rate exposure is the hidden cost of "cheap" foreign borrowing.
- **FDI** implies a lasting management interest/control stake; **FII/FPI** is portfolio investment for returns without control. Don't confuse the two.
- **Securitisation** converts illiquid receivables (e.g. housing loans) into tradable securities (pass-through certificates) sold to investors — the originator gets cash today; the risk moves to investors. It is *off-balance-sheet* financing.

### 4.3 Medium-term sources

**(h) Lease Financing.** Instead of *buying* an asset, the firm (the **lessee**) *uses* it and pays rent to the owner (the **lessor**). The core idea: **profits are earned by *using* assets, not by *owning* them** — so why sink scarce long-term capital into ownership?

- **Finance (Capital) Lease:** long-term, non-cancellable; substantially transfers all risks and rewards of ownership to the lessee; lease covers most of the asset's economic life; effectively a purchase financed by the lessor. Shown as an asset + liability by the lessee.
- **Operating Lease:** short-term, cancellable; lessor bears risk of obsolescence and usually maintenance (e.g., leasing a photocopier or aircraft). Good for assets prone to obsolescence.
- **Advantages:** conserves capital (100% financing), no large upfront outlay, lease rentals are tax-deductible, flexibility, avoids obsolescence risk (operating). **Disadvantage:** lessee loses ownership/salvage value; over the life it can cost more than buying.
- **Sale and lease-back:** firm sells an owned asset to a lessor and leases it back — unlocks cash tied up in the asset while retaining use.

*Finance vs Operating lease — the tests examiners apply.* A lease is a **finance lease** if any one holds: (i) ownership transfers by end of term; (ii) a bargain purchase option exists; (iii) term covers the major part of the asset's economic life; (iv) PV of lease payments ≈ substantially all of the asset's fair value; (v) the asset is so specialised only this lessee can use it. Otherwise it is an **operating lease**. The *substance over form* principle governs: a lease can be legally rental yet economically a purchase, and accounting follows the economics.

*Who claims depreciation — the pivot for buy-vs-lease sums.* In a lease, the **lessor owns and hence claims depreciation**; the lessee deducts only the **lease rental**. When *buying*, the firm owns and claims *both* depreciation *and* interest as deductions. This is exactly why a buy-vs-lease numerical must (a) give the buyer a depreciation tax shield and (b) give the lessee only a rental tax shield — miss either and the comparison is wrong (see Example 2).

**(i) Hire Purchase.** The hirer pays in instalments and **ownership transfers only after the last instalment**. Contrast with leasing where ownership never transfers (finance lease may have a purchase option). Interest portion is a charge; the hirer eventually owns the asset and claims depreciation.

*Lease vs Hire Purchase — a five-point distinction table the examiner loves:*

| Basis | Lease | Hire Purchase |
|---|---|---|
| Ownership | Stays with lessor throughout | Passes to hirer after last instalment |
| Depreciation claimed by | Lessor | Hirer |
| Deduction to user | Full lease rental | Only interest part of instalment |
| Nature of payment | Rental for use | Instalment = principal + interest |
| Purchase intent | Use, then return | Use, then own |

**(j) Public Deposits.** Company invites deposits from the public for 6 months to 3 years at attractive interest. Simple, no security/charge, no dilution — but regulated (Companies Act limits) and can be unstable if not renewed. *Verify current ICAI material / AY for the exact ceiling percentages and tenure caps, as deposit rules under the Companies Act 2013 and its Deposit Rules are periodically amended.*

### 4.4 Short-term sources — the working-capital toolkit

Short-term finance funds **current assets** (inventory, receivables) that turn back into cash within a year. It is repaid from the operating cycle itself.

**(k) Trade Credit.** Credit extended by *suppliers* — you buy goods now, pay in 30–60 days. **Spontaneous** (grows automatically with purchases), needs no negotiation, and is *interest-free* if no cash discount is forgone — but forgoing a cash discount for early payment can make it very expensive in implicit terms.

*The hidden cost of trade credit — quantify it.* Terms like "2/10, net 45" mean *take 2% discount if you pay within 10 days, else the full amount by day 45*. Skipping the discount to pay 35 days later "buys" you 35 days of credit at a cost of 2% of the invoice. Annualised, that implicit cost is roughly:

> Cost ≈ [ Discount % ÷ (100 − Discount %) ] × [ 365 ÷ (Credit period − Discount period) ]

For 2/10 net 45: ≈ [2 ÷ 98] × [365 ÷ 35] ≈ 2.041% × 10.43 ≈ **21.3% per annum** — far dearer than a bank overdraft. Moral: "free" trade credit becomes very expensive the moment you forgo the discount, so a firm with cheaper bank finance should *take* the discount (see Example 4).

**(l) Bank Finance for working capital:**
- **Cash Credit:** borrow up to a limit against security of inventory/receivables; interest only on the amount used. The workhorse of Indian working-capital finance.
- **Overdraft:** overdraw a current account up to a limit; short, fluctuating needs.
- **Bills Discounting:** the bank pays you now (less discount) for a bill of exchange due later — converts receivables to instant cash.
- **Letter of Credit:** bank guarantees payment to your supplier — not direct finance but eases trade credit.
- **Working Capital Demand Loan.**

*Cash credit vs overdraft — the fine line.* Both are limits, but cash credit is granted against a *drawing power* computed on the *value of hypothecated stock/receivables* and is the standard route for ongoing inventory finance; an overdraft is typically against the current account for *short, fluctuating* gaps and may be clean (unsecured) or secured. Interest on both is charged only on the *utilised* amount — a key attraction versus a term loan where interest accrues on the whole disbursed sum.

**(m) Commercial Paper (CP).** An **unsecured promissory note** issued by *large, creditworthy* companies to raise short-term funds (7 days to 1 year) directly from the money market, usually *cheaper* than bank credit. Issued at a discount to face value. Only high-rated firms qualify. *Verify current ICAI material / AY for the exact minimum credit rating, minimum net worth and denomination norms, as RBI CP guidelines are revised from time to time.*

**(n) Factoring.** The firm *sells* its **receivables** to a factor at a discount for immediate cash; the factor collects from customers. *With recourse* (firm bears bad-debt risk) vs *without recourse* (factor bears it). **Forfaiting** is the equivalent for *export* receivables (medium-term, without recourse).

*Factoring — the two service bundles.* A factor provides (i) **finance** (advance against receivables, typically 75–90% upfront, balance on collection) and (ii) **collection + sales-ledger administration + credit protection** (in without-recourse). So factoring is not merely borrowing — it *outsources the receivables function*. Cost = factor's discount/commission + interest on the advance. Compare against the saving in your own collection department and bad-debt losses to judge whether it pays (see Example 5).

**Factoring vs Bills discounting vs Forfaiting — don't blur them:**

| Basis | Bills Discounting | Factoring | Forfaiting |
|---|---|---|---|
| What is sold | A single bill of exchange | Whole book of receivables | Export receivable / trade bill |
| Recourse | Usually with recourse | With or without | Always without recourse |
| Ledger admin | No | Yes (factor manages) | No |
| Typical term | Short | Short | Medium-term |
| Scope | Domestic/trade | Domestic (mainly) | International (export) |

**(o) Inter-Corporate Deposits (ICDs), and accrued expenses / provisions** (wages and taxes owed but not yet paid) — spontaneous, cost-free short-term financing.

*Why accruals are the cheapest money of all.* Wages payable and taxes payable are amounts you *owe but have not yet paid* — the employee has worked but is paid month-end; tax is earned by the state daily but paid quarterly. In the gap, that money finances your operations at **zero explicit cost and zero negotiation**. It grows automatically with the business (spontaneous). The catch: you cannot stretch it (paying wages late or taxes late invites penalties and worse) — so it is real but *not manoeuvrable*.

### 4.5 The comparison that ties it together

| Feature | Equity Shares | Preference Shares | Debentures / Debt | Retained Earnings |
|---|---|---|---|---|
| Nature of holder | Owner | Hybrid owner | Creditor | Owner (internal) |
| Return | Dividend (variable) | Fixed dividend | Fixed interest | Implicit (opportunity cost) |
| Obligation to pay | None (discretionary) | Only if profits | Compulsory (legal) | None |
| Repayment | None (permanent) | On redemption (≤20 yrs) | On maturity | Not applicable |
| Voting / Control | Yes — dilutes control | Usually no | No | No dilution |
| Risk to company | Lowest | Medium | Highest (financial risk) | Lowest |
| Cost to company | Highest | Medium | Lowest | Moderate (opp. cost) |
| Tax treatment | Not deductible | Not deductible | **Deductible** | Not deductible |
| Charge on assets | No | No | Usually yes | No |
| Effect if payment skipped | No consequence | Accumulates (if cumulative) | Default → insolvency | Not applicable |

## 4.6 Financial Markets — Where Sources Are Bought and Sold

Sources of finance are traded in **financial markets** — the meeting place of those with surplus funds (savers) and those who need funds (firms). Two big divisions, split by **maturity of the instrument**:

- **Money Market** — the market for **short-term** funds (maturity **up to 1 year**). Deals in near-cash, highly liquid, low-risk, low-return instruments. Instruments: **Treasury Bills** (T-Bills, issued by RBI/Govt), **Commercial Paper**, **Certificates of Deposit (CDs)** (issued by banks), **Call/Notice money** (inter-bank overnight), **Commercial Bills**, **Repos**. Participants: RBI, banks, large corporates, mutual funds. Purpose: manage *liquidity / working capital*, not long-term growth. Regulated primarily by the **RBI**.

- **Capital Market** — the market for **long-term** funds (maturity **over 1 year**, including permanent equity). Instruments: **shares, debentures, bonds**. Higher risk, higher return, less liquid than money-market paper. Purpose: fund *fixed assets and long-term growth*. Regulated primarily by **SEBI**.

The capital market itself splits into:
- **Primary Market (New Issue Market):** where securities are issued for the *first* time and the company *actually receives the money* — IPO, FPO, rights issue, private placement. This is where financing genuinely happens.
- **Secondary Market (Stock Exchange, e.g. NSE/BSE):** where *existing* securities are traded among investors. The **company gets no new money** here — but the secondary market provides **liquidity** and **price discovery**, which is what makes investors willing to buy in the primary market in the first place. Without a resale market, few would ever subscribe.

*Money-market instruments — one-line identities you must be able to state:*
- **Treasury Bill (T-Bill):** short-term (91/182/364-day) government borrowing, **zero-coupon** (issued at discount, redeemed at face). Risk-free benchmark; issued by RBI on behalf of the Government.
- **Commercial Paper (CP):** unsecured corporate promissory note, issued at discount — a *company* instrument.
- **Certificate of Deposit (CD):** negotiable term-deposit receipt issued by a *bank/FI*, at discount.
- **Call money (up to 1 day) / Notice money (2–14 days):** inter-bank very-short lending to manage daily reserve gaps.
- **Repo (Repurchase Agreement):** sell a security now with a promise to buy it back later at a higher price — effectively a **collateralised short-term loan**; the rate is the repo rate. The RBI's repo/reverse-repo operations are its main tool to inject/absorb liquidity.
- **Commercial Bill:** a bill of exchange arising from a genuine trade transaction, discountable with a bank.

*Distinguish the primary market's four routes (a favourite theory question):* **Public issue** (IPO/FPO — offered to the public at large), **Rights issue** (to existing shareholders pro-rata), **Private placement** (to a select group of institutional/HNI investors — faster, cheaper, less disclosure), and **Preferential allotment** (to identified persons under SEBI norms). All four bring *fresh cash* to the company; only the public and rights routes touch the general public.

*Why the secondary market is indispensable even though the firm gets nothing:* the **price discovery** it performs continuously values a firm's securities, which (i) tells the firm the terms on which it can raise *future* capital, (ii) disciplines management (a falling share price signals investor displeasure), and (iii) provides the **liquidity** without which no rational investor would lock money into the primary market. Liquidity in the resale market *lowers the required return* investors demand at issue — so the secondary market indirectly cheapens primary-market financing. That causal chain is the deep "why" behind the trap "the company gets no money in the secondary market, so it doesn't matter" — it matters enormously.

*Figure 4 — the architecture of financial markets by maturity and function.*

```mermaid
flowchart TD
    FM["Financial markets"] --> MM["Money market - short term - up to 1 year - RBI regulated"]
    FM --> CM["Capital market - long term - over 1 year - SEBI regulated"]
    MM --> MMI["T-Bills - Commercial Paper - CDs - Call money - Repos"]
    CM --> PM["Primary market - new issues - company receives money"]
    CM --> SM["Secondary market - stock exchange - liquidity and price discovery"]
    PM --> PMI["IPO - FPO - Rights - Private placement"]
```

## 4.7 The Matching Principle (Hedging Approach) — and WHY

The single most important *decision rule* connecting sources to uses is the **matching principle** (also called the **hedging approach** to financing):

> **Match the maturity of the source of finance to the life of the asset it funds. Finance long-term (fixed / permanent) assets with long-term funds, and short-term (temporary current) assets with short-term funds.**

Refined for working capital, current assets have two layers:
- **Permanent (core) current assets** — the minimum inventory and receivables always on hand — behave like fixed assets and should be financed with **long-term** funds.
- **Temporary (fluctuating) current assets** — seasonal spikes — should be financed with **short-term** funds that can be repaid when the spike subsides.

**Why?** Two failures the principle prevents:

1. **Financing long assets with short funds (aggressive, under-financing) → liquidity crisis.** If Vishnu funds its 20-year plant with a 3-year loan, the loan falls due long before the plant generates enough to repay it. The firm must **refinance repeatedly**, exposed to interest-rate spikes and credit droughts; a single refusal to roll over the loan forces a fire-sale of the plant. Cheaper in good times, lethal in bad times.

2. **Financing short assets with long funds (conservative, over-financing) → idle cost.** If Vishnu funds a two-month seasonal inventory build-up with permanent equity or a 15-year debenture, then for the other ten months of the year that expensive long-term money sits **idle**, still demanding its high return. You are paying rent on a warehouse you use two months a year. This drags down return on capital and is *over-capitalisation*.

The matching (hedging) approach threads between these: it minimises both the *risk* of a liquidity crunch and the *cost* of idle funds. It is the applied form of everything above — cost, risk, and maturity all resolved into one clean rule.

**Three financing strategies, not two — place the hedging approach on a spectrum.** The exam frequently frames working-capital financing as a *choice of strategy*:
- **Aggressive:** even part of the *permanent* current assets (and occasionally fixed assets) are funded with short-term sources. Highest profitability (short-term funds are cheaper) but highest liquidity risk.
- **Conservative:** even part of the *temporary* current assets are funded with long-term sources. Lowest risk, lowest profitability (idle long-term funds).
- **Matching / Hedging:** the balanced middle — permanent needs on long-term funds, temporary needs on short-term funds.

The examiner's punchline: **there is a risk–return trade-off in financing exactly as in investing.** Aggressive = high return, high risk; conservative = low return, low risk; hedging = the reasoned middle. A firm's choice depends on management's risk appetite and the stability of its cash flows.

*Figure 5 — the matching principle mapping asset lives to source lives.*

```mermaid
flowchart LR
    A["Fixed assets - long life"] --> B["Long-term funds - equity and long debt"]
    C["Permanent current assets - core"] --> B
    D["Temporary current assets - seasonal"] --> E["Short-term funds - overdraft and trade credit"]
    B --> F["Matched - low liquidity risk and low idle cost"]
    E --> F
```

*Figure 5A — the same idea reframed as a strategy spectrum from aggressive to conservative.*

```mermaid
flowchart TD
    ST["How much short-term finance is used"] --> AG["Aggressive - short funds also cover permanent needs - high return high risk"]
    ST --> HE["Hedging - short funds cover only temporary needs - balanced"]
    ST --> CO["Conservative - long funds also cover temporary needs - low return low risk"]
    AG --> TR["Risk and return trade-off in financing"]
    HE --> TR
    CO --> TR
```

## 5. Worked Examples

### Example 1 (Warm-up) — Why equity is *not* the cheapest source

**Problem.** Anand Ltd is choosing between raising ₹50 lakh via (i) 12% debentures or (ii) equity shares on which investors expect a 16% return. Corporate tax is 25%. Compute the **effective cost to the company** of each source and identify the cheaper one. Ignore issue expenses.

**Reasoning first.** Cost to the company is the return it must *give up* to the provider — but for debt, interest is tax-deductible, so the government effectively refunds part of it. For equity, dividends are paid from post-tax profit, so there is no tax shield.

**Step 1 — Cost of debentures (after tax).**
Pre-tax interest rate = 12%.
After-tax cost = 12% × (1 − tax rate) = 12% × (1 − 0.25) = 12% × 0.75 = **9.00%**.

Check in rupees: interest = ₹50,00,000 × 12% = ₹6,00,000. Tax saved = ₹6,00,000 × 25% = ₹1,50,000. Net cost = ₹6,00,000 − ₹1,50,000 = ₹4,50,000, i.e. ₹4,50,000 / ₹50,00,000 = **9.00%.** ✓

**Step 2 — Cost of equity.**
Equity return of 16% is paid out of post-tax profit; no tax shield. Effective cost = **16.00%**.

**Step 3 — Compare.**

| Source | Nominal rate | Tax shield? | Effective cost |
|---|---|---|---|
| 12% Debentures | 12% | Yes (25%) | 9.00% |
| Equity | 16% | No | 16.00% |

**Conclusion.** Debt costs the company **9%** vs **16%** for equity — debt is far cheaper, confirming the queue logic: the front-of-queue, tax-shielded landlord is cheaper than the back-of-queue partner. *But* this does not mean "use all debt" — see Example 3 for the risk cost of doing so.

**What if the examiner tweaks it — issue costs.** Suppose the debentures carry **2% flotation cost** on face value and are redeemable at par after 5 years. The company receives only ₹49,00,000 (net of ₹1,00,000 issue cost) but pays interest on ₹50,00,000 and repays ₹50,00,000. The *effective* cost rises above the naive 9% because the denominator (net proceeds) shrinks. The lesson: **flotation cost always raises the true cost of a source**, and it hits equity and debt alike — which is exactly why retained earnings (zero flotation) edges out fresh equity in cost.

### Example 2 (Application) — Buy vs Lease

**Problem.** Bhaskar Ltd needs a machine costing **₹10,00,000**, useful life **5 years**, no salvage value, depreciated on straight-line. Two options:

- **Buy** using a 5-year loan at **10%** interest, repaying principal in one bullet at year-5 end (interest paid annually).
- **Lease** at an annual lease rental of **₹2,60,000** payable at each year-end for 5 years.

Tax rate **25%**; after-tax cost of capital (discount rate) **8%**. Advise whether to **buy or lease** by comparing the present value of after-tax cash outflows. PV factors at 8%: Yr1 0.926, Yr2 0.857, Yr3 0.794, Yr4 0.735, Yr5 0.681 (annuity 4.993).

**Reasoning first.** Both options acquire the *same* machine, so we compare only the **financing cash outflows**, after tax, in present-value terms — the cheaper PV of outflow wins. Buying gives a **depreciation tax shield** (you own it) plus an **interest tax shield**; leasing gives a **lease-rental tax shield**.

**Step 1 — LEASE option cash flows.**
Annual lease rent = ₹2,60,000. It is tax-deductible, so after-tax outflow = ₹2,60,000 × (1 − 0.25) = ₹2,60,000 × 0.75 = **₹1,95,000 per year** for 5 years.
PV = ₹1,95,000 × 4.993 = **₹9,73,635.**

**Step 2 — BUY option cash flows.**
Depreciation = ₹10,00,000 / 5 = ₹2,00,000 per year → depreciation tax shield = ₹2,00,000 × 25% = **₹50,000 per year** (an inflow/saving).
Interest = ₹10,00,000 × 10% = ₹1,00,000 per year → after-tax interest = ₹1,00,000 × 0.75 = **₹75,000 per year** (outflow).
Principal repayment = **₹10,00,000** at end of Year 5 (outflow).

*Note on the loan:* since the loan rate (10% pre-tax = 7.5% post-tax) differs from the 8% discount rate, we discount all buy-related flows at 8% for a like-for-like comparison with the lease.

Year-by-year net outflow for BUY:

| Year | After-tax interest (out) | Dep. tax shield (in) | Principal (out) | Net outflow | PV factor @8% | PV |
|---|---|---|---|---|---|---|
| 1 | 75,000 | (50,000) | — | 25,000 | 0.926 | 23,150 |
| 2 | 75,000 | (50,000) | — | 25,000 | 0.857 | 21,425 |
| 3 | 75,000 | (50,000) | — | 25,000 | 0.794 | 19,850 |
| 4 | 75,000 | (50,000) | — | 25,000 | 0.735 | 18,375 |
| 5 | 75,000 | (50,000) | 10,00,000 | 10,25,000 | 0.681 | 6,98,025 |
| **Total PV of buying** | | | | | | **₹7,80,825** |

**Step 3 — Compare PV of outflows.**

| Option | PV of after-tax outflow |
|---|---|
| Buy (borrow) | ₹7,80,825 |
| Lease | ₹9,73,635 |

**Conclusion.** **Buying is cheaper** by ₹9,73,635 − ₹7,80,825 = **₹1,92,810** in present-value terms. Bhaskar should **buy (borrow)** the machine. *Interpretation:* the lease rental of ₹2,60,000 is high relative to owning; ownership also captures the depreciation tax shield which leasing forfeits. Had the lease rental been lower (say ₹2,00,000), the answer could flip — the technique, not a memorised verdict, is what matters.

**What if the examiner tweaks it — salvage value and the discount rate.** Two common variations:
- **Add a salvage value** (say ₹1,00,000 at year-5). Under *buy*, the owner *receives* the salvage (an inflow in the buy column, reducing its net outflow) — leasing forfeits it. This tilts the answer further toward buying. If the salvage is taxable as a short-term gain, net it for tax.
- **Discount the buy flows at the after-tax cost of debt instead of 8%.** Some ICAI solutions discount the *buy/borrow* stream at the **after-tax cost of debt** (here 7.5%) because the loan cash flows are contractually as certain as the lease's — reserving the higher WACC only for risky operating flows. Read the question: if it *gives* a single discount rate, use it for both; if it says "discount financing flows at after-tax cost of debt," switch. Stating your assumption explicitly protects your marks.

### Example 3 (Exam-hard) — Choosing a financing *mix* under a profit scenario (EPS approach)

**Problem.** Chandra Ltd needs **₹80,00,000** to fund an expansion expected to raise annual **EBIT to ₹24,00,000**. Three financing plans:

- **Plan A — All equity:** issue 8,00,000 equity shares of ₹10 each.
- **Plan B — Equity + Debt:** ₹40,00,000 equity (4,00,000 shares of ₹10) + ₹40,00,000 12% debentures.
- **Plan C — Equity + Preference + Debt:** ₹20,00,000 equity (2,00,000 shares of ₹10) + ₹20,00,000 10% preference shares + ₹40,00,000 12% debentures.

Tax rate **30%**. (i) Compute **EPS** under each plan at EBIT = ₹24,00,000 and advise which maximises shareholder wealth. (ii) Then recompute EPS if a downturn cuts **EBIT to ₹6,00,000**, and comment on the **financial risk** revealed.

**Reasoning first.** Shareholder wealth is served by the plan giving the highest **EPS** — *provided* the firm can safely bear the fixed charges. Debt and preference introduce **fixed charges** (interest, pref-dividend) that are paid before equity. When EBIT is high, these cheap fixed charges leave *more* per equity share (favourable leverage). When EBIT falls, the same fixed charges devour profit and can turn EPS negative (unfavourable leverage). We must test *both* scenarios.

**Part (i) — EPS at EBIT = ₹24,00,000.**

Formula: EPS = [(EBIT − Interest) × (1 − t) − Preference Dividend] ÷ No. of equity shares.

Fixed charges:
- Interest (Plans B, C) = ₹40,00,000 × 12% = **₹4,80,000.**
- Preference dividend (Plan C) = ₹20,00,000 × 10% = **₹2,00,000.**

| Item | Plan A | Plan B | Plan C |
|---|---|---|---|
| EBIT | 24,00,000 | 24,00,000 | 24,00,000 |
| Less: Interest | — | 4,80,000 | 4,80,000 |
| EBT | 24,00,000 | 19,20,000 | 19,20,000 |
| Less: Tax @30% | 7,20,000 | 5,76,000 | 5,76,000 |
| PAT | 16,80,000 | 13,44,000 | 13,44,000 |
| Less: Pref. dividend | — | — | 2,00,000 |
| Earnings for equity | 16,80,000 | 13,44,000 | 11,44,000 |
| No. of equity shares | 8,00,000 | 4,00,000 | 2,00,000 |
| **EPS (₹)** | **2.10** | **3.36** | **5.72** |

**Advice (i).** At EBIT ₹24,00,000, **Plan C gives the highest EPS (₹5.72)**, then Plan B (₹3.36), then Plan A (₹2.10). The fixed charges (12% debt, 10% pref) cost *less than* the ~30% pre-tax return the ₹80 lakh earns (EBIT/Capital = 24/80 = 30%), so leverage is **favourable** and magnifies EPS. On profitability alone, Plan C wins.

**Part (ii) — EPS if EBIT falls to ₹6,00,000.**

| Item | Plan A | Plan B | Plan C |
|---|---|---|---|
| EBIT | 6,00,000 | 6,00,000 | 6,00,000 |
| Less: Interest | — | 4,80,000 | 4,80,000 |
| EBT | 6,00,000 | 1,20,000 | 1,20,000 |
| Less: Tax @30% | 1,80,000 | 36,000 | 36,000 |
| PAT | 4,20,000 | 84,000 | 84,000 |
| Less: Pref. dividend | — | — | 2,00,000 |
| Earnings for equity | 4,20,000 | 84,000 | (1,16,000) |
| No. of equity shares | 8,00,000 | 4,00,000 | 2,00,000 |
| **EPS (₹)** | **0.525** | **0.21** | **(0.58)** |

**Comment (ii).** The picture *inverts*. Now EBIT/Capital = 6/80 = 7.5%, *below* the fixed-charge cost. Leverage becomes **unfavourable**: Plan A (all-equity, no fixed charges) is safest at ₹0.525; Plan B collapses to ₹0.21; **Plan C turns negative (−₹0.58)** — after paying ₹4,80,000 interest and ₹2,00,000 preference dividend, equity holders are left worse than nothing.

**Overall conclusion.** This is the financing decision in miniature. Plan C maximises return *when times are good* but carries the greatest **financial risk** — its fixed charges make EPS swing violently with EBIT. The right choice depends on how **stable and predictable** Chandra's EBIT is. A firm confident of steady ₹24 lakh EBIT leans toward Plan C; a firm in a cyclical, volatile industry should temper the debt (Plan B) or stay conservative (Plan A). **There is no free lunch: the same fixed charges that magnify gains magnify losses.** This is exactly why financing is a *decision*, not a formula — reconciling the cheapness of debt (Example 1) against its risk (here).

**What if the examiner tweaks it — find the indifference EBIT.** A very common follow-up: *at what EBIT do two plans give the same EPS?* Set the EPS expressions equal. Comparing Plan A (all equity) with Plan B (equity + 12% debt), with no preference:

> EBIT × (1 − t) ÷ 8,00,000 = (EBIT − 4,80,000) × (1 − t) ÷ 4,00,000

The (1 − t) cancels. Cross-multiplying: 4,00,000·EBIT = 8,00,000·(EBIT − 4,80,000) ⇒ EBIT = 2·(EBIT − 4,80,000) ⇒ EBIT = 2·EBIT − 9,60,000 ⇒ **EBIT = ₹9,60,000.** *Reconcile:* at EBIT ₹9,60,000, Plan A EPS = 9,60,000 × 0.70 ÷ 8,00,000 = ₹0.84; Plan B EPS = (9,60,000 − 4,80,000) × 0.70 ÷ 4,00,000 = 4,80,000 × 0.70 ÷ 4,00,000 = ₹0.84. ✓ **Above** ₹9,60,000 EBIT, the levered Plan B wins; **below** it, the unlevered Plan A wins. This *indifference (break-even) EBIT* is the exact dividing line between favourable and unfavourable leverage — memorise the technique, not the number.

### Example 4 (Application) — The real cost of forgoing a cash discount

**Problem.** Deepak Traders buys ₹40,00,000 of goods a year on terms **"2/15, net 60"**. It can instead borrow from its bank at **14% per annum** to pay suppliers within the discount period. Should Deepak take the discount (borrowing if needed) or stretch payment to day 60? Also state the annual rupee gain from the better policy.

**Reasoning first.** Skipping the discount to pay 45 days later (day 60 minus day 15) means paying an extra 2% to keep the money 45 days. If the *annualised implicit cost* of that trade credit exceeds the 14% bank rate, Deepak should borrow at 14%, pay early, and pocket the discount.

**Step 1 — Annualised cost of forgoing the discount.**

> Cost = [ 2 ÷ (100 − 2) ] × [ 365 ÷ (60 − 15) ] = [2 ÷ 98] × [365 ÷ 45] = 0.020408 × 8.111 = **0.1655 ≈ 16.55% p.a.**

**Step 2 — Compare with the bank rate.**
Implicit cost of trade credit **16.55%** > bank borrowing rate **14%**. So the "free" extra credit is actually dearer than a loan.

**Step 3 — Decision and rupee gain.**
**Take the discount** — borrow from the bank at 14% if cash is short. Approximate annual saving:
- Discount captured = 2% × ₹40,00,000 = **₹80,000** (on the discounted purchase base; using gross for simplicity).
- Extra interest to fund early payment for 45 days on ~₹39,20,000 (net of discount) ≈ ₹39,20,000 × 14% × 45/365 ≈ ₹67,660.
- **Net gain ≈ ₹80,000 − ₹67,660 ≈ ₹12,340 per year.** The discount policy wins, consistent with the rate comparison (16.55% > 14%).

**Conclusion.** Whenever the *annualised* cost of forgone discount exceeds the marginal borrowing rate, **pay early and take the discount**. This is the disciplined way to treat "free" trade credit — it is only free until you skip a discount. **Trap check:** the naive view "trade credit costs nothing" is wrong precisely by the ₹12,340 (and the 2.55% rate gap) computed here.

### Example 5 (Exam-hard) — Should the firm factor its receivables?

**Problem.** Eshwar Ltd has annual credit sales of **₹60,00,000**, an average collection period of **2 months**, and bad debts of **1.5%** of sales. It spends **₹1,00,000 a year** running its own credit/collection department. A factor offers to buy the receivables **without recourse**, advancing **80%** of the book at **12% p.a.** interest, charging a **commission of 2%** of sales, and taking over all collection and bad-debt risk (so Eshwar saves its ₹1,00,000 admin cost and the bad debts). Should Eshwar factor? Assume 360 days and that factoring cuts the collection period to nil for Eshwar (cash comes upfront).

**Reasoning first.** Compare the **cost of factoring** against the **benefits it delivers** (admin saved + bad debts saved + notional interest saved on funds released). If benefits ≥ cost, factor.

**Step 1 — Average receivables (debtors).**
Debtors = ₹60,00,000 × (2 ÷ 12) = **₹10,00,000.**

**Step 2 — Cost of factoring (annual).**
- Commission = 2% × ₹60,00,000 = **₹1,20,000.**
- Interest on advance: factor advances 80% of ₹10,00,000 = ₹8,00,000 at 12% = **₹96,000.**
- (The remaining 20% = ₹2,00,000 is the factor's reserve, released on collection; no interest earned by Eshwar on it, but no interest charged either.)
- **Total cost of factoring = ₹1,20,000 + ₹96,000 = ₹2,16,000.**

**Step 3 — Benefits of factoring (annual).**
- Admin/collection cost saved = **₹1,00,000.**
- Bad debts saved (without recourse) = 1.5% × ₹60,00,000 = **₹90,000.**
- **Total explicit benefit = ₹1,90,000.**

**Step 4 — Compare.**

| | ₹ |
|---|---|
| Total cost of factoring | 2,16,000 |
| Total benefit (admin + bad debts saved) | 1,90,000 |
| **Net cost of factoring** | **26,000** |

**Conclusion.** On these numbers factoring costs **₹26,000 more** than it saves, so on a pure cost-benefit basis Eshwar should **not** factor — *unless* the ₹8,00,000 cash released upfront can be redeployed to earn **more than ₹26,000** (i.e. a return above ₹26,000 ÷ ₹8,00,000 ≈ **3.25%**), or unless the firm values the certainty and management-time savings of outsourcing collection. **Reconcile the decision rule:** factor only if benefits + return on released funds ≥ cost. **What if tweaked:** make it *with recourse* and the ₹90,000 bad-debt saving vanishes, worsening the case; drop the commission to 1% and factoring turns net-beneficial. The examiner controls the verdict through these levers — you control the *method*.

### Example 6 (Application) — Value of a right in a rights issue

**Problem.** Farhan Ltd's shares trade at **₹150** (cum-rights). It announces a **rights issue of 1 new share for every 4 held, at ₹100 each**. Find (i) the theoretical **ex-rights price**, (ii) the **value of one right**, and (iii) show an existing shareholder is left no worse off whether she exercises or sells the right.

**Reasoning first.** A rights issue sells new shares below market, so the post-issue price settles between the old market price and the subscription price — a weighted average. The "value of a right" is what compensates a shareholder for that price dilution.

**Step 1 — Ex-rights (theoretical) price.**
Take a bundle of 4 old shares (worth 4 × ₹150 = ₹600) plus 1 new share (paid ₹100). Total value = ₹700 for 5 shares.
Ex-rights price = ₹700 ÷ 5 = **₹140.**

**Step 2 — Value of one right.**
Value of a right = Ex-rights price − Subscription price, scaled by shares needed. Simplest form:
Value per new share right = (Ex-rights price − Issue price) = ₹140 − ₹100 = **₹40** attached to acquiring 1 new share, which required **4** rights, so **value per right (per existing share) = ₹40 ÷ 4 = ₹10.**
(Equivalently: (Cum-rights price − Issue price) ÷ (N + 1) = (150 − 100) ÷ 5 = ₹10 per existing share.)

**Step 3 — Show indifference (reconcile).**
Investor holding 4 shares, cum-rights wealth = 4 × ₹150 = ₹600.
- *If she exercises:* pays ₹100 for 1 new share; now holds 5 shares at ₹140 = ₹700; net of the ₹100 paid = ₹600. ✓
- *If she sells her rights:* holds 4 shares at ex-rights ₹140 = ₹560, plus sells 4 rights × ₹10 = ₹40; total = ₹600. ✓

**Conclusion.** Both routes leave her at **₹600** — the rights issue transfers no wealth *between* existing shareholders; it merely raises fresh capital while protecting proportional ownership. **Trap:** a shareholder who *ignores* the rights (neither exercises nor sells) genuinely loses the ₹40 — the price drop from ₹150 to ₹140 is real, and only exercising or selling the right recovers it. This is why rights are called "value" that must be acted upon.

## 6. Presentation / Format for the Exam

**(a) Cost-of-source and lease/buy questions** — always present a clear PV-of-cash-outflows table with columns: *Year | Cash flow items | Net flow | PV factor | Present value*, and a final total row. State the discount rate and PV factors used. End with a one-line **decision statement** ("Since PV of buying ₹7,80,825 < PV of leasing ₹9,73,635, the firm should buy").

**(b) EPS / financing-mix questions** — use the vertical format: EBIT → less Interest → EBT → less Tax → PAT → less Preference Dividend → Earnings for equity → ÷ shares → **EPS**. Show each plan in a parallel column. Always finish with an **advisory comment** linking EPS to financial risk. If asked, add the **indifference-EBIT** working (set the two EPS expressions equal) and interpret which plan wins above/below it.

**(c) Theory / "distinguish between" questions** (very common on this chapter) — answer in a **two-column table** (e.g., *Basis | Equity | Preference*): bases such as return, voting rights, repayment, risk, cost, tax. Examiners award marks per point of distinction, so a table of 5–6 bases scores fully. High-frequency pairs to have ready: *Equity vs Preference*, *Shares vs Debentures*, *Lease vs Hire Purchase*, *Finance vs Operating Lease*, *Factoring vs Bills Discounting*, *Money Market vs Capital Market*, *Primary vs Secondary Market*.

**(d) Classification questions** — group under headings *Long-term / Medium-term / Short-term* or *Owners' funds / Borrowed funds*, and note the regulator (SEBI/RBI) where markets are asked. If a "spontaneous vs negotiated" or "internal vs external" split is asked, use those lenses instead — read the demand words carefully.

**(e) Trade-credit / working-capital cost questions** — state the annualised-cost formula, plug in, compare with the borrowing rate, then give a one-line policy verdict. Show the rupee gain if asked.

**(f) Rights-issue questions** — compute ex-rights price via the bundle method, then value of a right, then demonstrate shareholder indifference (exercise vs sell) to earn the interpretation marks.

## 7. Connections — How This Chapter Wires Into the Rest of FM

- **→ Cost of Capital.** The "cost" attribute of each source becomes the input to computing the **Weighted Average Cost of Capital (WACC)**. Example 1's after-tax cost of debt is literally the Kd used there; the flotation-cost nuance and the retained-earnings-vs-fresh-equity gap reappear as Ke and Kr.
- **→ Capital Structure.** The *mix* decision in Example 3 is formalised into theories (Net Income, Net Operating Income, Traditional, MM) that ask the optimal debt-equity ratio to minimise WACC and maximise value. The frictions listed in Section 1 (tax shield, distress cost) are precisely what make MM's "irrelevance" break down in the real world.
- **→ Leverage.** The magnification effect seen in Example 3 is quantified as **financial leverage** (Degree of Financial Leverage), and combined with operating leverage into combined leverage. The indifference-EBIT (Example 3 tweak) is the financial break-even.
- **→ Capital Budgeting (the invest decision).** The *maturity* of sources here must match the *life* of projects evaluated there — the matching principle is the bridge between financing and investing. The lease-vs-buy PV technique (Example 2) is capital budgeting applied to a financing choice.
- **→ Working Capital Management.** Section 4.7's permanent vs temporary current assets, the aggressive/hedging/conservative spectrum, and the short-term toolkit (trade credit, cash credit, factoring, CP) are the raw material of working-capital financing strategy. Examples 4 and 5 are working-capital numericals in embryo.
- **→ Dividend Decision.** Retained earnings (4.1c) sits on the seam between the finance and distribute decisions — every rupee retained is a rupee not distributed. The signalling idea (Section 1) links to why dividend cuts are read as bad news.

## 8. Traps & Examiner Tricks

1. **"Equity is free/cheapest."** The number-one error. Equity is the **most expensive** source (highest risk → highest required return), just with no *contractual* cash outflow. Never call it free.
2. **Retained earnings have "no cost."** Wrong — they carry an **opportunity cost** equal to shareholders' required return. Ploughing profits into a sub-return project destroys value. They are only *marginally cheaper than fresh equity*, purely by saving flotation cost — not "free" and not "internal so costless."
3. **Forgetting the tax shield on debt.** Cost of debt in exams is nearly always **after-tax** = rate × (1 − t). Preference dividend gets **no** shield. Mixing these up is a classic mark-loser. Remember the shield is worthless if the firm has no taxable profit.
4. **Preference dividend deducted before tax.** No — preference dividend is an *appropriation of PAT*, deducted **after** tax, whereas interest is deducted **before** tax. Watch the EPS ladder.
5. **Primary vs secondary market cash.** The **company receives money only in the primary market.** Secondary-market trading gives the company nothing (just liquidity to investors). But do not conclude the secondary market "doesn't matter" — its liquidity and price discovery cheapen future primary-market fund-raising.
6. **Money vs capital market cut-off.** The dividing line is **1-year maturity**. Commercial Paper and Certificates of Deposit are **money-market** (short-term) instruments, *not* capital-market — even though issued by companies/banks. T-Bills are money-market and issued by Government/RBI, not SEBI-regulated.
7. **Leasing vs hire purchase ownership.** In **hire purchase, ownership transfers** after the last instalment; in **leasing, ownership stays with the lessor**. Depreciation is claimed by the *owner* — so the buyer/hirer claims it, the lessee does not.
8. **Matching principle direction.** Long assets ↔ long funds. Funding long assets with short funds = **liquidity risk** (aggressive); funding short assets with long funds = **idle-cost/over-capitalisation** (conservative). Don't invert them.
9. **"More debt always raises EPS."** Only when EBIT return exceeds the fixed-charge rate (favourable leverage). Below the **indifference EBIT**, debt *slashes* EPS and can turn it negative — see Example 3(ii) and its tweak.
10. **Bonus issue "raises finance."** A bonus issue capitalises reserves and brings in **no new cash** — it only rearranges the balance sheet. A rights issue *does* bring cash.
11. **Redeemable preference limit.** Under the Companies Act 2013, preference shares must be redeemable within **20 years** (infrastructure companies excepted) — irredeemable preference shares can no longer be issued in India.
12. **"Trade credit is free."** Only until you forgo a cash discount. The annualised cost of skipping "2/15 net 60" is ~16.5% — often dearer than a bank loan (Example 4). Always compare the implicit cost with the borrowing rate.
13. **ADR/GDR vs ECB.** ADR/GDR raise **equity** abroad (no repayment, no fixed charge); **ECB is debt** carrying interest *and* **currency risk**. Do not label ECB as equity or forget its exchange-rate exposure.
14. **Skipped preference dividend ≠ default.** An unpaid *cumulative* preference dividend becomes **arrears**; unpaid *debenture interest* is a **default** that can force insolvency. This distinction is why preference is "safer" fixed financing than debt.
15. **With-recourse vs without-recourse factoring.** Bad-debt risk stays with the *firm* under **recourse**, moves to the *factor* under **without recourse**. The bad-debt saving in a factoring decision (Example 5) exists *only* in the without-recourse case.
16. **Ignoring the right in a rights issue.** Neither exercising nor selling the right *forfeits* its value — the ex-rights price drop is a real loss to a passive shareholder (Example 6). The issue is wealth-neutral only if you act.

## 9. First-Principles Recap

Strip everything away and you are left with one chain of logic:

Every rupee of capital comes from a financier who bears some **risk**, and by the iron law *higher risk demands higher return*, that risk sets the **cost**. Position in the **queue of claims** determines the risk: debt-holders stand first (low risk, low cost, plus a tax shield), preference in the middle, equity last (high risk, high cost, no shield). The three distinct reasons debt is cheaper — priority of claim, security, and the pure tax subsidy — should be kept mentally separate, because only the first two are "risk" and only the tax shield needs profits to be worth anything. The very feature that makes debt cheap — its fixed, first-in-queue cheque — is what makes it dangerous: fixed charges must be paid in bad years too, creating **financial risk**, and there is an **indifference EBIT** below which leverage stops helping and starts hurting. So financing is a *balancing act* between the cheapness of debt and the safety of equity, and the right balance depends on how stable the firm's earnings are. Layered on top is **maturity**: money must be repaid on a schedule, so we **match** the life of each source to the life of the asset it funds — long with long, short with short — choosing consciously along the aggressive–hedging–conservative spectrum to trade liquidity risk against idle cost. These instruments are bought and sold in **markets** split by the same maturity idea: the **money market** for short-term liquidity (RBI), the **capital market** for long-term growth (SEBI), with the primary market delivering cash to firms and the secondary market delivering the liquidity and price discovery that make the primary market possible. And underneath it all sits the quiet truth that financing merely *slices* the pie — it changes firm value only through real frictions (taxes, distress costs, flotation costs, information gaps). Master those four attributes — **cost, risk, control, maturity** — plus the frictions that give them teeth, and you can reason your way to the right source for any situation, without memorising a single list.

## 10. Quick-Revision Sheet

**Core formulas**

| Purpose | Formula |
|---|---|
| After-tax cost of debt | Kd = Interest rate × (1 − Tax rate) |
| EPS (financing mix) | EPS = [(EBIT − Interest) × (1 − t) − Pref. Dividend] ÷ No. of equity shares |
| Favourable leverage condition | Return on capital (EBIT ÷ Total capital) > Fixed-charge rate |
| Indifference (break-even) EBIT | Set EPS of Plan 1 = EPS of Plan 2 and solve for EBIT |
| Lease vs Buy decision rule | Choose option with **lower PV of after-tax cash outflows** |
| Buy outflows (per year) | After-tax interest + Principal − Depreciation tax shield (− Salvage) |
| Depreciation tax shield | Depreciation × Tax rate |
| After-tax lease rental | Lease rent × (1 − Tax rate) |
| Cost of forgoing cash discount | [d ÷ (100 − d)] × [365 ÷ (Credit period − Discount period)] |
| Ex-rights price | (N × Cum-rights price + Issue price) ÷ (N + 1) |
| Value of a right (per share) | (Cum-rights price − Issue price) ÷ (N + 1) |

**Key facts table**

| Item | Remember this |
|---|---|
| Cheapest source | Debt (after-tax, has tax shield) |
| Most expensive source | Equity (highest risk, no shield) |
| Only source with tax shield | Debt / borrowings (interest deductible) |
| Source that dilutes control | Equity shares |
| Sources that preserve control | Debt, preference shares, retained earnings |
| Permanent capital (no repayment) | Equity + retained earnings |
| Pref. shares redeemable within | 20 years (Companies Act 2013; infra excepted) |
| Skipped payment consequence | Interest → default; Cumulative pref → arrears; Equity → nothing |
| Money market cut-off | Maturity ≤ 1 year; regulator RBI |
| Capital market | Maturity > 1 year; regulator SEBI |
| Company gets new cash in | Primary market only |
| Money-market instruments | T-Bills, Commercial Paper, CDs, Call money, Repos |
| Capital-market instruments | Shares, debentures, bonds |
| T-Bill / CP / CD nature | Issued at discount; T-Bill by Govt, CP by companies, CD by banks |
| Ownership transfers (HP vs Lease) | HP: yes, after last instalment; Lease: no (lessor owns) |
| Depreciation claimed by | The owner — buyer/hirer, or lessor (not lessee) |
| VC financing stages | Seed → Start-up → Early → Expansion → Later/Bridge |
| ADR vs GDR vs ECB | ADR (US equity), GDR (non-US equity), ECB (foreign-currency debt, currency risk) |
| Matching principle | Long assets ↔ long funds; short assets ↔ short funds |
| Short funds → long assets | Liquidity risk (aggressive) |
| Long funds → short assets | Idle cost / over-capitalisation (conservative) |
| Trade credit "2/15 net 60" cost | ~16.5% p.a. — dearer than most bank loans |
| Factoring bad-debt saving | Only under **without-recourse** factoring |

**One-line decision heuristics**
- Need cheapness and can bear fixed payments with stable EBIT → tilt to **debt**.
- Volatile earnings, want safety, or protecting borrowing capacity → tilt to **equity**.
- Want capital *without* diluting control and no tax shield needed → **preference shares** or **debt**.
- Funding a long-life asset → **long-term** source; funding seasonal current assets → **short-term** source.
- Asset prone to obsolescence, want to conserve capital → **lease** (operating).
- New, high-risk, high-growth venture with no track record → **venture capital**.
- Implicit cost of forgone discount > borrowing rate → **take the discount, borrow if needed**.
- Factoring benefits (admin + bad debts saved + return on freed cash) ≥ cost → **factor**.
- Above the indifference EBIT → **levered plan**; below it → **all-equity plan**.
