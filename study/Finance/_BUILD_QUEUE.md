# Finance Subjects Build Queue — one ~500-page PDF each (Rule 1)

6 comprehensive finance-knowledge subjects. Concept-first + worked examples + diagrams + practice Q&A. One `<Subject>_FULL.pdf` per subject in `Finance/`. Batches of 6 chapters (concept+qa); rebuild PDF after; session-limit resilient (re-check disk, reschedule ~3600s). Target ~18-22 chapters/subject → ~500 pages.

Builder: `scratchpad/build_subject_pdf.py "C:/Users/saiku/Desktop/certifications/Finance/<S>" "<Name>" "C:/Users/saiku/Desktop/certifications/Finance/<Out>_FULL.pdf"`.

## 1. Markets — "Financial Markets & Instruments" → Markets/, Financial-Markets_FULL.pdf
01 intro-financial-system-and-markets · 02 primary-market-issuance · 03 secondary-markets-and-exchanges · 04 money-markets · 05 capital-markets-overview · 06 equity-instruments · 07 bond-and-debt-markets · 08 foreign-exchange-markets · 09 derivatives-markets-overview · 10 mutual-funds-and-etfs · 11 market-participants-intermediaries · 12 trading-mechanics-order-types · 13 market-indices · 14 clearing-settlement-depositories · 15 market-regulation · 16 market-efficiency · 17 alternative-investments · 18 commodities-markets · 19 international-markets · 20 fintech-and-innovation

## 2. Economics — "Economics for Finance" → Economics/, Economics-for-Finance_FULL.pdf
Micro: demand-supply, elasticity, consumer theory, production-costs, market structures (perfect comp/monopoly/oligopoly), factor markets, market failure. Macro: GDP-national-income, inflation, unemployment, business-cycles, aggregate-demand-supply, money-and-banking, monetary-policy, fiscal-policy, central-banking, exchange-rates, balance-of-payments, international-trade, economic-indicators-for-finance. (~20 ch)

## 3. Investments — "Investments & Portfolio Management" → Investments/, Investments-Portfolio-Management_FULL.pdf
risk-and-return, portfolio-theory-markowitz, efficient-frontier, capm, apt-multifactor, asset-allocation, portfolio-construction, equity-portfolio-mgmt, fixed-income-portfolio, performance-measurement (sharpe/treynor/alpha/attribution), market-efficiency-emh, behavioral-finance, investment-policy-statement, alternatives-in-portfolios, factor-investing, passive-vs-active. (~20 ch)

## 4. FixedIncome — "Fixed Income" → FixedIncome/, Fixed-Income_FULL.pdf
bond-features-and-types, bond-pricing, yield-measures, spot-forward-rates, term-structure-theories, duration, convexity, interest-rate-risk, credit-risk-and-spreads, credit-analysis, securitization-abs-mbs, money-market-yields, bond-strategies, inflation-linked-and-floaters. (~18 ch)

## 5. Derivatives — "Derivatives" → Derivatives/, Derivatives_FULL.pdf
intro-and-uses, forwards, futures, futures-pricing-and-hedging, options-basics-payoffs, option-strategies, put-call-parity, binomial-option-pricing, black-scholes, the-greeks, swaps-interest-rate, currency-and-other-swaps, credit-derivatives, hedging-with-derivatives, arbitrage-and-risk. (~18 ch)

## 6. Risk — "Risk Management" → Risk/, Risk-Management_FULL.pdf
intro-risk-management, types-of-risk, market-risk, value-at-risk, expected-shortfall, credit-risk, counterparty-risk, operational-risk, liquidity-risk, interest-rate-risk-alm, risk-measurement-and-models, basel-and-regulation, stress-testing-scenario, enterprise-risk-management, derivatives-in-risk-mgmt. (~18 ch)

## ✅ ALL 6 SUBJECTS BUILT (first pass). PDFs: Financial-Markets (~360pg), Economics-for-Finance (~390), Investments-Portfolio-Management (~305), Fixed-Income (~295), Derivatives (~320), Risk-Management (~295). Comprehensive, all concepts. ~2000 pages total.
## Optional: 2x-deepen pass to lift each to ~500 pages (large spend) — pending user decision.

