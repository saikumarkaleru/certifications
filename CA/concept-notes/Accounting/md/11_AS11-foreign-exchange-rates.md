# Chapter 11 — AS 11: The Effects of Changes in Foreign Exchange Rates

## 1. The Problem — the real business situation that created the need

Picture an Indian company, Bharat Motors Ltd. It keeps its books in Rupees because that is the currency of the country it lives in, pays salaries in, files taxes in, and reports profit in. That currency — the one in which it primarily generates and spends cash and in which it presents its accounts — is its **reporting currency**.

Now Bharat Motors does something perfectly ordinary in the modern economy: on 1 January it imports steel from Germany for **€100,000**, to be paid after 90 days. On the day of purchase the exchange rate is ₹90 per euro. So the steel costs ₹90,00,000. Fine. Bharat Motors records an asset (steel) and a liability (payable to the German supplier).

Here is where the trouble starts. Money owed in euros does not sit still in Rupee terms. By 31 March, when Bharat Motors closes its books, the euro has strengthened to ₹93. Bharat Motors still owes exactly €100,000 — that number has not moved — but in Rupees that same debt is now worth ₹93,00,000. When it finally pays on 5 April, the rate is ₹94, so it actually hands over ₹94,00,000.

Three different Rupee numbers — ₹90,00,000, ₹93,00,000, ₹94,00,000 — for **one unchanging foreign-currency obligation of €100,000**. Which one is "true"? At what rate do we record the steel? At what rate do we show the payable on the balance sheet date? And that extra ₹4,00,000 Bharat Motors ended up paying — is it part of the cost of the steel? Interest? A loss? Where does it go?

This is not a rare corner case. Every importer, exporter, foreign borrower, company with an overseas branch or subsidiary, and anyone holding foreign currency, foreign receivables, or foreign loans faces it. Multiply Bharat Motors' single transaction by thousands of transactions across hundreds of companies and you see the scale of the problem: **foreign-currency amounts must be expressed in Rupees to be put into a Rupee balance sheet, but the exchange rate keeps changing, so the same foreign amount maps to different Rupee amounts at different dates.** Without a rule, every company would translate at whatever rate flattered its profit. AS 11 exists to impose one disciplined, economically honest way of doing this translation — and, crucially, of deciding where the gains and losses from rate changes belong.

## 2. The Core Idea — the single underlying principle

Strip AS 11 to its spine and it says this:

> **A foreign-currency amount is not a Rupee amount. It is a claim expressed in a different unit. To put it in Rupee books you must translate it using an exchange rate — and the *right* rate depends on whether the item is still "live" in foreign currency (its Rupee value genuinely fluctuates with the market) or is "frozen" at a past moment (its Rupee value was fixed when the transaction happened).**

The analogy that unlocks everything: think of a foreign-currency balance like **ice versus water**.

- Cash in a US-dollar bank account, a dollar receivable, a euro loan — these are **water**. They are alive, flowing, exposed to the market. If the rate moves, their real Rupee worth moves *today*. A dollar in your pocket buys more Rupees when the dollar strengthens. These are **monetary items**, and they must be re-measured (re-translated) at every balance sheet date using the **current rate** because their Rupee value genuinely is different now.

- A building you bought abroad, machinery, inventory, prepaid rent, goodwill — these are **ice**. The transaction that created them is over; the Rupee cost was locked in at the historical rate on the day you paid. A rate change afterward does not change what that building cost you. These are **non-monetary items**, and you leave them at the **historical rate** — you do not keep re-translating them.

That single distinction — *is this item a live foreign-currency claim (monetary) or a settled historical cost (non-monetary)?* — drives almost every rule in the standard. Once you truly feel *why* water must be re-measured and ice must not, you can re-derive the entire chapter from scratch instead of memorizing it.

The second half of the core idea answers "where does the gain/loss go?" The general answer is beautifully simple: **exchange differences on monetary items go straight to the Profit & Loss account** in the period they arise. The rate moved, your real position changed, so recognize it now.

## 3. Why it's built this way — the logic behind each rule

Let us reason our way into each design choice, because that is the only way to never forget them.

**Why translate at all?** Because a balance sheet must be in one currency. You cannot add ₹90,00,000 of Rupee cash to €100,000 of steel — the units don't match. Translation is just the "conversion of units" step, like converting kilometres to metres before you can add them.

