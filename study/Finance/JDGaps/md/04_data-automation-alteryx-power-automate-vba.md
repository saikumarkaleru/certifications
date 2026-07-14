# Automation Beyond Power Query: Alteryx, Power Automate, VBA

## The gap

You can already shape data in Power Query, model in Python, and build Power BI dashboards. But a large slice of 2026 finance JDs — especially at asset managers, GCCs and Big-4 managed services — still runs on three tools your bundles never touched: **Alteryx** (drag-and-drop ETL for analysts who don't code), **Microsoft Power Automate** (workflow/approval/email robots), and **VBA** (the Excel macro language that refuses to die). They are named explicitly, together, on real postings — and none of your six bundles teach them.

## Why companies ask for it

> **Real posting (Franklin Templeton, Fund Accounting / FA):** "VBA, Power Automate, Power BI, Alteryx."

That one line names all three. Franklin Templeton, Accenture, Genpact and most fund-admin / FP&A shared-service teams list them because their existing process estate is Excel-and-email; they want people who can *retrofit* automation onto legacy workflows without a full data-engineering project. Roles: **Fund Accounting, FP&A analysts, R2R/RTR teams, MIS analysts, financial-reporting associates, RPA/finance-transformation** roles in GCCs.

Why not just Python? Governance. In a bank or fund admin, IT won't let you run arbitrary Python against the GL. Alteryx and Power Automate are *sanctioned, auditable, licensed* platforms with lineage and logging — that's the whole reason they get paid for.

## What "proficient" looks like

The employer tests whether you can:

- Build an **Alteryx workflow** end-to-end: pull two files, clean, join, aggregate, and output — and explain each tool container.
- Stand up a **Power Automate flow** that triggers on an email/file/schedule, applies a condition, and sends an approval or a report.
- **Record, then edit** a VBA macro — add a loop, a variable, an `If`, and error handling — not just hit record.
- Say **when to use which** (the decision matters more than syntax).

## How to actually learn/do it

### Alteryx Designer

The whole product is a left-hand **tool palette** you drag onto a canvas and wire together left-to-right. Learn these categories:

| Palette | Key tools | What it does |
|---|---|---|
| **In/Out** | Input Data, Output Data, Browse | Read CSV/Excel/DB, write result, preview mid-stream |
| **Preparation** | Select, Filter, Formula, Sort, Sample, Data Cleansing | Pick/rename columns, `WHERE`, new calculated fields |
| **Join** | Join, Union, Join Multiple, Find Replace | `VLOOKUP`/merge on keys, stack tables |
| **Transform** | Summarize, Cross Tab, Transpose | Group-by/pivot/unpivot |
| **Parse** | Text to Columns, RegEx, DateTime | Split and reformat |

**Worked example — a 2-minute recon:** Input `GL.xlsx` → Input `Bank.csv` → **Select** to standardise the amount/date types on each → **Join** on `TxnID` → the **L and R (unmatched) outputs** are your exceptions, the **J (inner)** output is matched → **Summarize** the exceptions by amount → **Output Data** to `breaks.xlsx`. The unmatched anchors of a Join tool ARE the reconciliation. Wrap it once and it re-runs monthly in one click.

**Free practice:** Alteryx offers a free **14-day Designer trial** and a permanent **free "Designer Cloud" / Community edition** plus the **Weekly Challenge** archive and free "Foundational Micro-Credential" on the Alteryx Community — genuinely the fastest way to a line on the resume.

### Microsoft Power Automate

A **flow** = **Trigger → Action(s)**, built in a browser at make.powerautomate.com. It's almost certainly already in your Microsoft 365 licence.

- **Trigger** types: *automated* (When a new email arrives / a file is created in SharePoint), *scheduled* (Recurrence, e.g. every weekday 7 am), *instant* (button/manual).
- **Core actions**: Condition (If/Yes-No branch), Apply to each (loop), Get items (SharePoint/Excel table), Send an email (V2), Start and wait for an approval, Create file, HTTP.

**Worked example — invoice approval:** Trigger *When a new email arrives* with attachment → **Condition** subject contains "Invoice" → **Start and wait for an approval** (Approve/Reject) sent to the manager → on Approve, **Create file** in the "Approved" SharePoint folder and **Send an email** to AP. Zero code. This is the classic FP&A/AP demo.

**Free practice:** Any personal Microsoft account gets Power Automate free-tier; Microsoft Learn has free guided modules and there's a free desktop RPA client (**Power Automate for desktop**) bundled with Windows 11 for clicking legacy apps.

### VBA

Open the editor with **Alt + F11**. To learn fast: **Developer tab → Record Macro**, do the task once, stop, then **read and edit** the generated code — that's how everyone actually learns VBA.

**A real finance macro — loop through sheets and PDF each cost-centre's MIS:**

```vba
Sub ExportCostCentres()
    Dim ws As Worksheet
    Dim path As String
    path = ThisWorkbook.Path & "\MIS\"
    For Each ws In ThisWorkbook.Worksheets          ' loop
        If Left(ws.Name, 2) = "CC" Then             ' If condition
            ws.ExportAsFixedFormat Type:=xlTypePDF, _
                Filename:=path & ws.Name & ".pdf"
        End If
    Next ws
    MsgBox "Done"
End Sub
```

That single macro shows the four things interviewers probe: a **variable** (`Dim`), a **loop** (`For Each`), an **`If`**, and a real action. Add `On Error Resume Next` for basic error handling. **Free practice:** any Excel install — no licence, no internet.

### When to use which

| Need | Reach for |
|---|---|
| Repeatable multi-file **ETL / recon / blending**, no code, auditable | **Alteryx** |
| **Cross-app workflow** — email, approvals, SharePoint, Teams, scheduled reports | **Power Automate** |
| Manipulate **inside one workbook**, format, loop cells, quick-and-dirty | **VBA** |
| Heavy transforms already loading a model | **Power Query** (you have this) |
| Data science / large data / ML | **Python** (you have this) |

Rule of thumb: *data in files → Alteryx; actions across apps → Power Automate; things inside Excel → VBA.*

## How it shows up in interviews

**Q: "You get two files — our GL export and the bank statement — every morning. Walk me through automating the reconciliation without writing Python."**
A: "In Alteryx: two Input tools, a Select on each to normalise date and amount types, then a Join on the transaction key. The inner output is matched; the two unmatched anchors are my breaks, which I Summarize by amount and Output to an exceptions file. I'd schedule it, or hand it off in Power Automate on a 7 am recurrence that emails the exceptions to the team."

**Q: "Difference between Power Automate and VBA — when would you pick each?"**
A: "VBA lives inside one Excel workbook and is great for formatting, looping cells, or generating PDFs locally, but it can't reach email approvals or SharePoint cleanly and needs the file open. Power Automate is cloud, event-driven and cross-app — approvals, notifications, scheduled report distribution — with logging and governance IT accepts. I'd use VBA for in-workbook work and Power Automate for anything that crosses apps."

**Q: "How do you learn a macro if you don't know the syntax?"**
A: "Record it first, then open Alt+F11 and refactor the recorded code — replace absolute references with variables, wrap repeated steps in a For loop, add an If and `On Error` handling. Recording teaches you the object model faster than any tutorial."

## ATS keywords to add

Alteryx, Alteryx Designer, workflow automation, data blending, ETL, Power Automate, Microsoft Power Automate, Power Automate for desktop, RPA, robotic process automation, approval workflows, VBA, Excel macros, macro automation, process automation, finance transformation, automated reconciliation, scheduled reporting, Power Automate flows, Alteryx Core Micro-Credential
