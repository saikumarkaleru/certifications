# Q&A — The Working Capital Schedule

Practice bank for Chapter 11. Work each question before reading the answer. The build problems use clean numbers you can reproduce cell-for-cell in Excel; every schedule reconciles (assets − liabilities = NWC, and the account-level changes tie to ΔNWC). Days use a 365-day year throughout. Rounded balances are shown; carry full precision in your own sheet and expect ±1 rounding.

---

## Section A — Concept Checks (test the WHY)

**A1. Why can a company be more profitable and poorer on the very same day?**

Because profit is recognised on *accrual* — when a sale is earned — while cash moves on a different clock. Ship INR 100 of goods on 60-day credit and the P&L books revenue and profit today, but no cash arrives until the customer pays in two months; meanwhile you already paid the supplier for that inventory. Profit went up, cash went down. The gap between recognition and collection does not vanish — it is *parked* in a balance-sheet account (receivables), and that parked cash is working capital.

**A2. Why forecast each account as "days × flow" instead of guessing a balance or a growth rate?**

Because it separates the two drivers that move a balance for different reasons. The **days ratio** encodes *policy and efficiency* (credit terms, stocking, supplier terms), which is stable; the **flow** (revenue or COGS) encodes *scale*, which grows. Bolting the balance to its flow via days means every account re-forecasts itself consistently the moment you flex revenue. Typing "receivables grow 10%" severs that link and breaks the instant the revenue assumption changes.

**A3. Why is receivables paired with Revenue but inventory and payables paired with COGS?**

Match each balance to the flow it is *carried at*. Receivables are unpaid **sales**, sitting on the books at selling price, so they scale with Revenue. Inventory is valued at **cost**, and payables arise from **buying** goods recorded at cost — both scale with COGS (or purchases). Using Revenue for inventory or payables mixes a selling-price flow with a cost-basis balance, making the days figure economically meaningless and the forecast wrong.

**A4. Why does the cash impact of working capital carry the *opposite* sign of the change in NWC?**

Because net income already *assumed* cash moved when the sale or cost was booked; the cash flow statement must reverse that assumption wherever cash and recognition diverged. An increase in an operating **asset** (you are owed more, or hold more unsold goods) is cash you spent or haven't collected → a **use** of cash → negative. An increase in an operating **liability** (you owe suppliers more) is cash you booked as cost but still hold → a **source** → positive. Net it and cash flow = −ΔNWC. It falls straight out of the accrual-to-cash reconciliation; it is not a rule to memorise.

**A5. Why does growth consume cash even when margins are healthy?**

Because a bigger business needs a bigger "pipe." Hold days constant and every account scales with sales, so NWC scales with sales too. The *increase* in NWC is cash trapped to fill the larger operating cycle and never reaches shareholders. A profitable, fast-growing firm can therefore run out of money — the P&L shows the tap running hard while the growing pipe drinks the difference.

**A6. Why must cash, short-term debt, and dividends payable be excluded from the working-capital schedule?**

Cash is the model's ultimate *output plug*; folding it into NWC would make the schedule reference the very number it is helping to compute. Short-term debt, current portion of long-term debt, and dividends payable are **financing**, not operating — they belong to their own schedules and the CFF section. Sweeping any of them into NWC double-counts cash and corrupts CFO. The schedule must stay strictly *operating*.

**A7. Why is the working-capital schedule one of the safest, non-circular parts of the model?**

Because it depends only on Revenue and COGS, which sit *upstream* of interest expense and the cash sweep. Nothing in it references cash, debt, or interest, so it introduces no circular reference. That is why you build it early — it is stable and feeds the balance sheet and CFO cleanly without being caught in the interest loop.

**A8. Why carry a Cash Conversion Cycle (CCC) row even though it is "just" DSO + DIO − DPO?**

Because it is a one-number smoke detector for the schedule. CCC is how many days your *own* cash is locked in the cycle (inventory held + waiting to collect − supplier financing). If it silently balloons across the forecast you are assuming an unintended cash drain; if it drifts implausibly low you are assuming a heroic turnaround. A visible CCC row turns a hidden assumption into an alarm.

---

## Section B — Build / Computational Problems

**B1. Calibrate the days ratios from actuals.** Year 0 actuals (INR): Revenue 24,000; COGS 15,600; Accounts Receivable 2,630; Inventory 2,137; Accounts Payable 1,282. Compute DSO, DIO, DPO and CCC on a 365-day basis, with the exact Excel formula for each.

- DSO `=AR/Revenue*365` = 2,630 ÷ 24,000 × 365 = **40.0 days**
- DIO `=Inventory/COGS*365` = 2,137 ÷ 15,600 × 365 = **50.0 days**
- DPO `=AP/COGS*365` = 1,282 ÷ 15,600 × 365 = **30.0 days**
- CCC `=DSO+DIO-DPO` = 40 + 50 − 30 = **60.0 days**

