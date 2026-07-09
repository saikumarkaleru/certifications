# Q&A — International and Emerging-Market Bonds

A practice bank for the concept chapter *International and Emerging-Market Bonds*. Work each question before reading the answer. Formulas used throughout:

- Home return: $1+R_{home}=(1+R_{local})(1+R_{FX})$, with $R_{FX}=S_1/S_0-1$ and $S$ = home currency per unit of foreign currency.
- CIP forward: $F_0=S_0\,(1+i_{HC})/(1+i_{FC})$.
- Hedged return (approx.): $R_{hedged}\approx R_{local}-(i_{FC}-i_{HC})$.
- Spread ↔ default: $\text{Spread}\approx p\times(1-R)=p\times\text{LGD}$, so $p\approx\text{Spread}/\text{LGD}$.

---

## Section A — Concept Checks

**A1. What three orthogonal questions define any international bond?**
(1) *Who is the issuer and where do they live?* (2) *What currency are the cash flows in?* (3) *Under whose law and in which market is it issued and regulated?* Every piece of jargon — Yankee, eurodollar, hard-currency sovereign — is just a label for one combination of answers to these three axes.

**A2. Distinguish a foreign bond from a eurobond.**
A *foreign bond* is issued by a foreign issuer *into a domestic market*, in *that market's currency*, under *that market's rules* (e.g. a Japanese firm selling SEC-registered USD bonds in the US = a Yankee bond). A *eurobond* is issued in the offshore international market in a currency *different from the country where it is sold*, escapes any single national regulator, is usually in bearer form, and pays coupons gross. Foreign bonds are named by *host market* (Yankee, Samurai, Bulldog); eurobonds by *currency* (eurodollar, euroyen).

**A3. Does "eurobond" mean a bond denominated in euros?**
No. "Euro" here means *offshore*, not the euro currency. A USD bond sold offshore in London is a eurodollar bond; a yen bond sold offshore is a euroyen bond. The euro currency is irrelevant to the term.

**A4. Name the host market and currency for: Yankee, Samurai, Bulldog, Kangaroo, Maple, Panda.**
Yankee = USA/USD; Samurai = Japan/JPY; Bulldog = UK/GBP; Kangaroo (Matilda) = Australia/AUD; Maple = Canada/CAD; Panda = China onshore/CNY (its offshore cousin is the Dim sum bond in CNH).

**A5. Why does the euromarket exist historically?**
Regulatory arbitrage. In the 1960s US rules — Regulation Q interest-rate caps and the Interest Equalization Tax — made raising/holding dollars *inside* the US unattractive. Dollars held in European banks ("eurodollars") could be lent free of those rules. London became the hub of a lightly regulated, bearer-form, withholding-free offshore market. The original arbitrage faded, but English-law standardisation, efficiency, and a global investor base made the market permanent.

**A6. Write the home-currency return decomposition and identify the cross-term.**
$1+R_{home}=(1+R_{local})(1+R_{FX})$, which expands to $R_{home}=R_{local}+R_{FX}+R_{local}\times R_{FX}$. The cross-term $R_{local}\times R_{FX}$ is negligible for small moves but material in EM where both numbers can be large.

**A7. State CIP and explain why hedging destroys the yield pick-up.**
Covered interest rate parity: $F_0=S_0(1+i_{HC})/(1+i_{FC})$. If the foreign rate is higher, $F_0<S_0$ — the high-yield currency trades at a *forward discount*. Hedging means selling the foreign currency forward at $F_0$, locking in that discount. The unfavourable forward rate exactly offsets the higher coupon, so what survives is the bond's *spread and duration*, not its raw yield. You cannot hedge the currency **and** keep the pick-up — that would be arbitrage.

**A8. Contrast CIP and UIP.**
CIP is an *arbitrage identity* that holds (forward = spot × rate ratio) enforced by no-arbitrage. UIP is an *expectations theory*: the market *expects* the high-yield currency to depreciate by exactly the rate differential, $E[R_{FX}]\approx-(i_{FC}-i_{HC})$. UIP empirically fails at short horizons — high-yield currencies do not depreciate as much as predicted — which is the source of FX carry-trade profits (and their periodic crashes).

