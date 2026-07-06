# Q&A — Market Indices and Benchmarks

Companion practice bank for Chapter 13. Every question is followed by a full answer. Section A checks concepts, B applies them to numbers and situations, C rehearses interview questions with model answers, and D sharpens judgement through MCQs with reasoning.

---

## Section A — Concept Check

**A1. What single problem does a market index exist to solve, and what is that problem's technical name?**

An index exists to answer "did the market go up or down?" when there are thousands of individual price moves the human brain cannot aggregate. Its job is **information compression with representativeness**: shrink thousands of prices into one number without losing the essential signal of where the market is heading. Charles Dow's 1896 insight was that a handful of representative stocks, averaged, becomes a *thermometer* for the whole market — one number you can quote, track over time, and compare against. Everything else in index design is machinery serving that one goal.

**A2. Name the three design ingredients baked into the definition of an index.**

(1) **A basket of constituents** — a deliberate, rule-based, periodically reviewed set of securities (e.g., the 30 largest, most-traded firms). (2) **A weighting scheme** — the rule deciding how much each constituent's move influences the number; this is the single most consequential design choice. (3) **A base value and a divisor** — an index number is meaningful only relative to a starting point (Nifty's base was 1,000 on 3 November 1995), and a divisor keeps the number continuous when the basket changes.

**A3. Why is the mental model "an index is a hypothetical portfolio" so important?**

Because it explains *replicability*. The Sensex value is essentially what a portfolio holding those 30 stocks in index proportions would be worth, expressed as an index number. If an index is just a rule-based portfolio, you can physically *buy* its constituents in its weights and reproduce its return — which is the entire foundation of index funds and ETFs, and the reason derivatives can be written on an index as their underlying.

**A4. Why does a naive average-of-prices index break, and what fixes it?**

It breaks on **mechanical, non-market events** — chiefly stock splits. If a ₹300 stock does a 10-for-1 split it drops to ₹30 though nothing about the company changed; a simple average would "crash" purely from an accounting event. The fix is the **divisor**: instead of dividing by the number of stocks, you divide by an adjustable denominator recalculated whenever composition changes for a non-market reason, chosen so the index value is *unchanged at the instant the event happens*. Real price moves are then measured correctly afterward.

**A5. Contrast price-weighting, full-cap weighting, and free-float weighting in one sentence each.**

**Price-weighted**: influence is proportional to share *price*, so a high-priced stock dominates regardless of company size (economically arbitrary). **Full market-cap weighted**: influence is proportional to price × *all* shares outstanding, which is economically sensible but over-counts locked-away promoter and government stock that never trades. **Free-float cap weighted**: influence is proportional to price × only the *publicly tradable* shares, which is both realistic and replicable — the modern global standard.

**A6. What is the free-float factor, and how does it enter the weight calculation?**

The **free-float factor** is the fraction of a company's shares actually available for public trading — so a company with 70% promoter holding has a free-float factor of 0.30. Free-float market cap = price × shares outstanding × free-float factor. Weight in the index is then each stock's free-float cap divided by the total free-float cap of all constituents.

**A7. Why did free-float weighting "win" over full-cap weighting?**

Because it measures the market investors can *actually buy*. Full-cap weighting treats a 60%-government-owned PSU as if all its shares were investable, inflating the weight of promoter-heavy companies and distorting the tradable picture. Free-float counts only shares that trade, which (1) makes the index **replicable** — a fund can buy the available shares in index proportions without chasing locked-away promoter stock — and (2) stops a thinly-floated giant from dominating a benchmark no fund could physically track.

**A8. Distinguish rebalancing from reconstitution.**

**Reconstitution** changes *who* is in the index — swapping out companies that no longer qualify (shrunk, illiquid, delisted, merged) for ones that now do. **Rebalancing** changes *how much weight* each existing member carries — resetting weights to the methodology as prices and free-float factors drift, and applying caps to prevent over-concentration. Mnemonic: reconstitution = membership, rebalancing = weights. Nifty and Sensex are reviewed semi-annually; the S&P 500 quarterly.

