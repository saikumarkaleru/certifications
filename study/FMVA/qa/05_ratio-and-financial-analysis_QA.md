# Q&A — Ratio and Financial Analysis

Practice bank for FMVA Chapter 05. Work each question before reading the answer. All numbers are self-checked and reproducible in Excel.

---

## Section A — Concept Checks (test the *why*)

**A1. Why is a raw dollar figure like "$310m net income" analytically useless on its own?**

Because it carries *scale*. A dollar figure blends the quality of the business with the size of the business, and you cannot separate the two by looking at the number. $310m is spectacular against $500m of assets and trivial against $50bn. Dividing by a size measure (revenue, assets, equity) cancels the scale and leaves a standardised, unit-free number you can compare across time, across peers, and against your own forecast. A ratio measures *quality*; a dollar figure measures *quantity plus quality tangled together*.

**A2. A ratio "captures a relationship, not a level." Why does that make it forecastable?**

Levels (dollar amounts) require you to predict scale, which drifts arbitrarily year to year. Relationships — receivables ÷ revenue, gross profit ÷ revenue — are structural features of the business model and tend to be stable and persistent. A company rarely swings from 42 receivable-days to 90 and back; the collection cycle is baked into its industry and terms. Because the relationship is stable, you can hold it flat (or trend it gently) as a forecast assumption, then multiply it back onto a driver to recover the dollar line. Stability is what turns a historical ratio into a forward assumption.

**A3. Why must you never diagnose a business from a single ratio?**

A single ratio is one dot; it has no direction and no context. The same 18% ROE can come from fat margins and no leverage (a luxury brand) or thin margins rescued by turnover and debt (a discount retailer) — opposite businesses, identical headline. Only a *pattern* — a family of ratios read together, tracked over 3–5 years, and benchmarked against peers — reveals the real condition. DuPont exists precisely to prove one number hides the engine.

**A4. When a ratio mixes an income-statement flow with a balance-sheet stock, why use an average balance?**

The income statement measures activity *over the whole year* (a flow); the balance sheet is a *snapshot at year-end* (a stock). Pairing a full-year flow with only the closing photo mismatches the periods — the closing balance may reflect a year-end spike or trough that never represented the year. Averaging opening and closing balances, (open + close) ÷ 2, produces a stock that represents the period the flow spans. The rule that matters more than average-vs-ending is *consistency*: pick one convention and apply it to every ratio and every year, or trends become meaningless.

**A5. Why do receivables days use revenue but inventory and payables days use COGS?**

Match the flow to what actually drives the balance. Receivables arise from *sales* booked at selling price, so DSO must divide by revenue. Inventory and payables are carried and settled at *cost*, so DIO and DPO must divide by COGS. Using revenue for inventory days pairs a cost-based balance with a price-based flow, understating the days and overstating apparent efficiency — a classic error.

**A6. What is the single most important comparison DuPont enables, and what does each lever signal?**

DuPont factors ROE = Net margin × Asset turnover × Equity multiplier = Profitability × Efficiency × Leverage. High ROE driven by *margin* signals a premium/brand business; driven by *turnover* signals a volume/thin-margin business; driven by *leverage* is a warning flag, because leverage-financed ROE is fragile and reverses violently in a downturn. The comparison it enables is *why* two firms with the same ROE are actually nothing alike.

**A7. Why can "higher is always better" be wrong for liquidity and leverage ratios?**

Liquidity ratios have an optimal *band*, not a maximise direction: a 4.0x current ratio often signals idle cash, unsold inventory, and uncollected receivables — lazy working capital that depresses returns. Leverage is not purely bad either: some debt lowers the weighted cost of capital and lifts ROE. Both families must be read for a healthy range with industry context, not pushed to an extreme.

**A8. Why is ROIC (not ROE) the "purest" measure of operating value creation?**

ROIC = NOPAT ÷ Invested Capital, where NOPAT = EBIT × (1 − tax), strips out the effect of capital structure — it measures the return the *operations* earn on all the capital deployed, debt and equity alike, before financing choices. ROE, by contrast, is inflated by leverage. Because ROIC is capital-structure-neutral, it can be compared directly to WACC: ROIC > WACC means growth creates value; ROIC < WACC means growth destroys it.