**A9. Distinguish hard-currency from local-currency EM debt across five dimensions.**
Currency: USD/EUR vs issuer's own. Primary risk: sovereign credit/default vs currency+local rates. Governing law: New York/English vs local. Can the sovereign print its way out? No (the killer feature) vs Yes (inflate/devalue). Benchmark: JPMorgan EMBI vs GBI-EM. Default mode: outright default/restructuring vs erosion by devaluation.

**A10. What is "original sin"?**
An emerging economy's inability to borrow abroad in its own currency. Global investors will lend in dollars but not in size in local currency, forcing the sovereign into hard-currency debt — exactly the debt it *cannot* print its way out of. This is the root cause of EM default crises.

**A11. Why is a sovereign's local-currency rating higher than its foreign-currency rating?**
A government can always print its own money to service local-currency debt, so default risk there is low. It can never print dollars or euros, so foreign-currency debt genuinely can — and does — default. Ability to pay is unconditional in local currency but constrained by reserves in hard currency.

**A12. Write the spread-to-default relationship and state whether the resulting probability is real-world.**
$\text{Spread}\approx p\times(1-R)=p\times\text{LGD}$, so $p\approx\text{Spread}/\text{LGD}$. The result is a *risk-neutral* probability: it embeds a risk premium and therefore *overstates* the true real-world default probability. The gap is the sovereign risk premium the investor is paid to bear.

**A13. Distinguish ability to pay from willingness to pay.**
Ability to pay is economic — reserves, growth, debt/GDP, access to hard currency. Willingness to pay is political and legal — a sovereign may *choose* to default even when it could pay (there is no bankruptcy court to force a country). Sovereign credit blends both; corporate credit is mostly about ability.

**A14. What are EMBI and GBI-EM?**
JPMorgan benchmark indices: the EMBI (Global) tracks *hard-currency* EM sovereign debt; the GBI-EM tracks *local-currency* EM government debt. Different indices signal that these are two distinct asset classes with different risk drivers.

---

## Section B — Numerical / Applied

**B1. CIP forward rate.** Spot $S_0=0.2000$ USD/BRL, US 1-yr rate 4%, Brazil 1-yr rate 11%. Find the 1-year forward and the forward discount on the BRL.

*Solution.* $F_0=0.2000\times\dfrac{1.04}{1.11}=0.2000\times0.936937=0.187387$ USD/BRL.
Forward discount $=\dfrac{0.187387}{0.2000}-1=-6.31\%$, close to the $-(11\%-4\%)=-7\%$ rate differential (the difference is the exact-vs-approximate/compounding gap). The high-yield currency trades at a forward discount.

**B2. Hedged return.** Same data, and the BRL note returns 11% locally (bought at par, held one year, price flat). Invest \$1,000 fully hedged. What USD return results?

*Solution.* Convert: $1{,}000/0.2000=5{,}000$ BRL. Grow at 11%: $5{,}000\times1.11=5{,}550$ BRL. Convert back at the forward $0.187387$: $5{,}550\times0.187387=1{,}040.00$ USD → **+4.00%**. This equals the US risk-free rate exactly: CIP cancelled the 7% pick-up. If the note carried a +2% spread over the Brazilian risk-free rate, the hedged return would be roughly 6%.

**B3. Unhedged, currency falls.** Same 5,550 BRL at year-end; spot moves to $S_1=0.1800$ (BRL −10%). USD return?

*Solution.* $5{,}550\times0.1800=999.00$ USD → **−0.10%**. Check: $R_{FX}=0.18/0.20-1=-10\%$; $(1.11)(0.90)=0.999$ → −0.10%. Decomposition: local +11%, FX −10%, cross-term $0.11\times-0.10=-1.1\%$; sum = −0.1%. The fat coupon was more than wiped out by the currency loss.

**B4. Unhedged, currency rises.** Same position; spot moves to $S_1=0.2100$ (BRL +5%). USD return?

*Solution.* $(1.11)(1.05)=1.1655$ → **+16.55%**. Now the unhedged investor collects coupon *plus* currency gain — the upside of being long the bond and long the BRL. Contrast B2/B3/B4: hedging locked +4%; unhedged ranged from −0.1% to +16.55% depending purely on the exchange rate.

