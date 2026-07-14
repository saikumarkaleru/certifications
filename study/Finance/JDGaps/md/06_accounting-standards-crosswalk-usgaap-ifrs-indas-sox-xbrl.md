# Standards & Controls JDs Assume: US GAAP vs IFRS vs Ind AS, SOX/J-SOX, XBRL

## The gap

Your bundles teach **Ind AS, Schedule III and month-end**. But GCC and MNC-controllership JDs assume you can *also* speak **US GAAP and IFRS**, operate inside a **SOX / J-SOX** control framework, and understand **XBRL/MCA** filing. Indian entities of US or Japanese parents keep two sets of books and run a formal controls regime — none of which your Ind-AS-first material covers. That crosswalk and that controls vocabulary are the gap.

## Why companies ask for it

> **Real posting (HP, R2R, Bangalore):** "Highly skilled in US GAAP & IFRS … Ensure compliance with internal & SOX controls."

> **Real posting (Dentsu, Financial Control, Bangalore):** "IFRS + US GAAP; **J-SOX controls effectiveness attestation**; external audit support."

Every GCC controllership, R2R, financial-reporting and internal-audit role wants this because the India entity reports up to a parent on **US GAAP or IFRS** while filing locally on **Ind AS**, and a listed US parent is legally bound by **SOX** (Japanese parent → **J-SOX**). Roles: **R2R/RTR, financial reporting & consolidation, controllership, internal controls/SOX testing, statutory audit support** at HP, Dentsu, Accenture, Genpact, Deloitte/EY/PwC/KPMG managed services.

## What "proficient" looks like

You can name the **standard number and the practical difference** across the three frameworks for the big-ticket areas; explain **design vs operating effectiveness** and walk a control from an **RCM** to a **test of one**; classify a control gap as a **deficiency / significant deficiency / material weakness**; and describe how Indian companies **XBRL-tag and file** with MCA.

## How to actually learn/do it

### US GAAP vs IFRS vs Ind AS — the crosswalk

Ind AS is *converged with* IFRS (so they're close, with carve-outs); **US GAAP is the different one**. Learn the deltas on the areas auditors and interviewers hammer:

| Area | US GAAP | IFRS | Ind AS |
|---|---|---|---|
| **Revenue** | ASC 606 | IFRS 15 | Ind AS 115 — all 3 use the **5-step model**; substantially aligned |
| **Leases** | ASC 842 — lessee still splits **finance vs operating** (dual P&L model) | IFRS 16 — **single model**, almost all leases on balance sheet | Ind AS 116 — single model, follows IFRS 16 |
| **Financial instruments** | ASC 326 **CECL** (lifetime expected loss, day 1) | IFRS 9 — **3-stage ECL** model | Ind AS 109 — 3-stage ECL, follows IFRS 9 |
| **Inventory** | **LIFO permitted**; write-downs generally not reversed | LIFO **banned**; reversals allowed | LIFO banned; reversals allowed |
| **Consolidation** | VIE (variable interest) model | IFRS 10 single **control** model | Ind AS 110 control model |
| **Dev. costs / R&D** | Mostly **expensed** | **Capitalise** if IAS 38 criteria met | Capitalise (Ind AS 38) |
| **Component depreciation** | Not required | Required | Required |
| **Extraordinary items** | Prohibited | Prohibited | Prohibited |

The two you must be able to speak to cold: **leases** (US GAAP keeps the operating/finance split; IFRS/Ind AS collapse it into one on-balance-sheet model) and **credit losses** (US **CECL** = lifetime loss from day one; IFRS/Ind AS **ECL** = staged, moves to lifetime only on significant deterioration).

**Free study:** the **IFRS Foundation** publishes standards summaries free; **MCA** hosts Ind AS free; **FASB** ASC Basic View is free; the Big-4 "**US GAAP vs IFRS**" comparison PDFs (EY, PwC, KPMG, Deloitte) are the single best crosswalk resource — download one.

### Internal controls: SOX / J-SOX / IFC

- **SOX** (US Sarbanes-Oxley) **§302** = executives certify the financials; **§404** = management *and* the external auditor assess **internal control over financial reporting (ICFR)**.
- **J-SOX** = Japan's equivalent (Financial Instruments & Exchange Act) — same idea, management **attestation** of controls effectiveness (Dentsu's exact phrase).
- **IFC** = India's Internal Financial Controls over Financial Reporting under **Companies Act 2013 §143(3)(i)** — the auditor reports on IFC.

