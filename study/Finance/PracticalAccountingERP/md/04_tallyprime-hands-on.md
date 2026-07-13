# TallyPrime Hands-On

## What it is & where it's used

TallyPrime is the accounting and compliance backbone of Indian SMEs. Roughly 2 million-plus businesses run their books on Tally, which means when a hiring manager at a mid-size firm, a CA practice, or a trading/manufacturing company reads "Tally" on your resume, they mean: *can you actually pass entries, generate GST returns, and pull a Trial Balance without hand-holding?*

Roles that require it, day one:

- **Accounts Executive / Accounts Assistant** — voucher entry, bank reconciliation, ledger scrutiny.
- **Accountant / Sr. Accountant** — month-end close, GST/TDS working, MIS reports.
- **Audit article / audit assistant** — you *receive* client Tally data and vouch it.
- **Tax / GST executive** — GSTR-1 and GSTR-3B reconciliation straight out of Tally.
- **Finance analyst at an SME** — Tally is the source system before data hits Excel.

Globally, the equivalents are QuickBooks (US/UK SMEs), Xero (ANZ/UK), Zoho Books, and SAP B1 for larger shops. The *muscle* you build in Tally — double-entry discipline, master setup, tax mapping, reconciliation — ports directly to all of them.

## The gap: why companies want this (and college didn't teach it)

An MBA or B.Com teaches you *what* a journal entry is. It does not teach you that in Tally you press **F9** for a Purchase, that a "ledger" must sit under the correct "group" or your Balance Sheet mis-classifies, or that a wrong GST rate at ledger level silently corrupts your GSTR-1.

The specific gaps employers pay to close:

| College teaches | The job needs |
|---|---|
| Debit the receiver, credit the giver | Which *voucher type* (F5/F6/F7/F8/F9) records it, and the exact click-path |
| "GST is 18%" | Setting CGST/SGST/IGST ledgers, HSN codes, and tax-rate at stock/ledger level so returns auto-compute |
| Bank reconciliation concept | Matching Tally to a bank statement, setting the *bank date*, clearing 40 uncleared entries |
| Trial Balance definition | Drilling from Balance Sheet → group → ledger → voucher to find a ₹500 mismatch |

Companies want someone who can be handed a laptop with TallyPrime open and be productive in an hour, not someone who needs a week of "where's the sales entry?"

## What "proficient" looks like

A job-ready person can, unaided:

1. Create a company with correct financial year, GSTIN, and features enabled.
2. Build the group/ledger structure and stock items with tax rates.
3. Pass all five core vouchers (Sales, Purchase, Payment, Receipt, Journal) with GST auto-calculating.
4. Reconcile a bank ledger against a statement and explain every uncleared item.
5. Generate and *interpret* Balance Sheet, P&L, Trial Balance, Day Book, GSTR-1, GSTR-3B, and the Ledger.
6. Fix a mismatched Trial Balance by drill-down.

Speed benchmark: a proficient user passes a standard sales invoice in under 30 seconds and closes a month's bank rec in under 20 minutes.

## Hands-on: how to actually do it

> Navigation note: `Gateway of Tally` is your home. `Alt+G` (Go To) is the universal search — type any report/master name. `Ctrl+A` saves any screen. `Esc` backs out.

### 1. Company setup

```
Open TallyPrime → Alt+K (Company) → Create Company
  Company Name : Sharma Traders
  Financial year beginning : 1-Apr-2025
  Books beginning from      : 1-Apr-2025
  Set/Alter GST details     : Yes  → State: Telangana, GSTIN: 36ABCPS1234F1Z5, Reg type: Regular
  Base currency symbol      : ₹
Ctrl+A to save
```

Enable features once: **F11 (Features)** → set *Maintain Accounts = Yes*, *Enable Goods and Services Tax (GST) = Yes*, *Maintain Inventory = Yes*.

### 2. Masters — groups and ledgers

Every ledger MUST sit under a group; the group decides where it lands in the financials.

```
Gateway of Tally → Create (or Alt+G → "Create Ledger")
```

Core ledgers to create:

| Ledger | Under (Group) | Notes |
|---|---|---|
| Sales – GST 18% | Sales Accounts | Set GST rate 18%, HSN |
| Purchase – GST 18% | Purchase Accounts | Set GST rate 18% |
| CGST | Duties & Taxes | Type: GST, Tax type: Central |
| SGST | Duties & Taxes | Type: GST, Tax type: State |
| IGST | Duties & Taxes | Type: GST, Tax type: Integrated |
| HDFC Bank | Bank Accounts | Enter A/c no. + IFSC |
| Cash | Cash-in-Hand | Auto-exists |
| ABC Enterprises (customer) | Sundry Debtors | Set GSTIN + state |
| XYZ Suppliers (vendor) | Sundry Creditors | Set GSTIN + state |
| Rent | Indirect Expenses | — |

