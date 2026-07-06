# Q&A — Reading and Analysing Financial Statements

Practice bank for Chapter 03. Work each problem before reading the solution. All dollar figures are "$ in millions" unless stated. Numbers are self-checked and reconcile.

---

## Section A — Concept Check (the WHY of the technique)

**A1. Why do analysts call the Cash Flow Statement the "lie detector" of the three statements?**

Because accrual accounting lets management choose *when* revenue and expenses hit the Income Statement, net income is a matter of judgement and can be flattered. Cash that moves in and out of the bank is far harder to fake. The indirect bridge — CFO = Net Income + non-cash charges − ΔWorking Capital — means any profit that is *not* backed by cash must reappear as a growing accrual (rising receivables, inventory, or capitalised cost) on the Balance Sheet. So the gap between profit and cash is not hidden; it is mechanically visible. If reported earnings rise but CFO does not, the divergence points straight at the accrual doing the work.

**A2. Why common-size before comparing two companies or two years?**

Absolute dollars are not comparable across different sizes or eras. Common-sizing rebases every Income Statement line to a percent of revenue, and every Balance Sheet line to a percent of total assets, turning each figure into a structural ratio. A $500bn firm and a $2bn firm can then be laid side by side, and a company's own cost structure across five years becomes a clean trend. It converts scale-dependent numbers into scale-free ones, which is the only fair basis for peer and time comparison.

**A3. Why must you normalise earnings before forecasting, rather than forecast the reported number?**

Reported net income mixes recurring operating profit with non-recurring items — restructuring charges, impairments, gains on asset sales, litigation. If you forecast off a base year that contains a one-off, you implicitly repeat that one-off in *every* future year, distorting the whole model and any valuation built on it. Normalising strips the non-recurring items so you forecast the durable, repeatable earnings base. You forecast what the business actually does year in, year out — not a lucky (or unlucky) accident.

**A4. Why is the blue-font/black-font convention more than cosmetic?**

Blue = hardcoded input, black = formula. It lets any reader — an interviewer, a colleague, future-you — instantly separate assumptions from calculations. That distinction is the difference between an auditable model and an opaque one: you can trace every derived number back to its drivers, and you know exactly which cells to change to run a scenario. A model where inputs and formulas are indistinguishable cannot be trusted or stress-tested, which reads as unprofessional.

**A5. Why does a *rising* deferred revenue balance count as a good sign for a subscription business, even though it is a liability?**

Deferred revenue is cash the company has already collected but not yet earned. For a subscription model it represents booked, in-the-bank cash that will convert to recognised revenue in future periods. A growing balance means the company is selling and collecting ahead of delivery — strong forward demand and healthy cash timing. It is a liability only in the accounting sense of "we owe future service," not an economic warning.

**A6. Why is an unqualified (clean) audit opinion not a certificate that the business is healthy?**

An unqualified opinion states only that the statements are free of *material misstatement* under the applicable standards. It does not say the accounting is conservative, the earnings are high quality, or the business will survive. Auditors constrain outright lies but not spin, aggressive-but-permissible estimates, or a deteriorating business. The Critical Audit Matters section is where the auditor flags the riskiest estimates — that is the part worth reading, not just the opinion sentence.

---

## Section B — Build / Computational Problems

**B1. Build the margin and common-size block.** Firm A, $m:

| Line | FY23 | FY24 |
|---|---|---|
| Revenue | 900 | 1,100 |
| COGS | 540 | 700 |
| Operating expenses (excl. D&A) | 180 | 210 |
| D&A | 45 | 60 |

Compute, for both years: Gross Profit, EBIT, EBITDA, gross margin, EBIT margin, EBITDA margin, revenue growth, and common-size COGS. Then state the story.

**Solution (reproducible: each cell is a formula on the raw rows):**

Gross Profit = Revenue − COGS → FY23 = 900 − 540 = **360**; FY24 = 1,100 − 700 = **400**.
EBIT = Gross Profit − Opex − D&A → FY23 = 360 − 180 − 45 = **135**; FY24 = 400 − 210 − 60 = **130**.
EBITDA = EBIT + D&A → FY23 = 135 + 45 = **180**; FY24 = 130 + 60 = **190**.

