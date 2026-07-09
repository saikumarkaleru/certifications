<!-- v2-deep -->

# Chapter 17 — Time of Supply

> **Rates / thresholds / amendments flag:** Time-of-supply *provisions* (Secs 12–14 of the CGST Act, 2017) are structurally stable, but the surrounding machinery moves — the removal of the 30-day supplementary-invoice window, the abolition of the earlier "goods on payment" trigger, tweaks to reverse-charge lists, and e-invoicing timelines have all been amended. This chapter teaches the **logic that fixes the taxable moment** so the mechanism is permanent. **Always verify the exact triggers, the current reverse-charge list, and the applicable amendments against current ICAI study material for your attempt.**

---

## 1. The Problem — GST is a tax on an *event*, but events are stretched out in time

GST is charged on the *supply* of goods or services (Sec 9, CGST Act). Good. But a "supply" is not a single instant — it is a **process** smeared across days, weeks, sometimes months. Consider one perfectly ordinary transaction:

- **1 June** — a customer places an order and pays a 20% advance.
- **10 June** — you dispatch the goods.
- **12 June** — the goods reach the customer.
- **15 June** — you raise the tax invoice.
- **20 July** — the customer pays the balance.

The transaction touches *five* different dates. But the tax law needs a **single, unambiguous date** — one moment it can point to and say *"tax became payable here."* Without that single moment, three things collapse:

**Problem 1 — You cannot fix the *rate*.** Suppose GST on this item is 12% until 30 June and rises to 18% from 1 July. Which rate applies — the June rate or the July rate? The answer depends entirely on *which* of those five dates the law treats as decisive. The rate is frozen at the "time of supply"; get the time wrong and every rupee of tax is wrong.

**Problem 2 — You cannot fix the *return period*.** GST is paid month by month. Does this supply belong in the June return (GSTR-3B for June, paid ~20 July) or the July return? If you report it late, you owe **interest under Sec 50** and possibly a late fee. If you report it early, you have parked the government's money before you needed to. The month is decided by the time of supply.

**Problem 3 — You cannot enforce *anything* consistently.** Two honest taxpayers doing the identical deal could pick different dates and pay different tax in different months. A tax that lets each person choose their own moment is unadministrable. The law must **legislate the moment** so it is the same for everyone.

So the "time of supply" (TOS) is not a bookkeeping nicety. It is the **coordinate on the time axis** at which the charge under Sec 9 crystallises. Sec 9 tells you *whether* and *how much*; **time of supply tells you *when*, and through "when," it silently also fixes *which rate*.**

**Why the framers separated "time" from "value" and "place."** GST needs three coordinates to raise a single rupee of tax: *time of supply* (when — Secs 12–14), *place of supply* (where, and hence which tax — IGST Act Secs 10–13), and *value of supply* (how much — Sec 15). These are deliberately three *independent* determinations because each answers a different question and each can move without the others moving. A worked TOS problem answers only one of the three; do not let it bleed into value or place questions. The exam sometimes bundles all three into one problem precisely to see whether you keep them separate.

**A fourth, quieter consequence — input tax credit timing.** The recipient's right to ITC (Sec 16) is not governed by the supplier's TOS directly, but the two are linked in practice: the supplier must have *paid* the tax (which flows from his TOS landing in a return period) before the recipient's credit is safe. So a supplier who mis-times his TOS does not only expose himself to interest — he can jeopardise his customer's credit. TOS is therefore a *systemic* date, not a private one.

---

## 2. The Core Idea

> **The time of supply is the *earliest* of a small set of legally-fixed trigger events — normally issue of invoice, receipt of payment, or (for goods under reverse charge) receipt of the goods. The law picks the *earliest* trigger because it wants the tax in its hands at the first sign that value has changed hands — but it also caps *how late* the invoice trigger can be, so a supplier cannot delay tax simply by delaying his own paperwork.**

Two design instincts run through every rule in this chapter, and if you hold them firmly you can *derive* almost every provision instead of memorising it:

1. **"Earliest of" — the revenue-protection instinct.** The moment *any* recognised marker of the supply appears (money in, or invoice out), tax is due. The government does not wait for the transaction to fully complete. Cash flow to the exchequer is front-loaded.

2. **"Don't let the taxpayer control the clock" — the anti-manipulation instinct.** The invoice is issued *by the supplier*. If TOS depended purely on when he chose to invoice, he could postpone tax indefinitely. So the law imposes a **statutory last date for the invoice** (Sec 31), and if the invoice is late, TOS falls back to an event the taxpayer *cannot* game.

Everything else — the goods-vs-services split, the reverse-charge rules, vouchers, the residual rule, the rate-change rules — is these two instincts applied to different fact patterns.

**A third, subtler instinct — "use the most reliable witness available."** Every trigger the Act picks is an event that leaves an *independent record*: an invoice is a serially-numbered document, a bank credit is a third-party record, a goods-receipt is physically observable. Where one party's record is untrustworthy (the supplier under reverse charge), the law switches the anchor to the *other* party's records. Read every rule as the legislature asking "whose record can we least easily fake, and does that record already exist by this date?" This single question explains why forward charge leans on the supplier's invoice, reverse charge leans on the recipient's receipt/payment, and the residual rule leans on the return-filing deadline (a record the tax system itself owns).

---

## 3. Why It's Built This Way — the design logic before the sections

Before touching a single sub-section, understand the choices the legislature made. Each rule below is one of these choices in disguise.

| Design choice | The problem it solves | How the Act implements it |
|---|---|---|
| A single legislated moment | Supply is stretched across many dates | Secs 12/13 define ONE "time of supply" |
| "Earliest of" triggers | Front-load revenue; catch value the moment it moves | TOS = earliest of invoice / payment / (goods receipt) |
| Statutory last date for invoice | Supplier could delay tax by delaying invoice | Link TOS to Sec 31 due date, not actual invoice date |
| Goods vs services treated differently | Goods = a physical event you can see; services = often continuous, invisible | Sec 12 (goods) vs Sec 13 (services) |
| Reverse charge has its own clock | Recipient pays; supplier's invoice is not a reliable marker | Sec 12(3)/13(3): use goods-receipt / payment / date-of-payment-to-supplier |
| Residual rule | Some cases fit no trigger | Fall back to due date of return or date of tax payment |
| Change-in-rate rule (Sec 14) | Straddling supplies span the rate change | Special "2-of-3" rule *overrides* Secs 12/13 |

