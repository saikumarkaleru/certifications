# Liquidity, Cash Management & Bank Connectivity (SWIFT)

## What you'll be able to do
Design and run a cash pool — decide between notional and physical pooling, compute the interest benefit, and book the intercompany positions. Build a rolling liquidity forecast that a CFO would trust, execute a payment through the right channel, and read the plumbing that moves money: SWIFT, host-to-host (H2H), and bank APIs, plus the message formats (MT940, MT101, and the ISO 20022 / MX camt and pain messages that are replacing them). You'll also run bank account management (BAM) so the firm knows every account it owns and who can sign on it.

## The essentials

**Cash pooling — concentrating cash so the group borrows less and earns more.**

| | **Notional pooling** | **Physical pooling (ZBA sweep)** |
|---|---|---|
| Cash movement | None — balances *offset* on the bank's books | Real transfers sweep to a header account |
| Intercompany loans | Not created (no movement) | Created — each sweep is an IC loan |
| Interest | Bank pays/charges on the *net* balance | Header earns/pays; IC interest to participants |
| Needs | One bank, often one country, cross-guarantees | Works cross-bank; automated end-of-day sweep |
| India note | Restricted — RBI limits resident notional pooling and cross-border sweeps under FEMA | Domestic ZBA common; cross-border needs approval |

**Zero-balance account (ZBA):** each operating account is swept to (or funded from) a concentration/header account daily so it ends at zero. **Target-balance (TBA):** swept to a set target, not zero.

**Liquidity forecasting.** A rolling view of cash in/out by day (short horizon) and by week/month (longer). Direct method = sum actual receipts and payments (AR, AP, payroll, tax, debt). Best practice: a **13-week rolling cash flow** for operational liquidity, refreshed weekly, with actual-vs-forecast variance tracking.

**Payments & settlement rails.**
- **RTGS** (India): real-time gross, high value, 24×7.
- **NEFT**: batch, any value, 24×7.
- **SWIFT**: the cross-border messaging network (not the money itself) — banks settle via correspondents/nostro accounts.
- **Correspondent banking / nostro-vostro:** your bank holds an account (nostro) with a foreign bank to settle that currency.

**Bank connectivity — three ways a corporate talks to its banks:**

| Channel | What it is | Use when |
|---|---|---|
| **SWIFT** (via service bureau / Alliance Lite2) | Bank-neutral network; one pipe to many banks | Multi-bank, global, high volume |
| **Host-to-host (H2H)** | Direct secure file transfer (SFTP) to one bank | High volume with a single core bank |
| **API** | Real-time calls (balances, payments, status) | Modern, instant balances & payment status |

**Message formats.** MT = legacy SWIFT (FIN); MX = ISO 20022 XML, now the global standard (SWIFT MT→MX migration completed Nov 2025 for cross-border payments).

| Purpose | Legacy MT | ISO 20022 MX |
|---|---|---|
| End-of-day statement | MT940 | camt.053 |
| Intraday statement | MT942 | camt.052 |
| Credit transfer (single/bulk) | MT103 / MT101 | pain.001 |
| Payment status report | — | pain.002 |
| Bank-to-corp confirmation | MT900/910 | camt.054 |

**Bank Account Management (BAM).** The authoritative register of every bank account: bank, number, currency, purpose, signatories, mandates, and open/close status. Weak BAM = zombie accounts, fraud risk, failed audits. TMS modules or eBAM (ISO 20022 acmt messages) automate opening/closing with the bank.

## Hands-on — step by step
**Task 1 — run a physical (ZBA) cash pool for four Indian entities, one currency (INR), end of 14-Jul-2026.** Header = concentration account. End-of-day operating balances before sweep:

- Entity A: +₹3.00 cr
- Entity B: −₹1.20 cr (overdrawn)
- Entity C: +₹0.80 cr
- Entity D: −₹0.40 cr

**Step 1 — Net the pool.** 3.00 − 1.20 + 0.80 − 0.40 = **+₹2.20 cr** net long.

**Step 2 — Sweep to zero.** Each account moves its balance to/from the header:

```
A → header  +3.00      header → B  +1.20
C → header  +0.80      header → D  +0.40
```
Header end balance = 2.20 cr; every operating account = 0.

**Step 3 — Book intercompany.** Each sweep is an IC loan with the header/IHB. A and C are IC *lenders* to the pool; B and D are IC *borrowers*. Balances carried on IHB current accounts.

**Step 4 — Cost the benefit vs standalone.** Without pooling, B and D borrow externally at, say, 9% and A and C earn 5% on deposits. Pooled, the group only has a net +2.20 cr and B/D's overdrafts are funded internally.

- Overdraft interest avoided: (1.20 + 0.40) cr × (9% − 5%) spread /365 per day = 1.60 cr × 4% /365 = **₹1,753/day** ≈ **₹6.4 lakh/year** just on this snapshot spread. Scaled across the year and all entities, pooling saves real money — that's the pitch.

**Step 5 — Charge internal interest.** Header pays A and C, charges B and D, at a policy IC rate (e.g. overnight benchmark + spread), booked monthly on the IHB accounts.

**Task 2 — a 4-week slice of the rolling forecast (₹ cr):**

