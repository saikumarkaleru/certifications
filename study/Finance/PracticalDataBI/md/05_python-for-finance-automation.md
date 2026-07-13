# Python for Finance II: Automation

## What it is & where it's used

Automation is using Python to do the boring, repeatable finance work that eats your day: pulling numbers out of Excel files, reshaping them, writing formatted output back to Excel, emailing the result, and running the whole thing on a schedule without you touching it. It is the difference between "I spend the first two hours of every month copy-pasting the MIS" and "the MIS lands in the CFO's inbox at 8:00 AM on the 1st while I'm still asleep."

The core libraries are **pandas** (read/transform/write tabular data), **openpyxl** (fine-grained Excel control — formatting, formulas, multiple sheets, cell styling), **smtplib**/`email` (send mail via SMTP), and a scheduler (Windows Task Scheduler or `cron` on Linux; libraries like `schedule` for in-process timing).

Roles that live on this: **FP&A analysts** (monthly MIS, variance packs), **accounts/AP-AR teams** (vendor ageing, reconciliations), **tax/GST executives** (GSTR-2B vs purchase register matching), **treasury** (daily bank position), **audit** (sampling, ledger scrutiny), and anyone who owns a recurring "report" that today is a manual Excel ritual.

## The gap: why companies want this (and college didn't teach it)

An MBA teaches you *what* a variance analysis or a debtors ageing means. It never shows you that in a real company that report is regenerated **every single month from a messy dump** — the ERP exports a CSV with merged headers, three date formats, and vendor names spelled four ways. College assignments give you one clean dataset once. Industry gives you the same dirty dataset forever, on a deadline.

The specific gap: graduates can *build* a report once by hand in Excel but cannot *productionise* it. They don't know that a 90-minute manual task can become a 4-second script. Employers pay a premium for the person who says "I automated the AP ageing; it now runs itself" — that person just gave the team back 20 hours a month. This is the single most visible, promotable skill for a junior finance hire because the time saved is directly measurable.

## What "proficient" looks like

A job-ready person can, unaided:

- Read one or many Excel/CSV files into pandas, including specifying the header row, sheet name, and dtypes.
- Clean real dirt: strip whitespace, fix dates, dedupe, handle blanks, map inconsistent names.
- Do the transform (group-by, pivot, merge/lookup across sheets) in pandas.
- Write a **formatted** multi-sheet Excel file — bold headers, number formats (`#,##0.00`), frozen panes, coloured totals, even live Excel formulas — not a raw dump.
- Send that file as an email attachment via SMTP with a templated body.
- Schedule the script to run daily/monthly and log whether it succeeded or failed.
- Make it robust: if the input file is missing, it emails an alert instead of crashing silently.

## Hands-on: how to actually do it

### Read Excel/CSV into pandas

```python
import pandas as pd

# Read a specific sheet, telling pandas the header is on row 2 (0-indexed)
df = pd.read_excel("Purchase_Register_Jun26.xlsx",
                   sheet_name="Data", header=1,
                   dtype={"GSTIN": str, "Invoice_No": str})

# CSV with Indian date format
df = pd.read_csv("bank_stmt.csv", parse_dates=["Txn_Date"], dayfirst=True)
```

### Clean the dirt (this is 60% of real work)

```python
df.columns = df.columns.str.strip()                       # kill trailing spaces in headers
df["Vendor"] = df["Vendor"].str.strip().str.upper()       # normalise names
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")  # text -> number, bad -> NaN
df = df.dropna(subset=["Invoice_No"]).drop_duplicates()
df["Txn_Date"] = pd.to_datetime(df["Txn_Date"], dayfirst=True, errors="coerce")
```

### The transform — group, pivot, lookup

```python
# Debtors ageing buckets
today = pd.Timestamp("2026-06-30")
df["Days"] = (today - df["Invoice_Date"]).dt.days
bins   = [-1, 30, 60, 90, 10**6]
labels = ["0-30", "31-60", "61-90", "90+"]
df["Bucket"] = pd.cut(df["Days"], bins=bins, labels=labels)

ageing = df.pivot_table(index="Customer", columns="Bucket",
                        values="Outstanding", aggfunc="sum",
                        fill_value=0, margins=True, margins_name="Total")

# VLOOKUP-equivalent: merge master data onto transactions
out = txns.merge(master[["Vendor", "GSTIN", "PAN"]], on="Vendor", how="left")
```

### Write a *formatted* Excel workbook with openpyxl

