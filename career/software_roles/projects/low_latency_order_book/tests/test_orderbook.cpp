// -----------------------------------------------------------------------------
// tests/test_orderbook.cpp
//
// Self-contained assert-based test harness for the order book. No external test
// framework, no network access — just a tiny CHECK macro that counts pass/fail
// and returns a non-zero exit code on any failure (so ctest / CI can gate on it).
//
// Coverage:
//   * best_bid / best_ask / spread on an empty and populated book
//   * simple full match generates one trade at the resting price
//   * partial fill (aggressor larger than resting): remainder rests
//   * partial fill (resting larger than aggressor): resting shrinks
//   * price priority: better price fills first
//   * time priority (FIFO): older order at same price fills first
//   * market order sweeps multiple levels and drops unfilled remainder
//   * cancel removes liquidity and returns correct found/not-found
//   * non-crossing limit order just rests (no trade)
//   * depth snapshot aggregation
// -----------------------------------------------------------------------------

#include <cstdlib>
#include <iostream>
#include <vector>

#include "orderbook/order_book.hpp"

using namespace ob;

namespace {

int g_checks = 0;
int g_failures = 0;

// Minimal assertion: records the result and prints only on failure.
#define CHECK(cond)                                                         \
    do {                                                                    \
        ++g_checks;                                                         \
        if (!(cond)) {                                                      \
            ++g_failures;                                                   \
            std::cerr << "  FAIL [" << __LINE__ << "]: " #cond "\n";        \
        }                                                                   \
    } while (0)

// Helper: does an optional hold this exact value?
bool opt_eq(const std::optional<Price>& o, Price v) {
    return o.has_value() && *o == v;
}

// -------------------------------------------------------------------------
void test_empty_book() {
    OrderBook b;
    CHECK(b.empty());
    CHECK(!b.best_bid().has_value());
    CHECK(!b.best_ask().has_value());
    CHECK(!b.spread().has_value());
    CHECK(b.order_count() == 0);
}

void test_resting_no_cross() {
    OrderBook b;
    b.add_limit_order(Side::Buy, 100, 10);
    b.add_limit_order(Side::Sell, 101, 10);  // does not cross 100
    CHECK(opt_eq(b.best_bid(), 100));
    CHECK(opt_eq(b.best_ask(), 101));
    CHECK(opt_eq(b.spread(), 1));
    CHECK(b.order_count() == 2);
}

void test_simple_full_match() {
    OrderBook b;
    b.add_limit_order(Side::Sell, 101, 10);          // resting ask
    std::vector<Trade> trades;
    b.add_limit_order(Side::Buy, 101, 10, &trades);  // exactly crosses

    CHECK(trades.size() == 1);
    CHECK(trades[0].price == 101);          // trades at resting price
    CHECK(trades[0].quantity == 10);
    CHECK(trades[0].aggressor_side == Side::Buy);
    CHECK(b.empty());                       // both sides consumed
}

void test_partial_fill_aggressor_larger() {
    OrderBook b;
    b.add_limit_order(Side::Sell, 101, 10);
    std::vector<Trade> trades;
    // Buy 25 but only 10 available -> 10 fills, 15 rests as new best bid.
    b.add_limit_order(Side::Buy, 101, 25, &trades);

    CHECK(trades.size() == 1);
    CHECK(trades[0].quantity == 10);
    CHECK(!b.best_ask().has_value());       // ask fully consumed
    CHECK(opt_eq(b.best_bid(), 101));       // remainder rests at 101
    CHECK(b.quantity_at(Side::Buy, 101) == 15);
}

void test_partial_fill_resting_larger() {
    OrderBook b;
    b.add_limit_order(Side::Buy, 100, 40);  // big resting bid
    std::vector<Trade> trades;
    b.add_limit_order(Side::Sell, 100, 10, &trades);  // small aggressor

    CHECK(trades.size() == 1);
    CHECK(trades[0].quantity == 10);
    CHECK(opt_eq(b.best_bid(), 100));
    CHECK(b.quantity_at(Side::Buy, 100) == 30);  // 40 - 10
    CHECK(!b.best_ask().has_value());
}

void test_price_priority() {
    OrderBook b;
    // Two asks; the cheaper (100) must fill before the pricier (101).
    b.add_limit_order(Side::Sell, 101, 10);
    b.add_limit_order(Side::Sell, 100, 10);
    std::vector<Trade> trades;
    b.add_limit_order(Side::Buy, 101, 10, &trades);

    CHECK(trades.size() == 1);
    CHECK(trades[0].price == 100);          // best (lowest) ask filled first
    CHECK(opt_eq(b.best_ask(), 101));       // pricier ask still resting
}

void test_time_priority_fifo() {
    OrderBook b;
    // Two asks at the SAME price; the first submitted must fill first.
    const OrderId first  = b.add_limit_order(Side::Sell, 100, 10);
    const OrderId second = b.add_limit_order(Side::Sell, 100, 10);
    CHECK(second == first + 1);

    std::vector<Trade> trades;
    b.add_limit_order(Side::Buy, 100, 10, &trades);  // fills exactly one

    CHECK(trades.size() == 1);
    CHECK(trades[0].resting_id == first);   // oldest order filled first
    CHECK(b.quantity_at(Side::Sell, 100) == 10);  // the newer one remains
}

void test_market_order_sweeps_levels() {
    OrderBook b;
    b.add_limit_order(Side::Sell, 100, 10);
    b.add_limit_order(Side::Sell, 101, 10);
    b.add_limit_order(Side::Sell, 102, 10);
    std::vector<Trade> trades;
    // Market buy 25 sweeps 100 (10) + 101 (10) + 102 (5), leaving 5 @ 102.
    b.add_market_order(Side::Buy, 25, &trades);

    CHECK(trades.size() == 3);
    CHECK(trades[0].price == 100 && trades[0].quantity == 10);
    CHECK(trades[1].price == 101 && trades[1].quantity == 10);
    CHECK(trades[2].price == 102 && trades[2].quantity == 5);
    CHECK(opt_eq(b.best_ask(), 102));
    CHECK(b.quantity_at(Side::Sell, 102) == 5);
}

void test_market_order_unfilled_dropped() {
    OrderBook b;
    b.add_limit_order(Side::Sell, 100, 10);
    std::vector<Trade> trades;
    // Only 10 available; the remaining 15 of a market order is discarded.
    b.add_market_order(Side::Buy, 25, &trades);

    CHECK(trades.size() == 1);
    CHECK(trades[0].quantity == 10);
    CHECK(b.empty());                       // nothing rests from a market order
}

void test_market_order_empty_book() {
    OrderBook b;
    std::vector<Trade> trades;
    b.add_market_order(Side::Buy, 10, &trades);  // nothing to match
    CHECK(trades.empty());
    CHECK(b.empty());
}

void test_cancel() {
    OrderBook b;
    const OrderId id = b.add_limit_order(Side::Buy, 100, 10);
    b.add_limit_order(Side::Buy, 100, 20);  // same level, different order
    CHECK(b.quantity_at(Side::Buy, 100) == 30);

    CHECK(b.cancel_order(id) == true);      // found + removed
    CHECK(b.quantity_at(Side::Buy, 100) == 20);
    CHECK(b.cancel_order(id) == false);     // already gone
    CHECK(b.cancel_order(999999) == false); // never existed
}

void test_cancel_empties_level() {
    OrderBook b;
    const OrderId id = b.add_limit_order(Side::Sell, 105, 10);
    CHECK(opt_eq(b.best_ask(), 105));
    CHECK(b.cancel_order(id));
    CHECK(!b.best_ask().has_value());       // level removed when emptied
    CHECK(b.empty());
}

void test_listener_fires() {
    OrderBook b;
    int count = 0;
    Quantity total = 0;
    b.set_trade_listener([&](const Trade& t) {
        ++count;
        total += t.quantity;
    });
    b.add_limit_order(Side::Sell, 100, 10);
    b.add_limit_order(Side::Buy, 100, 10);  // triggers one trade
    CHECK(count == 1);
    CHECK(total == 10);
}

void test_depth_snapshot() {
    OrderBook b;
    b.add_limit_order(Side::Buy, 100, 10);
    b.add_limit_order(Side::Buy, 100, 5);   // aggregates with above
    b.add_limit_order(Side::Buy, 99, 20);
    b.add_limit_order(Side::Buy, 98, 30);

    const auto d = b.depth(Side::Buy, 2);    // top 2 levels only
    CHECK(d.size() == 2);
    CHECK(d[0].price == 100 && d[0].quantity == 15 && d[0].order_count == 2);
    CHECK(d[1].price == 99 && d[1].quantity == 20);
}

}  // namespace

int main() {
    std::cout << "Running order book tests...\n";

    test_empty_book();
    test_resting_no_cross();
    test_simple_full_match();
    test_partial_fill_aggressor_larger();
    test_partial_fill_resting_larger();
    test_price_priority();
    test_time_priority_fifo();
    test_market_order_sweeps_levels();
    test_market_order_unfilled_dropped();
    test_market_order_empty_book();
    test_cancel();
    test_cancel_empties_level();
    test_listener_fires();
    test_depth_snapshot();

    std::cout << "\nChecks run : " << g_checks << "\n";
    std::cout << "Failures   : " << g_failures << "\n";
    if (g_failures == 0) {
        std::cout << "ALL TESTS PASSED\n";
        return EXIT_SUCCESS;
    }
    std::cout << "SOME TESTS FAILED\n";
    return EXIT_FAILURE;
}
