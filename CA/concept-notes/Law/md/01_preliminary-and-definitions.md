<!-- v2-deep -->

# Chapter 01 — Companies Act 2013: Preliminary & Key Definitions

> *"A company is not a thing you can touch. It is a legal fiction — an artificial person the law agrees to pretend exists. Every definition in this chapter is the law drawing the exact outline of that fiction, because the moment you invent an invisible person who can own property and owe money, clever people will try to abuse the gap between the fiction and reality."*

---

## 1. The Problem — Why We Needed to Invent the "Company" at All

Imagine there is **no** company law. You and four friends want to build a railway. It needs crores of rupees, thousands of investors, and it will run for 100 years. Try to do this with only the ordinary law of partnership and contract, and you hit four brick walls:

**Problem 1 — The business dies when a person dies.**
A partnership is just an *agreement between specific humans*. Legally, the firm **is** the partners. So the day one partner dies, retires, or goes insane, that partnership legally dissolves. A railway that must run for a century cannot re-form its legal existence every time a shareholder dies. Investors will not commit money to something that evaporates on a funeral.

**Problem 2 — Unlimited, ruinous personal liability.**
In a partnership every partner is **jointly and severally liable** for the *whole* debt. If the firm owes ₹10 crore and cannot pay, creditors can seize *your house, your car, your savings* — not just the money you put in. Worse, they can chase *any one* partner for the *entire* amount. No sane small investor will buy ₹5,000 of railway shares if it means their entire net worth is on the hook for the railway's ₹500-crore debts. Without a liability cap, **mass public investment is impossible.**

**Problem 3 — You cannot pool money from thousands of strangers.**
A partnership works between a handful of people who trust each other and all manage the business. It collapses at scale. You cannot have 40,000 shareholders each being a "partner" who can bind the firm and is personally liable for everything.

**Problem 4 — Whose name owns the assets?**
If the firm *is* the humans, then the land, the trains, the tracks are owned by *the individuals jointly*. Every time ownership changes, title has to be re-registered to a new set of humans. Contracts are with *individuals*, so they must be re-signed. It is legally unworkable.

**The deeper abuse the law also had to prevent:** once you *do* invent a limited-liability artificial person, the opposite danger appears — **fraudsters hiding behind the fiction.** A cheat can set up "XYZ Ltd", take deposits from the public, siphon the money to himself, then let the company "fail" and say *"Sorry, the company owes you, not me, and the company has no money."* So the same law that grants the shield must also define **when the shield can be ripped away.**

Every definition and doctrine in this chapter exists to solve one of these five problems: **death, ruin, scale, ownership, and the fraud that limited liability invites.**

**A sixth, quieter problem — information asymmetry.** Even honest strangers will not invest unless they can *find out* whom they are dealing with. In a partnership, the terms are private; nobody outside knows who the partners are or what the firm owes. The company solves this by being **a public creature**: it exists only on a **register kept by the Registrar of Companies (ROC)**, and it must file its constitution, its officers, its charges, and its accounts. So the definitions in this chapter are not just about *creating* the fiction — they are about *making it checkable.* Whenever you wonder "why is this defined so precisely?", one honest answer is: *so an outsider can verify it before parting with money.*

**Why not just use a trust or a co-operative?** A trust holds property for beneficiaries but is not itself a person that can freely trade, sue, and take public capital; a co-operative serves its members on mutual principles, not open profit-seeking with tradeable shares. The company is the *only* form that simultaneously offers a separate person, transferable ownership, capped liability, and a public register — which is exactly why large commerce gravitates to it.

---

## 2. The Core Idea — The Artificial Person With a Ring-Fence Around It

The law's solution is one radical move: **create a new legal person.**

When a company is incorporated (registered), the law says: *"A brand-new person now exists — separate from every human who created it or owns it. It has its own name, its own PAN, can own property in its own name, can sue and be sued in its own name, can enter contracts, and — crucially — it lives until the law formally kills it, regardless of what happens to its members."*

This single fiction dissolves all four practical problems at once:

- Because the person is **separate**, it owns its own assets — ownership problem solved.
- Because the person is **immortal until wound up** (perpetual succession), the death of members is irrelevant — the death problem solved.
- Because the *company* owes the debts (not the members), and members only promised to pay for their shares, member liability is capped at the unpaid value of their shares — **limited liability** — the ruin problem solved.
- Because the shares are transferable and the person is separate, thousands of strangers can invest small sums freely — the scale problem solved.

But the fifth problem — **fraudsters abusing the shield** — cannot be solved by the fiction itself. It is solved by a *counter-doctrine*: **lifting / piercing the corporate veil.** The "veil" is the imaginary curtain between the company and its members. Normally the court respects it. But when the fiction is being used *as a cloak for fraud, evasion, or sham*, the court will **look behind the curtain**, identify the real humans, and hold *them* liable.

So the whole architecture is a **shield plus an exception to the shield**:

```mermaid
flowchart TD
    A["Humans want to do<br/>large risky long-lived business"] --> B["Law creates an<br/>ARTIFICIAL LEGAL PERSON"]
    B --> C["Separate legal entity<br/>owns its own assets"]
    B --> D["Perpetual succession<br/>survives member death"]
    B --> E["Limited liability<br/>members risk only share money"]
    C --> F["Mass public investment<br/>becomes possible"]
    D --> F
    E --> F
    F --> G{"Is the fiction being<br/>abused for fraud or evasion?"}
    G -->|No| H["Veil respected<br/>company alone is liable"]
    G -->|Yes| I["Court LIFTS the veil<br/>real humans held liable"]
```
*Figure 1 — The company is a shield the law grants, plus a court's power to withdraw the shield when it is abused.*

**A subtlety students miss — "artificial person" does NOT mean "citizen".** A company is a *legal person* (it can own, contract, sue) but it is **not a natural person or a citizen**. It therefore *cannot* claim rights that the Constitution reserves to *citizens* (e.g., certain fundamental rights under Article 19 such as freedom of speech/trade **as a citizen**), though it *can* claim rights available to any "person" (e.g., equality under Article 14, protection of property). It has **no body, no mind, and no soul** — so it cannot marry, take an oath in person, or go to jail; it acts only **through human agents** (Board, officers, members in meeting). This is why the law must always answer a second question after "is the company liable?" — namely, "**which human's act or intent is attributed to the company?**" That attribution question is the seed of the *alter ego* and *directing mind* doctrines you meet later.

**The company as a "nexus of contracts".** A useful first-principles lens: the company sits at the centre of a web of relationships — with members (via the constitution), directors (fiduciary duties), creditors (debt), employees (employment), and the State (regulation). The definitions in this chapter fix *who stands where* in that web, so that rights and duties attach to the right party. Get the category wrong and every downstream duty attaches wrongly.

---

## 3. Why It's Built This Way — The Logic of Each Safeguard

Before the section numbers, understand *why the machinery has the exact shape it has.* Each design choice is a plugged loophole.

- **Why "separate legal entity" is the foundation stone.** Everything else is a consequence. If the company were *not* a separate person, it could not own assets, could not survive members, and members could not have limited liability. This principle was cemented in **Salomon v. Salomon & Co. Ltd (1897)** — the House of Lords held that even a "one-man company" is legally distinct from that man, so his personal guarantee ranked ahead of unsecured creditors. The company, once validly incorporated, is a real legal person even if one human controls it entirely.

