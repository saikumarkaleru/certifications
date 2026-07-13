# MIS Reporting

## What it is & where it's used

MIS (Management Information System) reporting is the recurring, decision-ready summary of a company's financial and operational performance — usually a **monthly MIS pack** that goes to the CFO, MD, board, investors, or a lender. It is not the statutory financials (those follow Schedule III / Ind AS and go out annually). MIS is *internal, fast, and opinionated*: it tells management "here is what happened, here is why, here is what to do."

A typical monthly pack contains: P&L actual vs budget vs last month, cash position and 13-week cash flow, receivables (AR) and payables (AP) ageing, and a KPI dashboard (gross margin %, EBITDA %, DSO, DPO, headcount cost, revenue per employee). It closes with **commentary** — the paragraph that explains variances.

Roles that live and die by MIS: **FP&A analyst, management accountant, finance manager, financial controller, business finance / commercial finance partner, and startup "finance person #1."** In an FMCG or manufacturing SME the accountant who "does the books in Tally" is also expected to produce the MIS. In a funded startup, the founder wants an MIS pack by the 7th of every month or the investor calls get awkward. This is one of the most *hireable* practical skills in Indian finance because every company above ~₹5 crore turnover needs it and very few juniors can build one.

## The gap: why companies want this (and college didn't teach it)

College teaches you to *prepare* a P&L and balance sheet from a trial balance. It never teaches you to *interpret* one for a non-finance MD, or to build the same P&L **five ways** (by month, by product, by branch, actual vs budget, YoY). The MBA case method discusses strategy at 30,000 feet; the CA syllabus drills accounting standards. Neither hands you a blank Excel and says "the month closed yesterday, the MD wants the pack tomorrow at 9am, go."

The specific gaps MIS closes:

- **From "recording" to "reporting."** Employers already have Tally posting the entries. They pay you to turn that data into a one-page story.
- **Variance thinking.** Nobody in college asks "revenue is ₹8L below budget — is it price, volume, or mix?" That decomposition is the whole job.
- **Speed and templating.** Real MIS is the *same* template every month. The skill is building it once so it refreshes in 20 minutes, not rebuilding it for 3 days.
- **Commentary.** A number without a "so what" is useless to management. The gap is writing 5 crisp bullet points a CEO actually reads.

## What "proficient" looks like

A job-ready person can, unaided:

1. Pull a trial balance / ledger export from Tally or an ERP and map every GL to an MIS line (revenue, COGS, opex buckets) using a **mapping table**, not manual sorting.
2. Build a **P&L that auto-refreshes** with actual vs budget vs prior month and computes variances in ₹ and %.
3. Produce **AR/AP ageing** (0-30 / 31-60 / 61-90 / 90+) from an open-item invoice list.
4. Compute the standard KPIs — Gross Margin %, EBITDA %, DSO, DPO, CCC, Current Ratio, Revenue/Employee — and know what each *means*.
5. Build a **13-week rolling cash flow** so management sees the runway, not just the bank balance.
6. Write **commentary** that attributes each material variance to a driver (price/volume/mix/timing/one-off).
7. Do all of the above on a locked template that refreshes when new data is pasted in — turnaround measured in hours, not days.

## Hands-on: how to actually do it

### Step 1 — Export the data

From **TallyPrime**: `Gateway of Tally → Display More Reports → Trial Balance` → press `Alt+E` (Export) → format **Excel (Spreadsheet)** → set "Show Ledger-wise" and full year. For ledgers/ageing: `Display More Reports → Statements of Accounts → Outstandings → Receivables` → `Alt+E`. This gives you a bill-by-bill open items list with due dates.

### Step 2 — Map GLs to MIS lines (never sort by hand)

Keep a `Mapping` sheet: column A = Ledger name, column B = MIS bucket. Then in your data sheet:

```excel
=XLOOKUP([@Ledger], Mapping[Ledger], Mapping[MIS_Bucket], "UNMAPPED")
```

Guard against new ledgers slipping through:

```excel
=IF(COUNTIF(Mapping[Ledger],[@Ledger])=0, "⚠ NEW LEDGER", "OK")
```

### Step 3 — Build the P&L with SUMIFS

Actual by bucket, then variance vs budget:

```excel
Actual:      =SUMIFS(Data[Amount], Data[MIS_Bucket], $A5, Data[Month], "Jun")
Var ₹:       =[@Actual]-[@Budget]
Var %:       =IFERROR([@Actual]/[@Budget]-1, "")
Margin %:    =[@GrossProfit]/[@Revenue]
```

### Step 4 — AR/AP ageing buckets

Given an invoice list with `Due_Date` and `Outstanding`:

```excel
Days overdue: =MAX(0, TODAY()-[@Due_Date])
Bucket:       =IFS([@Days]<=30,"0-30", [@Days]<=60,"31-60", [@Days]<=90,"61-90", TRUE,"90+")
```

Then a summary pivot, or:

```excel
=SUMIFS(AR[Outstanding], AR[Customer], $A2, AR[Bucket], B$1)
```

### Step 5 — The KPI block

```excel
DSO   = (Trade Receivables / Credit Sales) * Days_in_period
      = (Receivables / Revenue) * 30
DPO   = (Trade Payables / Purchases) * 30
CCC   = DSO + DIO - DPO
EBITDA% = EBITDA / Revenue
```

### Optional — SQL if the data sits in a database

```sql
SELECT mis_bucket,
       SUM(CASE WHEN period = '2026-06' THEN amount END) AS actual_jun,
       SUM(CASE WHEN period = '2026-05' THEN amount END) AS actual_may
FROM gl_entries g
JOIN gl_mapping m ON g.ledger = m.ledger
GROUP BY mis_bucket
ORDER BY mis_bucket;
```

AR ageing in SQL:

```sql
SELECT customer,
  SUM(CASE WHEN CURRENT_DATE-due_date<=30 THEN outstanding ELSE 0 END) AS b_0_30,
  SUM(CASE WHEN CURRENT_DATE-due_date BETWEEN 31 AND 60 THEN outstanding ELSE 0 END) AS b_31_60,
  SUM(CASE WHEN CURRENT_DATE-due_date BETWEEN 61 AND 90 THEN outstanding ELSE 0 END) AS b_61_90,
  SUM(CASE WHEN CURRENT_DATE-due_date>90 THEN outstanding ELSE 0 END) AS b_90_plus
FROM open_invoices
GROUP BY customer;
```

### Optional — Power BI / DAX for a live dashboard

```dax
Revenue      = SUM(Fact[Amount])
GM %         = DIVIDE([Gross Profit], [Revenue])
Rev vs Bud % = DIVIDE([Revenue] - [Budget Revenue], [Budget Revenue])
DSO          = DIVIDE([Trade Receivables], [Revenue]) * 30
YoY Rev %    = DIVIDE([Revenue] - CALCULATE([Revenue], DATEADD('Cal'[Date],-1,YEAR)),
                      CALCULATE([Revenue], DATEADD('Cal'[Date],-1,YEAR)))
```

### The month-end adjusting entries behind the numbers

MIS is only right if provisions are booked. Typical month-end Dr/Cr:

| Entry | Dr | Cr |
|---|---|---|
| Accrue electricity bill not yet received | Power & Fuel Exp | Provision for Expenses |
| Depreciation for the month | Depreciation | Accumulated Depreciation |
| Prepaid insurance monthly charge | Insurance Exp | Prepaid Insurance |
| Salaries earned, paid next month | Salaries | Salary Payable |

## Worked example / mini-project

**Company:** Vitesse Components Pvt Ltd, an auto-parts SME. June 2026 close.

| P&L (₹ lakh) | Actual | Budget | Var ₹ | Var % | Prior Mo |
|---|---:|---:|---:|---:|---:|
| Revenue | 210 | 230 | (20) | -8.7% | 205 |
| COGS | 138 | 147 | 9 | — | 131 |
| **Gross Profit** | **72** | **83** | **(11)** | **-13.3%** | **74** |
| GM % | 34.3% | 36.1% | -1.8pp | | 36.1% |
| Employee cost | 28 | 27 | (1) | | 27 |
| Other opex | 19 | 20 | 1 | | 19 |
| **EBITDA** | **25** | **36** | **(11)** | **-30.6%** | **28** |
| EBITDA % | 11.9% | 15.7% | | | 13.7% |

**AR ageing (₹ lakh):**

| Customer | 0-30 | 31-60 | 61-90 | 90+ | Total |
|---|---:|---:|---:|---:|---:|
| Mahindra Tier-1 | 42 | 18 | 0 | 0 | 60 |
| Local OEM | 12 | 9 | 7 | 14 | 42 |
| **Total** | **54** | **27** | **7** | **14** | **102** |

**KPIs:** DSO = (102/210)×30 = **14.6 days** ✔ but ₹14L is 90+ overdue — a red flag. DPO ≈ 32 days. GM slipped because a steel price hike raised COGS while a volume dip lost fixed-cost absorption.

**Commentary (what management actually reads):**

- Revenue ₹210L, **8.7% below budget** — driven by a 9% volume shortfall at Local OEM; price and mix held.
- **GM fell 1.8pp to 34.3%** — ₹6L from steel cost inflation (not passed to customers), ₹5L from weaker fixed-cost absorption on lower volume.
- **EBITDA ₹25L vs ₹36L budget**; the entire ₹11L miss is gross-margin, not overhead — opex is on plan.
- **₹14L receivables >90 days at Local OEM** — same customer driving the volume drop. Recommend credit hold and a collection call before July dispatch.
- **Action:** file a price-revision request with Local OEM to recover steel inflation; target ₹4L/month margin recovery from August.

