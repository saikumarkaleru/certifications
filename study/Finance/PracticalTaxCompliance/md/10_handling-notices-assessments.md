# Handling tax notices & assessments

## What it is & where it's used

A tax notice is a formal communication from the Income Tax Department asking you to confirm something, produce evidence, or explain a mismatch. Handling them means: reading the notice correctly, identifying the section it was issued under, gathering the right documents, drafting a reply, and filing the response on the e-filing / e-proceedings portal before the deadline — without escalating a routine query into a full-blown assessment or penalty.

This is one of the most billed, most feared, and least-taught skills in Indian finance. It shows up everywhere:

| Role | How they touch notices |
|---|---|
| Accounts / Finance executive | Receives 143(1) intimations for the company, reconciles the mismatch, books the demand/refund |
| Tax associate (CA firm / Big 4) | Drafts replies to 143(2), 142(1), 148 for dozens of clients |
| Payroll / TDS team | Handles TRACES defaults, 200A intimations, short-deduction notices |
| Finance manager / controller | Signs off on representation, manages assessment exposure and provisions |
| Founder / SME owner | Personally liable — needs someone who can read a notice and not panic |

The moment a notice lands in the inbox, everyone looks for the one person who "knows how to handle it." That person gets promoted and paid.

## The gap: why companies want this (and college didn't teach it)

An MBA teaches you the *theory* of assessment — sections, timelines, appellate hierarchy — as exam facts. It never shows you an actual notice PDF, never makes you log into the portal, never makes you draft a reply under a 15-day clock. The gap is entirely operational:

- College teaches "Section 143(1) is a summary assessment." It never shows you that the intimation is an auto-generated CPC document where **Column A (as filed)** and **Column B (as computed)** sit side by side, and your whole job is to explain the delta.
- College never teaches the **e-Proceedings** tab, the difference between a mere *intimation* and an *adverse* notice, or that ignoring a 143(1) refund-adjustment proposal for 30 days = deemed acceptance.
- Faceless assessment (from 2020) changed everything to written submissions uploaded online. There is no "going to the officer's chamber" anymore — your **drafting quality is the representation.** MBAs are never taught to write a submission.

Employers pay for the person who can turn a scary PDF into a calm, evidenced, on-time reply. That is a learnable, mechanical skill — and it's the gap this chapter closes.

## What "proficient" looks like

A job-ready person, handed a notice, can unaided:

1. **Identify the section and sub-type** within 60 seconds (intimation vs scrutiny vs reassessment).
2. State the **response deadline and consequence of missing it.**
3. Pull the **matching data** — ITR, Form 26AS, AIS/TIS, Form 16/16A, books, bank statements — and build a reconciliation.
4. Draft a **point-wise reply** that answers each query with a document reference (Annexure-1, -2…).
5. File it via **e-Proceedings**, attach a consolidated PDF, and download the acknowledgement.
6. Know when to **agree and pay**, when to **contest**, and when to escalate to a CA/counsel.

## Hands-on: how to actually do it

### Step 1 — Decode the section

| Section | What it is | Trigger | Typical deadline | Consequence of ignoring |
|---|---|---|---|---|
| **143(1)** | Intimation (summary processing by CPC) | Arithmetic error, TDS/tax mismatch, disallowance u/s 143(1)(a) | 30 days to respond to adjustment proposal | Adjustment auto-confirmed; demand raised |
| **142(1)** | Inquiry before assessment | Non-filing, or AO wants documents/info | As stated (often 15 days) | Best-judgment assessment u/s 144; penalty u/s 272A |
| **143(2)** | Scrutiny notice | Return picked for detailed scrutiny (CASS/manual) | Must be **served within 3 months from end of FY in which return filed**; reply as scheduled | Assessment proceeds; adverse additions |
| **148** | Income escaping assessment (reassessment) | AO has "information" income escaped; preceded by 148A show-cause | As stated (30 days typical) | Reassessment, tax + interest + penalty |
| **156** | Notice of demand | Follows any order creating a demand | 30 days to pay | 1% p.m. interest u/s 220(2); recovery |
| **245** | Adjustment of refund against demand | Old demand outstanding | 30 days to respond | Refund adjusted |

### Step 2 — Log in and locate it

**Portal click-path (incometax.gov.in):**
```
Login → Pending Actions → e-Proceedings
→ select the AY → View Notices
→ read the notice PDF + "Response" button
→ Submit Response → upload PDF (max ~5 MB/attachment)
→ e-Verify (Aadhaar OTP / DSC) → download Acknowledgement (Transaction ID)
```
For 143(1) mismatches specifically: `Pending Actions → Response to Outstanding Demand` or the **"Agree / Disagree"** grid inside the intimation.

