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
Combines the existing Equity/Valuation/Investments-Portfolio-Management/Technical-Research
(career guide) + Technical-Analysis-Complete (deep book, from trading_learning/) + the new
Market Research handbook into one **2,252-page** volume for the 3 stock-market target roles
(Senior Equity Research, Market Research, Technical Research — see
job_apply_agent/job_search/senior_research_skills.md). Rebuild via
`sources_md/merge_stock_market_master.mjs` (Node/pdf-lib — run `npm install` once in
`sources_md/`, its `package.json` pins the dependency) after any component PDF changes;
front matter source is `sources_md/_stock_market_roles_frontmatter.html`, regenerated via
`sources_md/_render_frontmatter.py`. Deliberately still excludes the rest of
study/trading_learning/ (Options-Trading-Complete, The-Complete-Indian-Market-Trader — trading
mechanics, not research) and Finance-1_FULL.pdf (overlaps Investments component already merged
in) — can be added in a later stage if the target roles need trading-mechanics depth too.
