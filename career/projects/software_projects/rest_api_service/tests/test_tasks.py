"""Tests for task CRUD, pagination, filtering and ownership."""

from fastapi.testclient import TestClient


def _create_task(client, headers, **overrides):
    payload = {"title": "Write tests", "description": "cover CRUD"}
    payload.update(overrides)
    return client.post("/tasks", json=payload, headers=headers)


def test_create_task_returns_201(client: TestClient, auth_headers) -> None:
    resp = _create_task(client, auth_headers)
    assert resp.status_code == 201
    body = resp.json()
    assert body["title"] == "Write tests"
    assert body["status"] == "todo"
    assert body["id"] > 0


def test_create_task_invalid_title_returns_422(
    client: TestClient, auth_headers
) -> None:
    resp = client.post("/tasks", json={"title": ""}, headers=auth_headers)
    assert resp.status_code == 422


def test_get_task_returns_it(client: TestClient, auth_headers) -> None:
    task_id = _create_task(client, auth_headers).json()["id"]
    resp = client.get(f"/tasks/{task_id}", headers=auth_headers)
    assert resp.status_code == 200
    assert resp.json()["id"] == task_id


def test_get_missing_task_returns_404(
    client: TestClient, auth_headers
) -> None:
    resp = client.get("/tasks/99999", headers=auth_headers)
    assert resp.status_code == 404


def test_update_task_patches_fields(
    client: TestClient, auth_headers
) -> None:
    task_id = _create_task(client, auth_headers).json()["id"]
    resp = client.patch(
        f"/tasks/{task_id}",
        json={"status": "done", "title": "Updated"},
        headers=auth_headers,
    )
    assert resp.status_code == 200
    body = resp.json()
    assert body["status"] == "done"
    assert body["title"] == "Updated"


def test_delete_task_returns_204_then_404(
    client: TestClient, auth_headers
) -> None:
    task_id = _create_task(client, auth_headers).json()["id"]
    resp = client.delete(f"/tasks/{task_id}", headers=auth_headers)
    assert resp.status_code == 204
    # Subsequent fetch is a 404.
    assert client.get(f"/tasks/{task_id}", headers=auth_headers).status_code == 404


def test_list_pagination_metadata(
    client: TestClient, auth_headers
) -> None:
    for i in range(5):
        _create_task(client, auth_headers, title=f"task {i}")
    resp = client.get("/tasks?limit=2&offset=0", headers=auth_headers)
    assert resp.status_code == 200
    body = resp.json()
    assert body["total"] == 5
    assert body["limit"] == 2
    assert len(body["items"]) == 2


def test_list_filter_by_status(client: TestClient, auth_headers) -> None:
    _create_task(client, auth_headers, title="a", status="todo")
    _create_task(client, auth_headers, title="b", status="done")
    resp = client.get("/tasks?status=done", headers=auth_headers)
    assert resp.status_code == 200
    body = resp.json()
    assert body["total"] == 1
    assert body["items"][0]["status"] == "done"


def test_list_search_by_title(client: TestClient, auth_headers) -> None:
    _create_task(client, auth_headers, title="Buy groceries")
    _create_task(client, auth_headers, title="Read a book")
    resp = client.get("/tasks?q=groc", headers=auth_headers)
    assert resp.status_code == 200
    body = resp.json()
    assert body["total"] == 1
    assert "groceries" in body["items"][0]["title"].lower()


def test_user_cannot_access_others_task(client: TestClient) -> None:
    # User A creates a task.
    client.post(
        "/auth/register",
        json={"email": "a@example.com", "password": "password123"},
    )
    tok_a = client.post(
        "/auth/login",
        data={"username": "a@example.com", "password": "password123"},
    ).json()["access_token"]
    headers_a = {"Authorization": f"Bearer {tok_a}"}
    task_id = _create_task(client, headers_a).json()["id"]

    # User B must not see it (404, not 403, to avoid leaking existence).
    client.post(
        "/auth/register",
        json={"email": "b@example.com", "password": "password123"},
    )
    tok_b = client.post(
        "/auth/login",
        data={"username": "b@example.com", "password": "password123"},
    ).json()["access_token"]
    headers_b = {"Authorization": f"Bearer {tok_b}"}

    resp = client.get(f"/tasks/{task_id}", headers=headers_b)
    assert resp.status_code == 404
