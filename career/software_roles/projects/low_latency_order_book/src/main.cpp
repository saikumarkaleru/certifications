// -----------------------------------------------------------------------------
// src/main.cpp
//
// Demo driver for the limit order book:
//   1. Builds a two-sided book and prints the ladder.
//   2. Submits a crossing order and prints the resulting trades.
//   3. Demonstrates a market order and a cancel.
//   4. Runs a small, honest, LOCAL micro-benchmark (orders/sec) using <chrono>.
//
// The benchmark is a single-threaded, in-process measurement on this machine.
// It is NOT a claim about a production venue — it just shows the engine's
// order of magnitude and how to measure it.
// -----------------------------------------------------------------------------

#include <chrono>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <random>
#include <vector>

#include "orderbook/order_book.hpp"

using namespace ob;

namespace {

// Pretty-print the top `levels` of both sides as a ladder.
void print_book(const OrderBook& book, std::size_t levels = 5) {
    const auto bids = book.depth(Side::Buy, levels);
    const auto asks = book.depth(Side::Sell, levels);

    std::cout << "\n        --- ORDER BOOK ---\n";
    std::cout << "   price   |   bid qty  |  ask qty\n";
    std::cout << "  ---------+------------+-----------\n";

    // Asks printed high-to-low above the spread.
    for (auto it = asks.rbegin(); it != asks.rend(); ++it) {
        std::cout << "   " << std::setw(7) << it->price << " |"
                  << std::setw(11) << " " << " |" << std::setw(9)
                  << it->quantity << "\n";
    }
    // Bids printed high-to-low below the spread.
    for (const auto& lvl : bids) {
        std::cout << "   " << std::setw(7) << lvl.price << " |" << std::setw(11)
                  << lvl.quantity << " |" << std::setw(9) << " " << "\n";
    }

    std::cout << "  ---------+------------+-----------\n";
    if (auto bb = book.best_bid()) std::cout << "  best bid: " << *bb;
    if (auto ba = book.best_ask()) std::cout << "   best ask: " << *ba;
    if (auto sp = book.spread())   std::cout << "   spread: " << *sp;
    std::cout << "\n";
}

void print_trades(const std::vector<Trade>& trades) {
    if (trades.empty()) {
        std::cout << "  (no trades)\n";
        return;
    }
    for (const auto& t : trades) {
        std::cout << "  TRADE #" << t.id << "  " << to_string(t.aggressor_side)
                  << " aggressor=" << t.aggressor_id
                  << " resting=" << t.resting_id << "  qty=" << t.quantity
                  << " @ " << t.price << "\n";
    }
}

// -----------------------------------------------------------------------------
// Local micro-benchmark: sustained mixed add/cancel throughput.
// -----------------------------------------------------------------------------
void run_benchmark() {
    std::cout << "\n=== LOCAL MICRO-BENCHMARK (single thread, in-process) ===\n";

    constexpr int kOrders = 1'000'000;
    OrderBook book;

    // Deterministic pseudo-random stream so results are reproducible.
    std::mt19937_64 rng(42);
    std::uniform_int_distribution<int> price_dist(9'900, 10'100);
    std::uniform_int_distribution<int> qty_dist(1, 100);
    std::uniform_int_distribution<int> side_dist(0, 1);

    const auto start = std::chrono::steady_clock::now();

    std::uint64_t trades = 0;
    std::vector<Trade> scratch;
    scratch.reserve(8);
    for (int i = 0; i < kOrders; ++i) {
        scratch.clear();
        const Side side = side_dist(rng) ? Side::Buy : Side::Sell;
        book.add_limit_order(side, price_dist(rng), qty_dist(rng), &scratch);
        trades += scratch.size();
    }

    const auto end = std::chrono::steady_clock::now();
    const double secs =
        std::chrono::duration<double>(end - start).count();
    const double per_sec = kOrders / secs;

    std::cout << "  orders submitted : " << kOrders << "\n";
    std::cout << "  trades generated : " << trades << "\n";
    std::cout << "  resting orders   : " << book.order_count() << "\n";
    std::cout << "  wall time        : " << std::fixed << std::setprecision(3)
              << secs << " s\n";
    std::cout << "  throughput       : " << std::fixed << std::setprecision(0)
              << per_sec << " orders/sec (local, this machine)\n";
    std::cout << "  avg latency      : " << std::setprecision(1)
              << (secs / kOrders) * 1e9 << " ns/order (amortised)\n";
}

}  // namespace

int main() {
    std::cout << "Low-Latency Limit Order Book — demo\n";
    std::cout << "===================================\n";

    OrderBook book;

    // Live trade log via the listener hook.
    book.set_trade_listener([](const Trade& t) {
        std::cout << "    [listener] filled " << t.quantity << " @ " << t.price
                  << "\n";
    });

    // 1. Seed a two-sided book.
    std::cout << "\n[1] Seeding resting liquidity...\n";
    book.add_limit_order(Side::Buy, 100, 10);
    book.add_limit_order(Side::Buy, 99, 20);
    book.add_limit_order(Side::Buy, 98, 30);
    book.add_limit_order(Side::Sell, 101, 15);
    book.add_limit_order(Side::Sell, 102, 25);
    book.add_limit_order(Side::Sell, 103, 35);
    print_book(book);

    // 2. Aggressive crossing limit buy: 20 @ 102 should sweep 101 then part 102.
    std::cout << "\n[2] Aggressive BUY 20 @ 102 (crosses the spread)...\n";
    std::vector<Trade> trades;
    book.add_limit_order(Side::Buy, 102, 20, &trades);
    print_trades(trades);
    print_book(book);

    // 3. Market SELL 25 hits the bids top-down (price-time priority).
    std::cout << "\n[3] MARKET SELL 25 (hits best bids first)...\n";
    trades.clear();
    book.add_market_order(Side::Sell, 25, &trades);
    print_trades(trades);
    print_book(book);

    // 4. Cancel a resting order.
    std::cout << "\n[4] Cancel demo...\n";
    const OrderId to_cancel = book.add_limit_order(Side::Buy, 97, 50);
    std::cout << "  added resting BUY id=" << to_cancel << " (50 @ 97)\n";
    std::cout << "  cancel(" << to_cancel
              << ") -> " << (book.cancel_order(to_cancel) ? "OK" : "NOT FOUND")
              << "\n";
    std::cout << "  cancel(" << to_cancel
              << ") again -> "
              << (book.cancel_order(to_cancel) ? "OK" : "NOT FOUND")
              << " (already gone)\n";

    // 5. Throughput micro-benchmark.
    run_benchmark();

    std::cout << "\nDone.\n";
    return 0;
}