### 3.1 Why the advance is (mostly) not taxed for goods any more

Historically GST taxed *advances on goods* at receipt — the "payment" trigger fired even before dispatch. This was an administrative nightmare for small dealers (tax on money before you have even shipped, then reconcile later). By a 2017 notification the government **removed the "receipt of payment" trigger for supply of goods** for all registered persons. So today, for **goods under forward charge, an advance does NOT create a time of supply** — only the invoice (or its due date) matters. **Advances on *services*, however, remain fully taxable at receipt.** Keep this asymmetry burning in your mind; it is the single most examined trap in this chapter.

> **Verify for your attempt:** the notification excluding advances-on-goods from TOS is a rate-notification and could be amended. ICAI has consistently examined the current position (advances on goods not taxed; advances on services taxed). Confirm before your sitting.

### 3.2 Why the advance-on-goods relief does NOT rescue you from paperwork

A subtle exam point: the notification removes the *tax-timing* consequence of an advance on goods, but the supplier must still, on receiving an advance for goods, issue a **receipt voucher** (Sec 31(3)(d)). And if the deal later falls through, a **refund voucher** (Sec 31(3)(e)). So "advance on goods is not taxed" does **not** mean "advance on goods is invisible" — the documentation obligation survives even though no tax is due yet. Examiners test this by asking "what document must the supplier issue on receiving the advance?" — the answer is *receipt voucher*, and the *tax* is still nil until the invoice/removal.

### 3.3 Why "goods" and "services" split the chapter down the middle

The deepest reason for two separate sections is **observability**. A supply of goods has a physical, datable pivot — the goods *move* or are *made available*. That pivot is external, hard to fake, and already captured by the Sec 31 invoice deadline (removal/delivery). A service frequently has **no such pivot**: when exactly is "advisory services" supplied? When the advice is given, drafted, delivered, or acted upon? Because services resist a clean physical pivot, the law keeps the *payment* trigger alive for services (money is at least a datable event) and uses the 30/45-day window as its anti-delay cap. Read Secs 12 and 13 as *the same idea forced to compromise differently* because goods are observable and services often are not.

---

## 4. Full Technical Content — with the "why" welded to each provision

### 4.1 The building-block dates you must define first

Two phrases recur; nail them once.

**"Date of receipt of payment" (per the CGST Rules / Sec 12–13 explanation)** = the **earlier** of:
- (a) the date the payment is **entered in the books** of the supplier, or
- (b) the date the payment is **credited to his bank account**.

*Why the earlier?* Same revenue-protection instinct — whichever proof of payment appears first fixes the moment.

**"Date of issue of invoice"** = the actual date on the invoice — *but* the law constantly compares it to the **due date of issuing the invoice under Sec 31**, because the due date is the anti-manipulation backstop.

**A precision point on "receipt of payment."** The two limbs (book entry / bank credit) exist because either can come first depending on how the business runs. A firm that records a cheque on receipt but banks it days later is fixed by the *book entry*; a firm whose accountant posts entries weekly but whose bank shows an instant NEFT credit is fixed by the *bank credit*. The rule is not "whichever the taxpayer prefers" — it is mechanically **the earlier of the two actual dates**. Examiners give you both dates precisely to see whether you pick the earlier one rather than defaulting to bank credit.

### 4.2 Sec 31 — the invoice due dates (the backstop you cannot skip)

Time of supply for goods/services under forward charge leans on Sec 31, so learn these first.

| Supply | Sec 31 due date for the invoice |
|---|---|
| **Goods — movement involved** | On or **before removal** of goods for supply |
| **Goods — no movement** | On or before **delivery** / making available to recipient |
| **Continuous supply of goods** | On or before each **statement/payment** is issued/received |
| **Goods sent on approval (sale or return)** | Earlier of — when supply is *confirmed*, or **6 months** from removal |
| **Services (general)** | Within **30 days** of supply of service |
| **Services by banks/NBFCs/insurers** | Within **45 days** of supply of service |

*Why a deadline at all?* Because the invoice is the supplier's own document. Sec 31 says "you must invoice by this date," and Sec 12/13 then says "if you invoice late, we tax you as if you had invoiced on time." The two sections lock together to defeat delay.

**The "sale or return" (approval) subtlety.** Goods sent on approval are not yet a supply — the recipient may return them. But the supplier cannot hold them out indefinitely to defer tax. So Sec 31 caps the invoice at the **earlier of confirmation of supply or 6 months from removal**. If neither happens, at 6 months the law *deems* a supply and the invoice falls due, fixing TOS. This is the anti-manipulation instinct applied to a genuinely uncertain supply: uncertainty is tolerated for six months, then forcibly resolved.

### 4.3 Time of supply of GOODS — forward charge (Sec 12(2))

> **TOS of goods = the EARLIER of:**
> **(a) date of issue of invoice, OR the last date on which the invoice *should* have been issued under Sec 31; and**
> **(b) — [the "date of receipt of payment" limb, which has been *removed by notification* for registered suppliers of goods].**

Because limb (b) is switched off for goods, in practice:

> **TOS of goods (forward charge) = date of invoice, OR if the invoice is late/not issued, the Sec 31 due date (i.e. removal for movement cases; delivery otherwise) — whichever of the two applies. The advance is ignored.**

**Worked micro-logic.** Goods removed 10 June, invoice raised 15 June. Sec 31 due date = removal = 10 June. TOS = *earlier* of actual invoice (15 June) and due date (10 June) = **10 June**. The late invoice bought the supplier nothing — exactly the anti-manipulation design at work.