Guard the division in Excel: `=IF(Revenue=0,0,AR/Revenue*365)`. Note the denominators: Revenue for receivables (a selling-price balance), COGS for both inventory and payables (cost-basis balances).

**B2. Forecast one year, holding days flat.** From B1, Year 1 Revenue grows 25% to 30,000; COGS is 65% of revenue = 19,500; hold DSO/DIO/DPO at 40/50/30. Invert the ratios to get the balances, then compute NWC, ΔNWC and the cash-flow line.

Forecast balances `=days/365*flow`:

- AR = 40 ÷ 365 × 30,000 = **3,288**
- Inventory = 50 ÷ 365 × 19,500 = **2,671**
- AP = 30 ÷ 365 × 19,500 = **1,603**

| | Year 0 | Year 1 |
|---|---|---|
| Receivables | 2,630 | 3,288 |
| Inventory | 2,137 | 2,671 |
| Operating current assets | 4,767 | 5,959 |
| Payables | 1,282 | 1,603 |
| **Net working capital** | **3,485** | **4,356** |

- ΔNWC = 4,356 − 3,485 = **+871**
- Cash flow (CFO) = −ΔNWC = **−871**

**Reconciliation.** Assets rose 1,192; payables rose 321; 1,192 − 321 = 871 = ΔNWC — every account-level change ties to the total. Because days were held flat, NWC grew ~25% with sales (3,485 → 4,356). That 871 of profit was consumed purely to fund the bigger pipe.

**B3. Efficiency programme releases cash.** Same Year 1 Revenue 30,000 and COGS 19,500 as B2, but management compresses the cycle: DSO 40→32, DIO 50→45, DPO 30→40. Recompute the balances, ΔNWC, the cash line, and the new CCC. How much cash swung versus B2?

- AR = 32 ÷ 365 × 30,000 = **2,630**
- Inventory = 45 ÷ 365 × 19,500 = **2,404**
- AP = 40 ÷ 365 × 19,500 = **2,137**

NWC (Year 1 improved) = 2,630 + 2,404 − 2,137 = **2,897**

- ΔNWC = 2,897 − 3,485 = **−588** → Cash flow = −ΔNWC = **+588**
- New CCC = 32 + 45 − 40 = **37 days** (down from 60)

**Swing.** B2 *consumed* 871; B3 *released* 588 — a swing of **1,459** of cash flow on identical revenue, COGS and profit, entirely from a 23-day compression of the CCC. This is the value lever: no extra profit earned, yet ~1,500 of extra cash appeared. In reverse, a deteriorating CCC silently drains cash a P&L-only analyst never sees.

**B4. Two-year build and the "NWC grows at the blended rate" check.** Continue B2 (Year 1: Rev 30,000, COGS 19,500, days 40/50/30, NWC 4,356). Year 2: Revenue grows 20% to 36,000, COGS 65% = 23,400, days held flat. Build Year 2 and verify the shortcut.

- AR = 40 ÷ 365 × 36,000 = **3,945**
- Inventory = 50 ÷ 365 × 23,400 = **3,205**
- AP = 30 ÷ 365 × 23,400 = **1,923**

NWC (Year 2) = 3,945 + 3,205 − 1,923 = **5,227**

- ΔNWC = 5,227 − 4,356 = **+871** → Cash flow = **−871**

**Shortcut check.** With days held flat, every account scales with its flow and all flows grew 20%, so NWC must grow 20%: 4,356 × 1.20 = 5,227.2 ≈ 5,227. It ties. This is the self-check from the chapter: while everything grows and days are flat, each ΔNWC must be positive (cash-consuming). A negative ΔNWC here would signal a sign or denominator error.

**B5. Include the smaller items — and see how much they matter.** Forecast year: Revenue 20,000; COGS 12,000; Operating expenses 4,000. Assumptions: DSO 45, DIO 55, DPO 40; Prepaid expenses = 5% of OpEx; Accrued expenses = 8% of COGS; Deferred revenue = 10% of Revenue. Build full NWC and compare to a big-three-only NWC.

Balances: AR = 45 ÷ 365 × 20,000 = **2,466**; Inventory = 55 ÷ 365 × 12,000 = **1,808**; Prepaid = 5% × 4,000 = **200**; AP = 40 ÷ 365 × 12,000 = **1,315**; Accrued = 8% × 12,000 = **960**; Deferred revenue = 10% × 20,000 = **2,000**.

| | Amount |
|---|---|
| Operating current assets (AR + Inv + Prepaid) | 4,474 |
| Operating current liabilities (AP + Accrued + Deferred) | 4,275 |
| **Full NWC** | **199** |

