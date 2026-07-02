<!-- v2-deep -->

# Chapter 31 — Redemption of Preference Shares

## 1. The Problem

A company issued 10,000 preference shares of ₹100 each some years ago to raise ₹10,00,000. Preference shares are a strange animal: they behave like debt (fixed dividend, first claim on repayment) but they legally sit inside **share capital**. Now the promised redemption date has arrived and the company wants to pay these shareholders back their ₹10,00,000 and send them on their way.

Here is the tension. A creditor who lent the company money can be repaid freely — that is what a loan is. But **share capital is not a loan**. Share capital is the permanent buffer that stands between the company and its creditors. Trade creditors, bankers, and debenture-holders extended credit partly *because* they could see ₹10,00,000 of capital that shareholders had locked in and could not simply walk away with. That locked-in capital is the creditors' security cushion.

If the company is now allowed to hand ₹10,00,000 of that cushion back to preference shareholders, the creditors' security silently shrinks. Total assets fall by ₹10,00,000 (cash goes out), and the buffer protecting creditors evaporates. The preference shareholders — who ranked *above* equity shareholders — get out whole, while the company's remaining creditors are left with a thinner safety net than they bargained for.

So the real problem is not "how do we cut a cheque." The problem is: **how do we let preference shareholders exit without secretly picking the creditors' pockets?** The law's answer is a beautifully engineered piece of accounting machinery. This chapter is about understanding that machine so well that you can rebuild it from scratch in the exam, rather than memorising a list of conditions you don't understand.

**Why do companies redeem at all?** Because preference capital is expensive, permanent-looking money. A company that raised 12% preference capital in a high-interest era may, once cheaper funds are available, want to retire it — exactly like refinancing a loan. Preference shares are therefore a *bridge* instrument: equity in legal form, debt in economic behaviour, deliberately built to be temporary. Section 55's very existence (banning irredeemable preference shares) tells you the legislature wants this money to be repayable but repaid *safely*. Keep this dual nature in mind: it explains why the accounting borrows the vocabulary of capital (CRR, capital maintenance) while the commercial motive is pure debt-refinancing.

## 2. The Core Idea (analogy)

Think of a company's balance sheet as a **dam**. On one side is the reservoir of assets. The dam wall has a marked line called "**capital**" — a legal minimum water level below which the company is not allowed to release water to shareholders. Creditors camp downstream trusting that the water will never fall below that line without their consent.

Preference shareholders are like a group of people who put water *into* the reservoir and now want their water back. If we just open a gate and let their water flow out, the reservoir level drops below the capital line — the creditors' guarantee is broken.

The law's trick is the **lock-and-refill rule**:

- You may release the preference shareholders' water **only if** you *either* (a) simultaneously pour in **new water** from a fresh share issue, *or* (b) release water that is genuinely **surplus** — profits available for dividend, i.e. water sitting *above* the capital line that could legally have been drained away as dividend anyway.
- And crucially, if you drain surplus (profit) water, you must **build the dam wall higher by the same amount** so the marked "capital" line rises to compensate. That wall-raising is the **Capital Redemption Reserve (CRR)**.

The CRR is the heart of the whole scheme. It is a paper wall built out of profits that says: "We took ₹10,00,000 of redeemable capital off the books, but we have replaced it with ₹10,00,000 of an equally undistributable reserve." The creditors' cushion is preserved to the last rupee. Nothing left the protected zone on a net basis — capital was *substituted*, not *reduced*.

**Sharpen the analogy for the two extremes.** If you refill entirely with *new water* (fresh issue of equal face value), you never touch the surplus and there is nothing to wall-up: **CRR is nil**. If you refill entirely from *surplus* (no fresh issue), you must wall-up the whole amount: **CRR equals the full face value**. Every real problem is a blend of these two, and the CRR is simply "the part you funded from surplus." Hold this one sentence and you never have to memorise a formula: *CRR is whatever slice of face value did not come in as new share capital.*

## 3. Why It's Built This Way

Every design choice in Section 55 falls out of the single principle of **capital maintenance**: *the capital contributed by members must be maintained intact for the protection of creditors and may not be returned to members except through legally supervised procedures.*

Normally, returning capital to shareholders requires the heavy machinery of a **capital reduction** (Section 66) — a Tribunal-supervised process with creditor objections, or a court-supervised **buy-back** regime (Section 68). Those exist precisely because giving capital back to members is dangerous.

Redemption of preference shares is a **standing, pre-authorised exception** to this. The legislature said: "We will let you redeem preference shares *without* going to the Tribunal, *provided* you follow a self-enforcing recipe that automatically keeps the creditors' cushion intact." Section 55 *is* that recipe. Understand it as "capital reduction made safe enough to do without a court" and every rule becomes obvious:

- **Redeem only fully paid shares** → you can't return capital that was never fully contributed; a partly-paid share still owes the company money.
- **Redeem only out of profits or a fresh issue** → the two sources are the only two ways to redeem *without* net-shrinking the capital cushion. Fresh issue literally refills. Profits are, by definition, the distributable surplus above the capital line.
- **Create CRR when redeeming out of profits** → this is the "raise the wall" step that converts distributable profit into non-distributable reserve, plugging the exact hole the redemption created.
- **CRR can be used only for bonus shares** → once you have converted profit into a capital-like reserve to protect creditors, you must not let it leak back out as dividend. The only permitted exit is turning it into fully paid bonus *shares* — which keeps it locked inside capital forever.

This is why the topic is conceptually elegant rather than arbitrary. It is a closed accounting loop designed so that `Capital + Non-distributable reserves` never falls, no matter how the redemption is financed.

**A deeper "why" on the choice of sources.** Ask: why not let the company redeem out of *any* asset, e.g. by selling a building and paying shareholders? Because the *source* rule is not about where the cash comes from — cash is fungible — it is about which *reserve* absorbs the debit. When you redeem, some account on the liabilities-and-equity side must fall to keep the balance sheet balanced (assets down by cash paid). The law dictates that the account which falls must be a *distributable* one (free reserves / P&L) so that shareholders lose distributable wealth, not creditors' protection. The CRR then re-freezes that fallen distributable amount into a locked form. In other words, redemption *forces shareholders to give up dividend capacity equal to the capital returned* — that is the price of getting capital out without a Tribunal. This is the single most powerful sentence for reasoning about any tricky variation.

