# Vol Term Structure & Calendar Volatility Trades

*India F&O desk note — drafted July 2026. STT, SPAN, expiry-structure and lot sizes reflect 2026 as I understand them; SEBI has moved to fewer weekly expiries per exchange — verify the current expiry calendar and every number on NSE/SEBI/your broker before trading.*

## The idea

Volatility has a **term structure** just like interest rates do. The implied vol of a 3-day option, a 10-day option, a 30-day option, and a 60-day option on the same underlying are generally *different numbers*, and plotting IV against time-to-expiry gives you the vol term-structure curve. Most of the time in calm markets this curve is **upward-sloping (contango)**: near-dated options price *lower* IV than far-dated ones, because over a longer horizon more can happen — more events, more uncertainty, mean-reversion of vol toward a higher long-run level. In stressed markets the curve **inverts (backwardation)**: near-dated IV spikes *above* far-dated, because the fear is *right now* and the market expects vol to subside later.

Trading the term structure means taking positions that profit from the *relationship between* near and far implied vols, and from how that relationship evolves — largely independent of where spot goes. The primary instrument is the **calendar spread** (also called a time spread or horizontal spread): sell a near-dated option and buy a far-dated option at the **same strike**. You are, in essence, **short near-dated vol and long far-dated vol** — short the fast-decaying front, long the slow-decaying back.

**When does this earn its keep in India?** The Indian market is *unusually rich* for term-structure trading because of its **weekly expiry cycle**. You have a very short-dated weekly IV that is enormously sensitive to the *immediate* week's events, sitting in front of monthly IV that reflects a longer horizon. This creates a live, tradeable front-vs-back relationship every single week. Specifically:

- **Selling rich weekly vol against monthly** when the near weekly is pumped by an imminent event (expiry-week gamma demand, an event landing this week) but the event will *pass* — the classic "sell the expensive front, own the calmer back."
- **Owning a calendar into an event that sits in the *back* month** but not the front — you want the far-dated vega to inflate when the event approaches.
- **Playing the post-event term-structure normalisation:** after a big event, the front vol that spiked collapses faster than the back → the curve re-steepens → calendars (long back/short front) benefit.

