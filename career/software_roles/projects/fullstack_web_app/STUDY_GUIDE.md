# Study Guide — Full-Stack Task Tracker

A companion to the project explaining the concepts behind it, plus 20 interview-style
Q&A. Use it to walk an interviewer through *why* the app is built the way it is.

---

## 1. Client–server split

A full-stack app is divided into two independently deployable halves:

- **Client (frontend):** the React SPA that runs in the browser. It renders UI and holds
  UI state, but it has **no direct access to the database**. It knows only how to make
  HTTP requests.
- **Server (backend):** the FastAPI service. It owns business logic, validation, and the
  database. It exposes a JSON API over HTTP.

They communicate purely through the REST API contract. This decoupling means you can swap
the React frontend for a mobile app, or move SQLite to Postgres, without either side
caring — as long as the API contract holds.

## 2. REST

REST models the app's data as **resources** addressed by URLs, manipulated with standard
HTTP verbs:

| Verb   | Meaning              | Here                    |
|--------|----------------------|-------------------------|
| GET    | Read                 | `GET /api/tasks`        |
| POST   | Create               | `POST /api/tasks`       |
| PUT    | Update/replace       | `PUT /api/tasks/{id}`   |
| DELETE | Remove               | `DELETE /api/tasks/{id}`|

Responses use meaningful HTTP status codes: `200` OK, `201` Created, `204` No Content,
`404` Not Found, `422` Unprocessable Entity (validation).

## 3. State management (frontend)

React state lives in `App.jsx` using hooks:

- `useState` holds the `tasks` array, `loading`, `error`, and the active `filter`.
- `useEffect` loads tasks once on mount (empty dependency array).
- `useMemo` derives the filtered view without recomputing on every render.

State flows **down** via props (`App → TaskForm`, `App → TaskItem`); events flow **up**
via callbacks (`onCreate`, `onToggle`, `onDelete`). After each successful API call, we
update local state so the UI reflects the change immediately.

## 4. CORS

Browsers enforce the **same-origin policy**: JavaScript on `localhost:5173` cannot call
`localhost:8000` unless the server opts in. FastAPI's `CORSMiddleware` adds the
`Access-Control-Allow-Origin` headers that tell the browser the request is allowed. We
list the frontend origins explicitly rather than using `*` so it stays production-realistic.

## 5. Validation

Pydantic schemas (`schemas.py`) validate every incoming request body: `title` must be
1–200 chars, `priority` must be one of an enum. Bad data is rejected with `422` before it
ever reaches the database — validation lives at the edge of the server.

## 6. Build & deploy

- **Frontend build:** `npm run build` runs Vite, which bundles/minifies the React app into
  static `dist/` assets (HTML/CSS/JS). Those can be served by any static host or CDN.
- **Backend:** runs under Uvicorn (an ASGI server).
- **Docker:** each service has a `Dockerfile`; the frontend uses a **multi-stage build**
  (Node to build, nginx to serve). `docker-compose.yml` builds and runs both together with
  one command.

---

## Interview Q&A (20)

**1. What does "full-stack" mean in this project?**
It spans the browser UI (React), the API server (FastAPI), and the database (SQLite via
SQLAlchemy) — plus the Docker packaging that ties them together.

**2. Why FastAPI over Flask/Django?**
FastAPI gives async support, automatic request validation via Pydantic, and auto-generated
OpenAPI/Swagger docs out of the box, with very little boilerplate.

**3. What is an ORM and why use SQLAlchemy?**
An Object-Relational Mapper maps Python classes to database tables, so you write Python
instead of raw SQL. It prevents SQL injection through parameterization and makes swapping
databases easier.

**4. Difference between a SQLAlchemy model and a Pydantic schema?**
The SQLAlchemy `Task` model defines the database table. The Pydantic schemas define the
shape of API requests/responses and validate them. Keeping them separate decouples storage
from the API contract.

**5. Walk through what happens when a user adds a task.**
`TaskForm` calls `onCreate` → `api.createTask` sends `POST /api/tasks` → FastAPI validates
with `TaskCreate` → `crud.create_task` inserts via SQLAlchemy and commits → returns the new
row serialized as `TaskOut` (201) → React prepends it to state → UI re-renders.

**6. What is CORS and how did you handle it?**
Cross-Origin Resource Sharing. Because the frontend and backend run on different origins,
the browser blocks the call unless the server sends allow headers. I added FastAPI's
`CORSMiddleware` with the frontend origins whitelisted.

**7. Why not use `allow_origins=["*"]`?**
A wildcard allows any site to call the API and can't be combined with credentials safely.
Listing explicit origins is closer to production practice.

**8. How does the frontend know the backend URL?**
Via the Vite env variable `VITE_API_URL` in `.env`. Vite inlines `VITE_*` variables at
build time; `api.js` reads `import.meta.env.VITE_API_URL`.

**9. What are the HTTP status codes you return and why?**
`200` reads, `201` create, `204` delete (no body), `404` missing resource, `422`
validation failure. They let clients react programmatically without parsing messages.

**10. What is the difference between PUT and PATCH? Which did you use?**
PUT replaces a resource; PATCH partially updates. I used PUT but made it behave like a
partial update via `exclude_unset` so only provided fields change — a common pragmatic choice.

**11. How is validation done and where?**
At the server edge with Pydantic. Constraints like `min_length`, `max_length`, and the
`Priority` enum reject invalid input with `422` before any DB access.

**12. Why an in-memory database for tests?**
Speed and isolation — each test gets a clean schema and no files are written. I override
the `get_db` dependency to point at an in-memory SQLite engine.

**13. What is dependency injection here?**
FastAPI's `Depends(get_db)` injects a database session into each route and guarantees it's
closed afterward. In tests I override that dependency to inject the test session.

**14. Explain the React hooks you used.**
`useState` for local component state, `useEffect` for the initial data fetch (side effect),
and `useMemo` to derive the filtered task list efficiently.

**15. How does data flow between components?**
Unidirectional: state lives in `App`, passed down as props; child components signal changes
up through callback props. This "lifting state up" keeps a single source of truth.

**16. How do you handle errors from the API?**
`api.js` throws on non-2xx responses with the server's `detail` message; components catch
it and show an error banner or inline message, so failures are visible, not silent.

**17. What does `npm run build` produce and how is it deployed?**
Vite outputs minified static assets to `dist/`. In Docker, a multi-stage build compiles
them, then nginx serves the static files — no Node runtime in the final image.

**18. How does docker-compose wire the two services?**
It builds both images, maps ports (backend 8000, frontend 3000), passes the API URL as a
build arg to the frontend, and sets `depends_on` so the backend starts first.

**19. How would you add user authentication?**
Add a users table, hash passwords (e.g. bcrypt), issue JWTs on login, protect routes with a
FastAPI dependency that validates the token, and scope tasks to the authenticated user.

**20. How would you scale this from SQLite to production?**
Swap SQLite for Postgres via `DATABASE_URL`, add Alembic migrations, put the API behind
multiple Uvicorn/Gunicorn workers, serve the frontend from a CDN, and add indexes,
pagination, and caching as data grows.
