# Day One: The Company, Its Books, and Setting Up TallyPrime

## The situation

It's 6 April 2026, 9:40 a.m. You've just joined **Nirvana Traders & Services Pvt Ltd (NTSPL)** as Accounts Executive. The outgoing accountant left last week. On your desk: a folder marked "STATUTORY", last year's **audited Balance Sheet (31-Mar-2026)**, a login sheet for the GST and Income-tax portals, and a sticky note from the Finance Manager:

> "Set up FY2026-27 in TallyPrime today. GST + TDS + Payroll all switched on. Carry the opening balances from the audited BS. I need to pass the first purchase voucher tomorrow morning — so the masters must be ready."

This is the foundation. Every voucher, every return, every reconciliation for the next twelve months rests on getting the company master, the feature flags, and the chart of accounts right today. Get a GSTIN digit or a tax-ledger's rounding method wrong now and it silently corrupts GSTR-1 in May.

## What you're given

**Statutory identity (verify against the incorporation kit):**

| Field | Value |
|---|---|
| Legal name | Nirvana Traders & Services Pvt Ltd |
| Type | Private limited, incorporated 2019 |
| Registered office | Hyderabad, Telangana (state code **36**) |
| CIN | U51909TG2019PTC012345 |
| PAN | AABCN1234A |
| TAN | HYDN01234A |
| GSTIN | 36AABCN1234A1Z5 |
| GST registration | Regular, **monthly** filer |
| Bank | HDFC Current A/c xxxx4567 |
| Books | Accrual / mercantile, TallyPrime |
| Financial year | 01-Apr-2026 to 31-Mar-2027 (AY 2027-28) |

**Business lines:** (a) trading of industrial electrical components — HSN **8536**, GST **18%**; (b) services — installation & AMC — SAC **9987**, GST **18%**.

**Opening balances — extract from the audited Balance Sheet as at 31-Mar-2026** (these become 01-Apr-2026 opening balances):

| Ledger | Group | Dr (Rs) | Cr (Rs) |
|---|---|---:|---:|
| Equity Share Capital | Capital Account | | 50,00,000 |
| Reserves & Surplus | Reserves & Surplus | | 2,20,00,000 |
| HDFC Current A/c xxxx4567 | Bank Accounts | 18,00,000 | |
| Sundry Debtors (control) | Sundry Debtors | 96,00,000 | |
| Sundry Creditors (control) | Sundry Creditors | | 62,00,000 |
| Closing Stock (opening now) | Stock-in-Hand | 40,00,000 | |
| Fixed Assets (net block) | Fixed Assets | 1,60,00,000 | |
| GST Input Credit c/f (electronic credit ledger) | Duties & Taxes | 8,00,000 | |
| TDS receivable (26AS) | Loans & Advances (Asset) | 4,00,000 | |
| Provision for Tax / other net | Provisions | | 12,00,000 |

Dr total and Cr total each tie to **Rs 3,44,00,000** — a good sign the trial balance is square before you begin.

## Do it — step by step

### Step 1 — Create the company (Gateway of Tally > Alt+K: Company > Create)

Fill the Company Creation screen:

- **Name:** Nirvana Traders & Services Pvt Ltd
- **Mailing name / Address:** as above, Hyderabad, **State: Telangana**, **Country: India**, PIN.
- **Financial year begins from:** 01-Apr-2026
- **Books beginning from:** 01-Apr-2026
- **Base currency:** INR (₹), 2 decimal places, symbol behind: no.
- Set a **security control / TallyVault** password (statutory data).

### Step 2 — Switch on the statutory engines (F11: Company Features)

From Gateway of Tally press **F11**. Set these to **Yes** and drill in:

