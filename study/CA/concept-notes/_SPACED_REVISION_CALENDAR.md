# Spaced-Revision Calendar & System

*CA Intermediate, both groups, 6 subjects — Advanced Accounting, Corporate & Other Laws, Cost & Management Accounting, Auditing & Ethics, FM & SM, Taxation. Full-time, ~9-month runway to a **May 2027** attempt. You already own the three assets this system runs on: **concept notes** (`<Subject>/md/*.md`), **flashcard decks** (`<Subject>/flashcards/DECK.tsv`), and **Q&A/MCQ banks** (`<Subject>/qa/`). This file is the machine that keeps all ~125 chapters warm at once so nothing you learn in Month 1 is dead by Month 8.*

---

## 1. The spacing principle (why this works, in one paragraph)

A memory is strongest the moment you learn it and then decays on a curve — most of it is gone within a week unless you *retrieve* it. Each time you successfully pull a fact back from memory, the curve flattens: the next forgetting is slower, so the next review can wait longer. That is why you revise at **expanding intervals — Day 1, Day 3, Day 7, Day 21, then monthly** — instead of re-reading everything every day (which feels productive but wastes time on things you already know). Retrieval, not re-reading, is the active ingredient: close the note and *say/write the answer first*, then check. Across 6 subjects you cannot hold 125 chapters by will — you hold them by touching each one exactly when it is about to fade, and never sooner.

---

## 2. The weekly template (Mon–Sun)

Assumes ~8 hrs/day, one **practical** + one **theory** subject running in parallel (mirrors `_DAILY_PLAN_AND_METHOD.md`). Every day has four fixed slots. The **Revise** slot is filled *automatically* by the rolling queue in §3 — you never decide what's due, the calendar decides.

| Day | (a) Learn-new (~4 hr) | (b) Revise — what comes due (~1 hr) | (c) Flashcard-drill (~30 min) | (d) Self-test (~1 hr) |
|---|---|---|---|---|
| **Mon** | Practical ch. + Theory ch. | Chapters from **D-1, D-3, D-7, D-21** (see §3) | Anki due cards, both today's subjects | 5 MCQs on yesterday's topic |
| **Tue** | Practical ch. + Theory ch. | D-1, D-3, D-7, D-21 | Anki due cards | 5 MCQs |
| **Wed** | Practical ch. + Theory ch. | D-1, D-3, D-7, D-21 | Anki due cards | 1 full Q&A (timed, handwritten) |
| **Thu** | Practical ch. + Theory ch. | D-1, D-3, D-7, D-21 | Anki due cards | 5 MCQs |
| **Fri** | Practical ch. + Theory ch. | D-1, D-3, D-7, D-21 | Anki due cards | 1 full Q&A (timed, handwritten) |
| **Sat** | Lighter: finish/overflow ch. | D-1, D-3, D-7, D-21 **+ the week's 5 new chapters as a block** | Anki due cards + re-drill week's *lapsed* cards | **Weekly self-test:** 15 MCQs + 2 problems across the week |
| **Sun** | **No new learning** | **Monthly-cycle slice** (§4) — one subject's summary sweep | Anki due cards only (keep the streak) | Review weak-areas log; mark next week's due dates |

**Reading order inside every slot:** concept note (the *why*) → active recall (close it, explain aloud) → check → log misses. Never revise by re-reading passively.

---

## 3. The rolling revision queue — zero manual tracking

The whole trick: because you learn at a steady **~1 practical + 1 theory chapter per study day**, the spacing intervals become **fixed offsets on the calendar**. You never maintain a "due list" — you just count backwards from today.

### 3a. The daily count-back (the core habit)

Every morning, before new learning, open **four** chapters — the ones you first studied on these dates:

| Marker | = studied on | Why |
|---|---|---|
| **D-1** | yesterday | catch it before overnight decay |
| **D-3** | 3 days ago | the first big drop-off |
| **D-7** | 7 days ago (same weekday, last week) | consolidation |
| **D-21** | 21 days ago (same weekday, 3 weeks back) | long-term lock |

That's it. Four chapters/day, ~15 min each. No app, no list — the **calendar is the queue**. "What do I revise Tuesday?" → whatever you learned last Monday-adjacent dates: yesterday, last Sat, last Tue, and the Tue three weeks ago. Retrieval only: cover the note, recall the structure and the 3–5 load-bearing facts, then verify.

### 3b. The physical backup — a 5-slot index box (Leitner-style)

If you'd rather see it than count, run a **rotating checklist** with 5 slots. Each chapter is one line on a card (or one row in a sheet). A chapter moves one slot right each time you clear its review; if you blank on it, it drops back to Slot 1.

```
[ Slot 1 ]   [ Slot 2 ]   [ Slot 3 ]   [ Slot 4 ]   [ Slot 5 ]
 every day    every 3 d     weekly      every 3 wk    monthly
   (D-1)        (D-3)        (D-7)        (D-21)      (§4 cycle)
```

