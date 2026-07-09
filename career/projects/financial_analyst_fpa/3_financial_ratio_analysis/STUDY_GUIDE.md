# Study Guide — Financial Ratio Analysis + DuPont + Peer Benchmarking

Your cheat-sheet to defend this project line by line.

## 1. The 30-second pitch
> "I built a Python tool that pulls real financial statements for a target
> company and four peers, computes the full set of profitability, liquidity,
> leverage and efficiency ratios over several years, then does three things a
> good analyst does next: it breaks ROE apart with DuPont to see *what* is
> driving returns, it percentile-ranks the target against its peers so I know
> where it's strong or weak, and it screens earnings quality with an accruals
> and cash-conversion check. It outputs an Excel workbook and charts. Data is
> live from yfinance, cached locally, with an offline fallback so it always runs."

## 2. What ratio analysis is (and how an analyst uses it)
Raw statement numbers aren't comparable — a $400bn company and a $40bn company
can't be read off absolute dollars. Ratios turn those numbers into comparable
signals: margins, returns, coverage, turnover. One year is a snapshot; the
**trend** and the **peer comparison** tell the story. This is the first thing you
do when you pick up a new company: is it profitable, can it pay its bills, is it
over-levered, is it using its assets hard — and how does all that compare to last
year and to competitors.

## 3. THE key interview answer — DuPont
ROE (Net Income / Equity) is the number shareholders care about most, but alone
it hides *why*. DuPont factorises it into levers management can actually pull.

**3-step:** `ROE = Net Margin × Asset Turnover × Equity Multiplier`
- **Net Margin** (NI / Revenue) — profitability: how much of each sales dollar
  becomes profit.
- **Asset Turnover** (Revenue / Assets) — efficiency: how many sales dollars each
  asset dollar generates.
- **Equity Multiplier** (Assets / Equity) — leverage: how many asset dollars sit
  on each equity dollar. Higher = more debt amplifying returns.

So a high ROE is either a *profitable* business (Apple, big margins), an
*efficient* one (a retailer with thin margins but fast turnover), or a *levered*
one (using debt) — DuPont tells you which.

**5-step** splits Net Margin further to separate operations from financing/tax:
`ROE = Tax Burden × Interest Burden × Operating Margin × Asset Turnover × Equity Multiplier`
- **Tax Burden** (NI / Pretax) — fraction of profit kept after tax.
- **Interest Burden** (Pretax / EBIT) — fraction kept after interest; low means
  debt is eating into profit.
- **Operating Margin** (EBIT / Revenue) — *pure* operating profitability, before
  financing and tax.

The whole thing is a telescoping product — every intermediate term cancels and
you're left with exactly NI / Equity. That's why the project has a **unit test**
asserting the product of the drivers equals the directly-computed ROE (diff ≈ 0)
for both the 3- and 5-step versions, on every company and year.

## 4. Module walkthrough (`src/ratios/`)
- **`data.py`** — loads income statement, balance sheet, cash flow via yfinance.
  Caches each ticker to `input/` so reruns are offline; falls back to bundled
  illustrative numbers if there's no cache and no network. A single safe `get()`
  helper returns NaN for missing rows (Google/Meta carry ~no inventory), so the
  math never crashes.
- **`ratios.py`** — the four families:
  - *Profitability:* gross / operating / net margin, ROA, ROE, ROIC.
  - *Liquidity:* current, quick, cash ratio.
  - *Leverage:* debt/equity, debt/assets, interest coverage, net debt/EBITDA.
  - *Efficiency:* asset turnover, receivables turnover / DSO, inventory turnover /
    DIO, payables / DPO, cash conversion cycle.
  Balance-sheet items are averaged (this year + last year)/2 because they're
  divided into a full-year flow.
- **`dupont.py`** — the 3-step and 5-step decompositions above, each reconciling
  to ROE. Uses year-end equity consistently so the identity holds exactly.
- **`benchmark.py`** — for the latest year, **percentile-ranks** the target vs
  peers on each key ratio (0-100). Direction-aware: for "lower is better" ratios
  (debt, DSO, cash cycle) a low value scores a high percentile, so across the
  board "higher percentile = better positioned". Labels each Strong / Middle / Weak.