The deep reason calendars are attractive: **theta decays faster the nearer the expiry** (it's roughly proportional to 1/√time), so the near option you *sold* bleeds premium faster than the far option you *own* — you're net collecting theta — *while* you retain **long vega** in the back month. It's one of the few structures that is simultaneously **positive theta-ish and positive vega**, a combination short strangles (positive theta, negative vega) and long straddles (negative theta, positive vega) can't give you. That's the elegance and the appeal.

Honest caveat: calendars have a **negative-gamma-near-the-front risk** — a *large, fast* move away from the strike hurts, because the near short option you sold can blow through the strike and the structure's P&L profile tent-poles at the strike. Calendars *love* the underlying sitting near the strike and *hate* big fast moves. And the front-vs-back vol relationship can move against you (front spikes relative to back). It is not a free theta machine.

## The mechanics

**Construction of a long calendar (the standard trade):** at the same strike K, **sell the near-expiry option, buy the far-expiry option** — do it with calls or puts (put calendars and call calendars are similar in vega/theta structure; choose the wing that matches your directional lean and skew). Net position is a **debit** (the far option costs more than the near you sold).

**The Greeks — this is the whole trade:**

| Greek | Long calendar (sell near / buy far) | Why |
|---|---|---|
| Vega | **Positive** | Far option has more vega than near; net long vol |
| Theta | **Positive (typically)** | Near option decays faster than far; net collect |
| Gamma | **Negative near the front** | Short the fast-gamma near option |
| Delta | ~0 at ATM strike | Roughly neutral if struck ATM |

**The key sensitivities:**
- **Term-structure steepening (back IV up vs front) → gain.** You're long back vega, short front vega.
- **Front vol spike relative to back (curve inverts) → loss.** The short near leg's IV jumps.
- **Underlying pins near strike → gain** (front decays to zero, you keep the back's value).
- **Underlying makes a big fast move away from strike → loss** (negative gamma; the tent collapses).
- **Parallel IV rise → gain** (net long vega), but *how much* depends on whether front or back moves more.

**Diagonal variant:** sell near option at one strike, buy far option at a *different* strike → adds a directional lean (a diagonal is a calendar + a vertical). Useful when you have a mild directional view alongside the term-structure view.

**Margin.** A calendar has a *short near leg* — but it's covered by the *long far leg at the same strike* (the far option is a superior right/obligation), so under SPAN the risk is largely **defined and margin is modest** — roughly the net debit paid plus a small buffer, far less than a naked short. This margin efficiency is a big part of why calendars are popular. The debit paid is close to your max loss in the well-behaved case (though a violent move can, in some constructions, cost a bit more than the debit around the short strike — know your broker's SPAN treatment; verify).

## Worked trade

**Selling rich weekly Nifty vol against the monthly — a long put calendar. Date-stamp illustrative; verify expiry calendar, VIX, lot (Nifty = 75, verify), premiums, STT.**

Setup: Nifty ≈ **24,000**. The term structure today:

| Expiry | Days to expiry | ATM (24,000) IV | 24,000 PE premium (₹) |
|---|---|---|---|
| Near weekly | 4 | 13.5% (pumped by this week's event) | 95 |
| Monthly | 32 | 11.5% | 250 |

Note the **inversion at the front**: the near weekly IV (13.5%) is *above* the monthly (11.5%) — the front is rich because an event lands this week. Your thesis: the event passes benignly, front IV collapses, curve re-steepens, and Nifty sits near 24,000.

**Long put calendar:** Sell near-weekly 24,000 PE @ ₹95, Buy monthly 24,000 PE @ ₹250.
- **Net debit = (250 − 95) × 75 = ₹11,625.** This is your funding and approximate max loss.
- Greeks: **net vega positive** (long the 32-day, short the 4-day — back vega dominates), **net theta positive** (~+₹700/day early — the 4-day bleeds faster than the 32-day), **negative gamma** near the front, delta ≈ 0 at the 24,000 strike.

**Outcome scenarios at near-weekly expiry (4 days out):**

- **Best case — Nifty pins ~24,000, event passes, front IV crushes to 9%:** the near 24,000 PE expires ~worthless (you keep the ₹95 × 75 = ₹7,125 you sold it for), and you still own the monthly 24,000 PE. If the monthly IV holds ~11%, the monthly put is worth maybe ₹210 (some time-decay, but 28 days still to run). Position value ≈ monthly put ₹210×75 = ₹15,750; you paid net ₹11,625 → **gross P&L ≈ +₹4,125.** The front decay you harvested plus retained back value. You can now sell a *new* front weekly against the same monthly long — **roll the short leg** and collect again.

- **Front spikes instead (event escalates, near IV to 20%):** the short near put you sold balloons in value against you — mark-to-market loss on the front leg. The monthly long also gains (long vega) but less than the front spikes → net loss. The curve *inverting further* is the calendar's enemy.

- **Big fast move — Nifty gaps to 23,400:** negative gamma bites. The near 24,000 PE goes deep ITM (you're short it), and while the monthly 24,000 PE also gains, the near leg's intrinsic ramps faster in the immediate move → loss around the debit, capped-ish. Calendars hate big fast moves away from the strike.

- **Slow drift to 23,700:** the short near put decays but goes mildly ITM; the monthly retains value. Modest outcome, roughly flat-to-small either way — calendars are most profitable when spot *sits*.

**Costs:** two legs; **options STT ~0.15% of premium on the sell (verify)** on the sell-to-open of the near put and on closing the monthly; exchange charges, GST, flat brokerage per leg. Rolling the short weekly each week means *repeated* sell-side STT and charges — factor ~₹100–₹200 per roll. Since the strategy's edge is *harvesting front decay repeatedly*, these per-roll costs compound and must be cleared by the decay collected each week.

## Management

The calendar is a **managed, rolling structure**, not a fire-and-forget.

- **The core management move — roll the short front.** When the near weekly you sold expires (or nears worthlessness), **sell a fresh near weekly** at the same (or adjusted) strike against your still-alive monthly long. Each roll harvests another slug of front theta while you keep the long-back vega. This is "renting out" your long-dated option week after week — the calendar analogue of a covered call rolled repeatedly. As long as the front keeps decaying faster than the back and spot behaves, you compound.

- **Spot drifts away from strike (against your negative gamma):** recentre. Roll the *whole* calendar to a new strike nearer spot (close the old, open at the money), or morph into a **diagonal** by selling the new front at a strike closer to spot. You're chasing the tent-pole back under current spot, where the structure earns.

- **Front IV spikes vs back (curve inverts against you):** this is the term-structure risk materialising. If your thesis (front will calm) is broken, cut — the calendar is losing on exactly the relationship you bet on. If it's a temporary spike into an event you still expect to pass, you can hold, but size for the drawdown.

- **Back-month event approaches:** if you're *long* the calendar into an event that sits in the *monthly* window (not the weekly), the monthly vega inflating is your friend — the long back leg richens as the event nears. This is the "own the back, rent the front" event play.

- **Take-profit discipline:** calendars often hit their sweet spot when the front expires with spot near strike; take the win and either re-establish or step aside. Don't marry a calendar through a big move hoping it comes back to the strike — negative gamma punishes hope.

**Scenario grid:**
- Spot pins + front IV crush → **best** (front decay + steepening both help).
- Spot pins + parallel IV up → **good** (long net vega).
- Big fast move either way → **bad** (negative gamma).
- Front IV spikes vs back → **bad** (short front vega, curve inverting).
- Slow drift → **modest** (some front decay, some strike drift offset).

## Risk & sizing

**Max loss** in the well-behaved calendar is approximately the **net debit paid — ₹11,625** in the worked trade — realised if the far option loses most of its value (a violent move far from strike that guts the back leg while the front is also unfavourable, or a collapse in back-month IV). Note the debit is your *funding*, and unlike a naked short, the long far leg caps the disaster — SPAN treats it as largely defined-risk, so margin is efficient (~the debit plus buffer; verify with your broker's SPAN).

**The specific risks to size for:**
1. **Negative gamma / big-move risk:** a sharp gap away from the strike is the calendar's worst enemy. Size so a gap-day loss across all your calendars is bounded. Don't run calendars naked through known binary events that could gap the index — or accept you're then betting the move *won't* happen (short gamma).
2. **Term-structure risk (front spikes vs back):** you're structurally *short front vega, long back vega*. If the whole world's near-term fear explodes (front IV rockets), you lose. In a crash the *front* inverts hardest — calendars sold against a calm back can hurt exactly when everything else does.
3. **Roll/cost drag:** the repeated weekly rolls each carry STT + charges; a low-vol grind where the front barely decays can leave the cost of rolling eating the thin decay collected.

**Portfolio Greeks:** a book of long calendars is **net long vega, net positive theta, net short gamma** — a genuinely different risk profile from both the short-strangle crowd (short vega) and the long-straddle crowd (negative theta). That differentiation is the point: calendars let you be long vol *and* collect theta. But watch the **net short gamma** — like all short-gamma books, it's comfortable in the range and painful in the gap. And watch the **net long vega's term composition** — you want to be long *back* vega, short *front* vega; a parallel vol crush still nets a loss if your back vega dominates and the whole curve drops.

**The tail:** the calendar's tail is a *combination* — a violent directional gap (negative gamma) coinciding with a front-vol spike (term inversion). That's precisely a crash: index gaps down, near-dated IV explodes above far-dated, and your short front leg and negative gamma both hurt at once, only partly cushioned by the long back leg's vega gain. It's a bounded loss (the debit-ish), not a blow-up — the long far leg is your seatbelt — but respect that the "own the back, rent the front" trade sours in exactly the regime it looks safest before.

## Pitfalls & interview-ready summary

**Pitfalls:**
- **Treating a calendar as a free theta machine** — it's short gamma near the front; a big fast move away from the strike hurts regardless of how much theta you were collecting.
- **Ignoring the term-structure risk** — you're short front vega / long back vega; a front-IV spike (curve inversion) is a real loss even if spot is still.
- **Running it through a binary event that could gap the index** — unless you *want* to be short gamma, recentre or step aside before it.
- **Letting spot drift far from the strike without recentring** — the P&L tent-poles at the strike; off-strike, the structure stops earning. Roll the strike.
- **Under-counting roll costs** — repeated weekly short-leg rolls each pay STT + charges; in a low-decay grind the costs can exceed the thin front theta harvested.
- **Assuming SPAN is trivial** — it's efficient (defined-ish) but not zero, and a violent move can cost a touch more than the debit around the short strike; know your broker's treatment.

**Interview-ready summary:** Volatility has a term structure — near-dated and far-dated implied vols differ, usually upward-sloping (contango) in calm, inverting (backwardation) in stress. You trade it with **calendar spreads**: sell the near-expiry option, buy the far-expiry option at the same strike, making you **short front vega, long back vega, net positive theta (the near decays faster), long overall vega, and short gamma near the front**. India's weekly-expiry cycle makes this a live weekly game: sell the pumped near-weekly IV against a calmer monthly, harvest the fast front decay, and **roll the short front week after week** while retaining the long monthly vega — "rent the front, own the back." The trade loves the underlying pinning the strike and a front-IV crush (curve re-steepening); it loses on big fast moves (negative gamma) and on the front spiking relative to the back (curve inverting) — which is exactly a crash, when the front inverts hardest. Loss is bounded near the net debit because the long far leg is the seatbelt, and SPAN is efficient because the position is largely defined-risk. It's one of the few structures that is simultaneously positive-theta and long-vega — a genuinely differentiated book — but never mistake it for free money: it's short gamma, and it sours in the very regime it looks safest before.
