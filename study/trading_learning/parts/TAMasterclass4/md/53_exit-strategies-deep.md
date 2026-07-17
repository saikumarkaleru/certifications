# Exit Strategies (Deep)

Ask a hundred traders where their edge comes from and ninety-five will describe an entry — a pattern, an indicator cross, a level. Almost none will describe an exit. This is exactly backwards. Your entry determines *whether* you make money; your exit determines *how much.* Two traders can take the identical entry in the identical stock and one finishes the year up 30% while the other is flat — the entire difference is how they got out. The exit is where the money is actually made or lost, and it is the least-practised skill in all of trading. This chapter goes deep on exits: the stop that protects you, the target that pays you, the trail that lets winners breathe, and the psychology that makes exits so much harder than entries.

## The principle: the exit is a system, not a moment

An exit is not a single decision made in a panic when the screen turns red. It is a *pre-built system* with distinct components, each with its own job:

1. **The initial stop** — defines your risk (R) and marks where your thesis is proven wrong.
2. **The stop's evolution** — breakeven moves and trailing that lock in gains as the trade matures.
3. **The profit-taking rule** — how and where you harvest the win, whether fixed targets, partial scaling, or a full trend-trail.
4. **The time stop** — the exit for trades that neither win nor lose but simply die.

The reason exits are so hard is not technical — it's emotional. Losses trigger loss-aversion (we hold losers hoping to avoid crystallising the pain) and winners trigger disposition effect (we sell winners too early to lock in the *feeling* of being right). Left to instinct, the untrained trader does the exact opposite of what makes money: cuts winners short and lets losers run. Every technique in this chapter exists to replace instinct with a pre-committed system, so the decision is made in calm, not in fear.

There is a mathematical truth underneath all of it: **expectancy = (win% x average win) − (loss% x average loss).** Exits control both average win *and* average loss — the two largest levers in that equation. Improving your exits by widening the average win from 1.5R to 2.5R, or tightening the average loss from 1.2R to 0.9R, transforms a break-even system into a profitable one *without changing a single entry.* This is why professionals obsess over exits.

## Component 1 — the initial stop (protection)

The initial stop is sacred: it is the line that says "if price reaches here, I was wrong, and I leave without argument." Its placement is *structural*, not arbitrary. Common valid methods:

- **Structure stop:** below the swing low (for a long) or above the swing high — the price level that, if broken, invalidates your read of the chart.
- **ATR stop:** a multiple of Average True Range (e.g., 1.5–2 x ATR) beyond entry, which adapts to the instrument's volatility. A stop that's fine for HUL (low ATR) is far too tight for Adani Enterprises (high ATR); ATR normalises this.
- **Indicator stop:** below a moving average the trade is riding, or below a Supertrend/PSAR line.
- **Volatility-and-noise buffer:** wherever you place it, add a small buffer so ordinary noise doesn't take you out one tick before the move resumes — but never so much that you exceed 1R.

**The cardinal rules of the initial stop:**

- **Set it before entry, size to it.** The stop distance and your R determine quantity — never the reverse. You do not buy first and find a stop afterward.
- **Never widen it.** Moving a stop further away to "give it room" is the single most destructive habit in trading — it converts a defined 1R loss into an undefined catastrophe. If the price is challenging your stop, the market is telling you the thesis is failing; listen.
- **Honour it mechanically, ideally with a resting order.** A "mental stop" you plan to execute manually becomes, under stress, a hope. On volatile Indian F&O names and around news, a resting stop-loss order is far safer — though be aware that on a gap it fills at the open, not your level.
- **Account for gaps.** Overnight and event gaps (RBI, Budget, earnings, global cues) can jump straight through your stop. If you cannot survive a gap through the stop, reduce size or don't hold through the event.

## Component 2 — evolving the stop (breakeven & trailing)

Once a trade moves in your favour, the stop should evolve from *protecting capital* to *protecting profit.*

**The breakeven move:** after the trade travels a meaningful distance in your favour — commonly ~1R, or after a clear impulse leg confirms — move the stop to your entry (plus costs). Now the trade is "free": the worst case is a scratch. This is psychologically powerful and financially sound, but beware the trap of moving to breakeven *too early*: in a normal, healthy pullback the stock will often dip back toward entry before continuing, and a premature breakeven stop gets you scratched out of a winner. Give the trade room to breathe *before* you tighten. A good rule: only move to breakeven after price has cleared the pullback zone, not the instant you're green.

