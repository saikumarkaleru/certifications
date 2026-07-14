# How GCC/Shared-Services Finance Actually Runs: R2R/P2P/O2C, WD-Close, SLAs, RPA, SOPs

## The gap

Most India finance jobs in 2026 sit inside a **GCC** (Global Capability Centre) or **BPO/GBS** (Global Business Services) shared-services centre — Genpact, Accenture, HP, Cromwell, Dentsu, and hundreds of captive centres in Bangalore, Hyderabad, Gurugram, Pune. These run finance as a **factory** organised into *process towers* with *service-level agreements*, *working-day close calendars*, *ticketing queues*, and *desktop procedures*. Your bundles teach the accounting (Ind AS, month-end, reconciliations) but not the **operating model** the accounting runs inside. Interviewers screen hard on this vocabulary because it tells them whether you'll survive the floor from day one.

## Why companies ask for it

> Real posting (HP, Bangalore R2R): "R2R, AR & P2P ... Ensure compliance with internal & SOX controls ... Automate data workflows."

> Real posting (Genpact, FP&A/R2R): "Record-to-Report" delivery inside a shared-services engagement, with a company-wide push on "AI Gigafactory / agentic AI."

Every captive and BPO finance role — R2R analyst, P2P/AP specialist, O2C/collections analyst, general-ledger accountant, close lead, process SME, transition manager — is defined by which **tower** it belongs to and which **SLAs** it owns. Get the model and you speak their language in the first five minutes.

## What "proficient" looks like

The bar is that you can, unprompted, do the following:

- Name the three core towers and what each **owns end-to-end**.
- Explain a **WD1–WD5+ close calendar** and where a given task lands.
- Distinguish an **SLA** (a promise, e.g. 98% invoices posted in 2 days) from a **KPI** (a measured metric, e.g. days-to-close) and quote a couple of each.
- Describe how **SOP / DTP** documents are structured and why they matter for audit and transition.
- Explain a **transition/migration** (as-is → to-be, knowledge transfer, parallel run, go-live, hypercare).
- Say where **RPA** (UiPath, Automation Anywhere, Blue Prism) and **ticketing** (ServiceNow) fit.

## How to actually learn/do it

**The three process towers.** Memorise these cold.

| Tower | Full name | Owns end-to-end | Core sub-processes |
|---|---|---|---|
| **R2R** | Record-to-Report | The general ledger and the financial statements | Journals, accruals/prepayments, intercompany, fixed assets, bank & balance-sheet **reconciliations**, month-end close, MIS/reporting, SOX |
| **P2P** | Procure-to-Pay (a.k.a. Purchase-to-Pay, AP) | Buying and paying suppliers | Requisition → PO → goods receipt → invoice → **3-way match** → payment run → vendor master, aging |
| **O2C** | Order-to-Cash (a.k.a. Quote-to-Cash, AR) | Selling and collecting cash | Order → credit check → billing/invoice → **cash application** → collections/dunning → dispute/deduction → DSO |

Two supporting towers you should also name: **FP&A** (budget/forecast/variance) and **Treasury** (cash, banking, FX). "Hire-to-Retire" (H2R, payroll) sometimes sits in finance too.

**The working-day close calendar.** The close is run against *working days*, not calendar dates, so it survives weekends/holidays. WD0 is the last day of the month. A stylised R2R calendar:

| Day | Activity |
|---|---|
| WD1 | Sub-ledgers cut off; AP/AR post final invoices; FX rates loaded |
| WD2 | Accruals & prepayments; intercompany matching; fixed-asset depreciation run |
| WD3 | **Balance-sheet reconciliations**; flux/variance analysis |
| WD4 | Review, sign-offs, **commentary** for the BS/close call |
| WD5 | Ledger close, consolidation, MIS pack issued |

Learn to answer "what happens on WD2?" instantly — it is a classic screen.