- **Why limited liability is capped at the *unpaid* amount, not zero.** The law does not let members walk away scot-free. If you agreed to buy shares of face value ₹10 and paid only ₹6, you still owe ₹4 — the company (or its liquidator) can call it. This protects **creditors**: the promised capital is a fund creditors can rely on. Limited liability limits your downside to *your promise*, not below it.

- **Why there are TWO ways to limit liability — by shares and by guarantee.** A trading company raises a permanent capital fund, so members' liability is naturally measured by their *shares* (limited by shares). But a club, trade association, or charity has little share capital and only needs a *backstop* if it winds up — so members instead promise a fixed sum payable **only on winding up** (limited by guarantee). The guarantee amount **cannot be called while the company is a going concern** — that is the whole point; it is a winding-up fund, not working capital. A company can even be *limited by guarantee **and** have share capital*, in which case a member is liable both for unpaid share money *and* the guarantee. And a company can be **unlimited** (Sec 2(92)) — members bear full liability, the trade-off being far lighter regulation and freedom to return capital. This spectrum (unlimited → guarantee → shares) is the *why* behind Section 2 having separate definitions for each.

- **Why the law forces sub-categories (private, public, OPC, small).** A one-size company law would either over-regulate the corner shop or under-regulate the listed giant. The abuse to prevent is **mismatched regulation** — crushing a small business with disclosure rules meant for a company holding public money, or letting a company with 40,000 public investors escape scrutiny meant for a family firm. So the Act **scales the compliance burden to the public interest at stake.** More public money and more outside stakeholders → more rules.

- **Why holding/subsidiary/associate must be *defined precisely.***  Once a company can *own shares in another company*, fraudsters build **pyramids of companies** to hide control, shift losses into a subsidiary, dodge consolidation, or claim two "separate" companies are unrelated when one secretly controls the other. Precise definitions (based on **share capital, voting power, and board control**) force the true web of control into the open through consolidated accounts.

- **Why "listed" is its own category.** A listed company has taken money from the **anonymous investing public** via a stock exchange. The public cannot individually negotiate protections, so the law (and SEBI) must impose them. Listing status is the trigger for the heaviest disclosure and governance load.

- **Why veil-lifting is deliberately *narrow* and mostly judge-made.** If courts pierced the veil casually, limited liability would be worthless and investment would dry up (back to Problem 2). So piercing is an **exception**, used only for fraud, evasion of law/obligation, sham, or specific statutory commands — never merely because it would be convenient for a creditor.

- **Why definitions use "means", "includes", and "means and includes" — and why it matters.** This is a first-principles drafting point the examiner loves. A definition that says **"means"** is **exhaustive** — nothing outside the words counts (e.g., Sec 2(20) "company" *means*). A definition that says **"includes"** is **extensive/illustrative** — it *adds* to the ordinary meaning without limiting it (so the term is broader than the list). **"Means and includes"** is exhaustive *for the listed items* — the drafter has both defined and enumerated. Reading a definition correctly *is* the exam skill: whether a borderline body falls inside a term often turns entirely on this one word. (This connects to Interpretation of Statutes in the Other Laws part.)

- **Why the Act layers "company" inside "body corporate" inside "person".** The law needs *concentric* categories so a rule can be aimed at exactly the right width — some rules bite only "companies incorporated under the Act", some bite any "body corporate" (catching foreign companies and LLPs), and some bite any "person". Getting the width right is a deliberate design lever, not sloppiness.

---

## 4. Full Technical Content — Section by Section, Each With Its "Why"

> The Act is the **Companies Act, 2013** (India). Definitions live in **Section 2**. *Always confirm exact sub-clause numbers and current thresholds against the latest ICAI study material / bare Act, as amendments (esp. 2015, 2017, 2019, 2020, 2021) and rules revise limits.*

### 4.1 What a "company" is — Section 2(20)

**Section 2(20): "company" means a company incorporated under this Act or under any previous company law.**

*Why so circular?* Because the point is that a company is **a creature of statute** — it exists *only* because a law says it does and it was registered under that law. You cannot "become a company" by agreement, as you can a partnership. This ties company existence to the **register kept by the Registrar of Companies (ROC)**, which is what makes the public able to *check* who they are dealing with.

**The characteristics that flow from incorporation (know these cold):**

| Characteristic | What it means | Problem it solves |
|---|---|---|
| Separate legal entity | Company is a person distinct from members | Ownership, and shielding members |
| Limited liability | Members liable only up to unpaid share value (or guarantee) | Ruinous personal liability |
| Perpetual succession | Company lives regardless of member death/exit until wound up | Business dying with a person |
| Common seal (now optional) | Historically the company's "signature" | Acting as a person in contracts |
| Separate property | Company owns assets in its own name; members have **no insurable/ownership interest** in company assets | Re-registering title on every change |
| Capacity to sue and be sued | In its own name | Enforcing/being held to obligations |
| Transferability of shares | Especially in public companies | Free flow of investment |

**Landmark hooks for memory:**
- *Salomon v. Salomon (1897)* — separate entity, even a one-man company.
- *Lee v. Lee's Air Farming (1961)* — Lee could be **both** the controlling shareholder **and** an *employee* of his own company; when he died flying its plane, his widow claimed workers' compensation *from the company*. Company and man are different persons, so an employment contract between them is real.
- *Macaura v. Northern Assurance (1925)* — Macaura owned all the shares of a timber company but insured the timber in his **own** name. Timber burned; insurer refused. Held: the *company* owned the timber, **not** Macaura, so he had **no insurable interest**. Separate property, ruthlessly applied.

**Finer distinctions the exam probes:**

- **"Common seal is now optional" — since when and so what?** The **Companies (Amendment) Act, 2015** made the common seal **optional**. If a company *chooses* to have one, documents can be executed under seal; if it does **not**, documents may be signed by **two directors, or one director and the company secretary** (or one director where there is only one). Trap: a question may assume a seal is *mandatory* — it is not.

- **Members vs shareholders — not always identical.** A **member** is one whose name is entered in the **register of members** (Sec 2(55)). A subscriber to the memorandum becomes a member on incorporation *even before shares are allotted or a certificate issued*. A person holding a **share warrant** (bearer) historically was a *shareholder* but **not** a member. So "member" is a register concept; "shareholder" is an ownership concept — usually the same person, but the exam can split them.

- **The company's nationality, residence, and domicile.** A company **has** a nationality, residence, and domicile (fixed by place of incorporation and registered office) — but it is **not a citizen** (see §2). This matters for tax residence and for the *Daimler* enemy-character point.

- **"Perpetual succession" precisely stated.** Members may come and go, be born or die, become insolvent or insane — the company's *legal identity* is unaffected. The stock aphorism: *"Members may come and members may go, but the company goes on forever"* — **until** it is wound up or struck off. It is **not unconditional immortality** (see Trap 12).

### 4.2 Private vs Public company — Sections 2(68) and 2(71)

