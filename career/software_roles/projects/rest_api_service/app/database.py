"""Database engine, session factory and declarative base.

SQLite is used for zero-config local development. The `check_same_thread`
flag is required only for SQLite because FastAPI serves requests from a
thread pool. Swapping `DATABASE_URL` to Postgres needs no code changes.
"""

from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.config import settings

connect_args = (
    {"check_same_thread": False}
    if settings.database_url.startswith("sqlite")
    else {}
)

engine = create_engine(settings.database_url, connect_args=connect_args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    """Declarative base class for all ORM models."""


def get_db() -> Generator[Session, None, None]:
    """FastAPI dependency that yields a DB session and always closes it."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    """Create all tables. Import models so they register with the metadata."""
    from app import models  # noqa: F401  (side-effect import)

    Base.metadata.create_all(bind=engine)
