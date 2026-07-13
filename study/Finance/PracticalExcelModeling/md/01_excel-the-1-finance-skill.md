# Excel: the #1 finance skill and the gap it exposes

## What it is & where it's used

Excel is the universal spreadsheet — a grid of cells that becomes a calculator, a database, a reporting tool, and a modeling engine depending on how you use it. In finance it is not "one tool among many"; it is the default surface where numbers get worked. SAP, Oracle, Tally, Zoho Books, and every bank portal ultimately export to Excel because that's where humans reason about the data.

Every finance role touches it, but differently:

| Role | What they do in Excel daily |
|---|---|
| Accounts / AP-AR | Reconciliations, ageing schedules, ledger dumps, GST 2A/2B matching |
| Audit / assurance | Sampling, variance testing, tie-outs, TB-to-FS mapping |
| FP&A / analyst | Budgets, variance decks, rolling forecasts, KPI trackers |
| Investment banking / PE | 3-statement models, DCF, LBO, comps |
| Taxation | Computation sheets, TDS workings, GST returns prep, 26AS reconciliation |
| Treasury | Cash flow forecasting, interest schedules, bank position sheets |

If you can only bring one skill to a finance desk on day one, it is Excel. Everything else — Tally, SQL, Power BI — sits around it.

## The gap: why companies want this (and college didn't teach it)

An MBA teaches you *what* NPV, WACC, and working capital mean. A CA course teaches you *what* the standards require. Neither teaches you to **build the sheet that a manager trusts at 11 pm before a board meeting.** That build skill is the gap.

Concretely, college leaves you unable to:

- Pull the right value from a 40,000-row ledger dump **without scrolling** (lookups, not eyeballing).
- Build a formula that **doesn't break** when a row is inserted (absolute vs relative references, structured tables).
- Make one input change and have the **whole model recalculate correctly** (linked, not hardcoded).
- Produce output a reviewer can **audit in 30 seconds** (colour conventions, no buried constants).
- Do all of the above **fast, keyboard-only, under time pressure.**

Employers pay for the person who receives a messy export and returns a clean, correct, self-checking answer unaided. That's the difference between "I've used Excel" and "job-ready Excel."

## What "proficient" looks like

The concrete bar employers test for — a proficient person can, unaided:

1. **Navigate and clean** a raw export: remove duplicates, `TRIM`/`CLEAN` text, split columns, fix date-as-text.
2. **Look up and match** across sheets with `XLOOKUP`/`INDEX-MATCH`, and multi-criteria with `SUMIFS`.
3. **Build logic** with nested `IF`, `IFS`, `AND`/`OR`, and error-trap with `IFERROR`.
4. **Aggregate** thousands of rows via PivotTables in under two minutes.
5. **Model** with a clean inputs → calc → output structure and no hardcoded numbers inside formulas.
6. **Work keyboard-first** — `Ctrl+Arrow`, `Ctrl+Shift+Arrow`, `Alt+=`, `F4`, `Ctrl+;`.
7. **Self-check** — build a control total that must equal zero.

A rough ladder: Basic (formulas, formatting), Intermediate (lookups, pivots, charts — this is the *hiring minimum* for most accounts/analyst roles), Advanced (dynamic arrays, `LET`/`LAMBDA`, full 3-statement models).

## Hands-on: how to actually do it

**Lookups — use XLOOKUP, fall back to INDEX-MATCH.**

```excel
=XLOOKUP(A2, Vendors[GSTIN], Vendors[VendorName], "Not found")

=INDEX(Vendors[VendorName], MATCH(A2, Vendors[GSTIN], 0))
```

`XLOOKUP` looks up `A2` in the GSTIN column and returns the vendor name; the 4th argument replaces the ugly `#N/A`. `INDEX-MATCH` does the same and works in every Excel version.

**Multi-criteria sum — SUMIFS is the workhorse of accounts.**

```excel
=SUMIFS(Ledger[Amount], Ledger[Party], "Acme Ltd", Ledger[Type], "Sales", Ledger[Date], ">="&DATE(2025,4,1))
```

