# AI & automation in finance

## What it is & where it's used

"AI & automation in finance" means using three overlapping tool families to do finance work faster and with fewer errors:

1. **LLMs / Copilots** — ChatGPT, Claude, Microsoft 365 Copilot, Gemini. You give plain-English instructions ("prompts") and get back formulas, SQL, draft emails, variance commentary, reconciliations logic, GST notice replies, DCF explanations.
2. **RPA (Robotic Process Automation)** — bots that click through screens and move data the way a human would: Power Automate, UiPath, or even Excel VBA / Office Scripts. Used for repetitive, rule-based tasks — downloading bank statements, keying invoices into Tally, pulling GSTR-2B every month.
3. **Built-in AI features** — Copilot inside Excel, Power BI Copilot (writes DAX and narratives), Tally's AI add-ons, GSTN's e-invoice/IRP automation.

Where it shows up by role:

| Role | AI/automation use |
|---|---|
| Accounts / AP-AR executive | Auto-key invoices, 3-way match bots, draft vendor follow-up emails |
| GST / tax associate | Reconcile GSTR-2B vs purchase register, draft replies to notices, summarise circulars |
| FP&A / MIS analyst | Copilot writes DAX/formulas, generates variance commentary, builds monthly deck |
| Audit / internal audit | Sample selection, exception testing, summarise policies vs. transactions |
| Treasury / controller | Bank-recon bots, cash-flow forecasting prompts |

## The gap: why companies want this (and college didn't teach it)

Your MBA/CA syllabus teaches **concepts** — accounting standards, cost of capital, GST law. It does not teach that in a real month-end you will re-key the same numbers 40 times, or that a junior who can make a bot download 30 bank statements in 3 minutes is worth 5x one who does it by hand.

The specific gap:

- College assumes **one clean dataset**. Industry gives you a messy Tally export, a bank PDF, and a GSTR-2B JSON that must be joined — under time pressure.
- College grades **the right answer**. Employers pay for **the right answer produced repeatably and fast**, with an audit trail.
- Nobody teaches **how to instruct an AI safely** — what to paste, what NOT to paste (client PAN, salary data), and how to verify AI output before it hits a filing.

The finance-specific risk employers fear: an analyst who blindly trusts a hallucinated number in a board deck, or pastes confidential data into a public chatbot. The person who understands **both the tool and its limits** is the one who gets hired and promoted.

## What "proficient" looks like

A job-ready person can, unaided:

- Write a **prompt that produces a working Excel formula, SQL query, or DAX measure** on the first or second try, then verify it against a known-good number.
- Use Copilot in Excel/Power BI to **draft variance commentary**, then edit it for accuracy (not ship it raw).
- Build a **Power Automate flow** that moves files/data on a schedule without manual clicks.
- Record an **Excel macro / Office Script** for a repetitive cleanup and re-run it monthly.
- Know **data-governance red lines**: never paste PII, client-identifiable, or price-sensitive data into a public LLM; use the company-approved enterprise tool.
- **Sanity-check every AI output** — recompute totals, tie to source, flag anything the model "confidently" made up.

The bar is not "can code an AI model." It is "can use AI as a fast, cheap junior analyst — and catch its mistakes."

## Hands-on: how to actually do it

### 1. Prompt patterns that work for finance

Use this **structure** every time: *Role → Context → Task → Format → Constraints.*

```
Role: You are an FP&A analyst.
Context: I have a table with columns Month, Budget, Actual (INR lakhs).
Task: Write an Excel formula for the % variance in column D,
      and flag "REVIEW" if the unfavourable variance exceeds 10%.
Format: Give the formula only, then one line explaining it.
Constraints: Assume data starts in row 2. No macros.
```

Reusable prompt patterns:

| Pattern | Use it for | Example opener |
|---|---|---|
| **Explain-then-do** | Learning while producing | "Explain what a 3-way match is, then give the SQL to find mismatches." |
| **Formula generator** | Excel/DAX/SQL | "Write an XLOOKUP that returns HSN code from Sheet2, exact match." |
| **Reconciliation logic** | GSTR-2B vs books | "Given two tables by GSTIN+invoice no, list rows in A not in B." |
| **Draft & polish** | Emails, commentary | "Draft a polite payment-reminder email; overdue Rs 2,45,000, 45 days." |
| **Summarise-to-decision** | Circulars, policies | "Summarise this GST circular into 5 action points for a trader." |
| **Red-team / check** | Catch your own errors | "Here's my DCF. What assumptions look aggressive?" |

