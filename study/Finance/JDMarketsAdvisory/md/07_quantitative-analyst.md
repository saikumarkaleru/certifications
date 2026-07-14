# Quantitative Analyst (Quant)

## Snapshot
A Quantitative Analyst — "quant" — builds the mathematical models that price financial instruments, forecast markets, and measure risk. This is the deep end of finance, where the job is genuinely applied maths and code rather than spreadsheets and narrative. Quants split into flavours: **sell-side desk quants** at banks price and hedge derivatives and support traders; **buy-side quants** at hedge funds and quant asset managers build signals and systematic trading strategies (often called quant researchers); **risk/model quants** develop the models validators later check; and **vendor quants** at analytics firms build libraries and tools sold to the industry. Be honest up front: **the bar is high** — a strong STEM background, real programming ability, and comfort with stochastic calculus are effectively mandatory. Ladder: Junior/Associate Quant -> Quant Analyst -> Senior Quant / Quant Researcher -> VP/Lead Quant -> Head of Quant / Quant PM.

## What you'll actually do
- Build and maintain **pricing models** for derivatives (options, swaps, structured products) and calibrate them to market data.
- Develop **risk models** — sensitivities (Greeks), VaR, scenario and stress engines.
- Research and prototype trading signals or systematic strategies (buy-side), and backtest them rigorously against historical data.
- Apply **stochastic calculus, PDEs, Monte-Carlo simulation, time-series econometrics and machine learning** to real financial problems.
- Write production-quality code, clean data pipelines, and validate that model output is numerically stable and correct.
- Collaborate with traders, portfolio managers or risk teams to turn a desk problem into a working model.
- Document methodology so results are reproducible and defensible.

> Synthesised from real postings: build complex pricing and risk models, apply time-series and machine-learning techniques, and implement them in Python/C++ with strong software-engineering discipline.

## Must-have skills
Hard skills: **stochastic calculus and probability**, differential equations, numerical methods (Monte-Carlo, finite difference), time-series analysis, optimization, and increasingly machine learning. Deep understanding of **derivatives pricing** (Black-Scholes and beyond) for pricing roles, or statistical modelling for buy-side signal work. Above all, **strong programming** — this is a coding job, not a maths quiz. Soft skills: the ability to reduce a messy real-world problem to a clean model, intellectual honesty about what a model can't do, and clear communication with non-quants (a trader must trust your number in seconds).

## Tools & software
- **Python** — the lingua franca (numpy, pandas, scipy, scikit-learn, PyTorch/TensorFlow for ML quants).
- **C++** — still dominant for low-latency pricing libraries and HFT.
- **SQL** for data; sometimes R, MATLAB, or KDB+/q for tick data.
- **Bloomberg / Refinitiv** market data; internal pricing/risk libraries (QuantLib and proprietary).
- Git, Linux, and general software-engineering tooling — quants are expected to ship real code.

## Qualifications & certifications
Degree: this is the one role in this book where a **master's or PhD in a quantitative field** (financial engineering, maths, physics, statistics, CS, engineering) is close to a hard requirement. A B.Com/MBA-Finance alone will rarely clear the bar without serious quantitative retooling. Certifications:
- **CQF (Certificate in Quantitative Finance)** — the most targeted credential; designed exactly for this transition and respected as a signal of applied quant skill.
- **FRM** — helpful for risk-quant and model roles.
- **CFA** — useful context, but not what gets you a quant seat; the maths and code do.
Certifications supplement, never replace, demonstrable quantitative and programming ability.

## Experience & typical titles
| Band | Typical title | What's expected |
|---|---|---|
| Entry (0-2 yrs) | Junior Quant, Quant Analyst, Quant Developer | Implement/calibrate models, build tooling under guidance |
| 2-5 yrs | Quant Analyst, Quant Researcher, Associate | Own a model or strategy, research independently |
| 5-8 yrs | Senior Quant, VP Quant, Lead | Design methodology, mentor, own a book/desk's models |
| 8+ yrs | Head of Quant, Quant PM | Strategy, P&L or firm-wide model ownership |

## ATS keywords to mirror
Quantitative analyst, quant, pricing models, derivatives pricing, risk models, stochastic calculus, Monte Carlo, PDE, numerical methods, time series, machine learning, backtesting, Python, C++, SQL, QuantLib, Bloomberg, VaR, Greeks, optimization, systematic strategies, financial engineering, CQF, FRM, quantitative research.

## Salary in India (indicative, FY2026)
| Experience band | Indicative range (Rs LPA) |
|---|---|
| Entry (0-2 yrs) | 12 - 25 |
| 2-4 yrs | 25 - 45 |
| 5-8 yrs | 45 - 90+ |

*Approximate and wide. Buy-side/hedge-fund quant pay (with bonus) can far exceed these; bank and vendor roles cluster lower. Mumbai and Bengaluru dominate. Compensation reflects the genuinely scarce skill set.*

## Who's hiring
- **Global banks' GCCs / desks**: Goldman Sachs, Morgan Stanley, JPMorgan, Deutsche Bank, Nomura — desk and risk quants in Bengaluru/Mumbai.
- **Quant funds & prop shops**: WorldQuant, Tower Research, Graviton, AlphaGrep, Quadeye — buy-side and HFT research.
- **Asset managers & vendors**: quant teams at large AMCs; analytics vendors (Bloomberg, MSCI) building model libraries.
- **Analytics firms**: Acuity, S&P Global for model-development support roles.

## How to break in / stand out
Be clear-eyed: for a commerce/MBA-Finance reader, breaking into a true quant role usually requires **deliberately acquiring the quantitative foundation** — either a quant master's or a serious self-study path (CQF plus real maths). Don't fake it; the interviews probe stochastic calculus and coding directly.

The portfolio that impresses is a **working quant project on GitHub**: for example, implement an options pricer in Python (Black-Scholes plus a Monte-Carlo and a binomial-tree method), calibrate it to real market quotes, and compute and hedge the Greeks — or build and honestly backtest a simple systematic strategy with proper transaction costs and out-of-sample testing. Clean, documented, reproducible code that shows you understand *both* the maths and the software matters more than any certificate.

**The single biggest differentiator is provable depth**: the field is full of people who took an online course, and interviewers can tell in ten minutes. The candidate who can derive a result on the whiteboard *and* has shipped correct, tested code stands apart. If the full quant bar is out of reach, the adjacent roles in this book — model validation, risk analytics, or data-heavy financial analysis — are more realistic on-ramps that still use much of the same toolkit.
