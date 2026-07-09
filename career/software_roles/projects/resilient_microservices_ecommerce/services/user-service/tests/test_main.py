"""Tests for user-service: registration, login, token auth, password hashing."""
import os
import tempfile

os.environ["DB_PATH"] = os.path.join(tempfile.gettempdir(), "test_user.db")
os.environ["SECRET_KEY"] = "test-secret"
if os.path.exists(os.environ["DB_PATH"]):
    os.remove(os.environ["DB_PATH"])

from fastapi.testclient import TestClient  # noqa: E402

from app.main import app, hash_password, init_db, verify_password  # noqa: E402

init_db()
client = TestClient(app)


def test_health_and_ready():
    assert client.get("/healthz").status_code == 200
    assert client.get("/readyz").status_code == 200


def test_password_hashing_roundtrip():
    h = hash_password("hunter2")
    assert h != "hunter2"  # never stored in plaintext
    assert verify_password("hunter2", h)
    assert not verify_password("wrong", h)


def test_register_login_and_me():
    r = client.post("/register", json={"username": "alice", "password": "secret1"})
    assert r.status_code == 201

    # duplicate registration
    assert client.post("/register", json={"username": "alice", "password": "secret1"}).status_code == 409

    # login
    r = client.post("/login", json={"username": "alice", "password": "secret1"})
    assert r.status_code == 200
    token = r.json()["access_token"]

    # authed endpoint
    r = client.get("/me", headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 200
    assert r.json()["username"] == "alice"


def test_bad_login_rejected():
    assert client.post("/login", json={"username": "alice", "password": "nope123"}).status_code == 401


def test_invalid_token_rejected():
    assert client.get("/me", headers={"Authorization": "Bearer garbage"}).status_code == 401
    assert client.get("/me").status_code == 401
