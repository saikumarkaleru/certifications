# GST — Value of Supply

> Sec 15 CGST Act + Valuation Rules 27–35. Rules stable; verify GST rates, TCS position and Rule 32 slab figures against ICAI material.

## Snapshot
GST is ad valorem, so value must be pinned precisely. Default = **transaction value** (price actually paid/payable) but ONLY if (i) parties **unrelated** AND (ii) price is **sole consideration**. Then add inclusions (15(2)) and subtract discounts (15(3)). If price disqualified or missing → Valuation Rules ladder (OMV → like-kind → cost+10% → best judgement). GST value is always **exclusive of GST itself**.

## Core concepts
- "Transaction value" = starting price *after* 15(2)/15(3) surgery, not the invoice figure.
- Two gatekeepers fail independently: "unrelated" polices **who**; "sole consideration" polices **what**. "R.S." disqualifies — **R**elated or not **S**ole consideration → go to Rules.
- Rules are an **evidence hierarchy** — never skip a rung upward (weaker evidence over stronger).
- One value per transaction; split the **tax** (CGST+SGST/IGST), not the value.

## Key provisions / rules

### Sec 15(2) Inclusions — "T-P-I-I-S"
| Clause | Include | Watch-out |
|---|---|---|
| 15(2)(a) | **T**axes/duties/cesses/fees under any law **other than GST**, if charged separately | GST itself (CGST/SGST/IGST/Cess) NEVER included. TCS (Income-tax Act) **not** included (verify) |
| 15(2)(b) | **P**ayments supplier liable but recipient paid (not in price) | Only supplier's obligation; buyer's own liability (FOR-buyer freight) = nothing to add |
| 15(2)(c) | **I**ncidental expenses — commission, packing, done **at/before delivery** | Post-delivery independent service = separate supply |
| 15(2)(d) | **I**nterest/late fee/penalty for **delayed payment** | Taxed on **receipt** (Sec 12(6)/13(6)); accrued-unpaid not yet valued |
| 15(2)(e) | **S**ubsidies **price-linked**, **non-government** | Government subsidy always EXCLUDED; non-price-linked grant EXCLUDED |

### Sec 15(3) Exclusions (discounts)
| Type | Condition |
|---|---|
| Pre/at supply — 15(3)(a) | Must be **recorded in invoice** |
| Post-supply — 15(3)(b) | ALL FOUR: (1) agreement at/before supply, (2) linked to relevant invoices, (3) credit note issued, (4) recipient **reverses ITC** |

Post-supply discount with no prior agreement = NOT deductible. Blanket year-end rebate not tied to invoices = fails linkage.

### Valuation Rules ladder (15(4) → Rules 27–31)
| Rule | Trigger | Method |
|---|---|---|
| 27 | Non-money consideration (barter/exchange) | OMV → money + money-equivalent → like kind → 30/31 |
| 28 | Related/distinct persons | OMV → like kind → 30/31. **Proviso 1: full ITC → invoice value = OMV.** Proviso 2: goods for onward supply as-such → optional 90% of recipient's onward price |
| 29 | Through agent | OMV OR (supplier's option) **90%** of agent's price to unrelated customer → 30/31 |
| 30 | No anchor | **110% of cost** (cost + 10%) |
| 31 | Nothing works | Best judgement (services may skip 30, use 31 directly) |

- **OMV** = full money value (ex-GST) at **same time**, **unrelated**, **sole consideration**.
- "Like kind and quality" = substantially resembling in characteristics/quality/quantity/function/reputation.

### Sec 15(5) — notified sectors (Rule 32, PRIMARY, overrides transaction value)
- 32(2) Forex: rate-difference (|txn rate − RBI ref| × units; or 1% if no ref rate) OR annual slab (1% up to 1L min ₹250; ₹1,000+0.5% on 1L–10L; ₹5,500+0.1% above 10L, cap ₹60,000).
- 32(3) Air travel agent: **5% basic fare domestic / 10% international** (basic fare only, not total).
- 32(4) Life insurance: gross premium less investment portion; or 25% first year / 12.5% thereafter.
- 32(5) Second-hand goods **margin scheme**: SP − PP (no ITC availed); **negative margin ignored**; repossession → depreciation haircut per quarter.
- **Rule 33 pure agent** (excluded from value): 5-limb test — acts as pure agent on authorisation, separately indicated, additional to own supply, recipient liable, recovered at actuals no markup.
- **Rule 34** rate of exchange: goods → CBIC Customs Sec 14 rate; services → GAAP rate; at TOS date.
- **Rule 35** tax-inclusive: **Value = inclusive amount × 100 ÷ (100 + rate)**.

## Worked mini-example
Unrelated intra-State machine sale, GST 18%: Basic 5,00,000; municipal tax (separate) 20,000; packing 15,000; installation before delivery 25,000; late-payment interest received 8,000; private price-linked subsidy 30,000; invoice trade discount 40,000; pre-agreed post-supply discount (ITC reversed) 10,000.
- Add: 5,00,000 + 20,000 + 15,000 + 25,000 + 8,000 + 30,000 = **5,98,000**.
- Less: 40,000 + 10,000 = 50,000 → **Value = ₹5,48,000**. CGST 49,320 + SGST 49,320. Total = **₹6,46,640**.
- If subsidy were from State Govt → excluded → value 5,18,000.

## Exam traps & must-remember
1. GST itself **never** in value (15(2)(a) carve-out).
2. Government subsidy excluded; only non-government **price-linked** subsidy included.
3. Post-supply discount with no prior agreement = NOT deductible.
4. Rule 28 full-ITC proviso: invoice value accepted as OMV (revenue-neutral).
5. Ladder is sequential — can't use Rule 30 if OMV available.
6. TCS (Income-tax Act) NOT included in value (verify).
7. Tax-inclusive price → Rule 35 divisor (×100÷(100+rate)); don't apply rate on inclusive figure.
8. Delayed-payment interest taxed on **receipt** only.
9. Free supply to unrelated party = generally not a supply; between related/distinct persons = supply (Schedule I) → value under Rule 28.
10. Employer–employee related; but gifts up to ₹50,000/year not a supply. Sole agent/distributor deemed related.
11. Air agent 5%/10% on **basic fare**, not total fare.
12. Pure agent excludes only recipient's **third-party liability** at actuals; supplier's own out-of-pocket costs INCLUDED.
13. Add buyer-paid amount only if it discharged **supplier's** obligation.
14. Sec 15(5) notified supplies override transaction value (Rule 32 primary).
15. Negative margin (Rule 32(5)) ignored, not carried.
16. One value, split tax.

## One-line recall
- Value = transaction value IF unrelated AND sole consideration; else Rules.
- Inclusions T-P-I-I-S; exclusions = disclosed pre-supply discount / pre-agreed+ITC-reversed post-supply discount.
- GST, government subsidies, non-price-linked grants, TCS, pure-agent pass-through = NEVER in value.
- Rules ladder: 27 (non-money) → 28 (related; full ITC=invoice) → 29 (agent, 90%) → 30 (cost+10%) → 31 (best judgement).
- Rule 32 sectors override; Rule 35 tax-inclusive = ×100÷(100+rate).
- Air agent 5%/10% basic fare; second-hand = margin (negative ignored).