### 3. GST setup

```
F11 → GST = Yes → set company GSTIN & state.
At ledger level (Sales/Purchase): Set/alter GST details = Yes → Taxability: Taxable, Integrated Tax 18% → splits into CGST 9% + SGST 9% automatically for intra-state.
Stock item level: same GST-details screen, plus HSN/SAC code.
```

**Rule Tally applies automatically:** buyer state = seller state → **CGST + SGST**; different states → **IGST**. Set the state correctly on party ledgers or Tally picks the wrong tax.

### 4. Voucher entry — the five you use daily

| Voucher | Key | Records |
|---|---|---|
| Payment | F5 | Money going out (pay vendor, expenses) |
| Receipt | F6 | Money coming in (customer pays) |
| Contra | F4 | Bank↔Cash transfers |
| Purchase | F9 | Buying goods/services |
| Sales | F8 | Selling goods/services |
| Journal | F7 | Adjustments, provisions, depreciation |

**Sales invoice (F8)** — sell 10 units @ ₹1,000, intra-state 18% GST:

```
Gateway of Tally → Vouchers → F8 (Sales)
  Party A/c name : ABC Enterprises
  Sales ledger   : Sales – GST 18%
  Item : Product-A   Qty 10   Rate 1000   → Amount 10,000
  CGST  → 900   (auto)
  SGST  → 900   (auto)
  Total : 11,800
Ctrl+A to save
```

The equivalent journal Tally posts behind the screen:

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| ABC Enterprises (Debtor) | 11,800 | |
| Sales – GST 18% | | 10,000 |
| Output CGST | | 900 |
| Output SGST | | 900 |

**Receipt (F6)** — customer pays ₹11,800 into HDFC:

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| HDFC Bank | 11,800 | |
| ABC Enterprises | | 11,800 |

**Payment (F5)** — pay rent ₹20,000 from bank:

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| Rent | 20,000 | |
| HDFC Bank | | 20,000 |

**Journal (F7)** — provide depreciation ₹5,000:

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| Depreciation | 5,000 | |
| Accumulated Depreciation | | 5,000 |

### 5. Bank reconciliation

```
Gateway of Tally → Alt+G → "Bank Reconciliation" → select HDFC Bank
  (or: Banking → Bank Reconciliation)
For each entry, in the "Bank Date" column enter the date it actually cleared per the bank statement.
Entries with a bank date = reconciled. Blank bank date = still uncleared.
Bottom of screen shows: Balance as per Company books vs Balance as per Bank → difference must equal the sum of uncleared items.
Ctrl+A to save.
```

### 6. Key reports and their click-paths

