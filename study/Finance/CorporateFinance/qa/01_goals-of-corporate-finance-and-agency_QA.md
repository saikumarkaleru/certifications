# Q&A — The Goals of Corporate Finance & the Agency Problem

A mixed bank of theory and numerical questions. Theory answers include model wording and an interview one-liner. Numerical answers are fully worked and self-verified. Attempt each before reading the solution.

---

## Theory questions

### Q1 (Theory). What is the objective of the firm in corporate finance, and why "value" rather than "profit"?

**Model answer.** The normative objective is to **maximize long-run shareholder value** — the present value of the firm's expected future cash flows, discounted at a rate reflecting their risk. Common shareholders are the firm's **residual claimants** (paid after employees, suppliers, government, and creditors), so maximizing what's left for them tends, in efficient markets, to maximize total value.

We use *value* rather than *accounting profit* because profit is a single-period accrual figure that ignores three things value captures: the **timing** of cash (time value of money), the **risk** of cash (uncertain cash is worth less), and the **capital invested** to earn it. A manager can inflate this year's EPS by slashing R&D or maintenance and still destroy value.

**Interview one-liner:** *"Maximize value, not profit — value accounts for timing, risk, and capital; profit doesn't. And value is created only when ROIC exceeds WACC."*

---

### Q2 (Theory). Contrast shareholder primacy with stakeholder theory. What's the defensible reconciliation?

**Model answer.** **Shareholder primacy** (Friedman, Jensen) says the firm's single objective is maximizing shareholder value, giving management one clear, measurable maximand. **Stakeholder theory** (Freeman, ESG) says the firm should balance the interests of all stakeholders — employees, customers, suppliers, communities, environment.

Jensen's critique of pure stakeholder theory: an objective to serve *everyone* provides no way to trade off competing interests, so it becomes "accountable to all = accountable to none," which can shield managerial empire-building behind the language of purpose.

The reconciliation is **enlightened value maximization** (Jensen, 2001): the objective function remains long-run market value, but management recognizes you *cannot* maximize long-run value while abusing employees, cheating customers, or polluting — those destroy future cash flows. So stakeholder welfare is mostly an **input** to durable shareholder value, not a competing objective. Genuine externalities (e.g., uncompensated pollution) are best handled by regulation/taxation, not by discarding a coherent corporate objective.

**Interview one-liner:** *"Stakeholder satisfaction is usually a means to long-run shareholder value, not a competing end — that's enlightened value maximization."*

---

### Q3 (Theory). Name the three core corporate-finance decisions and the rule governing each.

**Model answer.**
1. **Investment (capital budgeting):** which real assets to own. Rule — accept every **positive-NPV** project, i.e. where ROIC > WACC. *This is where value is created.*
2. **Financing (capital structure):** how to fund assets. Rule — choose the debt/equity mix that **minimizes WACC**, trading off the tax shield and discipline of debt against distress and agency costs.
3. **Dividend / payout:** how much cash to return vs reinvest. Rule — **return cash whenever the firm cannot reinvest it above the cost of capital.**

The investment decision determines *how much* value exists; financing and payout mostly determine how it's *packaged and distributed*.

**Interview one-liner:** *"Invest above WACC, finance to minimize WACC, pay out what you can't reinvest above WACC."*

---

### Q4 (Theory). Define the agency problem and decompose agency costs.

**Model answer.** An **agency relationship** arises when a principal delegates decision authority to an agent. In a firm, shareholders (principals) hire managers (agents). The **agency problem** is the conflict from the agent having *different interests* and *superior information*, with contracts too incomplete to fully constrain managerial discretion.

**Jensen & Meckling (1976)** decompose **agency cost = monitoring costs + bonding costs + residual loss**:
- **Monitoring costs** — borne by the *principal* (audits, board oversight, analyst scrutiny).
- **Bonding costs** — borne by the *agent* (accepting covenants, holding equity, building reputation to reassure owners).
- **Residual loss** — the value still lost despite monitoring and bonding; the irreducible gap.

**Interview one-liner:** *"Separation of ownership and control plus information asymmetry equals agency cost — monitoring plus bonding plus residual loss."*

---

### Q5 (Theory). List the ways managers can act against shareholders' interests.

