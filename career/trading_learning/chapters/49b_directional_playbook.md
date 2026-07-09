# The Directional Trading Playbook — Expressing a View with Discipline

Almost every trader begins with a directional opinion. You look at a chart, read the news, feel the tape, and you form a view: *Nifty is going up*, or *Nifty is going down*. The directional bet is the most natural trade in the world — and, paradoxically, the most common way retail traders lose money. The reason is brutal and worth stating up front: **being right about direction is not enough.** You can call the move correctly and still lose, because an option is a bet on *direction, distance, speed, and volatility all at once*. This chapter is the bridge between knowing the four basic positions (Chapters 11–14) and trading them like a professional. It is the playbook for turning a view into a trade that survives contact with the market.

A directional trade has exactly one job: to make money when the underlying moves the way you expect, while losing a small, known amount when it does not. Everything that follows — strike, structure, expiry, size, and exit — is in service of that single job. Get the *view* right and the *trade construction* wrong, and you will join the majority who "knew it would fall" and still finished red.

## The five ways to bet direction

There is no single "bullish trade" or "bearish trade." There are at least five, and choosing among them *is* the skill. Here is the full menu, with the trade-offs that decide which one fits.

| Structure | Direction | Max loss | Max profit | Cost | Hurt by theta? | Hurt by IV drop? | Best when |
|---|---|---|---|---|---|---|---|
| **Long Call** | Bullish | Premium | Large/open-ended | Pay debit | **Yes (badly)** | Yes | Strong, fast up-move expected; IV cheap |
| **Long Put** | Bearish | Premium | Large (to zero) | Pay debit | **Yes (badly)** | Yes | Strong, fast down-move expected; IV cheap |
| **Short Put** | Bullish | Large (to zero) | Premium | Receive credit | No (helps you) | No (helps) | Mildly bullish / sideways-up; IV rich |
| **Short Call** | Bearish | Unlimited | Premium | Receive credit | No (helps) | No (helps) | Mildly bearish / sideways-down; IV rich |
| **Debit Vertical** (bull-call / bear-put spread) | Bullish / Bearish | Net debit | Capped (width − debit) | Pay (reduced) debit | Muted | Muted | A directional view with defined risk *and* tamed theta |
| **Futures** | Either | Large (symmetric) | Large (symmetric) | SPAN margin | **No theta at all** | No | Pure direction, multi-day, you can watch the stop |

Read that table until it is second nature, because it encodes the three questions that pick your weapon:

1. **How strong and fast is the move?** A big, quick move rewards a *bought* option (long call/put). A slow grind or a "probably won't fall much" view rewards a *sold* option or a *spread*.
2. **What is volatility doing?** When implied volatility is **cheap** (low IV Rank), options are on sale — *buying* is favoured. When IV is **rich**, you are paid to *sell* premium. Buying expensive options and watching IV deflate is one of the quietest ways to lose while being right on direction.
3. **How much defined risk do you need?** A naked bought option already has defined risk (the premium). A sold option does not — and that is where spreads earn their keep.

## The single most important idea: direction is necessary, not sufficient

Picture the classic trap. Nifty is at 24,000. You are convinced it falls. You buy the 24,000 weekly put for ₹120 on expiry-eve. The next day Nifty drifts down to 23,950 — *you were right* — and your put is worth ₹95. **You called the direction and lost money.** Why? Because the 50-point drop did not cover the time decay (theta) that ate the option overnight, and the move was too small and too slow.

This is the lesson that separates beginners from professionals. An option buyer is not just betting on *direction*; they are betting that the move will be **big enough and fast enough** to outrun decay, and that **volatility will not collapse** beneath them. Three things must go right, not one. Internalise this and you will stop buying cheap-looking far-expiry-eve options and calling it a "view."

## Strike selection — the delta map

Once you have chosen to *buy* a directional option, the next decision is *which strike*. The cleanest way to think about it is through **delta** (Chapter 22), which does triple duty: it is roughly the **probability** the option finishes in-the-money, the **rate** at which the option gains per point of underlying move, and a proxy for **how much premium is "real" (intrinsic) versus "hope" (time value)**.