| Feature | Set | Key entries |
|---|---|---|
| Enable Goods and Services Tax (GST) | Yes | Registration type **Regular**; GSTIN **36AABCN1234A1Z5**; applicable from 01-Apr-2026; periodicity **Monthly**; e-invoicing **Applicable** (T/O > Rs 5 cr, FY2026-27). |
| Enable Tax Deducted at Source (TDS) | Yes | TAN **HYDN01234A**; deductor type **Company – Other than Government**; PAN **AABCN1234A**; responsible person + designation. |
| Maintain Payroll | Yes | Enables salary, EPF/ESI/PT statutory heads. |
| Enable Goods (Inventory) | Yes | Trading arm needs stock items/HSN. |

Note on the law: from **01-Apr-2026** the Income-tax Act 2025 renumbers TDS sections (salary → **Sec 392**, other payments → **Sec 393**). Tally, TRACES and everyone on the job still use the familiar **192 / 194C / 194J / 194H / 194I / 194Q** labels — I'll use those throughout, having flagged the change once here.

### Step 3 — Build the group tree (chart of accounts)

Tally ships 28 primary groups; you rarely create new *groups*, you create *ledgers* under them. The working tree for a trading + services company:

```
Balance Sheet
├─ Capital Account
│   ├─ Equity Share Capital
│   └─ Reserves & Surplus
├─ Loans (Liability)                → (none yet)
├─ Current Liabilities
│   ├─ Duties & Taxes               → Output CGST/SGST/IGST, Input CGST/SGST/IGST,
│   │                                  TDS Payable 194C/194J/194H/194I/194Q, GST Payable
│   ├─ Provisions                   → Provision for Audit Fee, Provision for Tax
│   └─ Sundry Creditors             → vendor ledgers (bill-wise)
├─ Fixed Assets                     → Plant & Machinery, Office Equipment
├─ Current Assets
│   ├─ Bank Accounts                → HDFC Current A/c xxxx4567
│   ├─ Cash-in-Hand                 → Cash
│   ├─ Sundry Debtors               → customer ledgers (bill-wise)
│   ├─ Stock-in-Hand                → managed via inventory
│   └─ Loans & Advances (Asset)     → TDS Receivable, Prepaid Insurance
Profit & Loss A/c
├─ Sales Accounts                   → Sales-Goods, Sales-Services
├─ Purchase Accounts                → Purchases-Goods
├─ Direct Expenses                  → Freight Inward
├─ Indirect Incomes                 → Interest, Bank interest received
└─ Indirect Expenses                → Rent, Telecom, Salaries, Bank Charges, Depreciation,
                                       Audit Fee, Housekeeping, Professional Fee, Commission
```

### Step 4 — Create the key ledger masters (Gateway > Create > Ledger)

Six masters that must be exactly right:

**1. Sales-Goods** — Under **Sales Accounts**; GST applicable **Yes**; Type of supply **Goods**; HSN **8536**; GST rate **18%** (CGST 9 + SGST 9 intra / IGST 18 inter). Tally splits the tax automatically by place of supply.

**2. Sales-Services** — Under **Sales Accounts**; Type of supply **Services**; SAC **9987**; GST **18%**.

**3. Purchases-Goods** — Under **Purchase Accounts**; GST **Yes**; HSN **8536**; 18%.

**4. Output CGST** — Under **Duties & Taxes**; Type of duty/tax **GST**; Tax type **Central Tax**; Percentage left blank (picked from item/ledger); rounding **Normal, nearest 1**. Create the sibling set: Output SGST (State Tax), Output IGST (Integrated Tax), Input CGST, Input SGST, Input IGST — same group, correct tax type each.

**5. TDS Payable – 194J** — Under **Duties & Taxes**; Type of duty/tax **TDS**; Nature of payment **Fees for professional or technical services (194J)**. Repeat for 194C, 194H, 194I, 194Q.

**6. HDFC Current A/c xxxx4567** — Under **Bank Accounts**; enter A/c no. xxxx4567, IFSC, branch; enable **effective date for reconciliation** so the BRS (F5) works later.

Also: **Priya Rao** and 14 other employee masters live under Payroll Info (separate from ledgers); customer/vendor ledgers under Sundry Debtors/Creditors with **Maintain balances bill-by-bill = Yes**.