**Model answer.**
- **Empire-building** — value-destroying M&A and overinvestment for size, pay, and prestige.
- **Perquisite consumption** — jets, plush offices.
- **Entrenchment** — poison pills, golden parachutes, avoiding beneficial risk to protect their jobs.
- **Free-cash-flow hoarding** (Jensen 1986) — retaining cash rather than paying it out, to keep control of it.
- **Short-termism / earnings management** — hitting EPS targets tied to bonuses at the expense of long-term investment.
- **Excessive risk-aversion** — rejecting positive-NPV risky projects because managers' undiversified human capital is tied to the firm.

**Interview one-liner:** *"Empire-building, entrenchment, and hoarding free cash flow are the three you must be able to name."*

---

### Q6 (Theory). Explain the shareholder-creditor conflict and its four classic forms.

**Model answer.** Once a firm has debt, shareholders (residual claimants who control the firm) can expropriate value from creditors (fixed claimants). Equity is effectively a **call option** on the firm's assets — limited liability caps the downside at zero with unlimited upside — so shareholders *like* volatility; creditors, effectively **short a put**, hate it. Four forms:
1. **Asset substitution / risk-shifting** — after borrowing, swap safe projects for risky ones; upside to equity, downside to creditors.
2. **Underinvestment / debt overhang** (Myers 1977) — near distress, equity rejects positive-NPV projects because gains accrue mainly to creditors.
3. **Claim dilution** — issue new equal/higher-priority debt, diluting existing creditors.
4. **Excess dividends / leveraged recap** — drain cash to shareholders, leaving less asset backing for creditors.

Creditors respond with **covenants** (restricting dividends, new debt, asset sales; requiring coverage ratios), **collateral**, **shorter maturities**, and **higher spreads**.

**Interview one-liner:** *"Equity gambles with creditors' money via limited liability; covenants and pricing are the creditor's defense."*

---

### Q7 (Theory). What is the separation of ownership and control, and why does it persist despite causing agency costs?

**Model answer.** **Berle & Means (1932):** in the modern public corporation, ownership is dispersed across many shareholders while control sits with professional managers who own little of the firm. It persists because its benefits are large: **specialization** (skilled managers run the firm, passive investors just supply capital), **risk diversification** (owners hold small stakes across many firms), and **liquidity/capital formation** (freely tradable shares let firms raise capital from many passive investors). Governance exists to keep those benefits while containing the agency cost the separation creates.

**Interview one-liner:** *"Separation is efficient — the agency cost is the price of specialization, diversification, and liquidity."*

---

### Q8 (Theory). Why won't dispersed small shareholders monitor management? What solves it?

**Model answer.** The **free-rider problem.** A shareholder owning 0.01% bears 100% of any monitoring cost but captures only 0.01% of the benefit (the rest spills over to other owners). So no dispersed owner rationally monitors — and since all reason identically, **no one does**. It's solved by **blockholders, institutional investors, and activists** who internalize a much larger share of the benefit and therefore have the incentive and power to monitor.

**Interview one-liner:** *"Concentrated ownership internalizes the monitoring benefit that dispersed ownership free-rides away."*

---

### Q9 (Theory). Distinguish internal from external governance mechanisms.

**Model answer.**
- **Internal:** the **board of directors** (independent majority, separate chair/CEO, independent audit/comp/nomination committees); **executive compensation** (equity-based, long-vesting, performance-linked, with clawbacks); **concentrated/blockholder ownership**; and **debt as a disciplinary device** (forces cash out as interest, per Jensen 1986).
- **External:** the **market for corporate control** (takeover threat); **institutional and activist investors**; the **legal/regulatory regime** (fiduciary duties, disclosure, SOX/Cadbury/Companies Act & SEBI LODR); and **product-market competition, reputation, auditors, and analysts**.

**Interview one-liner:** *"Boards and pay work from inside; the takeover market and activists work from outside."*

---

### Q10 (Theory). Why is debt sometimes described as a governance mechanism?

**Model answer.** Jensen's **free-cash-flow hypothesis (1986):** mandatory interest payments force managers to **disgorge cash** they'd otherwise waste on empire-building, and subject them to ongoing **creditor and capital-market monitoring**. This is a major reason **LBOs** can create value — the leverage disciplines management and concentrates ownership. The caveat: too much debt raises distress and agency-of-debt costs, so there's an optimal, not unlimited, dose.

