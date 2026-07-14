# The Regulatory Reporting Landscape

## What you'll be able to do

After this chapter you can walk into a reg-reporting interview and correctly answer "who regulates whom, and what do they want filed?" You will be able to draw the four-layer reporting stack (prudential, statistical, transaction, tax), name the actual return/filing that lives in each layer for an Indian bank or NBFC, map the same layer to its global equivalent (US, UK, EU), and explain in one clean sentence why a bank spends crores on this function instead of treating it as a back-office afterthought. You will also know where the jobs are, what they pay in India in 2026, and the certifications that move your CV to the top of the pile.

## The essentials

Regulatory reporting is the machinery by which a regulated financial firm proves — on a fixed calendar, in a fixed format — that it is solvent, liquid, honest about its transactions, and compliant with tax-information rules. It is not accounting. Accounting answers "what did we earn?"; reg reporting answers "are you safe, and are you telling the state everything it is entitled to know?"

**Who regulates whom in India (2026):**

| Regulator | Regulates | Core reporting concern |
|---|---|---|
| RBI (Reserve Bank of India) | Banks, NBFCs, payment banks, ARCs, AD dealers | Capital, liquidity, asset quality, statistical returns |
| SEBI | Stock exchanges, brokers, MFs, AIFs, PMS, RIAs, merchant bankers | Investor protection, conduct, systemic risk |
| IRDAI | Life/general/health insurers, reinsurers, brokers | Solvency margin, policyholder protection |
| PFRDA | NPS, pension funds, points of presence | Pension corpus safety, subscriber reporting |
| IFSCA | All financial activity inside GIFT City IFSC | Unified regulator for the IFSC zone |

RBI, SEBI, IRDAI, PFRDA and IFSCA sit under a coordinating body, the FSDC (Financial Stability and Development Council), chaired by the Finance Minister. FIU-IND (under the Finance Ministry) is the anti-money-laundering reporting hub — CTRs, STRs, CCRs under the PMLA.

