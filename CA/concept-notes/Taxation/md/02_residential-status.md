# Chapter 02 — Residential Status & Scope of Total Income

> **Rates & limits change every year.** This chapter teaches the *structure and logic* of residence and the scope of income — which almost never changes. The day-count numbers (182, 60, 365, 730) and the ₹15 lakh threshold are stable but **always verify the exact figures, provisos, and the applicable Assessment Year against current ICAI study material before your attempt.**

---

## 1. The Problem — Who does a country get to tax, and on what?

Imagine you are the Government of India designing an income-tax. You immediately hit a boundary question that comes *before* any rate, any head of income, any deduction:

**Whose income can I legitimately tax, and how much of it — only the income that arose inside my borders, or their worldwide income?**

This is not a trivia question. Consider four people, all earning income in the same year:

- **A** — born, lives, works, and earns entirely in Mumbai.
- **B** — an Indian citizen who took a job in Dubai on 1 April and will live there for years, but still earns rent from a flat in Pune.
- **C** — a British consultant who flew into India for a 3-week project, earned a fee here, and flew home.
- **D** — a returning NRI who came back to India permanently after 20 years abroad and still has a US bank account earning interest.

If India taxes **worldwide income of everyone physically present**, then C — here for 3 weeks — would have to disclose and pay Indian tax on his UK salary, his UK house, his UK dividends. That is absurd and unenforceable; no country would accept it, and no professional would ever visit India. If instead India taxes **only income arising in India, for everyone**, then B could shift his entire economic life offshore, keep deep roots in India, and pay India almost nothing — a giant leak.

So a flat rule fails at both ends. The tax base must depend on **how strongly a person is connected to India** — and that connection must be measured by something *objective, verifiable, and hard to game*, not by a subjective "does he feel Indian?" test.

That measuring device is **residential status**. It is the gatekeeper of the entire Income-tax Act: before you can compute a single rupee of tax, you must know *which basket of income is even taxable* — and that depends on residence, not on citizenship, not on domicile, not on where the person banks.

---

## 2. The Core Idea — Tax follows *economic allegiance* (nexus), measured by presence

The organising principle behind residence is called **economic allegiance** or, in modern terms, **nexus**: a country may tax income to the extent a person *benefits from and is connected to* that country's economy, infrastructure, legal protection, and markets.

There are two natural nexuses:

| Nexus | Question it asks | Who it should catch |
|---|---|---|
| **Source nexus** | Did the income *arise here*? | Everyone, regardless of where they live — India built the road, the market, the court that made the income possible. |
| **Residence nexus** | Does the person *live here* / have their economic home here? | Residents — India provides them ongoing protection and services, so it can reach their *global* income. |

India's design decision, embodied in **Section 5**, is:

- **Everyone** pays tax on **India-source income** (source nexus is universal — you can't escape it by living abroad).
- **Residents additionally** pay tax on **foreign income** (residence nexus is the "extra reach" that only applies once you're economically anchored here).

The crucial insight your notes should burn in:

> **Residential status does NOT decide the *rate* of tax. It decides the *SCOPE* — the size of the net, i.e. *which* income falls into the taxable basket.** Two people with identical incomes but different residential statuses can owe very different tax, purely because one basket includes foreign income and the other doesn't.

And how do we *measure* residence objectively? Not by intention (unprovable), not by citizenship (a person can be a citizen yet live abroad for decades). We measure it by **physical presence in India, counted in days.** Days are on the passport, on immigration records, on flight tickets — hard to fake, easy to verify. That is *why* the whole test is a day-count test.

---

## 3. Why it's built this way — the logic behind every design choice

Before the sections, understand the five design decisions. Once these click, the rules feel inevitable rather than arbitrary.

**(a) Why citizenship is irrelevant.** Citizenship is a legal/political bond; income tax is about *economic* connection. A US citizen running a factory in India for 5 years is economically Indian; an Indian citizen who has settled in Canada is not. Taxing by citizenship would tax the wrong people. (The USA is a rare exception that taxes citizens worldwide — India deliberately does not.)

**(b) Why days, not intention.** Intention ("I meant to leave permanently") is unverifiable and manipulable. Days present are objective. So residence = a function of *days in India during the previous year* (and, for one category, prior years too).

**(c) Why there are TWO layers of conditions (basic + additional).** A simple resident/non-resident split is too blunt. Consider the returning NRI (D above): the day he lands permanently, he becomes a resident — but is it *fair* to instantly tax his foreign pension, foreign interest, foreign business built up over 20 years, the moment he steps off the plane? He hasn't re-integrated yet; taxing his global income immediately would punish return and encourage people to stay away. So India inserts a **middle, transitional category** — *Resident but Not Ordinarily Resident (RNOR)* — a soft-landing status. To sort people into ROR / RNOR / NR you need a *second* test measuring **depth and continuity** of connection, not just presence this year. Hence **additional conditions**.

**(d) Why 182 / 60 / 365 days.** These thresholds encode "roughly half the year, OR here-this-year-plus-substantial-recent-history." 182 ≈ half of 365 (majority of the year → clearly resident). The 60-days-this-year *plus* 365-days-in-4-prior-years combination catches someone who spends part of every year in India — no single year hits 182, but the *pattern* shows a real, recurring connection. The **relaxations** to 60→182 exist to *not punish* Indians who leave for employment or come home to visit.

**(e) Why RNOR is a shield only for *foreign* income.** RNOR still lives in India this year, so India's *source* nexus is full — all Indian income is taxed. What RNOR shields is *foreign* income (except foreign income from a business *controlled from* India). The logic: give the returnee time to repatriate/settle before the global net closes on him.

```mermaid
flowchart TD
    A["Design goal - tax by economic connection not citizenship"] --> B["Measure connection objectively - count days in India"]
    B --> C["Layer 1 basic conditions - are you a Resident this year"]
    C -->|No| D["Non-Resident - India-source income only"]
    C -->|Yes| E["Layer 2 additional conditions - how deep is the connection"]
    E -->|Deep and continuous| F["ROR - worldwide income taxed"]
    E -->|Shallow or recently returned| G["RNOR - India income plus foreign income from India-controlled business only"]
```
*Figure 1 — The policy logic: two layers of tests sort people into three baskets of scope.*

---

## 4. Full Technical Content — sections, definitions, tests, and their "why"

### 4.1 The statutory map

| Section | Deals with | One-line "why" |
|---|---|---|
| **Sec 6** | *How* residential status is determined (individuals, HUF, firm, company) | The measuring device (day-count / control tests) |
| **Sec 5** | *Scope* of total income for each status | The gatekeeper — which income basket is taxable |
| **Sec 7** | Income *deemed to be received* in India | Plug a timing/location loophole |
| **Sec 9** | Income *deemed to accrue or arise* in India | Plug a "where did it arise?" loophole |

**Memory hook:** *"6 decides WHO you are; 5 decides WHAT is caught; 7 & 9 stop you from arguing your way out."*

### 4.2 Residential status of an INDIVIDUAL — Section 6(1)

Everything starts with **Previous Year (PY)** presence. (Recall Ch.1: PY = the year income is earned; AY = the following year it is taxed.) You test residence *for each PY separately* — a person can be resident one year, NR the next.

#### Step 1 — Basic Conditions [Sec 6(1)]: Are you a RESIDENT at all?

An individual is **Resident** in India for a PY if he satisfies **at least ONE** of these:

- **(a)** In India for **≥ 182 days** during the PY; **OR**
- **(b)** In India for **≥ 60 days** during the PY **AND ≥ 365 days** during the **4 years immediately preceding** the PY.

If he satisfies **neither**, he is a **Non-Resident (NR)**.

> **Why "at least one"?** Either you're here most of the year (182), or you're here a chunk this year *and* have a clear recent pattern of coming (60 + 365). Both signal a real connection.

**Memory hook for the numbers:** *"182 = half a year. 60-this-year + 365-over-4-years = a habit, not a visit."*

#### The relaxations to condition (b) — 60 days becomes 182 days [Explanation 1 to Sec 6(1)]

Condition (b)'s 60-day trigger is *harsh* for two sympathetic groups. So the law **replaces 60 with 182** (i.e. only condition (a) can make them resident) in these cases:

1. **An Indian citizen who leaves India during the PY for the purpose of employment outside India** (or as a member of the crew of an Indian ship). — *Why:* We should not tax the global salary of Indians going abroad to work merely because they were physically here for the first two months before departing. Punishing labour export makes no policy sense.

2. **An Indian citizen or Person of Indian Origin (PIO)** who, being outside India, **comes on a visit to India** during the PY. — *Why:* NRIs visiting family should not risk becoming residents (and exposing worldwide income) just for a long holiday.

> **PIO definition (remember it):** A person is of Indian origin if **he, or either of his parents, or any of his grandparents, was born in undivided India** (i.e. India as it existed before Partition — includes present-day Pakistan and Bangladesh territory). *Why grandparents?* To keep the diaspora connection meaningful across generations without being infinite.

#### The high-income NRI carve-back — the ₹15 lakh rule [Explanation 1(b) proviso & Sec 6(1A)]

A modern anti-abuse layer. Wealthy Indians were arranging their days to be resident *nowhere* ("stateless" for tax) and paying tax in no country. Two responses:

- **Modified visit relaxation:** For the PIO/citizen *visiting* India whose **total income (other than foreign-source income) exceeds ₹15,00,000** in the PY, the 60-day limit is relaxed only to **120 days** (not 182). So a high-earning visitor who stays 120+ days can become resident. *Why:* the relaxation was meant to protect ordinary NRIs, not high-income individuals gaming presence.

- **Deemed resident [Sec 6(1A)]:** An **Indian citizen** with **total income (other than foreign source) > ₹15,00,000** who is **not liable to tax in any other country** by reason of domicile/residence → **deemed to be resident in India** regardless of days. *Why:* to end "stateless" tax residency for high-income Indian citizens. Such a person is always classified **RNOR** (see below) — India gets its source income but doesn't overreach on genuine foreign income.

> **Verify:** the ₹15,00,000 figure and the 120-day figure — confirm both in the current AY's ICAI material.

```mermaid
flowchart TD
    S["Start - individual - count days in PY"] --> Q1{"In India 182 days or more in PY"}
    Q1 -->|Yes| R["RESIDENT - go to additional conditions"]
    Q1 -->|No| Q2{"Special case - Indian citizen leaving for employment OR citizen/PIO visiting India"}
    Q2 -->|Yes - only 182-day test applies| NR["NON-RESIDENT unless 182 met - but check 15 lakh 120-day and 6(1A)"]
    Q2 -->|No - normal case| Q3{"60 days or more in PY AND 365 days or more in preceding 4 years"}
    Q3 -->|Yes| R
    Q3 -->|No| NR
```
*Figure 2 — Step 1 decision tree: are you a Resident (basic conditions and their relaxations)?*

#### Step 2 — Additional Conditions [Sec 6(6)]: ROR or RNOR?

*Only if* Step 1 made you a Resident. Now measure **depth/continuity** of the connection. A resident is **Resident and Ordinarily Resident (ROR)** only if he satisfies **BOTH** additional conditions:

- **(i)** He has been **Resident in India in at least 2 out of the 10** previous years immediately preceding the PY; **AND**
- **(ii)** He has been in India for **≥ 730 days in the 7** previous years immediately preceding the PY.

If a resident **fails either** of these → he is **Resident but Not Ordinarily Resident (RNOR)**.

> **Why "2 out of 10" and "730 in 7"?** Both encode *established, long-term* presence. "Resident in 2 of last 10 years" screens out someone only recently connected. "730 days in 7 years" ≈ an average of ~104 days/year — a genuine, sustained physical footprint. Fail either → you're too new (or too intermittent) to have your *global* income taxed → the softer RNOR basket.

**Memory hook:** *"To be ORDINARY (ROR) you need HISTORY: 2/10 and 730/7. Miss the history → you're 'not ordinarily' (RNOR)."*

**Additional RNOR triggers (attach to the same test):**
- The **120-day visitor** (₹15L case) who becomes resident is treated as **RNOR**.
- The **Sec 6(1A) deemed resident** is treated as **RNOR**.
- A person who is resident this year but was NR in 9 of the last 10 years, or here <730 days in last 7, is the classic *returning NRI* → RNOR for a couple of years until history builds up.

```mermaid
flowchart TD
    R["You are RESIDENT this year"] --> C1{"Resident in at least 2 of the last 10 previous years"}
    C1 -->|No| RNOR["RNOR"]
    C1 -->|Yes| C2{"In India at least 730 days in the last 7 previous years"}
    C2 -->|No| RNOR
    C2 -->|Yes| ROR["ROR - ordinarily resident"]
    X["120-day visitor OR 6(1A) deemed resident"] --> RNOR
```
*Figure 3 — Step 2: ROR needs BOTH additional conditions; failing either (or being a special-case resident) means RNOR.*

### 4.3 Residential status of an HUF — Section 6(2)

An HUF (Hindu Undivided Family) is a person too, but it can't "be present" in days. So the test shifts to **where the family's decisions are made**:

- **Resident:** an HUF is resident if the **control and management of its affairs is situated wholly or partly IN India** during the PY.
- **Non-Resident:** only if control & management is situated **wholly OUTSIDE** India.

> **Why "wholly or partly in India" for resident, but "wholly outside" for NR?** The bar to be resident is *low* (even partial Indian control ⇒ resident) and the bar to escape is *high* (must be **entirely** offshore). This reflects source-country protection of the tax base — it's easy to be caught, hard to slip out.

**ROR vs RNOR for HUF:** determined by testing the **KARTA** (manager) against the *individual additional conditions* [Sec 6(6)(b)]. If the karta satisfies both additional conditions → HUF is ROR; else RNOR. *Why the karta?* He is the mind and will of the family; his depth of Indian connection stands in for the family's.

### 4.4 Residential status of a FIRM / AOP / other persons — Section 6(2) & 6(4)

Same **control-and-management** logic as HUF, but no ROR/RNOR sub-split (that split exists only for individuals and HUFs):

- **Resident** if control & management is **wholly or partly in India**.
- **Non-Resident** only if **wholly outside** India.

### 4.5 Residential status of a COMPANY — Section 6(3)

A company is resident in India in a PY if **either**:

- **(a)** it is an **Indian company** (incorporated in India) — *always resident*, no matter where managed; **OR**
- **(b)** its **Place of Effective Management (POEM)** is **in India** in that year.

> **Why two tests?** (a) Incorporation is a bright-line: if you chose to register under Indian law and enjoy its corporate personality, you're in. (b) **POEM** — "the place where key management and commercial decisions necessary for the conduct of the business as a whole are, in substance, made" — is a *substance-over-form* test to stop a foreign-incorporated shell that is really run from a Mumbai boardroom from claiming NR status. It replaced the older, easily-gamed "control and management *wholly* in India" test. *Memory hook:* **"Indian company = always resident; foreign company = resident only if the real brain (POEM) sits in India."**

---

### 4.6 SCOPE OF TOTAL INCOME — Section 5 (the payoff)

Now that Sec 6 has labelled the person, **Sec 5 tells us which income basket is taxable.** Build it from three raw types of income:

1. **Income received or deemed to be received in India** (Sec 7 handles the "deemed received").
2. **Income which accrues or arises, or is deemed to accrue or arise, in India** (Sec 9 handles the "deemed").
3. **Income which accrues or arises AND is received OUTSIDE India** (pure foreign income).

The scope table — the single most important table in this chapter:

| Type of income | ROR | RNOR | NR |
|---|:---:|:---:|:---:|
| Received / deemed received **in India** | ✔ Taxable | ✔ Taxable | ✔ Taxable |
| Accrues / deemed to accrue **in India** | ✔ Taxable | ✔ Taxable | ✔ Taxable |
| Accrues **AND** received **outside India**, from a **business controlled from / profession set up in India** | ✔ Taxable | ✔ Taxable | ✘ Not taxable |
| Accrues **AND** received **outside India**, **any other** foreign income | ✔ Taxable | ✘ Not taxable | ✘ Not taxable |

**Read the pattern, don't memorise the grid:**

- **All three statuses** pay on **anything connected to India** (received in India or accruing in India). That's the *universal source nexus* — nobody escapes India-source income.
- **ROR** additionally pays on **all foreign income** — full *residence nexus*, worldwide.
- **RNOR** is ROR *minus* passive foreign income — it pays foreign income **only if it flows from a business controlled from India / profession set up in India.** *Why that one exception?* Because a business run *from* India is really an extension of Indian economic activity; only genuinely detached foreign income gets the shield.
- **NR** pays on **India-connected income only** — nothing foreign.

```mermaid
flowchart LR
    I["A rupee of income"] --> Q{"Connected to India - received here OR accrues here OR deemed 9/7"}
    Q -->|Yes| T["Taxable for ROR RNOR and NR"]
    Q -->|No - pure foreign income| F{"From a business controlled from India or profession set up in India"}
    F -->|Yes| G["Taxable for ROR and RNOR - NOT for NR"]
    F -->|No - passive foreign income| H["Taxable for ROR only"]
```
*Figure 4 — Scope of income as a flow: follow the rupee and ask "how connected to India is it?"*

> **Trap on "received":** *Received* means **first receipt**. If salary is *first received* in India and then remitted abroad, it was received in India. But **remittance to India of income already received abroad is NOT "received in India"** — it was received the first time, abroad. Re-bringing money to India does not create fresh taxability. *Why:* to tax it again on remittance would be double-counting the same receipt event.

### 4.7 Income *deemed to accrue or arise* in India — Section 9 (why it exists)

Left alone, "accrues in India" could be argued away. Sec 9 **defines** certain incomes as arising in India *by law*, closing the argument. Know the main heads and each rationale:

| Sec 9(1) item | Deemed to arise in India because… |
|---|---|
| **(i)** Income from any **business connection** in India, **property/asset/source** in India, or **transfer of a capital asset situate in India** | The economic root is Indian soil/market. Includes **indirect transfer** of shares deriving substantial value from Indian assets — *anti-avoidance so you can't sell "the Indian business" by selling an offshore holding company*. |
| **(ii)** **Salary** for services **rendered in India** | Work physically done here → India-source, even if paid abroad. |
| **(iii)** **Salary** paid by the **Government of India** to an **Indian citizen** for services **outside India** | India is the paymaster of its own citizen-servants; a sovereign taxing its diplomats' pay is fair. *(The allowances/perks abroad are separately exempt u/s 10 — different chapter.)* |
| **(iv) & (v)** **Dividend** paid by an **Indian company**; **Interest** payable by Govt / by a resident (with exceptions) / by an NR on money used for a business in India | The payer is Indian / the funds fuel Indian business → Indian source. |
| **(vi) & (vii)** **Royalty** and **Fees for Technical Services (FTS)** payable by Govt / by a resident / by an NR for use in a business in India | The IP or service is *consumed* in India → India taxes the source. |

**Memory hook for Sec 9:** *"Business connection, Indian property, salary-for-work-here, Govt-salary-to-citizens, and India-sourced dividend/interest/royalty/FTS — the law refuses to let you pretend these arose abroad."*

**Section 7 — income deemed to be *received*:** e.g. the **employer's contribution to a recognised provident fund** in excess of limits, and **interest credited** to RPF beyond the notified rate, and **transferred balance** — treated as received even though not paid out in cash. *Why:* prevents disguising real receipts as untouchable fund entries.

---

## 5. Worked Examples — full, reconciling computations

> These illustrate *classification* (the exam's favourite) and then *scope application*. Use the figures as method, not as current-year law.

### Example 1 (Easy) — plain individual, both basic conditions in play

**Facts:** Mr. Arun stayed in India **65 days** in PY 2025-26. In the **4 preceding years** he was present **100 + 90 + 95 + 120 = 405 days**. He is an ordinary Indian resident (no employment-abroad, not a visitor). Classify him.

**Solution — Step 1 (basic):**
- Condition (a): 65 days ≥ 182? **No.**
- Condition (b): 65 days ≥ 60? **Yes.** AND 405 days ≥ 365 in prior 4 years? **Yes.** → Condition (b) **satisfied.**
- Satisfies at least one basic condition ⇒ **RESIDENT.**

**Step 2 (additional)** — assume he has lived in India every year for the last decade, so easily: resident in ≥2 of last 10 (yes) and ≥730 days in last 7 (yes). ⇒ Both satisfied ⇒ **Resident and Ordinarily Resident (ROR).**

**Reconciliation:** He was here only 65 days this year, but the *recurring pattern* (405 days across 4 years) plus deep history makes him ROR — exactly the "habit, not a visit" logic. **His worldwide income is taxable.**

### Example 2 (Moderate) — the employment-abroad relaxation

**Facts:** Mr. Bhaskar, an **Indian citizen**, left India for the **first time on 15 September 2025** to take up employment in Singapore. He had lived in India all his life before that. Days in India in PY 2025-26 = 1 April to 15 September = **168 days** (assume). His non-foreign total income is ₹8 lakh. Classify.

**Solution — Step 1:**
- Because he is an Indian citizen **leaving for employment abroad**, the relaxation applies: condition (b)'s 60-day trigger is **replaced by 182 days** → *only* condition (a) can make him resident.
- Condition (a): 168 days ≥ 182? **No.**
- (₹15L rule doesn't bite: this relaxation is the pure "employment abroad" one under 6(1A)/Expl.1(a); his income ₹8L < ₹15L anyway, and the 120-day variant is for *visitors*, not those leaving for employment.)
- ⇒ **NON-RESIDENT** for PY 2025-26.

**Scope consequence (Sec 5):** As NR, **only his India-connected income is taxable** — his Indian salary for 1 April–15 Sept (services rendered in India, Sec 9(1)(ii)) and any Indian rent/interest. His **Singapore salary from 16 Sept onwards is foreign income → NOT taxable in India.**

**Reconciliation:** The relaxation did its job — India isn't taxing the global salary of a citizen who left to work abroad merely because he was here for the first 168 days. Note the knife-edge: had he stayed **182+ days** before leaving, condition (a) alone would make him resident.

### Example 3 (Exam-hard) — returning NRI, RNOR, and full scope computation

**Facts:** Ms. Chandni, an Indian citizen, had lived in the **USA for 20 years** (NR throughout). She returned to India **permanently on 1 April 2025**, so she is present in India the **entire PY 2025-26 (365 days)**. During PY 2025-26 she earned:

1. Salary for consultancy performed in India — **₹18,00,000** (received in India).
2. Rent from her flat in Bengaluru — **₹3,00,000** (received in India).
3. Interest on her US bank deposits — **₹4,00,000** (accrued and received in USA; a passive foreign source).
4. Profit from a **software business she controls from India**, operations in USA, income received in USA — **₹6,00,000**.
5. Dividend from a US company, received in USA — **₹1,00,000** (passive foreign).

Determine her residential status and her **total income taxable in India.**

**Step 1 — basic conditions:** Present 365 days ≥ 182 ⇒ **RESIDENT.**

**Step 2 — additional conditions:**
- (i) Resident in ≥ 2 of the **last 10** previous years? She was **NR in all 10** prior years (20 years abroad). **Fails.**
- Failing even one ⇒ **Resident but Not Ordinarily Resident (RNOR).**

**Step 3 — apply the Sec 5 scope grid to each item:**

| # | Income | Nature | Taxable for RNOR? | Amount ₹ |
|---|---|---|:---:|---:|
| 1 | Consultancy salary, services in India, received in India | India-source (received + accrues here) | ✔ | 18,00,000 |
| 2 | Bengaluru rent, received in India | India-source | ✔ | 3,00,000 |
| 3 | US bank interest, accrues + received in USA | Passive foreign | ✘ | — |
| 4 | Business income received in USA but **controlled from India** | Foreign income from India-controlled business | ✔ | 6,00,000 |
| 5 | US dividend, received in USA | Passive foreign | ✘ | — |
| | **Total income taxable in India** | | | **27,00,000** |

**Reconciliation & the teaching point:** Items 3 and 5 (₹5,00,000 of passive foreign income) escape *only because* she is RNOR, not ROR. The RNOR shield protects **passive** foreign income but **not** item 4 — a business **controlled from India** is treated as economically Indian, so ₹6,00,000 is caught. This is exactly the design in Section 4.6.

**Contrast — if she had been ROR** (say she'd returned years earlier and built the required history): items 3 and 5 would *also* be taxable, giving total income of **₹32,00,000**. Same person, same money — **₹5,00,000 difference in the tax base created purely by residential status.** That is Section 2's core idea made numerical.

**Contrast — if she were NR:** item 4 would *also* fall out (NR is never taxed on foreign income, even from an India-controlled business), leaving only items 1 + 2 = **₹21,00,000**.

| Status | Items taxed | Total income ₹ |
|---|---|---:|
| **ROR** | 1,2,3,4,5 | 32,00,000 |
| **RNOR** | 1,2,4 | 27,00,000 |
| **NR** | 1,2 | 21,00,000 |

*One set of facts, three baskets — the entire chapter in one table.*

---

## 6. Computation Format / Presentation (how to write it in the exam)

Examiners award marks for a **clean, staged layout.** Use this skeleton:

**Part A — Determination of Residential Status**
```
Step 1  Basic conditions [Sec 6(1)]
        (a) Days in PY .......... = XX  → ≥182 ?  Yes/No
        (b) Days in PY ≥ 60 ?  Yes/No
            Days in preceding 4 yrs = XXX → ≥365 ?  Yes/No
        [Note any relaxation: Indian citizen employment abroad / PIO visit → 60 replaced by 182 (or 120 if non-foreign income > ₹15L)]
        Conclusion: Resident / Non-Resident

Step 2  (only if Resident) Additional conditions [Sec 6(6)]
        (i)  Resident in ≥2 of last 10 PYs ?  Yes/No
        (ii) In India ≥730 days in last 7 PYs ?  Yes/No
        Conclusion: ROR (both satisfied) / RNOR (either failed)
```

**Part B — Scope of Total Income [Sec 5]** — one row per income item, a column of "Taxable? (reason)", and a total. Always **state the reason** (received in India / accrues in India / deemed u/s 9 / foreign income from India-controlled business / passive foreign). The reason column is where the marks live.

Golden rules:
- Determine status **first, completely**, then apply scope. Never mix.
- **Count days carefully** — day of arrival and day of departure are *both* counted as days in India (a standard ICAI convention). Verify the convention in your material.
- Quote the **section** beside each conclusion.

---

## 7. Connections — where this plugs into the rest of the syllabus

- **Chapter 1 (Basic Concepts):** *Previous Year* and *Assessment Year* — residence is tested **per previous year**. *Person* — each type of person has its own Sec 6 test.
- **Salary head:** Sec 9(1)(ii)/(iii) decide when foreign-earned salary is Indian-source; the RNOR/NR shield decides whether foreign salary is taxed at all.
- **Capital Gains:** Sec 9(1)(i) + **indirect transfer** rule decides when a non-resident's sale of shares is taxed in India.
- **Deductions & DTAA / Sec 90/91 (relief from double taxation):** an ROR taxed on worldwide income may have *already* paid foreign tax — hence **foreign tax credit / double-tax relief**. Residence is the *reason* double taxation arises.
- **TDS (Sec 195):** payments to non-residents are the trigger for withholding — you must know NR status to apply it.
- **Exempt incomes (Sec 10):** several exemptions (e.g. for non-residents, for Govt employees abroad) interact with the deeming rules.

---

## 8. Traps & Examiner Tricks

1. **Citizenship ≠ residence.** A foreign citizen present 182+ days is a *resident*; an Indian citizen abroad can be *NR*. The exam plants this constantly.
2. **"Received in India" vs "remitted to India."** Foreign income *remitted* to India stays foreign — remittance is **not** first receipt. Don't tax NR/RNOR on money they merely bring home.
3. **Forgetting the relaxation.** For an Indian citizen *leaving for employment* or a *citizen/PIO visiting*, the 60-day condition is **inoperative (raised to 182, or 120 if non-foreign income > ₹15L)**. Students wrongly apply 60 and mis-classify.
4. **The RNOR business exception.** Foreign income from a **business controlled from India / profession set up in India** *is* taxable for RNOR. Students often exempt all foreign income for RNOR — wrong.
5. **Day counting.** Both arrival and departure days count as in-India days. Off-by-one errors flip 182/60/730 thresholds.
6. **"2 out of 10" tests RESIDENT-years, not presence-years.** Condition 6(6)(i) asks in how many of the last 10 years he was a *resident*, not how many days.
7. **HUF/firm/company use CONTROL, not days.** Applying the day-count to an HUF or company is a classic error. And: **Indian company is *always* resident** regardless of POEM.
8. **RNOR only exists for individuals & HUFs.** Firms/AOP/companies are just Resident or NR — no "ordinarily" split.
9. **Sec 6(1A) deemed resident** applies only to **Indian citizens** with non-foreign income > ₹15L who are **not liable to tax anywhere** — and they are **RNOR**, not ROR.
10. **Salary by Govt to citizen abroad** is deemed to arise in India [Sec 9(1)(iii)] — taxable even for an NR, because the source is Indian.

---

## 9. First-Principles Recap

Strip everything away and one chain remains:

> A country taxes income to the extent it has an **economic claim (nexus)** on it. India has a **source claim** on all income arising here — so *everyone* pays on India-connected income. India has a **residence claim** on those economically anchored here — so *residents* additionally pay on foreign income. Because "anchored" is a matter of degree, India uses **objective day-counts** (Sec 6) to sort people into **NR** (no anchor → source income only), **RNOR** (new/shallow anchor → source income + India-controlled foreign business, a soft landing), and **ROR** (deep anchor → worldwide). **Section 5** is just this logic written as a grid; **Sections 7 & 9** stop taxpayers from arguing that Indian-source income arose or was received abroad.

If you can re-derive Figure 4 and the Sec 5 grid from "source nexus is universal, residence nexus is the extra reach," you never need to memorise the grid — you can *rebuild* it.

---

## 10. Quick-Revision Sheet

### Sections at a glance
| Section | Content |
|---|---|
| **6(1)** | Basic conditions for individual — Resident or NR |
| **6(1A)** | Deemed resident — Indian citizen, non-foreign income > ₹15L, not taxable anywhere → RNOR |
| **6(2)** | HUF / firm / AOP — control & management test |
| **6(3)** | Company — Indian company OR POEM in India |
| **6(6)** | Additional conditions — ROR vs RNOR (individual & HUF) |
| **Expl. 1 to 6(1)** | Relaxations: 60→182 (employment abroad / citizen-PIO visit); 60→120 if visitor's non-foreign income > ₹15L |
| **5** | Scope of total income by status |
| **7** | Income deemed to be received (e.g. excess RPF employer contribution/interest) |
| **9** | Income deemed to accrue/arise in India |

### Day-count / threshold table (VERIFY current AY)
| Test | Threshold | Meaning |
|---|---|---|
| Basic (a) | **182 days** in PY | Majority of year → resident |
| Basic (b) | **60 days** in PY **+ 365 days** in prior 4 yrs | Recurring pattern → resident |
| Relaxation | 60 → **182** | Citizen leaving for employment / citizen-PIO visiting |
| Relaxation (high income) | 60 → **120** | Visitor with non-foreign income **> ₹15,00,000** |
| Deemed resident 6(1A) | non-foreign income **> ₹15,00,000**, stateless | Indian citizen → RNOR |
| Additional (i) | Resident in **≥ 2 of last 10** PYs | Long-term connection |
| Additional (ii) | **≥ 730 days in last 7** PYs | Sustained presence |

### Status → scope (the grid to reproduce)
| Income | ROR | RNOR | NR |
|---|:--:|:--:|:--:|
| Received / accrues **in India** (incl. deemed 7 & 9) | ✔ | ✔ | ✔ |
| Foreign income from **business controlled from / profession set up in India** | ✔ | ✔ | ✘ |
| Other (passive) **foreign** income | ✔ | ✘ | ✘ |

### Non-individual persons
| Person | Resident if… | ROR/RNOR split? |
|---|---|:--:|
| **HUF** | control & mgmt **wholly or partly in India**; ROR/RNOR by testing **karta** on 6(6) | Yes |
| **Firm / AOP** | control & mgmt wholly or partly in India | No |
| **Company** | **Indian company (always)** OR **POEM in India** | No |

### Three memory hooks
- **"6 = WHO, 5 = WHAT, 7 & 9 = no escape."**
- **"182 half-a-year; 60+365 a habit; 2/10 & 730/7 = history for ROR."**
- **"Source nexus catches everyone; residence nexus is the extra reach that only closes fully on ROR."**

> **Final reminder:** confirm the ₹15,00,000 threshold, the 120-day figure, day-counting convention, and every numeric limit against **current ICAI study material for your applicable Assessment Year** before the exam.
