# Q&A — The Balance Sheet in Depth

A practice bank mixing conceptual/theory questions (with model answers and "how to say it in an interview") and fully-solved numerical problems. Every number is self-verified and reconciles.

---

## Section A — Conceptual / theory

### Q1. Why does the balance sheet always balance? (theory)

**Model answer.** Because of double-entry bookkeeping, which reflects the fact that every resource a company controls must have been financed by someone. The identity Assets = Liabilities + Equity holds by construction: any transaction that increases an asset either decreases another asset, increases a liability, or increases equity by exactly the same amount. There is no way to acquire a resource without recording an equal source of funding.

**How to say it in an interview:** *"It balances by construction — every asset was financed either by a creditor or an owner, so the two sides are always equal. It's arithmetic, not a coincidence."*

---

### Q2. Distinguish current from non-current, and explain the "operating cycle" nuance. (theory)

**Model answer.** Current assets are expected to convert to cash, be sold, or be consumed within one year *or one operating cycle if longer*; current liabilities are due in the same window. Non-current items sit beyond that horizon. The operating cycle is the time from buying inventory to collecting cash from selling it (DIO + DSO). For businesses with cycles longer than a year — whisky ageing, shipbuilding, real-estate development — inventory that will take, say, three years to sell is still classified as *current* because it is within the normal operating cycle.

**How to say it:** *"One year is the default, but the real test is the operating cycle — for a distiller, three-year-old inventory is still a current asset."*

---

### Q3. What is a contra account and why not just write the asset down directly? (theory)

**Model answer.** A contra account carries a balance opposite to the account it offsets — for example accumulated depreciation (credit balance) against gross PP&E, or allowance for doubtful accounts against gross receivables. You keep it separate rather than netting directly because the gross figure carries information. Gross PP&E of $500m with accumulated depreciation of $450m tells you the asset base is 90% depreciated and a capex cycle is imminent — a signal you would lose if the books only showed net PP&E of $50m.

**How to say it:** *"It offsets an account while preserving the gross number, and the gross-to-net ratio is itself a signal — like how depreciated the PP&E is."*

---

### Q4. Book value vs market value of equity — why do they diverge? (theory)

**Model answer.** Book value = assets − liabilities, an accounting number built mostly on historical cost. Market value is the market's forward-looking price of future cash flows. They diverge because (1) assets sit at cost less depreciation, not current worth; (2) internally-generated intangibles — brand, R&D, customer relationships — are not capitalized, so a company's most valuable assets are often invisible on the sheet; and (3) the market prices the future while the sheet records the past. That's why asset-light tech and consumer-brand firms trade at high price-to-book and distressed industrials can trade below book.

**How to say it:** *"Book value is backward-looking historical cost and ignores home-grown intangibles; market value prices the future. That gap is the whole game in valuation."*

---

### Q5. Is deferred revenue an asset or a liability, and is it good or bad? (theory)

**Model answer.** It's a liability — cash received in advance for goods or services not yet delivered, so the company owes a future performance. But it is a *favorable* liability: it's interest-free financing from customers, and rising deferred revenue is a leading indicator of future revenue and demand. For subscription and SaaS businesses it is one of the healthiest signals on the balance sheet.

**How to say it:** *"Liability, but a good one — customers funding us interest-free, and growth in it forecasts future revenue."*

---

### Q6. Where does goodwill come from, and can it ever increase? (theory)

**Model answer.** Goodwill arises only in an acquisition: purchase price minus the fair value of identifiable net assets acquired. It captures synergies, workforce, brand, and market position that can't be separately recognized. It is never amortized under US GAAP or IFRS, only tested for impairment at least annually. It can never rise after the deal — you cannot create goodwill internally — and it can only fall through impairment, which is irreversible for goodwill.

**How to say it:** *"Only from M&A, it's the premium over identifiable net assets, never amortized, only impaired downward — an impairment is management admitting they overpaid."*

---

### Q7. How did IFRS 16 / ASC 842 change the balance sheet? (theory)

**Model answer.** Before, operating leases were off-balance-sheet — disclosed in footnotes with rent expense on the income statement. From 2019, nearly all leases are capitalized: a right-of-use asset on the asset side and a lease liability on the liability side. It grossed up both sides for lease-heavy businesses (retailers, airlines, restaurants) and made leverage far more comparable across companies that lease versus buy.

**How to say it:** *"It put operating leases on the sheet — a right-of-use asset and a matching lease liability — which grossed up assets and debt for anyone lease-heavy."*

---

### Q8. What does it mean if retained earnings are large but the company has almost no cash? (theory)