**Why re-measure monetary items but freeze non-monetary items?** This is the heart of it. Accounting cost is meant to reflect economic reality.
- A €100,000 payable is a *promise to deliver €100,000 in the future*. Its burden on you, measured in your own currency, literally changes as the rate changes. If the euro rises, you will have to give up more Rupees — you are genuinely worse off *now*, before you even pay. Reporting it at the old ₹90 rate would hide a real, present increase in your liability. So we must show it at the current rate. That is faithful representation.
- A building bought for €100,000 is different. You already gave up the euros. The building is yours. Its *cost* is a historical fact — ₹90,00,000 — and no subsequent rate wiggle retroactively changes what you paid. Re-translating it every year would invent phantom gains and losses on an asset whose cost is settled and whose future value depends on its own usefulness, not on the euro. So we freeze it. (Its carrying amount may later be tested for impairment or, if it's inventory, compared to NRV — but that's a different question than exchange translation.)

**Why send exchange differences to P&L immediately (the general rule)?** Because the change has already happened and it is real. When your dollar receivable is worth more Rupees today, that gain is economically yours *now* — there is no reason to defer it. Accrual accounting recognizes changes when they occur, not only when cash moves. Deferring genuine exchange gains/losses would let companies smooth or hide their real currency exposure. So AS 11 says: recognize them in the period they arise, in P&L. This applies at **each** stage — at the balance sheet date (unrealized) and at settlement (realized). The standard deliberately does not wait for settlement, because a rate change is a real event even before you pay.

**Why do forward contracts need special handling?** Because a company that has locked in a future rate has *removed* its uncertainty. If Bharat Motors, on the day of import, books a forward contract to buy €100,000 at ₹91 in 90 days, then its real Rupee cost is fixed at ₹91,00,000 no matter what the spot rate does. The accounting should reflect that the ₹1,00,000 difference (forward ₹91 vs spot ₹90) is a known, financing-like cost to be spread over the 90 days — not a surprise. The rules for forwards exist to match this economic certainty.

**Why distinguish integral from non-integral foreign operations?** Because a foreign branch/subsidiary can relate to the parent in two completely different economic ways, and honesty demands different treatment:
- An **integral** operation is really just an extension of the parent's own business done abroad — a dependent limb. Its cash flows *are* the parent's cash flows in another currency. So its exchange exposure is the parent's exposure, and it is translated *as if the parent had done those transactions itself* (monetary/non-monetary split, differences to P&L).
- A **non-independent... no — a non-integral** operation is a self-contained foreign business that earns and spends in its own local currency, accumulates its own profits, and only sends dividends home. The parent's real exposure here is limited to its **net investment** in that operation. Re-translating each internal item to P&L would be misleading noise. So we translate the whole thing at closing rate and park the difference in a reserve — until the parent actually disposes of the investment and the gain/loss becomes real.

Every rule below is a consequence of these few principles.

## 4. Full Technical Content — through the RMPD lens

### 4.1 Scope and key definitions (the vocabulary you must own)

AS 11 applies to (a) accounting for **transactions in foreign currencies**, and (b) **translating the financial statements of foreign operations** (branches, subsidiaries, associates, JVs). It also covers forward exchange contracts. It does **not** deal with hedge accounting for items other than forward contracts, nor with restating financial statements for inflation, nor (directly) with foreign-currency borrowing costs — those interact with AS 16.

Definitions you must be able to state precisely:

| Term | Meaning | Why it matters |
|---|---|---|
| **Reporting currency** | The currency in which financial statements are presented (₹ for an Indian company). | The target unit of all translation. |
| **Foreign currency** | A currency other than the reporting currency. | The source unit being translated. |
| **Exchange rate** | Ratio for exchange of two currencies. | The conversion factor. |
| **Monetary items** | Money held, and assets/liabilities to be **received or paid in fixed or determinable amounts of money**. | These are re-translated at current rates ("water"). |
| **Non-monetary items** | Assets and liabilities **other than** monetary items. | These stay at historical rate ("ice"). |
| **Closing rate** | The exchange rate at the balance sheet date. | Used to re-measure monetary items and to translate non-integral operations. |
| **Average rate** | A rate approximating the actual rates over a period. | A practical shortcut for many similar transactions / P&L items. |
| **Fair value** | Amount for which an asset could be exchanged / liability settled between knowledgeable, willing parties in an arm's-length transaction. | Relevant when a non-monetary item is carried at fair value. |
| **Integral foreign operation** | A foreign operation whose activities are an **integral part** of the reporting enterprise. | Translated using the parent's own rules. |
| **Non-integral foreign operation** | A foreign operation that is **not** integral — it operates with a degree of autonomy. | Translated at closing rate; difference to reserve. |
| **Net investment in a non-integral operation** | The reporting enterprise's share in the **net assets** of that operation. | Defines the parent's true exposure. |

