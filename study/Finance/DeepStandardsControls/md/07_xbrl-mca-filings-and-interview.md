# XBRL, MCA/ROC Filings & Standards Interview Drills + Cheat-Sheet

## What you'll be able to do
Explain what **XBRL** is and why regulators use it, **tag** a financial-statement line item to a taxonomy element with the right context/unit/decimals, know **which companies must file in XBRL** and via which MCA forms, prepare the flow for the two headline **ROC filings — AOC-4 (financials)** and **MGT-7 (annual return)** — and know their due dates and taxonomy. Then you'll have a bank of **standards & controls interview drills** with strong answers, and a one-page **cheat-sheet of standard numbers and key GAAP/IFRS differences** to revise the night before.

## The essentials

**XBRL (eXtensible Business Reporting Language)** is an XML-based, machine-readable format for financial data. Instead of a PDF, each number carries a **tag** from a **taxonomy** (a dictionary of reporting concepts) so regulators can aggregate and compare across companies automatically. Core pieces:
- **Element / concept** — e.g. `Revenue from operations`.
- **Context** — *who* (entity) and *when* (instant for balance-sheet items, duration for P&L) plus dimensions.
- **Unit** — INR, shares, pure (for ratios/percentages).
- **Decimals / precision** — how exact the value is (e.g. `-5` = rounded to lakhs, `-7` = crores).
- **Instance document** — the actual tagged data file that gets validated and filed.
- **Extension** — where a company adds a concept the base taxonomy lacks (US GAAP allows liberal extensions; MCA's taxonomy is far more restricted).

MCA uses the **C&I (Commercial & Industrial) Ind AS / AS taxonomy**. SEBI/exchanges also require XBRL for listed-company disclosures.

**Who must file financials in XBRL with MCA (India):** (a) all **listed** companies and their Indian subsidiaries; (b) companies with **paid-up capital ≥ ₹5 crore**; (c) companies with **turnover ≥ ₹100 crore**; (d) all companies required to prepare accounts under **Ind AS**. Exemptions: banking, insurance, NBFC, power companies (they have their own regimes).

**The two headline ROC filings:**

| Form | What it is | Due date | Attachments |
|---|---|---|---|
| **AOC-4 / AOC-4 XBRL / AOC-4 CFS** | Financial statements + Board's report | Within **30 days** of AGM | Balance sheet, P&L, cash flow, notes, auditor's report, Board's report; XBRL instance if applicable |
| **MGT-7 / MGT-7A** | Annual return (shareholding, directors, meetings) | Within **60 days** of AGM | List of shareholders, KMP, MGT-8 (certification) for large cos |

AGM must generally be held within **6 months** of financial year-end (Sept 30 for a March year-end). **MGT-7A** is the abridged annual return for small companies and OPCs.

## Hands-on — step by step

**Tagging a line item in XBRL (MCA C&I taxonomy).** You're tagging *Revenue from operations = ₹1,250.75 crore* for FY 1-Apr-2025 to 31-Mar-2026, entity CIN L12345MH2010PLC000000.

1. **Prepare validated financials** in the notified Schedule III format.
2. **Open the MCA XBRL conversion tool** (or a certified third-party tool like IRIS, Webtel, DataTracks).
3. **Map the line** "Revenue from operations" to the taxonomy element `RevenueFromOperations` (period type: **duration**).
4. **Set the context** — entity = CIN; period = 2025-04-01 to 2026-03-31 (a *duration* because P&L; a balance-sheet item like `Equity` would use an *instant* = 2026-03-31).
5. **Set unit** = `INR`; **value** entered in the base reporting unit. If reporting in crore, enter 12507500000 (rupees) or set **decimals = -7** to signal crore-rounding — follow the tool's scale convention exactly.
6. **Tag prior-year comparative** (FY25) with its own context.
7. **Generate the instance document**, then **run MCA validation** (checks taxonomy compliance, mandatory tags, arithmetic — e.g. Assets = Liabilities + Equity).
8. **Pre-scrutiny** on the MCA/MCA21 V3 portal, attach to **AOC-4 XBRL**, affix DSC of director + practising professional, pay fee, submit; note the **SRN**.

**Filing flow — AOC-4 & MGT-7 (March year-end):**
1. FY ends **31-Mar-2026**. 2. Finalise & audit accounts. 3. Board approves. 4. **AGM by 30-Sep-2026.** 5. File **AOC-4 (XBRL)** by **~30-Oct-2026** (30 days post-AGM). 6. File **MGT-7** by **~29-Nov-2026** (60 days post-AGM). 7. Late filing → **₹100/day per form, no cap**.

## The output

**A tagged fact (instance-document extract, simplified):**
```
<in-capmkt:RevenueFromOperations
   contextRef="FY2026"      <!-- entity CIN + duration 2025-04-01..2026-03-31 -->
   unitRef="INR"
   decimals="-7">12507500000</in-capmkt:RevenueFromOperations>
```

**Filing calendar output (FY 2025-26, March year-end):**

| Milestone | Date |
|---|---|
| Financial year-end | 31-Mar-2026 |
| Last date for AGM | 30-Sep-2026 |
| AOC-4 (XBRL) due | ~30-Oct-2026 |
| MGT-7 due | ~29-Nov-2026 |
| Penalty if late | ₹100/day/form, uncapped |

## Checks, gotchas & red flags
- **Context type must match the concept:** balance-sheet items are **instant** (a date), P&L/cash-flow items are **duration** (a period). Swapping them fails validation.
- **Decimals/scale errors** are the classic XBRL bug — a value tagged at the wrong scale reports ₹1,250 as ₹1,250 crore or ₹12.5. Always reconcile the tagged instance back to the signed PDF.
- **Sign convention:** expenses and contra items may need negatives — check the element's balance attribute.
- **Don't over-extend:** MCA's taxonomy allows very limited extensions; forcing custom tags gets rejected. Map to the closest standard element.
- **AOC-4 vs AOC-4 CFS:** consolidated financials need the separate **CFS** form; a company with subsidiaries filing only standalone is non-compliant.
- **AGM date drives everything** — the 30/60-day clocks run from the *actual* AGM date, not the year-end.

## Standards & controls interview drills

**Q1. Company reporting in INR crore — how do you make sure the XBRL number is right?** The tagged value must reconcile exactly to the audited statement. I confirm three things: the **element** (correct concept), the **context** (instant vs duration, correct period/entity), and the **unit + decimals/scale** so ₹1,250.75 crore isn't mis-scaled. Then I run MCA validation (arithmetic checks like Assets = Equity + Liabilities) and tie the instance back to the signed PDF line by line before pre-scrutiny.

**Q2. Walk me from year-end to filed annual accounts for an Indian company.** Close and audit the books → Board approves financials and Board's report → hold the AGM within 6 months of year-end (by 30 Sep for a March close) → within **30 days** of AGM file **AOC-4** (XBRL if the company is listed, ≥₹5 cr capital, ≥₹100 cr turnover, or Ind AS) → within **60 days** file **MGT-7**. Late filing is ₹100/day per form with no cap, so the AGM date governs the whole calendar.

**Q3. Why do regulators mandate XBRL instead of PDFs?** Because XBRL is machine-readable: every number carries a taxonomy tag with context and unit, so the regulator can validate arithmetic automatically, aggregate across thousands of filers, and run comparisons and red-flag analytics without manual re-keying. It improves data quality and comparability — the trade-off is tagging discipline (right element, context type, and scale).

**Q4. Difference between a provision and a contingent liability, and where does each appear?** A provision meets all three recognition tests — present obligation, probable outflow, reliable estimate — so it's **booked** on the balance sheet (IAS 37 / Ind AS 37). A contingent liability is only a possible obligation, or can't be reliably measured, so it's **disclosed in the notes**, not recognised. The line is "probable and measurable" versus "possible."

## Cheat-sheet — standard numbers & key differences

**IFRS / Ind AS quick map** (Ind AS = 100 + IFRS/IAS no. in most cases):
| Topic | IFRS/IAS | Ind AS |
|---|---|---|
| Presentation | IAS 1 | Ind AS 1 |
| Inventories | IAS 2 | Ind AS 2 |
| Cash flows | IAS 7 | Ind AS 7 |
| Income taxes | IAS 12 | Ind AS 12 |
| PP&E | IAS 16 | Ind AS 16 |
| Employee benefits | IAS 19 | Ind AS 19 |
| Provisions/contingencies | IAS 37 | Ind AS 37 |
| Intangibles | IAS 38 | Ind AS 38 |
| Financial instruments | IFRS 9 | Ind AS 109 |
| Revenue | IFRS 15 | Ind AS 115 |
| Leases | IFRS 16 | Ind AS 116 |
| Consolidation | IFRS 10 | Ind AS 110 |
| Fair value | IFRS 13 | Ind AS 113 |

**US GAAP counterparts:** Revenue **ASC 606**, Leases **ASC 842**, Financial instruments **ASC 320/326 (CECL)**, Income taxes **ASC 740**, Consolidation **ASC 810**.

**Key differences (memorise):** LIFO — US allows, IFRS bans. Revaluation of PP&E — IFRS yes, US no. Impairment reversals — IFRS yes (not goodwill), US never. Development costs — IFRS capitalises if criteria met, US expenses R&D. DB remeasurements — IFRS OCI (no recycling), US corridor to P&L. Deferred tax — never discounted (both). Provisions — never confused with contingent liabilities (booked vs disclosed).

**India filing numbers:** AOC-4 = **30 days** post-AGM; MGT-7 = **60 days**; AGM = within **6 months** of year-end; XBRL thresholds = listed / ₹5 cr capital / ₹100 cr turnover / Ind AS; late fee = **₹100/day/form, uncapped**.

## Learn/practise (free)
- **MCA XBRL portal** (mca.gov.in/XBRL) — free taxonomy, filing manual, and business rules; download a live company's AOC-4 XBRL instance and read the tags.
- **IFRS Foundation** free taxonomy viewer and **SEC EDGAR** (free US XBRL filings) — compare how the same concept is tagged.
- **ICAI** Ind AS material and **MCA notified taxonomy** — free.
- Rehearse: take any listed company's annual report, pick ten P&L/BS lines, and hand-map each to its taxonomy element with the correct context type and scale; then reconcile to the PDF. Doing this once teaches XBRL faster than any lecture.
