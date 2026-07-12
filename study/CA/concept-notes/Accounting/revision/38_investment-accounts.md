# Investment Accounts

## Snapshot
Special three-column ledger keeping **units, income and capital** surgically separate for each type of investment. Governed by **AS 13**. Each investment type gets its own account. *Nominal column never touches P&L; Interest column never touches Balance Sheet.*

## Core concepts
Three columns (each investment type = separate account):
- **Nominal (Face Value)** — memorandum of units held; reconciles unit count, drives average cost. Closing c/d = face value still held.
- **Interest / Income** — income earned/accrued + accrued interest paid on purchase; net **closed to P&L**.
- **Principal (Capital / Cost)** — real capital cost, stripped of accrued interest. Closing c/d = carrying amount → **Balance Sheet**.

Balancing logic:
- Nominal — pure arithmetic (known, not a plug).
- Interest — balancing figure = income transferred to P&L (a genuine plug).
- Principal — **compute c/d independently = avg cost × units held; profit/loss is the plug**.

## Key provisions / rules — formulas, treatment; tables

**Cost of investment (AS 13) = Purchase price + Brokerage + Stamp duty + charges.** Accrued interest is NOT cost.

**Accrued Interest = Face Value × Annual Coupon Rate × (months since last coupon ÷ 12).**
Coupon received = rate × face value **held on the coupon date** (split if holdings changed mid-period).

**Cum vs Ex — "Cum = Carve out; Ex = Extra on. Buy adds brokerage; Sell subtracts brokerage."**

| Transaction | Principal-side value | Interest column | Cash |
|---|---|---|---|
| Cum buy | (Quoted + brokerage) − Accrued | Dr = Accrued | Quoted + brokerage |
| Ex buy | Quoted + brokerage | Dr = Accrued | Quoted + brokerage + Accrued |
| Cum sale | (Quoted − brokerage) − Accrued | Cr = Accrued | Quoted − brokerage |
| Ex sale | Quoted − brokerage | Cr = Accrued | (Quoted − brokerage) + Accrued |

**Year-end accrual (books close between coupons):** recognise stub-period interest as income (To P&L, Dr side) AND carry it as accrued interest receivable c/d. Next year b/d on Dr side, cleared when coupon arrives. Opening accrued interest → bring down Dr side "To Interest accrued b/d".

**TDS:** credit **gross** interest to Interest column; Bank Dr = net; TDS receivable Dr (asset).

**Bonus shares:** Nominal ↑ by face value; **Principal = 0** (no cost); no income.
New avg cost/share = Existing Principal ÷ (existing + bonus shares).

**Rights shares:**
- Subscribed → Nominal ↑ (face), Principal ↑ (cash paid).
- Renounced (sold) → **capital receipt, credit Principal (reduce cost)**. To P&L only if question says so, or shares quoted ex-right.

**Sale — profit/loss:**
Cost of units sold = Face sold × (Total Principal ÷ Total Nominal) [running ratio at sale date], or avg cost/share × shares.
Profit/(Loss) = Sale value (Principal part) − Cost of units sold.
**Profit → Dr side "To P&L"; Loss → Cr side "By P&L".** Default cost-flow = weighted average (recompute after every event); FIFO only if stated.

**Carrying value (AS 13):**
| Class | Measured at | Diminution |
|---|---|---|
| Long-term | Cost | Write down only for **other-than-temporary** decline → P&L; else disclose market value |
| Current | **Lower of cost & fair value** | Write down to fair value → P&L |
Applied investment-by-investment (or category). Write-back capped at original cost; never carry above cost.

**Dividend:** Pre-acquisition → reduce cost (credit Principal, NOT income). Post-acquisition → income (P&L). Same test as accrued interest / ex-right: *is there a cost sitting behind the receipt?*

## Journal entries
```
Purchase (ex-interest):
Investment A/c (Principal)  Dr  [price + brokerage]
Interest A/c               Dr  [accrued]
   To Bank                     [total]

Purchase (cum-interest):
Investment A/c (Principal)  Dr  [cum price + brokerage − accrued]
Interest A/c               Dr  [accrued]
   To Bank                     [cum price + brokerage]

Interest received:   Bank Dr / To Interest A/c

Sale (ex-interest, profit):
Bank Dr  [proceeds + accrued]
   To Investment A/c (cost of units sold)
   To Interest A/c (accrued)
   To P&L (profit)

Year-end accrual:    Interest A/c (accrued) Dr / To P&L
Pre-acq dividend:    Bank Dr / To Investment A/c (reduce cost)
Post-acq dividend:   Bank Dr / To Interest/Income A/c
Current inv write-down: P&L Dr / To Investment A/c (to fair value)
```
Bonus: no money entry (Nominal memorandum only). Rights subscribed: Investment A/c Dr / To Bank. Rights sold: Bank Dr / To Investment A/c (or To P&L if income).

## Worked mini-example
12% bond, coupons 30 Jun/31 Dec, buy ₹1,00,000 face @ ₹98 **cum-interest** on 1 May, brokerage 1%. Last coupon 31 Dec → accrued 4 months.
Accrued = 1,00,000 × 12% × 4/12 = ₹4,000. Cash = 98,000 + 980 = ₹98,980. Principal = 98,980 − 4,000 = **₹94,980**; Interest Dr = **₹4,000**.

## Exam traps & must-remember
- Adding accrued interest to cost (cum price already contains it → carve out).
- Cum/Ex direction reversed.
- Bonus added to Principal / treated as income (both wrong).
- Rights sold taken to P&L instead of reducing cost.
- Interest computed on wrong face value or year-end holding instead of coupon-date holding.
- Forgetting brokerage: add on buy, **deduct** on sale.
- Pre-acquisition dividend booked as income.
- Sale on coupon date → accrued = 0 (no phantom interest).
- Forgetting year-end accrued interest (income + receivable c/d).
- Crediting net-of-TDS interest instead of gross.
- Forcing Principal c/d as a plug — compute it independently, let profit/loss plug.
- Long-term temporary decline written down (only other-than-temporary).
- Writing investment above original cost.

## One-line recall
- Three columns: Nominal (units, memo) · Interest (income → P&L) · Principal (cost → B/S).
- Cost = price + brokerage + charges; accrued interest is never cost.
- Cum = Carve out; Ex = Extra on; Buy adds brokerage, Sell subtracts.
- Bonus: Nominal ↑, Principal 0; Rights sold: credit Principal.
- Long-term at cost; Current at lower of cost & fair value.
- Pre-acquisition receipt = capital (reduce cost); post-acquisition = income.
