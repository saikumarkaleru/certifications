# Q&A — PowerPoint, Pitchbooks and Presenting

A practice bank for Chapter 36. Work each question before reading the answer. Section B problems are reproducible in a blank Excel workbook so you can prove every number by hand; the presentation just displays what the model already computed. The rule throughout: a slide is an output layer, never a place where new arithmetic is invented.

---

## Section A — Concept-Check

**A1. What is a pitchbook and what is its job?**

A pitchbook is a bound (or PDF) deck an advisory bank presents to a client to win or execute a mandate — an IPO, sale, acquisition, financing or fairness opinion. Its job is persuasion backed by analysis: it establishes the bank's credibility, frames the client's situation and options, and lands on a recommended course of action with a supporting valuation. It is a sales document whose numbers must nonetheless survive scrutiny, because the client's CFO and lawyers will test them.

**A2. State the "one idea per slide" rule and why it holds.**

Each slide carries a single message, stated in the title as a full sentence, and every element on the slide exists to support that message. It holds because an audience reads the title, forms one expectation, and scans the body to confirm it; a slide with three competing ideas forces the reader to guess which one matters and slows the whole room. If a slide needs two messages, it needs to be two slides.

**A3. What is an "action title" (or "so-what title") and how does it differ from a label title?**

An action title states the conclusion as a sentence — "Revenue growth is decelerating as the core segment matures" — rather than labelling the content — "Revenue Analysis". The label tells you the topic; the action title tells you what to think about the topic. Reading only the action titles in sequence should reproduce the deck's argument as a coherent story, which is the fastest test of whether a deck has a spine.

**A4. Describe the standard structure of a sell-side pitchbook.**

Roughly: (1) cover and disclaimer; (2) executive summary / situation overview; (3) "why us" — the bank's credentials and relevant deal experience; (4) market and industry context; (5) the company's positioning and financial profile; (6) valuation (the football field plus each methodology); (7) the recommended transaction, process and timeline; (8) appendix with detailed models, comparable tables and assumptions. The persuasive arc moves from context, to analysis, to recommendation.

**A5. Why must every chart and table in a deck trace back to a single source model?**

Because inconsistency destroys credibility instantly. If the football field shows a DCF midpoint of $52 and the DCF page shows $54, the client stops trusting all the numbers, not just the two. A single linked source model — ideally pasted as linked values or refreshed from one file — guarantees that when an assumption changes, every dependent chart, the valuation summary and the recommendation all move together. Manual re-keying is where errors and embarrassment live.

**A6. What is a football field chart and what does it display?**

A football field is a horizontal floating-bar (stock) chart that shows the valuation range produced by each methodology — trading comparables, precedent transactions, DCF, LBO, 52-week trading range — stacked as parallel bars. Each bar runs from its low to its high estimate; the reader sees at a glance where the methods overlap. The overlap region is the defensible value conclusion, and a reference line for the current share price or offer price shows whether the proposal sits inside, above or below that range.

**A7. Distinguish "linked paste" from "paste as picture" when moving Excel content into PowerPoint, and when to use each.**

Linked paste keeps a live connection to the workbook, so the chart or table updates when the source changes — useful during drafting when numbers are still moving, but dangerous at distribution because a broken or moved file shows stale or error content. Paste as picture (enhanced metafile or PNG) freezes the exhibit as an image — safe for a final, distributed deck because nothing can silently change or break, at the cost of needing a manual refresh to update. Draft with links; distribute as pictures.

**A8. What is the "10/20/30" style guidance and what is its underlying point?**

A heuristic (Guy Kawasaki): roughly ten slides, twenty minutes, thirty-point minimum font. The exact numbers matter less than the discipline: force prioritisation, respect the audience's time and attention, and never put text so small it signals the slide is really a document. In banking the slide count is far higher, but the font-size and density discipline still applies to any slide meant to be presented rather than read alone.

**A9. Why does formatting consistency (fonts, colours, decimal places, units) matter beyond aesthetics?**

Consistency is a proxy for care. A reader who sees revenue as "$1,240.0m" on one page and "1.24bn" on the next, or three different blues for the same company, subconsciously downgrades the rigour of the analysis. Consistent units, a fixed decimal convention (e.g. one decimal for margins, zero for large currency figures), aligned decimals and a single colour for each entity let the reader spend attention on the argument instead of decoding the format.

**A10. What is the difference between a deck built to be presented and one built to be read (a "leave-behind")?**

