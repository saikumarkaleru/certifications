# AI-Era Finance Careers

## What it is & where it's used

"AI in finance" is not a job title — it is a layer that now sits under almost every finance task you already do. The reader who masters this chapter does not become a "prompt engineer"; they become the analyst, accountant, or tax associate who finishes in 40 minutes what a peer takes a day to do, and who can defend every number.

Concretely, AI shows up in finance work in four places:

| Layer | Tool examples | Finance task it touches |
|---|---|---|
| Assistant / chat | ChatGPT, Claude, Copilot, Gemini | Draft variance commentary, explain a formula, summarise a 200-page annual report, write SQL/DAX for you |
| Embedded copilots | Excel Copilot, Power BI Copilot, Tally add-ons, Zoho | In-app formula generation, "explain this pivot", auto-categorise ledgers |
| Document AI / OCR | Nanonets, Docsumo, GST-portal auto-populate (GSTR-2B), bank-statement parsers | Invoice/PO/bank-statement extraction into structured data |
| Custom automation | Python + LLM APIs, RPA (UiPath), macros | Batch reconciliation, exception flagging, three-way match, board-pack generation |

Roles that now expect this: FP&A analyst, financial analyst, controller/accounts manager, tax associate (Direct + GST), internal audit, equity research, and treasury. In India specifically, mid-size firms and Big-4 + next-tier (BDO, Grant Thornton, Nexdigm) are hiring associates who can "do more with less" — the AI-fluent CA-Inter/MBA is exactly that profile.

## The gap: why companies want this (and college didn't teach it)

Your MBA taught you *what* a DCF is and *why* WACC matters. It did not teach you that a controller now expects the month-end commentary drafted by an LLM and then **fact-checked and corrected by you** in 20 minutes. CA coursework drills the Companies Act and Ind AS — it does not drill feeding a trial balance into a model, catching the three hallucinated numbers, and shipping a clean schedule.

The gap is specific and it is about **judgement over output**:

- College rewards you for producing an answer. Industry now assumes the machine produces a first draft; you are paid to **verify, correct, and take ownership**.
- College treats tools as separate subjects. Industry needs them stitched: OCR pulls invoices → Python reconciles → LLM drafts the note → you sign off.
- College never taught **where AI is dangerous**: it invents citations, mis-reads a bracketed negative as positive, confidently averages the wrong column. Firms have been burned by juniors who pasted ChatGPT output into a filing.

So the thing companies actually pay a premium for is not "can you use ChatGPT" — everyone can. It is: **can you use it fast AND catch its mistakes AND explain your control over it to an auditor.**

## What "proficient" looks like

The employer's bar — what a job-ready person does unaided:

1. **Reframes a finance task into a good prompt** with role, context, data, format, and constraints — not "write me a variance analysis".
2. **Never trusts a number blindly.** Ties every AI-produced figure back to the source (trial balance, GSTR-2B, bank statement) before it leaves their desk.
3. **Uses AI to write tools, not just prose** — generates a working SQL query, an Excel formula, a Python reconciliation script, then reviews it line by line.
4. **Knows the data-security line**: never pastes client PII, unmasked PAN/GSTIN, salary data, or unpublished financials into a public chatbot. Uses enterprise/redacted versions.
5. **Automates one repetitive close/tax task** end-to-end and can show the before/after time saving.
6. **Explains the audit trail**: "AI drafted, I verified against X, here's my working."

## Hands-on: how to actually do it

### 1. A reusable finance prompt skeleton

```
Role: You are a senior FP&A analyst.
Context: Indian manufacturing SME, FY25-26, INR, figures in lakhs.
Data: [paste trial balance / table]
Task: Draft budget-vs-actual variance commentary for opex.
Rules: Only use numbers I gave you. Flag any figure you had to
       assume. Show % variance = (Actual-Budget)/Budget. No advice
       beyond the data. Output: 5 bullets, then a 3-column table.
```

The three rules — *only my numbers, flag assumptions, show the formula* — are what stop hallucination.

### 2. Let AI write the Excel, then you own it

Ask: "XLOOKUP to pull GST rate from a rate master, return 0 if not found." You should be able to read and correct what it returns:

```excel
=XLOOKUP(B2, RateMaster!A:A, RateMaster!B:B, 0, 0)

=LET(sales, SUMIFS(Data[Amt], Data[Region], A2),
     tax,   sales*0.18,
     sales + tax)
```