**Trailing methods** (choose one that matches the setup, per the setup-management chapter):

| Method | How it works | Best for | Trade-off |
|---|---|---|---|
| Swing-low trail | Move stop under each new higher-low | Trending swing trades | Loose; gives room but gives back more |
| Moving-average trail | Exit on close below 20/50-EMA | Steady trends | Simple; whipsaws in choppy trends |
| ATR / chandelier | Stop = highest high − 3 x ATR | Volatile trends | Adapts to volatility; can be wide |
| Parabolic SAR / Supertrend | Indicator flips | Fast momentum | Reactive; whipsaws in ranges |
| Structure trail | Under each confirmed pattern/level | Discretionary trend riding | Requires judgement |

The universal tension in trailing: **tight trails lock in more of each move but get shaken out early; loose trails ride the big trends but give back more at the top.** There is no free lunch. Match the trail to the setup — fat-tail momentum trades need *loose* trails to catch the whole move; steady grinders can use tighter ones. And never trail *toward* the price faster than the trend is moving — a trail is dragged behind the trade, never pushed into it.

## Component 3 — taking profit (harvest)

There are three archetypes, and mature traders often blend them.

**A) Fixed target (all-out).** Exit the entire position at a pre-defined level — a measured-move projection, a Fibonacci extension, the next major resistance, or a fixed R multiple. *Pros:* clean, decisive, high win-feel, removes management stress. *Cons:* caps the runner — you will repeatedly watch trades you exited at 2R go to 6R. Best for range-bound tapes, mean-reversion trades, and traders who value simplicity and a smooth equity curve.

**B) Scale-out (partials).** Take portions at successive targets — e.g., a third at 1.5R, a third at the next resistance, a third trailed for a trend. *Pros:* books certainty *and* keeps a runner; psychologically sustainable because you're "right" early and still exposed to a big move; moving the remainder's stop to breakeven after the first partial makes the whole trade risk-free. *Cons:* mathematically, scaling out *reduces* your average win versus letting it all run in a strong trend (you sold your best shares first). It optimises the *emotional* experience and smooths returns more than it maximises expectancy. For most discretionary traders that trade-off is worth it, because a sustainable process beats a theoretically optimal one you can't execute.

**C) Trend-trail (all-in, ride to the end).** No fixed target; hold the full position behind a trailing stop until the trend breaks. *Pros:* captures the fat tail — the occasional 5R+ runner that pays for many small losses; mathematically optimal for genuine trend-following. *Cons:* brutal to hold emotionally — you *will* give back a chunk from the peak on every trade, and most winners will reverse and stop you out below the high. Low win-feel, high dependence on rare big winners. Best for breakout and momentum setups where the payoff is a fat tail.

**A concrete blended template** many Indian swing traders use: enter 1R risk; at ~1.5–2R sell a third and move stop to breakeven (trade now risk-free); at the next major level sell another third; trail the final third under swing lows for a possible trend run. This banks partial profit, removes risk, and preserves upside — a pragmatic compromise between the mathematics and the psychology.

## Component 4 — the time stop (the exit for dead trades)

Not every trade wins or loses — many just *sit there.* A time stop exits positions that fail to perform within an expected window, freeing capital and attention (and reducing exposure to random news). If you took a breakout expecting momentum and three sessions later it's chopping sideways at entry, the thesis (immediate momentum) has quietly failed even though your price stop wasn't hit. Exit near breakeven and redeploy. Time stops are especially valuable in options, where *theta* bleeds your premium every day the underlying doesn't move — a long option that hasn't worked in two or three sessions is often best cut before decay compounds. Rule of thumb: define, at entry, "by when should this be working?" — and if that time passes with no progress, leave.

## Worked example: four exits, one entry

Reliance breaks out of a Rs 2,900–2,980 base, closing at Rs 2,995 on strong volume in 2026. Entry Rs 2,995, structure stop Rs 2,930 (below the base) — Rs 65 risk = 1R. Four traders, same entry:

- **Trader A (fixed target):** sets a target at Rs 3,125 (2R, the measured move of the base). Price hits it in five sessions; A exits fully, +2R. Clean. But Reliance continues to Rs 3,340 over the next month — A watches 5.3R walk away.
- **Trader B (scale-out):** sells a third at Rs 3,125 (2R), moves stop to Rs 2,995 (breakeven). Sells another third at Rs 3,240 (~3.8R) at the prior high. Trails the last third under swing lows; exits at Rs 3,300 (~4.7R) when a swing low breaks. Blended ≈ (2 + 3.8 + 4.7)/3 ≈ **3.5R**, with risk removed early. Sustainable and strong.
- **Trader C (trend-trail):** no target, trails under daily swing lows. Rides the full position from Rs 2,995 to a peak of Rs 3,360, gives back to the swing-low exit at Rs 3,300 — **≈4.7R** on the *entire* position. Mathematically the best result here — but C had to sit through two scary pullbacks and give back Rs 60 from the peak, which most traders cannot stomach.
- **Trader D (no system):** takes profit at Rs 3,040 (~0.7R) the moment the trade is green, because "a bird in hand" — then re-enters higher at Rs 3,180 chasing, gets stopped on a pullback for −1R. Net ≈ **−0.3R** on a move that paid the disciplined traders 2–5R. This is what instinct does.

The entry was identical for all four. The *exit system* produced outcomes ranging from −0.3R to +4.7R on the same price move. That is the entire thesis of this chapter.

## Building it into your routine

**Write the full exit plan before entry.** On every trade, pre-record: initial stop (price + R), breakeven-move trigger, trailing method, profit-taking rule and levels, and time stop. The exit system must exist *before* the emotion of an open position exists.

**Automate what you can.** Resting stop-loss orders and, where the broker supports it, target/GTT orders remove the moment-of-truth hesitation. The best exit is one you don't have to summon willpower to execute.

**Separate the decision from the screen.** Watching every tick corrodes exit discipline — you'll feel every wiggle and act on noise. For swing trades, manage on closes, not ticks. Set your orders and step back.

**Journal the *exit*, not just the entry.** For every closed trade, record: did I follow the exit plan? What would each of the three archetypes have yielded? Over months this reveals whether you're chronically cutting winners early (disposition effect) or holding losers past the stop (loss aversion) — the two failures the whole system exists to fix.

**Post-exit rule: no re-grief.** Once you've exited by plan, the trade is over. If it runs further without you, that is the *cost* of your chosen exit style, not a mistake. Chasing a trade you correctly exited is how a good exit becomes a bad re-entry (see Trader D).

## Pitfalls

- **Widening the stop** — the cardinal sin; turns a defined loss into an open-ended one.
- **Moving to breakeven too early** — gets you scratched out of winners on normal pullbacks.
- **Capping every winner at 2R** — starves the fat-tail trades that fund a momentum strategy.
- **Trailing too tight in a volatile trend** — repeated whipsaw-outs just below the eventual continuation.
- **No time stop** — capital and attention rot in dead trades; options bleed theta.
- **Manual "mental" stops under stress** — hope, not a stop; automate.
- **Ignoring gap risk** — stops don't protect against overnight/event gaps; size for it.
- **Re-griefing / revenge re-entry** — chasing a correctly-exited trade, usually at a worse price.

## Interview-ready summary

The exit, not the entry, determines how much you make — two traders with the identical entry can finish a year 30% apart purely on how they got out. A complete exit system has four components: an initial stop placed at structural invalidation and sized to 1R (never widened, ideally a resting order, and sized for gap risk); an evolving stop that moves to breakeven after the trade proves itself and then trails to protect profit; a profit-taking rule matched to the setup — fixed targets for range/mean-reversion trades, trend-trails for fat-tail momentum, and a scale-out blend that banks certainty while keeping a runner for most discretionary trading; and a time stop to cut dead trades that neither win nor lose. Because expectancy depends on average win and average loss — both controlled by exits — mastering exits can turn a break-even system profitable without touching a single entry. The hard part is emotional, so the whole discipline reduces to one rule: build the exit system in calm, before entry, and execute it mechanically, because instinct reliably cuts winners short and lets losers run.