---

## Section B — Build / Computational Problems

**Cobalt Tools — data ($ millions).** Income: Revenue 5,000; COGS 3,000; Gross profit 2,000; Opex 1,400; EBIT 600; Interest 100; EBT 500; Tax (30%) 150; Net income 350; Depreciation 150 (so EBITDA = 750). Balances (opening → closing): AR 500 → 700; Inventory 450 → 550; AP 300 → 400; Total assets 3,400 → 4,000; Equity 1,700 → 2,000. Cash 300; Total debt 1,200. Current assets = AR + Inv + Cash = 1,550; current liabilities = 800.

**B1. Compute the profitability panel (margins, ROA, ROE on averages). Show the Excel formulas.**

- Gross margin = 2,000 ÷ 5,000 = **40.0%** → `=B_gp/B_rev`
- Operating margin = 600 ÷ 5,000 = **12.0%** → `=B_ebit/B_rev`
- Net margin = 350 ÷ 5,000 = **7.0%** → `=B_ni/B_rev`
- Avg assets = (3,400 + 4,000) ÷ 2 = 3,700 → ROA = 350 ÷ 3,700 = **9.46%** → `=B_ni/AVERAGE(open_TA,close_TA)`
- Avg equity = (1,700 + 2,000) ÷ 2 = 1,850 → ROE = 350 ÷ 1,850 = **18.92%** → `=B_ni/AVERAGE(open_eq,close_eq)`

Format margins/returns as `0.0%`.

**B2. Build the efficiency panel (DSO, DIO, DPO, CCC) on average balances.**

Averages: AR 600, Inv 500, AP 350.
- DSO = 600 ÷ 5,000 × 365 = **43.8 days** → `=AVERAGE(o_AR,c_AR)/B_rev*365`
- DIO = 500 ÷ 3,000 × 365 = **60.8 days** (COGS!) → `=AVERAGE(o_Inv,c_Inv)/B_cogs*365`
- DPO = 350 ÷ 3,000 × 365 = **42.6 days** (COGS!) → `=AVERAGE(o_AP,c_AP)/B_cogs*365`
- CCC = DIO + DSO − DPO = 60.8 + 43.8 − 42.6 = **62.0 days**

Cobalt ties up cash for about 62 days per operating cycle. Format days as `0.0" days"`.

**B3. Compute liquidity and leverage. Guard the interest-coverage denominator.**

- Current ratio = 1,550 ÷ 800 = **1.94x** → `=CA/CL`
- Quick ratio = (1,550 − 550) ÷ 800 = 1,000 ÷ 800 = **1.25x** → `=(CA-Inv)/CL`
- D/E = 1,200 ÷ 2,000 = **0.60x** (interest-bearing debt ÷ equity) → `=Debt/Equity`
- Interest coverage = EBIT ÷ Interest = 600 ÷ 100 = **6.0x** → `=IF(Int=0,"n/a",EBIT/Int)`
- Net debt / EBITDA = (1,200 − 300) ÷ 750 = 900 ÷ 750 = **1.20x** → `=(Debt-Cash)/EBITDA`

Read together: modestly levered (0.60x D/E, 1.2x net debt/EBITDA — investment-grade territory) and comfortably covered (6.0x interest). Format times as `0.00"x"`.

**B4. Prove DuPont ties out to ROE exactly.**

- Net margin = 7.0% = 0.0700
- Asset turnover = Revenue ÷ Avg assets = 5,000 ÷ 3,700 = 1.3514×
- Equity multiplier = Avg assets ÷ Avg equity = 3,700 ÷ 1,850 = 2.0000×
- Product = 0.0700 × 1.3514 × 2.0000 = **0.18919 = 18.92%**

This equals ROE (350 ÷ 1,850 = 18.92%) to the penny. In Excel the audit cell is `=ROUND(net_margin*asset_turn*equity_mult - roe, 4)`, which must return `0`. A non-zero result means a stock/flow mismatch (e.g., ending equity in one term, average in another) to hunt down.