**Section 2(68) — Private company.** A company which, by its **articles**:
1. **Restricts the right to transfer its shares** — *why?* A private company is a closed circle (often family/friends); it does not want outsiders forcing their way in, and it does not take public money, so shares are not freely tradeable. Note: the articles **restrict** (regulate), they do not **prohibit** transfer — a member can still transfer, subject to conditions (e.g., pre-emption / board approval).
2. **Limits the number of members to 200** (excluding present and past employees who are members) — *why 200?* It is the line between a "private, closed" body and one large enough that it is effectively raising money from the public. Joint holders count as one member.
3. **Prohibits any invitation to the public** to subscribe for securities — *why?* This is the core distinction: a private company must **not** tap the public. The moment you solicit the public, you must accept public-company scrutiny.
   *Minimum members = 2.*

**Section 2(71) — Public company.** A company which is **not** a private company, **and** (per the section's structure) a company that is a **subsidiary of a public company is deemed public** even if its articles say "private" — *why this deeming?* To stop the **pyramid trick**: making a subsidiary "private" on paper to escape rules, while a public company (and thus public money) sits above it controlling it. Substance over form.
   *Minimum members = 7; no upper limit; minimum directors = 3 (private = 2, OPC = 1).*

**The three private-company restrictions dissected (why each is drafted as it is):**

- The **200-member cap counts holders, not holdings.** **Joint holders** of one or more shares are treated as **a single member**. **Present and past employees** who became members *while in employment* and *continued* after leaving are **excluded** from the count. So a company can have far more than 200 *humans* on its register and still be private if enough of them are excluded categories or joint holders. *Exam favourite: given a messy shareholder list, compute the effective member count.*
- The cap is **200, not 50.** Fifty was the 1956 Act figure. Under the 2013 Act it is **200**.
- "Invitation to the public" is read **widely** — even a *private placement dressed up* can be caught. The prohibition protects the whole logic of the private/public divide.

**Deemed public company — the exact mechanics.** A private company that is a **subsidiary of a public company** is treated as a **public company for the purposes of the Act**, *even if its articles retain the three private-company restrictions.* Practically it must then meet public-company requirements (e.g., minimum 3 directors, no bar on being under public-company obligations), because public money/control sits above it. This is **substance over form** in statutory form.

**Consequences that flow from the classification (why the label is worth fighting over):** Private companies enjoy numerous **exemptions/relaxations** — e.g., fewer directors (2 vs 3), can commence business more simply, various procedural relaxations, and (for eligible ones) small-company reliefs. Public companies face stricter norms on acceptance of deposits, related-party transactions, managerial remuneration, and (if listed) SEBI's LODR. So misclassifying a company mis-assigns its *entire* compliance regime.

> **Note on paid-up capital.** The 2013 Act originally prescribed a *minimum paid-up capital* (₹1 lakh private / ₹5 lakh public). The **Companies (Amendment) Act, 2015 removed** the minimum paid-up capital requirement. *Confirm in current material — many old questions still quote the old figures as a trap.*

### 4.3 One Person Company (OPC) — Sections 2(62) and 3

**The problem OPC solves:** A **sole** entrepreneur previously had a cruel choice — run a proprietorship (simple, but **unlimited personal liability**) or find a second person just to satisfy the "minimum 2 members" rule for a private company (artificial, often a sham nominee). Neither is honest. OPC (a J.J. Irani Committee recommendation) gives a **single** person the **limited-liability shield** without needing a fake second member.

**Section 2(62): OPC = a company which has only *one* person as a member.**

Key built-in safeguards (each solving a specific worry):

| Feature | Rule | Why |
|---|---|---|
| Nominee | The sole member must **name a nominee** in the memorandum who becomes member on his death/incapacity | Perpetual succession needs a successor — with one member, death would otherwise kill the company |
| Who can form | Only a **natural person** who is an **Indian citizen and resident** in India; and can form only **one** OPC and be nominee in only **one** | Prevents shell-company chains and misuse by non-persons |
| Conversion trigger | Historically OPC had to convert to private/public if paid-up capital exceeded **₹50 lakh** or average annual turnover exceeded **₹2 crore** (over 3 years). *The 2021 rules removed these thresholds, allowing OPCs to grow and convert voluntarily — confirm current rule.* | Originally to push large businesses out of the "one-man" form; later liberalised to encourage entrepreneurship |
| Restrictions | OPC **cannot** carry on Non-Banking Financial Investment activities / invest in securities of other bodies corporate; a minor cannot be member or nominee | OPC is for a genuine solo operating business, not a holding/finance vehicle |

*Section 3 (formation) tells you how many people form each type: Public = 7 or more, Private = 2 or more, OPC = 1.* **Memory hook: 7-2-1** (public–private–OPC).

**OPC is legally a species of private company.** Section 3(1)(c) creates OPC *as a private company*. So an OPC is a **private company with a single member** — it inherits private-company treatment except where the Act specifically relaxes it. This has practical bite: an OPC gets *additional* relaxations layered on top of private-company ones (e.g., **may dispense with AGMs**; simplified financials — cash-flow statement not required; board meetings — one director OPC can pass resolutions by entry in the minutes book). *Confirm exact reliefs in current material.*

**The nominee mechanics (finer points):**
- The nominee's **written consent** is filed with the ROC at incorporation.
- The nominee can **withdraw** consent; the member must then nominate another.
- The member can **change** the nominee at any time.
- On the member's death or incapacity to contract, the **nominee becomes the member** — securing perpetual succession *despite* there being only one member. The new member must in turn nominate someone.

**Residency test — watch the exact number.** "Resident in India" for OPC eligibility has been defined by reference to a **stay of a specified number of days in the previous financial year** — historically **182 days**, later reduced (the 2021 rules revised the period, and NRIs/Indian citizens were permitted to form OPCs). *This day-count is a classic amendment trap — verify the current figure and who is now eligible.*

### 4.4 Small company — Section 2(85)

**The problem:** A tiny company should not drown in the same compliance as a mid-size one. "Private company" alone is too broad — a ₹90-crore private company is not "small". So the Act carves a **sub-set of private companies** that get *relaxations* (fewer board meetings, no cash-flow statement, lighter penalties, simplified annual return).

**Section 2(85): a small company is a company (not public) whose:**
- **paid-up share capital** does **not** exceed a prescribed limit, **and**
- **turnover** does **not** exceed a prescribed limit.

*Both* conditions must be met (it is an **AND**). The figures have been raised repeatedly. Originally ₹50 lakh capital / ₹2 crore turnover; the widely-cited revised limits are **paid-up capital ≤ ₹4 crore and turnover ≤ ₹40 crore**. *Confirm the exact current limits in ICAI material — this is a favourite exam-update trap.*

**Who can NEVER be a small company (the exclusions — and their logic):**
- a **public company** — by definition too open;
- a **holding or subsidiary** company — it is part of a larger group, so not truly "small";
- a company registered under **Section 8** (non-profit) — different regime;
- a company governed by a **special Act** (e.g., banks, insurers).

*Why the exclusions?* Each is a way someone might *look* small on its own numbers while actually being embedded in something large or public — the relaxations would then be abused.

**Small-company status is DYNAMIC, not permanent.** Because it depends on the *previous year's* capital and turnover, a company can **become** a small company one year and **cease** to be one the next as it grows (or shrinks). There is **no separate registration** as a "small company" — the status is simply a fact tested each year. *Exam angle:* "Company X was small last year; this year turnover crossed the limit — is it still small?" Answer: it **ceases** to enjoy the reliefs once either threshold is breached.

**The relaxations a small company enjoys (know at least four):**
- **Fewer board meetings** — a small company may hold only **two board meetings a year** (one per half-year, with a minimum gap), instead of four.
- **Cash-flow statement not required** as part of financial statements.
- **Abridged / simplified annual return**, which may be **signed by the company secretary, or where there is none, by a director** (no mandatory PCS certification in the same way as larger companies).
- **Lower / lesser penalties** for certain defaults (the Act provides reduced penalties for small companies and OPCs).
- **Rotation of auditors** (Sec 139(2)) does **not** apply to small companies.
*Confirm the current list against ICAI material — reliefs have been expanded over time.*

**Distinguish the four "smaller-entity" concepts** (examiners deliberately blur them): **OPC** (one member), **small company** (private + within capital/turnover limits), **dormant company** (Sec 455 — inactive/formed for a future project, no significant accounting transactions), and **Section 8** (non-profit). They overlap partly (an OPC that is small gets both sets of reliefs) but are defined by **different tests** — membership, size, activity, and object respectively.

### 4.5 Holding, subsidiary, and associate — Sections 2(46), 2(87), 2(6)

These three define **control relationships between companies.** The abuse to prevent: **hiding true control and shifting profits/losses across a corporate pyramid** so outsiders can't see who really runs and who really owns what.

**Section 2(87) — Subsidiary company.** Company B is a subsidiary of Company A (the holding company) if A:
- **controls the composition of B's Board of Directors** (i.e., A can appoint/remove a majority of B's directors), **OR**
- **exercises or controls more than one-half of the total voting power** of B, either alone or with subsidiaries.

