# Low-Latency Limit Order Book (C++20)

A single-instrument **limit order book / matching engine** with strict
**price-time priority (FIFO)** matching, written in modern, header-focused
C++20. It ships with a demo + micro-benchmark, a self-contained test harness,
optional Python bindings, and a real-time WebSocket + web-GUI layer.

The core (engine + demo + tests) builds and runs with **only a C++20 compiler
and CMake** — no third-party libraries, no network access.

---

## What it does

- Accepts **limit** and **market** orders on both sides (buy/sell).
- Matches aggressing orders against resting liquidity in **price then time**
  order, producing **trades** at the resting order's price.
- Supports **partial fills**, **cancels**, and **top-of-book / depth** queries.
- Emits trades through both an out-parameter and an optional **trade listener**
  callback.

---

## Repository layout

```
low_latency_order_book/
├── include/orderbook/
│   ├── types.hpp          # Side, OrderType, Order, Trade, DepthLevel, Price
│   └── order_book.hpp     # OrderBook: matching engine (header-only)
├── src/main.cpp           # demo + local micro-benchmark
├── tests/test_orderbook.cpp   # assert-based tests (no external framework)
├── CMakeLists.txt         # C++20 build; CTest-registered tests
├── python/
│   ├── bindings.cpp       # OPTIONAL pybind11 module
│   └── README.md          # how to build/use the bindings
├── server/
│   ├── server.py          # WebSocket server (uses C++ binding or py fallback)
│   └── web/index.html     # browser GUI: live bid/ask ladder
├── README.md              # this file
└── STUDY_GUIDE.md         # interview prep: design, trade-offs, 15-20 Q&A
```

---

## Build & run the core (no dependencies)

```bash
cmake -S . -B build
cmake --build build

# run the tests (CTest-registered)
ctest --test-dir build --output-on-failure
# ...or run the binaries directly:
./build/orderbook_tests      # asserts; non-zero exit on failure
./build/orderbook_demo       # ladder, trades, cancel demo, micro-benchmark
```

On Windows with the MSYS2 MinGW toolchain, add `-G "MinGW Makefiles"` to the
configure step. The build defaults to `Release` so the benchmark is meaningful.

---

## Architecture

```
        add_limit_order / add_market_order / cancel_order
                              │
                              ▼
                       ┌────────────┐
   best bid ◀──────────│  OrderBook │──────────▶ best ask
   depth(Buy,N)        │  (matcher) │        depth(Sell,N)
                       └─────┬──────┘
              ┌──────────────┴──────────────┐
              ▼                              ▼
   bids_: map<Price, PriceLevel,   asks_: map<Price, PriceLevel,
              greater<Price>>                 less<Price>>
   (best = highest bid at begin)   (best = lowest ask at begin)
              │                              │
              ▼                              ▼
        PriceLevel { list<Order> orders (FIFO); Quantity total; }
                              │
        index_: unordered_map<OrderId, {side, price, list iterator}>
                              └──▶ O(1) cancel
```

- **Ordered maps** (`std::map`) keep price levels sorted so the best price is
  always `begin()` — O(1) top-of-book, O(log N) insert/erase of a level.
- **FIFO queue per level** (`std::list<Order>`) preserves time priority with
  O(1) append and O(1) erase given an iterator.
- **Order-id index** (`std::unordered_map`) stores each resting order's
  location (side, price, list iterator) so **cancel is O(1) average** without
  scanning a level.

### Why integer prices

Prices are `std::int64_t` **ticks**, not floating point. Exchanges quote on a
fixed tick grid; integers make comparisons exact and cheap and avoid
floating-point rounding bugs in matching. Convert to display currency only at
the UI edge (the web GUI divides by 100).

---

## Complexity

| Operation           | Complexity                       | Notes |
|---------------------|----------------------------------|-------|
| `add_limit_order`   | O(log N) + O(k)                  | find/insert level; k = resting orders consumed |
| `add_market_order`  | O(k) + O(log N) per drained level| sweeps best prices; never rests |
| `cancel_order`      | O(1) average                     | hash lookup + list erase; O(log N) if level empties |
| `best_bid`/`best_ask`| O(1)                            | front of ordered map |
| `spread`            | O(1)                             | |
| `quantity_at`       | O(log N)                         | map lookup |
| `depth(side, n)`    | O(n)                             | walk first n levels |

`N` = number of distinct price levels (small in practice); `k` = number of
resting orders touched by a match.

---

## Local micro-benchmark

`orderbook_demo` runs a single-threaded, in-process benchmark: 1,000,000 random
mixed limit orders through one book, timed with `<chrono>`. On the development
machine it reports on the order of **~3 million orders/sec** (~300 ns/order
amortised, including matching and ~0.77M generated trades).

This is an **honest local measurement**, not a production-venue claim: it is one
thread, one process, no networking, no persistence, and no risk checks. It shows
the data-structure choices are sound and how to measure throughput/latency.

---

## Optional extras (not required for the core)

### Python bindings — `python/`
pybind11 wrapper exposing `OrderBook` to Python. Requires `pip install
pybind11`; CMake auto-detects it and otherwise skips the module. See
`python/README.md`.

### Real-time server + GUI — `server/`
`server/server.py` streams live JSON snapshots over WebSocket; `server/web/
index.html` renders a color-coded bid/ask ladder with depth bars.

```bash
pip install websockets       # server-only dependency
python server/server.py      # ws://localhost:8765
# then open server/web/index.html in a browser
```

The server uses the compiled C++ engine if `orderbook_py` is importable,
otherwise a **pure-Python fallback** book — so it runs with **no compilation**.

---

## Design decisions (summary)

- **Header-only core** for easy inlining and simple consumption.
- **`std::map` + `std::list` + `unordered_map`** — the classic, cache-reasonable
  structure that gives O(1) top-of-book and O(1) cancel with clear complexity,
  rather than a premature lock-free/array design.
- **Integer tick prices** for exact, fast comparison.
- **Not thread-safe by design**: one book per matching thread fed by a single
  producer is faster than internal locking. Callers serialise access.
- **Trades priced at the resting order** (passive price), the standard
  convention.

See `STUDY_GUIDE.md` for the deeper rationale and interview Q&A.

---

## Verification status

Built with g++ 15.2 (MSYS2) + CMake 4.1:

- Core library, demo, and tests **compile cleanly** (`-Wall -Wextra
  -Wpedantic`, no warnings).
- Test harness: **56 assertions, 0 failures** (`ctest` passes).
- Server: verified end-to-end with the pure-Python fallback (client receives
  valid JSON snapshots).

Requires local setup: `pip install pybind11` (bindings), `pip install
websockets` (server), and a browser (GUI).
