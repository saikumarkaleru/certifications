# The Three Frameworks: US GAAP vs IFRS vs Ind AS

## What you'll be able to do

Sit in a GCC / Big-4 / treasury seat and instantly answer three questions any reviewer will fire at you: *which* rulebook governs a set of financials, *why* that one applies, and *what* the equivalent standard is in the other two. You will be able to read a filing footnote ("prepared under US GAAP" / "IFRS as issued by the IASB" / "Ind AS notified under the Companies Act") and know the reporting boundaries, restatement risk, and the carve-outs that make Ind AS *not quite* IFRS. You will be able to build a standard-numbering crosswalk so that when a US parent asks for an "ASC 842 memo" and your India team knows it as "Ind AS 116," nobody talks past each other.

## The essentials

**Three rulebooks, three issuers.**

| Framework | Issuer | Style | Primary users |
|---|---|---|---|
| **US GAAP** | FASB (Financial Accounting Standards Board), codified as **ASC** (Accounting Standards Codification) | Rules-based, bright lines, industry guidance | SEC registrants (US-listed cos), most private US cos |
| **IFRS** | IASB (International Accounting Standards Board) | Principles-based, judgement-heavy | 140+ jurisdictions: EU, UK, Gulf, Singapore, Australia, most of Asia/Africa |
| **Ind AS** | MCA/ICAI, converged with IFRS, notified under Companies (Ind AS) Rules 2015 | IFRS with **carve-outs / carve-ins** | Larger Indian companies (see applicability) |

**When each applies.**

*US GAAP* — mandatory for domestic SEC filers. Foreign private issuers may file under IFRS-as-issued-by-IASB without reconciliation. There is no "size threshold"; it's about being in the US reporting net.

*IFRS* — a jurisdiction *adopts* it (or mandates it for listed entities). "IFRS as issued by the IASB" is the pure form; the "EU-endorsed IFRS" is IFRS minus what the EU hasn't carved in (historically the IAS 39 "carve-out").

*Ind AS applicability (the number you must know cold):*

| Phase | Who | From |
|---|---|---|
| Mandatory | Listed cos + unlisted with **net worth ≥ ₹250 cr** | FY 2016-17 / 2017-18 |
| Banks/NBFCs | NBFCs net worth ≥ ₹500 cr (Phase I), ≥ ₹250 cr (Phase II) | FY 2018-19 onward |
| Everyone else | AS (the older Indian GAAP) | — |

Companies below the threshold and unlisted still use **AS** (Accounting Standards), the pre-convergence Indian GAAP. So India actually runs **two** GAAPs in parallel: Ind AS (IFRS-converged) and AS (legacy). Voluntary adoption of Ind AS is allowed but irreversible.

**Convergence, not adoption.** India did *not* adopt IFRS wholesale; it *converged*. Ind AS numbers mirror IFRS with a "1" prefix logic: **Ind AS 1xx ≈ IFRS**, **Ind AS 1–41 range ≈ IAS**. The differences are the **carve-outs** (India removed an IFRS option) and **carve-ins** (India added guidance).

