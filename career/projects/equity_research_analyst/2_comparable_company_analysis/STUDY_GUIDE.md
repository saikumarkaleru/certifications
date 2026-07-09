# Comparable Company Analysis — Interview Study Guide

A cheat sheet for defending every line of this project in an equity-research
interview. The model pulls a **real** target and peers from yfinance (default:
Apple vs six mega-cap tech names), computes their trading multiples, and values
the target off the peer set.

---

## 1. 30-Second Pitch
"I built a live comparable-company analysis. It pulls a target and six real
peers from yfinance, computes five trading multiples for each — P/E, EV/EBITDA,
EV/Revenue, P/B and PEG — and summarises the peer set with the median, mean and
quartiles. I apply the peer median multiple to the target's own metrics to get
an implied price under each method, which forms a football-field range I compare
to the market price. Then I run a rich/cheap screen two ways: z-scores of the
raw multiples, and an OLS regression of EV/EBITDA on growth and margin so I can
tell whether a name is expensive because it deserves to be — high growth, fat
margins — or expensive for no fundamental reason. For Apple today the comps put
it above the peer range, and both screens flag it as rich versus fundamentals."

---

## 2. What Comps Are and Why Equity Research Uses Them
Comparable-company analysis is **relative** (or *market*) valuation: a company
should be worth roughly what similar companies trade for, per dollar of
earnings, EBITDA, revenue or book value. It complements a DCF (project 1): the
DCF gives an intrinsic view from cash flows; comps give a market view — what
investors are actually paying for comparable businesses right now.

Analysts use comps because they are fast, grounded in observable prices, and
easy to communicate ("the group trades at ~18x EBITDA; our name is at 27x").
The art is choosing a genuinely comparable peer set and knowing which multiple
fits the business.

---

## 3. THE Key Answers (memorize these)
**Equity vs enterprise multiples.** P/E and P/B are *equity* multiples — they
use price / market cap, so they sit *after* the capital structure and pair with
equity metrics (EPS, book value). EV/EBITDA and EV/Revenue are *enterprise*
multiples — they use enterprise value, which is capital-structure neutral, so
they pair with pre-interest metrics (EBITDA, revenue). That's why for an
enterprise multiple I get an implied **EV** first, then subtract net debt to get
to equity value per share.

**Why the median, not the mean?** The median is robust to one outlier peer that
would drag the mean around. I lead with the median and also show quartiles to
convey the spread.

**Why EV/EBITDA is the workhorse.** It's neutral to leverage and to D&A
policy/tax, so it compares the operating businesses cleanly across companies
with different capital structures — which is exactly what you want in a peer set.

**PEG.** P/E divided by the earnings growth rate (in %). It adjusts a P/E for
growth: a 30x P/E on 60% growth (PEG 0.5) can be cheaper than a 15x P/E on 10%
growth (PEG 1.5). Rule of thumb: PEG under 1 looks cheap for the growth.

---

## 4. Walkthrough (module by module)
1. **`src/comps/data.py`** — pulls the target + peers from yfinance (price,
   shares, market cap, debt, cash, revenue, EBITDA, net income, book equity,
   EPS, growth, margin). Caches to `input/` and falls back to the cache, then a
   bundled snapshot, so it always runs offline.
2. **`src/comps/multiples.py`** — computes EV = market cap + debt − cash and the
   five multiples per company, guarding against negative/zero denominators.
3. **`src/comps/stats.py`** — the peer summary (median/mean/quartiles, target
   excluded) and the two screens: z-scores and the OLS regression.
4. **`src/comps/valuation.py`** — applies peer median multiples to the target
   for an implied price per method and the football-field range.
5. **`src/comps/report.py`** — writes the Excel workbook (Comps, Multiples,
   Implied, Screen) and the football-field chart.
6. **`main.py`** — orchestrates and prints the console summary.

---

## 5. The Rich/Cheap Screen (the differentiated bit)
A raw multiple alone doesn't say "expensive" — a high multiple can be *earned*
by better fundamentals. So I regress the peer set's **EV/EBITDA** on **revenue
growth** and **EBITDA margin**:

`fair EV/EBITDA = b0 + b1·growth + b2·margin`

Each name's **residual** (actual − predicted) is the verdict: a positive
residual means it trades richer than its growth and margins justify (RICH vs
fundamentals); a negative residual means cheaper (CHEAP). With only ~7 names the
R² is low and the fit is illustrative — I'd never trade off it blindly — but it
demonstrates the right idea: control for fundamentals before calling something
expensive. The z-score screen is the simpler cousin: how many standard
deviations a name's raw multiple sits from the peer average.

---

## 6. Interview Q&A

**Q1. "Walk me through a comps analysis."**
Pick a comparable peer set, compute trading multiples for each (P/E, EV/EBITDA,
EV/Revenue, P/B, PEG), take the peer median for each, apply those to the
target's own metrics to get an implied value per method, and compare the
resulting range to the current price. EV multiples give an implied EV, so
subtract net debt to reach equity value per share.

**Q2. "Why do EV/EBITDA and EV/Revenue use EV while P/E uses price?"**
Because EBITDA and revenue are pre-interest — they belong to all capital
providers — so they must be compared to enterprise value. Earnings and book
value are post-interest, equity-holder concepts, so they pair with price/market
cap. Mixing them (e.g. EV/EPS) would be inconsistent.

**Q3. "Apple's P/B implies a much lower price than the other methods — why?"**
P/B is a weak multiple for Apple: years of buybacks have shrunk its book equity,
so it trades at ~40x book while peers are ~7x. Applying the peer P/B to Apple's
tiny book gives an artificially low number. It's a good reminder to weight the
multiples that fit the business — here EV/EBITDA and P/E — and treat P/B as
noise for asset-light, buyback-heavy companies.

**Q4. "How do you pick comparables?"**
Same industry/business model, similar size, growth, margins and geography.
The tighter the peer set, the more meaningful the multiples. My set is mega-cap
tech, which is convenient and liquid but broad; in practice I'd tighten it (e.g.
pure software, or hardware) depending on the target.

**Q5. "A stock trades at a premium multiple — is it expensive?"**
Not necessarily. A premium can be justified by faster growth, higher margins,
or lower risk. That's exactly why I run the regression screen: it strips out the
part of the multiple explained by growth and margin, and the residual tells you
whether the premium is *earned* or not.

**Q6. "Comps vs DCF — which do you trust?"**
They answer different questions. Comps tell you what the market is paying for
similar businesses today (relative); a DCF tells you what the cash flows are
worth intrinsically. I use them together: if comps and DCF disagree sharply,
that gap is the thesis — either the market is mispricing the group or my cash-
flow assumptions are off.

**Q7. "What are the limitations of comps?"**
No two companies are identical; multiples move with sentiment (so comps inherit
market mispricing); accounting differences distort EBITDA and book value; and a
median hides a wide spread. I mitigate with a clean peer set, EV multiples for
comparability, quartiles to show dispersion, and the fundamentals screen.

---

## 7. Vocabulary
- **Trading multiple** — a ratio of value to a financial metric (e.g. EV/EBITDA)
  used to compare companies.
- **P/E** — Price / Earnings per share; equity multiple.
- **EV/EBITDA** — Enterprise Value / EBITDA; leverage- and D&A-neutral; the comp
  workhorse.
- **EV/Revenue** — Enterprise Value / Revenue; used when earnings/EBITDA are thin
  or margins vary widely.
- **P/B** — Price / Book value per share; price vs. accounting equity.
- **PEG** — P/E divided by the earnings growth rate (%); a growth-adjusted P/E.
- **Enterprise Value (EV)** — market cap + total debt − cash; value of the whole
  business to all capital providers.
- **Net debt** — total debt minus cash; the bridge from EV to equity value.
- **Median / quartiles** — robust central-tendency and spread measures across
  the peer set.
- **Z-score** — how many standard deviations an observation sits from the mean.
- **Residual (regression)** — actual minus predicted; here, how rich/cheap a name
  is versus what its growth and margin justify.
- **Football field** — a chart showing the valuation range implied by each
  method against the current price.