If the model gives you `VLOOKUP` with a hardcoded column index, you *fix it* to `XLOOKUP` — that judgement is the skill.

### 3. Generate SQL for a reconciliation, review before running

Prompt: "SQL: find invoices in our books not in GSTR-2B, MySQL." Expected output you must be able to vet:

```sql
SELECT b.invoice_no, b.gstin, b.taxable_val, b.igst
FROM   books_purchase b
LEFT   JOIN gstr2b g
       ON  b.invoice_no = g.invoice_no
       AND b.gstin       = g.gstin
WHERE  g.invoice_no IS NULL          -- in books, missing in 2B
ORDER  BY b.taxable_val DESC;
```

Red flag to catch: if the AI joins on `invoice_no` alone, duplicate invoice numbers across vendors give false matches. You add `AND b.gstin = g.gstin`. That correction is why they hired you, not the bot.

### 4. Python: batch-parse bank statements the AI helped you write

```python
import pandas as pd

# read all monthly statements, tag credits/debits, flag round-number txns
df = pd.read_excel("bank_stmt.xlsx")
df["type"] = df["amount"].apply(lambda x: "credit" if x > 0 else "debit")
df["round_flag"] = (df["amount"].abs() % 10000 == 0)   # audit red flag
suspense = df[df["narration"].str.contains("SUSPENSE|UNKNOWN",
                                           case=False, na=False)]
print(suspense[["date", "amount", "narration"]])
```

Always print a control total and tie it to the closing balance before trusting the output.

### 5. Power BI DAX the copilot drafts, you validate

```dax
Actual vs Budget % =
DIVIDE(
    SUM(Fact[Actual]) - SUM(Fact[Budget]),
    SUM(Fact[Budget])
)
```

Check the copilot didn't use `/` (which errors on zero budget) instead of `DIVIDE`.

### 6. GST-portal + AI reconciliation flow (India)

1. `services.gst.gov.in` → Returns Dashboard → download **GSTR-2B** (JSON/Excel).
2. Export purchase register from TallyPrime: **Gateway → Display → Account Books → Purchase Register → Alt+E (Export) → Excel**.
3. Feed both into the SQL/Python match above, or paste summarised columns into an LLM to draft the mismatch email to vendors.
4. **You** decide ITC eligibility — never the bot (Rule 37, Sec 16(2)(c) are judgement calls).

## Worked example / mini-project

**Goal:** AI-assisted GST ITC reconciliation for a Bengaluru trading firm, Jun 2026.

**Data (books purchase register, ₹ in full):**

| Invoice | Vendor GSTIN | Taxable | IGST |
|---|---|---|---|
| INV-101 | 29ABCDE1234F1Z5 | 2,00,000 | 36,000 |
| INV-102 | 29PQRST5678K1Z2 | 1,50,000 | 27,000 |
| INV-103 | 27LMNOP9012J1Z8 | 3,00,000 | 54,000 |

