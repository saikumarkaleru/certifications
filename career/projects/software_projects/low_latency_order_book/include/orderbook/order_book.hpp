#ifndef ORDERBOOK_ORDER_BOOK_HPP
#define ORDERBOOK_ORDER_BOOK_HPP

// -----------------------------------------------------------------------------
// orderbook/order_book.hpp
//
// A single-instrument limit order book with price-time priority (FIFO) matching.
//
// Data structures & complexity
// ----------------------------
//   bids_ : std::map<Price, PriceLevel, std::greater<Price>>
//   asks_ : std::map<Price, PriceLevel, std::less<Price>>
//       Sorted associative containers keyed by price. `bids_` is ordered high
//       -> low so begin() is the best (highest) bid; `asks_` low -> high so
//       begin() is the best (lowest) ask. Each node owns a PriceLevel holding
//       a FIFO queue of resting orders at that price.
//
//   PriceLevel::orders : std::list<Order>
//       A doubly linked list giving O(1) push_back (time priority preserved)
//       and O(1) erase given an iterator (needed for O(1) cancel).
//
//   index_ : std::unordered_map<OrderId, OrderLocation>
//       Maps an order id to (side, price, list-iterator) so cancel is O(1)
//       average, without scanning any level.
//
// Complexity summary (N = number of distinct price levels, small in practice):
//   add_limit_order   : O(log N) to find/insert the level + O(k) matching,
//                       where k = number of resting orders consumed.
//   add_market_order  : O(k) matching across consumed levels (+ O(log N) per
//                       exhausted level erased).
//   cancel_order      : O(1) average (hash lookup + list erase); may erase an
//                       emptied level in O(log N).
//   best_bid/best_ask : O(1) — front of the ordered map.
//   spread            : O(1).
//   depth(n)          : O(n) — walk the first n levels.
//
// Threading: NOT thread-safe by design. A production venue runs one book per
// matching thread and feeds it from a single-producer queue; adding locks here
// would only add latency. Callers must serialise access externally.
// -----------------------------------------------------------------------------

#include <algorithm>
#include <cstddef>
#include <functional>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <optional>
#include <unordered_map>
#include <vector>

#include "orderbook/types.hpp"

namespace ob {

// One price level: FIFO queue of resting orders plus a cached total quantity.
struct PriceLevel {
    // std::list keeps stable iterators (used by the cancel index) and gives
    // O(1) append / O(1) erase. Front == oldest order == highest time priority.
    std::list<Order> orders;
    Quantity total_quantity{0};  // cached sum of orders[*].remaining

    bool empty() const { return orders.empty(); }
};

class OrderBook {
public:
    // Callback invoked for every trade produced during a match. Kept as a
    // std::function so the demo, tests and the WebSocket layer can each observe
    // the flow without the engine knowing about them.
    using TradeListener = std::function<void(const Trade&)>;

    OrderBook() = default;

    // ---------------------------------------------------------------------
    // Order entry
    // ---------------------------------------------------------------------

    // Submit a limit order. It first aggresses against the opposite side at
    // marketable prices (price-time priority); any residual quantity rests on
    // the book. Returns the assigned order id. Emitted trades are appended to
    // `out_trades` (if non-null) and also delivered to the trade listener.
    OrderId add_limit_order(Side side, Price price, Quantity quantity,
                            std::vector<Trade>* out_trades = nullptr) {
        const OrderId id = next_order_id_++;
        Order incoming(id, side, OrderType::Limit, price, quantity);

        match(incoming, out_trades);

        // Rest the unfilled remainder on the book.
        if (incoming.remaining > 0) {
            rest(incoming);
        }
        return id;
    }

    // Submit a market order: match against the best available prices until it
    // is filled or the opposite side is exhausted. Never rests. Any unfilled
    // remainder is discarded (cancelled) — standard for a plain market order.
    OrderId add_market_order(Side side, Quantity quantity,
                             std::vector<Trade>* out_trades = nullptr) {
        const OrderId id = next_order_id_++;
        // Price sentinel makes a market buy match any ask and a market sell
        // match any bid: the marketable() check below always passes.
        const Price sentinel = (side == Side::Buy)
                                   ? std::numeric_limits<Price>::max()
                                   : std::numeric_limits<Price>::min();
        Order incoming(id, side, OrderType::Market, sentinel, quantity);
        match(incoming, out_trades);
        // Unfilled remainder is dropped (not rested).
        return id;
    }

    // Cancel a resting order by id. Returns true if it was found and removed.
    // O(1) average: hash lookup + list splice-out; may drop an emptied level.
    bool cancel_order(OrderId id) {
        auto it = index_.find(id);
        if (it == index_.end()) return false;

        const OrderLocation loc = it->second;
        index_.erase(it);

        if (loc.side == Side::Buy) {
            erase_from_side(bids_, loc);
        } else {
            erase_from_side(asks_, loc);
        }
        return true;
    }

    // ---------------------------------------------------------------------
    // Read-only market data accessors
    // ---------------------------------------------------------------------

    // Best (highest) bid price, if any bids rest.
    std::optional<Price> best_bid() const {
        if (bids_.empty()) return std::nullopt;
        return bids_.begin()->first;
    }

    // Best (lowest) ask price, if any asks rest.
    std::optional<Price> best_ask() const {
        if (asks_.empty()) return std::nullopt;
        return asks_.begin()->first;
    }