Sum of all Acme sales from 1-Apr-2025 onward. `COUNTIFS` and `AVERAGEIFS` follow the same pattern.

**Conditional logic with error trapping.**

```excel
=IFERROR(IF(D2>1000000, D2*0.1, D2*0.05), 0)
```

**GST split from a tax-inclusive amount (intra-state, 18%).**

```excel
=ROUND(A2/1.18*0.09, 2)   // CGST
=ROUND(A2/1.18*0.09, 2)   // SGST
```

**Data cleaning that saves reconciliations.**

```excel
=TRIM(CLEAN(A2))                 // strip stray spaces + non-printing chars
=TEXT(A2,"0000000000")           // pad GSTIN/PAN keys before matching
=DATEVALUE(A2)                   // convert text-dates so they compare correctly
```

**Dynamic arrays (Excel 365) — filter without a pivot.**

```excel
=FILTER(Ledger, Ledger[Balance]>0)
=SORT(UNIQUE(Ledger[Party]))
```

**The two keyboard reflexes that separate pros from beginners:** `F4` to toggle `$` anchors (`A1` → `$A$1`), and `Alt + =` to auto-sum a column instantly.

## Worked example / mini-project: GST 2B input-credit reconciliation

You have two sheets: **Books** (purchases you recorded) and **GSTR-2B** (what the portal says vendors filed). You must find invoices where credit is at risk.

**Books** (columns A–D): Invoice No, GSTIN, Taxable Value, GST in books.
**2B** (columns A–D): Invoice No, GSTIN, Taxable Value, GST as per 2B.

Step 1 — build a match key in both sheets (E2, filled down):

```excel
=TRIM(B2)&"|"&TRIM(A2)
```

Step 2 — in **Books**, pull the 2B tax against each invoice:

```excel
=XLOOKUP(E2, '2B'!$E$2:$E$5000, '2B'!$D$2:$D$5000, "MISSING IN 2B")
```

Step 3 — flag the difference (G2):

```excel
=IF(F2="MISSING IN 2B","BLOCK CREDIT", IF(ROUND(D2-F2,0)=0,"OK","MISMATCH ₹"&TEXT(D2-F2,"0")))
```

Sample result:

| Invoice | GSTIN | GST books | GST 2B | Flag |
|---|---|---|---|---|
| INV-101 | 29AABCU... | 18,000 | 18,000 | OK |
| INV-102 | 27AAAC...| 9,000 | 0 | MISSING IN 2B → BLOCK CREDIT |
| INV-103 | 24AACC... | 12,600 | 11,700 | MISMATCH ₹900 |

Step 4 — the control total (single cell, must show a real number, not error):

```excel
=SUMIF(G:G,"BLOCK CREDIT",D:D)   // total ITC you cannot claim this month
```

That last cell is what a manager actually reads. You've turned two raw dumps into a decision: how much input credit to reverse. This is exactly the kind of task a fresher gets in week one at a tax or audit firm.

## How it's tested

**In the interview (verbal):**
- "Difference between `VLOOKUP` and `INDEX-MATCH`? Why might `XLOOKUP` be better?"
- "What does `F4` do while editing a formula?" (Expect: toggles absolute/relative reference.)
- "How would you find duplicate invoice numbers?" (Answer: `COUNTIF(range,cell)>1`, or Remove Duplicates, or a pivot.)
- "A `SUMIFS` returns 0 but you expect a number — how do you debug?" (Text vs number, trailing spaces, date-as-text.)

**The practical test (this is where offers are decided):** a **timed 30–60 minute Excel test.** Typical brief:

> "Here's a 5,000-row sales export. Build a summary by region and month, flag any order above ₹5 lakh, look up the salesperson from the second tab, and give me total revenue with a control check. You have 40 minutes."

They watch (or infer from your file): Did you use lookups or copy-paste? Did you hardcode? Does it break if a row is added? Is there a self-check? For accounting roles the case is often **"reconcile these two ledgers"** or **"close these books and produce a TB."** Speed and correctness both count — and using the keyboard, not the mouse, visibly signals fluency.