```python
from openpyxl.styles import Font, PatternFill, Alignment, numbers

with pd.ExcelWriter("MIS_Jun26.xlsx", engine="openpyxl") as xl:
    ageing.to_excel(xl, sheet_name="Ageing")
    ws = xl.sheets["Ageing"]

    # Bold header row + fill colour
    hdr = Font(bold=True, color="FFFFFF")
    fill = PatternFill("solid", fgColor="1F4E78")
    for cell in ws[1]:
        cell.font, cell.fill = hdr, fill
        cell.alignment = Alignment(horizontal="center")

    # Indian number format on all data columns
    for row in ws.iter_rows(min_row=2, min_col=2):
        for c in row:
            c.number_format = '#,##0.00'

    ws.freeze_panes = "B2"                 # freeze header + first column
    ws.column_dimensions["A"].width = 30
```

You can even write **live Excel formulas** so the recipient sees a working sheet:

```python
ws["F2"] = "=SUM(B2:E2)"     # openpyxl writes the formula string; Excel evaluates it
```

### Send it by email (SMTP)

```python
import smtplib, ssl
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "Debtors Ageing — June 2026"
msg["From"]    = "mis-bot@company.com"
msg["To"]      = "cfo@company.com, controller@company.com"
msg.set_content("Hi team,\n\nPlease find the June debtors ageing attached.\n\nAuto-generated by MIS bot.")

with open("MIS_Jun26.xlsx", "rb") as f:
    msg.add_attachment(f.read(), maintype="application",
        subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename="MIS_Jun26.xlsx")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as s:
    s.login("mis-bot@company.com", APP_PASSWORD)   # Gmail: use an App Password, never your login
    s.send_message(msg)
```

> Security note: never hard-code passwords. Read from an environment variable: `APP_PASSWORD = os.environ["MAIL_PW"]`. For Gmail/Outlook you must generate an **App Password** (2FA required).

### Schedule it

**Windows Task Scheduler** (most Indian finance desktops are Windows):

1. Wrap your script in a `.bat`: `C:\Python\python.exe C:\scripts\mis.py >> C:\scripts\log.txt 2>&1`
2. Task Scheduler → Create Task → Triggers → *Monthly, day 1, 08:00* → Actions → *Start a program* → point to the `.bat`.
3. Tick "Run whether user is logged on or not."

**Linux/server (`cron`)** — run 8 AM on the 1st of every month:

```
0 8 1 * *  /usr/bin/python3 /home/fin/mis.py >> /home/fin/mis.log 2>&1
```

## Worked example / mini-project: month-end vendor ageing bot

**Goal:** every month, read the AP ledger export, build a vendor ageing report bucketed by days overdue, format it, and email it to the finance head.

Input `AP_Ledger.xlsx` (realistic ₹ data):

| Vendor | Invoice_No | Invoice_Date | Outstanding |
|---|---|---|---|
| ACME STEEL | INV-1001 | 2026-04-02 | 2,45,000 |
| ACME STEEL | INV-1044 | 2026-05-28 | 1,10,000 |
| BLUE LOGISTICS | INV-2210 | 2026-03-15 | 88,500 |
| ZENITH PACK | INV-3300 | 2026-06-20 | 3,20,000 |

```python
import pandas as pd, os, smtplib, ssl
from email.message import EmailMessage
from openpyxl.styles import Font, PatternFill

FILE = "AP_Ledger.xlsx"
if not os.path.exists(FILE):
    raise SystemExit("Input missing — alert should fire here")

df = pd.read_excel(FILE, dtype={"Invoice_No": str})
df["Invoice_Date"] = pd.to_datetime(df["Invoice_Date"])
df["Outstanding"]  = pd.to_numeric(df["Outstanding"], errors="coerce")

asof = pd.Timestamp("2026-06-30")
df["Days"]   = (asof - df["Invoice_Date"]).dt.days
df["Bucket"] = pd.cut(df["Days"], [-1,30,60,90,10**6],
                      labels=["0-30","31-60","61-90","90+"])

report = df.pivot_table(index="Vendor", columns="Bucket", values="Outstanding",
                        aggfunc="sum", fill_value=0, margins=True, margins_name="Total")

with pd.ExcelWriter("Vendor_Ageing_Jun26.xlsx", engine="openpyxl") as xl:
    report.to_excel(xl, sheet_name="Ageing")
    ws = xl.sheets["Ageing"]
    for c in ws[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="1F4E78")
    for row in ws.iter_rows(min_row=2, min_col=2):
        for c in row: c.number_format = '#,##0'
    ws.freeze_panes = "B2"; ws.column_dimensions["A"].width = 28
```

**Expected output** (₹):

