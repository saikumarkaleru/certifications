# Study Guide — Defending the Order Book in an Interview

This document explains the design so you can explain it confidently. Read the
"mental model" first, then the trade-offs, then rehearse the Q&A.

---

## 1. Mental model (say this in 30 seconds)

> "It's a single-instrument matching engine. Each side of the book is a sorted
> map from price to a price level; a price level is a FIFO queue of resting
> orders. Incoming orders match against the best opposite prices in price-then-
> time order, generating trades at the resting order's price. A hash index from
> order id to its list position gives O(1) cancels. Top-of-book is O(1) because
> the best price is always the front of the sorted map."

---

## 2. The matching algorithm (price-time priority)

1. An incoming order looks at the **best** price on the opposite side
   (`begin()` of the opposite map).
2. If that price is **marketable** (buy price ≥ ask, or sell price ≤ bid), it
   consumes orders at that level **oldest-first** (FIFO = time priority),
   producing a trade for each fill at the **resting** order's price.
3. When a level is exhausted it is erased and matching moves to the next best
   price. This repeats until the incoming order is filled or no marketable
   liquidity remains.
4. A **limit** order rests its unfilled remainder on its own side; a **market**
   order drops any unfilled remainder.

**Price priority** = better-priced resting orders fill first. **Time priority**
= at the same price, the order that arrived first fills first.

---

## 3. Data structures & why

| Structure | Choice | Why |
|-----------|--------|-----|
| Price levels | `std::map<Price, PriceLevel>` (bids `greater`, asks `less`) | Sorted, so best price = `begin()` (O(1)); level insert/erase O(log N). |
| Orders in a level | `std::list<Order>` (FIFO) | O(1) append (time order) and O(1) erase by iterator (needed for cancel). Stable iterators. |
| Cancel index | `std::unordered_map<OrderId, {side, price, iterator}>` | O(1) average lookup → cancel without scanning a level. |
| Prices | `std::int64_t` ticks | Exact, cheap comparison; no float rounding. |

Cached `total_quantity` per level makes depth snapshots and `quantity_at` O(1)
per level instead of summing the list each time.

---

## 4. Latency / data-structure trade-offs (know these cold)

- **`std::map` (red-black tree) vs `std::vector`/flat array of levels.**
  A tree gives clean O(log N) inserts and stable ordering. A flat array indexed
  by (price − floor)/tick can be **O(1)** and far more cache-friendly, which is
  what the fastest engines use when the price range is bounded. Trade-off:
  memory for the full price range and handling out-of-range prices. Our choice
  favors clarity and unbounded prices; the array is the natural next step.

- **`std::list` vs `std::deque` for the FIFO queue.**
  `list` gives O(1) erase-by-iterator and *stable* iterators (the cancel index
  stores them). `deque` is more cache-friendly for pure FIFO but erase from the
  middle (partial-cancel scenarios) is O(n) and iterators aren't stable. Since
  cancel-by-id is a first-class operation, `list` wins here.

- **Intrusive nodes / object pool.**
  `std::list` allocates a node per order. A production engine pre-allocates
  orders in a pool / uses an intrusive list to avoid per-order `new`/`delete`
  and improve locality. Mentioned as an extension.

- **No locks.** The book is single-threaded on purpose. Real venues shard by
  instrument and run one matching thread per book fed by a single-producer
  queue; internal locking would add latency and contention.

- **`std::function` trade listener.** Convenient but has indirection/allocation
  cost. On the hot path you'd template the callback or use the out-parameter
  (which the benchmark does).

---

## 5. Complexity table (memorize)

| Op | Cost |
|----|------|
| add_limit | O(log N) + O(k) |
| add_market | O(k) + O(log N)/drained level |
| cancel | O(1) avg |
| best_bid/ask, spread | O(1) |
| depth(n) | O(n) |

N = distinct price levels, k = resting orders consumed by the match.

---

## 6. Interview Q&A (15–20)

**Q1. What is price-time priority?**
Orders are ranked first by price (better prices trade first), then, among equal
prices, by arrival time (earlier orders trade first). It's the standard fair
matching rule on most equity exchanges.

**Q2. Why `std::map` and not `std::unordered_map` for price levels?**
Matching needs the *best* price and ordered traversal to the next-best. A hash
map has no ordering; a tree map keeps prices sorted so best = `begin()` in O(1)
and sweeping is a simple in-order walk.

**Q3. Why a `std::list` per level instead of a vector?**
FIFO append is O(1) for both, but cancel removes an arbitrary order by id in
O(1) with a list iterator, and list iterators stay valid across other
insert/erase. A vector erase from the middle is O(n) and invalidates positions.