**Model answer.** Retained earnings is cumulative net income less cumulative dividends — an accounting record of reinvested profit, not a cash reserve. A company can have huge retained earnings and little cash because it plowed those profits into PP&E, inventory, acquisitions, or buybacks. Equity is a claim, not a vault of cash. To see actual liquidity, look at the cash line and the cash flow statement, not retained earnings.

**How to say it:** *"Retained earnings isn't a cash pile — it's cumulative reinvested profit. The cash may all be sitting in the factory and inventory."*

---

### Q9. Explain LIFO vs FIFO and one comparability trap. (theory)

**Model answer.** FIFO assumes the oldest inventory is sold first, so COGS reflects older (usually lower) costs and ending inventory reflects recent costs — closer to current value. LIFO assumes the newest inventory is sold first, so in inflation COGS is higher, profit and taxes are lower, and ending inventory on the balance sheet is understated (old, cheap layers). The trap: LIFO is permitted under US GAAP but *banned under IFRS*, so comparing a US LIFO firm to an IFRS peer without a LIFO-reserve adjustment distorts both inventory and margins.

**How to say it:** *"LIFO understates balance-sheet inventory and, in inflation, lowers taxable income — but it's US-GAAP-only, so you must adjust via the LIFO reserve before comparing to IFRS peers."*

---

### Q10. Walk through what happens to the three statements when a company records a $10 inventory write-down (25% tax). (theory/linkage)

**Model answer.** Income statement: the write-down is an expense, so pre-tax income falls $10; at 25% tax, net income falls $7.50. Cash flow: start from net income −$7.50, add back the $10 non-cash write-down, so operating cash rises $2.50 (the tax saving). Balance sheet: inventory −$10 and cash +$2.50, so assets fall $7.50 net; equity falls $7.50 via retained earnings. Assets −$7.50 = Equity −$7.50; it balances.

**How to say it:** *"Non-cash charge — net income down $7.50, but add back the $10, so cash actually rises $2.50 from the tax shield, and the sheet still balances."*

---

## Section B — Numerical problems

### Q11. Build a balance sheet and prove it balances. (numerical)

Nova Retail's opening transactions: (1) issue equity for $150,000 cash (par negligible, treat all as common stock); (2) take a $50,000 long-term loan; (3) buy fixtures for $80,000 cash; (4) buy inventory $40,000 on credit; (5) sell inventory costing $25,000 for $45,000 cash; (6) accrue $3,000 wages payable (unpaid); (7) depreciate fixtures $2,000.

**Solution.**

Income statement: Revenue 45,000 − COGS 25,000 − Wages 3,000 − Depreciation 2,000 = **Net income 15,000.** No dividends → retained earnings 15,000.

Cash: +150,000 +50,000 −80,000 +45,000 = **165,000.**

| Assets | $ | Liab & Equity | $ |
|---|---|---|---|
| Cash | 165,000 | Accounts payable | 40,000 |
| Inventory (40,000−25,000) | 15,000 | Wages payable | 3,000 |
| Fixtures, net (80,000−2,000) | 78,000 | Long-term loan | 50,000 |
| | | Common stock | 150,000 |
| | | Retained earnings | 15,000 |
| **Total assets** | **258,000** | **Total L & E** | **258,000** |

Check: 165,000 + 15,000 + 78,000 = 258,000. Liabilities 93,000 + Equity 165,000 = 258,000. **Balances.** ✔

---

### Q12. Compute net receivables and the effect of a write-off. (numerical)

Gross receivables $200,000; allowance for doubtful accounts $12,000. The company then writes off a specific $5,000 account as uncollectible.

**Solution.**

Net receivables before = 200,000 − 12,000 = **$188,000.**

The write-off entry:
```
Dr  Allowance for doubtful accounts   5,000
    Cr  Accounts receivable                  5,000
```
Gross AR = 195,000; allowance = 7,000. Net receivables after = 195,000 − 7,000 = **$188,000 — unchanged.**

**Key insight (state this):** A specific write-off does *not* change net receivables or hit the income statement — the expense was already recognized when the allowance was created. Only *creating or topping up* the allowance (bad debt expense) hits the P&L.

---

### Q13. Gross vs net PP&E and the age signal. (numerical)

Company X: gross PP&E $600m, accumulated depreciation $480m. Company Y: gross PP&E $600m, accumulated depreciation $120m. Both use ~20-year straight-line lives.

**Solution.**

Net PP&E: X = 600 − 480 = **$120m**; Y = 600 − 120 = **$480m.**

Percent depreciated: X = 480/600 = **80%**; Y = 120/600 = **20%.**

Approx average age = % depreciated × useful life: X ≈ 0.80 × 20 = **16 years**; Y ≈ 0.20 × 20 = **4 years.**