*Why "OR" and why both a board test and a voting test?* Because control can be exercised **two ways** — by owning the *votes* or by controlling the *board*. A cheat who owns only 40% but has a contractual right to name most directors still *controls* B. Covering both closes the gap.

**Precision points on Sec 2(87) that decide marginal questions:**
- The voting-power test is **"more than one-half of the total voting power"** — read it as **> 50%**, *not* "≥ 50%". A flat **50–50** holding is **not** a subsidiary on the voting test (though board control could still make it one). Trap: "A holds exactly 50% of B's equity" → **not** a subsidiary via votes.
- It is **voting power**, not merely **paid-up equity share capital** — because preference shares can carry votes in some situations and the real question is *who can out-vote whom*. Read the question for *voting* rights, not just shareholding percentage.
- **"Composition of the Board"** is controlled when A can, *without anyone else's consent*, **appoint or remove all or a majority** of B's directors. Owning the *power to appoint the majority* is control even with a minority stake.
- **"Total share capital"** — the 2017 amendment aligned the test around **total voting power** (earlier drafting/rules referenced "total share capital" including certain preference capital). *Verify the exact current wording — this has been amended.*
- **Indirect control counts** — A controls B "either on its own or together with one or more of its subsidiary companies." So if A controls C, and A + C together control >50% of D, then **D is A's subsidiary** through the chain.

> **Layering restriction:** The Act (via rules under Section 2(87) proviso) restricts the **number of layers of subsidiaries** (generally **not more than two layers**, with exceptions). *Why?* Endless subsidiary-of-subsidiary chains are exactly how money and control are hidden. *Confirm the current layer limit and exemptions* (e.g., acquisition of a foreign company with its own multi-layer structure is generally not counted, and certain classes are exempt).

**Section 2(46) — Holding company.** The mirror image: A is the holding company of B if B is its subsidiary. (Definition simply says a company of which other companies are subsidiaries.) Note the 2017 amendment clarified "company" here includes any **body corporate**.

**Section 2(6) — Associate company.** A company in which another company has a **"significant influence"** — meaning control of **at least 20% of total voting power**, *or* control of business decisions under an agreement — **but which is NOT a subsidiary** and is not a joint venture. *Why 20%?* Below control (>50%) but enough to *materially influence* — the accounting world's threshold for "you influence this company, so you must disclose it." A joint venture is also treated as an associate for this purpose.

**Associate — the finer edges:**
- "Significant influence" = **≥ 20% of total voting power** *or* control of/participation in **business decisions under an agreement** — the *agreement* limb catches influence that does **not** show up as 20% shareholding. So a company holding only 15% but with a management/shareholders' agreement giving it a veto over key decisions can still be an associate.
- The **2017 amendment** clarified that "significant influence" is measured on **total voting power** (not "total share capital"), and expressly stated a **joint venture** is an associate. *Verify wording.*
- An associate is deliberately **not** a subsidiary — so it is **not** consolidated line-by-line but is brought into consolidated accounts by the **equity method** (Accounts chapter). The definition's job is to force *disclosure of influence*, one rung below control.

**The clean ladder of control (memorise the numbers):**

| Relationship | Test | Threshold |
|---|---|---|
| Associate | Significant influence | ≥ 20% voting power (but ≤ 50%, not control of board) |
| Subsidiary / Holding | Control | > 50% voting power **OR** control of Board composition |

```mermaid
flowchart LR
    A["Company A's stake / control<br/>in Company B"] --> Q1{"Controls Board<br/>OR >50% votes?"}
    Q1 -->|Yes| S["B is a SUBSIDIARY of A<br/>A is the HOLDING company"]
    Q1 -->|No| Q2{"Holds >= 20% votes<br/>or significant influence?"}
    Q2 -->|Yes| AS["B is an ASSOCIATE of A"]
    Q2 -->|No| N["Mere investment<br/>no special relationship"]
```
*Figure 2 — The control ladder: cross 20% and you "influence"; cross 50% or control the board and you "own".*

**Chains and indirect control — worked mini-illustration.** Suppose **A holds 60% of B**, and **B holds 55% of C**. Then B is A's subsidiary, and C is B's subsidiary — therefore, by Sec 2(87)'s "together with subsidiaries" logic, **C is also A's subsidiary**, and A is the **ultimate holding company**. Now if A *directly* holds 25% of D as well, D is A's **associate** (influence, not control) *unless* A + its subsidiaries together cross 50% of D, which would flip D into a subsidiary. Always add up **direct + indirect** control before answering.

### 4.6 Listed company — Section 2(52)

**Section 2(52): a listed company means a company which has *any of its securities* listed on a recognised stock exchange.**

*Why a separate label?* Because listing = the company sold securities to the **anonymous public** through an exchange. That public needs the strongest protection, so listing is the trigger for SEBI (LODR) regulations, extra disclosures, independent directors, audit committees, etc. **Note (2020 amendment):** the definition was refined so that companies which list *only certain classes of securities* (e.g., only debt/NCDs on certain terms) may be **excluded** from being "listed" for some purposes — *confirm current carve-outs.* The logic: full listed-company burden should fall where **public equity** is truly in play.

**Precision points:**
- The trigger is **"any of its securities"** — not necessarily *equity*. A company with only its **debentures/NCDs** listed can fall within "listed" (subject to the 2020 carve-outs). *So a "listed company" is not automatically a "listed equity company".*
- A **private company can, in a narrow sense, have listed securities** (e.g., listed debt) and thus attract certain listed-company obligations — which is exactly why the 2020 carve-out was introduced, to avoid over-burdening companies whose *equity* is not public. *Verify the exact classes excluded.*
- "Recognised stock exchange" points to the **Securities Contracts (Regulation) Act, 1956** — a definitional hand-off to securities law.

