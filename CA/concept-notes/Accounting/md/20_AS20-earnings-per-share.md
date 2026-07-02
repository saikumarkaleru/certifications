# Chapter 20 — AS 20 — Earnings Per Share

## 1. The Problem

Imagine two companies. Alpha Ltd earns a net profit of Rs. 10 crore this year. Beta Ltd earns Rs. 2 crore. Which company is doing better *for its owners*?

The naive answer — "Alpha, obviously" — is a trap. Suppose Alpha's profit is spread across 10 crore shares, while Beta's is spread across 50 lakh shares. Then each Alpha share carries Re. 1 of earnings, while each Beta share carries Rs. 4. A person who owns one share of Beta has a claim on four times the earning power of a person who owns one share of Alpha. Beta is the better performer *per unit of ownership*.

Absolute profit tells you the *size* of the pie. It tells you nothing about *how big your slice is*. And an investor never buys "the whole company" — he buys **shares**. The unit he cares about is the share, not the company.

There is a second, subtler problem. Profit is a moving target relative to the share count, because companies keep changing the number of shares outstanding — they issue fresh shares for cash, issue bonus shares, do rights issues, buy shares back, and they have lurking instruments (convertible debentures, employee stock options, convertible preference shares) that *could* become shares tomorrow. If you naively divide profit by "the number of shares on 31 March", you get a figure that can be gamed and that isn't comparable across time or across companies.

So the problem AS 20 solves is: **How do we express a company's performance as a single, honest, comparable "per share" number — one that (a) reflects only what belongs to the ordinary equity owner, (b) uses a fair count of shares even when the count changed mid-year, and (c) warns the owner about future dilution from instruments that haven't converted yet?**

That number is **Earnings Per Share (EPS)**. It is arguably the single most-quoted figure in all of financial reporting — it drives the Price-to-Earnings (P/E) ratio, analyst models, and management bonus schemes. AS 20 exists to make sure everybody computes it the *same* way, so that "EPS of Rs. 4.21" means the same thing in every annual report.

## 2. The Core Idea (analogy)

Think of a **pizza shared at a table**.

- The **pizza** is the net profit that belongs to the equity shareholders.
- The **number of people at the table** is the number of equity shares.
- **EPS is the size of one slice** — profit ÷ people.

Now, three real-life complications, each of which maps onto an AS 20 rule:

1. **People arrive and leave mid-meal.** If someone sits down only for the last 10 minutes, it's unfair to give them a slice as large as those who sat the whole time. So we count people by *how long they were at the table* — this is the **weighted average**.

2. **The pizza is cut into more pieces without more pizza arriving.** A bonus issue is exactly this — the company splits existing ownership into more shares but *no new money or profit comes in*. The pizza is the same size; there are just more, thinner slices now. Because nothing real changed, we must pretend the extra slices existed *all along* — even in last year's figures — so comparisons stay honest. This is **retrospective adjustment**.

3. **Some people at the next table hold a coupon that lets them join yours cheaply.** Convertible debentures, options and convertible preference shares are people with a *right to a slice* they haven't claimed yet. A cautious host warns the current diners: "If all these coupon-holders show up, your slice shrinks to *this*." That worst-case, shrunken slice is **Diluted EPS**.

Hold this picture. Every rule below is just a careful working-out of "profit that's truly ours ÷ a fair count of us, plus a warning about who might join."

## 3. Why It's Built This Way

Before the mechanics, internalise the four design decisions that generate almost every rule in AS 20. If you understand these, you can *derive* the standard rather than memorise it.

**Design decision 1 — The numerator must be "clean" equity profit.** The slice belongs to *equity* shareholders. Preference shareholders are a different table — they get a fixed dividend before equity sees anything. So preference dividend must be stripped out of the profit before dividing. Anything that isn't the residual claim of the ordinary owner is removed.

**Design decision 2 — The denominator must be time-fair.** A share that existed for two months cannot be counted equally with a share that existed for twelve, because it was only "at the table" for two months' worth of earning. Hence time-weighting.