## 4. Full Technical Content

### 4.1 What may be redeemed and the ban on irredeemable preference shares

Under **Section 55(1) of the Companies Act, 2013**, a company limited by shares **cannot issue irredeemable preference shares** (i.e., preference shares that are never repayable). Under **Section 55(2)**, a company may issue redeemable preference shares that are **liable to be redeemed within a period not exceeding 20 years** from the date of issue.

- **Exception (infrastructure projects):** A company engaged in setting up and dealing with infrastructural projects may issue preference shares redeemable **beyond 20 years but not exceeding 30 years**, subject to redemption of a minimum 10% of such shares per year from the 21st year onwards (on a proportionate basis) at the option of the shareholders. *(Confirm the exact 10%/proportionate wording in current ICAI material, as rules are periodically updated.)*
- Redeemable preference shares may be redeemed at **par** or at a **premium**.
- **Authority in Articles:** A company can issue redeemable preference shares only if it is **authorised by its Articles of Association**. Absence of such authority is itself a bar — a favourite one-mark theory point.
- **No redemption of partly-paid shares:** flows from Section 55(2)(a); see the three conditions below.

**Redemption is not a fresh commercial decision to reduce capital — it is the *honouring of a pre-agreed term*.** The shares were *born* redeemable. That is precisely why no Tribunal is needed: the "return of capital" was baked into the contract at issue and consented to by the world at large through public filing. Contrast Section 66 capital reduction, which is a *new* decision to return capital the world did not sign up for — hence the court.

### 4.2 The three conditions of Section 55(2)

Redemption is subject to the following mandatory conditions:

| # | Condition | Reason (first principles) |
|---|-----------|---------------------------|
| 1 | **Only fully paid-up** preference shares may be redeemed. | You cannot return capital not yet fully contributed. |
| 2 | Redemption must be **out of profits available for dividend**, **or out of the proceeds of a fresh issue** of shares made *for the purposes of redemption*. | These are the only two funding sources that keep the capital cushion intact. |
| 3 | Where redeemed **out of profits**, a sum equal to the **nominal (face) value** of shares redeemed must be transferred to the **Capital Redemption Reserve (CRR)**. | Substitutes the vanished capital with an equal undistributable reserve. |

**What counts as "profits available for dividend"?** These are **free reserves** and the credit balance of the **Statement of Profit and Loss** — amounts the company could lawfully have paid out as dividend. Illustrative *usable* items and *non-usable* items:

| Available for CRR (distributable) | NOT available for CRR |
|---|---|
| General Reserve | Securities Premium |
| Surplus in Statement of P&L (credit balance) | Capital Reserve |
| Dividend Equalisation Reserve | Revaluation Reserve |
| Workmen Compensation Reserve (excess, if free) | Capital Redemption Reserve (existing) |
| Voluntary reserves out of profits | Profit prior to incorporation / capital profits |

The acid test for any reserve: *"Could this have been distributed as dividend?"* If yes, it can create CRR. If it is a statutory/capital reserve that dividend rules forbid distributing, it cannot. This single question resolves nearly every "which reserves are available" trap.

### 4.3 The Capital Redemption Reserve (CRR)

**Amount to transfer to CRR = Nominal value of preference shares redeemed − Nominal value of fresh equity/preference shares issued for the purpose of redemption.**

In words: CRR plugs *only the part of the face value that was NOT refilled by a fresh issue*. If the entire redemption is financed by a fresh issue of equal face value, CRR is nil (the wall was refilled directly). If none is financed by fresh issue, CRR equals the full face value redeemed.

- CRR is created by transferring from **free reserves / distributable profits** (e.g., General Reserve, Surplus in Statement of P&L, Dividend Equalisation Reserve).
- **Securities Premium** and **Capital Reserve** are *not* free profits available for dividend and therefore **cannot** be used to create CRR.
- **Use of CRR:** By **Section 55(4)** read with **Section 63**, CRR may be used **only** for issuing **fully paid bonus shares** to members. It is treated as paid-up share capital for this purpose. It cannot be used to pay dividends, write off losses, or write off expenses.

The CRR is, in effect, a statutory quarantine: profits that could have been paid out as dividend are permanently locked into a capital-equivalent reserve, so the redemption does not net-reduce the protected fund.

**Fresh issue of *preference* shares to redeem preference shares — does it reduce CRR?** Yes. The rule says "fresh issue of *shares*," not "fresh issue of equity shares." A fresh issue of *new* redeemable preference shares to fund redemption of *old* preference shares also refills the capital and reduces CRR by its nominal value. The identity is about total *share capital* coming in, regardless of class. (Commercially this is just rolling over preference capital at a new rate.)

**Does a fresh issue of debentures reduce CRR? No.** Debentures are debt, not share capital — they do not refill the *capital* cushion, they add to creditors. If redemption is funded by issuing debentures, the **entire face value still goes to CRR** (the redemption is treated as fully out of profits for CRR purposes, because no *capital* came in). Classic trap: examiner funds redemption partly by a debenture issue and hopes you net it against CRR. Do not.

**"Available profits" vs "amount actually transferred."** The law requires transferring an amount *equal to the nominal value redeemed* to CRR when redeeming out of profits. You cannot transfer less to save reserves, and transferring more is meaningless. The amount is mechanically fixed by the identity, not a matter of discretion.

### 4.4 Premium payable on redemption

If shares are redeemed at a premium, that premium must be **provided for** (found) before redemption. The premium is **not** part of the CRR computation (CRR only covers *nominal* value). Sources for premium on redemption:

- **Securities Premium Account** (permitted by Section 52 for this purpose), and/or
- **Profit & Loss Account / free reserves.**