**The mirror case — an *early* invoice.** Goods to be removed 20 June, but invoice raised (with the supplier's choice) on 8 June. Sec 31 due date = removal = 20 June; actual invoice = 8 June. TOS = earlier of (8 June, 20 June) = **8 June**. Here the *invoice* date wins because the supplier issued it *before* the deadline. So the rule is symmetric: an early invoice *accelerates* TOS (it is a genuine trigger), a late invoice does *not defer* it (the deadline catches him). The invoice can only ever pull TOS *earlier* than the Sec 31 date, never later.

```mermaid
flowchart TD
    A["Supply of goods - forward charge"] --> B{"Invoice issued on or before the Sec 31 due date"}
    B -->|Yes| C["TOS equals date of invoice"]
    B -->|No or not issued| D["TOS equals Sec 31 due date - removal or delivery"]
    C --> E["Advance received is ignored for goods"]
    D --> E
```
*Figure 17.1 — Time of supply of goods under forward charge. The payment trigger is switched off, so only invoice timing (capped by the Sec 31 due date) matters.*

### 4.4 Time of supply of SERVICES — forward charge (Sec 13(2))

Services are different in kind. A service is often **invisible and continuous** — consulting, a subscription, a running contract. There is no "removal" you can photograph. So the law keeps the **payment trigger alive** and uses the **30/45-day invoice window** as the anti-manipulation cap.

> **TOS of services = the EARLIEST of:**
> **(a) if invoice issued *within* the Sec 31 window (30/45 days): the EARLIER of (i) date of invoice or (ii) date of receipt of payment; OR**
> **(b) if invoice NOT issued within the window: the EARLIER of (i) date of *provision* of service or (ii) date of receipt of payment; OR**
> **(c) if neither (a) nor (b) applies: the date the recipient shows receipt of the service in his books.**

Decoded into a decision the way you would actually apply it:

1. Was the invoice issued within 30 days (45 for banks etc.)?
2. **Yes →** TOS = earlier of *invoice date* and *payment date*.
3. **No →** TOS = earlier of *date service was provided* and *payment date*.

Notice the elegant symmetry with goods: a **timely** invoice lets you use the invoice date; a **late** invoice throws you back onto an event you cannot manipulate (the actual provision of service). Same instinct, adapted to a continuous supply.

**Advances on services ARE taxed.** Because the payment limb is live, if a client pays you an advance on 1 June for a service invoiced 15 July, the *advance* fixes TOS at 1 June for that portion. This is the asymmetry against goods.

**The "small advance" relief for services — a real exam wrinkle.** The proviso to Sec 13(2) (read with the invoice rules) gives a narrow relief: where the supplier receives an amount **up to ₹1,000 in excess** of the invoice value, he may, *at his option*, treat the TOS of that small excess as the **date of the invoice** for that excess, rather than the date the excess money was received. This spares businesses from raising a fresh tax entry for trivial over-payments (e.g. a customer who rounds ₹4,970 up to ₹5,000). It is optional, capped at ₹1,000 of *excess*, and applies to *services*. Examiners drop a small over-receipt into a services problem to see whether you know the excess need not create a separate earlier TOS. **Verify the ₹1,000 figure against current ICAI material.**

```mermaid
flowchart TD
    A["Supply of services - forward charge"] --> B{"Invoice issued within 30 days - 45 for banks"}
    B -->|Yes| C["TOS equals earlier of invoice date and payment date"]
    B -->|No| D["TOS equals earlier of date service provided and payment date"]
    C --> E{"If neither can be determined"}
    D --> E
    E -->|Fallback| F["TOS equals date recipient records receipt in books"]
```
*Figure 17.2 — Time of supply of services under forward charge. The payment trigger stays live, so advances are taxable; the 30/45-day window is the anti-delay cap.*

### 4.5 Reverse charge — why the clock is completely different (Secs 12(3) & 13(3))

Under **reverse charge (RCM)**, the *recipient* pays the tax, not the supplier. Now think about the design instinct: the trigger events for forward charge (invoice, payment received) are all **the supplier's actions**. But under RCM the supplier may be an unregistered person, a farmer, a foreign entity — someone who may not issue a GST invoice at all and certainly is not the one paying tax. **Using the supplier's invoice as the anchor would be unreliable and unenforceable against the person who actually owes the tax.**

So RCM anchors TOS to events **within the recipient's own control and records** — when *he* got the goods, when *he* paid the supplier — plus a hard backstop.

**Reverse charge on GOODS — TOS = EARLIEST of (Sec 12(3)):**
1. date of **receipt of the goods**;
2. date of **payment** (as entered in recipient's books or debited from bank, whichever earlier);
3. the day **immediately after 30 days** from the date of the supplier's invoice.
> If none can be determined → date of **entry in the recipient's books of account**.

**Reverse charge on SERVICES — TOS = EARLIEST of (Sec 13(3)):**
1. date of **payment**;
2. the day **immediately after 60 days** from the date of the supplier's invoice.
> If neither → date of **entry in the recipient's books**.
> **Special case — associated enterprises where the supplier is *outside India*:** TOS = **earlier of** date of entry in recipient's books **or** date of payment. (Cross-border related-party services have no reliable invoice, so the law leans entirely on the recipient's books/payment.)

Why 30 days for goods but **60 days** for services? Services take longer to complete and invoice, so the recipient is given a longer runway before the "invoice + N days" backstop bites — the same 30-vs-45/60 leniency logic that services get everywhere in GST.

**Note the *asymmetry between forward and reverse* charge on the payment side.** Under forward charge, "payment" means what the *supplier receives*. Under reverse charge, "payment" means what the *recipient pays to the supplier* — the money flows the same direction, but the *anchoring party* is now the recipient, because he is the one whose records the tax officer will audit. Never carry the forward-charge definition of "receipt of payment" mechanically into an RCM problem without asking *whose* payment event the section names.

**Why RCM on goods keeps a "receipt of goods" trigger but forward charge dropped its payment trigger.** These are not contradictory. Forward charge dropped the *supplier's payment* trigger for goods to spare small dealers from taxing advances. RCM keeps a *goods-receipt* trigger because the recipient physically taking delivery is the clearest, earliest, least-fakeable evidence that value has moved to the person who must now pay the tax. Different party, different most-reliable witness.

```mermaid
flowchart TD
    A["Reverse charge liability on recipient"] --> B{"Goods or services"}
    B -->|Goods| C["Earliest of receipt of goods - date of payment - day after 30 days from supplier invoice"]
    B -->|Services| D["Earliest of date of payment - day after 60 days from supplier invoice"]
    C --> E["If none determinable - date of entry in recipient books"]
    D --> E
```
*Figure 17.3 — Reverse charge time of supply. Anchored to the recipient's own events because the supplier's invoice is not a reliable marker when the recipient pays the tax.*

### 4.6 Vouchers (Sec 12(4) for goods / 13(4) for services)

A voucher is a **prepaid instrument** — a gift card, a meal coupon. The problem: has a "supply" happened when the voucher is *sold*, or only when it is *redeemed* for actual goods/services? The answer turns on whether we already know *what* will be bought (and hence its tax rate).

> **Rule: TOS of a voucher =**
> - **If the supply is *identifiable* at the time the voucher is issued → date of *issue* of the voucher.**
> - **If the supply is NOT identifiable at issue → date of *redemption* of the voucher.**

*Why?* GST needs to know the rate. A single-purpose voucher (e.g. a coupon redeemable only for a specific 18% product) already tells us the rate, so tax it at issue. A general "₹1,000 gift card" usable across a store of mixed-rate goods gives us no rate yet, so we must **wait until redemption** to know what was actually supplied. **Rate-certainty drives the timing** — the same logic as Sec 9 needing a rate.

**The vocabulary examiners hide behind.** "Single-purpose voucher" (redeemable for one known type of goods/service at a known rate) maps to *TOS = issue*. "Multi-purpose voucher" or a general gift card maps to *TOS = redemption*. The test is not the *value* on the voucher nor whether it is physical or digital — it is purely **"was the specific supply, and therefore the rate, knowable at issue?"** A ₹500 coupon for "any book" (books being a single rate) can still be identifiable; a ₹500 coupon for "anything in the store" (mixed rates) is not. Read the coupon's *scope*, not its price.

**Edge case — expired/unredeemed vouchers (breakage).** If a general voucher is never redeemed and lapses, no supply of the underlying goods/services ever occurs, so the redemption-based TOS never triggers. The GST treatment of such lapsed value is unsettled and beyond the core Sec 12(4)/13(4) rule — **do not invent a TOS for unredeemed general vouchers in the exam; confine your answer to the issue-vs-redemption test.**

### 4.7 Residual rule (Sec 12(5) / 13(5))

Some cases fit none of the above (records missing, unusual facts). The law needs a guaranteed fallback so a supply can never escape a TOS.

> **Residual TOS =**
> - **where a periodical return must be filed → the date on which that return is *due* to be filed; OR**
> - **in any other case → the date on which the *tax is paid*.**

This is pure gap-filling. It ties TOS to the next hard administrative deadline (the return due date), so there is always a determinable moment.

**When does the residual rule actually bite?** Almost never in a well-documented transaction — and that is the point. It is a *safety net*, not a primary rule. You reach it only after every specific trigger in 12(2)-(4) or 13(2)-(4) has failed to yield a date (e.g. no invoice, no ascertainable payment date, no book entry). In the exam, invoke the residual rule **only** when you can affirmatively show the specific limbs are all indeterminable; reaching for it prematurely is a marked error, because the examiner planted enough facts to solve it under the specific rule.

### 4.8 Time of supply for interest, late fee, penalty for delayed payment (Sec 12(6) / 13(6))

If a supplier charges **interest / late fee / penalty for delayed payment** of consideration, the TOS of *that extra amount* is the **date the supplier *receives* it**. Reason: this add-on is contingent and only becomes real when actually collected, so taxing it on receipt matches its nature.

**Why "receipt" and not the usual earliest-of.** For the *principal* supply, the law front-loads tax (earliest of triggers) because the value is certain. But interest for late payment is *inherently uncertain* — you do not know if, when, or how much you will collect until it arrives. Taxing an uncertain, contingent amount on an "earliest of invoice/payment" basis would tax phantom income. So the Act sensibly waits for **actual receipt**. This is a rare instance where the law deliberately chooses a *later* trigger — because certainty, not just speed, is a competing value. Note this add-on's *value* is part of the value of supply under Sec 15, but its *timing* is governed here.

### 4.9 Change in rate of tax — Sec 14 (overrides Secs 12 & 13)

This is the section examiners love, and it exists for one reason: some supplies **straddle** the moment the rate changes. Three events matter — **(1) supply of goods/service, (2) issue of invoice, (3) receipt of payment** — and the rate change sits somewhere in the middle. Sec 14 gives a clean **"2-out-of-3" majority rule**: look at whether invoice and payment happened *before* or *after* the rate change; whichever period holds the majority (2 of the 3 events) decides the rate.

> **Sec 14 logic (applies where supply is *before* OR *after* the rate change):**

**Case A — Supply *completed BEFORE* the rate change:**

| Invoice | Payment | Time of supply | Rate |
|---|---|---|---|
| After change | After change | earlier of invoice/payment | **NEW** |
| Before change | After change | date of invoice | **OLD** |
| After change | Before change | date of payment | **OLD** |

**Case B — Supply *provided AFTER* the rate change:**

| Invoice | Payment | Time of supply | Rate |
|---|---|---|---|
| Before change | After change | date of payment | **NEW** |
| Before change | Before change | earlier of invoice/payment | **OLD** |
| After change | Before change | date of invoice | **NEW** |

**The shortcut that makes this memoryless — the "2 of 3" test.** Take the three events {supply, invoice, payment}. If **two or more** fall on the *same side* of the rate-change date, that side wins:
- Supply before + (any two of the three before) → **old rate**; majority after → **new rate**.
- Equivalently: when **supply and one other event** are on the same side, that side's rate applies; when supply is alone, the **invoice-and-payment pair** decides.

You never need the two tables above if you internalise: **the majority of the three events wins, and the "time of supply" is the date of whichever event(s) sit on the winning side.**

**Reading the tables against the shortcut so you trust it.** Take Case A row 2: supply before, invoice before, payment after → two events (supply + invoice) before → old rate, and TOS = date of invoice (the "before-side" event that is a trigger). Case B row 1: supply after, invoice before, payment after → two events (supply + payment) after → new rate, TOS = date of payment. Every row is just "count the majority, then read off the winning-side trigger date." Where supply is *alone* on its side (Case A rows 2 and 3 are *not* this; look at Case A row 1 vs the structure), the invoice+payment pair are together and they decide both the rate and, being the two triggers, the TOS via *earlier of the two*. The tables and the shortcut are the same machine.

> **Payment-date relief under Sec 14:** for the purpose of Sec 14, if payment is credited to the bank account **more than 4 working days after** the rate change, the date of receipt of payment is taken as the **date of bank credit** (not book entry). This narrow proviso stops manipulation of the "book entry" date around a rate change.

**Why Sec 14 *overrides* Secs 12 and 13, not the other way round.** Secs 12/13 assume a *stable* rate — they only tell you *when*, and *when* silently picks the rate because the rate is constant across the relevant window. But when the rate itself moves mid-transaction, "when" is no longer enough — two supplies with identical TOS under Sec 12 could deserve different rates depending on where the *supply* sat relative to the change. Sec 14 therefore re-computes both the rate *and* the TOS using the three-event majority, and expressly says "notwithstanding sections 12 and 13." The moment a rate-change date appears in a problem straddled by the supply, **stop applying 12/13 and switch to Sec 14** — mixing the two is the single most common way students lose these marks.

```mermaid
flowchart TD
    A["Rate of tax changes on a date"] --> B{"How many of the three events fall on each side"}
    B --> C["Events - supply - invoice - payment"]
    C --> D{"Two or more BEFORE the change"}
    D -->|Yes| E["Old rate applies - TOS is date on the before side"]
    D -->|No| F["New rate applies - TOS is date on the after side"]
```
*Figure 17.4 — Change in rate of tax under Sec 14. The majority of the three events (supply, invoice, payment) decides the rate and the time of supply.*

### 4.10 The master decision flow — choosing the right rule first

Most wrong answers come not from mis-applying a rule but from applying the *wrong* rule. Before any computation, run this triage: is a rate change straddling the supply (→ Sec 14, stop)? If not, is it forward or reverse charge? Then goods or services? Only then apply the specific limb.

```mermaid
flowchart TD
    A["A supply - determine TOS"] --> B{"Does a rate change straddle this supply"}
    B -->|Yes| C["Apply Sec 14 - two of three majority - ignore Secs 12 and 13"]
    B -->|No| D{"Forward charge or reverse charge"}
    D -->|Reverse charge| E{"Goods or services"}
    E -->|Goods| F["Sec 12(3) - earliest of receipt - payment - invoice plus 30"]
    E -->|Services| G["Sec 13(3) - earliest of payment - invoice plus 60"]
    D -->|Forward charge| H{"Goods or services"}
    H -->|Goods| I["Sec 12(2) - invoice date or Sec 31 due date - advance ignored"]
    H -->|Services| J["Sec 13(2) - earlier of invoice or payment - advance taxed"]
    F --> K{"Is it a voucher"}
    G --> K
    I --> K
    J --> K
    K -->|Yes| L["Sec 12(4) or 13(4) - identifiable at issue then issue else redemption"]
    K -->|No trigger determinable| M["Residual - Sec 12(5) or 13(5) - return due date or date tax paid"]
```
*Figure 17.5 — Master triage. Pick the correct rule before computing; Sec 14 pre-empts everything when a rate change straddles the supply.*

---

## 5. Worked Examples — full, reconciling determinations

### Example 1 — Goods, forward charge, late invoice, with an advance

**Facts.** Rex Ltd manufactures fans (registered, forward charge). For an order:
- 5 August — customer pays 30% advance (₹30,000 of ₹1,00,000).
- 12 August — goods **removed** from factory for delivery.
- 18 August — tax **invoice** issued.
- 2 September — balance ₹70,000 received.

**Determine the time of supply.**

**Step 1 — Which rule?** Goods, forward charge → **Sec 12(2)**.
**Step 2 — Payment trigger?** For goods, the receipt-of-payment trigger is **removed**. So the 5 August advance and the 2 September balance are **both irrelevant** to TOS.
**Step 3 — Invoice vs Sec 31 due date.** Movement is involved → invoice due **on/before removal = 12 August**. Actual invoice = 18 August (late).
**Step 4 — TOS = earlier of actual invoice (18 Aug) and due date (12 Aug) = 12 August.**

**Reconciliation.** The whole ₹1,00,000 is taxed with TOS 12 August (August return). The late invoice did not defer tax; the advance did not accelerate it. Both design instincts visible in one example.

---

### Example 2 — Services, forward charge, advance received, invoice within window

**Facts.** Vega Consultants (registered) render advisory services.
- 10 June — client pays ₹40,000 advance.
- 28 June — service **completed**.
- 5 July — **invoice** for full ₹1,50,000 issued.
- 20 July — balance ₹1,10,000 received.

**Determine the time(s) of supply.**

**Step 1 — Rule.** Services, forward charge → **Sec 13(2)**. Payment trigger is **live**.
**Step 2 — Invoice within window?** Service completed 28 June; invoice 5 July → **7 days**, well within 30 days. So use: TOS = **earlier of invoice date and payment date**, applied to each receipt.
**Step 3 — The advance (₹40,000).** Earlier of payment (10 June) and invoice (5 July) = **10 June**. So ₹40,000 has **TOS 10 June** (June return).
**Step 4 — The balance (₹1,10,000).** Earlier of payment (20 July) and invoice (5 July) = **5 July**. So ₹1,10,000 has **TOS 5 July** (July return).

**Reconciliation.** Total consideration ₹1,50,000 = ₹40,000 (taxed June) + ₹1,10,000 (taxed July). The advance-on-service was taxed at receipt — the exact opposite of goods in Example 1. Split TOS is normal for services with advances.

---

### Example 3 — Reverse charge on goods

**Facts.** Orion Ltd buys goods from an unregistered dealer; the supply is under **RCM**.
- Supplier's invoice dated 1 October.
- Goods **received** by Orion 6 October.
- Orion **pays** the supplier 25 October.

**Determine the time of supply.**

**Rule — Sec 12(3):** earliest of
- receipt of goods = **6 October**;
- date of payment = **25 October**;
- day after 30 days from invoice = 1 Oct + 30 = 31 Oct → **1 November**.

**TOS = earliest = 6 October.** Orion accounts for RCM tax in its **October** return. Note TOS is anchored to *Orion's* events (its receipt of goods), not the supplier's invoice date — because Orion is the one paying the tax.

---

### Example 4 — Reverse charge on services, invoice-plus-60-days backstop bites

**Facts.** Orion Ltd receives legal services (RCM) from an advocate.
- Advocate's invoice dated 1 October.
- Orion **pays** on 20 December.

**Rule — Sec 13(3):** earliest of
- date of payment = **20 December**;
- day after 60 days from invoice = 1 Oct + 60 = 30 Nov → **1 December**.

**TOS = earliest = 1 December.** Because Orion delayed payment past the 60-day backstop, the *"invoice + 60 days"* limb fires first. Orion cannot defer RCM tax to December simply by paying late — the backstop pulls TOS into the **December return** period (1 Dec), and interest would run if reported later. Anti-manipulation instinct again.

---

### Example 5 — Change in rate of tax (Sec 14)

**Facts.** GST rate on a service rises from **12% to 18% on 1 September**. For one engagement:
- Service **provided**: 20 August (**before** change).
- **Invoice** issued: 3 September (**after** change).
- **Payment** received: 28 August (**before** change).

**Determine TOS and the applicable rate.**

**Step 1 — Supply is before the change → Case A.**
**Step 2 — 2-of-3 test.** Events: supply (20 Aug, before), invoice (3 Sep, after), payment (28 Aug, before). **Two events (supply + payment) are before** the change → **old side wins → OLD rate 12%.**
**Step 3 — TOS is the date on the winning (before) side that the table specifies.** Invoice after + payment before → TOS = **date of payment = 28 August**, rate **12%**.

**Reconciliation with the table.** Case A, "invoice after / payment before" → TOS = payment date, OLD rate. Matches. Had the payment *also* been on 3 September (after), then supply alone would be before, invoice+payment both after → majority after → **18%**, TOS = earlier of invoice/payment = 3 September. The single moving fact (payment side) flips the rate — exactly what Sec 14 is designed to resolve cleanly.

---

### Example 6 — Voucher

**Facts.** A retail chain sells (a) a coupon redeemable only against a specific 18% branded appliance, issued 10 May, redeemed 2 July; and (b) a generic ₹5,000 store gift card usable on any product, issued 10 May, redeemed 2 July.

- **(a) Single-purpose (supply identifiable at issue):** TOS = **date of issue = 10 May** (rate is already known — 18%).
- **(b) General gift card (supply not identifiable at issue):** TOS = **date of redemption = 2 July** (only then is it known what was bought and at what rate).

**Reconciliation.** Same two dates, opposite TOS — driven purely by whether the rate was knowable at issue. That is the whole of Sec 12(4)/13(4).

---

### Example 7 — Goods, forward charge, "no movement" supply (delivery, not removal)

**Facts.** Nimbus Ltd sells a large fabrication rig that is **installed at the buyer's site and never physically "removed"** in the ordinary sense — it is *made available* to the buyer on 14 November. Invoice is raised 9 November. An advance of ₹2,00,000 was received on 1 November.

**Determine the time of supply.**

**Step 1 — Rule.** Goods, forward charge → **Sec 12(2)**; payment trigger removed, so the 1 November advance is **ignored**.
**Step 2 — Which Sec 31 limb?** No movement is involved → invoice due **on/before delivery / when goods are made available = 14 November**.
**Step 3 — Invoice 9 November is *before* the due date (14 Nov).** So the invoice is timely and is itself the earlier trigger.
**Step 4 — TOS = earlier of invoice (9 Nov) and due date (14 Nov) = 9 November.**

**Reconciliation.** This is the *early-invoice* mirror of Example 1: because the invoice preceded the Sec 31 deadline, the invoice date governs. The examiner's trap here is twofold — (i) using the "removal" limb when the correct limb is "delivery/made available" for a no-movement supply, and (ii) taxing the 1 November advance, which for goods must be ignored. TOS falls in the **November** return regardless, but for the *right* reasons.

---

### Example 8 — Services, forward charge, invoice issued LATE (window breached)

**Facts.** Zephyr LLP (registered, general services — 30-day window) completes a service on **5 January**. It issues the invoice only on **20 February** (46 days later — outside 30 days). The client pays on **28 February**. No advance.

**Determine the time of supply.**

**Step 1 — Rule.** Services, forward charge → **Sec 13(2)**.
**Step 2 — Was the invoice within the 30-day window?** Service provided 5 Jan; 30 days ends 4 Feb. Invoice 20 Feb is **late**. So we drop to limb (b): **TOS = earlier of (date of provision of service) or (date of payment).**
**Step 3 — Compute.** Date of provision = **5 January**; date of payment = 28 February. Earlier = **5 January**.
**Step 4 — TOS = 5 January** (January return).

**Reconciliation.** Because Zephyr blew the 30-day window, the law refused to let the *invoice date* (20 Feb) govern and threw TOS back to the un-manipulable *date of provision* (5 Jan). Zephyr therefore owes tax in the **January** return and interest under Sec 50 for every day it under-reported — a punitive outcome engineered by the anti-delay cap. Contrast Example 2, where a *timely* invoice let the invoice date govern. The single variable that flips the whole answer is *whether the 30-day window was met*.

---

### Example 9 — Change in rate (Sec 14), supply AFTER the change, with the 4-day payment proviso

**Facts.** GST on a service **falls from 18% to 12% on 1 October**. For one engagement:
- Service **provided**: 8 October (**after** change).
- **Invoice** issued: 24 September (**before** change).
- **Payment**: entered in the supplier's books 27 September (**before**), but actually **credited to the bank on 9 October** — i.e. more than 4 working days after the 1 October change.

**Determine TOS and rate.**

**Step 1 — Supply is *after* the change → Case B.**
**Step 2 — Apply the payment proviso first.** Because bank credit (9 Oct) is **more than 4 working days after** the rate-change date (1 Oct), the date of receipt of payment is deemed to be the **date of bank credit = 9 October** (not the 27 September book entry). So *payment counts as AFTER* the change.
**Step 3 — 2-of-3 test.** Events: supply (8 Oct, after), invoice (24 Sep, before), payment (9 Oct, after). Two events (supply + payment) after → **new side wins → NEW rate 12%.**
**Step 4 — TOS.** Case B, "invoice before / payment after" → TOS = **date of payment = 9 October**, rate **12%.**

**Reconciliation.** Without the proviso, a taxpayer could backdate the *book entry* to 27 September to drag payment onto the "before" side and claim the 18%/12% treatment he preferred. The proviso closes that door: once bank credit lands beyond 4 working days of the change, the *bank* date (an independent third-party record) governs. Had the bank credited within 4 working days, the 27 September book entry would have stood and payment would count as *before*, giving supply-after but invoice+payment-before → majority before → **old 18%**, TOS = earlier of invoice/payment. One proviso, opposite result — a favourite examiner pivot.

---

### Example 10 — Reverse charge on services, associated enterprise with a supplier outside India

**Facts.** Helios Ltd (India) receives management services under RCM from its **parent company located outside India** (an associated enterprise). The parent raises an invoice on 5 March. Helios records the service in its books on **20 February** (accrued earlier) and pays on **15 April**.

**Determine the time of supply.**

**Step 1 — Rule.** RCM services → Sec 13(3), *but* this is the **special case**: supplier is an *associated enterprise located outside India*. TOS = **earlier of** (date of entry in the recipient's books) or (date of payment).
**Step 2 — Compare.** Book entry = **20 February**; payment = 15 April. Earlier = **20 February**.
**Step 3 — TOS = 20 February** (February return).

**Reconciliation.** Note the ordinary Sec 13(3) triggers (payment, or invoice+60 days) would have pointed at 15 April or ~4 May — *later*. The special associated-enterprise rule deliberately anchors TOS to the *earlier* of book entry or payment, precisely because cross-border related parties can arrange invoices and payments at will, so the law leans on the recipient's *accrual entry* (20 Feb) to catch the value the moment Helios recognised it. The trap is applying the plain "payment or invoice + 60 days" limb and missing that the associated-enterprise-abroad override pulls TOS all the way back to the book entry.

---

## 6. Format / Summary Table

| Scenario | Section | Time of supply = |
|---|---|---|
| **Goods — forward charge** | 12(2) | Date of invoice, or if late/none, **Sec 31 due date** (removal/delivery). *Advance ignored.* |
| **Services — forward charge** | 13(2) | Invoice in 30/45 days → **earlier of invoice or payment**; else **earlier of provision or payment**; else recipient's book entry. *Advance taxed.* |
| **Goods — reverse charge** | 12(3) | **Earliest** of: receipt of goods / payment / (invoice + 30 days + 1). Else book entry. |
| **Services — reverse charge** | 13(3) | **Earliest** of: payment / (invoice + 60 days + 1). Else book entry. Assoc. enterprise (foreign supplier) → earlier of book entry or payment. |
| **Voucher** | 12(4)/13(4) | Identifiable at issue → **issue date**; else **redemption date**. |
| **Residual** | 12(5)/13(5) | Return due date; else date tax is paid. |
| **Interest/late fee/penalty** | 12(6)/13(6) | **Date of receipt** of that amount. |
| **Change in rate** | 14 | **2-of-3** of {supply, invoice, payment} on same side → that side's rate; TOS = date on winning side. |

**One-line spine:** *Forward charge on goods watches the invoice; forward charge on services watches invoice-or-payment; reverse charge watches the recipient's own goods-receipt/payment plus an invoice-plus-N-days backstop; rate changes are decided by majority of three events.*

---

## 7. Connections

- **Sec 9 (Charge) → Sec 12–14 (Time):** Sec 9 says *whether* and *how much*; TOS says *when*, and *when* silently fixes *which rate* (Sec 14).
- **Sec 31 (Tax invoice):** TOS of forward-charge supplies is bolted to the Sec 31 invoice due dates. You cannot solve a TOS problem without knowing Sec 31 — study them together. Sec 31(3) documents (receipt voucher, refund voucher, payment voucher for RCM) also surface in TOS problems.
- **Sec 13 of IGST Act / place of supply:** *Time* and *place* of supply together decide *which* tax (CGST+SGST vs IGST) applies *when*. TOS fixes the tax period; place of supply fixes the tax's identity.
- **Sec 50 (Interest):** get TOS wrong → wrong return period → interest for delayed payment. TOS errors are expensive.
- **Reverse charge (Sec 9(3)/9(4)):** TOS under RCM (12(3)/13(3)) only matters once you have determined a supply *is* under RCM — link to the RCM chapter. Under RCM the recipient also issues a **payment voucher** (Sec 31(3)(g)) and, if the supplier is unregistered, a **self-invoice** (Sec 31(3)(f)).
- **Value of supply (Sec 15):** advances on services are taxed at TOS but the *value* on which tax is computed comes from Sec 15; interest/late fee for delayed payment is *valued* under Sec 15 but *timed* under 12(6)/13(6).
- **Input tax credit (Sec 16):** the supplier's TOS drives when he pays tax, which conditions the recipient's ability to safely claim ITC — TOS is a systemic, not private, date.

---

## 8. Traps & Examiner Tricks

1. **Advance on GOODS is NOT taxed; advance on SERVICES IS.** The single most tested distinction. If the question gives an advance on goods, ignore it for TOS; on services, it fixes a TOS.
2. **Late invoice does not defer tax on goods.** TOS drops to the Sec 31 due date (removal/delivery), not the actual invoice date. Students wrongly use the late invoice date.
3. **RCM services backstop is 60 days, goods is 30 days.** Swapping them is a classic error. Also: the trigger is the day *immediately after* the 30/60 days, i.e. invoice date + N + 1.
4. **RCM anchors to the recipient's events, not the supplier's invoice date** (except via the +30/+60 backstop). Do not use "date of invoice" as a standalone RCM trigger.
5. **Sec 14 overrides Secs 12/13.** The instant a question mentions a rate change straddling the supply, abandon the normal rules and run the 2-of-3 test.
6. **"Receipt of payment" = earlier of book entry or bank credit.** Not just bank credit (except the Sec 14 >4-working-days proviso).
7. **Voucher timing is about rate-certainty, not about when cash was taken.** Single-purpose = issue; general = redemption.
8. **Splitting the invoice value across two TOS.** For services with an advance, the advance and the balance can have *different* TOS in *different* months — you must split (Example 2).
9. **Continuous supply** has its own Sec 31 invoice dates (tied to statements/payments); do not apply the plain 30-day rule.
10. **"No movement" goods use the *delivery* limb, not removal.** For goods made available on site (no physical removal), the Sec 31 due date is *delivery/made available*, not removal (Example 7).
11. **Missing the 30/45-day window flips services onto the *date of provision*.** If the invoice is late for a service, do not fall back to the invoice date — fall back to the *date the service was provided* (Example 8). This is the mirror of trap 2 for services.
12. **The associated-enterprise-abroad override for RCM services.** When the RCM supplier is a foreign associated enterprise, TOS is the *earlier of book entry or payment* — often far earlier than the ordinary "payment / invoice + 60" limb (Example 10).
13. **The Sec 14 4-working-days payment proviso.** If bank credit lands more than 4 working days after the rate change, use the *bank-credit* date, not the book entry — this can flip payment to the "after" side and change the rate (Example 9).
14. **Receipt voucher survives the advance-on-goods relief.** No tax on the advance, but a *receipt voucher* is still mandatory. Questions on "what document is issued" trip students who think "not taxed = nothing to do."
15. **Do not reach the residual rule prematurely.** It applies only when every specific trigger is genuinely indeterminable; the examiner usually plants enough facts to solve under the specific limb.

---

## 9. First-Principles Recap

Start from nothing and rebuild the chapter:

1. GST taxes a *supply*, but a supply is smeared across many dates. The tax needs **one** date. → *Time of supply exists.*
2. The exchequer wants money early and cannot let taxpayers stall. → **Earliest-of triggers**, capped by a **statutory invoice deadline (Sec 31)**.
3. **Goods** are a visible physical event; the invoice (capped at removal/delivery) is a reliable marker, and taxing advances on goods was a nuisance, so the payment trigger was switched off. → *Goods TOS watches the invoice only.*
4. **Services** are often continuous and invisible; there is no "removal," so the **payment trigger stays live** and a **30/45-day invoice window** is the anti-delay cap. → *Services TOS = earlier of invoice/payment (or provision/payment if invoice is late); advances taxed.*
5. Under **reverse charge** the recipient pays, so the supplier's invoice is not a trustworthy anchor. → *Anchor to the recipient's goods-receipt/payment, with an invoice+30/60-day backstop; foreign associated enterprise → earlier of book entry or payment.*
6. **Vouchers** need a known rate; if the supply is identifiable at issue, tax at issue, else at redemption.
7. Any gap → **residual rule** (return due date / date tax paid) — a safety net, reached only when specific triggers fail.
8. When the **rate changes** mid-transaction, whichever period holds **2 of the 3 events** (supply, invoice, payment) wins the rate, and TOS is the date on that winning side (Sec 14, overriding 12/13); a payment credited >4 working days after the change is dated by bank credit.
9. Contingent add-ons (interest/late fee for delayed payment) are uncertain, so — uniquely — they are taxed on **actual receipt**, not earliest-of.

Every provision in the chapter is one of these nine sentences. You did not memorise; you *derived*.

---

## 10. Quick-Revision Sheet

**Core moment:** TOS = earliest legally-fixed trigger; invoice trigger capped by Sec 31 due date. **Triage first:** rate change straddling? → Sec 14. Else forward/reverse → goods/services.

**Goods — forward (Sec 12(2)):** invoice date, else Sec 31 due date (removal for movement / delivery for no-movement). **Advance IGNORED** (but issue a receipt voucher).

**Services — forward (Sec 13(2)):**
- Invoice within 30 days (45 = banks/NBFC/insurer) → **earlier of invoice or payment**.
- Invoice late → **earlier of provision or payment**.
- Else → recipient's book entry. **Advance TAXED.** Excess ≤ ₹1,000 → optionally TOS = invoice date (verify figure).

**Goods — RCM (Sec 12(3)):** earliest of — receipt of goods / payment / (invoice **+30** days +1). Else book entry.

**Services — RCM (Sec 13(3)):** earliest of — payment / (invoice **+60** days +1). Else book entry. Foreign associated enterprise → **earlier of book entry or payment**.

**Voucher (12(4)/13(4)):** identifiable at issue → **issue**; else → **redemption**. (Test = was the rate knowable at issue.)

**Residual (12(5)/13(5)):** return due date; else date tax paid. (Only when specific limbs all fail.)

**Interest/late fee/penalty (12(6)/13(6)):** date of **receipt** (contingent → wait for the cash).

**Receipt of payment** = earlier of book entry or bank credit.

**Change in rate (Sec 14) — 2-of-3 rule (overrides 12/13):**
- Supply **before** change: both invoice+payment after → NEW (earlier of the two); one before → OLD (that date).
- Supply **after** change: both invoice+payment before → OLD (earlier of the two); one after → NEW (that date).
- Shortcut: majority of {supply, invoice, payment} on one side → that side's rate; TOS = date on winning side. Payment >4 working days after change → use bank-credit date.

**Golden asymmetries to never forget:** advance on goods = ignored / advance on services = taxed; RCM goods +30 / RCM services +60; single-purpose voucher = issue / general = redemption; late invoice on goods → Sec 31 due date / late invoice on services → date of provision; contingent charges → taxed on receipt.

> **Flag:** verify the advance-on-goods exclusion, the ₹1,000 services-excess relief figure, the current RCM list, and any Sec 14 / e-invoicing amendments in the latest ICAI material for your attempt.
