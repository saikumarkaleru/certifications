# Pulling & Cleaning Data into Excel (BDP/BDH/BQL, CapIQ Plugin)

## What you'll be able to do

Get data out of Bloomberg and Capital IQ into a spreadsheet **as live, refreshable formulas** — not copy-paste that rots the moment the price moves. You'll write `=BDP` for a single current value, `=BDH` for a time series, `=BDS` for bulk/list data, know when to reach for BQL, and pull the same financials from CapIQ with `=CIQ` formulas. You'll build a clean, model-ready "Data" tab: one place all raw pulls land, from which your model reads — the discipline that stops a model from silently breaking. Worked outcome: five years of Infosys financials sitting in a tab your DCF/comps can point at.

## The drill — step by step

**0. Install & log in.** The Bloomberg add-in installs from the terminal (`WAPI`/`API<GO>` → "Excel Add-in") and needs you logged into Bloomberg on that machine. In Excel you'll see a **Bloomberg** ribbon tab. CapIQ's plugin installs separately and adds a **Capital IQ** ribbon (log in with your S&P credentials).

**1. `=BDP` — Bloomberg Data Point (one static/current value).**
Syntax: `=BDP("security", "field")`.
```
=BDP("INFO IN Equity","PX_LAST")          → last price
=BDP("INFO IN Equity","CUR_MKT_CAP")      → market cap
=BDP("INFO IN Equity","BEST_PE_RATIO")    → forward P/E (BEST = consensus estimate)
=BDP("INFO IN Equity","CRNCY")            → INR
```
The trick is knowing the **field mnemonic**. Find them with `FLDS <GO>` on the terminal (searchable field dictionary) or the FieldSearch button on the ribbon. `PX_LAST`, `CUR_MKT_CAP`, `SALES_REV_TURN`, `EBITDA`, `IS_EPS`, `BS_TOT_ASSET`, `TRAIL_12M_...`, `BEST_...` (estimates) are the ones you'll reuse.

**2. `=BDH` — Bloomberg Data History (a time series).**
Syntax: `=BDH("security","field(s)","start","end", [optional args])`.
```
=BDH("INFO IN Equity","PX_LAST","1/1/2021","12/31/2025","Per=M")
```
`Per=M` (monthly), `Per=Q`, `Per=Y` set frequency; `Fill=P` carries prices over non-trading days; `Days=W` restricts to weekdays. BDH spills a two-column (date, value) array **downward** — leave blank cells below the formula or it errors with `#N/A Requesting Data` colliding into your labels.

**3. `=BDS` — Bloomberg Data Set (bulk / list data that returns many rows/cols).**
Used for things that aren't a single number: index members, dividend history, the full list of a company's segments or peers.
```
=BDS("NIFTY Index","INDX_MEMBERS")     → all Nifty constituents
=BDS("INFO IN Equity","DVD_HIST")      → dividend history table
```

**4. BQL — Bloomberg Query Language (the modern, powerful way).**
BQL does filtering, aggregation and universe screening in one formula, returning a table. It's what you graduate to when BDP/BDH get clumsy. Conceptually: `get(...)` fields `for(...)` a universe `with(...)` parameters.
```
=BQL("members('NIFTY Index')","name, px_last, pe_ratio")
```
returns every Nifty member with its name, price and P/E in one spill. You don't need mastery on day one — know it exists and that it replaces stacking 50 BDP calls.

**5. CapIQ Excel plugin — `=CIQ` formulas.**
Same idea, S&P's data. `=CIQ("IQ ticker / identifier","mnemonic", [period])`.
```
=CIQ("INFO:","IQ_TOTAL_REV","IQ_FY-4")     → revenue, 4 years ago
=CIQ("INFO:","IQ_EBITDA","IQ_FY")          → latest FY EBITDA
=CIQ("INFO:","IQ_EBITDA","IQ_FY-1")        → prior FY
```
`IQ_FY`, `IQ_FY-1…-4` walk back fiscal years; `IQ_FQ` for quarters; `IQ_NTM`/`IQ_FY+1` for forward estimates. CapIQ mnemonics (`IQ_TOTAL_REV`, `IQ_EBIT`, `IQ_NI`, `IQ_TOTAL_DEBT`, `IQ_CASH_ST_INVEST`, `IQ_TEV` = enterprise value) come from the plugin's formula builder — use it, don't memorise.