**Design decision 3 — Purely cosmetic changes in share count must not distort trends.** Some changes in share count bring in *new resources* (cash issues) and some *don't* (bonus, share split). A cash issue genuinely gives the company more money to earn on, so it earns its place from the date the cash arrives. A bonus issue brings *nothing new* — it only re-slices existing ownership. If we time-weighted a bonus, this year's EPS would fall for a purely paper reason and would look worse than last year's — a false signal. So no-resource changes are pushed *backwards* through all periods presented (retrospective), keeping the trend line honest.

**Design decision 4 — The owner deserves a worst-case warning.** Instruments that can become equity are a sword hanging over today's shareholder. Prudence says: show him not just today's slice (Basic EPS) but the *diluted* slice assuming the sword falls (Diluted EPS). And — crucially — the warning must be *conservative but not misleading*: you only include a potential share if including it actually **reduces** EPS (dilutes). If a potential conversion would *increase* EPS, showing that increase would flatter the company and lull the owner — the opposite of a warning. Hence the **anti-dilution rule**: ignore anti-dilutive instruments.

Everything that follows is bookkeeping in service of these four ideas.

## 4. Full Technical Content (Recognition · Measurement · Presentation · Disclosure)

AS 20 applies to enterprises whose equity shares or potential equity shares are **listed** (or in the process of listing). Other enterprises that *choose* to disclose EPS must also comply with AS 20 so the figure is standardised. (Separately, Schedule III to the Companies Act requires EPS to be disclosed in the notes for every company — so in practice you compute AS 20 EPS for companies too.)

Key definitions to fix vocabulary:

- **Equity share**: an ownership share subordinate to all other classes (the residual claimant).
- **Potential equity share**: a financial instrument or contract that *may* entitle its holder to equity shares — e.g. convertible debentures, convertible preference shares, share warrants, options, and shares issuable on satisfaction of conditions.
- **Dilution**: a *reduction* in EPS (or an *increase* in loss per share) assuming conversion of potential equity shares.

### 4.1 Basic EPS

$$\text{Basic EPS} = \frac{\text{Net profit / loss for the period attributable to equity shareholders}}{\text{Weighted average number of equity shares outstanding}}$$

**(R) Recognition of the numerator — "attributable to equity shareholders."**
Start with net profit or loss for the period *after tax and after extraordinary items* (all items of income and expense, including tax, are already inside net profit). From this, **deduct preference dividends and any attributable tax thereon** to reach the equity shareholders' share.

Two rules on preference dividend, and here's the *why*:

- **Cumulative preference shares:** deduct the dividend for the current period **whether or not it has been declared/provided**. Reason: a cumulative preference dividend is an *unavoidable* prior claim — even if unpaid this year it becomes arrears the equity holder must clear before ever seeing a rupee. So it is not really the equity holder's money regardless of declaration.
- **Non-cumulative preference shares:** deduct only if the dividend is **declared/provided** for the period. Reason: if not declared, it lapses forever and the amount *is* available to equity — so there's nothing to strip out.

Also deduct, as a preference-type charge, any **premium payable on redemption of preference shares** or **excess of consideration paid over carrying amount on buy-back of preference shares** (it is a distribution to preference holders in substance).

**(M) Measurement of the denominator — the weighted average number of equity shares.**
Weight each block of shares by the **fraction of the period it was outstanding**. A share is included from the date consideration is receivable, which usually means:

| Manner of issue | Included from |
|---|---|
| Shares issued for cash | Date cash is receivable |
| Shares issued on voluntary reinvestment of dividends | Dividend reinvestment date |
| Shares issued on conversion of a debt instrument | Date of conversion |
| Shares issued for goods/services or on acquisition | Date the goods/asset is recognised / acquisition date |
| Shares issued in lieu of interest or principal | Date interest ceases to accrue |
| Bonus issue / share split / consolidation | Treated as if outstanding from the **start of the earliest period presented** (retrospective) |

