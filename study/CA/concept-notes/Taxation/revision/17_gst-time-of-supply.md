# GST — Time of Supply

> Secs 12–14 CGST Act. Verify current RCM list, advance-on-goods exclusion, ₹1,000 services relief and Sec 14/e-invoicing amendments against ICAI material.

## Snapshot
Time of Supply (TOS) fixes the single moment tax crystallises — and thereby the **rate** and the **return period**. Two instincts: "earliest of" triggers (front-load revenue) + "don't let taxpayer control the clock" (statutory invoice deadline caps delay). Sec 12 = goods, Sec 13 = services, Sec 14 = change in rate (overrides 12/13). Triage first: rate change straddling? → Sec 14. Else forward/reverse → goods/services.

## Core concepts
- **"Date of receipt of payment"** = earlier of (a) entry in supplier's books, or (b) credit to bank.
- **"Date of issue of invoice"** compared against Sec 31 due date (anti-manipulation backstop).
- Goods = visible physical pivot; services = often continuous/invisible → treated differently.
- Golden asymmetry: **advance on GOODS = ignored; advance on SERVICES = taxed.**

## Key provisions / rules

### Sec 31 invoice due dates (the backstop)
| Supply | Invoice due |
|---|---|
| Goods — movement | On/before **removal** |
| Goods — no movement | On/before **delivery**/made available |
| Continuous goods | On/before each statement/payment |
| Goods on approval (sale or return) | Earlier of confirmation OR **6 months** from removal |
| Services (general) | Within **30 days** |
| Services (banks/NBFC/insurer) | Within **45 days** |

### TOS rules
| Scenario | Sec | TOS |
|---|---|---|
| **Goods — forward** | 12(2) | Date of invoice, OR if late/none → **Sec 31 due date** (removal/delivery). **Advance ignored** (but issue receipt voucher u/s 31(3)(d)) |
| **Services — forward** | 13(2) | Invoice within 30/45 days → **earlier of invoice or payment**; if late → **earlier of provision or payment**; else recipient's book entry. **Advance taxed** |
| **Goods — RCM** | 12(3) | **Earliest** of: receipt of goods / payment / (invoice date **+30** days +1). Else book entry |
| **Services — RCM** | 13(3) | **Earliest** of: payment / (invoice date **+60** days +1). Else book entry. Foreign associated enterprise → **earlier of book entry or payment** |
| **Voucher** | 12(4)/13(4) | Supply identifiable at issue → **issue date**; else → **redemption date** (test = rate knowable at issue) |
| **Residual** | 12(5)/13(5) | Return due date; else date tax paid (only when all specific limbs fail) |
| **Interest/late fee/penalty for delayed payment** | 12(6)/13(6) | **Date of receipt** of that amount |

- Invoice can only pull TOS **earlier** than Sec 31 date, never later (early invoice accelerates; late invoice doesn't defer).
- Services small-advance relief: excess **up to ₹1,000** over invoice value → optionally TOS = invoice date (verify figure).
- RCM "payment" = what **recipient pays supplier** (not what supplier receives).

### Sec 14 — Change in rate of tax (overrides 12/13)
Three events {supply, invoice, payment}. **2-of-3 majority** on one side of the rate-change date decides the rate; TOS = date of the winning-side trigger.

**Case A — supply BEFORE change:**
| Invoice | Payment | TOS | Rate |
|---|---|---|---|
| After | After | earlier of invoice/payment | NEW |
| Before | After | invoice date | OLD |
| After | Before | payment date | OLD |

**Case B — supply AFTER change:**
| Invoice | Payment | TOS | Rate |
|---|---|---|---|
| Before | After | payment date | NEW |
| Before | Before | earlier of invoice/payment | OLD |
| After | Before | invoice date | NEW |

**Shortcut:** majority of the 3 events wins the rate; TOS = date on winning side. **Payment proviso:** if bank credit is **>4 working days** after rate change, use bank-credit date (not book entry).

## Worked mini-example
Rate 12%→18% on 1 Sep. Service provided 20 Aug (before), invoice 3 Sep (after), payment 28 Aug (before).
- Supply before → Case A. Events: supply(before) + payment(before) + invoice(after) = **2 before** → **OLD 12%**.
- Case A "invoice after / payment before" → TOS = **payment date 28 Aug**, rate **12%**.
- If payment had also been 3 Sep: invoice+payment both after → **18%**, TOS = 3 Sep.

## Exam traps & must-remember
1. **Advance on goods NOT taxed; advance on services IS** — most tested distinction.
2. Late invoice on **goods** → TOS = Sec 31 due date (removal/delivery), not invoice date.
3. RCM: services backstop **60 days**, goods **30 days**; trigger is day immediately after (+N+1).
4. RCM anchors to recipient's events, not supplier's invoice (except +30/+60 backstop).
5. Sec 14 **overrides** 12/13 — switch the moment a rate change straddles the supply.
6. "Receipt of payment" = earlier of book entry or bank credit (except Sec 14 >4-working-day proviso).
7. Voucher timing = rate-certainty, not cash timing. Single-purpose = issue; general = redemption.
8. Services with advance can have **split TOS** across two months.
9. Continuous supply uses its own Sec 31 dates (not plain 30-day).
10. No-movement goods use **delivery** limb, not removal.
11. Late invoice on **services** → fall to **date of provision** (not invoice date).
12. Foreign associated-enterprise RCM services → **earlier of book entry or payment**.
13. Sec 14 4-working-day proviso can flip payment side and change rate.
14. Receipt voucher still mandatory on advance-for-goods (not taxed ≠ nothing to do).
15. Don't reach residual rule prematurely.

## One-line recall
- Goods forward: invoice or Sec 31 due date; advance ignored.
- Services forward: earlier of invoice/payment (or provision/payment if late); advance taxed.
- RCM goods = earliest of receipt/payment/(invoice+30+1); RCM services = earliest of payment/(invoice+60+1).
- Voucher: identifiable → issue; else redemption. Residual → return due date/tax paid date.
- Interest/late fee → date of receipt.
- Sec 14: majority of {supply, invoice, payment} decides rate; overrides 12/13.