**Interpretation:** Same gross asset base, but X's fleet is 80% depreciated and roughly 16 years old — a large replacement capex wave is coming, and reported net PP&E understates the cash needed to sustain the business. Y's assets are young. The contra account (accumulated depreciation) is exactly what surfaces this; net PP&E alone would hide it.

---

### Q14. Working-capital days and the cash conversion cycle. (numerical)

Revenue $800m, COGS $560m. AR $109.6m, Inventory $92.1m, AP $69.0m.

**Solution.**

DSO = 109.6 / 800 × 365 = **50.0 days.**
DIO = 92.1 / 560 × 365 = **60.0 days.**
DPO = 69.0 / 560 × 365 = **45.0 days.**
CCC = 50.0 + 60.0 − 45.0 = **65.0 days.**

**Interpretation:** The company's cash is tied up for 65 days between paying suppliers and collecting from customers. To fund one more day of the cycle you need roughly (Revenue + COGS)-scaled working capital. If growth accelerates, working capital scales with it — an FP&A modeler forecasts each line off these day-counts.

---

### Q15. Goodwill on acquisition. (numerical)

Buyer pays $420m cash for Target. Target fair values: current assets $80m, PP&E $200m, identifiable intangibles $50m, assumed liabilities $60m.

**Solution.**

FV of identifiable net assets = 80 + 200 + 50 − 60 = **$270m.**
Goodwill = 420 − 270 = **$150m.**

Entry:
```
Dr  Current assets              80,000,000
Dr  PP&E                       200,000,000
Dr  Identifiable intangibles    50,000,000
Dr  Goodwill                   150,000,000
    Cr  Liabilities assumed              60,000,000
    Cr  Cash                            420,000,000
```
Debits 480,000,000 = Credits 480,000,000. ✔ Net assets recorded = 480 − 60 = 420 = cash paid.

---

### Q16. Goodwill impairment and three-statement effect. (numerical)

Continuing Q15: one year later the reporting unit's recoverable amount is $340m versus a carrying amount of $400m. Impairment is limited to goodwill. Tax rate 0% (goodwill impairment non-deductible here).

**Solution.**

Impairment = carrying 400 − recoverable 340 = **$60m** (goodwill 150 → 90).

```
Dr  Goodwill impairment loss    60,000,000
    Cr  Goodwill                          60,000,000
```
Income statement: −$60m pre-tax = −$60m net income (no tax benefit). Cash flow: net income −$60m, add back $60m non-cash → operating cash **unchanged**. Balance sheet: goodwill −$60m, retained earnings −$60m; assets −$60m = equity −$60m. **Balances**, and cash untouched — the classic "non-cash charge" payoff.

---

### Q17. Deferred revenue recognition over time. (numerical)

On 1 Jan a SaaS firm collects $24,000 cash for a 12-month subscription. Show the position at 31 March.

**Solution.**

On collection:
```
Dr  Cash                24,000
    Cr  Deferred revenue        24,000
```
Monthly earned = 24,000 / 12 = 2,000. Through 31 March (3 months) revenue recognized = 6,000.
```
Dr  Deferred revenue     6,000
    Cr  Revenue                  6,000
```
At 31 March: Cash 24,000 (asset), Deferred revenue 18,000 (liability, remaining 9 months), and 6,000 flowed to revenue → retained earnings. Assets 24,000 = Liabilities 18,000 + Equity 6,000. ✔

**Say this:** *"The cash came in day one but revenue is earned ratably; deferred revenue unwinds $2,000 a month as the obligation is fulfilled."*

---

### Q18. Issuing stock above par and a subsequent buyback. (numerical)

Firm issues 10,000 shares, $1 par, at $25. Later it buys back 1,000 shares at $30.

**Solution.**

Issuance:
```
Dr  Cash                        250,000
    Cr  Common stock (par)              10,000
    Cr  Additional paid-in capital     240,000
```
Equity rises $250,000 (10,000 par + 240,000 APIC).

Buyback (cost method):
```
Dr  Treasury stock               30,000
    Cr  Cash                             30,000
```
Treasury stock is contra-equity, so total equity falls $30,000 to **$220,000**; cash falls $30,000. Shares outstanding drop from 10,000 to 9,000 (issued 10,000 less 1,000 in treasury). Assets (cash) −30,000 = equity −30,000. ✔

---

### Q19. Book value per share and price-to-book. (numerical)

Total assets $1,200m, total liabilities $750m, shares outstanding 50m, share price $18.

**Solution.**

Book value of equity = 1,200 − 750 = **$450m.**
Book value per share = 450 / 50 = **$9.00.**
Market cap = 18 × 50 = **$900m.**
Price-to-book = 900 / 450 = **2.0×** (or 18 / 9 = 2.0×).