    // Difference between best ask and best bid. std::nullopt if either side is
    // empty (no two-sided market).
    std::optional<Price> spread() const {
        if (bids_.empty() || asks_.empty()) return std::nullopt;
        return asks_.begin()->first - bids_.begin()->first;
    }

    // Total resting quantity at a given price on a given side (0 if none).
    Quantity quantity_at(Side side, Price price) const {
        if (side == Side::Buy) {
            auto it = bids_.find(price);
            return it == bids_.end() ? 0 : it->second.total_quantity;
        }
        auto it = asks_.find(price);
        return it == asks_.end() ? 0 : it->second.total_quantity;
    }

    // Top-N aggregated depth for a side, best level first. O(n).
    std::vector<DepthLevel> depth(Side side, std::size_t levels) const {
        std::vector<DepthLevel> out;
        out.reserve(levels);
        if (side == Side::Buy) {
            collect_depth(bids_, levels, out);
        } else {
            collect_depth(asks_, levels, out);
        }
        return out;
    }

    // Number of live (resting) orders currently tracked. O(1).
    std::size_t order_count() const { return index_.size(); }

    // True if there are no resting orders on either side.
    bool empty() const { return index_.empty(); }

    // Register a callback fired for every generated trade (optional).
    void set_trade_listener(TradeListener listener) {
        listener_ = std::move(listener);
    }

private:
    // Ordered maps: bids high->low, asks low->high, so begin() is always best.
    using BidMap = std::map<Price, PriceLevel, std::greater<Price>>;
    using AskMap = std::map<Price, PriceLevel, std::less<Price>>;

    // Where a resting order lives, for O(1) cancel.
    struct OrderLocation {
        Side side;
        Price price;
        std::list<Order>::iterator it;  // stable iterator into the level's list
    };

    BidMap bids_;
    AskMap asks_;
    std::unordered_map<OrderId, OrderLocation> index_;

    OrderId next_order_id_{1};
    TradeId next_trade_id_{1};
    TradeListener listener_;

    // Would an incoming order at `price`/`side` cross a resting order at
    // `resting_price` on the opposite side?
    static bool crosses(Side incoming_side, Price incoming_price,
                        Price resting_price) {
        return incoming_side == Side::Buy ? incoming_price >= resting_price
                                          : incoming_price <= resting_price;
    }

    // Core matching loop. Consumes liquidity from the opposite side in strict
    // price-then-time order, generating trades, until the incoming order is
    // filled or no more marketable liquidity exists.
    void match(Order& incoming, std::vector<Trade>* out_trades) {
        if (incoming.side == Side::Buy) {
            match_against(incoming, asks_, out_trades);
        } else {
            match_against(incoming, bids_, out_trades);
        }
    }

    template <typename OppositeMap>
    void match_against(Order& incoming, OppositeMap& opposite,
                       std::vector<Trade>* out_trades) {
        while (incoming.remaining > 0 && !opposite.empty()) {
            auto level_it = opposite.begin();      // best opposite price level
            const Price level_price = level_it->first;

            // Stop once the best opposite price is no longer marketable.
            if (!crosses(incoming.side, incoming.price, level_price)) break;

            PriceLevel& level = level_it->second;

            // Walk the FIFO queue at this level (oldest first = time priority).
            while (incoming.remaining > 0 && !level.orders.empty()) {
                Order& resting = level.orders.front();
                const Quantity fill = std::min(incoming.remaining, resting.remaining);

                // Generate the trade at the resting order's price.
                const Trade trade(next_trade_id_++, incoming.id, resting.id,
                                  incoming.side, level_price, fill);
                if (out_trades) out_trades->push_back(trade);
                if (listener_) listener_(trade);

                incoming.remaining -= fill;
                resting.remaining  -= fill;
                level.total_quantity -= fill;

                if (resting.remaining == 0) {
                    // Fully filled resting order: drop it from book + index.
                    index_.erase(resting.id);
                    level.orders.pop_front();
                }
            }

            // Level fully consumed: erase the empty node (keeps begin() valid).
            if (level.orders.empty()) {
                opposite.erase(level_it);
            }
        }
    }

    // Insert an order's residual onto its own side and index its location.
    void rest(const Order& order) {
        if (order.side == Side::Buy) {
            insert_into_side(bids_, order);
        } else {
            insert_into_side(asks_, order);
        }
    }

    template <typename SameMap>
    void insert_into_side(SameMap& side_map, const Order& order) {
        PriceLevel& level = side_map[order.price];  // create level if absent
        level.orders.push_back(order);              // O(1), preserves time order
        level.total_quantity += order.remaining;
        auto list_it = std::prev(level.orders.end());
        index_[order.id] = OrderLocation{order.side, order.price, list_it};
    }

    template <typename SameMap>
    void erase_from_side(SameMap& side_map, const OrderLocation& loc) {
        auto level_it = side_map.find(loc.price);
        if (level_it == side_map.end()) return;  // defensive; should not happen
        PriceLevel& level = level_it->second;
        level.total_quantity -= loc.it->remaining;
        level.orders.erase(loc.it);
        if (level.orders.empty()) {
            side_map.erase(level_it);
        }
    }

    template <typename SameMap>
    static void collect_depth(const SameMap& side_map, std::size_t levels,
                              std::vector<DepthLevel>& out) {
        std::size_t taken = 0;
        for (const auto& [price, level] : side_map) {
            if (taken++ == levels) break;
            out.push_back(DepthLevel{price, level.total_quantity,
                                     level.orders.size()});
        }
    }
};

}  // namespace ob

#endif  // ORDERBOOK_ORDER_BOOK_HPP