**A9. What is the difference between a Price Return Index (PRI) and a Total Return Index (TRI), and why does it matter for benchmarking?**

A **PRI** tracks only price changes and ignores dividends; a **TRI** assumes dividends are reinvested. It matters because a real fund *earns and reinvests dividends*, so comparing a fund against a PRI unfairly flatters the fund — the fund gets credit for dividend income the benchmark pretends doesn't exist. SEBI now mandates that Indian funds benchmark against the **TRI** so the comparison is apples-to-apples.

**A10. Define alpha and beta in the context of a benchmark index.**

**Alpha** is a portfolio's excess return *over* its benchmark index — the value the manager added (or destroyed) beyond simply riding the market. **Beta** is the portfolio's sensitivity to the benchmark's moves — how much it tends to rise or fall for a given move in the index. The index serves as the "market portfolio" proxy against which both are measured, which is also why the index is central to CAPM.

---

## Section B — Applied / Scenario Questions

**B1. An index of three stocks (A ₹100, B ₹200, C ₹300) uses a simple price average, so it reads 200 with divisor 3. Stock C does a 10-for-1 split to ₹30. Compute the new divisor that keeps the index continuous.**

Just before the split the index was (100+200+300)/3 = 200. After the split the price sum is 100+200+30 = 330, but we want the index still to read 200 at that instant. New divisor = 330 / 200 = **1.65**. From now on the index = (sum of prices) / 1.65, so genuine future price moves register correctly while the split's mechanical drop is absorbed. (This is exactly how the Dow's divisor drifted from 30 down to roughly 0.163 over decades of splits.)

**B2. Two companies both have a full-cap of ₹20,000 cr: MegaPSU (75% promoter-held) and WidelyHeld (20% promoter-held). Compute each one's free-float cap and explain who dominates a free-float index.**

MegaPSU free-float factor = 1 − 0.75 = 0.25 → free-float cap = 0.25 × 20,000 = **₹5,000 cr**. WidelyHeld free-float factor = 1 − 0.20 = 0.80 → free-float cap = 0.80 × 20,000 = **₹16,000 cr**. Under full-cap weighting they tie; under free-float weighting **WidelyHeld dominates 16,000 to 5,000**, because most of MegaPSU's shares are locked with the government and never trade. Free-float gives the more investable, realistic picture.

**B3. Build a two-stock free-float index. Stock X: ₹500, 100 cr shares, free-float 0.50. Stock Y: ₹200, 200 cr shares, free-float 0.75. Base index = 1,000. Find the divisor, then the index after X rises to ₹550 and Y falls to ₹190.**

Base free-float caps: X = 500 × 100 × 0.50 = ₹25,000 cr; Y = 200 × 200 × 0.75 = ₹30,000 cr; total = ₹55,000 cr. Divisor = 55,000 / 1,000 = **55**. Next day: X = 550 × 100 × 0.50 = ₹27,500 cr; Y = 190 × 200 × 0.75 = ₹28,500 cr; total = ₹56,000 cr. Index = 56,000 / 55 = **1,018.18**, i.e. **+1.82%**. Note X rose 10% and Y fell only 5%, yet the index gained just 1.82% — because Y carried the larger free-float weight (30,000 vs 25,000). Cap-weighting lets the bigger constituent set the tone.

**B4. Two stocks: BigCo (₹100, market cap ₹10,00,000 cr) and PriceyCo (₹1,000, cap ₹50,000 cr). BigCo rises 20% to ₹120; PriceyCo falls 10% to ₹900. Compute the index move under price-weighting and under cap-weighting.**

**Price-weighted:** base sum = 100 + 1,000 = 1,100; new sum = 120 + 900 = 1,020; change = (1,020−1,100)/1,100 = **−7.3%**. **Cap-weighted:** BigCo +20% of 10,00,000 = +₹2,00,000 cr; PriceyCo −10% of 50,000 = −₹5,000 cr; net +₹1,95,000 cr on a base of ₹10,50,000 cr = **+18.6%**. Same day, same stocks, **opposite verdicts** — one method says the market fell 7%, the other says it rose 19%. This is precisely why weighting is the most consequential design choice, and why the price-weighted Dow can misrepresent the real US market.