**Order/preference in practice:** Companies typically use Securities Premium first (as it is otherwise restricted-use), then free profits. However, note the important distinction between this topic and debentures. For **preference shares**, the Companies Act 2013 permits Securities Premium to be applied towards premium on redemption of preference shares under Section 52(2)(d)... *(Note: Section 52(2)(d) references premium on redemption of preference shares/debentures — confirm the exact clause wording in current ICAI study material, as there has been examiner debate on whether premium on redemption of preference shares must come only from profits for certain company types.)*

For the CA Intermediate exam, the standard treatment is: **Premium on redemption of preference shares can be met out of Securities Premium Account and/or Profit & Loss (free reserves).**

**Why is the premium NOT substituted by CRR?** Because the premium is not *return of capital* — it is an *extra reward* to the exiting shareholder, economically like a final bonus dividend. The capital that was locked in was only the *face value*; that is all creditors ever relied on. Paying an additional premium out of distributable profit is exactly like paying a dividend: it reduces distributable surplus but never touches the protected capital line, so no wall-raising (CRR) is needed for it. This is why premium and CRR travel on completely separate tracks and must never be added together.

**Watch the direction of the Securities Premium balance.** Using Securities Premium to fund the redemption premium *reduces* the Securities Premium balance. But issuing fresh shares at a premium *increases* it. In a problem with both, net the two movements carefully when you present the closing balance (Example 3 does exactly this).

### 4.5 The minimum fresh issue calculation

This is the single most tested computation. The exam asks: *"What is the minimum amount of fresh shares the company must issue to carry out the redemption?"*

You need fresh issue when **profits available for redemption are insufficient** to fully back the redemption. The logic is a resource-balancing exercise.

**Step 1 — Identify the total funds needed at face value = Nominal value of preference shares to be redeemed.**

**Step 2 — Identify profits *available* for creating CRR** (free reserves + P&L surplus that management is willing/able to use). Note: money earmarked for premium on redemption reduces the profit pool if premium is met from profits.

**Step 3 — The governing identity:**

> **Nominal value redeemed = Fresh issue (nominal) + CRR (from profits)**

Because CRR is capped by the profits actually available:

> **Minimum fresh issue (nominal) = Nominal value redeemed − Profits available for CRR**

**Step 4 — Adjust for issue price.** If fresh shares are issued at a premium, the *nominal* value drives the CRR/redemption identity, but the *cash raised* = nominal + premium. If issued at a premium, you need fewer shares to raise a given amount of cash — but for the face-value substitution identity, always work with **nominal** value first, then convert to number of shares / cash as asked.

**Cash-sufficiency cross-check:** The company must also have enough *cash* to actually pay the redemption amount (face + premium). Sometimes the binding constraint is cash, not the CRR identity. Always verify the bank balance can absorb: `Cash out = Redemption amount (face + premium)` and `Cash in = Fresh issue proceeds (nominal + premium on new issue)`.

**Why "minimum"? Because fresh issue is the company's *last resort*.** Issuing new shares dilutes existing equity holders and costs money; using up free reserves is "cheaper" to the company (it only sacrifices dividend capacity it might not have used). So the rational company burns *all* available profit first and issues *only* the unavoidable shortfall as fresh shares. That is why the formula subtracts profits from face value — it assumes profits are consumed to the maximum permitted, and fresh issue fills what's left. If a problem imposes a *retention* ("keep ₹X of General Reserve"), that ₹X is walled off from the profit pool, *raising* the minimum fresh issue by exactly ₹X.

**The premium-on-new-issue subtlety.** When the examiner asks for "minimum fresh issue" and lets you issue at a premium, be careful what "minimum" means:
- Minimum **nominal (face) value** of fresh issue is fixed by the CRR identity and is *unaffected* by the issue premium — because premium on the new issue goes to Securities Premium, which cannot create CRR.
- Minimum **number of shares** = minimum nominal ÷ face value per share.
- Minimum **cash raised** rises if issued at a premium, but that extra cash is often *needed* to fund the premium on redemption / maintain a bank balance.

So "issue at a premium" never lets you issue *fewer* shares for the CRR rule; it only changes the cash mathematics. Students routinely get this backwards.

### 4.6 Complete set of journal entries

Below is the master template. Not every entry appears in every problem — pick the ones the facts require.

**(a) If any preference shares are not yet fully called/paid — make them fully paid first** (only fully paid shares are redeemable):

```
Preference Share Final Call A/c        Dr.
   To Preference Share Capital A/c
Bank A/c                               Dr.
   To Preference Share Final Call A/c
```

**(b) Fresh issue of shares for the purpose of redemption:**

At par:
```
Bank A/c                               Dr.   [nominal]
   To Equity/Preference Share Capital A/c    [nominal]
```

At premium:
```
Bank A/c                               Dr.   [nominal + premium]
   To Equity/Preference Share Capital A/c    [nominal]
   To Securities Premium A/c                 [premium]
```

