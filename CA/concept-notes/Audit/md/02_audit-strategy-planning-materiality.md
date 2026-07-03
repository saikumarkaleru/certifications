<!-- v2-deep -->

# Chapter 02 — Audit Strategy, Planning & Materiality

## 1. The Problem — You Cannot Check Everything, And Not Everything Deserves Checking

Imagine you are handed the books of a company with ₹800 crore of turnover, three lakh sales invoices, a lakh purchase entries, seven factories, two subsidiaries, inventory in nine warehouses, and a ledger with four thousand accounts. You have a team of six people and about eight weeks. Now answer honestly: **can you verify every transaction?**

You cannot. Not in eight weeks, not in eight years. And here is the deeper trap — even if you *could* check everything, it would be **wasteful and pointless**, because most of those transactions are tiny, routine, low-risk, and even if a few were wrong, it would not change the decision of a single investor or banker reading the accounts.

So the auditor faces two problems at once:

1. **The scarcity problem** — finite time, finite people, finite fees, versus an ocean of transactions. If you spread your effort evenly like butter on toast, you will look at everything shallowly and catch nothing.
2. **The relevance problem** — some errors matter and some do not. A ₹2,000 misclassification in a company with ₹50 crore profit changes nobody's mind. A ₹5 crore overstatement of revenue might turn a loss into a profit and mislead every shareholder.

Recall the trust/agency problem from Chapter 1: owners cannot verify managers, so they hire an independent expert to give **reasonable assurance** that the financial statements are free from **material** misstatement. Note the two load-bearing words — *reasonable*, not absolute; and *material*, not perfect. The entire architecture of planning and materiality flows from unpacking those two words.

**Why "reasonable" and not "absolute" assurance — the three permanent limitations.** The audit can never promise perfection because of inherent limitations that no amount of work removes: (a) the **nature of financial reporting** — many figures are *estimates* (provisions, useful lives, fair values, expected credit losses) that are inherently imprecise, so there is no single "correct" number to verify against; (b) the **nature of audit procedures** — the auditor relies on evidence that is *persuasive rather than conclusive*, works with management-supplied information, and cannot detect a collusive, well-concealed fraud with the certainty of an omniscient observer; and (c) the need for the audit to be **completed within a reasonable time and at a reasonable cost** — an audit that took three years and cost more than the company earns would be useless to the very users it serves. Planning and materiality are the disciplined response to limitation (c): they are how the auditor squeezes *reasonable* assurance out of *finite* resources. This is why "reasonable assurance" is a **high but not absolute** level of assurance — high enough that users can rely on the opinion, but honestly bounded by the three limitations above.

**The risk this chapter addresses:** an auditor who does not plan will either (a) run out of time and give an opinion on statements he barely examined, or (b) burn his hours on trivial areas and completely miss the one account where management had both the *motive* and the *opportunity* to lie. Both outcomes mean a **wrong opinion attached to a clean-looking signature** — the exact failure the audit exists to prevent.

Planning and materiality are therefore not administrative housekeeping. They are the auditor's answer to the question: *given that I can't check everything, how do I make sure that what I do check is enough to catch the misstatements that would actually mislead a user?*

**A finer distinction the exam tests — planning is not the same as "the plan."** Students collapse three ideas into one. *Planning* is the ongoing **activity** of thinking about the engagement. The *overall audit strategy* and the *audit plan* are two **documents/outputs** of that activity. And *scheduling* (who works which week) is a resourcing sub-decision inside the strategy. When an examiner asks "distinguish audit planning from audit programme," the crisp answer is: planning is the broad forward-thinking activity that sets scope, timing, direction and resources; the **audit programme** is the detailed *list of procedures* (the operational heart of the audit plan) that the assistants actually execute and sign off. One is the thinking; the other is the checklist that thinking produces.

---

## 2. The Core Idea — Aim Effort Where Money Is Both Large and Likely to Be Wrong

The core idea has two blades that cut together:

> **Materiality tells you how big a misstatement must be before it matters. Risk tells you where misstatements are most likely to hide. Planning is the act of pointing your scarce audit effort at the intersection — large amounts that are also risky.**

Everything else is detail. If an amount is trivially small, you do little, because even if it's wrong nobody is misled. If an amount is large but sits in a rock-solid, low-risk area (say, share capital that hasn't changed in years), you do a bit. If an amount is large **and** risky (revenue recognition, provisions, related-party dealings, inventory valuation), you throw the bulk of your effort there.

This is why an auditor's file for a company is never a uniform grid. It is deliberately **lopsided** — thick where money and risk concentrate, thin where they don't. That lopsidedness is not laziness; it is the *whole point*. A file that is evenly thick everywhere is the mark of an auditor who never planned.

Two standards operationalise this idea:

- **SA 300 — Planning an Audit of Financial Statements**: gives you the *machinery* — build an overall audit strategy, then a detailed audit plan.
- **SA 320 — Materiality in Planning and Performing an Audit**: gives you the *threshold* — how big is big enough to matter, and how to set a safety-margin below it.

They are joined at the hip: you cannot plan effort without knowing what "matters," and knowing what matters is useless unless you translate it into a plan of action.

**The third, silent partner — SA 315.** Planning has a hidden dependency the exam rewards you for naming: you cannot decide *where risk hides* without first **understanding the entity and its environment** (SA 315). So the true chain is **SA 315 (understand → find risks) → SA 320 (size the threshold) → SA 300 (aim effort) → SA 330 (respond)**. Materiality and risk are the two coordinates; SA 315 is the survey that produces the map, and SA 330 is the response you plot on it. Keep this quartet in your head — nearly every planning question is really testing whether you see all four working together.

*Figure 2.1 — The two blades of the core idea: materiality sets the size threshold, risk sets the location, planning aims effort at their intersection.*

```mermaid
flowchart TD
    A["Finite audit resources"] --> B["Where do I point them"]
    B --> C["Materiality asks HOW BIG must an error be to matter"]
    B --> D["Risk asks WHERE are errors most likely"]
    C --> E["Direct effort to LARGE amounts"]
    D --> F["Direct effort to RISKY amounts"]
    E --> G["Concentrate work at the INTERSECTION large plus risky"]
    F --> G
    G --> H["Reasonable assurance achieved efficiently"]
```

---

## 3. Why It's Built This Way — The Logic Behind Each Requirement

Before the technical content, let's earn each rule from first principles, so nothing has to be memorised.

**Why plan at all, formally and in writing?** Because human effort left unplanned drifts toward the easy and the familiar, not the important. A junior will happily vouch a hundred petty-cash slips because it's comfortable, while the ₹10 crore revenue-cut-off question goes untouched. A documented plan forces the engagement to confront risk *before* fieldwork begins, when there is still time to allocate senior staff and specialist attention to the hard areas. Planning is a **commitment device** against the natural gravity toward trivia.

