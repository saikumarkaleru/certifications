# The Volatility Skew & How to Trade It

*India F&O desk note — drafted July 2026. STT, SPAN, expiry-structure and lot sizes reflect 2026 as I understand them; verify every figure on NSE/SEBI/your broker before trading.*

## The idea

If Black–Scholes were literally true, every strike on the same expiry would price off the *same* implied volatility. It doesn't. Plot IV against strike and you get a **smile** or, more commonly in equity indices, a downward-sloping **skew**: out-of-the-money (OTM) puts trade at *higher* implied vol than ATM, and OTM calls trade at *lower* IV than ATM. The market charges more for downside protection than for upside lottery tickets. This shape is the volatility skew, and it is one of the richest, most persistent, and most tradeable structural features of the Indian index option market.

**Why the skew exists** is not a quirk — it's economics. Indices *crash down, drift up*. Big adverse moves are downside moves (2008, March 2020, gap-down opens on global risk-off), so the realised distribution has a fat left tail and negative skewness. Everyone who owns equity — mutual funds, PMS, retail portfolios — is naturally *long the underlying* and *wants to buy puts* for protection. That structural demand for downside insurance bids up OTM put IV. Meanwhile, upside is a slower grind, so OTM calls are less demanded (and are often *sold* as covered calls), keeping their IV lower. The result: the put wing is elevated, the call wing depressed.

**When does trading the skew earn its keep?** Three ways an experienced trader monetises it. First, the skew tells you *relative value*: if OTM puts are pricing 18% IV while ATM is 12%, put buyers are paying a steep premium — you might prefer to *sell* that expensive put wing (defined-risk) or express downside via put *spreads* rather than outright puts. Second, the *shape and steepness of the skew itself moves* — it steepens in fear (crash worry) and flattens in complacency — and you can trade the *change* in skew via risk reversals. Third, skew is a **cost input to every structure you build**: a put spread, a collar, a ratio, a broken-wing butterfly — each one's economics depend on which wing is rich and which is cheap. Understanding skew turns strategy selection from guesswork into relative-value arithmetic.

India specifics matter here. The Nifty/Bank Nifty put skew is generally *steep* — persistent institutional hedging demand plus event risk (global cues, policy) keep the left tail bid. On the call side, the *massive* Indian retail appetite for cheap OTM weekly calls (lottery tickets) can, on strong-trend days, actually *bid up* the near-OTM call wing intraday, temporarily flattening or even locally inverting the smile on the call side. So India's skew is "steep put wing, structurally cheap-ish call wing that retail flow occasionally distorts." Read it, don't assume it.

## The mechanics

