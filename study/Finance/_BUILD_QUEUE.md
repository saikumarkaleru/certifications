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

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 56 (ASM/GSM Surveillance
Framework to TRA — a preventive, pattern-triggered restriction distinct from Part 50's reactive
circuit filters, margin/call-auction restrictions structurally altering a stock's tradeable
character, stage-trajectory tracking as a regulator-validated risk-trend signal, the classification
announcement itself as a distinct market-moving event, a worked GSM-Stage-2 technical-inapplicability
example) and PART 59 (Post-Purchase Dissonance & Investment-Regret Research to Market Research —
distinct from pre-decision behavioural/comprehension research, why financial decisions are a high-
dissonance-risk category, dissonance-reduction behaviours as an observable proxy, regret-timing
window analysis as the most actionable application, a worked early-30-day exit-request-spike
diagnostic). Added matching glossary terms (Market Research) and one new Q&A each (Market Research
Q57, TRA Q48). Market Research 132->134pg, TRA 116->118pg. Master: 3,910 -> 3,914 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 57 (Reading the Futures Basis
to TRA — a continuously-live signal beyond Part 22.3's end-of-day FII positioning data, the
arbitrage-enforced fair-value range explaining why the basis self-corrects, basis expansion/
contraction as a sentiment gauge within that range, rollover-period distortion and rollover cost as
a related signal, a worked wide-premium-ahead-of-a-catalyst example) and PART 60 (Recommendation
Engine & Content-Personalization Testing to Market Research — distinct from Part 42's portfolio-
allocation robo-advisory research, click-through as an incomplete relevance metric, filter-bubble/
diversity research specific to financial-content stakes, cold-start research for new users, a
worked engagement-vs-quality-tradeoff algorithm-update diagnostic). Added matching glossary terms
(Market Research) and one new Q&A each (Market Research Q58, TRA Q49). Market Research 134->137pg,
TRA 118->121pg. Master: 3,914 -> 3,920 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 58 (Backtesting Pitfalls,
Deepened to TRA — deepens Part 10.2's one-line overfitting warning into why parameter count
mechanically drives overfitting risk, the essential in-sample/out-of-sample split, walk-forward
analysis as a repeated rolling-window test more rigorous than a single static split, a worked
7-parameter-strategy-tuned-on-the-same-dataset red-flag example) and PART 61 (Longitudinal Panel
Design for Tracking Sentiment Across Market Cycles to Market Research — a distinct panel-mechanics
layer beneath Part 10.4's tracker-consistency discipline and Part 23.5's investor-confidence-index
application, panel attrition bias correlating with the very outcome being tracked, panel
conditioning from repeated exposure, refreshment sampling as the standard defence, a worked
suspiciously-resilient-confidence-tracker-through-a-downturn diagnostic). Added matching glossary
terms (Market Research) and one new Q&A each (Market Research Q59, TRA Q50). Market Research
137->139pg, TRA 121->123pg. Master: 3,920 -> 3,924 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 59 (REITs & InvITs: A Distinct
Yield-Sensitive Technical Profile to TRA — bond-proxy behaviour distinct from ordinary equity,
interest-rate sensitivity as the dominant technical driver, mechanical ex-distribution price
adjustment as a non-informational move to distinguish from genuine weakness, lower beta/volatility
calibration, a worked ex-distribution-vs-rate-surprise two-move-differentiation example) and PART
62 (Contact-Center Speech Analytics Research to Market Research — distinct from Part 46's survey-
based CES/NPS, sentiment-trajectory/talk-time/keyword extraction beyond a single score, 100%-call-
coverage advantage over survey sampling with its own classification-error caution, compliance-risk
call flagging as a financial-services-specific use case, a worked stable-CSAT-but-escalating-
margin-call-sentiment diagnostic). Added matching glossary terms (Market Research) and one new Q&A
each (Market Research Q60, TRA Q51). Market Research 139->141pg, TRA 123->125pg. Master: 3,924 ->
3,928 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 60 (Physical Settlement &
Expiry-Week Options Mechanics to TRA — the structural shift from cash to physical settlement for
Indian stock options, why writers actively unwind near-the-money ITM positions into expiry, elevated
volume/volatility concentrated at near-the-money strikes, Max Pain's stakes revisited under physical
settlement, a worked choppy-expiry-day-price-action example) and PART 63 (Management-Tone Textual
Analysis Research to Market Research — distinct from Part 54's IR-perception surveys, hedging-
language/uncertainty-marker coding as a systematic linguistic signal, comparative/longitudinal
tracking over single-snapshot reads, the critical ground-truthing limitation before trusting a
linguistic shift as predictive, a worked rising-hedging-trend-vs-historical-outcomes validation
example). Added matching glossary terms (Market Research) and one new Q&A each (Market Research
Q61, TRA Q52). Market Research 141->143pg, TRA 125->127pg. Master: 3,928 -> 3,932 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 61 (Dealer Gamma Positioning
to TRA — a market-structure-level volatility driver distinct from Part 30.4's single-position
delta-neutral management, why net-short vs net-long dealer gamma dampens vs amplifies moves,
estimating the regime from aggregate OI/GEX proxies, why this matters most at major gamma-
concentration levels tying to Part 37.4/Part 60, a worked pinned-range-into-expiry example) and
PART 64 (MaxDiff Methodology, Deepened to Market Research — from a glossary term to an actual
best-worst-choice methodology, why simple rating scales cluster and fail to discriminate,
interval-level utility scores as a more actionable output than ordinal ranking, sample-size/item-
count design practicalities, a worked 15-feature-prioritization example fixing an "everything is
important" rating-scale failure). Added matching glossary terms (Market Research) and one new Q&A
each (Market Research Q62, TRA Q53). Market Research 143->145pg, TRA 127->129pg. Master: 3,932 ->
3,936 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 62 (IBC/Insolvency Events to
TRA — a distinct, later-stage legal event category beyond credit spreads/promoter pledging, the
moratorium's implication that ordinary technical analysis becomes largely meaningless, resolution-
plan-vs-liquidation as starkly different technical endpoints, trading-suspension/re-listing
considerations distinct from ASM/GSM, a worked pledge-and-spreads-history-into-IBC-admission
example) and PART 65 (Usability Testing Methodology for Complex Financial Workflows to Market
Research — the think-aloud protocol's diagnostic value beyond click observation, moderated-vs-
unmoderated tradeoffs for high-stakes flows, precise task-success metrics, error-consequence-
severity as the essential financial-category addition, a worked options-order-screen near-miss
example). Added matching glossary terms (Market Research) and one new Q&A each (Market Research
Q63, TRA Q54). Market Research 145->148pg, TRA 129->132pg. Master: 3,936 -> 3,942 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 63 (QIP & Preferential
Allotment to TRA — a dilutive capital-raise mechanism distinct from IPOs (Part 45) and buybacks
(Part 34.2), the regulator-defined QIP floor-price formula as a calculable reference level,
discount-to-floor reading and post-placement supply overhang, preferential-allotment lock-in as a
calendar-datable future overhang, a worked steep-discount-QIP overhang example) and PART 66
(Research Vendor Evaluation & Panel-Provider Selection to Market Research — deepens Part 12.1's RFP
basics into full evaluation methodology, panel-quality criteria beyond raw size, pilot-study
evaluation before full commitment, category-specific reference checks, a worked two-vendor-
comparison example). Added matching glossary terms (Market Research) and one new Q&A each (Market
Research Q64, TRA Q55). Market Research 148->150pg (milestone: crossed 150pg), TRA 132->134pg.
Master: 3,942 -> 3,946 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 64 (The Zero-Days-to-Expiry
(0DTE) Trading Phenomenon to TRA — a distinct microstructure regime from ordinary options analysis
elsewhere in this handbook, extreme theta decay/gamma explosion in an option's final hours, dealer-
gamma hedging flows (Part 61) compressed into hours rather than days, why 0DTE volume has changed
the character of expiry-day index price action generally, a worked catalyst-free late-session
reversal-and-partial-reversal example) and PART 67 (Syndicated Research Licensing & Multi-Client
Study Economics to Market Research — the distinct commissioning model from custom research covered
throughout this handbook, cost-sharing economics, the no-questionnaire-control limitation, add-on/
omnibus modules as a middle path, a worked syndicated-vs-custom-study decision example). Added
matching glossary terms (Market Research) and one new Q&A each (Market Research Q65, TRA Q56).
Market Research 150->152pg, TRA 134->136pg. Master: 3,946 -> 3,950 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 65 (Corporate Governance Red
Flags as Technical Catalysts to TRA — distinct from promoter pledging/insider signals/IBC events
elsewhere, mid-term auditor resignations as among the sharpest single-day catalysts, why the stated
reason must be read before calibrating severity, related-party-transaction pattern changes as a
more gradual trend-based signal, a worked RPT-linked-resignation-plus-circuit-lock example) and
PART 68 (Accessibility Research for Financial Platforms to Market Research — a distinct research
population/methodology from mainstream usability testing (Part 65), elevated financial-stakes
profile for accessibility failures, screen-reader compatibility testing surfacing invisible
failures, assistive-technology participant recruitment considerations, a worked colour-only-gain/
loss-indicator screen-reader failure example). Added matching glossary terms (Market Research) and
one new Q&A each (Market Research Q66, TRA Q57). Market Research 152->154pg, TRA 136->138pg.
Master: 3,950 -> 3,954 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 66 (Quarterly Shareholding
Pattern Disclosures to TRA — a distinct company-level aggregate disclosure from Part 52's scheme-
level MF data, quarter-over-quarter category-shift reading, distinguishing genuine net buying from
mechanical dilution/buyback base effects, number-of-shareholders data as a complementary
granularity layer, a worked FII-up/public-down-checked-against-corporate-actions example) and PART
69 (Customer Advisory Boards, Deepened to Market Research — deepens a one-line glossary mention
into full operating structure, CAB members' inherent non-representativeness, the relationship-
management-vs-research-objectivity tension, rotation/triangulation/explicit-critical-solicitation
as mitigations, a worked CAB-satisfaction-vs-representative-survey-dissatisfaction reconciliation
example). Added matching glossary terms (Market Research) and one new Q&A each (Market Research
Q67, TRA Q58). Market Research 154->156pg, TRA 138->140pg. Master: 3,954 -> 3,958 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 67 (Credit Rating Actions to
TRA — a discrete-event catalyst distinct from Part 48's continuous credit-spread signal and Part
29's equity-analyst-consensus material, why an investment-grade-to-sub-investment-grade downgrade
triggers mandate-driven forced institutional selling, rating-watch/outlook changes as an earlier
softer signal, multi-agency divergence as its own informative signal, a worked fallen-angel-
downgrade-after-negative-watch example) and PART 70 (Automated Price/Fee Monitoring via Web
Scraping to Market Research — a distinct data-collection infrastructure from Part 53's pricing-
research methodology, what continuous automated monitoring catches that periodic manual checks
miss, scraping-specific data-quality risks distinct from survey quality checks, legal/ethical
scraping boundaries, a worked brief-undisclosed-promotional-pricing-change diagnostic). Added
matching glossary terms (Market Research) and one new Q&A each (Market Research Q68, TRA Q59).
Market Research 156->159pg, TRA 140->143pg. Master: 3,958 -> 3,964 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 68 (The Pre-Open Session:
Order Collection & the IEP Mechanism to TRA — a distinct micro-session with its own three-sub-phase
price-discovery mechanism, watching the Indicative Equilibrium Price's own trajectory as a first
genuinely NSE-order-book-derived daily signal distinct from overnight GIFT Nifty cues (Part 19), why
the actual opening print can diverge from the final IEP, a worked rising-IEP-ahead-of-anticipated-
results example) and PART 71 (Diary Studies & Experience Sampling Method to Market Research —
deepens Part 4.4's brief mention, the diary-study-vs-ESM trigger-control design choice, compliance/
fatigue management as the central practical challenge, the specific fit for capturing financial
decisions before post-hoc rationalisation sets in, a worked impulsive-trading-behaviour ESM-design
example). Added matching glossary terms (Market Research) and one new Q&A each (Market Research
Q69, TRA Q60). Market Research 159->161pg, TRA 143->145pg. Master: 3,964 -> 3,968 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 69 (EPFO/NPS Structural Equity
Flows to TRA — a rules-driven, policy-mandated flow category distinct from Part 22's discretionary
DII buying, slow-moving and largely price-insensitive by construction, concentrated in index-
heavyweight names alongside ETF/reconstitution flows (Part 35.3/53), explicitly framed as
background structural context rather than a timing tool, a worked index-heavyweight relative-
resilience-during-a-correction example) and PART 72 (Video/Audio Disclaimer Effectiveness Research
to Market Research — distinct from Part 50's static-text comprehension research, speech-rate and
audio-visual-competition as format-specific comprehension risks, single-exposure comprehension
testing methodology, on-screen text supplementation requiring its own empirical validation, a
worked fast-disclaimer-plus-ineffective-on-screen-text diagnostic). Added matching glossary terms
(Market Research) and one new Q&A each (Market Research Q70, TRA Q61). Market Research 161->163pg,
TRA 145->147pg. Master: 3,968 -> 3,972 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 70 (Trade-for-Trade (T2T)
Segment to TRA — a distinct compulsory-delivery mechanism from Part 56's ASM/GSM margin-based
surveillance, mechanical elimination of the entire intraday technical character, thinner-liquidity
implications, distinguishing surveillance-triggered vs routine-new-listing T2T contexts, a worked
surveillance-flagged-T2T-stock intraday-strategy-inapplicability example) and PART 73 (Internal
Employee Pulse Surveys to Market Research — distinct from Part 47's external Glassdoor-style review
mining, frontline customer-facing sentiment as a genuine CX leading indicator, role/function
segmentation beneath an aggregate engagement score, the psychological-safety trust precondition for
credible responses, a worked pre-external-metric KYC-friction pulse-survey example). Added matching
glossary terms (Market Research) and one new Q&A each (Market Research Q71, TRA Q62). Market
Research 163->165pg, TRA 147->149pg. Master: 3,972 -> 3,976 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 71 (IPO Listing-Day Price
Discovery to TRA — a distinct, no-prior-close pre-open mechanism beyond Part 68's standard framework,
the issue-price-anchored listing-day price band, reading the listing-day IEP as a real-money test of
Part 45's GMP/subscription signals, distinct early-session volatility character for newly-listed
names, a worked GMP-vs-actual-listing-day-IEP gap example) and PART 74 (Win-Loss Analysis, Deepened
to Market Research — deepens a glossary term into a structured B2B interview protocol, independent-
interviewer as the single most consequential design choice, comparative win/loss sampling versus
loss-only post-mortems, timing/specificity-probing question design, a worked salesperson-conducted-
loss-only-vs-independent-comparative diagnostic showing "it's about price" was never differentiating).
Added matching glossary terms (Market Research) and one new Q&A each (Market Research Q72, TRA Q63).
Market Research 165->167pg, TRA 149->151pg. Master: 3,976 -> 3,980 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 72 (Non-Disposal Undertakings
to TRA — a less-visible promoter-encumbrance mechanism distinct from Part 49's formal pledge
framework, why an NDU creates a real "float isn't what it appears" constraint despite no formal
invocation mechanism, disclosure-variability caution requiring checking credit-rating-agency reports
and news flow beyond the standard pledge disclosure, NDU expiry as a datable future overhang event,
a worked clean-pledge-disclosure-vs-NDU-reference reconciliation example) and PART 75 (Semiotic
Analysis for Financial Brand Marks to Market Research — a distinct expert-analytical technique from
consumer-facing testing, category-relevant cultural weight of financial-brand symbolism in the
Indian market, the conformity-vs-departure-from-category-convention framework, why expert semiotic
interpretation needs empirical consumer validation, a worked unconventional-rebrand-colour-palette
diagnostic). Added matching glossary terms (Market Research) and one new Q&A each (Market Research
Q73, TRA Q64). Market Research 167->170pg, TRA 151->154pg. Master: 3,980 -> 3,986 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 73 (Promoter Group Inter-Se
Transfers to TRA — a distinct, often-overlooked disclosure category from Part 33.3/54's open-market
promoter transactions, why inter-se transfers are frequently misread as genuine buy/sell signals,
succession-planning/restructuring value when a pattern is genuine, distinguishing routine
reshuffling from meaningful pattern/scale, a worked promoter-to-family-trust-transfer-misread-as-
bearish example) and PART 76 (Retail Audit Panel Methodology to Market Research — deepens Part 17's
syndicated-vendor glossary mention, store-universe stratification by type/geography, sample-to-
total-market extrapolation, e-commerce/quick-commerce channel-coverage gaps, a worked retail-audit-
vs-company-reported-sales-discrepancy diagnostic). Added matching glossary terms (Market Research)
and one new Q&A each (Market Research Q74, TRA Q65). Market Research 170->172pg, TRA 154->156pg.
Master: 3,986 -> 3,990 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 74 (Muhurat Trading &
Samvat-Year Performance, Deepened to TRA — deepens Part 17's one-line cultural note into actual
session mechanics and the honest, calibrated statistical read distinguishing a real-but-modest
session-level tendency from the weaker year-ahead predictive claim popular commentary sometimes
implies, a worked client-question-response example) and PART 77 (Sample Ratio Mismatch to Market
Research — a foundational data-quality gate beneath Part 52's experimentation methodology, why SRM
invalidates any metric difference regardless of statistical significance, the chi-square check as a
near-automatic first-line gate, common root causes (bot traffic, loading-time assignment failures,
caching bugs), a worked significant-lift-invalidated-by-SRM example). Added matching glossary terms
(Market Research) and one new Q&A each (Market Research Q75, TRA Q66). Market Research 172->174pg,
TRA 156->158pg. Master: 3,990 -> 3,994 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 75 (FII Equity-vs-Debt Flow
Divergence to TRA — a distinct cross-asset-class signal beyond Part 22's equity-only FII/DII data,
distinguishing an intra-India risk-off rotation (offsetting equity-out/debt-in) from a genuine
broad exit (both asset classes outflowing), the interest-rate-differential alternative explanation
for debt flows, a worked offsetting-flows-during-global-risk-aversion example) and PART 78 (Price
Elasticity via Natural Experiments to Market Research — distinct from Part 16's stated-preference
methods, using a competitor's price change as a quasi-experiment for genuine cross-price elasticity,
the confounding-factors isolation discipline, natural experiments as opportunistic calibration for
stated-preference research rather than a replacement, a worked competitor-discount-launch sign-up-
decline example). Added matching glossary terms (Market Research) and one new Q&A each (Market
Research Q76, TRA Q67). Market Research 174->176pg, TRA 158->160pg. Master: 3,994 -> 3,998 pages —
just 2 pages from the 4,000-page milestone.

**2026-08-05, autonomous wake-cycle: 2 more new parts — 🎉 4,000-PAGE MILESTONE CROSSED**: added
PART 76 (Composite Multi-Factor Technical Scoring Models to TRA — formalising qualitative
confluence into an actual weighted composite score, non-redundant factor selection, equal-weighting
as an honest anti-overfitting default per Part 58.2's caution, the same walk-forward validation
discipline (Part 58.4) any systematic model requires, a worked three-factor RS/volume/IV-rank
composite-screen validation example) and PART 79 (Loyalty Program ROI & Redemption-Rate Analysis to
Market Research — distinct from Part 51's referral-program research, the self-selection-bias
correction via matched-cohort comparison, redemption rate as a distinct operational diagnostic
beyond enrollment, tier-transition analysis for tiered structures, a worked naive-vs-matched-cohort-
retention-gap-shrinkage example). Added matching glossary terms (Market Research) and one new Q&A
each (Market Research Q77, TRA Q68). Market Research 176->178pg, TRA 160->162pg. Master: 3,998 ->
**4,002 pages** — the compilation has officially crossed the 4,000-page milestone the user
originally requested ("i need 2000 pages notes"), now at roughly 2x that original target.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 77 (Total Promoter Encumbrance
to TRA — synthesising Part 49's pledge and Part 72's NDU material into one combined view, why the
two mechanisms carry different risk characters and shouldn't be naively summed as uniform risk, the
combined float-availability calculation, tracking the combined trend over successive disclosures, a
worked 45%-holding/18%-pledge/10%-NDU float-availability example) and PART 80 (Push Notification
Copy & Timing Optimization to Market Research — push notifications as the research subject rather
than Part 71's ESM-delivery-mechanism use, opt-in-rate research as the foundational gate, send-time
optimization as a distinct variable from copy, notification fatigue/frequency-cap research as an
aggregate-not-per-notification concern, a worked strong-individual-metrics-but-rising-opt-out-rate
diagnostic). Added matching glossary terms (Market Research) and one new Q&A each (Market Research
Q78, TRA Q69). Market Research 178->181pg, TRA 162->164pg. Master: 4,002 -> 4,007 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 78 (Margin Trading Facility
(MTF) Book Data to TRA — a distinct cash-market retail-leverage data source beyond securities-
lending (Part 51) and F&O OI (Part 37), MTF-collateral margin-call/forced-liquidation risk
structurally similar to but distinct from promoter-pledge invocation (Part 49), individual-stock
and market-wide MTF-trend reading, a worked rally-proportionally-funded-by-rising-MTF downside-
vulnerability example) and PART 81 (ESOP Sentiment Research to Market Research — distinct from Part
73's general pulse surveys and Part 47's external review mining, the intended-vs-actual-retention-
effect gap, ESOP-mechanics comprehension testing extending Part 50's discipline, liquidity-event
perception research specific to pre-IPO companies, a worked "grants don't factor into departures
despite sizeable value" diagnostic isolating the liquidity-confidence gap from a mechanics-
comprehension gap). Added matching glossary terms (Market Research) and one new Q&A each (Market
Research Q79, TRA Q70). Market Research 181->183pg, TRA 164->167pg. Master: 4,007 -> 4,012 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 79 (NSE-BSE Price Divergence
to TRA — a distinct dual-listing arbitrage relationship from Part 57's futures-spot basis, why
divergence is normally negligible for liquid names, liquidity-concentration reasoning for why
divergence risk concentrates in thinly-traded small-caps, the practical "trust the primary-liquidity
exchange" implication, a worked stale-thin-BSE-quote-vs-genuine-NSE-price example) and PART 82
(Concept-to-Launch Tracking to Market Research — a distinct longitudinal-pipeline question beyond
any single stage-specific method already covered, why stage-siloed research loses the organisation's
own predictive-validity calibration, designing a consistent metric bridge across concept/usability/
post-launch stages, a worked category-specific concept-test-calibration-gap discovery example).
Added matching glossary terms (Market Research) and one new Q&A each (Market Research Q80, TRA
Q71). Market Research 183->185pg, TRA 167->169pg. Master: 4,012 -> 4,016 pages.

**2026-08-05, autonomous wake-cycle: 2 more new parts**: added PART 80 (ETF Premium/Discount to
iNAV to TRA — a third distinct arbitrage relationship beyond Part 57's futures basis and Part 79's
NSE-BSE divergence, the creation/redemption arbitrage mechanism (Part 35.2) and what impairs it,
international/thematic ETFs' structural trading-hours-mismatch baseline, widening-beyond-typical-
range as the actual signal, a worked persistent-international-ETF-premium example) and PART 83 (App
Store Optimization Creative Testing to Market Research — distinct from Part 43's review mining,
screenshot-order as its own variable, icon testing as a disproportionately high-leverage overlooked
element, localised-vs-generic creative testing extending Part 15's cultural-adaptation discipline,
a worked bundled-icon-and-screenshot-refresh-masking-opposing-effects diagnostic). Added matching
glossary terms (Market Research) and one new Q&A each (Market Research Q81, TRA Q72). Market
Research 185->187pg, TRA 169->171pg. Master: 4,016 -> 4,020 pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts**: added PART 81 (Sector Valuation Re-Rating/
De-Rating to TRA — a fundamentals-informed layer beyond Part 20.5's pure price-based sector rotation,
why a sector can rally on price while de-rating and vice versa, historical-multiple-range context
extending Part 21.2/45's IV Rank logic to valuation multiples, combining valuation-regime context
with pure technical breakout signals, a worked clean-breakout-but-near-top-of-historical-valuation-
range confluence example) and PART 84 (Structured Mystery-Shop Protocol Design for Financial
Branches to Market Research — deepens Part 14's generic retail mystery shopping for a higher-stakes,
compliance-sensitive context, scenario scripting for cross-branch comparability, compliance-
checkpoint scoring as a distinct dimension from service-quality scoring, shopper training/
calibration as a prerequisite for trustworthy compliance data, a worked margin-trading-product-
launch mystery-shop-design example). Added matching glossary terms (Market Research) and one new
Q&A each (Market Research Q82, TRA Q73). Market Research 187->189pg, TRA 171->173pg. Master:
4,020 -> 4,024 pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts**: added PART 82 (Bulk-Deal Category-Code
Classification to TRA — a granularity layer beneath Part 33's general bulk/block deal framework,
why FII-to-DII vs FII-to-retail/HNI composition changes interpretation of an identical-looking
transaction, tracking category-composition trend across successive deals rather than a single
transaction, the classification-completeness limitation, a worked three-consecutive-weeks FII-
selling/HNI-buying pattern example) and PART 85 (Patent & R&D Investment Tracking to Market
Research — deepens Part 7's one-line CI checklist item, technology-area classification over raw
filing count, the 18-month patent-publication-lag caveat, combining patent/hiring-signal/product-
announcement data across their different lag characteristics for a fuller pipeline view, a worked
three-source innovation-pipeline reconstruction example). Added matching glossary terms (Market
Research) and one new Q&A each (Market Research Q83, TRA Q74). Market Research 189->193pg, TRA
173->175pg. Master: 4,024 -> 4,030 pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts**: added PART 83 (Substantial-Acquisition
Ownership-Threshold Disclosures to TRA — a distinct SEBI regulatory regime from Part 54's PIT/
insider-trading-window mechanics, applying to any acquirer not just insiders, the 5%/incremental-2%/
25%-open-offer thresholds and their distinct disclosure/action implications, threshold-crossing
sequences as a distinct accumulation-tracking signal beneath scattered bulk-deal monitoring, the
open-offer price as a distinct regulator-anchored valuation reference, a worked gradual 5%->7%->9%
stake-building-campaign example) and PART 86 (Cross-Functional Research Socialization to Market
Research — a distinct organisational-influence question from Part 27's presentation-design material,
embedding findings in recurring decision-making rituals rather than one-off readouts, building
stakeholder relationships continuously rather than reactively, translating findings into stakeholder-
specific language/stakes, a worked example diagnosing why a well-presented finding failed to move a
product roadmap). Added one new Q&A each (TRA Q75, Market Research Q84) and matching glossary terms
(Market Research). TRA deepening handbook 175->178pg, Market Research 193->178pg (page-count
correction from an inflated prior count, confirmed by direct PyMuPDF page check after rebuild — not
a content reduction). Master: 4,030 -> 4,018 pages (net -12, reflecting the Market Research page-
count correction).

**2026-08-06, autonomous wake-cycle: 2 more new parts**: added PART 84 (Rights Entitlement (RE)
Trading and the Renunciation Decision to TRA — a distinct instrument-mechanics question from Part
34.4's narrow chart-adjustment trap, the RE as a short-lived separately-listed tradeable instrument,
the three genuine choices facing an eligible shareholder (subscribe/sell/lapse) and what each implies,
why RE traded price can diverge from theoretical ex-rights value and what the gap signals, a worked
example advising on a rights issue where the RE trades below theoretical value) and PART 87 (Ad/Copy
Pre-Testing Diagnostic Deepening to Market Research — a distinct diagnostic-depth question from Part
10.3's pre/post basics, message-take-out coding to catch an unintended secondary message dominating
recall, competitive ad-clutter testing versus isolated-ad testing, emotional-response-curve measurement
as a complement to stated likeability, a worked example diagnosing a high-likeability ad with weak
in-market brand-tracker movement). Added one new Q&A each (TRA Q76, Market Research Q85) and matching
glossary terms (Market Research). TRA deepening handbook 178->180pg, Market Research 178->180pg.
Master: 4,018 -> 4,022 pages. (Also fixed a build-path bug from the prior cycle: the TRA rebuild had
briefly landed in sources_md/ instead of Finance/ due to a relative-path mistake, causing the merge to
pick up a stale copy — this cycle's rebuilds were run with correct paths from Finance/ directly.)

**2026-08-06, autonomous wake-cycle: 2 more new parts**: added PART 85 (Tender-Offer vs Open-Market
Buybacks — Distinct Technical Signatures to TRA — a distinct structural question from Part 34.2's
general floor-support framing, tender-offer mechanics and the calculable acceptance-ratio price
convergence, open-market buyback mechanics as a soft extended price-capped floor, why the choice of
mechanism itself signals management conviction, a worked example distinguishing the technical read of
both structures for the same company) and PART 88 (Employee Net Promoter Score (eNPS) as a Formal
Tracked Metric to Market Research — a distinct measurement object from Part 47's review mining and
Part 73's pulse surveys, why eNPS trades diagnostic depth for tracker-style comparability, eNPS as a
leading indicator of talent-retention risk in research-function continuity, the segmentation
discipline against a masking blended score, a worked example of a stable blended eNPS masking a
declining research-function segment alongside a hiring-signal corroboration). Added one new Q&A each
(TRA Q77, Market Research Q86) and matching glossary terms (Market Research). TRA deepening handbook
180->182pg, Market Research 180->182pg. Master: 4,022 -> 4,026 pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts**: added PART 86 (Demerger Mechanics — Record-
Date Handling and When-Issued Trading to TRA — a distinct corporate-action structure from bonus/
rights/buyback mechanics already covered, since a demerger creates a genuinely new, separately-valued
listed entity rather than adjusting an existing stock, the when-issued market as real-time price
discovery ahead of formal listing, why no clean value-attribution formula exists unlike a bonus/rights
adjustment, the post-listing technical reset treating each entity as a fresh chart, a worked example
reading a 65/35 WI-market split ahead of a digital-services/manufacturing demerger's formal listing)
and PART 89 (Customer Journey Mapping — Full Methodology Deepening to Market Research — a distinct
methodological-depth question from Part 8.2's stage/touchpoint sketch, evidence-grounding a map from
real behavioural/qualitative data rather than an internal workshop alone, identifying "moments of
truth" deserving disproportionate research investment, cross-functional ownership assignment as the
map's actionability test, a worked example where funnel analytics contradict a workshop's friction
assumptions on a document-upload step). Added one new Q&A each (TRA Q78, Market Research Q87) and
matching glossary terms (Market Research). TRA deepening handbook 182->184pg, Market Research
182->184pg. Master: 4,026 -> 4,030 pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts**: added PART 87 (Delisting Mechanics — Reverse
Book-Building and the Exit-Price Read to TRA — a distinct exit event from every corporate action
covered so far, how reverse book-building discovers the exit price in the opposite direction from a
normal IPO/FPO book-build, why the promoter's acceptance decision is a genuine non-mechanical choice
that can fail the delisting entirely, reading the stock's regular-market trading price during the
bidding window as a market-implied success probability, a worked example reading a stock trading
persistently below the floor price during an active reverse book-build) and PART 90 (AI/Synthetic
Respondents — Validity Risks and Appropriate Use to Market Research — a distinct methodological
question from every human-sample technique covered so far, what synthetic respondents can plausibly
approximate versus what they structurally cannot surface, the training-data-circularity risk for
fast-moving categories, appropriate use narrowed to pre-fielding screening never as a substitute for
real fieldwork on a real decision, a worked example evaluating a vendor's proposal to replace a real
concept test with a synthetic panel for a launch decision). Added one new Q&A each (TRA Q79, Market
Research Q88) and matching glossary terms (Market Research). TRA deepening handbook 184->187pg,
Market Research 184->187pg. Master: 4,030 -> 4,036 pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts**: added PART 88 (Anchor Investor Allocation and
Lock-In as a Listing-Day Technical Factor to TRA — a distinct pre-listing signal from Part 63's RII/
NII/QIB subscription data, why anchor composition/sizing reads as an early credibility signal before
public bidding opens, the anchor lock-in schedule as a distinct dated overhang calendar from promoter
lock-in, distinguishing routine anchor profit-booking from a genuine negative reassessment at lock-in
expiry, a worked example reading partial-exit bulk deals around a 30-day anchor lock-in expiry) and
PART 91 (Multi-Sided Platform Research — Supply-Side and Demand-Side Balance to Market Research — a
distinct research-object question from every single-audience method covered so far, why the more
visible demand side is systematically over-researched relative to supply, designing genuinely separate
instruments per side rather than one stretched instrument, reading cross-side dependencies where a
demand-side symptom has a supply-side root cause, a worked example tracing a lending marketplace's
borrower-disbursal complaint to a lender-side reconciliation friction). Added one new Q&A each (TRA
Q80, Market Research Q89) and matching glossary terms (Market Research). TRA deepening handbook
187->189pg, Market Research 187->189pg. Master: 4,036 -> 4,040 pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts**: added PART 89 (Split/Divergent Credit Ratings
Across Agencies to TRA — a distinct diagnostic question from a single-agency rating-change read, why a
split rating is informative beyond either individual agency's view, distinguishing a stable house-
methodology "second opinion" split from a genuinely issuer-specific adversarial split, reading which
rating the market's own pricing is actually weighting, a worked example on a fresh issuer-specific
split triggered by a related-party-transaction disclosure) and PART 92 (Regulatory-Disclosure-
Constrained Concept/Ad Testing Deepening to Market Research — a distinct methodological-depth question
from a one-line regulatory-awareness note, the core tension between mandated disclosures and message-
clarity optimisation, testing disclosure comprehension as a first-class metric alongside standard
concept/ad metrics, isolating genuine concept weakness from disclosure-driven comprehension drag via
mandated-minimum-vs-voluntary-content testing, a worked example diagnosing weak purchase intent in a
thematic mutual-fund concept test). Added one new Q&A each (TRA Q81, Market Research Q90) and matching
glossary terms (Market Research). TRA deepening handbook 189->191pg, Market Research 189->191pg.
Master: 4,040 -> 4,044 pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts**: added PART 90 (T+1 Settlement Cycle —
Technical Implications to TRA — a distinct market-microstructure question from the execution/impact
mechanics already covered, why T+1 tightens the practical capital-tie-up window for arbitrage/hedge
strategies, the tighter T+1 corporate-action cutoff timeline versus the older T+2 convention, faster
settlement's effect on observable float for short-holding-period strategies, a worked example
recalculating a dividend cum/ex cutoff for a TRA anchored to a T+2 mental model) and PART 93 (Win-Back
/ Lapsed-Customer Research Deepening to Market Research — a distinct discipline from the exit-survey
and predictive-churn material already covered, why the original exit reason often goes stale by the
time of win-back outreach, segmenting the lapsed base by time-since-lapse and lapse reason rather than
treating it as homogeneous, testing the win-back offer itself as a researchable question, a worked
example diagnosing why a blanket discount campaign backfired specifically for service-failure-lapsed
customers). Added one new Q&A each (TRA Q82, Market Research Q91) and matching glossary terms (Market
Research). TRA deepening handbook 191->193pg, Market Research 191->193pg. Master: 4,044 -> 4,048 pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts**: added PART 91 (Sovereign Gold Bonds vs Gold
ETFs — Distinct Technical Instruments to TRA — a distinct instrument-comparison question not addressed
by any prior commodity material, structural differences (ETF continuous creation/redemption vs SGB
fixed-tenor bond) driving different technical/liquidity behaviour, reading a genuine SGB discount-to-
fair-value versus simple illiquidity noise, the tax-treatment difference as a distinct practically-
relevant factor, a worked example advising on a persistent SGB discount explained by thin trading
volume) and PART 94 (Support-Ticket Text Analytics — Emerging-Issue Detection Deepening to Market
Research — a distinct methodological-depth question from Part 35.2's one-line VoC data-source mention,
volume-vs-severity weighting against naive raw-volume ranking, baseline-relative anomaly detection as
the correct "is this new" test, the risk of a coding taxonomy too coarse to catch an emerging sub-
issue, a worked example where manual re-sampling uncovers a rapidly-growing sub-issue masked within a
stable-looking broad theme). Added one new Q&A each (TRA Q83, Market Research Q92) and matching
glossary terms (Market Research). TRA deepening handbook 193->196pg, Market Research 193->196pg.
Master: 4,048 -> 4,054 pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts**: added PART 92 (Convertible Warrant Mechanics
— A Distinct Overhang Profile to TRA — a distinct instrument from Part 63's preferential-allotment
shares, why a warrant's conditional/deferred optionality creates a fundamentally different overhang
than a straight share allotment, reading the holder's voluntary-conversion timing as a real-time
conviction signal, the forfeiture-driven signal as a rare high-conviction negative read, a worked
example reading a promoter group's early voluntary conversion two months ahead of deadline) and PART
95 (Bundle and Tiered-Pricing Research to Market Research — a distinct pricing-research question from
the single-product Van Westendorp/Gabor-Granger/BPTO methods already covered, feature-to-tier
allocation as a conjoint-style research question, cannibalisation testing unique to multi-tier
pricing, tier-migration research examining the upgrade path rather than a one-time choice snapshot, a
worked example diagnosing a Plus-tier upgrade shortfall despite strong initial choice-based-conjoint
research). Added one new Q&A each (TRA Q84, Market Research Q93) and matching glossary terms (Market
Research). TRA deepening handbook 196->198pg, Market Research 196->198pg. Master: 4,054 -> 4,058 pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts**: added PART 93 (ESOP Exercise and Vesting as a
Distinct Float-Overhang Source to TRA — a distinct, recurring overhang source from the dated, one-time
events already covered, why ESOP-driven selling reflects personal-diversification motivation rather
than a view on the company, reading the disclosed ESOP pool/vesting schedule as a forward supply
estimate, the exception where a large concentrated senior-executive ESOP sale warrants closer
scrutiny, a worked example distinguishing routine broadly-distributed ESOP selling from a senior-
executive outlier transaction) and PART 96 (Competitive Claims Substantiation Research to Market
Research — a distinct pre-publication research question from win-loss and competitive-intelligence
material, why "we believe" isn't substantiation for a published comparative claim, the comparability-
trap of matching one's best-case figure against a competitor's non-comparable figure, building a
re-testable rather than one-time claims-monitoring process, a worked example auditing a "lowest
brokerage fees" claim and catching a promotional-vs-standard-rate comparability mismatch). Added one
new Q&A each (TRA Q85, Market Research Q94) and matching glossary terms (Market Research). TRA
deepening handbook 198->200pg, Market Research 198->200pg. Master: 4,058 -> 4,062 pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts**: added PART 94 (Index Options Final Settlement
Price — A Distinct Cash-Settlement Mechanism to TRA — a distinct settlement mechanism from Part 60's
stock physical-settlement material, how the final settlement price is computed as a 30-minute volume-
weighted average rather than the closing tick, why this dampens (relative to a single-tick mechanism)
last-second manipulation incentives, the stock-vs-index expiry-day framework distinction a TRA must
keep straight, a worked example explaining a Nifty closing-tick-vs-settlement-price gap to a client)
and PART 97 (Conversational AI/Chatbot Research — Distinct Evaluation Methodology to Market Research —
a distinct evaluation object from Part 65's screen-based usability testing, ambiguous conversational
task-completion measurement, the escalation-to-human handoff as a first-class research question for
regulated financial-services contexts, adversarial/edge-case probing as a required testing dimension,
a worked example where strong topline chatbot metrics mask a severe account-security escalation gap
surfaced only by targeted adversarial probing). Added one new Q&A each (TRA Q86, Market Research Q95)
and matching glossary terms (Market Research). TRA deepening handbook 200->202pg, Market Research
200->202pg. Master: 4,062 -> 4,066 pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts**: added PART 95 (Greenshoe Option / Post-Listing
Price Stabilization Mechanism to TRA — a distinct post-listing support mechanism from every pre-/at-
listing IPO signal already covered, how the over-allotment/borrowed-share stabilisation mechanism
actually works, why greenshoe-supported price action shouldn't be over-credited as pure organic
strength, the more informative post-window read once the mechanism's mandate ends, a worked example
distinguishing a stock's pre- vs post-stabilisation-window price action) and PART 98 (Recruiting Hard-
to-Reach and Low-Incidence Respondent Populations to Market Research — a distinct recruitment-
methodology question from the general small-sample B2B framing already covered, why incidence rate
drives both cost and screener-design stakes, specialised sourcing routes beyond a standard consumer
panel, the false-qualifier risk and the verification discipline it requires, a worked example
diagnosing suspiciously fast, low-quality CFO-panel qualification). Added one new Q&A each (TRA Q87,
Market Research Q96) and matching glossary terms (Market Research). TRA deepening handbook 202->205pg,
Market Research 202->205pg. Master: 4,066 -> 4,072 pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts**: added PART 96 (Large-Cap vs Mid-Cap vs Small-
Cap Rotation — A Distinct Market-Cap-Tier Signal to TRA — a distinct rotation axis from sector rotation
and breadth already covered, why cap-tier rotation reads as a distinct risk-appetite signal, combining
cap-tier rotation with breadth for a doubly-confirming or doubly-cautious read, the liquidity-risk
caveat separating the interpretive signal from actual executability at size, a worked example reading
a large-cap-led fresh-high against deteriorating breadth and flat mid/small-caps) and PART 99 (Crisis/
Reputation Research — Measuring Recovery After a Negative Event to Market Research — a distinct
research object from routine brand tracking, the pre-event-baseline problem and why routine tracking
doubles as crisis-preparedness, trust-specific metrics distinct from general brand-health measures
during an active crisis window, tracking the recovery trajectory rather than a single post-crisis
snapshot, a worked example diagnosing a stalled recovery plateau six weeks after a data-security
incident). Added one new Q&A each (TRA Q88, Market Research Q97) and matching glossary terms (Market
Research). TRA deepening handbook 205->207pg, Market Research 205->207pg. Master: 4,072 -> 4,076 pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts**: added PART 97 (Bond Covenant Breach and
Technical Default — A Distinct Credit-Event Trigger to TRA — a distinct trigger mechanism from rating-
agency actions already covered, why "technical default" doesn't mean the company has stopped paying,
what a covenant breach gives the lender and why the lender's actual response is the more informative
signal, reading a breach in the context of which specific covenant type was breached, a worked example
reading a company's covenant breach followed by a lender waiver with only a modest rate increase) and
PART 100 (Lifecycle/Onboarding Email Sequence Effectiveness Research to Market Research — a distinct
research object from Part 87's single-message ad-copy testing, why sequence-level functional metrics
reveal what single-message engagement metrics miss, sequence-position testing to isolate which
specific message drives the outcome, the fatigue/frequency-cap tension unique to a multi-message
sequence, a worked example diagnosing declining engagement in an onboarding sequence's later messages
despite a healthy aggregate KYC-completion outcome). Added one new Q&A each (TRA Q89, Market Research
Q98) and matching glossary terms (Market Research). TRA deepening handbook 207->209pg, Market Research
207->209pg. Master: 4,076 -> 4,080 pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts**: added PART 98 (FPI Registration Categories —
A Regulatory Layer Beneath the "FII/FPI" Label to TRA — a distinct regulatory-structure question
beneath Part 82's single FII/FPI bulk-deal category label, the risk-based-tiering logic behind the
category framework, why this matters practically via occasional beneficial-ownership disclosure
filings distinct from routine shareholding-pattern filings, framing this knowledge as interpretive
credibility literacy rather than a standalone trading edge, a worked example correctly triaging an
unfamiliar FPI-related disclosure filing) and PART 101 (Podcast/Audio Advertising Research to Market
Research — a distinct measurement environment from the video/visual ad testing already covered, host-
read versus produced-spot as a distinct format choice, attention-context measurement for genuinely
divided-attention listening, host-credibility-transfer as its own distinct metric, a worked example
diagnosing uneven purchase-intent lift for identical host-read ad copy across three podcasts). Added
one new Q&A each (TRA Q90, Market Research Q99) and matching glossary terms (Market Research). TRA
deepening handbook 209->211pg, Market Research 209->211pg. Master: 4,080 -> 4,084 pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts**: added PART 99 (Offer for Sale (OFS) vs Fresh
Issue — A Distinct Read on IPO Capital-Raise Intent to TRA — a distinct structural question beneath
the single "IPO" label, why the fresh-issue/OFS split changes what the listing actually signals, why a
heavy OFS component isn't automatically negative but warrants a specific "why now, by whom" question,
the use-of-proceeds disclosure as the fresh-issue component's real diagnostic value, a worked example
reading an 80%-OFS listing where sellers are long-held financial investors with no promoter
participation) and PART 102 (Recognising Segmentation Staleness and Drift to Market Research — a
distinct maintenance question from the original segmentation-methodology material, the two distinct
staleness mechanisms of population drift versus boundary drift, monitoring metrics that surface
staleness before it becomes acute, why re-segmenting too frequently carries its own real
organisational cost, a worked example diagnosing boundary drift from a sustained six-wave narrowing
revenue gap between segments with stable segment-size shares). Added one new Q&A each (TRA Q91, Market
Research Q100) and matching glossary terms (Market Research). TRA deepening handbook 211->214pg,
Market Research 211->214pg. Master: 4,084 -> 4,090 pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts**: added PART 100 (Executive Remuneration
Disclosure — ESOP-Linked Pay as an Incentive-Alignment Signal to TRA — a distinct disclosure category
from Part 93's ESOP float-overhang material, why the fixed-cash-vs-equity-linked pay mix is itself a
governance signal, the vesting-horizon caveat on alignment strength, reading disclosed remuneration
design alongside actual insider-selling behaviour as a consistency check, a worked example where a
heavily equity-linked CEO pay structure is undermined by systematic maximum-permissible selling at
every vesting date) and PART 103 (Employee Referral Program Effectiveness Research to Market Research
— a distinct research object from customer referral research already covered, why referred-hire
quality requires a longer measurement horizon than referral volume alone, segmenting by referrer
tenure/performance, the self-selection risk in referred-employee satisfaction research, a worked
example unpacking a naive referral-vs-non-referral retention comparison that overstates the program's
causal effect). Added one new Q&A each (TRA Q92, Market Research Q101) and matching glossary terms
(Market Research). TRA deepening handbook 214->216pg, Market Research 214->216pg. Master: 4,090 ->
4,094 pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts**: added PART 101 (Bulk/Block Deal Disclosure Lag
— Reading Positioning Data with a Built-In Delay to TRA — a distinct data-latency question beneath the
bulk-deal category/pattern material already covered, why the built-in reporting lag matters more for
fast-moving situations than slow accumulation patterns, why live price/volume action often front-runs
the formal disclosure and how to read the two together, the confirmation value the lag still provides
despite being backward-looking, a worked example sequencing a Tuesday volume-spike read against
Wednesday's bulk-deal confirmation) and PART 104 (Dark-Pattern Detection Research to Market Research —
a distinct research object from Part 56's engagement-design/trading-risk material, why dark-pattern
research requires a taxonomy-based audit methodology rather than a standard usability test,
comprehension-under-realistic-conditions testing beyond a presence/absence audit, the elevated
regulatory/reputational stakes specific to financial-services contexts, a worked example auditing a
margin-trading opt-in flow with a high usability completion rate but genuine dark-pattern structural
findings). Added one new Q&A each (TRA Q93, Market Research Q102) and matching glossary terms (Market
Research). TRA deepening handbook 216->218pg, Market Research 216->218pg. Master: 4,094 -> 4,098 pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts**: added PART 102 (Minimum Public Shareholding
(MPS) Compliance — A Distinct Deadline-Driven Event to TRA — a distinct compliance-driven event from
every voluntary corporate action already covered, the mechanisms companies use to restore compliance
and their distinct technical signatures, why a compliance-driven event carries a different signal than
the same mechanism used opportunistically, the deadline itself as a schedulable dated event, a worked
example reading a promoter OFS sized exactly to a compliance threshold ahead of a disclosed deadline)
and PART 105 (Onboarding UX Research for Digitally-Underserved First-Time Investors to Market Research
— a distinct research object from Part 41's literacy-assessment material, why standard usability-
testing norms understate real-world difficulty for this population, icon/visual-language comprehension
as a distinct testable layer beneath text simplification, assisted-mode onboarding as a genuine
real-world pattern worth explicitly researching, a worked example uncovering weak account-security
comprehension masked by a strong onboarding completion rate). Added one new Q&A each (TRA Q94, Market
Research Q103) and matching glossary terms (Market Research). TRA deepening handbook 218->220pg,
Market Research 218->220pg. Master: 4,098 -> 4,102 pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts**: added PART 103 (SME Platform to Main Board
Migration — A Distinct Listing-Transition Event to TRA — a distinct listing-status change from every
corporate action already covered, the mechanical trading-characteristic changes migration brings
(tighter circuit bands, broader investor eligibility, index-inclusion eligibility), why successful
migration itself functions as a credibility/graduation signal, the liquidity-transition adjustment
window rather than an instant re-rating, a worked example reading unchanged volume/volatility in the
first two weeks post-migration as expected rather than disappointing) and PART 106 (Channel Partner/
Distributor Research to Market Research — a distinct research audience from end-customer and multi-
sided-platform research, why channel-partner research requires its own purpose-built instrument, the
channel-conflict research question of incentive alignment between partner and end-customer interest,
segmenting partners by production volume and quality rather than satisfaction alone, a worked example
escalating a channel-conflict finding where advisors candidly admit steering clients toward higher-
commission products). Added one new Q&A each (TRA Q95, Market Research Q104) and matching glossary
terms (Market Research). TRA deepening handbook 220->223pg, Market Research 220->223pg. Master: 4,102
-> 4,108 pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts + a real bug fix**: added PART 104 (Weekly Expiry
Proliferation — The Structural Within-Week Volatility Pattern to TRA — a distinct structural-market
question from the single-expiry mechanics already covered, why theta-decay-driven activity concentrates
predictably around each weekly expiry, the realised-volatility-dampening effect on non-expiry days and
its limits, why this is a baseline expectation-setting framework rather than a standalone trading
signal, a worked example distinguishing structural Thursday-expiry volatility from a genuine catalyst)
and PART 107 (Trade Show/Industry Conference Effectiveness Research to Market Research — a distinct
measurement environment from digital-channel effectiveness research, why raw lead-count is a poor
standalone metric, the relationship-deepening value lead-generation metrics miss entirely, attributing
brand-visibility value distinct from any direct lead/relationship effect, a worked example evaluating a
conference sponsorship across all three value streams rather than lead conversion alone). Added one new
Q&A each (TRA Q96, Market Research Q105) and matching glossary terms (Market Research).

**Bug found and fixed this cycle**: the two `build_handbook_pdf.py` invocations (TRA and Market
Research) had been launched as concurrent background processes every cycle this session. The script
uses hardcoded shared temp-file paths (`_handbook_tmp.html`, `_handbook_raw.pdf` in `sources_md/`) with
no collision guard — running two instances concurrently is a genuine race condition where one process's
`stamp_and_outline` step can read the *other* process's temp raw PDF. This cycle it fully manifested:
the file saved as `Technical_Research_Deepening_Handbook.pdf` was actually a complete copy of the
Market Research content (242 pages), while the real Market Research build won the race and was correct.
Because both files have been growing by matching Part-for-Part increments each cycle, a full content
swap between the two files does not change the summed total page count — meaning this could have been
silently happening on prior cycles too without the page-count cross-check catching it. **Fix applied**:
rebuilt both PDFs strictly sequentially (TRA fully completes before Market Research starts), verified
by direct text-extraction spot-checks at multiple page offsets in each file individually and in the
re-merged master PDF, confirming no duplication and correct content in both. This also revealed the
two handbooks' true, previously-masked page counts diverge more than the "always ~equal" figures
logged in recent cycles suggested (Market Research carries a dedicated Part-by-part glossary section
TRA doesn't have) — TRA deepening handbook is genuinely 225pg, Market Research is genuinely 242pg.
Master: 4,108 -> 4,129 pages (the jump reflects both the 2 new parts and this correction). **Going
forward**: the two `build_handbook_pdf.py` calls will always be run strictly sequentially, never
concurrently, to prevent recurrence.

**2026-08-06, autonomous wake-cycle: 2 more new parts (sequential build confirmed clean)**: added PART
105 (Public NCD Issue Mechanics — A Distinct Fixed-Income Listing Event to TRA — a distinct instrument-
category listing event from every equity IPO mechanic already covered, why NCD pricing logic is
fundamentally different from equity IPO pricing, post-listing NCD trading as a lower-liquidity yield-
driven secondary market, the credit-quality read as the primary technical driver distinct from any
growth catalyst, a worked example reading a listed NCD's larger price reaction to a rating downgrade
versus the same company's more muted equity reaction) and PART 108 (Fieldwork Quality Control —
Training and Monitoring Field Interviewers to Market Research — a distinct upstream discipline from
the post-hoc data-quality checks already covered, standardisation training for verbatim question
wording, interviewer effects as a distinct systematic-bias source, back-checking as the field-level
verification analogue to post-collection screening, a worked example confirming interview fabrication
via back-check after pattern indicators flagged one interviewer's completed interviews as suspicious).
Added one new Q&A each (TRA Q97, Market Research Q106) and matching glossary terms (Market Research).
Both PDFs built strictly sequentially per last cycle's fix, with output re-verified via direct
text-extraction spot-checks — no recurrence of the race-condition corruption. TRA deepening handbook
225->227pg, Market Research 242->245pg. Master: 4,129 -> 4,134 pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts (sequential build confirmed clean)**: added PART
106 (Deep-OTM Tail-Hedge Positioning as a Distinct Sentiment Signal to TRA — a distinct positioning
question from near-the-money OI and PCR already covered, why deep-OTM put buying reflects insurance-
seeking rather than directional conviction, reading a build-up in deep-OTM put OI as a distinct
sentiment gauge, why elevated tail-hedge demand doesn't itself predict the crash scenario materialising,
a worked example reading a sustained deep-OTM Nifty put OI build-up during an otherwise calm market) and
PART 109 (Omnichannel Research: Showrooming, Webrooming & Cross-Channel Attribution to Market Research
— a distinct research question from single-channel shopper/digital-analytics research already covered,
why single-channel attribution systematically misreads cross-channel behaviour, why showrooming and
webrooming require distinct diagnostic responses rather than one generic omnichannel strategy,
measuring a store's "invisible" digital-assist value that point-of-sale data alone never captures, a
worked example diagnosing an unexpected online-sales decline following a store closure evaluated on
point-of-sale revenue alone). Added one new Q&A each (TRA Q98, Market Research Q107) and matching
glossary terms (Market Research). Both PDFs built strictly sequentially. TRA deepening handbook
227->229pg, Market Research 245->247pg. Master: 4,134 -> 4,138 pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts (sequential build confirmed clean)**: added PART
107 (Index Divisor Mechanics — Keeping an Index Number Continuous to TRA — a distinct mechanical
question from index rebalancing price effects already covered, what the divisor actually does in
separating compositional change from genuine market movement, why this matters for correctly
interpreting long-run historical index-level analysis, the distinction between a divisor adjustment
and a genuine index-level move, a worked example explaining why a 20-year index chart remains one
continuous, meaningful series despite near-total constituent turnover) and PART 110 (Public Review-
Response Research to Market Research — a distinct research question from review mining already
covered, why a public response's real audience is the broader future-browsing population rather than
just the original reviewer, response-quality dimensions beyond the binary responded/not-responded
decision, the response-consistency check as its own researchable pattern, a worked example diagnosing
why an improved response-rate policy produced generic, templated, delayed responses that failed to
move prospective-customer perception). Added one new Q&A each (TRA Q99, Market Research Q108) and
matching glossary terms (Market Research). Both PDFs built strictly sequentially. TRA deepening
handbook 229->232pg, Market Research 247->249pg. Master: 4,138 -> 4,143 pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts (sequential build confirmed clean)**: added PART
108 (Trading Plan Pre-Clearance Mechanics — The Framework Behind the Signal-Strength Distinction to
TRA — a distinct mechanical question beneath Part 54.3's structured-trading-plan-vs-discretionary-
purchase signal-strength comparison, why a plan must be publicly disclosed and locked in well before
execution, the formal internal pre-clearance and compliance-officer sign-off layer, why this full
apparatus is precisely what strips a plan-executed trade of real-time signal value, a worked example
answering an interview question by walking through the full procedural chain rather than just
asserting the conclusion) and PART 111 (SKU Rationalisation / Product-Discontinuation Research to
Market Research — a distinct, opposite-direction research question from concept testing/NPD research
already covered, why low sales volume alone is an insufficient discontinuation criterion, substitution
research as the single most decision-relevant question, communication research on how a discontinuation
is announced affecting the substitution outcome, a worked example diagnosing an unexpectedly costly
rationalisation round concentrated among a high-value customer segment). Added one new Q&A each (TRA
Q100, Market Research Q109) and matching glossary terms (Market Research). Both PDFs built strictly
sequentially. TRA deepening handbook 232->234pg, Market Research 249->252pg. Master: 4,143 -> 4,148
pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts (sequential build confirmed clean)**: added PART
109 (Buyback Share Extinguishment — A Structural Feature of the Indian Regime to TRA — a distinct
post-buyback mechanical question from Part 85's buyback-structure material, why mandatory extinguishment
makes the EPS/float effect immediate and permanent versus a treasury-share regime, reading the
extinguishment disclosure as the buyback's genuine completion confirmation, why this is a genuine
cross-market comparison point for ADR-linked names, a worked example comparing an Indian buyback's
durable per-share effect against a US comparable that may retain treasury shares) and PART 112
(Celebrity/Brand-Ambassador Image-Congruence Research to Market Research — a distinct research question
from Part 101's podcast host-credibility and finfluencer-disclosure material, congruence testing before
signing an endorsement deal, the attribute-transfer risk of negative/irrelevant associations
transferring alongside positive ones, category-fit versus company-fit as a distinct layer specific to
financial services, a worked example diagnosing a well-liked general celebrity's category-credibility
failure despite strong ad recall). Added one new Q&A each (TRA Q101, Market Research Q110) and matching
glossary terms (Market Research). Both PDFs built strictly sequentially. TRA deepening handbook
234->236pg, Market Research 252->254pg. Master: 4,148 -> 4,152 pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts (sequential build confirmed clean)**: added PART
110 (Creeping Acquisition — The Distinct Annual Promoter Stake-Building Allowance to TRA — a distinct
regulatory allowance from Part 83's threshold-crossing framework, why this specific carve-out exists
for an existing promoter's gradual accumulation versus a fresh acquirer's stake-building, reading a
promoter's consistent use of the full annual allowance as a distinctly strong, sustained conviction
signal, the corresponding lighter negative-space signal of not using available headroom, a worked
example reading a promoter's three-consecutive-year near-maximal creeping-acquisition pattern) and
PART 113 (In-App Review-Prompt Timing Research to Market Research — a distinct upstream research
question from Part 110's public review-response research, why prompt timing systematically biases
which users respond, the representativeness tension between optimising for positive volume and
genuine signal, testing prompt frequency/dismissal-respect as its own question, a worked example
diagnosing a review-prompt design generating negative reviews specifically about its own intrusiveness
rather than the underlying product). Added one new Q&A each (TRA Q102, Market Research Q111) and
matching glossary terms (Market Research). Both PDFs built strictly sequentially. TRA deepening
handbook 236->238pg, Market Research 254->256pg. Master: 4,152 -> 4,156 pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts (sequential build confirmed clean)**: added PART
111 (Put-Call Parity and Synthetic Positions — A Distinct Arbitrage-Based Framework to TRA — a distinct
foundational relationship from the Greeks-based options material already covered, what put-call parity
actually says and why it must hold via arbitrage in a liquid market, synthetic positions as parity's
direct practical consequence, why persistent parity violations are a distinct higher-conviction friction
signal rather than free money, a worked example reading a persistent parity deviation as evidence of a
stock-specific borrow constraint) and PART 114 (Cancellation-Flow Save-Offer Effectiveness Research to
Market Research — a distinct in-the-moment research object from Part 93's win-back and Part 104's dark-
pattern research, why cancellation reason must be captured before a save-offer is selected, distinguishing
genuine retention lift from mere friction-driven delay, the ethical/dark-pattern boundary specific to
cancellation-flow research, a worked example diagnosing an inflated same-day save-offer acceptance rate
masking poor multi-month retention). Added one new Q&A each (TRA Q103, Market Research Q112) and
matching glossary terms (Market Research). Both PDFs built strictly sequentially. TRA deepening handbook
238->241pg, Market Research 256->258pg. Master: 4,156 -> 4,161 pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts (sequential build confirmed clean)**: added PART
112 (Promoter Demat-Account Freeze — A Distinct Regulatory-Enforcement Signal to TRA — a distinct
enforcement mechanism from every disclosure-based promoter signal already covered, why a freeze is
categorically more severe than any interpretive disclosure-based finding, reading the freeze's specific
scope (promoter-level vs company-level), why a freeze is procedural/provisional rather than a final
determination and requires tracking the underlying resolution, a worked example reading an initial
freeze order and its subsequent resolved-compliance outcome) and PART 115 (Product Label/Claim
Substantiation Research to Market Research — a distinct research object from Part 96's competitive
claims substantiation, why a label claim requires ongoing rather than one-time verification, the
consumer-comprehension layer where a technically-true claim can still broadly mislead, cross-functional
research ownership spanning legal/R&D/market research, a worked example diagnosing a technically-
accurate "made with real fruit" claim that comprehension testing reveals creates an inflated impression).
Added one new Q&A each (TRA Q104, Market Research Q113) and matching glossary terms (Market Research).
Both PDFs built strictly sequentially; frontmatter total needed a one-page correction pass (4,167 guess
-> 4,166 actual), standard two-pass discipline. TRA deepening handbook 241->243pg, Market Research
258->261pg. Master: 4,161 -> 4,166 pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts (sequential build confirmed clean)**: added PART
113 (IPO Price Band and Cut-Off Price — The Book-Building Price-Discovery Process to TRA — a distinct
mechanical layer beneath the RII/NII/QIB subscription material already covered, how the price band
floor/cap is set in advance versus how the cut-off price is actually market-discovered through bidding,
the "cut-off price" bid option's specific purpose for retail investors, how the final cut-off price is
determined from the aggregate bid book, a worked example explaining why a specific-price bid below the
eventual cut-off price is rejected despite adequate funds) and PART 116 (Packaging Shelf-Standout
Testing to Market Research — a distinct research question from Part 14.3's share-of-shelf/planogram
material, why testing a design in isolation systematically overstates real-world standout, eye-tracking
and time-to-locate as objective standout measures beyond self-report, the standout/legibility tradeoff
between capturing attention and brand identification, a worked example diagnosing a bold redesign that
improves standout but measurably degrades brand identification). Added one new Q&A each (TRA Q105,
Market Research Q114) and matching glossary terms (Market Research). Both PDFs built strictly
sequentially. TRA deepening handbook 243->245pg, Market Research 261->263pg. Master: 4,166 -> 4,170
pages.

**2026-08-06, autonomous wake-cycle: 2 more new parts (sequential build confirmed clean)**: added PART
114 (Co-Location and Algorithmic Market Structure — A Distinct Infrastructure Layer to TRA — a distinct
underlying infrastructure layer from Part 18's execution/impact mechanics, why physical distance to the
matching engine translates directly into a measurable speed advantage, the regulatory framing of co-
location as an equally-purchasable paid service rather than preferential access, why this matters for a
TRA's execution-timing expectations rather than as a trading edge itself, a worked example explaining
ultra-fast, choppy price action in the seconds after a scheduled data release as algorithmic-
infrastructure-driven rather than considered price discovery) and PART 117 (Trade Promotion and
Slotting-Fee Research to Market Research — a distinct, more financially-focused research question from
Part 19's category-management material, why trade-promotion ROI research must separate incremental
lift from pantry-loading/pull-forward, slotting-fee breakeven modelling as a forward-looking question
distinct from promotion ROI measurement, why retailer-specific research doesn't transfer cleanly across
formats/relationships, a worked example evaluating a requested slotting fee against a retailer-specific
historical velocity benchmark). Added one new Q&A each (TRA Q106, Market Research Q115) and matching
glossary terms (Market Research). Both PDFs built strictly sequentially. TRA deepening handbook
245->247pg, Market Research 263->265pg. Master: 4,170 -> 4,174 pages.

**Running total: 4,174 pages.**
