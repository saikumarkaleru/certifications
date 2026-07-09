# Python bindings (OPTIONAL)

These pybind11 bindings expose the C++20 matching engine to Python. They are
**entirely optional** — the C++ core, demo, and tests build and run without
pybind11 or any Python packages.

## Why bindings?

The hot path (matching, cancel, depth) stays in optimized C++, while Python is
used for orchestration: quick experiments, feeding a live UI, plotting depth,
or writing higher-level strategy/replay scripts.

## Prerequisites

```bash
pip install pybind11
```

You also need the same C++ toolchain used for the core build (g++ 15 / MSVC /
clang with C++20).

## Build

From the **project root** (one level up from this folder):

```bash
# Point CMake at the pip-installed pybind11 CMake package.
cmake -S . -B build -Dpybind11_DIR=$(python -m pybind11 --cmakedir)
cmake --build build --target orderbook_py
```

On success CMake prints `pybind11 found — building optional Python module`
and produces `orderbook_py.<platform>.pyd` (Windows) or `.so` (Linux/macOS)
inside `build/`.

If pybind11 is **not** installed, CMake simply prints that it is skipping the
module — the core targets still build. This is by design.

## Use

Make sure the built module is importable (run Python from `build/`, or add
`build/` to `PYTHONPATH`, or copy the module next to your script):

```python
import orderbook_py as ob

book = ob.OrderBook()

# Seed resting liquidity.
book.add_limit_order(ob.Side.Buy, price=100, quantity=10)
book.add_limit_order(ob.Side.Sell, price=101, quantity=10)

print("best bid:", book.best_bid())   # 100
print("best ask:", book.best_ask())   # 101
print("spread  :", book.spread())     # 1

# Cross the spread and inspect the trades.
trades = book.add_limit_order(ob.Side.Buy, price=101, quantity=6)
for t in trades:
    print(t)                          # <Trade #... qty=6 @ 101>

# Top-of-book depth ladder.
print(book.depth(ob.Side.Sell, 5))
```

## Notes

- `add_limit_order` / `add_market_order` return a Python `list[Trade]` instead
  of using the C++ out-parameter — more idiomatic for Python callers.
- Prices are integer ticks (see the main README's design notes).
- The `server/` WebSocket layer will automatically use this module if it is
  importable, otherwise it falls back to a pure-Python simulated feed.
