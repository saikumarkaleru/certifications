"""FastAPI application entrypoint.

Wires together configuration, database initialisation, routers and a couple
of convenience endpoints (`/` and `/health`).
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import settings
from app.database import init_db
from app.routers import auth, tasks


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Create database tables on startup."""
    init_db()
    yield


app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    description=(
        "A production-style Task Manager REST API built with FastAPI, "
        "SQLAlchemy and JWT authentication."
    ),
    lifespan=lifespan,
)

app.include_router(auth.router)
app.include_router(tasks.router)


@app.get("/", tags=["meta"], summary="API root")
def root() -> dict[str, str]:
    """Return basic API metadata."""
    return {
        "name": settings.app_name,
        "version": "1.0.0",
        "docs": "/docs",
    }


@app.get("/health", tags=["meta"], summary="Health check")
def health() -> dict[str, str]:
    """Liveness probe used by containers / load balancers."""
    return {"status": "ok"}
