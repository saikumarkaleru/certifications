# Python for Finance I: pandas & numpy

## What it is & where it's used

**pandas** is a Python library that gives you a spreadsheet-like object called a *DataFrame* — rows and columns, but programmable. **numpy** is the numerical engine underneath it (fast arrays and math). Together they are the workhorses of every finance analytics team: you load a CSV/Excel/database extract, clean it, filter it, group it, join it to a master, and produce numbers — all in code that runs identically tomorrow with one click.

Where it shows up in real finance/accounts/tax roles:

| Role | What they do with pandas |
|---|---|
| FP&A / MIS analyst | Combine month-end exports into a P&L variance report |
| Accounts / AR-AP | Reconcile ledger vs bank, ageing of receivables |
| Tax / GST associate | Match GSTR-2B (portal) against purchase register (Tally/ERP) |
| Audit / internal audit | Sample testing, duplicate-invoice detection across lakhs of rows |
| Equity / credit research | Clean price/fundamental data, compute ratios and returns |

Excel breaks past ~100k rows and can't reliably repeat a 20-step manual process. pandas doesn't care whether it's 500 rows or 5 million, and the process is saved as a script.

## The gap: why companies want this (and college didn't teach it)

An MBA-Finance or CA syllabus teaches you *what* a receivables ageing or a GST reconciliation **means**. It does not teach you to produce one from a 2-lakh-row dump at 9 PM on close day. Colleges assume "the data is given, clean, and small." Industry data is none of those: it arrives as a messy export with merged headers, ₹ signs stuck in text, dates as `31-03-2026` in one file and `2026/03/31` in another, and duplicate invoice numbers.

The gap is **repeatable data handling at scale**. Employers have discovered that a fresher who can write 15 lines of pandas replaces hours of copy-paste-VLOOKUP and, crucially, does it *the same way every month* with an audit trail. That reliability — not fancy modelling — is what they pay a premium for.

## What "proficient" looks like

A job-ready person can, **unaided**, take two raw files and produce a correct output in under 30 minutes:

- Load CSV/Excel (right sheet, skip junk rows, set dtypes).
- Inspect: `.head()`, `.info()`, `.describe()`, `.shape`.
- Filter rows on multiple conditions and select columns.
- Clean: strip whitespace, fix ₹/comma text into numbers, parse dates, handle blanks/NaN, drop or flag duplicates.
- `groupby` + aggregate to get subtotals (sum, count, mean) by any dimension.
- `merge` two DataFrames (inner/left) on a key — and know *why* rows drop or duplicate.
- Add computed columns, sort, and export back to Excel with formatting intact.

If you can do a GST-2B vs purchase-register match or an AR ageing without googling every second line, you clear the bar.

## Hands-on: how to actually do it

Setup once: `pip install pandas numpy openpyxl`. Then `import pandas as pd` and `import numpy as np`.

**Load data**

```python
# CSV — set the invoice number as text so leading zeros survive
df = pd.read_csv("sales.csv", dtype={"invoice_no": str})

# Excel — pick sheet, skip 3 junk header rows, parse a date column
df = pd.read_excel("tb.xlsx", sheet_name="Data", skiprows=3,
                   parse_dates=["invoice_date"])
```

**Inspect**

```python
df.shape            # (rows, cols)
df.head(10)         # first 10 rows
df.info()           # dtypes + non-null counts — catches text-vs-number bugs
df.describe()       # min/max/mean of numeric cols
df["state"].value_counts()
```

**Filter & select** (`&` = and, `|` = or, each condition in parentheses)

```python
# Maharashtra invoices above ₹1,00,000
big = df[(df["state"] == "Maharashtra") & (df["amount"] > 100000)]

# only three columns
cols = df[["invoice_no", "party", "amount"]]

# .isin for a list; ~ negates
south = df[df["state"].isin(["Karnataka", "Tamil Nadu", "Kerala"])]
```

**Clean** — the part that eats 80% of real work

