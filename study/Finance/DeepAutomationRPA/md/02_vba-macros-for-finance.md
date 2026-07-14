# VBA Macros for Finance

## What you'll be able to do
Automate the repetitive month-end grind: record a macro, then read and rewrite its code so it's robust; declare variables, loop over rows and files, make decisions with `If`/`Select Case`, pop message boxes, write your own worksheet functions (UDFs), and handle errors so a macro fails gracefully instead of crashing. You'll build two real tools shown in full: (1) a **format-and-email report** macro that cleans a sheet and sends it via Outlook, and (2) a **two-ledger reconciliation** macro that matches transactions and flags breaks. This is the skill that turns "I spend Friday afternoon reformatting" into "I press a button."

## The essentials
**Where code lives.** Press **Alt+F11** to open the VBA editor (VBE). Code sits in *Modules* (Insert → Module) for general macros, or behind sheets/ThisWorkbook for event code. Save as **.xlsm** (macro-enabled) — .xlsx silently drops macros. Enable Developer tab: File → Options → Customize Ribbon → tick Developer. Set macro security: Trust Center → Macro Settings → "Disable with notification."

**Core syntax.**
| Concept | Example |
|---|---|
| Procedure | `Sub DoThing()` … `End Sub` |
| Variable | `Dim total As Double`, `Dim ws As Worksheet` |
| Object refs | `Set ws = ThisWorkbook.Sheets("Data")` |
| Cell/range | `ws.Range("B2").Value`, `ws.Cells(r, 2)` |
| Loop | `For r = 2 To lastRow … Next r` |
| Condition | `If amt > 0 Then … ElseIf … Else … End If` |
| Message | `MsgBox "Done: " & n & " rows"` |
| Comment | `' this is a comment` |

**Find the last row** (never hard-code): `lastRow = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row`.

**Speed switches.** Wrap heavy macros in `Application.ScreenUpdating = False` and `Application.Calculation = xlCalculationManual`, restore both at the end — often 10x faster.

**UDF** = a `Function` you call from a cell: `=GSTAMT(A2)`. It must return a value and live in a module.

**Error handling.** `On Error GoTo Handler` jumps to a label on failure; `On Error Resume Next` skips (use sparingly). Always restore app settings in the handler.

## Hands-on — step by step
**Step 1 — Record, then read.** Developer → Record Macro, name `CleanFmt`. Bold the header row, autofit columns, add thousands separators to column D, stop recording. Alt+F11 to see the generated code — it's verbose and full of `.Select`. You'll learn by cleaning it: remove `.Select`/`Selection`, reference ranges directly.

**Step 2 — Reconciliation macro (full code).** Two sheets: `Ledger` (our books) and `Bank` (statement), each with `Ref` in col A and `Amount` in col B. Match on Ref, compare amounts, write a status.

```vba
Sub ReconcileLedgers()
    Dim wsL As Worksheet, wsB As Worksheet, wsR As Worksheet
    Dim lastL As Long, lastB As Long, r As Long
    Dim ref As String, ledAmt As Double, bnkAmt As Variant
    Dim matchRow As Variant, n As Long

    On Error GoTo Handler
    Application.ScreenUpdating = False

    Set wsL = ThisWorkbook.Sheets("Ledger")
    Set wsB = ThisWorkbook.Sheets("Bank")
    ' create/refresh a Results sheet
    On Error Resume Next
    Application.DisplayAlerts = False
    ThisWorkbook.Sheets("Recon").Delete
    Application.DisplayAlerts = True
    On Error GoTo Handler
    Set wsR = ThisWorkbook.Sheets.Add
    wsR.Name = "Recon"
    wsR.Range("A1:D1").Value = Array("Ref", "Ledger", "Bank", "Status")

    lastL = wsL.Cells(wsL.Rows.Count, "A").End(xlUp).Row
    n = 1
    For r = 2 To lastL
        ref = Trim(CStr(wsL.Cells(r, "A").Value))
        ledAmt = wsL.Cells(r, "B").Value
        ' look up ref in Bank col A
        matchRow = Application.Match(ref, wsB.Columns("A"), 0)
        n = n + 1
        wsR.Cells(n, 1).Value = ref
        wsR.Cells(n, 2).Value = ledAmt
        If IsError(matchRow) Then
            wsR.Cells(n, 3).Value = "—"
            wsR.Cells(n, 4).Value = "MISSING IN BANK"
        Else
            bnkAmt = wsB.Cells(matchRow, "B").Value
            wsR.Cells(n, 3).Value = bnkAmt
            If Abs(ledAmt - bnkAmt) < 0.01 Then
                wsR.Cells(n, 4).Value = "MATCHED"
            Else
                wsR.Cells(n, 4).Value = "DIFF " & Format(ledAmt - bnkAmt, "#,##0.00")
            End If
        End If
    Next r

    ' colour the breaks red
    Dim lastR As Long
    lastR = wsR.Cells(wsR.Rows.Count, "A").End(xlUp).Row
    For r = 2 To lastR
        If wsR.Cells(r, 4).Value <> "MATCHED" Then
            wsR.Range("A" & r & ":D" & r).Interior.Color = RGB(255, 199, 206)
        End If
    Next r
    wsR.Columns("A:D").AutoFit

    Application.ScreenUpdating = True
    MsgBox "Reconciliation done: " & (lastR - 1) & " items checked.", vbInformation
    Exit Sub

Handler:
    Application.ScreenUpdating = True
    Application.DisplayAlerts = True
    MsgBox "Error " & Err.Number & ": " & Err.Description, vbCritical
End Sub
```