**B5. Implied default probability.** A 5-yr USD sovereign eurobond yields 9.5%; the 5-yr Treasury yields 4.0%; assume recovery 40% (LGD 60%). Find the annual and cumulative 5-year implied default probability.

*Solution.* Spread $=9.5\%-4.0\%=5.5\%=550$ bps. Annual $p\approx0.055/0.60=9.17\%$. Cumulative survival (constant hazard) $=(1-0.0917)^5=(0.9083)^5=0.6182$, so 5-yr cumulative default $\approx1-0.6182=38.2\%$. This is a risk-neutral probability, so it overstates true odds; a ~9% annual figure is consistent with a low-BB/high-B rating.

**B6. Recovery sensitivity.** Same 550 bps spread but assume harsher 25% recovery (LGD 75%). What annual $p$ now?

*Solution.* $p\approx0.055/0.75=7.33\%$ — *lower* than in B5 for the same spread, because each default now costs more (higher LGD). Lesson: recovery and default probability trade off for a given observed spread; you cannot pin one without assuming the other.

**B7. Dollar-investor loss on a devaluing local-currency bond.** Country Y's 1-yr local bond pays a 10% coupon; over the year the currency devalues 25% vs the dollar and the government does *not* default. What is the dollar holder's return, and is it a default?

*Solution.* $R_{FX}=-25\%$; $(1.10)(0.75)=0.825$ → **−17.5%**. A large loss but *not* a legal default — no missed payment, no restructuring. The loss arrived through inflation and FX, not a credit event.

**B8. Cross-term materiality.** Compare the approximation $R_{home}\approx R_{local}+R_{FX}$ with the exact figure when $R_{local}=20\%$ and $R_{FX}=-20\%$.

*Solution.* Approximation: $20\%-20\%=0\%$. Exact: $(1.20)(0.80)=0.96$ → **−4.0%**. The cross-term $0.20\times-0.20=-4\%$ is the entire difference. At EM-scale moves the simple sum is badly misleading; always compound.

**B9. Back out the recovery.** A sovereign USD bond trades at a 700 bps spread and the market believes the annual default probability is 14%. What recovery rate is implied?

*Solution.* $\text{Spread}=p\times\text{LGD}\Rightarrow\text{LGD}=0.07/0.14=0.50$, so recovery $R=1-\text{LGD}=50\%$. Confirms the three quantities — spread, $p$, recovery — are mutually determined; fix any two and the third follows.

**B10. Hedged return with a spread.** A foreign 1-yr bond yields $R_{local}=8\%$; foreign risk-free 6%, home risk-free 4%. Estimate the hedged return using the approximation.

*Solution.* $R_{hedged}\approx R_{local}-(i_{FC}-i_{HC})=8\%-(6\%-4\%)=6\%$. Equivalently, home rate 4% plus the bond's 2% spread over the foreign risk-free (8%−6%). Hedging keeps the *spread over the local risk-free*, not the absolute yield.

---

## Section C — Interview-Style

**C1. "Why doesn't hedging a 12% Brazilian bond leave me with 12%?"**
Because CIP forces the BRL to trade at a forward discount roughly equal to the rate gap. To hedge, I sell BRL forward at that discounted rate, which hands back the yield pick-up. I'm left with approximately my home risk-free rate plus whatever *spread* the bond earns over the Brazilian risk-free rate — not the headline 12%. Keeping both the hedge and the pick-up would be a pure arbitrage that CIP rules out (bar a small cross-currency basis).

**C2. "What's the difference between hard- and local-currency EM debt, and why does it matter for a portfolio?"**
Hard-currency debt (USD/EUR) is a *credit* bet: the sovereign can't print the currency, so it can genuinely default — that's original sin, benchmark EMBI. Local-currency debt is a *rates-plus-FX* bet: the sovereign rarely defaults but inflates/devalues instead, benchmark GBI-EM. They have different risk drivers, different investor bases, and low correlation — so a portfolio can be long one and short the other, and you must size and hedge them separately.

**C3. "Sovereigns print their own money — so how can they default?"**
They can always print *local* currency, so local-currency default is rare. But they cannot print dollars or euros. Hard-currency debt must be serviced from reserves or export earnings; when those run dry, the sovereign misses a coupon and defaults legally — Argentina, Russia 1998, Sri Lanka 2022, Ghana, Zambia. That's precisely why foreign-currency ratings sit below local-currency ratings for the same issuer.

