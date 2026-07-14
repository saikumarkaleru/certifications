# RBI & SEBI India Returns (Banks, NBFCs, Market Intermediaries)

## What you'll be able to do

You will be able to name the returns an Indian bank, NBFC and SEBI-registered intermediary actually file, describe the RBS/DSB/ADF concept that underpins RBI's data collection, explain what CRILC is and when a weekly filing is triggered, and walk through a reg-reporting analyst's real day — from data extraction to maker-checker to portal submission. You'll produce a filled-in return extract and a reporting calendar so the abstractions become concrete.

## The essentials

**RBI's supervisory architecture.** RBI moved from transaction-by-transaction inspection to **RBS — Risk-Based Supervision**, where the bank's own data feeds drive the supervisor's risk assessment. The data plumbing behind it:

- **DSB returns (Off-site Surveillance)** — the "Domestic Statutory and other returns" set that RBI's off-site monitoring uses. These carry capital adequacy, asset quality, large exposures, profitability. Historically named DSB-I, II, III etc.; now largely subsumed under the **RBS Tranche** data collection.
- **ADF (Automated Data Flow)** — RBI's mandate that returns be generated **straight from source systems** (CBS, treasury, GL) with **no manual intervention**, to guarantee data integrity. An ADF-compliant bank pulls the return from a central data repository, not from someone's spreadsheet.
- **CIMS (Centralised Information Management System)** — RBI's current data-receipt platform (successor to XBRL/e-Data), where most returns are now submitted.

**Key RBI returns for a bank:**

| Return | What | Frequency |
|---|---|---|
| Form A (Section 42) | CRR/SLR maintenance | Fortnightly |
| Form VIII | SLR holdings | Monthly |
| RCA3 / Basel III capital | CAR, RWA, capital tiers | Quarterly |
| LCR / NSFR / LR | Liquidity & leverage | Monthly/Quarterly |
| DSB / RBS Tranche | Off-site risk data | Quarterly |
| CRILC | Large credit exposures | Quarterly + event |
| SLBC / sectoral credit | Priority-sector, deployment | Monthly/Quarterly |
| RLC / FTD | Forex, cross-border | Various |

**CRILC — Central Repository of Information on Large Credits.** Banks report every borrower with **aggregate exposure ≥ ₹5 crore** quarterly. Critically, when an account becomes **SMA-2** (principal/interest overdue 61–90 days) or defaults, a **weekly** report is triggered, and RBI shares it across lenders — so no bank can hide a stressed borrower. SMA classification: SMA-0 (1–30 days overdue), SMA-1 (31–60), SMA-2 (61–90); beyond 90 days it's an NPA.

**NBFC returns.** NBFCs file on RBI's **CIMS/COSMOS** portal depending on layer (RBI's Scale-Based Regulation: Base, Middle, Upper, Top layers). Core returns: **DNBS-01** (financial details, quarterly for deposit-taking/large), **DNBS-02** (prudential norms — CRAR, provisioning), **DNBS-03** (important financial parameters), **DNBS-04A/B** (structural & dynamic liquidity / ALM), **DNBS-10** (statutory auditor certificate, annual), **DNBS-13** (overseas investment). NBFCs also feed CRILC if exposures qualify.

**SEBI reporting for market intermediaries:**

| Entity | Key filings |
|---|---|
| Stock brokers | Enhanced supervision monthly (client funds/securities), quarterly internal audit, half-yearly net worth |
| Mutual funds (AMCs) | Monthly portfolio disclosure, half-yearly, risk-o-meter, expense-ratio, scheme reporting to SEBI |
| AIFs | Quarterly report to SEBI (per category), PPM audit annually, valuation reporting |
| PMS | Monthly reporting to SEBI, quarterly to clients, APMI reporting |
| RIAs | Half-yearly reporting, annual compliance audit |
| Merchant bankers/RTAs | Periodic + event-based (offer documents, complaints — SCORES) |

SEBI filings go through the **SEBI Intermediary Portal (SI Portal)**, exchange platforms (NSE/BSE ENIT), and **SCORES** for grievances.

## Hands-on — step by step

**Task: file a quarter's CRILC for Meridian Bank.** Walk the analyst workflow.

1. **Extract.** Pull all borrowers with aggregate fund-based + non-fund-based exposure ≥ ₹5 crore from the CBS as at quarter-end. Say 120 borrowers, total exposure ₹3,400 crore.
2. **Enrich.** For each: outstanding, sanctioned limit, asset classification (Standard/SMA-0/1/2/NPA), days-past-due, and any restructuring flag. Join borrower CIN/PAN for unique identification across banks.
3. **Apply SMA logic.** One borrower, "Zenith Auto," has interest overdue 68 days → **SMA-2**. This flags a **weekly** reporting obligation for Zenith until it cures or turns NPA.
4. **Reconcile.** Total CRILC exposure must tie to the advances subledger. If CRILC shows ₹3,400 cr but the GL advances (for ≥₹5 cr accounts) show ₹3,380 cr, find the ₹20 cr gap *before* filing — usually an unbooked disbursement or an excluded facility type.
5. **Maker-checker.** Maker prepares the return; an independent checker validates classification and totals; both are logged. This is a hard control, not optional.
6. **Submit.** Upload the schema-validated file to the CRILC module on the RBI portal within the deadline (T+21 days for quarterly; the SMA-2 weekly file every Friday).
7. **Archive & audit trail.** Store the submission acknowledgement, the source extract, and the reconciliation. Auditors and RBI inspection will ask for lineage.

