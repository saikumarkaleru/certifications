# Financial Spreading & Normalizing Statements

## The Problem / Why this matters
Every borrower presents its financials differently — different line items, different groupings, aggressive classifications, one-off gains dressed up as operating profit. Before you can compare a borrower to peers, to covenants, or to last year, you must **restate its financials into a single, standard, apples-to-apples template**. That process is called *spreading*, and it is the unglamorous foundation on which every ratio, rating and decision rests. Spread badly and every number downstream is wrong.

## Core Idea
**Spreading** = taking the borrower's raw income statement, balance sheet and cash flow and re-mapping every line into the lender's standardised format, **normalizing** for distortions (one-offs, related-party items, accounting choices, off-balance-sheet debt) so the resulting numbers reflect the *true, recurring, economic* picture.

## Why it works this way
Ratios are only comparable if the inputs are defined consistently. If Firm A puts forex loss in "other income" and Firm B puts it in "operating expense," their operating margins aren't comparable until you standardise. And reported EBITDA can be inflated by non-recurring gains or hidden leverage (operating leases, factored receivables) that a lender must pull back onto the balance sheet.

```mermaid
graph LR
  A[Raw borrower statements] --> B[Map to standard template]
  B --> C[Normalize one-offs and reclassify]
  C --> D[Adjust for off-balance-sheet]
  D --> E[Clean recurring numbers]
  E --> F[Ratios rating and trend]
```

## Full technical content

**What gets spread.** Three statements, usually 3–5 years plus interim, into a fixed template:
- **Income statement:** revenue, COGS, gross profit, operating expenses, EBITDA, D&A, EBIT, interest, non-operating items, PBT, tax, PAT — with recurring vs non-recurring separated.
- **Balance sheet:** grouped into a lender view — current assets (cash, receivables, inventory), non-current assets, current liabilities (payables, short-term debt), long-term debt, net worth.
- **Cash flow:** CFO, CFI, CFF, and derived free cash flow / cash available for debt service.

**Normalizations the analyst makes:**
| Adjustment | Why |
|---|---|
| Strip **one-off gains/losses** (asset sales, forex, litigation) | Isolate recurring earning power |
| Reclassify **misplaced items** (forex in "other income") | Make margins comparable |
| Add back **operating leases** as debt (IFRS 16 style) | Capture hidden leverage |
| Add back **factored/discounted receivables** | Restore true debt and receivables |
| Adjust **related-party** revenue/purchases | Remove non-arm's-length distortion |
| Normalize **owner compensation** (private firms) | Reflect market-rate cost |
| Treat **contingent liabilities/guarantees** | Capture off-balance-sheet risk |
| Remove **capitalized expenses** that should be expensed | Undo profit inflation |

**Quality checks while spreading:** does the balance sheet balance? Does the change in retained earnings tie to net income minus dividends? Does the cash flow reconcile to the change in the cash line? Inconsistencies are red flags, not rounding.

**Output:** a clean multi-year trend of standardized figures ready for leverage, coverage, liquidity and profitability ratios, and for comparison against covenants and peers.

## Worked examples

**Example 1 — normalizing EBITDA.** Reported EBITDA is ₹120 cr. It includes a ₹25 cr one-off gain on sale of land and ₹10 cr of forex gain (non-operating), but excludes ₹15 cr of operating-lease rent that under IFRS 16 is really debt-servicing. *Normalized EBITDA* = 120 − 25 − 10 + 15 = **₹100 cr**. Leverage on ₹400 cr debt is 4.0x on the clean number vs a flattering 3.3x on the reported one. The lender uses 4.0x.

**Example 2 — restoring hidden debt.** A firm factors ₹80 cr of receivables (sold to a financier, off balance sheet) and has ₹120 cr of operating-lease commitments (~₹60 cr capitalized). Reported debt ₹300 cr. *Adjusted debt* = 300 + 80 + 60 = **₹440 cr** — nearly 50% higher. Debt/EBITDA jumps from 3.0x to 4.4x. This single adjustment can change the rating.

**Example 3 — related-party revenue.** ₹200 cr of a firm's ₹500 cr revenue is to a promoter-owned entity at above-market prices. Stripping the ₹30 cr of inflated margin lowers normalized EBITDA and reveals the standalone business is weaker than it looks.

## How it is tested in interviews
- **"What is financial spreading?"** — "Restating a borrower's statements into a standard template and normalizing for one-offs, reclassifications and off-balance-sheet items, so ratios are clean and comparable."
- **"What would you adjust for when spreading?"** — Name: one-off gains/losses, operating leases, factored receivables, related-party items, contingent liabilities, capitalized costs.
- **"Reported EBITDA is 120 with a 25 one-off gain and 15 of lease rent — what's your number?"** — Walk the 120 − 25 + 15 = 110 logic (adjust for the specific items given) and explain why the clean number drives leverage.
- **"Why add operating leases to debt?"** — "They're a fixed, debt-like obligation; ignoring them understates leverage and overstates coverage."

## Traps & common mistakes
- Taking **reported EBITDA** at face value.
- Missing **off-balance-sheet debt** (leases, factoring, guarantees) — the most common way leverage is understated.
- Not separating **recurring from one-off** — a firm can look profitable on the back of asset sales.
- Forgetting to **cross-check** the three statements tie out; distortions often reveal manipulation.

## First-principles recap
- Spreading standardizes messy statements so numbers are comparable.
- Normalize for **one-offs, reclassifications, and off-balance-sheet debt**.
- Restore hidden leverage (leases, factoring) — it changes the rating.
- Always verify the statements tie out; breaks are red flags.
- Clean, recurring numbers in — reliable ratios and ratings out.

## Quick-reference
| Step | Action |
|---|---|
| Map | Raw lines into standard template |
| Strip | One-off gains/losses |
| Reclassify | Items in the wrong bucket |
| Restore | Leases, factored receivables, guarantees to debt |
| Check | Balance sheet balances; CF ties to cash |
| Output | Clean multi-year recurring numbers |