### Step 3 — Build the reconciliation (Excel)

The core analytical task in 90% of notices is: *the department's number ≠ your number — explain the gap.* A 143(1)(a) TDS mismatch is a classic:

```excel
' Match income booked vs AIS/26AS by TAN/party
=XLOOKUP(A2, AIS!$A:$A, AIS!$C:$C, "NOT IN AIS")

' Gap column
=Books_Amount - AIS_Amount

' Flag material differences
=IF(ABS(D2)>1000, "EXPLAIN", "OK")

' TDS credit reconciliation
=SUMIF('26AS'!B:B, A2, '26AS'!D:D)   ' TDS per 26AS for this TAN
```

Put it in a clean table you can paste into the reply and attach:

| Party / TAN | As per 26AS/AIS (₹) | As per Books/ITR (₹) | Difference (₹) | Reason |
|---|---|---|---|---|
| ABC Ltd / MUMA1234B | 5,00,000 | 5,00,000 | 0 | Matched |
| XYZ Bank / DELX9876C | 82,400 | 0 | 82,400 | FD interest — accrued, offered in AY 2024-25 |

### Step 4 — Draft the reply (reusable skeleton)

```
To: The Assessing Officer / CPC / NaFAC
PAN: ABCDE1234F   |   AY: 2024-25
Notice u/s 143(1)(a) dated 12-06-2024, DIN: <DIN>

Sub: Response to proposed adjustment — reg.

1. This is with reference to the captioned intimation proposing an
   adjustment of ₹82,400 on account of interest income appearing in
   Form 26AS but allegedly not offered to tax.

2. The assessee submits that the said interest was offered under
   "Income from Other Sources" in Schedule OS, Row 3 of the return
   (refer Annexure-1: ITR-V / computation extract).

3. The apparent mismatch arises solely due to TDS being reflected in
   26AS in AY 2024-25 while the income was offered on accrual basis.
   Reconciliation enclosed as Annexure-2.

4. It is therefore prayed that the proposed adjustment be dropped and
   the return be processed as filed.

Enclosures: Annexure-1 (Computation), Annexure-2 (Reconciliation),
Annexure-3 (Bank interest certificate)
```

Merge everything into **one indexed PDF** (reply + annexures) before uploading.

## Worked example / mini-project

**Scenario.** Rao Traders Pvt Ltd files ITR for AY 2024-25 declaring total income ₹42,00,000, tax paid ₹10,92,000. On 12 Jun 2024 CPC issues a **143(1)(a)** intimation:

- Adds ₹1,20,000 — "contract receipts in 26AS not reconciled with turnover."
- Disallows ₹35,000 — "late deposit of employee PF, u/s 36(1)(va)."
- Proposed demand: ₹48,050 (tax + interest u/s 234).

**Your workflow:**

1. **Read** → It's an *intimation with adjustment proposal*, not scrutiny. 30-day clock.
2. **Reconcile the ₹1,20,000.** Pull 26AS contract receipts (Section 194C) vs revenue ledger:

```excel
=SUMIF('26AS'!C:C, "194C", '26AS'!E:E)      ' 26AS 194C receipts
=SUMIFS(Sales!Amt, Sales!Party, "Bharat Infra")
```
Finding: the ₹1,20,000 is a **March advance** appearing in 26AS (deductor booked it) but recognised as revenue in the *next* year per AS-9/Ind AS 115. **Contest** — it's timing, not escapement.

3. **The ₹35,000 PF.** Check challan dates vs due date. EPF for Feb 2024 (due 15 Mar) was actually deposited **22 Mar**. Post *Checkmate Services (SC, 2022)*, employee-contribution deposited after the PF-Act due date is **not deductible.** **Agree** — do not fight a lost cause.

4. **Respond on portal:** Disagree on ₹1,20,000 (with reconciliation Annexure), Agree on ₹35,000.

5. **Revised demand** after acceptance: tax on ₹35,000 @ ~26% ≈ ₹9,100 + interest ≈ ₹1,500 = **₹10,600.** Pay via **e-Pay Tax → Challan (Minor Head 400 – tax on regular assessment)**.

6. **Journal entries:**

| Particulars | Dr (₹) | Cr (₹) |
|---|---|---|
| Income Tax Expense (prior period) A/c | 10,600 | |
|   To Provision for Tax / Bank A/c | | 10,600 |
| *(Being demand u/s 143(1) accepted for PF disallowance, AY 24-25)* | | |