### 4.7 Other key definitions worth exact recall

| Section | Term | One-line essence | Why it exists |
|---|---|---|---|
| 2(11) | Body corporate | Any incorporated body, incl. foreign companies & LLPs; **excludes** co-operative societies & specified bodies | Broader than "company"; used so rules catch all corporate forms |
| 2(20) | Company | Incorporated under this/previous Act | Creature of statute |
| 2(45) | Government company | ≥ 51% paid-up capital held by Central/State Govt (alone or together) | Public money = special audit (CAG) |
| 2(42) | Foreign company | Incorporated outside India but has a place of business/operations in India (incl. electronic mode) | Bring foreign firms operating here under Indian disclosure |
| 2(85) | Small company | Private + capital & turnover under limits | Proportionate lighter compliance |
| 2(62) | OPC | One member | Limited liability for a solo founder |
| 2(30) | Debenture | Instrument evidencing a debt (incl. bonds) | Defines the borrowing instrument |
| 2(84) | Share | Share in the share capital of a company | The unit of ownership |
| 2(55) | Member | Subscriber to MOA, or one whose name is in the register of members / beneficial owner in depository | Fixes *who* has membership rights |
| 2(60) | Officer in default | Specific officers liable for a default | Pins criminal/civil liability on a human |
| 2(88) | Sweat equity | Shares issued to employees/directors for know-how / value addition | Reward without cash outflow |
| 2(31) | Deposit | Receipt of money by deposit/loan (with exclusions) | Protects public money lent to companies |
| 2(76) | Related party | Defined web of connected persons/entities | Controls conflicted transactions |
| Sec 8 | Non-profit company | Formed to promote commerce, art, science, charity etc.; profits applied to objects, no dividend | Charitable objects without the "Ltd"/"Pvt Ltd" tag |

**Government company — two traps.** (i) The 51% may be held by Central Govt, **any State Govt(s), or partly Central + partly State** — a mix still counts. (ii) A **subsidiary of a Government company** is *itself* a Government company. It is **not** an "agent of the Government" and its employees are **not** government servants — it remains a *separate legal person* (State-owned ≠ State).

**Section 8 (non-profit) — key features.** Formed to **promote** commerce, art, science, sports, education, research, social welfare, religion, charity, environment protection, etc.; **applies profits/income only to promoting its objects**; **prohibits dividend** to members. In return it gets to **drop "Limited"/"Private Limited"** from its name and enjoys certain exemptions. It is licensed by the Central Government; the licence can be **revoked** for breach, and a Section 8 company **cannot** be a "small company" and has restrictions on alteration of objects.

### 4.8 Lifting / Piercing the Corporate Veil — the counter-doctrine

Recall the fifth problem: limited liability **invites** fraud. The veil is the separation between company and members. Courts (and the statute) **lift** it — treat the company and the humans as one — in these situations:

**A. Judicial (judge-made) grounds — the court looks behind the curtain when:**

1. **Fraud or improper conduct / to defeat the law.** The classic: *Gilford Motor Co. v. Horne (1933)* — Horne signed a non-compete, then formed a company to solicit his old employer's customers, arguing "the *company* is competing, not me." Court saw the company as a **sham/cloak** and enforced the covenant against it. *Jones v. Lipman (1962)* — Lipman contracted to sell land, then transferred it to a company he controlled to escape the sale. Court pierced the veil and ordered specific performance.
2. **Enemy character in wartime.** *Daimler Co. v. Continental Tyre (1916)* — a company registered in England but controlled by German nationals during WWI was treated as an **enemy**; the court looked at *who really controlled it.*
3. **Evasion of tax or a legal obligation.** Where a company is a device to dodge tax (*Sir Dinshaw Maneckjee Petit* — a man formed companies purely to receive his own income and reduce tax; veil lifted). Also *CIT v. Meenakshi Mills* line of reasoning in the revenue context.
4. **Sham / façade / mere agent.** Where the company is really just the **alter ego or agent** of the members with no independent business.
5. **Protecting public interest / preventing injustice.**
6. **Determining the true character / single economic entity** where justice requires treating a group as one (used cautiously; e.g., *State of U.P. v. Renusagar Power Co.* — parent and subsidiary treated as one for a specific statutory purpose).

**A key modern caution — evasion vs concealment (the *Prest* refinement).** English law (*Prest v. Petrodel, 2013*) clarified that the veil is truly *pierced* only to defeat an **evasion** of an *existing* legal obligation using the company as a device; where the issue is merely **concealment** (finding out who is really behind the company) courts use *ordinary* legal tools (agency, trust, attribution) *without* piercing. Indian courts increasingly reason similarly. The exam point: **piercing is a last resort**, invoked only when no ordinary doctrine achieves justice and the company is a *device to evade*.

**B. Statutory grounds — the Act itself lifts the veil:**

| Situation | Section (confirm) | Who becomes personally liable |
|---|---|---|
| **Fraudulent conduct of business** during winding up / otherwise | **Sec 339** (fraudulent trading) | Persons who ran the business with intent to defraud creditors — **personally, without limit** |
| **Misrepresentation in prospectus** | **Sec 34 / 35** | Directors, promoters, experts — for loss to investors |
| **Failure to return application money / mis-statement** | Sec 26, 35 | Persons responsible |
| **Officer in default** provisions | Sec 2(60) & various | The specific human "officer in default" |
| **Misstatement / fraud generally** | Sec 447 | Persons guilty of fraud — punishment + liability |
| **Ultra vires / improper acts** | various | Directors personally |

*Why the statute keeps some grounds explicit rather than leaving all to judges?* For **certainty** — creditors and investors need to know in advance that fraud will not hide behind the shield, and courts need a firm hook.

**Consequence of lifting — what actually happens.** Lifting the veil does **not** dissolve the company or make members owners of its assets generally. It is **issue-specific**: for *that* transaction or *that* liability, the court disregards the separateness and attributes the act/liability to the humans (or treats two companies as one). Outside that issue, the company remains a separate person. *This narrowness is the whole point.*

```mermaid
flowchart TD
    A["Claimant argues the company<br/>is being misused"] --> B{"Ground to lift the veil?"}
    B -->|Fraud / sham / cloak| C["Lift veil — Gilford, Jones"]
    B -->|Evade tax or legal duty| D["Lift veil — Dinshaw Petit"]
    B -->|Enemy character in war| E["Lift veil — Daimler"]
    B -->|Statute commands it| F["Lift veil — Sec 339, 34, 35, 447"]
    B -->|None — just inconvenient for creditor| G["Veil stays — Salomon respected"]
    C --> H["Real humans held personally liable"]
    D --> H
    E --> H
    F --> H
```
*Figure 3 — Veil-lifting decision tree: the shield is withdrawn only for fraud, evasion, enemy character, or a statutory command — never mere convenience.*

---

## 5. Applied Scenarios (exam-style, reasoned to the outcome)