All rest on the **COSO 2013** framework (5 components, 17 principles).

**The workflow you must know:**
1. **RCM (Risk & Control Matrix)** — the master sheet listing each **risk → control → assertion → owner → frequency → test**.
2. **Design effectiveness** — is the control *capable* of preventing/detecting the risk? (walkthrough of one transaction).
3. **Operating effectiveness** — did it *actually operate* all year? (test a **sample** — e.g. 25 items for a daily control).
4. **Deficiency ladder:** a **control deficiency** < **significant deficiency** < **material weakness** (reasonable possibility of a material misstatement).
5. **Control types:** preventive vs detective, **manual vs automated**, and **ITGCs** (IT General Controls — access, change management, ops) that everything automated depends on.

**Worked example:** Risk = "unauthorised journal posted." Control = "all manual JEs >₹10 lakh require reviewer approval in SAP before posting." *Design test:* trace one JE — was approval captured? *Operating test:* pull 25 JEs from the year, confirm each has documented approver ≠ preparer. Two fail → evaluate: isolated slip (deficiency) or pervasive (significant/material).

### XBRL & MCA filings

**XBRL** (eXtensible Business Reporting Language) tags each financial-statement number to a standard **taxonomy** element so regulators read it by machine. In India, specified companies file financials in XBRL with **MCA** via forms **AOC-4 XBRL** (and cost audit in **CRA-4**); you validate in the **MCA XBRL validation tool**, generate the instance document, do a **pre-scrutiny**, and upload. SEBI listed entities also file XBRL on the exchanges. You don't hand-code XBRL — you map the trial balance to taxonomy tags in the tool.

## How it shows up in interviews

**Q: "Biggest practical difference in lease accounting across US GAAP and IFRS?"**
A: "IFRS 16 and Ind AS 116 use a single lessee model — nearly every lease goes on the balance sheet as a right-of-use asset and lease liability, with depreciation plus interest. US GAAP's ASC 842 still splits operating vs finance leases: both go on the balance sheet, but operating leases keep a straight-line single lease expense in P&L rather than the front-loaded depreciation-plus-interest pattern. So EBITDA and expense geography differ."

**Q: "Walk me through testing a SOX control."**
A: "I start from the RCM to get the control objective, assertion and frequency. First I test **design** with a walkthrough of one transaction to confirm the control can catch the risk. Then **operating effectiveness**: I pick a sample sized to frequency — say 25 for a daily control — and inspect evidence that it operated each time, like an approver different from the preparer. Exceptions get evaluated up the ladder from deficiency to significant deficiency to material weakness based on likelihood and magnitude."

**Q: "What's the difference between SOX, J-SOX and IFC?"**
A: "Same concept — management/auditor assurance over financial-reporting controls, all built on COSO. SOX is US law for SEC registrants (§302 certification, §404 ICFR); J-SOX is Japan's version requiring management attestation of control effectiveness; IFC is India's, under Companies Act §143(3)(i), where the statutory auditor opines on internal financial controls."

## ATS keywords to add

US GAAP, IFRS, Ind AS, ASC 606, IFRS 15, ASC 842, IFRS 16, IFRS 9, ECL, CECL, GAAP-to-IFRS reconciliation, SOX, Sarbanes-Oxley, J-SOX, §404, ICFR, IFC, Internal Financial Controls, COSO, Risk and Control Matrix (RCM), design and operating effectiveness, control testing, walkthrough, deficiency, significant deficiency, material weakness, ITGC, XBRL, AOC-4, MCA filing, statutory audit support, R2R
