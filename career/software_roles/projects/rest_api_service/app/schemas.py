"""Pydantic schemas — the API's request/response contract.

Schemas are intentionally separate from ORM models: they define what data
enters and leaves the API, enable validation, and prevent leaking internal
fields (e.g. `hashed_password`) to clients.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.models import TaskStatus

# --------------------------------------------------------------------------- #
# Auth / User schemas
# --------------------------------------------------------------------------- #


class UserCreate(BaseModel):
    """Payload for registering a new account."""

    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class UserRead(BaseModel):
    """Public representation of a user (never includes the password)."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    created_at: datetime


class Token(BaseModel):
    """OAuth2-style bearer token response."""

    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    """Decoded JWT claims we care about."""

    user_id: int | None = None


# --------------------------------------------------------------------------- #
# Task schemas
# --------------------------------------------------------------------------- #


class TaskBase(BaseModel):
    """Fields shared by create/update payloads."""

    title: str = Field(min_length=1, max_length=200)
    description: str | None = Field(default=None, max_length=5000)
    status: TaskStatus = TaskStatus.todo


class TaskCreate(TaskBase):
    """Payload for creating a task."""


class TaskUpdate(BaseModel):
    """Payload for partial updates (all fields optional)."""

    title: str | None = Field(default=None, min_length=1, max_length=200)
    description: str | None = Field(default=None, max_length=5000)
    status: TaskStatus | None = None


class TaskRead(TaskBase):
    """Full task representation returned to clients."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime


class PaginatedTasks(BaseModel):
    """A page of tasks plus pagination metadata."""

    items: list[TaskRead]
    total: int
    limit: int
    offset: int