**Scenario 1 — The uninsured sawmill (separate property).**
*Facts:* R owns 100% of the shares of Timber Pvt Ltd, which owns a stock of logs. R insures the logs in **his own name**. A fire destroys them. The insurer refuses to pay.
*Reasoning:* The logs belong to **Timber Pvt Ltd**, a separate legal person (Sec 2(20)). A shareholder — even a 100% shareholder — has **no ownership or insurable interest** in the company's assets (*Macaura v. Northern Assurance*). R insured property he did not legally own.
*Outcome:* Insurer is **not liable**; R cannot recover. The correct step would have been for **the company** to take the policy.

**Scenario 2 — The "private" subsidiary of a public parent.**
*Facts:* Alpha Ltd (a public company) holds 90% of Beta's shares. Beta's articles restrict share transfer, cap members at 200, and ban public invitations — so Beta calls itself a private company and claims private-company relaxations.
*Reasoning:* Under Sec 2(71), a company that is a **subsidiary of a public company is deemed to be a public company**, whatever its articles say. Beta is >50% controlled by Alpha, so Beta is Alpha's subsidiary (Sec 2(87)), hence **deemed public.**
*Outcome:* Beta must comply as a **public company**; it **cannot** claim private-company or small-company relaxations. (Substance over form defeats the pyramid trick.)

**Scenario 3 — The non-compete dodged through a new company.**
*Facts:* H sold his business and signed a covenant not to solicit its customers for 3 years. Six months later he forms "H Solutions Pvt Ltd", of which he is the sole controller, and *the company* starts soliciting those very customers. H argues, "I am not competing — a separate legal person is."
*Reasoning:* The company is a **mere cloak / sham** created to evade a legal obligation (*Gilford Motor v. Horne*). Courts lift the veil where the corporate form is a device to defeat the law.
*Outcome:* The court **lifts the veil**, treats the company as H himself, and **enforces the covenant** (injunction) against both H and H Solutions Pvt Ltd.

**Scenario 4 — Is it "small"?**
*Facts:* Gamma Pvt Ltd has paid-up capital ₹3 crore and turnover ₹50 crore. Delta Pvt Ltd has capital ₹1 crore, turnover ₹20 crore, but is a subsidiary of Omega Ltd.
*Reasoning:* Small company (Sec 2(85)) needs **both** capital **and** turnover under the limits *(≈ ₹4 cr / ₹40 cr — confirm current)*. Gamma fails the **turnover** test (₹50 cr > ₹40 cr) → **not small**. Delta meets the numbers but is a **subsidiary**, which is an **express exclusion** → **not small.**
*Outcome:* Neither qualifies as a small company. (Remember: numbers are AND, and holding/subsidiary is auto-excluded.)

**Scenario 5 — The lone founder wanting a shield.**
*Facts:* S, an Indian resident citizen, wants limited liability but has no partner and no wish to invent a fake second member.
*Reasoning:* An **OPC** (Sec 2(62), Sec 3) lets a single natural person incorporate with limited liability. S must **nominate** a person (for perpetual succession) and can form only **one** OPC. Minimum directors = 1.
*Outcome:* S incorporates an OPC, names a nominee in the memorandum, and gets the shield honestly.

**Scenario 6 — Counting members of a private company (the exclusion trick).**
*Facts:* Zeta Pvt Ltd's register shows 205 names. Of these, **8 are jointly-held pairs** (i.e., 8 pairs of two persons each = 16 names but 8 holdings held jointly), and **12 are present or past employees** who acquired shares while employed and continue to hold them. Zeta fears it has breached the 200-member cap for a private company.
*Reasoning:* Sec 2(68): (a) **joint holders count as ONE member.** The 8 joint pairs occupy 16 names but count as 8 members — a reduction of 8. (b) **Present and past employee-members are EXCLUDED** from the 200 count — remove 12. 
*Working (self-verified):* Start 205 names. Joint holders: 16 names collapse to 8 members → 205 − 8 = **197 members**. Exclude 12 employee-members → 197 − 12 = **185 counted members.** Since **185 ≤ 200**, Zeta is **within the limit** and remains a valid private company. 
*Outcome:* No breach. *Reconciliation:* even with 205 humans on the register, the *legal member count for the cap* is 185. (Trap the examiner sets: counting raw names.)

**Scenario 7 — Exactly 50% is NOT control (the subsidiary threshold).**
*Facts:* P Ltd holds **50%** of the equity voting shares of Q Ltd; the remaining 50% is held by an unrelated investor. P Ltd has **no** right to appoint a majority of Q's Board. Is Q a subsidiary of P? Separately, R Ltd holds **26%** of Q under a shareholders' agreement giving R a veto over Q's key business decisions.
*Reasoning:* Sec 2(87) subsidiary test on votes is **"more than one-half"** — i.e., **> 50%.** P holds *exactly* 50%, which is **not** more than half, and P does not control the Board → **Q is NOT P's subsidiary.** For R: 26% exceeds the **20%** significant-influence threshold *and* there is an agreement to control business decisions → **Q is an ASSOCIATE of R** (Sec 2(6)), provided Q is not R's subsidiary (it is not). 
*Cross-check:* Total voting power adds up (50 + 26 + others), and no single party crosses 50%, so **Q has no holding company** — consistent with "no one controls it." 
*Outcome:* Q is nobody's subsidiary; Q is R's associate. (Twin trap: treating 50% as control, and forgetting the *agreement* limb makes even a sub-20%/low stake an associate.)