| Report | Click-path |
|---|---|
| Balance Sheet | Gateway → Balance Sheet (or `Alt+G` → "Balance Sheet") |
| Profit & Loss | Gateway → Profit & Loss A/c |
| Trial Balance | Gateway → Display More Reports → Trial Balance |
| Day Book (all vouchers of a day) | Gateway → Day Book (`Alt+G` → "Day Book") |
| Ledger (a party's full statement) | Display More Reports → Account Books → Ledger |
| GSTR-1 (outward) | Gateway → Display More Reports → GST Reports → GSTR-1 |
| GSTR-3B (summary) | GST Reports → GSTR-3B |
| Stock Summary | Gateway → Stock Summary |
| Outstanding receivables | Display More Reports → Statements of Accounts → Outstanding → Receivables |

Universal tricks: **F2** changes the report date/period, **Alt+F2** sets a date range, **Ctrl+F12** filters, and **Alt+E** exports to Excel/PDF. On any figure, press **Enter to drill down** all the way to the voucher.

## Worked example / mini-project

Reproduce a mini month for **Sharma Traders**, April 2025. Create the company and ledgers above, then enter:

1. **02-Apr — Purchase (F9):** 50 units Product-A @ ₹700 from XYZ Suppliers, GST 18%. Value ₹35,000 + ₹6,300 CGST/SGST split (₹3,150 each) = ₹41,300.
2. **05-Apr — Payment (F5):** Pay XYZ ₹41,300 from HDFC Bank.
3. **10-Apr — Sales (F8):** 10 units @ ₹1,000 to ABC Enterprises, GST 18% → ₹11,800.
4. **15-Apr — Sales (F8):** 20 units @ ₹1,000 to ABC → ₹23,600.
5. **20-Apr — Receipt (F6):** ABC pays ₹35,400 into HDFC.
6. **30-Apr — Payment (F5):** Rent ₹20,000 from HDFC.
7. **30-Apr — Journal (F7):** Depreciation ₹5,000.

Now verify:

- **Trial Balance** (Gateway → Display More Reports → Trial Balance): total Dr = total Cr. If not, drill in.
- **Output GST payable** = ₹6,120 (on ₹34,000 sales); **Input GST** = ₹6,300 (on purchase). Net ITC carried forward ₹180. Check via **GSTR-3B**.
- **HDFC Bank ledger** movement: −41,300 −20,000 +35,400 = closing outflow ₹25,900 from opening. Reconcile assuming the ₹20,000 rent cheque hasn't cleared — set bank dates on the other two, leave rent's blank, and confirm the reconciliation difference = ₹20,000.
- **Stock Summary:** 50 in − 30 out = **20 units** Product-A on hand @ ₹700 = ₹14,000 closing stock.
- **P&L:** Gross Profit = Sales ₹34,000 − COGS (30 × ₹700 = ₹21,000) = ₹13,000; less Rent ₹20,000 and Depreciation ₹5,000 → net loss for the mini-month.

If every number ties, you've done a real close.

## How it's tested

**Interview questions:**

- Which voucher for a credit sale vs a cash sale? (F8; cash = F8 with Cash as party.)
- Difference between a group and a ledger?
- How does Tally decide CGST+SGST vs IGST?
- Where do you set the GST rate — company, ledger, or stock item? (Any/all; most specific wins.)
- My Trial Balance doesn't match — how do you find the error? (Drill Balance Sheet → group → ledger → voucher.)
- What's the entry for depreciation? For a bad debt write-off?

**Practical test (the real screen):** Companies give a laptop with TallyPrime and say:

> "Here are 8 vouchers and a bank statement. Enter them, reconcile the HDFC bank account, and show me the GSTR-1 and Balance Sheet."

Or hand you a company where the Trial Balance is off by ₹X and ask you to find it. They watch whether you *use shortcuts* (F8/F9, Enter-to-drill, Alt+E) or hunt through menus — that tells them your real hours on the tool.

## Common mistakes & how pros avoid them

| Mistake | Consequence | Pro habit |
|---|---|---|
| Ledger under wrong group (e.g. Rent under Sundry Creditors) | Mis-stated Balance Sheet | Verify group at creation; check Trial Balance grouping |
| Wrong/blank state on party ledger | GST computes IGST vs CGST/SGST wrong | Always fill GSTIN + state on parties |
| Using Journal (F7) for everything | Loses inventory + GST auto-calc | Use F8/F9 for trade, F7 only for adjustments |
| Forgetting HSN/SAC | GSTR-1 rejects/errors on portal | Set HSN at stock/ledger level upfront |
| Not setting bank date in rec | Reconciliation never balances | Enter bank date only for cleared items |
| Editing a saved company's financial year mid-way | Data corruption | Set FY correctly at creation |
| Not backing up | Total data loss | Alt+K → Backup weekly; keep company data folder copied |

## Learn-it roadmap & resources

**Time to proficiency:** 3–4 weeks of daily practice (1–2 hrs) to be job-ready for an Accounts Executive role; 2 months to be fully independent on GST returns and close.

| Week | Focus |
|---|---|
| 1 | Install, company setup, groups/ledgers, F5/F6/F8/F9 |
| 2 | GST setup, stock items, inventory vouchers, HSN |
| 3 | Bank rec, all reports, drill-down, exports |
| 4 | Full mini-close + GSTR-1/3B reconciliation |

**Resources:**

- **TallyPrime Educational mode** — free download from tallysolutions.com; runs full software (only restricts some dates) — practice unlimited.
- **Tally official YouTube channel & Help (F1 → Help)** — free, authoritative click-paths.
- **Certification:** *TallyEducation "TallyPrime with GST"* / *Tally ACE & PRO* certificates — inexpensive, recognized by Indian SMEs and add a resume line.
- Practice with any B.Com "Tally practical" workbook — do the entries, don't just read them.

## Quick-reference

**Voucher shortcuts (from Voucher screen):**

| Key | Voucher |
|---|---|
| F4 | Contra |
| F5 | Payment |
| F6 | Receipt |
| F7 | Journal |
| F8 | Sales |
| F9 | Purchase |

**Navigation & actions:**

| Key | Action |
|---|---|
| Alt+G | Go To (universal search) |
| Alt+K | Company menu |
| F11 | Features |
| Ctrl+A | Save/accept |
| Enter | Drill down |
| F2 / Alt+F2 | Change date / period |
| Alt+E | Export (Excel/PDF) |
| Esc | Go back |

**GST logic:** same state → CGST + SGST (½ each); different state → IGST (full rate). Common rates: 5%, 12%, 18%, 28%.

**Report paths:** Gateway of Tally → Balance Sheet / Profit & Loss / Day Book / Stock Summary directly; Trial Balance, Ledger, GST Reports, Outstanding via **Display More Reports**.

**Golden rule:** every ledger under the right group → correct financials; correct state on parties → correct GST; bank date only on cleared items → clean reconciliation.
