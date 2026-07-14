# Automation Portfolio & Interview Drills + Cheat-Sheet

## What you'll be able to do

By the end of this chapter you can package everything from this guide into a single, showable automation portfolio project — a real finance process, automated end-to-end, documented so a hiring manager grasps the value in 30 seconds and a technical interviewer can inspect the code. You will be able to answer the standard "how would you automate this finance task?" question with a structured, credible walkthrough, defend your tool choices, and reel off a one-page cheat-sheet of the automation stack — which tool for which job — plus the Excel/VBA/Power Query shortcuts and functions that come up in live tests. This is the chapter that turns "I know some automation" into "here is the thing I built, here is the time it saves, here is the code."

## The essentials

A portfolio project that lands interviews has five properties: it solves a **recognisable finance pain** (recon, MIS, AP, GST), it is **end-to-end** (input → process → output → notify), it shows a **before/after time saving** in numbers, it is **documented** (README + a 60-second demo GIF/video), and the **code is public** (GitHub) and clean. Interviewers don't reward cleverness; they reward *judgement* — did you pick the right tool, did you handle errors, can it be audited.

**The reference project — "Daily MIS & Bank Recon Pack":** it ingests a bank CSV and a ledger extract, reconciles them (Power Query or Python), refreshes a Power BI/Excel MIS dashboard, flags breaks, and e-mails a PDF pack to the finance head every morning. It legitimately touches every tool an analyst is hired for. You claim a real number: "manual = 45 min/day; automated = under 2 min; ~15 hours/month saved."

**The "how would you automate X?" answer framework — always use these six beats:**

1. **Clarify** the process, inputs, outputs, frequency, volume.
2. **Map** the as-is steps (a swimlane in words).
3. **Pick the tool** with the decision rule (below) and justify it.
4. **Handle exceptions** — what breaks, how you catch it, maker-checker.
5. **Govern** — credentials, audit log, service account, versioning.
6. **Measure** — time saved, error reduction, and what you'd automate next.

## Hands-on — step by step

**Build the portfolio repo:**

1. **Create the GitHub repo** `finance-automation-recon`. Structure:
   ```
   /data      sample_bank.csv, sample_ledger.xlsx (fake data — never real client data)
   /pq        recon.pq  (Power Query M)
   /python    recon.py  (pandas alternative)
   /uipath    DailyRecon.xaml
   /docs      demo.gif, dashboard.png
   README.md
   ```
2. **Write the Power Query version.** In Excel: Data → Get Data → From CSV (bank), From Workbook (ledger). Merge the two queries on `Ref` (Left Outer). Add a custom column `Status = if [BookAmount] = [Amount] then "MATCHED" else "BREAK"`. Close & Load to a table. This is your no-code, auditable core.
3. **Add the Python version** (shows range):
   ```python
   import pandas as pd
   bank = pd.read_csv("data/sample_bank.csv")
   led  = pd.read_excel("data/sample_ledger.xlsx")
   m = bank.merge(led, on="Ref", how="left", indicator=True)
   m["Status"] = (m["Amount"] == m["BookAmount"]).map({True:"MATCHED", False:"BREAK"})
   breaks = m[(m._merge=="left_only") | (m.Status=="BREAK")]
   breaks.to_csv("out/breaks.csv", index=False)
   print(f"{len(m)-len(breaks)} matched, {len(breaks)} breaks")
   ```
4. **Add a dashboard.** A Power BI or Excel PivotChart: matched vs breaks by day, total value reconciled, top break reasons. Screenshot it to `/docs/dashboard.png`.
5. **Record a demo.** Screen-record the run (input file appears → click refresh → dashboard updates → email fires). Export a 30–60s GIF to `/docs/demo.gif` and embed it at the top of the README.
6. **Write the README** with: one-line pitch, the before/after time table, an architecture diagram (input→Power Query→dashboard→email), "tools used", "how to run", and "what I'd do next (queue-based unattended bot, API pull)".
7. **Commit clean history** — small, sensible commits; a `.gitignore` for temp files; no credentials, no real data.

## The output

The README top section a recruiter sees:

```markdown
# Daily MIS & Bank Recon Automation
Reconciles the bank statement against the ledger, refreshes the MIS
dashboard, and emails a break-report pack every morning — hands-free.

| Metric        | Manual   | Automated | Saving        |
|---------------|----------|-----------|---------------|
| Time / day    | 45 min   | < 2 min   | ~43 min       |
| Errors        | ~3/week  | 0         | eliminated    |
| Time / month  | 15 hrs   | 40 min    | ~14 hrs saved |

Tools: Power Query · Python (pandas) · Power BI · UiPath (unattended) · Outlook
![demo](docs/demo.gif)
```

Deliverable = a public repo with three working implementations, a dashboard image, a demo GIF, and a quantified value story — the single strongest thing you can put on a finance-analyst CV under "Projects".

