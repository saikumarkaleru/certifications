"""API tests using FastAPI's TestClient against an in-memory SQLite database."""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base, get_db
from app.main import app

# Isolated in-memory DB so tests never touch the real tasks.db file.
engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(autouse=True)
def fresh_db():
    """Recreate the schema before each test for isolation."""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


client = TestClient(app)


def test_health():
    resp = client.get("/api/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "healthy"}


def test_list_tasks_empty():
    resp = client.get("/api/tasks")
    assert resp.status_code == 200
    assert resp.json() == []


def test_create_task():
    payload = {"title": "Write resume", "description": "Full-stack", "priority": "high"}
    resp = client.post("/api/tasks", json=payload)
    assert resp.status_code == 201
    data = resp.json()
    assert data["id"] > 0
    assert data["title"] == "Write resume"
    assert data["priority"] == "high"
    assert data["completed"] is False
    assert "created_at" in data


def test_create_task_validation_error():
    # Empty title violates min_length=1.
    resp = client.post("/api/tasks", json={"title": ""})
    assert resp.status_code == 422


def test_create_task_invalid_priority():
    resp = client.post("/api/tasks", json={"title": "x", "priority": "urgent"})
    assert resp.status_code == 422


def test_get_task():
    created = client.post("/api/tasks", json={"title": "Read task"}).json()
    resp = client.get(f"/api/tasks/{created['id']}")
    assert resp.status_code == 200
    assert resp.json()["title"] == "Read task"


def test_get_task_not_found():
    resp = client.get("/api/tasks/9999")
    assert resp.status_code == 404


def test_update_task():
    created = client.post("/api/tasks", json={"title": "Old"}).json()
    resp = client.put(
        f"/api/tasks/{created['id']}",
        json={"title": "New", "completed": True},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["title"] == "New"
    assert data["completed"] is True


def test_update_task_not_found():
    resp = client.put("/api/tasks/9999", json={"title": "x"})
    assert resp.status_code == 404


def test_delete_task():
    created = client.post("/api/tasks", json={"title": "Delete me"}).json()
    resp = client.delete(f"/api/tasks/{created['id']}")
    assert resp.status_code == 204
    # Confirm it is gone.
    assert client.get(f"/api/tasks/{created['id']}").status_code == 404


def test_delete_task_not_found():
    resp = client.delete("/api/tasks/9999")
    assert resp.status_code == 404


def test_full_crud_flow():
    # Create two, list, update one, delete one.
    a = client.post("/api/tasks", json={"title": "A"}).json()
    client.post("/api/tasks", json={"title": "B"}).json()
    assert len(client.get("/api/tasks").json()) == 2
    client.put(f"/api/tasks/{a['id']}", json={"completed": True})
    client.delete(f"/api/tasks/{a['id']}")
    remaining = client.get("/api/tasks").json()
    assert len(remaining) == 1
    assert remaining[0]["title"] == "B"