| Metric | FY23 | FY24 |
|---|---|---|
| Gross margin (GP÷Rev) | 360/900 = **40.0%** | 400/1,100 = **36.4%** |
| EBIT margin (EBIT÷Rev) | 135/900 = **15.0%** | 130/1,100 = **11.8%** |
| EBITDA margin | 180/900 = **20.0%** | 190/1,100 = **17.3%** |
| Common-size COGS | 540/900 = **60.0%** | 700/1,100 = **63.6%** |
| Revenue growth | — | 1,100/900 − 1 = **+22.2%** |

**Story:** Revenue grew 22%, but gross margin fell 3.6 points and EBIT *fell in absolute dollars* (135 → 130). COGS crept from 60.0% to 63.6% of sales — the extra revenue carried thin incremental margin. Incremental gross profit was only (400 − 360)/(1,100 − 900) = 40/200 = **20%** versus a 40% base gross margin, so growth was bought with discounting or absorbed input inflation. A model holding margins flat would overstate future profit.

**B2. Reconcile the indirect CFO bridge and compute cash conversion.** Firm B, FY24, $m:

| Line | FY24 |
|---|---|
| Net Income | 120 |
| D&A | 50 |
| Stock-based comp | 15 |
| Increase in Accounts Receivable | (85) |
| Increase in Inventory | (40) |
| Increase in Accounts Payable | 20 |

Compute CFO, verify the bridge, and give cash conversion (CFO ÷ NI). Interpret.

**Solution:**
CFO = NI + non-cash (D&A + SBC) − ΔWorking Capital.
ΔWorking Capital drains: AR +85 and Inventory +40 use cash (−125); AP +20 provides cash (+20). Net WC = −105.
CFO = 120 + 50 + 15 − 85 − 40 + 20 = **80**.
Check: 120 + 65 (non-cash) − 105 (net WC) = 80. ✓
Cash conversion = 80 / 120 = **66.7%**.

**Interpret:** Despite $120m of profit and $65m of non-cash add-backs, only $80m became cash — conversion of 67% is well below the ~100% healthy threshold. Working capital consumed $105m, driven by an $85m receivables build. Either customers are paying slowly or revenue was recognised aggressively. Investigate the receivables note before trusting FY24 earnings.

**B3. Build the three reconciliation check rows.** Firm C, FY24, $m: opening cash 30; CFO 80; CFI (110); CFF 50; closing cash 50. Retained earnings: opening 400; net income 120; dividends 40; closing 480. Balance sheet: total assets 1,000; total liabilities 520; total equity 480. Write each check formula and its result; flag OK/ERROR.

**Solution (all must equal 0):**

| Check | Formula | Value | Flag |
|---|---|---|---|
| BS balances | Assets − (Liab + Equity) = 1,000 − (520 + 480) | **0** | OK |
| RE ties | RE_beg + NI − Div − RE_end = 400 + 120 − 40 − 480 | **0** | OK |
| Cash ties | Cash_beg + CFO + CFI + CFF − Cash_end = 30 + 80 − 110 + 50 − 50 | **0** | OK |

All three tie to zero, so `=IF(ABS(check)<0.5,"OK","ERROR")` returns **OK** for each. The historicals are internally consistent and safe to build on. (Note the cross-tie: RE closing of 480 equals total equity of 480 here, consistent with a single-class equity with no other reserves.)

**B4. Normalise earnings through two one-offs.** Firm D reports FY24 net income of $300m. Notes reveal: a $140m pre-tax gain on selling a warehouse, and an $60m pre-tax restructuring charge. Tax rate 25%. FY23 normalised NI was $180m. Compute FY24 normalised NI and real underlying growth versus the reported growth.

**Solution:**
After-tax gain = 140 × (1 − 0.25) = **105** (increased reported NI, so subtract it).
After-tax restructuring = 60 × (1 − 0.25) = **45** (reduced reported NI, so add it back).
Normalised NI = 300 − 105 + 45 = **240**.
Underlying growth = 240 / 180 − 1 = **+33.3%**.
Reported growth = 300 / 180 − 1 = **+66.7%**.

The reported +67% is roughly double the real +33%, inflated by a one-time asset-sale gain that outweighed the restructuring charge. Forecast off **$240m**, not $300m.