**Interview one-liner:** *"Debt disciplines managers by forcing free cash out the door as contractual interest."*

---

### Q11 (Theory). How does executive compensation both solve and create agency problems?

**Model answer.** **Solves:** equity-based pay (RSUs, performance shares, options) makes managers **residual claimants**, aligning their wealth with shareholders'; long vesting and performance conditions (relative TSR, ROIC hurdles) fight short-termism; clawbacks and ownership guidelines bond behavior. **Creates:** poorly structured options give convex payoffs that encourage **risk-shifting** and **earnings manipulation** to hit price/EPS targets; peer-benchmarking **ratchets** pay upward regardless of performance; short vesting rewards short-termism. So compensation is a two-edged sword — *design* is everything.

**Interview one-liner:** *"Ownership aligns; badly designed options mis-align — comp is a two-edged sword."*

---

### Q12 (Theory). Outside the US/UK, what is often the dominant agency conflict, and through what channel?

**Model answer.** In much of Europe, Asia, India, and Latin America, ownership is **concentrated** in a family, founder, or the state rather than dispersed. So the primary conflict is not manager-vs-owner but **controlling shareholder vs minority shareholders.** The controller often has **control rights exceeding cash-flow rights** (a "wedge") via **dual-class shares** or **pyramid structures**, and can extract value through **tunneling** — related-party transactions, transfer pricing, or dilutive issuance that siphon value to the controller at minorities' expense. This is why minority-protection law and related-party-transaction scrutiny dominate governance risk in those markets.

**Interview one-liner:** *"In controlled firms the risk is tunneling by the controller, not empire-building by hired managers."*

---

## Numerical questions

### Q13 (Numerical). Value creation: ROIC vs WACC.

**Problem.** Helios Ltd invests ₹200 crore of new capital at WACC = 10%. Plan A earns ROIC = 8% forever; Plan B earns ROIC = 14% forever. Each is a level perpetuity (cash flow = ROIC × capital). Which creates value, and by how much?

**Solution.**
```
Plan A cash flow = 0.08 × 200 = ₹16 cr ;  PV = 16 / 0.10 = ₹160 cr ; NPV = 160 − 200 = −₹40 cr
Plan B cash flow = 0.14 × 200 = ₹28 cr ;  PV = 28 / 0.10 = ₹280 cr ; NPV = 280 − 200 = +₹80 cr
```
**Verify with the spread identity** `NPV = (ROIC − WACC)/WACC × Capital`:
- A: `(0.08 − 0.10)/0.10 × 200 = (−0.02/0.10) × 200 = −40` ✓
- B: `(0.14 − 0.10)/0.10 × 200 = (0.04/0.10) × 200 = +80` ✓

**Answer.** Plan A **destroys ₹40 cr** (grows the firm but earns below cost of capital); Plan B **creates ₹80 cr**. Growth is only valuable when **ROIC > WACC**. A manager who prefers A for the prestige of a bigger balance sheet is exhibiting the manager-shareholder agency problem.

---

### Q14 (Numerical). Agency cost of a perk and the ownership fix.

**Problem.** CEO Ravi owns 3% of Zephyr Corp; the rest is dispersed. He wants a ₹40 crore corporate art collection and private box that add zero operating value but give him personal benefit he values at ₹5 crore. (a) Does he pursue it at 3% ownership? (b) At what ownership stake does he stop wanting it? (c) State the agency cost.

**Solution.**
(a) At 3%:
```
Ravi's share of cost = 0.03 × 40 = ₹1.2 cr ; benefit = ₹5 cr ; net = 5 − 1.2 = +₹3.8 cr → he pursues it
```
(b) He is indifferent when his share of cost = his benefit:
```
s × 40 = 5  →  s = 5/40 = 0.125 = 12.5%
```
Above **12.5%** ownership he rejects it. Check at 20%: `0.20 × 40 = ₹8 cr cost > ₹5 cr benefit → net −₹3 cr → rejects.` ✓

(c) **Agency cost = ₹40 cr of firm value destroyed** to deliver ₹5 cr of private benefit — a **deadweight loss of ₹35 cr**, of which outside shareholders bear 97% (₹38.8 cr) of the spend.

