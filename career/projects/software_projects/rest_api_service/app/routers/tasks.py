"""Task CRUD routes with pagination and filtering.

All routes are scoped to the authenticated user: a user can only see and
mutate their own tasks. Ownership is enforced in every query.
"""

from typing import Annotated

from fastapi import APIRouter, HTTPException, Query, status
from sqlalchemy import select

from app.deps import CurrentUser, DbSession
from app.models import Task, TaskStatus
from app.schemas import PaginatedTasks, TaskCreate, TaskRead, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["tasks"])


def _get_owned_task(task_id: int, user_id: int, db) -> Task:
    """Fetch a task by id ensuring it belongs to the user, else raise 404."""
    task = db.get(Task, task_id)
    if task is None or task.owner_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    return task


@router.post(
    "",
    response_model=TaskRead,
    status_code=status.HTTP_201_CREATED,
    summary="Create a task",
)
def create_task(
    payload: TaskCreate, current_user: CurrentUser, db: DbSession
) -> Task:
    """Create a new task owned by the authenticated user."""
    task = Task(**payload.model_dump(), owner_id=current_user.id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@router.get("", response_model=PaginatedTasks, summary="List tasks")
def list_tasks(
    current_user: CurrentUser,
    db: DbSession,
    status_filter: Annotated[
        TaskStatus | None,
        Query(alias="status", description="Filter by task status"),
    ] = None,
    q: Annotated[
        str | None, Query(description="Case-insensitive title search")
    ] = None,
    limit: Annotated[int, Query(ge=1, le=100)] = 20,
    offset: Annotated[int, Query(ge=0)] = 0,
) -> PaginatedTasks:
    """Return a paginated, optionally filtered list of the user's tasks."""
    base = select(Task).where(Task.owner_id == current_user.id)

    if status_filter is not None:
        base = base.where(Task.status == status_filter)
    if q:
        base = base.where(Task.title.ilike(f"%{q}%"))

    total = len(db.execute(base).scalars().all())

    page = base.order_by(Task.created_at.desc()).limit(limit).offset(offset)
    items = db.execute(page).scalars().all()

    return PaginatedTasks(
        items=list(items), total=total, limit=limit, offset=offset
    )


@router.get("/{task_id}", response_model=TaskRead, summary="Get a task")
def get_task(
    task_id: int, current_user: CurrentUser, db: DbSession
) -> Task:
    """Return a single task owned by the user, or 404."""
    return _get_owned_task(task_id, current_user.id, db)


@router.patch(
    "/{task_id}", response_model=TaskRead, summary="Update a task"
)
def update_task(
    task_id: int,
    payload: TaskUpdate,
    current_user: CurrentUser,
    db: DbSession,
) -> Task:
    """Partially update a task. Only provided fields are changed."""
    task = _get_owned_task(task_id, current_user.id, db)

    updates = payload.model_dump(exclude_unset=True)
    for field, value in updates.items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)
    return task


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a task",
)
def delete_task(
    task_id: int, current_user: CurrentUser, db: DbSession
) -> None:
    """Delete a task owned by the user. Returns 204 on success, 404 if absent."""
    task = _get_owned_task(task_id, current_user.id, db)
    db.delete(task)
    db.commit()