**B5. A Nifty 50 index fund charges a 0.20% expense ratio, loses ~0.05% to rebalancing transaction costs, and ~0.03% to cash drag. If the Nifty 50 TRI returns 12.0%, what does the fund return, and what is the tracking difference?**

Fund return ≈ 12.0 − 0.20 − 0.05 − 0.03 = **11.72%**. Tracking difference ≈ **0.28%**. This shows *structurally why a plain index fund cannot beat its index* — the index carries no fees or trading costs, so the fund lags by roughly its all-in costs. Yet the same fund typically beats the *majority of active funds*: SPIVA studies show ~80–90% of active large-cap funds underperform their benchmark over 15 years, mostly because of their far higher fees.

**B6. A promoter of an index constituent sells a 10% stake into the public market. Nothing else changes. What happens to that stock's weight in a free-float index, and when?**

Its **free-float factor rises** (more shares are now publicly tradable), so its free-float market cap and hence its index weight **increase** — even though the price and total shares outstanding are unchanged. But the change is not instantaneous in the index: providers reset free-float factors at scheduled **rebalancing** dates, so the higher weight is applied at the next review, not the moment the promoter sells. At that rebalancing, passive funds tracking the index must buy more of the stock to match its new higher weight.

**B7. When Tesla was added to the S&P 500 in December 2020, index funds had to buy roughly $80 billion of the stock at once. Explain the mechanism and why the buying was "price-insensitive."**

This is the **index-inclusion effect** driven by **reconstitution**. Every S&P 500 index fund and ETF is mandated to hold the index constituents in index weights; the instant Tesla joined, each fund was *forced* to buy it to keep matching the benchmark, regardless of Tesla's valuation. The demand was **price-insensitive** because the funds' job is to track, not to judge whether Tesla was cheap or dear — they must own it at whatever price. Predictable flows like this are why traders position ahead of announced index changes, and why inclusion often causes a price pop.

**B8. An ETF's traded market price drifts to 1.5% above the value of its underlying holdings (its NAV). Describe the arbitrage that pulls it back and who performs it.**

**Authorised Participants (APs)** — large institutions — perform **creation**: they assemble the basket of underlying stocks (cheaper, at NAV), deliver it to the fund in exchange for new ETF units, and sell those units into the market at the inflated price, pocketing the ~1.5% gap. This selling pushes the ETF price back **down** toward NAV. (If the ETF instead traded *below* NAV, APs buy cheap ETF units and *redeem* them for the more valuable underlying stock, pushing the price up.) This continuous creation/redemption arbitrage keeps an ETF's traded price glued to the value of the underlying index basket.

---

## Section C — Interview-Style Questions (with model answers)

**C1. "Explain to a non-finance friend what a stock index actually is and why it exists."**

*Model answer:* Imagine trying to judge today's weather by reading the temperature of every street in a city — useless. An index is like the city's single reported temperature: it takes a chosen basket of important stocks and combines them into one number so you can instantly say whether the market rose or fell. It exists because the human brain can't aggregate thousands of individual price moves into a verdict. Technically it's a rule-based, single-number measure of a basket's performance over time — and crucially it behaves like a *hypothetical portfolio*, so you can actually buy those stocks in the same proportions and reproduce the index's return. That replicability is what makes index funds, ETFs, and index derivatives possible. So an index is simultaneously a thermometer for sentiment, a yardstick for performance, and a blueprint for a portfolio.

**C2. "Why do professionals prefer the S&P 500 over the Dow, even though the Dow is more famous?"**