## Checks, gotchas & red flags

- **Never commit real or client data / credentials.** Use obviously fake names and amounts. A leaked key in git history is a hard interview fail — scrub with `git filter-repo` if it happens.
- **The number must be defensible.** If you claim "15 hours saved", be ready to explain the arithmetic. Vague "huge time savings" reads as fluff.
- **Show error handling**, not just the happy path — a reviewer looks for the break/exception branch. A recon that only handles perfect matches is a toy.
- **Don't over-engineer.** A four-tool project is impressive *only if each tool is justified*. If Power Query alone solves it, saying so shows better judgement than bolting on a bot.
- **Broken demo GIF / dead repo** undoes everything. Test the "how to run" steps on a clean machine.
- **README-less repo** = invisible work. If it isn't explained, it doesn't count.

## Interview drill

**Q1. "Walk me through automating the monthly GST reconciliation (GSTR-2B vs purchase register)."**
Clarify: inputs are the 2B JSON/Excel from the GST portal and the purchase register from Tally; monthly; a few thousand lines. Map: download 2B, match on GSTIN + invoice no + taxable value, classify matched / mismatch / missing-in-books / missing-in-2B. Tool: Power Query for the match (auditable, no-code, finance-owned) with a Python fallback for volume; RPA only for the portal download since there's no clean API. Exceptions: rounding tolerance of ₹1, fuzzy invoice numbers flagged for human review — maker-checker before any ITC is claimed. Govern: no ITC auto-claimed, full log. Measure: cuts a two-day manual match to an hour, and catches mismatches that risk ITC reversal.

**Q2. "You have Excel, VBA, Power Query, Python and UiPath. A vendor emails an invoice PDF daily that must be keyed into SAP. Pick your stack."**
Extraction: the PDF has no API, so either UiPath Document Understanding or a Python parser (pdfplumber/camelot) to pull header + line items. Entry into SAP: SAP GUI has scripting, so UiPath (or the SAP GUI Scripting API) drives the transaction reliably. So: Python/UiPath for extract, UiPath unattended for SAP entry, with a validation table check before posting. VBA/Power Query don't fit — they can't read the PDF or drive SAP well. I'd add a maker-checker park-and-post so a human releases the document.

**Q3. "What makes an automation *maintainable* six months later?"**
Clear naming and comments, externalised config (paths, emails, thresholds in one place, not hard-coded), robust selectors/keys instead of positions, error handling with logging, version control with a README, and no embedded credentials. Plus a documented owner — automation that only one person understands is a liability when they leave.

## Learn/practise (free) + Cheat-Sheet

**Tool decision cheat-sheet:**

| Job | Reach for | Why |
|---|---|---|
| Data cleanup, joins, refreshable ETL in Excel | **Power Query** | No-code, auditable, repeatable on refresh |
| Excel event/UI automation, custom functions | **VBA / Office Scripts** | Lives in the workbook, no extra licence |
| Heavy data, stats, APIs, ML, big files | **Python (pandas)** | Scales past Excel, huge library ecosystem |
| Reporting/dashboards from many sources | **Power BI** | Model + visuals + scheduled refresh |
| GUI-only legacy app, no API, repetitive | **RPA (UiPath)** | Mimics the human across apps |
| App has a clean API | **API integration** | Robust — prefer over RPA every time |
| Cross-app workflow glue, cloud connectors | **Power Automate** | Trigger-based, 100s of connectors |

**Excel / Power Query / VBA quick-reference:**

- Excel functions: `XLOOKUP`, `SUMIFS`, `INDEX/MATCH`, `LET`, `LAMBDA`, `FILTER`, `UNIQUE`, `TEXTSPLIT`, `IFERROR`.
- Shortcuts: `Ctrl+T` (table), `Ctrl+Shift+L` (filter), `Alt+=` (AutoSum), `Ctrl+Shift+Enter` (legacy array), `F4` (lock `$` reference / repeat), `Ctrl+G→Alt+S` (Go To Special), `Alt+A+M` (remove duplicates).
- Power Query M essentials: `Table.Merge`, `Table.NestedJoin`, `Table.AddColumn`, `Table.Group`, `Table.SelectRows`, `Text.Trim`, `each`, `[Column]` referencing; parameters for file paths.
- VBA essentials: `Range`, `Cells`, `For Each`, `Workbooks.Open`, `Application.ScreenUpdating = False`, `On Error Resume Next`/`GoTo`, `Dim x As Long`.

**Free practice:** UiPath Community + Academy; Microsoft Learn (Power Query, Power BI, Power Automate); Kaggle for pandas datasets; the RBI/NSE public data for realistic finance files. Rehearsal loop: take any manual task you did this week, time it, automate it with the *simplest* tool that works, log the saving, push to GitHub. Ten such micro-projects, and the portfolio writes itself.