**Why split strategy from plan?** Because scope-and-direction decisions (which offices, which subsidiaries, what timing, which specialists, how big the team) are a *different kind* of thinking from procedure-level decisions (do I confirm receivables or examine subsequent receipts). Mixing them produces mush. Strategy is the *aerial map*; the plan is the *street-by-street route*. You must draw the map before the route, because the route depends on where you've decided to go.

**Why a materiality threshold instead of chasing every rupee?** Because the user of accounts is a *decision-maker*, not an accountant seeking perfection. Materiality is defined by reference to whether a misstatement, individually or in aggregate, could reasonably be expected to **influence the economic decisions** of users taken on the basis of the financial statements. If it wouldn't change a decision, chasing it wastes the audit's scarce resources and delays the report that users actually need. The threshold is the auditor's formal recognition that *the goal is a reliable decision, not a flawless ledger.*

**Why performance materiality — a number *below* materiality?** This is the most beautiful piece of logic in the chapter, so slow down. Suppose materiality for the financial statements as a whole is ₹1 crore. If you set your working threshold at exactly ₹1 crore, you'd ignore every individual error under ₹1 crore. But **errors aggregate**. Fifty different accounts each understated by ₹5 lakh — every one "below materiality" — sum to ₹2.5 crore, which is *materially* wrong. Also, your sampling only *tests a portion*; undetected errors lurk in the untested remainder. So you deliberately work to a **lower** number (performance materiality) to leave a cushion, so that the sum of (a) uncorrected small errors you did catch and (b) undetected errors you never saw still stays under overall materiality. Performance materiality is a **buffer against aggregation and against the imperfection of sampling.** It is risk management expressed as a number.

**Why benchmarks and percentages?** Because "how big is big" is meaningless in the abstract — ₹1 crore is catastrophic for a small trader and a rounding error for a conglomerate. Materiality must be *relative* to the entity, so we anchor it to a benchmark that reflects what users care about (profit, revenue, or net assets, depending on the business) and apply a judgement-based percentage.

**Why not just pick the largest number on the face of the accounts as the benchmark?** Because size is not the same as *relevance to decisions*. Total assets of an asset-light software firm may be trivial while its earnings are what the market prices; total revenue of a razor-thin-margin trading house may dwarf a profit figure that is nonetheless what its bankers watch. The benchmark is chosen for **decision-relevance and stability**, not for being the biggest figure. Picking a benchmark is really answering "what single number would a reasonable user of *this* entity look at first?"

**Why is materiality set for the financial statements as a whole, not per-user?** Because different users care about different things — a lender watches solvency, an investor watches earnings, a supplier watches liquidity — and the auditor cannot design a bespoke threshold for each. So SA 320 sets materiality at the level of the *common information needs of users as a group*. The auditor does **not** consider the possible effect on one particular user whose needs are extreme or idiosyncratic; that would make the threshold un-workable. This is the same reasoning that lets us make standard **assumptions about users** (below).

**Why document all of this?** Because judgement that isn't written down cannot be reviewed, cannot be defended if the audit is questioned years later, and cannot guide the team. Documentation converts one person's private reasoning into the engagement's shared, reviewable, defensible plan.

**Why does the auditor — not management — set materiality?** Because materiality is an **audit-planning tool**, an input to designing procedures and evaluating findings. It is *not* a figure disclosed in the financial statements, *not* negotiated with the client, and *not* the same as any "materiality" management might use for its own accounting policies. Letting management set it would let the audited party decide how hard it gets audited — an obvious conflict. The auditor exercises this judgement independently and keeps the figure inside the audit file.

---

## 4. Full Technical Content — The Standards, By Purpose

### 4.1 SA 300 — Planning an Audit of Financial Statements

**Purpose (the "why" of the whole standard):** to ensure the audit is conducted in an *effective manner* — meaning attention is devoted to important areas, potential problems are identified and resolved on a timely basis, and the engagement is properly organised, staffed, directed and supervised.

SA 300 spells out the benefits of planning, and each benefit maps to a risk it defeats:

| Benefit of planning (SA 300) | The risk it defeats |
|---|---|
| Helps devote appropriate attention to important areas | Effort scattered on trivia; big risks missed |
| Helps identify and resolve problems on a timely basis | Nasty surprises discovered too late to address before the report deadline |
| Helps organise and manage the engagement efficiently | Duplicated work, idle staff, blown budgets and fees |
| Assists in selecting team members with appropriate capabilities and competence, and assigning work to them | A junior sent to audit a complex derivatives portfolio he cannot understand |
| Facilitates direction and supervision of the team and review of their work | Team members work in the dark; errors in their work go uncaught |
| Assists in coordinating work done by component auditors and experts | The valuation expert's work arrives too late or doesn't fit the audit's needs |

**Preliminary engagement activities (do these *before* planning):** SA 300 requires the auditor, at the *beginning* of the current audit, to:
- perform procedures regarding the **continuance** of the client relationship and the specific engagement (is this client still one we want, with acceptable integrity?);
- evaluate compliance with **ethical requirements**, including **independence** (SA 220 / the Code); and
- establish an **understanding of the terms of the engagement** (SA 210 — the engagement letter).

*Why first?* Because there's no sense planning an audit you shouldn't accept, or that you're not independent to perform. These gate-keeping checks come before you invest in strategy. A subtle point examiners probe: performing these *preliminary* activities at the start of the **current** period helps the auditor identify events that may adversely affect the ability to plan and perform — for example, a loss of independence, or discovering management integrity issues that would make continuance inappropriate. They are a *filter*, and the filter runs every year, not only in year one.

**The two-layer output of SA 300:**

