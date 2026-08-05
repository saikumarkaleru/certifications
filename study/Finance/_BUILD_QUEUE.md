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

**2026-08-04, later pass**: added qa/ files for 5 more EquityCapitalMarkets chapters (02
primary-markets-IPO, 03 secondary-markets-trading, 04 market-participants, 05 equity-instruments,
06 market-indices — 9 of 20 chapters now have qa/). 71 -> 81pg. Remaining 11 chapters without
qa/: 01, 08, 09, 11, 13-19.

**2026-08-04, later pass 2**: added qa/ for 4 more chapters (01 overview, 08 fundamental-analysis,
09 three-statement-modeling, 11 research-note-thesis — 13 of 20 chapters now have qa/). 81 -> 89pg.
Remaining 7 chapters without qa/: 13-19 (technical-analysis-essentials, market-efficiency-
behavioral-finance, corporate-actions, capital-raising-followons, sell-side-vs-buy-side,
portfolio-construction-risk, esg-in-equity-analysis).

**2026-08-04, later pass 3**: added qa/ for the final 7 chapters (13 technical-analysis-essentials,
14 market-efficiency-behavioral-finance, 15 corporate-actions, 16 capital-raising-followons, 17
sell-side-vs-buy-side, 18 portfolio-construction-risk incl. worked Sharpe/alpha/information-ratio
numericals, 19 esg-in-equity-analysis). **All 20/20 chapters in EquityCapitalMarkets now have
qa/ — this subject's qa/ pass is complete.** 89 -> 108pg (47pg -> 108pg total across this whole
stage-3 effort on this subject).

**Running total after 2026-08-04 stage-3 work: 3,676 pages** (Market Research 18->29, Equity & CM
47->108 via content + full 20/20 qa/ coverage, Valuation 51->405 via the free-win swap).

**Checked Investments**: already has full 18/18 qa/ coverage (matches its 320pg build) — no
further qa/-folder work needed there.