## 7. Market Research — "Market Research Analyst Handbook" → sources_md/MARKET_RESEARCH_COMPLETE_HANDBOOK.md, Market_Research_Study_Guide.pdf
Added 2026-08-04: the one subject in the stock-market-roles cluster this library did not
previously cover (job_apply_agent/lib/roles.ts added a `market_research` target role).
Stage 1 (18pg): research design (exploratory/descriptive/causal), primary vs secondary
research, qualitative methods (IDIs/FGDs/ethnography), quantitative/survey design + sample
size math, data analysis (cross-tabs/segmentation/significance/conjoint), market sizing
(TAM/SAM/SOM worked example), competitive intelligence, consumer insights/reporting,
careers + interview Q&A. Built like TRA_COMPLETE_HANDBOOK.md (single-file handbook) via the
new generic `sources_md/build_handbook_pdf.py`. Same "build toward 2000 pages in stages"
plan as the rest of this library — later stages can 10x-deepen each PART into full chapters
with worked INR case studies, matching the depth of subjects 1-6 above.

## Stock-Market-Roles-Master_FULL.pdf (compiled, not a new subject)
Combines Equity & Capital Markets + Valuation + Investments-Portfolio-Management +
Technical-Research (career guide) + Technical-Analysis-Complete (deep book) +
Options-Trading-Complete (NSE F&O, deep book, both from trading_learning/) + the new
Market Research handbook into one **3,250-page** volume for the 3 stock-market target roles
(Senior Equity Research, Market Research, Technical Research — see
job_apply_agent/job_search/senior_research_skills.md). Scope is deliberately strict: only
stock-market content, not general finance — see 2026-08-04 note below. Rebuild via
`sources_md/merge_stock_market_master.mjs` (Node/pdf-lib — run `npm install` once in
`sources_md/`, its `package.json` pins the dependency) after any component PDF changes;
front matter source is `sources_md/_stock_market_roles_frontmatter.html`, regenerated via
`sources_md/_render_frontmatter.py`. Deliberately excludes the generic multi-role finance
subjects (01/02/04/06/07/08_*.pdf — Accounting/Corp Finance/Modeling/Credit/Derivatives-Quant/
Economics; framed for IB/Credit/FP&A broadly, not stock-market specifically) and
Finance-1_FULL.pdf (overlaps Investments component already merged in).

**2026-08-04**: user asked to grow this toward 3,000 pages "don't repeat same topics." First
pass added the 6 generic finance-interview subjects above (+333pg) — user corrected: "only add
contents related to stock market." Reverted that; added Options-Trading-Complete (998pg,
NSE F&O options — squarely stock-market, zero overlap with the charting book) instead, landing
at 3,250. Keep this scope boundary for any future stage: stock-market/equity/derivatives-on-
equity content only, not general corporate/credit/IB finance.

## Stage 3 (in progress): "each topic 1,000 pages minimum"
User's next ask: every section of the master ≥1,000 pages. Current per-section page counts:
Equity & Capital Markets 47 · Valuation 51 · Investments-Portfolio-Mgmt 320 · Technical Research
career guide 66 · **Technical Analysis Complete 1,747 (done)** · **Options Trading Complete 998
(~done)** · Market Research 18→**29** (first deepening pass, 2026-08-04: added research-brief/
objective-translation, 6 industry-worked design examples, full worked questionnaire incl. Van
Westendorp + choice-based conjoint task, panel data-quality checks, regression + conjoint
worked numeric examples, 4 more sector sizing examples, win-loss worked example, brand/ad-
research part, B2B research part, research-ops/vendor/ethics/DPDP-Act part, +14 Q&A). Still
~970pg short of 1,000 for this section alone.

**Honest scope note**: closing the remaining gap (Equity&CM, Valuation, Investments,
Technical-career, Market Research ≈ **3,400+ more pages** as of 2026-08-04) is a multi-session
undertaking — each deepening pass adds roughly 10-20pg per section. User confirmed pace:
"keep going every message" — continue additively each turn: pick the thinnest section, add
genuinely new sub-sections (worked examples, case studies, deeper frameworks — never restate
existing content), rebuild, refresh the master. Do not restate already-added content across
passes — check what a chapter/section already covers before adding to it.

