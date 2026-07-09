"""CRUD helper functions — isolate DB logic from the HTTP layer."""
from typing import List, Optional

from sqlalchemy.orm import Session

from . import models, schemas


def get_tasks(db: Session, skip: int = 0, limit: int = 100) -> List[models.Task]:
    return (
        db.query(models.Task)
        .order_by(models.Task.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_task(db: Session, task_id: int) -> Optional[models.Task]:
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def create_task(db: Session, task: schemas.TaskCreate) -> models.Task:
    db_task = models.Task(
        title=task.title,
        description=task.description or "",
        priority=task.priority.value,
        completed=task.completed,
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task(
    db: Session, db_task: models.Task, updates: schemas.TaskUpdate
) -> models.Task:
    data = updates.model_dump(exclude_unset=True)
    if "priority" in data and data["priority"] is not None:
        data["priority"] = data["priority"].value
    for field, value in data.items():
        setattr(db_task, field, value)
    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, db_task: models.Task) -> None:
    db.delete(db_task)
    db.commit()