Reproduce it: paste a Tally TB into `Data`, map GLs, and every table above refreshes with SUMIFS.

## How it's tested

**Interview questions:**
- "Walk me through what goes into a monthly MIS pack."
- "Revenue is up but EBITDA is down — how do you explain that to the MD?"
- "How do you decompose a revenue variance into price, volume, and mix?"
- "What's the difference between MIS and statutory reporting?"
- "DSO jumped from 45 to 60 days — what do you investigate?"

**Practical / assessment tests companies give:**
- A **timed Excel test** (45-90 min): here's a raw TB and last month's template — produce the P&L, ageing, and 3 commentary bullets.
- A **"broken template"** test: SUMIFS returns wrong totals because of an unmapped ledger; find and fix it.
- A **case:** "Books close today, MD wants the pack by 9am — what's your checklist?"
- Sometimes a **SQL screen** (build the ageing query) or a **Power BI take-home** (one dashboard page from a CSV).

## Common mistakes & how pros avoid them

| Mistake | How pros avoid it |
|---|---|
| Hard-coding numbers / manual sorting each month | Locked template driven by SUMIFS + XLOOKUP mapping; only paste raw data |
| New ledger silently dropped from P&L | An "UNMAPPED / ⚠ NEW LEDGER" check cell that must read zero before publishing |
| P&L doesn't tie to Tally | Reconcile MIS revenue & PAT to the TB every month — a control-total cell |
| Commentary just restates numbers ("revenue down 8%") | Attribute to a *driver* — price/volume/mix/timing/one-off — and add an action |
| Ignoring cash — only P&L | Always include cash position + 13-week flow; profit ≠ liquidity |
| MIS on the 20th | Automate so it lands by working day 5-7; late MIS is useless |
| Mixing accruals in one month, cash in another | Book month-end provisions (depreciation, accruals, prepaids) before pulling |
| One giant P&L, no segmentation | Slice by product/branch/customer — that's where insight hides |

## Learn-it roadmap & resources

**Time to proficiency:** ~6-8 weeks part-time if you already know accounting. Week 1-2: Excel (SUMIFS, XLOOKUP, IFS, pivots, tables). Week 3-4: build a full P&L + ageing template from a real Tally export. Week 5-6: KPIs, variance decomposition, commentary writing. Week 7-8: Power BI / SQL layer for a live dashboard.

**Resources:**
- *Excel:* ExcelJet (free formula reference), Chandoo.org, Leila Gharani (YouTube).
- *FP&A / MIS:* CFI's FP&A and Financial Modeling courses (paid); "Financial Intelligence" by Berman & Knight (interpretation).
- *Power BI:* Microsoft Learn "Power BI in a Day" (free), Enterprise DNA.
- *SQL:* Mode SQL Tutorial (free), SQLBolt.
- *India-specific:* TallyPrime documentation on exports and outstandings; practice on any SME's TB.

**Certifications:** Microsoft PL-300 (Power BI Data Analyst), CFI's FMVA (includes FP&A/dashboard modules), Tally certifications. None are mandatory — a **portfolio MIS pack** you built beats any certificate in an interview.

## Quick-reference

| Item | Formula / step |
|---|---|
| Map GL to bucket | `=XLOOKUP(Ledger, Map[L], Map[Bucket], "UNMAPPED")` |
| Actual by bucket | `=SUMIFS(Data[Amt], Data[Bucket], $A5, Data[Month], "Jun")` |
| Variance % | `=IFERROR(Actual/Budget-1,"")` |
| Ageing bucket | `=IFS(D<=30,"0-30",D<=60,"31-60",D<=90,"61-90",TRUE,"90+")` |
| Gross Margin % | Gross Profit / Revenue |
| EBITDA % | EBITDA / Revenue |
| DSO | (Receivables / Revenue) × Days |
| DPO | (Payables / Purchases) × Days |
| CCC | DSO + DIO − DPO |
| Tally TB export | Trial Balance → `Alt+E` → Excel |
| Tally AR ageing | Outstandings → Receivables → `Alt+E` |
| Control check | MIS PAT must tie to Tally TB; UNMAPPED count = 0 |
| Delivery target | Working day 5-7, same template every month |

**Pack contents, in order:** P&L (actual/budget/prior) → EBITDA bridge → cash position + 13-week flow → AR/AP ageing → KPI dashboard → commentary (5 bullets, each = variance + driver + action).
