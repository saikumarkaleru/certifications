# The Treasury Function & TMS (Kyriba, SAP TRM, FIS)

## What you'll be able to do
Walk into a corporate treasury team and know where you sit, what the front/middle/back office each own, and what a treasury analyst actually produces on a Tuesday morning: a consolidated cash position, a funding decision, a deal ticket, and a set of controls that keep it clean. You'll be able to describe how a Treasury Management System (TMS) — Kyriba, SAP Treasury & Risk Management (TRM), or FIS Quantum/Integrity — pulls bank balances, positions cash, records deals, and feeds the GL. You'll build a simple daily cash position by hand so you understand exactly what the system automates, and you'll speak the language of the in-house bank (IHB), value dating, and zero-balancing.

## The essentials

**What treasury exists to do.** Treasury protects and mobilises the firm's cash. Four mandates:
1. **Cash & liquidity** — know today's cash to the rupee, forecast tomorrow's, never let a subsidiary run dry or leave idle balances earning nothing.
2. **Funding & capital** — raise short-term (CP, working-capital lines, overdrafts) and long-term debt, manage the maturity ladder, keep headroom on committed facilities.
3. **Financial risk** — FX, interest-rate, commodity and counterparty risk, hedged within a board-approved policy.
4. **Banking & controls** — bank relationships, account opening/closing (BAM), payment security, and segregation of duties so no one person can both deal and settle.

**Front / middle / back office.** The classic separation that prevents fraud and error:

| Office | Owns | Typical roles | Key rule |
|---|---|---|---|
| Front | Dealing: FX, MM, debt, investments; positioning cash | Dealer, cash manager | Executes within limits |
| Middle | Risk, limits, policy, MTM, P&L, compliance | Risk analyst, treasury controller | Independent check on front |
| Back | Settlement, confirmation, reconciliation, accounting | Settlements analyst | Never deals; confirms deals |

An analyst usually starts in the back or middle office. Segregation of duties (SoD) means the person who **deals** cannot **confirm** or **settle** the same trade.

**The TMS.** A single system of record for cash, deals, and risk. The big three in Indian GCCs and MNCs:

| TMS | Vendor | Strengths |
|---|---|---|
| **Kyriba** | Kyriba (SaaS, cloud) | Bank connectivity, payments hub, cash forecasting, fraud detection |
| **SAP TRM** | SAP (part of S/4HANA) | Deep ERP/GL integration, hedge accounting, in-house cash (IHC module) |
| **FIS Quantum / Integrity** | FIS | Debt & investment heavy, treasury for large corporates/banks |

What a TMS does that a spreadsheet can't safely do: auto-imports bank statements (MT940/camt.053), values deals to market, enforces dealing limits, produces the settlement instructions, and posts journals to the ERP — all with an audit trail.

**In-house bank (IHB).** Treasury acts as an internal bank to its own subsidiaries: each unit holds an internal current account with treasury instead of many external bank accounts. Treasury nets intercompany flows, runs a central external account, and charges/pays internal interest. Fewer bank accounts, fewer external payments, one FX desk. SAP calls this In-House Cash (IHC).

**Cash positioning** is the daily act of assembling every bank balance, adding known inflows/outflows for value date, and deciding: invest the surplus, or draw the line to cover the gap.

## Hands-on — step by step
**Task: build today's (14-Jul-2026) consolidated cash position and decide the action.** Group treasury in Mumbai; three bank accounts.