- New chapter enters **Slot 1** the day you learn it.
- Clear it → promote to next slot. Blank on it → back to **Slot 1**.
- Each day you only work the slots that are "due" that day. Slot 5 chapters are handled by the monthly cycle (§4), so they leave the box.

### 3c. One rolling tracker row per chapter (optional, if you like a sheet)

Keep a single sheet, one row per chapter, six columns. Fill a date when done; the **next blank tells you when it's due**:

| Chapter | Learned | D-1 ✓ | D-3 ✓ | D-7 ✓ | D-21 ✓ | Monthly ✓ |
|---|---|---|---|---|---|---|
| Cost/04 Overheads | 12-Jul | 13-Jul | 15-Jul | 19-Jul | 02-Aug | (rolls into Aug cycle) |

Once a chapter has all five ticks it is "warm" — it now only reappears in the monthly full-subject sweep. This is the graduation gate.

---

## 4. The monthly full-subject revision cycle

The daily count-back keeps *recent* chapters alive; the monthly cycle keeps *old, graduated* chapters from silently dying. Every 4 weeks, do one **full-subject summary sweep** per subject — but spread across the month so it's ~1 hr on Sundays, not a lost week.

**Rotation (6 subjects → one per ~5 days, all six covered inside each 4-week block):**

| Sun / slot | Subject swept | How (fast, high-level) |
|---|---|---|
| Wk1 Sun | Advanced Accounting | Read only note headers + your own margin notes; redo 2 flagged problems |
| Wk1 Sun (2nd half) | Corporate & Other Laws | Recite section structure from memory; re-drill lapsed Anki cards |
| Wk2 Sun | Cost & Management Accounting | Re-work 2 formula-heavy sums cold |
| Wk2 Sun (2nd half) | Auditing & Ethics | Recall SA numbers + key clauses aloud |
| Wk3 Sun | FM & SM | Re-do 2 ratio/valuation sums; recite SM frameworks |
| Wk3 Sun (2nd half) | Taxation | One income computation + 3 GST scenarios cold |
| Wk4 Sun | **Full mock slot** | 3-hr timed paper from `<Subject>/exam/` or PDF; grade it |

Rule: a monthly sweep is **retrieval + weak spots only** — never a full re-read. If you're reading everything again, the daily queue failed upstream; fix that, don't re-read.

### How the flashcards (`DECK.tsv`) plug in

Your flashcards are what make §3 nearly automatic — **Anki already implements the exact 1/3/7/21/monthly curve for you**, at the *card* level. Use them as the always-on layer under the chapter-level system:

1. **Import once.** Each `<Subject>/flashcards/DECK.tsv` (~100 cards/subject, ~600 total) imports into Anki as tab-separated. In Anki: *File → Import → Fields separated by Tab → map Field 1 = Front, Field 2 = Back → pick/create a deck per subject* (e.g. `CA::Cost`). Re-import after you edit a deck; Anki updates existing cards and adds new ones.
2. **Gate cards to what you've learned.** Don't unleash all 600 on Day 1. When you finish a chapter, **unsuspend that chapter's cards** (tag cards by chapter on import, e.g. `#Cost04`, then unsuspend by tag). New cards enter Anki's own Day 1/3/7/21 schedule — matching your chapter's count-back, one level finer.
3. **Daily driver.** The **(c) Flashcard-drill** slot = "clear today's Anki due count." Set new-cards/day ≈ your learning rate (10–15) and reviews/day uncapped. Cards you fail auto-return to Day 1 — the same lapse-demotion as the Slot-1 rule in §3b.
4. **Anki does the tracking so your box doesn't have to.** Card-level = Anki (automatic). Chapter-level = the calendar count-back (§3a) + monthly sweep (§4). Between the two, every fact and every chapter has a scheduled next-touch and you maintain almost nothing by hand.

---

## 5. Putting it together — the one-minute daily routine

1. **Anki first** (15–30 min): clear today's due cards. *(card-level spacing — automatic)*
2. **Count back** (1 hr): open D-1, D-3, D-7, D-21 chapters; retrieve, check, log misses. *(chapter-level spacing — calendar-driven)*
3. **Learn new** (4 hr): 1 practical + 1 theory chapter, concept-note-first; drop each into Slot 1 / write today's date in the tracker.
4. **Self-test** (1 hr): MCQs or a timed Q&A on yesterday's topic.
5. **Sunday only:** run this block's monthly-sweep slice (§4) instead of new learning.

**Weekly cost:** ~5 hr of pure revision + ~3 hr flashcards, buying permanent retention of all 6 subjects. **Non-negotiables:** (1) retrieval before checking, always; (2) never skip the Anki daily clear — a skipped day dumps a backlog and breaks the curve; (3) a blanked chapter goes back to Slot 1, no ego. Follow this and by final revision (Mar–Apr 2027) you're reviewing summary sheets and mocks, not relearning — exactly where a both-groups May 2027 pass is won.