**SLAs vs KPIs.** Practise a few numbers you can defend: invoice posting SLA 95–98% within 48 hrs; PO-backed invoice touchless rate; close in WD5; unapplied-cash %; DSO/DPO; recon completeness and **aged open items > 90 days**; SLA **green/amber/red** RAG status reported weekly.

**SOP / DTP.** An SOP (Standard Operating Procedure) is the high-level "what/why"; a **DTP (Desktop Procedure)** is the click-by-click "how" — screenshots of the exact SAP/Oracle screens, T-codes, who approves, what the control is. When work moves to a GCC it *cannot* migrate without DTPs. Free practice: write a one-page DTP for a task you know (e.g. "post a manual accrual journal") with purpose, frequency, inputs, step-by-step screens, control point, and RACI.

**Transitions/migrations.** The lifecycle: *as-is study → to-be design → Knowledge Transfer (KT) → parallel run/shadow → go-live → hypercare (30–90 days of extra support) → steady state (BAU)*. Deliverables: process maps, DTPs, a **RACI**, a cutover plan. This is the single most valued phrase-set for anyone above analyst.

**RPA in finance.** You don't need to code a bot, but know the shape. A **UiPath** bot logs into SAP, downloads a report, opens Excel, reformats, and emails it — replacing a "swivel-chair" manual task. Vendors: **UiPath, Automation Anywhere, Blue Prism**. Good candidates: bank-statement download, recon prep, invoice data entry, report distribution. Terms: *attended vs unattended bot, orchestrator, bot runner, human-in-the-loop*. Free practice: the **UiPath Community Edition** and free Academy give a real certificate; build one bot that reads an Excel and writes a summary.

**Ticketing & controls.** Work arrives as **tickets/cases** in **ServiceNow** (or Jira). Learn queue, priority (P1–P4), SLA clock, and *first-time-right*. Controls: **SOX / J-SOX** control testing, **maker-checker (four-eyes)**, segregation of duties, and the **RCM** (Risk & Control Matrix).

## How it shows up in interviews

**Q: "Walk me through the P2P process end-to-end and where the key control is."**
"Requisition raised and approved → PO issued → goods/services received and a GRN posted → supplier invoice arrives → the system performs a **3-way match** of PO, GRN and invoice within tolerance → if matched it's parked for payment, if not it's routed to a resolution queue → payment run releases it, and I update the vendor aging. The critical control is the 3-way match plus **maker-checker** on the payment run, which is a SOX control because it prevents duplicate or fraudulent payments."

**Q: "It's WD3 and a balance-sheet recon won't tie — a ₹4 lakh unreconciled item. What do you do?"**
"I quantify and age it, check whether it's timing (in-transit, unposted accrual) or a genuine difference, trace it to source, and post a correcting or accrual journal with backup. If I can't clear it by cut-off I log it on the recon with an owner and a resolution date, flag it in the WD4 commentary, and escalate anything above the materiality threshold so the BS call isn't surprised."

**Q: "What makes a transition successful?"**
"Complete DTPs and process maps before KT, a proper parallel run so we catch gaps while the retained team still owns it, a clear RACI, defined SLAs from go-live, and a real hypercare window. Success is measured by SLA attainment and error rate reaching steady state without the client re-absorbing work."

## ATS keywords to add

Record-to-Report (R2R), Procure-to-Pay (P2P), Order-to-Cash (O2C), General Ledger, month-end close, working-day close calendar (WD1–WD5), balance-sheet reconciliations, three-way match, cash application, DSO/DPO, SLA/KPI management, RAG reporting, SOP/DTP documentation, transitions and migrations, knowledge transfer (KT), hypercare, RACI, Global Capability Centre (GCC), shared services / GBS, RPA (UiPath, Automation Anywhere, Blue Prism), ServiceNow, SOX/J-SOX controls, maker-checker, Risk & Control Matrix (RCM), process improvement, first-time-right.
