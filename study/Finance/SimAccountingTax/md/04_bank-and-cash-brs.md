# Bank & Cash: Building the Bank Reconciliation Statement

## The situation

It's 1 May 2026, 10:00 a.m. April is closed on paper, but the Finance Manager won't sign off the month until the **bank reconciliation** is done:

> "The HDFC statement is in your inbox. Our Tally bank ledger says one thing, the bank says another. Tell me *why* they differ, book anything that's genuinely ours — charges, interest, auto-debits — and get me a BRS that ties to the bank's closing balance. I don't want a single unexplained rupee."

A BRS is the control that proves your cash book is real. It's the first thing an auditor tests and the fastest way to catch a fraud, a missed entry, or a bounced cheque.

## What you're given

**Tally bank ledger — HDFC Current A/c xxxx4567 (as per books), April 2026:**

| Date | Particulars | Dr (receipts) | Cr (payments) | Balance |
|---|---|---:|---:|---:|
| 01-Apr | Opening balance | | | 18,00,000 Dr |
| 08-Apr | Recd – Mysore Motors (cheq dep) | 29,50,000 | | 47,50,000 Dr |
| 15-Apr | Paid – Deccan Electricals (Cheq 100234) | | 11,80,000 | 35,70,000 Dr |
| 22-Apr | Paid – Bombay Switchgear (NEFT) | | 14,16,000 | 21,54,000 Dr |
| 28-Apr | Paid – Rent, Cyber Estates (Cheq 100235) | | 1,77,000 | 19,77,000 Dr |
| 30-Apr | Deposited – April collections (cheq) | 8,00,000 | | 27,77,000 Dr |
| | **Closing balance as per books** | | | **27,77,000 Dr** |

**HDFC bank statement extract — A/c xxxx4567, April 2026:**

```
Date     Narration                         Withdrawal   Deposit     Balance
01-Apr   Opening balance                                            18,00,000 Cr
09-Apr   CLG INWARD - MYSORE MOTORS                     29,50,000   47,50,000 Cr
18-Apr   CHQ 100234 - DECCAN ELECTRICALS   11,80,000                35,70,000 Cr
22-Apr   NEFT OUT - BOMBAY SWITCHGEAR      14,16,000                21,54,000 Cr
25-Apr   ACH AUTO-DEBIT - LIC INSURANCE     60,000                  20,94,000 Cr
30-Apr   BANK CHARGES + GST                  1,180                  20,92,820 Cr
30-Apr   INT CREDIT - SAVINGS SWEEP                        6,820     20,99,640 Cr
------------------------------------------------------------------------------
         Closing balance as per bank                                20,99,640 Cr
```

Note the mirror convention: a Current A/c is an **asset** in your books (Dr balance) but a **liability** to the bank (Cr balance) — same money, opposite sign.

## Do it — step by step

### Step 1 — Tick off what matches

Line up both sides and mark items appearing in *both*:

| Item | Books | Bank | Status |
|---|---|---|---|
| Opening 18,00,000 | 01-Apr | 01-Apr | Matched |
| Mysore receipt 29,50,000 | 08-Apr | 09-Apr (cleared) | Matched (1-day float) |
| Deccan cheque 100234 11,80,000 | 15-Apr | 18-Apr | Matched |
| Bombay NEFT 14,16,000 | 22-Apr | 22-Apr | Matched |

### Step 2 — Isolate the differences (four types)