**Interpretation:** The market values equity at twice book — it's pricing in intangible value, growth, or returns above cost of capital that the historical-cost sheet doesn't capture. A P/B below 1× would suggest the market expects returns below cost of capital or looming impairments.

---

### Q20. Current portion of long-term debt and the liquidity trap. (numerical)

A company reports "long-term debt $500m" and current liabilities $180m, current assets $220m. A footnote reveals $90m of the long-term debt matures within 12 months and should be reclassified as current.

**Solution.**

Correct current liabilities = 180 + 90 = **$270m.**
Correct non-current debt = 500 − 90 = **$410m.**
Current ratio as reported = 220 / 180 = **1.22×** (looks comfortable).
Current ratio corrected = 220 / 270 = **0.81×** (below 1 — current assets don't cover current liabilities).

**Interpretation:** Ignoring CPLTD overstated liquidity badly; the corrected picture shows a potential refinancing squeeze within a year. Always reclassify the current portion before computing liquidity ratios.

---

### Q21. Full mini balance sheet with contras, then key ratios. (numerical)

Given: Cash 60; Gross AR 100; Allowance for doubtful accounts 8; Inventory 70; Gross PP&E 300; Accumulated depreciation 120; Goodwill 40; Accounts payable 55; Accrued expenses 15; Short-term debt 20; Long-term debt 130; Common stock + APIC 150. Solve for retained earnings, then compute current and quick ratios. (All in $m.)

**Solution.**

Net AR = 100 − 8 = 92. Net PP&E = 300 − 120 = 180.
Total assets = 60 + 92 + 70 + 180 + 40 = **442.**
Total liabilities = 55 + 15 + 20 + 130 = **220.**
Equity must = 442 − 220 = **222.** Given common stock + APIC = 150, so **retained earnings = 222 − 150 = 72.**

Current assets = Cash 60 + Net AR 92 + Inventory 70 = 222.
Current liabilities = AP 55 + Accrued 15 + ST debt 20 = 90.
Current ratio = 222 / 90 = **2.47×.**
Quick ratio = (222 − 70) / 90 = 152 / 90 = **1.69×.**

Check identity: Assets 442 = Liabilities 220 + Equity 222. ✔ Comfortable liquidity; quick ratio above 1 means even excluding inventory the firm covers short-term obligations.

---

### Q22. Debt schedule impact — net debt and leverage. (numerical)

Total debt (ST + LT) $150m, cash $30m, EBITDA $60m, EBIT $45m, interest expense $9m.

**Solution.**

Net debt = 150 − 30 = **$120m.**
Gross leverage = Total debt / EBITDA = 150 / 60 = **2.5×.**
Net leverage = Net debt / EBITDA = 120 / 60 = **2.0×.**
Interest coverage = EBIT / Interest = 45 / 9 = **5.0×.**

**Interpretation:** 2.0× net leverage is moderate and 5.0× interest coverage is healthy — the company earns 5× its interest bill, so debt service is comfortable. A credit analyst reads these three numbers straight off the balance sheet and income statement to size default risk.

---

### Q23. Equity roll-forward. (numerical)

Opening equity $400m. During the year: net income $70m, dividends paid $25m, new shares issued $30m, share buybacks $40m, other comprehensive income (unrealized gain) $5m.

**Solution.**

Closing equity = 400 + 70 − 25 + 30 − 40 + 5 = **$440m.**

Breakdown of the change: retained earnings +45 (70 income − 25 dividends); paid-in capital +30 (issuance); treasury −40 (buyback); AOCI +5. Net change +40.

**Say this:** *"Equity rolls forward as opening plus net income, less dividends, plus net share issuance, plus OCI. Buybacks and dividends are the two ways cash leaves to shareholders."*

---

### Q24. Reconciling a cash-vs-equity confusion. (conceptual + numerical)

A company shows retained earnings of $300m but cash of only $12m. An interviewer asks: "Where did the money go?" Its non-cash assets: net PP&E $260m, inventory $70m, net receivables $40m; liabilities total $82m.

**Solution.**

Total assets = 12 + 260 + 70 + 40 = 382. Equity = 382 − 82 = 300, matching retained earnings + assume no separate paid-in for simplicity.

**Answer:** The reinvested profit (retained earnings) is not sitting as cash — it has been deployed into productive assets: $260m of PP&E, $70m of inventory, $40m of receivables. Retained earnings measures cumulative profit *kept in the business*, and that capital now lives on the asset side as plant, stock, and money owed by customers — not in the bank. This is the single most common conceptual confusion the balance sheet exposes.

---

*End of Q&A — The Balance Sheet in Depth.*