**Answer.** The perk is pursued precisely because Ravi's tiny stake lets him externalize 97% of the cost — the essence of the manager-shareholder conflict and the free-rider logic. Raising his equity stake past 12.5% internalizes enough cost to align him; this is the rationale for equity-based pay.

---

### Q15 (Numerical). Risk-shifting / asset substitution.

**Problem.** Titan Ltd owes creditors ₹120 cr face value, due in one year. Two strategies, two equally likely states, firm values in ₹cr:

| | Safe | Risky |
|---|---|---|
| Up (0.5) | 140 | 200 |
| Down (0.5) | 130 | 60 |

Creditors get min(value, 120); equity gets max(value − 120, 0). Ignore discounting. Who prefers what, and what's total firm value under each?

**Solution.**
*Total expected firm value:*
```
Safe:  0.5×140 + 0.5×130 = 70 + 65 = ₹135 cr
Risky: 0.5×200 + 0.5×60  = 100 + 30 = ₹130 cr
```
*Creditors:*
```
Safe:  min(140,120)=120 ; min(130,120)=120 → E = 0.5×120 + 0.5×120 = ₹120 cr
Risky: min(200,120)=120 ; min(60,120)=60   → E = 0.5×120 + 0.5×60  = ₹90 cr
```
*Shareholders:*
```
Safe:  140−120=20 ; 130−120=10           → E = 0.5×20 + 0.5×10 = ₹15 cr
Risky: 200−120=80 ; max(60−120,0)=0      → E = 0.5×80 + 0.5×0  = ₹40 cr
```
**Check pieces sum to whole:** Safe 120+15 = 135 ✓; Risky 90+40 = 130 ✓.

**Answer.** **Shareholders prefer the risky strategy** (equity E = ₹40 cr > ₹15 cr) even though it **reduces total firm value by ₹5 cr** — limited liability shields them in the ₹60 cr state. **Creditors prefer safe** (₹120 cr > ₹90 cr): risk-shifting transfers ₹30 cr of expected value from them to equity *and* destroys ₹5 cr overall. This is why lenders impose covenants restricting risk, leverage, and asset sales.

---

### Q16 (Numerical). Debt overhang / underinvestment (Myers).

**Problem.** Nimbus Ltd will be worth, in one year, ₹80 cr (good, prob 0.5) or ₹40 cr (bad, prob 0.5) with its current assets. It owes creditors ₹70 cr. A new project needs **₹10 cr invested today by shareholders** and adds a **certain ₹15 cr** to firm value in both states. Ignore discounting. Will shareholders fund it? Is it positive-NPV for the firm?

**Solution.**
*Firm NPV of the project:* adds ₹15 cr for a ₹10 cr outlay → **+₹5 cr, clearly positive.**

*Without the project* — equity = max(value − 70, 0):
```
Good: 80−70 = 10 ; Bad: max(40−70,0) = 0 → E[equity] = 0.5×10 + 0.5×0 = ₹5 cr
```
*With the project* — firm values become 95 (good) and 55 (bad):
```
Good: 95−70 = 25 ; Bad: max(55−70,0)=0 → E[equity before outlay] = 0.5×25 + 0.5×0 = ₹12.5 cr
Shareholders paid ₹10 cr today → net to equity = 12.5 − 10 = ₹2.5 cr
```
Compare shareholder wealth: **without = ₹5 cr; with = ₹2.5 cr.**

**Answer.** Shareholders **reject** the positive-NPV project. Even though it adds ₹5 cr to firm value, most of the ₹15 cr gain flows to **creditors** (it rescues their claim in the bad state, where firm value rises from 40 to 55), while shareholders fund the full ₹10 cr. This is **debt overhang / underinvestment** — a distressed firm skips good projects because equity captures too little of the payoff. Verify creditor gain: creditor value goes from `0.5×70 + 0.5×40 = ₹55 cr` to `0.5×70 + 0.5×55 = ₹62.5 cr`, i.e. +₹7.5 cr — more than the whole ₹5 cr of firm NPV, confirming value shifts to debt.

---

### Q17 (Numerical). WACC and the financing decision.