**Carve-outs that matter in interviews:**
- **Ind AS 21 / foreign currency:** option to capitalise exchange differences on long-term foreign-currency monetary items into the cost of a depreciable asset (a legacy relief IFRS doesn't allow).
- **Ind AS 103 (business combinations):** common-control combinations use the **pooling-of-interests** method (IFRS 3 scopes them out entirely).
- **Ind AS 109:** some FVTPL election differences and the treatment of certain financial guarantee contracts.
- **Ind AS 32/109 puttable instruments, and the "bright-line" lease treatments** align but presentation nuances differ.

## Hands-on — step by step

**Task:** A US parent ("ParentCo," SEC filer, US GAAP) has an Indian subsidiary ("IndiaCo," listed, net worth ₹900 cr). You must (a) confirm each entity's framework, (b) list what IndiaCo reports *twice*, (c) build a crosswalk for the group's revenue, lease and financial-instrument standards.

**Step 1 — Classify each entity.**
- ParentCo: SEC filer → **US GAAP (ASC)**.
- IndiaCo: listed + net worth ₹900 cr (> ₹250 cr) → **Ind AS**, statutory.
- For the US consolidation, IndiaCo also prepares a **US GAAP reporting package** ("stat-to-GAAP" conversion). So IndiaCo maintains books once and reports twice.

**Step 2 — Identify the conversion deltas (stat-to-US-GAAP).** The recurring adjustments IndiaCo's controller books each quarter:
- **Ind AS 21 carve-out:** if IndiaCo capitalised FX losses on long-term ECB into a plant's cost, reverse it under US GAAP (US GAAP expenses it). Say ₹40 lakh capitalised → reversing entry increases current-period FX expense, reduces asset & future depreciation.
- **Component depreciation, ECL staging, lease discount rate** differences flow through as top-side adjustments.

**Step 3 — Build the crosswalk table** (below). Map the exact standard trio for each topic the group cares about.

**Step 4 — Worked mini-reconciliation of one delta.** IndiaCo net profit under Ind AS = ₹500 lakh. The only GAAP difference this quarter is the FX capitalisation carve-out (₹40 lakh capitalised under Ind AS, expensed under US GAAP; ignore tax for simplicity).

```
Net profit (Ind AS)                       500
Less: FX loss expensed under US GAAP      (40)
Add back: depreciation on that FX not
   taken under US GAAP (₹40L/10yr)          4
Net profit (US GAAP)                      464
```

That ₹464 lakh is what rolls into ParentCo's consolidation.

## The output

**Standard-numbering crosswalk — the artefact to memorise:**

| Topic | US GAAP (ASC) | IFRS | Ind AS |
|---|---|---|---|
| Presentation of FS | 205/210 etc. | IAS 1 | Ind AS 1 |
| Inventories | ASC 330 | IAS 2 | Ind AS 2 |
| Cash flows | ASC 230 | IAS 7 | Ind AS 7 |
| Income taxes | ASC 740 | IAS 12 | Ind AS 12 |
| PP&E | ASC 360 | IAS 16 | Ind AS 16 |
| **Revenue** | **ASC 606** | **IFRS 15** | **Ind AS 115** |
| **Leases** | **ASC 842** | **IFRS 16** | **Ind AS 116** |
| **Financial instruments** | ASC 320/326 (CECL) | **IFRS 9** | **Ind AS 109** |
| Foreign currency | ASC 830 | **IAS 21** | Ind AS 21 |
| Fair value | ASC 820 | IFRS 13 | Ind AS 113 |
| **Consolidation** | ASC 810 | **IFRS 10** | Ind AS 110 |
| **Business combinations** | ASC 805 | **IFRS 3** | Ind AS 103 |
| Associates (equity method) | ASC 323 | IAS 28 | Ind AS 28 |
| Impairment of assets | ASC 360/350 | IAS 36 | Ind AS 36 |
| Provisions | ASC 450 | IAS 37 | Ind AS 37 |
| Employee benefits | ASC 715 | IAS 19 | Ind AS 19 |

**Reconciliation note (delivered to ParentCo):** "IndiaCo Q net profit ₹500L (Ind AS) reconciles to ₹464L (US GAAP); sole difference is the Ind AS 21 long-term FX capitalisation carve-out, reversed for US GAAP."

## Checks, gotchas & red flags

- **Ind AS ≠ IFRS.** Never tell a client "we're IFRS-compliant" if you're on Ind AS — the carve-outs (common-control pooling, FX capitalisation) break equivalence. Say "Ind AS, converged with IFRS."
- **AS vs Ind AS confusion.** A ₹50 cr unlisted company is on **AS**, not Ind AS. Check net worth and listing status before assuming.
- **CECL vs ECL.** US GAAP financial-instrument impairment is **CECL (ASC 326)** — lifetime losses from day one, no staging. IFRS 9 / Ind AS 109 uses **3-stage ECL**. They are *not* the same model even though both are "expected loss."
- **Numbering trap:** IAS vs IFRS both live under the IASB — IAS are the *older* standards not yet replaced. Don't say "IFRS 21"; foreign currency is **IAS 21**.
- **Net worth is computed per the Rules**, not casual book value — includes securities premium, excludes revaluation reserves and certain items. Verify against the definition before concluding on applicability.

## Interview drill

**Q1: "Our India entity has net worth ₹300 cr and is unlisted. Which framework?"**
A: Ind AS is mandatory — unlisted entities with net worth ≥ ₹250 cr fall in the mandatory net, so ₹300 cr triggers Ind AS. If it were, say, ₹200 cr and unlisted, it would stay on legacy AS. Listing status would force Ind AS regardless of size.

**Q2: "Name two Ind AS carve-outs from IFRS and why they exist."**
A: (1) Ind AS 103 requires **pooling-of-interests for common-control combinations** — IFRS 3 scopes those out, so India added guidance rather than leave a gap; it preserves book values in group restructurings. (2) Ind AS 21 permits **capitalising exchange differences on long-term foreign-currency monetary items** into asset cost — a relief carried over from Indian GAAP to soften P&L volatility for infrastructure/ECB-heavy firms. Both mean Ind AS financials aren't automatically IFRS-compliant.

**Q3: "US parent, IFRS-reporting European sub, Ind AS Indian sub — how many conversions?"**
A: The group consolidates under **US GAAP**. The European sub converts IFRS→US GAAP; the Indian sub converts Ind AS→US GAAP. Two conversion packages, each isolating that framework's deltas (e.g., IAS 21 capitalisation, CECL vs ECL, lease discount-rate policy) as top-side adjustments feeding the parent's consolidation.

## Learn/practise (free)

- **IFRS Foundation** website — standards summaries free; full text needs (free) registration.
- **MCA India** (mca.gov.in) — Ind AS text and Companies (Ind AS) Rules, free and authoritative for applicability.
- **FASB ASC Basic View** — free registration gives read access to the Codification.
- **ICAI** educational materials and "Ind AS vs IFRS" comparison booklets — free PDFs, best single source for carve-outs.
- **Rehearse:** take any listed Indian company's annual report (Ind AS) and a US peer's 10-K, and build the crosswalk yourself for revenue, leases, and financial instruments — then list three reconciling items you'd expect between them.
