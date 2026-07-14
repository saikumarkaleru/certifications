# Treasury & Cash Tech: TMS (Kyriba/SAP TRM), FX Hedging, Liquidity, SWIFT/Settlements

## The gap

Your bundles decode *what a treasury role is*; they don't teach the **plumbing** treasury runs on. Corporate and bank treasury JDs in 2026 want the **systems** (a Treasury Management System — Kyriba, SAP TRM, FIS), the **FX-hedging mechanics** (forwards, swaps, and enough **hedge accounting** to survive an audit), **liquidity/cash positioning**, and the **bank connectivity** layer (SWIFT, MT/MX messages, settlements and confirmations). None of that is in DCF/modelling or the treasury career decode — it's operational treasury tech, and it's a gap.

## Why companies ask for it

> Real posting (Dentsu, Bangalore Financial Control): "... treasury, Insurance, **Hedging FX exposure** ..."

> Real posting (Intel, Treasury): "settlements, **TMS/SAP HANA**, KYC/AML, money markets."

Roles: corporate treasury analyst/manager, GCC treasury-ops, bank middle/back office, treasury tech/implementation (Luxoft-style), and FP&A roles that own FX. JPMorgan/Citi/Intel-type treasury desks and every GCC treasury tower expect this.

## What "proficient" looks like

You can produce a **daily cash position**, decide a short-term investment or borrowing, explain why a company hedges a specific FX exposure and how a **forward** neutralises it, describe what a **TMS** automates versus spreadsheets, and trace a payment from instruction to settlement via **SWIFT**. You know the vocabulary of **hedge accounting** (cash-flow vs fair-value hedge, hedge effectiveness, OCI) without pretending to be an IFRS-9 specialist.

## How to actually learn/do it

**The daily cash position.** The core treasury deliverable. Pull opening bank balances (via bank portal or SWIFT statement), layer expected inflows (AR collections) and outflows (payroll, AP runs, tax, debt service), and compute the **closing position per currency per bank**. Surplus → invest (money-market fund, fixed deposit, commercial paper); deficit → draw on a revolving credit facility or intercompany loan. Free practice: build a 5-bank, 3-currency cash-position sheet in Excel with an opening balance, dated flows, and a target minimum buffer.

**Liquidity structures & the in-house bank.** Learn **cash pooling**: *physical/zero-balancing* (funds physically swept to a header account nightly) vs *notional pooling* (balances offset for interest without moving cash). An **in-house bank (IHB)** makes one treasury entity act as banker to all subsidiaries — running **intercompany loans**, netting, and a **payment factory** ("**POBO/COBO**" — payments/collections on behalf of). These are the exact phrases treasury-transformation JDs use.

**Treasury Management Systems.** A TMS is the system of record for cash, debt, investments, and hedges. Know the leaders and what they do:

| TMS | Notes |
|---|---|
| **Kyriba** | Cloud market leader — cash management, payments hub, bank connectivity, risk |
| **SAP TRM / S/4HANA Treasury** | SAP shops; deep GL integration; "TRM-HANA" in the Intel JD |
| **FIS Quantum / Integrity** | Large corporates and banks |
| **ION / Reval, GTreasury** | Also common |

What a TMS actually does that a spreadsheet can't: auto-imports bank statements, forecasts cash, books and revalues deals, generates **hedge-accounting** entries, connects to banks for payments, and gives an audit trail. Free/low-cost practice: watch vendor product demos and read Kyriba/SAP TRM datasheets so you can *speak the modules* (Cash Management, Payments, FX/Risk, In-House Banking).

**FX hedging mechanics.** The building blocks:

- **Forward contract** — lock a rate today for a future date. If you'll receive USD 1m in 90 days and fear the rupee strengthening, you *sell USD forward*; the forward rate reflects the interest-rate differential (**forward points**), not a forecast.
- **FX swap** — spot leg + offsetting forward leg; used to roll positions and manage funding across currencies.
- **Option** — right not obligation; pay a premium for downside protection with upside retained.
- **Natural hedge / netting** — offset a USD payable against a USD receivable before hedging the residual.

