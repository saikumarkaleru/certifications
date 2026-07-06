# Q&A — The Equity Schedule

Practice bank for Chapter 14. Work each question before reading the answer. This chapter's engine is two BASE roll-forwards — Retained Earnings (Opening + Net Income − Dividends) and Share Capital (Opening + Issuances − Buybacks) — wired to their sources so the balance sheet ties out. Every number below is built so you can reproduce it cell-for-cell in Excel and watch it reconcile. Sign convention throughout: inflows positive, outflows (dividends, buybacks) negative, then a plain `SUM` rolls each column.

---

## Section A — Concept Checks (test the WHY)

**A1. Why does equity need a dedicated schedule when it is "just" the residual Assets − Liabilities?**

Because on the balance sheet equity is a *stock* — a photo — but that photo changes for reasons that originate in two other statements at once. Net income (income statement) pushes it up, dividends and buybacks (cash-flow financing) pull it down, issuances push it up again. If you compute equity as a bare plug (Assets − Liabilities), you get a number with no audit trail: nobody can say *why* it moved. Worse, you have used the balance sheet's own balancing identity to fill equity, so the identity can never catch an error — it is guaranteed to "balance" while hiding a mistake somewhere else. The schedule rebuilds equity from its actual drivers, which both explains every movement and turns the balance-sheet check into a real diagnostic.

**A2. Why does net income appear in the equity schedule but issuing shares does not appear on the income statement?**

Because net income is *earned* value — the reward for operating — and earned value accrues to owners, so it credits retained earnings. Issuing shares is *contributed* value — owners putting money in — which is a financing transaction between the company and its shareholders, not a profit. The income statement measures performance; selling your own stock is not performance, it is capital raising. So an issuance touches cash and share capital only, never revenue or expense. Confusing the two would let a company inflate "earnings" simply by selling stock.

**A3. Why must the dividend number feed two statements from a single source cell?**

Because a dividend is one economic event with two consequences: it reduces retained earnings (equity) and it reduces cash (financing outflow). Those are the same dollars viewed from two statements. If you type the dividend into the retained earnings roll-forward and separately type it into cash-flow financing, the two copies can silently drift when an assumption changes — and the moment they disagree, the balance sheet breaks. Driving both links off one cell makes divergence impossible: two links, one number.

**A4. Why does opening retained earnings for any forecast year have to be a formula pointing at the prior year's closing, not a typed figure?**

Because that link *is* the roll-forward. It guarantees that whatever ended last year begins this year exactly, so a change to any early assumption ripples down the whole timeline. Hard-key the opening and the chain snaps: this year ignores last year's net income and dividends, and the schedule degrades into disconnected snapshots. `Opening = prior Closing` is the single wire that keeps equity alive and reactive.

**A5. Why does the `MAX(0, …)` guard belong in every payout-ratio dividend formula?**

Because in a loss year a naive `Payout% × Net Income` goes negative, and a negative dividend is nonsense — it would *add* value to equity, as if shareholders paid the company for the privilege of a loss. `MAX(0, Payout% × NI)` floors dividends at zero, so in a loss year the company simply pays nothing and equity falls by the full loss, which is the correct economics. Boards cut dividends when earnings vanish; the guard encodes that.

**A6. Why does the equity schedule make the *entire* three-statement model balance, not just the equity line?**

Because both the equity schedule and the cash-flow financing section trace to the same underlying transactions. The financing section records the *cash* effect of dividends, issuances, and buybacks; the equity schedule records the *equity* effect of those identical events plus net income (whose cash effect runs through operating activities). Since assets and equity move off the same events, Assets = Liabilities + Equity proves out automatically. And if the schedule and financing section ever disagree, the imbalance is exactly the size of the discrepancy — the schedule is a built-in error detector.

**A7. Why is retained earnings not the same thing as cash?**

