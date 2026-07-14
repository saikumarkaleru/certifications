# Advanced Power Query & Power Automate

## What you'll be able to do
Build a *refreshable* data pipeline instead of copy-pasting. In Power Query you'll go past "remove columns": merge and append queries, add custom columns in M, parameterise a file path or period, unpivot a crosstab into a tidy table, and group/aggregate — all as steps that re-run at the click of Refresh. Then in Power Automate (cloud flows) you'll schedule a report refresh, route an approval, and trigger an email/Teams message on an event using connectors. The worked example: a monthly **branch sales consolidation** that pulls many files, cleans them, and fires an approval + Teams alert when a branch is over budget.

## The essentials
**Power Query (Get & Transform)** lives in Excel (Data → Get Data) and Power BI. Every click writes a step in the **Applied Steps** pane; the underlying language is **M** (case-sensitive, functional). Queries *load* to a table, the Data Model, or "connection only."

Key operations:
| Task | Where | Note |
|---|---|---|
| **Append** | Home → Append Queries | stack tables with same columns (Jan+Feb+Mar) |
| **Merge** | Home → Merge Queries | join on key(s); Left Outer / Inner / Anti |
| **Custom column** | Add Column → Custom | write an M expression |
| **Unpivot** | Transform → Unpivot Columns | turn month-columns into rows |
| **Group By** | Transform → Group By | sum/count per key |
| **Parameters** | Manage Parameters | reusable inputs (folder, period) |

**Merge join kinds:** Left Outer (all left + matches), Inner (only matches), **Left Anti** (rows in left with *no* match — perfect for "unmatched/missing" recon). 

**M basics.** A query is `let … in`: `let Source = …, Step2 = Table.SelectRows(Source, each [Amount] > 0) in Step2`. `each` is shorthand for a function; `[Column]` references a field. Custom column example: `if [Region]="West" then [Sales]*1.1 else [Sales]`.

**From Folder** (Data → Get Data → From File → From Folder) reads *every* file in a folder and combines them — drop next month's file in and Refresh; no rebuild.

**Power Automate** (flow.microsoft.com) runs *cloud flows*. A flow = **trigger** + **actions**. 
- Triggers: *Recurrence* (scheduled), *When a new email arrives*, *When a file is created* (SharePoint/OneDrive), *When an item is created* (Lists), manual button.
- Actions via **connectors**: Outlook/Exchange, Teams, SharePoint, Excel Online (Business), Approvals, HTTP, and the "Dataflow/Power BI refresh" connectors.
- **Approvals**: "Start and wait for an approval" pauses the flow until someone clicks Approve/Reject; you branch on the outcome.
- Dynamic content passes data between steps; **Condition** and **Apply to each** give logic and loops.

Licensing note: Power Query is free (built into Excel/Power BI Desktop). Power Automate *cloud flows* need a Microsoft 365 work/school account; the standard connectors (Outlook, Teams, SharePoint, Excel Online, Approvals) are included in most M365 business plans. Premium connectors (SQL Server on-prem via gateway, Dataverse, HTTP) may need a per-user/per-flow plan.

## Hands-on — step by step
**Part A — Consolidate branch files in Power Query.**
1. Put `Delhi.xlsx`, `Mumbai.xlsx`, `Chennai.xlsx` in one folder, each with a sheet `Sales` shaped as a crosstab: `Product | Jan | Feb | Mar`.
2. Excel → Data → Get Data → From File → **From Folder** → pick the folder → **Combine & Transform**. Power Query shows a sample; it auto-generates a function that opens each file's `Sales` sheet and appends them, adding a `Source.Name` column.
3. **Clean the branch name:** Add Column → Custom Column, name `Branch`:
```
Text.BeforeDelimiter([Source.Name], ".")
```
4. **Unpivot months:** select `Jan, Feb, Mar` → Transform → **Unpivot Columns**. Rename `Attribute`→`Month`, `Value`→`Sales`. You now have tidy rows: Branch, Product, Month, Sales.
5. **Parameter for period.** Home → Manage Parameters → New, name `pPeriod`, type Text, current value `Mar`. Then Home → Keep Rows / filter `Month` = `pPeriod`, but change the filter step's formula to reference the parameter:
```
= Table.SelectRows(#"Renamed", each [Month] = pPeriod)
```
Change `pPeriod` once and every downstream number moves to a different month.
6. **Merge a budget.** Load a `Budget` query (Branch, Month, Budget). Home → **Merge Queries** → match on Branch *and* Month (Ctrl-click both) → Left Outer → expand `Budget`.
7. **Variance custom column** `Variance`: `= [Sales] - [Budget]`, and `OverBudget`: `if [Sales] > [Budget] then "YES" else "NO"`.
8. **Group By** (a second query, reference the cleaned one): Transform → Group By → group on Branch → New column `TotalSales` = Sum of `Sales`.
9. Home → **Close & Load To** → Table (or "Only Create Connection" + Add to Data Model). Next month: drop the new file in the folder, hit **Refresh All** — done.

