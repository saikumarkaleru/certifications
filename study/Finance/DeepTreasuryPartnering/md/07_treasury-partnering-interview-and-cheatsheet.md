# Treasury & Partnering Interview Drills + Cheat-Sheet

## What you'll be able to do

Sit across from a treasury or FP&A panel and handle the four cases they actually run: price and book a forward hedge, build and defend a cash-flow forecast, tell a partnering/influence story that lands, and present a recommendation to a "CFO" on the spot. You'll also carry a one-page cheat-sheet of treasury terms, hedge mechanics, and communication frameworks you can revise on the train to the interview. This chapter assumes you've read the treasury and partnering chapters; it's the rehearsal and the quick-reference.

## The essentials

Interview cases test whether you can *do the job out loud*: get the mechanics right, tie the numbers, state a recommendation, and stay calm under a follow-up. The pattern for every answer: **state the answer → show the mechanics → tie the number → name the risk/what you'd verify.** Never narrate your whole thought process without landing a conclusion.

## Hands-on — step by step (four drills)

### Drill 1 — Price and book a forward hedge

**Prompt.** "You're a treasury analyst. Your firm imports components and will pay **USD 1,000,000 in 90 days**. Spot USD/INR is **83.20**. You want to hedge with a forward. How do you price it and what do you book?"

**Answer.**
1. **Direction.** We're *short* USD (we owe dollars), so we **buy USD forward** — lock the rate today.
2. **Forward rate = spot × (1 + INR rate × t) / (1 + USD rate × t).** Say INR 90-day rate 7%, USD 5.5%, t = 90/360 = 0.25.
   - Forward = 83.20 × (1 + 0.07×0.25) / (1 + 0.055×0.25) = 83.20 × 1.0175 / 1.01375 ≈ **83.51**.
   - The ~31 paise premium reflects the interest-rate differential (INR trades at a forward premium because its rate is higher) — *not* a rupee "view."
3. **Locked cost.** USD 1,000,000 × 83.51 = **₹8.351 cr**, fixed, regardless of where spot goes.
4. **Accounting (cash-flow hedge, Ind AS 109).** Designate the forward as a hedge of a highly probable forecast purchase. Effective portion of fair-value change goes to **OCI / cash-flow hedge reserve**; on settlement it reclassifies to the cost of the components. Document the hedge relationship at inception and test effectiveness.
5. **What I'd verify live:** the actual USD and INR money-market rates, whether we book a forward or buy an option (if the purchase is only *probable*), and the counterparty credit line.

**Why this scores:** you gave direction, the exact formula, a tied number, the accounting, and named the verification. That's a treasury hire's answer.

### Drill 2 — Build a cash-flow forecast

**Prompt.** "Build a 13-week cash-flow forecast. Walk me through it."

**Answer.**
1. **Why 13 weeks:** it's the treasury standard — a full quarter, weekly granularity, short enough to be accurate, long enough to see a crunch coming.
2. **Method — direct, not indirect.** Start with **opening cash**, add **receipts** (collections from AR ageing, not revenue), subtract **disbursements** (payroll, supplier payments from AP ageing, tax, debt service, capex), get **closing cash** = next week's opening.
3. **Worked week:** Opening ₹5.0 cr + receipts ₹3.2 cr − payroll ₹1.1 cr − suppliers ₹2.4 cr − GST ₹0.4 cr = **closing ₹4.3 cr.** Roll 13 times.
4. **The output that matters:** the *minimum* closing balance across 13 weeks vs. the **minimum operating cash / covenant floor**. If week 7 dips below the floor, that's the message — flag it now, arrange the working-capital line before it's urgent.
5. **Drivers to stress:** collection timing (push AR out a week), a delayed large receipt, a tax outflow. Treasury lives on *timing*, not P&L.
6. **Verify live:** actual AR/AP ageing, confirmed vs. expected receipts, and the covenant definition of "cash."

### Drill 3 — A partnering / influence situation (STAR)

**Prompt.** "Tell me about a time you influenced a decision you didn't control."

**Answer (STAR).**
- **Situation:** A regional sales head wanted a 35% discount that breached our 20% self-approval floor, at quarter-end.
- **Task:** Protect the discount floor without killing a deal that hit her target.
- **Action:** I built the deal economics *before* the meeting, found the real cost was the renewal anchor it would reset — not the single deal — acknowledged her target, showed her that number, and brought two costed paths that still closed on time. I closed with a committed action and an owner.
- **Result:** She took the 2-year lock; we captured ₹2.6 cr, kept the blended discount intact, and she now calls me before she prices, not after. *That last line is the point — I became a partner, not a policeman.*

### Drill 4 — "Present this to the CFO" case

**Prompt.** "Gross margin missed budget by 3 points. Present it to me as the CFO. Go."

