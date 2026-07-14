# Enterprise ERP Depth: SAP (beyond overview), Oracle, Workday, NetSuite, D365

## The gap

Your bundles give you hands-on TallyPrime and an *overview* of SAP FICO — enough to define what a GL is, not enough to survive a screening call that asks "which T-code do you post a vendor invoice in?". Every mid-2026 MNC/GCC finance JD assumes daily life *inside* an enterprise ERP, and Tally is not one. The gap is transactional fluency in SAP FICO plus literacy in the other four systems you will be asked about — Oracle, Workday, NetSuite, Dynamics 365 — because your existing material stops at the overview.

## Why companies ask for it

> Real posting (HP, R2R Bangalore): "Hands on experience in SAP... R2R, AR & P2P; Automate data workflows." Real posting (Accenture FP&A): "SAP, Oracle, Hyperion, Anaplan." Real posting (Luxoft): "SAP Finance, Workday Financials, Oracle Financial Services."

Who needs it: any Record-to-Report, AP/AR, General Accounting, financial-control or FP&A seat in a GCC or MNC (HP, Dentsu, Genpact, Accenture, Intel). The ERP *is* the job — you post, extract, reconcile and report inside it eight hours a day. SME and startup roles lean NetSuite or D365; large listed and captive-shared-services lean SAP; Oracle Fusion and Workday show up in specific captives.

## What "proficient" looks like

The bar for an entry-to-mid R2R/GL accountant is not configuration — that's a consultant's job. It is confident *end-user* operation: you know the module map (FI vs CO), you can name and use the day-to-day T-codes without a cheat sheet, you understand the document flow (a posting creates a document number, hits the GL, updates sub-ledgers), and you can pull and interrogate a line-item report. You can also say, accurately, which SAP version you worked on and the difference from the current one. For the other ERPs the bar is lower: know what each is, who uses it, and the equivalent concept, so you're not blank when a recruiter mentions it.

## How to actually learn/do it

**SAP FICO — the module map.** FI (Financial Accounting: GL, AP, AR, Asset Accounting, Bank) produces the external statements; CO (Controlling: cost centres, internal orders, profit centres, product costing) is the internal/management view. R2R lives mostly in FI-GL; P2P touches FI-AP; O2C touches FI-AR.

**The T-codes to actually memorise** (a T-code is typed into the command box top-left):

| T-code | Does | Area |
|---|---|---|
| `FB50` | Post a GL document (enter view) | FI-GL |
| `F-02` | Post a GL document (general, with posting keys) | FI-GL |
| `FB60` | Post a vendor (AP) invoice | FI-AP |
| `FB70` | Post a customer (AR) invoice | FI-AR |
| `F-53` / `F110` | Manual payment / automatic payment run | FI-AP |
| `FBL1N` / `FBL5N` / `FBL3N` | Vendor / customer / GL line-item display | Reporting |
| `FS10N` | GL account balance display | Reporting |
| `FAGLB03` | GL balance (new GL) | Reporting |
| `AS01` / `AFAB` | Create asset / run depreciation | FI-AA |
| `F.05` / `FAGL_FC_VAL` | Foreign-currency revaluation | Month-end |

**Tiny worked example — post and verify a rent accrual.** In `FB50`, enter company code, document date, then two lines: debit *Rent Expense* ₹1,00,000 (posting key 40), credit *Accrued Liabilities* ₹1,00,000 (posting key 50); the debits-equal-credits indicator must go green; simulate, then post — SAP returns "Document 1000000123 posted". Verify it in `FBL3N` by opening the Accrued Liabilities GL and filtering on your document number. That five-minute loop — post, get a doc number, trace it in a line-item report — is exactly what "hands on SAP" means on a JD.

**S/4HANA vs ECC.** ECC (ECC 6.0) is the legacy on-premise version many captives still run; S/4HANA is the current (2026) in-memory successor. Say the difference credibly: S/4HANA merges FI and CO into the **Universal Journal (table ACDOCA)** so there's a single source of truth and no reconciliation between FI and CO; the **Business Partner** replaces separate customer/vendor masters; the UI is **Fiori** tiles rather than the old SAP GUI; and reporting is real-time on line items. If you trained on ECC, say ECC — don't claim S/4 you haven't seen.

**The other four, in one line each.** *Oracle Fusion Cloud ERP* (and legacy *E-Business Suite/EBS*) — large enterprises; the finance module is "Oracle Financials", navigation is web-based, the equivalent of a GL inquiry is the Account Inspector/Financial Reporting. *Workday Financials* — HR-first companies extending into finance; everything is a "business process" with worklets, no T-codes. *NetSuite* (Oracle) — the default cloud ERP for mid-market/SME and startups; role-based dashboards, saved searches instead of T-codes. *Microsoft Dynamics 365 Finance* — Microsoft-shop mid-market; tightly integrated with Excel and Power Platform.

**How to get hands-on for free / cheap.**
- **SAP** — no fully-free live system, but: (1) SAP Learning (learning.sap.com) has free courses and **openSAP**; (2) a personal **S/4HANA Fully-Activated Appliance** trial runs on SAP Cloud Appliance Library (you pay only cloud compute, a few dollars/day, stoppable); (3) YouTube walkthroughs of `FB50`/`FBL3N` let you rehearse the exact screens; (4) SAP Learning Hub (paid) if an employer sponsors it.
- **Oracle** — Oracle offers free Cloud ERP trial/guided tours via Oracle University; **Oracle Cloud Free Tier** for the tech side.
- **NetSuite** — request a product tour/demo; SuiteLife learning content is free to browse.
- **Dynamics 365** — a **free 30-day trial** of D365 Finance is genuinely self-serve at trials.dynamics.com; spin one up and post a journal.
- **Workday** — no public trial; learn the vocabulary from Workday's docs and demo videos.

## How it shows up in interviews

**Q: "Walk me through how you'd post a vendor invoice in SAP and then check it hit the ledger."**
A: "I'd use `FB60` — enter the vendor, invoice date, amount, tax code and the expense GL and cost object. On posting SAP generates a document number. To verify, I'd open `FBL1N` for that vendor to see the open item, and `FBL3N` or `FS10N` on the expense GL to confirm the debit. At month-end that open item would clear against the payment run via `F110`."

**Q: "Have you worked on S/4HANA or ECC — what's the difference?"**
A: "I trained on [be honest]. The key change in S/4HANA is the Universal Journal, table ACDOCA — FI and CO postings share one line-item table, so there's no FI-CO reconciliation and reporting is real-time. Master data moves to the Business Partner model and the front end is Fiori instead of the classic GUI."

**Q: "We run NetSuite, you've used SAP — is that a problem?"**
A: "The concepts transfer directly — chart of accounts, subsidiaries, sub-ledgers, period close. NetSuite replaces T-codes with role dashboards and saved searches; I'd be productive on the transaction set within days and I've already run a trial to see the posting flow."

## ATS keywords to add

SAP FICO, SAP S/4HANA, SAP ECC, FI-GL, FI-AP, FI-AR, Asset Accounting, Universal Journal (ACDOCA), FB50, FB60, FBL3N, FS10N, F110, Record-to-Report (R2R), P2P, O2C, Oracle Fusion Cloud ERP, Oracle EBS, Workday Financials, NetSuite, Microsoft Dynamics 365 Finance, ERP end-user, GL posting, period-end close.