**Global counterparts** (you'll meet these in any GCC/global bank in India):

| Region | Prudential | Markets/conduct | Central bank / statistical |
|---|---|---|---|
| US | Fed (FR Y-9C, FFIEC 031/041 Call Report), OCC | SEC, FINRA, CFTC | Federal Reserve |
| UK | PRA (COREP/FINREP under UK rules) | FCA | Bank of England |
| EU | ECB / EBA (COREP, FINREP) | ESMA | ECB, national central banks |

**The four-layer reporting stack** — memorise this; it is the spine of the whole domain:

1. **Prudential** — capital adequacy and liquidity. "Are you strong enough to absorb losses?" Basel III/IV: CAR, CET1, LCR, NSFR, leverage ratio. Filed to RBI (in India), reported via COREP in Europe.
2. **Statistical / supervisory** — granular data the central bank uses to run monetary policy and supervise. RBI's DSB returns, ADF (Automated Data Flow), sectoral credit, BSR (Basic Statistical Returns), CRR/SLR maintenance.
3. **Transaction reporting** — trade-by-trade or account-by-account feeds. Securities transactions (MiFID II / EMIR in EU, CReMS/trade repositories in India), CRILC for large credit exposures, FIU CTR/STR.
4. **Tax information reporting** — FATCA (US), CRS (OECD), TDS/TCS statements, GST returns, SFT (Statement of Financial Transactions, Form 61A).

A single instrument touches several layers at once. A ₹50 crore term loan to a corporate hits prudential (RWA/capital), statistical (sectoral credit return), transaction (CRILC if aggregate exposure ≥ ₹5 crore), and tax (interest TDS). That overlap is precisely why the function is hard and well-paid.

## Hands-on — step by step

Let's build the mental model with a worked mini-example: a small commercial bank, "Meridian Bank," with a ₹1,000 crore balance sheet. Trace one week's reporting obligations.

1. **Identify the regulator.** Meridian is a scheduled commercial bank → RBI is primary. Its treasury also deals in G-secs and forex → SEBI/FEMA touchpoints and RBI's FED.
2. **Map each layer to a concrete deliverable.**
   - Prudential: quarterly CAR/RWA return (RBS/Tranche II data), monthly LCR (Form on liquidity), NSFR quarterly.
   - Statistical: fortnightly Form A (CRR/SLR — Section 42), monthly sectoral deployment of credit, quarterly BSR.
   - Transaction: CRILC (large exposures ≥ ₹5 cr, reported quarterly + weekly for SMA-2/default), FIU CTR by 15th of next month.
   - Tax: quarterly TDS return (26Q), annual SFT (Form 61A) by 31 May, FATCA/CRS by 31 May.
3. **Attach an owner and a deadline to each.** In a real bank this is a "reporting calendar" — a spreadsheet with 200-plus line items, each with regulation reference, frequency, cut-off, maker, checker, and submission portal (RBI's e-Kuber / XBRL / CIMS; SEBI's SI Portal; income-tax reporting portal).
4. **Trace data lineage for one number.** Take LCR's "cash outflows." It pulls retail deposits from the core banking system (CBS), applies run-off factors, and sums. You must be able to say which source table each figure came from — regulators audit lineage.
5. **Reconcile to the GL.** Every prudential number must tie back to the audited general ledger. If RWA-bearing assets in the capital return don't reconcile to loans-and-advances in the balance sheet, the return is wrong.

## The output

A regulator does not want prose; it wants a structured file. The finished artefact of this chapter is a **reporting inventory** — the one document every analyst is handed on day one:

```
MERIDIAN BANK — REGULATORY REPORTING INVENTORY (extract)
Layer         | Return           | Regulator | Freq       | Deadline        | Portal
Prudential    | Capital Adequacy | RBI       | Quarterly  | 21 days from qtr| CIMS/XBRL
Prudential    | LCR              | RBI       | Monthly    | 15th next month | CIMS
Prudential    | NSFR             | RBI       | Quarterly  | 21 days         | CIMS
Statistical   | Form A (CRR/SLR) | RBI       | Fortnightly| 7 days          | e-Kuber
Statistical   | Sectoral credit  | RBI       | Monthly    | 10th next month | CIMS
Transaction   | CRILC            | RBI       | Qtrly+event| 21 days / weekly| CRILC portal
Tax           | FATCA/CRS        | CBDT/IT   | Annual     | 31 May          | Reporting Portal
Tax           | SFT (61A)        | CBDT/IT   | Annual     | 31 May          | Reporting Portal
AML           | CTR              | FIU-IND   | Monthly    | 15th next month | FINGATE
```

That inventory, kept current against circulars, IS the job's foundation.

## Checks, gotchas & red flags

- **The GL is the source of truth.** Every prudential figure must reconcile to audited financials. A return that doesn't tie to the balance sheet is a finding.
- **Deadlines are statutory, not aspirational.** RBI penalises late/incorrect returns; SEBI issues administrative warnings and fines. "T+21 days" means 21 calendar days, not working days, unless the circular says otherwise — check.
- **One transaction, many returns.** The classic error is treating layers as independent. A loan restructuring changes RWA (prudential), asset classification (CRILC/DSB), and provisioning — update all, not one.
- **Circulars change the rules mid-year.** RBI Master Directions are living documents. The red flag is running last quarter's template without checking for an amending circular.
- **"Nil" is still a return.** Many returns require a nil filing when there's nothing to report; silence is a default.

## Interview drill

**Q: A retail deposit and a wholesale deposit of the same size — do they hit regulatory reports differently?**
A: Yes, materially. For LCR, retail/small-business deposits get a low run-off factor (5–10%) because they're "sticky," while unsecured wholesale funding from a financial counterparty gets up to 100% run-off. So the wholesale deposit consumes far more HQLA in the liquidity calculation. For capital they may be identical (deposits aren't risk-weighted assets), but for NSFR the retail deposit gets higher Available Stable Funding weighting. Same rupee value, very different regulatory footprint.

**Q: Why do banks spend so heavily on reg reporting instead of automating it once and forgetting it?**
A: Three reasons. First, the rules change constantly — Basel endgame, RBI Master Direction updates, new FATCA/CRS schemas — so it's a maintenance problem, not a build-once problem. Second, penalties and reputational cost of a wrong return dwarf the cost of doing it well. Third, data lineage: the same number must reconcile across prudential, statistical and tax layers pulled from different systems, and keeping those tied requires ongoing controls, reconciliation, and skilled people.

## Learn/practise (free)

- **RBI website → Notifications → Master Directions** (free): read the Master Direction on Financial Statements and the Basel III capital circular. This is the primary source; everything else is commentary.
- **RBI DBIE / CIMS public data portal** (free): browse the actual statistical returns banks file — you'll see the real formats.
- **BIS.org** (free): the Basel Framework consolidated text, searchable, no paywall.
- **SEBI Intermediaries Portal circulars** and **Income-tax Reporting Portal FATCA/CRS guidance notes** (free PDFs).
- Rehearse by building your own reporting inventory (as above) for a fictional bank in Excel, one row per return, sourced from real RBI circulars. This single artefact demonstrates domain fluency better than any certificate.

**Career/pay angle (India, 2026):** Reg-reporting analysts sit in bank finance, GCC captive centres (JPMorgan, Deutsche, Nomura, UBS in Bengaluru/Mumbai/Pune), and Big-4 risk advisory. Entry analyst: ₹6–11 lakh; 3–5 yr with COREP/Basel exposure: ₹14–24 lakh; AVP/manager: ₹25–45 lakh. The differentiators that raise pay: hands-on COREP/FINREP or RBI ADF experience, Axiom/Vermeg/OneSumX tooling, and the ability to reason about a number's lineage. FRM and the RBI/IIBF certifications help; SQL + a prudential mind help more.
