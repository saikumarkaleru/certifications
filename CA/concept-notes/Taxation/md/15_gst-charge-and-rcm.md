# Chapter 15 — Charge of GST (Levy & Reverse Charge)

> *Flag: All rates, thresholds, notified RCM lists and composition ceilings below reflect the CGST Act 2017 and IGST Act 2017 as commonly examined. Rates and notifications (especially RCM notifications 4/2017-CT(R), 13/2017-CT(R), 7/2019-CT(R) and the composition rates in Sec 10) are amended frequently. Always re-verify the exact figures, the notified lists, and the applicable date against current ICAI study material for your attempt.*

---

## 1. The Problem

You now know (from the earlier chapters) *what* a supply is, *where* it is taxable, and *when* it is taxable. But knowing that a transaction is a taxable supply is useless until the law answers three brutally practical questions:

1. **On what authority is the tax even charged?** A tax on citizens cannot exist by administrative wish. Article 265 of the Constitution says plainly: *"No tax shall be levied or collected except by authority of law."* So somewhere there must be a single **charging section** — the legal switch that turns "this is a supply" into "therefore ₹X of tax is payable." Without it, the entire GST apparatus is unconstitutional.

2. **Who actually hands the money to the government?** The natural answer is "the seller collects GST from the buyer and deposits it." That works beautifully — *when the seller is a registered, traceable, well-behaved business.* But GST's tax base deliberately reaches into corners where the supplier is a small unregistered farmer, an individual advocate, a goods-transport operator with one truck, or a company sitting *outside India* altogether. If the law insisted "only the supplier pays," those supplies would either escape tax entirely or be impossible to enforce. The department would be chasing thousands of tiny, invisible, or foreign suppliers. **How do you tax a supply when the supplier is unregistered, hard to trace, or beyond your jurisdiction?**

3. **What about the corner shop?** GST's compliance machinery — invoice-level returns, input tax credit matching, monthly filings — is built for organised business. Impose that full machinery on a ₹40-lakh-turnover kirana store or a small dhaba and you crush it under paperwork it cannot handle, while collecting a trivial amount of tax. **How do you keep small dealers inside the tax net without destroying them with compliance?**

This chapter is the answer to all three. The charging section (Sec 9 / Sec 5) answers the first. The **reverse charge mechanism** answers the second. The **composition levy** answers the third. Every rule below is a solution — read it as one.

---

## 2. The Core Idea

Strip away the detail and GST's charge stands on three pillars:

> **One levy, collected in whichever way is easiest to enforce, with a simplified lane for the small.**

- **The levy itself** is a single tax on the *value of supply*, at the notified rate. That is Sec 9 of the CGST Act (for intra-State supply) and Sec 5 of the IGST Act (for inter-State supply). This is the constitutional switch.

- **The default collection route is Forward Charge**: the *supplier* collects GST from the recipient and pays it to the government. This is how ~95% of GST flows.

- **Where forward charge would fail, the law flips the burden — Reverse Charge**: the *recipient* pays the GST directly to the government, on the supplier's behalf. Same tax, same rate — only the *person liable to pay* changes. It is not a new tax; it is a change of collection agent, chosen precisely because the recipient (a large, registered, traceable business) is far easier to hold accountable than the supplier.

- **For small dealers, the law offers Composition Levy (Sec 10)**: pay a tiny flat percentage of turnover, file quarterly, forget invoice-level tax and input credit. It trades away ITC and inter-State sales in exchange for near-zero compliance.

Hold this one sentence: **the tax never changes; only *who pays* and *how much paperwork* changes, and each variation is chosen to make collection actually work.**

---

## 3. Why It's Built This Way

**Why a separate charging section at all?** Because a modern tax statute separates *definitional* provisions (what is a supply, what is value, what is the rate) from the *operative* provision that says "tax **shall be levied**." The word "levy" is the legal trigger. Courts read the charging section strictly: if a transaction does not fall squarely inside it, no tax can be demanded, however much the department wishes otherwise. So GST needed one clean sentence to charge the tax — and it lives in Sec 9(1)/5(1).

