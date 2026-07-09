#!/usr/bin/env python3
"""Real-time order-book WebSocket server.

Streams order-book snapshots as JSON to any connected client (see web/index.html
for a browser GUI). It runs a small simulated order flow so you can watch the
ladder update live.

Two backends, chosen automatically at startup:

  1. C++ engine  — if the optional pybind11 module `orderbook_py` is importable
                   (build it via `python/README.md`), the real matching engine
                   drives the book.
  2. Pure-Python fallback — a compact, self-contained reimplementation of the
                   same price-time-priority book, used when the binding is not
                   built. This means the server works WITHOUT compiling anything.

Dependency (server only):  pip install websockets

Run:
    pip install websockets          # one-time
    python server/server.py         # then open server/web/index.html

The server listens on ws://localhost:8765 by default (override with --host /
--port). It broadcasts a fresh snapshot roughly every 500 ms.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import random
import sys
from typing import Any

# `websockets` is the ONLY third-party dependency and it is required only for
# this server, never for the C++ core. Fail with a helpful message if missing.
try:
    import websockets
except ImportError:  # pragma: no cover - environment dependent
    sys.stderr.write(
        "ERROR: the 'websockets' package is required to run the server.\n"
        "       Install it with:  pip install websockets\n"
    )
    sys.exit(1)


# ---------------------------------------------------------------------------
# Backend selection
# ---------------------------------------------------------------------------
def build_backend() -> tuple[Any, str]:
    """Return (book, backend_name).

    Prefers the compiled C++ engine; otherwise uses the pure-Python fallback.
    """
    try:
        import orderbook_py as ob  # type: ignore

        return CppBookAdapter(ob), "cpp (orderbook_py)"
    except ImportError:
        return PyOrderBook(), "python-fallback"


class CppBookAdapter:
    """Adapts the pybind11 `orderbook_py.OrderBook` to the tiny interface the
    server needs (add_limit / add_market / cancel / snapshot)."""

    def __init__(self, ob_module: Any) -> None:
        self._ob = ob_module
        self._book = ob_module.OrderBook()

    def add_limit(self, side: str, price: int, qty: int) -> None:
        s = self._ob.Side.Buy if side == "buy" else self._ob.Side.Sell
        self._book.add_limit_order(s, price, qty)

    def add_market(self, side: str, qty: int) -> None:
        s = self._ob.Side.Buy if side == "buy" else self._ob.Side.Sell
        self._book.add_market_order(s, qty)

    def snapshot(self, levels: int = 10) -> dict[str, Any]:
        bids = [
            {"price": d.price, "qty": d.quantity, "orders": d.order_count}
            for d in self._book.depth(self._ob.Side.Buy, levels)
        ]
        asks = [
            {"price": d.price, "qty": d.quantity, "orders": d.order_count}
            for d in self._book.depth(self._ob.Side.Sell, levels)
        ]
        return _pack_snapshot(bids, asks)


class PyOrderBook:
    """Self-contained price-time-priority book (pure-Python fallback).

    Mirrors the C++ semantics closely enough for the live demo: FIFO queues per
    price level, best-price-first matching, aggregated depth snapshots. It is
    intentionally simple (dict-of-lists) rather than latency-optimized — the C++
    engine is the performance story; this just keeps the server runnable with no
    build step.
    """

    def __init__(self) -> None:
        # price -> list[[order_id, remaining]]   (FIFO: index 0 is oldest)
        self._bids: dict[int, list[list[int]]] = {}
        self._asks: dict[int, list[list[int]]] = {}
        self._next_id = 1

    def _match(self, side: str, price: int, qty: int) -> int:
        """Match `qty` against the opposite side; return unfilled remainder."""
        if side == "buy":
            # Sweep cheapest asks first while marketable.
            for lvl_price in sorted(self._asks):
                if qty <= 0 or lvl_price > price:
                    break
                qty = self._consume(self._asks, lvl_price, qty)
        else:
            # Sweep highest bids first while marketable.
            for lvl_price in sorted(self._bids, reverse=True):
                if qty <= 0 or lvl_price < price:
                    break
                qty = self._consume(self._bids, lvl_price, qty)
        return qty

    @staticmethod
    def _consume(book: dict[int, list[list[int]]], price: int, qty: int) -> int:
        queue = book[price]
        while qty > 0 and queue:
            resting = queue[0]
            fill = min(qty, resting[1])
            resting[1] -= fill
            qty -= fill
            if resting[1] == 0:
                queue.pop(0)
        if not queue:
            del book[price]
        return qty

    def add_limit(self, side: str, price: int, qty: int) -> None:
        remaining = self._match(side, price, qty)
        if remaining > 0:
            book = self._bids if side == "buy" else self._asks
            book.setdefault(price, []).append([self._next_id, remaining])
        self._next_id += 1

    def add_market(self, side: str, qty: int) -> None:
        # +/- inf limit makes it always marketable; remainder is dropped.
        sentinel = 10**18 if side == "buy" else -(10**18)
        self._match(side, sentinel, qty)
        self._next_id += 1

    def snapshot(self, levels: int = 10) -> dict[str, Any]:
        def side_depth(book: dict[int, list[list[int]]], reverse: bool):
            out = []
            for price in sorted(book, reverse=reverse)[:levels]:
                queue = book[price]
                out.append(
                    {
                        "price": price,
                        "qty": sum(o[1] for o in queue),
                        "orders": len(queue),
                    }
                )
            return out

        bids = side_depth(self._bids, reverse=True)
        asks = side_depth(self._asks, reverse=False)
        return _pack_snapshot(bids, asks)


def _pack_snapshot(bids: list[dict], asks: list[dict]) -> dict[str, Any]:
    best_bid = bids[0]["price"] if bids else None
    best_ask = asks[0]["price"] if asks else None
    spread = (best_ask - best_bid) if (best_bid is not None and best_ask is not None) else None
    return {
        "type": "snapshot",
        "bids": bids,
        "asks": asks,
        "best_bid": best_bid,
        "best_ask": best_ask,
        "spread": spread,
    }


# ---------------------------------------------------------------------------
# Simulated order flow
# ---------------------------------------------------------------------------
def seed(book: Any) -> None:
    """Populate an initial two-sided book around a mid of 10000."""
    for i in range(1, 11):
        book.add_limit("buy", 10000 - i, random.randint(5, 50))
        book.add_limit("sell", 10000 + i, random.randint(5, 50))


def step(book: Any) -> None:
    """Apply one random market event to keep the book moving."""
    roll = random.random()
    if roll < 0.45:
        side = random.choice(["buy", "sell"])
        mid = 10000
        offset = random.randint(0, 8)
        price = mid - offset if side == "buy" else mid + offset
        book.add_limit(side, price, random.randint(1, 30))
    elif roll < 0.75:
        book.add_market(random.choice(["buy", "sell"]), random.randint(1, 20))
    else:
        # Occasionally reseed a level so liquidity never fully drains.
        side = random.choice(["buy", "sell"])
        off = random.randint(1, 10)
        book.add_limit(side, 10000 - off if side == "buy" else 10000 + off,
                       random.randint(5, 40))


# ---------------------------------------------------------------------------
# WebSocket plumbing
# ---------------------------------------------------------------------------
CLIENTS: set[Any] = set()


async def handler(ws: Any) -> None:
    CLIENTS.add(ws)
    try:
        async for _ in ws:  # we don't expect client messages; just keep alive
            pass
    finally:
        CLIENTS.discard(ws)


async def broadcaster(book: Any, backend_name: str, interval: float) -> None:
    seed(book)
    while True:
        step(book)
        snap = book.snapshot(10)
        snap["backend"] = backend_name
        payload = json.dumps(snap)
        if CLIENTS:
            await asyncio.gather(
                *(c.send(payload) for c in list(CLIENTS)),
                return_exceptions=True,
            )
        await asyncio.sleep(interval)


async def main_async(host: str, port: int, interval: float) -> None:
    book, backend_name = build_backend()
    print(f"order-book server: backend = {backend_name}")
    print(f"listening on ws://{host}:{port}  (open server/web/index.html)")
    async with websockets.serve(handler, host, port):
        await broadcaster(book, backend_name, interval)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="localhost")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--interval", type=float, default=0.5,
                        help="seconds between snapshot broadcasts")
    args = parser.parse_args()
    try:
        asyncio.run(main_async(args.host, args.port, args.interval))
    except KeyboardInterrupt:
        print("\nshutting down.")


if __name__ == "__main__":
    main()