A presented deck is sparse — the presenter carries the detail verbally, and dense slides compete with the speaker. A leave-behind must stand alone, so it carries more text, footnotes and self-contained explanation because no one is there to narrate. Trouble comes from using one deck for both jobs: it is too dense to present and too terse to read. Decide the primary use first, then design density to match.

---

## Section B — Build / Computational Problems

Every exhibit below is computed in Excel first; the slide only displays the result. Reproduce each in a blank sheet.

**B1. Build the football field data.** You have these valuation ranges ($/share): Trading comps 42–56; Precedent transactions 48–64; DCF 46–60; LBO 40–52; 52-week range 38–54. The current share price is 45; the proposed offer is 58.

A floating bar needs a *base* (the low, plotted invisible) and a *length* (high minus low, plotted visible). Lay out:

| Method | Low | High | Base (invisible) | Range length |
|---|---|---|---|---|
| Trading comps | 42 | 56 | 42 | 14 |
| Precedents | 48 | 64 | 48 | 16 |
| DCF | 46 | 60 | 46 | 14 |
| LBO | 40 | 52 | 40 | 12 |
| 52-week | 38 | 54 | 38 | 16 |

Excel: Base in `D2` = `=B2`, Range length in `E2` = `=C2-B2`, fill down. Build a stacked horizontal bar of columns D and E, then set the D series fill to No Fill. The visible E bars now float from each low to each high.

Reconcile: 42 + 14 = 56 ✓, 48 + 16 = 64 ✓, 46 + 14 = 60 ✓, 40 + 12 = 52 ✓, 38 + 16 = 54 ✓.

**B2. Find the defensible overlap.** Using B1, the concentration of value is where the "analytical" methods (comps, precedents, DCF; exclude the 52-week price and the sponsor-constrained LBO) overlap.

Overlap low = the highest of the three lows = `=MAX(46,48,42)` = **48**.
Overlap high = the lowest of the three highs = `=MIN(60,64,56)` = **56**.

So the value convergence zone is **$48–$56**, midpoint `=(48+56)/2` = **$52**. The offer of $58 sits **above** the entire overlap — a premium to fair value — which is exactly the message the sell-side action title should carry: "The $58 offer exceeds our $48–$56 analytical range." If MIN(highs) had come out below MAX(lows), there would be no overlap and you would flag divergence instead.

**B3. Add and position the reference lines.** On the same chart you must place a vertical marker for the current price (45) and the offer (58). A clean method: add each as an XY scatter series with two points sharing the x-value and spanning the y-axis, e.g. current price points (45, 0) and (45, 6). Confirm placement numerically: 45 is below the DCF low (46) and below the overlap low (48), so the current-price line sits to the left of every analytical bar — visually confirming the stock trades below fair value. The offer line at 58 sits to the right of the overlap high (56). No arithmetic changes; you are only proving where the lines fall.

**B4. Premium-to-price table for the recommendation slide.** Offer 58; unaffected price 45; 52-week high 54; analytical midpoint 52 (from B2).

Premium to unaffected: `=(58/45)-1` = 0.28889 → **28.9%**.
Premium to 52-week high: `=(58/54)-1` = 0.07407 → **7.4%**.
Premium to analytical midpoint: `=(58/52)-1` = 0.11538 → **11.5%**.