| Vendor | 0-30 | 31-60 | 61-90 | 90+ | Total |
|---|---|---|---|---|---|
| ACME STEEL | 0 | 1,10,000 | 0 | 2,45,000 | 3,55,000 |
| BLUE LOGISTICS | 0 | 0 | 0 | 88,500 | 88,500 |
| ZENITH PACK | 3,20,000 | 0 | 0 | 0 | 3,20,000 |
| **Total** | 3,20,000 | 1,10,000 | 0 | 3,33,500 | 7,63,500 |

Then attach and email exactly as in the SMTP block above. Point Task Scheduler at it for the 1st of each month — you never touch the ageing report again.

## How it's tested

**Interview questions:**

- "The ERP export has the header on row 3 and dates as `DD-MM-YYYY`. How do you read it correctly?" (Answer: `read_excel(header=2)` + `pd.to_datetime(..., dayfirst=True)`.)
- "How is `pd.merge(how='left')` different from an Excel VLOOKUP? What happens to non-matches?" (Left keeps all left rows; misses become `NaN`.)
- "How would you email a formatted Excel file every Monday without a person running it?" (SMTP + Task Scheduler/cron.)
- "How do you keep the SMTP password out of the code?" (Env var / secrets manager, App Password.)

**Practical test:** A timed take-home or on-screen task — "Here's a 5,000-row messy sales dump. Produce a clean, formatted Excel MIS with monthly totals by region, and a Python script we can re-run next month." They score you on: does it re-run without editing, is the output *formatted* (not raw), did you handle blank/duplicate rows, and did you make it fail gracefully.

## Common mistakes & how pros avoid them

| Mistake | Fix |
|---|---|
| Hard-coding file paths/dates so it breaks next month | Use `datetime.now()` and relative/config-driven paths |
| Delivering a raw pandas dump with no formatting | Always style headers, set `#,##0` formats, freeze panes |
| Password in the script, pushed to Git | Env vars; `.gitignore` secrets; App Passwords |
| Script crashes silently at 8 AM, nobody notices | Wrap in `try/except`, log to file, email an alert on failure |
| `to_excel` on a filename that's open in Excel → PermissionError | Close the file / write to a timestamped name |
| Ignoring dtype — GSTIN `27ABC...` read as float, invoice `007` loses leading zeros | Pass `dtype=str` for IDs/codes |
| Chained slow loops over rows | Vectorise with pandas group-by/`cut`, not `for` loops |

## Learn-it roadmap & resources

**Time to job-ready: 4–6 weeks** if you already know basic Python (Chapter 04).

- **Week 1–2:** pandas read/clean/transform. Rebuild an old Excel report of yours in pandas.
- **Week 3:** openpyxl formatting + writing multi-sheet workbooks with formulas.
- **Week 4:** smtplib email + scheduling; convert one real recurring task into a scheduled bot.
- **Week 5–6:** robustness — logging, try/except, config files; build the ageing/MIS mini-project end-to-end.

Resources:

- *Automate the Boring Stuff with Python* (Al Sweigart) — free online; the Excel + email chapters are exactly this.
- **pandas** docs "10 minutes to pandas"; **openpyxl** official tutorial (both free).
- YouTube: "Python Excel automation" walkthroughs.
- Certification: none is required, but **Microsoft PL-300** (Power BI) and Google's Python courses on Coursera signal seriousness. The real credential is a GitHub repo showing a working MIS bot.

## Quick-reference

| Task | Snippet |
|---|---|
| Read Excel sheet | `pd.read_excel(f, sheet_name="Data", header=1)` |
| Read CSV, IN dates | `pd.read_csv(f, parse_dates=["d"], dayfirst=True)` |
| Force text dtype | `dtype={"GSTIN": str}` |
| Clean headers | `df.columns = df.columns.str.strip()` |
| Text → number | `pd.to_numeric(s, errors="coerce")` |
| Ageing buckets | `pd.cut(days, bins, labels=...)` |
| VLOOKUP | `a.merge(b, on="key", how="left")` |
| Pivot with totals | `pivot_table(..., margins=True)` |
| Write Excel | `df.to_excel("out.xlsx", index=False)` |
| Bold header (openpyxl) | `cell.font = Font(bold=True)` |
| ₹ number format | `cell.number_format = '#,##0.00'` |
| Freeze panes | `ws.freeze_panes = "B2"` |
| Send mail | `smtplib.SMTP_SSL("smtp.gmail.com", 465)` |
| Secret from env | `os.environ["MAIL_PW"]` |
| Schedule (cron) | `0 8 1 * * python mis.py` |
| Schedule (Windows) | Task Scheduler → Monthly → run `.bat` |