Buy-backs and cancellations are subtracted on a time-weighted basis from the date they occur (they *reduce* the average from that date onward).

**Bonus and split — retrospective, no time-weighting (from Design decision 3).** A bonus issue, a share split, or a consolidation changes the number of shares *without a corresponding change in resources*. So AS 20 requires you to adjust the number of shares outstanding **as if the event had occurred at the beginning of the earliest period reported** — and to restate the prior period's EPS accordingly for comparability. There is no time-weighting: the bonus shares are deemed to have always existed.

**Rights issue — the hybrid, handled by the theoretical ex-rights factor.** A rights issue is the awkward middle case: it brings in *cash* (like a fresh issue) but usually at a price *below* fair value (like a partial bonus, because the discount is a gift to existing holders). AS 20 splits it into these two components using the **adjustment factor**:

$$\text{Adjustment factor} = \frac{\text{Fair value per share immediately before the rights exercise}}{\text{Theoretical ex-rights fair value per share (TERP)}}$$

where

$$\text{TERP} = \frac{\text{Fair value of all shares before rights} + \text{Total amount received on exercise of rights}}{\text{Number of shares outstanding after the rights issue}}$$

**Why TERP?** Immediately after a below-market rights issue, the market price *drops* — because the same total company value is now spread over more shares, each of which paid in less than fair value. TERP is the new, theoretically fair price per share right after the issue. The ratio (old fair value ÷ TERP) is always **greater than 1**, and it isolates the "bonus element" hidden inside the rights issue. You then:

1. Multiply the number of shares outstanding *before* the rights issue by the adjustment factor (this inflates them for the bonus element and pushes it retrospectively, just like a bonus).
2. Restate all prior-period EPS by *dividing* the earlier EPS by this same factor (equivalently multiplying earlier share counts by the factor).

So a rights issue = a small bonus (retrospective, via the factor) + a cash issue (time-weighted from the rights date). We will see this split cleanly in Worked Example 3.

### 4.2 Diluted EPS

$$\text{Diluted EPS} = \frac{\text{Adjusted net profit attributable to equity holders}}{\text{Weighted average shares} + \text{Weighted average dilutive potential equity shares}}$$

**(R/M) Adjust the numerator** for the after-tax effect of items that would *disappear* on conversion:
- **Add back** interest on convertible debentures (net of tax), because on conversion the debenture — and its interest expense — vanishes, so profit rises.
- **Add back** dividends on convertible preference shares that were deducted in Basic EPS, because on conversion those become equity and the preference dividend ceases.
- Adjust for any other consequential change in income/expense (e.g. employee-profit-share or interest that keys off those instruments), net of tax.

**(M) Adjust the denominator** by adding the weighted average number of shares that *would* be issued on conversion, assumed converted at the **beginning of the period** (or date of issue of the instrument, if later).

**Options and warrants — the treasury stock method.** For options/warrants that are "in the money" (exercise price below the average market price), only the shares issued *for no consideration* are dilutive. The logic: the option-holder pays the exercise price in cash; the company is assumed to use that cash to buy back shares at the average market price. The *net* new shares — those issued free — are the dilutive element:

$$\text{Incremental shares} = \text{Options} - \frac{\text{Options} \times \text{Exercise price}}{\text{Average market price}} = \text{Options} \times \frac{\text{Market} - \text{Exercise}}{\text{Market}}$$

These incremental shares carry **no earnings and no numerator adjustment** — so their incremental EPS is Rs. 0, which makes options *always dilutive* whenever they are in the money (and ignored when out of the money).

**(R) The anti-dilution rule — the heart of Diluted EPS (from Design decision 4).** A potential equity share is included **only if it is dilutive** — i.e. only if its conversion *decreases* EPS from continuing operations (or increases loss per share). To apply this correctly when several instruments exist, you must **sequence** them:

1. For each potential-equity instrument, compute its **incremental EPS** = (after-tax numerator effect) ÷ (number of shares it would add).
2. **Rank** them from *smallest* incremental EPS (most dilutive) to *largest* (least dilutive). Options, at Rs. 0, usually rank first.
3. Add them into the running EPS calculation **one series at a time, in that order**. After each addition, check the running EPS. Keep an instrument only while it *lowers* the running EPS.
4. The moment an instrument's incremental EPS **exceeds** the current running diluted EPS, that instrument (and every remaining one, since they're even less dilutive) is **anti-dilutive** — exclude it.

The control figure ("net profit from continuing ordinary operations") is what you test dilution against; discontinued/extraordinary components do not flip the dilution decision. Sequencing matters because an instrument that looks anti-dilutive against Basic EPS might be dilutive against an already-lowered running figure, and vice versa — you must add most-dilutive-first to find the *lowest possible* EPS, which is the honest worst case.

### 4.3 Presentation & Disclosure (overview — detailed in Part 6)

- Present **Basic and Diluted EPS on the face of the Statement of Profit and Loss**, with **equal prominence**, for every period presented, and for each class of equity share that has a different right to share in profit.
- Present EPS **even if the amounts are negative** (loss per share).
- Diluted EPS is presented **even if equal to Basic EPS** (they are shown on separate lines regardless).

## 5. Worked Examples

### Example 1 — Basic EPS with a cash issue and a buy-back (time-weighting)

**Facts (FY 2025-26 of Vega Ltd):**
- Equity shares outstanding on 1 April 2025: 1,00,000
- 1 August 2025: issued 30,000 equity shares for cash
- 1 January 2026: bought back 12,000 equity shares
- Net profit after tax: Rs. 8,00,000
- 10% cumulative preference share capital: Rs. 5,00,000 (dividend not yet declared)

**Step 1 — Clean the numerator.** Preference dividend = 10% × 5,00,000 = **Rs. 50,000**. It is *cumulative*, so we deduct it even though not declared (Design decision 1).
Earnings attributable to equity = 8,00,000 − 50,000 = **Rs. 7,50,000**.

**Step 2 — Weighted average shares (time-weight each block).**

| Period | Months | Shares outstanding | Weighted |
|---|---|---|---|
| 1 Apr – 31 Jul | 4 | 1,00,000 | 4,00,000 |
| 1 Aug – 31 Dec | 5 | 1,30,000 | 6,50,000 |
| 1 Jan – 31 Mar | 3 | 1,18,000 | 3,54,000 |
| **Total** | 12 | | **14,04,000** |

Weighted average = 14,04,000 ÷ 12 = **1,17,000 shares**.

*Cross-check by the incremental method:* 1,00,000 (full year) + 30,000 × 8/12 (Aug–Mar) − 12,000 × 3/12 (Jan–Mar) = 1,00,000 + 20,000 − 3,000 = **1,17,000**. ✓ Ties out.

**Step 3 — Basic EPS** = 7,50,000 ÷ 1,17,000 = **Rs. 6.41**.

### Example 2 — Bonus issue (retrospective restatement over two years)

**Facts:**
- FY 2024-25: net profit attributable to equity = Rs. 18,00,000; equity shares outstanding all year = 6,00,000. Reported Basic EPS = **Rs. 3.00**.
- On 1 October 2025, during FY 2025-26, the company makes a **bonus issue of 1 share for every 2 held**. Bonus shares = 6,00,000 ÷ 2 = 3,00,000, taking the total to 9,00,000.
- FY 2025-26: net profit attributable = Rs. 22,50,000.

**Step 1 — Current year (2025-26).** A bonus brings no new resources, so we treat the bonus shares as outstanding *from the start of the year* — **no time-weighting**. Weighted average = **9,00,000 shares**.
Basic EPS 2025-26 = 22,50,000 ÷ 9,00,000 = **Rs. 2.50**.

