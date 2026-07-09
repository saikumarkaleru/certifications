"""Tests for product-service using FastAPI's TestClient (in-memory, no server)."""
import os
import tempfile

os.environ["DB_PATH"] = os.path.join(tempfile.gettempdir(), "test_product.db")

# Fresh DB per test session.
if os.path.exists(os.environ["DB_PATH"]):
    os.remove(os.environ["DB_PATH"])

from fastapi.testclient import TestClient  # noqa: E402

from app.main import app, init_db  # noqa: E402

init_db()
client = TestClient(app)


def test_health_and_ready():
    assert client.get("/healthz").status_code == 200
    assert client.get("/readyz").status_code == 200


def test_product_crud_lifecycle():
    # create
    r = client.post("/products", json={"name": "Widget", "price": 9.99, "stock": 5})
    assert r.status_code == 201
    pid = r.json()["id"]

    # read
    r = client.get(f"/products/{pid}")
    assert r.status_code == 200
    assert r.json()["name"] == "Widget"

    # list
    assert any(p["id"] == pid for p in client.get("/products").json())

    # update
    r = client.put(f"/products/{pid}", json={"name": "Widget2", "price": 12.5, "stock": 3})
    assert r.status_code == 200
    assert r.json()["name"] == "Widget2"

    # delete
    assert client.delete(f"/products/{pid}").status_code == 204
    assert client.get(f"/products/{pid}").status_code == 404


def test_missing_product_returns_404():
    assert client.get("/products/999999").status_code == 404


def test_validation_rejects_negative_price():
    r = client.post("/products", json={"name": "Bad", "price": -1})
    assert r.status_code == 422
