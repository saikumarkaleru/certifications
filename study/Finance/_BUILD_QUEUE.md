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

**Running total: 3,757 pages.**