Because retained earnings is cumulative *undistributed profit*, an equity concept, while cash is one specific asset. Profit that was retained may have been spent on inventory, plant, or debt repayment — the earnings stayed with owners as a claim, but the cash left for other assets. A company can have huge retained earnings and almost no cash, or negative retained earnings and plenty of cash from an equity raise. The roll-forward tracks the claim; the cash balance is a separate line driven by the whole cash-flow statement.

---

## Section B — Build / Computational Problems

Convention for all builds: outflows stored **negative**, closing line is a literal `=SUM(opening, additions, deductions)`.

**B1. The basic retained-earnings roll-forward.** Opening retained earnings (end of Y0) = **400**. Net income: Y1 = 200, Y2 = 250, Y3 = 300. Dividend policy = 25% payout ratio. Give the three closing balances.

Step 1 — dividends = 25% × NI: `50.0, 62.5, 75.0`.

Step 2 — roll forward, opening = prior closing:

| Line | Y1 | Y2 | Y3 |
|---|---:|---:|---:|
| Opening retained earnings | 400.0 | 550.0 | 737.5 |
| (+) Net income | 200.0 | 250.0 | 300.0 |
| (−) Dividends (25% × NI) | (50.0) | (62.5) | (75.0) |
| **Closing retained earnings** | **550.0** | **737.5** | **962.5** |

Verify the chain: 400 + 200 − 50 = **550.0** → Y2 opening; 550 + 250 − 62.5 = **737.5** → Y3 opening; 737.5 + 300 − 75 = **962.5**. Each opening equals the prior closing. ✓

**B2. Add share capital, then total equity.** Extend B1. Opening share capital = **250**. Y1: issue 60 of new stock. Y3: repurchase 30 (retired). No SBC.

Share capital roll-forward:

| Line | Y1 | Y2 | Y3 |
|---|---:|---:|---:|
| Opening share capital | 250.0 | 310.0 | 310.0 |
| (+) Issuances | 60.0 | 0.0 | 0.0 |
| (−) Buybacks | 0.0 | 0.0 | (30.0) |
| **Closing share capital** | **310.0** | **310.0** | **280.0** |

Total shareholders' equity (add B1 retained earnings):

| Line | Y1 | Y2 | Y3 |
|---|---:|---:|---:|
| Share capital (closing) | 310.0 | 310.0 | 280.0 |
| Retained earnings (closing) | 550.0 | 737.5 | 962.5 |
| **Total shareholders' equity** | **860.0** | **1,047.5** | **1,242.5** |

**Integrity check (Y3).** Opening total equity = 310 + 737.5 = 1,047.5. Closing − Opening − NI + Div − Issuance + Buyback = 1,242.5 − 1,047.5 − 300 + 75 − 0 + 30 = 0. ✓ (1,242.5 − 1,047.5 = 195; 195 − 300 = −105; −105 + 75 = −30; −30 + 30 = 0.)

**B3. Reconstruct the missing flow.** You are handed two consecutive balance sheets: opening total equity = **1,000**, closing total equity = **1,180**. Net income for the year = 250. The company issued 30 of new equity and made no buyback. What dividend was paid?

Set up the identity and solve for dividends D:
`Closing = Opening + NI − D + Issuance − Buyback`
`1,180 = 1,000 + 250 − D + 30 − 0`
`1,180 = 1,280 − D`  →  **D = 100.0**

Check: 1,000 + 250 − 100 + 30 = 1,180. ✓ This is the everyday analyst skill — the roll-forward run backwards to recover an undisclosed flow.

**B4. The negative-income dividend guard.** Opening retained earnings = **150**. Y1 net income = **−60** (a loss). Payout ratio = 30%.

Naive formula: 30% × (−60) = −18 → dividends of −18 would *add* 18 to equity: 150 − 60 − (−18) = **108** (wrong — phantom inflow).

Guarded formula `=MAX(0, 30% × NI)`: dividends = 0.

| Line | Y1 (guarded) |
|---|---:|
| Opening retained earnings | 150.0 |
| (+) Net income | (60.0) |
| (−) Dividends | 0.0 |
| **Closing retained earnings** | **90.0** |