**Part B — Power Automate flow: refresh + approval + alert.**
1. Save the workbook to **SharePoint/OneDrive for Business** (cloud flows can only reach cloud files) as a Table named `tblConsol`.
2. Go to flow.microsoft.com → **Create → Scheduled cloud flow**. Name "Monthly Sales Consolidation", Recurrence: 1st of month, 09:00.
3. Action: **Excel Online (Business) → List rows present in a table** → point to the workbook and `tblConsol`.
4. Action: **Apply to each** over the rows. Inside, add a **Condition**: `OverBudget is equal to YES`.
5. In the *If yes* branch: **Approvals → Start and wait for an approval** → type "Approve/Reject", Title = `Branch @{items('Apply_to_each')?['Branch']} over budget`, assigned to the finance controller, Details = variance amount via dynamic content.
6. After the approval, add a **Condition** on `Outcome = Approve`. If approved → **Post message in a chat or channel (Teams)** to the #finance channel: "Overspend at @{...Branch} of INR @{...Variance} approved." If rejected → **Send an email (V2)** back to the branch manager asking for justification.
7. Add a final **Send an email (V2)** to the controller with the run summary. **Save** → **Test → Manually** to dry-run.

## The output
**Power Query result table** (loaded to the sheet, fully refreshable):

```
Branch    Product   Month  Sales    Budget   Variance  OverBudget
Delhi     Widget    Mar    520,000  500,000   20,000   YES
Mumbai    Widget    Mar    460,000  500,000  -40,000   NO
Chennai   Widget    Mar    610,000  550,000   60,000   YES
```
**Power Automate run:** two approval requests (Delhi, Chennai) land in the controller's Approvals hub and Outlook; on approval a Teams message posts to #finance and a summary email is sent. The whole month-end consolidation now runs itself on the 1st at 9am with a human gate only where money is over budget.

## Checks, gotchas & red flags
- **Refresh must reproduce, not accumulate.** From-Folder appends *all* files present — if last month's file is still there you'll double-count. Keep the folder to the current set or add a date filter.
- **Data types before load.** Power Query is case-sensitive and type-strict; set each column's type (the little icon) so `Sales` sums instead of erroring. A wrong type on a merge key → zero matches.
- **Merge key must be clean on both sides** — trailing spaces or "Delhi " vs "Delhi" silently produce nulls (use Left Anti join to *see* the unmatched rows).
- **Cloud flows can't reach local files.** The workbook must live in SharePoint/OneDrive Business; a desktop path fails.
- **`Apply to each` on thousands of rows is slow and can hit action limits** — filter rows *before* the loop (use "List rows" with a filter query) rather than looping everything.
- **Approvals need valid work emails**; external/guest approvers may need extra config.
- **Timezone:** Recurrence uses UTC by default — set the timezone or your 09:00 fires at 14:30 IST.
- Don't hard-code the period inside a step *and* in the parameter — change it in one place only.

## Interview drill
**Q: Merge vs Append in Power Query — when each?**
A: Append stacks tables with the *same columns* vertically (combining Jan, Feb, Mar branch files into one longer table). Merge joins tables *side by side* on a key to bring columns together (attaching Budget to Sales on Branch+Month). Recon uses a Left Anti merge to isolate rows with no match.

**Q: How would you build a report that a colleague can update with zero Excel skill?**
A: Power Query From-Folder into a parameterised query loaded to a Table/Data Model. They just drop the new file in the folder and press Refresh All — every clean, merge, unpivot and variance step re-runs deterministically. Optionally schedule a Power Automate flow to refresh and email it so they don't even open Excel.

**Q: What's the trigger-plus-action model in Power Automate, and give a finance example?**
A: A cloud flow starts on a *trigger* (a schedule, a new email, a file created) and then runs *actions* through connectors. Example: Recurrence trigger on the 1st → List rows from an Excel table → for over-budget rows, Start-and-wait-for-approval → on approve, post to Teams and email the controller. It's event-driven RPA without code.

## Learn/practise (free)
Power Query is free in Excel and in **Power BI Desktop** (free download) — practise M there with the "Advanced Editor." Microsoft Learn has full free paths: "Get and transform data in Power BI" and "Automate a business process using Power Automate." For Power Automate, the personal Microsoft 365 developer/trial tenant gives a free work account with standard connectors; or use the **free Power Automate plan** for basic flows. Ken Puls / Excelguru and "Curbal" (YouTube) teach M superbly for free. Rehearse by taking three messy CSVs, combining From-Folder, unpivoting, merging a budget, and confirming the grouped total ties to the raw sum — then schedule a trial flow that emails you the result.