**The monetary vs non-monetary test — the single most examined judgment.** Ask: *"Is this item a right to receive, or an obligation to pay, a fixed or determinable number of currency units?"* If yes → monetary. If it is a thing or a right whose amount is not a fixed sum of money → non-monetary.

| Item | Monetary or Non-monetary? | Reasoning |
|---|---|---|
| Cash, bank balances | Monetary | Money itself. |
| Trade receivables / payables | Monetary | Fixed sums to be received/paid. |
| Loans given / taken, deposits | Monetary | Fixed determinable money. |
| Provision to be settled in cash (e.g. cash bonus) | Monetary | Fixed money obligation. |
| Investments held in redeemable preference shares / debentures | Monetary | Fixed redemption amount. |
| Inventory | Non-monetary | A physical asset; amount not a fixed sum of money. |
| PPE (land, building, plant) | Non-monetary | Physical asset at historical cost. |
| Intangibles, goodwill | Non-monetary | Not a claim to fixed money. |
| Equity investments (shares held) | Non-monetary | Ownership, not a fixed money claim. |
| Advances paid for goods/services / prepaid expenses | Non-monetary | You will receive goods/services, not money back. |
| Advances received against goods to be supplied | Non-monetary | You will discharge by delivering goods, not money. |
| Share capital, securities premium | Non-monetary | Not a money claim. |

Note the subtle traps in the table: a **prepaid expense** and an **advance to a supplier for goods** are non-monetary (you get value/goods, not money), whereas a **loan** is monetary (you get money back). This exact distinction is a favourite exam trick.

### 4.2 RECOGNITION — the three moments in a foreign-currency transaction's life

Every foreign-currency monetary transaction passes through up to three accounting moments. Master these and you can solve any transaction question.

**(a) Initial recognition (transaction date).** Record the foreign-currency amount in Rupees by applying the **exchange rate at the date of the transaction** (the spot rate) to the foreign amount. For practicality, an **average rate** for a week or month may be used if it doesn't fluctuate significantly. This is where both monetary and non-monetary items get their first Rupee value.

> Steel purchase: €100,000 × ₹90 = ₹90,00,000. Record steel (asset) and creditor (liability) at ₹90,00,000.

**(b) Reporting at each subsequent balance sheet date.** Now the monetary/non-monetary split governs:

- **Monetary items → report at CLOSING rate.** Re-translate the foreign amount using the balance sheet-date rate. The change from the previously recorded Rupee amount is an **exchange difference**.
- **Non-monetary items carried at historical cost → keep at the rate on the transaction date.** Do **not** re-translate. (No exchange difference arises.)
- **Non-monetary items carried at fair value** (e.g. an item revalued) → translate the fair value using the rate that existed **when the fair value was determined**.

> At 31 March: creditor is monetary → re-translate at closing ₹93: €100,000 × ₹93 = ₹93,00,000. Steel is non-monetary → stays at ₹90,00,000.

**(c) Settlement.** When a monetary item is actually received or paid, translate at the **rate on the settlement date**. The difference between this and the amount at which it was last carried is again an **exchange difference**.

> On 5 April, pay at ₹94: €100,000 × ₹94 = ₹94,00,000 handed over, against a creditor carried at ₹93,00,000.

### 4.3 MEASUREMENT — how the exchange differences are computed and where they go

**The general recognition rule for exchange differences:** exchange differences arising on the **settlement** of monetary items **or** on **reporting** an enterprise's monetary items at rates different from those at which they were initially recorded (or reported in previous statements) are recognised as **income or expense in the Profit & Loss account** in the period in which they arise.

Trace Bharat Motors' ₹4,00,000 total swing:
- At 31 Mar (year 1 close): liability rose from ₹90,00,000 to ₹93,00,000 → exchange **loss of ₹3,00,000** to P&L of year 1 (unrealized but recognized).
- At 5 Apr (settlement in year 2): liability rose from ₹93,00,000 to ₹94,00,000 → exchange **loss of ₹1,00,000** to P&L of year 2 (realized).
- Total ₹4,00,000 loss, correctly split across the two periods. The steel remains at ₹90,00,000 throughout. This is the whole logic in one example.

**The important exception — AS 11 does NOT push exchange gains/losses into asset cost.** Under AS 11 (the ICAI standard for non-Ind AS entities), exchange differences on a monetary item that funded an asset are **not** capitalised into that asset; they go to P&L. (This is a key contrast with the older AS 11 pre-2004 "capitalise into fixed asset cost" idea, which was removed.)