**B5. Working-capital day-count schedule.** Firm E, FY24, $m: Revenue 1,460; COGS 1,095; Accounts Receivable 200; Inventory 180; Accounts Payable 150. Use 365 days. Compute DSO, DIO, DPO and the cash conversion cycle.

**Solution:**
DSO = AR ÷ Revenue × 365 = 200 / 1,460 × 365 = **50.0 days**.
DIO = Inventory ÷ COGS × 365 = 180 / 1,095 × 365 = **60.0 days**.
DPO = AP ÷ COGS × 365 = 150 / 1,095 × 365 = **50.0 days**.
Cash Conversion Cycle = DSO + DIO − DPO = 50 + 60 − 50 = **60.0 days**.

Cash is tied up in operations for 60 days: the firm waits 50 days to collect and holds stock 60 days (110 days of investment), offset by 50 days of supplier financing. To free cash, shorten DSO/DIO or extend DPO — these same day-counts become the working-capital forecast drivers.

**B6. Sloan balance-sheet accruals ratio.** Firm F, $m: Net Income 100; CFO 70; CFI (150); total assets: opening 900, closing 1,100. Compute the accruals ratio and interpret.

**Solution:**
Average total assets = (900 + 1,100) / 2 = **1,000**.
Accruals = (NI − CFO − CFI) ÷ Avg Total Assets = (100 − 70 − (−150)) / 1,000 = (100 − 70 + 150) / 1,000 = 180 / 1,000 = **18.0%**.
A high positive accruals ratio means earnings are leaning heavily on non-cash balance-sheet growth rather than cash — Sloan's research links high accruals to weaker future returns. (Here CFI is largely investing outflow; a large chunk of the gap between accrual profit and cash is asset build.) Treat FY earnings with caution and dig into what drove the asset growth.

---

## Section C — Interview-Style Questions

**C1. "Walk me through how you would spread a company's historicals from a 10-K."**

I read the MD&A first to get management's narrative and the drivers, then go to the audited statements for the numbers and the notes to verify and adjust. In Excel I lay out years across the top, oldest on the left, line items down the side, and freeze panes. I hardcode the actuals in blue exactly as reported, and compute every subtotal — gross profit, EBITDA, EBIT, pre-tax, net income — as black formulas so component errors surface. Then I build three check rows: the balance sheet balancing, retained earnings tying, and cash tying, each wrapped in an IF flag. I don't proceed until all three read OK. Finally I layer common-size, margins, growth rates, and the working-capital day-counts, and I normalise for one-offs from the notes. The output is a clean, reconciled historicals tab ready to become the left edge of the model.

**C2. "A company grows revenue 20% but its stock falls on earnings. What might the statements show?"**

Most likely the *quality* of that growth is poor. Gross margin may have compressed — revenue bought with discounting, so incremental margin is far below the base and profit dollars barely moved. Or the cash isn't there: CFO growing slower than net income, with receivables ballooning (rising DSO), suggesting aggressive recognition or channel stuffing. Or the growth was flattered by a one-off gain that won't recur. I'd common-size the P&L to see the margin trend, check cash conversion against net income, and look at DSO/DIO. Twenty percent top-line growth means nothing if margins are collapsing and it isn't converting to cash.

**C3. "What is quality of earnings and how do you assess it quickly?"**

Quality of earnings is whether reported profit is cash-backed, recurring, and conservatively stated. My two fast checks: first, cash conversion — CFO ÷ net income — which should sit above ~100% over a cycle because D&A is a non-cash add-back; persistently below 80–100% flags accrual build-up. Second, normalisation: strip restructuring, impairments, asset-sale gains, and litigation to get underlying earnings, and watch for a large GAAP-to-adjusted gap or "one-off" charges that recur every year. I also scan the balance-sheet accruals ratio and working-capital day-counts. High-quality earnings survive triangulation against cash and the balance sheet; low-quality earnings fall apart.

**C4. "Company A books gross revenue, Company B books net commission. How do you compare them?"**

Their "revenue" lines mean different things — a marketplace booking gross merchandise value looks many times larger than an agent booking only its take rate, even for identical economics. I would not compare top-line revenue or revenue multiples directly. I'd move down to a comparable level: gross profit, EBITDA, or contribution, and use margin and multiple analysis on those. The principal-versus-agent (gross-versus-net) judgement is in the revenue-recognition note under ASC 606 / IFRS 15, so I'd read that first to know which basis each company uses before drawing any comparison.

