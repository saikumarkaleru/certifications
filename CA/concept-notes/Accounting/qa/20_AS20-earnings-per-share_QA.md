# Q&A — AS 20 — Earnings Per Share

A complete exam-oriented question bank. Every question is immediately followed by its full model answer. All computational data is internally consistent and reconciles.

---

## Section A — Concept-check Questions (test the WHY)

**A1. Why does AS 20 use a *weighted average* number of equity shares instead of the closing or opening number?**

EPS matches earnings (a flow generated over the whole year) with the capital that actually produced them. Shares issued for cash mid-year only worked for part of the year, so they should contribute proportionately. Using closing numbers would understate EPS (dividing full-year profit by capital not yet employed); using opening numbers would overstate it. Weighting by the fraction of the period the shares were outstanding gives a fair per-share figure.

**A2. Bonus and share splits are NOT time-weighted, yet a fresh cash issue is. Why the difference?**

A bonus/split brings **no new resources** into the company — the same earning power is simply divided into more shares. Because there is no change in resources, AS 20 treats the increased shares as if they had **always existed** and restates all prior periods (retrospective). A cash issue brings **new resources** that earn only from the issue date, so it is time-weighted (prospective).

**A3. Why is preference dividend deducted from net profit for Basic EPS, and does it matter whether the dividend is declared?**

Basic EPS measures earnings available to **equity** shareholders, so the prior claim of preference shareholders is removed. For **cumulative** preference shares the dividend for the year is deducted **whether or not it is declared** (the claim accrues). For **non-cumulative** shares, only the dividend **declared/provided** for the year is deducted.

**A4. What is the logic of the Theoretical Ex-Rights Price (TERP) adjustment for a rights issue?**

A rights issue at a price below fair value contains a **bonus element** (a gift) plus a genuine cash-raising element. AS 20 splits it: the bonus element is treated retrospectively via an **adjustment factor = Fair value before exercise ÷ TERP**, applied to all shares before the rights date and to prior-period EPS; the cash element is time-weighted from the rights date.

**A5. In Diluted EPS, why are potential equity shares only included if they are *dilutive*, and why must they be ranked?**

The purpose of Diluted EPS is to warn of the **maximum possible dilution**. A potential share is dilutive only if converting it **reduces** EPS (or increases loss per share); anti-dilutive items are ignored so a company cannot flatter its diluted figure. Because adding items one-by-one can flip a series from dilutive to anti-dilutive, they are ranked by **incremental EPS (most dilutive first)** and added sequentially, stopping when EPS starts to rise.

**A6. Why does the treasury stock method assume options are bought back at *average* market price?**

Options dilute only to the extent they are issued **below** fair value. The proceeds on exercise are assumed reinvested to buy back shares at the average market price; only the "free" shares (issued minus bought back) are dilutive. Using the average price reflects the year's typical fair value and prevents cherry-picking a favourable spot price.

---

## Section B — Graded Computational Problems

### B1 (Easy) — Time-weighting a cash issue and a buy-back

Data: Net profit after tax Rs 45,00,000. Equity shares on 1 Apr 2023: 10,00,000. On 1 Aug 2023 issued 3,00,000 shares for cash at fair value. On 1 Jan 2024 bought back 1,20,000 shares. No preference shares. Compute Basic EPS for FY 2023-24.

**Solution — weighted average shares:**

| Period | Shares | Months | Weighted |
|---|---|---|---|
| 1 Apr (opening) | 10,00,000 | 12/12 | 10,00,000 |
| 1 Aug cash issue | +3,00,000 | 8/12 | +2,00,000 |
| 1 Jan buy-back | −1,20,000 | 3/12 | −30,000 |
| **Weighted average** | | | **11,70,000** |

Basic EPS = 45,00,000 ÷ 11,70,000 = **Rs 3.85**.

### B2 (Easy–Medium) — Bonus issue, retrospective restatement

Data: Net profit — FY 2022-23 Rs 18,00,000; FY 2023-24 Rs 24,00,000. Equity shares throughout 2022-23: 5,00,000. On 1 Sep 2023 the company made a bonus issue of 1 share for every 5 held. Compute Basic EPS for 2023-24 and the restated comparative for 2022-23.

**Solution:** Bonus shares = 5,00,000 × 1/5 = 1,00,000. Total shares = 6,00,000. A bonus is **not time-weighted**; treat as always outstanding and restate the prior year.

- Basic EPS 2023-24 = 24,00,000 ÷ 6,00,000 = **Rs 4.00**
- Restated EPS 2022-23 = 18,00,000 ÷ 6,00,000 = **Rs 3.00** (originally reported Rs 3.60 = 18,00,000 ÷ 5,00,000).

Reconciliation: both years now share the same 6,00,000 denominator, so the EPS trend (Rs 3.00 → Rs 4.00) is comparable.

### B3 (Medium) — Rights issue with TERP adjustment factor