**Paragraph 46 / 46A relief (know it exists, and flag it).** Because large rupee depreciation created huge P&L hits on foreign loans, the Government/ICAI provided an *optional* relief through paragraphs 46 and 46A of AS 11 (via the Companies (Accounting Standards) Rules): a company **may** opt to (i) add/deduct exchange differences on **long-term foreign-currency monetary items** relating to acquisition of a **depreciable capital asset** to the **cost of that asset** (and depreciate over its life), and (ii) accumulate other long-term monetary item exchange differences in a "**Foreign Currency Monetary Item Translation Difference Account (FCMITDA)**" and amortise over the life of the item (but not beyond 31 March 2020). This is an *option*, applied consistently. For the exam, state that the default treatment is P&L, and that para 46A permits this alternative for eligible long-term items — **confirm the exact current applicability and cut-off dates in the latest ICAI study material**, as this relief was time-bound.

### 4.4 Forward exchange contracts

A forward contract fixes today the rate at which you will buy/sell foreign currency on a future date. AS 11 splits forwards into two economically different purposes.

**(a) Forward contracts NOT for trading/speculation and not to hedge a firm commitment — i.e. taken to establish the amount of the reporting currency for an existing underlying asset/liability.** Two components:

- **Premium or discount** = difference between the **forward rate** and the **spot rate at inception** (per unit) × foreign amount. This is a *known financing cost/income* and is **amortised as expense or income over the life of the contract**.
- **Exchange difference** on the contract = change in spot rate over reporting periods, applied to the contract amount, taken to **P&L** in the period.
- Any **profit/loss on cancellation or renewal** is recognised in P&L in that period.

> Example: import €100,000, spot ₹90, take a 3-month forward at ₹91.
> Premium = (91 − 90) × 100,000 = ₹1,00,000, amortised over 3 months (≈ ₹33,333/month) to P&L as expense.
> The underlying creditor (monetary) is still re-translated at spot at each balance sheet date, and its exchange difference goes to P&L too — but because the forward exists, the net P&L impact of spot movement on creditor is broadly offset by the opposite spot movement on the forward.

**(b) Forward contracts for trading/speculation, OR to hedge a firm commitment / highly probable forecast transaction.** No underlying recognised item; the contract is a bet or a hedge of something not yet on the books. Here:
- **No premium/discount amortisation.**
- The contract is **marked to market**: gain/loss = foreign amount × (forward rate available at reporting date for the remaining maturity − contract rate). Recognised in **P&L**. (For firm-commitment/forecast hedges, ICAI guidance/AS 30 principles may apply; **for AS 11 exam purposes, speculative forwards are marked to market with gains and losses to P&L, and premium/discount is not separately amortised**.)

### 4.5 Foreign operations — integral vs non-integral

When a parent consolidates or incorporates a foreign branch/subsidiary, it must translate that operation's financial statements into Rupees. AS 11 first asks: **is the operation integral or non-integral?** Indicators of a **non-integral** operation (autonomy) include:

- The operation transacts **mostly in its own local currency**, not the parent's.
- Its day-to-day activities are carried out with **autonomy** from the parent.
- It has its own local **financing**, sales, costs, and accumulates cash locally.
- The parent's cash flows are **insulated** from the operation's day-to-day activities (parent only affected by dividends/net investment).

If these are absent — the operation is a mere conduit, buying/selling on the parent's behalf, financed by the parent, with cash flows directly affecting the parent — it is **integral**.