**Step 3 — Format-and-email report (full code).** Uses Outlook (installed on most GCC desktops). Late binding, no reference needed.

```vba
Sub EmailReport()
    Dim ws As Worksheet, olApp As Object, mail As Object
    Dim lastRow As Long, total As Double, r As Long
    On Error GoTo Handler
    Set ws = ThisWorkbook.Sheets("Report")
    ws.Range("A1:D1").Font.Bold = True
    ws.Columns("A:D").AutoFit
    lastRow = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row
    For r = 2 To lastRow
        total = total + ws.Cells(r, 4).Value
    Next r
    Set olApp = CreateObject("Outlook.Application")
    Set mail = olApp.CreateItem(0)   ' 0 = mail item
    mail.To = "controller@company.com"
    mail.Subject = "Daily Report " & Format(Date, "dd-mmm-yyyy")
    mail.Body = "Hi," & vbCrLf & vbCrLf & _
        "Total for today: INR " & Format(total, "#,##0.00") & _
        " across " & (lastRow - 1) & " lines." & vbCrLf & _
        "Regards," & vbCrLf & "Finance Automation"
    mail.Display    ' use .Send to send automatically
    MsgBox "Draft created, total INR " & Format(total, "#,##0"), vbInformation
    Exit Sub
Handler:
    MsgBox "Error " & Err.Number & ": " & Err.Description, vbCritical
End Sub
```

**Step 4 — A UDF.** In a module:
```vba
Function GSTAMT(base As Double, Optional rate As Double = 0.18) As Double
    GSTAMT = base * rate
End Function
```
Use `=GSTAMT(A2)` → 18% GST, or `=GSTAMT(A2, 0.12)` for 12%.

**Step 5 — Run & bind.** Press F5 in VBE to run, or add a button: Developer → Insert → Button (Form Control) → assign `ReconcileLedgers`.

## The output
Running `ReconcileLedgers` produces a fresh **Recon** sheet:

```
Ref     Ledger      Bank        Status
INV001  120,000.00  120,000.00  MATCHED
INV002   80,000.00   79,500.00  DIFF 500.00      ← red
INV003   50,000.00   —          MISSING IN BANK  ← red
```
and a popup "Reconciliation done: 3 items checked." `EmailReport` opens a pre-filled Outlook draft with the day's total. Both are one-click, repeatable, and leave an auditable coloured trail.

## Checks, gotchas & red flags
- **Save as .xlsm.** Saving as .xlsx destroys every macro without warning.
- **Never leave `.Select`/`Activate`** from recorded code — it's slow and breaks when the wrong sheet is active. Reference objects directly.
- **Floating-point:** compare amounts with `Abs(a-b) < 0.01`, never `a = b` — 79.5 stored as 79.4999999 will falsely flag.
- **`Application.Match` returns an error**, not zero, on no-match — test with `IsError`, don't assume.
- **Restore settings in the handler:** if a macro dies with `ScreenUpdating=False`, the screen freezes until you re-run. Always reset in the error path.
- **Auto-send is dangerous:** keep `.Display` (draft) until tested; only switch to `.Send` when the recipient and content are verified. A bad loop can email 500 people.
- **Trim and CStr** keys before matching — trailing spaces and number-vs-text mismatches are the #1 recon false-break.

## Interview drill
**Q: How do you make a VBA macro run faster on 100k rows?**
A: Turn off `ScreenUpdating`, set `Calculation` to manual, and disable `EnableEvents`; read the range into a Variant array (`arr = ws.Range(...).Value`), process in memory, write back in one shot. Avoid `.Select`, and restore all settings at the end and in the error handler.

**Q: Difference between a Sub and a Function in VBA?**
A: A `Sub` performs actions and returns nothing; you run it from a button or F5. A `Function` returns a value and can be called from a worksheet cell as a UDF or from other code. Recon/email are Subs; `GSTAMT` is a Function.

**Q: How do you handle errors so a finance macro doesn't crash mid-run?**
A: `On Error GoTo Handler` at the top, a labelled `Handler:` block at the end that reports `Err.Number`/`Err.Description` and restores `ScreenUpdating`, `Calculation`, and `DisplayAlerts`. Use `On Error Resume Next` only around a single known-safe line (like deleting a sheet that may not exist), then immediately reinstate `On Error GoTo Handler`.

## Learn/practise (free)
Everything here runs in any licensed desktop Excel — no extra tools. Free learning: Excel Macro Mastery (excelmacromastery.com) is the best VBA reference; Chandoo and WiseOwl (YouTube) have full free courses. Microsoft's VBA language reference on Microsoft Learn documents every object/method. Practise by recording a macro for any manual task you do, then opening it and deleting all `.Select` lines until it still works — that single exercise teaches the object model faster than any tutorial. Rebuild the reconciliation above with your own two CSVs to internalise `Match`, `IsError`, and the last-row pattern.
