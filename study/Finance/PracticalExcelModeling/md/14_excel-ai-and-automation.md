# Excel + AI (Copilot) and Automation

## What it is & where it's used

This chapter is about making Excel do the boring 80% *for* you — so you spend your day on judgment, not grunt work. Three tools stack together:

1. **Copilot in Excel** — Microsoft's built-in AI. You type an instruction in plain English ("highlight rows where GST paid is above ₹50,000 and add a variance column") and it writes the formula, formats the range, or drafts an analysis.
2. **Macros / VBA** — recorded or hand-written scripts that replay clicks and keystrokes. This is how you turn a 40-minute month-end formatting ritual into one button press.
3. **LAMBDA** — Excel's native way to build your *own* reusable functions with no code, so a messy nested formula becomes `=NETSALARY(basic, hra)`.

**Who pays for this:** FP&A analysts (monthly MIS packs), audit/statutory teams (repetitive workpapers), tax associates (GST reconciliation, TDS working), accounts-payable teams (invoice cleanup), and anyone who produces the *same* report every month. In an India finance job, "the person who automated the MIS" gets noticed fast — because everyone else is still doing it by hand at 9 PM.

## The gap: why companies want this (and college didn't teach it)

Your MBA taught you *what* a variance analysis means. It never taught you that in a real company you'll rebuild that variance report **12 times a year from a raw SAP/Tally dump that arrives in a slightly different shape each time**. The gap is *repetition at scale*.

College treats Excel as a calculator you use once for an assignment. Employers treat Excel as a **production line** — the same file, refreshed monthly, that six people depend on. Nobody taught you:

- That a recorded macro can eliminate the 30 clicks you do every single close.
- That AI can now write your `SUMIFS` faster than you can remember the argument order.
- That copy-pasting a giant nested formula into 200 cells is a *liability* — one edit and it silently breaks — whereas a named LAMBDA is auditable.

Companies want people who **remove work**, not people who heroically absorb it. That mindset shift is the real gap.

## What "proficient" looks like

A job-ready person can, unaided:

- Use Copilot to generate, explain, and *sanity-check* a formula — and know when the AI is wrong.
- Record a macro for a repetitive formatting/cleanup task, then **open the VBA editor and edit it** (change a range, add a loop, wire it to a button).
- Judge **when to automate vs. when not to** (the "will I do this 3+ times?" test).
- Write a basic LAMBDA and save it as a Named Range so the whole team can use `=GSTSPLIT(...)`.
- Explain the risk: macros can't be undone with Ctrl+Z, so you always work on a copy.

The bar is *not* "expert VBA developer." It's "removes their own repetitive work and can read a macro someone else wrote."

## Hands-on: how to actually do it

### 1. Copilot in Excel

Copilot lives on the **Home tab (rightmost)** in Microsoft 365. Your data must be a proper Table (`Ctrl+T`). Then click Copilot and type instructions:

```
Add a column called "GST Rate" that divides Tax Amount by Taxable Value, formatted as a percentage.
```
```
Show me total Taxable Value by State, sorted highest to lowest.
```
```
Highlight in red every row where Invoice Date is after the GST return due date.
```

Copilot returns the formula and offers to insert it. **Critical habit:** ask it to explain, then verify one row by hand. Example — you asked for a vendor-wise total and Copilot gives:

```excel
=SUMIFS(Invoices[Amount], Invoices[Vendor], [@Vendor], Invoices[FY], "2025-26")
```

Good prompt patterns that work reliably:
- "Write an Excel formula to..." (it returns copy-usable syntax)
- "Explain what this formula does: `=XLOOKUP(...)`"
- "What's wrong with this formula? It returns #N/A"

If you don't have Copilot licensed, the **free fallback** is ChatGPT/Gemini/Claude in a browser: paste your column headers and describe the goal — the formula logic is identical.

### 2. Record and edit a macro

Turn on the Developer tab: **File → Options → Customize Ribbon → tick Developer.**

Record: **Developer → Record Macro → name it `FormatMIS` → do your steps → Stop Recording.**

Say you recorded formatting a report. Open **Developer → Visual Basic (Alt+F11)** to see and edit it:

```vba
Sub FormatMIS()
    ' Recorded: format the month-end MIS sheet
    Columns("A:F").AutoFit
    Range("A1:F1").Font.Bold = True
    Range("A1:F1").Interior.Color = RGB(0, 51, 102)
    Range("A1:F1").Font.Color = RGB(255, 255, 255)
    Columns("C:E").NumberFormat = "#,##0"   ' Indian thousands
    ActiveWindow.FreezePanes = True
End Sub
```

