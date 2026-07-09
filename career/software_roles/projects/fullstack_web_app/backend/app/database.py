"""Database configuration: SQLAlchemy engine, session factory, and Base."""
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite file lives next to the app package by default. Override with DATABASE_URL.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./tasks.db")

# check_same_thread is required only for SQLite when used across threads (uvicorn).
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """FastAPI dependency that yields a scoped DB session and always closes it."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