1. **Unpresented cheque** — Rent Cheq 100235 Rs 1,77,000: in books 28-Apr, **not yet in bank** (payee hasn't banked it). Reduces book balance but not yet bank.
2. **Deposit in transit** — 30-Apr collections Rs 8,00,000: in books, **not yet credited** by bank.
3. **Bank-only debits not in books** — LIC auto-debit (ACH) Rs 60,000; bank charges + GST Rs 1,180.
4. **Bank-only credit not in books** — sweep interest Rs 6,820.

Types 3 and 4 are **real transactions of NTSPL that the bank knows and the books don't** — they must be *booked*. Types 1 and 2 are **timing differences** — nothing to book, they only appear in the BRS statement.

### Step 3 — Pass the adjusting entries in Tally (Payment / Journal via F5/F7)

**Insurance auto-debit** (this is the monthly prepaid-insurance debit; Rs 60,000 paid, Rs 5,000/mo expense — book the payment against Prepaid Insurance):

```
Dr  Prepaid Insurance (Loans & Advances)   60,000
    Cr  HDFC Current A/c xxxx4567                    60,000
(Being annual LIC premium auto-debited 25-Apr, ACH)
```

**Bank charges (with GST — ITC available):**

```
Dr  Bank Charges                            1,000
Dr  Input CGST                                 90
Dr  Input SGST                                 90
    Cr  HDFC Current A/c xxxx4567                     1,180
(Being bank charges + GST, 30-Apr)
```

**Interest / sweep credit:**

```
Dr  HDFC Current A/c xxxx4567                6,820
    Cr  Interest Received (Indirect Income)          6,820
(Being savings-sweep interest, 30-Apr)
```

### Step 4 — Re-derive the book balance after booking

| | Rs |
|---|---:|
| Book balance before adjustments | 27,77,000 |
| Less: insurance auto-debit | (60,000) |
| Less: bank charges + GST | (1,180) |
| Add: interest credit | 6,820 |
| **Adjusted book balance** | **27,22,640** |

### Step 5 — Reconcile in Tally (F5 – Bank Reconciliation)

Open the HDFC ledger > **F5 (Reconcile)**. Enter the **bank date** against each voucher. Tally then shows: cleared items (bank date filled), and **"Amounts not reflected in bank"** = the unpresented cheque and the deposit in transit. The screen's **"Balance as per bank" should read 20,99,640** once done.

## The deliverable

**Bank Reconciliation Statement — HDFC Current A/c xxxx4567 as at 30-Apr-2026:**

| Particulars | Rs | Rs |
|---|---:|---:|
| Balance as per books (adjusted) | | 27,22,640 |
| **Add:** cheque issued but not yet presented | | |
| — Rent Cheq 100235 (Cyber Estates) | 1,77,000 | |
| | | 1,77,000 |
| | | 28,99,640 |
| **Less:** deposit made but not yet credited | | |
| — April collections deposited 30-Apr | 8,00,000 | |
| | | (8,00,000) |
| **Balance as per bank statement** | | **20,99,640** |

Ties exactly to HDFC's closing of **Rs 20,99,640**. Zero unexplained items.

## How it's checked

- **BRS closing = bank statement closing** to the rupee (20,99,640). The single hard tie-out.
- **Adjusted book balance** (27,22,640) reconciles to bank via only *timing* items — every non-timing difference has been booked, not left in the BRS.
- **Tally F5 "difference"** field reads **0.00**; only the unpresented cheque and deposit-in-transit remain unmarked (no bank date).
- **Follow-up in May:** the two timing items must clear early May; if the Rs 1,77,000 cheque is still outstanding after 3 months it's stale — reverse it.
- **Bank charges GST** captured as ITC and appears in GSTR-2B (small but real credit).

## Common mistakes & red flags

| Mistake | Consequence | Fix |
|---|---|---|
| Forcing a match by editing the book balance | Hides a missing/fraud entry | Never plug — book real items, list timing items |
| Booking bank charges/interest as timing items | BRS never ties; balance drifts each month | They're real — pass journal entries |
| Ignoring an old unpresented cheque | Overstated payable / stale cheque | Reverse cheques unpresented > 3 months |
| Missing an auto-debit (ACH/SI) | Book cash overstated, later shock | Scan statement for ECS/ACH/SI/EMI lines |
| A bank debit you can't identify | Possible fraud or wrong account | Escalate immediately; don't book to "suspense" and move on |

## On the job & in the interview

The "why": the bank statement is the one number in your books an outsider independently confirms. A clean BRS every month is the cheapest fraud-detection control a company has — an unexplained debit is a red flag before it's a loss. It's also the auditor's first request, so a tidy monthly BRS makes year-end painless.

**Q: What's the difference between an item you *book* and an item you list on the BRS?**
A: Items the bank knows but books don't (charges, interest, auto-debits) are **real** — I pass journal entries. Timing differences (unpresented cheques, deposits in transit) are already in books, just not yet in the bank — they only appear on the BRS statement and clear on their own.

**Q: Books show Rs 27,77,000, bank shows Rs 20,99,640. Walk me through the gap.**
A: Book side needs Rs 60,000 insurance + Rs 1,180 charges booked and Rs 6,820 interest added → adjusted Rs 27,22,640. Then add the unpresented rent cheque Rs 1,77,000 and subtract the Rs 8,00,000 deposit in transit → Rs 20,99,640, matching the bank.

**Q: A cheque you issued three months ago is still unpresented. What do you do?**
A: Investigate whether it was lost or the payee never banked it; if genuinely stale (typically > 3 months) I reverse it — Dr Bank, Cr the party — reinstating the liability, and reissue if still payable.
