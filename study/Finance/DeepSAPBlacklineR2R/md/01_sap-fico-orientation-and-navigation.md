# SAP FICO Orientation & Navigation

## What you'll be able to do

After this chapter you can sit at a fresh SAP session, log into a client, drive the **SAP GUI** and **Fiori launchpad** by memory, jump to any transaction using the **command field**, and read the org structure of a company the way a GCC controller reads it: Company Code → Chart of Accounts → Controlling Area → Cost/Profit Centers. You'll know which numbers live in **FI** and which live in **CO**, and you'll be able to open a GL master (FS00), a vendor/customer master, and a cost-centre master (KS01/KS03) and explain every tab. You'll also be able to tell an interviewer the real differences between **S/4HANA** and **ECC** without bluffing.

## The drill — step by step

**1. Log in.** SAP Logon pad → double-click the system (e.g. `PRD`, `QAS`, `DEV`) → enter **Client** (3 digits, e.g. 800), **User**, **Password**, **Language** EN. A client is a self-contained data world; a GCC often has one client for the whole group and many company codes inside it.

**2. Learn the command field.** Top-left white box. Type transaction codes here.
- `FS00` → go to that T-code in the current window.
- `/n` + code (`/nFS00`) → close current, open new in same window.
- `/o` + code (`/oFB03`) → open in a **new** session (window) — keep a display session open while you post.
- `/nend` → log off; `/nex` → log off without the "do you want to end" popup.
- `/i` → close current session.
Type `SESSION_MANAGER` or just navigate the **SAP Easy Access** menu tree (Accounting → Financial Accounting → General Ledger…) if you don't know the code.

**3. Read the org structure — the spine of FICO.**

| Object | What it is | Config T-code to view |
|---|---|---|
| **Company Code** (4-char, e.g. `1000`) | The legal entity that produces a balance sheet & P&L. Statutory books live here. | `OX02` |
| **Chart of Accounts** (e.g. `INT`/`CAIN`) | The master list of GL account numbers, shared across company codes | `OB13` |
| **Controlling Area** (e.g. `1000`) | The CO umbrella; can span several company codes if they share a COA & fiscal year | `OKKP` |
| **Cost Center** (e.g. `IT-DEL-100`) | Where cost is *collected* — a department (IT, Finance, Facilities) | `KS03` |
| **Profit Center** (e.g. `PC-RETAIL`) | Where profit is *measured* — a business line / responsibility area | `KE53` |
| **Segment / Business Area** | Reporting slices under IFRS 8 / new GL | doc splitting config |

Worked example: GCC entity **1000 – Acme India Pvt Ltd**, chart of accounts **CAIN**, controlling area **1000**. IT department cost centre **IT-DEL-100** posts salary and AMC costs; profit centre **PC-SHARED** absorbs them; at month end those costs get *assessed* to the business profit centres.

**4. FI vs CO — the mental split.**
- **FI (Financial Accounting)** = external books. Every posting hits a **GL account**, produces the statutory Balance Sheet & P&L, feeds tax and audit. Sub-ledgers: **AP** (vendors), **AR** (customers), **Asset Accounting (AA)**, **Bank**.
- **CO (Controlling)** = internal management view. The *same* expense also lands on a **cost element / cost centre / internal order** so managers see cost by department and product. In S/4HANA FI and CO are merged into one line-item table (`ACDOCA` — the Universal Journal), so a P&L GL expense account **is** the cost element (cost element is now just a GL account of type "Primary Costs/Revenue").

**5. Master data — open one of each.**

*GL master — `FS00`:* enter GL account `400000` + company code `1000`.
- **Type/Description** tab: Account group (e.g. P&L Expense), P&L vs Balance-sheet flag, short/long text.
- **Control Data** tab: currency, tax category, **Open Item Management** (tick for clearing accounts like GR/IR, bank clearing), **Line Item Display**, Sort key.
- **Create/Bank/Interest** tab: field status group (which fields are required at posting), post automatically only.

*Vendor master — `BP` in S/4HANA* (the single **Business Partner** transaction; ECC used `XK01/FK01`). Roles: FI Vendor (`FLVN00/01`), Purchasing. Key fields: reconciliation account (e.g. `160000` Trade Payables), payment terms, withholding tax (TDS) type/code, bank details.

*Customer master — `BP`* (ECC: `XD01/FD01`). Recon account `140000`, payment terms, credit control.

