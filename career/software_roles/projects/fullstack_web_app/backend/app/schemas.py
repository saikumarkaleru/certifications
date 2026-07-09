"""Pydantic schemas for request validation and response serialization."""
from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="Short task title")
    description: Optional[str] = Field("", max_length=1000)
    priority: Priority = Priority.medium
    completed: bool = False


class TaskCreate(TaskBase):
    """Payload for creating a task."""


class TaskUpdate(BaseModel):
    """Payload for partial updates — every field is optional."""

    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    priority: Optional[Priority] = None
    completed: Optional[bool] = None


class TaskOut(TaskBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