**(a) The Overall Audit Strategy** — sets the **scope, timing and direction** of the audit and guides the development of the detailed plan. In establishing it, the auditor:
- identifies the **characteristics of the engagement that define its scope** (financial reporting framework applicable, industry-specific reporting, locations/components, reliance on internal audit);
- ascertains the **reporting objectives to plan the timing** of the audit and the nature of communications required (deadlines for interim and final reporting, key dates for meetings with those charged with governance);
- considers the **factors that, in the auditor's professional judgement, are significant** in directing the team's efforts (determination of materiality, preliminary identification of high-risk areas, results of previous audits, evidence of management's commitment to sound internal control);
- considers the results of **preliminary engagement activities**; and
- ascertains the **nature, timing and extent of resources** necessary to perform the engagement (how many people, how experienced, when deployed, budget).

Think of the strategy as answering four questions: **What are we auditing? When must it be done? Where are the risky areas that should shape our effort? Who and how much do we need?**

*A finer distinction — scope vs direction, which students blur.* **Scope** is about the *boundaries and characteristics* of the engagement (which framework, which components, which locations, whether internal audit's work will be used). **Direction** is about *where within those boundaries effort is steered* (materiality, the preliminary high-risk areas, prior-year results, management's control attitude). Scope draws the fence; direction decides which paddocks inside the fence get the most attention. If an exam question lists "determination of materiality" under scope, it is wrong — materiality is a **direction** factor.

**(b) The Audit Plan** — more detailed than the strategy; it converts strategy into specific procedures. It must include a description of:
- the **nature, timing and extent of planned risk assessment procedures** (as per SA 315);
- the **nature, timing and extent of planned further audit procedures** at the assertion level (as per SA 330) — i.e., tests of controls and substantive procedures; and
- **other planned procedures** required to comply with the SAs.

*The "nature, timing and extent" (NTE) triad — decode it, because it recurs everywhere.* **Nature** = *what kind* of procedure and its purpose (inspection, observation, external confirmation, recalculation, analytical procedure) and whether it is a test of controls or a substantive test. **Timing** = *when* it is performed (interim vs at/after year-end) and which period it covers. **Extent** = *how much* (sample size, number of locations, quantity of items). Higher assessed risk pushes all three toward *more persuasive* evidence: more reliable **nature** (e.g., external confirmation over internal enquiry), timing **closer to** or **at** year-end, and **larger** extent. Any question about "how does the auditor respond to higher risk" is answered through this triad.

*Relationship between the two:* The strategy sets the broad approach; the plan details the procedures that, if performed, achieve that approach. They are **not linear and once-off** — the standard stresses that planning is **continuous and iterative**. As the audit progresses and you learn things (a control you expected to rely on fails; a new risk emerges), you **update and change** the strategy and plan. Planning is a dial you keep turning, not a switch you flip once.

**Direction, supervision and review:** SA 300 requires the auditor to plan the **nature, timing and extent of direction and supervision** of team members and the **review** of their work. The extent scales with risk and staff competence — a risky area worked by a junior needs close supervision; a low-risk area worked by an experienced manager needs less. (This dovetails with SA 220, Quality Control.) A neat way to remember the drivers: direction/supervision/review intensity rises with (i) the **assessed risk** of the area, (ii) the **complexity** of the subject matter, and (iii) falls with the **competence and experience** of the staff assigned. A complex, high-risk area handed to a first-year article requires the most oversight of all.

**Documentation (SA 300 para on documentation):** the auditor shall document:
- the **overall audit strategy**;
- the **audit plan**; and
- any **significant changes** made during the engagement to the strategy or plan, and the **reasons** for such changes.

*Why document changes and reasons?* Because a change of plan mid-audit is exactly where things go wrong and exactly what a later reviewer or regulator will scrutinise. Recording *why* you changed course shows the change was a reasoned response to new information, not drift.

**Additional considerations for initial (first-year) audits:** SA 300 flags that an *initial* audit needs *more* planning, because the auditor has no prior cumulative knowledge of the entity. Extra activities include arrangements with the **predecessor auditor** (e.g., review of prior working papers, subject to SA 210/ethical clearance) and procedures on **opening balances** (SA 510). *Why more?* A continuing auditor carries forward a stock of understanding — known control weaknesses, the entity's estimation habits, past misstatements — that shortcuts risk assessment. A first-year auditor starts cold and must build that understanding from scratch, and must additionally satisfy himself that **opening balances** (which he did not audit) do not contain misstatements that materially affect the current period, and that prior-period **closing balances** were correctly carried forward.

*Figure 2.2 — SA 300 flow: gate-keeping first, then strategy, then plan, with a continuous feedback loop back into both.*

```mermaid
flowchart TD
    A["Preliminary engagement activities"] --> A1["Client continuance"]
    A --> A2["Ethics and independence"]
    A --> A3["Engagement terms letter"]
    A1 --> B["Establish OVERALL AUDIT STRATEGY"]
    A2 --> B
    A3 --> B
    B --> B1["Scope what and where"]
    B --> B2["Timing when and deadlines"]
    B --> B3["Direction materiality and risk focus"]
    B --> B4["Resources who and how much"]
    B1 --> C["Develop detailed AUDIT PLAN"]
    B2 --> C
    B3 --> C
    B4 --> C
    C --> C1["Risk assessment procedures SA 315"]
    C --> C2["Further audit procedures SA 330"]
    C --> C3["Other required procedures"]
    C1 --> D["Perform the audit"]
    C2 --> D
    C3 --> D
    D --> E["New information or changed risk"]
    E -->|update and document reasons| B
    E -->|update and document reasons| C
```

**The interaction between strategy and plan — one causes revisions in the other.** A point ICAI illustrations stress: the strategy and plan are *interrelated*, so a change in one may cause a consequential change in the other. If, while executing the plan, a substantive procedure reveals a misstatement suggesting a pervasive control breakdown, the *strategy's* resourcing and timing (send more senior staff, extend the timetable) may need revisiting, which in turn respawns detailed *plan* procedures. The feedback loop in Figure 2.2 runs both ways.

### 4.2 SA 320 — Materiality in Planning and Performing an Audit

**Purpose:** to apply the concept of materiality appropriately in *planning and performing* the audit. (A companion standard, **SA 450 — Evaluation of Misstatements Identified During the Audit**, deals with materiality when *evaluating* the effect of misstatements found and uncorrected. SA 320 is about setting the yardstick; SA 450 is about measuring against it at the end.)

**The concept (rooted in the financial reporting framework):** Misstatements, including omissions, are considered **material** if they, individually or in the aggregate, could reasonably be expected to **influence the economic decisions of users** taken on the basis of the financial statements. Three features of this definition carry all the weight:

1. **It's about users' decisions**, not the auditor's convenience — materiality is judged from the standpoint of a reasonable user relying on the accounts.
2. **Individually or in aggregate** — small errors that sum to a large one are material together even if each is immaterial alone. (This is the seed of performance materiality.)
3. Judgements about materiality are made in light of surrounding circumstances and are affected by the **size and/or nature** of a misstatement — quantitative *and* qualitative.

**Materiality is a matter of professional judgement, framework-dependent.** SA 320 deliberately fixes no formula. Where the applicable financial reporting framework (say, Ind AS or AS) itself defines or discusses materiality, that provides a frame of reference; where it does not, the SA 320 concept above supplies it. The consequence for the exam: never write "materiality equals a fixed percentage" — write "materiality is determined by professional judgement, commonly expressed as a percentage of an appropriate benchmark, and framework-informed."

**Assumptions about users (why we can generalise):** SA 320 lets the auditor assume users:
- have a **reasonable knowledge** of business and accounting and a **willingness to study** the information with reasonable diligence;
- understand that statements are prepared and audited to **levels of materiality** (i.e., not to perfection);
- recognise the **uncertainties** inherent in measuring amounts based on estimates and judgement; and
- make **reasonable economic decisions** on the basis of the statements.

*Why this matters:* it frees the auditor from designing the audit for a hypothetical user who needs every rupee correct. The audit serves the *reasonable, diligent* user — and that is who the threshold is calibrated for.

**The three materiality figures SA 320 requires you to determine:**

**(i) Materiality for the financial statements as a whole ("overall materiality").** Set when establishing the overall strategy. Usually computed as a **percentage applied to a chosen benchmark.**

Choosing the benchmark — the standard lists factors:
- the **elements** of the financial statements (assets, liabilities, equity, revenue, expenses);
- whether there are items on which **users tend to focus** for the particular entity;
- the **nature of the entity**, where it is in its life cycle, and the industry/economic environment;
- the entity's **ownership structure and financing** (e.g., debt-financed entities → users focus on assets and claims rather than earnings); and
- the **relative volatility** of the benchmark.

Common benchmarks and their logic (percentages are indicative ranges used in practice / ICAI illustrations — **confirm current ICAI-quoted figures**, as SA 320 itself does not fix numbers):

| Benchmark | Typical range | When it's the right choice — the logic |
|---|---|---|
| Profit before tax | ~5% | Profit-oriented entity; users (investors) focus on earnings |
| Total revenue / turnover | ~0.5% – 1% | Profit is small, volatile, or near break-even, making PBT an unstable base; or a growth/loss-making company where revenue is what users watch |
| Total assets | ~1% – 2% | Asset-intensive or balance-sheet-driven entity |
| Net assets / equity | ~1% – 5% | Investment entities, funds where net asset value is the headline number |
| Gross profit / total expenses | varies | Not-for-profit or entities where expenditure is the focus |

*Why not always use PBT?* Because if profit is near zero, 5% of it is almost nothing, and you'd set an absurdly tiny materiality that makes the audit un-performable. When the natural benchmark is unstable, switch to a steadier one (often revenue). The benchmark must reflect *what users of this particular entity actually care about* and must be *stable enough to be a reliable yardstick.*

*A refinement examiners like — "normalising" the benchmark.* When the chosen benchmark figure is distorted by a **one-off item** (a large asset-sale gain, an exceptional impairment, a pandemic-year collapse), the auditor may use a *normalised* figure — e.g., PBT **before** the exceptional item, or an average of the last few years' PBT — rather than the raw distorted number. The principle is the same as the volatility factor: the benchmark must represent the entity's *sustainable* performance that users price, not a freak year. Document the normalisation and its reason.

**(ii) Materiality level(s) for particular classes of transactions, account balances or disclosures — where applicable.** Sometimes a misstatement *below* overall materiality would *still* influence users if it hits a **specific sensitive area**. Examples: **related-party transactions**; **directors' remuneration** (a legally sensitive disclosure); a figure that determines compliance with a **loan covenant** or a **regulatory ratio**; the amount at which a company just crosses from loss to profit; and disclosures where users have a **particular sensitivity** (e.g., segment results in a business known for a specific division). For such items you set a *lower, specific* materiality. *Why:* the sensitivity here is **qualitative** — the *nature* of the item, not just its size, makes even a small error decision-relevant.

*Factors that flag the need for a specific (lower) materiality*, per SA 320: whether **law/regulation or the framework** drives users' expectations about a particular item's measurement or disclosure; **key disclosures** relating to the industry in which the entity operates; and whether **attention is focused on a particular aspect** of the business separately disclosed (e.g., a newly acquired business). If none of these apply, you may not need any specific materiality at all — it is set "where applicable," not always.

**(iii) Performance materiality.** Defined as an amount (or amounts) set at *less than* materiality for the financial statements as a whole (and less than any specific materiality for particular areas) to **reduce to an appropriately low level the probability that the aggregate of uncorrected and undetected misstatements exceeds materiality** for the statements as a whole.

Break that definition into its two jobs:
- **Aggregation cushion:** many individually-immaterial misstatements can add up past overall materiality; working to a lower number means you catch and consider more of them.
- **Undetected-error cushion:** you sample; the untested population may contain errors you never saw. The gap between performance materiality and overall materiality is the room left for those.

In practice, performance materiality is often set at **50%–75% of overall materiality** (some firms use down to ~50% for higher-risk engagements, up to ~75% for lower-risk). *The higher the risk / the more misstatements you expect, the LOWER you push performance materiality* — a bigger cushion for a riskier audit. **Confirm the specific percentages in current ICAI material**; SA 320 fixes the *principle*, not the number.

*What determines where in the 50–75% band you land?* The auditor's judgement, informed by: (i) his **understanding of the entity**, updated during risk assessment; (ii) the **nature and extent of misstatements identified in prior audits** — a history of many errors argues for a lower percentage; and (iii) his resulting **expectation of misstatements in the current period**. This is why performance materiality is not a mechanical "always 75%" — it is calibrated to how error-prone this specific entity has proven to be.

*A trap-laden subtlety — one overall materiality can spawn several performance materialities.* Performance materiality can be set at a **lower level for a particular class or balance** than the general performance materiality, if that area is expected to contain more misstatements. So do not assume a single performance-materiality number for the whole audit; a high-error area (say, manual journal-heavy accruals) can carry its own tighter performance materiality even below the general one.

*Figure 2.3 — Why performance materiality sits below overall materiality: it reserves headroom for undetected and aggregated errors.*

```mermaid
flowchart TD
    A["Overall materiality the line above which users are misled"] --> B["Reserve headroom for two dangers"]
    B --> C["Undetected errors sampling never tested everything"]
    B --> D["Aggregation many small errors summing up"]
    C --> E["Set PERFORMANCE MATERIALITY below overall materiality"]
    D --> E
    E --> F["Work and test to this lower number"]
    F --> G["Even after adding back undetected plus uncorrected errors total stays under overall materiality"]
```

**A fourth threshold you must not forget — the "clearly trivial" level.** Below performance materiality sits an even smaller amount: the threshold below which misstatements are **clearly trivial** and need not be accumulated (this belongs to SA 450 but is set during planning and examined alongside SA 320). "Clearly trivial" is *not* a synonym for "not material" — it is a much lower bar, meaning amounts so small that, even summed, they could not conceivably matter, whether taken individually, in aggregate, or judged by size or nature. Misstatements above "clearly trivial" but below materiality **must still be accumulated** and evaluated at completion; only those below "clearly trivial" can be ignored. Confusing "clearly trivial" with "immaterial" is a classic error — there is a whole zone between them that must be tracked.

*The full ladder, from largest to smallest:* **Overall materiality** (users misled above this) > **Performance materiality** (working buffer) > **Clearly-trivial threshold** (below which not even accumulated). Specific materiality, where it exists, is a *parallel, lower* line for a sensitive area, with its own performance materiality beneath it.

*Figure 2.4 — The materiality ladder: four thresholds, from the line that misleads users down to the amount too small to bother tracking.*

```mermaid
flowchart TD
    A["Overall materiality for the FS as a whole"] --> B["Specific materiality for sensitive areas set LOWER where applicable"]
    A --> C["Performance materiality set BELOW overall as a buffer"]
    B --> D["Specific performance materiality below the specific level"]
    C --> E["Clearly trivial threshold set well below performance materiality"]
    D --> E
    E --> F["Below this misstatements need not even be accumulated"]
    C --> G["Between clearly trivial and materiality all misstatements are accumulated and evaluated"]
```

**Materiality and audit risk are inversely related — a crucial linkage.** The *lower* you set materiality, the *more* misstatements become "material," so the *more* evidence you must gather to be confident none exceed it — hence *more* work, driving detection risk down. Materiality is therefore not just a reporting threshold; it is a **dial that directly sets how much audit work you do.** Set it too high and you might miss decision-relevant errors; set it too low and you drown in un-performable work. (This connects to the audit risk model — Chapter 3.)

**Revision as the audit progresses (SA 320 requirement):** The auditor shall **revise** materiality (and, if applicable, specific and performance materiality) if he becomes aware of information during the audit that would have caused a *different* initial determination — e.g., actual results diverge sharply from the estimates used to set materiality (you used *projected* profit of ₹20 crore; actuals come in at ₹8 crore), a **decision to dispose of a major part** of the business, or a **change in the auditor's understanding** of the entity and its operations. *Why:* materiality set on stale numbers is a yardstick made of rubber. And if revised *downward*, the auditor must reconsider whether performance materiality is still appropriate and whether the **nature, timing and extent of further procedures** remain adequate — often meaning *more* work. Note the asymmetry: a downward revision is the dangerous one, because procedures already completed to a *higher* threshold may now be insufficient and may have to be **extended or repeated**.

**Documentation (SA 320 requirement):** the auditor shall document the amounts and the *factors considered* in their determination:
- materiality for the financial statements as a whole;
- materiality level(s) for particular classes/balances/disclosures, if applicable;
- performance materiality; and
- any **revision** of the above as the audit progressed.

*Why record the factors, not just the numbers?* Because the number is a conclusion; the *factors* are the reasoning. A reviewer must be able to see *why* PBT was chosen over revenue and *why* 5% and not 3% — otherwise the figure is an unaccountable guess.

### 4.3 How Materiality Directs Effort — Tying It Back to Assertions

Materiality doesn't float above the audit; it lands on **specific assertions** in **specific accounts**. Recall the assertions (SA 315) that management implicitly makes about the numbers:

| Category | Assertion | Plain meaning |
|---|---|---|
| Transactions/events | Occurrence | It really happened and pertains to the entity |
| | Completeness | Nothing that should be recorded is left out |
| | Accuracy | Amounts recorded correctly |
| | Cut-off | Recorded in the correct period |
| | Classification | Recorded in the right accounts |
| Account balances | Existence | The asset/liability really exists |
| | Rights and obligations | The entity owns it / owes it |
| | Completeness | All balances recorded |
| | Valuation and allocation | Recorded at an appropriate value |
| Presentation/disclosure | Occurrence, completeness, classification, accuracy, valuation | Disclosed events happened, all needed disclosures made, clearly and correctly |

Planning uses materiality **plus** the risk to each assertion to decide *where and how much* to test. For **revenue**, the risky assertions are usually **occurrence** (fictitious sales inflating revenue) and **cut-off** (sales of next year pulled into this year). For **inventory**, it's **existence** and **valuation** (does it exist, and is it worth what's stated after obsolescence?). For **liabilities and provisions**, it's **completeness** (the temptation is to *hide* liabilities, so you hunt for the *unrecorded* ones). Naming the assertion at risk is what turns "audit revenue" into a targeted procedure — you design the test to attack the specific lie management would be tempted to tell.

