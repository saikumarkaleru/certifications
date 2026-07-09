# -----------------------------------------------------------------------------
# Low-Latency Limit Order Book — build definition
#
# Core targets (NO external dependencies):
#   orderbook            INTERFACE library exposing the header-only engine
#   orderbook_demo       demo + micro-benchmark  (src/main.cpp)
#   orderbook_tests      assert-based test harness (tests/test_orderbook.cpp)
#
# The tests are registered with CTest so `ctest` gates on them.
#
# Optional target (only if pybind11 is found — never required for the core):
#   orderbook_py         pybind11 module (python/bindings.cpp)
#
# Usage:
#   cmake -S . -B build
#   cmake --build build
#   ctest --test-dir build --output-on-failure
# -----------------------------------------------------------------------------
cmake_minimum_required(VERSION 3.16)
project(low_latency_order_book LANGUAGES CXX)

# --- Language standard --------------------------------------------------------
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Default to an optimized build if the user didn't pick one (matters for the
# micro-benchmark numbers).
if(NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
    set(CMAKE_BUILD_TYPE Release CACHE STRING "Build type" FORCE)
endif()

# --- Header-only core library -------------------------------------------------
add_library(orderbook INTERFACE)
target_include_directories(orderbook INTERFACE
    ${CMAKE_CURRENT_SOURCE_DIR}/include)
target_compile_features(orderbook INTERFACE cxx_std_20)

# Warnings as a courtesy (kept non-fatal so the core always builds).
if(MSVC)
    set(OB_WARNINGS /W4)
else()
    set(OB_WARNINGS -Wall -Wextra -Wpedantic)
endif()

# --- Demo / micro-benchmark ---------------------------------------------------
add_executable(orderbook_demo src/main.cpp)
target_link_libraries(orderbook_demo PRIVATE orderbook)
target_compile_options(orderbook_demo PRIVATE ${OB_WARNINGS})

# --- Tests --------------------------------------------------------------------
enable_testing()
add_executable(orderbook_tests tests/test_orderbook.cpp)
target_link_libraries(orderbook_tests PRIVATE orderbook)
target_compile_options(orderbook_tests PRIVATE ${OB_WARNINGS})
add_test(NAME orderbook_tests COMMAND orderbook_tests)

# --- OPTIONAL pybind11 module -------------------------------------------------
# Only built when pybind11 is discoverable (e.g. `pip install pybind11` then
# pass -Dpybind11_DIR=$(python -m pybind11 --cmakedir)). The core build and the
# tests never depend on this.
find_package(pybind11 QUIET CONFIG)
if(pybind11_FOUND)
    message(STATUS "pybind11 found — building optional Python module 'orderbook_py'")
    pybind11_add_module(orderbook_py python/bindings.cpp)
    target_link_libraries(orderbook_py PRIVATE orderbook)
else()
    message(STATUS "pybind11 NOT found — skipping optional Python module "
                   "(this is expected; run `pip install pybind11` to enable it)")
endif()