**B5. Forecast Year 3 receivables. Year 3 revenue is projected at $5,600m; hold the DSO driver flat. What is forecast AR and its cash-flow effect?**

When a ratio *drives a forecast closing balance*, calibrate it on the closing balance for internal consistency (not the average, which is used for diagnosis). Closing-balance DSO for Year 2 = 700 ÷ 5,000 × 365 = **51.1 days**.

Forecast AR = (DSO ÷ 365) × Forecast revenue = (51.1 ÷ 365) × 5,600 = 0.14 × 5,600 = **$784m**.

The *change* in AR = 784 − 700 = **+$84m**, an increase in an asset, so a **working-capital cash outflow of $84m** on the cash flow statement. Excel: `=dso_end/365*fcst_rev` for the balance, `=fcst_AR - prior_AR` for the change (flip the sign into the CFS). This is the whole loop: historical ratio → forward assumption → dollar balance → cash-flow line.

**B6. Cobalt's Year 1 gross margin was 38.0%. Compute the year-over-year change and interpret.**

YoY = 40.0% − 38.0% = **+2.0 percentage points** (a *ppt* change, not a percent change). As a growth rate the Excel form is `=Y2/Y1-1` only for level ratios; for two percentages report the *point* difference, `=Y2-Y1`. Margin expanded 2 points — better pricing or cost control — a positive trend worth confirming isn't a one-off before baking it into the forecast.

---

## Section C — Interview-Style Questions

**C1. "Walk me through DuPont analysis and why an analyst uses it."**

DuPont decomposes ROE into three levers: ROE = Net margin × Asset turnover × Equity multiplier, i.e. Profitability × Efficiency × Leverage. Algebraically every term cancels back to Net income ÷ Equity, so it adds no new information at the total level — its value is *diagnostic*. It tells you *why* a firm earns its return: a high-margin/low-turnover brand, a low-margin/high-turnover retailer, or a lightly-profitable firm juiced by leverage. That matters because leverage-driven ROE is fragile — it magnifies losses in a downturn — so two firms with identical 18% ROE can carry completely different risk. The five-step version splits margin further into an interest burden and a tax burden, isolating how much of ROE is operating versus financing and tax.

**C2. "A company's current ratio is 4.0. Is that good?"**

Not necessarily — and I'd push back on the premise that higher is always better. Above ~2.0 a current ratio often signals *lazy* working capital: idle cash earning nothing, inventory that isn't selling, receivables not collected. That depresses ROA and ROE. I'd want to decompose it — is it cash (fine, if there's a use for it), inventory (possible obsolescence), or receivables (possible collection problem)? I'd also compare to the industry: a supermarket healthily runs below 1.0 because it sells inventory for cash before paying suppliers. Liquidity has a healthy band, not a maximise direction.

**C3. "Which single ratio would you look at first to judge whether a company can survive its debt, and why?"**

Interest coverage (Times Interest Earned = EBIT ÷ interest), read alongside a balance-sheet leverage ratio. Capital-structure ratios like D/E tell you *how much* debt sits on the balance sheet, but coverage tells you whether the cash flows can actually *service* it. A firm can look modestly levered yet be one bad quarter from a missed payment if earnings are thin or volatile. A TIE of 8x is comfortable; 1.5x is dangerous. Rating agencies map coverage almost directly to credit ratings, and credit markets quote Net debt/EBITDA (investment-grade below ~3x). I always read a leverage ratio and a coverage ratio together.

**C4. "How do ratios connect to building a three-statement model?"**

Ratios *are* the forecast drivers. I forecast revenue, then apply gross and operating margins to get COGS and EBIT — the margins are my P&L assumptions. DSO, DIO, and DPO forecast AR, inventory, and payables directly, and their period-over-period change is the working-capital line on the cash flow statement. A target D/E or Net debt/EBITDA sizes borrowing on the debt schedule, and interest coverage sanity-checks that the modelled debt is serviceable. After the build, I re-run every ratio on the *forecast* years as an audit: if projected ROE balloons to 45% or margin marches to 60%, an assumption is broken. Ratios are both the input and the audit of the model — a closed loop.

