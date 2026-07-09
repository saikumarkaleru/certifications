// -----------------------------------------------------------------------------
// python/bindings.cpp
//
// OPTIONAL pybind11 bindings exposing the C++ order book to Python. This file is
// only compiled when pybind11 is available (see CMakeLists.txt). The core engine,
// demo and tests have NO dependency on pybind11.
//
// Build (from the project root, after `pip install pybind11`):
//   cmake -S . -B build -Dpybind11_DIR=$(python -m pybind11 --cmakedir)
//   cmake --build build --target orderbook_py
//
// The resulting module (orderbook_py.*.pyd / .so) drops next to the build dir;
// add that directory to PYTHONPATH or copy the module beside your script.
//
// Usage from Python:
//   import orderbook_py as ob
//   book = ob.OrderBook()
//   trades = book.add_limit_order(ob.Side.Buy, price=100, quantity=10)
//   print(book.best_bid(), book.best_ask(), book.spread())
//   print(book.depth(ob.Side.Buy, 5))
// -----------------------------------------------------------------------------

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include <optional>
#include <vector>

#include "orderbook/order_book.hpp"

namespace py = pybind11;
using namespace ob;

// Thin wrappers that return the generated trades as a Python list, which is far
// more natural than the C++ out-parameter style.
static std::vector<Trade> py_add_limit(OrderBook& b, Side side, Price price,
                                       Quantity qty) {
    std::vector<Trade> trades;
    b.add_limit_order(side, price, qty, &trades);
    return trades;
}

static std::vector<Trade> py_add_market(OrderBook& b, Side side, Quantity qty) {
    std::vector<Trade> trades;
    b.add_market_order(side, qty, &trades);
    return trades;
}

PYBIND11_MODULE(orderbook_py, m) {
    m.doc() = "Low-latency limit order book (C++20 core) exposed to Python.";

    py::enum_<Side>(m, "Side")
        .value("Buy", Side::Buy)
        .value("Sell", Side::Sell);

    py::enum_<OrderType>(m, "OrderType")
        .value("Limit", OrderType::Limit)
        .value("Market", OrderType::Market);

    py::class_<Trade>(m, "Trade")
        .def_readonly("id", &Trade::id)
        .def_readonly("aggressor_id", &Trade::aggressor_id)
        .def_readonly("resting_id", &Trade::resting_id)
        .def_readonly("aggressor_side", &Trade::aggressor_side)
        .def_readonly("price", &Trade::price)
        .def_readonly("quantity", &Trade::quantity)
        .def("__repr__", [](const Trade& t) {
            return "<Trade #" + std::to_string(t.id) + " qty=" +
                   std::to_string(t.quantity) + " @ " +
                   std::to_string(t.price) + ">";
        });

    py::class_<DepthLevel>(m, "DepthLevel")
        .def_readonly("price", &DepthLevel::price)
        .def_readonly("quantity", &DepthLevel::quantity)
        .def_readonly("order_count", &DepthLevel::order_count)
        .def("__repr__", [](const DepthLevel& d) {
            return "<DepthLevel price=" + std::to_string(d.price) + " qty=" +
                   std::to_string(d.quantity) + ">";
        });

    py::class_<OrderBook>(m, "OrderBook")
        .def(py::init<>())
        .def("add_limit_order", &py_add_limit, py::arg("side"),
             py::arg("price"), py::arg("quantity"),
             "Submit a limit order; returns the list of resulting Trades.")
        .def("add_market_order", &py_add_market, py::arg("side"),
             py::arg("quantity"),
             "Submit a market order; returns the list of resulting Trades.")
        .def("cancel_order", &OrderBook::cancel_order, py::arg("order_id"),
             "Cancel a resting order by id; True if it was found.")
        .def("best_bid", &OrderBook::best_bid)
        .def("best_ask", &OrderBook::best_ask)
        .def("spread", &OrderBook::spread)
        .def("quantity_at", &OrderBook::quantity_at, py::arg("side"),
             py::arg("price"))
        .def("depth", &OrderBook::depth, py::arg("side"), py::arg("levels"),
             "Top-N aggregated depth for a side, best level first.")
        .def("order_count", &OrderBook::order_count)
        .def("empty", &OrderBook::empty);
}
