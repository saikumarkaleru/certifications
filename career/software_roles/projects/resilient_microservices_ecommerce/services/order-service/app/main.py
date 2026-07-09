"""Order Service — create/list orders.

Calls the Product Service to validate products before creating an order.
This is where the resiliency story lives: HTTP calls to the dependency use a
short timeout, a bounded retry with backoff, and degrade to a clear 503 error
instead of hanging when the dependency is down.
"""
from __future__ import annotations

import json
import logging
import os
import sqlite3
import sys
import time
from contextlib import contextmanager
from typing import Iterator

import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# --------------------------------------------------------------------------- #
# Configuration
# --------------------------------------------------------------------------- #
SERVICE_NAME = os.getenv("SERVICE_NAME", "order-service")
DB_PATH = os.getenv("DB_PATH", "/tmp/order.db")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL", "http://localhost:8001")
# Fault-tolerance knobs (all tunable via env)
HTTP_TIMEOUT = float(os.getenv("HTTP_TIMEOUT", "2.0"))
HTTP_RETRIES = int(os.getenv("HTTP_RETRIES", "3"))
RETRY_BACKOFF = float(os.getenv("RETRY_BACKOFF", "0.2"))


# --------------------------------------------------------------------------- #
# Structured JSON logging
# --------------------------------------------------------------------------- #
class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        payload = {
            "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(record.created)),
            "level": record.levelname,
            "service": SERVICE_NAME,
            "logger": record.name,
            "msg": record.getMessage(),
        }
        if record.exc_info:
            payload["exc"] = self.formatException(record.exc_info)
        return json.dumps(payload)


def _build_logger() -> logging.Logger:
    logger = logging.getLogger(SERVICE_NAME)
    logger.setLevel(LOG_LEVEL)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JsonFormatter())
    logger.handlers = [handler]
    logger.propagate = False
    return logger


log = _build_logger()


# --------------------------------------------------------------------------- #
# Database
# --------------------------------------------------------------------------- #
@contextmanager
def get_db() -> Iterator[sqlite3.Connection]:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db() -> None:
    with get_db() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS orders (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER NOT NULL,
                quantity   INTEGER NOT NULL,
                unit_price REAL    NOT NULL,
                total      REAL    NOT NULL,
                created_at TEXT    NOT NULL
            )
            """
        )
    log.info("database initialised at %s", DB_PATH)


# --------------------------------------------------------------------------- #
# Resilient dependency call: timeout + retry + backoff + clear failure
# --------------------------------------------------------------------------- #
def fetch_product(product_id: int) -> dict:
    """Fetch a product from the product-service.

    Retries transient failures (timeouts / connection errors / 5xx) with linear
    backoff. A 404 is *not* retried — it is a definitive answer. When the
    dependency stays unavailable we raise 503 so the caller fails fast and loud.
    """
    url = f"{PRODUCT_SERVICE_URL}/products/{product_id}"
    last_exc: Exception | None = None

    for attempt in range(1, HTTP_RETRIES + 1):
        try:
            with httpx.Client(timeout=HTTP_TIMEOUT) as client:
                resp = client.get(url)
            if resp.status_code == 404:
                raise HTTPException(status_code=404, detail="product not found")
            if resp.status_code >= 500:
                raise httpx.HTTPStatusError(
                    "upstream 5xx", request=resp.request, response=resp
                )
            resp.raise_for_status()
            return resp.json()
        except HTTPException:
            raise  # definitive (404) — do not retry
        except (httpx.TimeoutException, httpx.TransportError, httpx.HTTPStatusError) as exc:
            last_exc = exc
            log.warning(
                "product-service call failed (attempt %s/%s): %s",
                attempt, HTTP_RETRIES, exc,
            )
            if attempt < HTTP_RETRIES:
                time.sleep(RETRY_BACKOFF * attempt)  # linear backoff

    log.error("product-service unavailable after %s attempts", HTTP_RETRIES)
    raise HTTPException(
        status_code=503,
        detail=f"product-service unavailable: {last_exc}",
    )


# --------------------------------------------------------------------------- #
# Schemas
# --------------------------------------------------------------------------- #
class OrderIn(BaseModel):
    product_id: int = Field(gt=0)
    quantity: int = Field(gt=0)


class Order(BaseModel):
    id: int
    product_id: int
    quantity: int
    unit_price: float
    total: float
    created_at: str


# --------------------------------------------------------------------------- #
# App
# --------------------------------------------------------------------------- #
app = FastAPI(title="Order Service", version="1.0.0")


@app.on_event("startup")
def _startup() -> None:
    init_db()
    log.info("%s started, product-service=%s", SERVICE_NAME, PRODUCT_SERVICE_URL)


@app.get("/healthz")
def healthz() -> dict:
    return {"status": "ok", "service": SERVICE_NAME}


@app.get("/readyz")
def readyz() -> dict:
    """Ready when our own DB works. The product-service being down does not make
    us un-ready — we degrade gracefully per request instead."""
    try:
        with get_db() as conn:
            conn.execute("SELECT 1")
        return {"status": "ready", "service": SERVICE_NAME}
    except Exception as exc:  # pragma: no cover - defensive
        raise HTTPException(status_code=503, detail=f"not ready: {exc}")


@app.post("/orders", response_model=Order, status_code=201)
def create_order(payload: OrderIn) -> Order:
    product = fetch_product(payload.product_id)  # resilient call
    unit_price = float(product["price"])
    total = round(unit_price * payload.quantity, 2)
    created_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    with get_db() as conn:
        cur = conn.execute(
            "INSERT INTO orders (product_id, quantity, unit_price, total, created_at) "
            "VALUES (?,?,?,?,?)",
            (payload.product_id, payload.quantity, unit_price, total, created_at),
        )
        oid = cur.lastrowid

    log.info("created order id=%s product_id=%s total=%s", oid, payload.product_id, total)
    return Order(
        id=oid,
        product_id=payload.product_id,
        quantity=payload.quantity,
        unit_price=unit_price,
        total=total,
        created_at=created_at,
    )


@app.get("/orders", response_model=list[Order])
def list_orders() -> list[Order]:
    with get_db() as conn:
        rows = conn.execute("SELECT * FROM orders ORDER BY id").fetchall()
    return [Order(**dict(r)) for r in rows]


@app.get("/orders/{order_id}", response_model=Order)
def get_order(order_id: int) -> Order:
    with get_db() as conn:
        row = conn.execute("SELECT * FROM orders WHERE id = ?", (order_id,)).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="order not found")
    return Order(**dict(row))