```python
# "₹1,20,500" (text) -> 120500.0 (number)
df["amount"] = (df["amount"].astype(str)
                .str.replace("₹", "", regex=False)
                .str.replace(",", "", regex=False)
                .str.strip())
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")  # bad -> NaN

# trim stray spaces in text keys (a top cause of failed merges)
df["party"] = df["party"].str.strip().str.upper()

# mixed date formats -> real dates
df["invoice_date"] = pd.to_datetime(df["invoice_date"],
                                    dayfirst=True, errors="coerce")

df["amount"] = df["amount"].fillna(0)        # blanks -> 0
df = df.drop_duplicates(subset=["invoice_no"])  # kill dupes on key

# flag (don't delete) duplicates for review
df["is_dup"] = df.duplicated(subset=["invoice_no"], keep=False)
```

**groupby — subtotals**

```python
# total & count of sales per state
by_state = (df.groupby("state")
              .agg(total=("amount", "sum"),
                   invoices=("invoice_no", "count"))
              .reset_index()
              .sort_values("total", ascending=False))
```

**merge — the VLOOKUP replacement**

```python
merged = pd.merge(purchase, gstr2b,
                  on="invoice_no", how="left",
                  suffixes=("_book", "_portal"),
                  indicator=True)   # _merge col shows both / left_only
```

**numpy for conditional columns**

```python
df["gst_rate"] = np.where(df["amount"] > 50000, 0.18, 0.12)
df["gst"] = df["amount"] * df["gst_rate"]
```

**Export**

```python
merged.to_excel("recon_output.xlsx", index=False)
```

## Worked example / mini-project: GST-2B vs Purchase-Register match

You have the **purchase register** from Tally and **GSTR-2B** downloaded from the GST portal. Goal: find invoices where Input Tax Credit (ITC) in your books doesn't match the portal — the classic monthly ITC reconciliation.

`purchase_register.csv`

| invoice_no | supplier_gstin | taxable | igst |
|---|---|---|---|
| INV001 | 27ABCDE1234F1Z5 | 100000 | 18000 |
| INV002 | 29PQRST5678G2Z1 | 50000 | 9000 |
| INV003 | 27ABCDE1234F1Z5 | 20000 | 3600 |

`gstr2b.csv` (portal shows INV001 with a different tax, and no INV003)

| invoice_no | igst |
|---|---|
| INV001 | 17000 |
| INV002 | 9000 |

```python
import pandas as pd

pr  = pd.read_csv("purchase_register.csv", dtype={"invoice_no": str})
b2b = pd.read_csv("gstr2b.csv", dtype={"invoice_no": str})

# clean keys so the match doesn't fail on spaces/case
for d in (pr, b2b):
    d["invoice_no"] = d["invoice_no"].str.strip().str.upper()

m = pd.merge(pr, b2b, on="invoice_no", how="left",
             suffixes=("_book", "_2b"), indicator=True)

m["igst_2b"] = m["igst_2b"].fillna(0)
m["diff"] = m["igst_book"] - m["igst_2b"]

def status(r):
    if r["_merge"] == "left_only":
        return "Missing in 2B (ITC at risk)"
    return "OK" if abs(r["diff"]) < 1 else "Tax mismatch"

m["status"] = m.apply(status, axis=1)
print(m[["invoice_no", "igst_book", "igst_2b", "diff", "status"]])
```

Output:

| invoice_no | igst_book | igst_2b | diff | status |
|---|---|---|---|---|
| INV001 | 18000 | 17000 | 1000 | Tax mismatch |
| INV002 | 9000 | 9000 | 0 | OK |
| INV003 | 3600 | 0 | 3600 | Missing in 2B (ITC at risk) |

You just flagged ₹3,600 of ITC you can't claim yet and a ₹1,000 mismatch to query the supplier — the exact deliverable a GST associate produces every month, now reproducible in seconds.

## How it's tested

**Interview questions (conceptual):**
- Difference between `merge` types — what happens to unmatched rows in `inner` vs `left`?
- Why did your merge produce *more* rows than either input? (Answer: duplicate keys → many-to-many.)
- `loc` vs `iloc`? When does a "SettingWithCopyWarning" appear?
- How do you replace a nested VLOOKUP / a pivot table with pandas?
- Difference between `apply`, `map`, and vectorised operations (and why vectorised is faster).