## Common mistakes & how pros avoid them

| Mistake | Why it hurts | Pro habit |
|---|---|---|
| Hardcoding numbers inside formulas (`=B2*0.18`) | Nobody can find or change the assumption | Put 18% in a labelled input cell; reference it |
| Manual `VLOOKUP` with a counted column index | Breaks the instant a column is inserted | `XLOOKUP` / `INDEX-MATCH` on named columns |
| Forgetting `$` anchors when copying | Formula drifts, silent wrong answers | Hit `F4`; know what to lock |
| No error trapping | `#N/A` cascades and breaks totals | Wrap in `IFERROR` |
| No control total | Errors ship undetected | One cell that must equal zero |
| Mixing inputs, calcs, outputs on one sheet | Un-auditable | Blue = input, black = formula; separate zones |
| Merged cells everywhere | Kills sorting, pivots, references | "Center Across Selection" instead |
| Volatile mega-formulas nobody can read | Un-reviewable, un-maintainable | Break into steps or use `LET` to name parts |

The colour convention (blue font for hardcoded inputs, black for formulas) is a genuine industry standard — reviewers scan for blue to find every assumption in seconds.

## Learn-it roadmap & resources

**Realistic time-to-proficiency** (from an MBA/CA base, practising ~1 hr/day):

| Level | Time | You can then... |
|---|---|---|
| Basic → Intermediate | 3–4 weeks | Lookups, `SUMIFS`, pivots, clean charts — clears most job screens |
| Intermediate → job-ready | 6–8 weeks | Handle real dumps, reconcile unaided, pass timed tests |
| Advanced | 3–4 months | Dynamic arrays, `LET`/`LAMBDA`, full 3-statement models |

**Resources:**
- *Free:* Microsoft's own Excel training (support.microsoft.com), ExcelJet's formula reference, Chandoo.org, Kenji Explains and Leila Gharani on YouTube. For India-specific GST/TDS sheets, the CBIC and income-tax portals give real return formats to rebuild.
- *Paid / certification:* Microsoft Office Specialist (MOS): Excel Associate/Expert — the globally-recognised cert; Corporate Finance Institute (CFI) Excel courses; Wall Street Prep / BIWS for modeling. In India, an MOS Excel Expert badge on a resume meaningfully de-risks you to a hiring manager.
- *Practice, not watching:* download a bank statement and a ledger, and force yourself to reconcile them keyboard-only. Repetition on real data beats any course.

Turn off the mouse for an hour a day. That single constraint builds the fluency employers actually test.

## Quick-reference

| Task | Formula / shortcut |
|---|---|
| Lookup (modern) | `=XLOOKUP(val, lookup_col, return_col, "NA")` |
| Lookup (any version) | `=INDEX(ret, MATCH(val, look, 0))` |
| Multi-criteria sum | `=SUMIFS(sum, c1, k1, c2, k2)` |
| Count with condition | `=COUNTIFS(range, criteria)` |
| Duplicate check | `=COUNTIF(A:A, A2)>1` |
| Error trap | `=IFERROR(formula, 0)` |
| Clean text key | `=TRIM(CLEAN(A2))` |
| Text-date → date | `=DATEVALUE(A2)` |
| GST 18% split | `=ROUND(amt/1.18*0.09,2)` each for CGST & SGST |
| Filter (365) | `=FILTER(tbl, tbl[col]>0)` |
| Unique list | `=SORT(UNIQUE(range))` |
| Auto-sum | `Alt + =` |
| Toggle absolute ref | `F4` |
| Today's date (static) | `Ctrl + ;` |
| Jump to data edge | `Ctrl + Arrow` |
| Select to edge | `Ctrl + Shift + Arrow` |
| Remove duplicates | Data tab → Remove Duplicates |
| PivotTable | `Alt, N, V` → drag fields |

**GST rate reminder (intra-state):** total rate splits equally into CGST + SGST (e.g. 18% = 9% + 9%); inter-state is a single IGST at the full rate. Colour code: **blue = input, black = formula.** Always end with one **control cell that must equal zero.**