**(c) Amount due to preference shareholders becomes payable** (transfer capital + premium on redemption to a shareholders' liability account):

```
Redeemable Preference Share Capital A/c   Dr.   [face value]
Premium on Redemption of Pref. Shares A/c Dr.   [premium payable]
   To Preference Shareholders A/c                [face + premium]
```

**(d) Provide for the premium on redemption** (source it from Securities Premium / free reserves):

```
Securities Premium A/c                 Dr.   [up to available]
Profit & Loss A/c (or General Reserve) Dr.   [balance]
   To Premium on Redemption of Pref. Shares A/c
```

**(e) Pay the preference shareholders:**

```
Preference Shareholders A/c            Dr.
   To Bank A/c
```

**(f) Transfer to CRR the nominal value redeemed but NOT covered by a fresh issue:**

```
General Reserve A/c / Profit & Loss A/c   Dr.
   To Capital Redemption Reserve A/c
```
Amount = Nominal value redeemed − Nominal value of fresh issue made for redemption.

**(g) Later — using CRR for bonus shares (if asked):**

```
Capital Redemption Reserve A/c         Dr.
   To Bonus to Shareholders A/c
Bonus to Shareholders A/c              Dr.
   To Equity Share Capital A/c
```

**Sequencing discipline (why the order matters):** The logical order is (a) → (b) fresh issue *before* payment so the cash is in the bank → (c) crystallise the amount due → (d) provide premium → (e) pay → (f) create CRR. Two rules of thumb the examiner rewards: (i) **cash must arrive before it leaves** — always show the fresh issue receipt before the payment to shareholders; (ii) **CRR is created last**, once you know exactly how much face value was *not* refilled by fresh issue. Creating CRR before knowing the fresh issue is a sequencing error.

**A note on the "Premium on Redemption" account.** Some textbooks skip the separate `Premium on Redemption of Preference Shares A/c` and directly debit Securities Premium / P&L in entry (c). Both are acceptable; the two-account version (used above) is cleaner because it separates *the obligation* (entry c) from *the funding of it* (entry d). Use whichever your problem's structure favours, but be consistent.

### 4.7 Decision flow

```mermaid
flowchart TD
    A["Preference shares due for redemption"] --> B["Are they fully paid?"]
    B -->|"No"| C["Call up and collect balance first"]
    B -->|"Yes"| D["Choose funding source"]
    C --> D
    D --> E["Enough free profits to cover full face value?"]
    E -->|"Yes"| F["Redeem fully out of profits - transfer full face value to CRR"]
    E -->|"No"| G["Make a fresh issue for the shortfall"]
    G --> H["CRR = Face value redeemed minus fresh issue nominal"]
    F --> I["Provide premium on redemption from Securities Premium or profits"]
    H --> I
    I --> J["Pay shareholders and complete redemption"]
```
*Figure 1 — The redemption decision tree: fully-paid gate, then the profit-versus-fresh-issue funding choice that drives the CRR amount.*

### 4.8 The two funding sources as a balance — a mental model

```mermaid
flowchart LR
    A["Face value of preference shares redeemed"] --> B["Split into two funding buckets"]
    B --> C["Bucket 1 - Fresh issue nominal - refills capital directly"]
    B --> D["Bucket 2 - Free profits transferred to CRR"]
    C --> E["Capital plus CRR after equals Capital before"]
    D --> E
    F["Premium on redemption - separate side payment"] --> G["Funded from Securities Premium then free profits - never CRR"]
```
*Figure 2 — Every rupee of face value must land in one of two buckets fresh capital or CRR while the premium travels on a completely separate track.*

## 5. Worked Examples

### Example 1 — Redemption fully out of profits, at par (the base case)

**Facts.** Sunrise Ltd. has 20,000 8% Redeemable Preference Shares of ₹100 each, fully paid, due for redemption at par. The company has a General Reserve of ₹30,00,000 and adequate cash. No fresh issue is made.

**Reasoning.** Redemption amount = 20,000 × ₹100 = ₹20,00,000. Since no fresh shares are issued, the *entire* nominal value must be substituted by CRR to keep the capital cushion intact. Profits available (₹30,00,000) exceed ₹20,00,000, so full redemption out of profits is possible.

CRR required = ₹20,00,000 − ₹0 (fresh issue) = **₹20,00,000.**

**Journal entries.**

```
1. Redeemable Preference Share Capital A/c   Dr.  20,00,000
      To Preference Shareholders A/c                  20,00,000

2. Preference Shareholders A/c               Dr.  20,00,000
      To Bank A/c                                      20,00,000

3. General Reserve A/c                       Dr.  20,00,000
      To Capital Redemption Reserve A/c               20,00,000
```

**Reconciliation.** Before: Pref Capital ₹20,00,000 + General Reserve ₹30,00,000 = ₹50,00,000 in the "protected + reserves" block. After: Pref Capital ₹0 + General Reserve ₹10,00,000 + CRR ₹20,00,000 = ₹30,00,000. The drop of ₹20,00,000 exactly equals the cash paid out (₹20,00,000) — assets fell by the same amount, so the accounting equation holds. Critically, the *undistributable* fund (Capital + CRR) went from ₹20,00,000 (capital) to ₹20,00,000 (CRR): **creditors' cushion unchanged.** General Reserve fell only because distributable profit was converted, not because protection was lost.

### Example 2 — Partly out of fresh issue, at par (minimum fresh issue)

**Facts.** Meridian Ltd. wishes to redeem its 30,000 9% Redeemable Preference Shares of ₹100 each at par. The company's free reserves available for redemption are: General Reserve ₹12,00,000 and Surplus in Statement of P&L ₹6,00,000. It wants to keep a minimum General Reserve of ₹2,00,000 after redemption for operational comfort. Any shortfall is to be met by a fresh issue of equity shares of ₹10 each at par. Determine the minimum fresh issue and pass entries.

**Step 1 — Redemption amount (face).** 30,000 × ₹100 = ₹30,00,000.

**Step 2 — Profits usable for CRR.**
- General Reserve available for use = ₹12,00,000 − ₹2,00,000 (retained) = ₹10,00,000.
- P&L Surplus usable = ₹6,00,000.
- Total profits usable = ₹16,00,000.

**Step 3 — Minimum fresh issue (nominal).**
> Minimum fresh issue = Face value redeemed − Profits available for CRR
> = ₹30,00,000 − ₹16,00,000 = **₹14,00,000.**

Number of equity shares = ₹14,00,000 / ₹10 = **1,40,000 shares.**

**Step 4 — CRR.** CRR = Face redeemed − Fresh issue nominal = ₹30,00,000 − ₹14,00,000 = ₹16,00,000 (exactly the profits transferred). ✔

**Journal entries.**

```
1. Bank A/c                               Dr.  14,00,000
      To Equity Share Capital A/c                 14,00,000
   (Fresh issue of 1,40,000 equity shares of Rs.10 at par for redemption)

2. Redeemable Preference Share Capital A/c Dr.  30,00,000
      To Preference Shareholders A/c              30,00,000

3. Preference Shareholders A/c            Dr.  30,00,000
      To Bank A/c                                 30,00,000

4. General Reserve A/c                    Dr.  10,00,000
   Profit & Loss A/c (Surplus)            Dr.   6,00,000
      To Capital Redemption Reserve A/c           16,00,000
```

**Reconciliation of the substitution identity:**

| Component | Amount (₹) |
|-----------|-----------:|
| Face value redeemed | 30,00,000 |
| Less: Fresh issue (nominal) | (14,00,000) |
| = CRR to be created | 16,00,000 |
| CRR actually created (10,00,000 + 6,00,000) | 16,00,000 ✔ |

**Undistributable fund check.** Before: Pref Capital ₹30,00,000. After: Equity Capital (new) ₹14,00,000 + CRR ₹16,00,000 = ₹30,00,000. The protected block is fully preserved — the fresh issue refilled ₹14,00,000 directly and CRR quarantined the other ₹16,00,000. **Cash check:** cash in ₹14,00,000, cash out ₹30,00,000, net cash outflow ₹16,00,000 — funded from existing cash, matching the ₹16,00,000 of profits that were "spent" on redemption rather than dividend.

### Example 3 — Fresh issue at a premium + redemption at a premium (exam-hard, full reconciliation)

**Facts.** Zenith Ltd.'s Balance Sheet (extract) as on 31 March 2026:

| Equity & Liabilities | ₹ |
|---|---:|
| Equity Share Capital (shares of ₹10) | 40,00,000 |
| 10% Redeemable Preference Share Capital (2,00,000 shares of ₹10 each), fully paid | 20,00,000 |
| Securities Premium | 3,00,000 |
| General Reserve | 8,00,000 |
| Surplus in Statement of P&L | 5,00,000 |
| Bank | 25,00,000 |

The preference shares are redeemable at a **premium of 10%**. To finance the redemption the company issues the *minimum necessary* number of equity shares of ₹10 each at a **premium of 25%**, such that after redemption the General Reserve and P&L Surplus are used to the maximum (i.e., issue the minimum fresh shares needed). Pass journal entries and show the reconciliation.

**Step 1 — Amounts.**
- Face value of preference shares redeemed = ₹20,00,000.
- Premium on redemption = 10% × ₹20,00,000 = ₹2,00,000.
- Total cash payable to preference shareholders = ₹22,00,000.

**Step 2 — Fund the premium on redemption first.** Premium on redemption is met from Securities Premium first, then profits. Securities Premium available = ₹3,00,000, which fully covers the ₹2,00,000 premium. So use Securities Premium ₹2,00,000; no profit needed for the premium. (Securities Premium remaining = ₹1,00,000.)

*Note on CRR — the premium does NOT enter the CRR/fresh-issue identity, which is purely about nominal ₹20,00,000.*

**Step 3 — Minimum fresh issue (nominal).** Profits available for CRR = General Reserve ₹8,00,000 + P&L Surplus ₹5,00,000 = ₹13,00,000 (Securities Premium cannot be used for CRR).

> Minimum fresh issue (nominal) = ₹20,00,000 − ₹13,00,000 = **₹7,00,000.**

Number of new equity shares = ₹7,00,000 / ₹10 = **70,000 shares**, issued at ₹12.50 each (₹10 + 25%).
- Cash raised = 70,000 × ₹12.50 = ₹8,75,000, of which nominal ₹7,00,000 and Securities Premium ₹1,75,000.

**Step 4 — CRR.** CRR = ₹20,00,000 − ₹7,00,000 (fresh nominal) = ₹13,00,000 = full profits available. ✔

**Step 5 — Cash check.**
- Cash before = ₹25,00,000; + fresh issue ₹8,75,000 = ₹33,75,000.
- Pay preference shareholders ₹22,00,000 → Bank after = ₹11,75,000. Positive, so cash is sufficient. ✔

**Journal entries.**

```
1. Bank A/c                                Dr.   8,75,000
      To Equity Share Capital A/c                    7,00,000
      To Securities Premium A/c                      1,75,000
   (Issue of 70,000 equity shares of Rs.10 at Rs.12.50 for redemption)

2. 10% Redeemable Preference Share Capital A/c Dr. 20,00,000
   Premium on Redemption of Pref. Shares A/c    Dr.  2,00,000
      To Preference Shareholders A/c                22,00,000

3. Securities Premium A/c                  Dr.   2,00,000
      To Premium on Redemption of Pref. Shares A/c   2,00,000
   (Premium on redemption met out of Securities Premium)

4. Preference Shareholders A/c             Dr.  22,00,000
      To Bank A/c                                   22,00,000

5. General Reserve A/c                     Dr.   8,00,000
   Profit & Loss A/c (Surplus)             Dr.   5,00,000
      To Capital Redemption Reserve A/c             13,00,000
```

**Post-redemption reconciliation of key balances:**

| Account | Before (₹) | Movement (₹) | After (₹) |
|---|---:|---:|---:|
| Equity Share Capital | 40,00,000 | +7,00,000 | 47,00,000 |
| 10% Redeemable Pref. Capital | 20,00,000 | −20,00,000 | 0 |
| Securities Premium | 3,00,000 | +1,75,000 − 2,00,000 | 2,75,000 |
| General Reserve | 8,00,000 | −8,00,000 | 0 |
| Surplus in P&L | 5,00,000 | −5,00,000 | 0 |
| Capital Redemption Reserve | 0 | +13,00,000 | 13,00,000 |
| Bank | 25,00,000 | +8,75,000 − 22,00,000 | 11,75,000 |

**Undistributable-fund proof.** Before, the protected block = Equity ₹40,00,000 + Pref ₹20,00,000 = ₹60,00,000 of share capital. After = Equity ₹47,00,000 + CRR ₹13,00,000 = ₹60,00,000. Capital + CRR is exactly preserved: the ₹20,00,000 of redeemed preference capital was replaced by ₹7,00,000 fresh equity + ₹13,00,000 CRR. **The creditors' cushion did not move by a single rupee** — which is the entire point of Section 55.

### Example 4 — Partly-paid shares + insufficient cash forces a larger issue (two binding constraints)

**Facts.** Harbour Ltd. has 40,000 7% Redeemable Preference Shares of ₹100 each, on which ₹90 has been called and paid. They are redeemable **at par**. Balances: General Reserve ₹15,00,000; Surplus in P&L ₹3,00,000; Securities Premium ₹1,00,000; Bank ₹8,00,000. The company will first make the shares fully paid, then redeem them. It wishes to retain **at least ₹4,00,000 in Bank** after redemption, meeting any shortfall by issuing equity shares of ₹10 each **at par**. Determine the fresh issue and pass entries.

**Step 1 — Make shares fully paid.** Uncalled = ₹10 per share × 40,000 = ₹4,00,000 to be called and collected. After this, face value fully paid = 40,000 × ₹100 = ₹40,00,000, and Bank rises to ₹8,00,000 + ₹4,00,000 = ₹12,00,000.

**Step 2 — Redemption amount (face, at par).** ₹40,00,000. No premium.

**Step 3 — Which constraint binds — CRR or cash?**
- *CRR-rule minimum fresh issue* = Face − profits available = ₹40,00,000 − (GR ₹15,00,000 + P&L ₹3,00,000) = ₹40,00,000 − ₹18,00,000 = ₹22,00,000. (Securities Premium cannot make CRR.)
- *Cash constraint*: Bank after redemption must be ≥ ₹4,00,000. Bank now ₹12,00,000. If fresh issue (at par) raises ₹F cash and redemption pays out ₹40,00,000:
  Bank after = 12,00,000 + F − 40,00,000 ≥ 4,00,000 ⇒ F ≥ 32,00,000.

The **cash constraint (₹32,00,000) is larger** than the CRR-rule minimum (₹22,00,000), so cash binds. The company must issue **₹32,00,000** of equity = 3,20,000 shares of ₹10.

**Step 4 — CRR with the actual (larger) fresh issue.** CRR = Face − fresh issue nominal = ₹40,00,000 − ₹32,00,000 = **₹8,00,000.** Only ₹8,00,000 of profits are transferred to CRR; the remaining profits (₹18,00,000 − ₹8,00,000 = ₹10,00,000) stay as free reserves. This is the key insight: **issuing more shares than the CRR-minimum reduces the CRR** (more of the face value was refilled by fresh capital), leaving more distributable reserves intact.

**Journal entries.**

```
1. Preference Share Final Call A/c        Dr.   4,00,000
      To 7% Redeemable Pref. Share Capital A/c    4,00,000
   (Final call of Rs.10 on 40,000 pref shares)

2. Bank A/c                               Dr.   4,00,000
      To Preference Share Final Call A/c          4,00,000

3. Bank A/c                               Dr.  32,00,000
      To Equity Share Capital A/c                32,00,000
   (Issue of 3,20,000 equity shares of Rs.10 at par for redemption)

4. 7% Redeemable Pref. Share Capital A/c  Dr.  40,00,000
      To Preference Shareholders A/c             40,00,000

5. Preference Shareholders A/c            Dr.  40,00,000
      To Bank A/c                                40,00,000

6. General Reserve A/c                    Dr.   8,00,000
      To Capital Redemption Reserve A/c           8,00,000
   (CRR = face 40,00,000 less fresh issue nominal 32,00,000)
```

**Cash reconciliation.** Bank: 8,00,000 (open) + 4,00,000 (final call) + 32,00,000 (issue) − 40,00,000 (redemption) = **₹4,00,000** — exactly the required minimum. ✔
**Undistributable-fund proof.** Before (fully paid): Pref Capital ₹40,00,000. After: Equity ₹32,00,000 + CRR ₹8,00,000 = ₹40,00,000. Cushion preserved. ✔
**Trap defused:** a naïve student would issue only ₹22,00,000 (CRR-minimum) and end with Bank = 12,00,000 + 22,00,000 − 40,00,000 = −₹6,00,000, an impossible overdraft. The cash cross-check is what saves you.

### Example 5 — CRR later used for a bonus issue (tracking balances across parts)

**Facts (continuation).** Take Sunrise Ltd. from Example 1 immediately after redemption. Its CRR is ₹20,00,000 and General Reserve is ₹10,00,000. Equity Share Capital is ₹25,00,000 (2,50,000 shares of ₹10). The company now declares a bonus issue of **one fully paid equity share of ₹10 for every five held**, using CRR first and then General Reserve. Pass entries and state the effect.

**Step 1 — Bonus shares.** Existing 2,50,000 shares ÷ 5 = **50,000 bonus shares** of ₹10 = ₹5,00,000 to be capitalised.

**Step 2 — Source.** Use CRR first: CRR can fund the whole ₹5,00,000 (it has ₹20,00,000). General Reserve untouched.

**Journal entries.**

```
1. Capital Redemption Reserve A/c        Dr.   5,00,000
      To Bonus to Shareholders A/c                5,00,000

2. Bonus to Shareholders A/c             Dr.   5,00,000
      To Equity Share Capital A/c                 5,00,000
   (Capitalisation of CRR into 50,000 fully paid bonus shares)
```

**Effect / reconciliation.** CRR falls from ₹20,00,000 to ₹15,00,000; Equity Share Capital rises from ₹25,00,000 to ₹30,00,000. Total shareholders' funds are **unchanged** (₹5,00,000 merely moved from one reserve into share capital) — a bonus issue never changes net worth, it only reclassifies reserves into capital. Note the **direction of the loop**: profit → (redemption) → CRR → (bonus) → share capital. The ₹5,00,000 that started as distributable General Reserve in Example 1 is now *permanently* locked as equity share capital and can never return to shareholders as dividend. This is the "closed loop" the theory promised, shown numerically. **Exam warning:** the ₹5,00,000 of CRR now used is *gone* — a later sub-part asking to redeem more preference shares cannot re-use it.

## 6. Presentation & Disclosure Formats

### 6.1 Balance Sheet (Schedule III, Division I) presentation

Under **"Shareholders' Funds → Reserves and Surplus"**, the CRR is shown as a distinct line item:

```
Reserves and Surplus
   Capital Reserve                         xxx
   Capital Redemption Reserve              xxx   <-- created on redemption
   Securities Premium                      xxx
   General Reserve                         xxx
   Surplus (Statement of Profit and Loss)  xxx
                                          -----
   Total                                   xxx
```

- Redeemable preference shares are presented under **"Share Capital"** while outstanding; once redeemed they disappear from Share Capital.
- **Premium on Redemption of Preference Shares**, until paid, is a liability (part of amount payable to preference shareholders) — typically shown under "Other Current Liabilities."

### 6.2 Notes / disclosure requirements

- Terms of redemption of any outstanding redeemable preference shares, **including the earliest date of redemption**, must be disclosed (Schedule III requirement for share capital notes).
- Movement in CRR (opening, additions, utilisation for bonus, closing) is shown in the Reserves and Surplus note.
- If redemption was funded by a fresh issue, the fresh issue is disclosed in the Share Capital reconciliation note (shares issued during the year).

### 6.3 Ind AS twist (awareness only)

Under **Ind AS 32**, a redeemable preference share that carries a mandatory redemption obligation and/or a mandatory (non-discretionary) dividend is classified as a **financial liability**, not equity — the fixed dividend appears as **finance cost** in the P&L, not as an appropriation of profit. This is the opposite of the AS/Schedule III Division I treatment (where such shares sit in Share Capital and dividend is an appropriation). At CA Intermediate the *default is the AS treatment* used throughout this chapter, but be aware that "substance over form" reclassifies these shares as debt under Ind AS. *(Confirm scope of Ind AS in the current syllabus for your attempt — flagged as verify.)* The irony worth noting: Ind AS finally admits in the accounts what this chapter argued from the start — a redeemable preference share is economically a loan.

## 7. Connections

```mermaid
graph LR
    A["Capital Maintenance Principle"] --> B["Sec 55 Redemption of Pref Shares"]
    A --> C["Sec 66 Capital Reduction"]
    A --> D["Sec 68 Buy-back of Shares"]
    B --> E["CRR - non distributable"]
    D --> E
    E --> F["Sec 63 Bonus Issue - only permitted use"]
    G["Sec 52 Securities Premium"] --> B
    G --> D
```
*Figure 3 — Redemption of preference shares is one of three capital-maintenance-preserving routes to return capital; all three converge on the CRR/bonus machinery.*

- **Buy-back of shares (Section 68):** Uses the *same* CRR logic. When shares are bought back out of free reserves or securities premium, an amount equal to the nominal value bought back is transferred to CRR — identical creditor-protection reasoning. Redemption of preference shares is the conceptual parent of buy-back.
- **Bonus issue (Section 63):** The *only* permitted use of CRR. Studying the two together shows the closed loop: profit → CRR → bonus capital, never back to dividend.
- **Securities Premium (Section 52):** The permitted uses of securities premium (bonus, premium on redemption, buy-back expenses, preliminary expenses, share issue expenses) overlap directly with this topic — it funds premium on redemption but *cannot* fund CRR.
- **Redemption of debentures:** Structurally similar (DRR — Debenture Redemption Reserve), but debentures are *debt*, so the reasoning differs: DRR is about ensuring cash is set aside to repay a loan, whereas CRR is about substituting for lost *capital*. Do not confuse CRR (capital substitution) with DRR (debt repayment cushion).
- **Capital reduction (Section 66):** The "hard" route that redemption avoids. Redemption = pre-authorised, self-policing capital reduction.

**CRR vs DRR — a side-by-side that examiners love to test:**

| Feature | CRR (Sec 55) | DRR (Debenture Redemption Reserve) |
|---|---|---|
| Instrument redeemed | Preference **shares** (capital) | **Debentures** (debt) |
| Purpose of the reserve | *Substitute* lost capital to protect creditors | Set aside profits so cash is available to repay a *loan* |
| Source | Free reserves / P&L only | Profits (P&L) |
| Reduced by fresh *share* issue? | Yes — fresh issue reduces CRR | No such reduction mechanism |
| Permitted use after purpose served | Fully paid **bonus shares** only | Released to General Reserve after redemption |
| Underlying principle | Capital maintenance | Debt-servicing prudence |

The one-line discriminator: **CRR replaces capital; DRR reserves cash for debt.** If you can articulate that, you will not mix them up.

## 8. Traps & Examiner Tricks

1. **CRR on nominal value only — never on premium.** The single most common error. CRR = face value redeemed − fresh issue face value. The premium on redemption is dealt with *separately* (via Securities Premium / profits). Never inflate CRR by the premium.

2. **Securities Premium cannot create CRR.** Students transfer Securities Premium to CRR — wrong. CRR must come from *distributable* profits (free reserves / P&L). Securities Premium is not a profit available for dividend. (It *can* fund premium on redemption, though.)

3. **"Fresh issue for the purpose of redemption."** Only shares issued *specifically to finance the redemption* reduce the CRR requirement. If the company issued shares last year for expansion, those do **not** count — the full face value must go to CRR. Watch for date/purpose clues.

4. **Minimum fresh issue vs. cash sufficiency.** The CRR identity gives the *minimum* fresh issue for the capital rule, but the problem may separately demand a minimum bank balance be maintained. Then the binding constraint becomes cash, and you may need to issue *more* shares (or issue at a premium) than the pure CRR identity suggests. Always run the bank-balance cross-check. (Example 4 is built on this.)

5. **Issue price vs. nominal value in the identity.** When fresh shares are issued at a premium, students plug the *cash raised* into the CRR identity. Wrong — the identity uses **nominal value**. The premium on the new issue goes to Securities Premium, not into the redemption/CRR substitution.

6. **Only fully-paid shares.** If the problem gives partly-paid preference shares, you must first call up and collect the balance (entries) before redeeming. A common trick is to slip in "₹80 paid on ₹100 shares."

7. **CRR misuse.** CRR can be used *only* for fully paid bonus shares. Any question implying CRR was used to pay dividend / write off losses / fund expenses describes an illegal act — flag it.

8. **Provision for premium "before" redemption.** Premium on redemption must be arranged/provided before the shares are redeemed. Sequencing in the journal matters: provide premium (entry d) before/at the point of paying shareholders.

9. **Availability vs. willingness of profits.** A question may say "the company wishes to retain ₹X of General Reserve." That retained amount is *not available* for CRR, which increases the minimum fresh issue. Read constraints carefully.

10. **Bonus shares reduce future redemption flexibility.** If CRR is later capitalised as bonus shares, it is gone — a later part of the same question cannot re-use it. Track balances across sub-parts. (Example 5 shows this.)

11. **Debenture issue does not reduce CRR.** If redemption is financed by issuing debentures (or taking a loan), no *share capital* comes in — the entire face value still goes to CRR. Only a fresh issue of **shares** (equity or preference) reduces CRR. Do not net debentures against the CRR requirement.

12. **Capital Reserve / Revaluation Reserve are not "profits available for dividend."** They cannot create CRR, exactly like Securities Premium. Only reserves that *could have been paid as dividend* qualify. The examiner may bury a Capital Reserve in the trial balance to tempt you.

13. **Redeeming at a discount is not permitted.** Preference shares are redeemed at par or premium, never below par. A question offering a "redemption at a discount" is testing whether you know this is impermissible.

14. **Fresh issue of *preference* shares also reduces CRR.** Do not assume the refill must be equity. New preference shares issued to fund redemption of old ones reduce CRR by their nominal value just the same.

15. **"Profits available for dividend" ≠ entire General Reserve if some is committed.** If a reserve is earmarked (e.g., a statutory reserve, or an amount pledged elsewhere), it is not freely available. Read the nature of each reserve, not just its size.

16. **Both premium sources move the Securities Premium balance in opposite directions.** Fresh issue at premium *adds* to Securities Premium; funding redemption premium *subtracts* from it. Compute the closing balance as a net movement, not just the closing of one leg.

## 9. First-Principles Recap

Strip everything away and one sentence remains: **capital must be maintained for creditors, so when redeemable preference capital leaves the company it must be replaced — rupee for rupee of face value — either by fresh share capital coming in, or by locking away an equal amount of profit as a Capital Redemption Reserve.**

Everything else is a corollary:
- *Why only fully-paid?* You can't return what wasn't fully put in.
- *Why only profits or fresh issue?* They are the only two sources that don't net-shrink the cushion.
- *Why CRR = face − fresh issue?* Because fresh issue already refilled that part; CRR plugs the rest.
- *Why can't Securities Premium make CRR?* CRR must come from something that could otherwise have gone out as dividend, so that quarantining it actually costs the shareholders their distributable surplus. Premium was never distributable.
- *Why is premium on redemption separate?* It is an *extra* payment, not part of the capital being substituted, so it is funded but never enters the CRR identity.
- *Why can CRR only become bonus shares?* Because letting it back out as dividend would undo the whole protection.
- *Why doesn't a debenture issue reduce CRR?* Because debentures add creditors, not capital — the cushion isn't refilled, so the whole face value must still be walled up.
- *Why does issuing more than the minimum fresh issue reduce CRR?* Because more face value was refilled directly by capital, leaving a smaller hole to plug — the two sources always sum to the face value.

If you can derive the three Section 55 conditions from the capital-maintenance principle alone — without looking them up — you own this topic.

## 10. Quick-Revision Sheet

**Governing law:** Section 55, Companies Act 2013 (no irredeemable pref shares; redeem within 20 years; 30 years for infrastructure cos.). Must be authorised by Articles.

**Three conditions (Sec 55(2)):**
1. Only **fully paid** shares redeemable.
2. Redeem out of **profits available for dividend** or **proceeds of a fresh issue** made for redemption.
3. Redeem out of profits ⇒ transfer **nominal value** to **CRR**.

**Master identity:**
> Nominal value redeemed = Fresh issue (nominal) + CRR
> ⇒ **CRR = Nominal redeemed − Fresh issue nominal**
> ⇒ **Minimum fresh issue = Nominal redeemed − Profits available for CRR**

**CRR facts:**
- Source: free reserves / P&L surplus **only** (NOT Securities Premium, NOT Capital Reserve, NOT Revaluation Reserve).
- Reduced by fresh issue of **shares** (equity OR preference); **not** reduced by debentures/loans.
- Use: **only** fully paid **bonus shares** (Sec 55(4) + Sec 63). Treated as paid-up capital.
- Amount = nominal value only; **premium excluded**.

**Premium on redemption:**
- Fund from **Securities Premium** first, then **free reserves / P&L**.
- Provided *before* redemption; never part of CRR.
- Redemption at par or premium only — **never at a discount**.

**Core journal entries:**

| Purpose | Entry |
|---|---|
| Make partly-paid fully paid | Pref Final Call Dr.; To Pref Capital / Bank Dr.; To Pref Final Call |
| Fresh issue (at premium) | Bank Dr.; To Share Capital, To Securities Premium |
| Amount due | Redeemable Pref Cap Dr., Premium on Redemption Dr.; To Pref Shareholders |
| Provide premium | Securities Premium / P&L Dr.; To Premium on Redemption |
| Pay off | Pref Shareholders Dr.; To Bank |
| Create CRR | General Reserve / P&L Dr.; To CRR |
| Bonus (later) | CRR Dr.; To Bonus to Shareholders; then To Equity Share Capital |

**Checklist for any problem:**
1. Are pref shares fully paid? If not, call up first.
2. Redemption amount = face; premium = separate.
3. Profits available for CRR (after any retention constraint)? Exclude Sec Premium / Capital Reserve.
4. Minimum fresh issue = face − available profits. (Debentures/loan don't count as refill.)
5. Actual fresh issue = larger of CRR-minimum and any cash-constraint minimum.
6. CRR = face − *actual* fresh issue nominal.
7. Fund premium from Securities Premium then profits.
8. Cash cross-check: Bank after = Bank before + issue proceeds − (face + premium) ≥ any required minimum.
9. Prove: Capital + CRR after = Capital before (cushion preserved).

**One-line memory hook:** *"Refill with new capital or wall-up with CRR — face value for face value — and premium is a side payment, not part of the wall."*