**New persistent infra (2026-08-04)**: `sources_md/build_subject_pdf.py` — generic builder for
the chapter-folder subjects (`Finance/EquityCapitalMarkets/md/*.md`, `Finance/Valuation/md/*.md`,
`Finance/Investments/md/*.md`, etc., 18-20 chapters each). Replaces the old, now-gone
`scratchpad/build_subject_pdf.py`. Usage:
`python build_subject_pdf.py ../<SubjectDir> "<Title>" ../<Output>.pdf`. Switching to this
builder changed baseline page counts slightly (e.g. Equity & Capital Markets 47->61pg from the
builder alone, before any new content) since pagination differs marginally from whatever
produced the original PDFs — not a content change, just a re-render.

**Progress log**:
- Market Research: 18 -> 29pg (see stage-3 intro above for what was added).
- Equity & Capital Markets (`Finance/EquityCapitalMarkets/md/`): 47 -> 63pg. Deepened chapter 07
  (equity-research-process: added Channel Checks & Primary Research in Equity Analysis section
  incl. the SEBI insider-trading compliance boundary, and a full worked research note — "TechCo
  India Ltd" — DCF+comps+thesis+catalysts+risks+falsification end to end) and chapter 12
  (stock-pitch: added the full initiation-of-coverage note structure incl. sensitivity-table
  convention, two more worked pitches — banking sector P/B-via-ROE framework, tech-sector short
  disaggregating a blended NRR metric — and a sector-specific valuation frameworks quick
  reference: banks/NBFCs, insurance EV/VNB, cyclicals through-the-cycle EV/EBITDA, real-estate
  NAV, pre-profit tech). 18 other chapters in this subject (01-06, 08-11, 13-20) not yet touched
  — next pass on this subject should deepen those before returning to ch.07/12.
- **Valuation, big free win (2026-08-04)**: discovered the master was using `Finance/03_Valuation.pdf`
  (51pg, concept-chapters only) when `_components/Valuation_FULL.pdf` (405pg — same 18 chapters
  PLUS a full `qa/*_QA.md` set per chapter that 03_Valuation.pdf's build never included) already
  existed. Swapped the merge script to point at the FULL version. Valuation section: **51 -> 405pg,
  zero new writing** — effectively done for the 1,000pg target once 1-2 more deepening passes land.
  **Lesson for future passes**: before hand-writing new content for Equity/Investments/any other
  subject, check `_components/<Subject>_FULL.pdf` page count against what's actually wired into
  `merge_stock_market_master.mjs` — Equity & Capital Markets was checked and has no qa/ folder
  (genuinely needs new writing, already in progress), but always verify per-subject first.

- **Equity & Capital Markets gets a qa/ folder (2026-08-04)**: added `EquityCapitalMarkets/qa/`
  (mirroring Valuation/Investments' structure) with 4 chapters' worth of Q&A so far (07
  equity-research-process, 10 applied-equity-valuation, 12 stock-pitch, 20 indian-equity-markets
  — theory + worked numerical problems, same house style as Valuation's qa/). Updated
  `build_subject_pdf.py` to auto-include a chapter's `qa/<stem>_QA.md` sibling if present
  (interleaved right after its chapter, own TOC level-2 entry). 63 -> 71pg. 16 chapters still
  need qa files (01-06, 08-09, 11, 13-19) — next pass on this subject, write those before
  anything else, since this qa/ pattern is now the highest-leverage way to grow this subject
  (each QA file added roughly +2pg for ~20-30 min of work, matching Valuation's own ratio at
  scale: 18 qa files roughly matched or exceeded the size of the 18 concept chapters).

**Running total after 2026-08-04 stage-3 work: 3,639 pages** (Market Research 18->29, Equity & CM
47->71 (63 from content, +8 from the qa/ folder), Valuation 51->405 via the free-win swap).