Opening cleared balances (from this morning's MT940 import):

- HDFC current a/c: ₹4.20 cr
- ICICI current a/c: ₹1.10 cr
- Citi USD a/c: USD 300,000 (spot 86.40 → ₹2.592 cr)

Known value-dated flows for today:

- Customer collections expected (confirmed): +₹1.80 cr into HDFC
- Vendor payment run (already approved): −₹3.50 cr from HDFC
- Payroll: −₹0.90 cr from ICICI
- USD export receipt: +USD 120,000 into Citi (₹1.037 cr)

**Step 1 — Import & reconcile.** In the TMS (say Kyriba), bank statements arrive overnight as MT940. The system auto-matches statement lines to expected items; you clear breaks in the reconciliation workbench. By hand you'd tie the bank's opening balance to your ledger.

**Step 2 — Convert FX to base currency.** Citi USD balance 300,000 × 86.40 = ₹2.592 cr; USD receipt 120,000 × 86.40 = ₹1.0368 cr. Always position in one base currency (INR here).

**Step 3 — Build the position per account (₹ cr):**

| Account | Opening | +In | −Out | Projected close |
|---|---|---|---|---|
| HDFC | 4.20 | 1.80 | 3.50 | 2.50 |
| ICICI | 1.10 | 0.00 | 0.90 | 0.20 |
| Citi (INR eqv) | 2.592 | 1.0368 | 0.00 | 3.629 |
| **Group** | 7.892 | 2.837 | 4.40 | **6.329** |

**Step 4 — Apply the target/minimum.** Policy: keep ₹0.50 cr minimum operating buffer per INR account; sweep the rest to the concentration account and invest overnight. ICICI at ₹0.20 cr is **below buffer** by ₹0.30 cr → fund it from HDFC via internal transfer.

**Step 5 — Decide the action.** After topping ICICI to ₹0.50 cr (move ₹0.30 cr HDFC→ICICI), HDFC = ₹2.20 cr. Group surplus above buffers ≈ ₹6.329 − (0.50+0.50) INR buffers − keep USD working = about ₹4.8 cr investable. Place ₹4.5 cr in an overnight liquid fund / TREPS at ~6.6% p.a.

**Step 6 — Record & instruct.** Raise the internal transfer, book the overnight investment as a deal (money-market deal ticket), and let the TMS generate the payment/settlement instruction. Middle office checks it's within the counterparty limit; back office confirms and settles.

## The output
**Daily Cash Position — Group Treasury — 14-Jul-2026 (₹ cr)**

```
Opening cleared balance (all accounts, INR eqv)      7.892
Add: confirmed inflows                             + 2.837
Less: approved outflows                            - 4.400
--------------------------------------------------------
Projected closing balance                            6.329
Less: operating buffers (2 × 0.50)                 - 1.000
Less: FX working balance retained (Citi)           - 0.829
--------------------------------------------------------
Investable surplus                                   4.500
Action: overnight liquid fund @ ~6.6% p.a.
   Interest earned (1 day) = 4.5cr × 6.6% /365 ≈ ₹8,137
Internal funding: HDFC → ICICI  ₹0.30 cr (restore buffer)
```
One overnight day of ₹4.5 cr left idle in a current account earns nothing; positioned, it earns ~₹8,100 — that is the treasury analyst's daily value-add, multiplied across a year.

## Checks, gotchas & red flags
- **Value date, not booking date.** Position on when cash actually moves. A cheque credited today but clearing T+1 is not spendable today.
- **Cleared vs ledger balance.** Only cleared/available funds count for investing. Uncleared floats bite.
- **FX at one rate, disclosed.** Convert all currencies at a single agreed rate and state it; don't mix yesterday's and today's spot.
- **Buffers per account, not just group.** A group surplus hides a subsidiary about to overdraw — always check each account against its minimum.
- **SoD breach.** If the same login that raised the investment also confirmed it, that's a red flag auditors will catch.
- **Forecast vs actual.** Track how far your projected close missed the real close; persistent bias means bad inputs (AP/AR feeds) — fix the source.

## Interview drill
**Q: Walk me through how a cash position is built and why value dating matters.** A: Start with opening cleared balances per account, convert foreign currencies to base at one spot rate, layer confirmed inflows and approved outflows **by value date**, and net to a projected close. Value dating matters because I can only invest or must cover funds that actually settle that day — booking a receivable today that clears T+2 would overstate spendable cash and could leave an account overdrawn. Then I apply per-account buffers before deciding to invest the surplus or draw a line.

**Q: What does a TMS give you over Excel?** A: A single system of record with controls Excel can't enforce — automated bank statement import (MT940/camt.053) and reconciliation, deal capture with limit checks, mark-to-market, straight-through settlement instructions, and automatic GL posting with a full audit trail and segregation of duties. Excel has no SoD, is error-prone at scale, and leaves no tamper-evident trail.

**Q: What is an in-house bank and why use one?** A: Treasury runs internal current accounts for each subsidiary and a single external account for the group, netting intercompany flows and charging internal interest. It cuts external bank accounts and cross-border payments, centralises FX and investment, and gives visibility of all cash — lowering bank fees and idle balances.

## Learn/practise (free)
- **ACT (Association of Corporate Treasurers)** free resources and the *Treasurer's Wiki* — front/middle/back office, cash management basics.
- **Kyriba, SAP, FIS websites** — product datasheets and demo videos are free; watch a Kyriba cash-positioning demo to see the workflow.
- **SAP TRM**: a free SAP Learning Hub trial or the openSAP courses let you click through the TRM/IHC transaction flow without a live client.
- **Rehearse the position build** in Excel monthly: pull three mock bank statements, position in one base currency, apply buffers, and write the one-page action note above. That single artefact is exactly what the job asks for.
- **Corporate annual reports** (e.g. Infosys, Reliance treasury notes) — read how a real group describes its liquidity and cash management policy.