**Translating an INTEGRAL foreign operation** (treat its items *as if* they were the parent's own foreign-currency transactions):
- **Monetary items** → **closing rate**.
- **Non-monetary items at historical cost** → **transaction-date (historical) rate**.
- **Non-monetary items at fair value** → rate when fair value was determined.
- **Income and expenses** → transaction-date rates (average rate as approximation).
- **Exchange differences** → **P&L**.

**Translating a NON-INTEGRAL foreign operation** (translate the whole entity, preserving its local relationships):
- **All assets and liabilities (monetary AND non-monetary)** → **closing rate**.
- **Income and expense items** → rates at the **dates of transactions** (average rate is a practical approximation).
- The resulting net **exchange difference** → **accumulated in a separate component of equity ("Foreign Currency Translation Reserve", FCTR)**; it is **NOT taken to P&L** while the investment is held.
- On **disposal** of the non-integral operation, the accumulated FCTR relating to it is **transferred to P&L** and recognised as part of the gain/loss on disposal (the deferred amount finally becomes real).

**Change in classification.** If an operation changes from integral to non-integral (or vice versa), apply the new method **prospectively from the date of change**. When it becomes non-integral, exchange differences on non-monetary items *at the date of change* are accumulated in FCTR; when it becomes integral, the translated amounts at the date of change become the new historical-cost carrying amounts (and the FCTR is *not* reversed to P&L until disposal).

Notice the deep logic: for a non-integral operation everything moves at closing rate so that the **local-currency relationships (ratios, structure) are preserved** in Rupee terms, and the parent's exposure — its net investment — is the only thing whose fluctuation is captured, sensibly parked in reserve until realized.

### 4.6 The core journal entries

Import of goods on credit (initial recognition):
```
Purchases / Steel A/c ........ Dr   90,00,000
    To Creditor (foreign) A/c            90,00,000
(€100,000 × ₹90)
```
At balance sheet date — monetary liability re-translated (loss):
```
Foreign Exchange Loss A/c .... Dr    3,00,000
    To Creditor (foreign) A/c            3,00,000
(₹93,00,000 − ₹90,00,000)
```
On settlement (further loss):
```
Creditor (foreign) A/c ....... Dr   93,00,000
Foreign Exchange Loss A/c .... Dr    1,00,000
    To Bank A/c                          94,00,000
```
Exchange gain on a receivable (rate moved in your favour):
```
Debtor (foreign) A/c ......... Dr    XX
    To Foreign Exchange Gain A/c         XX
```
Forward contract premium (amortised expense):
```
Premium on Forward Contract A/c ... Dr   1,00,000
    To Bank / Forward Contract Payable A/c   1,00,000
(then amortise each period:)
P&L A/c ... Dr    33,333
    To Premium on Forward Contract A/c   33,333
```
Non-integral operation — translation difference to reserve:
```
Foreign Currency Translation Reserve A/c ... Dr / Cr  XX
    (balancing figure after translating assets & liabilities
     at closing rate and P&L at average rate)
```

## 5. Worked Examples

### Example 1 (easy) — Import, year-end, settlement across two years

Sundar Ltd (reporting currency ₹) imports machinery components (inventory) worth **USD 50,000** on **1 Feb 2025** on credit. Rates: 1 Feb ₹82; 31 Mar 2025 (year-end) ₹84; settlement 15 May 2025 ₹83.5.

**Step 1 — Initial recognition (1 Feb, spot ₹82).**
Inventory and creditor = 50,000 × 82 = **₹41,00,000**.

**Step 2 — Classify.** Inventory = **non-monetary** (stays at ₹41,00,000, never re-translated for exchange). Creditor = **monetary** (re-translate at closing).

**Step 3 — Year-end (31 Mar, closing ₹84).**
Creditor now = 50,000 × 84 = ₹42,00,000. It rose by ₹1,00,000 → **exchange loss ₹1,00,000 to P&L of FY 2024-25.** Inventory stays ₹41,00,000.

**Step 4 — Settlement (15 May, ₹83.5).**
Pay 50,000 × 83.5 = ₹41,75,000 against creditor carried at ₹42,00,000. Difference ₹25,000 in our favour → **exchange gain ₹25,000 to P&L of FY 2025-26.**

**Sanity check:** total actual cost swing = paid ₹41,75,000 vs original ₹41,00,000 = ₹75,000 net loss overall, split as ₹1,00,000 loss (Y1) then ₹25,000 gain (Y2) = ₹75,000 net. Inventory sits at historical ₹41,00,000. Reasoning is internally consistent.

### Example 2 (medium) — Monetary vs non-monetary discrimination + advance

Vega Ltd pays a **non-refundable advance of USD 20,000 on 10 Mar 2025** (rate ₹83) to a US supplier for a machine, and takes delivery on **20 Apr 2025** paying the **balance USD 30,000** (rate ₹85). Year-end 31 Mar 2025 rate ₹84. At what value is the machine recorded, and are there any exchange differences?

**Step 1 — Classify the advance.** An advance for a machine gives a right to **receive a machine, not money** → **non-monetary**. So at year-end 31 Mar it is **NOT re-translated**; it stays at 20,000 × 83 = **₹16,60,000**. No exchange difference on the advance. (This is the classic trap — students wrongly re-translate advances at closing rate.)

**Step 2 — Year-end.** Nothing to re-measure (the advance is non-monetary; no monetary payable exists yet). Exchange difference = **nil** at 31 Mar.

**Step 3 — Delivery 20 Apr.** Balance USD 30,000 paid at ₹85 = ₹25,50,000. Machine cost = advance portion ₹16,60,000 + balance ₹25,50,000 = **₹42,10,000**.

**Key insight:** because the advance was non-monetary and settled by delivery, the machine's cost blends the ₹83 rate (advance) and ₹85 rate (balance). No exchange gain/loss ever hits P&L here — there was never a live monetary exposure that outlived a balance-sheet date. Contrast with a *loan* of USD 20,000, which would be monetary and re-translated at ₹84 at year-end.

### Example 3 (medium-hard) — Forward contract on an existing payable

On **1 Jan 2025**, Orbit Ltd buys raw material from a UK supplier for **GBP 100,000** on 3-month credit. Spot ₹105/£. Same day it enters a **3-month forward to buy GBP 100,000 at ₹107**. Year-end 31 Mar 2025 (contract maturity) spot ₹109. The forward is to cover an existing liability (not speculative).

**Step 1 — Premium/discount at inception.** Forward ₹107 − spot ₹105 = ₹2 per £. Premium = 2 × 100,000 = **₹2,00,000**, to be **amortised over 3 months** (Jan–Mar) as expense. Here the whole 3 months fall in one period, so full ₹2,00,000 hits P&L as premium expense.

**Step 2 — Underlying creditor re-translated at spot at year-end.** Creditor initially 100,000 × 105 = ₹1,05,00,000. At 31 Mar spot ₹109 → 100,000 × 109 = ₹1,09,00,000. Exchange **loss ₹4,00,000** to P&L on the creditor.

**Step 3 — Forward contract exchange difference.** The forward's spot-driven gain: spot moved ₹105 → ₹109 = ₹4 gain per £ on 100,000 = **₹4,00,000 gain** on the forward, to P&L.

**Step 4 — Net effect.** Creditor loss ₹4,00,000 is offset by forward gain ₹4,00,000 → net zero from spot movement, leaving only the **₹2,00,000 premium** as the true cost of certainty. Effective Rupee cost of the material = ₹1,05,00,000 + ₹2,00,000 = **₹1,07,00,000 = 100,000 × ₹107**, exactly the forward rate. The accounting has faithfully reproduced the economics: Orbit locked in ₹107, and that is what it "paid" in substance.

### Example 4 (exam-hard) — Non-integral foreign subsidiary translation

Indus Ltd (₹) owns a **non-integral** US subsidiary. Simplified subsidiary balance sheet (USD) and rates:

| Item | USD | Rate applied | ₹ |
|---|---|---|---|
| Fixed assets | 200,000 | Closing 84 | 1,68,00,000 |
| Inventory | 50,000 | Closing 84 | 42,00,000 |
| Debtors | 40,000 | Closing 84 | 33,60,000 |
| Cash | 10,000 | Closing 84 | 8,40,000 |
| **Total assets** | **300,000** | | **2,52,00,000** |
| Creditors | 60,000 | Closing 84 | 50,40,000 |
| Share capital | 150,000 | Rate on date of investment 78 | 1,17,00,000 |
| Retained earnings | 90,000 | At various/average 80 | 72,00,000 |
| **Total** | **300,000** | | **2,39,40,000** |

**Step 1 — Recognize the method.** Non-integral → translate **all assets and all liabilities at closing rate** (note: even fixed assets and inventory go at closing rate, unlike the integral method). Equity/share capital is carried at the rate on the date of acquisition; retained earnings at the rates when earned (average as approximation).

**Step 2 — Compute the balancing difference.** Assets ₹2,52,00,000 − liabilities (creditors) ₹50,40,000 = net assets in ₹ = **₹2,01,60,000**. Equity translated = share capital ₹1,17,00,000 + retained earnings ₹72,00,000 = ₹1,89,00,000. 

Foreign Currency Translation Reserve (balancing figure) = ₹2,01,60,000 − ₹1,89,00,000 = **₹12,60,000 (credit — a translation gain)**.

**Step 3 — Where it goes.** This ₹12,60,000 is **NOT** routed through P&L. It sits in the **Foreign Currency Translation Reserve** under equity, and stays there until Indus Ltd **disposes** of the subsidiary, at which point it is transferred to P&L as part of the gain/loss on disposal.

**Insight:** because assets and liabilities all move at closing rate, the subsidiary's internal structure (its ratios) is preserved in Rupee terms; the only "new" number is the translation reserve, which captures the change in Indus Ltd's net investment — precisely the exposure the parent actually bears.

## 6. Presentation & Disclosure formats

**In the Profit & Loss statement:** net exchange differences taken to P&L are typically shown within *other income* (net gain) or under *other expenses* (net loss). Under Schedule III, they appear grouped and disclosed by note.

**In the Balance Sheet / equity:** the **Foreign Currency Translation Reserve** (for non-integral operations) is shown as a **separate component of Reserves and Surplus** (Other Equity). Any **FCMITDA** balance (if para 46A option used) is shown separately and amortised.

**Mandatory disclosures under AS 11:**
1. The **amount of exchange differences included in net profit or loss** for the period.
2. **Net exchange differences accumulated in the foreign currency translation reserve** as a separate component of equity, and a **reconciliation** of its opening and closing amount.
3. When the **reporting currency differs** from the currency of the country of domicile, the **reason**, and the reason for **any change** in reporting currency.
4. When there is a **change in classification** of a significant foreign operation (integral ↔ non-integral): the **nature of the change, the reason, its impact on shareholders' funds**, and the impact on net profit/loss for each prior period presented had the change occurred at the beginning of the earliest period.
5. (If para 46/46A option adopted) disclosure of the **fact of the option** and the amounts capitalised/held in FCMITDA and amortised.
6. An enterprise is **encouraged** to disclose its **foreign currency risk management policy**.

Illustrative note wording: *"Exchange differences arising on settlement / restatement of foreign currency monetary items are recognised as income or expense in the period in which they arise. During the year, a net exchange loss of ₹X (previous year: gain ₹Y) has been recognised in the Statement of Profit and Loss. The Foreign Currency Translation Reserve moved from ₹A to ₹B, the change of ₹C representing translation of the Company's non-integral foreign operation at the closing rate."*

## 7. Connections

- **AS 2 (Inventories):** inventory is non-monetary, recorded at the transaction-date rate. But AS 2's **lower of cost or NRV** still applies — and if NRV is in foreign currency, translate NRV at closing rate before comparing. AS 11 fixes the cost; AS 2 may still write it down.
- **AS 10 (PPE):** fixed assets are non-monetary, carried at historical-rate cost. Exchange differences do **not** normally enter PPE cost under AS 11 (contrast the optional para 46A capitalisation for long-term monetary items funding depreciable assets).
- **AS 16 (Borrowing Costs):** exchange differences on foreign-currency borrowings are treated as borrowing cost **to the extent they are a regarded as an adjustment to interest cost**; the rest is an AS 11 exchange difference. The two standards must be read together for foreign loans.
- **AS 13 / Investments:** equity investments are non-monetary (historical rate); investments in the nature of fixed-return instruments (redeemable) may be monetary.
- **AS 21 / 23 / 27 (Consolidation):** the integral/non-integral translation feeds directly into consolidated financial statements of subsidiaries, associates and JVs. FCTR arises on consolidation.
- **AS 29 (Provisions):** a foreign-currency provision settled in cash is monetary; re-translate at closing rate.
- **Ind AS 21** (contrast): uses a **functional currency** approach and the concept of items re-measured through OCI; AS 11 uses reporting currency and the integral/non-integral split. Know the difference if the paper contrasts them.
- **Other CA subjects:** *FM/SFM* — forward contracts, currency hedging, interest-rate parity explain *why* the forward premium equals the interest differential; *Taxation* — Section 43A of the Income-tax Act deals with exchange differences on assets acquired from abroad, and can differ from AS 11 treatment (a reconciling item); *Audit* — verifying year-end translation and disclosure.

## 8. Traps & Examiner Tricks

1. **Re-translating non-monetary items.** The number one error: re-translating inventory, PPE, advances, or prepaid expenses at closing rate. They stay at historical rate. Always classify *first*.
2. **Advance paid/received treated as monetary.** An advance to a supplier for goods, or an advance received against goods to be supplied, is **non-monetary** (settled by goods, not money). Examiners love slipping this in beside a genuine payable.
3. **Forgetting the year-end restatement for monetary items.** Some students only book the difference at settlement. AS 11 requires recognition at **each** balance sheet date too — the unrealized difference goes to P&L now, not deferred to payment.
4. **Sending non-integral translation differences to P&L.** They go to the **FCTR in equity**, not P&L — until disposal. Conversely, sending integral operation differences to reserve is wrong; those go to P&L.
5. **Premium vs exchange difference on forwards.** Premium/discount = (forward − spot at inception), **amortised over the contract life**. The exchange difference = movement in **spot**, to P&L. Mixing these up, or amortising a speculative forward's premium, loses marks.
6. **Speculative vs hedging forward.** A speculative forward (or one hedging a firm commitment) is **marked to market** with no premium amortisation. A forward covering an existing recognised asset/liability uses the premium-amortisation method. Read the question to see which.
7. **Using the wrong rate for the underlying.** Initial recognition uses **transaction-date spot**, not the forward rate; the forward is accounted separately.
8. **Fair-valued non-monetary items.** If an item is carried at fair value, translate the fair value at the rate on the date **the fair value was determined**, not the original transaction date and not closing rate.
9. **Integral vs non-integral misclassification.** Watch the indicators: local financing + local currency sales/costs + autonomy = non-integral; a dependent conduit financed by the parent = integral. The classification changes *every* translated number.
10. **Disposal of non-integral operation.** On disposal, the accumulated FCTR is recycled to P&L. Forgetting this understates the disposal gain/loss.
11. **Para 46A time limits.** If the question invokes the capitalisation option, remember it is optional, for long-term items, and time-bound — do not apply it as the default. **Confirm current applicability in ICAI material.**

## 9. First-Principles Recap

- A balance sheet must be in one currency, so foreign amounts must be **translated** — the rate you use depends on what kind of item it is.
- **Monetary = live money claims (water)** → re-measure at **current/closing rate** because their real Rupee value truly changes. **Non-monetary = settled historical costs (ice)** → keep at **historical rate** because a rate change doesn't alter what you paid.
- A foreign transaction has up to **three moments**: initial (transaction rate), each balance-sheet date (closing rate for monetary), settlement (settlement rate).
- **Exchange differences on monetary items → P&L, in the period they arise** — both unrealized (year-end) and realized (settlement), because the economic change is real *now*.
- Non-monetary items generate **no** exchange difference (unless carried at fair value, then use the fair-value-date rate).
- A **forward contract** splits into an amortised **premium/discount** (known cost of certainty) and a **spot-driven exchange difference** (to P&L); speculative/firm-commitment forwards are **marked to market**.
- **Integral** foreign operation = extension of the parent → translate with the parent's monetary/non-monetary rules, differences to **P&L**.
- **Non-integral** foreign operation = autonomous business → translate **everything at closing rate**, differences to **FCTR in equity**, recycled to P&L only on **disposal** — because the parent's real exposure is just its **net investment**.
- Classification (monetary/non-monetary; integral/non-integral) is the decision that drives every number — do it *before* touching a calculator.

## 10. Quick-Revision Sheet

**Translation rates:**

| Situation | Rate |
|---|---|
| Initial recognition (any item) | Transaction-date spot (avg allowed) |
| Monetary item at B/S date | **Closing rate** |
| Monetary item on settlement | Settlement-date rate |
| Non-monetary at historical cost | **Historical (transaction) rate — no re-translation** |
| Non-monetary at fair value | Rate on date fair value determined |
| Integral operation | As parent (monetary→closing, non-monetary→historical); diff → **P&L** |
| Non-integral operation | **All A & L → closing**; income/exp → avg; diff → **FCTR (equity)** |

**Where the difference goes:** Monetary items & integral ops → **P&L**. Non-integral ops → **FCTR (equity)**, recycled to **P&L on disposal**.

**Monetary (re-translate):** cash, bank, debtors, creditors, loans, deposits, redeemable investments, cash-settled provisions.
**Non-monetary (freeze):** inventory, PPE, intangibles, goodwill, equity investments, prepaid expenses, advances for goods (paid or received), share capital.

**Forward contract (hedge of recognised item):**
- Premium/discount = (forward rate − spot at inception) × amount → **amortise over contract life**.
- Exchange diff = change in **spot** × amount → **P&L**.
- Cancellation/renewal profit/loss → **P&L**.
**Forward (speculative / firm-commitment hedge):** mark to market → **P&L**; no premium amortisation.

**Key journal (monetary loss at year-end):**
```
Forex Loss A/c ... Dr    (closing − recorded)
    To Creditor A/c
```

**Core disclosures:** exchange diff in P&L; FCTR reconciliation (opening→closing); reason if reporting currency ≠ domicile currency; nature/reason/impact of change in integral↔non-integral classification.

**Flag to confirm in ICAI material:** para 46/46A optional capitalisation of exchange differences on long-term foreign-currency monetary items (into depreciable asset cost / FCMITDA) — optional, time-bound; verify current applicability and cut-off.
