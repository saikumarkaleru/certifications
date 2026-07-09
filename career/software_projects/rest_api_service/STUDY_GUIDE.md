# Study Guide — Task Manager REST API

This document explains the design of the project and provides interview-style
Q&A. It is aimed at a fresher/SDE preparing to defend this project.

## 1. Architecture & layering

The app follows a **layered architecture** so each concern is isolated and
independently testable:

```
HTTP request
   │
   ▼
routers/ ......... HTTP concerns: paths, status codes, query params
   │
   ▼
deps.py .......... cross-cutting dependencies (DB session, current user)
   │
   ▼
models.py ........ persistence (SQLAlchemy ORM tables)
schemas.py ....... validation & serialization (Pydantic)
   │
   ▼
database.py ...... engine + session lifecycle
config.py ........ environment configuration
```

**Why separate `models` (ORM) from `schemas` (Pydantic)?**
The ORM model is the *database shape*; the Pydantic schema is the *API
contract*. Keeping them separate means we never accidentally serialize an
internal column (like `hashed_password`), we can evolve the DB and the API
independently, and we get automatic request validation + OpenAPI docs.

## 2. Data model

- `User`: `id`, `email` (unique), `hashed_password`, `created_at`.
- `Task`: `id`, `title`, `description`, `status` (enum), timestamps,
  `owner_id` (FK to `users.id`).
- One-to-many: a user has many tasks (`cascade="all, delete-orphan"` so
  deleting a user removes their tasks).

## 3. Authentication & authorization

- **Register**: email + password; password is bcrypt-hashed before storage.
- **Login**: verifies the password and returns a signed **JWT** whose `sub`
  claim is the user id plus an `exp` expiry.
- **Protected routes**: the `get_current_user` dependency extracts the bearer
  token, decodes it, and loads the user — raising `401` on any failure.
- **Authorization**: every task query is filtered by `owner_id`, so users can
  only read/modify their own data.

## 4. HTTP status codes

Correct status codes are part of a good REST API: `201` for creation, `204`
for deletes with no body, `401` for auth failures, `404` for missing/unowned
resources, `409` for conflicts (duplicate email), `422` for validation errors
(FastAPI's default for schema violations).

## 5. Pagination & filtering

`GET /tasks` supports `limit`/`offset` pagination and returns
`{items, total, limit, offset}` so clients can render page controls. It also
supports filtering by `status` and a case-insensitive `q` title search using
SQL `ILIKE`. Bounds (`limit` 1–100, `offset` ≥ 0) are enforced by FastAPI's
`Query` validators.

## 6. Testing

Tests use FastAPI's `TestClient` (built on httpx) against an **in-memory
SQLite** database. The `get_db` dependency is overridden to point at the test
session, and the schema is recreated per test for isolation. Coverage:
auth flow, CRUD happy paths, validation (`422`), not-found (`404`), and
cross-user isolation.

---

## Interview Q&A (15–20)

**Q1. What is FastAPI and why use it?**
An async Python web framework built on Starlette + Pydantic. It gives you
type-driven request validation, dependency injection, and automatic OpenAPI/
Swagger docs, with performance comparable to Node/Go frameworks.

**Q2. What is ASGI and how does it differ from WSGI?**
ASGI is the asynchronous successor to WSGI. It supports `async`/`await`,
long-lived connections (WebSockets), and concurrency without threads. FastAPI
is ASGI; Flask (classic) is WSGI.

**Q3. Why Pydantic schemas instead of returning ORM objects directly?**
Pydantic validates and serializes data, enforces the API contract, and hides
internal fields. `from_attributes=True` (formerly `orm_mode`) lets a schema
read directly from an ORM object.

**Q4. How does dependency injection work here?**
FastAPI resolves function parameters declared with `Depends(...)`. We use it
for the DB session (`get_db`) and the authenticated user (`get_current_user`).
Dependencies are cached per-request and are trivial to override in tests.

**Q5. How is the database session managed?**
`get_db` is a generator dependency that yields a `Session` and closes it in a
`finally` block, guaranteeing cleanup even if the handler raises.

**Q6. How does JWT authentication work?**
On login we sign a token containing the user id and an expiry using a secret
key (HS256). On each protected request the client sends `Authorization:
Bearer <token>`; we verify the signature and expiry and load the user. Tokens
are stateless — no server-side session store required.

**Q7. Why hash passwords, and why bcrypt?**
So a database leak doesn't expose credentials. bcrypt is a slow, salted
adaptive hash designed to resist brute-force and rainbow-table attacks.

**Q8. Difference between authentication and authorization?**
Authentication proves *who you are* (valid token). Authorization decides *what
you may do* (here: you may only access tasks where `owner_id == your id`).

**Q9. Why return 404 instead of 403 for another user's task?**
Returning `403` would confirm the resource exists. `404` avoids leaking the
existence of resources the caller isn't allowed to see.

**Q10. When do you use 201 vs 200 vs 204?**
`201` when a new resource is created (and typically return it). `200` for a
successful read/update returning a body. `204` for success with no body (a
delete).

**Q11. What triggers a 422 in FastAPI?**
Request validation failures — a missing required field, wrong type, or a value
violating a constraint (e.g. `password` shorter than 8 chars). FastAPI returns
a structured error automatically.

**Q12. Why PATCH instead of PUT for updates?**
`PATCH` is a partial update — clients send only the fields they want to change.
We use Pydantic's `exclude_unset=True` so unspecified fields are untouched.
`PUT` implies replacing the whole resource.

**Q13. How is pagination implemented and why return `total`?**
Via SQL `LIMIT`/`OFFSET`. Returning `total` lets the client compute the number
of pages and render "showing X of N" UIs. (For very large datasets,
keyset/cursor pagination scales better than offset.)

**Q14. How does SQLAlchemy 2.0 differ from 1.x here?**
We use the typed `Mapped[...]` / `mapped_column(...)` declarative style and the
`select()` + `session.execute()` query API, which is fully typed and the
recommended modern pattern.

**Q15. Why keep configuration in `config.py` with env vars?**
The twelve-factor principle: config lives in the environment, not the code.
Secrets (JWT key) and per-environment values (DB URL) can change without code
edits, and nothing sensitive is committed.

**Q16. How would you switch from SQLite to Postgres?**
Change `DATABASE_URL` (e.g. `postgresql+psycopg://...`). The SQLite-only
`check_same_thread` arg is applied conditionally, so no code changes are
needed. For schema evolution you'd add Alembic migrations.

**Q17. How are the tests isolated from real data?**
They run against an in-memory SQLite DB with `StaticPool`, override the
`get_db` dependency, and recreate/drop the schema around each test — so tests
never touch `tasks.db` and don't interfere with each other.

**Q18. What is `lifespan` in `main.py`?**
FastAPI's startup/shutdown hook. We use it to create tables on startup. It
replaces the older `@app.on_event("startup")` handlers.

**Q19. How would you add rate limiting or CORS?**
CORS via `CORSMiddleware`; rate limiting via middleware (e.g. slowapi) or an
upstream gateway/reverse proxy. Both are cross-cutting concerns added at the
app/middleware layer.

**Q20. What would you improve for production?**
Alembic migrations, refresh tokens + token revocation, structured logging,
request IDs, CORS config, rate limiting, health/readiness split, CI running
`pytest` + linting, and running under Gunicorn/Uvicorn workers behind a proxy.
```
