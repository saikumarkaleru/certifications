# Study Guide — Three-Statement Model + DCF (read this, own the interview)

Your cheat-sheet for **defending this project**. Understand this page and you can
walk any FP&A interviewer through a real linked model, a debt schedule, scenarios,
a sensitivity table, and a DCF — with confidence.

---

## 1. The 30-second pitch

> "I built a driver-based three-statement model in Python. It pulls Microsoft's
> real financials from yfinance, derives the operating assumptions from that
> data — growth, margins, working-capital days, capex — and projects a fully
> linked income statement, balance sheet and cash flow five years out. The
> balance sheet ties out to zero every year. On top of that I added a debt
> revolver with a cash sweep, bull/base/bear scenarios, a two-way sensitivity
> table, and a DCF valuation off the model's free cash flow. It caches the data
> so it runs offline, and it writes a clean Excel workbook plus charts."

---

## 2. What a three-statement model IS (and why FP&A cares)

Three financial statements, linked so they move as one:
- **Income Statement (P&L):** did we make a profit? (revenue − costs)
- **Balance Sheet:** what do we own and owe at a point in time? (assets =
  liabilities + equity)
- **Cash Flow Statement:** where did the actual cash go? (**profit ≠ cash**)

Every budget, forecast and valuation in FP&A is built on this. If you can build
and explain it, you can do the core of the job.

---

## 3. THE key answer: how the three statements link

**Memorize this — it's the single most common FP&A interview question.**

> "Net income from the income statement is the top line of the cash flow
> statement and it flows into retained earnings on the balance sheet.
> Depreciation is subtracted on the P&L but added back on the cash flow because
> it's non-cash — and it reduces PP&E on the balance sheet. Changes in working
> capital and capex adjust cash further. The ending cash on the cash flow
> statement becomes the cash line on the balance sheet — and that's what makes
> the balance sheet balance."

Three links to remember:
1. **Net income** → equity/retained earnings (BS) and top of cash flow (CF).
2. **Depreciation** → reduces P&L profit, added back on CF (non-cash), reduces PP&E (BS).
3. **Ending cash** (CF) → cash line (BS).

---

## 4. Walk through each module

**`data.py` — get real data, derive the drivers.**
Pulls `income_stmt` / `balance_sheet` / `cashflow` for MSFT, caches them to
`input/`, and turns them into assumptions: revenue growth (historical CAGR),
gross margin, opex %, tax rate, D&A %, capex %, and working-capital days
(DSO/DIO/DPO). Each derived number is *clamped* into a believable band so one
weird figure can't blow up the model; anything messy falls back to a constant.
It builds a **simplified opening balance sheet** (cash, receivables, inventory,
PP&E / payables, debt) and sets **opening equity as the plug** so the opening
sheet balances exactly.

**`forecast.py` — the linked engine (the heart).**
For each year it builds the IS down to EBIT, computes working-capital balances,
runs the debt schedule (below), then the cash flow, then the balance sheet, and
rolls every balance forward. It also computes **FCFF** for the DCF.

**Income statement:** Revenue grows → COGS from gross margin → Gross Profit →
less opex and depreciation → **EBIT** → less interest → **Pre-tax income** →
less tax → **Net income**.

**Working capital (drives cash):** Receivables = revenue × DSO/365; Inventory =
COGS × DIO/365; Payables = COGS × DPO/365. An **increase** in receivables or
inventory **uses** cash; an increase in payables **releases** cash.

**Cash flow:** Net income + depreciation − change in working capital = **cash from
operations**; − capex = investing; − dividends ± debt = financing; sum + last
year's cash = **ending cash**.

**Balance sheet:** PP&E = prior + capex − depreciation; Equity = prior + net
income − dividends; Cash comes straight from the cash flow. The **Balance Check**
row proves Assets − (Liab + Equity) ≈ 0 every year.

**The debt schedule / cash sweep (`forecast.py`, the impressive bit).**
We keep a **minimum cash buffer** (5% of revenue). Cash **above** the buffer is
*swept* to pay down debt (revolver first, then term debt). If cash falls **below**
the buffer, we **draw the revolver** to top it back up. Interest is charged on the
**average of opening and closing debt** — which makes the model circular (interest
→ net income → cash → debt → interest), so we **iterate to convergence each year**,
exactly like Excel's iterative calculation.

**`scenarios.py` — cases + sensitivity.**
*Scenarios:* re-run the whole model flexing the two drivers that matter most —
revenue growth and gross margin. Bull = optimistic, Base = derived, Bear = stress.
*Sensitivity:* a 5×5 grid, rows = revenue growth, columns = gross margin, each cell
= the DCF **value per share** — so you can see what has to be true for the
valuation to hold.

