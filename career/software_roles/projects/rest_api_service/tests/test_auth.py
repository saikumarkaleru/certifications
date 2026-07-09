"""Tests for the authentication flow."""

from fastapi.testclient import TestClient


def test_register_returns_201_and_user(client: TestClient) -> None:
    resp = client.post(
        "/auth/register",
        json={"email": "new@example.com", "password": "password123"},
    )
    assert resp.status_code == 201
    body = resp.json()
    assert body["email"] == "new@example.com"
    assert "id" in body
    assert "hashed_password" not in body  # never leak the hash


def test_register_duplicate_email_returns_409(client: TestClient) -> None:
    payload = {"email": "dup@example.com", "password": "password123"}
    client.post("/auth/register", json=payload)
    resp = client.post("/auth/register", json=payload)
    assert resp.status_code == 409


def test_register_short_password_returns_422(client: TestClient) -> None:
    resp = client.post(
        "/auth/register",
        json={"email": "x@example.com", "password": "short"},
    )
    assert resp.status_code == 422


def test_login_success_returns_token(client: TestClient) -> None:
    client.post(
        "/auth/register",
        json={"email": "login@example.com", "password": "password123"},
    )
    resp = client.post(
        "/auth/login",
        data={"username": "login@example.com", "password": "password123"},
    )
    assert resp.status_code == 200
    body = resp.json()
    assert body["token_type"] == "bearer"
    assert body["access_token"]


def test_login_wrong_password_returns_401(client: TestClient) -> None:
    client.post(
        "/auth/register",
        json={"email": "wp@example.com", "password": "password123"},
    )
    resp = client.post(
        "/auth/login",
        data={"username": "wp@example.com", "password": "wrongpassword"},
    )
    assert resp.status_code == 401


def test_protected_route_without_token_returns_401(
    client: TestClient,
) -> None:
    resp = client.get("/tasks")
    assert resp.status_code == 401