Tiny worked example: exporter expects **USD 1,000,000 in 90 days**, spot 83.00, 90-day forward 83.60. Selling forward locks ₹8.36 crore regardless of where spot lands. If spot falls to 82.00 at maturity, the hedge saved ₹1.6m versus being unhedged; if spot rises to 84.50, you "lost" upside — but treasury's job is *certainty*, not speculation.

**Hedge accounting basics** (enough to not fail an audit). Under **IFRS 9 / Ind AS 109**: a **cash-flow hedge** (hedging a forecast transaction) parks the effective portion of the derivative's gain/loss in **OCI** and recycles it to P&L when the hedged item hits; a **fair-value hedge** runs both through P&L. You must document **hedge designation** and test **effectiveness**. You don't need to build the model — you need to say those words correctly.

**Money markets.** Know the short-end instruments treasury touches: **T-bills, commercial paper (CP), certificates of deposit (CD), repos, money-market funds**, and India's overnight benchmarks — **MIBOR** and the tri-party repo (**TREPS**). Globally, **SOFR** replaced LIBOR.

**Bank connectivity & settlements.** Payments and statements move over **SWIFT**. Legacy **MT** messages are migrating to **ISO 20022 MX** (the 2025 CBPR+ cutover): **MT103** (single customer payment) → **pacs.008**; **MT202** (bank-to-bank) → **pacs.009**; **MT940/MT942** (end-of-day/intraday statements) feed the TMS. India's rails: **RTGS/NEFT** and **UPI**. **Settlement** = the actual movement of funds on value date; a **confirmation** (via SWIFT or platforms like MarkitWire/DTCC) is the two counterparties agreeing trade terms — the middle/back-office matching step. **Nostro/vostro** accounts and **reconciliation** of them is core back-office work. **Bank Account Management (BAM)** — opening/closing accounts, **KYC** refresh, and maintaining signatories — is increasingly its own JD line.

## How it shows up in interviews

**Q: "An exporter will receive USD 1m in three months and is worried about the rupee. How do you hedge?"**
"Sell USD 1m forward for 90 days, which locks the rupee value at the forward rate — spot adjusted for the interest-rate differential. That removes uncertainty; we're not taking a view on direction. I'd first net any USD payables in that window and only hedge the residual exposure, per the hedging policy."

**Q: "What does a TMS give you that Excel doesn't?"**
"Automated bank-statement import via SWIFT, a real-time multi-bank multi-currency cash position, deal capture with revaluation, straight-through payments, auto-generated hedge-accounting entries, and a full audit trail with segregation of duties. Excel breaks on control, scale, and connectivity — exactly what auditors and SOX care about."

**Q: "Cash-flow hedge vs fair-value hedge?"**
"A cash-flow hedge protects a future forecast cash flow — the effective portion sits in OCI and recycles to P&L when the hedged item is recognised. A fair-value hedge protects the value of an existing asset/liability and both sides go through P&L. Either way I document the hedge relationship and test effectiveness under IFRS 9 / Ind AS 109."

## Certification

The gold standard is the **CTP (Certified Treasury Professional)** from the AFP — the treasury equivalent of the CFA for corporate treasury, and it's named on senior treasury JDs. **ACT (Association of Corporate Treasurers)** qualifications are the UK/global route. For the tech side, Kyriba and SAP offer product certifications valued by treasury-transformation/implementation employers.

## ATS keywords to add

Treasury Management System (TMS), Kyriba, SAP TRM / S/4HANA Treasury, FIS, cash positioning, liquidity management, cash pooling (physical/notional), in-house bank, payment factory (POBO/COBO), intercompany funding, FX hedging, forwards/swaps/options, natural hedge/netting, hedge accounting (IFRS 9 / Ind AS 109), cash-flow hedge, hedge effectiveness, money markets, commercial paper, repo/TREPS, MIBOR/SOFR, SWIFT, ISO 20022, MT103/MT940/pacs.008, RTGS/NEFT, settlements, confirmations, nostro/vostro reconciliation, Bank Account Management (BAM), KYC, CTP.