Now *edit* it — add a loop the recorder could never write, e.g. delete blank rows in a Tally export:

```vba
Sub CleanTallyDump()
    Dim i As Long, lastRow As Long
    lastRow = Cells(Rows.Count, "A").End(xlUp).Row
    ' Loop bottom-up so deleting a row doesn't skip the next one
    For i = lastRow To 2 Step -1
        If Trim(Cells(i, "A").Value) = "" Then
            Rows(i).Delete
        End If
    Next i
    MsgBox "Cleanup done. Rows now: " & Cells(Rows.Count, "A").End(xlUp).Row
End Sub
```

Wire it to a button: **Developer → Insert → Button (Form Control) → assign `CleanTallyDump`.** Save the file as **.xlsm** (macro-enabled) or macros vanish.

### 3. When to automate (the decision rule)

| Situation | Automate? |
|---|---|
| One-off, never repeats | No — just do it |
| Same task 3+ times, stable steps | Yes — record a macro |
| Complex logic reused across files | Yes — LAMBDA or VBA |
| Steps change every time / need judgment | No — keep it manual |
| Touches money and can't be checked | Automate, but add a reconciliation check |

Rule of thumb: **if (time saved per run × times per year) > (time to build × 2), automate it.**

### 4. LAMBDA basics

LAMBDA lets you name a formula. Instead of retyping a net-salary calc everywhere:

```excel
=LAMBDA(basic, hra, da, basic + hra + da - (basic*0.12))(50000, 20000, 5000)
```

Make it reusable: **Formulas → Name Manager → New → Name: `NETSALARY`**, Refers to:

```excel
=LAMBDA(basic, hra, da, basic + hra + da - (basic*0.12))
```

Now anyone types `=NETSALARY(50000, 20000, 5000)` → returns **68,000** (after 12% PF on basic). Another practical one — split a GST-inclusive amount into base + tax:

```excel
// Name: GSTBASE  — extract taxable value from an 18% inclusive amount
=LAMBDA(inclusive, rate, inclusive / (1 + rate))
// Usage: =GSTBASE(11800, 0.18)  →  10,000
```

Pair with `MAP` to apply across a range without dragging:

```excel
=MAP(A2:A100, LAMBDA(x, x/(1+0.18)))
```

## Worked example / mini-project

**Goal:** Automate a monthly GST Input Tax Credit (ITC) reconciliation — purchase register vs. GSTR-2B.

**Data (Purchase Register, sheet `PR`):**

| Vendor GSTIN | Invoice No | Taxable (₹) | IGST (₹) |
|---|---|---|---|
| 29ABCDE1234F1Z5 | INV-101 | 100000 | 18000 |
| 27PQRSX5678L1Z2 | INV-102 | 50000 | 9000 |
| 29ABCDE1234F1Z5 | INV-103 | 75000 | 13500 |

**GSTR-2B (sheet `2B`)** has the same columns as downloaded from the portal.

**Step 1 — match with a formula.** In `PR`, add a "Matched in 2B" column:

```excel
=IF(SUMIFS('2B'[IGST], '2B'[Invoice No], [@[Invoice No]], '2B'[Vendor GSTIN], [@[Vendor GSTIN]]) = [@IGST], "Matched", "MISMATCH")
```

**Step 2 — a reusable LAMBDA** for eligible ITC (block credit if unmatched):

```excel
// Name: ELIGIBLEITC
=LAMBDA(igst, status, IF(status="Matched", igst, 0))
// Usage in a column: =ELIGIBLEITC([@IGST], [@[Matched in 2B]])
```

**Step 3 — a macro** to produce the mismatch report every month with one click:

```vba
Sub GSTReconReport()
    Dim ws As Worksheet
    Set ws = Sheets("PR")
    ws.AutoFilterMode = False
    ' Filter to only MISMATCH rows
    ws.Range("A1").AutoFilter Field:=5, Criteria1:="MISMATCH"
    ws.Range("A1").CurrentRegion.Copy
    Sheets.Add.Name = "Mismatch_" & Format(Date, "MMM-YY")
    ActiveSheet.Paste
    Application.CutCopyMode = False
    ws.AutoFilterMode = False
    MsgBox "Mismatch report ready. Follow up with vendors before filing GSTR-3B."
End Sub
```