### 2. Getting real formulas from an LLM

Ask, then paste this into Excel:

```
=IFERROR(XLOOKUP(A2, Vendors[GSTIN], Vendors[VendorName], "Not found"), "Error")
```

Variance flag (from the prompt above):

```
=IF((C2-B2)/B2 < -0.10, "REVIEW", TEXT((C2-B2)/B2, "0.0%"))
```

### 3. SQL the LLM writes for you — GSTR-2B vs purchase register

```sql
-- Invoices in books but MISSING in 2B (ITC at risk)
SELECT pr.gstin, pr.invoice_no, pr.taxable_value, pr.igst
FROM purchase_register pr
LEFT JOIN gstr2b b
       ON pr.gstin = b.gstin AND pr.invoice_no = b.invoice_no
WHERE b.invoice_no IS NULL;
```

### 4. Python snippet for a repetitive reconciliation

```python
import pandas as pd

books = pd.read_excel("purchase_register.xlsx")
b2b   = pd.read_excel("gstr2b.xlsx")

merged = books.merge(b2b, on=["gstin", "invoice_no"],
                     how="outer", indicator=True)

only_books = merged[merged["_merge"] == "left_only"]   # ITC at risk
only_2b    = merged[merged["_merge"] == "right_only"]   # vendor filed, you didn't book
print(f"Missing in 2B: {len(only_books)} | Missing in books: {len(only_2b)}")
only_books.to_excel("itc_at_risk.xlsx", index=False)
```

### 5. DAX from Power BI Copilot (verify before trusting)

```dax
Variance % =
DIVIDE(
    SUM('P&L'[Actual]) - SUM('P&L'[Budget]),
    SUM('P&L'[Budget])
)
```

### 6. RPA basics — Power Automate (no code)

A first flow every finance junior should build:

1. Go to **make.powerautomate.com** → **Create** → **Scheduled cloud flow**.
2. Trigger: run **1st of every month, 9 AM**.
3. Action: **Outlook → Get attachments** where subject contains "Bank Statement".
4. Action: **OneDrive → Create file** in `/Recon/{Month}/`.
5. Action: **Send me an email** "3 statements filed."

For desktop clicking (e.g., keying into Tally), use **Power Automate Desktop** → record clicks → replace the manual keying loop.

## Worked example / mini-project

**Goal:** Automate the monthly ITC reconciliation for a small trading firm, "Sharma Traders."

**Inputs (reproduce with dummy data):**

| gstin | invoice_no | taxable_value (Rs) | igst (Rs) | source |
|---|---|---|---|---|
| 27ABCDE1234F1Z5 | INV-101 | 1,00,000 | 18,000 | books |
| 29PQRST5678K2Z1 | INV-102 | 50,000 | 9,000 | books |
| 27ABCDE1234F1Z5 | INV-101 | 1,00,000 | 18,000 | 2B |
| 24LMNOP9012Q3Z9 | INV-777 | 75,000 | 13,500 | 2B |

**Step 1 — Prompt the LLM:**

```
Role: GST analyst. I have purchase_register and gstr2b tables
(gstin, invoice_no, taxable_value, igst). Write Python to output:
(a) invoices in books not in 2B, (b) in 2B not in books,
(c) total IGST at risk. Save to Excel.
```

**Step 2 — Run the Python from section 4.** Result:

- INV-102 → in books, **not in 2B** → Rs 9,000 IGST at risk (chase vendor to file).
- INV-777 → in 2B, **not in books** → Rs 13,500 (book it or query the vendor).

**Step 3 — Copilot drafts the commentary:** "For June, Rs 9,000 ITC is blocked pending vendor filing of INV-102; one unrecorded inward supply (INV-777, Rs 13,500 IGST) requires booking."

**Step 4 — You verify:** recompute `SUMIF` on IGST, tie totals to Tally's GSTR-2 report, confirm the two exceptions by eye. Then file.

**Step 5 — Automate next month:** save the Python + a Power Automate flow that drops both files into a folder and emails you the exception count. Month-end task drops from ~2 hours to ~10 minutes.

