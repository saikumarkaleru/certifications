"""Tests for order-service.

The product-service dependency is stubbed via httpx's MockTransport so tests
run fully offline and also exercise the fault-tolerant retry/timeout path.
"""
import os
import tempfile

os.environ["DB_PATH"] = os.path.join(tempfile.gettempdir(), "test_order.db")
if os.path.exists(os.environ["DB_PATH"]):
    os.remove(os.environ["DB_PATH"])

import httpx  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

from app import main  # noqa: E402
from app.main import app, init_db  # noqa: E402

init_db()
client = TestClient(app)


def _patch_fetch(monkeypatch_fn):
    """Helper to replace httpx.Client with a mock transport."""


def test_health_and_ready():
    assert client.get("/healthz").status_code == 200
    assert client.get("/readyz").status_code == 200


def test_create_order_happy_path(monkeypatch):
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"id": 1, "name": "Widget", "price": 10.0, "stock": 9})

    transport = httpx.MockTransport(handler)

    class _Client(httpx.Client):
        def __init__(self, *a, **k):
            k["transport"] = transport
            super().__init__(*a, **k)

    monkeypatch.setattr(main.httpx, "Client", _Client)

    r = client.post("/orders", json={"product_id": 1, "quantity": 3})
    assert r.status_code == 201
    body = r.json()
    assert body["total"] == 30.0
    assert body["unit_price"] == 10.0


def test_order_unknown_product_returns_404(monkeypatch):
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(404, json={"detail": "product not found"})

    transport = httpx.MockTransport(handler)

    class _Client(httpx.Client):
        def __init__(self, *a, **k):
            k["transport"] = transport
            super().__init__(*a, **k)

    monkeypatch.setattr(main.httpx, "Client", _Client)
    r = client.post("/orders", json={"product_id": 42, "quantity": 1})
    assert r.status_code == 404


def test_order_dependency_down_returns_503(monkeypatch):
    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("connection refused")

    transport = httpx.MockTransport(handler)

    class _Client(httpx.Client):
        def __init__(self, *a, **k):
            k["transport"] = transport
            super().__init__(*a, **k)

    # Speed up the retry backoff during the test.
    monkeypatch.setattr(main, "RETRY_BACKOFF", 0.0)
    monkeypatch.setattr(main.httpx, "Client", _Client)
    r = client.post("/orders", json={"product_id": 1, "quantity": 1})
    assert r.status_code == 503
    assert "unavailable" in r.json()["detail"]