**Result:** what used to be an afternoon of VLOOKUPs and eyeballing is now — refresh the two sheets, click the button, chase the mismatches. On this data, INV-103 unmatched → ₹13,500 ITC blocked until the vendor uploads it. That number is exactly what a reviewer wants surfaced *before* filing.

## How it's tested

**Interview questions:**
- "Walk me through the last thing you automated in Excel. How much time did it save?"
- "A macro deleted the wrong rows and there's no undo. What do you do / how do you prevent it?" (Answer: always run on a copy; version the file.)
- "When would you *not* automate something?"
- "Difference between a recorded macro and VBA you write yourself?"
- "What is a LAMBDA and why use it over a nested formula?" (Answer: reuse, single point of edit, readability, auditability.)

**Practical tests companies give:**
- **Timed cleanup screen:** "Here's a messy 5,000-row Tally/SAP export. Clean it and produce a vendor-wise summary in 20 minutes." They watch whether you do it by hand or reach for a macro/pivot.
- **"Automate this" case:** given a repetitive monthly report, record a macro live on a shared screen.
- **Formula-from-English:** "Write the formula for X" — increasingly they *allow* Copilot/AI and instead test whether you can **verify** the output.

## Common mistakes & how pros avoid them

| Mistake | How pros avoid it |
|---|---|
| Trusting Copilot/AI output blindly | Verify one row by hand; ask AI to explain its own formula |
| Running a macro on the only copy of live data | Always work on a duplicate file; macros ignore Ctrl+Z |
| Saving as .xlsx (macros silently lost) | Save as **.xlsm** |
| Hard-coding ranges (`A2:A500`) that break next month | Use Tables + structured references, or `End(xlUp)` to find last row |
| Automating a one-off | Apply the "3+ times" rule first |
| Giant nested formula copied 200 times | Convert to a named LAMBDA — one place to fix |
| Emailing .xlsm files (blocked by many gateways) | Zip it, or share via Teams/SharePoint |
| Deleting rows top-down in a loop (skips rows) | Loop **bottom-up** (`For i = lastRow To 2 Step -1`) |

## Learn-it roadmap & resources

**Time to job-ready: 3–4 weeks, ~1 hour/day.**

- **Week 1 — Copilot / AI formulas.** Practice prompting for `SUMIFS`, `XLOOKUP`, conditional formatting. If unlicensed, use free ChatGPT/Gemini. Goal: never get stuck on syntax again.
- **Week 2 — Record & run macros.** Automate your own recurring formatting task. Learn to save .xlsm and assign buttons.
- **Week 3 — Edit VBA.** Learn variables, `For` loops, `If`, `MsgBox`, `Cells`/`Range`, and `End(xlUp)`. Build the GST-recon macro above.
- **Week 4 — LAMBDA + MAP.** Convert your three most-used nested formulas into named functions.

**Resources (mostly free):**
- Microsoft Learn — "Automate tasks with the Macro Recorder" and "LAMBDA function" docs.
- ExcelIsFun and Leila Gharani (YouTube) — best free VBA and LAMBDA channels.
- Chandoo.org — India-friendly Excel automation examples.
- **Certification:** Microsoft Office Specialist (MOS): Excel Expert (MO-201) validates macros/LAMBDA on a CV; the free skills matter more than the badge in India.

## Quick-reference

| Task | How |
|---|---|
| Open Copilot | Home tab → Copilot (M365) |
| Turn on macros | File → Options → Customize Ribbon → Developer |
| Record macro | Developer → Record Macro |
| Open code editor | `Alt+F11` |
| Save with macros | Save as **.xlsm** |
| Find last row (VBA) | `Cells(Rows.Count,"A").End(xlUp).Row` |
| Loop that deletes rows | `For i = lastRow To 2 Step -1` |
| Message box | `MsgBox "text"` |
| Name a LAMBDA | Formulas → Name Manager → New |
| LAMBDA syntax | `=LAMBDA(a, b, a+b)(1, 2)` |
| Apply over a range | `=MAP(range, LAMBDA(x, x*1.18))` |
| GST base from inclusive | `=inclusive/(1+rate)` |
| Automate decision | (time saved/run × runs/yr) > (build time × 2) |

**Golden rules:** verify AI output, work on a copy (no undo for macros), save as .xlsm, and only automate what you'll repeat 3+ times.