**2026-08-04, TRA handbook near-miss (important lesson)**: attempted to deepen
`Technical_Research_Study_Guide.pdf` (66pg) by expanding `sources_md/TRA_COMPLETE_HANDBOOK.md`
and rebuilding via `build_handbook_pdf.py` — the rebuild produced only 27pg, LESS than the
existing 66pg file. Investigated: the committed 66pg PDF was **not actually built from
TRA_COMPLETE_HANDBOOK.md at all** — it came from a richer, illustrated pipeline
(`study/trading_learning/learn/build_illustrated_handbook.py`, diagram+what-it-is+why-it-works+
psychology+trade-plan format) whose markdown source no longer exists in this repo (the PDF was
merged in from a prior workspace as a pre-built artifact — see `git log --follow` on the file).
**Restored the original 66pg file via `git checkout`** rather than overwriting it with the
thinner rebuild. Lesson for any future file: before rebuilding ANY existing PDF from a source
file, sample-compare the current committed PDF's actual text against the source you're about to
build from — matching filenames/topics doesn't guarantee they're actually linked, especially
after repo reorganisations.
Instead, built the enriched TRA_COMPLETE_HANDBOOK.md (worked Greeks/straddle numericals,
position-sizing/R-multiple worked trade, backtested-strategy-metrics worked example, two full
worked trade setups, 12-Q interview appendix — all genuinely new, non-overlapping with the
original 66pg file's different content) as a **separate new file**,
`Technical_Research_Deepening_Handbook.pdf` (27pg), added as its own master section (4b) rather
than replacing anything.

**2026-08-04, Market Research deepening pass 2**: added 3 new parts — PART 13 (Digital & Social
Research Methods: social listening, web/app analytics + A/B testing, MROCs, mobile ethnography/
passive metering), PART 14 (Retail & Shopper Research: share of shelf, planogram testing, retail
audits, mystery shopping, e-commerce share-of-search), PART 15 (International & Cross-Cultural
Research: translation/back-translation, cultural response-style bias, multi-country fieldwork
logistics, India-specific adaptation) — plus a full worked k-means segmentation case study (6.10)
and 6 more interview Q&A. 29 -> 37pg.

**Running total after all 2026-08-04 stage-3 work: 3,712 pages.**

**Status of all 7 sections**: Technical Analysis 1,747 (done) · Options Trading 998 (~done) ·
Valuation 405 · Investments 320 · Equity & Capital Markets 109 · Market Research 37 · Technical
Research career guide 66 + Deepening Handbook 27 = 93. Five sections still well short of 1,000.
Every section that had a "free" structural lever (missing qa/ folder, an unused pre-built _FULL
version) has now had it applied — all further growth from here requires genuinely new written
content (worked examples, new sub-topics), at roughly the same pace demonstrated in this stage's
passes (~10-40pg per deepening pass).

**2026-08-04, Equity-CM worked-examples pass (beyond qa/)**: added a 5th worked example to ch.18
(4-stock portfolio construction/concentration trade-off + factor-investing diversification
example), a 4th+5th to ch.02 (full IPO subscription/allotment mechanics incl. retail-lottery-vs-
NII-proportionate allotment math, and a contrasting weak-demand/undersubscribed-QIB scenario), a
4th to ch.15 (full dividend-date sequence with real dates, tender-offer-vs-open-market buyback
comparison), and a 4th+5th to ch.06 (sized passive-flow impact of an index inclusion in ₹cr and
days-of-volume terms, and a free-float-change-without-a-rebalance example). 108 -> 109pg.
**Note**: page growth was smaller than the ~2,600 words added would suggest (word count confirmed
via `wc -w`, content confirmed present in the rendered PDF via text search) — each chapter+qa
unit apparently had trailing whitespace slack that absorbed most of the new text without adding
full pages. Content is genuine and verified; just be aware the page-count/word-count ratio isn't
perfectly linear when editing already-existing chapters (vs. this is much more linear when adding
brand-new qa/ files or brand-new PART sections, which force clean page breaks).

**2026-08-04, autonomous wake-cycle pass 1** (user asked for continuous 10-min work cycles):
added PART 16 (Advanced Pricing Research & Revenue Management: BPTO, price elasticity worked
example, dynamic/revenue-management pricing, pricing-research pitfalls incl. hypothetical bias)
and PART 17 (Syndicated Data & Panel-Based Research: retail-audit vs household-panel distinction,
key syndicated metrics — distribution/penetration/buying-rate/source-of-growth — and limitations)
to Market Research. 37 -> 41pg. Master: 3,713 -> 3,717 pages.

**2026-08-04, autonomous wake-cycle pass 2**: added PART 15 (Intermarket Analysis: bonds-equities,
commodities-currencies incl. USD/INR-crude relationship, USD-commodities, bonds-commodities, a
worked multi-signal confluence example, and limits/regime-breakdown caveats) and PART 16 (Building
a Systematic Trading System: strategy components, a fully-specified worked trend-following
strategy with ATR-based stops, why explicit specification matters even for discretionary traders)
to the Technical Research Deepening Handbook. 27 -> 31pg. Also fixed two more stale frontmatter
row page-counts (TRA deepening handbook, Market Research) that were still showing pre-update
numbers. Master: 3,717 -> 3,720 pages.

**2026-08-04, autonomous wake-cycle pass 3**: added PART 18 (New Product Development & Concept
Testing: NPD funnel, concept screening vs testing, the standard concept-test measurement battery,
monadic/sequential-monadic/comparative designs, a worked top-box-score interpretation example
incl. norms-database benchmarking, product/sensory testing incl. blind-vs-branded and JAR scales)
and PART 19 (Category Management & Trade Marketing Research: assortment/incrementality analysis,
trade-promotion-effectiveness research incl. the pull-forward/pantry-loading effect and ROI
calculation, the retailer-relationship angle) to Market Research — genuine, previously-uncovered
topics (NPD/concept testing especially was a real gap). 41 -> 45pg. Master: 3,720 -> 3,724 pages.

**2026-08-04, rendering pipeline upgrade (user asked for charts/images, not just text)**:
investigated why the PDFs were text-heavy and found two real, fixable defects in
`build_subject_pdf.py`/`build_handbook_pdf.py`, not a content gap:
1. **Mermaid diagrams were rendering as raw text**, not diagrams — many EquityCapitalMarkets
   chapters (and others) have ```mermaid fenced blocks, but Chrome's print-to-pdf had no mermaid.js
   loaded, so they rendered as plain code text. Fixed by downloading `mermaid.min.js` locally
   (`sources_md/vendor/mermaid.min.js`, no CDN dependency at build time) and injecting an init
   script that converts `<pre><code class="mermaid">` blocks into real rendered SVG diagrams;
   bumped Chrome's `--virtual-time-budget` 30000->60000ms to give rendering time to complete.
2. **Markdown tables were silently broken** — python-markdown's `tables` extension requires a
   blank line before a table, and most tables in this content immediately follow a bold
   `**Label:**` line with no blank line, so they rendered as raw pipe-delimited text instead of
   HTML tables. Fixed with a preprocessing pass (`ensure_blank_line_before_tables()`) in both
   builders that inserts the missing blank line automatically — fixes every table across the
   whole library without touching any of the ~400 source markdown files individually.
Both fixes verified visually (rendered pages to PNG and inspected) before rebuilding for real.

**New: real charts, not just diagrams**. Added `sources_md/generate_charts.py`
(matplotlib, `python generate_charts.py` to regenerate) producing 5 PNGs in `sources_md/charts/`:
segmentation scatter plot (Market Research 6.10), price-elasticity curve (16.2), TAM/SAM/SOM
funnel (7.1), long-straddle payoff diagram (TRA 5.9), backtest equity-curve+drawdown chart
(TRA 10.5) — embedded via markdown image syntax at each worked example. Added `img { max-width:
92%; ... border ... }` CSS to both builders for clean, bordered, centered image rendering.

**Rebuilt affected PDFs**: Equity & Capital Markets 109->115pg (diagrams+tables now real),
Market Research 45->46pg, TRA Deepening Handbook 31->32pg (both +1 chart each net of table fix).
Master: 3,724 -> 3,733 pages.

**Note for future builds**: any NEW subject/handbook chapter with a mermaid diagram or a table
immediately after a bold label will now render correctly automatically — no special handling
needed, both fixes are baked into the two shared builder scripts.

**2026-08-04, autonomous wake-cycle: 3 more charts**: added `efficient_frontier.png` (4,000
simulated portfolios, individual assets, max-Sharpe tangency portfolio, Capital Market Line) to
Equity & Capital Markets ch.18; `candlestick_ma_rsi.png` (candlestick chart with 50/200-day MA
and RSI panel) to TRA handbook Part 3.1; `brand_funnel.png` (unaided->aided->consideration->
trial->repeat->loyal funnel) to Market Research Part 10.2. Caught and fixed two chart-generation
bugs before committing: the efficient-frontier chart's axis was dominated by the CML line's
extrapolation (fixed with explicit xlim/ylim based on the portfolio cloud, not the line), and the
candlestick chart's moving averages had edge-artifact spikes from `np.convolve(mode='same')`
(fixed with a proper trailing/backward-looking `trailing_ma()` helper, NaN-padded at the front
only). Both verified visually before rebuilding. Equity & CM 115pg (unchanged page count, image
absorbed into existing chapter space), TRA 32->33pg, Market Research 46pg (unchanged). Master:
3,733 -> 3,734 pages.

**2026-08-04, autonomous wake-cycle: 3 more charts (11 total now)**: `nps_driver_analysis.png`
(horizontal bar chart of regression betas, not-significant driver greyed out) and
`conjoint_attribute_importance.png` (pie chart of attribute importance %) added to Market
Research 6.7/6.8; `greeks_across_strikes.png` (Delta/Gamma/Theta curves across strikes, real
Black-Scholes math via scipy.stats.norm) added to TRA Part 5.4. Market Research 46->47pg, TRA
33->34pg. Master: 3,734 -> 3,736 pages.

**2026-08-04, checked Investments before touching it**: test-rebuilt Investments/ via
`build_subject_pdf.py` (301pg vs the original 320pg _components file) — close enough, and a text
sample confirmed genuinely matching content (same chapter text), unlike the TRA near-miss. But
the original has a dedicated TOC page and LaTeX-rendered math my builder doesn't produce, so
**deliberately did not overwrite it** — not worth the risk for a marginal page gain. If Investments
needs deepening later, follow the TRA pattern (a separate additional file, not an overwrite) unless
the TOC/LaTeX gap is closed in the builder first.

Added 2 more worked examples to Equity & Capital Markets chapters not yet touched: ch.09
(three-statement-modeling — full working-capital schedule driven off DSO/DIO/DPO days with a
2-year ΔNWC calc, and a "sanity-check the model's implied ratios" example) and ch.19 (ESG —
quantifying a governance discount via a WACC premium in an actual DCF re-run, and using India's
BRSR disclosure data as a real research input rather than a compliance checkbox). 115 -> 116pg.
Master: 3,736 -> 3,737 pages.

**2026-08-05, autonomous wake-cycle**: added worked examples to ch.14 (market efficiency —
a weak-form-efficiency backtest example showing edge disappearing after transaction costs, and
an analyst-target-price anchoring example) and ch.17 (sell-side vs buy-side — a full worked
"2-and-20-with-a-hurdle" fee calculation, and how MiFID-II-style research unbundling changed
sell-side economics in practice). 116 -> 117pg. Master: 3,737 -> 3,738 pages.

**2026-08-05, autonomous wake-cycle**: added worked examples to ch.13 (technical-analysis-
essentials — a false-golden-cross example testing the "probabilities not certainties" discipline,
and a fundamentals-plus-technicals entry-timing example) and ch.20 (Indian-equity-markets
capstone — DII/SIP-flow offset to FPI selling, and a circuit-breaker mechanics example). 117 ->
118pg. Master: 3,738 -> 3,739 pages.

**Chapters in EquityCapitalMarkets with worked-example additions so far**: 02, 06, 07, 09, 12, 13,
14, 15, 17, 18, 19, 20 (12 of 20). Remaining untouched beyond their original 3 examples: 01, 03,
04, 05, 08, 10, 11, 16 (8 chapters) — good candidates for the next pass.

**2026-08-05, autonomous wake-cycle**: added worked examples to ch.04 (market-participants —
hedge fund/PMS mandate-flexibility example, custodian-vs-broker settlement-failure scenario) and
ch.05 (equity-instruments — a full worked ADR ratio/arbitrage-band calculation, and why a company
chooses preferred shares over debt for covenant/control reasons). Page count unchanged (118, both
absorbed into existing whitespace) but content verified present (file size grew 2272KB->2282KB).
Master stays 3,739 pages this pass — chapters with worked-example additions now: 02, 04, 05, 06,
07, 09, 12, 13, 14, 15, 17, 18, 19, 20 (14 of 20). Remaining: 01, 03, 08, 10, 11, 16.

**2026-08-05, autonomous wake-cycle: 2 more new PARTs**: added PART 20 (Marketing Mix Modeling &
Media Effectiveness Research: adstock/carryover, diminishing-returns saturation, marginal-ROI
budget reallocation with a worked TV-vs-digital example) and PART 21 (Customer Retention, Churn &
Lifetime Value Research: contractual vs non-contractual and voluntary vs involuntary churn,
predictive churn modelling's research contribution, a worked CLV formula example, and the
CAC:CLV ratio connecting retention back to acquisition economics) to Market Research. 47 -> 51pg
— confirms new-PART additions add pages far more reliably than mid-chapter insertions (this
session's recurring lesson). Also fixed 3 more stale frontmatter row counts (Equity & CM,
TRA Deepening Handbook, Market Research) that had drifted from actual page counts across recent
passes. Master: 3,739 -> 3,743 pages.

**2026-08-05, autonomous wake-cycle: 2 new TRA parts**: added PART 17 (Seasonality, Calendar
Effects & Market Cycles: Santa Claus rally, Muhurat trading, result-season/expiry-day patterns,
sector rotation via relative strength, honest limits of seasonal edges) and PART 18 (Algorithmic
Execution & Market Microstructure: VWAP/TWAP benchmarks, iceberg orders/hidden liquidity, market
impact and why "the chart says buy" isn't the whole execution story — directly relevant crossover
with a derivatives-desk background). 34 -> 37pg. Master: 3,743 -> 3,746 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 22 (Neuromarketing & Implicit
Measurement Techniques to Market Research: eye-tracking, facial coding, IAT, GSR, where implicit
methods add genuine value vs are overused, practical/ethical constraints incl. heightened DPDP
obligations for biometric data) and PART 19 (Global Market Cues & Gap Trading to TRA: the
structural overnight-information-gap explanation for why Indian markets always open with global
cues baked in, the standard pre-market checklist incl. SGX/GIFT Nifty, gap types — common/
breakaway/exhaustion — and a full worked pre-market-view synthesis example). Market Research
51->53pg, TRA 37->39pg. Master: 3,746 -> 3,750 pages.

**2026-08-05, autonomous wake-cycle**: added worked examples to ch.03 (secondary-markets-trading
— stock-level vs index-level circuit breaker distinction, a worked institutional market-impact
cost calculation) and ch.08 (fundamental-analysis — a full worked Porter's Five Forces on Indian
organised retail, and decomposing a cyclical earnings beat before extrapolating it in a
valuation). 118 -> 120pg. Master: 3,750 -> 3,752 pages. Chapters with worked-example additions
now: 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 17, 18, 19, 20 (16 of 20). Remaining: 01, 10,
11, 16.

**2026-08-05, autonomous wake-cycle**: added worked examples to ch.10 (applied-equity-valuation —
a full worked football-field range across 4 methods, and why EV/EBITDA beats P/E for comparing
differently-levered peers) and ch.11 (research-note-and-thesis — a worked update note reacting to
an in-line-but-margin-miss quarter, and a weak-note-rewritten-to-pass-the-variant-view-test
example). 120 -> 121pg. Master: 3,752 -> 3,753 pages. Chapters with worked-example additions now:
02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20 (18 of 20). Remaining: 01, 16.

**2026-08-05, autonomous wake-cycle: EquityCapitalMarkets worked-examples pass complete**: added
the final 2 chapters — ch.01 (overview — a worked cross-country cost-of-capital comparison
showing capital-market depth's real economic effect, and a money-market/capital-market maturity-
matching example) and ch.16 (capital-raising — a full worked QIP dilution/EPS-accretion-vs-
dilution calculation, and a preferential-allotment-for-strategic-partnership example). **All 20
of 20 EquityCapitalMarkets chapters now have worked-example additions beyond their original 3**,
on top of the earlier 20/20 qa/ coverage — this subject has had two full enrichment passes.
121pg (content absorbed into whitespace this round, verified present via file-size growth
2305KB->2315KB). Master: 3,753 pages (unchanged this round).

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 23 (Financial Services &
Investment Product Research to Market Research — the most direct bridge in this handbook to a
stock-market-role background: trust/risk-perception dynamics, financial-literacy-aware survey
design, SEBI/IRDAI disclosure constraints on concept testing, investor segmentation by risk
tolerance/self-directed-vs-advised/life-stage, a worked options-feature-adoption-barrier
diagnostic, and investor-confidence tracking) and PART 20 (Sector & Thematic Index Trading to
TRA — Bank Nifty's concentration/rate-sensitivity/higher-IV character, Nifty IT's USD/INR and
US-tech-cycle sensitivity, factor/thematic indices, and a worked relative-strength sector-
rotation example). Market Research 53->55pg, TRA 39->41pg. Master: 3,753 -> 3,757 pages.

**2026-08-05, autonomous wake-cycle: 2 more charts (13 total)**: `mmm_saturation_curves.png`
(TV vs Digital diminishing-returns curves, marked at their worked-example spend levels, visually
showing why marginal ROI differs from average ROI) embedded in Market Research 20.4;
`clv_vs_churn.png` (CLV plotted against churn rate, a steep 1/churn curve marked at the 15%/20%
worked-example points) embedded in 21.4. Page count unchanged (55, absorbed into whitespace) but
content verified present (file size grew 1251KB->1402KB). Master: 3,757 pages (unchanged this
round, verified via rebuild).

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 24 (Agile & Rapid Research
Methods to Market Research: unmoderated remote testing platforms, the rapid-vs-rigorous decision
framework, continuous/always-on research, maintaining methodological discipline under speed
pressure) and PART 21 (Volatility Trading & India VIX-Based Strategies to TRA: VIX mechanics with
a worked expected-move conversion, the VIX-Nifty inverse relationship and when it decouples,
long/short-vega strategies, volatility mean-reversion, and a worked term-structure/backwardation
interpretation example). Market Research 55->57pg, TRA 41->43pg. Master: 3,757 -> 3,761 pages.

**2026-08-05, autonomous wake-cycle: integrity check + 2 more new parts**: verified the full
master PDF opens cleanly and is readable end-to-end (3,761 pages at that point) after many
consecutive rebuilds — no corruption. Then added PART 25 (Qualitative Data Analysis: From
Transcripts to Themes, to Market Research — the full coding process step by step, inductive vs
deductive coding, inter-coder reliability via Cohen's Kappa, what NVivo/Atlas.ti actually does)
and PART 22 (Reading Daily FII/DII and Exchange Data Publications, to TRA — provisional vs final
FII/DII figures and their limitations, FII derivatives positioning as a distinct signal from cash
flows, NSE Bhavcopy and delivery-percentage as an underused signal, and a worked multi-source
daily-data-synthesis example). Market Research 57->59pg, TRA 43->45pg. Master: 3,761 -> 3,765
pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 26 (Sampling Weighting &
Post-Stratification to Market Research — a worked single-variable weighting calculation,
multi-variable RIM/raking weighting, post-stratification vs simple weighting, and design-effect/
unmeasured-bias limits) and PART 23 (Options Strategy Selection by Market Regime to TRA — a
2-dimension trend×IV-level framework mapping each of the 4 regimes to the right strategy family,
with a worked range-bound+low-IV regime example arguing for a contrarian long-volatility
position). Market Research 59->61pg, TRA 45->47pg. Master: 3,765 -> 3,769 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 27 (Data Storytelling &
Executive Presentation to Market Research: structuring a live findings readout for a time-
constrained senior audience, handling real-time pushback without becoming defensive, live-
presentation-specific visualisation principles, presentation-stage tools) and PART 24
(Timeframe-Specific Trading Playbooks to TRA: distinct intraday/swing/positional playbooks —
dominant tools, risk parameters, and realistic routines for each — plus a worked example showing
the same breakout signal sized and managed completely differently across all three timeframes).
Market Research 61->63pg, TRA 47->49pg. Master: 3,769 -> 3,773 pages.

**2026-08-05, autonomous wake-cycle: filled Q&A appendix gaps**: both handbooks' Q&A appendices
had stopped covering content once new Parts kept getting added beyond them (TRA's 12 questions
only covered Parts 1-16, missing 17-24; Market Research's 20 questions only covered through
Part 15, missing 16-27). Added 7 more Q&A to TRA (covering seasonality, execution/VWAP, global
cues, sector IV differences, FII/DII data synthesis, options-by-regime, timeframe-specific
stops) and 8 more to Market Research (covering MMM marginal-vs-average ROI, CLV non-linearity,
implicit-measurement limits, financial-product regulatory constraints, the rapid-research
decision framework, inter-coder disagreement, weighting vs discarding data, live-pushback
handling). TRA 12->19 questions, Market Research 20->28 questions — now covering every Part in
both handbooks. Market Research 63->64pg, TRA 49->50pg. Master: 3,773 -> 3,775 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 28 (Market Entry & Expansion
Research to Market Research — the full 5-step entry-research structure incl. entry-mode
recommendation, a worked metro-to-Tier2/3 geographic-expansion example, and the non-geographic
category-entry/brand-extension-fit version of the same question) and PART 25 (Building and
Maintaining a Personal Watchlist & Daily Workflow to TRA — tiered watchlist structure, a full
daily workflow stitched together from earlier Parts' pre-market/intraday/EOD pieces, the trading
journal for accountability and skill improvement, and watchlist pruning discipline). Market
Research 64->66pg, TRA 50->52pg. Master: 3,775 -> 3,779 pages.

**2026-08-05, autonomous wake-cycle: frontmatter sync**: the frontmatter table had drifted badly
stale (still showing TRA at 34pg and Market Research at 51pg after many subsequent wake-cycle
passes pushed them to 52pg and 66pg) — resynced both rows and the total. Master: 3,779 -> 3,780
pages (the frontmatter itself gained a page from the longer descriptions).

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 29 (Advanced Statistical
Techniques: Structural Equation Modeling to Market Research — latent variables vs single survey
items, path models and fit indices, when SEM is worth the complexity vs when regression alone
suffices) and PART 26 (Market Breadth Indicators in Depth to TRA — advance-decline line
divergence, new-highs/new-lows as a complementary breadth measure, McClellan Oscillator/Summation
Index, and a worked triple-confirmed breadth-divergence example flagging a narrow, weakening
rally despite a fresh index high). Market Research 66->68pg, TRA 52->54pg. Master: 3,780 -> 3,784
pages.

**2026-08-05, autonomous wake-cycle: 2 more charts (15 total)**: `breadth_divergence.png`
(two-panel chart: index making a fresh high while the cumulative A-D line below fails to
confirm) embedded in TRA 26.5; `sem_path_model.png` (a real SEM path diagram — product/service
quality feeding latent Satisfaction, driving latent Loyalty and Advocacy/NPS, labelled path
coefficients) embedded in Market Research 29.3. Page counts steady (content verified via
file-size growth: TRA 1243KB->1352KB, Market Research 1548KB->1604KB). Master: 3,784 pages
(unchanged this round, verified via rebuild).

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 30 (Research Budgeting & ROI
Justification to Market Research — budget components, honest ROI-demonstration approaches incl.
decision-influence tracking and cost-avoidance framing, build-vs-buy for research capability, a
worked headcount-business-case example) and PART 27 (Commodity-Specific Technical Patterns to
TRA — gold's trending character and round-number levels, crude's sharper reversals and event-gap
risk, silver's dual character and the gold-silver ratio as a mean-reversion tool, a worked
crude-oil resistance-plus-OPEC+-calendar example). Market Research 68->70pg, TRA 54->56pg.
Master: 3,784 -> 3,788 pages.

**2026-08-05, autonomous wake-cycle: frontmatter re-sync + 2 more new parts**: resynced TRA/Market
Research frontmatter row counts and total again (34pg drift accumulates fast across cycles — worth
checking every 2-3 passes going forward). Then added PART 31 (Commercial Due Diligence & M&A-
Support Research to Market Research — the strongest direct crossover with equity/IB work in this
handbook: CDD methodology incl. customer reference calls, the compressed 2-4-week deal-clock
timeline, a worked reference-call red-flag example showing forward-looking churn risk a headline
retention metric misses, and CDD-specific deliverable format) and PART 28 (Pairs Trading &
Correlation-Based Technical Setups to TRA — pair selection with economic rationale vs coincidental
correlation, cointegration, z-score mean-reversion mechanics, why "market-neutral" still carries
pair-relationship-breakdown risk, and a full worked banking-sector pairs trade). Market Research
70->72pg, TRA 56->58pg. Master: 3,788 -> 3,792 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 32 (Sustainability & ESG
Consumer Research to Market Research — distinct from the equity-ESG investment-risk chapter
elsewhere in this compilation, this covers consumer sustainability *attitudes*: the well-
documented attitude-behaviour gap, segmenting sustainability commitment rather than treating
"the green consumer" as one segment, greenwashing perception research linking back to the BRSR
equity-ESG material, and a worked willingness-to-pay discounting example) and PART 29 (Reading
Broker/Analyst Consensus as Technical Context to TRA — consensus target price/rating distribution
as one confluence input not a standalone signal, estimate-revision momentum as a genuine event-
driven catalyst, the trap of letting bullish consensus override technical discipline, and a
worked upgrade-cluster-plus-volume-breakout confluence example). Market Research 72->74pg, TRA
58->60pg. Master: 3,792 -> 3,796 pages.

**2026-08-05, autonomous wake-cycle: frontmatter re-sync + 2 more new parts — master crosses
3,800 pages**: resynced frontmatter again, then added PART 33 (Pre-IPO & Investor Perception
Research to Market Research — a genuine capital-markets-adjacent discipline: structured investor/
analyst interviews ahead of a roadshow probing awareness, concerns, valuation expectations, and
messaging effectiveness; why this exists — the cost of discovering a messaging gap during the
compressed roadshow window itself vs weeks earlier; a worked example surfacing a segment-
relationship confusion ahead of a follow-on offering) and PART 30 (Multi-Leg Options Adjustments
& Rolling Strategies to TRA — covered-call rolling mechanics, adjusting a tested iron condor/
strangle (roll the untested side vs the tested side vs close entirely), delta-neutral systematic
adjustment, and a fully worked tested-short-strangle roll-down example with the explicit "is the
thesis still intact" branching decision). Market Research 74->76pg, TRA 60->62pg. Master: 3,796
-> 3,800 pages.

**2026-08-05, autonomous wake-cycle: integrity check + 2 more new parts**: full integrity check
across master (3,800pg at that point) and both handbooks confirmed no corruption, valid TOCs
(Market Research 196 entries, TRA 163 entries). Then added PART 34 (Influencer & Creator Economy
Research to Market Research — selection research beyond follower count incl. audience-authenticity
checks, effectiveness measurement adapted from Part 10's ad toolkit incl. brand lift studies and
MMM integration, sponsored-content disclosure research, a worked strong-engagement-weak-
conversion diagnostic example) and PART 31 (Trading Psychology: Managing Your Own Biases Live to
TRA — a distinct inward-facing angle from Part 12's market-wide behavioural finance: loss
aversion/disposition effect, revenge trading, confirmation bias in position management,
overconfidence after a winning streak, and concrete countermeasures incl. pre-committed exit
criteria, the journal's bias-detection function, and mandatory cooling-off rules). Market Research
76->78pg, TRA 62->64pg. Master: 3,800 -> 3,804 pages.

**2026-08-05, autonomous wake-cycle: frontmatter re-sync + 2 more charts (17 total)**: resynced
frontmatter again. Added `prospect_theory_value_function.png` (the real Kahneman-Tversky value
function, steeper on the loss side, quantifying "losses hurt ~2.25x more than equivalent gains
feel good") embedded in TRA 31.2 as the actual psychological mechanism behind loss aversion, not
just an abstract label; and `influencer_funnel_diagnostic.png` (this-campaign-vs-benchmark funnel
bar chart, visually showing the gap opening at the link-click stage) embedded in Market Research
34.5. Page counts steady (content verified via file-size growth). Master: 3,804 pages (unchanged
this round, verified via rebuild).

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 35 (Voice of Customer (VoC)
Programs to Market Research — continuous listening distinct from project-based studies,
transactional surveys/support-ticket mining/review mining as the three core VoC sources, closing
the loop as the defining operational requirement, a worked VoC-detects-usability-study-diagnoses
triangulation example) and PART 32 (Reading Quarterly-Results-Day Price Action to TRA —
options-implied expected move as a quantified benchmark, initial reaction vs multi-day drift as
two distinct phases connecting to PEAD, volume as the genuine-repricing-vs-overreaction signal,
a fully worked multi-signal results-gap trade decision). Market Research 78->80pg, TRA 64->66pg.
Master: 3,804 -> 3,808 pages.

**2026-08-05, autonomous wake-cycle: frontmatter re-sync + 2 more new parts**: resynced
frontmatter again, then added PART 36 (Retail Media Networks & E-commerce Advertising Research to
Market Research — closed-loop measurement's directness and its organic/incremental-confusion
trap, share of search as the ongoing tracking metric, a worked holdout-test example reconciling
platform-reported 8:1 ROAS against a true 3:1 incremental lift) and PART 33 (Reading Bulk/Block
Deal Disclosures for Technical Context to TRA — what a disclosure does and doesn't tell you,
promoter buying/selling as a distinct closely-watched sub-signal, combining block-deal data with
technical support levels, a worked institutional-block-at-support confluence example). Market
Research 80->82pg, TRA 66->68pg. Master: 3,808 -> 3,812 pages.

**2026-08-05, autonomous wake-cycle: filled Q&A appendix gaps again**: both appendices had again
fallen behind (TRA 19 questions covering through Part 24 of 33; Market Research 28 questions
covering through Part 27 of 36). Added 8 more Q&A to TRA (watchlist pruning, breadth divergence
as caution not proof, crude's event-gap risk vs gold, market-neutral vs risk-free in pairs
trading, consensus sentiment vs technical entry timing, revenge-trading avoidance, volume-based
gap-quality read, promoter-sale over-reading caution) and 8 more to Market Research (Tier-2/3
entry-research mistake, SEM overkill judgment, decision-influence vs hard ROI, CDD reference-call
vs historical-metric conflict, sustainability willingness-to-pay unreliability, investor-
perception finding-to-fix translation, influencer campaign root-cause diagnosis, VoC detection-
vs-diagnosis limits) — both appendices now cover every Part again. Market Research 82->83pg, TRA
68->69pg. Master: 3,812 -> 3,814 pages.

**2026-08-05, autonomous wake-cycle: frontmatter re-sync + 2 more new parts**: resynced
frontmatter, then added PART 37 (Mobile App UX Research & In-App Analytics to Market Research —
directly relevant given broking/trading apps are a huge category for this compilation's target
roles: in-app micro-surveys, app-store review mining for competitive benchmarking and version-
regression detection, mobile-specific usability considerations incl. own-device testing, a worked
Android-vs-iOS KYC-upload activation-drop diagnostic) and PART 34 (Reading Corporate Announcements
for Technical Setups to TRA — buyback announcements as a mechanical floor-support mechanism,
board-meeting intimations as known-dated-catalyst windows, the bonus/rights unadjusted-chart-data
trap, a worked example distinguishing a genuine breakdown from an unadjusted-bonus-issue
artifact). Market Research 83->85pg, TRA 69->71pg. Master: 3,814 -> 3,818 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 38 (Survey Programming & Data
Quality in Practice to Market Research — skip-logic/routing implementation risk and full-path
testing, soft-launch as the last quality gate before full field, in-line data-quality checks built
into the programming itself, a worked tracking-study Wave-4 programming-error-vs-genuine-shift
diagnostic) and PART 35 (ETF & Index Fund Flow Data as a Sentiment Input to TRA — creation/
redemption mechanics as a passive-flow proxy distinct from FII/DII cash flows, why ETF flows
matter disproportionately for index-heavyweight stocks, a worked 3-source flow-data synthesis
example combining FII/DII/ETF data). Market Research 85->87pg, TRA 71->72pg. Master: 3,818 ->
3,821 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 39 (Geospatial &
Location-Based Research to Market Research — trade-area analysis and gravity-model catchment
sizing, site-selection research combining trade-area demand with competitive density and footfall/
mobility data, cannibalisation analysis as the geospatial version of the incrementality discipline
already applied to retail media (Part 36) and assortment (Part 19), a worked new-bank-branch
cannibalisation-vs-standalone-trade-area example) and PART 36 (Cross-Market Arbitrage & ADR-NSE
Price Linkages to TRA — why an ADR premium/discount is a genuine stock-specific pre-market signal,
computing the ratio-adjusted ADR-implied move, the arbitrage mechanism that keeps the linkage
tight vs cases where it loosens, distinguishing a stock-specific ADR signal from a market-wide
global-cues echo, a worked IT-services-ADR-ahead-of-the-open example). Added matching glossary
terms and one new Q&A each (Market Research Q37, TRA Q28) tied to the new Parts. Market Research
87->90pg, TRA 72->75pg. Master: 3,821 -> 3,827 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 40 (Retail Investor &
Trading-App Research to Market Research — why retail-broking research is a distinct sub-
discipline vs generic fintech UX, KYC/activation-funnel research distinguishing UX-caused vs
regulatory-inherent drop-off, trading-frequency behavioural segmentation, trust-signal and risk-
perception-calibration research specific to real-money apps, a worked 30-day F&O-churn diagnostic
separating UX/risk-comprehension/natural-segment hypotheses) and PART 37 (Options Open Interest
(OI) Data as a Technical Signal to TRA — OI as a third data layer beyond price/volume, the four-
quadrant long-buildup/short-buildup/short-covering/long-unwinding read, Max Pain and PCR as
sentiment-adjacent OI derivatives, strike-level OI concentration as dynamic support/resistance, a
worked Nifty weekly-expiry OI-and-PCR synthesis example). Added matching glossary terms (Market
Research) and one new Q&A each (Market Research Q38, TRA Q29). Market Research 90->92pg, TRA
75->77pg. Master: 3,827 -> 3,831 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 41 (Financial Literacy &
Investor Education Research to Market Research — distinct from Part 40's in-product risk-
perception work, covers standardised financial-literacy assessment instruments, pre/post
comprehension-gain evaluation design for education content vs satisfaction-only measurement, and
the harder behavioural-follow-through question of whether education actually changes downstream
trading behaviour, a worked mandatory-pre-F&O-module evaluation example) and PART 38 (Relative
Strength Ranking Across the Stock Universe to TRA — distinct from Part 20.5's two-index ratio
chart, covers universe-wide percentile RS ranking, why percentile rank strips out market-regime
confounds that raw trailing return doesn't, the RS-rank-plus-base-pattern screening use case, the
regime-dependency limitation, a worked RS-ranked breakout-candidate validation example). Added
matching glossary terms (Market Research) and one new Q&A each (Market Research Q39, TRA Q30).
Market Research 92->94pg, TRA 77->79pg. Master: 3,831 -> 3,835 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 39 (Volume Profile & Market
Profile (TPO) Analysis to TRA — reframes the chart around price rather than time, Point of
Control/Value Area as a volume-derived S/R framework distinct from chart-based S/R, high-volume
vs low-volume nodes, Market Profile/TPO and Initial Balance as the older time-weighted cousin, a
worked open-outside-prior-Value-Area example) and PART 42 (Robo-Advisory & Algorithmic
Recommendation Research to Market Research — distinct from Part 40's app-trust and Part 41's
literacy research, covers risk-profiling-questionnaire validation as a measurement-quality
problem, explainability research as progressive disclosure applied to algorithmic recommendations,
override/disagreement analysis as a diagnostic data source, a worked drawdown-triggered-override-
spike diagnostic tying back to the stated-vs-revealed-preference theme). Added matching glossary
terms (Market Research) and one new Q&A each (Market Research Q40, TRA Q31). Market Research
94->96pg, TRA 79->81pg. Master: 3,835 -> 3,839 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 40 (Elliott Wave Theory,
Deepened to TRA — deepens Part 4.2's 4-bullet summary into the three inviolable rules vs
guidelines distinction, Fibonacci confluence as the actual actionable output of a wave count, a
worked 5-wave-count validation + Wave 4 target-zone example) and PART 43 (Alternative Data as a
Market Research Input to Market Research — satellite/app-download/web-traffic signals as a
distinct evidence layer, speed/frequency as the core value proposition vs slower primary research,
ground-truthing discipline before trusting a new alternative-data source, alternative data as a
trigger for targeted primary follow-up rather than a standalone finding, a worked app-download-
surge diagnostic). Added matching glossary terms (Market Research) and one new Q&A each (Market
Research Q41, TRA Q32). Market Research 96->98pg, TRA 81->83pg. Master: 3,839 -> 3,843 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 41 (Harmonic Patterns to TRA
— precise Fibonacci-ratio X-A-B-C-D structures distinct from Part 2's visual-shape chart patterns,
the four classic Gartley/Bat/Butterfly/Crab templates, the Potential Reversal Zone, confluence
with volume-profile/swing-level evidence, a worked Bat-pattern-plus-VAH-confluence example) and
PART 44 (Advisor/Distribution-Channel Research to Market Research — researching the IFA/MFD/RM
intermediary as a distinct subject from the end investor, advisor satisfaction/needs research, RM
productivity research, the double-blind-spot risk of researching only one side of the channel, a
worked advisor-positive-vs-end-investor-risk-misunderstanding reconciliation example). Added
matching glossary terms (Market Research) and one new Q&A each (Market Research Q42, TRA Q33).
Market Research 98->100pg (milestone: crossed 100pg), TRA 83->85pg. Master: 3,843 -> 3,847 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 42 (Point & Figure Charting,
Deepened to TRA — deepens Part 3's one-line mention into a third organising principle beyond time
(Part 1-38) and price-by-volume (Part 39), box size/reversal-amount parameters, Double/Triple
Top-Bottom patterns, the horizontal-count target-projection method, a worked Triple-Top-breakout
target example) and PART 45 (IPO Grey-Market & Pre-Listing Investor Sentiment Research to Market
Research — distinct from Part 23's pre-IPO messaging testing, category-wise RII/NII/QIB
subscription-data segmentation, grey-market premium's real but limited evidentiary value, the
listing-day-pop validation/ground-truthing exercise, a worked divergent-subscription-vs-GMP
reconciliation example). Added matching glossary terms (Market Research) and one new Q&A each
(Market Research Q43, TRA Q34). Market Research 100->104pg, TRA 85->88pg. Master: 3,847 -> 3,854
pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 43 (Reading the Order Book:
Bid-Ask Imbalance & Order Flow Footprint Charts to TRA — a fourth, forward-looking data layer
beyond historical-trade-based techniques, bid-ask imbalance and its fast-decaying/spoofing caveat
extending Part 18.3's iceberg-order discussion, footprint charts extending Part 39's volume
profile down to single-candle granularity, a worked breakout-candle footprint-validation example)
and PART 46 (Support & Service Experience Research for Broking & Wealth Platforms to Market
Research — distinct from Part 40's onboarding/trust research, Customer Effort Score vs NPS, First
Contact Resolution as the diagnostic layer beneath CES, complaint-handling research under
financial-services regulatory scrutiny, a worked NPS/CES-divergence trade-dispute diagnostic).
Added matching glossary terms (Market Research) and one new Q&A each (Market Research Q44, TRA
Q35). Market Research 104->106pg, TRA 88->90pg. Master: 3,854 -> 3,858 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 44 (Ichimoku Kinko Hyo,
Deepened to TRA — deepens Part 3.1's one-line mention into the full five-line system: Tenkan-sen,
Kijun-sen, both Senkou Spans forming the cloud, Chikou Span; cloud thickness/colour reads, the
Tenkan/Kijun cross weighted by cloud position, a worked full-alignment synthesis example) and PART
47 (Employee-Review Mining to Market Research — Glassdoor-style review data as an equity-research-
adjacent signal distinct from Part 43's satellite/app-download alt-data, the review-platform self-
selection-bias limitation, trend-over-snapshot and sector-relative comparison as the defensible use
case, text-mining themes beyond the star rating, a worked pre-launch employee-sentiment-decline
diagnostic). Added matching glossary terms (Market Research) and one new Q&A each (Market Research
Q45, TRA Q36). Market Research 106->108pg, TRA 90->92pg. Master: 3,858 -> 3,862 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 45 (Volatility Skew to TRA —
distinct from Part 21.5's term structure, the negative-skew baseline shape for equity indices,
skew steepness as a direction-specific fear gauge distinct from VIX's level, skew behaviour around
events and post-event normalisation, a worked RBI-decision put-skew-widening example) and PART 48
(Regulatory & Policy-Change Impact Perception Research to Market Research — a rule change rather
than a product/market event as the research trigger, stakeholder-impact mapping across differently-
affected groups, formal consultation/comment-period research feeding regulatory submissions, post-
implementation impact tracking, a worked SEBI margin-requirement-increase impact-research example).
Added matching glossary terms (Market Research) and one new Q&A each (Market Research Q46, TRA
Q37). Market Research 108->110pg, TRA 92->94pg. Master: 3,862 -> 3,866 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 46 (Anchored VWAP to TRA —
distinct from Part 18.2's execution-benchmark framing of VWAP, session VWAP as an intraday
directional-bias reference, AVWAP generalising the calculation to any significant anchor date, why
AVWAP from a major low carries genuine behavioural support weight from actual holders' cost basis,
a worked post-results-low AVWAP retest example) and PART 49 (GIFT City, Cross-Border & NRI Investor
Research to Market Research — a regulation/geography-defined segment distinct from wealth-tier
segmentation, geography-specific NRI sub-segmentation across Gulf/US-UK-Canada/other, GIFT City's
dollar-denominated product context, the relationship-triggered rather than self-directed customer
journey, a worked NRI-product research-scoping example). Added matching glossary terms (Market
Research) and one new Q&A each (Market Research Q47, TRA Q38). Market Research 110->112pg, TRA
94->96pg. Master: 3,866 -> 3,870 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 47 (Auction Market Theory to
TRA — the theoretical "why" underneath Part 39's volume-profile mechanics: balance vs imbalance
states and their distinct profile shapes, excess/single-print tails as a structural rejection
signal distinct from a candlestick reversal, a worked live day-typing example transitioning from
balance to imbalance tactics) and PART 50 (Disclosure Comprehension & Readability Testing to
Market Research — distinct from Part 41's broad financial-literacy research, readability metrics
as a necessary-not-sufficient screen, genuine comprehension testing vs self-reported understanding,
plain-language rewriting with iterative re-testing, a worked margin-call-disclosure comprehension-
failure-and-fix example). Added matching glossary terms (Market Research) and one new Q&A each
(Market Research Q48, TRA Q39). Market Research 112->115pg, TRA 96->99pg. Master: 3,870 -> 3,876
pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 48 (Credit Spreads as an
Equity-Stress Leading Indicator to TRA — distinct from Part 15.2's bond-yield-level material,
why credit markets often lead equity weakness, high-yield spreads as the most sensitive segment,
the Indian-market translation via NBFC/credit-sensitive-stock underperformance, a worked flat-
index-but-underperforming-NBFCs early-warning example) and PART 51 (Referral & Word-of-Mouth
Growth Research to Market Research — distinct from Part 18's CLV/retention and Part 40's onboarding
research, NPS as an imperfect proxy for actual referral behaviour, referral-incentive research
distinguishing expansion from substitution, trigger-moment mapping for referral-ask placement, a
worked high-NPS-but-weak-referral-quality diagnostic). Added matching glossary terms (Market
Research) and one new Q&A each (Market Research Q49, TRA Q40). Market Research 115->117pg, TRA
99->101pg. Master: 3,876 -> 3,880 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 49 (Promoter Share Pledging as
a Technical Red-Flag Signal to TRA — distinct from Part 33.3's ordinary promoter-sale reading, LTV-
threshold invocation mechanics creating price-triggered forced-selling risk, absolute-level vs
trend reading of pledge percentage, why high pledge creates a structural technical "ceiling," a
worked rising-pledge-trend-plus-weakening-chart example) and PART 52 (Experimentation Methodology
to Market Research — beyond simple A/B testing: peeking and sequential testing, multi-armed
bandits as a distinct optimise-during-test paradigm vs fixed-allocation testing, guardrail metrics
protecting against a "winning" test that damages something else, a worked bandit-based onboarding-
experiment guardrail-timing example). Added matching glossary terms (Market Research) and one new
Q&A each (Market Research Q50, TRA Q41). Market Research 117->119pg, TRA 101->103pg. Master:
3,880 -> 3,884 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 50 (Circuit Filters, Trading
Halts & Market-Wide Circuit Breakers to TRA — a hard, exchange-imposed price constraint distinct
from any chart-based level, individual-stock filter bands and locked-circuit exit risk, market-
wide circuit breakers as a distinct index-level halt mechanism, self-reinforcing filter-approach
urgency dynamics, a worked small-cap-nearing-circuit exit-risk example) and PART 53 (Brokerage-Fee
& Pricing-Model Perception Research to Market Research — the zero-brokerage category norm reshaping
what pricing research even means here, fee-structure comprehension research distinct from Part 50's
disclosure comprehension testing, cross-platform fee comparison research, perceived fee fairness as
distinct from fee level, a worked rising-F&O-support-contacts-despite-full-disclosure diagnostic).
Added matching glossary terms (Market Research) and one new Q&A each (Market Research Q51, TRA
Q42). Market Research 119->121pg, TRA 103->105pg. Master: 3,884 -> 3,888 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 51 (Securities Lending Data &
Short-Squeeze Setups to TRA — SLBM short-interest data as a distinct positioning source from
options OI, absolute-level-plus-trend reading mirroring Part 49's pledge-data discipline, the
short-squeeze forced-covering mechanism, days-to-cover as the more complete squeeze-potential gauge
than short-interest level alone, a worked pre-results elevated-days-to-cover example) and PART 54
(Investor Relations Effectiveness Perception Research to Market Research — the IR function itself
as a distinct research object from Part 32/45's investor-perception-of-the-story material, analyst/
institutional respondent population and access considerations, benchmarkable IR dimensions
(earnings-call quality, disclosure timeliness, management accessibility, messaging consistency),
the hard-to-isolate but real valuation-adjacent consequence, a worked declining-analyst-coverage
diagnostic). Added matching glossary terms (Market Research) and one new Q&A each (Market Research
Q52, TRA Q43). Market Research 121->123pg, TRA 105->107pg. Master: 3,888 -> 3,892 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 52 (Mutual Fund Portfolio
Disclosures to TRA — a stock-specific positioning signal distinct from Part 22's aggregate DII
flow data, reading scheme-level buying/selling, new-entry/complete-exit as the highest-signal
disclosure category, the reporting-lag caveat distinguishing this from live intraday data, a
worked new-entry-from-a-well-regarded-fund example) and PART 55 (Finfluencer Marketing Research to
Market Research — distinct from Part 34's generic influencer-effectiveness material, disclosure-
compliance research as a higher-stakes version of transparency testing, credibility/expertise-
perception research beyond engagement metrics, ongoing content-accuracy audits as a distinct
compliance-adjacent function, a worked strong-metrics-vs-compliance-flag reconciliation example).
Added matching glossary terms (Market Research) and one new Q&A each (Market Research Q53, TRA
Q44). Market Research 123->126pg, TRA 107->110pg. Master: 3,892 -> 3,898 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 53 (Index Reconstitution &
Rebalancing Flow Effects to TRA — a scheduled, mechanically-predictable event distinct from Part
35's ongoing ETF-flow dynamics, forced price-insensitive index-fund buying/selling on inclusion/
exclusion, the "buy the rumour, sell the news" anticipatory-rally-then-fade pattern, effective-date
closing-auction volume vs price-move distinction, a worked pre-announcement-rally entry-risk
example) and PART 56 (Gamification Research to Market Research — the dual-use-design tension unique
to trading apps, engagement-metric research vs a distinct behaviour-quality measurement layer,
regulatory attention as a research-scoping input rather than a compliance afterthought, segment-
specific vulnerability research prioritising new/inexperienced traders, a worked trading-streak-
pilot segmented-harm diagnostic). Added matching glossary terms (Market Research) and one new Q&A
each (Market Research Q54, TRA Q45). Market Research 126->128pg, TRA 110->112pg. Master: 3,898 ->
3,902 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 54 (Promoter/Insider Buying,
Deepened to TRA — deepens Part 33.3's brief mention into the SAST regulatory framework: trading
window closures explaining transaction timing, structured trading plans vs discretionary open-
market purchases as a signal-strength distinction, disclosure thresholds and cumulative-tracking
discipline, a worked post-results discretionary-purchase timing-vs-structure example) and PART 57
(Hiring-Signal & Job-Posting Analysis, Deepened to Market Research — deepens Part 3's one-line CI
checklist item into a systematic methodology: volume-trend limitations distinguishing expansion
from replacement hiring, functional/seniority posting mix as the more diagnostic layer, LinkedIn
headcount-by-function as a confirming lagging signal, a worked market-entry hiring-pattern
diagnostic). Added matching glossary terms (Market Research) and one new Q&A each (Market Research
Q55, TRA Q46). Market Research 128->130pg, TRA 112->114pg. Master: 3,902 -> 3,906 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 55 (USD/INR as a Standalone
Technical Market to TRA — from a macro-input role (Part 15.2) to a directly tradeable currency-
derivatives chart, round-number psychology, RBI intervention zones creating a distinct policy-
driven ceiling/floor dynamic, offshore NDF market cues as an ADR-style overnight signal, a worked
contained-depreciation-pace-near-a-round-number example) and PART 58 (Cohort Analysis & Retention-
Curve Methodology to Market Research — distinct from Part 21's single-number CLV output, the cohort
table's row/column/diagonal reading, retention-curve flattening as more diagnostic than any single
month's number, cohort-vs-cohort comparison as a rigorous non-experimental evaluation method, a
worked onboarding-redesign Month-1-vs-Month-4 divergence example). Added matching glossary terms
(Market Research) and one new Q&A each (Market Research Q56, TRA Q47). Market Research 130->132pg,
TRA 114->116pg. Master: 3,906 -> 3,910 pages.

**Running total: 3,910 pages.**
