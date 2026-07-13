# Chapter 2: The Indian F&O Market — NSE, SEBI, the Index Family & Who Trades

Before you ever buy a single option, you need to know the field you are playing on, the referee who makes the rules, the "scoreboards" you are allowed to bet on, and who else is sitting at the table with you. Most beginners skip this and jump straight to "buy a Nifty call." That is like learning to drive by pressing the accelerator without knowing what road you are on, what the traffic rules are, or who the other drivers are. This chapter fixes that. It is the map of the Indian derivatives world.

By the end you will understand the exchange (NSE), the regulator (SEBI), the handful of indices you can actually trade options on, what an index even *is* under the hood, the kinds of people who trade and *why*, and the plumbing — trading hours, lots, and notional value — that turns "I think Nifty goes up" into a real position with real rupees at risk.

## Core concepts

### The exchange: NSE (and a bit of BSE)

An **exchange** is the regulated marketplace where buyers and sellers meet. In India, derivatives trading happens mainly on the **National Stock Exchange (NSE)**, headquartered in Mumbai and launched in the mid-1990s. The older **Bombay Stock Exchange (BSE)**, founded in 1875 (Asia's oldest), also runs a derivatives segment that has grown sharply in recent years.

A few facts worth internalizing, because they shape everything:

- The **F&O segment** ("Futures and Options") is where derivatives trade. A *derivative* is a contract whose value is *derived* from something else — here, the level of an index or the price of a stock.
- By sheer **number of contracts traded**, NSE has in recent years ranked as the **world's largest derivatives exchange**. This is driven overwhelmingly by **index options** — Nifty and Bank Nifty options especially — and by the explosion of short-dated weekly expiries that retail traders love.
- Be careful how you read "largest." It is largest by **contract count**, not by the rupee value of the underlying or by the maturity of the market. A single Nifty option lot is small in notional compared to a US S&P contract, so huge *volume* does not mean the deepest or most institutional market. It mostly reflects an enormous, very active retail base trading tiny, cheap, expiring-this-week options.

Think of NSE as a giant, electronic, screen-based bazaar. There is no trading floor with people shouting; everything is matched by computers on a **price-time priority** basis — the best price gets filled first, and among equal prices, whoever placed the order earliest.

### The regulator: SEBI

The **Securities and Exchange Board of India (SEBI)** is the statutory regulator for India's securities markets — the referee. Established as a statutory body in 1992, SEBI's job is to (1) protect investors, (2) develop the market, and (3) regulate it. For an options trader, SEBI's fingerprints are everywhere:

- It decides **which products** can be listed (e.g., approving — and sometimes pruning — weekly expiries).
- It sets **margin rules** through the framework the clearing corporation enforces (you will meet **SPAN margin** in a later chapter — the system that calculates how much cash you must post to take a risky position).
- It enforces **investor-protection disclosures**. This is why your broker shows that blunt warning: SEBI's own studies found that roughly **9 out of 10 individual F&O traders lose money**, with the average loser losing meaningful sums. That number is not marketing fear; it is a regulator-measured fact, and it should sit at the back of your mind through this entire book.
- It governs **conduct** — insider trading, manipulation, broker behavior, and so on.

Two more pieces of plumbing live behind SEBI. **Clearing corporations** (NSE's is **NSE Clearing**, formerly NSCCL) sit in the middle of every trade as the *central counterparty* — they guarantee that even if the other side defaults, your trade settles. And **depositories** (NSDL, CDSL) hold your securities electronically. You will rarely think about them, but they are why a cash-settled option simply credits or debits rupees to your account at expiry without anyone delivering physical share certificates.

### The index family you can trade

You cannot buy an "option on the whole market." You buy options on specific, well-defined **indices** (and on individual stocks). An **index** is just a single number that summarizes the prices of a basket of stocks — a thermometer for a slice of the market. Here are the ones that matter for an Indian options trader:

- **Nifty 50** — the flagship NSE index: the 50 largest, most liquid companies across sectors (Reliance, HDFC Bank, Infosys, TCS, ICICI Bank, and so on). When the news says "the market was up today," they usually mean Nifty. It is broad, diversified, and the single most-traded options underlying. Picture it around the ~24,000 level.
- **Bank Nifty (Nifty Bank)** — the 12 largest, most liquid banking stocks. It is far more *concentrated* and *volatile* than Nifty because it is a single sector dominated by a few giant banks. Traders love it precisely because it moves fast — big gains and big losses. Picture it around the ~52,000 level.
- **FinNifty (Nifty Financial Services)** — banks *plus* the rest of finance: NBFCs (non-banking finance companies), insurers, housing-finance firms. Broader than Bank Nifty but still finance-focused. Think of it as "Bank Nifty's bigger cousin."
- **Nifty Midcap Select** — a basket of mid-cap companies (the tier below the large caps). It lets traders take a view on the more domestically-driven, higher-beta mid-cap segment.
- **BSE's Sensex and Bankex** — the **Sensex** is BSE's flagship: 30 large companies, the index your parents quote. **Bankex** is BSE's banking index. BSE has aggressively grown options on these, and Sensex weekly options in particular have pulled in big volumes, making BSE a real competitor to NSE in index options.

A crucial point that earns its own chapter later: **index options in India are European-style and cash-settled**. *European* means you can only exercise at expiry, not before. *Cash-settled* means no shares change hands — at expiry the exchange just computes the index level and pays the difference in rupees. **Stock options**, by contrast, are American-style in exercise convention and **physically settled** — if you hold them to expiry in-the-money, you must actually deliver or take delivery of the shares. This single difference (cash vs physical settlement) is why beginners are almost always steered to *index* options first.

### How an index is built: free-float market-cap weighting

If an index is the average of 50 stocks, what kind of average? Not a simple one. India's main indices use **free-float market-capitalization weighting**. Let's unpack that in plain English.

- **Market capitalization** ("market cap") = share price * total number of shares. It is the total rupee value of a company. A company worth ₹15 lakh crore obviously matters more to the economy than one worth ₹50,000 crore.
- **Free float** = only the shares that are *actually available for public trading*. Shares locked up with promoters (founders/owners), the government, or strategic holders are *not* free-floating. If a company is huge but the founder owns 75% of it, only the remaining 25% really trades, so it should carry less weight than its full size suggests.
- **Free-float market cap** = share price * (free-floating shares only). The index weights each company by this number.

Intuition: imagine a class where each student's vote counts in proportion to how much pocket money they actually bring to school each day (not how rich their family is on paper). Companies with more *tradable* value swing the index more.

The mechanics, simplified:

```
Index level = (Sum of free-float market caps of all members / Base market cap) * Base index value
```

The "base" is a historical reference point fixed when the index launched, so the index reads as a clean number (like 24,000) rather than crores of rupees. As member prices move through the day, the numerator changes and the index ticks up or down. An **index committee** periodically *rebalances* — adding rising companies, dropping fallers — so the index keeps reflecting the segment it is meant to represent.

Practical consequence for a trader: in Bank Nifty, the two or three largest banks (e.g., HDFC Bank and ICICI Bank) carry a very large combined weight. So Bank Nifty is really "a few mega-banks plus some passengers." When you trade a Bank Nifty option, you are mostly taking a view on those heavyweights. Knowing the weighting tells you *what actually drives the number you are betting on*.

### Who trades, and why

Markets work because different people want different things. Understanding the cast helps you know who is on the other side of your trade — and they are usually more informed than a new retail trader. Group people first by **motive**:

1. **Hedgers** — they already own (or owe) something and use options to reduce risk, like insurance. A mutual fund holding ₹500 crore of stocks might buy Nifty puts so a crash hurts less. A company expecting a payment might hedge. Hedgers are *willing to pay* premium for protection — they are natural option *buyers* of protection.
2. **Speculators** — they have no underlying exposure; they take a position purely to profit from a view on direction or volatility. Most retail option buyers are speculators. They provide the market its liquidity and its excitement — and they are the group SEBI's loss statistics describe.
3. **Arbitrageurs** — they exploit tiny pricing inconsistencies (e.g., between futures, options, and the cash index) to lock in near-riskless profit. They keep prices *consistent*. If put-call parity (a relationship you will learn) breaks, arbitrageurs pounce and fix it within seconds.
4. **Market makers** — they continuously quote *both* a buy price (bid) and a sell price (ask), earning the small spread between them. They are the shopkeepers who always have inventory. Without them, you could not get filled instantly. They are not betting on direction; they are running a high-volume, risk-managed flow business and hedging constantly.

Now group the *same* people by **who they are** — the labels you'll see in market commentary:

- **FIIs (Foreign Institutional Investors)** — overseas funds. They move large sums and their flows often set the market's tone. "FIIs were net sellers today" is a headline you'll read constantly.
- **DIIs (Domestic Institutional Investors)** — Indian mutual funds, insurers (like LIC), pension funds. In recent years steady DII buying (fed by monthly SIP inflows from retail investors) has often absorbed FII selling.
- **Retail** — individuals like you. Collectively enormous in the options market by volume, but individually small and, per SEBI, mostly loss-making in F&O.
- **Proprietary ("prop") traders** — firms (and increasingly algorithmic/high-frequency shops) trading their *own* capital. Much of the market-making and arbitrage is done by sophisticated prop and HFT players. When you buy a weekly option, the seller is very often one of these professional, well-hedged firms — a sobering thing to remember.

### The structure of the F&O segment: hours and expiries

The Indian equity and F&O markets run on **trading days from Monday to Friday**, excluding exchange holidays. Core timings:

- **Pre-open session:** about 9:00 a.m. to 9:08 a.m. — orders are collected and a single opening price is discovered.
- **Normal trading:** **9:15 a.m. to 3:30 p.m. IST**. This is the window you will live in.
- **Post-close:** a short session after 3:30 for closing-price-based orders.

(The exchange has experimented with extended hours for some derivatives; treat exact timings as "currently roughly this," since SEBI/exchange rules evolve.)

**Expiry** is the heartbeat of options. Every option has an expiry date on which it settles and ceases to exist. Indian index options offer **weekly** and **monthly** expiries. For years each index had its own weekly expiry on a different weekday, creating a "daily expiry" buffet across the week. SEBI has since **rationalized** this — limiting each exchange to fewer weekly-expiry products to curb excessive short-dated speculation. The exact weekday and which indices have weeklies are the kind of detail that *changes by regulation*, so always confirm the current schedule with your broker. The principle to lock in: **shorter-dated options decay faster and are cheaper but riskier**; weekly options are where most retail volume — and most retail losses — concentrate.

### Lots and notional value

You cannot trade 1 unit of Nifty. Derivatives trade in fixed bundles called **lots**. The **lot size** is the number of underlying units in one contract, fixed by the exchange (and revised periodically so the rupee value of a lot stays in a target band).

This matters enormously because it determines **how much money is really riding on your trade** — the **notional value**:

```
Notional value = Index level * Lot size
```

A ₹100 option premium feels tiny, but multiply it by the lot size and you see the real exposure. Lots are why options are *leveraged*: a small premium controls a large notional. Leverage cuts both ways — it is exactly why a "cheap" option can wipe out your capital, and why option *selling* requires posting large margins against potentially large losses. Let's make this concrete.

## Worked example (₹, Nifty/Bank Nifty)

Suppose:

- Nifty 50 is trading at **24,000**.
- The Nifty lot size is **75** units (lot sizes change over time — use this as illustrative).
- You buy **one lot** of a weekly Nifty **24,200 call** (a call gives the right to "buy" the index at 24,200 — you profit if Nifty rises). The premium quoted is **₹100 per unit**.

**Step 1 — Notional value (the real exposure):**

```
Notional = Index level * Lot size = 24,000 * 75 = ₹18,00,000
```

So this one small contract represents control over ₹18 lakh of "Nifty." That is the leverage.

**Step 2 — Cost to buy (your maximum loss as a buyer):**

```
Premium paid = Premium per unit * Lot size = 100 * 75 = ₹7,500
```

You pay ₹7,500. As an option *buyer*, that ₹7,500 is the **most** you can lose — a defined, limited risk. (Plus small costs: brokerage, STT, exchange fees, GST — covered later.)

**Step 3 — Effective leverage:**

```
Leverage ratio = Notional / Premium = 18,00,000 / 7,500 = 240x
```

You are controlling ₹18 lakh of market exposure with ₹7,500. A 1% move in Nifty (₹18,000 of notional) is more than twice your entire premium. That is breathtaking leverage — thrilling on the way up, brutal on the way down.

**Step 4 — A quick payoff sanity check at expiry.** Since index options are European and cash-settled, at expiry the exchange just looks at the Nifty settlement level:

- If Nifty expires at **24,500**: the 24,200 call is worth `24,500 - 24,200 = 300` per unit. Value = `300 * 75 = ₹22,500`. You paid ₹7,500, so profit ≈ `22,500 - 7,500 = ₹15,000` (before costs).
- If Nifty expires at **24,200 or below**: the call is worthless. You lose the full ₹7,500 premium. Nothing is delivered; the contract simply expires.

Now flip the seat. The person who **sold** you that call collected ₹7,500 up front, but in the 24,500 scenario they *pay out* ₹22,500 — a net loss of ₹15,000 on a ₹7,500 credit, and their loss grows without limit the higher Nifty goes. To take that risk, the seller must post **margin** (often tens of thousands of rupees per lot, computed by SPAN). This asymmetry — buyers risk a little for a lot, sellers earn a little while risking a lot — is the central tension of the whole options game, and we will return to it again and again.

## Common mistakes / risk note

- **Mistaking "₹100 premium" for "₹100 risk."** Beginners forget the lot multiplier. Your real outlay and exposure are `premium * lot size`. Always compute notional before clicking buy.
- **Confusing volume with safety.** "NSE is the world's biggest derivatives exchange" gets misread as "so it must be easy money here." The opposite is closer to the truth: that volume is largely retail churning short-dated options against professional, hedged sellers — and ~90% of those retail traders lose money (SEBI). Size of the market says nothing about *your* edge.
- **Ignoring settlement style.** Selling deep in-the-money *stock* options and forgetting they are **physically settled** can land you with an obligation to deliver shares (and a large delivery margin) at expiry. Index options spare you this — another reason to start with indices.
- **Chasing weekly expiries for the "cheap" premium.** Cheap means low probability and fast time-decay. The lottery-ticket feel is exactly what the loss statistics are built on.
- **Forgetting who is on the other side.** Your counterparty is usually a market maker or prop/HFT firm with better data, faster execution, and a hedged book — not an equally-uninformed beginner.
- **Treating lot sizes, tax rates, expiry weekdays, and margins as fixed.** They are set by SEBI and the exchanges and **change**. Always confirm current values before trading.

## Key takeaways

- **NSE** is the dominant Indian derivatives exchange (largest in the world by contract count, driven by index options); **BSE** (Sensex, Bankex) is a fast-growing rival. **SEBI** is the regulator setting the rules, products, margins, and investor protections.
- The tradable index family: **Nifty 50** (broad), **Bank Nifty** (concentrated, volatile), **FinNifty** (broader finance), **Nifty Midcap Select**, plus BSE's **Sensex** and **Bankex**.
- Indices use **free-float market-cap weighting**: bigger *tradable* companies move the number more — so a handful of mega-stocks really drives indices like Bank Nifty.
- **Index options are European and cash-settled**; **stock options are physically settled** — a key reason to start with index options.
- The players sort by motive (**hedgers, speculators, arbitrageurs, market makers**) and identity (**FIIs, DIIs, retail, prop/HFT**). You — retail — are statistically the most likely to lose.
- Trading runs **9:15 a.m.–3:30 p.m. IST**, Mon–Fri, with **weekly and monthly expiries** (recently rationalized by SEBI).
- Options trade in **lots**; **notional = index level * lot size**, which creates large **leverage**. A small premium controls a large notional — the source of both the appeal and the danger.

## Practice problems

1. **(Conceptual)** Explain in one or two sentences why "NSE is the world's largest derivatives exchange" does *not* imply that trading options on NSE is easy or profitable for a retail beginner.
2. **(Conceptual)** A company has a market cap of ₹10,00,000 crore, but its promoters hold 70% of the shares. Roughly what free-float market cap does the index use for it, and why is free-float weighting more sensible than full market-cap weighting?
3. **(Numeric)** Bank Nifty is at 52,000 and the lot size is 30. (a) What is the notional value of one lot? (b) You buy one lot of a call at a premium of ₹400 per unit — what do you pay, and what is your maximum loss?
4. **(Numeric)** Using problem 3's data, compute the effective leverage ratio (notional / premium paid).
5. **(Conceptual)** Match each trader to their primary motive: (i) an HDFC mutual fund buying Nifty puts against its stock holdings; (ii) a college student buying a weekly Nifty call hoping for a 2% rally; (iii) an HFT firm continuously quoting bid and ask on Bank Nifty options; (iv) a desk exploiting a mispricing between Nifty futures and options.
6. **(Numeric + reasoning)** From problem 3, the call buyer pays the premium. At expiry Bank Nifty settles at 53,000 and the strike was 52,200. (a) What is the call worth per unit and in total (lot size 30)? (b) Was the trade profitable, and what does the *seller* of that call experience?

## Solutions

**1.** The "largest" ranking is by *number of contracts traded*, not by depth, sophistication, or trader profitability. That volume is overwhelmingly retail trading cheap, short-dated index options against professional, hedged market-makers and prop/HFT firms. SEBI's own studies show roughly 9 in 10 individual F&O traders lose money. So large volume reflects intense (often loss-making) retail activity — not an easy edge for a newcomer.

**2.** Free float = the non-promoter, publicly tradable portion. With promoters holding 70%, only 30% is free-floating, so free-float market cap ≈ `0.30 * 10,00,000 = ₹3,00,000 crore`. This is more sensible because the index should reflect the value that actually trades and influences prices. Promoter-locked shares don't change hands daily, so counting them would overstate a company's real impact on the market.

**3.** (a) Notional = `52,000 * 30 = ₹15,60,000`. (b) Premium paid = `400 * 30 = ₹12,000`. As a buyer, that ₹12,000 (plus small transaction costs) is your maximum possible loss.

**4.** Leverage = `Notional / Premium = 15,60,000 / 12,000 = 130x`. One lot gives exposure to ₹15.6 lakh of Bank Nifty for ₹12,000 — about 130 times your outlay. A 1% Bank Nifty move (₹15,600 of notional) exceeds your entire premium.

**5.** (i) Hedger — protecting existing holdings with puts (insurance). (ii) Speculator — a pure directional bet with no underlying exposure. (iii) Market maker — quoting both sides to earn the spread, not betting on direction. (iv) Arbitrageur — locking in profit from a pricing inconsistency between related instruments.

**6.** (a) The 52,200 call at a 53,000 settlement is worth `53,000 - 52,200 = 800` per unit; total = `800 * 30 = ₹24,000`. (b) The buyer paid ₹12,000 and receives ₹24,000, so profit ≈ `24,000 - 12,000 = ₹12,000` before costs — profitable. The seller collected ₹12,000 up front but must pay out ₹24,000 at settlement, a net loss of ₹12,000, and (had Bank Nifty risen further) their loss would have kept growing — which is why option sellers must post substantial SPAN margin. The trade is cash-settled, so only rupees change hands; nothing is physically delivered.