**Defining the skew precisely.** A common desk metric is the **25-delta risk reversal**: IV(25-delta put) − IV(25-delta call). A positive, large number = steep put skew (puts richer). You can also quote **put-wing slope** (IV difference per unit of strike or per delta) and **skew steepness** relative to its own history (is today's skew rich or cheap vs the last 3 months?). The point of a normalised measure (by delta, not raw strike) is comparability across expiries and vol levels.

**Greeks of skew trades.** The clean skew trade is the **risk reversal**: sell the (expensive) OTM put and buy the (cheap) OTM call, or vice versa. Structurally:

| Structure | What it is | Primary exposure | Vega/skew |
|---|---|---|---|
| Risk reversal (short put / long call) | Sell OTM put, buy OTM call | Long delta (synthetic long-ish) | Short skew — profits if skew *flattens* |
| Risk reversal (long put / short call) | Buy OTM put, sell OTM call | Short delta | Long skew — profits if skew *steepens* |
| Put spread (buy higher, sell lower put) | Debit vertical | Short delta, defined | Sells the steepest part of the wing to fund |
| Ratio put spread | Buy 1 near put, sell 2 further puts | Short delta + short tail vega | Harvests rich far-put IV |
| Broken-wing butterfly | Asymmetric fly | Directional lean, defined | Skips a wing to exploit skew pricing |

The insight: **whenever a structure lets you *sell* the expensive wing and *buy* the cheap wing, the skew is working for you.** A bull put spread (sell higher put, buy lower put) sells into the rich near-put IV — the skew subsidises the trade. A put ratio spread sells the fat far-put wing at extra volume. Conversely, buying an outright OTM put means *paying* the richest IV on the board — expensive protection; often a put *spread* is better value precisely because you sell the even-richer far wing back.

**Margin.** Risk reversals have a *naked short leg* (the sold option) → SPAN margin, and if that short is a put, downside risk is large — treat like a short-vol/directional position with proper SPAN. Vertical spreads (put/call spreads) are **defined-risk** → low SPAN (~width − credit). Ratio spreads have *net short options* → unbounded-ish risk on the extra short → real SPAN and tail exposure. Match margin awareness to which legs are naked.

## Worked trade

**Exploiting the steep Nifty put skew with a bull put spread — selling the rich wing. Date-stamp illustrative; verify VIX, lot (Nifty = 75, verify), premiums, STT.**

Setup: Nifty ≈ **24,000**, moderately constructive view (or neutral-to-mildly-bullish). India VIX = 12. You observe the skew:

| Strike | Type | Delta | Implied Vol | Premium (₹) |
|---|---|---|---|---|
| 24,000 | ATM | ~0.50 | 12.0% | 150 |
| 23,700 | OTM put | ~0.30 | 13.5% | 78 |
| 23,500 | OTM put | ~0.22 | 15.0% | 52 |
| 23,300 | OTM put | ~0.15 | 16.5% | 34 |
| 24,300 | OTM call | ~0.30 | 11.0% | 60 |

Notice the skew: the 23,300 put trades **16.5% IV** vs the same-delta-ish 24,300 call at **11.0%**. Downside insurance is *far* richer. You monetise by **selling the rich put wing, defined-risk**.

**Bull put spread:** Sell 23,700 PE @ ₹78, Buy 23,500 PE @ ₹52.
- Net credit = (78 − 52) × 75 = **₹1,950**.
- Max loss = (200 width − 26 credit) × 75 = **₹13,050**.
- You *sold* 13.5% IV and *bought back* 15.0% IV — you're short the near wing (richer per your view) but the far wing you bought is even richer. The credit exists partly *because* of skew: the near put's elevated IV fattens the premium you collect.
- Greeks: net **short delta** modestly (you're mildly bullish/neutral — profits if Nifty holds above 23,700), **short vega** on the wing, **long theta**, short gamma near the short strike.

**Alternative — the put ratio spread (harvest the fat far wing harder):** Buy 1× 23,700 PE @ ₹78, Sell 2× 23,500 PE @ ₹52.
- Net = −78 + (2×52) = +₹26 credit per share → ₹1,950 credit, but now you're **net short one 23,500 put** → downside tail risk below 23,500, unbounded-ish, real SPAN. You've sold *extra* units of the richest-IV strike. Only for those who can manage the tail; not defined-risk. I show it to illustrate "sell the fat wing at volume," but the bull put spread is the disciplined version.

**Outcome scenarios for the bull put spread:**
- **Nifty at/above 23,700 at expiry:** both puts expire worthless-ish, keep ~full ₹1,950 credit. Return on ₹13,050 risk ≈ 15% for the cycle. The skew handed you a richer credit than a symmetric market would.
- **Nifty at 23,600:** short put ITM by 100, long put OTM. Loss ≈ (100 − 26) × 75 = ₹5,550.
- **Nifty gaps to 23,400:** max loss ≈ **₹13,050**, capped by the long 23,500 put. The wing you bought — even at rich IV — earned its keep as the tail guard.

**Costs:** two option legs; **STT ~0.15% of premium on sells (verify)** applies to the sell-to-open of the 23,700 put and any buy/sell to close; exchange charges + GST + flat brokerage per leg. Budget ~₹100–₹200 all-in; it trims the ₹1,950 credit modestly.

## Management

**The skew trade is managed on two axes: spot (delta) and skew-shape (vega/skew).**

- **Spot drifts up / holds (for you):** the bull put spread decays in your favour — long theta working. Take profit at ~50% of the credit rather than squeezing to expiry (gamma risk near the short strike rises into expiry). Redeploy.
- **Spot falls toward the short strike (against you):** roll the tested short put down-and-out for a credit, or convert to a wider spread, or take the defined loss. Because the structure is defined-risk, you're never forced — you *choose*.
- **Skew steepens (fear rises, VIX up):** your short near-put IV rises (mark-to-market pain on the short leg) but the far put you own also gains — the *spread's* vega is partially self-hedged, which is the beauty of selling a wing via a spread rather than naked. A naked short put would suffer the full skew-steepening; the spread cushions it.
- **Skew flattens (complacency):** favourable to the short-put-wing seller — the rich IV you sold deflates.

**Trading the *change* in skew directly** — the risk reversal. If you forecast the skew will **steepen** (e.g. into a period of rising crash-worry, global risk-off brewing), put on a **long-skew risk reversal**: buy the OTM put, sell the OTM call. As the put wing bids up relative to the call wing, the structure gains *even if spot is unchanged*. Manage it by watching the 25-delta RR metric versus its history: enter when skew is historically *flat* (cheap to get long skew) and exit when it's *steep* (skew has richened). This is a pure relative-value vol trade — delta-hedge it with futures if you want to isolate the skew move from direction.

**Scenarios summary for skew positions:**
- Move for you + skew flattens: best case for a short-put-wing seller.
- Move against + skew steepens: worst case — but defined-risk spread caps it; naked risk reversal does not.
- IV up (parallel, no skew change): affects the *level* not the *shape* — hits net vega; separate from the skew bet.

## Risk & sizing

**Defined-risk skew trades (put spreads, iron structures):** max loss is (width − credit) × lot, known up front — **₹13,050** in the worked spread. Size so a cluster of these all hitting max loss on a correlated gap-down is a drawdown, not a disaster. Because index skew trades are almost always *short the downside wing*, they **all lose together in a crash** — that's the correlation trap. Model the "Nifty gaps −4%" morning: every bull put spread on the book prints toward max loss *simultaneously* while VIX and skew both spike. Cap aggregate short-put-wing exposure accordingly.

**Naked-leg skew trades (risk reversals, ratios):** the short leg carries real, SPAN-margined, potentially large loss — a short-put risk reversal is *synthetically long the index with a fat downside tail*, and in a crash you eat the full steepening plus the directional loss plus SPAN inflation. Size these like the directional/short-vol positions they are, not like "just a skew trade."

**Portfolio Greeks:** track net vega *by strike region* — a book that's quietly short the put wing across many expiries is short the exact thing that blows up in a crash (crash = down move + IV spike + skew steepening, all three hitting the short put wing at once). This triple-whammy is why put-wing sellers look brilliant for months and then have one catastrophic week. Keep a portion of genuinely long far-OTM puts (or long-skew risk reversals) as a tail hedge so the book isn't purely short the crash.

**The tail:** the skew is *steep for a reason* — it's the market's memory of crashes. Selling the put wing harvests a real risk premium, but you are, once again, **selling insurance against the exact event that recurs**. The far-OTM put you keep buying (in a spread) or ignore (naked) is the difference between a bounded bad day and a blow-up.

## Pitfalls & interview-ready summary

**Pitfalls:**
- **Buying outright OTM puts for protection at the richest IV on the board** — you're paying the peak of the skew. A put *spread* (selling the even-richer far wing back) is usually better value.
- **Selling the put wing naked** — you collect the skew premium and the crash-tail risk in full; SPAN inflates as you lose. Use spreads.
- **Confusing skew *level* with skew *shape*** — a parallel IV rise is a vega/level event; a steepening is a shape event. Different trades, different hedges.
- **Assuming India's skew is always textbook** — retail lottery-ticket call buying can distort the call wing on trend days; read the live surface, don't assume.
- **Ignoring the correlation of short-put-wing positions** — they all detonate together in a gap-down. Size for the simultaneous case.
- **Squeezing defined-risk credit spreads to expiry** — the last bit of premium is mostly gamma risk near your short strike. Take ~50% and redeploy.

**Interview-ready summary:** The volatility skew is the persistent pattern where OTM index puts trade at higher implied vol than OTM calls, because indices crash down and everyone wants downside insurance — structural hedging demand bids the put wing. You measure it with the 25-delta risk reversal (IV of 25Δ put minus 25Δ call) and track its steepness versus history. You trade it two ways: (1) **relative value** — build structures that *sell the rich wing and buy the cheap wing*, e.g. a bull put spread that sells the fat near-put IV defined-risk, so the skew subsidises your credit; (2) **skew-shape bets** — risk reversals that profit when the skew steepens or flattens, ideally delta-hedged to isolate the shape. In India the put skew is structurally steep (institutional hedging, event risk) while heavy retail call-buying can distort the call wing. Always prefer defined-risk (spreads) over naked short wings, because every short-put-wing position on the book loses together in a crash — down move, IV spike, and skew steepening all hammer the same leg at once, and the steep skew is exactly the market pricing that recurring tail.
