# Task Manager REST API

A production-style REST API for managing tasks, built with **FastAPI**,
**SQLAlchemy 2.0**, **Pydantic v2** and **JWT authentication**. Users register,
log in, and perform full CRUD on their own tasks with pagination, filtering and
search. Every task is scoped to its owner.

## Features

- JWT bearer authentication (register / login, bcrypt-hashed passwords)
- Full CRUD for tasks with proper HTTP status codes
- Pagination (`limit` / `offset`) with total-count metadata
- Filtering by `status` and case-insensitive title search (`q`)
- Per-user data isolation (you can only touch your own tasks)
- Layered architecture (routers -> deps -> models/schemas -> database)
- Env-based configuration via `pydantic-settings`
- Auto-generated OpenAPI docs at `/docs`
- Pytest suite using FastAPI `TestClient` against an in-memory SQLite DB
- Dockerfile (slim base, non-root user)

## Tech stack

| Concern        | Choice                          |
|----------------|---------------------------------|
| Web framework  | FastAPI (ASGI)                  |
| Server         | Uvicorn                         |
| ORM            | SQLAlchemy 2.0 (typed mappings) |
| Validation     | Pydantic v2                     |
| Auth           | PyJWT + passlib/bcrypt          |
| Database       | SQLite (swap `DATABASE_URL`)    |
| Tests          | pytest + httpx TestClient       |

## Project layout

```
rest_api_service/
├── app/
│   ├── main.py          # FastAPI app, lifespan, router wiring, /health
│   ├── config.py        # env-based settings (pydantic-settings)
│   ├── database.py      # engine, session factory, get_db dependency
│   ├── models.py        # SQLAlchemy models (User, Task)
│   ├── schemas.py       # Pydantic request/response schemas
│   ├── auth.py          # password hashing + JWT create/decode
│   ├── deps.py          # get_current_user + shared dependencies
│   └── routers/
│       ├── auth.py      # /auth/register, /auth/login
│       └── tasks.py     # /tasks CRUD + pagination/filter
├── tests/               # pytest suite (auth + tasks)
├── requirements.txt
├── Dockerfile
├── .env.example
├── README.md
└── STUDY_GUIDE.md
```

## Quickstart (local)

```bash
# 1. Create + activate a virtualenv
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment (optional; sensible defaults exist)
cp .env.example .env

# 4. Run the API (auto-creates tasks.db on startup)
uvicorn app.main:app --reload

# 5. Open the interactive docs
#    http://127.0.0.1:8000/docs
```

## Run with Docker

```bash
docker build -t task-api .
docker run -p 8000:8000 task-api
# docs at http://127.0.0.1:8000/docs
```

## Run the tests

```bash
pip install -r requirements.txt
pytest
```

## API endpoints

| Method | Path              | Auth | Description                              |
|--------|-------------------|------|------------------------------------------|
| GET    | `/`               | No   | API metadata                             |
| GET    | `/health`         | No   | Liveness probe                           |
| POST   | `/auth/register`  | No   | Create an account (201)                  |
| POST   | `/auth/login`     | No   | Get a JWT bearer token                   |
| POST   | `/tasks`          | Yes  | Create a task (201)                      |
| GET    | `/tasks`          | Yes  | List tasks (pagination + filter + search)|
| GET    | `/tasks/{id}`     | Yes  | Get one task (404 if missing/not owned)  |
| PATCH  | `/tasks/{id}`     | Yes  | Partial update                           |
| DELETE | `/tasks/{id}`     | Yes  | Delete a task (204)                      |

### Query parameters for `GET /tasks`

| Param    | Type    | Default | Notes                                  |
|----------|---------|---------|----------------------------------------|
| `status` | enum    | –       | `todo` \| `in_progress` \| `done`      |
| `q`      | string  | –       | Case-insensitive title substring match |
| `limit`  | int     | 20      | 1–100                                   |
| `offset` | int     | 0       | ≥ 0                                     |

## curl examples

```bash
BASE=http://127.0.0.1:8000

# Register
curl -s -X POST $BASE/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"me@example.com","password":"supersecret123"}'

# Login -> capture token (login uses form-encoded OAuth2 fields)
TOKEN=$(curl -s -X POST $BASE/auth/login \
  -d "username=me@example.com&password=supersecret123" \
  | python -c "import sys,json;print(json.load(sys.stdin)['access_token'])")

# Create a task
curl -s -X POST $BASE/tasks \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title":"Buy groceries","description":"milk, eggs","status":"todo"}'

# List tasks (page of 10, only done, matching "gro")
curl -s -H "Authorization: Bearer $TOKEN" \
  "$BASE/tasks?limit=10&offset=0&status=todo&q=gro"

# Update a task
curl -s -X PATCH $BASE/tasks/1 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"status":"done"}'

# Delete a task
curl -s -X DELETE $BASE/tasks/1 -H "Authorization: Bearer $TOKEN"
```

## HTTP status codes used

| Code | When                                                        |
|------|-------------------------------------------------------------|
| 200  | Successful GET / PATCH                                       |
| 201  | Resource created (register, create task)                    |
| 204  | Successful delete (no body)                                 |
| 401  | Missing/invalid token, or bad login credentials             |
| 404  | Task not found or not owned by the caller                   |
| 409  | Email already registered                                    |
| 422  | Request body/query failed validation                        |

## Security notes

- Passwords are never stored in plaintext (bcrypt via passlib).
- `SECRET_KEY` **must** be overridden in production (see `.env.example`).
- Cross-user access returns `404` (not `403`) to avoid leaking existence.

See `STUDY_GUIDE.md` for the design rationale and interview Q&A.