*The directional-testing principle, made explicit.* For **overstatement-prone** items (assets and income — management's incentive is to inflate the balance sheet and profit), you test **from the recorded figure to supporting evidence** (does this recorded sale/asset really exist and belong here?). For **understatement-prone** items (liabilities and expenses — the incentive is to hide them), you test **from independent sources back to the records** (search for unrecorded liabilities: subsequent payments, unmatched supplier statements, post-year-end invoices). Materiality tells you the size worth chasing; the *direction* of the likely lie tells you which way to point the test. This pairing is the operational essence of "large and risky."

---

## 5. Applied Scenarios — Reasoning to the Audit Response

**Scenario 1 — The break-even benchmark trap.**
*Facts:* GreenGro Ltd, an agri-inputs company, had PBT of ₹18 crore last year but this year, after a bad monsoon, expects PBT of only ₹40 lakh on turnover of ₹520 crore. The junior proposes materiality of 5% of PBT = ₹2 lakh.

*Reasoning:* ₹2 lakh materiality on a ₹520 crore business is absurd — nearly every account would be "material," the audit becomes un-performable, and the tiny threshold reflects a one-off profit dip, not what users care about. PBT here is **volatile and near break-even**, disqualifying it as a stable benchmark. Switch to a steadier base users would focus on for a company in a rough patch — **revenue**. At, say, 0.75% of ₹520 crore, overall materiality ≈ ₹3.9 crore, a sensible yardstick. Document *why* the benchmark was changed. *Lesson:* the benchmark must be stable and user-relevant; a collapsing PBT triggers a switch, usually to revenue.

**Scenario 2 — The qualitatively material small number.**
*Facts:* For MetroBuild Ltd, overall materiality is ₹1.2 crore. The auditor finds directors' remuneration is overstated by ₹9 lakh, and separately a related-party loan of ₹15 lakh to a director's firm is undisclosed. Both are far below ₹1.2 crore. The manager says "immaterial, ignore."

*Reasoning:* Wrong. **Nature can make a small amount material.** Directors' remuneration and related-party transactions are legally and governance-sensitive disclosures (also tied to Companies Act requirements); a misstatement here can influence users' judgement about stewardship and conflicts regardless of size. These call for a **specific (lower) materiality** under SA 320, and the misstatements should be evaluated as **qualitatively material**. The auditor should seek correction/disclosure and, if refused, consider the impact on the opinion. *Lesson:* materiality is size **and/or** nature — sensitive disclosures pierce the quantitative threshold.

**Scenario 3 — Mid-audit surprise forces revision.**
*Facts:* At planning, PixelSoft Ltd was budgeted to earn ₹30 crore PBT; materiality was set at 5% = ₹1.5 crore, performance materiality at 75% = ₹1.125 crore (low-risk assessment). During fieldwork, a major customer goes insolvent; actual PBT will be ₹9 crore, and the auditor now suspects aggressive revenue recognition.

*Reasoning:* Two things changed — the **benchmark magnitude** (actual profit far below projection) and the **risk** (fraud risk in revenue is now higher). SA 320 requires **revising overall materiality downward** to reflect real PBT (5% of ₹9 crore = ₹45 lakh). Because materiality dropped and risk rose, **performance materiality must be pushed lower** (toward 50% given higher risk), and the auditor must reconsider whether the planned **nature, timing and extent** of procedures on revenue are still sufficient — almost certainly expanding substantive testing and adding cut-off and occurrence procedures. Every change and its reason goes into the documentation. *Lesson:* materiality is a live figure; divergence of actuals from estimates and emerging risk both force revision, and revision cascades into more work.

**Scenario 4 — The evenly-thick file.**
*Facts:* A reviewer opens the audit file of a manufacturing client and finds roughly equal working-paper volume on share capital (unchanged for six years), petty cash, revenue, and inventory valuation.

*Reasoning:* This is a **planning failure**, not thoroughness. Share capital and petty cash are low-risk, low-impact; revenue (occurrence/cut-off) and inventory valuation (obsolescence) are high-risk, high-value. A properly planned audit under SA 300, driven by materiality and risk, would be **lopsided** toward revenue and inventory. Equal effort everywhere means senior attention was *not* directed to where misstatement is both likely and large. *Lesson:* the shape of the file should mirror the map of risk × materiality; uniform effort is a red flag.

**Scenario 5 — The full numerical build, benchmark to clearly-trivial (exam-hard, self-checked).**
*Facts:* Nimbus Foods Ltd, a stable, profitable FMCG company. Latest figures: Revenue ₹1,200 crore, PBT ₹96 crore, Total assets ₹640 crore, Equity ₹300 crore. Prior audits found few, small misstatements; risk assessed as low-to-moderate. Directors' remuneration ₹6 crore is a sensitive disclosure. Determine overall materiality, specific materiality for directors' remuneration, performance materiality, and the clearly-trivial threshold, and state the total misstatement the audit is designed to keep the accounts within.

*Reasoning and computation:*
- **Benchmark choice:** PBT is stable and the entity is profit-focused → use **PBT at 5%**. Overall materiality = 5% × ₹96 crore = **₹4.8 crore**.
- *Cross-check against other benchmarks for sanity:* 0.5% of revenue = ₹6 crore; 1% of total assets = ₹6.4 crore; both are in the same order of magnitude as ₹4.8 crore, confirming PBT-5% is not producing an absurd figure. (Had PBT-5% come to, say, ₹5 lakh while revenue-0.5% was ₹6 crore, that mismatch would itself signal PBT is the wrong, unstable benchmark — the check *is* the diagnosis.)
- **Specific materiality (directors' remuneration):** a legally sensitive disclosure; set a *lower* level, say ₹25 lakh, reflecting that users would react to even a modest misstatement here. (Any defensible low figure works; the *reasoning* — nature-driven sensitivity — is what earns marks.)
- **Performance materiality:** low-to-moderate risk and a clean prior history → toward the **higher** end of the band, say **75%**. PM = 75% × ₹4.8 crore = **₹3.6 crore**.
- **Clearly-trivial threshold:** commonly a small fraction of overall materiality (practice often uses roughly 5%). ~5% × ₹4.8 crore = **₹24 lakh** — below this, misstatements need not even be accumulated. (**Confirm the percentage convention in current ICAI material**; SA fixes no number.)

*Self-verification — does the ladder hold?* Clearly-trivial ₹24 lakh < performance materiality ₹3.6 crore < overall materiality ₹4.8 crore. ✓ Ordering correct. Specific materiality ₹25 lakh sits *below* overall materiality as required for a sensitive area. ✓ The audit is designed so that the **aggregate of uncorrected plus undetected misstatements stays below ₹4.8 crore**; by working to ₹3.6 crore, the ₹1.2 crore gap is the reserved headroom for aggregation and sampling error. *Lesson:* build the ladder top-down (overall → performance → clearly trivial), carve specific materiality sideways for sensitive items, and always sanity-check the chosen benchmark against one or two alternatives.

**Scenario 6 — Revenue vs assets: same profit, opposite benchmark (what-if the examiner tweaks the entity).**
*Facts:* Two companies, identical PBT of ₹10 crore.
(A) **LendWell Finance Ltd** — an NBFC financed heavily by debentures and public deposits; total assets ₹2,000 crore, thin equity.
(B) **BrightApp Ltd** — an asset-light SaaS firm; total assets ₹120 crore, no debt, valued by the market on earnings growth.
Which benchmark for each?

*Reasoning:* Same profit, but users differ. For **LendWell**, the dominant users are **lenders and depositors** who care about **solvency and asset cover**, and the entity is **balance-sheet-driven**; the natural benchmark is **total assets** (or net assets), say 1% of ₹2,000 crore = **₹20 crore** — far above 5% of PBT (₹50 lakh). Using PBT here would set an implausibly tight threshold for a ₹2,000 crore balance sheet and ignore what its actual users watch. For **BrightApp**, users are **equity investors pricing earnings**; **PBT at 5%** = **₹50 lakh** is right, and total assets would be a poor benchmark because the assets are trivial relative to the value drivers. *Self-check:* the benchmark tracks *ownership structure and financing* and *what users focus on* — exactly the SA 320 factors — and the two answers diverge by 40× despite identical profit. *Lesson:* never reflex to "5% of PBT." First ask *who uses these accounts and what do they watch*; the financing structure often decides the benchmark.

**Scenario 7 — Aggregation of individually-immaterial errors (why performance materiality exists, in numbers).**
*Facts:* Overall materiality for Coastal Traders Ltd is ₹1 crore; performance materiality was set at ₹700 lakh. At completion the auditor has accumulated the following *uncorrected* misstatements, each individually below overall materiality: overstated inventory ₹35 lakh, understated warranty provision ₹28 lakh, unrecorded supplier invoice ₹22 lakh, revenue recognised early ₹40 lakh, and misclassified (non-P&L) ₹15 lakh. Management refuses to adjust, arguing "each one is immaterial."

*Reasoning:* Evaluate under SA 450 against SA 320 materiality — but note *classification-only* errors don't affect the profit/net-asset aggregate the same way. Aggregate the ones affecting profit and net position: 35 + 28 + 22 + 40 = **₹125 lakh**. This **exceeds overall materiality of ₹100 lakh**, so the accounts are **materially misstated in aggregate** even though every component is individually immaterial. Management's argument is precisely the fallacy performance materiality guards against. *Self-check:* had the auditor complacently worked to ₹1 crore instead of ₹700 lakh, he might have stopped accumulating small items and never revealed the ₹125 lakh pile-up; the ₹70 lakh cushion (gap between PM and materiality) is what forced enough small items into view. The ₹15 lakh misclassification is separately evaluated for *qualitative* impact (does it distort a key ratio or covenant?) but is not simply added to the profit-effect total. *Outcome:* seek correction; if refused, the effect on the audit opinion must be considered (likely a **qualified opinion**). *Lesson:* "each is immaterial" is never a defence — aggregate first, then judge; and mind that classification errors are assessed on their own footing.

---

## 6. Procedure / Documentation Summary

**The planning workflow, start to finish:**

1. **Preliminary engagement activities** — client continuance; ethics and independence evaluation; confirm/agree engagement terms (engagement letter, SA 210).
2. **Obtain/update understanding of the entity and its environment** (SA 315) sufficient to identify risk areas — feeds both strategy and materiality.
3. **Set overall materiality** — choose benchmark, justify the percentage, compute; document benchmark rationale (and any normalisation).
4. **Set specific materiality** for sensitive classes/balances/disclosures where a smaller misstatement would influence users; document.
5. **Set performance materiality** below overall (and below specific) materiality, calibrated to expected risk and prior-year error history; document the percentage logic. Set the **clearly-trivial threshold** for accumulation of misstatements.
6. **Establish the overall audit strategy** — scope, timing, direction, resources.
7. **Develop the detailed audit plan** — planned risk-assessment procedures (SA 315) and planned further procedures at assertion level (SA 330), plus other required procedures.
8. **Plan direction, supervision and review** proportionate to risk and staff competence.
9. **Execute, monitoring continuously**; when new information or changed risk appears, **update strategy/plan and revise materiality**, documenting the change and the reason.
10. **At/near completion**, use SA 450 to evaluate whether uncorrected misstatements, individually or in aggregate, exceed materiality.

**What must be in the file:**

| Document | Source SA | Must record |
|---|---|---|
| Overall audit strategy | SA 300 | Scope, timing, direction, resources |
| Audit plan | SA 300 | Nature/timing/extent of risk-assessment and further procedures |
| Significant changes to strategy/plan | SA 300 | The change **and the reasons** for it |
| Materiality determinations | SA 320 | Overall materiality; specific materiality (if any); performance materiality; **and the factors considered** |
| Clearly-trivial threshold | SA 450 (set in planning) | The amount below which misstatements are not accumulated |
| Revision of materiality | SA 320 | Revised amounts and reasons; reconsideration of further procedures |

---

## 7. Connections

- **Chapter 1 (Nature & objective of audit):** planning and materiality are the operational answer to *reasonable* assurance and *material* misstatement — the qualifiers baked into the audit's objective. The three inherent limitations (framework, procedures, time/cost) are *why* reasonable assurance is the ceiling and *why* we plan.
- **SA 315 (Identifying and assessing risks):** supplies the *risk map* that planning aims at; you cannot direct effort without first understanding the entity and its risks. Planning and risk assessment are inseparable.
- **SA 330 (Auditor's responses to assessed risks):** the audit plan's "further procedures" are literally SA 330 responses; higher assessed risk → more persuasive, more extensive procedures, decided through the nature-timing-extent triad.
- **Audit risk model (AR = IR × CR × DR):** materiality and detection risk are inversely linked; setting materiality is one lever, evidence quantity is the other. Explored fully in Chapter 3.
- **SA 450 (Evaluating misstatements):** the back-end partner of SA 320 — you set the yardstick (and the clearly-trivial threshold) in planning and measure found misstatements against it at completion; aggregation is judged here.
- **SA 220 / SQC 1 (Quality control):** direction, supervision and review planned under SA 300 are quality-control mechanisms; competent staffing is both a planning and a quality decision.
- **SA 210 (Engagement terms) and client acceptance:** the preliminary activities that gate the whole planning process.
- **SA 510 (Opening balances):** the initial-audit add-on — first-year planning must cover opening balances and predecessor-auditor arrangements.
- **Companies Act 2013:** materiality interacts with statutory disclosures — e.g., director's remuneration (Sec 197), related-party transactions (Sec 188), and CARO reporting — where *nature* makes small amounts material; also the auditor's Sec 143 duties presuppose a properly planned audit.

---

## 8. Traps & Examiner Tricks

1. **"Materiality is a fixed rule / a single percentage."** *False.* SA 320 fixes no numbers; it's a matter of **professional judgement** using benchmarks. Any answer quoting "materiality = 5% always" loses marks. Say the number is *judgement-based* and *entity-specific.*
2. **Forgetting the qualitative dimension.** Examiners love a *small* amount in a *sensitive* area (director's pay, related parties, an amount that flips loss to profit, a covenant breach). The trap answer says "immaterial — ignore." The right answer invokes **nature-based materiality** and specific materiality.
3. **Confusing overall vs performance vs specific materiality.** Overall = the top-line threshold for the statements; **performance = a lower working figure** to buffer aggregation and undetected error; **specific = a lower figure for particular sensitive areas.** Mixing these up is a classic slip. Performance materiality is always **below** overall.
4. **Getting the risk–materiality direction backwards.** Higher risk → **lower** performance materiality (bigger cushion), and lower materiality → **more** audit work. Some students write the inverse. Reason it: more risk means more room needed for undetected error, so tighten the working threshold.
5. **Treating planning as a one-time event.** SA 300 stresses planning is **continuous and iterative**; the plan is revisited and revised. "Plan once at the start and never touch it" is wrong.
6. **Strategy vs plan mix-up.** Strategy = scope/timing/direction/resources (the map). Plan = detailed procedures (the route). If a question asks for contents of the *strategy*, do not list audit procedures; if it asks for the *plan*, do not list resource/timing decisions.
7. **Forgetting to revise materiality when actuals diverge.** If the exam gives you a *projected* profit at planning and *actual* profit later that's very different, the examiner is testing whether you know SA 320 **requires revision** — and that downward revision triggers reconsideration of procedures already performed to a higher threshold.
8. **Omitting documentation.** Every planning and materiality decision — including **the reasons/factors** and any **changes** — must be documented. Answers that stop at "the auditor decides X" without "and documents it" leave marks on the table.
9. **Thinking planning means all work is done before fieldwork.** No — planning is *not* a discrete phase that finishes before evidence-gathering; it continues throughout, and *some* substantive procedures may even begin during planning.
10. **"Planning is only for large/complex audits."** Scale of planning varies with the entity's size and complexity, but *every* audit is planned. A small audit needs less, not zero.
11. **Confusing "clearly trivial" with "immaterial."** They are different bars. "Clearly trivial" is *far* below materiality — the accumulation cut-off. Misstatements above clearly-trivial but below materiality **must still be accumulated** and evaluated. Writing "below materiality, so ignore" skips the whole middle zone and is wrong.
12. **Assuming one performance materiality for the whole audit.** A high-error class or balance can carry its *own* lower performance materiality. Blanket single-figure answers miss this refinement.
13. **Confusing audit plan with audit programme.** The audit **programme** is the detailed list of procedures (part of the plan) that assistants execute and initial. If asked to distinguish them, don't treat them as identical — the plan is broader; the programme is the operational checklist.
14. **Reflexively using 5% of PBT for every entity.** For debt-financed / asset-heavy / loss-making / investment entities the right benchmark may be total assets, revenue or net assets. Always justify the benchmark from *who the users are and what they watch* (Scenario 6).
15. **Thinking management sets or is told the exact materiality.** Materiality is the **auditor's** planning judgement, kept in the audit file — not disclosed in the financial statements and not negotiated with the client.
16. **Ignoring the benchmark sanity-check.** A robust answer cross-checks the chosen benchmark against an alternative; a wildly different result flags that the primary benchmark may be unstable (Scenario 5).

---

## 9. First-Principles Recap

Strip everything away and here is the skeleton:

- You **cannot** check everything (scarcity), and you **shouldn't** (relevance). So you must aim. And because of three permanent limitations (estimates in reporting, persuasive-not-conclusive evidence, finite time/cost) the best you can honestly offer is **reasonable, not absolute, assurance**.
- To aim, you need to know **what size of error matters** (materiality — set by users' decisions, anchored to a stable, entity-relevant benchmark) and **where errors hide** (risk — from understanding the entity and its assertions).
- Point effort at the **intersection of large and risky.** That is planning.
- Because errors **aggregate** and because you only **sample**, work to a threshold **below** the one that matters — that safety margin is **performance materiality.** Below even that lies the **clearly-trivial** line, under which you don't bother accumulating.
- Because *nature* can make a *small* error decision-relevant, carve out **specific materiality** for sensitive areas.
- Because facts change, treat both the plan and the materiality figures as **living**, revising and documenting as you learn.
- **SA 300** is the machinery (strategy then plan, continuously updated, documented). **SA 320** is the threshold (overall, specific, performance, revised, documented). **SA 315** draws the risk map they aim at; **SA 330** is the response; **SA 450** measures what you found against the yardstick.

Every rule in this chapter is a defence against one failure: **signing a clean opinion on statements that were, in a way that would have changed a user's decision, wrong.**

---

## 10. Quick-Revision Sheet

**Key Standards**

| SA | Title | One-line purpose |
|---|---|---|
| SA 300 | Planning an Audit of Financial Statements | Build overall strategy + detailed plan so effort hits important areas; document both and any changes |
| SA 320 | Materiality in Planning and Performing an Audit | Set overall, specific and performance materiality by judgement; revise as needed; document amounts and factors |
| SA 450 | Evaluation of Misstatements Identified During the Audit | (Back-end) accumulate above clearly-trivial; measure found misstatements against materiality |
| SA 315 | Identifying and Assessing the Risks of Material Misstatement | Supplies the risk map planning aims at |
| SA 330 | The Auditor's Responses to Assessed Risks | The "further procedures" the plan schedules, via nature-timing-extent |
| SA 510 | Initial Audit Engagements — Opening Balances | Extra first-year planning: opening balances + predecessor auditor |

**SA 300 — Overall Strategy sets four things**

| Element | Question answered |
|---|---|
| Scope | What/where are we auditing (framework, components, locations) |
| Timing | When — deadlines, interim vs final, reporting to TCWG |
| Direction | Materiality + preliminary risk areas that focus effort |
| Resources | Who (team size, skill), how much (budget), when deployed |

**SA 300 — Audit Plan details three things:** planned risk-assessment procedures (SA 315); planned further procedures at assertion level (SA 330 — tests of controls + substantive); other required procedures. *Plan direction/supervision/review too.* The **audit programme** is the detailed procedure-list within the plan.

**NTE triad (used everywhere):** **Nature** = what kind of procedure / test-of-controls vs substantive; **Timing** = interim vs year-end; **Extent** = sample size / coverage. Higher risk → more reliable nature, timing nearer year-end, larger extent.

**Preliminary engagement activities (before planning):** client continuance; ethics + independence; engagement terms (SA 210). Run **every year**, not just year one.

**SA 320 — Three materiality figures (plus a fourth threshold)**

| Figure | What | Why |
|---|---|---|
| Overall materiality | % × benchmark for FS as a whole | Threshold above which users are misled |
| Specific materiality | Lower figure for sensitive classes/balances/disclosures | *Nature* makes small errors decision-relevant |
| Performance materiality | Below overall (often ~50–75%) | Cushion for aggregation + undetected (sampling) error |
| Clearly-trivial threshold | Well below performance materiality | Below this, misstatements not even accumulated (SA 450) |

**The ladder:** Overall > Performance > Clearly-trivial; Specific runs as a lower parallel line for sensitive areas (with its own PM).

**Benchmarks:** PBT ~5% (profit-focused); Revenue ~0.5–1% (volatile/near-break-even/loss-making); Total assets ~1–2% (asset-heavy / lenders' focus); Net assets ~1–5% (funds). *Confirm exact ICAI-quoted percentages; SA 320 fixes no numbers.* **Normalise** a benchmark distorted by a one-off item. Always **sanity-check** against one alternative benchmark.

**Key relationships:**
- Materiality ↓ ⇒ audit work ↑ (inverse).
- Risk ↑ ⇒ performance materiality ↓ (bigger cushion).
- Materiality = **size AND/OR nature** (quantitative + qualitative).
- Benchmark follows **who the users are and what they watch** (financing/ownership structure often decides it).

**Revise materiality when** actuals diverge from planning estimates, a major part of the business is disposed, or understanding of the entity changes; **downward** revision ⇒ reconsider nature/timing/extent — procedures already done to a higher threshold may need extending.

**Documentation checklist:** overall strategy; audit plan; significant changes + reasons; overall/specific/performance materiality + **factors**; clearly-trivial threshold; materiality revisions.

**The one sentence:** *Because you can't check everything and not everything matters, plan your scarce effort onto amounts that are both large (materiality) and likely wrong (risk), work to a buffer below what matters (performance materiality), carve lower thresholds for sensitive items, and keep both the plan and the threshold alive and documented.*