**Answer (top-down, so-what, 25 seconds).**
"Margin came in at 61% versus 64% budget — but it's **mostly a fixable freight issue, not a demand problem.** Three drivers, and they tie to the full 3 points: freight from the new supplier is 1.6 points, re-tender under way, back to plan by Q3; a one-off SKU-7 clearance discount is 0.8 point and won't repeat; FX on imported components is 0.6 point, and I'd like to hedge 60% forward. Demand and pricing are on plan. **The one decision I need from you is approval of the forward hedge.**"
Then stop — let the CFO ask. Have the SKU detail ready as backup.

## The output — the cheat-sheet

**Treasury terms**

| Term | Meaning |
|---|---|
| Spot / forward | Rate for immediate / future-dated FX settlement |
| Forward premium/discount | Currency trades above/below spot due to rate differential |
| Forward points | The premium/discount in pips added to spot |
| NDF | Non-deliverable forward — cash-settled, for restricted currencies |
| Swap (FX) | Simultaneous spot buy + forward sell (or vice versa) |
| MTM | Mark-to-market — current fair value of an open position |
| Notional | Face amount a derivative is based on |
| Netting | Offsetting receivables/payables to reduce settlement volume |
| Sweep / pooling | Concentrating group cash into one account |
| 13-week CFF | Direct-method rolling weekly cash forecast |
| Covenant | Lender condition (e.g., min DSCR, max leverage) |
| WACC | Weighted average cost of capital — the carry/discount rate |
| Value date | Date a payment actually settles |

**Hedge types**

| Instrument | Use | Payoff | Cost |
|---|---|---|---|
| Forward | Lock a known future FX/rate flow | Symmetric — locked rate, no upside | No premium; opportunity cost |
| Futures | Exchange-traded lock | Symmetric, daily margined | Margin, basis risk |
| Option | Protect but keep upside | Asymmetric — floor/cap | Premium paid |
| Swap (IRS) | Convert floating↔fixed rate | Exchange of rate flows | Spread |
| Collar | Bounded protection cheaply | Cap + floor | Low/zero net premium |

Hedge accounting (Ind AS 109 / IFRS 9): **cash-flow hedge** (future flow) → effective portion to OCI; **fair-value hedge** (existing asset/liability) → to P&L. Document at inception; test effectiveness.

**Communication frameworks**

| Framework | Use |
|---|---|
| SCQA | Frame any message: Situation, Complication, Question, Answer |
| Minto pyramid | Answer first; 3-4 MECE supports beneath |
| So-what test | Push every line to an action |
| STAR | Behavioural answers: Situation, Task, Action, Result |
| Action title | Slide title = the takeaway, not the topic |
| Power/interest grid | Map stakeholders per decision |
| Credible challenge | Acknowledge goal → surface number → offer path |

## Checks, gotchas & red flags

- **Forward premium ≠ a rupee view.** It's pure interest-rate differential. Saying "the forward is higher because the rupee will weaken" is the classic tell that you don't understand covered interest parity.
- **Direct vs. indirect cash forecast:** treasury uses **direct** (receipts/disbursements). Confusing it with the indirect (net-income-to-cash) statement is a red flag.
- **Numbers must tie:** the hedge cost, the 13-week closing balance, and the 3 margin drivers must each reconcile. Panels probe the sum.
- **Land the answer.** The commonest failure is narrating without a recommendation. Every case ends with "so my answer/ask is X."
- **Don't bluff a live rate.** "I'd pull the actual money-market rates and the counterparty line before booking" is strength, not weakness.

## Interview drill (meta)

**Q1. "Why hedge at all — isn't it just a cost?"**
"We hedge to remove *earnings volatility* from a risk we're not paid to take — FX on imports. A forward locks the rupee cost of a known dollar payable so margin is protected regardless of spot. We're an importer, not an FX trader; certainty on ₹8.35 cr is worth more than a punt on the rate."

**Q2. "When would you use an option instead of a forward?"**
"When the exposure is only *probable*, not committed — say a bid we might not win — so I don't want an obligation to deliver. An option caps the downside while leaving upside, at the cost of the premium. For a firm, committed payable, a forward is cheaper and cleaner."

**Q3. "You have five minutes with the CFO and a bad number. What's your structure?"**
"Answer first — the takeaway framed by so-what. Then a MECE breakdown that ties exactly to the variance, each driver with its nature and action. Then the one decision I need. I own the number calmly, bring the fix, and keep the detail in backup for the questions I know are coming."

## Learn/practise (free)

- **RBI FEDAI** materials and any bank's treasury explainer — free, India-specific FX forward and hedge mechanics.
- **CFA Institute / Investopedia** — free, correct notes on covered interest parity, forwards vs. options, IRS.
- **Rehearse free:** build the 90-day forward and the 13-week cash forecast in Excel with your own numbers; change spot and rates, watch the locked cost and closing balances move. Explain each out loud in under 60 seconds.
- **Mock the four drills** into a phone recorder; replay and cut every sentence that doesn't land the answer. The panel scores *landing*, not thoroughness.
- **Ind AS 109 / IFRS 9** hedge-accounting summaries (ICAI study material, free) — enough to say where the MTM lands (OCI vs P&L) and why.