Reconcile the first: 45 × 1.28889 = 58.00 ✓. Present all three at one decimal place (A9's consistency rule); a table mixing "28.89%" and "7%" reads as careless.

**B5. Revenue bridge (waterfall) data.** A slide must explain the move from FY24 revenue of 1,200 to FY25 revenue of 1,356 via: Volume +90, Price +120, FX −30, Discontinued −24. Prove it foots and set up the floating "base" for the waterfall.

Running total: 1,200 → +90 = 1,290 → +120 = 1,410 → −30 = 1,380 → −24 = **1,356**. Check `=1200+90+120-30-24` = **1356** ✓ — the bridge ties to the FY25 endpoint, so the exhibit is honest.

Waterfall base (the invisible spacer under each floating block) for an increase sits at the *previous* cumulative; for a decrease it sits at the *new* (lower) cumulative:

| Bar | Value | Cumulative after | Base (invisible) | Visible height |
|---|---|---|---|---|
| FY24 (anchor) | 1,200 | 1,200 | 0 | 1,200 |
| Volume (+) | 90 | 1,290 | 1,200 | 90 |
| Price (+) | 120 | 1,410 | 1,290 | 120 |
| FX (−) | 30 | 1,380 | 1,380 | 30 |
| Discontinued (−) | 24 | 1,356 | 1,356 | 24 |
| FY25 (anchor) | 1,356 | 1,356 | 0 | 1,356 |

For a down bar, base = cumulative *after* the fall (FX: 1,410−30 = 1,380; Discontinued: 1,380−24 = 1,356). Stacked bar of Base (no fill) + Visible height renders the classic floating waterfall.

**B6. Chart y-axis manipulation check.** A draft chart plots FY24 = 1,200 and FY25 = 1,356 with the y-axis starting at 1,150. Compute the true change and the visual exaggeration.

True change: `=(1356/1200)-1` = 0.13 → **+13.0%**.
Bar heights above a 1,150 baseline: FY24 shows 1,200−1,150 = 50; FY25 shows 1,356−1,150 = 206. Apparent ratio `=206/50` = **4.12×**, i.e. the FY25 bar looks over four times taller than FY24 for a change that is really 13%. Fix: start the axis at zero, where the height ratio equals 1,356/1,200 = 1.13, matching reality. This is the numeric case for the "always start bar charts at zero" rule.

**B7. Slide-count / timing budget.** A management presentation is allotted 45 minutes: 30 minutes of speaking and 15 minutes for Q&A. At a disciplined pace of roughly 1.5 minutes per content slide, plus a title and a closing slide that take negligible time:

Content-slide budget: `=30/1.5` = **20 content slides**. Total deck ≈ 20 + 2 = **22 slides**. If the drafted deck has 40 content slides, required pace = `=30/40` = 0.75 min = **45 seconds per slide** — too fast to land any message, so the fix is to cut to ~20 or move detail to the appendix, not to talk faster.

**B8. Comps table rounding reconciliation.** A comparable-companies exhibit lists EV = 4,875.4 and EBITDA = 612.9. The displayed EV/EBITDA multiple is "8.0x".

Precise multiple: `=4875.4/612.9` = 7.9546 → rounds to **8.0x** at one decimal ✓. Now confirm the reader can't back into a contradiction: if someone divides the *displayed* rounded figures they still get 7.95, which rounds to 8.0 — consistent. Trap to avoid: never display EV and EBITDA rounded to whole numbers (4,875 / 613 = 7.953) *and* the multiple to two decimals as "7.95x", because a checker dividing the shown inputs (4,875/613 = 7.9527) gets a different last digit and flags a phantom error. Keep displayed precision internally reconcilable.

---

## Section C — Interview-Style Questions

**C1. "Walk me through how you'd build a football field chart."**

I collect a low and high from each methodology: comps and precedents from the multiple ranges applied to the metric, DCF from the sensitivity grid, LBO from the price that hits the sponsor's target IRR, and the 52-week range from market data. In Excel I create a "base" column equal to each low and a "range" column equal to high minus low, build a stacked horizontal bar, and set the base series to no fill so the bars float. I add current-price and offer reference lines as scatter series. The message is the overlap zone, stated in the action title — the current price relative to that zone tells the client whether the stock is under-valued and whether the offer is fair.

**C2. "A managing director says the deck 'has no story'. What does that mean and how do you fix it?"**

It means the slides are a pile of exhibits rather than an argument — you can shuffle them without changing anything, which proves there's no spine. I fix it by reading only the action titles top to bottom; if they don't narrate a coherent case (situation → analysis → recommendation), the story is missing. I rewrite each title as a full-sentence conclusion, reorder slides so each one sets up the next, cut slides that don't advance the argument to the appendix, and make sure the executive summary states the recommendation the rest of the deck earns. The test passes when the titles alone read like a memo.

**C3. "How do you make sure the numbers in a 60-page pitchbook are all consistent?"**

Single source of truth: every number flows from one model file, pasted linked while drafting and converted to pictures for the final version so nothing breaks or silently updates. I keep a short list of the headline figures — enterprise value, offer price, key multiples, valuation midpoint — and check each appears identically everywhere (exec summary, valuation page, football field, recommendation). I fix formatting conventions up front so consistency is structural, and before it goes out a fresh pair of eyes ties the football field back to each methodology page.

**C4. "Why not just start bar charts wherever the data starts, to show detail?"**

Because a non-zero baseline distorts the visual proportion between bars — a 13% increase can be made to look like a 4x jump if the axis starts just below the smaller value (I can show the arithmetic: bar heights of 50 versus 206 above a truncated base). Bars encode magnitude by area from zero, so truncating the axis lies about the magnitude even when the labels are accurate, and a sophisticated audience will catch it and distrust the rest. If I genuinely need to show small differences, I use a line chart, an indexed series, or clearly labelled data values — not a truncated bar axis.

**C5. "When would you link Excel into PowerPoint versus pasting a picture?"**

I link while the model is still moving, so every edit flows through and I'm never re-pasting forty exhibits by hand. But the moment the deck is finalised and leaves my machine I paste as pictures, because a linked file that gets moved, renamed or opened without the source shows broken links or stale numbers in front of the client — the worst possible failure. So: linked for the live working draft, frozen pictures for anything distributed. If a distributed deck must stay updatable, I keep the source file bundled and controlled, but that's the exception.

**C6. "Your slide has a great chart but the audience looks lost. What went wrong?"**

Most likely the slide has no action title telling them what to conclude, so they're reverse-engineering the point while I talk — attention split, message lost. Or the slide carries more than one idea. The in-the-moment fix is to say the conclusion first ("the takeaway here is...") then walk the evidence; the structural fix is a full-sentence title, one idea per slide, and cutting anything that doesn't support it. A chart is evidence; the title supplies the argument.

---

## Section D — Common-Error Spotting

**D1.** *A football field bar for the DCF is built with Low in the base column and High in the range column.* Wrong: the range (visible) column must be High − Low, not High. With base 46 and range 60, the bar would float from 46 to 106 instead of 46 to 60. Fix: range = `=C-B` = 14, so the bar spans 46 to 60.

**D2.** *The valuation summary slide shows a DCF midpoint of $53; the DCF detail page shows $54.* Inconsistency between exhibits — a credibility killer. Cause is almost always a manually re-typed number that didn't get updated when the model changed. Fix: link both to the same model cell (or paste both from the same refreshed source) so they can't diverge.

**D3.** *A revenue bar chart starts its y-axis at 1,150 to "show the growth more clearly".* Visual distortion: it exaggerates a real +13.0% into an apparent ~4x (heights 50 vs 206). Fix: start bar-chart axes at zero; if fine detail matters, switch to a line or indexed chart.

**D4.** *Every slide title is a label — "Revenue", "Margins", "Valuation".* No story: labels state topics, not conclusions. A reader can't follow the argument from the titles. Fix: rewrite as full-sentence action titles that state the "so what", so the titles alone narrate the case.

**D5.** *A revenue waterfall shows FY24 1,200 bridging to FY25 1,356 but the drivers listed sum to +180.* The bridge doesn't foot: 1,200 + 180 = 1,380 ≠ 1,356. Something is missing or mislabelled (the true drivers net to +156). Fix: reconcile drivers to the endpoint before charting — an exhibit that doesn't foot is worse than no exhibit.

**D6.** *The final deck was emailed as a .pptx with all Excel charts pasted as live links.* On the client's machine the links break or show stale/error content, and the client can potentially click through to your underlying model. Fix: paste as pictures for any distributed deck; keep the linked version only as your internal working file.

**D7.** *Margins appear as "23.7%", "24%" and "0.251" on three consecutive slides.* Inconsistent units and precision signal carelessness and force the reader to decode formats. Fix: one convention — e.g. one decimal place, percentage format — applied everywhere the metric appears.

**D8.** *A single "appendix" slide crams the full comps table, the DCF sensitivity grid and the LBO summary onto one page in 7-point font.* Violates one-idea-per-slide and readable-font discipline; nothing can be read or discussed. Fix: one exhibit per slide at a legible size, or move genuine backup to clearly separated appendix pages.

**D9.** *The comps exhibit displays EV as 4,875, EBITDA as 613, and the multiple as "7.95x".* Rounding EV/EBITDA to whole numbers while quoting the multiple to two decimals invites phantom mismatches when a checker divides the visible figures. Fix: show enough precision that dividing the displayed inputs reproduces the displayed multiple.

**D10.** *One presented deck is reused unchanged as the printed leave-behind.* If built sparse to present, it's unreadable alone; if built dense to read, it's death-by-bullet to present. Fix: decide the primary use, match density to it, and produce a variant for the secondary use.

---

*End of practice bank — Chapter 36.*