Check: 150 − 60 − 0 = 90. ✓ Equity correctly falls by the full loss; the guard suppressed a $18 error.

**B5. Stock-based compensation consistency.** Opening retained earnings = **300**, opening share capital (common + APIC) = **500**. Y1 net income = 100 (this figure is *after* a $20 non-cash SBC expense). Payout = 0. SBC of 20 credits APIC. Build Y1 equity two ways — with and without the SBC line — and show which balances.

With the SBC line:

| Line | Y1 |
|---|---:|
| Opening share capital | 500.0 |
| (+) Stock-based comp | 20.0 |
| **Closing share capital** | **520.0** |
| Closing retained earnings (300 + 100) | 400.0 |
| **Total equity** | **920.0** |

On the cash-flow statement SBC is a $20 non-cash add-back in operating activities, so cash is $20 higher than net income alone implies. That $20 of extra assets must be matched by $20 of extra equity — supplied precisely by the APIC increase. **Total equity = 920, and the balance sheet ties.**

Omit the SBC line and share capital stays 500, total equity = 900. But cash still carried the $20 add-back, so assets exceed liabilities + equity by exactly **20** — the balance sheet breaks by the SBC amount. This is the classic "forgot SBC" imbalance.

**B6. DPS method with a shares roll-forward.** Opening shares outstanding = **40m**. DPS: Y1 = $2.00. In Y1 the company issues **5m** new shares mid-year; dividends are declared on the year-end share count. What are Y1 dividends, and what is the closing share count?

Shares roll-forward: 40m opening + 5m issued − 0 repurchased = **45m closing**.
Dividends = DPS × year-end shares = $2.00 × 45m = **$90m**.

(Note the modeling choice: paying on year-end shares means the newly issued shares receive the full dividend. If the policy pays only on the opening 40m, dividends = $80m. State the convention explicitly — it changes the number by $10m.)

---

## Section C — Interview-Style Questions (model answers)

**C1. "Walk me through how a $1 increase in net income flows through the three statements."**

Net income rises $1. On the cash-flow statement it is the top line of operations, so — assuming no working-capital offset — cash rises $1. On the equity schedule, that same $1 credits retained earnings, so equity rises $1. On the balance sheet, assets go up $1 (cash) and equity goes up $1 (retained earnings): both sides move together and it balances. The equity schedule is the connective piece — it is the mechanism by which the income statement's result actually lands on the balance sheet. Without it there is no path for profit to reach equity.

**C2. "A company pays a $50 cash dividend. Take me through all three statements."**

Income statement: no effect — dividends are a distribution of profit, not an expense, so they never touch the P&L. Cash-flow statement: a $50 financing outflow, so cash falls $50. Equity schedule: retained earnings falls $50 (Closing = Opening + NI − Dividends). Balance sheet: assets down $50 (cash), equity down $50 (retained earnings) — balanced. The key point interviewers listen for is that the dividend hits equity and cash but *not* earnings, and that the equity reduction and the cash reduction are the same $50 sourced from one assumption.

**C3. "How does a share buyback differ from a dividend across the statements?"**

Both return capital to shareholders and both are financing outflows that reduce cash, and neither touches the income statement. The difference is *where* they land in equity. A dividend reduces retained earnings. A buyback reduces contributed capital — either as a contra-equity treasury-stock line (if the shares are held) or by retiring common stock and APIC (if cancelled). A buyback also cuts share count, which raises EPS mechanically, whereas a dividend leaves share count unchanged. So on the balance sheet both shrink assets and equity equally, but the buyback additionally changes the per-share denominator that valuation cares about.

**C4. "Why can't I just plug equity as Assets minus Liabilities and skip the schedule?"**

You can make the sheet *appear* balanced that way, but you have destroyed your only error check. If equity is defined as Assets − Liabilities, the balance-sheet identity is true by construction and can never reveal a mistake — any error elsewhere just gets absorbed into the equity plug. Building equity independently from its drivers (net income, dividends, issuances, buybacks) and *then* comparing Assets to Liabilities + Equity is what makes the check meaningful. A zero check earned two independent ways is proof; a zero check that was assumed is nothing.