*Model answer:* Because of the weighting method. The Dow is **price-weighted** across just 30 stocks — a historical quirk from 1896 when summing prices was the only feasible arithmetic. Price-weighting means a high-priced stock outvotes a low-priced one *regardless of company size*: a ₹1,000 stock has ten times the influence of a ₹100 stock even if the ₹100 stock is a far bigger company. That's economically arbitrary — a stock split, which changes nothing real, would halve a company's Dow influence. The **S&P 500** is **free-float market-cap weighted** across 500 stocks covering ~80% of US market cap, so influence tracks real economic size and only publicly tradable shares. It's broader, more representative, and replicable, which is why trillions of dollars are benchmarked to it. My one-liner: a price-weighted index lets a high-priced small company outvote a low-priced giant, which is exactly the flaw free-float cap-weighting fixes.

**C3. "A fund manager tells you she returned 15% last year. Is that good? Walk me through how you'd judge it."**

*Model answer:* Fifteen percent means nothing in isolation — I need the **benchmark**. If her mandate is large-cap Indian equity, I compare against the Nifty 50 **Total Return Index** for the same period. If the Nifty TRI returned 22%, she actually *destroyed* value versus simply buying an index fund — she underperformed by 7 percentage points, i.e. negative **alpha**. If the Nifty TRI returned 10%, she added 5 points of alpha, which is genuinely good. I insist on the *Total* Return Index, not the Price Return Index, because her fund earned and reinvested dividends, so benchmarking against a dividend-blind PRI would unfairly flatter her. I'd also check her **beta** and risk taken to earn that return. The deeper point: a return is only meaningful relative to the opportunity cost of the cheap, passive alternative — the index.

**C4. "Explain free float and why an index maker bothers with it instead of just using total market cap."**

*Model answer:* Free float is the slice of a company's shares actually available for public trading — it excludes promoter holdings, government stakes, and strategic locked-in holdings. Free-float market cap = price × shares outstanding × free-float factor. Index makers bother with it for two reasons. First, **realism**: if the government owns 60% of a PSU, that 60% never trades, so counting it overstates the company's true footprint in the *investable* market. Full-cap weighting would let promoter-heavy giants dominate a benchmark disproportionately to what investors can actually own. Second, **replicability**: an index fund can only buy shares that trade. A free-float index weights companies by exactly the shares a fund can physically acquire, so the fund can track it faithfully without trying to buy locked-away stock. That's why Sensex, Nifty, S&P 500, MSCI, and FTSE all moved to free-float.

**C5. "How does an index fund work, can it beat its index, and why would anyone buy one if it can't?"**

*Model answer:* An index fund's mandate is not to *beat* an index but to *become* it — hold the same stocks in the same free-float weights and deliver the same return minus a tiny fee. For a liquid index like the Nifty 50 it uses **full replication** (buy all 50 in exact weights); for a huge index it uses **sampling**. It structurally *cannot* beat its index, because the index itself bears no fees or trading costs, whereas the fund pays an expense ratio, rebalancing costs, and suffers cash drag — the gap is called **tracking error**, and it means the fund lags the index by roughly its all-in cost, maybe 0.2–0.3%. So why buy one? Because it reliably beats *most active managers*: SPIVA data show 80–90% of active large-cap funds underperform their benchmark over 15 years after their much higher fees. You give up the tiny chance of beating the market in exchange for near-certainty of beating the average professional, at a fraction of the cost. Over decades, that fee gap compounds into an enormous advantage.

---

## Section D — Multiple-Choice Questions (with reasoning)

**D1. The single most consequential design choice in building an index is:**
(a) The number of constituents
(b) The base date
(c) The weighting method
(d) The name of the index provider

**Answer: (c).** The weighting method decides how much each constituent influences the number, and it can produce *opposite verdicts* on the same day from the same stocks (see B4). The number of constituents and base date matter less, and the provider's name is cosmetic.

**D2. Under free-float weighting, a company with 80% promoter holding has a free-float factor of:**
(a) 0.80
(b) 0.20
(c) 1.00
(d) 0.60

**Answer: (b).** The free-float factor is the *publicly tradable* fraction = 1 − promoter/locked holding = 1 − 0.80 = 0.20. Only that 20% counts toward the company's free-float market cap and index weight.

**D3. A stock in a price-weighted index does a 2-for-1 split (price halves). Without an adjustment, the index would:**
(a) Rise, because there are more shares
(b) Stay exactly the same
(c) Fall, because the summed price dropped
(d) Double