**Problem.** Orion Ltd: equity ₹600 cr (cost of equity 15%), debt ₹400 cr (pre-tax cost 9%), tax rate 25%. (a) Compute WACC. (b) If it earns ROIC of 11% on its capital, is it creating value? (c) Intuitively, why might adding modest debt lower WACC?

**Solution.**
(a)
```
V = 600 + 400 = ₹1,000 cr ; E/V = 0.6 ; D/V = 0.4
After-tax cost of debt = 9% × (1 − 0.25) = 6.75%
WACC = 0.6 × 15% + 0.4 × 6.75% = 9.0% + 2.7% = 11.7%
```
(b) ROIC 11% < WACC 11.7% → **destroying value** (spread = −0.7%). EVA on ₹1,000 cr = `(0.11 − 0.117) × 1,000 = −₹7 cr` per year.

(c) Debt is cheaper than equity (lower required return + tax-deductible interest), so replacing some equity with debt lowers the weighted average — up to the point where rising distress and agency-of-debt costs push both k_e and k_d up faster than the mix benefit. That trade-off defines the optimal capital structure.

**Answer.** WACC = **11.7%**; at 11% ROIC the firm **destroys value**; modest leverage can lower WACC via the cheaper, tax-shielded cost of debt until distress costs dominate.

---

### Q18 (Numerical). Payout decision — reinvest or return cash.

**Problem.** Vega Ltd generates ₹100 cr of free cash flow. Its cost of capital is 12%. It has two possible uses: (i) reinvest all ₹100 cr in a project earning 9% forever, or (ii) pay it out to shareholders who can earn 12% (the market rate) elsewhere. As a level perpetuity, which is better and by how much?

**Solution.**
*Reinvest at 9%:* value created = `(0.09 − 0.12)/0.12 × 100 = (−0.03/0.12) × 100 = −₹25 cr`. The ₹100 cr becomes worth `0.09×100/0.12 = ₹75 cr`.
*Pay out:* shareholders redeploy ₹100 cr at 12%, exactly the cost of capital → **zero NPV, value preserved at ₹100 cr.**

**Answer.** **Pay it out.** Reinvesting below the cost of capital destroys ₹25 cr; returning the cash preserves the full ₹100 cr because shareholders can earn the required return themselves. Rule confirmed: **return cash whenever internal reinvestment earns below WACC.** A manager who insists on reinvesting the ₹100 cr at 9% (to keep control of the cash and grow the empire) is the **free-cash-flow agency problem** in action.

---

### Q19 (Numerical). Covenant / coverage-ratio screen (credit angle).

**Problem.** A loan covenant requires **Interest Coverage (EBIT/Interest) ≥ 3.0x** and **Net Debt/EBITDA ≤ 3.5x**. Sirius Ltd reports EBIT ₹90 cr, D&A ₹30 cr, interest ₹25 cr, total debt ₹380 cr, cash ₹30 cr. (a) Is it in compliance? (b) A shareholder-friendly board proposes a ₹60 cr debt-funded special dividend (adds ₹60 cr debt, drains ₹0 cash, interest rises by ₹6 cr). Does it breach either covenant?

**Solution.**
(a) Before:
```
EBITDA = EBIT + D&A = 90 + 30 = ₹120 cr
Interest coverage = 90 / 25 = 3.6x  ≥ 3.0x ✓
Net debt = 380 − 30 = ₹350 cr ; Net Debt/EBITDA = 350 / 120 = 2.92x ≤ 3.5x ✓  → compliant
```
(b) After the debt-funded dividend (debt → 440, cash unchanged 30, interest → 31):
```
Interest coverage = 90 / 31 = 2.90x  < 3.0x  ✗ BREACH
Net debt = 440 − 30 = ₹410 cr ; Net Debt/EBITDA = 410 / 120 = 3.42x  ≤ 3.5x ✓ (just inside)
```
**Answer.** Currently compliant. The special dividend **breaches the interest-coverage covenant** (2.90x < 3.0x), even though leverage stays just inside the 3.5x limit. This is exactly the **shareholder-creditor conflict** (excess dividends / leveraged recap) that covenants exist to block — the coverage covenant catches the transfer of value from creditors to shareholders that the leverage covenant alone would have missed.

---

### Q20 (Numerical). Aligning pay: how much equity makes the manager indifferent to effort?