**C5. "Two firms are in the same industry. One has DSO of 30 days, the other 75. What might explain it and is one clearly better?"**

DSO measures how many days sales sit uncollected. Thirty days means fast collection or cash/upfront terms; 75 means generous credit terms or weakening collections. It's not automatically that lower is better: extending credit can be a deliberate sales lever that wins customers, so the 75-day firm might be buying growth. Red flags would be DSO *rising over time* (weakening collections, channel stuffing, or looming bad debt) or DSO far above the peer median with no revenue payoff. I'd look at the trend and the receivables aging, not just the level, and check the two firms genuinely sell on the same terms before calling either healthier.

---

## Section D — Common-Error Spotting

**D1. Broken formula: inventory turnover.**
```
Inventory turnover  =Revenue / AVERAGE(open_Inv, close_Inv)
```
**Wrong flow.** Inventory is carried at *cost*, so turnover must use COGS, not revenue: `=COGS/AVERAGE(open_Inv,close_Inv)`. Using revenue pairs a price-based numerator with a cost-based denominator, inflating turnover and understating DIO — the firm looks more efficient than it is.

**D2. Broken formula: DSO.**
```
DSO  =AVERAGE(open_AR, close_AR) / Revenue
```
**Missing the × 365.** As written this returns a fraction (e.g. 0.12), not days. DSO must scale by the number of days in the period: `=AVERAGE(open_AR,close_AR)/Revenue*365`. (And never × 100 — that gives 12, neither a fraction nor days.)

**D3. Broken formula: debt-to-equity.**
```
D/E  =Total_Liabilities / Total_Equity
```
**Loose debt definition.** This dumps payables, accruals, and deferred items — all *operating*, not financing — into "debt", overstating gearing. Leverage ratios use *interest-bearing* debt: short-term borrowings + current portion of long-term debt + long-term debt + capitalised leases. Use `=Interest_Bearing_Debt/Total_Equity` and hold that definition constant across every year and peer.

**D4. Broken formula: interest coverage with no guard.**
```
Interest coverage  =EBIT / Interest_Expense
```
**No zero-denominator guard.** A debt-free firm has zero interest expense, and this returns `#DIV/0!`, which then poisons any average or chart downstream. Wrap it: `=IF(Interest_Expense=0,"n/a",EBIT/Interest_Expense)` or `=IFERROR(EBIT/Interest_Expense,"n/a")`. (Economically, "n/a" is correct — an unlevered firm has infinite coverage.)

**D5. Broken formula: net debt / EBITDA.**
```
Net debt/EBITDA  =(Total_Debt + Cash) / EBITDA
```
**Sign error.** *Net* debt subtracts cash, because cash can be used to repay debt: `=(Total_Debt - Cash)/EBITDA`. Adding cash overstates leverage and would make a cash-rich firm look riskier than a cash-poor one — backwards.

**D6. Broken practice: inconsistent averaging.**
```
ROE (Year 1)  =NI_1 / Equity_close_1          'ending balance
ROE (Year 2)  =NI_2 / AVERAGE(Eq_open_2, Eq_close_2)   'average balance
```
**Mixed conventions across years.** Year 1 uses the ending balance, Year 2 the average. The "trend" between them is now an artefact of the method, not the business, and DuPont won't tie out. Pick one convention (averages for return/turnover ratios is textbook-correct) and apply it identically to every year and every ratio.

**D7. Broken practice: hard-coded ratio.**
```
Gross margin  =0.40
```
**Typed, not linked.** A ratio should always be a live formula referencing the statements — `=Gross_Profit/Revenue` — so it updates when you flex an assumption and can audit the model. A hard-coded number silently goes stale the moment any input changes and defeats the entire purpose of the ratio panel.

---

*Self-check: every computed figure above ties out numerically, and the DuPont audit (B4) returns exactly ROE (18.92%), confirming the panel is internally consistent.*