**A reg-reporting analyst's actual day:** morning — run extraction jobs, check overnight data-load failures; mid-morning — reconcile returns to GL, chase breaks with business units; midday — maker-checker sign-offs; afternoon — submit due returns, handle RBI/SEBI queries on prior filings, update the reporting calendar for circular changes; ongoing — improve automation so more returns become ADF-compliant.

## The output

The artefact is the **CRILC submission summary + a reporting calendar row**:

```
MERIDIAN BANK — CRILC QUARTERLY SUBMISSION  Q1 FY27
Total borrowers ≥ INR 5 cr:            120
Aggregate exposure:               INR 3,400 cr   (ties to GL advances ✓)
  Standard:                       INR 3,180 cr
  SMA-0/1:                        INR   150 cr
  SMA-2 (weekly trigger):         INR    40 cr   [Zenith Auto — 68 dpd]
  NPA:                            INR    30 cr
Submission: CIMS/CRILC module  |  Ack: CRILC-2027-Q1-004821  |  Filed: T+18 days ✓

REPORTING CALENDAR (extract)
Return   | Freq        | Cut-off      | Deadline   | Maker | Checker | Portal
CRILC    | Qtrly       | Qtr-end      | T+21 days  | R.Nair| S.Iyer  | CIMS
CRILC-wk | Weekly(SMA2)| Every Friday | Same day   | R.Nair| S.Iyer  | CIMS
Form A   | Fortnightly | Alt Friday   | T+7 days   | K.Rao | S.Iyer  | e-Kuber
```

## Checks, gotchas & red flags

- **CRILC ≥ ₹5 crore is aggregate, not per-facility.** A borrower with three ₹2 cr facilities (₹6 cr total) is in scope. Filtering per-facility understates the return.
- **SMA-2 triggers weekly, not quarterly.** Miss the weekly filing and you've breached a specific RBI requirement designed to catch inter-bank stress early.
- **ADF means no manual touch.** If an analyst edits a return in Excel after extraction, it's no longer ADF-compliant and the integrity claim breaks. Fix the source, not the output.
- **Asset classification must be consistent across returns.** The same account can't be Standard in DSB and SMA-2 in CRILC — RBI cross-checks and inconsistency is a red flag.
- **SEBI net-worth/segregation breaches are event-based.** A broker's client-funds shortfall isn't a "wait for month-end" item; enhanced supervision expects prompt reporting.
- **Nil and event returns still count.** Many SEBI/RBI returns require a nil filing; absence is treated as non-filing.
- **Deadlines are calendar days.** "T+21" almost always means calendar, and a portal outage on the last day is your problem, not the regulator's — file early.

## Interview drill

**Q: What exactly is the ADF mandate and why does RBI insist on it?**
A: Automated Data Flow requires banks to generate regulatory returns directly from source systems — core banking, treasury, GL — into a central repository and out to RBI, with zero manual intervention. RBI insists because manual, spreadsheet-built returns are error-prone and manipulable; if the number is pulled straight from the transaction system, RBI can trust its integrity and rely on it for risk-based supervision. Practically it means the reg-reporting team's job shifts from "keying numbers" to "building and controlling data pipelines and reconciliations."

**Q: A ₹6 crore borrower goes 65 days overdue. Walk me through the CRILC consequence.**
A: At ≥₹5 cr aggregate the borrower is already in the quarterly CRILC. At 65 days overdue it's SMA-2 (the 61–90 day bucket). SMA-2 triggers a weekly CRILC report every Friday until the account either cures below SMA-2 or slips past 90 days into NPA. RBI shares that SMA-2 status with every other lender to the same borrower, so all banks see the stress simultaneously — that early-warning, no-hiding function is the whole purpose of CRILC.

## Learn/practise (free)

- **RBI website → Regulatory Reporting / Master Directions** (free): the CRILC circular, the Scale-Based Regulation framework for NBFCs, and the list of returns with formats.
- **RBI CIMS portal public pages and the "Returns" master list** (free) show the actual return codes (DNBS series, RCA3, Form A).
- **SEBI Intermediaries section + APMI/AMFI circulars** (free) for broker, PMS, AIF and MF reporting formats; the SI Portal user manuals are public.
- Rehearse by downloading a real NBFC's annual report and mapping its disclosures to the DNBS returns that would have produced them; and by building the CRILC extract-reconcile-submit workflow in Excel with dummy data, including the SMA ageing logic (a simple days-past-due formula bucketing into SMA-0/1/2/NPA). That single spreadsheet demonstrates you understand both the rule and the data mechanics.