**Step 2 — Restate the comparative (2024-25).** For the trend to be honest, last year's EPS must be re-computed as if the bonus shares had *always* existed. Bonus factor = 9,00,000 ÷ 6,00,000 = **1.5**.
Restated shares for 2024-25 = 6,00,000 × 1.5 = 9,00,000.
Restated EPS 2024-25 = 18,00,000 ÷ 9,00,000 = **Rs. 2.00** (down from the originally reported Rs. 3.00).

**Why this matters:** without restatement, the report would show EPS falling from Rs. 3.00 to Rs. 2.50 — implying deteriorating performance. But per-share earnings *actually rose* (from a restated Rs. 2.00 to Rs. 2.50, +25%). The bonus merely re-sliced the pizza; restatement reveals the true improvement.

### Example 3 — Rights issue with the theoretical ex-rights factor

**Facts (Nova Ltd):**
- Equity shares outstanding before rights: 2,00,000
- Rights issue: **1 new share for every 4 held, at Rs. 15 per share**
- Fair value of one share *immediately before* the rights exercise (cum-rights): **Rs. 25**
- Rights shares issued on **1 January 2026**; year-end 31 March 2026
- Net profit attributable to equity, FY 2025-26: Rs. 9,50,000
- Net profit attributable to equity, FY 2024-25: Rs. 8,00,000 (2,00,000 shares outstanding all of that year; reported EPS Rs. 4.00)

**Step 1 — Rights shares and TERP.**
Rights shares = 2,00,000 ÷ 4 = 50,000. Total after rights = **2,50,000**.

$$\text{TERP} = \frac{(2,00,000 \times 25) + (50,000 \times 15)}{2,50,000} = \frac{50,00,000 + 7,50,000}{2,50,000} = \frac{57,50,000}{2,50,000} = \textbf{Rs. 23}$$

