"""SQLAlchemy ORM models."""
from datetime import datetime, timezone

from sqlalchemy import Boolean, Column, DateTime, Integer, String

from .database import Base


def _utcnow() -> datetime:
    """Timezone-aware UTC now (replaces deprecated datetime.utcnow)."""
    return datetime.now(timezone.utc)


class Task(Base):
    """A single task/to-do item — the main resource of the API."""

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False, index=True)
    description = Column(String(1000), nullable=True, default="")
    priority = Column(String(10), nullable=False, default="medium")  # low | medium | high
    completed = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, nullable=False, default=_utcnow)
    updated_at = Column(
        DateTime, nullable=False, default=_utcnow, onupdate=_utcnow
    )