**C4. "Local-currency EM debt never defaults — so it's safe, right?"**
It rarely *defaults*, but that's not the same as safe. Losses arrive through devaluation and inflation instead. A 25% currency crash costs a dollar investor about as much as a moderate default haircut — it just isn't labelled "default." The risk didn't disappear; it changed channels from credit to currency.

**C5. "How do you extract a market-implied default probability, and what's the catch?"**
Take the sovereign spread over the matched-maturity Treasury and divide by LGD: $p\approx\text{spread}/(1-\text{recovery})$. The catch is threefold: it's a *risk-neutral* probability that overstates real-world odds because it embeds a risk premium; it's only as good as your recovery assumption (which trades off directly against $p$); and the single-period formula ignores term structure of hazard. Useful for relative value, not a literal forecast.

**C6. "When would you deliberately leave EM currency exposure unhedged?"**
When I have a positive view on the currency and want the full carry, and can tolerate the volatility — or, more precisely, when I believe hedging costs (the rate differential CIP makes me give up) exceed the currency's *expected* depreciation. That's a bet that UIP fails in my favour: the high-yield currency won't fall as much as the forward implies. If I only want the diversification benefit of foreign *rates* without FX noise, I hedge instead.

**C7. "Explain 'original sin' and its consequence."**
It's an EM economy's inability to borrow abroad in its own currency because foreign lenders won't take the currency risk in size. It forces the sovereign to issue hard-currency debt — the one kind it cannot inflate or print away. The consequence is that EM crises become *default* crises rather than mere inflation episodes, because the government's ultimate escape valve (the printing press) doesn't work on dollar liabilities.

**C8. "Why does a global bond allocation help a domestic fixed-income portfolio, and what's the hidden cost?"**
Rate cycles are imperfectly correlated across countries — different central banks ease and tighten at different times — so foreign bonds lower portfolio volatility, and EM adds a growth-and-risk yield premium. The hidden cost is that unhedged foreign bonds import currency risk, which is not zero-mean over relevant horizons and adds volatility. Many global mandates therefore hedge FX back to the base currency to capture the *rates* diversification without the FX noise, and treat any unhedged currency exposure as a separate, conscious position.

---

## Section D — Multiple Choice (with reasoning)

**D1.** A eurodollar bond is best described as:
A) A bond denominated in euros sold in the US
B) A USD bond issued offshore, outside any single national regulator
C) A US Treasury sold to European investors
D) A bond paying coupons in both euros and dollars

**Answer: B.** "Euro" means offshore, not the euro currency. A eurodollar bond is a USD-denominated bond issued in the international market outside US regulation, typically bearer form, coupons paid gross. A is the classic trap.

**D2.** A Brazilian company sells SEC-registered USD bonds in the US. This is a:
A) Eurodollar bond  B) Samurai bond  C) Yankee bond  D) Panda bond

**Answer: C.** A foreign issuer selling into the US domestic market in USD under US rules is a Yankee bond. If it were sold *offshore* in USD it would be a eurodollar bond; foreign bonds are named by host market, eurobonds by currency.

**D3.** A US investor holds a foreign bond that returned +6% locally while the foreign currency fell 8%. The home-currency return is closest to:
A) −2.0%  B) −2.5%  C) +6.0%  D) −14%

**Answer: B.** $(1.06)(0.92)=0.9752$ → −2.48% ≈ −2.5%. The simple sum (−2%) omits the cross-term $0.06\times-0.08=-0.48\%$; at this scale it's the difference between A and the correct B.

**D4.** Under CIP, if the foreign interest rate exceeds the home rate, the foreign currency's forward rate (home per foreign) is:
A) Above spot (forward premium)  B) Equal to spot  C) Below spot (forward discount)  D) Undefined

**Answer: C.** $F_0=S_0(1+i_{HC})/(1+i_{FC})$; with $i_{FC}>i_{HC}$ the ratio is <1, so $F_0<S_0$ — a forward discount. Selling the high-yield currency forward at this discount is exactly what erases the hedged carry.