- **`quality.py`** —
  - *Trend flags:* first year vs latest, labelled Improving / Deteriorating /
    Flat, with a 5% noise band and direction awareness.
  - *Earnings-quality red flags:* **accruals ratio** = (NI − Operating Cash Flow)
    / Total Assets (big positive = profit booked ahead of cash = lower quality);
    and **cash conversion** = CFO / NI (should be ≥ 1; below 1 is a yellow flag).
- **`reporting.py`** — writes the multi-sheet Excel workbook and four PNG charts.

## 5. Interview Q&A
**Q: Walk me through DuPont — what drives a high ROE?**
A: "ROE = net margin × asset turnover × equity multiplier. So a high ROE comes
from being very profitable, very efficient with assets, or heavily levered — or a
mix. The 5-step version splits net margin into tax burden, interest burden and
operating margin, so I can tell a genuinely profitable business from one that
just has a low tax bill or is leaning on cheap debt. The product always
reconciles back to net income over equity — that's the whole elegance of it."

**Q: Current vs quick ratio?**
A: "Both measure whether short-term assets cover short-term liabilities. The quick
ratio strips out inventory because inventory can be slow or costly to turn into
cash, so it's the more conservative liquidity test. The cash ratio goes further —
only cash — for the most stressed view."

**Q: ROIC vs ROE?**
A: "ROE is net income over equity — it's affected by leverage and tax structure.
ROIC is after-tax operating profit (NOPAT = EBIT × (1 − tax rate)) over invested
capital — debt plus equity. ROIC strips out how the company is financed, so it
measures the return on the *operating business itself* and is comparable across
firms with different capital structures. If ROIC comfortably exceeds the cost of
capital, the business is creating value regardless of leverage."

**Q: How do you benchmark a company against peers fairly?**
A: "Same ratio, same period, comparable peer set, and rank rather than raw
compare. In this project I percentile-rank the target against its four peers on
each key ratio, and I flip the direction for 'lower is better' metrics so a low
debt/equity scores as strong. That gives me an at-a-glance read of where the
company leads and lags, instead of arguing about absolute numbers."

**Q: What's the cash conversion cycle?**
A: "CCC = DSO + DIO − DPO. Days to collect from customers, plus days inventory
sits, minus days you take to pay suppliers. It's how long cash is tied up in
working capital. Lower is better, and it can go negative — Apple runs a negative
cycle because suppliers effectively finance its inventory, which is a huge
working-capital advantage."

**Q: How would you spot low earnings quality or red flags?**
A: "Profit is an opinion; cash is a fact. I check the accruals ratio — net income
minus operating cash flow, over assets — because a big positive gap means profit
is being booked well ahead of the cash arriving. And I check cash conversion,
CFO over net income, which should be around one or higher. If reported earnings
keep rising but operating cash flow lags, that's a yellow flag worth digging into
— revenue recognition, receivables ballooning, or aggressive accruals."

## 6. Vocabulary to know cold
- **ROE** — Net Income / Equity. Return to shareholders.
- **ROA** — Net Income / Total Assets. Return on the whole asset base.
- **ROIC** — NOPAT / Invested Capital. Return on the operating business,
  financing-neutral.
- **DuPont** — factorising ROE into margin × turnover × leverage (3-step) or into
  tax/interest burden × operating margin × turnover × leverage (5-step).
- **Equity Multiplier** — Assets / Equity. The leverage lever in DuPont.
- **Tax Burden / Interest Burden** — NI/Pretax and Pretax/EBIT; fraction of
  profit surviving tax and interest.
- **Current / Quick / Cash ratio** — short-term liquidity, increasingly strict.
- **Interest Coverage** — EBIT / Interest Expense; times operating profit covers
  interest.
- **Net Debt / EBITDA** — (Debt − Cash) / EBITDA; years of cash earnings to repay
  debt.
- **Asset Turnover** — Revenue / Assets; sales generated per asset dollar.
- **DSO / DIO / DPO** — days sales outstanding (collect), days inventory
  outstanding (sell), days payables outstanding (pay).
- **Cash Conversion Cycle** — DSO + DIO − DPO; days cash is tied up in working
  capital.
- **Accruals Ratio** — (NI − CFO) / Assets; earnings-quality screen.