### Step 5 — Post the opening balances

Enter each opening figure in the ledger master's **Opening Balance** field (Dr/Cr as in the table). Tally shows a running **Difference in opening balances** at the bottom — it must read **0.00** when done. The GST Input Credit c/f of Rs 8,00,000 sits in the electronic credit ledger conceptually; in books it's the debit opening of Input tax carried forward.

## The deliverable

A ready company file. Verification screen — **Gateway > Balance Sheet** as at 01-Apr-2026:

| Liabilities | Rs | Assets | Rs |
|---|---:|---|---:|
| Equity Share Capital | 50,00,000 | Fixed Assets (net) | 1,60,00,000 |
| Reserves & Surplus | 2,20,00,000 | Closing Stock (opening) | 40,00,000 |
| Sundry Creditors | 62,00,000 | Sundry Debtors | 96,00,000 |
| Duties & Taxes (net) | — | Bank – HDFC | 18,00,000 |
| Provisions | 12,00,000 | GST Input Credit c/f | 8,00,000 |
| | | TDS Receivable | 4,00,000 |
| **Total** | **3,44,00,000** | **Total** | **3,44,00,000** |

Plus F11 confirms GST, TDS and Payroll = **Yes**, and the ledger list shows all six output/input GST heads and five TDS payables.

## How it's checked

- **Opening difference = 0.00.** Any non-zero means a ledger was missed or a Dr/Cr flipped.
- **GSTIN checksum & state code.** 36 = Telangana; last char Z5 pattern valid. A wrong state code makes every intra/inter classification wrong.
- **TAN and PAN** match the physical certificates and TRACES login.
- **Sales/Purchase ledgers** carry the right HSN/SAC and supply type — Tally uses these to auto-split CGST/SGST vs IGST.
- Balance Sheet **ties to the prior-year audited figures** to the rupee (3,44,00,000 each side).

## Common mistakes & red flags

| Mistake | Consequence | Fix |
|---|---|---|
| "Books beginning from" set to a wrong date | Opening balances land in wrong period | Set both FY-begin and books-begin to 01-Apr-2026 |
| GST rate typed into the tax *ledger* percentage | Double or zero tax on invoices | Leave rate blank on Duties & Taxes ledger; set it on the stock item / sales ledger |
| CGST and SGST tax types swapped | GSTR-1/3B classify tax under wrong head | Recheck each: Central vs State vs Integrated |
| Bill-wise = No on debtors/creditors | Can't track outstanding invoices or do 194Q YTD | Turn on Maintain balances bill-by-bill |
| Forgot e-invoicing flag | May sales invoices lack IRN → invalid | Enable e-invoicing in F11 GST details |

## On the job & in the interview

The "why": the master setup is where **tax law becomes software behaviour**. A regular monthly filer with T/O Rs 12 cr triggers e-invoicing, 194Q buyer-side TDS, and tax audit — all three flow from the turnover thresholds, so the feature flags aren't cosmetic, they encode compliance obligations.

**Q: NTSPL trades goods and sells services. How many sales ledgers, and why?**
A: At least two — Sales-Goods (HSN 8536) and Sales-Services (SAC 9987) — because HSN vs SAC, the supply type, and GSTR-1 tables differ. Same 18% rate, but reporting and classification demand separate ledgers.

**Q: Where do you configure that a supplier bill attracts reverse charge or that we're an e-invoice company?**
A: F11 Company Features > GST details enables e-invoicing (T/O > Rs 5 cr, FY2026-27); reverse charge is flagged on the purchase ledger / voucher, not the company master.

**Q: The opening Balance Sheet shows a difference of Rs 4,00,000. What's your first check?**
A: A missing asset ledger — most likely the TDS Receivable (Rs 4,00,000 from Form 26AS) wasn't posted. I'd confirm total Dr = total Cr = 3,44,00,000 against the audited BS.