Big-three-only NWC = 2,466 + 1,808 − 1,315 = **2,959**. Adding prepaid (+200), accrued (−960) and deferred revenue (−2,000) collapses NWC from 2,959 to 199 — a 2,760 gap. Omitting the smaller items overstates trapped cash by more than 90%. For services and subscription firms, deferred revenue and accruals are not rounding — they can dominate.

**B6. DPO on COGS vs on purchases.** A firm has COGS 12,000, beginning inventory 1,000, ending inventory 1,500, and Accounts Payable 1,200. Compute DPO both ways and explain the gap.

- Purchases = COGS + ending inventory − beginning inventory = 12,000 + 1,500 − 1,000 = **12,500**
- DPO on COGS = 1,200 ÷ 12,000 × 365 = **36.5 days**
- DPO on purchases = 1,200 ÷ 12,500 × 365 = **35.0 days**

They differ because inventory *grew* by 500 during the year — the firm bought more than it sold, so purchases exceed COGS and the true payables-generating flow is larger. When inventory swings are material, purchases is the purer denominator; when inventory is stable, COGS is the standard practical choice. Whatever you pick, use the *same* flow in both calibration and forecast.

---

## Section C — Interview-Style Questions (model answers)

**C1. "A company is growing 30% a year and is profitable. Why might it still need to raise cash?"**

Growth consumes working capital. If the business holds its days ratios constant, receivables and inventory scale up with sales, and while payables scale too, the *net* of operating assets over liabilities (NWC) rises with revenue. That increase is cash trapped in the operating cycle — funding a bigger receivables book and a bigger inventory stack before customers pay. Profit shows on the P&L, but a large slice is locked in the balance sheet, not in the bank. If operating cash generation can't cover the NWC build plus capex, the firm must draw a revolver or raise equity despite being profitable. It is the classic "profitable but insolvent" trap.

**C2. "Walk me through how a INR 10 increase in inventory flows through the three statements."**

Income statement: no effect — buying inventory is not an expense until the goods sell, so net income is unchanged. Cash flow statement: an increase in an operating asset is a *use* of cash, so CFO and ending cash both fall by 10. Balance sheet: inventory rises 10, cash falls 10 — the asset side nets to zero, liabilities and equity unchanged, so it still balances. Economically, I converted 10 of cash into 10 of goods in the warehouse.

**C3. "Why do you use Revenue for DSO but COGS for DIO and DPO?"**

Match each balance to the flow it is carried at. Receivables are unpaid *sales* recorded at selling price, so they scale with Revenue. Inventory is carried at *cost*, and payables come from *purchasing* goods at cost — both scale with COGS (or, more precisely, purchases). Pairing inventory or payables with Revenue would divide a cost-basis balance by a selling-price flow, so the days number would silently absorb the gross margin and mean nothing. The forecast built on it would then be wrong the moment margins move.

**C4. "What is negative working capital — and is it a red flag?"**