## How it's tested

**Interview questions:**

- "How would you use ChatGPT/Copilot in your day, and what would you *never* paste into it?" (They test data-governance awareness.)
- "The AI gives you a formula that returns a wrong total. What's your process?" (Verification mindset.)
- "Walk me through automating a task you did manually." (Do you think in repeatable processes?)
- "What are LLM hallucinations and why do they matter for a filing?"

**Practical / assessment tests companies give:**

- **Timed Copilot/Excel test:** "Here's a messy 5,000-row export. Use any AI help to reconcile and produce a variance summary in 30 minutes." They watch *how* you prompt and *whether* you verify.
- **Prompt-craft screen:** given a business ask, write the prompt(s) you'd use.
- **RPA task:** "Build a flow that emails a reminder when an invoice is >30 days overdue."
- **Judgment case:** "This AI-generated board number looks off — find the error." (The error is planted.)

## Common mistakes & how pros avoid them

| Mistake | How pros avoid it |
|---|---|
| Pasting client PAN/GSTIN/salary into a public chatbot | Use enterprise/approved tools; anonymise; paste structure, not sensitive values |
| Shipping AI output unchecked | Always recompute totals, tie to source, spot-check 3-5 rows |
| Trusting a hallucinated citation (fake section/circular no.) | Verify every legal reference against the actual GST portal / bare act |
| Vague prompts ("analyse this") | Use Role-Context-Task-Format-Constraints; give a sample of the data |
| Automating a broken process | Fix and document the manual process first, *then* automate |
| No audit trail | Keep the prompt, the source file, and a note of what you verified |
| Over-automating one-off tasks | Automate only recurring, rule-based work (the 80/20) |

## Learn-it roadmap & resources

**Time to job-ready: ~4-6 weeks, part-time.**

| Week | Focus |
|---|---|
| 1 | Prompt patterns; use ChatGPT/Copilot to generate Excel formulas daily |
| 2 | LLM for SQL + reconciliation logic; learn to verify every output |
| 3 | Power Automate — build 2-3 scheduled/desktop flows |
| 4 | Copilot in Excel & Power BI (DAX + narratives) |
| 5-6 | End-to-end mini-project (the ITC recon above); learn data-governance rules |

**Resources:**

- **Free:** Microsoft Learn — Power Automate & Copilot paths; Google's "Prompting Essentials"; Anthropic/OpenAI prompt guides; YouTube (Leila Gharani for Excel+AI).
- **Paid:** Microsoft 365 Copilot licence (if employer provides); UiPath Academy (free RPA certs); Coursera "Generative AI for Finance."
- **Certifications worth it:** Microsoft **PL-900** (Power Platform), **UiPath RPA Associate**, Microsoft **PL-300** (Power BI, includes Copilot).

**Staying relevant:** treat AI as a **force multiplier, not a replacement**. The finance jobs that survive belong to people who pair domain judgment (accounting standards, GST law, materiality) with tool fluency. Learn one new automation each month; keep a personal "prompt library" of what works.

## Quick-reference

**Prompt skeleton:** `Role → Context (with data sample) → Task → Format → Constraints`

**Key formulas / snippets:**

| Need | Snippet |
|---|---|
| Lookup with error handling | `=IFERROR(XLOOKUP(A2, tbl[key], tbl[val], "NA"), "Err")` |
| Variance flag | `=IF((Actual-Budget)/Budget < -0.1, "REVIEW", "OK")` |
| Missing in 2B (SQL) | `LEFT JOIN ... WHERE b.invoice_no IS NULL` |
| Recon (Python) | `books.merge(b2b, on=[...], how="outer", indicator=True)` |
| Variance % (DAX) | `DIVIDE(SUM(Actual)-SUM(Budget), SUM(Budget))` |

**Red lines — never paste into a public LLM:** PAN, Aadhaar, GSTIN-linked client data, salary/HR data, price-sensitive/unpublished financials.

**Verify-before-ship checklist:** recompute totals · tie to source · spot-check 3-5 rows · verify every cited section/circular · keep prompt + source as audit trail.

**Automate only if:** recurring + rule-based + stable process. One-off or judgment-heavy → do it manually.