**C5. "What's the difference between dividends declared and dividends paid, and which one hits retained earnings?"**

Declaration is the board's decision to distribute; at that moment retained earnings is debited and a dividends-payable liability is created — so *declared* dividends are what reduce equity. Payment is the later cash settlement that clears the payable and reduces cash. In most annual models the two coincide within the period, so we use one number. But if a dividend is declared in one year and paid in the next, retained earnings falls on declaration while cash falls on payment, and a dividends-payable liability bridges the gap. Strictly, the retained-earnings roll-forward should use *dividends declared*.

---

## Section D — Common-Error Spotting

**D1. Spot the error:** the modeler typed `=485` into the closing shareholders' equity cell on the balance sheet, taken from the prior model.

Hard-coded closing equity — the number-one killer of a live model. Equity now ignores every assumption: change net income or dividends and equity does not move, so the balance sheet can only balance by accident. Fix: delete the hard-code and link the balance-sheet equity lines to the schedule's closing balances, which roll forward from their drivers.

**D2. Spot the error:** dividends are stored as a positive 60 and the closing line reads `=Opening + NetIncome + Dividends`.

Sign error. With dividends positive and a `+` in the formula, a distribution *increases* retained earnings — backwards. Either store dividends negative and keep `=SUM(...)`, or store them positive and subtract. Pick "outflows negative," enforce it everywhere, and let a plain `SUM` do the arithmetic so the sign logic lives in the data, not scattered across formulas.

**D3. Spot the error:** net income is added in the retained-earnings roll-forward *and* the modeler separately added net income to the balance-sheet equity total to "make it tie."

Double-counting net income. It belongs in the retained-earnings roll-forward exactly once; the balance-sheet equity line should be a pure link to the schedule's closing balance with no fresh math. Adding it twice overstates equity by a full year's profit and forces the modeler to hunt for a compensating fudge elsewhere. Fix: balance-sheet equity lines contain links only.

**D4. Spot the error:** the P&L expenses $20 of stock-based comp, cash flow adds it back, but the equity schedule has no SBC line.

The balance sheet will be out by exactly $20. SBC is non-cash, so the add-back leaves cash (and thus assets) $20 higher, but with no offsetting APIC increase, equity is $20 short. Add a `(+) Stock-based comp` line to the share-capital roll-forward, linked to the same SBC figure the cash-flow add-back uses.

**D5. Spot the error:** Y2 opening retained earnings is typed as `=737` (a value) rather than linked to Y1's closing cell.

Broken roll-forward chain. The opening is now frozen and blind to any change in Y1's net income or dividends, so every year from Y2 on is wrong the moment an early assumption moves. Fix: set Y2 opening `=` the cell holding Y1's closing retained earnings, so the corkscrew is unbreakable.

**D6. Spot the error:** payout formula is `=Payout% * NetIncome` with no floor, and Y3 shows a loss.

In the loss year this produces a negative dividend that *adds* to equity — a phantom inflow. Wrap it: `=MAX(0, Payout% * NetIncome)`. In a loss year dividends become zero and equity falls by the full loss, which is the correct behavior.

**D7. Spot the error:** the company repurchased and *retired* shares, but the modeler parked the full cost in a treasury-stock contra account and left common stock/APIC unchanged.

Treasury-versus-retirement confusion. Retired shares should reduce common stock and APIC (they no longer exist); only *held* shares go to treasury stock at cost. The total equity may look right, but the component split is wrong and — critically — the share count used for EPS is misstated, distorting per-share valuation. Match the accounting treatment to what actually happened to the shares.

---

*Self-check across this bank: every roll-forward obeys Closing = Opening + Net Income − Dividends + Issuances − Buybacks; every build's integrity row (Closing − Opening − NI + Div − Issuance + Buyback) resolves to 0; and every dividend, issuance, and buyback is a single number shared between the equity schedule and cash-flow financing.*