**C5. "Why read at least two consecutive years, and where does the insight actually live?"**

A single year is a snapshot with no baseline — you can't tell if a 40% gross margin is strong or a collapse from 50%. Insight lives in the *change*: margin expansion or compression, receivables outrunning revenue, cost lines creeping up as a percent of sales, deferred revenue building. Reading consecutive years side by side, ideally common-sized, is what surfaces the trend and the anomalies. That's why I always spread at least three years and read them together, cross-referencing the MD&A for management's explanation of each move.

---

## Section D — Common-Error Spotting

**D1. Broken formula.** An analyst types Gross Profit as the hardcoded number `360` in blue, next to Revenue `900` and COGS `540`. What's wrong?

Gross Profit is a subtotal and must be a **black formula**, `=Revenue − COGS` (`=900 − 540`), not a hardcoded blue input. Hardcoding it hides component errors — if COGS is later corrected, gross profit won't update and the mistyped subtotal masks the break. It also violates the blue/black convention: a subtotal typed as an input is un-auditable. Fix: `Gross Profit = Revenue − COGS`, in black.

**D2. Broken bridge.** A model computes CFO as `=Net Income − D&A − ΔReceivables`. Given NI 120, D&A 50, receivables *increased* 85, it returns 120 − 50 − 85 = −15. What's wrong?

Two errors. First, D&A is a *non-cash* charge and must be **added back**, not subtracted: the sign is wrong. Second, a receivables *increase* uses cash, so it is subtracted — the formula happens to subtract it, which is correct in direction, but the overall structure is broken by the D&A sign. Correct bridge: `CFO = NI + D&A − ΔAR (+ other WC)` = 120 + 50 − 85 = **85** (before other working-capital items). Adding back non-cash charges is the whole point of the indirect method.

**D3. Broken common-size.** To common-size the Income Statement, an analyst enters `=B10/B4` in the COGS cell and drags it down and across, with revenue in row 4. Cells below break. What's wrong?

The revenue reference must be **row-anchored** so it doesn't drift when dragged: use `=B10/B$4`, not `=B10/B4`. Without the `$`, dragging down moves the denominator from row 4 to row 5, 6, … and each line gets divided by the wrong number. The mixed reference `B$4` locks the revenue row while letting the column move when dragged across years. (For a common-size balance sheet, anchor the total-assets row the same way.)

**D4. Broken normalisation.** Firm reports NI 300 including a $140m pre-tax asset-sale gain, tax 25%. The analyst computes normalised NI as `300 − 140 = 160`. What's wrong?

The one-off must be removed **after tax**, not at its pre-tax amount. The gain lifted net income by only its after-tax value: 140 × (1 − 0.25) = 105. Normalised NI = 300 − 105 = **195**, not 160. Subtracting the full pre-tax 140 double-counts the tax the company never kept and understates underlying earnings. Always tax-effect one-offs before adjusting net income.

**D5. Broken check row.** An analyst writes the cash tie as `=Cash_beg + CFO + CFI + CFF + Cash_end` and is puzzled it never equals zero. What's wrong?

The ending cash must be **subtracted**, not added: the identity is Cash_beg + CFO + CFI + CFF = Cash_end, so the check is `Cash_beg + CFO + CFI + CFF − Cash_end`, which should equal 0. Adding Cash_end instead roughly doubles the ending balance and the flag will always read ERROR even on correct data — masking whether the statements truly tie. Fix the sign so a genuine mis-key is what trips the flag.

**D6. Broken DIO.** An analyst computes Days Inventory Outstanding as `Inventory ÷ Revenue × 365`. Why is this wrong?

Inventory is carried at cost, so it must be divided by **COGS**, not revenue: `DIO = Inventory ÷ COGS × 365`. Dividing by revenue mixes a cost-based numerator with a price-based denominator, understating the true days inventory sits (because revenue > COGS). The same cost-basis logic applies to DPO, which also uses COGS. DSO is the exception — receivables are recorded at selling price, so DSO correctly uses revenue.

---

*End of Q&A bank. Rework any problem you missed straight in Excel — build the schedule, wire the checks, and confirm every tie reads OK before moving to the forecast chapters.*