**6. Build the clean Data tab.** Discipline that separates a pro model from a mess:
- One tab named `Data_Raw`. Formulas only reference it; the model never calls BDP directly in the middle of a calc.
- **Columns = periods (FY-4…FY), rows = line items.** Put the entity ticker in one cell (`B1`) and reference it: `=CIQ($B$1,"IQ_TOTAL_REV","IQ_FY-4")`. Change one cell → whole tab re-points to a new company.
- Immediately below each live-formula block, **paste-special → values** into a mirror block if you need a point-in-time snapshot (see gotchas).
- Add a **units row** and a **currency cell**; convert to a single reporting currency explicitly.

**Worked example — Infosys 5-yr revenue & EBITDA, model-ready:**

| Row / `IQ_FY-` | FY-4 | FY-3 | FY-2 | FY-1 | FY |
|---|---|---|---|---|---|
| Formula (Revenue) | `=CIQ($B$1,"IQ_TOTAL_REV","IQ_FY-4")` | …`-3` | …`-2` | …`-1` | …`IQ_FY` |
| Revenue (₹ cr) | 100,472 | 121,641 | 146,767 | 153,670 | 162,990 |
| EBITDA (₹ cr) | 26,000 | 30,700 | 34,900 | 36,100 | 38,900 |
| EBITDA margin | 25.9% | 25.2% | 23.8% | 23.5% | 23.9% |

(Numbers illustrative — the point is every cell is a formula keyed to `$B$1`.)

## The output

A single `Data_Raw` tab: ticker cell up top, a currency/units header, one clean block per statement (IS, BS, CF), periods across, live formulas that refresh on open, and a values-mirror for the version you actually valued off. Your comps and DCF tabs contain **zero** BDP/CIQ calls — they read from `Data_Raw` by cell reference. Hand it to a colleague, they change `$B$1` from `INFO:` to `TCS:` and the whole book reprices.

## Checks & gotchas

- **`#N/A Requesting Data` / `#N/A Invalid Field`** — data still loading (wait/refresh) vs. a wrong mnemonic (fix via FLDS/formula builder). Don't build on top of a cell that's still `Requesting`.
- **Point-in-time vs. restated.** Live formulas pull *today's* view of history — companies restate, and consensus estimates drift daily. If your valuation must be reproducible, paste-special values and date-stamp the snapshot. This is the single most common "my model changed overnight" bug.
- **Currency & scale.** CapIQ may return USD while Bloomberg FA showed INR; ₹ crore vs. ₹ mn vs. absolute. Force one currency, one scale, and label it. A 100x error hides here.
- **Fiscal-year misalignment.** `IQ_FY` for an Indian March year-end ≠ a US December year-end peer — you'll calendarise in Chapter 3.
- **Blank-cell collisions.** BDH/BDS spill arrays; leave room or they overwrite (or error against) adjacent cells.
- **Broken on a machine without a login.** These formulas only resolve where the add-in + entitlement live. Email the workbook and the recipient sees `#NAME?` unless they too have the plugin — send the values-mirror.

## Interview drill

**Q: "Difference between BDP, BDH and BDS?"**
A: "BDP returns one current/static value for one field. BDH returns a historical time series with a frequency you set. BDS returns bulk or list-type data — index members, dividend schedules — that isn't a single scalar. One point, one history, one set."

**Q: "How do you make sure a Bloomberg-linked model is reproducible?"**
A: "Isolate all live pulls in a Data tab, then paste-special the values you actually valued off and date-stamp them, because live formulas re-pull restated financials and shifting consensus every time the book opens. The audit version is static; the live version is for updating."

**Q: "Why keep a separate Data tab instead of calling BDP inside the model?"**
A: "Auditability and portability — one place to check every input, one cell to re-point the whole model to a new ticker, and the calc engine keeps working even if the data connection drops."

## Practise free

The formula *thinking* transfers completely without a licence:
- **Python `yfinance`** — `yf.Ticker("INFY.NS").financials` and `.history(period="5y")` reproduce BDH/CIQ pulls for Indian tickers (`.NS` = NSE). Build the exact `Data_Raw` layout in pandas and export to Excel.
- **Screener.in export** — the "Export to Excel" button on any company gives you 10 years of financials in one sheet; treat it as your CapIQ dump and build the clean tab on top.
- **`nsepy` / NSE bhavcopy** — free historical prices for the BDH drill.
- **`=STOCKHISTORY()`** in Microsoft 365 Excel — a genuine free BDH analogue for prices: `=STOCKHISTORY("INFY","1/1/2021",,2,0,0,1)`.
Drill: replicate the Infosys revenue/EBITDA table above from a Screener.in export, then rebuild it in pandas so you understand what the plugin does under the hood.