**Why split CGST and IGST?** India is a federation. The Constitution (101st Amendment, Article 246A + Article 269A) lets *both* the Centre and the States tax the same supply — but neither may tax across the country. So:
- An **intra-State** supply (within one State) is taxed *twice over the same base*: **CGST** to the Centre + **SGST** to the State, each at half the rate. Sec 9 of the CGST Act charges the CGST half; a parallel SGST Act charges the other.
- An **inter-State** supply is taxed by a single **IGST** (Centre collects, then apportions the State's share). Sec 5 of the IGST Act charges it. IGST rate = CGST + SGST rate, so the total is identical whichever way the goods move — that neutrality is the whole point of "one nation, one tax."

**Why reverse charge?** Follow the anti-cascade logic. GST wants to tax value addition *everywhere*, including services bought from people outside the organised net. But you cannot register and audit every roadside transporter or every foreign software vendor. So the law makes the *recipient* — who is registered, keeps books, and files returns — pay the tax and (usually) claim it back as ITC. The government's money is secured from a party it can actually reach. Reverse charge is enforcement pragmatism, not extra taxation.

**Why composition?** The genius of GST — invoice matching and seamless ITC — is also its burden. A tiny dealer selling to final consumers gains almost nothing from ITC (his customers can't use it either) but would drown in monthly returns. Composition says: give up ITC and inter-State ambitions, pay a token flat rate on turnover, file once a quarter. The State loses little revenue (these are small players) and gains compliance from businesses that would otherwise stay informal. It is a deliberate, rational trade.

---

## 4. Full Technical Content

### 4.1 The Charging Section — Sec 9 CGST Act / Sec 5 IGST Act

**Sec 9(1), CGST Act — the core levy:**

> *"There shall be levied a tax called the central goods and services tax on all intra-State supplies of goods or services or both, except on the supply of alcoholic liquor for human consumption, on the value determined under section 15 and at such rates, not exceeding 20%, as may be notified by the Government on the recommendations of the Council, and collected in such manner as may be prescribed, and shall be paid by the taxable person."*

Unpack every clause — each is load-bearing:

| Clause | What it means | Why it matters |
|---|---|---|
| "shall be levied a tax called CGST" | The constitutional switch is thrown | Without this, no CGST can be demanded |
| "on all intra-State supplies of goods or services or both" | Scope = supplies within a State | Inter-State supplies go to Sec 5 IGST instead |
| "except alcoholic liquor for human consumption" | Alcohol is *constitutionally* outside GST | States still levy State Excise/VAT on it |
| "on the value determined under section 15" | Base = transaction value (Sec 15) | Links charge to valuation rules |
| "rates not exceeding 20%" | Statutory ceiling per Act | So CGST + SGST caps at 40%; actual rates (0/5/12/18/28) are *notified*, not in the Act |
| "shall be paid by the taxable person" | Default liability = supplier | This is **forward charge** |

**The five special sub-sections of Sec 9** (these are examiner favourites):

- **Sec 9(1) proviso — Petroleum products:** GST on petroleum crude, high-speed diesel, petrol (motor spirit), natural gas and aviation turbine fuel shall be levied **with effect from a date notified** by the Government on the Council's recommendation. Translation: these five are *within* GST constitutionally but **not yet notified**, so currently they bear the old regime (Central Excise + State VAT). Alcohol (above) is *permanently* out; petroleum is *temporarily* out.

- **Sec 9(2):** covers the petroleum-product deferral mechanism (levy from notified date).

- **Sec 9(3) — Reverse charge on notified supplies:** the Government may notify categories of goods/services where **tax is paid by the recipient** on reverse charge. (See 4.3.)

- **Sec 9(4) — Reverse charge on supplies from unregistered persons:** where a *registered* person receives supplies from an *unregistered* supplier, tax may be paid by the recipient on reverse charge, for **notified classes of registered persons** and notified supplies. (Currently narrow — see 4.3.)

- **Sec 9(5) — Electronic Commerce Operator (ECO):** for **notified services** (e.g. passenger transport by cab aggregators, accommodation by unregistered hotels, restaurant services through the ECO), the **e-commerce operator** (Ola, Uber, Zomato, etc.) is made liable to pay GST *as if it were the supplier*. Rationale: the platform is the single traceable choke-point; taxing thousands of individual drivers/restaurants is impractical.

**Sec 5, IGST Act** mirrors Sec 9 word-for-word for **inter-State** supplies and **imports**, with two extra points: the rate ceiling is **40%** (since IGST = CGST + SGST), and IGST is also the tax on **import of goods** (collected as a customs duty under the Customs Tariff Act) and **import of services**.

### 4.2 Forward Charge (the default)

Under forward charge the **supplier**:
1. adds GST to the invoice value,
2. **collects** it from the recipient,
3. **deposits** it with the government (after netting his own input tax credit), and
4. files returns reporting it.

The recipient simply pays the tax-inclusive invoice and claims the GST as ITC (if eligible). This is the ordinary flow for almost all registered-supplier transactions.

### 4.3 Reverse Charge Mechanism (RCM) — Sec 2(98), Sec 9(3)/(4)/(5)

**Definition — Sec 2(98):** *"reverse charge"* means the liability to pay tax by the **recipient** of supply of goods or services (or both) instead of the supplier, under Sec 9(3)/(4) of CGST or Sec 5(3)/(4) of IGST.

**Key operating rules of RCM — memorise the logic, not a list:**

1. **The recipient pays in cash, not from ITC.** RCM liability must be discharged through the **electronic cash ledger**; you cannot use input tax credit to *pay* an RCM liability. (You first pay it in cash; *then* you may claim that same amount back as ITC if the inward supply is used for business — subject to eligibility.) Reason: the government wants the actual cash secured.

2. **Compulsory registration — Sec 24(iii).** A person *required to pay tax under reverse charge* must register **regardless of turnover** — the ₹20 lakh/₹40 lakh threshold does *not* protect him. Reason: RCM only works if the recipient is in the tax net.

3. **Self-invoicing — Sec 31(3)(f).** When a registered recipient buys from an *unregistered* supplier under RCM, the **recipient must issue an invoice to himself** (and a payment voucher). Reason: the unregistered supplier issues no tax invoice, so a document must exist to support the tax and the ITC.

4. **Composition dealers are hit hard by RCM.** A composition dealer pays his flat composition rate on outward supplies *and* must additionally pay RCM (at the *normal* rate) on notified inward supplies — with **no ITC** available to him. RCM is one of the real costs of being in composition.

5. **Time of supply is different under RCM** (covered in the Time of Supply chapter): for goods, the *earliest* of date of receipt of goods / date of payment / 30 days from invoice; for services, earliest of date of payment / 60 days from invoice.

**Sec 9(3) — Notified goods under RCM (illustrative, verify current list):**

| Supply of goods | Supplier | Recipient who pays RCM |
|---|---|---|
| Cashew nuts (not shelled/peeled) | Agriculturist | Any registered person |
| Tobacco leaves | Agriculturist | Any registered person |
| Silk yarn | Manufacturer of silk yarn from cocoons | Any registered person |
| Raw cotton | Agriculturist | Any registered person |
| Lottery | State Govt / UT / local authority | Lottery distributor/selling agent |

**Sec 9(3) — Notified services under RCM (the exam heavyweight — Notification 13/2017; illustrative):**

| Service | Supplier | Recipient liable under RCM |
|---|---|---|
| **Goods Transport Agency (GTA)** consignment (where GTA has *not* opted 12% forward charge) | GTA | Specified recipients — factory, registered society, co-op, **any registered person**, body corporate, partnership firm, casual taxable person |
| **Legal services** by advocate / firm of advocates | Individual advocate / senior advocate / firm | **Any business entity** located in taxable territory |
| Services by an **arbitral tribunal** | Arbitral tribunal | Any business entity |
| **Sponsorship** services | Any person | Body corporate or partnership firm |
| Services by **Government / local authority** (excluding some, e.g. renting of immovable property to unregistered person, postal, aircraft/vessel, transport of goods/passengers) | Central/State Govt, local authority | Any business entity |
| Services by a **director** of a company to the company (in personal, not employee, capacity) | Director | The company / body corporate |
| Services by an **insurance agent** | Insurance agent | Insurance company |
| Services by a **recovery agent** | Recovery agent | Bank / NBFC / financial institution |
| **Renting of a motor vehicle** (passenger, where fuel cost included, to a body corporate, supplier not charging 12%) | Any person other than body corporate | Body corporate |
| Import of service | Person located outside India | Recipient (importer) in India |

*Memory hook — think "the recipient is always the bigger, traceable, registered party." GTA → the business shipping goods; advocate → the business client; director → the company; import → the Indian importer. The State collects from the party it can actually audit.*

**Sec 9(4) — Supplies from unregistered suppliers:** Originally sweeping (any purchase from an unregistered person triggered RCM), it was suspended and then **restricted to notified classes** to avoid crushing every business. Currently the principal live case is the **real-estate promoter**: a builder must pay RCM on shortfall purchases of inputs/input services from unregistered suppliers below the 80% procurement threshold, and on cement bought from unregistered persons. *Verify the current notified list for your attempt.*

**Sec 9(5) — E-Commerce Operator liability:** For notified services the **ECO pays GST as if it were the supplier**: (i) passenger transport by radio-taxi/motor-cab/motorcycle/omnibus (Ola, Uber), (ii) accommodation in hotels/clubs where the *actual supplier is unregistered* (via Oyo, etc.), (iii) house-keeping (plumbing, carpentry) where actual supplier is unregistered, (iv) **restaurant service** supplied through the platform (Zomato, Swiggy) other than by restaurants in specified premises. If the ECO has no physical presence in the taxable territory, its **representative** (or an appointed person) is liable.

```mermaid
flowchart TD
    A["A taxable supply has occurred"] --> B{"Is it a supply notified under Sec 9 3 or Sec 5 3"}
    B -->|Yes| R["RECIPIENT pays GST in cash under RCM"]
    B -->|No| C{"Is it a Sec 9 5 notified service through an e-commerce operator"}
    C -->|Yes| E["E-COMMERCE OPERATOR pays GST as if supplier"]
    C -->|No| D{"Registered recipient buying from unregistered supplier in a Sec 9 4 notified class"}
    D -->|Yes| R
    D -->|No| F["SUPPLIER pays GST under FORWARD CHARGE"]
```
*Figure 15.1 — The charge decision tree: who is liable to pay the GST on a given supply.*

### 4.4 Composition Levy — Sec 10, CGST Act

**What it is:** an *optional* scheme letting a small registered person pay tax at a **flat low percentage of turnover** instead of the normal rate on value, with **no input tax credit** and drastically reduced compliance (quarterly payment via **CMP-08**, annual return **GSTR-4**).

**Sec 10(1)/(2) — Composition for goods (and restaurant service):**

- **Eligibility threshold:** aggregate turnover in the **preceding** financial year up to **₹1.5 crore** (₹75 lakh for specified **Special Category States** — e.g. the North-Eastern States, Himachal, etc.). *Verify the current figure and State list.*
- **Rates (of turnover in State/UT):**

| Category of registered person | CGST | SGST | Total |
|---|---|---|---|
| **Manufacturers** (other than notified goods e.g. ice-cream, pan masala, tobacco, aerated water) | 0.5% | 0.5% | **1%** |
| **Traders / other suppliers of goods** | 0.5% | 0.5% | **1%** (of turnover of *taxable* supplies) |
| **Restaurants** (supply of food/drink, not serving alcohol) | 2.5% | 2.5% | **5%** |

*Note: for a trader, the 1% is on turnover of **taxable** supplies of goods and services in the State; for a manufacturer/restaurant it is on total turnover in the State.*

**Sec 10(2A) — Composition for service providers (and mixed suppliers):**
- A **separate scheme** for suppliers of *services* (or mixed goods+services) who could not use 10(1) because they supply services beyond the small permitted limit.
- **Threshold:** aggregate turnover in the preceding FY up to **₹50 lakh**.
- **Rate:** **6%** (3% CGST + 3% SGST) of turnover.

**The permitted-services sweetener in 10(1):** a *goods* composition dealer may *also* supply services up to the higher of **₹5 lakh** or **10% of turnover** in the preceding year, without losing 10(1) eligibility. Reason: a small trader who also does a little repair/installation work shouldn't be thrown out of the scheme.

**Sec 10(2) — Conditions (WHO can opt) — every one is a design choice:**

| Condition | Why it exists |
|---|---|
| **No inter-State outward supplies** | Composition is intra-State by design; inter-State means IGST + full compliance |
| **No supply through an e-commerce operator** that collects TCS | ECO sales imply organised, often inter-State trade — inconsistent with the simple scheme |
| **Not a supplier of goods/services *not leviable* to GST** (e.g. alcohol dealer) | Can't compound tax on things outside GST |
| **Not a manufacturer of notified goods** (ice-cream, pan masala, tobacco, aerated water, fly-ash bricks etc.) | High-value/sin goods excluded to protect revenue |
| **Not a casual taxable person or non-resident taxable person** | These are transient — the scheme assumes an ongoing small business |
| **All registrations under the same PAN must opt together** | Prevents splitting a big business into "small" pieces to abuse the scheme |
| **Cannot collect tax from customers** and **cannot claim ITC** | It's a *turnover* tax, not a value-added tax — this is the core trade-off |
| **Must pay RCM at normal rates** on notified inward supplies | The RCM logic (4.3) overrides the composition simplicity |
| **Must issue a *Bill of Supply*, not a tax invoice**, stating *"composition taxable person, not eligible to collect tax on supplies"* | Warns the buyer that no ITC flows from this purchase |
| **Must display "composition taxable person"** on notice boards and signboards | Transparency to customers and department |

**Sec 10(3)/(5) — Exit and penalty:** the option **lapses automatically** the day turnover crosses the ceiling during the year (from then he becomes a normal taxpayer). If a person opts wrongly (was ineligible) or breaches conditions, he pays **tax at normal rates** on the tainted supplies plus a **penalty** (Sec 10(5) → treated like Sec 73/74 demand).

```mermaid
flowchart TD
    A["Registered person considering composition"] --> B{"Preceding-year aggregate turnover within ceiling 1.5cr goods or 50L services"}
    B -->|No| X["Not eligible - pay normal GST with ITC"]
    B -->|Yes| C{"Makes any inter-State outward supply or supplies through TCS e-commerce operator"}
    C -->|Yes| X
    C -->|No| D{"Deals in non-leviable goods like alcohol or is a notified excluded manufacturer"}
    D -->|Yes| X
    D -->|No| E["ELIGIBLE - pay flat rate on turnover no ITC no tax collection quarterly CMP-08"]
```
*Figure 15.2 — Composition eligibility gate under Sec 10: turnover, then the disqualifiers.*

---

## 5. Worked Examples

### Example 1 — Forward charge vs the value base (Sec 9 + Sec 15)

**Facts:** Radhika Traders (Maharashtra, registered) sells goods to a customer in Maharashtra for a taxable value of ₹1,00,000. Applicable GST rate = 18%.

**Solution:**
- This is an **intra-State** supply → CGST (Sec 9) + SGST apply, each at half of 18% = **9%**.
- CGST = 9% × ₹1,00,000 = **₹9,000**
- SGST = 9% × ₹1,00,000 = **₹9,000**
- Invoice value = ₹1,00,000 + ₹9,000 + ₹9,000 = **₹1,18,000**
- Radhika (the supplier) **collects ₹18,000** from the customer and deposits it (net of her own ITC). This is forward charge — the default under Sec 9(1).

*Reconciliation:* If instead the customer were in Gujarat (inter-State), the same 18% would be a single **IGST of ₹18,000** under Sec 5 IGST — identical total, only the split changes. Tax neutrality across State lines. Verified.

### Example 2 — Reverse charge on legal + GTA services

**Facts:** Vega Industries Pvt Ltd (registered, Karnataka) incurs the following in a month:
- (a) Legal fees of ₹2,00,000 to an individual advocate (intra-State). GST rate 18%.
- (b) Freight of ₹50,000 to a Goods Transport Agency that has **not** opted for 12% forward charge (intra-State). RCM rate on GTA = 5%.
- (c) Purchase of stationery ₹40,000 from a *registered* dealer, GST 18% (forward charge).

**Which supplies are RCM, and what does Vega pay?**

**Solution:**

| Item | Charge type | Reason | GST computation | Who pays |
|---|---|---|---|---|
| (a) Legal fees | **RCM** | Sec 9(3) — advocate to business entity | 18% × ₹2,00,000 = ₹36,000 → CGST ₹18,000 + SGST ₹18,000 | **Vega**, in cash |
| (b) GTA freight | **RCM** | Sec 9(3) — GTA not on 12% forward charge, recipient is registered | 5% × ₹50,000 = ₹2,500 → CGST ₹1,250 + SGST ₹1,250 | **Vega**, in cash |
| (c) Stationery | Forward charge | Registered supplier, no notification | 18% × ₹40,000 = ₹7,200 | The dealer collects it |

**RCM cash liability for Vega = ₹36,000 + ₹2,500 = ₹38,500** (CGST ₹19,250 + SGST ₹19,250), paid through the **electronic cash ledger** — *not* set off against ITC.

**Then** Vega may claim **₹38,500 as input tax credit** (both are business inputs and eligible), so the *net* economic cost of RCM is nil — but the **cash must move first**. For the stationery, Vega pays the dealer ₹47,200 and claims ₹7,200 ITC normally.

*Reconciliation:* Note the advocate and the small GTA never touch the tax — the government secured ₹38,500 from Vega, a large auditable company, exactly as RCM intends. Also note: even if Vega were below the registration threshold, receiving these RCM supplies would force registration under Sec 24(iii). Verified.

### Example 3 — Composition levy, trader (Sec 10(1))

**Facts:** Kirti Stores, a **trader** in Rajasthan (not a special-category State), opted for composition. Turnover for the year:
- Taxable supplies of goods within Rajasthan: ₹80,00,000
- Exempt supplies of goods: ₹10,00,000
- Interest earned on a fixed deposit: ₹5,00,000
- Also received GTA freight service under RCM: freight ₹1,00,000 (RCM rate 5%)

Preceding-year turnover was ₹1.2 crore (within ₹1.5 crore). Compute total GST payable.

**Solution:**

*Step 1 — Composition tax on outward supplies.* For a **trader**, the rate is **1% of the turnover of *taxable* supplies of goods** in the State (exempt supplies are **excluded** for a trader; interest on FD is an *exempt service*, also excluded).
- Taxable turnover = ₹80,00,000
- Composition tax = 1% × ₹80,00,000 = **₹80,000** → CGST ₹40,000 + SGST ₹40,000

*Step 2 — RCM on inward GTA (Sec 9(3) overrides composition simplicity).* Composition dealers still pay RCM at **normal** rates.
- RCM = 5% × ₹1,00,000 = **₹5,000** → CGST ₹2,500 + SGST ₹2,500, paid in **cash**, **no ITC** available to a composition dealer.

*Step 3 — Total GST payable by Kirti Stores* = ₹80,000 (composition) + ₹5,000 (RCM) = **₹85,000**.

*Reconciliation:* Kirti collects **no** tax from customers (issues a Bill of Supply), claims **no** ITC, and the FD interest and exempt goods correctly drop out of a *trader's* 1% base. If Kirti had been a **manufacturer**, the 1% would apply to **total** turnover in the State (₹90,00,000 of goods, still excluding pure exempt-service interest), i.e. ₹90,000 — illustrating why "trader vs manufacturer" changes the base. Verified.

### Example 4 — Composition for a service provider (Sec 10(2A)) + turnover breach

**Facts:** Nitin runs a small event-management **service** business in Kerala. Preceding-year turnover ₹42 lakh, so he opted for the **6% service composition** (Sec 10(2A)) on 1 April. During the year his turnover reaches ₹50,00,000 on 15 December and rises to ₹58,00,000 by 31 March.

**Solution:**
- Nitin is eligible on 1 April (₹42 lakh < ₹50 lakh preceding-year ceiling).
- On the **turnover of ₹50,00,000** earned *up to the day he crosses the ceiling*, composition applies at **6%** → 6% × ₹50,00,000 = **₹3,00,000** (CGST ₹1,50,000 + SGST ₹1,50,000).
- **Sec 10(3):** the moment turnover **exceeds ₹50 lakh** (on 15 December), the composition option **lapses**. From that point Nitin becomes a **normal taxpayer**: on the further ₹8,00,000 he charges GST at the **normal rate** (say 18%) *and* can claim ITC on inputs from that date. Normal-rate GST = 18% × ₹8,00,000 = **₹1,44,000** (before ITC).

*Reconciliation:* The scheme protected him only while genuinely small; growth automatically ejected him — no revenue leakage. He must also file the intimation of withdrawal and shift to normal returns. Verified.

---

## 6. Format / Summary

**Charge-of-GST reference card:**

| Question | Provision | Answer |
|---|---|---|
| Legal authority to charge | Sec 9(1) CGST / Sec 5(1) IGST | Levy on value (Sec 15) at notified rate |
| Intra-State supply | Sec 9 CGST + SGST Act | CGST + SGST, half rate each |
| Inter-State supply / imports | Sec 5 IGST | Single IGST = CGST + SGST rate |
| Outside GST permanently | — | Alcoholic liquor for human consumption |
| Outside GST till notified | Sec 9(2) proviso | 5 petroleum products |
| Default payer | Sec 9(1) | Supplier (forward charge) |
| Recipient pays | Sec 9(3)/(4), 5(3)/(4) | Notified goods/services; unregistered supplier (notified) |
| Platform pays | Sec 9(5) | E-commerce operator on notified services |
| Small-dealer scheme | Sec 10(1) / 10(2A) | 1% / 5% / 6% flat on turnover, no ITC |

**RCM discharge rule (one line):** *Pay in cash first (no ITC to pay it), self-invoice if supplier unregistered, register compulsorily under Sec 24 — then claim ITC if eligible.*

**Composition trade-off (one line):** *Give up ITC, tax-collection, and inter-State sales; gain a flat low rate and quarterly filing.*

---

## 7. Connections

- **Supply (Sec 7) & Schedule I/II/III:** the charge only bites on a "supply." No supply → no levy, however the money moves.
- **Value of Supply (Sec 15):** the charging section pins the tax to the Sec 15 value — the two are read together.
- **Place of Supply (IGST Act):** decides intra vs inter-State, i.e. *which* charging section (Sec 9 vs Sec 5) fires.
- **Time of Supply (Sec 12/13):** RCM has its **own** time-of-supply rules — the "pay in cash" duty crystallises there.
- **Registration (Sec 22–24):** Sec 24(iii) forces RCM recipients to register with no threshold; composition needs registration under Sec 10.
- **Input Tax Credit (Sec 16–17):** forward charge feeds the ITC chain; RCM tax is claimable as ITC; composition dealers get **zero** ITC — the scheme's price.
- **Exemptions:** an exempt supply is *within* the charging section but relieved by notification; distinguish from alcohol/petroleum which are *outside* the charge.

---

## 8. Traps & Examiner Tricks

1. **"RCM can be paid using ITC."** *False.* RCM must be paid in **cash** via the electronic cash ledger; ITC can be *claimed afterwards* but never *used to pay* the RCM itself.
2. **Threshold exemption saves an RCM recipient.** *No.* Sec 24(iii): anyone liable under RCM must register **regardless of turnover**.
3. **Alcohol vs petroleum confusion.** Alcohol for human consumption is **permanently outside** GST (constitutionally); the five petroleum products are **inside but not yet notified**. Don't swap them.
4. **Composition dealer collects GST / issues a tax invoice.** *Never.* He issues a **Bill of Supply**, collects **no** tax, and shows the "composition taxable person" declaration.
5. **Applying 1% to a trader's total (incl. exempt) turnover.** For a **trader**, the 1% is on **taxable** supplies only; for a **manufacturer/restaurant** it's on **total** turnover in the State. Examiners plant exempt supplies and FD interest to test this.
6. **Composition ceiling mix-up.** ₹1.5 crore (goods, Sec 10(1)) vs ₹50 lakh (services, Sec 10(2A)) vs ₹75 lakh (special-category States). And the *permitted extra services* limit in 10(1) is higher of ₹5 lakh or 10% of turnover.
7. **Composition + inter-State sale.** A single inter-State **outward** supply disqualifies composition. (Inter-State *inward* purchases are fine.)
8. **Forgetting RCM on a composition dealer.** He still pays RCM at **normal** rates on notified inward supplies, with no ITC — a common missed line in computations.
9. **GTA trap.** RCM applies only where the GTA has **not** opted for the 12% forward-charge rate. If the GTA charges 12% forward, the recipient does **not** pay RCM.
10. **Sec 9(5) ECO vs Sec 9(3).** Under 9(5) the ECO pays as *deemed supplier* (e.g. Uber, Zomato); don't confuse with ordinary TCS by e-commerce operators under Sec 52.

---

## 9. First-Principles Recap

Start from Article 265: no tax without law. GST therefore needs a single sentence that *levies* the tax — Sec 9 (CGST, intra-State) and Sec 5 (IGST, inter-State), each charging tax on the Sec 15 value at a notified rate, capped by statute. Because India is a federation, an intra-State supply is split into CGST + SGST while an inter-State supply bears one IGST — engineered so the total is identical either way (one nation, one tax).

The **default** is that the supplier collects and pays (forward charge). But the tax base deliberately includes suppliers the department cannot easily reach — the unregistered, the tiny, the foreign, the platform-based. For those, forcing the supplier to pay would mean the tax escapes. So the law **flips the collection agent to the recipient** (reverse charge) — always choosing the larger, registered, auditable party — securing the cash first and letting ITC neutralise the cost. Same tax, smarter collection.

Finally, GST's own compliance machinery would crush the smallest dealers. So the law offers them a **flat turnover tax with almost no paperwork** (composition), on the honest condition that they surrender ITC, tax collection, and inter-State reach. Grow past the ceiling and you graduate automatically to the normal regime.

Every rule in this chapter is one of three answers: *how is the tax authorised* (the charge), *how do we actually collect it* (forward vs reverse vs ECO), and *how do we keep the small alive* (composition).

---

## 10. Quick-Revision Sheet

**Charge**
- Sec 9(1) CGST: levy on intra-State supply, value u/s 15, rate ≤ 20%, paid by taxable person (forward charge).
- Sec 5 IGST: inter-State supply + imports, single IGST (= CGST+SGST), ceiling 40%.
- Out of GST: alcohol (permanent); petroleum ×5 (till notified — Sec 9(2)).
- Special sub-sections: 9(3) RCM notified supplies · 9(4) RCM from unregistered (notified classes) · 9(5) ECO deemed supplier.

**Reverse Charge (Sec 2(98), 9(3)/(4)/(5))**
- Recipient pays; **cash only** (no ITC to pay it); claim ITC after.
- **Compulsory registration** — Sec 24(iii), no threshold.
- **Self-invoice** — Sec 31(3)(f) — when supplier unregistered.
- Key 9(3) services: **GTA** (unless 12% FC), **advocate/legal**, arbitral tribunal, **sponsorship**, Govt services, **director** to company, insurance agent, recovery agent, motor-vehicle renting to body corporate, **import of service**.
- 9(5) ECO: cab aggregators, restaurant via platform (Zomato/Swiggy), unregistered-hotel accommodation, house-keeping.

**Composition (Sec 10)**
- 10(1) goods: preceding-year turnover ≤ **₹1.5 cr** (₹75 L special States).
  - Manufacturer **1%** (total turnover) · Trader **1%** (taxable turnover) · Restaurant **5%** (total).
  - May supply services up to higher of ₹5 L or 10% of turnover.
- 10(2A) service providers: turnover ≤ **₹50 L**, rate **6%**.
- Conditions: no inter-State outward supply · no supply via TCS e-commerce operator · not dealing in non-leviable goods · not a notified excluded manufacturer (ice-cream, pan masala, tobacco, aerated water) · not CTP/NRTP · all same-PAN registrations opt together.
- **No ITC · no tax collection · Bill of Supply · quarterly CMP-08 · annual GSTR-4 · pay RCM at normal rates.**
- Sec 10(3): option lapses the day turnover crosses the ceiling · Sec 10(5): wrong opt-in → normal tax + penalty.

*Flag once more: confirm all rates, thresholds and notified RCM/ECO/composition lists against the latest ICAI material and notifications for your exam attempt.*