- **Deep ITM (delta ≈ 0.70–0.85).** Behaves almost like the future. High cost, but most of the premium is intrinsic, so **little is at risk to theta**. Highest probability, lowest leverage. Choose this when you have **strong conviction** and want the option to *track* the move reliably without bleeding.
- **ATM (delta ≈ 0.50).** The balanced choice and the most *gamma*-rich — it accelerates fastest as the move develops. Maximum time value, so **maximum theta risk**. The default for a clear directional view with a near-term catalyst.
- **OTM (delta ≈ 0.20–0.35).** Cheap, all hope, all time value. Big percentage payoff *if* the move is large and quick, but it expires worthless far more often than buyers expect. This is a **lottery ticket**, correct only for a genuine "explosive move soon" thesis — not for a routine directional lean.

A useful rule of thumb: **the weaker your conviction or the slower your expected move, the more ITM you should buy** (so theta and probability work less against you); **the more explosive and imminent the move, the further OTM you can justify.** Most disciplined directional buyers live around **ATM to slightly-ITM (delta 0.5–0.65)** — enough leverage to matter, enough intrinsic value to survive a day of chop.

## The two enemies of the option buyer

A bought directional option fights two headwinds every single day.

**Theta — the rent you pay for time.** Every day you hold a long option, time value drains away, and it drains *fastest in the final week* (Chapter 24). On **expiry day**, an ATM option is almost pure theta — it can lose a third of its value in a few hours of no movement. The implication is sharp: **do not buy a near-expiry option to express a multi-day view.** If your thesis is "Nifty falls over the next three or four sessions," buy a put with two or three *weeks* to expiry, not the one that dies tomorrow. Match the option's life to your thesis's horizon.

**Vega — the volatility you overpaid for.** If you buy options when implied volatility is high (say, right before an event, or during a panic) and IV then collapses, your option loses value *even if the underlying moves your way*. Check **IV Rank** (Chapter 35) before buying: a low rank means options are cheap and buying is sensible; a high rank warns you that you are paying up, and a spread (which sells one leg) or an outright credit structure may be the better expression.

## The decision tree: naked option, spread, or future?

Here is the practical flowchart a professional runs in seconds:

- **Is IV cheap (low rank) AND do you expect a big, fast move?** → **Buy the option outright** (ATM/slightly-ITM). You want maximum exposure to a real move, and cheap premium means theta is small in rupee terms.
- **Is your view directional but moderate, and you want defined risk with tamed theta?** → **Buy a debit vertical** (bull-call spread for up, bear-put spread for down). Selling the further strike pays for part of the premium and *cancels much of the theta and vega* — you give up the far tail of profit you probably would not have captured anyway. This is the **workhorse directional trade** and usually the right answer when in doubt.
- **Is IV rich and your view only mildly directional ("won't fall much")?** → **Sell premium** the other side (a short put for bullish, a bear-call *credit* spread for bearish). Now theta works *for* you.
- **Is this a pure multi-day directional play and you can actively manage a stop?** → **Trade the future.** No theta, no vega, clean delta-1 exposure. The price is symmetric risk and SPAN margin, so it demands a hard stop and disciplined sizing.

Notice the elegance: the *same* bullish view becomes a long call, a bull-call spread, a short put, or a long future depending entirely on **volatility and conviction**. The view is the easy part; the structure is the craft.

## Matching expiry to your horizon (DTE)

- **Intraday / 1-day thesis** → today's or this week's expiry, ATM, and *be out before the close* — you are renting gamma and must pay theta, so speed is everything.
- **2–10 day thesis** → next weekly or the monthly, slightly-ITM, so a day of chop does not gut you.
- **Multi-week / positional** → monthly or next-month, ITM or a vertical, so theta is a gentle drizzle rather than a downpour.

The cardinal sin is the mismatch: a multi-day view expressed through an expiry-day option. You are then betting your *thesis* and *the clock* simultaneously, and the clock is undefeated.

## Entry, target and stop — the directional trade plan

A directional bet without a written plan is a hope, not a trade. Define all three before you enter:

- **Entry / trigger.** Do not buy "because it feels weak." Enter on a *signal*: a break of a clear level (support/resistance), a confirmed pattern, momentum aligning with your higher-timeframe trend. The level you entered against is also your **invalidation**.
- **Target.** Set it on the *underlying*, not the premium. "I'll book if Nifty reaches 23,800" is concrete; "I'll book at some profit" is not. A reasonable first target is the next support/resistance or roughly a **0.5–1× expected-move** distance. On a winner, booking **50–60% of the move** and trailing a runner beats greed, especially near expiry.
- **Stop.** The cleanest stop for a directional option is **a reclaim of the level you entered against** (e.g., "I bought puts because Nifty broke 24,000; if it closes back above 24,000, the breakdown failed and I'm out"). Translate that into a premium loss you can stomach — typically **cut at 30–50% of the premium** if your hard level is hit. Because a bought option already has a defined max loss (the premium), your stop's job is to save *most* of the premium when you are wrong, not to prevent a margin disaster.

## Position sizing for directional bets

Apply the same **1–2% rule** as everywhere else in this book (Chapter 48): the **most you can lose on the trade** — for a bought option, the premium; for a future, the distance to your stop — should be **1–2% of your trading capital**, no more. Directional option buying *feels* cheap ("it's only ₹6,000 for one lot"), which seduces traders into oversizing and into treating each premium as disposable. It is not. A string of "small" full-premium losses on bought options is the single most common equity-curve killer in retail F&O. Size so that **ten losers in a row is an inconvenience, not a catastrophe.**

## A worked example, end to end

Suppose Nifty has been ranging around 24,000 and then, intraday, **breaks below 24,000 support and prints a new low**, while your momentum and pattern signals both flag *sell* and IV Rank is low (≈ 24). Here is the disciplined directional trade, start to finish.

- **View:** bearish continuation — support broke, momentum confirms.
- **Volatility check:** IV is cheap (rank 24), so *buying* is reasonable; no need to sell premium.
- **Structure choice:** conviction is moderate and you want defined risk, so you weigh a **bear-put debit spread** versus an outright **long put**. If your manager or mandate demands a *pure directional* bet, you take the **long put**; if defined risk with tamed theta is allowed, the **bear-put spread** is the cleaner expression.
- **Strike:** buy the **24,000 put** (ATM, at the broken level, delta ≈ 0.55–0.60) — enough delta to track the move, enough intrinsic value to survive chop.
- **Expiry:** if this is a same-session idea, today's expiry and *out before close*; if it is a 2–3 day thesis, step out to the next weekly so theta does not gut you overnight.
- **Entry:** on the break and new low, not before.
- **Target:** the next support — say **23,800**, then a runner toward 23,700.
- **Stop:** a **reclaim of 24,000** (the broken level). If Nifty closes back above 24,000, the breakdown failed; exit and accept ~30–40% of the premium as the cost of being wrong.
- **Size:** premium paid ≤ 1–2% of capital. One lot for a test; scale only with confirmation.

That is a complete directional trade: a view, a volatility check, a structure chosen for the conditions, a strike chosen by delta, an expiry matched to the horizon, and entry/target/stop/size all defined *before* the click. Notice how little of the work is the "view" — the view took ten seconds; the *construction* is the profession.

## Common mistakes (and the fix)

- **Buying expiry-day options for a multi-day view.** *Fix:* match DTE to your horizon.
- **Buying far-OTM "cheap" options as a routine directional bet.** *Fix:* trade ATM/slightly-ITM unless you genuinely expect an explosive, imminent move.
- **Buying options when IV is rich.** *Fix:* check IV Rank; if high, prefer a spread or sell premium.
- **No level-based stop.** *Fix:* enter against a level and let a reclaim of that level be your exit.
- **Oversizing because the premium "feels small."** *Fix:* the premium *is* your risk; size it to 1–2%.
- **Confusing being right on direction with making money.** *Fix:* respect that distance, speed, and volatility must also cooperate — pick structures that do not need all three to be perfect.

## Key takeaways

- A directional view is the *start* of a trade, not the trade. Direction must be paired with the right **structure, strike, expiry, and size**.
- There are **five ways** to bet a direction; **volatility and conviction** decide which one fits. When in doubt, the **debit vertical** is the disciplined workhorse.
- The option buyer's enemies are **theta and vega** — match expiry to your horizon and check **IV Rank** before paying up.
- Select strikes by **delta**: ATM-to-slightly-ITM for most directional bets; OTM only for genuine explosive theses.
- Define **entry, target, stop (a level reclaim), and size (1–2%)** before you enter — every time.
- The view is easy; the construction is the craft. Master the construction and you become the rare trader who makes money *because* they were right, not despite it.