Negative NWC means operating current liabilities exceed operating current assets — customers and suppliers together fund the entire operating cycle and then some. It is common and *desirable* for supermarkets, e-commerce, and subscription businesses: customers pay up front (low DSO, deferred revenue) while suppliers wait (high DPO). For these firms growth *releases* cash — as NWC becomes more negative, −ΔNWC is positive — so they self-fund expansion. It is only a red flag if it stems from distress (stretching suppliers because you can't pay) rather than structural strength. So: negative CCC by business model is excellent; negative because you are squeezing creditors under stress is a warning.

**C5. "How does working capital feed a DCF valuation?"**

Unlevered free cash flow = EBIT(1−t) + D&A − CapEx − ΔNWC. The exact ΔNWC from the working-capital schedule is subtracted, because cash trapped in the operating cycle is not available to investors. If you under-forecast the working-capital build during a high-growth phase — say by trending days ratios optimistically down — you understate ΔNWC, overstate FCF, and overvalue the company. Working capital is where many rosy DCFs quietly break: the growth is real, but the analyst forgot it has to be *funded* before it becomes distributable cash.

**C6. "You can pull only one lever — DSO, DIO, or DPO. Which improves cash, and what's the catch?"**

Any of the three shortens the cash conversion cycle: cut DSO (collect faster), cut DIO (hold less inventory), or raise DPO (pay suppliers slower), each giving a one-time cash release as the account resets. The catch is that each is only free up to a point — tightening DSO can cost sales, slashing DIO risks stockouts, and stretching DPO strains suppliers and can cost you pricing or terms. So the "best" lever is business-specific, and a model that trends any of them improving forever asserts an operational miracle with no named mechanism.

---

## Section D — Common-Error Spotting (what is wrong?)

**D1. Wrong denominator in the inventory forecast.** A model forecasts inventory with `=DIO/365*Revenue`. What is broken, and what is the fix?

Inventory is carried at *cost*, so it must be driven by COGS, not Revenue. Using Revenue inflates the balance by the gross-margin factor (here it would overstate inventory by 1 ÷ (COGS/Revenue)). The historical DIO was calibrated against COGS, so pairing it with Revenue in the forecast is internally inconsistent — the days no longer mean what they were measured to mean. Fix: `=DIO/365*COGS`. Same error and fix applies to payables (`=DPO/365*COGS`, never Revenue).

**D2. Sign error into the cash flow statement.** The CFO line reads `=ΔNWC` (i.e. `=NWC_t - NWC_{t-1}`) with a plus sign. In B2, that would add +871 to CFO. Why does the balance sheet then fail, and what is correct?

The cash impact is the *opposite* of the change in NWC: an increase in NWC consumes cash. Writing `=+ΔNWC` puts +871 into CFO when the truth is −871 — a 1,742 error in cash. Cash is the balance-sheet plug, so the wrong cash flows to the balance sheet and Assets no longer equal Liabilities + Equity: the model breaks by exactly twice ΔNWC. Fix: `=-(NWC_t - NWC_{t-1})`, i.e. cash flow = −ΔNWC. This is the single most common model-breaker — check it first when the balance sheet won't tie.

**D3. Cash plugged into working capital.** An analyst includes the cash line and the revolver inside the NWC block, then wonders why CFO looks wrong and the model won't balance. Diagnose.

Cash and the revolver do not belong in NWC. Cash is the model's *output* — the balancing item — so including it means the schedule references the number it is helping to produce, and its "change" double-counts with the cash roll-forward. The revolver is *financing*, not operating; it belongs in CFF, not CFO. Both corrupt the CFO working-capital line. Fix: strip cash, short-term debt, current portion of LTD, and dividends payable out of the schedule. NWC must be strictly operating current assets minus operating current liabilities.

**D4. Mixed day-count.** History was calibrated with `AR/Revenue*360`, but the forecast inverts with `DSO/365*Revenue`. The balances drift a little every year. Why?

The 360 calibration produces a DSO that is ~1.4% lower than the 365 version for the same balance; inverting with 365 then re-inflates the balance inconsistently, so the forecast receivables no longer reproduce the historical relationship even with "flat" days. The distortion is small but systematic and pollutes every account. Fix: pick one convention (365 is standard) and use it in *both* the historical days calculation and the forecast inversion. Never mix.

**D5. Hard-coded balance growth.** A junior model forecasts `Receivables = prior receivables * 1.10` instead of days-driven. Revenue is then flexed from +10% to +40% in a scenario. What goes wrong?

The receivables balance is now divorced from sales. When revenue is switched to +40% growth, receivables still grow only 10%, so implied DSO silently collapses — the model is unknowingly assuming customers pay dramatically faster in the high-growth case, which understates the working-capital build and overstates cash. Days-driven forecasting (`=DSO/365*Revenue`) keeps the balance tethered to its flow so it stays consistent under any revenue assumption. Fix: replace the growth hard-code with the days-based formula.

**D6. Reversed ΔNWC ordering.** A model computes `ΔNWC = NWC_{t-1} - NWC_t` (prior minus current) and feeds it straight to CFO with a minus sign: `=-ΔNWC`. In B2 that yields +871 in CFO. What is the defect?

Two sign flips that don't cancel correctly. The change should be current minus prior (`NWC_t − NWC_{t-1} = +871`), and cash flow is its negative (−871). Reversing the subtraction to prior-minus-current gives −871, and then negating it in CFO gives +871 — the wrong sign, exactly the D2 failure by a different route. Fix: standardise on `ΔNWC = NWC_t − NWC_{t-1}` and `Cash = −ΔNWC`, and sanity-check with the B4 rule: while everything grows and days are flat, the CFO working-capital line must be *negative*.

**D7. Heroic days improvement.** A five-year forecast trends DSO from 60 to 20, DIO from 90 to 40, and DPO from 30 to 75, with no explanation; the CCC row falls from 120 to −15. Why is this a review failure even though every formula is "correct"?

The formulas compute fine, but the *assumptions* assert a total operational transformation — collecting three times faster, halving inventory, more than doubling supplier credit — with no named mechanism. Each year the improving days release cash, manufacturing a large fictitious tailwind that flatters FCF and valuation. The CCC row is the tell: a 135-day swing to negative should never pass unquestioned. Fix: hold days flat (or trend gently with a defensible reason), and always eyeball the CCC row for drift before trusting the cash line.

---

*Master check: from a blank sheet, can you (1) calibrate DSO/DIO/DPO from actuals with the right denominators, (2) invert them to balances, (3) difference to ΔNWC, (4) negate for the CFO cash line, and (5) confirm the account-level changes tie to ΔNWC and the balance sheet balances? If yes, you own this chapter.*