The ₹1,20,000 timing item: **no entry** — it reverses naturally as it's taxed next year. Download the acknowledgement (Transaction ID), file it. Done in under two hours.

## How it's tested

**Interview questions:**
- "What's the difference between 143(1) and 143(2)?" (Summary/CPC vs detailed scrutiny/AO.)
- "You get a 143(1)(a) with a TDS mismatch — walk me through your first four steps."
- "Client got a 148. What do you check before replying?" (Whether 148A procedure was followed, validity of reopening, time limits, the "information" basis.)
- "Deadline for responding to a 143(1) adjustment? Consequence of missing it?" (30 days; deemed acceptance.)
- "Employee PF deposited late — deductible?" (No, post-Checkmate.)

**Practical assessments companies actually give:**
- **The "here's a notice PDF, draft the reply" test** — a sample intimation and a folder of documents; produce the reconciliation + reply in 60–90 min.
- **A mismatch reconciliation in Excel** — 26AS vs books, find and explain every gap.
- **A portal walkthrough** — "show me where you'd file the response" (screen-share).
- **Case judgment** — a mixed notice where some items should be agreed and some contested; they test whether you know *when to fight*.

## Common mistakes & how pros avoid them

| Mistake | Why it hurts | Pro habit |
|---|---|---|
| Treating every 143(1) as an emergency | Most are refunds/no-action intimations | Read the last page — "no action required" vs adjustment proposal |
| Missing the 30-day window | Adjustment auto-confirmed, demand raised | Diary every DIN with deadline the day it arrives |
| Fighting genuinely lost items (late PF, bogus expense) | Invites penalty, wastes goodwill | Concede clean losers, contest strong points only |
| Replying without annexures / DIN reference | Reply treated as unsubstantiated | Every claim → an annexure; quote DIN & AY on page 1 |
| Uploading 12 separate files | Officer can't follow; looks amateur | One indexed, bookmarked PDF |
| Not verifying the notice is genuine | Fraud/phishing PDFs exist | Verify DIN on portal: `Authenticate Notice/Order Issued by ITD` |
| Ignoring AIS/TIS | Half of all mismatches originate there | Reconcile books → AIS/TIS → 26AS every time |

## Learn-it roadmap & resources

**Time to proficiency: 4–6 weeks** of deliberate practice alongside a job.

| Week | Focus |
|---|---|
| 1 | Memorise the section table; read 5 real anonymised notices |
| 2 | Master the portal: e-Proceedings, Response to Demand, Authenticate DIN, e-Pay Tax |
| 3 | Build 3 reconciliations (26AS/AIS vs books) in Excel end-to-end |
| 4 | Draft 3 replies from templates; get them reviewed by a CA |
| 5–6 | Shadow live notices; learn agree-vs-contest judgment |

**Resources:**
- **Income Tax portal help section** + the "e-Proceedings" user manual (free).
- **income-tax.gov.in → AIS** and **TRACES** (for TDS/26AS) — practice logins.
- Bare Act: **Sections 139–158** (skim), free on incometaxindia.gov.in.
- **Taxmann / Taxsutra** blogs for landmark cases (Checkmate, Ashish Agarwal on 148).
- ICAI's **Background Material on Faceless Assessment** (free PDF).
- Certification: **ICAI Certificate Course on Faceless Assessment**, or any GST+IT practitioner course; the CA Inter Taxation paper itself covers the statutory base.

## Quick-reference

**Section cheat-sheet**
- `143(1)` — CPC intimation → **30 days** to respond to adjustment
- `142(1)` — inquiry / call for docs → reply or face 144
- `143(2)` — scrutiny → served within **3 months** of FY-end of filing
- `148` — reassessment → preceded by **148A** show-cause
- `156` — demand notice → **pay in 30 days**, else 1% p.m. u/s 220(2)
- `245` — refund adjusted against old demand

**Portal paths**
- File reply: `Pending Actions → e-Proceedings → Submit Response`
- Pay demand: `e-Pay Tax → Minor Head 400`
- Verify notice: `Authenticate Notice/Order Issued by ITD` (use DIN)

**Excel workhorses**
- `=XLOOKUP(party, AIS_range, amt_range, "NOT IN AIS")`
- `=SUMIF('26AS'!TAN, party, '26AS'!TDS)`
- `=IF(ABS(Books-AIS)>1000,"EXPLAIN","OK")`

**Golden rules**
1. Identify the section first. 2. Note the deadline the day it arrives. 3. Reconcile before you draft. 4. Concede losers, contest winners. 5. One indexed PDF, every claim annexed, DIN on page 1. 6. Always download the acknowledgement.