**D5.** A fully hedged foreign bond position primarily retains exposure to:
A) The foreign currency  B) The interest-rate differential  C) The bond's spread and duration  D) Nothing — it earns zero

**Answer: C.** Hedging with an FX forward neutralises the currency and, via CIP, surrenders the rate differential, but the bond's credit *spread* over the local risk-free and its *duration* survive. It behaves like a home-currency spread/duration instrument (plus any small cross-currency basis).

**D6.** A 5-yr USD sovereign bond has a 600 bps spread over Treasuries; assumed recovery is 25%. The implied annual default probability is closest to:
A) 6.0%  B) 8.0%  C) 24%  D) 1.5%

**Answer: B.** LGD $=1-0.25=0.75$; $p\approx0.06/0.75=8.0\%$. Choice A wrongly divides by 1 (ignores LGD); C confuses spread/LGD roles.

**D7.** Which statement about UIP is correct?
A) It is a no-arbitrage identity that always holds
B) It says forward = spot × rate ratio
C) It predicts high-yield currencies depreciate by the rate differential, and empirically fails short-term
D) It is enforced by FX forwards

**Answer: C.** UIP is an *expectations* theory, not an identity (that's CIP, described in B). It predicts $E[R_{FX}]\approx-(i_{FC}-i_{HC})$ but fails at short horizons — the failure is what makes the carry trade profitable.

**D8.** Rating agencies typically assign a sovereign's local-currency debt a *higher* rating than its foreign-currency debt because:
A) Local debt has shorter maturities
B) The government can always print its own currency but not foreign currency
C) Local debt is collateralised
D) Foreign debt has lower recovery by law

**Answer: B.** The government's unconditional ability to print local money makes local-currency default rare; it cannot print dollars/euros, so foreign-currency debt carries genuine default risk and a lower rating. This is the ratings expression of original sin.

**D9.** A sovereign faces a crisis. Its local-currency bondholders are most likely to suffer through ______, while its USD bondholders suffer through ______.
A) Default; inflation  B) Inflation/devaluation; outright default and restructuring  C) Both through outright default  D) Both through devaluation

**Answer: B.** Same sovereign, same crisis, two different loss channels: local-currency holders lose via inflation and FX devaluation (usually no default event); USD holders face legal default, litigation under New York law, and a haircut.

**D10.** Which pairing of asset class and benchmark index is correct?
A) Local-currency EM debt → EMBI Global
B) Hard-currency EM debt → GBI-EM
C) Hard-currency EM debt → EMBI Global; local-currency EM debt → GBI-EM
D) Both use the same index

**Answer: C.** JPMorgan's EMBI Global tracks hard-currency (USD/EUR) EM sovereigns; the GBI-EM tracks local-currency EM government debt. Distinct indices for distinct asset classes with distinct risk drivers.

**D11.** The FX carry trade earns money primarily when:
A) CIP is violated  B) UIP holds exactly  C) UIP fails and high-yield currencies don't depreciate as much as implied  D) Both currencies are hedged

**Answer: C.** Borrowing a low-yield currency to invest in a high-yield one profits precisely when UIP fails — the high-yield currency doesn't fall by the full rate differential. CIP (A) is an arbitrage identity that generally holds; if UIP held exactly (B), expected carry profit would be zero.

**D12.** An investor wants the diversification benefit of foreign interest-rate cycles without importing exchange-rate volatility. The appropriate action is to:
A) Buy unhedged local-currency EM debt
B) Hedge the currency back to the base currency, isolating rates and spread
C) Buy only domestic bonds
D) Short the foreign currency and the bond

**Answer: B.** Currency-hedging back to base currency strips out FX noise while retaining the foreign bond's rates/spread exposure — the diversification objective. Unhedged EM (A) adds exactly the FX volatility they want to avoid.

---

## Self-Verification Notes

B1–B4 reproduce Example 1 (forward 0.187387; hedged +4.00%; unhedged −0.10% and +16.55%). B5–B6 match Example 2 ($p\approx9.17\%$, ~38.2% cumulative; 7.33% at 25% recovery). B7 matches Example 3 (−17.5%, non-default). B8–B10 and MCQ arithmetic (D3: 0.9752; D6: 0.08) independently re-checked.