**Problem.** Manager Leela can exert extra effort that costs her a personal ₹2 cr (time, stress) but raises firm value by ₹40 cr. She is paid a fixed salary plus a fraction *s* of firm value. What minimum equity fraction *s* makes her willing to exert the effort? Interpret.

**Solution.**
She exerts effort if her share of the value gain ≥ her private cost:
```
s × 40 ≥ 2  →  s ≥ 2/40 = 0.05 = 5%
```
**Answer.** She needs at least a **5% equity-linked stake** in firm value. Below 5% she captures too little of the ₹40 cr gain to justify her ₹2 cr private cost, so she shirks — a residual loss. This is the quantitative logic of **performance-based equity compensation**: give the agent enough of the residual claim that her private cost-benefit tracks the shareholders'. Note the symmetry with the perk problem (Q14) — ownership can both stop value-destroying perks *and* motivate value-creating effort.

---

### Q21 (Numerical). Empire-building acquisition — does it create or destroy value?

**Problem.** Atlas Ltd (cost of capital 12%) acquires Target Co for ₹500 cr. Target will generate ₹48 cr of after-tax free cash flow forever, growing at 2% perpetually. Management touts the deal as "growth." (a) What is Target worth to Atlas? (b) Value created or destroyed? (c) What agency issue does this illustrate?

**Solution.**
(a) Growing perpetuity value = `CF₁ / (r − g)`:
```
Value to Atlas = 48 / (0.12 − 0.02) = 48 / 0.10 = ₹480 cr
```
(b)
```
NPV = value − price = 480 − 500 = −₹20 cr → DESTROYS ₹20 cr
```
Implied acquisition yield: at ₹500 cr price, `500 = 48/(0.12 − g_break)` → `0.12 − g_break = 48/500 = 0.096` → the deal only breaks even if growth were **2.4%**, above the assumed 2% — Atlas overpaid.

**Answer.** The firm gets bigger (more revenue, more assets, higher headline earnings) but **destroys ₹20 cr** because it paid ₹500 cr for ₹480 cr of value. This is textbook **empire-building** — growth in size that lowers per-share value, typically driven by managerial prestige/pay incentives rather than shareholder value. It's exactly why acquirers' shares often fall on deal announcements and why boards and activists scrutinize M&A.

---

### Q22 (Numerical). Free-rider monitoring economics.

**Problem.** A firm's value would rise by ₹100 cr if management were properly monitored, but monitoring costs any single shareholder ₹5 cr to carry out. (a) Would a 1% shareholder monitor? (b) A 40% blockholder? (c) What's the minimum stake at which monitoring is individually rational?

**Solution.**
A shareholder with fraction *s* captures `s × 100` of the benefit and pays the full ₹5 cr cost. Monitor if `s × 100 ≥ 5`.
```
(a) 1%:  0.01 × 100 = ₹1 cr  < ₹5 cr → does NOT monitor
(b) 40%: 0.40 × 100 = ₹40 cr > ₹5 cr → DOES monitor
(c) Break-even: s × 100 = 5 → s = 5% 
```
**Answer.** The 1% holder free-rides (captures ₹1 cr, pays ₹5 cr — a personal loss), so monitoring doesn't happen despite being hugely value-additive for owners as a group. A blockholder above **5%** finds it privately rational to monitor. This is why **concentrated ownership, institutions, and activists** are central to governance — they internalize enough of the collective benefit to overcome the **free-rider problem** that paralyzes dispersed owners.

---

## One-page self-test (cover the answers)

1. Value created only when **ROIC > WACC**.
2. Three decisions: **invest, finance, pay out.**
3. Agency cost = **monitoring + bonding + residual loss.**
4. Manager-shareholder conflicts: **empire-building, entrenchment, FCF hoarding, short-termism.**
5. Shareholder-creditor conflicts: **risk-shifting, underinvestment/overhang, claim dilution, excess dividends** → **covenants.**
6. Separation of ownership & control: **Berle & Means 1932**; benefits = specialization, diversification, liquidity.
7. **Free-rider problem** → why blockholders/institutions/activists matter.
8. Stakeholder reconciliation = **enlightened value maximization.**
9. Governance internal = **board, pay, blockholders, debt**; external = **takeover market, activists, law, product market.**
10. Debt disciplines via **forcing out free cash flow** (Jensen 1986).
