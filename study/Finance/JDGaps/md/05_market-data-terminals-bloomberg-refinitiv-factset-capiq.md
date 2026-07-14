# Market-Data Terminals Hands-On: Bloomberg, Refinitiv, FactSet, Capital IQ

## The gap

Your knowledge guides *mention* Bloomberg and Capital IQ; they never teach you to **drive** them. Every equity research, IB, PE, credit and buy-side JD assumes you can sit at a terminal and pull a company, a comp set, a chart and a screen in seconds. That muscle memory — the function codes, the Excel add-ins — is the gap, and it's the one that separates "I've heard of Bloomberg" from "I've used Bloomberg."

## Why companies ask for it

> **Real posting (Street Neon, Institutional Research, Mumbai):** "Familiarity with financial databases such as Bloomberg, Capital IQ, Refinitiv, FactSet."

> **Real posting (Acuity, Model Risk):** data sources "Bloomberg / Refinitiv / MSCI / Markit / CapIQ."

Roles: **equity/credit research associate, IB analyst, PE/VC associate, buy-side analyst, model-risk and market-risk analysts, KPO/research at Acuity, Moody's, MSCI, Evalueserve.** These are the terminals the whole capital-markets industry runs on; the JD uses "familiarity with" as a polite filter for people who've never touched one.

## What "proficient" looks like

You can, without a manual: pull a security's description and financials, build a trading comps set, chart relative performance, run an equity screen, and — crucially — **pull the data into Excel** with the add-in so a model refreshes live. On Bloomberg specifically, you know the **function-then-`<GO>`** grammar and a dozen core mnemonics.

## How to actually learn/do it

### Bloomberg Terminal

Grammar: type a **ticker + yellow market key** (e.g. `AAPL US <Equity>`), then a **function mnemonic**, then hit **`<GO>`** (the green key). `HELP HELP` opens live chat with Bloomberg staff — free, 24/7, the best learning shortcut there is.

| Function | Does |
|---|---|
| **DES** | Company/security description — the front page |
| **FA** | Financial Analysis — full financials, ratios, segments |
| **GP** | Line chart (GIP intraday, G historical) |
| **RV** | Relative Value — comparable companies table |
| **EQS** | Equity Screening — build a rules-based screen |
| **SRCH** | Fixed-income / bond search |
| **PORT** | Portfolio & risk analytics |
| **BQL / FLDS** | Bloomberg Query Language; field finder |
| **N / CN** | News; company news |
| **WEI / ECO** | World equity indices; economic calendar |

**Excel add-in (the part that matters for a modelling job):**
- `=BDP("AAPL US Equity","PX_LAST")` — one current value (Bloomberg Data Point).
- `=BDH("AAPL US Equity","PX_LAST","1/1/2025","6/30/2026")` — a history series (Data History).
- `=BDS(...)` — bulk/set data (e.g. all holders).
- **BQL** for complex screens/aggregations in one formula.
Master `BDP`/`BDH` and you can wire a live comps sheet in minutes.

**Free/cheap access:** the **Bloomberg Market Concepts (BMC)** e-learning course (~8 hours, ~₹1,600 / paid but often free through a university) gives a **certificate** you list on the resume and teaches the exact functions above. Many Indian B-school libraries and some public libraries have a terminal — book an hour.

### Refinitiv (LSEG) Eikon / Workspace

Eikon is being replaced by **Workspace**. It's more **search-bar and app-driven** than Bloomberg's command line — type a company name, open the Company Overview app. Excel add-in functions: **`=TR(...)`** and the newer **`=RDP.Data(...)`**, plus a point-and-click **"Build Formula"** wizard so you don't memorise field names. Best for: **FX, fixed income, commodities, and news** (Reuters), and often cheaper than Bloomberg, so common in Indian KPOs.

### FactSet

Menu/workstation-driven rather than command-line; strong at **portfolio analytics, quant screening (Universal Screening), and clean, presentation-ready comps/tearsheets**. Excel add-in: **`=FDS(...)`** codes and the FactSet ribbon. Loved by buy-side and IB for its Excel/PowerPoint model-building tools.

### S&P Capital IQ (CapIQ / CIQ)

Web platform + the killer **Excel plug-in** (`=CIQ(...)`). Best for **screening, trading & transaction comps, and credit**:
- **Screening**: build a universe (sector, geography, size, metrics) → export.
- **Comps**: pull a company → "Comparable Companies" / "Precedent Transactions" (M&A deals) → export the whole table to Excel.
- The CIQ Excel formulas let you build a bankers' comps sheet that refreshes.
CapIQ is the standard for **PE/M&A/credit** shops in India.

### Preqin

The **private-markets** database — **PE, VC, private credit, real assets, infrastructure**: fund performance (IRR/TVPI), fund managers (GPs), LPs, and deal/fundraising data you cannot get from public terminals. Named on PE/fund-of-funds and placement-agent JDs.

### Free / cheap alternatives to practise on (India-first)

| Paid tool | Free stand-in |
|---|---|
| Bloomberg/CapIQ **screener** | **Screener.in**, **Tijori Finance**, **TradingView** screener |
| Company financials / filings | **Screener.in**, **NSE**/**BSE** corporate filings, **MCA**, company IR pages |
| Charts (GP) | **TradingView**, NSE charts |
| Macro (ECO) | **RBI**, **MOSPI**, **FRED**, **Trading Economics** |
| Bond search (SRCH) | **NSE/BSE debt**, RBI, **CCIL** |
| Global fundamentals | **stockanalysis.com**, SEC **EDGAR**, **Financial Modeling Prep** free API |

Build a comps table in Screener.in, then you can honestly say you understand the *workflow* — and add the **BMC certificate** to prove terminal literacy.

## How it shows up in interviews

**Q: "You need a quick trading-comps set for a listed FMCG company on Bloomberg — walk me through it."**
A: "I'd load the ticker with `<Equity><GO>`, open **DES** to confirm it's the right entity, then **RV** for the peer relative-value comps, or **EQS** to build a custom peer screen on sector, size and margin. To model it, I'd pull the same fields into Excel with `BDP` for current multiples and `BDH` for history, so the sheet refreshes."

**Q: "Bloomberg vs Capital IQ — when do you reach for which?"**
A: "Bloomberg for live markets, fixed income, FX and news, and anything real-time. Capital IQ for deep screening, trading and precedent-transaction comps, and credit work — its Excel plug-in and precedent-transactions database are stronger for M&A modelling. FactSet sits between them and is best for portfolio analytics and polished tearsheets; Preqin for private-markets data neither of the others has."

**Q: "You don't have a terminal — how do you keep your skills current?"**
A: "I completed **Bloomberg Market Concepts**, so I know the DES/FA/GP/EQS grammar and the `BDP`/`BDH` add-in. For live practice I use Screener.in and TradingView to build comps and screens, and NSE/BSE and MCA for filings — same workflow, no licence."

## ATS keywords to add

Bloomberg Terminal, Bloomberg Market Concepts (BMC), BDP, BDH, BQL, DES, FA, EQS, Refinitiv Eikon, Refinitiv Workspace, LSEG, FactSet, S&P Capital IQ, CapIQ, CIQ Excel plug-in, Preqin, financial databases, trading comparables, precedent transactions, equity screening, comps analysis, market data, TradingView, Screener.in