Data: Equity shares before rights: 8,00,000. On 1 Oct 2023 a rights issue of 1 share for every 4 held was made at Rs 20; fair value (cum-rights) immediately before exercise was Rs 30. Net profit FY 2023-24 Rs 40,00,000; FY 2022-23 Rs 33,00,000 (8,00,000 shares throughout). Compute Basic EPS 2023-24 and restated 2022-23.

**Solution:**

Rights shares = 8,00,000 × 1/4 = 2,00,000. Shares after rights = 10,00,000.

TERP = [(30 × 8,00,000) + (20 × 2,00,000)] ÷ 10,00,000
= [2,40,00,000 + 40,00,000] ÷ 10,00,000 = 2,80,00,000 ÷ 10,00,000 = **Rs 28**.

Adjustment factor = Fair value before ÷ TERP = 30 ÷ 28 = **1.0714**.

Weighted average shares 2023-24:

| Period | Computation | Weighted |
|---|---|---|
| 1 Apr–30 Sep (pre-rights, adjusted) | 8,00,000 × 30/28 × 6/12 | 4,28,571 |
| 1 Oct–31 Mar (post-rights) | 10,00,000 × 6/12 | 5,00,000 |
| **Total** | | **9,28,571** |

Basic EPS 2023-24 = 40,00,000 ÷ 9,28,571 = **Rs 4.31**.

Restated EPS 2022-23 = 33,00,000 ÷ (8,00,000 × 30/28) = 33,00,000 ÷ 8,57,143 = **Rs 3.85** (before adjustment it was Rs 4.13).

### B4 (Exam-hard) — Diluted EPS: options + debentures + anti-dilution sequencing

Data (FY 2023-24):
- Net profit after tax: Rs 53,00,000
- 15% Convertible preference shares: Rs 20,00,000 (dividend Rs 3,00,000), convertible into 50,000 equity shares
- Weighted average equity shares: 20,00,000
- 12% Convertible debentures: Rs 50,00,000 face, convertible into 4,00,000 equity shares
- Options: 2,00,000 options, exercise price Rs 15; average market price Rs 25
- Tax rate: 30%

Compute Basic and Diluted EPS.

**Step 1 — Basic EPS.** Earnings for equity = 53,00,000 − 3,00,000 (preference dividend) = 50,00,000.
Basic EPS = 50,00,000 ÷ 20,00,000 = **Rs 2.50**.

**Step 2 — Incremental EPS of each potential equity share:**

- *Options (treasury stock method):* Buy-back = 2,00,000 × 15/25 = 1,20,000 shares; incremental (free) shares = 2,00,000 − 1,20,000 = **80,000**. No earnings effect. Incremental EPS = 0 ÷ 80,000 = **Rs 0.00**.
- *Debentures:* Interest = 12% × 50,00,000 = 6,00,000; after-tax add-back = 6,00,000 × (1 − 0.30) = 4,20,000. Incremental EPS = 4,20,000 ÷ 4,00,000 = **Rs 1.05**.
- *Preference:* Dividend saved = 3,00,000 (no tax effect). Incremental EPS = 3,00,000 ÷ 50,000 = **Rs 6.00**.

**Step 3 — Rank most-dilutive first and add sequentially:** Options (0.00) → Debentures (1.05) → Preference (6.00).

| Stage | Numerator (Rs) | Denominator | EPS (Rs) | Effect |
|---|---|---|---|---|
| Basic | 50,00,000 | 20,00,000 | 2.50 | — |
| + Options | 50,00,000 | 20,80,000 | 2.40 | Dilutive ✓ |
| + Debentures | 54,20,000 | 24,80,000 | 2.19 | Dilutive ✓ |
| + Preference | 57,20,000 | 25,30,000 | 2.26 | Anti-dilutive ✗ (exclude) |

Adding preference raises EPS from 2.19 to 2.26, so it is anti-dilutive and excluded.

**Diluted EPS = Rs 2.19** (54,20,000 ÷ 24,80,000). Present Basic Rs 2.50 and Diluted Rs 2.19 on the face of the P&L.

---

## Section C — Past-paper-style Full Question (ICAI pattern)

**C1.** Sunrise Ltd furnishes the following for the year ended 31 March 2024:
- Net profit for the year after tax: Rs 75,00,000
- 10% Cumulative preference share capital: Rs 25,00,000 (dividend not yet declared)
- Equity shares on 1 April 2023: 12,00,000 of Rs 10 each
- On 1 July 2023, issued 4,00,000 equity shares for cash at fair value
- On 1 January 2024, made a bonus issue of 2 shares for every 5 shares then held
- 9% Convertible debentures Rs 40,00,000 convertible into 3,00,000 equity shares (outstanding all year); tax rate 30%

Compute Basic and Diluted EPS with reconciliations.

**Model answer:**

*Numerator for Basic EPS:* Preference shares are **cumulative**, so deduct the year's dividend even though not declared: 10% × 25,00,000 = 2,50,000.
Earnings for equity = 75,00,000 − 2,50,000 = **Rs 72,50,000**.