**`valuation.py` — the DCF.**
1. **WACC:** cost of equity via CAPM (risk-free + beta × equity-risk-premium),
   after-tax cost of debt (rate × (1−tax)), blended by equity/debt weights.
2. Discount each year's **FCFF** at the WACC.
3. **Terminal value** (Gordon growth): FCFF_last × (1+g) / (WACC − g), discounted back.
4. **Enterprise value** = PV(FCFF) + PV(terminal value).
5. **Equity value** = EV − net debt; **per share** = equity ÷ shares.

**`reporting.py`** — writes the Excel workbook (one tab per statement + debt,
FCFF, scenarios, sensitivity, DCF, assumptions) and the PNG charts.

---

## 5. Why the balance sheet balances (the "magic")

It's an accounting identity, not magic. Every transaction hits two places. As
long as (a) the **opening** sheet balances (we set equity as the plug) and (b)
cash is taken from the cash flow statement, the sheet balances every year
automatically. The math checks out: the change in assets each year exactly
equals the change in liabilities + equity — depreciation, capex and working
capital all cancel, leaving net income + Δpayables − dividends ± debt on both
sides. The `Balance Check` row prints ~0.000000 every year to prove it.

---

## 6. FCFF vs the cash flow statement (don't mix these up)

The cash flow statement's operating cash flow is **levered** — it's after
interest. The DCF uses **FCFF = EBIT × (1 − tax) + D&A − capex − change in NWC**,
which is **unlevered** — it deliberately ignores interest, because the DCF values
the whole enterprise (all capital providers) and then subtracts net debt at the
end to get to equity. Using interest twice would double-count the financing.

---

## 7. Interview Q&A (practice these out loud)

**Q: Walk me through the three statements.**
A: Use section 3 verbatim.

**Q: If depreciation goes up by $10, what happens to all three statements?**
A: "On the P&L, pre-tax income falls $10, so net income falls $10 × (1 − tax) =
$7.50 at an 18% tax rate that's about $8.20 — use the number for the tax rate you
quote. On the cash flow, net income is down but we add back the full $10 of
depreciation, so cash actually goes **up** by the tax saving. On the balance
sheet, PP&E falls $10, cash rises by the tax saving, and equity falls by the drop
in net income. It still balances."

**Q: Why can a profitable company run out of cash?**
A: "Profit isn't cash. Fast growth ties up cash in receivables and inventory, and
heavy capex drains it, so operating cash can sit well below net income. That's
exactly why we model the cash flow statement separately — and why I added a
revolver that draws when cash dips below the buffer."

**Q: What's the plug / balancing item in your model?**
A: "Two answers. In the *opening* balance sheet, equity is the plug so the
simplified sheet ties out. In the *forecast*, **cash** is effectively the plug —
it comes from the cash flow statement and absorbs the difference, which is why the
sheet balances every year."

**Q: How does your cash sweep work?**
A: "I keep a minimum cash buffer of 5% of revenue. Any cash above that gets swept
to pay down debt — revolver first, then term debt. If cash falls below the buffer,
I draw the revolver to restore it. Interest is on average debt, which makes it
circular, so I iterate each year until interest converges — the same thing Excel's
iterative calc does."

**Q: How did you get to your DCF value, and what's WACC?**
A: "WACC is the blended required return of debt and equity holders — cost of
equity from CAPM, after-tax cost of debt, weighted by how much of each is in the
capital structure; here it's around 9.7%, mostly equity. I discount five years of
unlevered free cash flow at the WACC, add a Gordon-growth terminal value at 2.5%,
sum to enterprise value, subtract net debt, and divide by shares to get value per
share. My number came out below the market price, which is a reasonable, conservative
DCF — the market is pricing in more growth than my clamped assumptions."

**Q: Why is your value below the market price — is the model wrong?**
A: "No — a DCF is only as bullish as its assumptions. I clamp growth and use a
2.5% terminal rate, so it's deliberately conservative. The sensitivity table shows
how the value moves with growth and margin; push those to the market's implied
assumptions and the gap closes."

---

## 8. Words you should be able to define cold
EBIT, EBITDA, NOPAT, **FCFF** (unlevered free cash flow), **WACC**, CAPM, beta,
**terminal value** (Gordon growth), working capital, **DSO/DIO/DPO**, capex,
depreciation (non-cash), retained earnings, **cash sweep**, revolver, net debt,
enterprise vs equity value, and the accounting equation (Assets = Liabilities +
Equity).

If any are fuzzy, look them up now — they will come up.
