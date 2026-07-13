# The Options Strategy Encyclopedia — 200 Strategies, and When to Use Each

Most option books give you a dozen strategies and leave you to guess which one fits the morning in
front of you. This encyclopedia does the opposite. It catalogues **200 option strategies** — every
structure a professional desk actually uses on Indian markets, from the single long call to the
pterodactyl — and, for each one, answers the only questions that matter at the moment of the trade:
**what is the idea, when and why do I put it on, how do I build it on Nifty, what are the exact numbers,
and what will hurt me.**

Every payoff diagram, every maximum profit, maximum loss, breakeven and risk:reward ratio in the pages
that follow was **computed by a Black-Scholes pricing engine on Nifty at 24,000** — not typed in by
hand. The premiums carry a realistic index volatility skew; the calendar and diagonal payoffs are valued
with the back-month leg still alive at front-month expiry. So when an entry says a bull call spread risks
164 points to make 136, those numbers are internally consistent with the picture beside them. Multiply
any "points" figure by the lot size (about **75 for Nifty**, **15 for Bank Nifty**) to get rupees per lot.

## How to read every entry

Each strategy is laid out the same way, so you can flip to any one and find what you need in seconds:

- **The idea (intuition)** — the plain-English story of why the structure exists.
- **When & why to use it** — the market conditions that call for it (direction, volatility regime, time
  to expiry, catalyst) and, just as important, when *not* to.
- **How to build it (₹, Nifty)** — the exact legs, with a worked debit/credit in points and rupees.
- **The numbers** — max profit, max loss, breakeven(s), net debit/credit and risk:reward, modelled at
  Nifty 24,000.
- **Greeks & behaviour** — the net delta, theta and vega, so you know what is really driving the P&L.
- **Management & exit** — a concrete target, a stop or adjustment, and when to take it off.
- **Risk note** — the honest danger.

A word on the scary-looking risk:reward numbers you will meet in the income chapters. When an entry sells
a naked put or holds the index against a short call, the engine reports the **theoretical** worst case —
the loss if Nifty fell all the way to zero. That is a real, bounded number, but it is not how the trade
behaves in practice; it is why a cash-secured put can show a risk:reward of 0.01. Read those as a
reminder, not a forecast: **premium selling is not free money.** You survive it by sizing small and
managing early, never by pretending the tail does not exist. The SEBI studies are blunt — roughly nine in
ten retail F&O traders lose money. This encyclopedia is written to put you in the other tenth, and that
starts with respecting risk on every single page.

## The master decision map — choosing a strategy in two questions

Before you reach for any structure, answer two questions: **which way do I think the market goes (or
doesn't)?** and **is implied volatility cheap or rich?** Those two axes select your strategy family. Use
this map as your index into the 200 entries.

### Step 1 — What is your directional view?

- **Strongly directional (you expect a real move):** single long options, debit verticals, backspreads,
  risk reversals, ratio backspreads, diagonals and stock-replacement LEAPS.
- **Mildly directional (a drift, not a thrust):** credit verticals, ratio spreads, broken-wing
  butterflies, jade lizards, covered calls and cash-secured puts, calendars placed off-centre.
- **Neutral / range-bound (you expect it to sit still):** iron condors, iron butterflies, short
  straddles and strangles, calendars and double calendars, the wheel.
- **Neutral but you expect a breakout (range about to snap):** long straddles and strangles, reverse iron
  condors/butterflies, ratio backspreads.
- **You own a portfolio and want to protect it:** protective puts, collars, fences, put-spread collars,
  tail-risk put spreads, index hedge overlays.

### Step 2 — Is implied volatility cheap or rich? (Use IV Rank / India VIX)

- **IV is LOW (IV rank below ~30, calm India VIX):** *be a net buyer of options and time.* Favour long
  calls/puts, debit spreads, backspreads, **long calendars and diagonals** (you buy cheap time value),
  and reverse iron condors. Avoid selling premium for thin credits.
- **IV is HIGH (IV rank above ~50–70, elevated VIX, post-event):** *be a net seller of premium.* Favour
  iron condors, iron butterflies, short strangles, credit spreads, jade lizards and the wheel — you are
  selling expensive insurance and letting it decay. Define your risk with wings.
- **IV is MIDDLING:** lean on structures that are vega-light and live on direction or pin — verticals,
  butterflies, diagonals — rather than betting on volatility itself.

### Putting the two together

|                       | **Low IV (buy options)**                 | **High IV (sell premium)**                  |
|-----------------------|------------------------------------------|---------------------------------------------|
| **Bullish**           | Long call, bull call (debit) spread, call backspread, call diagonal | Bull put (credit) spread, cash-secured put, jade lizard, risk reversal |
| **Bearish**           | Long put, bear put (debit) spread, put backspread, put diagonal | Bear call (credit) spread, covered put, ratio put spread |
| **Neutral / range**   | Long calendar, double calendar, butterfly | Iron condor, iron butterfly, short strangle, the wheel |
| **Expecting breakout**| Long straddle/strangle, reverse iron condor | Ratio backspread (often a credit), bear call/bull put ladder |
| **Protecting a book** | Protective put, married put, tail-risk put spread | Collar, costless collar, fence (sell a call to fund the put) |

### The third axis professionals never forget — time and the catalyst

Direction and volatility choose the *family*; **days to expiry and the event calendar choose the exact
strike and tenor.** A 45-day, 16-delta iron condor managed at half profit is a different animal from a
same-day expiry straddle, even though both are "neutral." Throughout the playbook chapters you will find
strategies tied to specific Indian catalysts — Budget day, RBI policy, single-stock results, weekly and
monthly expiry, an India VIX spike — because the right trade on Tuesday is the wrong trade on expiry
Thursday. When two structures fit your view and your volatility read equally well, let the calendar break
the tie: nearer expiry means faster theta and sharper gamma; further expiry means more vega and more room
to be wrong.

Read the chapters in order once, to build the map in your head. After that, trade from the map: **view,
then volatility, then the calendar** — and turn to the exact entry that matches all three.
