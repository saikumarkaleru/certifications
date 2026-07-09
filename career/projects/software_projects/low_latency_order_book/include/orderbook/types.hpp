#ifndef ORDERBOOK_TYPES_HPP
#define ORDERBOOK_TYPES_HPP

// -----------------------------------------------------------------------------
// orderbook/types.hpp
//
// Fundamental value types used throughout the matching engine.
//
// Design notes:
//  * Prices are represented as integer "ticks" (std::int64_t), NOT floating
//    point. Real exchanges quote prices on a fixed tick grid; using integers
//    avoids rounding error and makes price comparison exact and branch-cheap.
//    A helper (Price) is a strong-ish alias so the intent is clear at call
//    sites while remaining trivially copyable and comparable.
//  * Quantities are unsigned 64-bit; an order can never have negative size.
//  * All types here are trivially copyable / cheap to pass by value.
// -----------------------------------------------------------------------------

#include <cstdint>
#include <string>

namespace ob {

// Integer price in ticks. Convert to/from a display currency at the edges.
using Price = std::int64_t;

// Order / trade quantity (number of shares / lots / contracts).
using Quantity = std::uint64_t;

// Monotonically increasing identifier assigned to every accepted order.
using OrderId = std::uint64_t;

// Monotonically increasing identifier assigned to every generated trade.
using TradeId = std::uint64_t;

// Which side of the book an order rests on / aggresses against.
enum class Side : std::uint8_t {
    Buy,   // bid  — wants to buy at or below its limit price
    Sell   // ask  — wants to sell at or above its limit price
};

// Order semantics.
enum class OrderType : std::uint8_t {
    Limit,   // rest on the book if not fully matched
    Market   // match against the best available prices; never rests
};

// Human-readable helpers (used by the demo / logging; not on the hot path).
inline const char* to_string(Side s) {
    return s == Side::Buy ? "BUY" : "SELL";
}

inline const char* to_string(OrderType t) {
    return t == OrderType::Limit ? "LIMIT" : "MARKET";
}

inline Side opposite(Side s) {
    return s == Side::Buy ? Side::Sell : Side::Buy;
}

// -----------------------------------------------------------------------------
// Order: a single resting or incoming instruction.
//
// `remaining` tracks the unfilled quantity; `quantity` is the original size so
// consumers can report fill ratios. For market orders `price` is ignored on the
// buy side (treated as +inf) / sell side (treated as -inf) by the matcher.
// -----------------------------------------------------------------------------
struct Order {
    OrderId   id{0};
    Side      side{Side::Buy};
    OrderType type{OrderType::Limit};
    Price     price{0};
    Quantity  quantity{0};   // original submitted quantity
    Quantity  remaining{0};  // unfilled quantity (<= quantity)

    Order() = default;

    Order(OrderId id_, Side side_, OrderType type_, Price price_, Quantity qty_)
        : id(id_), side(side_), type(type_), price(price_),
          quantity(qty_), remaining(qty_) {}

    // True once the order has been completely filled.
    bool filled() const { return remaining == 0; }
};

// -----------------------------------------------------------------------------
// Trade: the immutable record produced when an aggressing order matches a
// resting order. `price` is always the resting order's price (price of the
// order that was on the book first), which is standard price-time convention.
// -----------------------------------------------------------------------------
struct Trade {
    TradeId  id{0};
    OrderId  aggressor_id{0};  // the incoming order that initiated the match
    OrderId  resting_id{0};    // the passive order that was sitting on the book
    Side     aggressor_side{Side::Buy};
    Price    price{0};         // execution price (== resting order's price)
    Quantity quantity{0};      // matched quantity

    Trade() = default;

    Trade(TradeId id_, OrderId aggressor, OrderId resting, Side aggr_side,
          Price price_, Quantity qty_)
        : id(id_), aggressor_id(aggressor), resting_id(resting),
          aggressor_side(aggr_side), price(price_), quantity(qty_) {}
};

// One aggregated price level in a depth snapshot (price + total resting qty).
struct DepthLevel {
    Price    price{0};
    Quantity quantity{0};  // sum of all resting orders at this price
    std::size_t order_count{0};
};

}  // namespace ob

#endif  // ORDERBOOK_TYPES_HPP
