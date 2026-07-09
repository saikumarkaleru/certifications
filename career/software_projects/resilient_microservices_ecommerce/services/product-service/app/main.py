"""Product Service — catalog CRUD.

A small, self-contained FastAPI microservice backed by SQLite so it runs with
zero external dependencies. Demonstrates health/readiness probes, structured
JSON logging and env-var configuration.
"""
from __future__ import annotations

import json
import logging
import os
import sqlite3
import sys
import time
from contextlib import contextmanager
from typing import Iterator, Optional

from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, Field

# --------------------------------------------------------------------------- #
# Configuration (12-factor: everything via environment variables)
# --------------------------------------------------------------------------- #
SERVICE_NAME = os.getenv("SERVICE_NAME", "product-service")
DB_PATH = os.getenv("DB_PATH", "/tmp/product.db")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()


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
# Database helpers (SQLite, no ORM to keep dependencies tiny)
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
            CREATE TABLE IF NOT EXISTS products (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                name        TEXT    NOT NULL,
                description TEXT    NOT NULL DEFAULT '',
                price       REAL    NOT NULL,
                stock       INTEGER NOT NULL DEFAULT 0
            )
            """
        )
    log.info("database initialised at %s", DB_PATH)


# --------------------------------------------------------------------------- #
# Schemas
# --------------------------------------------------------------------------- #
class ProductIn(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    description: str = ""
    price: float = Field(ge=0)
    stock: int = Field(ge=0, default=0)


class Product(ProductIn):
    id: int


# --------------------------------------------------------------------------- #
# App
# --------------------------------------------------------------------------- #
app = FastAPI(title="Product Service", version="1.0.0")


@app.on_event("startup")
def _startup() -> None:
    init_db()
    log.info("%s started", SERVICE_NAME)


@app.get("/healthz")
def healthz() -> dict:
    """Liveness: process is up and can serve traffic."""
    return {"status": "ok", "service": SERVICE_NAME}


@app.get("/readyz")
def readyz() -> dict:
    """Readiness: dependencies (the DB) are reachable."""
    try:
        with get_db() as conn:
            conn.execute("SELECT 1")
        return {"status": "ready", "service": SERVICE_NAME}
    except Exception as exc:  # pragma: no cover - defensive
        log.exception("readiness check failed")
        raise HTTPException(status_code=503, detail=f"not ready: {exc}")


@app.post("/products", response_model=Product, status_code=201)
def create_product(payload: ProductIn) -> Product:
    with get_db() as conn:
        cur = conn.execute(
            "INSERT INTO products (name, description, price, stock) VALUES (?,?,?,?)",
            (payload.name, payload.description, payload.price, payload.stock),
        )
        pid = cur.lastrowid
    log.info("created product id=%s name=%s", pid, payload.name)
    return Product(id=pid, **payload.model_dump())


@app.get("/products", response_model=list[Product])
def list_products() -> list[Product]:
    with get_db() as conn:
        rows = conn.execute("SELECT * FROM products ORDER BY id").fetchall()
    return [Product(**dict(r)) for r in rows]


@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int) -> Product:
    with get_db() as conn:
        row = conn.execute(
            "SELECT * FROM products WHERE id = ?", (product_id,)
        ).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="product not found")
    return Product(**dict(row))


@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, payload: ProductIn) -> Product:
    with get_db() as conn:
        cur = conn.execute(
            "UPDATE products SET name=?, description=?, price=?, stock=? WHERE id=?",
            (payload.name, payload.description, payload.price, payload.stock, product_id),
        )
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="product not found")
    log.info("updated product id=%s", product_id)
    return Product(id=product_id, **payload.model_dump())


@app.delete("/products/{product_id}", status_code=204, response_class=Response)
def delete_product(product_id: int):
    with get_db() as conn:
        cur = conn.execute("DELETE FROM products WHERE id = ?", (product_id,))
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="product not found")
    log.info("deleted product id=%s", product_id)
    return Response(status_code=204)