| Week | Opening | Collections | AP + payroll | Tax/debt | Net | Closing |
|---|---|---|---|---|---|---|
| W1 | 2.20 | 5.0 | −4.2 | −0.6 | +0.2 | 2.40 |
| W2 | 2.40 | 4.5 | −5.0 | 0.0 | −0.5 | 1.90 |
| W3 | 1.90 | 6.2 | −4.8 | −1.5 | −0.1 | 1.80 |
| W4 | 1.80 | 4.0 | −4.6 | 0.0 | −0.6 | 1.20 |

W4 closing ₹1.20 cr is near the ₹1.00 cr minimum — flag it now and pre-arrange line drawdown or delay a discretionary payment.

**Task 3 — execute a supplier payment.** Domestic ₹4.6 cr → RTGS via H2H: TMS generates a **pain.001** file, pushes it over SFTP to the bank, bank returns **pain.002** (accepted), and next morning **camt.053** confirms the debit for reconciliation. Cross-border USD would go as pain.001 → correspondent → beneficiary bank, tracked via SWIFT gpi.

## The output
**Daily cash-pool & sweep report — 14-Jul-2026 (₹ cr)**

```
Entity   Pre-sweep   Sweep       Post   IC position (with IHB)
A          +3.00     -3.00        0.00   IC receivable  3.00
B          -1.20     +1.20        0.00   IC payable     1.20
C          +0.80     -0.80        0.00   IC receivable  0.80
D          -0.40     +0.40        0.00   IC payable     0.40
Header      —        +2.20        2.20   net pool long  2.20
--------------------------------------------------------------
External position: single +2.20 cr, invested overnight.
Overdraft interest avoided today ≈ ₹1,753 (1.60cr @ 4% spread).

Payment executed: RTGS ₹4.60 cr, channel H2H,
   pain.001 sent 11:04, pain.002 ACSC 11:05, camt.053 T+1 tie-out.
Liquidity flag: W4 closing 1.20cr vs 1.00cr min — arrange headroom.
```

## Checks, gotchas & red flags
- **Notional pooling is restricted in India.** RBI/FEMA limit resident notional pooling and cross-border sweeps — don't propose a global notional pool for Indian entities without checking; domestic ZBA is the usual answer.
- **Every physical sweep is an intercompany loan** — needs an IC agreement, arm's-length interest, and transfer-pricing/thin-cap awareness. Auditors will ask.
- **Sweep must leave accounts funded, not just zeroed** — a ZBA that zeroes an account with a cheque still clearing causes a return.
- **ISO 20022 migration is done for cross-border (Nov 2025)** — MT103/MT202 are being retired; make sure files are camt/pain, not legacy MT, or payments reject.
- **BAM hygiene:** unknown or dormant accounts are the top audit finding and a fraud vector. Reconcile the account register to bank confirmations.
- **Forecast variance:** if actuals keep beating/missing forecast, the AR/AP feed is stale — fix inputs, don't just widen buffers.
- **Value date vs booking date** again governs pooling — sweep on cleared funds.

## Interview drill
**Q: Notional vs physical pooling — when would you use each, and what's the India catch?** A: Notional pooling offsets balances on the bank's books with no cash movement and no intercompany loans — clean, but it needs one bank and cross-guarantees, and in India RBI/FEMA restrict resident and cross-border notional pooling. Physical pooling (ZBA) sweeps real cash to a header account, creating intercompany loans that need agreements and arm's-length interest; it works across banks and is the practical domestic route. For an Indian group I'd default to domestic ZBA and keep any notional/cross-border structure offshore and legally cleared.

**Q: What's the difference between SWIFT, host-to-host, and API connectivity?** A: SWIFT is a bank-neutral network — one pipe to many banks, ideal for multi-bank global setups. Host-to-host is a direct secure SFTP link to a single bank, good for high volume with a core bank. APIs are real-time calls for instant balances and payment status. Many corporates run H2H or SWIFT for bulk payments and APIs for real-time visibility.

**Q: What is MT940 and what's replacing it?** A: MT940 is the legacy SWIFT end-of-day bank statement used to reconcile and build the cash position. It's being replaced by ISO 20022 camt.053 (XML), which carries richer structured data; the cross-border MT-to-MX migration completed in November 2025, so treasuries should be consuming camt messages now.

## Learn/practise (free)
- **SWIFT / ISO 20022 (iso20022.org)** — free message specs; read a camt.053 and a pain.001 sample to see the XML structure.
- **RBI website** — FEMA master directions on cash management, pooling, and cross-border remittances (authoritative and free).
- **Bank corporate-banking demos** (HDFC, ICICI, Citi, JPMorgan) publish free H2H/API and pooling brochures.
- **Build the 13-week cash flow** in Excel from a mock AR/AP ledger and track weekly actual-vs-forecast variance — this is the single most requested treasury deliverable.
- **Practise the sweep math**: take four random balances, net them, write the sweep entries and the IC positions, and compute the overdraft-interest saved. Repeat until it's automatic.
- **APIthon / bank sandbox APIs** (some Indian banks and Swift's developer portal) let you call balance and payment-status endpoints free for practice.
