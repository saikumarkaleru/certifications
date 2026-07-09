"""Pytest fixtures.

Each test runs against a fresh in-memory SQLite database. We override the
`get_db` dependency so the app uses the test session, and rebuild the schema
per test for full isolation.
"""

from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base, get_db
from app.main import app

# In-memory DB shared across connections within a test via StaticPool.
engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)


def _override_get_db() -> Generator:
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(autouse=True)
def _fresh_schema() -> Generator[None, None, None]:
    """Create all tables before each test and drop them afterwards."""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    """A TestClient wired to the in-memory test database."""
    app.dependency_overrides[get_db] = _override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


@pytest.fixture
def auth_headers(client: TestClient) -> dict[str, str]:
    """Register + log in a user and return an Authorization header."""
    email = "user@example.com"
    password = "supersecret123"

    client.post("/auth/register", json={"email": email, "password": password})
    resp = client.post(
        "/auth/login", data={"username": email, "password": password}
    )
    token = resp.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}