**Answer: (c).** Price-weighting sums prices, so a halved price mechanically drops the sum and the index — even though nothing real changed. The fix is recalculating the **divisor** so the index is unchanged at the instant of the split.

**D4. Which set of indices is free-float market-cap weighted?**
(a) Dow Jones and Nikkei 225
(b) Sensex, Nifty 50, and S&P 500
(c) Nikkei 225 and FTSE 100
(d) Dow Jones and S&P 500

**Answer: (b).** Sensex, Nifty 50, and S&P 500 are all free-float cap-weighted. The Dow and Nikkei 225 are the notable *price-weighted* holdouts, so (a), (c), and (d) each wrongly include a price-weighted index.

**D5. The Sensex has a base value of 100 and a base period of 1978–79. A Sensex of 80,000 therefore means:**
(a) The 30 stocks average ₹80,000
(b) The basket is worth 800× its 1978–79 value
(c) The market P/E is 800
(d) There are 80,000 shares in the index

**Answer: (b).** An index number is relative to its base; 80,000 against a base of 100 means the basket is 800 times its base-period value. It is not an average price, a P/E, or a share count.

**D6. "Reconstitution" of an index refers to:**
(a) Resetting the weights of existing members
(b) Recalculating the divisor after a split
(c) Changing which companies are constituents
(d) Reinvesting dividends into the index

**Answer: (c).** Reconstitution = changing *membership* (adding/removing companies). Resetting weights of existing members is **rebalancing** (a); divisor recalculation (b) is the continuity mechanism; dividend reinvestment (d) is the PRI-vs-TRI distinction.

**D7. Same day: BigCo (huge market cap, low price) rises 20%; PriceyCo (small cap, high price) falls 10%. A price-weighted index of the two would most likely:**
(a) Rise, tracking the bigger company
(b) Fall, because the high-priced stock dominates
(c) Stay flat
(d) Be impossible to compute

**Answer: (b).** Price-weighting keys on price, not size, so the high-priced PriceyCo dominates and its 10% fall outweighs BigCo's 20% rise (worked in B4: −7.3%). A cap-weighted index would instead *rise*, because BigCo's economic size dominates.

**D8. A fund's return minus its benchmark index's return, driven by fees, cash drag, and transaction costs, is called:**
(a) Alpha
(b) Beta
(c) Tracking error
(d) The divisor

**Answer: (c).** That gap is **tracking error** (or tracking difference). Alpha is a *deliberate* excess return from active skill; beta is sensitivity to the index; the divisor is the continuity denominator. For a passive fund this gap is structurally negative by roughly the expense ratio.

**D9. SEBI requires Indian mutual funds to benchmark against the Total Return Index rather than the Price Return Index because:**
(a) The TRI is always a higher number, flattering the fund
(b) A fund reinvests dividends, so only the TRI gives an apples-to-apples comparison
(c) The PRI cannot be computed for Indian indices
(d) The TRI has fewer constituents

**Answer: (b).** A real fund earns and reinvests dividends; benchmarking against a dividend-blind PRI would unfairly flatter the fund. The TRI assumes dividend reinvestment, making the comparison fair. It is not about which number is higher per se, and both indices have identical constituents.

**D10. The ETF creation/redemption mechanism keeps an ETF's market price near its NAV by:**
(a) A regulator fixing the price daily
(b) The fund manager buying back units at NAV
(c) Authorised Participants arbitraging the gap between ETF price and underlying basket value
(d) Halting trading whenever price diverges from NAV

**Answer: (c).** Authorised Participants create units (swap the underlying basket for new units) when the ETF trades above NAV and redeem units for stock when it trades below, and this arbitrage force continuously pulls the traded price back to the value of the underlying index basket. No regulator or halt is involved.

---

*End of practice bank. Re-attempt Section D from memory after a day; if you can also reproduce the divisor logic (A4, B1), the price-vs-cap opposite-verdict example (B4, C2), and the reason free-float won (A7, C4) unprompted, the chapter is secure.*