**Step 2 — Adjustment factor** = Fair value before ÷ TERP = 25 ÷ 23 = **1.086957**.
(Interpretation: the rights issue contains a bonus element of ~8.7% — that's the discount gifted to existing holders — which must be pushed backwards; the rest is a genuine cash issue from 1 January.)

**Step 3 — Weighted average for 2025-26.** Split the year at the rights date:
- Pre-rights block (1 Apr – 31 Dec, 9 months): 2,00,000 shares, *grossed up by the factor*:
 2,00,000 × (25/23) × (9/12) = 2,17,391.30 × 0.75 = **1,63,043.48**
- Post-rights block (1 Jan – 31 Mar, 3 months): 2,50,000 × (3/12) = **62,500**

Weighted average = 1,63,043.48 + 62,500 = **2,25,543 shares** (rounded).

**Step 4 — Basic EPS 2025-26** = 9,50,000 ÷ 2,25,543 = **Rs. 4.21**.

**Step 5 — Restate 2024-25.** Multiply the prior share count by the factor (equivalently, divide the old EPS by it):
Restated EPS 2024-25 = 4.00 × (23/25) = 4.00 × 0.92 = **Rs. 3.68**.
*Check via shares:* restated shares = 2,00,000 × 25/23 = 2,17,391; restated EPS = 8,00,000 ÷ 2,17,391 = **Rs. 3.68**. ✓

Notice how the rights issue behaves as a **hybrid**: the bonus element (the 25/23 gross-up) is retrospective and hits the prior year, while the pure cash element (the extra 50,000 shares) is time-weighted from 1 January only.

### Example 4 — Diluted EPS with convertible debentures and stock options (with anti-dilution sequencing)

**Facts (Orion Ltd, FY 2025-26):**
- Net profit attributable to equity shareholders (already after preference dividend): **Rs. 10,00,000**
- Weighted average equity shares: **5,00,000** → Basic EPS = **Rs. 2.00**
- 12% Convertible Debentures of Rs. 20,00,000; each Rs. 100 debenture converts into **8 equity shares**; outstanding all year. Tax rate 30%.
- Employee stock options: **1,00,000 options**, exercise price Rs. 15; average market price of the share during the year Rs. 20.

**Step 1 — Incremental EPS of each potential equity share.**

*Convertible debentures:*
- Potential shares = (20,00,000 ÷ 100) × 8 = 20,000 × 8 = **1,60,000 shares**
- Interest saved (added back to profit) = 12% × 20,00,000 = 2,40,000; **after tax** = 2,40,000 × (1 − 0.30) = **Rs. 1,68,000**
- Incremental EPS = 1,68,000 ÷ 1,60,000 = **Rs. 1.05 per share**

*Options (treasury stock method):* exercise price Rs. 15 < market Rs. 20 → in the money.
- Proceeds on exercise = 1,00,000 × 15 = 15,00,000; shares repurchasable at market = 15,00,000 ÷ 20 = 75,000
- Incremental (free) shares = 1,00,000 − 75,000 = **25,000 shares**; numerator effect = Rs. 0
- Incremental EPS = 0 ÷ 25,000 = **Rs. 0 per share**

**Step 2 — Rank by incremental EPS (most dilutive first).**

| Rank | Instrument | Incremental EPS |
|---|---|---|
| 1 | Options | Rs. 0.00 |
| 2 | Convertible debentures | Rs. 1.05 |

**Step 3 — Add in sequence, checking the running EPS each time.**

| Stage | Numerator (Rs.) | Denominator (shares) | Running EPS | Dilutive? |
|---|---|---|---|---|
| Basic | 10,00,000 | 5,00,000 | 2.0000 | — |
| + Options | 10,00,000 | 5,25,000 | 1.9048 | Yes (2.00 → 1.90) → keep |
| + Debentures | 11,68,000 | 6,85,000 | 1.7051 | Yes (1.90 → 1.71) → keep |

Each addition lowers the running EPS, so both are dilutive.

**Diluted EPS = 11,68,000 ÷ 6,85,000 = Rs. 1.71.**

**Step 4 — The anti-dilution safeguard (illustration).** Suppose Orion *also* had 10% convertible preference shares of Rs. 5,00,000 convertible into 10,000 equity shares. Preference dividend saved on conversion = Rs. 50,000; incremental EPS = 50,000 ÷ 10,000 = **Rs. 5.00**. Since Rs. 5.00 is *greater than* the running diluted EPS of Rs. 1.71, converting these would *raise* EPS — they are **anti-dilutive** and must be **excluded** from Diluted EPS. Including them (giving 12,18,000 ÷ 6,95,000 = Rs. 1.75) would understate dilution and *flatter* the company — precisely what the anti-dilution rule forbids.

## 6. Presentation & Disclosure Formats

**On the face of the Statement of Profit and Loss** (with equal prominence, both years):

```
Statement of Profit and Loss (extract) ....... 2025-26      2024-25
Profit for the year ........................ 8,00,000     ...
Earnings per equity share (face value Rs. 10):
   Basic (Rs.) ............................    6.41        (restated) ...
   Diluted (Rs.) ..........................    5.90        (restated) ...
```

Both Basic and Diluted are shown even if one is negative and even if the two are equal.

**In the notes, AS 20 requires disclosure of:**

1. The **amounts used as the numerators** for Basic and Diluted EPS, and a **reconciliation of those amounts to the net profit/loss** for the period. (i.e. net profit → less preference dividend → Basic numerator → add back after-tax interest/dividend on dilutive instruments → Diluted numerator.)
2. The **weighted average number of equity shares** used as the denominator for Basic and Diluted EPS, and a **reconciliation of these denominators to each other** (Basic shares + dilutive potential shares = Diluted shares).
3. The **nominal (face) value** of the shares along with the EPS figures.

**Illustrative numerator reconciliation (Orion Ltd, Example 4):**

| | Rs. |
|---|---|
| Net profit for the year (after tax) | 10,00,000 |
| *Numerator for Basic EPS* | **10,00,000** |
| Add: interest on convertible debentures (net of tax) | 1,68,000 |
| *Numerator for Diluted EPS* | **11,68,000** |

**Illustrative denominator reconciliation:**

| | Shares |
|---|---|
| Weighted average shares (Basic) | 5,00,000 |
| Add: dilutive options | 25,000 |
| Add: dilutive convertible debentures | 1,60,000 |
| Weighted average shares (Diluted) | **6,85,000** |

**Additional presentation rules to remember:**
- If the number of shares changes due to a bonus, split, consolidation or the bonus-element of a rights issue **after the balance sheet date but before the financial statements are approved**, EPS for all periods presented is computed on the *new* number of shares (the event is treated as if it happened at the start). Disclose this fact.
- Where an enterprise presents EPS for each class of equity share with different rights, present each separately.

## 7. Connections

- **AS 5 (Prior Period & Changes / Extraordinary items):** Net profit *including* extraordinary items and tax is the starting numerator. Although Indian AS 20 tests dilution against profit from *continuing ordinary operations*, the EPS presented uses total net profit less preference dividend.
- **AS 4 (Events after the Balance Sheet Date):** the post-year-end bonus/split/rights rule above is an AS 20-specific adjusting treatment for share counts.
- **AS 25 (Interim Financial Reporting):** requires Basic and Diluted EPS in interim statements too, using the same principles.
- **AS 26 (Intangibles) / AS 14 (Amalgamations):** shares issued as purchase consideration in an acquisition enter the weighted average from the **acquisition date** — links to how consideration is dated.
- **Companies Act, 2013 — Schedule III & buy-back (Sec. 68) / bonus (Sec. 63):** the buy-back and bonus mechanics that *change* the share count are governed there; AS 20 tells you how those changes flow into EPS. Premium on redemption of preference shares (Sec. 55) is treated as a preference charge in the numerator.
- **Financial Management (P/E ratio, valuation):** EPS is the denominator-input to the P/E multiple and to dividend-payout and earnings-yield analysis — the same figure you compute here is consumed directly in valuation.
- **Ind AS 33** is the converged equivalent; its principles mirror AS 20 closely, so this chapter transfers almost intact if you later study Ind AS.

## 8. Traps & Examiner Tricks

1. **Cumulative vs non-cumulative preference dividend.** Examiners love to say "dividend not declared." If cumulative → still deduct. If non-cumulative and not declared → do **not** deduct. Reversing this is the single most common error.
2. **Bonus/split are NOT time-weighted.** Students instinctively apply the "months outstanding" fraction to bonus shares — wrong. Bonus shares are deemed outstanding from the *start of the earliest period presented*. Only cash issues and buy-backs are time-weighted.
3. **Forgetting to restate the comparative** after a bonus or the bonus-element of a rights issue. The prior year's EPS must be recomputed; leaving it at the originally reported figure loses marks.
4. **Rights issue at fair value.** If the rights price *equals* fair value, there is **no bonus element** — the adjustment factor is 1, and you simply time-weight it as an ordinary cash issue. Don't force a TERP factor where none exists.
5. **Options out of the money.** If exercise price ≥ average market price, the option is **anti-dilutive** and is ignored entirely — do not run the treasury method. Also note: it's the **average** market price over the period, not the closing price.
6. **Wrong anti-dilution sequencing.** Adding a *less* dilutive instrument before a *more* dilutive one can wrongly classify a dilutive instrument as anti-dilutive. Always rank by incremental EPS, smallest first (options at Rs. 0 nearly always go first).
7. **Testing dilution against Basic EPS instead of the running figure.** An instrument must be tested against the *running* diluted EPS after adding all more-dilutive instruments, not against Basic EPS.
8. **Numerator add-back for debentures must be net of tax.** Forgetting the (1 − tax rate) factor inflates Diluted EPS. Convertible *preference* dividends, by contrast, are added back *without* a tax adjustment (dividends are post-tax appropriations).
9. **Loss per share.** When there's a loss, potential shares that would *reduce* the loss per share are anti-dilutive and excluded — dilution *increases* a loss, it doesn't shrink it. Present the loss per share with a minus sign for both Basic and Diluted.
10. **Buy-back reduces the weighted average from the buy-back date**, not from the year start — a mirror-image of a mid-year cash issue.
11. **Premium on redemption / buy-back of preference shares** must be deducted from the numerator like a preference dividend — easy to miss.

## 9. First-Principles Recap

- EPS exists because owners buy *shares*, not whole companies; absolute profit hides how big each owner's slice is. EPS = profit per unit of ownership, making performance comparable across companies and years.
- The numerator is *equity* profit: net profit after tax **minus** preference dividend (and any preference redemption premium) — because the residual belongs only to equity holders.
- The denominator is *time-fair*: shares are weighted by the fraction of the period they existed, because a share present for two months earned for only two months.
- Changes in share count that bring **new resources** (cash issues, buy-backs) are time-weighted from their date; changes that bring **no resources** (bonus, split) are pushed retrospectively to the start of all periods presented — otherwise a purely cosmetic re-slicing would fake a change in performance.
- A rights issue is a **hybrid**: the below-market discount is a bonus element (retrospective, via the factor Fair value ÷ TERP) and the balance is a cash issue (time-weighted from the rights date).
- Diluted EPS is a **worst-case warning**: it assumes convertibles/options become shares, adjusting the numerator (add back after-tax interest, and preference dividend) and the denominator (add potential shares).
- Options dilute via the **treasury stock method** — only the "free" shares (those beyond what the exercise proceeds could buy back at market) count, at zero incremental earnings.
- The **anti-dilution rule** is non-negotiable: include a potential equity share only if it *lowers* EPS; sequence instruments most-dilutive-first so the reported Diluted EPS is the lowest, most honest figure.
- Both Basic and Diluted EPS are presented with equal prominence, for every period, even when negative or equal, with full numerator/denominator reconciliations disclosed.

## 10. Quick-Revision Sheet

**Basic EPS** = (Net profit after tax − Preference dividend) ÷ Weighted average equity shares.

**Preference dividend:** cumulative → deduct always; non-cumulative → deduct only if declared. Also deduct redemption/buy-back premium.

**Weighted average:** time-weight cash issues (from cash-due date) and buy-backs (from buy-back date). Bonus/split → retrospective, from start of earliest period, no time-weighting → restate prior EPS.

**Rights issue factor:**
- TERP = (FV of shares before + proceeds from rights) ÷ shares after.
- Adjustment factor = FV before ÷ TERP (> 1).
- Pre-rights shares × factor × time-fraction; post-rights shares × time-fraction. Restate prior EPS = old EPS ÷ factor.

**Diluted EPS** = (Basic numerator + after-tax interest on convert. debentures + preference dividend on convert. pref) ÷ (Basic shares + dilutive potential shares).

**Options (treasury stock):** incremental shares = Options × (Market − Exercise) ÷ Market; incremental EPS = 0; dilutive only if Exercise < Average market price.

**Convertible incremental EPS** = after-tax numerator effect ÷ shares on conversion.

**Anti-dilution:** rank by incremental EPS (smallest first); add one series at a time; keep only while running EPS falls; stop when incremental EPS ≥ running EPS.

**Presentation:** Basic and Diluted on the face of P&L, equal prominence, all periods, even if negative or equal; disclose face value, numerator reconciliation to net profit, and denominator reconciliation.

**Worked anchors:** Basic (Ex.1) = 7,50,000 ÷ 1,17,000 = **Rs. 6.41**; Bonus restatement (Ex.2) 3.00 → **2.00** restated, current **2.50**; Rights (Ex.3) TERP **23**, factor **25/23**, EPS **4.21**, prior restated **3.68**; Diluted (Ex.4) **11,68,000 ÷ 6,85,000 = Rs. 1.71**, with the 10% pref (incremental EPS Rs. 5.00 > 1.71) excluded as anti-dilutive.