**GSTR-2B (as downloaded):** contains INV-101 and INV-103 only. INV-102 is missing (vendor hasn't filed).

**Step 1 — AI drafts the reco logic**, you run the SQL from section 3. Output: INV-102 flagged.

**Step 2 — Journal impact.** ITC on INV-102 (₹27,000) cannot be claimed this month. Provisional entry to hold it:

| Particulars | Dr (₹) | Cr (₹) |
|---|---|---|
| Purchases A/c | 1,50,000 | |
| ITC Ineligible/Blocked (2B mismatch) A/c | 27,000 | |
| To Vendor (Sundry Creditor) A/c | | 1,77,000 |

When the vendor files and INV-102 appears in a later 2B, reverse the block and claim:

| Particulars | Dr (₹) | Cr (₹) |
|---|---|---|
| Input IGST A/c | 27,000 | |
| To ITC Ineligible/Blocked A/c | | 27,000 |

**Step 3 — AI drafts the vendor email**, you edit: *"INV-102 (₹1,77,000) not reflecting in our June GSTR-2B; ITC of ₹27,000 withheld until your GSTR-1 is filed."*

**Result:** eligible ITC this month = 36,000 + 54,000 = **₹90,000**, ₹27,000 correctly deferred. A task that is 2 hours by hand is ~25 minutes — and you can defend every rupee. That defensibility is the deliverable.

## How it's tested

Interviews and practical screens for AI-era finance roles:

**Conceptual / judgement questions**
- "You asked ChatGPT for a variance analysis and it gave a number that doesn't tie to the TB. What do you do?" (Answer: trace to source, never ship unverified.)
- "What would you *never* paste into a public LLM?" (Client PII, PAN/GSTIN, salaries, unpublished results, MNPI.)
- "Where does AI fail in a GST reco?" (ITC eligibility, Rule 37 reversal, blocked credits u/s 17(5) — human calls.)

**Practical assessments companies actually give**
- A **timed case**: "Here's a trial balance and a messy AI-drafted commentary — find and fix the 3 errors in 20 minutes."
- A **live tool test**: "Write a prompt to reconcile these two files, then show me the Excel/SQL you'd use." They watch whether you verify.
- A **"close these books" case** where using AI is *allowed* and they judge your control, audit trail, and speed — not whether you memorised formulas.
- Excel + Power BI hands-on where Copilot is enabled and they see if you catch its `DIVIDE`/join mistakes.

## Common mistakes & how pros avoid them

| Mistake | How pros avoid it |
|---|---|
| Pasting client PII/GSTIN/salary into a public chatbot | Redact first, or use enterprise/on-prem tools; know the firm's AI policy |
| Trusting AI numbers without tying to source | Always reconcile to TB / 2B / bank balance before shipping |
| Accepting hallucinated citations (a fake ICAI para, a wrong section) | Verify every legal/standard reference against the bare act/standard |
| Vague prompts → vague junk | Use the role-context-data-format-rules skeleton |
| Letting AL do the *judgement* (ITC eligibility, provisioning, going concern) | AI drafts, human decides; keep the call yours |
| No audit trail — "the AI said so" | Document: prompt used, source verified, your correction |
| Using AI to *replace* learning fundamentals | Learn the concept first so you can catch the bot's errors |

The one-line rule: **AI is a fast intern, not a partner. You review its work; you sign the file.**

## Learn-it roadmap & resources

Realistic time-to-proficiency: **4–6 weeks** part-time to be interview-ready, assuming you already know Excel and basic accounting.

| Week | Focus | Deliverable |
|---|---|---|
| 1 | Prompting for finance; the RCDFR skeleton; data-security rules | 10 saved prompts for your real tasks |
| 2 | AI-assisted Excel/DAX; catch its mistakes | Rebuild a report with Copilot, log every error you caught |
| 3 | SQL + Python for reconciliation (AI writes, you review) | The GST/bank reco mini-project above |
| 4 | Document AI / OCR + end-to-end automation | One repetitive close task automated, timed before/after |
| 5–6 | Audit trail, governance, mock timed case | A 1-page "how I use AI safely" you can talk through |

**Resources**
- Free: OpenAI/Anthropic prompting guides; Microsoft *Copilot in Excel/Power BI* Learn modules; freeCodeCamp Python; Mode SQL tutorial; the GST portal's own advisories.
- Paid: Coursera *Generative AI for Business/Finance*; Wall Street Prep / CFI AI-for-finance modules; DataCamp Python-for-finance track.
- India-specific: ICAI's Digital Accounting & Assurance Board material; TallyPrime + GST reco practice.
- Certifications worth listing on a CV: Microsoft **PL-300** (Power BI), any recognised Generative-AI-for-Finance course. No single "AI finance" cert is a must-have yet — the **portfolio of an automated task** beats a certificate.

## Quick-reference

| Need | Copy-usable |
|---|---|
| Prompt skeleton | Role → Context → Data → Task → Rules (only my numbers / flag assumptions / show formula) |
| Lookup | `=XLOOKUP(key, lookup_col, return_col, 0, 0)` |
| Safe division (DAX) | `DIVIDE(num, den)` — never `/` |
| Variance % | `(Actual - Budget) / Budget` |
| SQL: in books, not in 2B | `LEFT JOIN … ON invoice_no AND gstin WHERE g.invoice_no IS NULL` |
| Python control check | Print `df["amount"].sum()`, tie to closing balance |
| GST reco path | GST portal → GSTR-2B ↓ · Tally → Purchase Register → Alt+E ↓ · match |
| Never paste | PII, PAN/GSTIN, salaries, unpublished results, MNPI |
| Golden rule | AI drafts → you verify to source → you sign |
| ITC block entry | Dr Purchases, Dr ITC-Ineligible, Cr Creditor; reverse when 2B updates |
