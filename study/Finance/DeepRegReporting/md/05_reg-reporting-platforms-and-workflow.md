# Reg-Reporting Platforms & Workflow: AxiomSL, OneSumX, Regnology

## What you'll be able to do

By the end of this chapter you will be able to walk into an interview for a
regulatory-reporting analyst role — the Luxoft / DXC / GCC "Reg Reporting COE"
type of job — and talk credibly about **how the reporting platforms actually
work end-to-end**: how source data is ingested, mapped to a return template,
run through validation rules, reconciled to the general ledger (GL), signed off,
and submitted to the regulator (RBI, PRA, EBA, MAS, HKMA, Fed). You'll know the
names of the three market-leading engines — **AxiomSL (now part of Adenza /
Nasdaq)**, **Wolters Kluwer OneSumW / OneSumX**, and **Regnology (the merged
BearingPoint RegTech + Vizor)** — what each does, where they differ, and what an
analyst's day on them looks like. You will also understand, honestly, that you
**cannot get a personal login** to any of these; they are licensed to banks, so
I'll give you the free way to build the exact same muscle.

## The essentials

A regulatory reporting platform is essentially a **rules engine sitting on top
of a data warehouse**. Its job: take granular bank data, transform it into the
line-items a regulator's template demands, prove the numbers are internally
consistent, and file them in the required electronic format (XBRL, XML, CSV, or
the regulator's proprietary schema).

The three big engines, at a glance:

| Platform | Owner (2026) | Strength | Typical filer |
|---|---|---|---|
| **AxiomSL ControllerView** | Adenza → Nasdaq | Data-integration depth, huge global taxonomy library, transparent lineage | Large global/US banks, foreign-bank branches |
| **OneSumX for Regulatory Reporting** | Wolters Kluwer | Regulatory Update Service (WK's own team maintains the rules), Basel/finance integration | European + APAC banks, insurers |
| **Regnology (Rcloud / ABACUS)** | Regnology | Strong on EBA/ECB granular reporting, AnaCredit, SaaS/cloud, regulator-side tooling | EU banks, and regulators themselves |

Whatever the brand, the pipeline is the **same five stages**:

1. **Ingestion / data sourcing** — pull balances and transactions from the GL,
   sub-ledgers, risk systems, trade/position stores. Usually a nightly batch of
   flat files or a data-mart feed loaded to a staging area.
2. **Mapping to templates** — assign each source record to a regulatory
   line-item using dimensions (product, counterparty type, residual maturity,
   currency, risk weight, IFRS-9 stage). This is the "classification" step.
3. **Validation rules** — run the regulator's published edit checks (EBA calls
   them "validation rules", the Fed "edit checks"): intra-form arithmetic,
   cross-form consistency, sign checks, plausibility ranges.
4. **Reconciliation to GL** — prove the return ties back to audited financials
   (total assets on the return = balance-sheet total assets).
5. **Sign-off & submission** — four-eyes review, maker-checker, attestation by
   an accountable person, then filing in the regulator's channel.

The **Regulatory Update Service** concept matters: because rules change every
quarter, banks pay the vendor to ship updated taxonomies (e.g. EBA DPM 3.x,
RBI's revised ADF/RBS returns) so the analyst maps *once* and the engine applies
the new logic.

## Hands-on — step by step

Let's carry a small worked example through a OneSumX-style workflow, producing a
COREP-style **Own Funds / capital line** and reconciling it. Numbers are ₹ crore
for a fictional foreign-bank branch, "Meridian Bank India".

**Step 1 — Source the data.** The nightly batch lands three staging files:
- `GL_BALANCES.csv` — every GL account with a closing balance.
- `LOANS.csv` — loan-level: borrower, product, rating, exposure, IFRS-9 stage.
- `CAPITAL.csv` — equity, reserves, AT1 instruments.

You load them into the platform's staging schema. In AxiomSL you'd point a
"DataSource" object at the file; in OneSumX you use the "Data Integration Layer".

**Step 2 — Map to the template.** You build (or inherit) a mapping table. Example
rows:

| Source GL code | Description | Reg line-item | Bucket logic |
|---|---|---|---|
| 3001 | Paid-up equity | CET1 – Capital instruments | direct |
| 3100 | Retained earnings | CET1 – Retained earnings | direct |
| 3400 | AT1 perpetual bond | Additional Tier 1 | direct |
| 1200-1299 | Corporate loans | Credit RWA – Corporates | ×100% RW |
| 1300-1399 | Retail loans | Credit RWA – Retail | ×75% RW |

**Step 3 — Compute risk-weighted assets and capital.** Say the mapped totals are:

- CET1 capital = equity 800 + retained earnings 400 − intangibles 50 = **1,150**
- AT1 = **150** → Tier 1 = 1,300
- Tier 2 (sub-debt + eligible provisions) = **200** → Total capital = **1,500**
- Corporate exposure 6,000 × 100% = 6,000 RWA
- Retail exposure 2,000 × 75% = 1,500 RWA
- Operational + market RWA (given) = 2,500
- **Total RWA = 10,000**

**Step 4 — Ratios (the engine fills these cells automatically):**
- CET1 ratio = 1,150 / 10,000 = **11.50%**
- Tier 1 ratio = 1,300 / 10,000 = **13.00%**
- Total Capital Ratio (CRAR) = 1,500 / 10,000 = **15.00%**

**Step 5 — Run validation rules.** The engine fires edit checks such as:
- `v0001`: CET1 ≤ Tier 1 ≤ Total capital → 1,150 ≤ 1,300 ≤ 1,500 ✔
- `v0234`: Total RWA = Σ(credit + market + operational) → 6,000+1,500+2,500 =
  10,000 ✔
- `v0570`: CRAR ≥ regulatory minimum (RBI 11.5% incl. CCB) → 15.0% ✔

Any failing rule throws a blocking error you must clear before submission.

**Step 6 — Reconcile to GL.** Pull "total assets" from the return and compare to
the trial-balance total assets. Suppose return shows 9,850 but GL shows 9,900 —
a **50 crore break**. You drill the lineage: the engine shows the break sits in
"other assets", traced to GL account 1950 that was never mapped. You add the
mapping row, re-run, break = 0. This drill-down is the platform's killer feature:
**data lineage** from the reported cell back to the source transaction.

**Step 7 — Sign-off & submit.** The preparer (you) marks the return "Ready". A
reviewer does four-eyes, checks the variance commentary ("RWA up 300 cr QoQ on
new corporate lending"), and approves. The accountable executive attests. The
engine generates the **XBRL instance** against the regulator's taxonomy and files
it through the channel (for RBI, the CIMS/ADF portal; for EBA, the national
competent authority's collection gateway).

## The output

The finished artefact is the **validated, reconciled return package**:

```
MERIDIAN BANK INDIA — CAPITAL ADEQUACY RETURN (as at 30-Jun-2026)   ₹ crore
--------------------------------------------------------------------------
CET1 capital ...............................  1,150
Additional Tier 1 ..........................    150
Tier 1 capital .............................  1,300
Tier 2 capital .............................    200
TOTAL CAPITAL (eligible) ...................  1,500
Credit risk RWA ............................  7,500
Market risk RWA ............................    900
Operational risk RWA .......................  1,600
TOTAL RWA ..................................  10,000
--------------------------------------------------------------------------
CET1 ratio ........ 11.50%   Tier 1 ....... 13.00%   CRAR ...... 15.00%
Validation: 412 rules run, 0 failures.  GL recon: NIL break.
Preparer: A.Analyst  Reviewer: B.Manager  Attested: C.CFO  Status: SUBMITTED
```

Attached: variance commentary, validation log, and GL reconciliation showing
return total assets = GL total assets = 9,900.

## Checks, gotchas & red flags

- **GL must tie exactly.** A return that doesn't reconcile to audited financials
  is the fastest way to a regulator query. Zero tolerance on the balance-sheet
  total; document any timing differences.
- **Unmapped accounts** silently drop numbers. Always run a "completeness" check:
  Σ(mapped source) = Σ(total GL). Any residual = an unmapped bucket.
- **Sign conventions.** Regulators expect provisions/contra-assets in specific
  signs; a flipped sign passes arithmetic but fails a plausibility rule.
- **Taxonomy version drift.** Filing last quarter's DPM against this quarter's
  gateway = rejected instance. Confirm the Regulatory Update Service is applied.
- **Manual overrides ("adjustments").** Every top-side journal in the reporting
  layer needs an audit trail and reviewer sign-off — auditors hunt these.
- **Double counting across returns.** Same exposure feeding CRAR and LCR must be
  consistent; cross-form validation rules exist precisely to catch this.

## Interview drill

**Q1. "Walk me through what happens between the GL closing and a return being
filed."** *Answer:* Nightly the GL and sub-ledgers feed staging; the engine maps
each record to reg line-items using product/counterparty/maturity dimensions;
it computes the return, runs the regulator's validation rules, and I reconcile
the return back to the trial balance. Breaks are drilled via data lineage to
source, fixed in mapping, and re-run. Then maker-checker sign-off, attestation,
and submission as XBRL/XML through the regulator's channel.

**Q2. "You find total assets on the return is 50 crore below the GL. What do you
do?"** *Answer:* Run the completeness check to locate the bucket, use lineage to
drill from the failing cell to source, and I'd expect an unmapped or
mis-mapped GL account. I add/correct the mapping, re-run, confirm the break is
nil, and document the fix in the recon file — I never plug the difference.

**Q3. "What's the difference between AxiomSL and OneSumX in practice?"**
*Answer:* Both are rules engines with lineage. AxiomSL (now Nasdaq/Adenza) is
prized for deep data integration and transparent, user-configurable logic — you
can see and change the calc. OneSumX leans on Wolters Kluwer's Regulatory Update
Service, where WK's own regulatory team maintains the rule content, so it's more
"managed". Regnology is strongest on EBA granular reporting like AnaCredit and is
increasingly cloud/SaaS.

## Learn/practise (free)

You cannot license these engines personally — they're bank-only. Build the
identical skill for free:

- **Rebuild the pipeline in Excel/Power Query + Python.** Take a fake GL CSV,
  write a mapping table, use `merge`/`XLOOKUP` to classify, compute RWA and
  ratios, then code the validation rules as boolean asserts and a GL-recon check.
  This *is* the platform in miniature.
- **Read the actual templates.** EBA "reporting frameworks" (COREP/FINREP) and
  their **validation rules** lists are published free; download a COREP template
  and its rules and reproduce the arithmetic.
- **RBI**: read the ADF/RBS return formats and the CIMS documentation on the RBI
  website; map a sample trial balance to Form A / capital-adequacy return.
- **XBRL**: install the free **Arelle** open-source XBRL processor and validate a
  sample EBA instance to see taxonomy-based validation first-hand.
- **Vendor learning**: Wolters Kluwer, Nasdaq/Adenza and Regnology publish free
  webinars, product docs and demo videos — watch them to learn the exact
  menu/vocabulary ("ControllerView", "Data Integration Layer", "Rcloud").
