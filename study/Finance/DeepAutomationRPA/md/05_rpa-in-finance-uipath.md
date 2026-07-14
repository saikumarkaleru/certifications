# RPA in Finance: UiPath, Automation Anywhere, Blue Prism

## What you'll be able to do

By the end of this chapter you can explain what Robotic Process Automation (RPA) actually is (and isn't), tell an interviewer the difference between an attended and an unattended bot, and — most importantly — build a working UiPath bot that automates a real finance process end-to-end: log into a bank portal (or open a downloaded statement), pull the day's transaction file, reconcile it against a ledger extract in Excel, flag the breaks, and post/write-back the matched items. You will know when RPA is the right tool versus an API or a macro, and you'll be able to speak to governance (bot IDs, credential vaults, maker-checker, audit logs) the way a GCC or shared-services hiring manager expects. You can rehearse all of this free on the UiPath Community Edition.

## The essentials

RPA is software that mimics a human using a computer — it clicks, types, reads screens, opens files, copies cells — driven by a defined workflow. It sits *on top* of existing systems (SAP, a bank portal, Excel, a web ERP) and needs no change to those systems. That is its whole selling point in finance: the underlying apps often have no API, or IT will not sanction a database integration, but a bot can do exactly what the analyst did, only faster and without fatigue.

**The three market leaders (mid-2026):**

| Tool | Position in India/GCC | Dev environment | Notable |
|---|---|---|---|
| **UiPath** | Market leader, most job postings, biggest India footprint | Studio (visual, VB/C# expressions) + Community free | Best learning path (UiPath Academy, free certs); AI/Document Understanding strong |
| **Automation Anywhere** | Strong in BPO/BFSI back-offices | Cloud-native "Automation 360" (browser-based Control Room) | Bot Store; good for high-volume unattended fleets |
| **Blue Prism** (SS&C) | Enterprise/bank IT-governed shops | "Process Studio" — no recorder, code-like, object/process split | Very governance-heavy; favoured where audit rules are strict |

**Attended vs unattended — know this cold:**

- **Attended bot** runs on the user's own machine, triggered by the human (a button, a hotkey), works *alongside* them — e.g. a bot the AP clerk fires to auto-fill an invoice screen. Think co-pilot.
- **Unattended bot** runs on a server/VM with no human present, triggered by a schedule or a queue, at 2 a.m. — e.g. the nightly bank-reconciliation run. Needs an Orchestrator (UiPath) / Control Room (AA) to license, schedule, log and hand out credentials.

**Core building blocks (UiPath vocabulary):** *Workflow* (a .xaml file of steps), *Activity* (one step — Click, Type Into, Read Range), *Recorder* (watches you do a task and generates activities), *Selector* (the XML address of a UI element the bot targets), *Orchestrator* (the web control plane: assets, queues, robots, schedules, logs), *Asset* (a stored config value or credential), *Queue* (a list of work items processed transactionally).

**When RPA is the right tool — the decision rule:**

| Situation | Use |
|---|---|
| Target app has a clean, supported **API** | API integration (Python/Power Automate) — more robust, no screen fragility |
| It's all inside **Excel/Outlook**, one machine, simple | **VBA / Office Scripts / Power Query** — lighter, free, no bot licence |
| **No API, multiple apps, GUI-only, repetitive, rule-based, high volume** | **RPA** — this is its sweet spot |
| Process needs **judgement / changes every time** | Keep it human (or add AI-in-the-loop, carefully) |

RPA is a bridge for legacy/GUI systems. If a real API exists, prefer it — bots break when a screen layout, a button label, or a login flow changes.

## Hands-on — step by step

**Worked example — daily bank reconciliation.** Every morning you download an HDFC current-account statement (CSV), compare it against the ledger extract from Tally/SAP (Excel), and mark which bank lines match a book entry. Amounts in rupees.

`bank_statement.csv`:

| Date | Description | Ref | Amount |
|---|---|---|---|
| 2026-07-13 | NEFT ACME LTD | N123 | 250000 |
| 2026-07-13 | UPI VENDOR X | U987 | -18500 |
| 2026-07-13 | BANK CHG | — | -472 |

`ledger.xlsx`:

| Ref | Party | BookAmount | Status |
|---|---|---|---|
| N123 | Acme Ltd | 250000 | |
| U987 | Vendor X | -18500 | |

**Build it in UiPath Studio:**

1. **New Process** → name it `DailyBankRecon`. Studio opens `Main.xaml` with an empty *Sequence*.
2. **Get the file.** For practice, drop the CSV into a `C:\Recon\in\` folder (in production a *Use Application/Browser* + *Type Into* + *Click* sequence, or a recorded login, downloads it from the portal — that's the "attended login" part). Add **Read CSV** activity → input `C:\Recon\in\bank_statement.csv` → output DataTable `dtBank`.
3. **Read the ledger.** Add **Excel Process Scope** → **Use Excel File** (`ledger.xlsx`) → **Read Range** → output `dtLedger`.
4. **Match.** Add a **For Each Row in DataTable** over `dtBank`. Inside, use an **Assign** to look up the ref in the ledger:
   `matchRow = dtLedger.AsEnumerable().FirstOrDefault(Function(r) r("Ref").ToString = CurrentRow("Ref").ToString)`
5. **Decide** with an **If**:
   - Condition: `matchRow IsNot Nothing AndAlso CDbl(matchRow("BookAmount")) = CDbl(CurrentRow("Amount"))`
   - **Then** (matched): Assign `matchRow("Status") = "MATCHED"`.
   - **Else** (break): add the row to a `dtBreaks` DataTable via **Add Data Row** (this is the exception list).
6. **Post / write back.** After the loop, **Write Range** `dtLedger` back to `ledger.xlsx` (Status column now populated) and **Write CSV** `dtBreaks` to `C:\Recon\out\breaks_2026-07-13.csv`.
7. **Notify.** Add **Send Outlook Mail Message** → to the accountant, subject "Bank recon 2026-07-13: 2 matched, 1 break", attach the breaks file.
8. **Log & credentials.** Wrap risky steps in **Try Catch**; use **Log Message** at each stage. Never hard-code the portal password — store it as an **Orchestrator Asset (Credential)** or Windows Credential and fetch with **Get Credential**.
9. **Run** (green ▶). Watch it step through. To schedule unattended, publish to **Orchestrator** and set a 7:30 a.m. trigger.

The **Recorder** (Ribbon → Recording → *App/Web*) shortcut: click "Record", perform the portal login and download manually once, hit Save — Studio generates the Click/Type Into activities and their selectors for you. You then clean up the selectors and wrap them in Try Catch.

## The output

Console/Orchestrator log:
```
[INFO] DailyBankRecon started 07:30:01
[INFO] Read 3 bank rows, 2 ledger rows
[INFO] N123  250000  -> MATCHED
[INFO] U987  -18500  -> MATCHED
[WARN] BANK CHG -472  -> BREAK (no ledger ref)
[INFO] Wrote breaks_2026-07-13.csv (1 row); ledger written back; mail sent
[INFO] Completed 07:30:14  duration 13s
```

`ledger.xlsx` (Status filled) and `breaks_2026-07-13.csv`:

| Date | Description | Ref | Amount |
|---|---|---|---|
| 2026-07-13 | BANK CHG | — | -472 |

Deliverable = reconciled ledger + a one-line break (bank charges not yet booked — the accountant posts an expense entry) + an audit-logged, e-mailed run.

## Checks, gotchas & red flags

- **Must tie out:** matched + breaks = total bank lines (2 + 1 = 3). If not, a row was dropped — check the loop and date/number formats.
- **Type traps:** CSV amounts come in as *text*. `CDbl()` them before comparing, and beware "18,500" (comma) or "(18500)" (brackets = negative) — strip/convert first.
- **Selector fragility (the #1 RPA failure):** dynamic IDs, changed labels, or a portal redesign break the bot silently. Use anchors, wildcards (`*`), and stable attributes; never rely on screen coordinates.
- **Idempotency:** if the bot re-runs, don't double-post. Check the Status flag before writing.
- **Credentials in plain text** in a variable or config = instant audit fail. Always use a vault/Asset.
- **No exception handling** = a single pop-up hangs the whole unattended run. Wrap in Try Catch and route failures to a queue.
- **Governance red flags:** no bot ID, no maker-checker on what it posts, no audit log, bot running under a personal login instead of a service account. Auditors will ask exactly these.

## Interview drill

**Q1. "Attended or unattended bot for month-end bank recon across 40 accounts — which and why?"**
Unattended. It's high-volume, rule-based, runs overnight with no human, and needs central scheduling, credential vaulting and audit logs — that's Orchestrator/unattended territory. Attended suits a human-triggered, single-desk task. I'd feed the 40 accounts through an Orchestrator *queue* so each is a transactional work item with retry and a clean per-account audit trail.

**Q2. "The bank has a REST API. Would you still use RPA?"**
No — I'd integrate via the API (Python/requests or Power Automate). It's far more robust than screen-scraping, survives UI changes, and is easier to audit. RPA is my tool when there's *no* API and the system is GUI-only. Choosing RPA over an available API is a common anti-pattern that creates fragile automation.

**Q3. "How do you make an RPA bank-recon auditable?"**
Service account (not a personal login), credentials in a vault/Asset, unique bot ID, Log Message at every stage into Orchestrator, a maker-checker so the bot proposes postings but a human approves the break entries, versioned workflow in Git, and an exception queue so nothing fails silently. I'd also reconcile control totals (matched + breaks = total) each run.

## Learn/practise (free)

- **UiPath Community Edition** — free Studio download, full-featured for learning; **Community Orchestrator** (free cloud tenant) to practise assets, queues and schedules.
- **UiPath Academy** — free courses and the **UiPath Certified Professional – Automation Developer Associate (UiPath-ADAv1)** cert path; do the "RPA Developer Foundation".
- **Automation Anywhere University** and **Blue Prism Learning** — free community/learning editions to see the other two Control Rooms.
- **Rehearse cheaply:** you need no bank at all — generate a fake `bank_statement.csv`, build the recon above, then extend it: add a portal-login recording against any practice site (UiPath's own ACME test site), route breaks to a queue, and schedule an unattended run on your own machine. Put the .xaml on GitHub — that becomes a portfolio piece (next chapter).