**Practical test (what actually decides it):** a timed take-home or live screen. Typical brief: *"Here are two CSVs — a sales dump and a customer master. Give me total sales per region, flag customers with no master record, and export to Excel. 30 minutes."* They watch whether you check dtypes, handle the dirty ₹ column, pick the right join, and notice dropped rows. Some firms give a Jupyter notebook and one messy file and simply say "reconcile these."

## Common mistakes & how pros avoid them

| Mistake | Consequence | Pro habit |
|---|---|---|
| Merging on untrimmed/mixed-case keys | Silent non-matches | `.str.strip().str.upper()` both keys first |
| Ignoring `.info()` — amount is text | `sum()` concatenates or errors | Check dtypes immediately after load |
| `how="inner"` by default | Silently drops unmatched rows | Use `how="left"` + `indicator=True` to see drops |
| Not checking row count after merge | Duplicated rows inflate totals | Compare `len()` before/after; check key uniqueness |
| Chained indexing `df[df.x>1]["y"]=0` | SettingWithCopyWarning, no change | Use `.loc[mask, "y"] = 0` |
| `dropna()` everything | Deletes valid rows with one blank | Fill or subset: `fillna(0)`, `dropna(subset=[...])` |
| Losing leading zeros in invoice/GSTIN | Broken keys | `dtype=str` on read |

Golden rule: after every merge, print `df["_merge"].value_counts()` and confirm row counts. Most "wrong numbers" in finance pandas are a bad join, not bad math.

## Learn-it roadmap & resources

**Time to job-ready: 3–5 weeks** at ~1 hr/day if you already know finance logic (you do).

| Week | Focus |
|---|---|
| 1 | Python basics + read/inspect CSV/Excel; `head/info/describe` |
| 2 | Filtering, `loc/iloc`, cleaning (dtypes, dates, ₹-text, NaN) |
| 3 | `groupby` aggregations; `merge`/`concat`; computed columns |
| 4 | Rebuild 2–3 of your own Excel reports in pandas end-to-end |
| 5 | Speed, `pivot_table`, export formatting, edge cases |

**Resources**
- *pandas official "10 minutes to pandas"* — free, start here.
- Kaggle **"Pandas" micro-course** — free, hands-on, ~4 hrs.
- Wes McKinney, *Python for Data Analysis* (3rd ed.) — the reference (pandas' creator).
- Practice on real data: RBI/NSE downloads, or your own bank statement/Tally exports.

**Certification:** none is required for pandas itself; recruiters test the skill, not a badge. If you want a credential, *Google Data Analytics (Coursera)* or a Kaggle certificate signals intent. Your strongest asset is a GitHub repo with 2–3 reconciliations like the one above.

## Quick-reference

```python
import pandas as pd, numpy as np

pd.read_csv("f.csv", dtype={"id": str})          # load, keep id as text
pd.read_excel("f.xlsx", sheet_name="S", skiprows=2, parse_dates=["dt"])
df.head(); df.info(); df.describe(); df.shape     # inspect
df["c"].value_counts()                            # frequency

df[(df.a > 100) & (df.b == "X")]                  # filter (parentheses!)
df[df.state.isin(["KA","TN"])]                    # value in list
df.loc[mask, "col"] = 0                           # safe assignment

pd.to_numeric(s, errors="coerce")                 # text -> number
s.str.replace(",", "", regex=False)               # strip commas
pd.to_datetime(s, dayfirst=True, errors="coerce") # dd-mm-yyyy -> date
df.fillna(0); df.dropna(subset=["k"])             # missing values
df.drop_duplicates(subset=["k"])                  # dedupe
df.duplicated(subset=["k"], keep=False)           # flag dupes

df.groupby("g").agg(total=("amt","sum"),
                    n=("id","count")).reset_index()
pd.merge(a, b, on="k", how="left", indicator=True)
np.where(cond, x, y)                              # if-else column
df.sort_values("amt", ascending=False)
df.to_excel("out.xlsx", index=False)              # export
```

| Merge `how` | Keeps |
|---|---|
| `inner` | keys in **both** |
| `left` | **all left** + matching right |
| `right` | all right + matching left |
| `outer` | **everything**, NaN where unmatched |
