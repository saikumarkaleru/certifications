# Terminal Orientation: Bloomberg & Capital IQ Function Drills

## What you'll be able to do

Sit down at a Bloomberg terminal cold and drive it: pick the right asset class with the yellow keys, load a ticker, run the core functions an analyst uses every day (DES, FA, GP, EQS, RV, BICS, WACC, BETA), and read the screens fast enough to answer a "what's this company worth and how's it trading" question in five minutes. You'll also know where the same things live in S&P Capital IQ (CapIQ) so you can switch platforms without re-learning. By the end you can look up Infosys, read its description, financials and price chart, and pull a peer set — the raw material for every model in this guide.

## The drill — step by step

**1. The yellow keys (market sectors).** The keyboard's yellow keys set the asset class so the terminal knows what "INFO" means. The ones you'll touch: `EQUITY` (stocks), `GOVT` (sovereign bonds), `CORP` (corporate bonds), `CMDTY` (commodities), `CRNCY` (FX), `INDEX`, `MMKT` (money markets), `MTGE`. The workflow is always: **type the name → press the yellow key → press `<GO>`.**

`<GO>` (the green key) executes. `<HELP>` once explains the current screen; `<HELP><HELP>` (twice) opens live chat with the Bloomberg help desk — genuinely useful, a real person answers.

**2. Load a security.** Type `INFO` then press `EQUITY`. The autocomplete/ticker-lookup drops a match list. Infosys trades in several places, so you disambiguate by exchange code:

| What you type | Meaning |
|---|---|
| `INFO IN <EQUITY> <GO>` | Infosys, NSE India listing (`IN` = India) |
| `INFO US <EQUITY> <GO>` | Infosys ADR on NYSE |
| `INFY IN <EQUITY>` | also resolves (ticker vs. short name) |

`IN` is the Bloomberg country/exchange code for India. If you don't know the ticker, type the company name and hit `EQUITY <GO>` — the security-finder (SECF) list appears; arrow down and Enter.

**3. Now run the core functions.** Once a security is loaded, you just type the mnemonic and `<GO>`; it applies to the loaded ticker. Drill them in this order:

- **`DES <GO>`** — Description. Business summary, sector, key execs, listing details, GICS/BICS classification, a snapshot of price and market cap. Your first stop on any name.
- **`FA <GO>`** — Financial Analysis. The workhorse. Tabs across the top: Income Statement (IS), Balance Sheet (BS), Cash Flow (CF), Ratios, Segments, Multiples. Change the period toggle to Annual/Quarterly and the currency (INR/USD). This is where you read 5 years of P&L.
- **`GP <GO>`** — Graph Price. Candlestick/line price chart. Change the range with the field boxes (`1D`, `1M`, `1Y`, `5Y`). `GIP` = intraday, `GPO` = price only.
- **`GPO`, `HP`** — `HP` (Historical Prices) is the tabular price history you'd export.
- **`EQS <GO>`** — Equity Screening. Build a peer/universe screen with criteria (country = India, BICS sub-industry = IT Consulting & Services, market cap > $5bn). Returns a list you can save — this seeds your comps set.
- **`RV <GO>`** — Relative Value. Auto-builds a comparable-companies grid for the loaded name (EV/EBITDA, P/E, growth) against a peer group Bloomberg guesses; you can edit the peers. This is a pre-baked comps table.
- **`BICS`** — Bloomberg Industry Classification. Used inside EQS/RV to define the peer universe (Bloomberg's answer to GICS).
- **`WACC <GO>`** — Weighted Average Cost of Capital. Bloomberg's computed cost of equity (via CAPM), cost of debt, capital weights, and blended WACC. Read it, don't trust it blindly — check the inputs.
- **`BETA <GO>`** — regression of the stock vs. its index (adjusted/raw beta, R²). Set the index to NSE Nifty for an Indian name.
- **`CN <GO>`** — Company News. `TOP <GO>` = top market news.
- **`PORT <GO>`** — Portfolio & Risk Analytics (needs a saved portfolio).
- **`FLDS <GO>`** — field finder; searches every data field name (needed later for Excel BDP).

Navigation muscle memory: the **red `<CANCEL>`** stops a running query; **`<MENU>`** (or the left-arrow) goes back one screen; **`PANEL`/green arrows** cycle between the four screen panels; `1<GO>`…`4<GO>` open a function on a numbered panel.

**4. Capital IQ (the cheaper, web-based cousin).** CapIQ is browser-based, not a keyboard terminal. Layout is a left-nav of modules:

- **Companies** — search a company → a company profile with tabs: Tearsheet, Financials, Comparable Companies, Transactions, Estimates, Ownership.
- **Screening** — the EQS equivalent; build company/transaction screens with a criteria builder.
- **Comps** — pre-built comparable-company templates you clone.
- **Transactions** — M&A/precedent-deal database (used in Chapter 4).
- **Tearsheet** — a one-page company summary (description, financials, multiples) you can export to PDF/Excel — the standard "hand this to the MD" page.

Same job, different door: Bloomberg `DES` ≈ CapIQ company profile; `FA` ≈ CapIQ Financials tab; `RV`/`EQS` ≈ CapIQ Comps/Screening; deal work ≈ CapIQ Transactions.

**Worked example — Infosys in five screens:**
1. `INFO IN EQUITY <GO>` → loads.
2. `DES <GO>` → read: "Infosys Ltd, IT consulting, HQ Bengaluru, mkt cap ≈ ₹6.5 lakh cr / ~$78bn, ADR: INFY US."
3. `FA <GO>` → IS tab, Annual, INR → note FY revenue ≈ ₹1.53 lakh cr, EBIT margin ≈ 21%.
4. `GP <GO>`, set 5Y → see the multi-year price trend.
5. `RV <GO>` → peer grid vs. TCS, Wipro, HCLTech — read Infosys EV/EBITDA vs. peer median.

## The output

Your "orientation output" is a filled scratch sheet — one row per function, so you can answer a snap valuation question:

| Function | Field read | Infosys value (illustrative) |
|---|---|---|
| DES | Sector / mkt cap | IT Services / ~$78bn |
| FA (IS) | Revenue / EBIT margin | ₹1.53 lakh cr / ~21% |
| FA (Ratios) | ROE | ~30% |
| GP 5Y | Trend | up, cyclical dips |
| BETA | Adj. beta vs Nifty | ~0.7 |
| WACC | Blended WACC | ~11–12% |
| RV | EV/EBITDA vs peer median | e.g. 18x vs 16x → slight premium |

## Checks & gotchas

- **Wrong yellow key = wrong or no security.** `INFO` alone means nothing; `INFO EQUITY` does. Always press the sector key.
- **Which listing?** ADR (`US`) vs. local (`IN`) have different currency, price and multiples. State which one you're using.
- **Currency & scale on FA.** Toggle INR vs. USD deliberately; Indian filings are often in ₹ crore — confirm the units box before you quote a number.
- **WACC/BETA are model outputs, not gospel.** Bloomberg's beta window and index choice drive the number — check the regression index is Nifty, not S&P 500, for an Indian name.
- **RV peers are auto-picked.** Bloomberg's default peer set will include names you'd reject; you must curate (Chapter 3).

## Interview drill

**Q: "Walk me through the first three things you do on a Bloomberg when handed a new ticker."**
A: "Load it with the right yellow key, run `DES` to understand the business, size and classification, then `FA` to read the last few years of income statement, margins and returns. `GP` for the price trend. That tells me what it does, how it earns and how the market's treating it before I touch a model."

**Q: "What's the difference between EQS and RV?"**
A: "`EQS` is a screener — I define criteria and it returns a universe. `RV` is relative-value — it takes the loaded name and builds a comps grid against a peer group, showing valuation multiples side by side. EQS finds the peers; RV compares them. In CapIQ these are the Screening and Comparable Companies modules."

**Q: "Bloomberg vs. Capital IQ — when would you reach for which?"**
A: "Bloomberg for live markets, fixed income, FX, real-time news and speed once you know the mnemonics. CapIQ for deep private-company data, M&A/transaction comps and clean Excel-exportable tearsheets. Most desks use both."

## Practise free

You can rehearse 80% of this without a terminal:
- **Bloomberg Market Concepts (BMC)** — Bloomberg's own ~8-hour paid-but-cheap e-course (often free via a college/library licence); teaches the mental model and mnemonics.
- **Screener.in** — India's best free `FA` substitute: 10-year P&L, balance sheet, cash flow, ratios per company. Look up Infosys and read exactly what FA shows.
- **Tijori Finance** — free tier gives segment and peer views (an RV-style comps grid).
- **NSE India / BSE India** — official price history and corporate filings (your `HP`/`CN`).
- **TIKR / stockanalysis.com** — free CapIQ-style tearsheets and global comps.
Drill: open Screener.in, pull Infosys, TCS, Wipro, HCLTech side by side, and reproduce the RV table above by hand. That single exercise builds the reading speed the terminal only accelerates.
