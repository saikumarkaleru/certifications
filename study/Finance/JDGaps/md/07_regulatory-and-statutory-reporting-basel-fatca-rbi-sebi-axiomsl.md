# Regulatory & Statutory Reporting: Basel, FATCA/CRS, RBI/SEBI, AxiomSL/OneSumX

## The gap

This is an entire, well-paid domain your six bundles skip. **Regulatory reporting** — the returns banks and financial institutions file with regulators on capital, liquidity, tax residency and transactions — is nothing like management MIS. It has its own standards (**Basel III/IV**), its own tax regimes (**FATCA/CRS**), its own regulator returns (**RBI, SEBI**), and its own dedicated software estate (**AxiomSL, OneSumX, Regnology, Moody's**). Learn the vocabulary and you unlock a market of GCC/BFSI jobs most candidates can't even read the JD for.

## Why companies ask for it

> **Real posting (Luxoft, Finance Tech, Bangalore):** "Regulatory Reporting, General Ledger, Treasury, Liquidity Management, Capital Management, IFRS Reporting, **Basel Reporting** … reg tools: **AxiomSL, Moody's, OneSumX, Regnology**, Oracle Financial Services."

Banks *must* file these returns — it's the law, and errors mean regulatory penalties — so the work is non-discretionary and recession-proof. Every foreign bank, GCC captive (JPMC, Deutsche, Barclays, UBS, HSBC, StanChart, Nomura, Wells Fargo) and consultancy (Luxoft, Capco, TCS, Accenture) staffs large **regulatory-reporting** teams in Mumbai, Bangalore, Pune and Hyderabad. Roles: **regulatory reporting analyst, Basel/RWA analyst, liquidity (LCR/NSFR) reporting, FinCrime/AML tech BA, statutory reporting, tax-operations (FATCA/CRS).** It pays a premium precisely because so few candidates understand it.

## What "proficient" looks like

You can explain **what each return measures and why the regulator wants it**, trace a number from the **GL → data mart → reg-reporting engine → regulator submission**, and speak the platform vocabulary: what an **AxiomSL "run"** is, what **data lineage** and **adjustments** mean, and how validation/EBA-taxonomy filing works.

## How to actually learn/do it

### Basel III / IV — bank capital & liquidity

The global rulebook (from the Basel Committee, implemented in India via **RBI Master Directions**). Two families of ratios:

| Ratio | Formula (essence) | Question it answers |
|---|---|---|
| **CAR / CRAR** | Capital ÷ **RWA** (risk-weighted assets), min ~9% (RBI) + buffers | Enough capital to absorb losses? |
| **CET1** | Common equity ÷ RWA | Highest-quality capital cushion |
| **LCR** | HQLA ÷ 30-day net cash outflows ≥ 100% | Survive a 30-day stress? |
| **NSFR** | Available ÷ Required stable funding ≥ 100% | Funding stable over 1 year? |
| **Leverage ratio** | Tier 1 ÷ total exposure | Backstop independent of risk weights |

**RWA** is the heart of it: each asset gets a **risk weight** (a government bond ~0%, a mortgage ~35%, an unrated corporate ~100%) and RWA = exposure × weight, across **credit, market and operational** risk. **Basel IV** (RBI phasing in from 2025-26) tightens this with the **standardised output floor** capping how far internal models can lower RWA. Reports flow into RBI's **RBS/DSB returns** and, globally, EBA **COREP** (capital) and **FINREP** (financial) taxonomies.

### FATCA / CRS — tax-residency reporting

- **FATCA** (US law) — financial institutions identify **US persons** and report their accounts (via the CBDT/IRS route in India).
- **CRS** (OECD Common Reporting Standard) — the multilateral version: identify account holders' **tax residencies** and report to their home tax authority.
Operationally it's **self-certification, indicia search, and Form 61B** filing to the Indian income-tax department. Named on **tax-operations and KYC** JDs.

### RBI & SEBI returns

- **RBI:** the **DSB (Off-site Surveillance) returns**, **RBS** (Risk-Based Supervision) data, CRR/SLR, priority-sector, and the **CIMS / XBRL** filing portal that replaced the old RBI XBRL site.
- **SEBI:** for AMCs/brokers/AIFs — periodic filings, **SCORES**, half-yearly and disclosure returns via exchange portals.

### FEMA (corporate cross-border)

The exchange-control law behind foreign investment/borrowing filings — **FC-GPR** (shares issued to non-residents), **FC-TRS** (transfer), **ECB** returns, all now on the RBI **FIRMS** portal. Shows up on controllership JDs at companies with foreign shareholders.

### The reg-reporting platforms

You won't buy these, but you must speak them:

| Platform | Note |
|---|---|
| **AxiomSL (ControllerView)** | Market leader; ingests source data, applies rules, produces regulator-ready returns with full **lineage** |
| **Wolters Kluwer OneSumX** | Basel, liquidity, COREP/FINREP |
| **Regnology (BearingPoint Abacus)** | European Basel/statistical reporting |
| **Moody's** | Credit/regulatory analytics |
| **Oracle Financial Services (OFSAA)** | Analytics + reg reporting |

**How the workflow actually runs (AxiomSL mental model):** source systems (GL, loans, deposits) → a **data-ingestion layer** (mapping, validation) → **business rules / classification** (assign risk weights, HQLA categories) → a **"run"** that produces the return → **validation rules** (regulator's edit checks) and **manual adjustments** with sign-off → **submission** in the regulator's format (XBRL/taxonomy). The BA's job is **data mapping, lineage, reconciliation** (report ties back to GL) and clearing validation breaks.

**Free ways to build credibility (no licence needed):**
- Read the **RBI Master Direction on Basel III Capital** and one **RBI DSB return** format — both free on rbi.org.in.
- Read the **EBA** COREP/FINREP overview (free).
- Download a real bank's **Pillar 3 / Basel disclosures** (in every bank annual report) and read how CAR, LCR, NSFR and RWA are presented — that's the *output* of the whole machine.
- Study the **Form 61B / CRS** guidance on the income-tax site.
- Optional paid credentials that read well: **FRM** (GARP), or a "regulatory reporting" micro-course.

## How it shows up in interviews

**Q: "What does LCR measure and where does the data come from?"**
A: "LCR is High-Quality Liquid Assets divided by total net cash outflows over a 30-day stress, and it must be at least 100% — can the bank survive a month-long run without central-bank help. HQLA is mostly cash, central-bank reserves and government bonds; the outflows are stressed run-off rates on deposits and wholesale funding. The data comes from the deposit and treasury systems into the GL and the reg-reporting engine, where each item is bucketed by HQLA level and run-off rate."

**Q: "Walk me through how a Basel capital return is produced in a tool like AxiomSL."**
A: "Source data — loans, exposures, collateral, ratings — is ingested and mapped to the reporting model. Business rules assign each exposure its asset class and risk weight to compute RWA across credit, market and operational risk. A run aggregates capital over RWA to produce CET1, Tier 1 and CAR, populates the return, then validation rules — the regulator's edit checks — flag breaks. We reconcile the total back to the GL, book any approved adjustments with sign-off, and submit in the required taxonomy. Throughout, lineage lets us trace any reported number back to source."

**Q: "FATCA vs CRS?"**
A: "Both report financial-account information for tax purposes. FATCA is US-specific — identify and report US persons' accounts. CRS is the OECD multilateral standard covering all participating jurisdictions — you determine each holder's tax residencies and report to their home authorities. In India both run on customer self-certification and indicia checks, filed to the income-tax department via Form 61B."

## ATS keywords to add

Regulatory reporting, Basel III, Basel IV, CAR, CRAR, CET1, RWA, risk-weighted assets, LCR, NSFR, liquidity reporting, capital adequacy, COREP, FINREP, Pillar 3, FATCA, CRS, Form 61B, RBI returns, DSB returns, RBS, CIMS, SEBI reporting, FEMA, FC-GPR, FC-TRS, ECB reporting, AxiomSL, OneSumX, Regnology, Moody's, OFSAA, data lineage, data mapping, reconciliation, statutory reporting