**Q4. How is cancel O(1)?**
An `unordered_map<OrderId, location>` stores each resting order's side, price,
and its `std::list` iterator. Cancel is a hash lookup plus a list `erase(it)` —
no scanning. If the level becomes empty we erase the map node (O(log N)).

**Q5. At what price does a trade execute?**
At the **resting** (passive) order's price. The aggressor may have been willing
to pay more (or accept less); it gets price improvement. This is the standard
convention and prevents the aggressor from setting the print price.

**Q6. How do you handle partial fills?**
Each order tracks `remaining`. A fill is `min(aggressor.remaining,
resting.remaining)`. Whichever hits zero is removed; the other keeps its
reduced `remaining` (the resting side stays on the book; the aggressor rests its
leftover if it's a limit order).

**Q7. What happens to an unfilled market order?**
It's dropped — a market order never rests. If the book can't fill it fully, the
remainder is simply not executed. (Real venues may reject or convert; a plain
market order discards.)

**Q8. How does a market order match every price?**
We give it a sentinel price (+∞ for buy, −∞ for sell) so the "is it marketable?"
check always passes; it then sweeps best-price-first until filled or the side is
empty.

**Q9. Why integer prices?**
Exchanges quote on a discrete tick grid. Integers make comparisons exact and
cheap and eliminate floating-point rounding errors that could mis-order or
mis-match. Display formatting (÷100) happens only at the UI.

**Q10. Is it thread-safe? How would you scale it?**
No, by design. You scale by **sharding per instrument**: one book per matching
thread, each fed by a single-producer lock-free queue. That avoids lock
contention and keeps each book's hot data in one core's cache.

**Q11. What's the worst-case latency of a single order?**
A limit order that sweeps many levels/orders is O(log N + k). The k term (orders
consumed) dominates a large marketable sweep. Top-of-book ops and cancels are
effectively constant time.

**Q12. How would you make it faster / lower latency?**
Flat array of price levels (O(1), cache-friendly) within a bounded price band;
an object pool / intrusive list to kill per-order allocation; templated
callbacks instead of `std::function`; batching and warm caches; avoiding
`std::map` node allocation with a custom allocator.

**Q13. How do you get the top-N depth efficiently?**
Each level caches `total_quantity`, so `depth(n)` is an in-order walk of the
first n map nodes — O(n) — reading the cached sum and order count per level.

**Q14. What invariants must always hold?**
`remaining ≤ quantity`; a level's `total_quantity` equals the sum of its
orders' `remaining`; every id in the index points to a live order; empty levels
are erased; bids' best ≥ never exceeds asks' best without a trade (no locked/
crossed book left resting).

**Q15. How is the engine tested without a framework?**
A tiny `CHECK` macro counts assertions and failures and returns a non-zero exit
code, so CTest/CI can gate on it. Tests cover full/partial fills, price
priority, FIFO time priority, market sweeps, dropped market remainder, cancels
(including re-cancel and unknown id), listener firing, and depth aggregation —
56 assertions.

**Q16. What about order modification (amend)?**
Not implemented as a primitive. A price change or size *increase* loses time
priority (cancel + re-add). A size *decrease* can keep priority by just lowering
`remaining`. This is a good extension to mention.

**Q17. Self-trade prevention / iceberg / stop orders?**
Not implemented — deliberately scoped. Self-trade prevention would check the
resting order's owner before filling; icebergs show partial size and refill;
stops activate at a trigger price. All are natural extensions on top of this
core.

**Q18. Why a header-only core?**
It's small and template-light enough that header-only keeps the build trivial,
lets the compiler inline the hot path, and makes it easy to drop into the demo,
tests, and pybind11 module without a link step.

**Q19. How does the Python/WebSocket layer relate to the engine?**
Optional. pybind11 exposes the C++ book to Python; the WebSocket server streams
JSON snapshots to a browser ladder. The server falls back to a pure-Python book
if the binding isn't built, so the demo runs without compiling C++.

**Q20. What did you actually verify?**
Core + demo + tests compile clean under g++ 15.2 with `-Wall -Wextra
-Wpedantic`; 56/56 test assertions pass under CTest; the WebSocket server was
smoke-tested end-to-end (client receives valid snapshots). Bindings need
pybind11, the server needs `websockets`, and the GUI needs a browser.

---

## 7. Possible extensions (say 2–3 if asked "what next?")

- Flat-array price levels within a bounded band for O(1) cache-friendly access.
- Object pool / intrusive list to remove per-order heap allocation.
- Order **amend** with correct time-priority semantics.
- **Self-trade prevention**, **iceberg**, **stop / stop-limit**, IOC/FOK
  time-in-force.
- Sharded multi-instrument engine with per-book threads and lock-free ingress.
- Persistence / an event journal for replay and crash recovery.
- Nanosecond latency histograms (p50/p99) instead of amortised throughput.