*Weighted average shares.* First find shares before the bonus, then apply the bonus factor retrospectively (bonus of 1 Jan 2024 is treated as always outstanding, including on the July issue).

Shares on which bonus is computed = 12,00,000 + 4,00,000 = 16,00,000. Bonus = 16,00,000 × 2/5 = 6,40,000. Bonus factor = (16,00,000 + 6,40,000)/16,00,000 = 22,40,000/16,00,000 = **1.4**.

| Period | Shares | Bonus factor | Months | Weighted |
|---|---|---|---|---|
| 1 Apr (opening) | 12,00,000 | ×1.4 | 12/12 | 16,80,000 |
| 1 Jul cash issue | 4,00,000 | ×1.4 | 9/12 | 4,20,000 |
| **Weighted average** | | | | **21,00,000** |

Basic EPS = 72,50,000 ÷ 21,00,000 = **Rs 3.45**.

*Diluted EPS.* Debentures: interest = 9% × 40,00,000 = 3,60,000; after-tax add-back = 3,60,000 × 0.70 = 2,52,000. Incremental EPS = 2,52,000 ÷ 3,00,000 = Rs 0.84 < Basic 3.45 → dilutive.

- Diluted numerator = 72,50,000 + 2,52,000 = 75,02,000
- Diluted denominator = 21,00,000 + 3,00,000 = 24,00,000
- **Diluted EPS = 75,02,000 ÷ 24,00,000 = Rs 3.13**.

*Presentation on face of Statement of Profit and Loss:*

| | Basic | Diluted |
|---|---|---|
| Earnings per equity share (Rs) | 3.45 | 3.13 |

### Reconciliation of denominator (disclosure)

| | Shares |
|---|---|
| Weighted average for Basic EPS | 21,00,000 |
| Add: dilutive convertible debentures | 3,00,000 |
| Weighted average for Diluted EPS | 24,00,000 |

---

## Section D — MCQs / Case Scenarios

**D1.** A company reports a net **loss**. It holds convertible debentures whose conversion would reduce the loss per share. For Diluted EPS these debentures are:
(a) Dilutive (b) Anti-dilutive (c) Ignored entirely (d) Added to numerator only.
**Answer: (b) Anti-dilutive.** In a loss year, anything that *reduces* loss per share is anti-dilutive and excluded — potential shares can never make a loss look worse.

**D2.** Bonus shares issued after the balance-sheet date but before the financial statements are approved:
(a) Ignored (b) Adjusted only in next year (c) Adjusted retrospectively in EPS of the current and all prior periods presented (d) Time-weighted.
**Answer: (c).** AS 20 requires EPS to be restated for bonus/splits occurring even after year-end but before approval, for all periods shown.

**D3.** Adjustment factor for a rights issue equals:
(a) TERP ÷ Fair value before (b) Fair value before ÷ TERP (c) Rights price ÷ TERP (d) Fair value before ÷ Rights price.
**Answer: (b) Fair value before exercise ÷ TERP.** This factor (>1) grosses up pre-rights shares for the embedded bonus element.

**D4.** For the treasury stock method on options, the number of dilutive shares is:
(a) Total options (b) Options × exercise price ÷ market price (c) Options × (1 − exercise price ÷ average market price) (d) Zero.
**Answer: (c).** Only the "free" shares (issued less those notionally repurchased at average market price) are dilutive.

**D5.** Partly paid equity shares are included in the weighted average:
(a) At full number (b) Ignored (c) To the extent entitled to dividends relative to fully paid shares (d) Only if fully called.
**Answer: (c).** They rank as a fraction of a fully paid share based on dividend entitlement.

**D6. Case:** X Ltd's Basic EPS is Rs 5.00. It has one class of convertible preference shares whose incremental EPS is Rs 5.00 (exactly equal). Including it in Diluted EPS is:
(a) Mandatory (b) Optional (c) Excluded, as it is not dilutive (d) Anti-dilutive.
**Answer: (c) Excluded.** A potential share is dilutive only if it **reduces** EPS; one that leaves EPS unchanged is not dilutive and is left out.

**D7.** Which is deducted from net profit for Basic EPS numerator when computing earnings for equity shareholders?
(a) Equity dividend (b) Tax on distributed profits and preference dividend including any arrears deducted this year for cumulative shares (c) Interest on debentures (d) Proposed bonus.
**Answer: (b).** Preference dividend (current year, cumulative whether declared or not) and its attributable distribution tax reduce earnings available to equity.

**D8. Case:** During the year a company issued shares in a business combination (purchase) on 1 October. These shares are:
(a) Retrospectively adjusted (b) Ignored (c) Included in the weighted average from 1 October (the date consideration/resources were recognised) (d) Excluded until next year.
**Answer: (c).** Shares issued for consideration (e.g. an acquisition) are weighted from the date they are recognised, since resources are received then — unlike a bonus.