*Cost centre master — create `KS01`, change `KS02`, display `KS03`:* enter controlling area `1000`, cost centre `IT-DEL-100`, valid-from/to dates, category (e.g. `1` Administration), person responsible, hierarchy area, profit centre link.

**6. Fiori.** Modern S/4HANA front-end is the **Fiori launchpad** (browser). Tiles group apps by role (GL Accountant, AP Accountant). Key apps mirror GUI T-codes: **Manage Journal Entries** (≈ FB50/FB03), **Post General Journal Entries**, **Display Line Items – General Ledger** (≈ FBL3N as the app **Display Line Item, GL**), **Trial Balance**. You can still open the classic T-code inside Fiori via the "SAP GUI for HTML" tile. Search apps in the top search bar.

## The output

A one-page orientation map you can reproduce blind:

```
CLIENT 800
  └─ Company Code 1000 (Acme India) ──> statutory B/S + P&L  [FI]
        Chart of Accounts: CAIN
        Controlling Area 1000  ───────> management view       [CO]
             Cost Centers: IT-DEL-100, FIN-DEL-200 ...
             Profit Centers: PC-SHARED, PC-RETAIL ...
Master data:
  GL      FS00   (e.g. 400000 Salaries, 160000 Trade Payables)
  Vendor  BP     (recon a/c 160000, TDS code, payment terms)
  Customer BP    (recon a/c 140000)
  Cost ctr KS01/03  (IT-DEL-100 -> PC-SHARED)
Navigation: command field  /n /o ; Easy Access menu ; Fiori tiles
```

## Checks & gotchas

- **Client vs Company Code confusion** is the classic rookie error — client is the login environment, company code is the legal entity. You post to a company code; you log into a client.
- A GL account must exist **at both** chart-of-accounts level and company-code level (`FS00` shows both) before you can post — "account not created in company code 1000" is a real error.
- **Open Item Management** must be ON for clearing accounts (GR/IR, bank clearing) or you can never clear them; it must be OFF for reconciliation accounts (you never post directly there).
- In S/4HANA you **cannot** use `XK01/FD01` to create vendors/customers — it redirects to `BP`. Saying "I'll create the vendor in XK01" in an S/4 shop flags you as ECC-only.
- Cost element vs GL account: in ECC they were separate objects (`KA01` to create a cost element); in S/4HANA cost elements are folded into GL master data (account type merged). Know this — it's the #1 "do you actually know S/4" question.

## Interview drill

**Q1. Difference between S/4HANA and ECC in Finance terms?**
"S/4HANA runs on the HANA in-memory column DB and merges FI and CO into one line-item table, the **Universal Journal `ACDOCA`** — one source of truth, no reconciliation between FI and CO, real-time reporting, no aggregate/index tables like BSEG/GLT0 for reporting. Business Partner replaces separate vendor/customer masters, cost elements become GL accounts, and the New Asset Accounting and material ledger are mandatory. ECC is the older ERP on a classic RDBMS with separate FI and CO totals tables that had to be reconciled."

**Q2. Company Code vs Controlling Area vs Profit Centre?**
"Company code is the legal entity that files statutory accounts. Controlling area is the CO reporting umbrella and can group several company codes if they share the chart of accounts and fiscal year. Profit centre is a responsibility/business-line slice for internal profitability, cutting across cost centres."

**Q3. Where does a salary expense land in both FI and CO?**
"FI: Dr Salaries GL (P&L expense), Cr Salary Payable / Bank. Simultaneously in CO the debit carries a cost object — the department cost centre — because that P&L account is a primary cost element. Month-end assessments then push the cost centre balance to profit centres."

## Practise free

- **openSAP** (open.sap.com) — free MOOCs: "SAP S/4HANA Finance" and "Financial Accounting in SAP S/4HANA" give guided navigation and screenshots.
- **SAP Learning Hub / Learning Journeys** at learning.sap.com — free tutorials; some hands-on need a paid subscription, but the reading and videos are open.
- A live sandbox is the only true rehearsal: SAP offers **S/4HANA Fully-Activated Appliance** trials on SAP CAL (24-hour AWS/Azure instance, you pay only cloud compute ~₹100–300/session) and a **BTP free tier**. Third-party training servers (Michael Management, ERPPrep) rent GUI access hourly.
- Free-forever: install **SAP GUI** (free download with an SAP account) and practise *navigation muscle memory* — command field syntax, menu paths, session handling — even against a demo/idle connection, so on day one you move fast.
- Draw the org-structure map above from memory each morning until it's automatic; that single diagram answers 40% of FICO interview questions.