**Scenario 8 — Indirect control through a chain (add direct + indirect).**
*Facts:* A Ltd holds **70%** of B Ltd. B Ltd holds **60%** of C Ltd. A Ltd *also* directly holds **15%** of C Ltd. Is C a subsidiary of A?
*Reasoning:* B is A's subsidiary (70% > 50%). C is B's subsidiary (60% > 50%). Under Sec 2(87), A controls voting power in C **"together with its subsidiary"** B. Even ignoring A's direct 15%, A *controls* B which controls 60% of C, so **C is A's subsidiary through the chain.** (A's direct 15% + control of B's 60% only reinforces it.) 
*Self-verify with the layering rule:* A → B → C is **two layers** of subsidiaries below A, which is generally *within* the permitted limit *(confirm current layer cap)*. 
*Outcome:* **C is a subsidiary of A**, and A is the **ultimate holding company** of both B and C. Consolidated accounts of A must include B and C. (Trap: judging C only by A's *direct* 15% and wrongly calling it a mere associate.)

**Scenario 9 — Salomon holds: one-man company, honest use, veil stays.**
*Facts:* M owns 99.9% of NovaTech Pvt Ltd and runs it single-handedly. NovaTech, having genuinely traded, becomes insolvent owing ₹80 lakh to trade creditors. There is **no fraud** — just business failure. Creditors demand M pay personally, arguing "he *is* the company."
*Reasoning:* *Salomon v. Salomon* — a validly incorporated company is a **separate person even if one human owns and runs it entirely.** Mere control, or the company's inability to pay, is **not** a ground to lift the veil (Trap 8). No fraud, sham, evasion, or statutory trigger is present. 
*Outcome:* Creditors **cannot** reach M personally; their claim is against NovaTech's assets only. M's downside is limited to his unpaid share money (here, nil if fully paid). *Contrast Scenario 3:* there, the company was a **cloak to evade an existing obligation** — here it is a genuine business that failed. That single difference flips the result. 

---

## 6. Procedure / Compliance Summary — Choosing and Forming the Right Type

While detailed incorporation is Chapter 2, the *definitional choices* made at formation are here:

```mermaid
flowchart TD
    A["How many founders<br/>and how much public money?"] --> B{"Just one founder?"}
    B -->|Yes, Indian resident citizen| C["Form an OPC<br/>1 member + nominee"]
    B -->|No| D{"Will you invite the public<br/>to subscribe?"}
    D -->|No, closed circle <=200| E["PRIVATE company<br/>min 2 members, 2 directors"]
    D -->|Yes, raise from public| F["PUBLIC company<br/>min 7 members, 3 directors"]
    E --> G{"Capital and turnover<br/>both under limits?"}
    G -->|Yes and not subsidiary/holding| H["Enjoy SMALL company relaxations"]
    G -->|No| I["Ordinary private company compliance"]
    F --> J{"List securities on<br/>a stock exchange?"}
    J -->|Yes| K["LISTED company<br/>SEBI LODR + heaviest compliance"]
    J -->|No| L["Unlisted public company"]
```
*Figure 4 — Formation decision tree: the founder count and the appetite for public money drive the legal category, which drives the compliance load.*

A second axis runs *across* that tree — **how members' liability is limited** — which is chosen at drafting of the memorandum, independent of private/public:

```mermaid
flowchart TD
    A["How should members'<br/>liability be capped?"] --> B{"Any cap at all?"}
    B -->|No cap| U["UNLIMITED company<br/>members fully liable<br/>lighter regulation"]
    B -->|Yes| C{"Cap measured by what?"}
    C -->|Unpaid amount on shares| S["Company LIMITED BY SHARES<br/>most common trading form"]
    C -->|Fixed sum promised<br/>payable only on winding up| G["Company LIMITED BY GUARANTEE<br/>clubs, charities, associations"]
    G --> H{"Also has share capital?"}
    H -->|Yes| GS["Guarantee + share capital<br/>member liable for both"]
    H -->|No| GN["Pure guarantee company"]
```
*Figure 5 — The liability axis: unlimited, limited by shares, or limited by guarantee with or without share capital.*

**Formation minimums at a glance:**

| Type | Min members | Max members | Min directors | Public invitation? |
|---|---|---|---|---|
| OPC | 1 | 1 | 1 | No |
| Private | 2 | 200 | 2 | No |
| Public | 7 | No limit | 3 | Yes |

**Key forms/registers (indicative — detailed in Ch. 2):** SPICe+ (INC-32) for incorporation, INC-33/34 (e-MOA/e-AOA), AGILE-PRO (for GSTIN/EPFO/ESIC/bank account), and the ROC register that makes company status publicly verifiable. *Confirm current form names.*

**Consequences of the classification on ongoing compliance (why the choice is not cosmetic):**

| Dimension | Private (esp. small) | Public / Listed |
|---|---|---|
| Min directors | 2 (OPC 1) | 3 (listed: often more + independent directors) |
| Board meetings/yr | 4 (small: 2) | 4 (listed: with committees) |
| Cash-flow statement | Not required if small | Required |
| Public deposits | Tighter limits/from members | Broader regime under Sec 73–76 |
| SEBI LODR | No | Listed: Yes |
| Auditor rotation (Sec 139(2)) | Not for small/OPC | Applies to prescribed public cos |

*Confirm all specifics against current ICAI material.*

---

## 7. Connections — How This Chapter Wires Into the Rest of the Law

- **Chapter 2 (Incorporation, MOA/AOA):** The definitions here decide *which* incorporation route, capital clause, and object clause you use. "Separate legal entity" is *born* at incorporation (Sec 9).
- **Prospectus & Public Deposits:** "Public company" and "listed company" status are the triggers for prospectus rules (Sec 23–42) and deposit rules — because those chapters are about **public money**, the very thing these categories track.
- **Accounts & Audit:** Holding/subsidiary/associate (Sec 2(6), 2(46), 2(87)) drive **consolidated financial statements** (Sec 129) — the whole point of defining control is to force the group's true picture into the accounts. Small-company/OPC status drives *reliefs* (no cash-flow statement, fewer meetings, no auditor rotation).
- **Directors:** Minimum director counts (1/2/3) and "officer in default" (Sec 2(60)) connect to Board composition and personal liability.
- **Related-party & conflicted transactions:** Sec 2(76) "related party" and the holding/subsidiary/associate web feed Sec 188 (related-party transactions) and loan-to-director rules.
- **Winding up / IBC:** Veil-lifting for **fraudulent trading (Sec 339)** connects to insolvency; the shield's limits matter most when the company is dying.
- **SEBI Act & LODR:** "Listed company" hands off to the securities-law regime; "recognised stock exchange" hands off to the SCRA 1956.
- **Other Laws (Interpretation of Statutes):** Reading definitions ("means" vs "includes", inclusive vs exhaustive) is itself an examinable skill in the Other Laws part — and this chapter is where you first apply it.

---

## 8. Traps & Examiner Tricks

1. **Minimum paid-up capital is GONE.** The 2015 amendment removed the ₹1 lakh/₹5 lakh minimums. Questions quoting them as *current* are testing whether you know the amendment. There is **no** minimum paid-up capital now.
2. **Small company numbers are "AND", exclusions are automatic.** Both capital **and** turnover must be under the limits. A holding **or** subsidiary company, a Section 8 company, and a company under a special Act can **never** be small — regardless of their numbers.
3. **Subsidiary-of-public is deemed public.** Even with private-company articles, a subsidiary of a public company is public (Sec 2(71)). Classic trap.
4. **Member count: "200" vs "50".** Under the 2013 Act a private company limit is **200** (it was 50 under the 1956 Act). Old figure = trap. Also: **past/present employee-members are excluded** from the count, and **joint holders count as one.**
5. **Associate vs Subsidiary threshold.** Associate = **≥20%** voting power (significant influence, *or* control of business decisions by agreement). Subsidiary = **>50%** or **board control**. Do not confuse "significant influence" (20%) with "control" (50%).
6. **Macaura trap.** A 100% shareholder still does **not** own the company's assets and has **no** insurable interest in them.
7. **Salomon holds even for one-man companies.** A validly incorporated company is separate even if one person owns and runs everything. Do **not** lift the veil merely because one person controls the company — you need fraud/evasion/sham/statute.
8. **Veil-lifting is narrow.** Mere inconvenience to a creditor, or the company simply being unable to pay, is **not** a ground. Look for **fraud, sham, evasion, enemy character, or an express statutory provision.**
9. **"Body corporate" ≠ "company".** Body corporate (Sec 2(11)) is broader — includes foreign companies and LLPs — but **excludes** co-operative societies and certain notified bodies. A question may hinge on this width.
10. **OPC restrictions.** Only a **natural person, Indian citizen and resident**; can form **one** OPC and be nominee in **one**; **cannot** do NBFI/invest-in-securities activity; a **minor** cannot be member/nominee. The old ₹50 lakh/₹2 crore mandatory-conversion thresholds were **relaxed** in 2021 — check current position and the revised **residency day-count**.
11. **Listed definition carve-out (2020).** Some companies listing only specified securities (e.g., only certain debt) may be excluded from "listed" for certain purposes. "Listed" ≠ "listed equity". Watch the update.
12. **Perpetual succession ≠ immortality.** The company survives *members'* deaths, but it **can** be wound up / struck off — it lives *until the law ends it*, not forever unconditionally.
13. **"More than half" vs "at least half".** Subsidiary voting test is **> 50%**; **exactly 50%** is NOT a subsidiary on votes. Similarly Government company is **≥ 51%** (not "more than half loosely").
14. **Voting power ≠ shareholding %.** Sec 2(87)/2(6) turn on **voting power**, which can diverge from equity percentage where preference or differential-rights shares vote. Read for *votes*, not just holding.
15. **Common seal is optional (2015).** Do not assume a document needs a seal; two directors (or a director + CS) can execute.
16. **Member ≠ shareholder always.** Subscribers to the MOA are members on incorporation before allotment; register-of-members entry is what makes a "member".
17. **Government company is still a separate person.** Its employees are **not** government servants; State ownership does not make it "the State" for every purpose.
18. **OPC is a private company.** It gets private-company treatment *plus* extra OPC reliefs — do not treat it as a wholly separate species with no private-company rules.
19. **Guarantee amount cannot be called while a going concern.** In a company limited by guarantee, the guaranteed sum is payable **only on winding up** — a question implying it funds day-to-day operations is wrong.

---

## 9. First-Principles Recap

Strip everything away and rebuild it from zero:

1. Big, long-lived, risky business needs **money from many strangers**. Strangers won't invest if the venture **dies with a person**, **ruins them personally**, or is a **black box they cannot check.**
2. The law's fix: **invent an artificial legal person** — separate, immortal-until-wound-up, owning its own assets, and **registered publicly** so outsiders can verify it. From this one fiction fall **separate entity, perpetual succession, separate property, capacity to sue, and (via a promise-cap) limited liability.** *(Salomon, Lee, Macaura.)*
3. That person is **not a citizen and has no mind of its own** — so the law must always answer "**whose act/intent is attributed to it?**", and it must choose **how liability is capped** (unlimited → guarantee → shares).
4. The fiction must be **regulated in proportion to the public interest at stake** — hence the categories. One founder → **OPC** (a private company for a solo owner). Closed circle, no public money → **private**; if tiny → **small** (relaxations). Public money → **public**; if traded on an exchange → **listed** (heaviest load).
5. Once companies can **own other companies**, control hides in **pyramids** — so the law defines control precisely: **≥20% = associate (influence)**, **>50% or board control = subsidiary/holding**, counts **direct + indirect** control, **limits layers**, and forces the true group into **consolidated accounts.**
6. The shield **invites fraud**, so the law keeps a **counter-power**: **lift the veil** for fraud, sham/cloak, evasion of law/tax, enemy character, or where a **statute** (Sec 339, 34, 35, 447) commands — and hold the **real humans** liable. But this power is **narrow and issue-specific**, or the shield (and investment) would be worthless.

If you can regenerate the categories and the veil doctrine from *"we invented a public, checkable person, and we must both trust and police that fiction,"* you never need to memorise them.

---

## 10. Quick-Revision Sheet

**Core sections**

| Section | Term | Key number / rule |
|---|---|---|
| 2(20) | Company | Incorporated under this/previous Act |
| 2(68) | Private company | Restricts transfer; **max 200** members; no public invitation; **min 2** |
| 2(71) | Public company | Not private; subsidiary of public = **deemed public**; **min 7**; **min 3 directors** |
| 2(62) | OPC | **One** member + nominee; natural Indian resident citizen; one OPC only; **min 1 director**; is a *private company* |
| 2(85) | Small company | Private + capital **≤ ₹4 cr** *and* turnover **≤ ₹40 cr** *(confirm)*; excludes public/holding/subsidiary/Sec 8/special-Act; status is *dynamic* |
| 2(87) | Subsidiary | Control of **Board** OR **>50%** voting power (direct + indirect); layers limited (≈2) |
| 2(46) | Holding | Company whose subsidiaries exist (incl. body corporate) |
| 2(6) | Associate | **Significant influence = ≥20%** voting power *or* control of decisions by agreement (not subsidiary); JV included |
| 2(52) | Listed | Any securities listed on recognised stock exchange (some 2020 carve-outs; "listed" ≠ "listed equity") |
| 2(11) | Body corporate | Incl. foreign cos & LLPs; excl. co-op societies, specified bodies |
| 2(45) | Government company | **≥51%** Govt paid-up capital (Central/State/both); subsidiary of Govt co is also a Govt co |
| 2(42) | Foreign company | Incorporated outside India + place of business/operations (incl. electronic mode) in India |
| 2(55) | Member | Subscriber to MOA / name in register / beneficial owner in depository |
| 2(60) | Officer in default | Human on whom default liability is pinned |
| Sec 8 | Non-profit | Charitable objects; no dividend; may drop "Ltd"; cannot be "small" |
| Sec 3 | Formation | Public **7** / Private **2** / OPC **1** (memory: **7-2-1**) |
| Sec 9 | Effect of incorporation | Separate legal person, perpetual succession, common seal (optional), capacity to sue |

**Formation minimums (7-2-1):** Public 7 members / 3 directors • Private 2 / 2 • OPC 1 / 1. Max members: Private 200, OPC 1, Public unlimited.

**Control ladder:** ≥20% (or agreement) = **Associate** (influence) → >50% or board control = **Subsidiary/Holding** (control). Count **direct + indirect**; exactly 50% ≠ subsidiary on votes.

**Liability axis:** Unlimited (Sec 2(92)) → Limited by guarantee (winding-up backstop, not working capital) → Limited by shares (unpaid amount). Guarantee ± share capital possible.

**Characteristics of a company:** Separate legal entity • Limited liability • Perpetual succession • Separate property • Common seal (optional) • Capacity to sue & be sued • Transferable shares • Artificial person, *not* a citizen, acts through agents.

**Veil-lifting grounds:** Fraud/sham/cloak (*Gilford, Jones*) • Tax/obligation evasion (*Dinshaw Petit*) • Enemy character (*Daimler*) • Single economic entity where justice requires (*Renusagar*) • Statute (Sec **339** fraudulent trading; Sec **34/35** prospectus; Sec **447** fraud). **Not** lifted for mere creditor inconvenience; **issue-specific** and **narrow** (evasion, not mere concealment — *Prest*).

**Landmark cases:** *Salomon* (separate entity, even one-man co) • *Lee* (member can also be employee) • *Macaura* (no insurable interest in company property) • *Gilford / Jones* (sham to evade obligation) • *Daimler* (enemy character) • *Dinshaw Petit* (tax evasion) • *Prest v. Petrodel* (evasion vs concealment).

**Amendment flags to verify in current ICAI material / bare Act:** no minimum paid-up capital (2015) • common seal optional (2015) • small-company limits (₹4 cr / ₹40 cr) • OPC conversion thresholds removed + residency day-count revised (2021) • subsidiary "total voting power" wording & layer limit (2017) • associate "voting power"/JV (2017) • listed-company carve-outs (2020).

---

*End of Chapter 01. Next: Chapter 02 — Incorporation of a Company, MOA & AOA — where this artificial person is actually born.*
